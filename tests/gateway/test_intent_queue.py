"""Phase 1 T1.1 — durable intent queue with on-disk lifecycle states.

The queue is the deposit path (C7) and issues the fencing token + lease at
claim (C3). Lifecycle states are durable on-disk facts (subdirectory per
state), surviving a process restart — contrast watcher.py:78's in-memory
_pending dict which loses events while down.
"""

from __future__ import annotations

import threading

import pytest

from gateway import paths
from gateway.intent_queue import (
    STATES,
    Intent,
    IntentQueue,
    compute_intent_id,
)


@pytest.fixture
def root(tmp_path, monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    return tmp_path


def _intent(payload=None, identity=None, depends_on=None):
    payload = payload or {"kind": "source", "url": "https://example.com/a"}
    identity = identity or {"agent": "tester", "project": "p", "session": "s"}
    iid = compute_intent_id(payload, identity)
    return Intent(
        intent_id=iid,
        payload=payload,
        identity=identity,
        head_oid="deadbeef",
        depends_on=depends_on,
    )


def test_submit_durable_then_new_instance_sees_submitted(root):
    q = IntentQueue()
    intent = _intent()
    iid = q.submit(intent)

    # A *fresh* instance (simulating a process restart) sees the durable state.
    q2 = IntentQueue()
    assert q2.get_state(iid) == "submitted"
    loaded = q2.load(iid)
    assert loaded is not None
    assert loaded.payload == intent.payload
    assert loaded.identity == intent.identity


def test_compute_intent_id_is_stable_and_content_addressed():
    p = {"kind": "source", "url": "u"}
    ident = {"agent": "a"}
    assert compute_intent_id(p, ident) == compute_intent_id(p, ident)
    assert compute_intent_id(p, ident) != compute_intent_id(
        {"kind": "source", "url": "v"}, ident
    )


def test_claim_issues_monotonic_fencing_token_and_lease(root):
    q = IntentQueue()
    intent = _intent()
    iid = q.submit(intent)

    c1 = q.claim(lease_ttl=0.01, now=1000.0)
    assert c1 is not None
    assert c1.intent.intent_id == iid
    assert q.get_state(iid) == "claimed"
    assert c1.fencing_token == 1
    assert c1.lease_deadline > 1000.0

    # Lease expired -> reclaim, then claim again issues a strictly higher token.
    q.reclaim_expired(now=2000.0)
    c2 = q.claim(lease_ttl=120.0, now=2000.0)
    assert c2 is not None
    assert c2.fencing_token == 2


def test_claim_returns_none_when_empty(root):
    q = IntentQueue()
    assert q.claim() is None


def test_reclaim_expired_returns_claimed_to_submitted(root):
    q = IntentQueue()
    iid = q.submit(_intent())
    q.claim(lease_ttl=0.01, now=1000.0)
    assert q.get_state(iid) == "claimed"

    reclaimed = q.reclaim_expired(now=5000.0)
    assert iid in reclaimed
    assert q.get_state(iid) == "submitted"


def test_renew_extends_lease_and_blocks_reclaim(root):
    q = IntentQueue()
    iid = q.submit(_intent())
    q.claim(lease_ttl=10.0, now=1000.0)

    assert q.renew(iid, lease_ttl=10000.0, now=1005.0) is True
    reclaimed = q.reclaim_expired(now=2000.0)
    assert iid not in reclaimed
    assert q.get_state(iid) == "claimed"


def test_set_get_state_round_trip_all_states(root):
    q = IntentQueue()
    iid = q.submit(_intent())
    for state in STATES:
        q.set_state(iid, state)
        assert q.get_state(iid) == state


def test_fencing_token_persists_across_instances(root):
    q = IntentQueue()
    iid = q.submit(_intent())
    q.claim(lease_ttl=120.0, now=1.0)
    q2 = IntentQueue()
    assert q2.fencing_token(iid) == 1


def test_concurrent_claim_one_winner_distinct_monotonic_tokens(root):
    """SILENT-CORRUPTION-7: N concurrent claimers, exactly one wins per intent.

    The acquire primitive must be an atomic rename, so two claimers cannot both
    "win" candidates[0] with the same old+1 token. With several submitted
    intents and many threads, each intent must be claimed exactly once and the
    fencing tokens issued must all be distinct (1 per intent, monotonic).
    """
    q = IntentQueue()
    n_intents = 8
    iids = set()
    for i in range(n_intents):
        iid = q.submit(_intent(payload={"kind": "source", "n": i}))
        iids.add(iid)

    claims = []
    errors = []
    claims_lock = threading.Lock()
    barrier = threading.Barrier(16)

    def _worker():
        barrier.wait()
        # Each worker drains until empty.
        while True:
            try:
                c = q.claim(lease_ttl=120.0, now=1.0)
            except Exception as e:  # a losing claimer must NOT crash (atomic acquire)
                with claims_lock:
                    errors.append(e)
                return
            if c is None:
                return
            with claims_lock:
                claims.append(c)

    threads = [threading.Thread(target=_worker) for _ in range(16)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert errors == [], f"claim() raced and crashed: {errors!r}"

    # Every intent claimed exactly once — no double-claim, no lost intent.
    claimed_ids = [c.intent.intent_id for c in claims]
    assert sorted(claimed_ids) == sorted(iids), (
        f"expected each intent claimed once, got {claimed_ids}"
    )
    assert len(claimed_ids) == len(set(claimed_ids)), "an intent was double-claimed"
    # Each intent's fencing token is 1 (first issue), one per intent.
    for c in claims:
        assert c.fencing_token == 1


def test_fencing_survives_queue_record_loss(root):
    """ROBUSTNESS-6: durable fencing counter outlives the queue record.

    A crash that loses the claimed/ record must NOT reset the highest issued
    fencing token to zero — otherwise a resurrected slow worker's stale token
    would be accepted. The durable counter persists outside the per-state file.
    """
    q = IntentQueue()
    iid = q.submit(_intent())
    c = q.claim(lease_ttl=120.0, now=1.0)
    assert c.fencing_token == 1

    # Simulate a crash that loses the queue record entirely.
    found = q._find(iid)
    assert found is not None
    found[1].unlink()
    assert q._find(iid) is None

    # The durable fencing token still reports the highest issued value.
    q2 = IntentQueue()
    assert q2.fencing_token(iid) == 1


def test_set_declared_writes_rejects_traversal_and_absolute_paths(root, tmp_path):
    """Defense-in-depth: declared writes are self-declared by the producer, and
    crash recovery DELETES them. A path that escapes the root (``..`` segment or
    absolute) must never persist into the queue record. Validate at write time.
    """
    q = IntentQueue()
    iid = q.submit(_intent())
    q.claim(lease_ttl=120.0, now=1.0)

    abs_path = str((tmp_path / "outside" / "escape.md"))
    q.set_declared_writes(
        iid,
        [
            "wiki/sources/ok.md",
            "../escape.md",
            "wiki/../../escape.md",
            abs_path,
        ],
    )

    # Only the in-root path survives; every escaping entry is dropped.
    assert q.declared_writes(iid) == ["wiki/sources/ok.md"]
