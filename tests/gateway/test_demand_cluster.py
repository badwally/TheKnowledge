"""Tests for demand_cluster op + CLI driver (Task D1).

TDD — failing tests first (RED), then implement (GREEN).

Named negative control: the --trigger test asserts an intent IS submitted for a
triggered cluster, AND a no-trigger (trigger=False) case asserts NO intent is
submitted — proving the submit is conditional, not unconditional.
"""
from __future__ import annotations

import os

import pytest


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """Minimal git repo with KNOWLEDGE_ROOT redirected to tmp_path."""
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    import subprocess
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "config", "user.email", "test@test"], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "config", "user.name", "test"], check=True)
    (tmp_path / ".gitignore").write_text(".knowledge/\n")
    subprocess.run(["git", "-C", str(tmp_path), "add", ".gitignore"], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "commit", "-qm", "seed"], check=True)
    return tmp_path


# ---------------------------------------------------------------------------
# Step 1 — RED: clustering recurring gaps surfaces a triggered cluster
# ---------------------------------------------------------------------------


def test_demand_cluster_surfaces_recurring_gap(repo):
    """Recording a gap 4× (past cold_start=3 and recurrence_mass=5 threshold)
    and calling demand_cluster() should surface at least one triggered cluster.

    cold_start_min_recurrences == 3, recurrence_mass == 5:
    4 identical entries → trigger_mass == 4 (each unique text × count).
    But wait: 4 identical texts → one unique text, count==4, trigger_mass==4 < 5.
    Use 6 entries so trigger_mass==6 >= 5.
    """
    from gateway.demand_ledger import DemandLedger
    from gateway.ops.demand_cluster import demand_cluster

    ledger = DemandLedger(root=repo)
    for _ in range(6):
        ledger.record_gap("what is the half-life of semaglutide", caller="agent-1")
    result = demand_cluster(root=repo)
    clusters = result.data["clusters"]
    assert any(c.triggered for c in clusters), (
        f"Expected at least one triggered cluster; got: {clusters!r}"
    )


# ---------------------------------------------------------------------------
# Step 3 — GREEN (after impl): --trigger path + named negative control
# ---------------------------------------------------------------------------


def test_demand_cluster_trigger_submits_synthesis_intent(repo):
    """trigger=True submits a demand_trigger=True synthesis intent into submitted/."""
    from gateway.demand_ledger import DemandLedger
    from gateway.intent_queue import IntentQueue
    from gateway.ops.demand_cluster import demand_cluster

    ledger = DemandLedger(root=repo)
    for _ in range(6):
        ledger.record_gap("what is the half-life of semaglutide", caller="agent-1")

    q = IntentQueue(root=repo)
    depth_before = q.depth()

    result = demand_cluster(root=repo, trigger=True, queue=q)

    assert result.success
    # At least one triggered cluster → at least one intent submitted
    clusters = result.data["clusters"]
    triggered = [c for c in clusters if c.triggered]
    assert triggered, "Expected triggered clusters"
    assert q.depth() > depth_before, (
        f"Expected intent in queue after trigger=True; depth unchanged at {q.depth()}"
    )
    # Verify payload shape of submitted intent (queue rooted at repo directly)
    submitted_dir = repo / "submitted"
    if submitted_dir.exists():
        import json
        intent_files = list(submitted_dir.iterdir())
        assert intent_files, "No intent files found in submitted/"
        payloads = [json.loads(f.read_text()) for f in intent_files]
        demand_intents = [p for p in payloads if p.get("payload", {}).get("demand_trigger")]
        assert demand_intents, f"No demand_trigger intent found; payloads: {payloads!r}"
        assert demand_intents[0]["payload"]["page_type"] == "synthesis"


def test_demand_cluster_no_trigger_submits_no_intent(repo):
    """NEGATIVE CONTROL: trigger=False must NOT submit any intent even for triggered clusters.

    This proves the intent submission is conditional on trigger=True, not unconditional.
    """
    from gateway.demand_ledger import DemandLedger
    from gateway.intent_queue import IntentQueue
    from gateway.ops.demand_cluster import demand_cluster

    ledger = DemandLedger(root=repo)
    for _ in range(6):
        ledger.record_gap("what is the half-life of semaglutide", caller="agent-1")

    q = IntentQueue(root=repo)
    depth_before = q.depth()

    result = demand_cluster(root=repo, trigger=False, queue=q)

    assert result.success
    # Clusters may be triggered (ledger state), but no NEW intent should land in queue
    assert q.depth() == depth_before, (
        f"Expected no new intents when trigger=False; depth went {depth_before} → {q.depth()}"
    )


# ---------------------------------------------------------------------------
# Step 4 — CLI round-trip
# ---------------------------------------------------------------------------


def test_demand_cluster_cli_smoke(repo):
    """wiki demand-cluster exits 0 and reports clusters (no --trigger)."""
    from gateway.cli import main

    ret = main(["demand-cluster"])
    assert ret == 0


def test_demand_cluster_cli_trigger_flag(repo):
    """wiki demand-cluster --trigger exits 0."""
    from gateway.demand_ledger import DemandLedger
    from gateway.cli import main

    ledger = DemandLedger(root=repo)
    for _ in range(6):
        ledger.record_gap("what is the half-life of semaglutide", caller="agent-1")

    ret = main(["demand-cluster", "--trigger"])
    assert ret == 0
