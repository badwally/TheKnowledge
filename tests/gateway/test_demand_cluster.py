"""Tests for demand_cluster op + CLI driver (Task D1, fixed per review).

TDD — failing tests first (RED), then implement (GREEN).

Named negative control: records ONE non-recurring gap (below cold_start=3 and
recurrence_mass=5 thresholds) → ledger never triggers → submitted dir is EMPTY.
This is the ledger's own conditionality; the op's trigger=True path is what wires the
queue so intents land in the right location (root/.knowledge/intents/submitted).

Negative control goes RED on pre-fix code (where the queue was not wired on trigger=True
and the wrong-instance depth test passed for the wrong reason).
"""
from __future__ import annotations

import json
import subprocess

import pytest


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """Minimal git repo with KNOWLEDGE_ROOT redirected to tmp_path."""
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "config", "user.email", "test@test"], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "config", "user.name", "test"], check=True)
    (tmp_path / ".gitignore").write_text(".knowledge/\n")
    subprocess.run(["git", "-C", str(tmp_path), "add", ".gitignore"], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "commit", "-qm", "seed"], check=True)
    return tmp_path


def _submitted_intents(repo) -> list[dict]:
    """Return all intent payloads from the repo-rooted submitted/ dir."""
    submitted_dir = repo / ".knowledge" / "intents" / "submitted"
    if not submitted_dir.exists():
        return []
    return [
        json.loads(f.read_text())
        for f in submitted_dir.iterdir()
        if f.suffix == ".json"
    ]


# ---------------------------------------------------------------------------
# Step 1 — RED: clustering recurring gaps surfaces a triggered cluster
# ---------------------------------------------------------------------------


def test_demand_cluster_surfaces_recurring_gap(repo):
    """Recording a gap 6x (past cold_start=3 and recurrence_mass=5 thresholds)
    and calling demand_cluster(trigger=True) should surface at least one triggered cluster.

    cold_start_min_recurrences == 3, recurrence_mass == 5:
    6 identical entries -> one unique text, count==6, trigger_mass==6 >= 5.
    """
    from gateway.demand_ledger import DemandLedger
    from gateway.ops.demand_cluster import demand_cluster

    ledger = DemandLedger(root=repo)
    for _ in range(6):
        ledger.record_gap("what is the half-life of semaglutide", caller="agent-1")
    result = demand_cluster(root=repo, trigger=True)
    clusters = result.data["clusters"]
    assert any(c.triggered for c in clusters), (
        f"Expected at least one triggered cluster; got: {clusters!r}"
    )


# ---------------------------------------------------------------------------
# Step 3 — GREEN (after impl): trigger=True submits to the right location
# ---------------------------------------------------------------------------


def test_demand_cluster_trigger_submits_synthesis_intent(repo):
    """trigger=True wires the queue so a synthesis intent lands in
    repo/.knowledge/intents/submitted/ for a triggered cluster.
    """
    from gateway.demand_ledger import DemandLedger
    from gateway.ops.demand_cluster import demand_cluster

    ledger = DemandLedger(root=repo)
    for _ in range(6):
        ledger.record_gap("what is the half-life of semaglutide", caller="agent-1")

    result = demand_cluster(root=repo, trigger=True)

    assert result.success
    clusters = result.data["clusters"]
    triggered = [c for c in clusters if c.triggered]
    assert triggered, "Expected triggered clusters"

    # Verify the intent landed on-disk in the repo-rooted submitted dir.
    intents = _submitted_intents(repo)
    assert intents, (
        "Expected synthesis intent in repo/.knowledge/intents/submitted/; found none"
    )
    demand_intents = [p for p in intents if p.get("payload", {}).get("demand_trigger")]
    assert demand_intents, f"No demand_trigger=True intent found; payloads: {intents!r}"
    assert demand_intents[0]["payload"]["page_type"] == "synthesis"


def test_demand_cluster_no_trigger_returns_empty_clusters(repo):
    """trigger=False skips cluster() entirely; returns empty cluster list and
    leaves submitted/ empty. This is the report-only path.
    """
    from gateway.demand_ledger import DemandLedger
    from gateway.ops.demand_cluster import demand_cluster

    ledger = DemandLedger(root=repo)
    for _ in range(6):
        ledger.record_gap("what is the half-life of semaglutide", caller="agent-1")

    result = demand_cluster(root=repo, trigger=False)
    assert result.success
    assert result.data["clusters"] == [], (
        f"Expected empty clusters for trigger=False; got: {result.data['clusters']!r}"
    )
    assert _submitted_intents(repo) == [], "Expected no submitted intents for trigger=False"


def test_demand_cluster_negative_control_non_recurring_gap_submits_nothing(repo):
    """NAMED NEGATIVE CONTROL: a single non-recurring gap (count=1, below cold_start=3
    and recurrence_mass=5) never reaches trigger-mass -> ledger does NOT submit ->
    the submitted dir is empty even with trigger=True.

    This proves intent submission is conditional on the LEDGER's trigger-mass (the real
    conditionality), not on an op-layer gate. The pre-fix implementation passed a
    wrong-instance queue and measured depth on a different object -- this test would
    pass for the wrong reason there. Here we check the on-disk submitted dir directly.
    """
    from gateway.demand_ledger import DemandLedger
    from gateway.ops.demand_cluster import demand_cluster

    ledger = DemandLedger(root=repo)
    # Record a SINGLE gap -- count==1, well below cold_start_min_recurrences==3
    # and recurrence_mass==5. This cluster will never trigger.
    ledger.record_gap("unique one-off question about semaglutide", caller="agent-1")

    result = demand_cluster(root=repo, trigger=True)
    assert result.success

    # No cluster should be triggered.
    clusters = result.data["clusters"]
    assert not any(c.triggered for c in clusters), (
        f"Expected no triggered clusters for a single-occurrence gap; got: {clusters!r}"
    )

    # No intent should land in submitted/.
    intents = _submitted_intents(repo)
    assert intents == [], (
        f"Expected empty submitted dir for non-recurring gap; found: {intents!r}"
    )


# ---------------------------------------------------------------------------
# Step 4 -- CLI round-trip
# ---------------------------------------------------------------------------


def test_demand_cluster_cli_smoke(repo):
    """wiki demand-cluster (no --trigger) exits 0."""
    from gateway.cli import main

    ret = main(["demand-cluster"])
    assert ret == 0


def test_demand_cluster_cli_trigger_flag(repo):
    """wiki demand-cluster --trigger exits 0 and submits intent for recurring gaps."""
    from gateway.demand_ledger import DemandLedger
    from gateway.cli import main

    ledger = DemandLedger(root=repo)
    for _ in range(6):
        ledger.record_gap("what is the half-life of semaglutide", caller="agent-1")

    ret = main(["demand-cluster", "--trigger"])
    assert ret == 0

    intents = _submitted_intents(repo)
    assert intents, "Expected at least one submitted intent after --trigger with recurring gaps"
