"""Phase 1 T1.4 — CommitGate: serial commit + MVCC CAS + idempotency + fencing.

The CommitGate owns the single serial commit (decision 1). It holds the
`librarian-commit` mutex (the §4 migration delta — commit mutex replaces the
global wiki-author barrier for the commit step), generalizes the
discharge_orphans git-shell (`git add -- <explicit>`, never -A), and enforces
MVCC compare-and-swap (three cases), idempotency keyed off committed state (C2),
and fencing (C3).
"""

from __future__ import annotations

import subprocess
import threading

import pytest

from gateway import locking
from gateway.commit_gate import AuthoredIntent, CommitGate
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id


def _git(root, *args, check=True):
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=check
    )


@pytest.fixture
def repo(tmp_path, monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "test@test")
    _git(tmp_path, "config", "user.name", "test")
    (tmp_path / ".gitignore").write_text(".knowledge/\n")
    (tmp_path / "README.md").write_text("seed\n")
    _git(tmp_path, "add", "README.md", ".gitignore")
    _git(tmp_path, "commit", "-qm", "seed")
    return tmp_path


def _authored(q, *, writes, payload=None, base_oid="HEAD"):
    payload = payload or {"kind": "source", "target": list(writes)[0]}
    ident = {"agent": "tester"}
    iid = compute_intent_id(payload, ident)
    intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid=base_oid)
    q.submit(intent)
    claim = q.claim(now=1.0)
    q.set_state(iid, "authored")
    return AuthoredIntent(intent=intent, writes=writes, base_oid=base_oid), claim.fencing_token


def test_lock_name_registered():
    assert "librarian-commit" in locking.LOCK_NAMES


def test_commit_no_overlap_writes_and_commits(repo):
    q = IntentQueue()
    authored, token = _authored(q, writes={"wiki/sources/x.md": "# X\nbody\n"})
    gate = CommitGate(queue=q)

    r = gate.commit(authored, token)

    assert r.success, r.errors
    assert r.disposition == "committed"
    assert (repo / "wiki/sources/x.md").read_text() == "# X\nbody\n"
    log = _git(repo, "log", "-1", "--format=%B").stdout
    assert f"Intent-Id: {authored.intent.intent_id}" in log
    assert q.get_state(authored.intent.intent_id) == "committed"
    assert str(r.canonical_path).endswith("wiki/sources/x.md")


def test_redeliver_committed_intent_is_noop_from_history(repo):
    q = IntentQueue()
    authored, token = _authored(q, writes={"wiki/sources/y.md": "# Y\n"})
    gate = CommitGate(queue=q)
    gate.commit(authored, token)
    head_before = _git(repo, "rev-parse", "HEAD").stdout.strip()

    # Idempotency is keyed off committed history, not the queue status file:
    # remove the queue record entirely and redeliver — still a no-op.
    iid = authored.intent.intent_id
    for d in ("committed",):
        p = q._state_dir(d) / f"{iid}.json"
        if p.exists():
            p.unlink()

    r2 = gate.commit(authored, token)
    assert r2.no_op is True
    assert r2.disposition == "committed"
    head_after = _git(repo, "rev-parse", "HEAD").stdout.strip()
    assert head_before == head_after


def test_stale_fencing_token_rejected(repo):
    q = IntentQueue()
    authored, token1 = _authored(q, writes={"wiki/sources/z.md": "# Z\n"})
    iid = authored.intent.intent_id
    # Simulate a crashed worker: return the intent to claimed, expire its lease,
    # reclaim, and let a fresh worker re-claim -> a strictly higher fencing token.
    q.set_state(iid, "claimed")
    q.renew(iid, lease_ttl=0.001, now=1.0)
    q.reclaim_expired(now=10_000.0)
    q.claim(now=10_001.0)  # token 2 issued to the reclaimer
    q.set_state(iid, "authored")
    assert q.fencing_token(iid) == 2
    gate = CommitGate(queue=q)

    head_before = _git(repo, "rev-parse", "HEAD").stdout.strip()
    r = gate.commit(authored, token1)  # stale token 1
    assert not r.success
    assert r.disposition == "rejected"
    assert "fencing" in (r.summary + " ".join(r.errors)).lower()
    assert _git(repo, "rev-parse", "HEAD").stdout.strip() == head_before


