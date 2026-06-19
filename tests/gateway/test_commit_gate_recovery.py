"""Phase 1 T1.4 — CommitGate crash recovery (C1).

A crash mid-reattachment can leave a partially-written working tree (the N-file
writes precede the atomic git boundary, and write_atomic is per-file). Recovery:
on restart, `git reset --hard HEAD` + `git clean -fd` to HEAD, then re-claim the
in-flight intent from `claimed` (its lease has expired).
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


def test_recover_resets_dirty_tree_and_reclaims(repo):
    q = IntentQueue()
    # An in-flight intent claimed with an already-expired lease (crashed worker).
    payload = {"kind": "source", "target": "wiki/sources/a.md"}
    ident = {"agent": "tester"}
    iid = compute_intent_id(payload, ident)
    q.submit(Intent(intent_id=iid, payload=payload, identity=ident))
    q.claim(lease_ttl=0.001, now=1.0)
    assert q.get_state(iid) == "claimed"

    # Simulate a torn write: stray untracked file + modified tracked file.
    (repo / "wiki").mkdir()
    (repo / "wiki" / "partial.md").write_text("half-written\n")
    (repo / "tracked.md").write_text("corrupted by torn write\n")

    gate = CommitGate(queue=q)
    reclaimed = gate.recover(now=10_000.0)

    # Working tree clean post-restart.
    porcelain = _git(repo, "status", "--porcelain").stdout
    assert porcelain.strip() == "", f"tree not clean: {porcelain!r}"
    assert (repo / "tracked.md").read_text() == "original\n"
    assert not (repo / "wiki" / "partial.md").exists()

    # Intent re-runs from claimed -> back to submitted for a fresh claim.
    assert iid in reclaimed
    assert q.get_state(iid) == "submitted"
