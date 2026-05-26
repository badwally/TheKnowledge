"""TOOL-14: contradiction_drift — nightly JSON snapshot + diff tests."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from gateway import paths
from gateway.lint import LintFinding, SEVERITY_WARNING
from gateway.ops.contradiction_drift import (
    _diff,
    _drift_path,
    _load_snapshot,
    _serialize_findings,
    _weekly_digest,
    run_contradiction_drift,
)


# --- helpers ----------------------------------------------------------------


def _finding(domain: str, a_page: str = "concept/foo", b_page: str = "concept/bar") -> LintFinding:
    return LintFinding(
        check="contradictions",
        severity=SEVERITY_WARNING,
        message=f"contradiction in '{domain}'",
        metadata={
            "domain": domain,
            "a_page": a_page,
            "b_page": b_page,
            "a_text": "A says X.",
            "b_text": "B says not-X.",
            "rationale": "direct conflict",
        },
    )


# --- unit tests -------------------------------------------------------------


def test_serialize_findings_filters_non_contradictions(kb_root: Path) -> None:
    findings = [
        _finding("alpha"),
        LintFinding(check="orphans", severity="warning", message="orphan"),
    ]
    result = _serialize_findings(findings)
    assert len(result) == 1
    assert result[0]["domain"] == "alpha"


def test_serialize_findings_stable_sort(kb_root: Path) -> None:
    findings = [
        _finding("beta", "concept/z", "concept/a"),
        _finding("alpha", "concept/x", "concept/y"),
    ]
    result = _serialize_findings(findings)
    assert result[0]["domain"] == "alpha"
    assert result[1]["domain"] == "beta"


def test_diff_empty_previous(kb_root: Path) -> None:
    current = [{"domain": "alpha", "a_page": "concept/foo", "b_page": "concept/bar", "rationale": ""}]
    new, resolved = _diff([], current)
    assert new == current
    assert resolved == []


def test_diff_no_change(kb_root: Path) -> None:
    items = [{"domain": "alpha", "a_page": "concept/foo", "b_page": "concept/bar", "rationale": ""}]
    new, resolved = _diff(items, items)
    assert new == []
    assert resolved == []


def test_diff_resolved_item(kb_root: Path) -> None:
    previous = [{"domain": "alpha", "a_page": "concept/foo", "b_page": "concept/bar", "rationale": ""}]
    new, resolved = _diff(previous, [])
    assert new == []
    assert resolved == previous


def test_diff_new_item(kb_root: Path) -> None:
    previous = [{"domain": "alpha", "a_page": "concept/foo", "b_page": "concept/bar", "rationale": ""}]
    current = previous + [{"domain": "alpha", "a_page": "concept/baz", "b_page": "concept/qux", "rationale": ""}]
    new, resolved = _diff(previous, current)
    assert len(new) == 1
    assert new[0]["a_page"] == "concept/baz"
    assert resolved == []


def test_load_snapshot_missing(kb_root: Path) -> None:
    assert _load_snapshot("2026-01-01") == []


def test_run_writes_snapshot(kb_root: Path) -> None:
    with patch("gateway.lint.contradictions.run", return_value=[_finding("alpha")]):
        result = run_contradiction_drift(date_str="2026-05-26")

    assert result.success
    p = _drift_path("2026-05-26")
    assert p.exists()
    data = json.loads(p.read_text())
    assert data["date"] == "2026-05-26"
    assert data["total"] == 1
    assert len(data["findings"]) == 1


def test_run_diff_against_yesterday(kb_root: Path) -> None:
    yesterday_items = [{"domain": "alpha", "a_page": "concept/old", "b_page": "concept/gone", "rationale": ""}]
    yesterday_data = {"date": "2026-05-25", "findings": yesterday_items, "new": [], "resolved": []}
    _drift_path("2026-05-25").parent.mkdir(parents=True, exist_ok=True)
    _drift_path("2026-05-25").write_text(json.dumps(yesterday_data))

    new_finding = _finding("alpha", "concept/new1", "concept/new2")
    with patch("gateway.lint.contradictions.run", return_value=[new_finding]):
        result = run_contradiction_drift(date_str="2026-05-26")

    data = json.loads(_drift_path("2026-05-26").read_text())
    assert len(data["new"]) == 1
    assert data["new"][0]["a_page"] == "concept/new1"
    assert len(data["resolved"]) == 1
    assert data["resolved"][0]["a_page"] == "concept/old"


def test_run_empty_wiki_produces_zero_findings(kb_root: Path) -> None:
    with patch("gateway.lint.contradictions.run", return_value=[]):
        result = run_contradiction_drift(date_str="2026-05-26")

    assert result.success
    data = json.loads(_drift_path("2026-05-26").read_text())
    assert data["total"] == 0


def test_run_digest_included(kb_root: Path) -> None:
    with patch("gateway.lint.contradictions.run", return_value=[]):
        result = run_contradiction_drift(date_str="2026-05-26", include_digest=True)

    assert "7 days" in result.summary or "last 7 days" in result.summary.lower() or "Contradiction drift" in result.summary
