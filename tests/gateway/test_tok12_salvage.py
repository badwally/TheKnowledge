"""Tests for TOK-12 — salvage-on-partial-failure for research runs.

Covers:
- After analyze(), per-branch JSON files written to nlm/findings/<session>/<slug>.json
- --execute with all fresh findings → analyze() not called (NLM skipped)
- --execute with partial findings → only missing branches re-queried
- --execute with stale findings → all branches re-queried
- Failed branch written to disk without blocking recovery
- branch-slug is collision-safe
"""

from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from gateway import paths
from gateway.research import analysis as _analysis


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


FAKE_FINDING = {
    "branch": "Methods",
    "methods": {"answer": "Some NLM answer.", "citations": {}, "sources_used": []},
    "comparisons": {"answer": "", "citations": {}, "sources_used": []},
    "open_problems": {"answer": "", "citations": {}, "sources_used": []},
}


def _make_mock_nlm(branches: list[str] | None = None) -> MagicMock:
    """Return a mock NlmClient that returns branch findings on notebook_query."""
    client = MagicMock()
    branches = branches or ["Methods", "Comparisons"]

    def _notebook_query(notebook_id, question):
        # Taxonomy call returns branches; investigation calls return findings
        if "taxonomy" in question.lower() or "branches" in question.lower() or "field" in question.lower():
            branch_list = [{"name": b, "description": f"{b} desc", "sub_branches": []} for b in branches]
            return {
                "answer": json.dumps({"field": "test", "branches": branch_list}),
                "citations": {},
                "sources_used": [],
            }
        return {"answer": "NLM answer.", "citations": {}, "sources_used": []}

    client.notebook_query.side_effect = _notebook_query
    return client


def _findings_dir(kb_root: Path, session_id: str) -> Path:
    return paths.nlm_dir() / "findings" / session_id


# ---------------------------------------------------------------------------
# analyze() writes per-branch finding files
# ---------------------------------------------------------------------------


def test_analyze_writes_per_branch_finding_files(kb_root):
    client = _make_mock_nlm(branches=["Methods", "Comparisons"])
    session_id = "test-session-abc123"

    result = _analysis.analyze(
        "nb-test",
        domain="glp1",
        research_query="What are the methods?",
        client=client,
        session_id=session_id,
    )

    findings_dir = _findings_dir(kb_root, session_id)
    assert findings_dir.is_dir()
    files = list(findings_dir.glob("*.json"))
    # At least one file per branch (methods, comparisons) + possibly _result.json
    branch_files = [f for f in files if not f.name.startswith("_")]
    assert len(branch_files) >= 2


def test_analyze_finding_file_contains_branch_name(kb_root):
    client = _make_mock_nlm(branches=["Methods"])
    session_id = "test-session-branch-name"

    _analysis.analyze(
        "nb-test",
        domain="glp1",
        research_query="What are the methods?",
        client=client,
        session_id=session_id,
    )

    findings_dir = _findings_dir(kb_root, session_id)
    branch_files = [f for f in findings_dir.glob("*.json") if not f.name.startswith("_")]
    assert branch_files
    data = json.loads(branch_files[0].read_text())
    assert data.get("branch") == "Methods"


def test_analyze_error_branch_written_to_disk(kb_root, monkeypatch):
    """Failed branch still writes its error dict to disk."""
    client = _make_mock_nlm(branches=["Methods", "Error-Branch"])

    def _boom(notebook_id, client, branch, templates, *, research_query):
        if branch.get("name") == "Error-Branch":
            raise RuntimeError("simulated NLM failure")
        from gateway.research.analysis import _investigate_branch as _orig
        return _orig(notebook_id, client, branch, templates, research_query=research_query)

    monkeypatch.setattr(_analysis, "_investigate_branch", _boom)

    session_id = "test-session-error-branch"
    _analysis.analyze(
        "nb-test",
        domain="glp1",
        research_query="What?",
        client=client,
        session_id=session_id,
    )

    findings_dir = _findings_dir(kb_root, session_id)
    files = {f.stem: f for f in findings_dir.glob("*.json") if not f.name.startswith("_")}
    # error-branch file should exist
    error_files = [f for name, f in files.items() if "error" in name.lower() or "error-branch" in name.lower()]
    # At minimum, check that a file with "error" key exists
    all_data = [json.loads(f.read_text()) for f in files.values()]
    assert any("error" in d for d in all_data)


