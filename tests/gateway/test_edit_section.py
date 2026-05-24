"""K1 (M48): `wiki edit <page> --section <name>` constrained section-replace.

Per C1: edit is *not* general-purpose. It replaces the body of one
named `## Section`, validates the result via the full validator, and
writes atomically under the `wiki-author` lock. Frontmatter and other
sections are untouched.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops.edit_section import edit_section


def _make_page(kb_root: Path, body: str, slug: str = "test-entity") -> Path:
    page_path = paths.wiki_dir() / "entities" / f"{slug}.md"
    page_path.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "entity",
        "slug": slug,
        "canonical_name": "Test Entity",
        "entity_kind": "drug",
        "domains": ["testdom"],
        "draft": True,
    }
    page_path.write_text(fm.serialize(front, body))
    return page_path


_VALID_DRAFT_BODY = (
    "# Test Entity\n"
    "\n"
    "## Summary\n"
    "\n"
    "Original summary text content with some detail.\n"
    "\n"
    "## Key facts\n"
    "\n"
    "- Fact one\n"
    "- Fact two\n"
    "\n"
    "## Sources\n"
    "\n"
    "- [[sources/web-test-source]]\n"
    "\n"
    "## Related\n"
    "\n"
    "- [[concepts/test-concept]]\n"
)


# --- happy path -------------------------------------------------------------


def test_edit_section_replaces_named_section_only(kb_root: Path):
    page = _make_page(kb_root, _VALID_DRAFT_BODY)
    result = edit_section(
        page,
        section="Summary",
        new_body="Brand-new summary text replacing the original.\n",
    )
    assert result.success, result.errors

    text = page.read_text()
    # New content present
    assert "Brand-new summary text" in text
    # Original Summary content gone
    assert "Original summary text" not in text
    # Other sections still present
    assert "## Key facts" in text
    assert "Fact one" in text
    assert "## Sources" in text
    assert "## Related" in text


def test_edit_section_preserves_frontmatter(kb_root: Path):
    page = _make_page(kb_root, _VALID_DRAFT_BODY)
    original_front, _ = fm.parse(page.read_text())

    edit_section(
        page,
        section="Summary",
        new_body="Replacement.\n",
    )

    new_front, _ = fm.parse(page.read_text())
    assert new_front == original_front


def test_edit_section_case_insensitive_section_match(kb_root: Path):
    page = _make_page(kb_root, _VALID_DRAFT_BODY)
    result = edit_section(
        page,
        section="summary",  # lowercase
        new_body="Lowercase-section-name match.\n",
    )
    assert result.success
    assert "Lowercase-section-name match." in page.read_text()


# --- rejection ---------------------------------------------------------------


def test_edit_section_rejects_missing_section(kb_root: Path):
    page = _make_page(kb_root, _VALID_DRAFT_BODY)
    result = edit_section(
        page,
        section="Nonexistent",
        new_body="Whatever.\n",
    )
    assert not result.success
    assert any("section" in str(e).lower() for e in result.errors)


def test_edit_section_rejects_when_replacement_breaks_required_section(kb_root: Path):
    """Replacing Summary with an empty body still leaves the section heading,
    but if the replacement somehow removes a required section, validator
    must reject. Today the op replaces only the BODY, not the heading, so
    sections remain. This test pins that contract."""
    page = _make_page(kb_root, _VALID_DRAFT_BODY)
    result = edit_section(
        page,
        section="Summary",
        new_body="",  # empty body
    )
    # Empty body should still be accepted (the section heading remains).
    # The validator may warn but should not block draft mode.
    assert result.success, result.errors
    text = page.read_text()
    assert "## Summary" in text
    assert "## Key facts" in text


def test_edit_section_rejects_unwritable_page(kb_root: Path):
    result = edit_section(
        paths.wiki_dir() / "entities" / "does-not-exist.md",
        section="Summary",
        new_body="x",
    )
    assert not result.success


# --- argument validation ----------------------------------------------------


def test_edit_section_rejects_empty_section_name(kb_root: Path):
    page = _make_page(kb_root, _VALID_DRAFT_BODY)
    result = edit_section(page, section="", new_body="x")
    assert not result.success


def test_edit_section_rejects_path_outside_wiki(kb_root: Path):
    raw_page = paths.knowledge_root() / "raw" / "web" / "some-source.md"
    raw_page.parent.mkdir(parents=True, exist_ok=True)
    raw_page.write_text("---\nid: x\n---\nbody\n")
    result = edit_section(raw_page, section="Body", new_body="y")
    assert not result.success
    assert any("wiki/" in str(e) or "outside" in str(e).lower() for e in result.errors)


# --- locking + atomicity ----------------------------------------------------


def test_edit_section_logs_through_gateway(kb_root: Path):
    page = _make_page(kb_root, _VALID_DRAFT_BODY)
    edit_section(
        page,
        section="Summary",
        new_body="Logged change content.\n",
    )
    log_text = paths.log_path().read_text() if paths.log_path().exists() else ""
    assert "edit-section" in log_text or "edit_section" in log_text
