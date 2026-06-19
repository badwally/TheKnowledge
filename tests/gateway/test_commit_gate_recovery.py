"""Phase 1 T1.4 — CommitGate crash recovery (C1).

A crash mid-reattachment can leave a partially-written working tree (the N-file
writes precede the atomic git boundary, and write_atomic is per-file). Recovery
must revert ONLY the failed intent's declared write set — never `git reset
--hard` / `git clean -fd` the shared tree, which would destroy other sessions'
and the watcher's uncommitted/untracked work (BLOCKER-1). Tracked paths the
intent dirtied are `git checkout --`'d; untracked paths it created are `rm`'d.
Then the in-flight intent is re-claimed from `claimed` (its lease has expired).
"""

from __future__ import annotations

import subprocess

import pytest

from gateway.commit_gate import CommitGate
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
    # `.knowledge/` holds derived/operational state; gitignored in production.
    (tmp_path / ".gitignore").write_text(".knowledge/\n")
    (tmp_path / "tracked.md").write_text("original\n")
    _git(tmp_path, "add", "tracked.md", ".gitignore")
    _git(tmp_path, "commit", "-qm", "seed")
    return tmp_path


def test_recover_reverts_only_failed_intent_writes_preserving_unrelated(repo):
    """BLOCKER-1: recovery is scoped to the failed intent's declared write set.

    Unrelated uncommitted work in the SHARED tree — another session's untracked
    file and an unrelated tracked modification (e.g. the watcher's in-flight
    edits) — MUST survive recovery. Only the crashed intent's partial writes are
    reverted.
    """
    q = IntentQueue()
    # An in-flight intent claimed with an already-expired lease (crashed worker).
    # Its declared write set: a tracked path it dirtied + an untracked path it
    # created.
    payload = {"kind": "source", "target": "tracked.md"}
    ident = {"agent": "tester"}
    iid = compute_intent_id(payload, ident)
    q.submit(Intent(intent_id=iid, payload=payload, identity=ident))
    q.claim(lease_ttl=0.001, now=1.0)
    assert q.get_state(iid) == "claimed"

    # The gate durably records the declared write set before touching the tree.
    q.set_declared_writes(iid, ["tracked.md", "wiki/sources/a.md"])

    # The crashed intent's partial writes: a torn tracked file + a new untracked.
    (repo / "wiki" / "sources").mkdir(parents=True)
    (repo / "wiki" / "sources" / "a.md").write_text("half-written by crashed intent\n")
    (repo / "tracked.md").write_text("corrupted by the crashed intent\n")

    # UNRELATED uncommitted work that must NOT be destroyed:
    #   (a) another session's / the watcher's untracked file
    (repo / "raw" / "inbox").mkdir(parents=True)
    (repo / "raw" / "inbox" / "unrelated.md").write_text("another session's drop\n")
    #   (b) an unrelated tracked modification
    (repo / "other.md").write_text("v0\n")
    _git(repo, "add", "other.md")
    _git(repo, "commit", "-qm", "add other")
    (repo / "other.md").write_text("unrelated in-flight edit\n")

    gate = CommitGate(queue=q)
    reclaimed = gate.recover(now=10_000.0)

    # The crashed intent's partial writes are reverted.
    assert (repo / "tracked.md").read_text() == "original\n"
    assert not (repo / "wiki" / "sources" / "a.md").exists()

    # Unrelated work SURVIVES — recovery did not blanket reset/clean the tree.
    assert (repo / "raw" / "inbox" / "unrelated.md").read_text() == "another session's drop\n"
    assert (repo / "other.md").read_text() == "unrelated in-flight edit\n"

    # Intent re-runs from claimed -> back to submitted for a fresh claim.
    assert iid in reclaimed
    assert q.get_state(iid) == "submitted"
