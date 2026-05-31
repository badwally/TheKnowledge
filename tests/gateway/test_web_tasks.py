"""Tests for the M40 in-memory task store."""

from __future__ import annotations

import asyncio
import threading

import pytest

from gateway.web.tasks import CapacityError, TaskStore


@pytest.fixture
def store():
    return TaskStore()


# --- bounded concurrency (260530 review, finding #2) ----------------------


def test_run_in_thread_rejects_when_at_capacity():
    """At max_concurrent in-flight tasks, the next submission raises
    CapacityError rather than spawning an unbounded daemon thread."""
    store = TaskStore(max_concurrent=2)
    release = threading.Event()
    started = threading.Semaphore(0)

    def blocker() -> dict:
        started.release()
        release.wait(timeout=5)
        return {"ok": True}

    ids = [store.create("ingest") for _ in range(2)]
    for rec in ids:
        store.run_in_thread(rec.task_id, blocker)

    # Both workers have entered (acquired their slots).
    assert started.acquire(timeout=5)
    assert started.acquire(timeout=5)

    third = store.create("ingest")
    with pytest.raises(CapacityError):
        store.run_in_thread(third.task_id, blocker)
    # The rejected task is recorded as failed, not left dangling "queued".
    assert store.get(third.task_id).status == "failed"

    release.set()


def test_capacity_frees_after_completion():
    """A slot is released when a task finishes, so new work is admitted."""
    store = TaskStore(max_concurrent=1)
    release = threading.Event()
    started = threading.Semaphore(0)

    def blocker() -> dict:
        started.release()
        release.wait(timeout=5)
        return {"ok": True}

    first = store.create("ingest")
    store.run_in_thread(first.task_id, blocker)
    assert started.acquire(timeout=5)

    # Capacity is full.
    busy = store.create("ingest")
    with pytest.raises(CapacityError):
        store.run_in_thread(busy.task_id, blocker)

    # Let the first finish; its slot frees.
    release.set()
    for _ in range(50):
        if store.get(first.task_id).status == "done":
            break
        threading.Event().wait(0.05)
    assert store.get(first.task_id).status == "done"

    # A new task is now admitted (and completes immediately).
    nxt = store.create("ingest")
    store.run_in_thread(nxt.task_id, lambda: {"ok": True})
    for _ in range(50):
        if store.get(nxt.task_id).status == "done":
            break
        threading.Event().wait(0.05)
    assert store.get(nxt.task_id).status == "done"


def test_create_task_returns_record(store):
    record = store.create("ingest")
    assert record.task_id
    assert record.op_name == "ingest"
    assert record.status == "queued"
    assert record.started_at is None
    assert record.finished_at is None
    assert record.result is None
    assert record.error is None


def test_get_task_returns_record(store):
    created = store.create("query")
    fetched = store.get(created.task_id)
    assert fetched is not None
    assert fetched.task_id == created.task_id


def test_get_unknown_task_returns_none(store):
    assert store.get("nonexistent") is None


def test_mark_running_updates_status_and_started_at(store):
    record = store.create("ingest")
    store.mark_running(record.task_id)
    fetched = store.get(record.task_id)
    assert fetched.status == "running"
    assert fetched.started_at is not None


def test_mark_done_records_result_and_finished_at(store):
    record = store.create("ingest")
    store.mark_running(record.task_id)
    store.mark_done(record.task_id, result={"summary": "ok"})
    fetched = store.get(record.task_id)
    assert fetched.status == "done"
    assert fetched.finished_at is not None
    assert fetched.result == {"summary": "ok"}


def test_mark_failed_records_error(store):
    record = store.create("ingest")
    store.mark_running(record.task_id)
    store.mark_failed(record.task_id, error="boom")
    fetched = store.get(record.task_id)
    assert fetched.status == "failed"
    assert fetched.error == "boom"
    assert fetched.finished_at is not None


def test_run_async_executes_callable_and_records_result(store):
    async def runner():
        record = store.create("ingest")
        await store.run_async(record.task_id, lambda: {"summary": "ran"})
        return record.task_id

    task_id = asyncio.run(runner())
    fetched = store.get(task_id)
    assert fetched.status == "done"
    assert fetched.result == {"summary": "ran"}


def test_run_async_captures_exception(store, kb_root):
    def boom():
        raise ValueError("bad input")

    async def runner():
        record = store.create("ingest")
        await store.run_async(record.task_id, boom)
        return record.task_id

    task_id = asyncio.run(runner())
    fetched = store.get(task_id)
    assert fetched.status == "failed"
    # Consumer-facing error is sanitized — raw exception text is NOT exposed
    # (260530 review finding #5); the task_id is the correlation handle.
    assert "bad input" not in fetched.error
    assert task_id in fetched.error


def test_failure_detail_logged_but_not_returned(store, kb_root):
    """Raw exception detail (e.g. LLM subprocess stderr) goes to log.md
    operator-only; the consumer-facing error field is sanitized (finding #5)."""
    from gateway import paths

    secret = "/Users/x/.secret/creds last stderr: INTERNAL-DIAGNOSTIC"

    def boom():
        raise RuntimeError(f"`claude -p` failed; {secret}")

    record = store.create("query")
    store.run_in_thread(record.task_id, boom)
    for _ in range(50):
        if store.get(record.task_id).status == "failed":
            break
        threading.Event().wait(0.05)

    fetched = store.get(record.task_id)
    assert fetched.status == "failed"
    # The leak: raw stderr must NOT be in the response error field.
    assert secret not in fetched.error
    assert record.task_id in fetched.error
    # But the full detail IS recoverable by the operator in log.md.
    log_text = paths.log_path().read_text()
    assert secret in log_text
    assert record.task_id in log_text