def test_contradictory_edit_dead_letters(repo):
    q = IntentQueue()
    # Author against a base where the file is absent, but HEAD now has it with
    # different content -> contradictory.
    (repo / "wiki/sources").mkdir(parents=True)
    (repo / "wiki/sources/c.md").write_text("HEAD content\n")
    _git(repo, "add", "wiki/sources/c.md")
    _git(repo, "commit", "-qm", "add c")

    authored, token = _authored(
        q, writes={"wiki/sources/c.md": "authored content\n"},
        base_oid="0" * 40,  # authored against a non-existent base for this path
    )
    gate = CommitGate(queue=q)
    r = gate.commit(authored, token)
    assert not r.success
    assert q.get_state(authored.intent.intent_id) == "dead_lettered"


def test_bounded_rebase_dead_letters_contention(repo):
    """C4: HEAD perpetually moving under the rebase → bounded → contention.

    Contention is distinct from needs-merge: here _merge_rebase keeps succeeding
    but the post-merge re-CAS never lands 'commit' because HEAD keeps moving.
    The bounded attempt count dead-letters as 'contention'.
    """
    q = IntentQueue()
    (repo / "wiki/sources").mkdir(parents=True)
    (repo / "wiki/sources/r.md").write_text("v0\n")
    _git(repo, "add", "wiki/sources/r.md")
    _git(repo, "commit", "-qm", "v0")
    base = _git(repo, "rev-parse", "HEAD:wiki/sources/r.md").stdout.strip()

    authored, token = _authored(
        q, writes={"wiki/sources/r.md": "v0\nmerged-claim\n"},
        base_oid=base,
    )
    gate = CommitGate(queue=q, max_rebase_attempts=2)

    # Mutate HEAD so the initial CAS sees an overlap and routes to rebase.
    (repo / "wiki/sources/r.md").write_text("v1\n")
    _git(repo, "add", "wiki/sources/r.md")
    _git(repo, "commit", "-qm", "v1")

    # Simulate HEAD perpetually moving under us: _merge_rebase succeeds (returns
    # the authored payload) but the re-CAS always sees an overlap → never commits.
    gate._merge_rebase = lambda a: dict(a.writes)  # type: ignore[attr-defined]
    gate._classify = lambda a: "rebase"  # type: ignore[attr-defined]
    # Force the very first classify (before the loop) to 'rebase' too.

    r = gate.commit(authored, token)
    assert not r.success
    assert q.get_state(authored.intent.intent_id) == "dead_lettered"
    assert "contention" in (r.summary + " ".join(r.errors)).lower()


def test_concurrent_overlap_dead_letters_needs_merge_no_lost_update(repo):
    """SILENT-CORRUPTION-4 / F1: a concurrent overlapping change is NOT dropped.

    An intent authored against base blob B is committed; a SECOND intent authored
    against the SAME base B (it never saw the first edit) must NOT blind-overwrite
    the now-divergent HEAD. The Phase-1 scaffold fails safe: dead-letter as
    needs-merge, preserving the first writer's change (no lost update).
    """
    q = IntentQueue()
    (repo / "wiki/concepts").mkdir(parents=True)
    (repo / "wiki/concepts/k.md").write_text("# K\nbase body\n")
    _git(repo, "add", "wiki/concepts/k.md")
    _git(repo, "commit", "-qm", "base k")
    base = _git(repo, "rev-parse", "HEAD:wiki/concepts/k.md").stdout.strip()

    # Writer 1 commits a concurrent change to the page.
    a1, t1 = _authored(
        q, writes={"wiki/concepts/k.md": "# K\nbase body\nwriter-1 addition\n"},
        payload={"kind": "concept", "n": 1}, base_oid=base,
    )
    gate = CommitGate(queue=q)
    r1 = gate.commit(a1, t1)
    assert r1.success, r1.errors
    head_after_1 = (repo / "wiki/concepts/k.md").read_text()
    assert "writer-1 addition" in head_after_1

    # Writer 2 authored against the SAME base B (did not see writer 1's edit).
    a2, t2 = _authored(
        q, writes={"wiki/concepts/k.md": "# K\nbase body\nwriter-2 addition\n"},
        payload={"kind": "concept", "n": 2}, base_oid=base,
    )
    r2 = gate.commit(a2, t2)

    # MUST dead-letter — never silently overwrite writer 1's change.
    assert not r2.success
    assert q.get_state(a2.intent.intent_id) == "dead_lettered"
    assert "needs-merge" in (r2.summary + " ".join(r2.errors)).lower()
    # Writer 1's change is intact on disk (no lost update).
    assert (repo / "wiki/concepts/k.md").read_text() == head_after_1
    assert "writer-2 addition" not in (repo / "wiki/concepts/k.md").read_text()


