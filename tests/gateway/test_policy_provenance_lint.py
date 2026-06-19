"""Tests for lint/policy_provenance — out-of-band policy-edit detector (G7).

A policy.yaml whose last change has no policy-edit provenance node is flagged.
A policy.yaml that was last touched by a policy-edit intent is not flagged.

Named negative control: a freshly-written policy (no provenance at all) is
always flagged. This guards against the lint silently doing nothing when
provenance nodes are absent.

Hardcoded threshold constants (commit_gate.py COMMIT_LOCK_ACQUIRE_TIMEOUT,
deposit.py MAX_BACKLOG) are NOT gated by this runtime path — they require
code-review and merge. The lint message must document this boundary.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml


@pytest.fixture()
def tmp_kb(tmp_path, monkeypatch):
    """Minimal KB root with provenance dir and policies dir."""
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    (tmp_path / ".knowledge" / "provenance").mkdir(parents=True)
    (tmp_path / ".knowledge" / "policies").mkdir(parents=True)
    return tmp_path


def _write_policy(root: Path, domain: str, data: dict) -> Path:
    pol_dir = root / ".knowledge" / "policies" / domain
    pol_dir.mkdir(parents=True, exist_ok=True)
    p = pol_dir / "policy.yaml"
    p.write_text(yaml.dump(data))
    return p


def _write_provenance_node(root: Path, intent_id: str, basis: dict) -> None:
    """Record a provenance node via the REAL recorder.

    CRITICAL 2: the original fixture fabricated a {"basis": ...} shape that did
    NOT match production (provenance.record persists under "decision_basis").
    Driving the real recorder means the test fails if the lint reads the wrong
    key — the same fabricated-schema defect class as T1's reattachment test.
    """
    from gateway import provenance

    provenance.record(intent_id, basis, root=root)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_out_of_band_policy_edit_is_flagged(tmp_kb):
    """A policy.yaml with no policy-edit provenance node is flagged."""
    from gateway.lint import policy_provenance

    _write_policy(tmp_kb, "med", {"domain": {"slug": "med"}, "version": 1})
    # No provenance nodes at all.
    findings = policy_provenance.run(root=tmp_kb)
    assert any(
        f.check == "policy-provenance" and "med" in f.message
        for f in findings
    ), f"expected a finding for 'med'; got {findings}"


def test_provenanced_policy_is_not_flagged(tmp_kb):
    """A policy.yaml with a matching policy-edit provenance node is clean."""
    from gateway.lint import policy_provenance

    _write_policy(tmp_kb, "med", {"domain": {"slug": "med"}, "version": 2})
    _write_provenance_node(
        tmp_kb,
        "abc123",
        {"op": "policy-edit", "domain": "med", "provenance_type": "policy-edit"},
    )
    findings = policy_provenance.run(root=tmp_kb)
    med_findings = [f for f in findings if "med" in f.message]
    assert not med_findings, (
        f"provenanced policy should not be flagged; got {med_findings}"
    )


def test_multiple_domains_only_unprovenanced_flagged(tmp_kb):
    """With two domains, only the one lacking provenance is flagged."""
    from gateway.lint import policy_provenance

    _write_policy(tmp_kb, "med", {"domain": {"slug": "med"}, "version": 1})
    _write_policy(tmp_kb, "econ", {"domain": {"slug": "econ"}, "version": 2})
    _write_provenance_node(
        tmp_kb,
        "def456",
        {"op": "policy-edit", "domain": "econ", "provenance_type": "policy-edit"},
    )

    findings = policy_provenance.run(root=tmp_kb)
    slugs = {f.message for f in findings if f.check == "policy-provenance"}
    # econ has provenance → clean; med does not → flagged
    assert any("med" in s for s in slugs), f"med should be flagged; findings: {findings}"
    assert not any("econ" in s for s in slugs), f"econ should not be flagged; findings: {findings}"


def test_no_policies_returns_empty(tmp_kb):
    """With no policy files, the check returns no findings."""
    from gateway.lint import policy_provenance

    findings = policy_provenance.run(root=tmp_kb)
    assert findings == []


def test_lint_message_documents_threshold_constants_boundary(tmp_kb):
    """Lint finding message must mention hardcoded constants + code-review gate."""
    from gateway.lint import policy_provenance

    _write_policy(tmp_kb, "med", {"domain": {"slug": "med"}, "version": 1})
    findings = policy_provenance.run(root=tmp_kb)
    assert findings, "expected at least one finding"
    msg = findings[0].message
    # The message must document that threshold constants are code-review gated
    assert any(
        kw in msg.lower()
        for kw in ("threshold", "code-review", "code review", "hardcoded", "constant")
    ), f"lint message must mention hardcoded threshold/code-review gate; got: {msg!r}"


def test_gate_recorded_node_is_recognized_by_lint(tmp_path, monkeypatch):
    """End-to-end: a node recorded by the REAL CommitGate policy-edit path is
    recognized by the lint (the recorded key matches the read key).

    Closes the loop on CRITICAL 2: drives a real policy-edit commit through the
    gate, then asserts the lint does NOT flag that domain (the gate's recorded
    decision_basis carries op/domain/provenance_type and the lint reads
    decision_basis). An out-of-band domain in the same KB IS flagged.
    """
    import subprocess
    from gateway.commit_gate import AuthoredIntent, CommitGate
    from gateway.embedding_index import EmbeddingIndex
    from gateway.intent_queue import Intent, IntentQueue, compute_intent_id
    from gateway.lint import policy_provenance

    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    monkeypatch.setenv("GATEWAY_DEV_SKIP_POLICY_GATES", "1")  # no corpus in unit env

    def _git(*args):
        subprocess.run(["git", "-C", str(tmp_path), *args], check=True, capture_output=True)

    _git("init", "-q")
    _git("config", "user.email", "test@test")
    _git("config", "user.name", "test")
    (tmp_path / ".gitignore").write_text(".knowledge/\n.index/\n")
    (tmp_path / "README.md").write_text("seed\n")
    _git("add", "README.md", ".gitignore")
    _git("commit", "-qm", "seed")

    # Domain "gated": will receive a real gate-recorded policy-edit.
    _write_policy(tmp_path, "gated", {"domain": {"slug": "gated"}, "version": 1})
    # Domain "oob": out-of-band — policy.yaml exists, no provenance node.
    _write_policy(tmp_path, "oob", {"domain": {"slug": "oob"}, "version": 1})
    (tmp_path / ".knowledge" / "eval" / "dedup").mkdir(parents=True, exist_ok=True)

    q = IntentQueue()
    gate = CommitGate(queue=q, embedding_index=EmbeddingIndex())

    new_policy = {"domain": {"slug": "gated"}, "filter": {"threshold_include": 0.8}, "version": 2}
    payload = {
        "op": "policy-edit", "domain": "gated", "policy_data": new_policy,
        "reason": "gated edit", "policy_version": 2,
    }
    identity = {"agent": "librarian-admin", "role": "policy-admin"}
    iid = compute_intent_id(payload, identity, semantics="policy-edit-gated")
    intent = Intent(intent_id=iid, payload=payload, identity=identity, head_oid="HEAD")
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")
    authored = AuthoredIntent(intent=intent, writes={}, base_oid="HEAD")

    result = gate.commit(authored, fencing_token=q.fencing_token(iid))
    assert result.disposition == "committed", f"gate commit failed: {result.summary}"

    findings = policy_provenance.run(root=tmp_path)
    flagged = {f.metadata.get("domain") for f in findings if f.check == "policy-provenance"}
    assert "gated" not in flagged, (
        f"gate-recorded domain must NOT be flagged; flagged={flagged}"
    )
    assert "oob" in flagged, f"out-of-band domain must be flagged; flagged={flagged}"
