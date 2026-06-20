"""Unit tests for the G1 pre-merge gate eval-floor logic.

These tests exercise the importable check functions in gateway.scripts.gate
WITHOUT running the full test suite, subprocess calls, or any live eval.

Negative controls are named and must go RED on below-floor / regressed input.
"""

import pytest

from gateway.scripts.gate import (
    LINT_BASELINES,
    RECALL_FLOOR,
    GateCheckResult,
    _parse_lint_count,
    check_embedding_namespaces,
    check_lint_counts,
    check_merge_map,
    check_recall_floor,
)


# ---------------------------------------------------------------------------
# Fake objects for the unit tests — no real evals, no subprocess calls.
# ---------------------------------------------------------------------------


class _FakeReport:
    """Minimal stand-in for NamespaceGateReport."""

    def __init__(
        self,
        namespace: str,
        passed: bool,
        value: float = 0.9,
        floor: float = 0.8,
        fallback_active: bool = False,
        fallback_falsifiable: bool = False,
    ):
        self.namespace = namespace
        self.passed = passed
        self.value = value
        self.floor = floor
        self.metric = "test-metric"
        self.fallback_active = fallback_active
        self.fallback_falsifiable = fallback_falsifiable
        self.model_version = "test-v1"

    def summary(self) -> str:
        status = "PASS" if self.passed else "FAIL"
        return f"[{status}] {self.namespace}: {self.metric}={self.value:.3f}"


# ---------------------------------------------------------------------------
# check_recall_floor
# ---------------------------------------------------------------------------


class TestCheckRecallFloor:
    def test_at_floor_passes(self):
        """Recall exactly at the floor (0.90) must pass — gate is >=, not >."""
        result = check_recall_floor(RECALL_FLOOR)
        assert result.passed is True, f"expected pass at floor {RECALL_FLOOR}: {result.message}"

    def test_above_floor_passes(self):
        """Baseline 0.926 must pass."""
        result = check_recall_floor(0.926)
        assert result.passed is True, f"expected pass at baseline 0.926: {result.message}"

    # Negative control — must go RED on below-floor input
    def test_below_floor_fails(self):
        """0.85 < 0.90: gate must return failure (negative control)."""
        result = check_recall_floor(0.85)
        assert result.passed is False, (
            "NEGATIVE CONTROL FAILED: check_recall_floor(0.85) returned passed=True; "
            "the gate is inert on below-floor recall."
        )

    def test_zero_fails(self):
        """Recall=0.0 must fail."""
        result = check_recall_floor(0.0)
        assert result.passed is False

    def test_just_below_floor_fails(self):
        """0.8999 is just below the floor — must fail."""
        result = check_recall_floor(0.8999)
        assert result.passed is False, (
            "NEGATIVE CONTROL FAILED: 0.8999 should be below floor 0.90"
        )

    def test_result_is_named_tuple(self):
        result = check_recall_floor(0.95)
        assert isinstance(result, GateCheckResult)
        assert hasattr(result, "passed")
        assert hasattr(result, "message")

    def test_custom_floor(self):
        """Custom floor parameter is respected."""
        result = check_recall_floor(0.75, floor=0.80)
        assert result.passed is False
        result2 = check_recall_floor(0.80, floor=0.80)
        assert result2.passed is True


# ---------------------------------------------------------------------------
# check_merge_map
# ---------------------------------------------------------------------------


class TestCheckMergeMap:
    def test_empty_regressions_passes(self):
        result = check_merge_map([])
        assert result.passed is True

    # Negative control — any regression must fail
    def test_one_regression_fails(self):
        """NEGATIVE CONTROL: one regression must cause failure."""
        result = check_merge_map([("case-A", "merge", "distinct", "embedding")])
        assert result.passed is False, (
            "NEGATIVE CONTROL FAILED: check_merge_map with 1 regression returned passed=True"
        )

    def test_multiple_regressions_fail(self):
        regressions = [("a", "merge", "distinct", "r1"), ("b", "distinct", "merge", "r2")]
        result = check_merge_map(regressions)
        assert result.passed is False
        assert "2 regression" in result.message

    def test_message_contains_count(self):
        result = check_merge_map([("x", "merge", "distinct", "rule")])
        assert "1" in result.message


