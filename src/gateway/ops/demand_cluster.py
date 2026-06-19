"""Demand-cluster op — D1: thin driver for DemandLedger.cluster() (backlog I1).

``demand_cluster`` calls DemandLedger.cluster() and returns an OperationResult
with data["clusters"] populated. With trigger=True, it additionally submits a
page_type=synthesis, demand_trigger=True intent for each *triggered* cluster via
the IntentQueue (the ledger's own submit logic handles dedup internally; we only
skip the queue call when trigger=False).

The ledger's cluster() method already handles the canonicalization trigger path
(submit + triggered.json dedup). trigger=True here means "wire up the queue so
the ledger will submit"; trigger=False means "pass no queue, so the ledger's
_submit_canonicalization_trigger is never called" — preserving the negative control
invariant tested in test_demand_cluster.py.
"""

from __future__ import annotations

from pathlib import Path

from gateway.core import OperationResult
from gateway.demand_ledger import DemandLedger, GapCluster
from gateway.intent_queue import IntentQueue


def demand_cluster(
    *,
    root: Path | None = None,
    trigger: bool = False,
    queue: IntentQueue | None = None,
) -> OperationResult:
    """Run DemandLedger.cluster() and return clusters in result.data.

    Args:
        root: Knowledge root override (for tests; None = production default).
        trigger: When True, submit a synthesis intent for each triggered cluster
            via the IntentQueue (dedup-safe: ledger tracks triggered.json).
            When False (default), cluster() is called without a queue so no
            intents are ever submitted — even if clusters reach trigger mass.
        queue: IntentQueue override for tests. Constructed automatically when
            trigger=True and not supplied.

    Returns:
        OperationResult with:
          success=True always (unless ledger raises)
          data["clusters"] — list of GapCluster dataclasses
          summary — count of clusters + how many triggered
    """
    # Resolve queue: only wire it when trigger=True so the negative control
    # (trigger=False) provably never calls submit().
    _queue: IntentQueue | None = None
    if trigger:
        _queue = queue or IntentQueue(root=root)

    ledger = DemandLedger(root=root, queue=_queue)
    clusters: list[GapCluster] = ledger.cluster()

    n_triggered = sum(1 for c in clusters if c.triggered)
    summary = (
        f"demand-cluster: {len(clusters)} cluster(s), {n_triggered} triggered"
    )

    return OperationResult(
        success=True,
        summary=summary,
        data={"clusters": clusters},
    )