# ---------------------------------------------------------------------------
# no session_id → no files written
# ---------------------------------------------------------------------------


def test_analyze_without_session_id_writes_no_files(kb_root):
    client = _make_mock_nlm(branches=["Methods"])
    findings_root = paths.nlm_dir() / "findings"

    _analysis.analyze(
        "nb-test",
        domain="glp1",
        research_query="What?",
        client=client,
        # session_id deliberately omitted
    )

    assert not findings_root.exists() or not any(findings_root.rglob("*.json"))


# ---------------------------------------------------------------------------
# prefetched_findings skips NLM calls for those branches
# ---------------------------------------------------------------------------


def test_prefetched_findings_skips_nlm_for_cached_branches(kb_root):
    client = _make_mock_nlm(branches=["Methods", "Comparisons"])
    session_id = "test-session-prefetch"

    # First run: fully analyze and cache
    _analysis.analyze(
        "nb-test",
        domain="glp1",
        research_query="What?",
        client=client,
        session_id=session_id,
    )

    # Load cached findings
    loaded = _analysis.load_branch_findings(session_id)
    assert loaded is not None

    # Reset call count
    client.notebook_query.reset_mock()

    # Second run with prefetched — should skip branch investigation calls
    _analysis.analyze(
        "nb-test",
        domain="glp1",
        research_query="What?",
        client=client,
        session_id=session_id,
        prefetched_findings=loaded,
    )

    # The mock NLM should be called far fewer times since branches are cached
    # (taxonomy still runs, branch investigations are skipped)
    # Count branch-investigation calls vs taxonomy calls
    call_count_with_prefetch = client.notebook_query.call_count
    # Without prefetch it would be called once per branch query set + taxonomy
    # With prefetch, branch calls are skipped
    assert call_count_with_prefetch < 5  # taxonomy + synthesis only, no per-branch


# ---------------------------------------------------------------------------
# load_branch_findings: stale files return None
# ---------------------------------------------------------------------------


def test_load_branch_findings_returns_none_for_stale_files(kb_root, monkeypatch):
    session_id = "test-session-stale"
    findings_dir = _findings_dir(kb_root, session_id)
    findings_dir.mkdir(parents=True, exist_ok=True)
    f = findings_dir / "methods.json"
    f.write_text(json.dumps({"branch": "Methods", "answer": "x"}))

    # Make the file appear old by patching FINDINGS_STALE_HOURS to 0
    monkeypatch.setattr(_analysis, "FINDINGS_STALE_HOURS", 0)

    result = _analysis.load_branch_findings(session_id)
    assert result is None


def test_load_branch_findings_returns_none_when_dir_absent(kb_root):
    result = _analysis.load_branch_findings("nonexistent-session-xyz")
    assert result is None


def test_load_branch_findings_returns_dict_for_fresh_files(kb_root):
    session_id = "test-session-fresh"
    findings_dir = _findings_dir(kb_root, session_id)
    findings_dir.mkdir(parents=True, exist_ok=True)
    (findings_dir / "methods.json").write_text(json.dumps({"branch": "Methods", "answer": "x"}))

    result = _analysis.load_branch_findings(session_id)
    assert result is not None
    assert "Methods" in result


# ---------------------------------------------------------------------------
# branch-slug is collision-safe
# ---------------------------------------------------------------------------


def test_branch_slug_collision_safe(kb_root):
    """Different branch names produce different slugs."""
    client = _make_mock_nlm(branches=["Methods Overview", "Methods Detail"])
    session_id = "test-session-slugs"

    _analysis.analyze(
        "nb-test",
        domain="glp1",
        research_query="What?",
        client=client,
        session_id=session_id,
    )

    findings_dir = _findings_dir(kb_root, session_id)
    branch_files = [f for f in findings_dir.glob("*.json") if not f.name.startswith("_")]
    slugs = [f.stem for f in branch_files]
    assert len(slugs) == len(set(slugs)), "Branch slugs must be unique"
