"""`wiki preflight` — planner/executor pre-flight gap coverage check (Phase 5, D12).

READ-TIER op: no writes, no token spend, no CommitGate intents enqueued.

Given a proposed plan text, this op:
1. Runs `retrieve()` (LLM-free, FTS/BM25) to estimate wiki coverage of the plan.
2. Checks the DemandLedger for outstanding gaps whose text overlaps the plan.
3. Returns an enrichment-status summary: how well the wiki currently covers
   the plan's topics, and whether there are pending demand gaps that overlap.

Callers (planner, executor) use this to decide whether to proceed with the plan
or to prompt a `wiki research` / ingest cycle first.
"""

from __future__ import annotations

from pathlib import Path

from gateway.core import OperationResult


def preflight(
    plan_text: str,
    *,
    root: Path | None = None,
) -> OperationResult:
    """Read-tier pre-flight: estimate wiki coverage + outstanding gaps for a plan.

    No writes, no LLM calls, no intent enqueues.

    Args:
        plan_text: The proposed research or synthesis plan text.
        root: Optional KNOWLEDGE_ROOT override (for tests).

    Returns:
        OperationResult(success=True, data={
            "gaps": [...],            # matching outstanding gap texts from DemandLedger
            "enrichment_status": {
                "coverage": "high" | "partial" | "low",
                "sections_found": int,
                "matching_gaps": int,
            }
        })
    """
    if not plan_text or not plan_text.strip():
        return OperationResult(
            success=False,
            errors=["plan_text must be non-empty"],
            summary="preflight rejected: empty plan",
        )

    from gateway.ops.retrieve import retrieve
    from gateway.demand_ledger import DemandLedger, _load_gaps

    # --- Step 1: FTS retrieval (LLM-free) to estimate coverage ---
    _block, sections = retrieve(plan_text.strip(), k=8)
    sections_found = len(sections)

    # Coverage heuristic: based on number of relevant sections returned
    if sections_found >= 5:
        coverage = "high"
    elif sections_found >= 2:
        coverage = "partial"
    else:
        coverage = "low"

    # --- Step 2: Check DemandLedger for overlapping outstanding gaps ---
    # Load raw gaps from .knowledge/demand/gaps.jsonl — no clustering, no embedding.
    # Simple word-overlap heuristic (same as A4 carry-forward suppression).
    plan_words = {w for w in plan_text.lower().split() if len(w) > 3}
    matching_gaps: list[str] = []

    if plan_words:
        gaps_path = (
            (root / ".knowledge" / "demand" / "gaps.jsonl")
            if root is not None
            else None
        )
        records = _load_gaps(gaps_path) if gaps_path else _load_gaps(
            __import__("gateway.demand_ledger", fromlist=["_gaps_path"])._gaps_path()
        )
        seen_texts: set[str] = set()
        for r in records:
            gap_words = {w for w in r.text.lower().split() if len(w) > 3}
            if gap_words & plan_words and r.text not in seen_texts:
                matching_gaps.append(r.text)
                seen_texts.add(r.text)

    return OperationResult(
        success=True,
        summary=(
            f"preflight: coverage={coverage} ({sections_found} sections), "
            f"{len(matching_gaps)} matching gap(s)"
        ),
        data={
            "gaps": matching_gaps,
            "enrichment_status": {
                "coverage": coverage,
                "sections_found": sections_found,
                "matching_gaps": len(matching_gaps),
            },
        },
    )


def preflight_op(plan_text: str, *, root: Path | None = None) -> OperationResult:
    """CLI/MCP wrapper for preflight — delegates to preflight()."""
    return preflight(plan_text, root=root)
