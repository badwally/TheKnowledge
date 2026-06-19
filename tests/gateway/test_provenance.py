"""Phase 1 T1.5 — operational-provenance log + per-producer telemetry stub.

The intent queue is a write-ahead log that yields an operational-provenance
graph (corpus-change -> intent -> agent), distinct from content-provenance
(claim -> source). It records the decision basis sufficient to audit and replay
a canonicalization without re-running the LLM (decision 3). Adds alongside
log.md — does not replace it.
"""

from __future__ import annotations

import subprocess

import pytest

from gateway import provenance
from gateway.commit_gate import AuthoredIntent, CommitGate
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id


def _git(root, *args, check=True):
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=check
    )


@pytest.fixture
def root(tmp_path, monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    return tmp_path


@pytest.fixture
def repo(root):
    _git(root, "init", "-q")
    _git(root, "config", "user.email", "test@test")
    _git(root, "config", "user.name", "test")
    (root / ".gitignore").write_text(".knowledge/\n")
    (root / "README.md").write_text("seed\n")
    _git(root, "add", "README.md", ".gitignore")
    _git(root, "commit", "-qm", "seed")
    return root


def test_record_appends_node_with_decision_basis(root):
    node_id = provenance.record(
        "intent-abc",
        {"policy_version": "v3", "dedup_score": 0.12,
         "dedup_candidates": ["entities/x"], "merge_rebase_branch": "no-overlap"},
    )
    assert node_id
    nodes = provenance.read_nodes()
    assert len(nodes) == 1
    n = nodes[0]
    assert n["intent_id"] == "intent-abc"
    assert n["decision_basis"]["policy_version"] == "v3"
    assert n["decision_basis"]["dedup_score"] == 0.12
    assert "timestamp" in n


def _commit_one(repo, q, rel="wiki/sources/p.md"):
    payload = {"kind": "source", "target": rel}
    ident = {"agent": "tester"}
    iid = compute_intent_id(payload, ident)
    intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid="HEAD")
    q.submit(intent)
    token = q.claim(now=1.0).fencing_token
    q.set_state(iid, "authored")
    gate = CommitGate(queue=q, provenance=provenance)
    return gate.commit(
        AuthoredIntent(intent=intent, writes={rel: "# P\n"}, base_oid="HEAD",
                       decision_basis={"policy_version": "v1"}),
        token,
    ), iid


def test_commit_records_exactly_one_node(repo):
    q = IntentQueue()
    result, iid = _commit_one(repo, q)
    assert result.success
    nodes = [n for n in provenance.read_nodes() if n["intent_id"] == iid]
    assert len(nodes) == 1
    assert nodes[0]["decision_basis"]["commit"]


def test_replay_from_node_without_llm(repo):
    q = IntentQueue()
    result, iid = _commit_one(repo, q)
    nodes = [n for n in provenance.read_nodes() if n["intent_id"] == iid]
    basis = nodes[0]["decision_basis"]
    # The node carries the canonical path — replay needs no LLM call.
    assert basis["canonical_path"].endswith("wiki/sources/p.md")
    assert str(result.canonical_path) == basis["canonical_path"]


def test_producer_telemetry_counters(root):
    t = provenance.ProducerTelemetry()
    t.incr("agent-a", "accept")
    t.incr("agent-a", "accept")
    t.incr("agent-a", "merge")
    t.incr("agent-b", "reject")
    snap = t.snapshot()
    assert snap["agent-a"]["accept"] == 2
    assert snap["agent-a"]["merge"] == 1
    assert snap["agent-b"]["reject"] == 1
