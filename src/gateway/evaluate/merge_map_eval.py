"""I3 — merge-map golden re-eval: dedup precision/recall gate.

Runs the real ``dedup.adjudicate`` (or a supplied override) over every case in
the curated dedup golden and returns precision, recall, and a list of
regressions (cases where the adjudicator's decision does not match the golden).

This is the non-regression gate for the CommitGate policy-edit branch: a
policy change that regresses merge precision dead-letters the intent and leaves
the policy file unchanged.

Design decision (Step 0, Task 6): the Phase-3 golden
(.knowledge/eval/dedup/golden.yaml) already contains merge/link/distinct
ground-truth for each pair.  Rather than adding a separate merge_map_golden.yaml,
we reuse that file — it was PURPOSE-BUILT for exactly this adjudicator scoring.
Adding a duplicate would be surface-anchor duplication with zero signal gain.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import yaml

from gateway.dedup import Candidate, DepositIdentity, adjudicate


@dataclass(frozen=True)
class MergeMapResult:
    """Result of a merge-map golden evaluation run.

    precision — fraction of predicted merges that are correct
                (avoids false-positive merges that corrupt identity)
    recall    — fraction of true merges that were predicted
                (avoids missing real duplicates)
    regressions — list of (name, expected, got, rule) for mis-scored cases
    """

    precision: float
    recall: float
    regressions: list[tuple[str, str, str, str]] = field(default_factory=list)


def merge_map_eval(
    golden_path: Path,
    *,
    root: Path | None = None,
    adjudicator: Callable | None = None,
) -> MergeMapResult:
    """Score the curated dedup golden with the real adjudicator.

    Parameters
    ----------
    golden_path:
        Path to the YAML golden file (typically
        `.knowledge/eval/dedup/golden.yaml`).
    root:
        Optional KB root (unused by the default adjudicator; forwarded so the
        CommitGate can supply it for any KB-relative path resolution needed by
        future adjudicator variants).
    adjudicator:
        Optional override adjudicator function with signature
        ``(identity: DepositIdentity, candidates: list[Candidate]) -> str``.
        When None, uses the real ``dedup.adjudicate`` with the standard
        blocking_band=0.15 and identity_threshold=0.30.

    Returns
    -------
    MergeMapResult with precision, recall, and a list of regressions.
    """
    data = yaml.safe_load(golden_path.read_text())
    cases = data.get("cases", [])

    regressions: list[tuple[str, str, str, str]] = []
    predicted_merges = 0
    true_merges = 0
    correct_merges = 0

    for case in cases:
        name = case["name"]
        a = case["a"]
        b = case["b"]
        expected = case["expect"]

        identity = DepositIdentity(
            entity_kind=a["entity_kind"],
            canonical_name=a["canonical_name"],
            aliases=tuple(a.get("aliases", [])),
            domains=tuple(a.get("domains", [])),
        )
        candidate = Candidate(
            slug=b["slug"],
            entity_kind=b["entity_kind"],
            canonical_name=b["canonical_name"],
            aliases=tuple(b.get("aliases", [])),
            domains=tuple(b.get("domains", [])),
            nn_distance=b.get("nn_distance", 1.0),
        )

        if adjudicator is not None:
            # Custom adjudicator — call with the same interface
            got = adjudicator(identity, [candidate])
            rule = "custom"
        else:
            verdict = adjudicate(
                identity,
                [candidate],
                blocking_band=0.15,
                identity_threshold=0.30,
            )
            got = verdict.decision
            rule = verdict.rule

        if expected == "merge":
            true_merges += 1
        if got == "merge":
            predicted_merges += 1
            if expected == "merge":
                correct_merges += 1

        if got != expected:
            regressions.append((name, expected, got, rule))

    # precision: of predicted merges, how many were correct?
    precision = correct_merges / predicted_merges if predicted_merges > 0 else 1.0
    # recall: of true merges, how many did we catch?
    recall = correct_merges / true_merges if true_merges > 0 else 1.0

    return MergeMapResult(
        precision=precision,
        recall=recall,
        regressions=regressions,
    )
