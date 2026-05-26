"""ONT-11: backfill_synthesizes and synthesizes-coverage lint tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.lint.synthesizes_coverage import run as coverage_run
from gateway.lint import SEVERITY_ERROR
from gateway.ops.backfill_synthesizes import (
    _extract_candidates,
    _preferred_tier,
    backfill_synthesizes,
)


# --- unit tests for helpers -------------------------------------------------


def test_extract_candidates_sources():
    body = "Analysis [[sources/arxiv-2403-12345]] supports [[sources/pubmed-39847203]].\n"
    candidates = _extract_candidates(body)
    assert candidates == ["sources/arxiv-2403-12345", "sources/pubmed-39847203"]


def test_extract_candidates_synthesis():
    body = "Builds on [[synthesis/glp1-reward-modulation]] and [[synthesis/gi-appetite]].\n"
    candidates = _extract_candidates(body)
    assert candidates == ["synthesis/gi-appetite", "synthesis/glp1-reward-modulation"]


def test_extract_candidates_deduplicates():
    body = "[[sources/arxiv-2403-12345]] and [[sources/arxiv-2403-12345]] again.\n"
    candidates = _extract_candidates(body)
    assert candidates == ["sources/arxiv-2403-12345"]


def test_extract_candidates_ignores_other_wikilinks():
    body = "See [[concepts/food-noise]] and [[entities/glp1]] and [[sources/web-2026-01-01-abc]].\n"
    candidates = _extract_candidates(body)
    assert candidates == ["sources/web-2026-01-01-abc"]


def test_extract_candidates_empty_body():
    assert _extract_candidates("No wikilinks here.\n") == []


def test_preferred_tier_sources_only():
    candidates = ["sources/arxiv-001", "sources/pubmed-002"]
    assert _preferred_tier(candidates) == candidates


def test_preferred_tier_synthesis_only():
    candidates = ["synthesis/glp1-review", "synthesis/appetite"]
    assert _preferred_tier(candidates) == candidates


def test_preferred_tier_mixed_prefers_sources():
    candidates = ["sources/arxiv-001", "synthesis/glp1-review"]
    result = _preferred_tier(candidates)
    assert result == ["sources/arxiv-001"]
    assert "synthesis/glp1-review" not in result


# --- backfill_synthesizes integration tests ---------------------------------


def _make_synthesis(kb_root: Path, slug: str, body: str, synthesizes=None) -> Path:
    p = paths.wiki_dir() / "synthesis" / f"{slug}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    front: dict = {
        "type": "synthesis",
        "slug": slug,
        "title": slug.replace("-", " ").title(),
    }
    if synthesizes is not None:
        front["synthesizes"] = synthesizes
    p.write_text(fm.serialize(front, body))
    return p


def test_backfill_adds_synthesizes_from_wikilinks(kb_root):
    body = "Summary [[sources/arxiv-2403-12345]] and [[sources/pubmed-001]].\n"
    _make_synthesis(kb_root, "test-synth", body)

    result = backfill_synthesizes()
    assert result.success
    assert "1 updated" in result.summary

    p = paths.wiki_dir() / "synthesis" / "test-synth.md"
    front, _ = fm.parse(p.read_text())
    assert "synthesizes" in front
    assert set(front["synthesizes"]) == {"sources/arxiv-2403-12345", "sources/pubmed-001"}


def test_backfill_skips_pages_with_existing_synthesizes(kb_root):
    body = "Summary [[sources/arxiv-001]].\n"
    _make_synthesis(kb_root, "already-has-it", body, synthesizes=["sources/arxiv-001"])

    result = backfill_synthesizes()
    assert result.success
    assert "1 skipped" in result.summary


def test_backfill_skips_pages_with_no_qualifying_wikilinks(kb_root):
    body = "Just prose, no source links, [[concepts/food-noise]].\n"
    _make_synthesis(kb_root, "no-sources", body)

    result = backfill_synthesizes()
    assert result.success
    assert "1 skipped" in result.summary


def test_backfill_dry_run_does_not_write(kb_root):
    body = "Analysis [[sources/arxiv-2403-12345]].\n"
    p = _make_synthesis(kb_root, "dry-run-test", body)
    text_before = p.read_text()

    result = backfill_synthesizes(dry_run=True)
    assert result.success
    assert "dry-run" in result.summary
    assert p.read_text() == text_before  # unchanged


def test_backfill_resolves_mixed_to_sources(kb_root):
    body = "Based on [[sources/arxiv-001]] and [[synthesis/glp1-review]].\n"
    _make_synthesis(kb_root, "mixed-refs", body)

    backfill_synthesizes()
    p = paths.wiki_dir() / "synthesis" / "mixed-refs.md"
    front, _ = fm.parse(p.read_text())
    # Mixed → sources/ wins
    assert all(r.startswith("sources/") for r in front["synthesizes"])


def test_backfill_multiple_pages(kb_root):
    _make_synthesis(kb_root, "page-a", "[[sources/arxiv-001]].\n")
    _make_synthesis(kb_root, "page-b", "[[sources/pubmed-002]].\n")
    _make_synthesis(kb_root, "page-c", "[[sources/web-2026-01-01-abc]].\n")

    result = backfill_synthesizes()
    assert result.success
    assert "3 updated" in result.summary


def test_backfill_empty_synth_dir(kb_root):
    result = backfill_synthesizes()
    assert result.success
    assert "0 updated" in result.summary or "no synthesis dir" in result.summary


def test_backfill_is_idempotent(kb_root):
    body = "Analysis [[sources/arxiv-001]].\n"
    _make_synthesis(kb_root, "idempotent-page", body)

    first = backfill_synthesizes()
    second = backfill_synthesizes()
    assert first.success and second.success
    assert "1 updated" in first.summary
    assert "1 skipped" in second.summary


# --- synthesizes-coverage lint escalation -----------------------------------


def test_synthesizes_coverage_severity_is_error(kb_root):
    _make_synthesis(kb_root, "no-synthesizes", "Prose without wikilinks.\n")
    findings = coverage_run()
    assert len(findings) == 1
    assert findings[0].severity == SEVERITY_ERROR
    assert findings[0].check == "synthesizes-coverage"


def test_synthesizes_coverage_no_finding_when_set(kb_root):
    _make_synthesis(kb_root, "has-synthesizes", "[[sources/arxiv-001]].\n", synthesizes=["sources/arxiv-001"])
    findings = coverage_run()
    assert findings == []


def test_synthesizes_coverage_no_finding_empty_dir(kb_root):
    findings = coverage_run()
    assert findings == []
