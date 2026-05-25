"""Tests for ONT-3: contradiction page type."""

from __future__ import annotations

from pathlib import Path
import textwrap

import pytest

from gateway import validator as v
from gateway import wiki_pages
from gateway.lint import SEVERITY_WARNING


# ── wiki_pages schema ─────────────────────────────────────────────────────────

def test_contradiction_schema_registered() -> None:
    schema = wiki_pages.schema_for_type("contradiction")
    assert schema is not None
    assert schema.type_name == "contradiction"
    assert schema.citation_grounded is False


def test_contradiction_schema_required_fields() -> None:
    schema = wiki_pages.schema_for_type("contradiction")
    assert "parties" in schema.required_fields
    assert "severity" in schema.required_fields
    assert "status" in schema.required_fields


def test_contradiction_schema_has_summary_section() -> None:
    schema = wiki_pages.schema_for_type("contradiction")
    assert any("Summary" in s for s in schema.required_sections)


def test_contradiction_schema_directory() -> None:
    schema = wiki_pages.schema_for_type("contradiction")
    assert "contradictions" in schema.directory


# ── validator enums ───────────────────────────────────────────────────────────

def test_contradiction_severity_enum_members() -> None:
    assert v.CONTRADICTION_SEVERITY_ENUM >= {"major", "minor", "methodological"}


def test_contradiction_status_enum_members() -> None:
    assert v.CONTRADICTION_STATUS_ENUM >= {"open", "investigating", "resolved", "wontfix"}


# ── validate_contradiction_frontmatter ───────────────────────────────────────

def _good_contradiction_front() -> dict:
    return {
        "type": "contradiction",
        "slug": "glp1-dose-ceiling-vs-titration",
        "parties": ["[[sources/web-2026-01-01-abc123]]", "[[sources/arxiv-2024.12345]]"],
        "severity": "major",
        "status": "open",
    }


def test_good_contradiction_frontmatter_passes() -> None:
    result = v.validate_contradiction_frontmatter(_good_contradiction_front())
    assert result.ok


def test_unknown_severity_is_error() -> None:
    front = _good_contradiction_front()
    front["severity"] = "critical"
    result = v.validate_contradiction_frontmatter(front)
    assert not result.ok
    assert any("severity" in e.message.lower() for e in result.errors)


def test_unknown_status_is_error() -> None:
    front = _good_contradiction_front()
    front["status"] = "pending"
    result = v.validate_contradiction_frontmatter(front)
    assert not result.ok
    assert any("status" in e.message.lower() for e in result.errors)


def test_missing_parties_is_error() -> None:
    front = _good_contradiction_front()
    del front["parties"]
    result = v.validate_contradiction_frontmatter(front)
    assert not result.ok


def test_empty_parties_is_error() -> None:
    front = _good_contradiction_front()
    front["parties"] = []
    result = v.validate_contradiction_frontmatter(front)
    assert not result.ok


# ── validate_wiki_page for contradiction ─────────────────────────────────────

_CONTRADICTION_BODY = textwrap.dedent("""\
    ## Summary

    Source A claims X; Source B claims not-X.
""")


def test_validate_wiki_page_contradiction_passes() -> None:
    front = _good_contradiction_front()
    result = v.validate_wiki_page(front, _CONTRADICTION_BODY, "contradiction")
    assert result.ok


def test_validate_wiki_page_contradiction_bad_severity_fails() -> None:
    front = _good_contradiction_front()
    front["severity"] = "extreme"
    result = v.validate_wiki_page(front, _CONTRADICTION_BODY, "contradiction")
    assert not result.ok


# ── contradiction_pages lint ──────────────────────────────────────────────────

def _write_contradiction_page(root: Path, slug: str, severity: str, status: str) -> None:
    pages_dir = root / "wiki" / "contradictions"
    pages_dir.mkdir(parents=True, exist_ok=True)
    content = textwrap.dedent(f"""\
        ---
        type: contradiction
        slug: {slug}
        parties:
          - "[[sources/web-2026-01-01-abc123]]"
          - "[[sources/arxiv-2024.12345]]"
        severity: {severity}
        status: {status}
        resolution: ""
        ---

        ## Summary

        Contradiction between source A and source B.
    """)
    (pages_dir / f"{slug}.md").write_text(content)


def test_contradiction_pages_lint_open_major_is_warning(kb_root: Path) -> None:
    _write_contradiction_page(kb_root, "dose-ceiling", "major", "open")
    from gateway.lint import contradiction_pages
    findings = contradiction_pages.run()
    assert any(f.severity == SEVERITY_WARNING for f in findings)
    assert any("dose-ceiling" in f.message for f in findings)


def test_contradiction_pages_lint_resolved_not_reported(kb_root: Path) -> None:
    _write_contradiction_page(kb_root, "dose-ceiling", "major", "resolved")
    from gateway.lint import contradiction_pages
    findings = contradiction_pages.run()
    assert len(findings) == 0


def test_contradiction_pages_lint_open_minor_not_reported(kb_root: Path) -> None:
    _write_contradiction_page(kb_root, "minor-issue", "minor", "open")
    from gateway.lint import contradiction_pages
    findings = contradiction_pages.run()
    # Only open+major are reported as warnings
    assert len(findings) == 0


def test_contradiction_pages_lint_no_pages_returns_empty(kb_root: Path) -> None:
    from gateway.lint import contradiction_pages
    findings = contradiction_pages.run()
    assert findings == []


# ── migration no-op when jsonl absent ────────────────────────────────────────

def test_migration_noop_when_jsonl_absent(kb_root: Path) -> None:
    import importlib.util
    import pathlib
    script = pathlib.Path(__file__).parent.parent.parent / "migrations" / "0003-migrate-contradictions-jsonl.py"
    spec = importlib.util.spec_from_file_location("migrate_contradictions_jsonl", script)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    result = mod.run(dry_run=True)
    assert result == 0  # 0 pages migrated
