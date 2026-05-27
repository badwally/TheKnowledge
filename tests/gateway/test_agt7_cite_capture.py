"""AGT-7: capture-to-cite — cite_capture() tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.ops.cite_capture import (
    _find_source_by_url,
    _find_target_by_overlap,
    _normalize_url,
    _tokenize,
    cite_capture,
)
from gateway.core import OperationResult


# --------------------------------------------------------------------------- #
# Helpers                                                                      #
# --------------------------------------------------------------------------- #


def _make_raw_source(
    kb_root: Path,
    *,
    source_id: str = "web-2026-test-abc",
    source_type: str = "web",
    url: str = "https://example.com/paper",
    title: str = "Test Paper",
    wiki_pages: list[str] | None = None,
) -> Path:
    d = paths.raw_dir() / source_type
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{source_id}.md"
    front = {
        "id": source_id,
        "type": source_type,
        "url": url,
        "title": title,
        "ingested_at": "2026-05-01T00:00:00Z",
        "wiki_pages": wiki_pages or [],
        "domains": [],
    }
    p.write_text(fm.serialize(front, "body text"))
    return p


def _make_wiki_source_page(kb_root: Path, source_id: str = "web-2026-test-abc") -> Path:
    d = paths.wiki_dir() / "sources"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{source_id}.md"
    front = {"type": "source", "slug": source_id, "title": "Test Paper", "sources": []}
    p.write_text(fm.serialize(front, f"## Summary\n\nSummary of {source_id}.\n"))
    return p


def _make_wiki_page(
    kb_root: Path,
    *,
    sub: str = "concepts",
    slug: str = "food-noise",
    title: str = "Food Noise",
    body: str = "Food noise is a persistent mental chatter about food.\n",
    draft: bool = False,
) -> Path:
    d = paths.wiki_dir() / sub
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{slug}.md"
    front: dict = {
        "type": "concept",
        "slug": slug,
        "title": title,
        "sources": [],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    if draft:
        front["draft"] = True
    p.write_text(fm.serialize(front, body))
    return p


# --------------------------------------------------------------------------- #
# _normalize_url                                                               #
# --------------------------------------------------------------------------- #


def test_normalize_strips_trailing_slash() -> None:
    assert _normalize_url("https://example.com/") == _normalize_url("https://example.com")


def test_normalize_strips_query_params() -> None:
    assert _normalize_url("https://example.com/page?foo=bar") == _normalize_url("https://example.com/page")


def test_normalize_lowercases() -> None:
    assert _normalize_url("https://EXAMPLE.COM/Page") == "https://example.com/page"


# --------------------------------------------------------------------------- #
# _find_source_by_url                                                          #
# --------------------------------------------------------------------------- #


def test_find_source_by_url_hit(kb_root: Path) -> None:
    _make_raw_source(kb_root, url="https://example.com/paper")
    result = _find_source_by_url("https://example.com/paper")
    assert result is not None
    source_id, source_type = result
    assert source_id == "web-2026-test-abc"
    assert source_type == "web"


def test_find_source_by_url_normalizes(kb_root: Path) -> None:
    _make_raw_source(kb_root, url="https://example.com/paper/")
    result = _find_source_by_url("https://example.com/paper")
    assert result is not None


def test_find_source_by_url_miss(kb_root: Path) -> None:
    result = _find_source_by_url("https://notingested.example.com/")
    assert result is None


# --------------------------------------------------------------------------- #
# _tokenize + _find_target_by_overlap                                         #
# --------------------------------------------------------------------------- #


def test_tokenize_filters_short_words() -> None:
    tokens = _tokenize("the cat sat on mat")
    assert "the" not in tokens
    assert "sat" not in tokens  # 3 chars
    assert "cat" not in tokens  # 3 chars


def test_tokenize_filters_stop_words() -> None:
    tokens = _tokenize("this food noise concept")
    assert "this" not in tokens
    assert "food" in tokens
    assert "noise" in tokens


def test_find_target_by_overlap_matches(kb_root: Path) -> None:
    _make_wiki_page(kb_root, slug="food-noise", title="Food Noise")
    target = _find_target_by_overlap("Food noise is persistent mental chatter about food")
    assert target is not None
    assert "food-noise" in target


def test_find_target_by_overlap_no_match_returns_none(kb_root: Path) -> None:
    target = _find_target_by_overlap("xyzzy quux")
    assert target is None


# --------------------------------------------------------------------------- #
# cite_capture — validation                                                    #
# --------------------------------------------------------------------------- #


def test_cite_capture_empty_quote_fails(kb_root: Path) -> None:
    result = cite_capture("", "https://example.com")
    assert not result.success
    assert any("quote" in e for e in result.errors)


def test_cite_capture_empty_url_fails(kb_root: Path) -> None:
    result = cite_capture("Some claim.", "")
    assert not result.success
    assert any("url" in e for e in result.errors)


# --------------------------------------------------------------------------- #
# cite_capture — URL already ingested path                                     #
# --------------------------------------------------------------------------- #


def test_cite_capture_reuses_ingested_source(kb_root: Path) -> None:
    """When URL is already ingested, cite_capture skips re-ingest."""
    _make_raw_source(kb_root, source_id="web-2026-test-abc", url="https://example.com/paper")
    _make_wiki_source_page(kb_root, "web-2026-test-abc")
    _make_wiki_page(
        kb_root,
        slug="food-noise",
        body="Food noise is a persistent mental chatter about food.\n",
    )

    result = cite_capture(
        "Food noise is a persistent mental chatter about food.",
        "https://example.com/paper",
        target_page="wiki/concepts/food-noise.md",
    )
    assert result.success
    assert "reused" in result.summary
    assert "web-2026-test-abc" in result.summary


# --------------------------------------------------------------------------- #
# cite_capture — no target auto-pick fallback                                  #
# --------------------------------------------------------------------------- #


def test_cite_capture_no_target_no_overlap_fails(kb_root: Path) -> None:
    """When auto-pick finds nothing, returns failure with informative error."""
    _make_raw_source(kb_root, source_id="web-2026-test-abc", url="https://example.com/paper")
    _make_wiki_source_page(kb_root, "web-2026-test-abc")
    # No wiki pages to overlap with

    result = cite_capture(
        "xyzzy quux unique token",
        "https://example.com/paper",
    )
    assert not result.success
    assert "auto-pick" in result.errors[0] or "target" in result.errors[0].lower()


# --------------------------------------------------------------------------- #
# MCP parity                                                                   #
# --------------------------------------------------------------------------- #


def test_mcp_wiki_cite_capture_callable() -> None:
    from gateway import mcp_server
    assert callable(getattr(mcp_server, "wiki_cite_capture", None)), (
        "wiki_cite_capture must be registered as an MCP tool in mcp_server.py"
    )


# --------------------------------------------------------------------------- #
# CLI registration                                                             #
# --------------------------------------------------------------------------- #


def test_cli_cite_capture_registered() -> None:
    from gateway.cli import IMPLEMENTED, SUBCOMMANDS
    assert "cite-capture" in IMPLEMENTED
    assert "cite-capture" in SUBCOMMANDS
