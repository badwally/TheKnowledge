"""Phase 1 T1.3 — status-query op: intent_id -> typed disposition (A1).

Maps intent_id -> terminal disposition union (committed->path,
merged->canonical_path, rejected->rule, quarantined->queue,
dead_lettered->reason); non-terminal returns retry_after («deposit.max_wait»).
An agent author can write the deposit wait-loop from this contract alone.
"""

from __future__ import annotations

import pytest

from gateway.intent_queue import Intent, IntentQueue, compute_intent_id
from gateway.ops.intent_status import DEFAULT_RETRY_AFTER, intent_status


@pytest.fixture
def q(tmp_path, monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    return IntentQueue()


def _seed(q, state, *, result=None, payload=None):
    payload = payload or {"kind": "source", "target": "wiki/sources/x.md"}
    ident = {"agent": "tester"}
    iid = compute_intent_id(payload, ident)
    q.submit(Intent(intent_id=iid, payload=payload, identity=ident))
    q.set_state(iid, state, result=result)
    return iid


def test_committed_returns_canonical_path(q):
    iid = _seed(q, "committed", result={"canonical_path": "wiki/sources/x.md"})
    r = intent_status(iid, queue=q)
    assert r.success
    assert r.disposition == "committed"
    assert r.canonical_path is not None
    assert str(r.canonical_path) == "wiki/sources/x.md"


def test_merged_returns_canonical_path_different_from_target(q):
    iid = _seed(
        q, "committed",
        payload={"kind": "entity", "target": "wiki/entities/dup.md"},
        result={"disposition": "merged", "canonical_path": "wiki/entities/canon.md"},
    )
    r = intent_status(iid, queue=q)
    assert r.disposition == "merged"
    assert str(r.canonical_path) == "wiki/entities/canon.md"
    assert str(r.canonical_path) != "wiki/entities/dup.md"


def test_rejected_returns_rule(q):
    iid = _seed(q, "rejected", result={"reason": "ungrounded-claim"})
    r = intent_status(iid, queue=q)
    assert r.disposition == "rejected"
    assert "ungrounded-claim" in r.summary


def test_dead_lettered_returns_reason(q):
    iid = _seed(q, "dead_lettered", result={"reason": "contention"})
    r = intent_status(iid, queue=q)
    assert r.disposition == "dead_lettered"
    assert "contention" in r.summary


@pytest.mark.parametrize("state", ["submitted", "claimed", "authored"])
def test_non_terminal_returns_retry_after(q, state):
    iid = _seed(q, state)
    r = intent_status(iid, queue=q)
    assert r.disposition == state
    assert r.retry_after == DEFAULT_RETRY_AFTER


def test_unknown_intent_id_returns_failure(q):
    r = intent_status("0000000000000000", queue=q)
    assert not r.success
