"""Tests for the `wiki concept-add` gateway op (M46-followup Fix C).

Surfaced during the 2026-05-23 ai-native-business build: there was no
gateway-side path to author a `wiki/concepts/<slug>.md` page. `wiki query`
files synthesis pages even when a concept anchor is what's wanted, and
direct file writes are blocked by hard rule #1. This op closes that gap.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm


_VALID_CONCEPT_BODY = """\
## Summary

Substrate-first AI places models underneath the operating model [[sources/web-2026-04-23-e4c]].

## Key claims

- Solo founder + N agents replaces small-team org [[sources/web-2026-04-23-e4c]].
- Unit economics flip when human labor becomes a variable software cost [[sources/web-2025-10-04-aae]].

## Sources

- [[sources/web-2026-04-23-e4c]] — Pieter Levels portfolio operating model
- [[sources/web-2025-10-04-aae]] — AI-native GTM playbook

## Related

- [[mocs/ai-native-business]]
"""

# When `synthesizes:` is set, the body must include a `## Included works`
# section that mirrors the synthesizes list 1:1 (validator M45 § 3.6).
_VALID_CONCEPT_BODY_WITH_INCLUDED_WORKS = """\
## Summary

Substrate-first AI places models underneath the operating model [[sources/web-2026-04-23-e4c]].

## Key claims

- Solo founder + N agents replaces small-team org [[sources/web-2026-04-23-e4c]].
- Unit economics flip when human labor becomes a variable software cost [[sources/web-2025-10-04-aae]].

## Included works

- [[sources/web-2026-04-23-e4c]]
- [[sources/web-2025-10-04-aae]]

## Sources

- [[sources/web-2026-04-23-e4c]] — Pieter Levels portfolio operating model
- [[sources/web-2025-10-04-aae]] — AI-native GTM playbook

## Related

- [[mocs/ai-native-business]]
"""


def _seed_source_pages(kb_root: Path, *source_ids: str) -> None:
    """Create minimal wiki/sources/<id>.md pages so concept-add citations
    resolve. The validator requires `[[sources/<id>]]` wikilinks to point
    at existing pages."""
    src_dir = kb_root / "wiki" / "sources"
    src_dir.mkdir(parents=True, exist_ok=True)
    for sid in source_ids:
        (src_dir / f"{sid}.md").write_text(
            f"---\ntype: source\nsource_id: {sid}\nsource_type: web\n"
            f"title: stub\ningested_at: '2026-01-01T00:00:00Z'\n---\n# stub\n"
        )


def test_concept_add_creates_page_with_required_fields(kb_root):
    from gateway.ops.concept_add import concept_add

    _seed_source_pages(kb_root, "web-2026-04-23-e4c", "web-2025-10-04-aae")

    result = concept_add(
        slug="ai-native-substrate",
        canonical_name="AI as Substrate",
        body=_VALID_CONCEPT_BODY,
        domain="ai-native-business",
    )

    assert result.success, result.errors
    page_path = kb_root / "wiki" / "concepts" / "ai-native-substrate.md"
    assert page_path.exists()
    front, body = fm.parse(page_path.read_text())
    assert front["type"] == "concept"
    assert front["slug"] == "ai-native-substrate"
    assert front["canonical_name"] == "AI as Substrate"
    assert front["domains"] == ["ai-native-business"]
    assert "Summary" in body
    assert "Key claims" in body


def test_concept_add_rejects_invalid_slug(kb_root):
    from gateway.ops.concept_add import concept_add

    result = concept_add(
        slug="AI Native Substrate!",
        canonical_name="x",
        body=_VALID_CONCEPT_BODY,
        domain="ai-native-business",
    )

    assert not result.success
    assert any("slug" in e.lower() for e in result.errors)


def test_concept_add_rejects_duplicate_slug(kb_root):
    from gateway.ops.concept_add import concept_add

    _seed_source_pages(kb_root, "web-2026-04-23-e4c", "web-2025-10-04-aae")

    # First add succeeds
    first = concept_add(
        slug="ai-native-substrate",
        canonical_name="AI as Substrate",
        body=_VALID_CONCEPT_BODY,
        domain="ai-native-business",
    )
    assert first.success, first.errors

    # Second add for same slug must refuse
    second = concept_add(
        slug="ai-native-substrate",
        canonical_name="AI as Substrate",
        body=_VALID_CONCEPT_BODY,
        domain="ai-native-business",
    )

    assert not second.success
    assert any("exists" in e.lower() or "duplicate" in e.lower() for e in second.errors)


def test_concept_add_with_draft_flag_sets_draft_true(kb_root):
    from gateway.ops.concept_add import concept_add

    _seed_source_pages(kb_root, "web-2026-04-23-e4c", "web-2025-10-04-aae")

    result = concept_add(
        slug="ai-native-substrate",
        canonical_name="AI as Substrate",
        body=_VALID_CONCEPT_BODY,
        domain="ai-native-business",
        draft=True,
    )

    assert result.success, result.errors
    page_path = kb_root / "wiki" / "concepts" / "ai-native-substrate.md"
    front, _ = fm.parse(page_path.read_text())
    assert front.get("draft") is True
    assert "draft_started_at" in front


def test_concept_add_cite_sources_populates_synthesizes(kb_root):
    from gateway.ops.concept_add import concept_add

    _seed_source_pages(kb_root, "web-2026-04-23-e4c", "web-2025-10-04-aae")

    result = concept_add(
        slug="ai-native-substrate",
        canonical_name="AI as Substrate",
        body=_VALID_CONCEPT_BODY_WITH_INCLUDED_WORKS,
        domain="ai-native-business",
        cite_sources=["web-2026-04-23-e4c", "web-2025-10-04-aae"],
    )

    assert result.success, result.errors
    page_path = kb_root / "wiki" / "concepts" / "ai-native-substrate.md"
    front, _ = fm.parse(page_path.read_text())
    synthesizes = front.get("synthesizes") or []
    assert "sources/web-2026-04-23-e4c" in synthesizes
    assert "sources/web-2025-10-04-aae" in synthesizes


def test_concept_add_rejects_body_missing_required_sections(kb_root):
    """The concept schema requires Summary / Key claims / Sources / Related
    sections. A body missing them must be refused with a specific error."""
    from gateway.ops.concept_add import concept_add

    bad_body = "## Just one section\n\nNo Summary, no Key claims, etc.\n"

    result = concept_add(
        slug="ai-native-substrate",
        canonical_name="AI as Substrate",
        body=bad_body,
        domain="ai-native-business",
    )

    assert not result.success
    combined = " | ".join(result.errors).lower()
    assert "missing" in combined or "section" in combined