# ---------------------------------------------------------------------------
# check_embedding_namespaces
# ---------------------------------------------------------------------------


class TestCheckEmbeddingNamespaces:
    def test_all_passed_passes(self):
        reports = {
            "section": _FakeReport("section", passed=True),
            "entity": _FakeReport("entity", passed=True),
            "question": _FakeReport("question", passed=True),
        }
        result = check_embedding_namespaces(reports)
        assert result.passed is True

    def test_fallback_active_and_falsifiable_passes(self):
        """I2 design: entity namespace may ride active+falsifiable fallback.

        passed=False but fallback_active+fallback_falsifiable → gate OK.
        This mirrors the real entity namespace behavior (lexical encoder cannot
        hit precision 1.0 on hard identity pairs; gate accepts fallback mode).
        """
        reports = {
            "section": _FakeReport("section", passed=True),
            "entity": _FakeReport(
                "entity",
                passed=False,
                fallback_active=True,
                fallback_falsifiable=True,
            ),
            "question": _FakeReport("question", passed=True),
        }
        result = check_embedding_namespaces(reports)
        assert result.passed is True, (
            "entity in active+falsifiable fallback mode should pass the gate (I2 design)"
        )

    # Negative control — failing AND not in valid fallback mode must cause gate failure
    def test_one_failed_namespace_not_in_fallback_fails(self):
        """NEGATIVE CONTROL: failed namespace without active+falsifiable fallback must fail."""
        reports = {
            "section": _FakeReport("section", passed=True),
            # failed, fallback_active=False → not in I2 fallback mode → must fail gate
            "entity": _FakeReport("entity", passed=False, fallback_active=False),
            "question": _FakeReport("question", passed=True),
        }
        result = check_embedding_namespaces(reports)
        assert result.passed is False, (
            "NEGATIVE CONTROL FAILED: failed namespace without active fallback did not fail gate"
        )

    def test_fallback_active_but_not_falsifiable_fails(self):
        """NEGATIVE CONTROL: active fallback that is NOT falsifiable → rubber stamp → gate fails."""
        reports = {
            "section": _FakeReport("section", passed=True),
            "entity": _FakeReport(
                "entity",
                passed=False,
                fallback_active=True,
                fallback_falsifiable=False,  # rubber stamp → gate must reject
            ),
            "question": _FakeReport("question", passed=True),
        }
        result = check_embedding_namespaces(reports)
        assert result.passed is False, (
            "NEGATIVE CONTROL FAILED: non-falsifiable fallback should not satisfy the gate"
        )

    def test_all_failed_no_fallback_fails(self):
        reports = {
            "section": _FakeReport("section", passed=False),
            "entity": _FakeReport("entity", passed=False),
            "question": _FakeReport("question", passed=False),
        }
        result = check_embedding_namespaces(reports)
        assert result.passed is False

    def test_empty_reports_passes(self):
        """No namespaces configured → gate passes (no failures to report)."""
        result = check_embedding_namespaces({})
        assert result.passed is True


# ---------------------------------------------------------------------------
# check_lint_counts
# ---------------------------------------------------------------------------


class TestCheckLintCounts:
    def test_at_baseline_passes(self):
        """Counts exactly at the baselines must pass."""
        result = check_lint_counts(dict(LINT_BASELINES))
        assert result.passed is True

    def test_below_baseline_passes(self):
        """Counts below baselines (improvement) must pass."""
        counts = {k: max(0, v - 10) for k, v in LINT_BASELINES.items()}
        result = check_lint_counts(counts)
        assert result.passed is True

    # Negative control — any scope above baseline must fail
    def test_orphans_above_baseline_fails(self):
        """NEGATIVE CONTROL: orphans count above baseline must fail the gate."""
        counts = dict(LINT_BASELINES)
        counts["orphans"] = LINT_BASELINES["orphans"] + 1
        result = check_lint_counts(counts)
        assert result.passed is False, (
            "NEGATIVE CONTROL FAILED: orphans above baseline did not fail the gate"
        )

    def test_schema_drift_above_baseline_fails(self):
        """NEGATIVE CONTROL: schema-drift count above baseline must fail."""
        counts = dict(LINT_BASELINES)
        counts["schema-drift"] = LINT_BASELINES["schema-drift"] + 1
        result = check_lint_counts(counts)
        assert result.passed is False, (
            "NEGATIVE CONTROL FAILED: schema-drift above baseline did not fail the gate"
        )

    def test_broken_wikilinks_above_baseline_fails(self):
        """NEGATIVE CONTROL: broken-wikilinks count above baseline must fail."""
        counts = dict(LINT_BASELINES)
        counts["broken-wikilinks"] = LINT_BASELINES["broken-wikilinks"] + 1
        result = check_lint_counts(counts)
        assert result.passed is False, (
            "NEGATIVE CONTROL FAILED: broken-wikilinks above baseline did not fail the gate"
        )

    def test_message_includes_scope(self):
        counts = dict(LINT_BASELINES)
        counts["orphans"] = LINT_BASELINES["orphans"] + 5
        result = check_lint_counts(counts)
        assert "orphans" in result.message


