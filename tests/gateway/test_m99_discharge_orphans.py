"""M99: discharge_orphans — batch synthesize wiki pages for orphaned sources."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from gateway import frontmatter as fm, paths
from gateway.core import OperationResult


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _write_raw_source(
    kb_root: Path,
    *,
    source_type: str = "web",
    slug: str = "test-src",
    domain: str = "glp1",
    wiki_pages: list[str] | None = None,
    title: str = "Test source",
) -> Path:
    d = paths.raw_dir() / source_type
    d.mkdir(parents=True, exist_ok=True)
    front: dict = {
        "id": slug,
        "type": source_type,
        "title": title,
        "domains": [domain],
        "ingested_at": "2026-01-01T00:00:00Z",
    }
    if wiki_pages is not None:
        front["wiki_pages"] = wiki_pages
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, "Source body.\n"))
    return p


def _ok_result(**kwargs) -> OperationResult:
    defaults = dict(success=True, summary="Wrote draft: wiki/synthesis/ans.md", data={})
    defaults.update(kwargs)
    return OperationResult(**defaults)


# ---------------------------------------------------------------------------
# Core logic tests
# ---------------------------------------------------------------------------


def test_discharges_orphan_source(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    _write_raw_source(kb_root, slug="orphan-1", domain="glp1", wiki_pages=None)

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", limit=5)

    assert result.success
    assert "1 synthesis drafts filed" in result.summary
    mock_q.assert_called_once()
    call_kwargs = mock_q.call_args
    assert call_kwargs.kwargs["domain"] == "glp1"
    assert call_kwargs.kwargs["draft"] is True


def test_skips_covered_sources(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    _write_raw_source(
        kb_root, slug="covered-src", domain="glp1",
        wiki_pages=["wiki/synthesis/existing.md"]
    )

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", limit=5)

    assert result.success
    assert "no orphan sources found" in result.summary
    mock_q.assert_not_called()


def test_filters_by_domain(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    _write_raw_source(kb_root, slug="glp1-src", domain="glp1")
    _write_raw_source(kb_root, slug="other-src", domain="other-domain")

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", limit=5)

    assert mock_q.call_count == 1


def test_respects_limit(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    for i in range(5):
        _write_raw_source(kb_root, slug=f"src-{i}", domain="glp1")

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", limit=3)

    assert mock_q.call_count == 3
    assert "3 synthesis drafts filed" in result.summary


def test_dry_run_does_not_call_query(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    _write_raw_source(kb_root, slug="dry-src", domain="glp1")

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", dry_run=True)

    mock_q.assert_not_called()
    assert "dry-run" in result.summary
    assert "1 synthesis drafts filed" in result.summary


def test_no_orphans_returns_success(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    result = discharge_orphans("glp1")

    assert result.success
    assert "no orphan sources found" in result.summary


def test_empty_domain_returns_error(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    result = discharge_orphans("")

    assert not result.success
    assert "domain is required" in result.errors[0]


def test_query_failure_recorded_in_errors(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    _write_raw_source(kb_root, slug="fail-src", domain="glp1")
    fail = OperationResult(success=False, summary="NLM error", data={}, errors=["timeout"])

    with patch("gateway.ops.query.query", return_value=fail):
        result = discharge_orphans("glp1")

    assert not result.success
    assert "0 synthesis drafts filed" in result.summary
    assert len(result.errors) == 1


# ---------------------------------------------------------------------------
# CLI wiring
# ---------------------------------------------------------------------------


def test_cli_parser_discharge_orphans() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["routine", "discharge-orphans", "--domain", "glp1"])
    assert ns.domain == "glp1"
    assert ns.limit == 10
    assert ns.dry_run is False


def test_cli_parser_discharge_orphans_limit() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["routine", "discharge-orphans", "--domain", "glp1", "--limit", "5"])
    assert ns.limit == 5


def test_cli_parser_discharge_orphans_dry_run() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["routine", "discharge-orphans", "--domain", "glp1", "--dry-run"])
    assert ns.dry_run is True


def test_cli_discharge_orphans_calls_op(kb_root: Path) -> None:
    from gateway.cli import _run_routine_cmd
    import argparse

    ns = argparse.Namespace(
        subcommand="routine",
        routine_name="discharge-orphans",
        domain="glp1",
        limit=5,
        dry_run=True,
    )
    with patch("gateway.ops.discharge_orphans.discharge_orphans", return_value=_ok_result()) as mock_op:
        rc = _run_routine_cmd(ns)

    mock_op.assert_called_once_with("glp1", limit=5, dry_run=True)
    assert rc == 0
