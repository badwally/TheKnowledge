"""Pre-merge gate — runs in sequence, exits non-zero on the FIRST failure.

Sequence:
  1. Full pytest suite
  2. Fast + new tiers green (M1 split: not slow and not e2e)
  3. retrieval_eval recall@10 >= RECALL_FLOOR (0.90)
  4. merge_map_eval regressions == []
  5. embedding_eval all namespaces passed
  6. Scoped lints: orphans / schema-drift / broken-wikilinks at baseline

Invoke:
  .venv/bin/python -m gateway.scripts.gate [--skip-suite] [--eval-only]

The floor-check logic is factored into check_recall_floor() so it can be
unit-tested without running the full suite.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple

# ---------------------------------------------------------------------------
# Baselines — update when the lint baseline genuinely improves (not to paper
# over regressions). The gate fires on NEW regressions above these counts.
# ---------------------------------------------------------------------------
RECALL_FLOOR: float = 0.90  # do not lower; baseline 0.926
LINT_BASELINES: dict[str, int] = {
    "orphans": 758,
    "schema-drift": 191,
    "broken-wikilinks": 1,
}

# Path to the dedup golden used by merge_map_eval
_DEDUP_GOLDEN = Path(".knowledge/eval/dedup/golden.yaml")


# ---------------------------------------------------------------------------
# Importable check functions (unit-testable without running the suite)
# ---------------------------------------------------------------------------


class GateCheckResult(NamedTuple):
    passed: bool
    message: str


def check_recall_floor(recall: float, floor: float = RECALL_FLOOR) -> GateCheckResult:
    """Return a GateCheckResult for a retrieval recall value against the floor.

    This function is the importable unit under test — it contains no I/O.
    """
    if recall >= floor:
        return GateCheckResult(
            passed=True,
            message=f"retrieval recall@10={recall:.3f} >= floor {floor:.3f}  PASS",
        )
    return GateCheckResult(
        passed=False,
        message=f"retrieval recall@10={recall:.3f} < floor {floor:.3f}  FAIL",
    )


def check_merge_map(regressions: list) -> GateCheckResult:
    """Return a GateCheckResult for a merge_map_eval regressions list."""
    if not regressions:
        return GateCheckResult(passed=True, message="merge_map_eval: 0 regressions  PASS")
    summary = ", ".join(str(r) for r in regressions[:3])
    more = f" (+{len(regressions) - 3} more)" if len(regressions) > 3 else ""
    return GateCheckResult(
        passed=False,
        message=f"merge_map_eval: {len(regressions)} regression(s): {summary}{more}  FAIL",
    )


def check_embedding_namespaces(
    reports: dict,
) -> GateCheckResult:
    """Return a GateCheckResult for the embedding_eval namespace reports dict.

    A namespace passes if:
      - r.passed is True (metric >= floor), OR
      - r.fallback_active and r.fallback_falsifiable (the named lexical fallback
        is active AND the gate is independently falsifiable — I2 design).

    The entity namespace currently rides the active+falsifiable fallback by design:
    its Phase-3 hard identity pairs (brand↔generic, abbreviation↔expansion) are
    beyond lexical reach, so the gate accepts the fallback-mode outcome (see
    test_embedding_adequacy.py and the I2 design note in embedding_eval.py).
    """

    def _ns_ok(r) -> bool:
        return r.passed or (
            getattr(r, "fallback_active", False)
            and getattr(r, "fallback_falsifiable", False)
        )

    failed = [ns for ns, r in reports.items() if not _ns_ok(r)]
    if not failed:
        summaries = "  ".join(r.summary() for r in reports.values())
        return GateCheckResult(
            passed=True,
            message=f"embedding_eval: all namespaces OK  ({summaries})  PASS",
        )
    fail_summaries = "  ".join(reports[ns].summary() for ns in failed)
    return GateCheckResult(
        passed=False,
        message=f"embedding_eval: {len(failed)} namespace(s) failed: {fail_summaries}  FAIL",
    )


def check_lint_counts(scope_counts: dict[str, int]) -> GateCheckResult:
    """Return a GateCheckResult comparing current lint counts against LINT_BASELINES.

    Fires on new regressions (count > baseline); does not require zero findings.
    """
    regressions = []
    for scope, baseline in LINT_BASELINES.items():
        current = scope_counts.get(scope, 0)
        if current > baseline:
            regressions.append(f"{scope}: {current} > baseline {baseline}")
    if not regressions:
        detail = "  ".join(f"{s}={scope_counts.get(s, 0)}" for s in LINT_BASELINES)
        return GateCheckResult(
            passed=True,
            message=f"lint: no regressions above baseline  ({detail})  PASS",
        )
    return GateCheckResult(
        passed=False,
        message=f"lint: regressions detected: {'; '.join(regressions)}  FAIL",
    )


# ---------------------------------------------------------------------------
# Gate steps
# ---------------------------------------------------------------------------


def _banner(msg: str) -> None:
    print(f"\n{'='*72}", flush=True)
    print(f"  {msg}", flush=True)
    print(f"{'='*72}", flush=True)


def _run_pytest(args: list[str]) -> GateCheckResult:
    """Run pytest with the given args, streaming output. Return pass/fail."""
    cmd = [sys.executable, "-m", "pytest"] + args
    print(" ".join(cmd), flush=True)
    result = subprocess.run(cmd, check=False)
    if result.returncode == 0:
        return GateCheckResult(passed=True, message="pytest: PASS")
    return GateCheckResult(passed=False, message=f"pytest: FAIL (exit {result.returncode})")


def step_full_suite() -> GateCheckResult:
    _banner("Step 1: Full pytest suite")
    return _run_pytest(["-q"])


def step_fast_tiers() -> GateCheckResult:
    _banner("Step 2: Fast + new tiers (not slow, not e2e)")
    return _run_pytest(["-q", "-m", "not slow and not e2e"])


def step_retrieval_eval() -> GateCheckResult:
    """Run retrieval eval and check recall@10 >= RECALL_FLOOR."""
    _banner("Step 3: Retrieval eval (fts recall@10 >= 0.90)")
    from gateway.evaluate.retrieval_eval import evaluate, format_report

    report = evaluate(retriever="fts", k=10)
    formatted = format_report(report, show_misses=True)
    # Print using grep-friendly format so one-pass capture works
    print(formatted, flush=True)
    recall = report.recall_at(10)
    return check_recall_floor(recall)


def step_merge_map_eval() -> GateCheckResult:
    """Run merge_map_eval and check regressions == []."""
    _banner("Step 4: Merge-map eval (no regressions)")
    from gateway.evaluate.merge_map_eval import merge_map_eval

    golden_path = Path(".knowledge/eval/dedup/golden.yaml")
    result = merge_map_eval(golden_path)
    print(
        f"merge_map_eval: precision={result.precision:.3f}  recall={result.recall:.3f}"
        f"  regressions={len(result.regressions)}",
        flush=True,
    )
    return check_merge_map(result.regressions)


def step_embedding_eval() -> GateCheckResult:
    """Run embedding_eval over all namespaces and check all passed."""
    _banner("Step 5: Embedding eval (all namespaces pass)")
    from gateway.evaluate.embedding_eval import evaluate_all

    reports = evaluate_all()
    for ns, r in reports.items():
        print(r.summary(), flush=True)
    return check_embedding_namespaces(reports)


def _parse_lint_count(output: str, scope: str) -> int | None:
    """Extract the finding count from wiki lint --scope output.

    Output format:
        ok: lint: N finding(s)
          scope: N

    Returns None if the scope line is absent or unparseable — callers must
    treat None as a gate failure (fail-closed), not as count 0.
    """
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith(f"{scope}:"):
            parts = stripped.split(":")
            if len(parts) >= 2:
                try:
                    return int(parts[1].strip())
                except ValueError:
                    pass
    return None


def step_scoped_lints() -> GateCheckResult:
    """Run scoped lints and check counts are at or below baselines.

    Fail-closed: if a lint subprocess exits non-zero, or if the count line
    is absent/unparseable in its output, the step fails immediately rather
    than treating the missing count as 0 (which would silently pass the gate
    on a broken invocation).
    """
    _banner("Step 6: Scoped lints (orphans / schema-drift / broken-wikilinks)")
    scope_counts: dict[str, int] = {}
    for scope in LINT_BASELINES:
        cmd = [sys.executable, "-m", "gateway.cli", "lint", "--scope", scope]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        output = result.stdout + result.stderr

        if result.returncode != 0:
            print(f"lint --scope {scope}: subprocess exited {result.returncode}", flush=True)
            print(output, flush=True)
            return GateCheckResult(
                passed=False,
                message=(
                    f"lint --scope {scope} exited {result.returncode} (subprocess failure)  FAIL"
                ),
            )

        count = _parse_lint_count(output, scope)
        if count is None:
            print(f"lint --scope {scope}: count line absent or unparseable in output:", flush=True)
            print(output, flush=True)
            return GateCheckResult(
                passed=False,
                message=(
                    f"lint --scope {scope}: cannot parse count from output (fail-closed)  FAIL"
                ),
            )

        scope_counts[scope] = count
        print(f"lint --scope {scope}: {count}", flush=True)
    return check_lint_counts(scope_counts)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def run_gate(*, skip_suite: bool = False) -> int:
    """Run all gate steps in sequence; return exit code (0=pass, non-zero=fail).

    Set skip_suite=True to skip steps 1 and 2 (full suite + fast tiers) and
    run only the eval + lint steps. Useful when the suite was already run in CI.
    """
    steps = []
    if not skip_suite:
        steps += [
            ("Step 1: full suite", step_full_suite),
            ("Step 2: fast tiers", step_fast_tiers),
        ]
    steps += [
        ("Step 3: retrieval eval", step_retrieval_eval),
        ("Step 4: merge-map eval", step_merge_map_eval),
        ("Step 5: embedding eval", step_embedding_eval),
        ("Step 6: scoped lints", step_scoped_lints),
    ]

    for label, fn in steps:
        result = fn()
        print(f"\n{result.message}", flush=True)
        if not result.passed:
            _banner(f"GATE FAILED at {label}")
            return 1

    _banner("PRE-MERGE GATE PASSED")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m gateway.scripts.gate",
        description=__doc__,
    )
    parser.add_argument(
        "--skip-suite",
        action="store_true",
        help="Skip steps 1 and 2 (full suite + fast tiers); run evals + lints only.",
    )
    ns = parser.parse_args(argv)
    return run_gate(skip_suite=ns.skip_suite)


if __name__ == "__main__":
    sys.exit(main())
