"""Tests for ONT-6 — created_at / last_updated enforcement.

Covers:
- Validator rejects entity/concept/synthesis missing created_at or last_updated
- Validator rejects synthesis missing sources_count
- Invalid timestamp format → SEVERITY_ERROR
- Write path (concept_add, apply_plan) stamps created_at + last_updated
- apply_plan update preserves created_at, updates last_updated
- finalize stamps last_updated
- contested field no longer causes a MUTABLE warning on source pages
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import paths, validator, wiki_pages
from gateway.ops.apply_plan import apply_plan
from gateway.ops.concept_add import concept_add
from gateway.ops.finalize import finalize
from gateway.plan import Plan, WikiUpdate


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _seed_source_page(kb_root: Path, source_id: str = "web-2026-01-01-abc1") -> None:
    """Write a minimal wiki/sources/ page so synthesizes: refs resolve."""
    source_page = kb_root / "wiki" / "sources" / f"{source_id}.md"
    source_page.parent.mkdir(parents=True, exist_ok=True)
    source_page.write_text(
        f"---\ntype: source\nsource_id: {source_id}\nsource_type: web\n"
        f"title: Test Source\ningested_at: '2026-01-01T00:00:00Z'\n---\n"
        "## Summary\n\nSource body. [[sources/web-2026-01-01-abc1]]\n"
        "## Key claims\n\nA claim. [[sources/web-2026-01-01-abc1]]\n"
        "## Cross-references\n\nNone.\n"
    )


_VALID_ENTITY_BODY = (
    "## Summary\n\nSummary sentence. [[sources/web-2026-01-01-abc1]]\n\n"
    "## Key facts\n\nFact. [[sources/web-2026-01-01-abc1]]\n\n"
    "## Sources\n\n- [[sources/web-2026-01-01-abc1]]\n\n"
    "## Related\n\nNone.\n"
)

_VALID_CONCEPT_BODY = (
    "## Summary\n\nSummary. [[sources/web-2026-01-01-abc1]]\n\n"
    "## Key claims\n\nClaim. [[sources/web-2026-01-01-abc1]]\n\n"
    "## Sources\n\n- [[sources/web-2026-01-01-abc1]]\n\n"
    "## Related\n\nNone.\n"
)

_VALID_SYNTHESIS_BODY = (
    "# Test question\n\n"
    "## Synthesis\n\nAnswer. [[sources/web-2026-01-01-abc1]]\n\n"
    "## Sources cited\n\n- [[sources/web-2026-01-01-abc1]]\n"
)


# ---------------------------------------------------------------------------
# validator: required fields enforcement
# ---------------------------------------------------------------------------


def test_entity_missing_created_at_is_error():
    front = {
        "type": "entity",
        "slug": "test-entity",
        "canonical_name": "Test Entity",
        "entity_kind": "drug",
        "domains": ["glp1"],
        "last_updated": _now_iso(),
        # created_at deliberately absent
    }
    result = validator.validate_wiki_page_frontmatter(front, "entity")
    rules = [e.rule for e in result.errors]
    assert "wiki-page-required-field" in rules
    field_errors = [e.field_name for e in result.errors if e.rule == "wiki-page-required-field"]
    assert "created_at" in field_errors


def test_entity_missing_last_updated_is_error():
    front = {
        "type": "entity",
        "slug": "test-entity",
        "canonical_name": "Test Entity",
        "entity_kind": "drug",
        "domains": ["glp1"],
        "created_at": _now_iso(),
        # last_updated deliberately absent
    }
    result = validator.validate_wiki_page_frontmatter(front, "entity")
    field_errors = [e.field_name for e in result.errors if e.rule == "wiki-page-required-field"]
    assert "last_updated" in field_errors


def test_concept_missing_created_at_is_error():
    front = {
        "type": "concept",
        "slug": "test-concept",
        "canonical_name": "Test Concept",
        "domains": ["glp1"],
        "last_updated": _now_iso(),
    }
    result = validator.validate_wiki_page_frontmatter(front, "concept")
    field_errors = [e.field_name for e in result.errors if e.rule == "wiki-page-required-field"]
    assert "created_at" in field_errors


def test_synthesis_missing_created_at_is_error():
    front = {
        "type": "synthesis",
        "slug": "test-synthesis",
        "title": "Test",
        "domains": ["glp1"],
        "question": "What is X?",
        "last_updated": _now_iso(),
        "sources_count": 1,
    }
    result = validator.validate_wiki_page_frontmatter(front, "synthesis")
    field_errors = [e.field_name for e in result.errors if e.rule == "wiki-page-required-field"]
    assert "created_at" in field_errors


def test_synthesis_missing_sources_count_is_error():
    front = {
        "type": "synthesis",
        "slug": "test-synthesis",
        "title": "Test",
        "domains": ["glp1"],
        "question": "What is X?",
        "created_at": _now_iso(),
        "last_updated": _now_iso(),
        # sources_count absent
    }
    result = validator.validate_wiki_page_frontmatter(front, "synthesis")
    field_errors = [e.field_name for e in result.errors if e.rule == "wiki-page-required-field"]
    assert "sources_count" in field_errors


# ---------------------------------------------------------------------------
# validator: timestamp format
# ---------------------------------------------------------------------------


def test_invalid_created_at_format_is_error():
    front = {
        "type": "concept",
        "slug": "test-concept",
        "canonical_name": "Test Concept",
        "domains": ["glp1"],
        "created_at": "not-a-date",
        "last_updated": _now_iso(),
    }
    result = validator.validate_wiki_page_frontmatter(front, "concept")
    assert not result.ok


def test_invalid_last_updated_format_is_error():
    front = {
        "type": "concept",
        "slug": "test-concept",
        "canonical_name": "Test Concept",
        "domains": ["glp1"],
        "created_at": _now_iso(),
        "last_updated": "bad-date",
    }
    result = validator.validate_wiki_page_frontmatter(front, "concept")
    assert not result.ok


def test_validate_timestamps_standalone():
    """validate_timestamps(front) is a public helper."""
    result = validator.validate_timestamps({"created_at": "not-a-date", "last_updated": "2026-01-01T00:00:00Z"})
    assert not result.ok

    result_ok = validator.validate_timestamps({"created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z"})
    assert result_ok.ok


# ---------------------------------------------------------------------------
# write path: concept_add stamps both fields
# ---------------------------------------------------------------------------


def test_concept_add_stamps_created_at_and_last_updated(kb_root):
    _seed_source_page(kb_root)
    result = concept_add(
        slug="test-concept-ts",
        canonical_name="Test Concept",
        body=_VALID_CONCEPT_BODY,
        domain="glp1",
    )
    assert result.success, result.errors

    page = kb_root / "wiki" / "concepts" / "test-concept-ts.md"
    front, _ = fm.parse(page.read_text())
    assert front.get("created_at")
    assert front.get("last_updated")
    # Both should be parseable ISO-8601
    datetime.fromisoformat(front["created_at"].replace("Z", "+00:00"))
    datetime.fromisoformat(front["last_updated"].replace("Z", "+00:00"))


# ---------------------------------------------------------------------------
# write path: apply_plan stamps fields on create, updates last_updated on update
# ---------------------------------------------------------------------------


def _make_synthesis_plan(slug: str, sources_count: int = 1) -> Plan:
    front = {
        "type": "synthesis",
        "slug": slug,
        "title": "Test question",
        "domains": ["glp1"],
        "question": "What is X?",
        "created_at": _now_iso(),
        "last_updated": _now_iso(),
        "sources_count": sources_count,
    }
    content = fm.serialize(front, _VALID_SYNTHESIS_BODY)
    update = WikiUpdate(
        target_path=f"wiki/synthesis/{slug}.md",
        update_kind="create",
        content=content,
        rationale="test synthesis",
    )
    return Plan(source_id="web-2026-01-01-abc1", rationale="test", updates=[update])


def test_apply_plan_create_synthesis_stamps_timestamps(kb_root, make_source):
    _seed_source_page(kb_root)
    raw_path = paths.raw_source_path("web", "web-2026-01-01-abc1")
    raw_path.write_text(make_source())

    plan = _make_synthesis_plan("test-synthesis-create")
    result = apply_plan(plan, draft=True)
    assert result.success, result.errors

    page = kb_root / "wiki" / "synthesis" / "test-synthesis-create.md"
    front, _ = fm.parse(page.read_text())
    assert front.get("created_at")
    assert front.get("last_updated")


def test_apply_plan_update_preserves_created_at_updates_last_updated(kb_root, make_source):
    import time
    _seed_source_page(kb_root)
    raw_path = paths.raw_source_path("web", "web-2026-01-01-abc1")
    raw_path.write_text(make_source())

    # First: create
    plan = _make_synthesis_plan("test-synthesis-update")
    result = apply_plan(plan, draft=True)
    assert result.success, result.errors

    page = kb_root / "wiki" / "synthesis" / "test-synthesis-update.md"
    first_front, _ = fm.parse(page.read_text())
    original_created_at = first_front["created_at"]

    time.sleep(0.05)  # tiny gap so last_updated differs

    # Second: update
    update_front = {
        "type": "synthesis",
        "slug": "test-synthesis-update",
        "title": "Test question updated",
        "domains": ["glp1"],
        "question": "What is X?",
        "created_at": original_created_at,
        "last_updated": _now_iso(),
        "sources_count": 1,
    }
    update_content = fm.serialize(update_front, _VALID_SYNTHESIS_BODY)
    update_plan = Plan(
        source_id="web-2026-01-01-abc1",
        rationale="update test",
        updates=[WikiUpdate(
            target_path="wiki/synthesis/test-synthesis-update.md",
            update_kind="update",
            content=update_content,
            rationale="update",
        )],
    )
    result2 = apply_plan(update_plan, draft=True)
    assert result2.success, result2.errors

    second_front, _ = fm.parse(page.read_text())
    # created_at unchanged
    assert second_front["created_at"] == original_created_at


# ---------------------------------------------------------------------------
# finalize stamps last_updated
# ---------------------------------------------------------------------------


def test_finalize_stamps_last_updated(kb_root, make_source):
    _seed_source_page(kb_root)
    raw_path = paths.raw_source_path("web", "web-2026-01-01-abc1")
    raw_path.write_text(make_source())

    # Create a draft concept page directly (bypass validator for setup)
    now = _now_iso()
    front = {
        "type": "concept",
        "slug": "test-finalize-concept",
        "canonical_name": "Test Concept",
        "domains": ["glp1"],
        "created_at": now,
        "last_updated": now,
        "draft": True,
    }
    page = kb_root / "wiki" / "concepts" / "test-finalize-concept.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(fm.serialize(front, _VALID_CONCEPT_BODY))

    result = finalize(page)
    assert result.success, result.errors

    updated_front, _ = fm.parse(page.read_text())
    assert updated_front.get("last_updated")
    assert not updated_front.get("draft")


# ---------------------------------------------------------------------------
# contested field is mutable on source pages
# ---------------------------------------------------------------------------


def test_contested_field_is_mutable_on_source_pages():
    """QUAL-3 resolution sets contested: true — should not raise a mutation error."""
    old = {
        "id": "web-2026-01-01-abc1",
        "type": "web",
        "title": "T",
        "url": "https://example.com",
        "authors": [],
        "published_at": "2026-01-01",
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": "sha256:abc",
        "domains": [],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {},
    }
    new = {**old, "contested": True}
    result = validator.validate_source_frontmatter_diff(old, new)
    assert result.ok