def test_writes_serialized_at_one_gate(repo):
    q = IntentQueue()
    gate = CommitGate(queue=q)

    authored_list = []
    for i in range(6):
        a, t = _authored(
            q, writes={f"wiki/sources/s{i}.md": f"# S{i}\n"},
            payload={"kind": "source", "n": i},
        )
        authored_list.append((a, t))

    results = {}
    threads = []

    def _do(a, t, idx):
        results[idx] = gate.commit(a, t)

    for idx, (a, t) in enumerate(authored_list):
        th = threading.Thread(target=_do, args=(a, t, idx))
        threads.append(th)
    for th in threads:
        th.start()
    for th in threads:
        th.join()

    assert all(r.success for r in results.values()), [r.errors for r in results.values()]
    # Linear history, no index.lock corruption: every file present.
    for i in range(6):
        assert (repo / f"wiki/sources/s{i}.md").exists()


def test_cas_three_cases_against_real_oid_divergence(repo):
    """BLOCKER-2: CAS compares real per-path blob OIDs, not the literal 'HEAD'.

    Exercises all three classification cases against real out-of-band HEAD
    mutation — no monkeypatch of _merge_rebase/_classify:

      - no-overlap: the intent's path is unrelated to what moved at HEAD → commit;
      - rebase (mergeable): HEAD's blob == the authored base (nothing concurrent
        actually changed the body) → re-applies and commits;
      - contradictory: the authored base never existed but HEAD now has the path
        → dead-letter.
    """
    (repo / "wiki/sources").mkdir(parents=True)

    # --- case 1: no-overlap ---
    (repo / "wiki/sources/p1.md").write_text("# P1\nv0\n")
    _git(repo, "add", "wiki/sources/p1.md")
    _git(repo, "commit", "-qm", "p1 v0")
    p1_base = _git(repo, "rev-parse", "HEAD:wiki/sources/p1.md").stdout.strip()

    q = IntentQueue()
    # Author against p1's real blob OID, but write an UNRELATED new path.
    payload = {"kind": "source", "n": "nooverlap"}
    ident = {"agent": "tester"}
    iid = compute_intent_id(payload, ident)
    intent = Intent(intent_id=iid, payload=payload, identity=ident)
    q.submit(intent)
    token = q.claim(now=1.0).fencing_token
    q.set_state(iid, "authored")
    gate = CommitGate(queue=q)
    authored = AuthoredIntent(
        intent=intent, writes={"wiki/sources/fresh.md": "# Fresh\n"},
        base_oid=p1_base, base_oids={"wiki/sources/fresh.md": None},
    )
    # Mutate HEAD on p1 out-of-band (unrelated to the write).
    (repo / "wiki/sources/p1.md").write_text("# P1\nv1\n")
    _git(repo, "add", "wiki/sources/p1.md")
    _git(repo, "commit", "-qm", "p1 v1")
    r = gate.commit(authored, token)
    assert r.success, r.errors
    assert r.disposition == "committed"

    # --- case 2: rebase (mergeable) ---
    (repo / "wiki/sources/p2.md").write_text("# P2\nbody\n")
    _git(repo, "add", "wiki/sources/p2.md")
    _git(repo, "commit", "-qm", "p2")
    p2_base = _git(repo, "rev-parse", "HEAD:wiki/sources/p2.md").stdout.strip()
    payload2 = {"kind": "source", "n": "rebase"}
    iid2 = compute_intent_id(payload2, ident)
    intent2 = Intent(intent_id=iid2, payload=payload2, identity=ident)
    q.submit(intent2)
    token2 = q.claim(now=2.0).fencing_token
    q.set_state(iid2, "authored")
    # Make a NON-overlapping HEAD move elsewhere so _classify sees p2 unchanged
    # vs base (HEAD blob == base) — the mergeable/no-real-change rebase path.
    authored2 = AuthoredIntent(
        intent=intent2, writes={"wiki/sources/p2.md": "# P2\nbody\nclaim\n"},
        base_oid=p2_base, base_oids={"wiki/sources/p2.md": p2_base},
    )
    r2 = gate.commit(authored2, token2)
    assert r2.success, r2.errors
    assert (repo / "wiki/sources/p2.md").read_text() == "# P2\nbody\nclaim\n"

    # --- case 3: contradictory ---
    (repo / "wiki/sources/p3.md").write_text("# P3\nhead-only\n")
    _git(repo, "add", "wiki/sources/p3.md")
    _git(repo, "commit", "-qm", "p3")
    payload3 = {"kind": "source", "n": "contradictory"}
    iid3 = compute_intent_id(payload3, ident)
    intent3 = Intent(intent_id=iid3, payload=payload3, identity=ident)
    q.submit(intent3)
    token3 = q.claim(now=3.0).fencing_token
    q.set_state(iid3, "authored")
    # Author thought p3 was absent (base None) but HEAD now has it → contradictory.
    authored3 = AuthoredIntent(
        intent=intent3, writes={"wiki/sources/p3.md": "# P3\nauthored\n"},
        base_oid="0" * 40, base_oids={"wiki/sources/p3.md": None},
    )
    r3 = gate.commit(authored3, token3)
    assert not r3.success
    assert q.get_state(iid3) == "dead_lettered"
    assert "contradictory" in (r3.summary + " ".join(r3.errors)).lower()


