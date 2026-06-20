"""Integration — demand-loop flow: corpus-miss → record_gap × N → demand_cluster(trigger=True)
→ synthesis intent submitted → run_worker commits the canonicalization page.

Drives the REAL ops end-to-end:
  DemandLedger.record_gap() → DemandLedger.cluster() (via demand_cluster(trigger=True))
  → IntentQueue.submit() (inside cluster()) → run_worker (ops/committer.py)
  → CommitGate commits the synthesis page.

No monkeypatching of the core path. Only KNOWLEDGE_ROOT is redirected to a tmp git repo.

Named negative controls (brief Step 3):
  - A single non-recurring gap does NOT trigger (trigger-mass gate).
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from gateway.commit_gate import CommitGate
from gateway.demand_ledger import DemandLedger
from gateway.embedding_index import EmbeddingIndex, LexicalFallbackEncoder, thresholds
from gateway.intent_queue import IntentQueue
from gateway.ops.committer import run_worker
from gateway.ops.demand_cluster import demand_cluster


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _git(root, *args, check=True):
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=check
    )


def _submitted_ids(queue: IntentQueue) -> set[str]:
    """Return all intent IDs currently in the submitted state."""
    submitted_dir = queue._state_dir("submitted")
    if not submitted_dir.exists():
        return set()
    return {p.stem for p in submitted_dir.glob("*.json") if not p.name.startswith(".")}


# ---------------------------------------------------------------------------
# Fixture
# ---------------------------------------------------------------------------


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
    # Live domain so synthesis commit is not quarantined
    for dom in ("glp1",):
        pol = tmp_path / ".knowledge" / "policies" / dom
        pol.mkdir(parents=True)
        (pol / "policy.yaml").write_text(f"domain: {dom}\n")
    return tmp_path


# ---------------------------------------------------------------------------
# Helper: record the same gap text enough times to reach trigger-mass.
# thresholds() returns recurrence_mass=5 and cold_start_min_recurrences=3.
# A text must recur >= cold_start_min times to contribute trigger mass.
# We record it recurrence_mass times (5) so trigger_mass >= threshold.
# ---------------------------------------------------------------------------


def _record_gap_n(ledger: DemandLedger, text: str, n: int) -> None:
    for _ in range(n):
        ledger.record_gap(text, caller="test")


# ---------------------------------------------------------------------------
# Test: demand loop — single recurring gap reaches trigger-mass → synthesis submitted
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_demand_loop_recurring_gap_triggers_synthesis(repo):
    """corpus-miss → record_gap × N → demand_cluster(trigger=True) → synthesis committed.

    The gap text must recur >= recurrence_mass times (default 5) before the cluster
    fires. After firing, run_worker commits the synthesis page.

    Drives the REAL path:
      DemandLedger.record_gap() → cluster() auto-submits intent →
      IntentQueue → run_worker → CommitGate → synthesis page on disk in git.

    This test goes RED if:
      - cluster() does not submit when trigger_mass is reached
      - run_worker does not commit the synthesis intent
      - the committed page lacks the centroid title
    """
    t = thresholds()
    recurrence_mass = int(t["demand.recurrence_mass"])          # 5
    cold_start_min = int(t["demand.cold_start_min_recurrences"])  # 3

    # Record the same gap text enough times to hit both cold-start gate and trigger-mass
    gap_text = "how does semaglutide reduce appetite in the hypothalamus"
    n_records = max(recurrence_mass, cold_start_min)

    queue = IntentQueue()
    ledger = DemandLedger(root=repo, queue=queue)
    _record_gap_n(ledger, gap_text, n_records)

    # demand_cluster(trigger=True) calls cluster() which auto-submits for triggered clusters
    result = demand_cluster(root=repo, trigger=True, queue=queue)

    assert result.success, f"demand_cluster failed: {result.errors}"
    clusters = result.data["clusters"]
    assert len(clusters) >= 1, "no clusters returned"

    triggered = [c for c in clusters if c.triggered]
    assert len(triggered) >= 1, (
        f"no cluster reached trigger-mass after {n_records} records; "
        f"clusters={[(c.centroid_text, c.recurrence_mass) for c in clusters]}"
    )

    # The triggered cluster must have submitted an intent to the queue
    submitted = _submitted_ids(queue)
    assert len(submitted) >= 1, (
        "triggered cluster did not submit a synthesis intent to the queue; "
        f"submitted dir is empty"
    )

    # run_worker drains the submitted synthesis intent through the gate
    idx = EmbeddingIndex()
    gate = CommitGate(queue=queue, embedding_index=idx)
    run_worker(once=True, queue=queue, gate=gate)

    # The synthesis page must exist on disk
    synthesis_dir = repo / "wiki" / "synthesis"
    synthesis_pages = list(synthesis_dir.glob("*.md")) if synthesis_dir.exists() else []
    assert len(synthesis_pages) >= 1, (
        "run_worker did not commit any synthesis page for the demand-triggered cluster"
    )

    # The page content must reference the centroid topic
    committed_text = synthesis_pages[0].read_text()
    # Title contains the gap text (slug-derived from centroid_text)
    assert "semaglutide" in committed_text.lower() or "appetite" in committed_text.lower(), (
        f"synthesis page does not reference the gap topic; content={committed_text[:300]}"
    )


@pytest.mark.integration
def test_demand_loop_single_gap_does_not_trigger(repo):
    """Named negative control: a single non-recurring gap does NOT trigger.

    The cold-start gate requires >= cold_start_min_recurrences (default 3)
    occurrences before a gap contributes trigger-mass. A single recording
    contributes 0 trigger-mass, so recurrence_mass (5) is never reached.

    This test goes RED if the cold-start gate is removed (a single record would
    then trigger, polluting the intent queue with low-signal synthesis intents).
    """
    t = thresholds()
    # Only record ONCE — below cold_start_min threshold
    gap_text = "how does liraglutide affect gastric emptying rate"

    queue = IntentQueue()
    ledger = DemandLedger(root=repo, queue=queue)
    ledger.record_gap(gap_text, caller="test")  # exactly one record

    result = demand_cluster(root=repo, trigger=True, queue=queue)

    assert result.success, f"demand_cluster failed: {result.errors}"
    clusters = result.data["clusters"]

    # Cluster may form but must NOT trigger (single record below cold-start gate)
    triggered = [c for c in clusters if c.triggered]
    assert len(triggered) == 0, (
        f"single non-recurring gap must NOT trigger; triggered clusters: {triggered}"
    )

    # No synthesis intent must have been submitted
    submitted = _submitted_ids(queue)
    assert len(submitted) == 0, (
        f"single gap must not submit any intent; found submitted={submitted}"
    )


@pytest.mark.integration
def test_demand_loop_trigger_false_never_submits(repo):
    """When trigger=False (default), demand_cluster does NOT call cluster() and
    nothing is submitted even if the gap would trigger.

    Drives the report-only branch of demand_cluster: no queue side-effects.
    """
    t = thresholds()
    recurrence_mass = int(t["demand.recurrence_mass"])

    gap_text = "what is the mechanism of GIP receptor activation by tirzepatide"
    queue = IntentQueue()
    ledger = DemandLedger(root=repo, queue=queue)
    _record_gap_n(ledger, gap_text, recurrence_mass)

    # trigger=False → report-only path — no submission even if mass is reached
    result = demand_cluster(root=repo, trigger=False, queue=queue)

    assert result.success
    assert result.data["clusters"] == [], "trigger=False must return empty clusters list"

    submitted = _submitted_ids(queue)
    assert len(submitted) == 0, (
        "trigger=False must not submit any intent; "
        f"found submitted={submitted}"
    )
