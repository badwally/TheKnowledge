"""Tests for `wiki finalize-batch` (M49, AGT-2).

Three layers:
- Deterministic Cat A: drafts where stale-drafts metadata says
  `unresolved_claims == 0` -> auto-finalize.
- Suggest path (Phase C/D): uses AnthropicAPIClient -- mocked here.
- Aggressive integration: auto-applies single-source-per-line LLM cites
  with verified evidence quotes.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops.finalize_batch import finalize_batch


_ENTITY_BODY_TEMPLATE = """\
# {title}

## Summary

Test org.

## Key facts

- Type: organization

## Sources

None.

## Related

None.
"""


def _write_draft_entity(kb_root: Path, slug: str, *, age_days: int = 12,
                        unresolved: int = 0, body: str = "") -> Path:
    page = kb_root / "wiki" / "entities" / f"{slug}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    started = (datetime.now(timezone.utc) - timedelta(days=age_days)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    title = slug.replace("-", " ").title()
    front = {
        "type": "entity",
        "slug": slug,
        "title": title,
        "canonical_name": title,
        "entity_kind": "organization",
        "domains": ["test-domain"],
        "draft": True,
        "draft_started_at": started,
        "draft_unresolved_claims": unresolved,
    }
    page.write_text(fm.serialize(front, body or _ENTITY_BODY_TEMPLATE.format(title=title)))
    return page


def test_dry_run_lists_cat_a_drafts_but_does_not_finalize(kb_root):
    p = _write_draft_entity(kb_root, "acme-corp", age_days=12, unresolved=0)

    result = finalize_batch(execute=False, suggest=False)

    assert result.success
    front_after, _ = fm.parse(p.read_text())
    assert front_after.get("draft") is True
    # The summary or warnings should mention the candidate
    haystack = "\n".join([result.summary, *result.warnings])
    assert "acme-corp" in haystack


def test_execute_finalizes_cat_a(kb_root):
    p = _write_draft_entity(kb_root, "beta-corp", age_days=12, unresolved=0)

    result = finalize_batch(execute=True, suggest=False)

    assert result.success
    front_after, _ = fm.parse(p.read_text())
    assert "draft" not in front_after
    assert "finalized_at" in front_after


def test_domain_filter_skips_other_domains(kb_root):
    a = _write_draft_entity(kb_root, "alpha-co", age_days=12, unresolved=0)

    b_path = kb_root / "wiki" / "entities" / "other-co.md"
    started = (datetime.now(timezone.utc) - timedelta(days=12)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    b_path.write_text(fm.serialize(
        {
            "type": "entity",
            "slug": "other-co",
            "title": "Other Co",
            "canonical_name": "Other Co",
            "entity_kind": "organization",
            "domains": ["other-domain"],
            "draft": True,
            "draft_started_at": started,
            "draft_unresolved_claims": 0,
        },
        _ENTITY_BODY_TEMPLATE.format(title="Other Co"),
    ))

    result = finalize_batch(domain="test-domain", execute=True, suggest=False)

    a_front, _ = fm.parse(a.read_text())
    b_front, _ = fm.parse(b_path.read_text())
    assert "draft" not in a_front
    assert b_front.get("draft") is True