def test_idempotency_trailer_exact_not_prefix_collidable(repo):
    """BLOCKER-3: a hex-prefix-colliding intent_id is NOT treated as committed.

    Two intent_ids share a prefix (abcd1234 vs abcd1234ef). After committing the
    SHORTER one, redelivering the LONGER one must commit normally — the trailer
    resolution is exact-value, not an unanchored `--grep` substring.
    """
    q = IntentQueue()
    short_id = "abcd1234"
    long_id = "abcd1234ef567890"
    assert long_id.startswith(short_id)  # colliding prefix

    def _commit_with_id(iid, rel):
        payload = {"kind": "source", "target": rel}
        ident = {"agent": "tester"}
        intent = Intent(intent_id=iid, payload=payload, identity=ident)
        q.submit(intent)
        token = q.claim(now=1.0).fencing_token
        q.set_state(iid, "authored")
        gate = CommitGate(queue=q)
        return gate.commit(
            AuthoredIntent(intent=intent, writes={rel: f"# {iid}\n"},
                           base_oid="HEAD", base_oids={rel: None}),
            token,
        )

    r_short = _commit_with_id(short_id, "wiki/sources/short.md")
    assert r_short.success, r_short.errors

    # The longer id, whose prefix matches the committed short id's trailer,
    # must NOT be treated as already-committed — it commits its own page.
    r_long = _commit_with_id(long_id, "wiki/sources/long.md")
    assert r_long.success, r_long.errors
    assert r_long.no_op is not True, "prefix collision falsely matched a trailer"
    assert (repo / "wiki/sources/long.md").exists()


def test_status_query_does_not_block_on_commit_mutex(repo):
    """Never-regress: reads are non-blocking against a committed ref."""
    from gateway.ops.intent_status import intent_status

    q = IntentQueue()
    authored, token = _authored(q, writes={"wiki/sources/q.md": "# Q\n"})
    iid = authored.intent.intent_id

    held = threading.Event()
    release = threading.Event()

    def _hold_mutex():
        with locking.file_lock("librarian-commit"):
            held.set()
            release.wait(timeout=5)

    holder = threading.Thread(target=_hold_mutex)
    holder.start()
    assert held.wait(timeout=5)
    try:
        r = intent_status(iid, queue=q)  # must return while mutex is held
        assert r.disposition == "authored"
    finally:
        release.set()
        holder.join()
