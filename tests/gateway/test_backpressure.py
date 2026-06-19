from __future__ import annotations

import pytest

from gateway import paths
from gateway.intent_queue import IntentQueue
from gateway.ops import deposit as deposit_mod


@pytest.fixture
def queue(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "knowledge_root", lambda: tmp_path)
    return IntentQueue()


def _payload():
    return {"page_type": "entity", "title": "T", "body": "some body"}


def test_deposit_queues_when_below_backlog(queue):
    """Negative control: with the queue empty, deposit returns queued (+ retry_after)."""
    r = deposit_mod.deposit(_payload(), {"identity": "agent-a"}, queue=queue)
    assert r.disposition == "queued"
    assert r.retry_after is not None
    assert r.intent_id


def test_deposit_sheds_load_when_backlog_exceeded(queue, monkeypatch):
    """Under load (submitted backlog >= MAX_BACKLOG), deposit returns rejected:overloaded
    + retry_after and enqueues nothing new."""
    monkeypatch.setattr(deposit_mod, "MAX_BACKLOG", 3)
    for i in range(3):
        deposit_mod.deposit(
            {"page_type": "entity", "title": f"T{i}", "body": "b"},
            {"identity": "agent-a"},
            queue=queue,
        )
    assert queue.depth() == 3
    r = deposit_mod.deposit(_payload(), {"identity": "agent-a"}, queue=queue)
    assert r.disposition == "rejected:overloaded"
    assert r.retry_after is not None
    assert not r.success
    assert queue.depth() == 3  # nothing new enqueued


def test_queue_depth_counts_submitted(queue):
    assert queue.depth() == 0
    deposit_mod.deposit(_payload(), {"identity": "a"}, queue=queue)
    assert queue.depth() == 1
