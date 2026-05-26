"""SRCH-2: wiki index --rebuild tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from gateway import frontmatter as fm, paths
from gateway.ops.index_rebuild import (
    _collect_domains,
    _collect_wiki_pages,
    _count_raw_sources,
    _render_index,
    rebuild,
)


# --- helpers ----------------------------------------------------------------


def _make_moc(kb_root: Path, domain: str) -> Path:
    d = paths.wiki_dir() / "mocs"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{domain}.md"
    front = {"type": "moc", "slug": domain, "domain": domain, "last_updated": "2026-01-01T00:00:00Z"}
    p.write_text(fm.serialize(front, f"# {domain} MOC\n"))
    return p


def _make_wiki_page(
    kb_root: Path,
    page_type: str,
    slug: str,
    domain: str | None = "test-domain",
    domains: list[str] | None = None,
) -> Path:
    _TYPE_TO_DIR = {
        "entity": "entities",
        "concept": "concepts",
        "synthesis": "synthesis",
        "moc": "mocs",
        "source": "sources",
        "artifact": "artifacts",
        "proposal": "proposals",
    }
    dir_name = _TYPE_TO_DIR.get(page_type, f"{page_type}s")
    d = paths.wiki_dir() / dir_name
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{slug}.md"
    front: dict[str, Any] = {
        "type": page_type,
        "slug": slug,
        "title": f"{slug} title",
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-05-01T00:00:00Z",
    }
    if domains is not None:
        front["domains"] = domains
    elif domain:
        front["domains"] = [domain]
    p.write_text(fm.serialize(front, f"Body for {slug}."))
    return p


def _make_raw_source(kb_root: Path, source_id: str, domain: str = "test-domain") -> Path:
    from gateway import validator
    body = "Source body."
    p = paths.raw_source_path("web", source_id)
    p.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "id": source_id,
        "title": f"Source {source_id}",
        "type": "web",
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": validator.compute_content_hash(body),
        "domains": [domain] if domain else [],
    }
    p.write_text(fm.serialize(front, body))
    return p


# --- _collect_domains -------------------------------------------------------


def test_collect_domains_empty(kb_root: Path):
    domains = _collect_domains()
    assert isinstance(domains, set)


def test_collect_domains_finds_moc(kb_root: Path):
    _make_moc(kb_root, "glp1-reward-modulation")
    domains = _collect_domains()
    assert "glp1-reward-modulation" in domains


def test_collect_domains_multiple(kb_root: Path):
    _make_moc(kb_root, "domain-a")
    _make_moc(kb_root, "domain-b")
    domains = _collect_domains()
    assert {"domain-a", "domain-b"}.issubset(domains)


# --- _count_raw_sources -----------------------------------------------------


def test_count_raw_sources_empty(kb_root: Path):
    counts = _count_raw_sources()
    assert isinstance(counts, dict)


def test_count_raw_sources_by_domain(kb_root: Path):
    _make_raw_source(kb_root, "web-2026-01-01-aaa", domain="domain-x")
    _make_raw_source(kb_root, "web-2026-01-01-bbb", domain="domain-x")
    _make_raw_source(kb_root, "web-2026-01-01-ccc", domain="domain-y")
    counts = _count_raw_sources()
    assert counts.get("domain-x", 0) >= 2
    assert counts.get("domain-y", 0) >= 1


def test_count_raw_sources_untagged(kb_root: Path):
    _make_raw_source(kb_root, "web-2026-01-01-zzz", domain="")
    counts = _count_raw_sources()
    assert counts.get("__untagged__", 0) >= 1


# --- _collect_wiki_pages ----------------------------------------------------


def test_collect_wiki_pages_empty(kb_root: Path):
    result = _collect_wiki_pages()
    assert isinstance(result, dict)


def test_collect_wiki_pages_by_domain_and_type(kb_root: Path):
    _make_wiki_page(kb_root, "entity", "test-entity", domain="domain-a")
    _make_wiki_page(kb_root, "concept", "test-concept", domain="domain-a")
    result = _collect_wiki_pages()
    assert "test-entity" in result.get("domain-a", {}).get("entity", [])
    assert "test-concept" in result.get("domain-a", {}).get("concept", [])


def test_collect_wiki_pages_multi_domain(kb_root: Path):
    _make_wiki_page(kb_root, "synthesis", "cross-syn", domains=["domain-a", "domain-b"])
    result = _collect_wiki_pages()
    assert "cross-syn" in result.get("domain-a", {}).get("synthesis", [])
    assert "cross-syn" in result.get("domain-b", {}).get("synthesis", [])


# --- rebuild() --------------------------------------------------------------


def test_rebuild_dry_run_no_write(kb_root: Path):
    _make_moc(kb_root, "test-domain")
    _make_raw_source(kb_root, "web-2026-01-01-dry", domain="test-domain")
    original = paths.index_path().read_text() if paths.index_path().exists() else ""
    result = rebuild(dry_run=True)
    assert result.success
    if original:
        assert paths.index_path().read_text() == original


def test_rebuild_writes_index(kb_root: Path):
    _make_moc(kb_root, "research-domain")
    _make_raw_source(kb_root, "web-2026-01-01-idx", domain="research-domain")
    _make_wiki_page(kb_root, "concept", "key-concept", domain="research-domain")
    result = rebuild(dry_run=False)
    assert result.success
    assert paths.index_path().exists()
    content = paths.index_path().read_text()
    assert "# Knowledge Index" in content
    assert "research-domain" in content
    assert "Last rebuilt:" in content


def test_rebuild_includes_domain_section(kb_root: Path):
    _make_moc(kb_root, "glp1")
    _make_raw_source(kb_root, "web-2026-01-01-g1", domain="glp1")
    _make_wiki_page(kb_root, "concept", "food-noise", domain="glp1")
    result = rebuild(dry_run=False)
    content = paths.index_path().read_text()
    assert "### glp1" in content
    assert "food-noise" in content


def test_rebuild_health_section(kb_root: Path):
    result = rebuild(dry_run=False)
    content = paths.index_path().read_text()
    assert "## Health" in content
    assert "Orphans:" in content
    assert "Untriaged inbox:" in content


def test_rebuild_result_data(kb_root: Path):
    _make_moc(kb_root, "domain-z")
    result = rebuild(dry_run=False)
    assert result.data.get("domains", 0) >= 1
    assert "raw_sources" in result.data


def test_rebuild_counts_in_header(kb_root: Path):
    _make_moc(kb_root, "counting-domain")
    _make_raw_source(kb_root, "web-2026-05-01-c1", domain="counting-domain")
    _make_raw_source(kb_root, "web-2026-05-01-c2", domain="counting-domain")
    _make_wiki_page(kb_root, "entity", "entity-one", domain="counting-domain")
    rebuild(dry_run=False)
    content = paths.index_path().read_text()
    assert "Sources:" in content
    assert "Entities:" in content


def test_rebuild_cross_domain_section(kb_root: Path):
    _make_moc(kb_root, "domain-x")
    _make_moc(kb_root, "domain-y")
    _make_wiki_page(kb_root, "synthesis", "cross-synthesis", domains=["domain-x", "domain-y"])
    rebuild(dry_run=False)
    content = paths.index_path().read_text()
    assert "## Cross-domain" in content
    assert "cross-synthesis" in content


# --- MCP registration check -------------------------------------------------


def test_mcp_wiki_index_rebuild_registered():
    from gateway import mcp_server
    assert callable(getattr(mcp_server, "wiki_index", None))
