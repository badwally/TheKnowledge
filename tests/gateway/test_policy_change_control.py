"""G7 — privileged-intent policy-edit path + CommitGate gate tests.

Tests:
1. Allowlisted identity enqueues a policy-edit intent (disposition="queued").
2. Non-allowlisted identity is rejected (disposition="rejected", error mentions
   allowlist/privilege).
3. CommitGate gate: a policy-edit intent that would regress the merge-map golden
   is dead-lettered and the policy file is NOT changed (crux test — no monkeypatch
   of the gate or adjudicator).
4. CommitGate gate: a benign edit that holds both gates commits and the policy IS
   updated (negative control of the negative control).
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest
import yaml

from gateway.ops.policy_edit import policy_edit
from gateway.intent_queue import IntentQueue


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def tmp_queue_env(tmp_path, monkeypatch):
    """Minimal queue environment — just needs KNOWLEDGE_ROOT + .knowledge dir."""
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    (tmp_path / ".knowledge").mkdir(parents=True, exist_ok=True)
    return tmp_path


@pytest.fixture()
def tmp_gate_env(tmp_path, monkeypatch):
    """Full gate environment: real git repo + IntentQueue + CommitGate + live domain.

    Seeds the dedup golden so the merge-map gate runs in the test environment.
    """
    import shutil
    from gateway.commit_gate import CommitGate
    from gateway.embedding_index import EmbeddingIndex

    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))

    def _git(*args):
        subprocess.run(
            ["git", "-C", str(tmp_path), *args],
            check=True, capture_output=True,
        )

    _git("init", "-q")
    _git("config", "user.email", "test@test")
    _git("config", "user.name", "test")
    (tmp_path / ".gitignore").write_text(".knowledge/\n.index/\n")
    (tmp_path / "README.md").write_text("seed\n")
    _git("add", "README.md", ".gitignore")
    _git("commit", "-qm", "seed")

    # Seed a live domain with a policy file so the gate can find it.
    dom_dir = tmp_path / ".knowledge" / "policies" / "med"
    dom_dir.mkdir(parents=True)
    policy_path = dom_dir / "policy.yaml"
    initial_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.7, "threshold_exclude": 0.3},
        "version": 1,
    }
    policy_path.write_text(yaml.dump(initial_policy))

    # Copy the real dedup golden so the merge-map gate runs in the tmp env.
    real_golden = (
        Path(__file__).parent.parent.parent
        / ".knowledge/eval/dedup/golden.yaml"
    )
    golden_dir = tmp_path / ".knowledge" / "eval" / "dedup"
    golden_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(real_golden, golden_dir / "golden.yaml")

    q = IntentQueue()
    idx = EmbeddingIndex()
    gate = CommitGate(queue=q, embedding_index=idx)
    return gate, q, tmp_path, policy_path, initial_policy


# ---------------------------------------------------------------------------
# G7 Step 5 — allowlist + enqueue tests
# ---------------------------------------------------------------------------

def test_allowlisted_identity_enqueues_policy_edit(tmp_queue_env):
    res = policy_edit(
        "med",
        {"domain": {"slug": "med"}, "filter": {"threshold_include": 0.7}},
        identity={"agent": "librarian-admin", "role": "policy-admin"},
        reason="raise threshold",
    )
    assert res.success and res.disposition == "queued", (
        f"expected success+queued; got {res.disposition}, errors={res.errors}"
    )


def test_non_allowlisted_identity_rejected(tmp_queue_env):
    res = policy_edit(
        "med",
        {"domain": {"slug": "med"}},
        identity={"agent": "random-worker"},
        reason="x",
    )
    assert res.disposition == "rejected", f"expected rejected; got {res.disposition}"
    assert any("allowlist" in e or "privileg" in e for e in res.errors), (
        f"error must mention allowlist/privilege: {res.errors}"
    )


def test_policy_edit_enqueued_intent_has_policy_edit_op(tmp_queue_env):
    """Payload op must be 'policy-edit' so the CommitGate dispatch recognises it."""
    res = policy_edit(
        "med",
        {"domain": {"slug": "med"}, "filter": {"threshold_include": 0.7}},
        identity={"agent": "librarian-admin", "role": "policy-admin"},
        reason="test intent payload",
    )
    assert res.success
    q = IntentQueue()
    # Read the intent off disk (returns (state, record) or None)
    read = q._read(res.intent_id)
    assert read is not None, "intent not found in queue"
    _state, record = read
    payload = record.get("payload") or {}
    assert payload.get("op") == "policy-edit", f"wrong op in payload: {payload}"
    assert payload.get("domain") == "med"
    assert "policy_data" in payload
    assert "reason" in payload
    assert "policy_version" in payload


def test_policy_edit_missing_reason_rejected(tmp_queue_env):
    """Missing reason is rejected (reason documents the change motivation)."""
    res = policy_edit(
        "med",
        {"domain": {"slug": "med"}},
        identity={"agent": "librarian-admin", "role": "policy-admin"},
        reason="",
    )
    assert res.disposition == "rejected"


def test_policy_edit_empty_policy_data_rejected(tmp_queue_env):
    """Empty or None policy_data is rejected (nothing to write)."""
    res = policy_edit(
        "med",
        {},
        identity={"agent": "librarian-admin", "role": "policy-admin"},
        reason="valid reason",
    )
    assert res.disposition == "rejected"


# ---------------------------------------------------------------------------
# G7 Step 9 — CommitGate gate tests (through the REAL gate, no monkeypatch)
# ---------------------------------------------------------------------------

def _make_policy_edit_authored_intent(gate, q, domain: str, policy_data: dict,
                                       reason: str, policy_path: Path):
    """Build an AuthoredIntent for a policy-edit without going through policy_edit().

    The gate tests need full control of what's in the policy write to force a
    regression scenario, so we craft the AuthoredIntent directly.

    Policy files live under .knowledge/ (gitignored). The gate's policy-edit
    branch writes them directly (not via git add), so we pass an EMPTY writes
    dict — the gate builds its own write in _apply_policy_edit from the payload.
    """
    from gateway.commit_gate import AuthoredIntent
    from gateway.intent_queue import Intent, compute_intent_id

    payload = {
        "op": "policy-edit",
        "domain": domain,
        "policy_data": policy_data,
        "reason": reason,
        "policy_version": int(policy_data.get("version", 1)),
    }
    identity = {"agent": "librarian-admin", "role": "policy-admin"}
    iid = compute_intent_id(payload, identity, semantics=f"policy-edit-{reason}")
    intent = Intent(intent_id=iid, payload=payload, identity=identity, head_oid="HEAD")
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")

    # Empty writes: the policy-edit gate branch reads the domain + policy_data
    # from the payload and writes to .knowledge/ directly (gitignored path).
    return AuthoredIntent(
        intent=intent,
        writes={},
        base_oid="HEAD",
        decision_basis={"policy_edit": True, "reason": reason},
    ), iid


def test_gate_dead_letters_regressing_policy_edit(tmp_gate_env):
    """An edit that makes the adjudicator regress the merge-map golden is dead-lettered.

    We inject a policy_data that carries a broken 'dedup' sub-key that the gate
    can detect as forcing a geometry-only merge strategy (nn_distance_threshold
    set to 0.5, which would merge type1-vs-type2-distinct incorrectly).

    The gate runs merge_map_eval BEFORE writing the policy; on regression it
    dead-letters and leaves the policy file UNCHANGED.
    """
    gate, q, root, policy_path, initial_policy = tmp_gate_env

    # A "regressing" policy_data: sets dedup.strategy = "geometry-only" which
    # the gate must detect as forcing regression of the merge-map golden.
    regressing_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.7},
        "dedup": {"strategy": "geometry-only", "nn_distance_threshold": 0.5},
        "version": 2,
    }
    authored, iid = _make_policy_edit_authored_intent(
        gate, q, "med", regressing_policy, "switch to geometry-only dedup", policy_path
    )

    token = q.fencing_token(iid)
    result = gate.commit(authored, fencing_token=token)

    assert result.disposition == "dead_lettered", (
        f"expected dead_lettered; got {result.disposition}\n"
        f"summary={result.summary}\nerrors={result.errors}"
    )
    # Policy file must NOT have been changed
    on_disk = yaml.safe_load(policy_path.read_text())
    assert on_disk == initial_policy, (
        "policy file was mutated despite dead-lettering"
    )


def test_gate_commits_benign_policy_edit(tmp_gate_env):
    """A benign edit that holds both gates commits and the policy IS updated.

    This is the negative control of the negative control: if the gate dead-lettered
    ALL policy edits, this test would catch it.
    """
    gate, q, root, policy_path, initial_policy = tmp_gate_env

    benign_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.75, "threshold_exclude": 0.3},
        "version": 2,
    }
    authored, iid = _make_policy_edit_authored_intent(
        gate, q, "med", benign_policy, "raise threshold slightly", policy_path
    )

    token = q.fencing_token(iid)
    result = gate.commit(authored, fencing_token=token)

    assert result.disposition == "committed", (
        f"expected committed; got {result.disposition}\n"
        f"summary={result.summary}\nerrors={result.errors}"
    )
    # Policy file MUST have been updated
    on_disk = yaml.safe_load(policy_path.read_text())
    assert on_disk == benign_policy, (
        f"policy file not updated after benign commit; got {on_disk}"
    )
