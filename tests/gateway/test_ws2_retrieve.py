"""WS2: wiki retrieve composite RAG primitive tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths, search_index
from gateway.ops.retrieve import retrieve, retrieve_op


def _page(slug: str, title: str, body: str, domain: str = "d", draft: bool = False) -> None:
    d = paths.wiki_dir() / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept", "slug": slug, "title": title, "domains": [domain],
        "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z",
    }
    if draft:
        front["draft"] = True
    (d / f"{slug}.md").write_text(fm.serialize(front, body))


def test_retrieve_returns_wrapped_block(kb_root: Path):
    _page(
        "gastric", "Gastric emptying",
        "## Mechanism\n\nThe drug delays gastric emptying via vagal signaling.\n",
    )
    search_index.refresh(rebuild=True)
    block, sections = retrieve("gastric emptying vagal", domain="d")
    assert sections
    assert "<page " in block and "</page>" in block
    assert 'section="Mechanism"' in block
    assert "vagal signaling" in block


def test_retrieve_preserves_source_citations(kb_root: Path):
    _page(
        "cited", "Cited concept",
        "## Body\n\nA claim grounded in evidence [[sources/web-2026-01-01-abc]].\n",
    )
    search_index.refresh(rebuild=True)
    block, _ = retrieve("claim grounded evidence", domain="d")
    assert "[[sources/web-2026-01-01-abc]]" in block


def test_retrieve_respects_budget(kb_root: Path):
    for i in range(6):
        _page(f"p{i}", f"Page {i}", f"## S{i}\n\n" + ("token alpha " * 200) + "\n")
    search_index.refresh(rebuild=True)
    block, sections = retrieve("token alpha", domain="d", budget_chars=1500)
    assert len(block) <= 1500 + 2000  # last section may overshoot by one block
    assert len(sections) < 6


def test_retrieve_caps_section_size(kb_root: Path):
    _page("big", "Big page", "## Huge\n\n" + ("word " * 5000) + "\n")
    search_index.refresh(rebuild=True)
    _block, sections = retrieve("word", domain="d", max_section_chars=500)
    assert sections
    assert "[section truncated]" in sections[0].text
    assert len(sections[0].text) <= 600


def test_retrieve_excludes_drafts_by_default(kb_root: Path):
    _page("draftp", "Draft term page", "## X\n\nunique draftonly content here.\n", draft=True)
    search_index.refresh(rebuild=True)
    _block, sections = retrieve("draftonly content", domain="d")
    assert sections == []


def test_retrieve_empty_query(kb_root: Path):
    block, sections = retrieve("", domain="d")
    assert block == "" and sections == []


def test_retrieve_op_no_results(kb_root: Path):
    _page("x", "X", "## Y\n\ncontent.\n")
    search_index.refresh(rebuild=True)
    result = retrieve_op("nonexistent quantum chromodynamics", domain="d")
    assert not result.success
    assert "no results" in result.summary


def test_retrieve_op_success_logs_and_returns_data(kb_root: Path):
    _page("topic", "Topic page", "## Detail\n\nrelevant detail about widgets.\n")
    search_index.refresh(rebuild=True)
    result = retrieve_op("relevant widgets", domain="d", caller="test")
    assert result.success
    assert result.data["section_count"] >= 1
    assert result.data["sources"][0]["path"].startswith("wiki/concepts/")
    assert paths.log_path() in result.paths_touched


def test_retrieve_op_xml_escaping(kb_root: Path):
    # Title with special chars must not break the <page> attributes.
    _page("amp", "Tax & Form <1120>", "## Filing\n\nhow to file the form.\n")
    search_index.refresh(rebuild=True)
    block, _ = retrieve("file the form", domain="d")
    assert "&amp;" in block and "&lt;1120&gt;" in block


def test_mcp_wiki_retrieve_registered():
    from gateway import mcp_server
    assert hasattr(mcp_server, "wiki_retrieve")


def test_retrieve_multi_domain_balances_quota(kb_root: Path):
    # alpha dominates lexically (5 matching pages); beta has 2.
    for i in range(5):
        _page(f"a{i}", f"Alpha {i}", f"## S\n\nshared signal token alpha-{i}.\n", domain="alpha")
    for i in range(2):
        _page(f"b{i}", f"Beta {i}", f"## S\n\nshared signal token beta-{i}.\n", domain="beta")
    search_index.refresh(rebuild=True)

    # Single global call collapses toward the dominant domain...
    _block_single, single = retrieve("shared signal token", k=4)
    assert {s.domain for s in single} == {"alpha"}, "precondition: global call collapses to alpha"

    # ...multi-domain quota merge must surface BOTH named domains.
    _block, sections = retrieve("shared signal token", domains=["alpha", "beta"], k=4)
    doms = {s.domain for s in sections}
    assert "alpha" in doms and "beta" in doms, f"expected both domains, got {doms}"


def test_retrieve_multi_domain_dedups_and_survives_budget(kb_root: Path):
    # One page tagged to BOTH domains.
    d = paths.wiki_dir() / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    both = {
        "type": "concept", "slug": "dual", "title": "Dual tagged",
        "domains": ["alpha", "beta"],
        "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z",
    }
    (d / "dual.md").write_text(fm.serialize(both, "## S\n\nshared signal token dual.\n"))
    # Plus several large single-domain pages so the budget truncates well below
    # the merged set (8 distinct pages; a budget that admits only ~3 sections).
    for i in range(4):
        _page(f"a{i}", f"Alpha {i}", "## S\n\nshared signal token " + ("alpha " * 300), domain="alpha")
    for i in range(4):
        _page(f"b{i}", f"Beta {i}", "## S\n\nshared signal token " + ("beta " * 300), domain="beta")
    search_index.refresh(rebuild=True)

    _block, sections = retrieve(
        "shared signal token", domains=["alpha", "beta"], k=8, budget_chars=6000,
    )
    paths_seen = [s.rel_path for s in sections]
    assert len(paths_seen) == len(set(paths_seen)), "no page should appear twice"
    assert len(sections) < 8, "budget should truncate the merged set"
    assert {s.domain for s in sections} >= {"alpha", "beta"}, "balance survives truncation"


def test_retrieve_op_accepts_domains(kb_root: Path):
    for i in range(3):
        _page(f"a{i}", f"Alpha {i}", f"## S\n\nshared signal token a{i}.\n", domain="alpha")
    _page("b0", "Beta 0", "## S\n\nshared signal token b0.\n", domain="beta")
    search_index.refresh(rebuild=True)
    res = retrieve_op("shared signal token", domains=["alpha", "beta"], k=4)
    assert res.success
    assert res.data["section_count"] >= 2


def test_mcp_wiki_retrieve_accepts_domains(kb_root: Path):
    from gateway.mcp_server import wiki_retrieve
    for i in range(3):
        _page(f"a{i}", f"Alpha {i}", f"## S\n\nshared signal token a{i}.\n", domain="alpha")
    _page("b0", "Beta 0", "## S\n\nshared signal token b0.\n", domain="beta")
    search_index.refresh(rebuild=True)
    res = wiki_retrieve("shared signal token", domains="alpha,beta", k=4)
    assert res["success"]
    # _serialize exposes the assembled block as `summary`; both named domains
    # must appear as <page domain="..."> attributes (balanced, not collapsed).
    assert 'domain="alpha"' in res["summary"]
    assert 'domain="beta"' in res["summary"]
