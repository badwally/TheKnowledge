"""TOOL-8: wiki daily — daily triage list tests."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.ops.daily_review import (
    DailyReviewResult,
    _collect_orphan_sources,
    _collect_recently_ingested,
    _collect_stale_drafts,
    format_daily_review,
    run_daily_review,
    run_daily_review_op,
)


# --------------------------------------------------------------------------- #
# Helpers                                                                      #
# --------------------------------------------------------------------------- #


def _make_raw_source(
    kb_root: Path,
    source_type: str = "web",
    *,
    slug: str = "test-src",
    title: str = "Test Source",
    ingested_at: str = "2026-01-01T00:00:00Z",
    wiki_pages: list[str] | None = None,
    domains: list[str] | None = None,
) -> Path:
    d = paths.raw_dir() / source_type
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{slug}.md"
    front: dict = {
        "id": slug,
        "type": source_type,
        "title": title,
        "ingested_at": ingested_at,
        "wiki_pages": wiki_pages if wiki_pages is not None else [],
        "domains": domains or [],
    }
    p.write_text(fm.serialize(front, "body"))
    return p


def _make_wiki_draft(
    kb_root: Path,
    *,
    slug: str = "draft-pg",
    title: str = "Draft Page",
    started_at: str = "2026-01-01T00:00:00Z",
    subdirectory: str = "synthesis",
) -> Path:
    d = paths.wiki_dir() / subdirectory
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{slug}.md"
    front: dict = {
        "type": "synthesis",
        "slug": slug,
        "title": title,
        "draft": True,
        "draft_started_at": started_at,
        "synthesizes": [],
    }
    p.write_text(fm.serialize(front, "## Included works\n"))
    return p


# --------------------------------------------------------------------------- #
# _collect_stale_drafts                                                        #
# --------------------------------------------------------------------------- #


def test_stale_draft_detected(kb_root: Path) -> None:
    _make_wiki_draft(kb_root, slug="old-draft", started_at="2026-01-01T00:00:00Z")
    now = datetime(2026, 5, 26, 0, 0, 0, tzinfo=timezone.utc)
    results = _collect_stale_drafts(now=now, stale_days=7)
    slugs = [d.slug for d in results]
    assert "old-draft" in slugs


def test_fresh_draft_not_flagged(kb_root: Path) -> None:
    _make_wiki_draft(kb_root, slug="fresh-draft", started_at="2026-05-25T00:00:00Z")
    now = datetime(2026, 5, 26, 0, 0, 0, tzinfo=timezone.utc)
    results = _collect_stale_drafts(now=now, stale_days=7)
    slugs = [d.slug for d in results]
    assert "fresh-draft" not in slugs


def test_stale_draft_age_days(kb_root: Path) -> None:
    _make_wiki_draft(kb_root, slug="aged-draft", started_at="2026-05-01T00:00:00Z")
    now = datetime(2026, 5, 26, 0, 0, 0, tzinfo=timezone.utc)
    results = _collect_stale_drafts(now=now, stale_days=7)
    aged = next(d for d in results if d.slug == "aged-draft")
    assert aged.age_days == 25


def test_stale_drafts_sorted_oldest_first(kb_root: Path) -> None:
    _make_wiki_draft(kb_root, slug="very-old", started_at="2026-01-01T00:00:00Z")
    _make_wiki_draft(kb_root, slug="less-old", started_at="2026-04-01T00:00:00Z")
    now = datetime(2026, 5, 26, 0, 0, 0, tzinfo=timezone.utc)
    results = _collect_stale_drafts(now=now, stale_days=7)
    slugs = [d.slug for d in results]
    assert slugs.index("very-old") < slugs.index("less-old")


# --------------------------------------------------------------------------- #
# _collect_orphan_sources                                                      #
# --------------------------------------------------------------------------- #


def test_orphan_source_detected(kb_root: Path) -> None:
    _make_raw_source(kb_root, slug="orphan-src", wiki_pages=[])
    results = _collect_orphan_sources(limit=50)
    ids = [o.source_id for o in results]
    assert "orphan-src" in ids


def test_covered_source_not_orphan(kb_root: Path) -> None:
    _make_raw_source(
        kb_root,
        slug="covered-src",
        wiki_pages=["wiki/sources/covered-src.md"],
    )
    results = _collect_orphan_sources(limit=50)
    ids = [o.source_id for o in results]
    assert "covered-src" not in ids


def test_orphan_limit_respected(kb_root: Path) -> None:
    for i in range(10):
        _make_raw_source(kb_root, slug=f"orphan-{i}", wiki_pages=[])
    results = _collect_orphan_sources(limit=5)
    assert len(results) <= 5


# --------------------------------------------------------------------------- #
# _collect_recently_ingested                                                   #
# --------------------------------------------------------------------------- #


def test_recent_source_included(kb_root: Path) -> None:
    _make_raw_source(
        kb_root,
        slug="recent-src",
        ingested_at="2026-05-26T01:00:00Z",
        wiki_pages=["wiki/sources/recent-src.md"],
    )
    since = datetime(2026, 5, 26, 0, 0, 0, tzinfo=timezone.utc)
    results = _collect_recently_ingested(since=since)
    ids = [r.source_id for r in results]
    assert "recent-src" in ids


def test_old_source_excluded(kb_root: Path) -> None:
    _make_raw_source(
        kb_root,
        slug="old-src",
        ingested_at="2026-01-01T00:00:00Z",
    )
    since = datetime(2026, 5, 26, 0, 0, 0, tzinfo=timezone.utc)
    results = _collect_recently_ingested(since=since)
    ids = [r.source_id for r in results]
    assert "old-src" not in ids


def test_recently_ingested_sorted_newest_first(kb_root: Path) -> None:
    _make_raw_source(kb_root, slug="older", ingested_at="2026-05-26T01:00:00Z", wiki_pages=[])
    _make_raw_source(kb_root, slug="newer", ingested_at="2026-05-26T02:00:00Z", wiki_pages=[])
    since = datetime(2026, 5, 26, 0, 0, 0, tzinfo=timezone.utc)
    results = _collect_recently_ingested(since=since)
    ids = [r.source_id for r in results]
    assert ids.index("newer") < ids.index("older")


# --------------------------------------------------------------------------- #
# run_daily_review integration                                                 #
# --------------------------------------------------------------------------- #


def test_run_daily_review_returns_result(kb_root: Path) -> None:
    result = run_daily_review()
    assert isinstance(result, DailyReviewResult)
    assert result.as_of != ""


def test_run_daily_review_op_success(kb_root: Path) -> None:
    op = run_daily_review_op()
    assert op.success is True
    assert "Daily triage" in op.summary


# --------------------------------------------------------------------------- #
# format_daily_review                                                          #
# --------------------------------------------------------------------------- #


def test_format_sections_present(kb_root: Path) -> None:
    result = DailyReviewResult(as_of="2026-05-26T00:00:00Z")
    text = format_daily_review(result)
    assert "Inbox:" in text
    assert "New sources" in text
    assert "Stale drafts" in text
    assert "Orphan sources" in text


def test_format_shows_stale_draft(kb_root: Path) -> None:
    from gateway.ops.daily_review import DraftItem
    result = DailyReviewResult(
        as_of="2026-05-26T00:00:00Z",
        stale_drafts=[DraftItem(slug="old", title="Old Draft", age_days=10, wiki_path="wiki/synthesis/old.md")],
    )
    text = format_daily_review(result)
    assert "old.md" in text
    assert "10d" in text


# --------------------------------------------------------------------------- #
# MCP parity                                                                   #
# --------------------------------------------------------------------------- #


def test_mcp_wiki_daily_callable() -> None:
    from gateway import mcp_server
    assert callable(getattr(mcp_server, "wiki_daily", None)), (
        "wiki_daily must be registered as an MCP tool in mcp_server.py"
    )


# --------------------------------------------------------------------------- #
# Web route                                                                    #
# --------------------------------------------------------------------------- #


def test_today_route_returns_200(kb_root: Path) -> None:
    from fastapi.testclient import TestClient
    from gateway.web.app import create_app

    client = TestClient(create_app())
    resp = client.get("/today")
    assert resp.status_code == 200
    data = resp.json()
    assert "as_of" in data
    assert "inbox_count" in data
    assert "stale_drafts" in data
    assert "orphan_sources" in data
    assert "recently_ingested" in data


def test_today_route_respects_stale_days_param(kb_root: Path) -> None:
    from fastapi.testclient import TestClient
    from gateway.web.app import create_app

    client = TestClient(create_app())
    resp = client.get("/today?stale_days=1&lookback_hours=1")
    assert resp.status_code == 200
