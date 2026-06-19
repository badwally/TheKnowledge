"""Tests for revert_resolution op — Phase 5 Task 1, G1.

Mirrors the ops/deposit.py pattern: validate, durably enqueue, acknowledge.
Uses tmp_queue_env from test_deposit.py (same fixture pattern).

Note on IntentQueue API: IntentQueue has no public read_record method.
The internal _read(intent_id) -> (state, rec) | None is used for test
verification. This was confirmed in Step 0 (intent_queue.py:205-211).
"""

from __future__ import annotations

import pytest

from gateway.ops.revert_resolution import revert_resolution
from gateway.intent_queue import IntentQueue


@pytest.fixture
def tmp_queue_env(tmp_path, monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    (tmp_path / ".knowledge").mkdir(parents=True, exist_ok=True)
    return tmp_path


# ---------------------------------------------------------------------------
# G1 — revert_resolution enqueues a provenanced, reversible intent
# ---------------------------------------------------------------------------

def test_revert_resolution_enqueues_provenanced_intent(tmp_queue_env):
    """A revert-resolution call enqueues durably and returns a queued receipt."""
    res = revert_resolution("act-abc123", {"agent": "tester"})

    assert res.success
    assert res.disposition == "queued"
    assert res.intent_id

    q = IntentQueue()
    found = q._read(res.intent_id)
    assert found is not None, "intent must be on disk after ack"
    state, rec = found
    assert state == "submitted"
    assert rec["payload"]["reverts_act"] == "act-abc123"
    assert rec["payload"]["reversal_type"] == "contradiction-resolution"
    assert rec["identity"]["operation"] == "revert-resolution"


def test_revert_resolution_idempotent_same_act_same_intent_id(tmp_queue_env):
    """Content-addressed: same act_id + same identity → same intent_id (idempotent)."""
    a = revert_resolution("act-abc123", {"agent": "tester"})
    b = revert_resolution("act-abc123", {"agent": "tester"})
    assert a.success
    assert b.success
    assert a.intent_id == b.intent_id


def test_revert_resolution_different_acts_different_intent_ids(tmp_queue_env):
    """Different act_ids produce different intent_ids."""
    a = revert_resolution("act-111", {"agent": "tester"})
    b = revert_resolution("act-222", {"agent": "tester"})
    assert a.intent_id != b.intent_id


def test_revert_resolution_payload_carries_policy_version(tmp_queue_env):
    """Payload includes the reversal policy version for auditability."""
    res = revert_resolution("act-xyz", {"agent": "tester"})
    q = IntentQueue()
    _, rec = q._read(res.intent_id)
    assert "policy_version" in rec["payload"]
    assert rec["payload"]["policy_version"] == "contradiction-reversal-policy-v1"


def test_revert_resolution_returns_retry_after(tmp_queue_env):
    """Receipt includes retry_after so callers know when to poll for terminal state."""
    res = revert_resolution("act-abc123", {"agent": "tester"})
    assert res.retry_after is not None
    assert res.retry_after > 0


def test_revert_resolution_negative_control_empty_act_id_rejected(tmp_queue_env):
    """An empty act_id is rejected before enqueue (validation)."""
    res = revert_resolution("", {"agent": "tester"})
    assert not res.success
    assert res.disposition == "rejected"


def test_revert_resolution_identity_merged_into_intent(tmp_queue_env):
    """The caller-supplied identity dict is preserved in the intent record."""
    res = revert_resolution("act-abc123", {"agent": "my-agent", "session": "s42"})
    q = IntentQueue()
    _, rec = q._read(res.intent_id)
    assert rec["identity"]["agent"] == "my-agent"
    assert rec["identity"]["session"] == "s42"
    assert rec["identity"]["operation"] == "revert-resolution"
