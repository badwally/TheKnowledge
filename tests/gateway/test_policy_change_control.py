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
    # Dev-skip the retrieval gate's MISSING-GOLDEN case only — a unit env has no
    # indexed corpus to score. This does NOT bypass a real regression or an
    # eval exception (both still fail closed); the merge-map golden IS seeded
    # below and runs for real.
    monkeypatch.setenv("GATEWAY_DEV_SKIP_POLICY_GATES", "1")

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
# MINOR — «policy-version provenance»: version-conflict guard + monotone bump
# ---------------------------------------------------------------------------

def _seed_on_disk_policy(root, domain, version):
    pol_dir = root / ".knowledge" / "policies" / domain
    pol_dir.mkdir(parents=True, exist_ok=True)
    (pol_dir / "policy.yaml").write_text(
        yaml.dump({"domain": {"slug": domain}, "version": version})
    )


def test_policy_edit_rejects_stale_version(tmp_queue_env):
    """A proposed version not greater than the on-disk version is rejected."""
    _seed_on_disk_policy(tmp_queue_env, "med", 5)
    res = policy_edit(
        "med",
        {"domain": {"slug": "med"}, "filter": {"threshold_include": 0.7}, "version": 5},
        identity={"agent": "librarian-admin", "role": "policy-admin"},
        reason="stale edit (same version)",
    )
    assert res.disposition == "rejected", f"stale version must reject; got {res.disposition}"
    assert any("version" in e.lower() and "conflict" in e.lower() for e in res.errors), (
        f"error must name the version conflict; got {res.errors}"
    )


def test_policy_edit_rejects_lower_version(tmp_queue_env):
    """A proposed version below the on-disk version is rejected."""
    _seed_on_disk_policy(tmp_queue_env, "med", 5)
    res = policy_edit(
        "med",
        {"domain": {"slug": "med"}, "version": 3},
        identity={"agent": "librarian-admin", "role": "policy-admin"},
        reason="downgrade attempt",
    )
    assert res.disposition == "rejected"


def test_policy_edit_accepts_greater_version(tmp_queue_env):
    """A proposed version strictly greater than on-disk is accepted + carried."""
    _seed_on_disk_policy(tmp_queue_env, "med", 5)
    res = policy_edit(
        "med",
        {"domain": {"slug": "med"}, "version": 6},
        identity={"agent": "librarian-admin", "role": "policy-admin"},
        reason="legit bump",
    )
    assert res.disposition == "queued", f"greater version must queue; got {res.disposition}"
    read = IntentQueue()._read(res.intent_id)
    assert read is not None
    assert read[1]["payload"]["policy_version"] == 6


def test_policy_edit_auto_bumps_missing_version(tmp_queue_env):
    """An edit omitting version auto-bumps to on-disk + 1 (monotone)."""
    _seed_on_disk_policy(tmp_queue_env, "med", 5)
    res = policy_edit(
        "med",
        {"domain": {"slug": "med"}, "filter": {"threshold_include": 0.8}},
        identity={"agent": "librarian-admin", "role": "policy-admin"},
        reason="auto-bump",
    )
    assert res.disposition == "queued"
    read = IntentQueue()._read(res.intent_id)
    assert read is not None
    payload = read[1]["payload"]
    assert payload["policy_version"] == 6, f"expected auto-bump to 6; got {payload['policy_version']}"
    assert payload["policy_data"]["version"] == 6, "policy_data must carry the bumped version"


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


