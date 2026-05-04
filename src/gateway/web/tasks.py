"""In-memory task store for long-running web ops.

Records persist for the lifetime of the `wiki serve` process. Restart
loses in-flight task history; `log.md` is the durable activity record.
"""

from __future__ import annotations

import asyncio
import threading
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable


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

    def __init__(self) -> None:
        self._records: dict[str, TaskRecord] = {}
        self._lock = threading.Lock()

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
