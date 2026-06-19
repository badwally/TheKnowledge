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

    # Force every rebase attempt to fail by making the merge step always raise.
    def _always_conflict(*a, **k):
        raise gate.RebaseConflict("forced")

    gate._merge_rebase = _always_conflict  # type: ignore[attr-defined]

    # Mutate HEAD so the CAS sees an overlap and routes to rebase.
    (repo / "wiki/sources/r.md").write_text("v1\n")
    _git(repo, "add", "wiki/sources/r.md")
    _git(repo, "commit", "-qm", "v1")

    r = gate.commit(authored, token)
    assert not r.success
    assert q.get_state(authored.intent.intent_id) == "dead_lettered"
    assert "contention" in (r.summary + " ".join(r.errors)).lower()


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
