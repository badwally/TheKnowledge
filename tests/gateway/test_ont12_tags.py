"""ONT-12: tags field codification — optional list[str] for sub-domain clustering."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.lint.invalid_tags import run as lint_invalid_tags
from gateway.validator import validate_wiki_page_frontmatter


# --------------------------------------------------------------------------- #
# Helpers                                                                      #
# --------------------------------------------------------------------------- #


def _concept_front(tags=None) -> dict:
    front: dict = {
        "type": "concept",
        "slug": "test-concept",
        "canonical_name": "Test Concept",
        "domains": ["test"],
        "sources": [],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    if tags is not None:
        front["tags"] = tags
    return front


def _write_concept(kb_root: Path, slug: str, tags=None) -> Path:
    d = paths.wiki_dir() / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{slug}.md"
    front = _concept_front(tags)
    front["slug"] = slug
    p.write_text(fm.serialize(front, "## Summary\n\nA concept.\n"))
    return p


# --------------------------------------------------------------------------- #
# Validator                                                                    #
# --------------------------------------------------------------------------- #


def test_validator_accepts_valid_tags_list() -> None:
    front = _concept_front(tags=["sub-topic-a", "sub-topic-b"])
    result = validate_wiki_page_frontmatter(front, "concept")
    warning_rules = [w.rule for w in result.warnings]
    assert "tags-invalid-type" not in warning_rules


def test_validator_accepts_empty_tags_list() -> None:
    front = _concept_front(tags=[])
    result = validate_wiki_page_frontmatter(front, "concept")
    warning_rules = [w.rule for w in result.warnings]
    assert "tags-invalid-type" not in warning_rules


def test_validator_accepts_absent_tags() -> None:
    front = _concept_front()  # no tags key
    result = validate_wiki_page_frontmatter(front, "concept")
    warning_rules = [w.rule for w in result.warnings]
    assert "tags-invalid-type" not in warning_rules


def test_validator_warns_on_string_tags() -> None:
    front = _concept_front(tags="single-tag")  # scalar, not list
    result = validate_wiki_page_frontmatter(front, "concept")
    warning_rules = [w.rule for w in result.warnings]
    assert "tags-invalid-type" in warning_rules


def test_validator_warns_on_list_with_non_string_items() -> None:
    front = _concept_front(tags=["valid", 42])
    result = validate_wiki_page_frontmatter(front, "concept")
    warning_rules = [w.rule for w in result.warnings]
    assert "tags-invalid-type" in warning_rules


# --------------------------------------------------------------------------- #
# Lint                                                                         #
# --------------------------------------------------------------------------- #


def test_lint_passes_for_valid_tags(kb_root: Path) -> None:
    _write_concept(kb_root, "good-tags", tags=["topic-a", "topic-b"])
    findings = lint_invalid_tags()
    slugs = [f.path for f in findings]
    assert not any("good-tags" in s for s in slugs)


def test_lint_passes_when_no_tags(kb_root: Path) -> None:
    _write_concept(kb_root, "no-tags")
    findings = lint_invalid_tags()
    slugs = [f.path for f in findings]
    assert not any("no-tags" in s for s in slugs)


def test_lint_flags_string_tags(kb_root: Path) -> None:
    _write_concept(kb_root, "string-tag", tags="bad-tag-string")
    findings = lint_invalid_tags()
    slugs = [f.path for f in findings]
    assert any("string-tag" in s for s in slugs)


def test_lint_finding_is_warning(kb_root: Path) -> None:
    from gateway.lint import SEVERITY_WARNING
    _write_concept(kb_root, "warn-tag", tags="not-a-list")
    findings = lint_invalid_tags()
    for f in findings:
        if "warn-tag" in f.path:
            assert f.severity == SEVERITY_WARNING
            return
    pytest.fail("no finding for warn-tag")


def test_lint_registered_in_known_checks() -> None:
    from gateway.ops.lint import KNOWN_CHECKS
    assert "tags-invalid-type" in KNOWN_CHECKS
