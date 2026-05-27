"""ONT-7: per-claim confidence validation and lint distribution."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.lint.claim_confidence import (
    CONFIDENCE_TIERS,
    run_distribution,
    run_propagation,
)
from gateway.validator import validate_wiki_page_frontmatter


# --------------------------------------------------------------------------- #
# Helpers                                                                      #
# --------------------------------------------------------------------------- #


def _make_synthesis(
    kb_root: Path,
    *,
    slug: str = "test-synthesis",
    confidence: str | None = None,
    synthesizes: list[str] | None = None,
    domains: list[str] | None = None,
) -> Path:
    d = paths.wiki_dir() / "synthesis"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{slug}.md"
    front: dict = {
        "type": "synthesis",
        "slug": slug,
        "title": slug.replace("-", " ").title(),
        "domains": domains or ["test"],
        "question": "What?",
        "sources_count": 0,
        "synthesizes": synthesizes or [],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    if confidence is not None:
        front["confidence"] = confidence
    included = "\n".join(
        f"- [[{ref}]]" for ref in (synthesizes or [])
    )
    body = f"## Included works\n\n{included}\n" if synthesizes else "## Included works\n\n"
    p.write_text(fm.serialize(front, body))
    return p


def _make_source_wiki_page(
    kb_root: Path,
    *,
    source_id: str = "arxiv-2401-00001",
    confidence: str | None = None,
) -> Path:
    d = paths.wiki_dir() / "sources"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{source_id}.md"
    front: dict = {
        "type": "source",
        "slug": source_id,
        "title": "Test Source",
        "sources": [],
    }
    if confidence is not None:
        front["confidence"] = confidence
    p.write_text(fm.serialize(front, "## Summary\n\nA source.\n"))
    return p


def _make_concept(
    kb_root: Path,
    *,
    slug: str = "test-concept",
    confidence: str | None = None,
    domains: list[str] | None = None,
) -> Path:
    d = paths.wiki_dir() / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{slug}.md"
    front: dict = {
        "type": "concept",
        "slug": slug,
        "title": slug.replace("-", " ").title(),
        "domains": domains or ["test"],
        "sources": [],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    if confidence is not None:
        front["confidence"] = confidence
    p.write_text(fm.serialize(front, "## Summary\n\nA concept.\n"))
    return p


# --------------------------------------------------------------------------- #
# Validator — confidence enum                                                  #
# --------------------------------------------------------------------------- #


def test_validator_accepts_valid_confidence_tiers() -> None:
    for tier in CONFIDENCE_TIERS:
        front = {
            "type": "synthesis",
            "slug": f"synth-{tier}",
            "title": f"Synth {tier}",
            "domains": ["test"],
            "question": "What?",
            "sources_count": 0,
            "synthesizes": [],
            "confidence": tier,
            "created_at": "2026-01-01T00:00:00Z",
            "last_updated": "2026-01-01T00:00:00Z",
        }
        result = validate_wiki_page_frontmatter(front, "synthesis")
        error_rules = [e.rule for e in result.errors]
        assert "confidence-invalid" not in error_rules, f"tier={tier} should be valid"


def test_validator_rejects_invalid_confidence() -> None:
    front = {
        "type": "concept",
        "slug": "bad-confidence",
        "title": "Bad",
        "domains": ["test"],
        "confidence": "strong",
        "sources": [],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    result = validate_wiki_page_frontmatter(front, "concept")
    error_rules = [e.rule for e in result.errors]
    assert "confidence-invalid" in error_rules


def test_validator_no_error_when_confidence_absent() -> None:
    front = {
        "type": "concept",
        "slug": "no-confidence",
        "title": "No Confidence",
        "domains": ["test"],
        "sources": [],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    result = validate_wiki_page_frontmatter(front, "concept")
    error_rules = [e.rule for e in result.errors]
    assert "confidence-invalid" not in error_rules


# --------------------------------------------------------------------------- #
# Lint — distribution                                                          #
# --------------------------------------------------------------------------- #


def test_distribution_counts_annotated_pages(kb_root: Path) -> None:
    _make_concept(kb_root, slug="c-established", confidence="established", domains=["alpha"])
    _make_concept(kb_root, slug="c-tentative", confidence="tentative", domains=["alpha"])
    _make_concept(kb_root, slug="c-none", domains=["alpha"])
    findings = run_distribution()
    alpha = next((f for f in findings if "alpha" in f.metadata.get("domain", "")), None)
    assert alpha is not None
    assert alpha.metadata["established"] == 1
    assert alpha.metadata["tentative"] == 1
    assert alpha.metadata["none"] == 1


def test_distribution_finding_check_name(kb_root: Path) -> None:
    _make_concept(kb_root, slug="dist-check", domains=["beta"])
    findings = run_distribution()
    for f in findings:
        assert f.check == "confidence-distribution"


def test_distribution_pct_annotated(kb_root: Path) -> None:
    _make_concept(kb_root, slug="ann-1", confidence="established", domains=["gamma"])
    _make_concept(kb_root, slug="ann-2", confidence="tentative", domains=["gamma"])
    _make_concept(kb_root, slug="ann-3", domains=["gamma"])  # none
    findings = run_distribution()
    gamma = next(f for f in findings if f.metadata.get("domain") == "gamma")
    assert gamma.metadata["pct_annotated"] == 66  # 2/3


def test_distribution_registered_in_known_checks() -> None:
    from gateway.ops.lint import KNOWN_CHECKS
    assert "confidence-distribution" in KNOWN_CHECKS
    assert "confidence-propagation" in KNOWN_CHECKS


# --------------------------------------------------------------------------- #
# Lint — propagation                                                           #
# --------------------------------------------------------------------------- #


def test_propagation_flags_synthesis_stronger_than_source(kb_root: Path) -> None:
    _make_source_wiki_page(kb_root, source_id="arxiv-2401-00001", confidence="tentative")
    _make_synthesis(
        kb_root,
        slug="overconfident-synth",
        confidence="established",
        synthesizes=["sources/arxiv-2401-00001"],
    )
    findings = run_propagation()
    slugs = [f.path for f in findings]
    assert any("overconfident-synth" in s for s in slugs)


def test_propagation_passes_when_confidence_matches(kb_root: Path) -> None:
    _make_source_wiki_page(kb_root, source_id="arxiv-2401-00002", confidence="tentative")
    _make_synthesis(
        kb_root,
        slug="correct-synth",
        confidence="tentative",
        synthesizes=["sources/arxiv-2401-00002"],
    )
    findings = run_propagation()
    slugs = [f.path for f in findings]
    assert not any("correct-synth" in s for s in slugs)


def test_propagation_passes_when_no_source_confidence(kb_root: Path) -> None:
    _make_source_wiki_page(kb_root, source_id="arxiv-2401-00003")  # no confidence
    _make_synthesis(
        kb_root,
        slug="no-source-conf-synth",
        confidence="established",
        synthesizes=["sources/arxiv-2401-00003"],
    )
    findings = run_propagation()
    slugs = [f.path for f in findings]
    assert not any("no-source-conf-synth" in s for s in slugs)


def test_propagation_finding_severity_is_warning(kb_root: Path) -> None:
    from gateway.lint import SEVERITY_WARNING
    _make_source_wiki_page(kb_root, source_id="arxiv-2401-00004", confidence="speculative")
    _make_synthesis(
        kb_root,
        slug="sev-test-synth",
        confidence="established",
        synthesizes=["sources/arxiv-2401-00004"],
    )
    findings = run_propagation()
    for f in findings:
        assert f.severity == SEVERITY_WARNING
