"""ONT-5: canonical_source required on paper entities."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.lint.paper_canonical_source import run as lint_run
from gateway.validator import validate_wiki_page_frontmatter


# --------------------------------------------------------------------------- #
# Helpers                                                                      #
# --------------------------------------------------------------------------- #


def _make_entity(
    kb_root: Path,
    *,
    slug: str = "semaglutide-paper",
    entity_kind: str = "paper",
    canonical_source: str | None = None,
    title: str = "Test Paper Entity",
) -> Path:
    d = paths.wiki_dir() / "entities"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{slug}.md"
    front: dict = {
        "type": "entity",
        "slug": slug,
        "title": title,
        "canonical_name": title,
        "entity_kind": entity_kind,
        "domains": ["test-domain"],
        "sources": [],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    if canonical_source is not None:
        front["canonical_source"] = canonical_source
    p.write_text(fm.serialize(front, "## Summary\n\nA paper.\n"))
    return p


# --------------------------------------------------------------------------- #
# Lint check                                                                   #
# --------------------------------------------------------------------------- #


def test_lint_flags_paper_without_canonical_source(kb_root: Path) -> None:
    _make_entity(kb_root, slug="paper-no-source")
    findings = lint_run()
    slugs = [f.metadata.get("slug") for f in findings]
    assert "paper-no-source" in slugs


def test_lint_passes_paper_with_canonical_source(kb_root: Path) -> None:
    _make_entity(kb_root, slug="paper-with-source", canonical_source="arxiv-2401-12345")
    findings = lint_run()
    slugs = [f.metadata.get("slug") for f in findings]
    assert "paper-with-source" not in slugs


def test_lint_ignores_non_paper_entities(kb_root: Path) -> None:
    _make_entity(kb_root, slug="person-entity", entity_kind="person")
    findings = lint_run()
    slugs = [f.metadata.get("slug") for f in findings]
    assert "person-entity" not in slugs


def test_lint_check_name_is_paper_canonical_source(kb_root: Path) -> None:
    _make_entity(kb_root, slug="flagged-paper")
    findings = lint_run()
    assert all(f.check == "paper-canonical-source" for f in findings)


def test_lint_finding_severity_is_warning(kb_root: Path) -> None:
    from gateway.lint import SEVERITY_WARNING
    _make_entity(kb_root, slug="warning-paper")
    findings = lint_run()
    assert all(f.severity == SEVERITY_WARNING for f in findings)


def test_lint_finding_path_is_relative(kb_root: Path) -> None:
    _make_entity(kb_root, slug="path-check-paper")
    findings = lint_run()
    for f in findings:
        assert not f.path.startswith("/"), f"path should be relative: {f.path}"


def test_lint_registered_in_known_checks() -> None:
    from gateway.ops.lint import KNOWN_CHECKS
    assert "paper-canonical-source" in KNOWN_CHECKS


# --------------------------------------------------------------------------- #
# Validator warning                                                            #
# --------------------------------------------------------------------------- #


def _valid_paper_front(**overrides) -> dict:
    base = {
        "type": "entity",
        "slug": "some-paper",
        "title": "Some Paper",
        "canonical_name": "Some Paper",
        "entity_kind": "paper",
        "domains": ["test"],
        "sources": [],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    base.update(overrides)
    return base


def test_validator_warns_paper_without_canonical_source() -> None:
    front = _valid_paper_front()
    result = validate_wiki_page_frontmatter(front, "entity")
    warn_codes = [w.rule for w in result.warnings]
    assert "paper-missing-canonical-source" in warn_codes


def test_validator_no_warning_with_canonical_source() -> None:
    front = _valid_paper_front(canonical_source="arxiv-2401-12345")
    result = validate_wiki_page_frontmatter(front, "entity")
    warn_codes = [w.rule for w in result.warnings]
    assert "paper-missing-canonical-source" not in warn_codes


def test_validator_warning_does_not_cause_error() -> None:
    """Missing canonical_source is a warning, not a hard error."""
    front = _valid_paper_front()
    result = validate_wiki_page_frontmatter(front, "entity")
    error_codes = [e.rule for e in result.errors]
    assert "paper-missing-canonical-source" not in error_codes
    assert result.ok


def test_validator_no_warning_for_non_paper_entity() -> None:
    front = _valid_paper_front(entity_kind="person")
    result = validate_wiki_page_frontmatter(front, "entity")
    warn_codes = [w.rule for w in result.warnings]
    assert "paper-missing-canonical-source" not in warn_codes
