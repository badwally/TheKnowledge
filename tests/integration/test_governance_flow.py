"""Integration — governance flow: policy-edit intent via production committer → eval + merge-map gate →
dead-letters on a regressing policy, commits on a benign one.

Drives the REAL production path end-to-end (C1 fix, post-T2 D0 reopen):
  policy_edit() (ops/policy_edit.py) → IntentQueue.submit() →
  run_worker/drain_once (ops/committer.py) → CommitGate.commit() →
  _apply_policy_edit() → eval-retrieval gate → merge-map golden gate →
  dead-letter (regressing) OR commit (benign).

Tests A and B drive the path via run_worker(once=True) — the real production
committer — NOT via a direct gate.commit() call.  gate.commit()-direct tests
for _apply_policy_edit() gate-unit coverage are in test_policy_change_control.py.

Named negative controls (brief Step 4 / hunt #5):
  - The regressing policy (wide blocking_band that merges distinct pairs) goes to
    dead-letter via the gate's merge-map gate. The committer routes it there (not
    author_deposit) — the dead-letter reason names the precision regression.
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
from gateway.ops.committer import run_worker
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
# Test A: regressing policy → dead-lettered BY THE GATE via run_worker
# (the production committer routes the intent, not dead-letters in author_deposit)
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_governance_regressing_policy_dead_lettered(gate_env):
    """A policy with wide blocking_band that merges distinct pairs is dead-lettered
    by the gate's merge-map golden gate, via the REAL production committer path.

    Production path: policy_edit() → q.submit() → run_worker (drain_once routes to
    gate.commit()) → _apply_policy_edit() → merge-map golden gate → dead-letter.

    The gate evaluates the PROPOSED dedup params (blocking_band=0.99) against the
    golden — genuine merge-map precision regression. The policy file is NOT written.

    This test goes RED if:
      - The committer dead-letters in author_deposit (wrong routing — not gate path).
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
    enqueue_result = policy_edit(
        "med", regressing_policy,
        reason="loosen dedup to near-everything-merges",
        queue=q,
    )
    assert enqueue_result.success, f"policy_edit enqueue failed: {enqueue_result.errors}"
    iid = enqueue_result.intent_id

    # Drive via the REAL production committer: run_worker(once=True) routes the
    # policy-edit intent to gate.commit() → _apply_policy_edit() → dead-letter.
    run_worker(once=True, queue=q, gate=gate)

    state = q.get_state(iid)
    assert state == "dead_lettered", (
        f"regressing policy must be dead_lettered; queue state={state!r}"
    )
    result_meta = q.get_result(iid) or {}
    reason = result_meta.get("reason", "")
    # The dead-letter reason must come from the gate's merge-map gate, not author_deposit.
    assert "page_type" not in reason.lower(), (
        f"dead-letter came from author_deposit path (page_type error): {reason!r}"
    )
    assert any(
        kw in reason.lower() for kw in ("regress", "precision", "merge-map", "policy")
    ), f"dead-letter reason must name a policy gate failure; got: {reason!r}"

    # Policy file must NOT have been changed
    on_disk = yaml.safe_load(policy_path.read_text())
    assert on_disk == initial_policy, (
        f"policy mutated despite dead-lettering a regressing edit; on_disk={on_disk}"
    )


