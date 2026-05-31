"""In-memory task store for long-running web ops.

Records persist for the lifetime of the `wiki serve` process. Restart
loses in-flight task history; `log.md` is the durable activity record.
"""

from __future__ import annotations

import asyncio
import os
import threading
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable


# Default ceiling on concurrently-running web tasks. Each task is a paid
# LLM/NotebookLM job on a daemon thread; without a cap a flood of requests
# spawns unbounded threads and unbounded concurrent spend (260530 review,
# finding #2). Override via WIKI_MAX_CONCURRENT_TASKS.
_DEFAULT_MAX_CONCURRENT = 4


def _default_max_concurrent() -> int:
    raw = os.environ.get("WIKI_MAX_CONCURRENT_TASKS")
    if raw is None:
        return _DEFAULT_MAX_CONCURRENT
    try:
        value = int(raw)
    except ValueError:
        return _DEFAULT_MAX_CONCURRENT
    return value if value > 0 else _DEFAULT_MAX_CONCURRENT


class CapacityError(RuntimeError):
    """Raised when the task store is at its concurrent-task ceiling.

    Routes let this propagate; the app maps it to HTTP 503 so the caller can
    back off and retry rather than the server silently overcommitting.
    """


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class TaskRecord:
    task_id: str
    op_name: str
    status: str = "queued"  # queued | running | done | failed
    started_at: str | None = None
    finished_at: str | None = None
    result: dict[str, Any] | None = None
    error: str | None = None


class TaskStore:
    """Process-local task registry. Thread-safe via a single lock."""

    def __init__(self, max_concurrent: int | None = None) -> None:
        self._records: dict[str, TaskRecord] = {}
        self._lock = threading.Lock()
        self.max_concurrent = (
            max_concurrent if max_concurrent is not None else _default_max_concurrent()
        )
        # Admission control for run_in_thread: non-blocking acquire, so excess
        # work is rejected (503) rather than queued — an attacker's flood does
        # not accumulate threads or memory.
        self._slots = threading.BoundedSemaphore(self.max_concurrent)

    def create(self, op_name: str) -> TaskRecord:
        record = TaskRecord(task_id=str(uuid.uuid4()), op_name=op_name)
        with self._lock:
            self._records[record.task_id] = record
        return record

    def get(self, task_id: str) -> TaskRecord | None:
        with self._lock:
            return self._records.get(task_id)

    def mark_running(self, task_id: str) -> None:
        with self._lock:
            record = self._records.get(task_id)
            if record is not None:
                record.status = "running"
                record.started_at = _now_iso()

    def mark_done(self, task_id: str, *, result: dict[str, Any]) -> None:
        with self._lock:
            record = self._records.get(task_id)
            if record is not None:
                record.status = "done"
                record.result = result
                record.finished_at = _now_iso()

    def mark_failed(self, task_id: str, *, error: str) -> None:
        with self._lock:
            record = self._records.get(task_id)
            if record is not None:
                record.status = "failed"
                record.error = error
                record.finished_at = _now_iso()

    async def run_async(self, task_id: str, fn: Callable[[], Any]) -> None:
        """Run `fn` in a worker thread, updating the task record on completion."""
        self.mark_running(task_id)
        try:
            result = await asyncio.to_thread(fn)
            payload = result if isinstance(result, dict) else {"value": result}
            self.mark_done(task_id, result=payload)
        except Exception as e:  # noqa: BLE001 — capture all
            self.mark_failed(task_id, error=f"{type(e).__name__}: {e}")

    def run_in_thread(self, task_id: str, fn: Callable[[], Any]) -> None:
        """Spawn a daemon thread to run `fn`, updating the task record on completion.

        Unlike `run_async`, this works in both async and sync contexts (including
        the synchronous TestClient used in tests).

        Admission is bounded by `max_concurrent`: if all slots are in use the
        task is marked failed and `CapacityError` is raised (the route maps it
        to HTTP 503). The slot is released when the worker finishes.
        """
        if not self._slots.acquire(blocking=False):
            self.mark_failed(task_id, error="server at capacity; retry later")
            raise CapacityError(
                f"task store at capacity ({self.max_concurrent} concurrent tasks)"
            )

        def _worker() -> None:
            self.mark_running(task_id)
            try:
                result = fn()
                payload = result if isinstance(result, dict) else {"value": result}
                self.mark_done(task_id, result=payload)
            except Exception as e:  # noqa: BLE001 — capture all
                self.mark_failed(task_id, error=f"{type(e).__name__}: {e}")
            finally:
                self._slots.release()

        t = threading.Thread(target=_worker, daemon=True)
        t.start()
