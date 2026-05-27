"""ONT-14: question page type — status enum, synthesis link, lint checks."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.lint.unanswered_questions import (
    run_answered_no_synthesis,
    run_open_questions,
)
from gateway.validator import validate_question_frontmatter, validate_wiki_page
from gateway.wiki_pages import PAGE_SCHEMAS


# --------------------------------------------------------------------------- #
# Helpers                                                                      #
# --------------------------------------------------------------------------- #


def _write_question(
    kb_root: Path,
    slug: str,
    *,
    status: str = "open",
    synthesis: str | None = None,
    title: str | None = None,
) -> Path:
    d = paths.wiki_dir() / "questions"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{slug}.md"
    front: dict = {
        "type": "question",
        "slug": slug,
        "title": title or slug.replace("-", " ").title(),
        "domains": ["test"],
        "status": status,
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    if synthesis is not None:
        front["synthesis"] = synthesis
    body = "## Question\n\nWhat?\n\n## Context\n\nSome context.\n"
    p.write_text(fm.serialize(front, body))
    return p


# --------------------------------------------------------------------------- #
# Page schema                                                                  #
# --------------------------------------------------------------------------- #


def test_question_page_schema_registered() -> None:
    assert "question" in PAGE_SCHEMAS


def test_question_schema_directory() -> None:
    schema = PAGE_SCHEMAS["question"]
    assert schema.directory == "wiki/questions"


def test_question_required_fields() -> None:
    schema = PAGE_SCHEMAS["question"]
    assert "status" in schema.required_fields
    assert "domains" in schema.required_fields


# --------------------------------------------------------------------------- #
# Validator                                                                    #
# --------------------------------------------------------------------------- #


def test_validator_accepts_valid_status_values() -> None:
    for status in ("open", "partial", "answered"):
        front = {"status": status, "synthesis": "my-synthesis" if status == "answered" else None}
        result = validate_question_frontmatter(front)
        error_rules = [e.rule for e in result.errors]
        assert "question-status-unknown" not in error_rules, f"status={status} should be valid"


def test_validator_rejects_invalid_status() -> None:
    front = {"status": "in-progress"}
    result = validate_question_frontmatter(front)
    error_rules = [e.rule for e in result.errors]
    assert "question-status-unknown" in error_rules


def test_validator_warns_answered_without_synthesis() -> None:
    front = {"status": "answered"}  # no synthesis key
    result = validate_question_frontmatter(front)
    warning_rules = [w.rule for w in result.warnings]
    assert "question-answered-missing-synthesis" in warning_rules


def test_validator_no_warning_when_answered_with_synthesis() -> None:
    front = {"status": "answered", "synthesis": "my-synthesis-slug"}
    result = validate_question_frontmatter(front)
    warning_rules = [w.rule for w in result.warnings]
    assert "question-answered-missing-synthesis" not in warning_rules


def test_validator_no_warning_for_open_without_synthesis() -> None:
    front = {"status": "open"}
    result = validate_question_frontmatter(front)
    warning_rules = [w.rule for w in result.warnings]
    assert "question-answered-missing-synthesis" not in warning_rules


# --------------------------------------------------------------------------- #
# Lint                                                                         #
# --------------------------------------------------------------------------- #


def test_open_questions_finding_for_open(kb_root: Path) -> None:
    _write_question(kb_root, "open-q", status="open")
    findings = run_open_questions()
    assert any("open-q" in f.path for f in findings)


def test_open_questions_finding_for_partial(kb_root: Path) -> None:
    _write_question(kb_root, "partial-q", status="partial")
    findings = run_open_questions()
    assert any("partial-q" in f.path for f in findings)


def test_open_questions_no_finding_for_answered(kb_root: Path) -> None:
    _write_question(kb_root, "answered-q", status="answered", synthesis="some-synth")
    findings = run_open_questions()
    assert not any("answered-q" in f.path for f in findings)


def test_answered_no_synthesis_flagged(kb_root: Path) -> None:
    _write_question(kb_root, "no-synth-q", status="answered")  # no synthesis
    findings = run_answered_no_synthesis()
    assert any("no-synth-q" in f.path for f in findings)


def test_answered_with_synthesis_not_flagged(kb_root: Path) -> None:
    _write_question(kb_root, "with-synth-q", status="answered", synthesis="my-synth")
    findings = run_answered_no_synthesis()
    assert not any("with-synth-q" in f.path for f in findings)


def test_lint_checks_registered_in_known_checks() -> None:
    from gateway.ops.lint import KNOWN_CHECKS
    assert "open-questions" in KNOWN_CHECKS
    assert "answered-no-synthesis" in KNOWN_CHECKS