# ---------------------------------------------------------------------------
# Test B: benign policy → committed via run_worker (negative control of negative control)
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_governance_benign_policy_commits(gate_env):
    """A benign policy-edit intent routed through run_worker is committed by the gate.

    Production path: policy_edit() → q.submit() → run_worker → _apply_policy_edit() → committed.

    The benign policy only adjusts the filter threshold (no dedup change) so it
    cannot regress the merge-map golden. The gate evaluates the real policy data
    via _derive_dedup_params and finds no regression.

    This test goes RED if:
      - The committer dead-letters in author_deposit (wrong routing).
      - The gate dead-letters even benign edits (over-aggressive gate).
      - The policy file is not updated after a passing gate.
    """
    gate, q, root, policy_path, initial_policy = gate_env

    benign_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.75, "threshold_exclude": 0.35},
        # No dedup block → gate uses DEFAULT_BLOCKING_BAND / DEFAULT_IDENTITY_THRESHOLD
        # which are the production baseline → no regression.
        "version": 2,
    }
    enqueue_result = policy_edit(
        "med", benign_policy,
        reason="raise filter threshold slightly",
        queue=q,
    )
    assert enqueue_result.success, f"policy_edit enqueue failed: {enqueue_result.errors}"
    iid = enqueue_result.intent_id

    # Drive via the REAL production committer
    run_worker(once=True, queue=q, gate=gate)

    state = q.get_state(iid)
    assert state == "committed", (
        f"benign policy must be committed via run_worker; queue state={state!r}"
    )
    # Policy file MUST have been updated on disk
    on_disk = yaml.safe_load(policy_path.read_text())
    assert on_disk == benign_policy, (
        f"policy file not updated after benign commit; on_disk={on_disk}"
    )


@pytest.mark.integration
def test_governance_benign_commit_is_durable_in_git(gate_env):
    """A benign policy-edit via run_worker creates a git commit with Intent-Id trailer.

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
    enqueue_result = policy_edit(
        "med", benign_policy,
        reason="durable commit verification",
        queue=q,
    )
    assert enqueue_result.success, f"policy_edit enqueue failed: {enqueue_result.errors}"
    iid = enqueue_result.intent_id

    run_worker(once=True, queue=q, gate=gate)

    state = q.get_state(iid)
    assert state == "committed", (
        f"expected committed via run_worker; queue state={state!r}"
    )

    # The git log must carry the Intent-Id trailer for this intent
    log_out = _git(root, "log", "--format=%H%n%B", "-n", "5").stdout
    assert f"Intent-Id: {iid}" in log_out, (
        f"no commit carries Intent-Id trailer for {iid}; recent log:\n{log_out}"
    )

    # `git status` must be clean — no dangling uncommitted policy change
    status_out = _git(root, "status", "--porcelain").stdout
    assert not status_out.strip(), (
        f"git status not clean after benign policy commit via run_worker; status:\n{status_out}"
    )


# ---------------------------------------------------------------------------
# Test C: full end-to-end via policy_edit() enqueue → run_worker (real operator path)
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_governance_full_flow_via_policy_edit_enqueue_then_run_worker(gate_env):
    """Full operator path: policy_edit() enqueues → run_worker drains → commits.

    This is the REAL production path an operator triggers:
      wiki policy-edit → policy_edit() → q.submit() → (wiki commit-worker)
      → run_worker → drain_once → [policy-edit routing] → gate.commit()
      → _apply_policy_edit() → commit (benign) or dead-letter (regressing).

    This test goes RED if:
      - policy_edit() fails to enqueue.
      - run_worker fails to route the policy-edit intent to the gate (routes to
        author_deposit instead → dead-letter on page_type error).
      - gate.commit() does not recognize the policy-edit op (dispatch miss).
      - The gate dead-letters a benign policy driven by the real enqueue path.
    """
    gate, q, root, policy_path, initial_policy = gate_env

    benign_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.73, "threshold_exclude": 0.3},
        "version": 2,
    }
    enqueue_result = policy_edit(
        "med",
        benign_policy,
        reason="full operator-path test",
        queue=q,
    )
    assert enqueue_result.success, f"policy_edit enqueue failed: {enqueue_result.errors}"
    assert enqueue_result.disposition == "queued"
    iid = enqueue_result.intent_id

    # Real production committer path — no manual claim or AuthoredIntent construction
    run_worker(once=True, queue=q, gate=gate)

    state = q.get_state(iid)
    assert state == "committed", (
        f"full operator path: policy must be committed via run_worker; state={state!r}"
    )

    # Policy must be on disk with the new values
    on_disk = yaml.safe_load(policy_path.read_text())
    assert on_disk == benign_policy, (
        f"policy not updated after full operator-path commit; on_disk={on_disk}"
    )