# ---------------------------------------------------------------------------
# _parse_lint_count — fail-closed sentinel behaviour
# ---------------------------------------------------------------------------


class TestParseLintCount:
    """Unit tests for _parse_lint_count's sentinel-None (fail-closed) contract.

    The step_scoped_lints caller treats None as a gate failure, so these tests
    verify the parser returns None exactly when the scope line is absent or
    unparseable, rather than silently returning 0.
    """

    # Real output sample from wiki lint --scope orphans
    _REAL_ORPHANS_OUTPUT = (
        "ok: lint: 758 finding(s)\n"
        "  orphans: 758\n"
        "report: /tmp/2026-06-20T00-00-00Z-orphans.md\n"
        "  touched: /tmp/2026-06-20T00-00-00Z-orphans.md\n"
        "  touched: /Users/andrewgrant/code/knowledge/log.md"
    )

    def test_parses_real_output(self):
        """Parser extracts count from the real wiki lint --scope output format."""
        count = _parse_lint_count(self._REAL_ORPHANS_OUTPUT, "orphans")
        assert count == 758, f"expected 758, got {count!r}"

    def test_parses_schema_drift(self):
        output = "ok: lint: 191 finding(s)\n  schema-drift: 191\nreport: /tmp/x.md"
        count = _parse_lint_count(output, "schema-drift")
        assert count == 191

    def test_parses_broken_wikilinks(self):
        output = "ok: lint: 1 finding(s)\n  broken-wikilinks: 1\nreport: /tmp/x.md"
        count = _parse_lint_count(output, "broken-wikilinks")
        assert count == 1

    # NEGATIVE CONTROLS — these must return None (fail-closed), NOT 0

    def test_absent_scope_line_returns_none(self):
        """NEGATIVE CONTROL: absent scope line must return None, not 0.

        Pre-fix behaviour returned 0 → check_lint_counts saw 0 <= baseline → PASS.
        Post-fix: None is returned; step_scoped_lints treats None as gate failure.
        """
        output = "ok: lint: 0 finding(s)\nreport: /tmp/x.md"
        count = _parse_lint_count(output, "orphans")
        assert count is None, (
            "NEGATIVE CONTROL FAILED: absent scope line should return None (fail-closed), "
            f"got {count!r} instead"
        )

    def test_empty_output_returns_none(self):
        """NEGATIVE CONTROL: empty output (broken subprocess) must return None."""
        count = _parse_lint_count("", "orphans")
        assert count is None, (
            "NEGATIVE CONTROL FAILED: empty output should return None, "
            f"got {count!r}"
        )

    def test_unparseable_value_returns_none(self):
        """NEGATIVE CONTROL: non-integer after scope: returns None."""
        output = "ok: lint: ? finding(s)\n  orphans: not-a-number\nreport: /tmp/x.md"
        count = _parse_lint_count(output, "orphans")
        assert count is None, (
            "NEGATIVE CONTROL FAILED: non-integer count value should return None, "
            f"got {count!r}"
        )

    def test_wrong_scope_returns_none(self):
        """NEGATIVE CONTROL: output for a different scope returns None for the requested scope."""
        output = "ok: lint: 191 finding(s)\n  schema-drift: 191\nreport: /tmp/x.md"
        count = _parse_lint_count(output, "orphans")
        assert count is None, (
            "NEGATIVE CONTROL FAILED: output for schema-drift should not parse as orphans"
        )
