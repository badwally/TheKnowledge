"""Integration — governance flow: policy-edit intent via gate → eval + merge-map gate →
dead-letters on a regressing policy, commits on a benign one.

Drives the REAL CommitGate._apply_policy_edit() path end-to-end:
  policy_edit() (ops/policy_edit.py) → IntentQueue.submit() →
  CommitGate.commit() → eval-retrieval gate → merge-map golden gate →
  dead-letter (regressing) OR commit (benign).

No monkeypatching of the core gate path. The real policy_data is evaluated
by the gate against the real dedup golden — not a hardcoded string match.

Named negative controls (brief Step 4 / hunt #5):
  - The regressing policy (wide blocking_band that merges distinct pairs) goes to
    dead-letter. The gate must evaluate the PROPOSED dedup params, not a string.
  - The benign policy (filter threshold adjustment, no dedup change) commits.

GATEWAY_DEV_SKIP_POLICY_GATES=1 is set so the retrieval-golden gate is bypassed
in the unit environment (no FTS index), while the merge-map golden gate RUNS
for real (the golden is seeded from the production .knowledge/eval/dedup/golden.yaml).
This mirrors the pattern in test_policy_change_control.py:tmp_gate_env.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

from gateway.commit_gate import AuthoredIntent, CommitGate
from gateway.embedding_index import EmbeddingIndex
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id
from gateway.ops.policy_edit import policy_edit


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _git(root, *args, check=True):
    return subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True, text=True, check=check
    )


# The real dedup golden lives here in production; the gate tests seed it into tmp.
_REAL_GOLDEN = (
    Path(__file__).parent.parent.parent
    / ".knowledge" / "eval" / "dedup" / "golden.yaml"
)

# The real gitignore for gateway-level tests: .knowledge/policies/ is git-TRACKED.
# A blanket ".knowledge/" would mask BLOCKER 1 (policy writes must be committed).
_REAL_GITIGNORE = (
    ".index/\n"
    ".knowledge/locks/\n"
    ".knowledge/lint/\n"
    ".knowledge/watcher.*\n"
    ".knowledge/scheduler.*\n"
    ".knowledge/auth.yaml\n"
    ".knowledge/secrets.env\n"
    ".knowledge/demand/\n"
    ".knowledge/transcripts/\n"
    ".knowledge/intents/\n"
    ".knowledge/provenance/\n"
    ".knowledge/fencing/\n"
)

_ALLOWLISTED_PRINCIPAL = "librarian-admin:policy-admin"


# ---------------------------------------------------------------------------
# Fixture: full gate environment with seeded policy + dedup golden
# ---------------------------------------------------------------------------


@pytest.fixture
def gate_env(tmp_path, monkeypatch):
    """Real git repo + CommitGate + live domain + seeded dedup golden.

    GATEWAY_DEV_SKIP_POLICY_GATES=1: skips the retrieval-golden gate in unit
    environment (no FTS index); the merge-map golden gate runs for real.
    GATEWAY_POLICY_PRINCIPAL: allowlisted so policy_edit() enqueues.
    """
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    monkeypatch.setenv("GATEWAY_DEV_SKIP_POLICY_GATES", "1")
    monkeypatch.setenv("GATEWAY_POLICY_PRINCIPAL", _ALLOWLISTED_PRINCIPAL)

    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "test@test")
    _git(tmp_path, "config", "user.name", "test")
    (tmp_path / ".gitignore").write_text(_REAL_GITIGNORE)
    (tmp_path / "README.md").write_text("seed\n")
    _git(tmp_path, "add", "README.md", ".gitignore")
    _git(tmp_path, "commit", "-qm", "seed")

    # Seed a live domain policy — committed (tracks production: .knowledge/policies/ is tracked)
    dom_dir = tmp_path / ".knowledge" / "policies" / "med"
    dom_dir.mkdir(parents=True)
    policy_path = dom_dir / "policy.yaml"
    initial_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.7, "threshold_exclude": 0.3},
        "version": 1,
    }
    policy_path.write_text(yaml.dump(initial_policy))

    # Copy the real dedup golden into the tmp env so the merge-map gate runs.
    golden_dir = tmp_path / ".knowledge" / "eval" / "dedup"
    golden_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(_REAL_GOLDEN, golden_dir / "golden.yaml")

    _git(tmp_path, "add", "--",
         ".knowledge/policies/med/policy.yaml",
         ".knowledge/eval/dedup/golden.yaml")
    _git(tmp_path, "commit", "-qm", "seed policy + golden")

    q = IntentQueue()
    idx = EmbeddingIndex()
    gate = CommitGate(queue=q, embedding_index=idx)
    return gate, q, tmp_path, policy_path, initial_policy


# ---------------------------------------------------------------------------
# Helper: build a policy-edit AuthoredIntent directly (for full gate control)
# Mirrors _make_policy_edit_authored_intent in test_policy_change_control.py.
# ---------------------------------------------------------------------------


def _make_policy_edit_intent(gate, q, domain: str, policy_data: dict, reason: str):
    """Craft an AuthoredIntent for a policy-edit without going through policy_edit().

    Full control over policy_data lets us construct genuinely-regressing and
    genuinely-benign policies. The gate reads domain + policy_data from the
    payload — the real proposed policy, not a string match (hunt #5).
    """
    payload = {
        "op": "policy-edit",
        "domain": domain,
        "policy_data": policy_data,
        "reason": reason,
        "policy_version": int(policy_data.get("version", 1)),
    }
    identity = {"agent": "librarian-admin", "role": "policy-admin"}
    iid = compute_intent_id(payload, identity, semantics=f"policy-edit:{domain}:{reason}")
    intent = Intent(intent_id=iid, payload=payload, identity=identity, head_oid="HEAD")
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")

    # Empty writes: the gate reads domain + policy_data from the payload and
    # constructs the write itself inside _apply_policy_edit.
    authored = AuthoredIntent(
        intent=intent,
        writes={},
        base_oid="HEAD",
        decision_basis={"policy_edit": True, "reason": reason},
    )
    return authored, iid


# ---------------------------------------------------------------------------
# Test A: regressing policy → dead-letter (the gate must evaluate the REAL policy)
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_governance_regressing_policy_dead_lettered(gate_env):
    """A policy with wide blocking_band that merges distinct pairs is dead-lettered.

    The gate evaluates the PROPOSED dedup params (blocking_band=0.99) against the
    golden — this causes genuine merge-map precision regression (distinct pairs are
    incorrectly merged). The policy file is NOT written.

    This test goes RED if:
      - The gate uses a hardcoded string match instead of evaluating the real policy
        (hunt #5). A policy without "geometry-only" in the name would sail through.
      - The merge-map gate is bypassed or skipped.
      - The gate commits a regressing policy.
    """
    gate, q, root, policy_path, initial_policy = gate_env

    # Genuinely regressing: wide blocking_band + identity_threshold forces near-everything
    # to merge. No hardcoded "geometry-only" string — tests that the gate evaluates params.
    regressing_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.7, "threshold_exclude": 0.3},
        "dedup": {
            "strategy": "loose-merge-all",
            "blocking_band": 0.99,
            "identity_threshold": 0.99,
        },
        "version": 2,
    }
    authored, iid = _make_policy_edit_intent(
        gate, q, "med", regressing_policy, "loosen dedup to near-everything-merges"
    )

    token = q.fencing_token(iid)
    result = gate.commit(authored, fencing_token=token)

    assert result.disposition == "dead_lettered", (
        f"regressing policy must be dead-lettered; got {result.disposition}\n"
        f"summary={result.summary}\nerrors={result.errors}"
    )
    assert any("regress" in e.lower() or "precision" in e.lower() for e in result.errors), (
        f"dead-letter error must name the merge-precision regression; got {result.errors}"
    )
    # Policy file must NOT have been changed
    on_disk = yaml.safe_load(policy_path.read_text())
    assert on_disk == initial_policy, (
        f"policy mutated despite dead-lettering a regressing edit; on_disk={on_disk}"
    )


@pytest.mark.integration
def test_governance_regressing_policy_queue_state_is_dead_lettered(gate_env):
    """Queue state reflects dead-letter after a regressing policy is rejected.

    Verifies the gate transitions the intent to dead_lettered in the queue,
    not just returns a dead_lettered OperationResult.
    """
    gate, q, root, policy_path, initial_policy = gate_env

    regressing_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.7},
        "dedup": {
            "blocking_band": 0.98,
            "identity_threshold": 0.98,
        },
        "version": 2,
    }
    authored, iid = _make_policy_edit_intent(
        gate, q, "med", regressing_policy, "regressing-queue-state-check"
    )

    token = q.fencing_token(iid)
    gate.commit(authored, fencing_token=token)

    state = q.get_state(iid)
    assert state == "dead_lettered", (
        f"intent queue state must be dead_lettered after regressing policy; got {state}"
    )


# ---------------------------------------------------------------------------
# Test B: benign policy → commits (negative control of the negative control)
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_governance_benign_policy_commits(gate_env):
    """A benign edit that passes both gates is committed and the policy IS updated.

    This is the negative control of the negative control: if the gate dead-lettered
    ALL policy edits, this test would catch it (and reveal that the guard is broken).

    The benign policy only adjusts the filter threshold (no dedup change) so it
    cannot regress the merge-map golden. The gate evaluates the real policy data
    via _derive_dedup_params and finds no regression.

    This test goes RED if:
      - The gate dead-letters even benign edits (over-aggressive gate).
      - The policy file is not updated after a passing gate.
      - The commit is not durable (no Intent-Id trailer in git log).
    """
    gate, q, root, policy_path, initial_policy = gate_env

    benign_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.75, "threshold_exclude": 0.35},
        # No dedup block → gate uses DEFAULT_BLOCKING_BAND / DEFAULT_IDENTITY_THRESHOLD
        # which are the production baseline → no regression.
        "version": 2,
    }
    authored, iid = _make_policy_edit_intent(
        gate, q, "med", benign_policy, "raise filter threshold slightly"
    )

    token = q.fencing_token(iid)
    result = gate.commit(authored, fencing_token=token)

    assert result.disposition == "committed", (
        f"benign policy must commit; got {result.disposition}\n"
        f"summary={result.summary}\nerrors={result.errors}"
    )
    # Policy file MUST have been updated
    on_disk = yaml.safe_load(policy_path.read_text())
    assert on_disk == benign_policy, (
        f"policy file not updated after benign commit; on_disk={on_disk}"
    )


@pytest.mark.integration
def test_governance_benign_commit_is_durable_in_git(gate_env):
    """A successful benign policy-edit creates a git commit with Intent-Id trailer.

    Verifies the commit goes through the gate's atomic boundary (_commit_reversal_writes)
    so the policy change is durable and carries a commit-level audit trail.

    This test goes RED if the gate writes the file directly (bare write_text) without
    going through git commit — the file would be present but not in git history
    (and would be silently reverted by a git checkout / recover()).
    """
    gate, q, root, policy_path, initial_policy = gate_env

    benign_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.72, "threshold_exclude": 0.3},
        "version": 2,
    }
    authored, iid = _make_policy_edit_intent(
        gate, q, "med", benign_policy, "durable commit verification"
    )

    token = q.fencing_token(iid)
    result = gate.commit(authored, fencing_token=token)

    assert result.disposition == "committed", (
        f"expected committed; got {result.disposition} ({result.summary})"
    )

    # The git log must carry the Intent-Id trailer for this intent
    log_out = _git(root, "log", "--format=%H%n%B", "-n", "5").stdout
    assert f"Intent-Id: {iid}" in log_out, (
        f"no commit carries Intent-Id trailer for {iid}; recent log:\n{log_out}"
    )

    # `git status` must be clean — no dangling uncommitted policy change
    status_out = _git(root, "status", "--porcelain").stdout
    assert not status_out.strip(), (
        f"git status not clean after benign policy commit; status:\n{status_out}"
    )


# ---------------------------------------------------------------------------
# Test C: policy_edit() → full end-to-end via queue → gate (drive BOTH branches
# using the real enqueue path, not the AuthoredIntent shortcut)
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_governance_full_flow_via_policy_edit_enqueue_then_gate_commit(gate_env):
    """Full end-to-end: policy_edit() enqueues → claim → gate.commit() commits.

    Policy-edit intents are NOT routed through drain_once/run_worker. The production
    flow is:
      policy_edit() → q.submit()                  (enqueue as privileged intent)
      claim = q.claim()                            (acquire by the committer or CLI)
      gate.commit(authored, token) with op=policy-edit payload
        → _apply_policy_edit() (dual-gate) → commit or dead-letter.

    drain_once() dead-letters policy-edit intents because author_deposit() cannot
    render them (no page_type/title). That dead-letter behavior is correct and
    intentional — policy-edit is a separate privileged path.

    This test drives the REAL enqueue path via policy_edit() and then verifies the
    claim → gate.commit() path commits successfully for a benign policy.

    This test goes RED if:
      - policy_edit() fails to enqueue the intent.
      - gate.commit() does not recognize the policy-edit op (dispatch miss).
      - The gate dead-letters a benign policy driven by the real enqueue path.
    """
    gate, q, root, policy_path, initial_policy = gate_env

    # Enqueue via the real policy_edit() op (uses server-sourced principal from env)
    benign_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.73, "threshold_exclude": 0.3},
        "version": 2,
    }
    enqueue_result = policy_edit(
        "med",
        benign_policy,
        reason="end-to-end gate commit test",
        queue=q,
    )
    assert enqueue_result.success, (
        f"policy_edit enqueue failed: {enqueue_result.errors}"
    )
    assert enqueue_result.disposition == "queued"
    iid = enqueue_result.intent_id

    # Claim the intent (as a committer would), then build an AuthoredIntent and commit.
    # The gate's policy-edit dispatch reads domain + policy_data from the PAYLOAD,
    # so writes={} is correct — the gate builds its own write in _apply_policy_edit.
    claim = q.claim(now=1.0)
    assert claim is not None, "could not claim enqueued policy-edit intent"
    q.set_state(iid, "authored")

    intent = claim.intent
    authored = AuthoredIntent(
        intent=intent,
        writes={},
        base_oid="HEAD",
        decision_basis={"policy_edit": True},
    )
    result = gate.commit(authored, fencing_token=claim.fencing_token)

    assert result.disposition == "committed", (
        f"end-to-end benign policy gate commit: {result.disposition}\n"
        f"summary={result.summary}\nerrors={result.errors}"
    )

    # Policy must be on disk with the new values
    on_disk = yaml.safe_load(policy_path.read_text())
    assert on_disk == benign_policy, (
        f"policy not updated after full gate commit; on_disk={on_disk}"
    )