def test_gate_dead_letters_disguised_regressing_policy(tmp_gate_env):
    """CRITICAL 1: a corpus-corrupting policy NOT named 'geometry-only' is dead-lettered.

    The original gate only dead-lettered a hardcoded string match
    (dedup.strategy == "geometry-only"). A genuinely corpus-corrupting policy
    expressed differently — loose strategy, near-1.0 nn threshold, dedup disabled
    — sailed through and was written to disk.

    The gate must DERIVE the dedup parameters from policy_data, simulate
    adjudication with THOSE params against the golden, and dead-letter on ANY
    merge-precision regression — for all strategies, not one string.

    This policy sets a wide blocking_band (0.99) so the lexical-fallback distances
    in the golden cause type1/type2 and Fed-branch DISTINCT pairs to be mis-merged.
    """
    gate, q, root, policy_path, initial_policy = tmp_gate_env

    disguised_regressing = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.7},
        # No literal "geometry-only" anywhere. A loose, near-everything-merges
        # config that corrupts identity.
        "dedup": {
            "strategy": "loose",
            "nn_distance_threshold": 0.99,
            "blocking_band": 0.99,
            "identity_threshold": 0.99,
            "enabled": False,
        },
        "version": 2,
    }
    authored, iid = _make_policy_edit_authored_intent(
        gate, q, "med", disguised_regressing, "loosen dedup (disguised)", policy_path
    )

    token = q.fencing_token(iid)
    result = gate.commit(authored, fencing_token=token)

    assert result.disposition == "dead_lettered", (
        f"disguised regressing policy must be dead-lettered; got {result.disposition}\n"
        f"summary={result.summary}\nerrors={result.errors}"
    )
    assert any("regress" in e.lower() or "precision" in e.lower() for e in result.errors), (
        f"dead-letter error must name the failing merge-precision metric; got {result.errors}"
    )
    # Policy file must NOT have been changed.
    on_disk = yaml.safe_load(policy_path.read_text())
    assert on_disk == initial_policy, "policy mutated despite dead-lettering a regressing edit"


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


# ---------------------------------------------------------------------------
# HIGH 1 — FAIL-CLOSED: a gate eval that raises must dead-letter (not skip)
# ---------------------------------------------------------------------------

def test_gate_fails_closed_when_eval_raises(tmp_gate_env, monkeypatch):
    """If a gate eval raises, the intent is dead-lettered and the policy is unchanged.

    Adversarial control for the fail-open vulnerability: previously the gate
    caught all exceptions and continued (log-and-skip), so a regressing edit
    sailed through whenever an eval threw. The gate must FAIL CLOSED — any
    gate-eval exception dead-letters the intent without writing the policy.

    We force the merge-map gate to raise by making merge_map_eval blow up.
    This is NOT a monkeypatch of the gate itself — it simulates a real
    downstream failure (corrupt golden, import error, etc.).
    """
    gate, q, root, policy_path, initial_policy = tmp_gate_env

    # Force merge_map_eval to raise — simulates a corrupt golden / runtime fault.
    import gateway.evaluate.merge_map_eval as mm_mod

    def _boom(*args, **kwargs):
        raise RuntimeError("simulated eval fault")

    monkeypatch.setattr(mm_mod, "merge_map_eval", _boom)

    benign_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.75},
        "version": 2,
    }
    authored, iid = _make_policy_edit_authored_intent(
        gate, q, "med", benign_policy, "edit during eval fault", policy_path
    )

    token = q.fencing_token(iid)
    result = gate.commit(authored, fencing_token=token)

    assert result.disposition == "dead_lettered", (
        f"gate must fail CLOSED on eval exception; got {result.disposition}\n"
        f"summary={result.summary}\nerrors={result.errors}"
    )
    assert any("fail" in e.lower() and "clos" in e.lower() for e in result.errors), (
        f"dead-letter error must indicate failing closed; got {result.errors}"
    )
    # Policy file must NOT have been changed.
    on_disk = yaml.safe_load(policy_path.read_text())
    assert on_disk == initial_policy, "policy mutated despite fail-closed dead-letter"


