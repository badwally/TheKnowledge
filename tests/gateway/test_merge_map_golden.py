"""I3 — merge-map golden gate: precision/recall over the curated dedup golden.

merge_map_eval runs the REAL dedup.adjudicate over every case in the curated
golden file and returns precision, recall, and a list of regressions.

Falsifiability negative control (mirrors Phase-3): a geometry-only adjudicator
(merge iff nn_distance ≤ threshold) MUST produce regressions — proving the
golden is not trivially satisfied and actually exercises alias-authority
discipline, not a distance tautology.
"""

from __future__ import annotations

import pytest
from pathlib import Path

from gateway.evaluate.merge_map_eval import merge_map_eval, MergeMapResult


# --- canonical path to the Phase-3 golden (same file as test_dedup_golden.py) ---
_GOLDEN = (
    Path(__file__).parent.parent.parent
    / ".knowledge/eval/dedup/golden.yaml"
)


def test_merge_map_eval_returns_result_object():
    """merge_map_eval returns a MergeMapResult with precision/recall/regressions."""
    result = merge_map_eval(_GOLDEN)
    assert isinstance(result, MergeMapResult)
    assert 0.0 <= result.precision <= 1.0
    assert 0.0 <= result.recall <= 1.0
    assert isinstance(result.regressions, list)


def test_merge_map_eval_real_adjudicator_passes_golden():
    """Real adjudicator scores the golden with no regressions (precision+recall = 1)."""
    result = merge_map_eval(_GOLDEN)
    assert result.regressions == [], (
        f"merge_map_eval: unexpected regressions on real adjudicator: {result.regressions}"
    )
    assert result.precision == 1.0, f"precision={result.precision}"
    assert result.recall == 1.0, f"recall={result.recall}"


def test_merge_map_eval_falsifiability_broken_adjudicator_regresses():
    """A geometry-only adjudicator MUST produce regressions (falsifiability negative control).

    Passes a custom adjudicator that decides 'merge' iff nn_distance <= 0.30,
    and 'distinct' otherwise. This will mis-score cases where alias-authority
    determines the decision differently from pure geometry:
      - type1-vs-type2-distinct: nn=0.198 → geometry says 'merge'; truth is 'distinct'
      - fed-branches-distinct:   nn=0.25  → geometry says 'merge'; truth is 'distinct'
    """
    from gateway.dedup import Candidate, DepositIdentity

    def broken_adjudicator(identity: DepositIdentity, candidates: list[Candidate]) -> str:
        if not candidates:
            return "distinct"
        return "merge" if candidates[0].nn_distance <= 0.30 else "distinct"

    result = merge_map_eval(_GOLDEN, adjudicator=broken_adjudicator)
    assert len(result.regressions) >= 2, (
        f"geometry-only adjudicator must mis-score >= 2 cases; got {result.regressions}"
    )
    # precision must be < 1.0 (some merge decisions were wrong)
    assert result.precision < 1.0, (
        f"geometry-only adjudicator should not achieve precision=1: {result.precision}"
    )


def test_merge_map_eval_root_kwarg_accepted(tmp_path):
    """root= kwarg is forwarded without error (gate uses it for KB-relative paths)."""
    result = merge_map_eval(_GOLDEN, root=tmp_path)
    assert isinstance(result, MergeMapResult)
