"""SRCH-1: wiki search full-text search tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.ops.search import (
    SearchHit,
    SearchResult,
    format_results,
    search,
)


# --- helpers ----------------------------------------------------------------


def _make_wiki_page(
    kb_root: Path,
    page_type: str,
    slug: str,
    title: str,
    domain: str = "test-domain",
    body: str = "Page body content.",
) -> Path:
    type_dir = paths.wiki_dir() / f"{page_type}s"
    type_dir.mkdir(parents=True, exist_ok=True)
    p = type_dir / f"{slug}.md"
    front = {
        "type": page_type,
        "slug": slug,
        "title": title,
        "domains": [domain],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-05-01T00:00:00Z",
    }
    p.write_text(fm.serialize(front, body))
    return p


def _make_raw_source(
    kb_root: Path,
    source_type: str,
    source_id: str,
    title: str,
    body: str = "Source body.",
    domain: str = "test-domain",
) -> Path:
    from gateway import validator
    p = paths.raw_source_path(source_type, source_id)
    p.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "id": source_id,
        "title": title,
        "type": source_type,
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": validator.compute_content_hash(body),
        "domains": [domain],
    }
    p.write_text(fm.serialize(front, body))
    return p


# --- search() ---------------------------------------------------------------


def test_search_empty_query(kb_root: Path):
    result = search("")
    assert result.hits == []
    assert result.total == 0


def test_search_title_match(kb_root: Path):
    _make_wiki_page(kb_root, "concept", "glp1-weight-loss", "GLP-1 and Weight Loss")
    result = search("weight loss")
    assert result.total >= 1
    hit = result.hits[0]
    assert hit.score == 3
    assert "weight loss" in hit.title.lower()


def test_search_slug_match(kb_root: Path):
    _make_wiki_page(kb_root, "concept", "reward-blunting", "Reward Blunting Phenomenon", body="Unrelated content here.")
    result = search("reward-blunting")
    assert result.total >= 1
    hit = next(h for h in result.hits if h.slug == "reward-blunting")
    assert hit.score >= 2


def test_search_body_match(kb_root: Path):
    _make_wiki_page(kb_root, "synthesis", "food-noise-review", "Food Noise Review", body="Patients report reduced food noise after dosing.")
    result = search("food noise")
    assert result.total >= 1
    body_hit = next((h for h in result.hits if h.slug == "food-noise-review"), None)
    assert body_hit is not None


def test_search_no_match(kb_root: Path):
    _make_wiki_page(kb_root, "concept", "semaglutide", "Semaglutide")
    result = search("zzznomatch999")
    assert result.total == 0
    assert result.hits == []


def test_search_score_ordering(kb_root: Path):
    _make_wiki_page(kb_root, "concept", "ozempic-info", "Ozempic Drug Info", body="No match here.")
    _make_wiki_page(kb_root, "synthesis", "ozempic-review", "Summary Page", body="Ozempic is effective for weight loss.")
    result = search("ozempic")
    assert result.hits[0].score >= result.hits[-1].score


def test_search_scope_wiki_only(kb_root: Path):
    _make_wiki_page(kb_root, "concept", "wiki-only-page", "Wiki Only Term")
    _make_raw_source(kb_root, "web", "web-2026-01-01-abc", "Wiki Only Term Raw")
    result = search("Wiki Only Term", scope="wiki")
    assert all("wiki/" in str(h.path) for h in result.hits)


def test_search_scope_raw_only(kb_root: Path):
    _make_wiki_page(kb_root, "concept", "raw-only-concept", "Raw Only Concept")
    _make_raw_source(kb_root, "web", "web-2026-01-01-def", "Raw Source Match")
    result = search("Raw Source Match", scope="raw")
    assert all("raw/" in str(h.path) for h in result.hits)


def test_search_domain_filter(kb_root: Path):
    _make_wiki_page(kb_root, "concept", "glp1-concept", "GLP-1 Concept", domain="glp1-reward-modulation")
    _make_wiki_page(kb_root, "concept", "other-concept", "GLP-1 Other Concept", domain="edge-ai-agentic")
    result = search("glp-1", domain="glp1-reward-modulation")
    assert all(h.domain == "glp1-reward-modulation" for h in result.hits)


def test_search_type_filter(kb_root: Path):
    _make_wiki_page(kb_root, "concept", "test-concept", "Test Matching Concept")
    _make_wiki_page(kb_root, "synthesis", "test-synthesis", "Test Matching Synthesis")
    result = search("test matching", page_type="concept")
    assert all(h.page_type == "concept" for h in result.hits)


def test_search_limit(kb_root: Path):
    for i in range(10):
        _make_wiki_page(kb_root, "concept", f"limit-test-{i}", f"Limit Test Page {i}")
    result = search("limit test", limit=3)
    assert len(result.hits) <= 3
    assert result.total >= 3


def test_search_case_insensitive(kb_root: Path):
    _make_wiki_page(kb_root, "concept", "case-test", "Case Sensitivity Test")
    r1 = search("case sensitivity")
    r2 = search("CASE SENSITIVITY")
    r3 = search("Case Sensitivity")
    assert r1.total == r2.total == r3.total


def test_search_raw_source(kb_root: Path):
    _make_raw_source(kb_root, "web", "web-2026-05-01-xyz", "Unique Raw Source Title")
    result = search("Unique Raw Source Title")
    assert result.total >= 1
    hit = next(h for h in result.hits if h.slug == "web-2026-05-01-xyz")
    assert hit.score == 3


# --- format_results() -------------------------------------------------------


def test_format_results_empty():
    result = SearchResult(query="nothing", total=0)
    out = format_results(result)
    assert "No results" in out


def test_format_results_with_hits(kb_root: Path):
    _make_wiki_page(kb_root, "concept", "fmt-test", "Format Test Page", body="Searchable content.")
    result = search("format test")
    out = format_results(result, relative_to=paths.knowledge_root())
    assert "fmt-test" in out
    assert "Format Test Page" not in out or "fmt-test" in out  # path shown


def test_format_results_shows_total(kb_root: Path):
    _make_wiki_page(kb_root, "concept", "tot-test", "Total Test")
    result = search("total test")
    out = format_results(result)
    assert "result" in out


# --- MCP parity check -------------------------------------------------------


def test_mcp_wiki_search_registered():
    """wiki_search must be a callable in mcp_server (not CLI_ONLY)."""
    from gateway import mcp_server
    assert callable(getattr(mcp_server, "wiki_search", None))