def test_gate_dev_skip_env_marker_allows_missing_goldens(tmp_path, monkeypatch):
    """With the explicit dev-skip env marker, a missing golden is skipped (not dead-lettered).

    This proves the fail-closed default is bypassable ONLY via an explicit
    opt-in env marker — never a blanket catch-all. Without goldens AND with the
    marker set, a benign edit commits.
    """
    import subprocess
    from gateway.commit_gate import CommitGate
    from gateway.embedding_index import EmbeddingIndex

    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    monkeypatch.setenv("GATEWAY_DEV_SKIP_POLICY_GATES", "1")

    def _git(*args):
        subprocess.run(["git", "-C", str(tmp_path), *args], check=True, capture_output=True)

    _git("init", "-q")
    _git("config", "user.email", "test@test")
    _git("config", "user.name", "test")
    (tmp_path / ".gitignore").write_text(".knowledge/\n.index/\n")
    (tmp_path / "README.md").write_text("seed\n")
    _git("add", "README.md", ".gitignore")
    _git("commit", "-qm", "seed")

    dom_dir = tmp_path / ".knowledge" / "policies" / "med"
    dom_dir.mkdir(parents=True)
    policy_path = dom_dir / "policy.yaml"
    initial = {"domain": {"slug": "med"}, "version": 1}
    policy_path.write_text(yaml.dump(initial))
    # NOTE: no golden seeded — the dev-skip marker must allow this to pass.

    q = IntentQueue()
    gate = CommitGate(queue=q, embedding_index=EmbeddingIndex())

    benign = {"domain": {"slug": "med"}, "filter": {"threshold_include": 0.8}, "version": 2}
    authored, iid = _make_policy_edit_authored_intent(
        gate, q, "med", benign, "edit with dev-skip", policy_path
    )
    result = gate.commit(authored, fencing_token=q.fencing_token(iid))
    assert result.disposition == "committed", (
        f"dev-skip marker should allow commit with missing goldens; got "
        f"{result.disposition} ({result.summary})"
    )


# ---------------------------------------------------------------------------
# HIGH 2 — PATH TRAVERSAL on the domain slug
# ---------------------------------------------------------------------------

def test_policy_edit_rejects_traversal_domain(tmp_queue_env):
    """policy_edit() rejects a domain slug containing path-traversal sequences."""
    for evil in ("../escape", "../../etc/passwd", "med/../../../tmp/x"):
        res = policy_edit(
            evil,
            {"domain": {"slug": "x"}, "filter": {"threshold_include": 0.7}},
            identity={"agent": "librarian-admin", "role": "policy-admin"},
            reason="traversal attempt",
        )
        assert res.disposition == "rejected", (
            f"domain {evil!r} must be rejected at policy_edit(); got {res.disposition}"
        )
        assert any("slug" in e.lower() or "invalid" in e.lower() for e in res.errors), (
            f"error must name the invalid slug; got {res.errors}"
        )


def test_policy_edit_accepts_valid_slug(tmp_queue_env):
    """A valid slug still queues (negative control of the traversal rejection)."""
    res = policy_edit(
        "med",
        {"domain": {"slug": "med"}, "filter": {"threshold_include": 0.7}},
        identity={"agent": "librarian-admin", "role": "policy-admin"},
        reason="valid slug",
    )
    assert res.disposition == "queued", f"valid slug must queue; got {res.disposition}"


def test_gate_dead_letters_traversal_domain(tmp_gate_env):
    """The gate dead-letters a traversal domain and writes NO file outside policies root.

    Defense in depth: even if a traversal intent reaches the gate (bypassing
    the policy_edit() check), the gate must reject it. We snapshot the tree
    before + after to prove no file escaped the policies root.
    """
    gate, q, root, policy_path, initial_policy = tmp_gate_env

    # A sentinel path outside the policies root that traversal would target.
    escape_target = root / "ESCAPED.yaml"
    assert not escape_target.exists()

    evil_policy = {"domain": {"slug": "x"}, "filter": {"threshold_include": 0.7}, "version": 2}
    # Build the intent directly with a traversal domain (bypasses policy_edit()).
    authored, iid = _make_policy_edit_authored_intent(
        gate, q, "../ESCAPED", evil_policy, "traversal at gate", policy_path
    )

    token = q.fencing_token(iid)
    result = gate.commit(authored, fencing_token=token)

    assert result.disposition == "dead_lettered", (
        f"gate must dead-letter traversal domain; got {result.disposition}\n"
        f"summary={result.summary} errors={result.errors}"
    )
    # No file written outside the policies root.
    assert not escape_target.exists(), "traversal wrote a file outside the policies root!"
    assert not (root / "ESCAPED.yaml").exists()
    # The legit policy is untouched.
    on_disk = yaml.safe_load(policy_path.read_text())
    assert on_disk == initial_policy
