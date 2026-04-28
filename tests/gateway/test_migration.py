"""Tests for M8: legacy slug detection, citation rewrite, vault migration."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from gateway import citations
from gateway import frontmatter as fm
from gateway import paths
from gateway import slugmap
from gateway.ops.batch_ingest import batch_ingest
from gateway.ops.migrate import migrate_vault


# --- fixtures ---------------------------------------------------------------


def _write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return path


@pytest.fixture
def synthetic_vault(tmp_path: Path) -> Path:
    """Build a minimal legacy vault fixture mimicking real research-notebook output."""
    vault = tmp_path / "obsidian_test"

    # YouTube source
    _write(
        vault / "sources" / "_5qjj2CzBSw.md",
        fm.serialize(
            {
                "type": "source",
                "video_id": "_5qjj2CzBSw",
                "url": "https://youtube.com/watch?v=_5qjj2CzBSw",
                "title": "Ozempic and the Brain",
                "channel": "Dr. Leaf Show",
                "duration": "PT55M34S",
                "publish_date": "2026-01-14T15:30:23Z",
                "relevance_score": 4,
                "tags": [],
            },
            "Legacy YouTube summary body for the Ozempic episode.\n",
        ),
    )

    # arXiv source
    _write(
        vault / "sources" / "arxiv_2404.01358.md",
        fm.serialize(
            {
                "type": "source-paper",
                "source_type": "arxiv",
                "url": "http://arxiv.org/abs/2404.01358v1",
                "title": "GLP-1 receptor agonism in mesolimbic circuitry",
                "authors": [{"name": "J. Liu"}],
                "publish_date": "2024-04-02",
                "relevance_score": 5,
            },
            "Legacy arXiv abstract body.\n",
        ),
    )

    # PubMed source
    _write(
        vault / "sources" / "pubmed_39847203.md",
        fm.serialize(
            {
                "type": "source-paper",
                "source_type": "pubmed",
                "pmid": "39847203",
                "url": "https://pubmed.ncbi.nlm.nih.gov/39847203/",
                "title": "Reward modulation by GLP-1RA: a review",
                "publish_date": "2025-02-01",
                "relevance_score": 3,
            },
            "Legacy PubMed abstract body.\n",
        ),
    )

    # Concept page with wikilink to the YouTube source slug
    _write(
        vault / "concepts" / "food-noise.md",
        fm.serialize(
            {
                "type": "concept",
                "concept_type": "phenomenon",
                "tags": ["mental-health"],
            },
            "# Food noise\n\n"
            "Food noise is reduced by GLP-1 RAs as discussed in [[_5qjj2CzBSw]] "
            "and confirmed by [[arxiv_2404.01358]].\n",
        ),
    )

    # Synthesis page that cites both sources/<slug> and bare <slug>
    _write(
        vault / "synthesis" / "dose-response.md",
        fm.serialize(
            {
                "type": "synthesis",
                "title": "Dose response synthesis",
            },
            "# Dose response synthesis\n\n"
            "Combining [[sources/_5qjj2CzBSw]] with [[pubmed_39847203]] reveals a clear pattern.\n",
        ),
    )

    # MOC
    _write(
        vault / "mocs" / "test-domain.md",
        fm.serialize(
            {"type": "moc"},
            "# Test domain — MOC\n\nKey concept: [[food-noise|Food noise]].\n",
        ),
    )

    return vault


# --- slugmap.py ------------------------------------------------------------


def test_detect_youtube_legacy_source(synthetic_vault):
    src = slugmap.detect_legacy_source(synthetic_vault / "sources" / "_5qjj2CzBSw.md")
    assert src is not None
    assert src.source_type == "youtube"
    assert src.canonical_id == "yt-_5qjj2CzBSw"


def test_detect_arxiv_strips_version(synthetic_vault):
    src = slugmap.detect_legacy_source(synthetic_vault / "sources" / "arxiv_2404.01358.md")
    assert src is not None
    assert src.source_type == "arxiv"
    assert src.canonical_id == "arxiv-2404.01358"


def test_detect_pubmed(synthetic_vault):
    src = slugmap.detect_legacy_source(synthetic_vault / "sources" / "pubmed_39847203.md")
    assert src is not None
    assert src.source_type == "pubmed"
    assert src.canonical_id == "pubmed-39847203"


def test_detect_unknown_returns_none(tmp_path):
    bogus = _write(
        tmp_path / "sources" / "weird.md",
        fm.serialize({"type": "source"}, "no identifying info"),
    )
    assert slugmap.detect_legacy_source(bogus) is None


def test_build_slug_map_maps_all_three(synthetic_vault):
    out = slugmap.build_slug_map(synthetic_vault)
    assert set(out.keys()) == {"_5qjj2CzBSw", "arxiv_2404.01358", "pubmed_39847203"}
    canonical_ids = {ls.canonical_id for ls in out.values()}
    assert canonical_ids == {"yt-_5qjj2CzBSw", "arxiv-2404.01358", "pubmed-39847203"}


def test_citation_mapping_covers_bare_and_qualified(synthetic_vault):
    slug_map = slugmap.build_slug_map(synthetic_vault)
    mapping = slugmap.citation_mapping(slug_map)
    assert mapping["_5qjj2CzBSw"] == "sources/yt-_5qjj2CzBSw"
    assert mapping["sources/_5qjj2CzBSw"] == "sources/yt-_5qjj2CzBSw"
    assert mapping["arxiv_2404.01358"] == "sources/arxiv-2404.01358"


def test_save_slug_map_writes_yaml(synthetic_vault, tmp_path):
    slug_map = slugmap.build_slug_map(synthetic_vault)
    target_dir = tmp_path / "audit"
    out = slugmap.save_slug_map("test-domain", slug_map, target_dir)
    data = yaml.safe_load(out.read_text())
    assert data["domain"] == "test-domain"
    assert data["count"] == 3
    assert {e["canonical_id"] for e in data["entries"]} == {
        "yt-_5qjj2CzBSw",
        "arxiv-2404.01358",
        "pubmed-39847203",
    }


# --- citations.rewrite_wikilinks ------------------------------------------


def test_rewrite_wikilinks_handles_bare_qualified_aliased_anchored():
    text = (
        "Bare: [[a]] | "
        "Qualified: [[sources/a]] | "
        "Aliased: [[a|Display]] | "
        "Anchored: [[a#sec]] | "
        "Both: [[a#sec|Display]] | "
        "Untouched: [[concepts/x]]"
    )
    out = citations.rewrite_wikilinks(text, {"a": "sources/yt-canon", "sources/a": "sources/yt-canon"})
    assert "[[sources/yt-canon]]" in out
    assert "[[sources/yt-canon|Display]]" in out
    assert "[[sources/yt-canon#sec]]" in out
    assert "[[sources/yt-canon#sec|Display]]" in out
    assert "[[concepts/x]]" in out  # not in mapping; untouched


def test_rewrite_wikilinks_no_mapping_is_identity():
    text = "stuff [[x]] more"
    assert citations.rewrite_wikilinks(text, {}) == text


# --- migrate_vault end-to-end ----------------------------------------------


def test_migrate_vault_dry_run_writes_only_audit(kb_root, synthetic_vault):
    result = migrate_vault(synthetic_vault, "test-domain", dry_run=True)
    assert result.success
    assert "DRY RUN" in result.summary

    audit = paths.knowledge_internal() / "migrations" / "test-domain-slug-map.yaml"
    assert audit.exists()
    # No raw or wiki files written on dry-run
    assert not list(paths.raw_dir_for("youtube").glob("*.md"))
    assert not list((paths.wiki_dir() / "concepts").glob("*.md"))


def test_migrate_vault_writes_raw_sources_and_wiki_pages(kb_root, synthetic_vault):
    result = migrate_vault(synthetic_vault, "test-domain")
    assert result.success, result.errors

    # Raw sources written under correct type directories
    yt_path = paths.raw_source_path("youtube", "yt-_5qjj2CzBSw")
    arxiv_path = paths.raw_source_path("arxiv", "arxiv-2404.01358")
    pubmed_path = paths.raw_source_path("pubmed", "pubmed-39847203")
    assert yt_path.exists() and arxiv_path.exists() and pubmed_path.exists()

    # Each has canonical frontmatter shape
    front, body = fm.parse(yt_path.read_text())
    assert front["id"] == "yt-_5qjj2CzBSw"
    assert front["type"] == "youtube"
    assert front["domains"] == ["test-domain"]
    assert front["meta"]["legacy_recovery"] == "summary-only"
    # Legacy relevance_score=4 → filter.score = 0.8
    assert front["filter"]["score"] == 0.8
    assert front["filter"]["policy_version"] == "test-domain-legacy-v1"
    assert "Legacy YouTube summary body" in body

    # Wiki source pages written
    assert paths.wiki_source_path("yt-_5qjj2CzBSw").exists()
    assert paths.wiki_source_path("arxiv-2404.01358").exists()
    assert paths.wiki_source_path("pubmed-39847203").exists()


def test_migrate_vault_rewrites_concept_citations(kb_root, synthetic_vault):
    migrate_vault(synthetic_vault, "test-domain")

    concept = paths.wiki_dir() / "concepts" / "food-noise.md"
    assert concept.exists()
    front, body = fm.parse(concept.read_text())
    assert front["draft"] is True
    assert front["legacy_provenance"]["legacy_concept_type"] == "phenomenon"
    # Citations rewritten
    assert "[[sources/yt-_5qjj2CzBSw]]" in body
    assert "[[sources/arxiv-2404.01358]]" in body
    assert "[[_5qjj2CzBSw]]" not in body
    # Required sections backfilled
    assert "## Summary" in body
    assert "## Key claims" in body
    assert "## Sources" in body
    assert "## Related" in body


def test_migrate_vault_synthesis_handles_qualified_and_bare_links(kb_root, synthetic_vault):
    migrate_vault(synthetic_vault, "test-domain")

    syn = paths.wiki_dir() / "synthesis" / "dose-response.md"
    assert syn.exists()
    front, body = fm.parse(syn.read_text())
    assert front["draft"] is True
    assert front["question"]
    # Both forms rewritten
    assert "[[sources/yt-_5qjj2CzBSw]]" in body
    assert "[[sources/pubmed-39847203]]" in body
    # Required synthesis sections
    assert "## Synthesis" in body
    assert "## Sources cited" in body


def test_migrate_vault_moc_committed_with_required_sections(kb_root, synthetic_vault):
    migrate_vault(synthetic_vault, "test-domain")

    moc = paths.wiki_dir() / "mocs" / "test-domain.md"
    assert moc.exists()
    front, body = fm.parse(moc.read_text())
    assert front["type"] == "moc"
    assert front["domain"] == "test-domain"
    # Required MOC sections
    for s in ("Overview", "Key entities", "Key concepts", "Synthesis pages"):
        assert f"## {s}" in body


def test_migrate_vault_log_entry_recorded(kb_root, synthetic_vault):
    migrate_vault(synthetic_vault, "test-domain")
    log_text = paths.log_path().read_text()
    assert "migrate" in log_text
    assert "test-domain" in log_text
    assert "youtube=1" in log_text and "arxiv=1" in log_text and "pubmed=1" in log_text


def test_migrate_vault_missing_directory_errors(kb_root, tmp_path):
    result = migrate_vault(tmp_path / "nope", "test-domain")
    assert not result.success
    assert any("not found" in e for e in result.errors)


def test_migrate_vault_empty_sources_errors(kb_root, tmp_path):
    (tmp_path / "obsidian_empty" / "sources").mkdir(parents=True)
    result = migrate_vault(tmp_path / "obsidian_empty", "test-domain")
    assert not result.success
    assert any("no legacy sources" in e for e in result.errors)


# --- batch_ingest dispatcher ----------------------------------------------


def test_batch_ingest_requires_legacy_import_flag(kb_root, synthetic_vault):
    result = batch_ingest(synthetic_vault, domain="test-domain")
    assert not result.success
    assert any("--legacy-import" in e for e in result.errors)


def test_batch_ingest_requires_domain(kb_root, synthetic_vault):
    result = batch_ingest(synthetic_vault, legacy_import=True)
    assert not result.success
    assert any("--domain" in e for e in result.errors)


def test_batch_ingest_dispatches_to_migrate_vault(kb_root, synthetic_vault):
    result = batch_ingest(
        synthetic_vault, legacy_import=True, domain="test-domain", dry_run=True
    )
    assert result.success
    assert "DRY RUN" in result.summary
