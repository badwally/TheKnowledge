"""Phase 1 T1.5 — provenance coverage (C7).

Every committed corpus change must resolve to exactly one operational-provenance
node, INCLUDING watcher/poller ingest — no corpus state without an ancestor.
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


def test_every_committed_change_has_ancestor(repo):
    q = IntentQueue()
    gate = CommitGate(queue=q, provenance=provenance)
    for i in range(3):
        payload = {"kind": "source", "n": i}
        ident = {"agent": "tester"}
        iid = compute_intent_id(payload, ident)
        intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid="HEAD")
        q.submit(intent)
        token = q.claim(now=float(i)).fencing_token
        q.set_state(iid, "authored")
        rel = f"wiki/sources/s{i}.md"
        gate.commit(AuthoredIntent(intent=intent, writes={rel: f"# S{i}\n"},
                                   base_oid="HEAD"), token)

    gaps = provenance.coverage_gap()
    assert gaps == [], f"committed changes without a provenance ancestor: {gaps}"


def test_watcher_ingest_emits_provenance_node(repo):
    """A watcher ingest is a corpus change — it must produce a provenance node (C7)."""
    from gateway.core import OperationResult
    from gateway.watcher import WatcherDaemon

    (repo / "raw" / "inbox").mkdir(parents=True)
    inbox_file = repo / "raw" / "inbox" / "note.md"
    inbox_file.write_text("# Note\n")
    raw_path = repo / "raw" / "web" / "note.md"

    def _stub_ingest(path):
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        raw_path.write_text("# Note\n")
        return OperationResult(success=True, summary="ingested",
                               paths_touched=[raw_path])

    daemon = WatcherDaemon(inbox=repo / "raw" / "inbox", ingest_fn=_stub_ingest)
    daemon._process(inbox_file)

    nodes = provenance.read_nodes()
    watcher_nodes = [n for n in nodes if n["decision_basis"].get("producer") == "watcher"]
    assert len(watcher_nodes) == 1
    assert watcher_nodes[0]["decision_basis"]["source_id"] == "note"
    # The marker node records the paths it produced (CORRECTNESS-9).
    assert "raw/web/note.md" in watcher_nodes[0]["decision_basis"]["paths_touched"]


def test_real_watcher_commit_not_flagged_as_coverage_gap(repo):
    """CORRECTNESS-9: a real watcher commit covered by a producer marker is NOT a gap.

    The watcher daemon writes raw/ then commits SEPARATELY (after the provenance
    node is written, so the node cannot carry the commit SHA). coverage_gap()
    must treat a corpus commit whose touched paths are all produced by a marker
    node as covered — not falsely flag it.
    """
    from gateway.core import OperationResult
    from gateway.watcher import WatcherDaemon

    (repo / "raw" / "inbox").mkdir(parents=True)
    inbox_file = repo / "raw" / "inbox" / "n2.md"
    inbox_file.write_text("# N2\n")
    raw_path = repo / "raw" / "web" / "n2.md"

    def _stub_ingest(path):
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        raw_path.write_text("# N2\n")
        return OperationResult(success=True, summary="ingested",
                               paths_touched=[raw_path])

    daemon = WatcherDaemon(inbox=repo / "raw" / "inbox", ingest_fn=_stub_ingest)
    daemon._process(inbox_file)

    # The watcher daemon commits the produced raw path SEPARATELY, after the node.
    _git(repo, "add", "raw/web/n2.md")
    _git(repo, "commit", "-qm", "watcher ingest n2")
    watcher_sha = _git(repo, "rev-parse", "HEAD").stdout.strip()

    # Control: a corpus commit with NEITHER a commit-SHA node NOR a producer
    # marker IS a real gap — proves coverage_gap actually detects gaps (i.e. the
    # commit-block parser reads touched paths, not silently dropping them).
    (repo / "wiki" / "sources").mkdir(parents=True)
    (repo / "wiki" / "sources" / "orphan.md").write_text("# Orphan\n")
    _git(repo, "add", "wiki/sources/orphan.md")
    _git(repo, "commit", "-qm", "uncovered corpus change")
    orphan_sha = _git(repo, "rev-parse", "HEAD").stdout.strip()

    gaps = provenance.coverage_gap()
    assert watcher_sha not in gaps, (
        f"real watcher commit falsely flagged as a coverage gap: {gaps}"
    )
    assert orphan_sha in gaps, (
        f"genuinely uncovered corpus commit not detected as a gap: {gaps}"
    )
