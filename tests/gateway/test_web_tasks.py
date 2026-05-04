"""Tests for the M40 in-memory task store."""

from __future__ import annotations

import asyncio

import pytest

from gateway.web.tasks import TaskStore


@pytest.fixture
def store():
    return TaskStore()


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


def test_run_async_captures_exception(store):
    def boom():
        raise ValueError("bad input")

    async def runner():
        record = store.create("ingest")
        await store.run_async(record.task_id, boom)
        return record.task_id

    task_id = asyncio.run(runner())
    fetched = store.get(task_id)
    assert fetched.status == "failed"
    assert "bad input" in fetched.error
