"""Librarian Phase 2 (T3) — commit-time embedding freshness.

The committer upserts a committed page's embedding rows current-as-of-HEAD as
part of the commit flow (an incremental upsert on commit, NOT a lazy per-query
rebuild — commit-time dedup READS the embedding index, design §13). The proving
property: an intent committed earlier in the same serialization window is
visible to an entity-namespace NN-search before the next intent commits.

These tests exercise the REAL CommitGate over a REAL temp git repo with a REAL
EmbeddingIndex — no monkeypatching of the commit path.
"""

from __future__ import annotations

import subprocess

import pytest

from gateway.commit_gate import AuthoredIntent, CommitGate
from gateway.embedding_index import EmbeddingIndex
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
    (tmp_path / ".gitignore").write_text(".knowledge/\n.index/\n")
    (tmp_path / "README.md").write_text("seed\n")
    _git(tmp_path, "add", "README.md", ".gitignore")
    _git(tmp_path, "commit", "-qm", "seed")
    return tmp_path


def _authored(q, *, writes, payload=None, base_oid="HEAD"):
    payload = payload or {"kind": "entity", "target": list(writes)[0]}
    ident = {"agent": "tester"}
    iid = compute_intent_id(payload, ident)
    intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid=base_oid)
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")
    claim_token = q.fencing_token(iid)
    return AuthoredIntent(intent=intent, writes=writes, base_oid=base_oid), claim_token


_ENTITY_A = (
    "---\ntype: entity\ntitle: Semaglutide\naliases: [Ozempic, Wegovy]\n---\n"
    "# Overview\nA GLP-1 receptor agonist.\n"
)
_ENTITY_B = (
    "---\ntype: entity\ntitle: Semaglutide injection\naliases: [Ozempic]\n---\n"
    "# Overview\nGLP-1 agonist.\n"
)


def test_commit_upserts_entity_namespace_freshness(repo):
    """A page committed earlier in the window is visible to entity-NN before the
    next commit — proves incremental upsert-on-commit (not lazy rebuild)."""
    q = IntentQueue()
    idx = EmbeddingIndex()
    gate = CommitGate(queue=q, embedding_index=idx)

    a, ta = _authored(q, writes={"wiki/entities/semaglutide.md": _ENTITY_A})
    r = gate.commit(a, ta)
    assert r.success, r.errors

    # current-as-of-HEAD: A is in the entity namespace immediately after commit.
    hits = idx.nn("entity", "Semaglutide Ozempic Wegovy", k=5)
    assert hits and hits[0].key == "wiki/entities/semaglutide.md", \
        [(h.key, h.distance) for h in hits]
    assert hits[0].distance < 0.30  # within the strict dedup operating point

    # Before B commits (same serialization window), the dedup lookup SEES A.
    pre_b = idx.nn("entity", "Semaglutide injection Ozempic", k=5)
    assert any(h.key == "wiki/entities/semaglutide.md" for h in pre_b), \
        "earlier-in-window page must be visible to the next intent's dedup"


def test_commit_without_embedding_index_creates_no_rows(repo):
    """Negative control: embedding_index=None → NO entity rows. Proves the
    upsert is the cause, not a lazy rebuild elsewhere."""
    from gateway import paths

    q = IntentQueue()
    gate = CommitGate(queue=q)  # no embedding index
    a, ta = _authored(q, writes={"wiki/entities/semaglutide.md": _ENTITY_A})
    r = gate.commit(a, ta)
    assert r.success, r.errors

    # No store written by the commit. A fresh index reading it sees nothing.
    assert not paths.embedding_db_path().exists() or \
        EmbeddingIndex().nn("entity", "Semaglutide", k=5) == []


def test_commit_no_embedding_index_is_back_compat_noop(repo):
    """A CommitGate with no embedding index commits cleanly (Phase-1 back-compat)."""
    q = IntentQueue()
    gate = CommitGate(queue=q)
    a, ta = _authored(q, writes={"wiki/sources/x.md": "# X\nbody\n"})
    r = gate.commit(a, ta)
    assert r.success and r.disposition == "committed"
    assert (repo / "wiki/sources/x.md").read_text() == "# X\nbody\n"


def test_commit_upserts_section_namespace(repo):
    """Committed page sections land in the section namespace too."""
    q = IntentQueue()
    idx = EmbeddingIndex()
    gate = CommitGate(queue=q, embedding_index=idx)
    a, ta = _authored(q, writes={"wiki/entities/semaglutide.md": _ENTITY_A})
    gate.commit(a, ta)

    sec = idx.nn("section", "GLP-1 receptor agonist overview", k=5)
    assert any(h.key.startswith("wiki/entities/semaglutide.md#") for h in sec)
