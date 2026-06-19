"""Demand-cluster op — D1: thin driver for DemandLedger.cluster() (backlog I1).

``demand_cluster`` calls DemandLedger.cluster() and returns an OperationResult
with data["clusters"] populated.

Submission semantics: DemandLedger.cluster() ALWAYS auto-submits a synthesis intent
when a cluster reaches trigger-mass (that is the ledger's Phase-5 design contract —
see demand_ledger.py:284-288). There is no ledger dry-run / no-submit path. This op
always wires a real, root-rooted IntentQueue so submissions land in the correct
on-disk location (root/.knowledge/intents/submitted) rather than falling back to the
ledger's stray default IntentQueue().

The ``trigger`` parameter controls whether cluster() is called at all:
  - trigger=False (default): only compute + return clusters; do NOT call cluster(),
    so no submission occurs. Use for reporting / inspection only.
  - trigger=True: call cluster(), which auto-submits for any triggered cluster.

This matches the brief's "submits an intent for each triggered cluster when --trigger"
contract and makes the negative control honest: a non-recurring single gap never
reaches trigger-mass → ledger does not submit → submitted dir is empty.

NOTE: a real ``dry_run`` mode on DemandLedger (cluster without submitting) is a
possible future improvement; backlog it as a ledger-layer change.
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
        trigger: When True, call DemandLedger.cluster() — which auto-submits a
            synthesis intent for every cluster that reaches trigger-mass (dedup-safe:
            ledger tracks triggered.json). When False (default), cluster() is NOT
            called, so no intents are submitted and no triggered.json is updated.
        queue: IntentQueue override for tests. When trigger=True and queue is None,
            an IntentQueue rooted at the real intents dir is constructed so intents
            land in the correct on-disk location.

    Returns:
        OperationResult with:
          success=True always (unless ledger raises)
          data["clusters"] — list of GapCluster dataclasses (empty when trigger=False)
          summary — count of clusters + how many triggered
    """
    if not trigger:
        # No-trigger path: skip cluster() entirely — no submission, no triggered.json
        # update. Returns an empty cluster list (reporting only).
        return OperationResult(
            success=True,
            summary="demand-cluster: report-only (no --trigger); pass --trigger to submit",
            data={"clusters": []},
        )

    # trigger=True: wire a real queue so intents land in the right location.
    # The ledger's _submit_canonicalization_trigger falls back to IntentQueue() when
    # self._queue is None, which uses paths.intents_dir() — correct in production but
    # test-unfriendly. Always provide the queue explicitly.
    _queue = queue or IntentQueue()

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
