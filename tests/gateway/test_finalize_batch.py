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
from unittest.mock import patch

import pytest

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops.cite_suggest import CiteSuggestion
from gateway.ops.finalize_batch import finalize_batch, _write_run_report


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
        "created_at": started,
        "last_updated": started,
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
            "created_at": started,
            "last_updated": started,
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


# ---------------------------------------------------------------------------
# Phase D helpers + tests
# ---------------------------------------------------------------------------

def _write_draft_concept_with_unresolved(kb_root: Path, slug: str,
                                         source_id: str) -> Path:
    page = kb_root / "wiki" / "concepts" / f"{slug}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    started = (datetime.now(timezone.utc) - timedelta(days=20)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    title = slug.replace("-", " ").title()
    front = {
        "type": "concept",
        "slug": slug,
        "title": title,
        "canonical_name": title,
        "domains": ["test-domain"],
        "created_at": started,
        "last_updated": started,
        "draft": True,
        "draft_started_at": started,
        "draft_unresolved_claims": 1,
        "sources": [source_id],
    }
    body = (
        f"# {title}\n\n"
        "## Summary\n\n"
        "A cited fact appears in source one.\n\n"
        "## Key claims\n\n"
        "- No additional claims.\n\n"
        "## Sources\n\n"
        "None.\n\n"
        "## Related\n\n"
        "None.\n"
    )
    page.write_text(fm.serialize(front, body))
    return page


def test_aggressive_applies_unambiguous_suggestion_then_finalizes(kb_root):
    sid = "web-2026-01-01-zzz"
    # Wiki source page (cite op requires this to exist)
    wiki_src = kb_root / "wiki" / "sources" / f"{sid}.md"
    wiki_src.parent.mkdir(parents=True, exist_ok=True)
    wiki_src.write_text(fm.serialize(
        {"type": "source", "source_id": sid, "source_type": "web",
         "title": "Z", "domains": ["test-domain"]},
        "# Z\n",
    ))
    # Raw source body
    raw = kb_root / "raw" / "web" / f"{sid}.md"
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(fm.serialize(
        {"id": sid, "type": "web", "title": "Z",
         "url": "https://example.com/z", "domains": ["test-domain"]},
        "A cited fact appears in source one.\n",
    ))

    page = _write_draft_concept_with_unresolved(kb_root, "test-concept", sid)

    # Compute the actual line number of the claim in the on-disk file
    # (frontmatter + body, after fm.serialize).
    text = page.read_text()
    target_line = next(
        i + 1
        for i, line in enumerate(text.splitlines())
        if "A cited fact appears" in line
    )

    with patch("gateway.ops.finalize_batch.suggest_cites") as mock_suggest:
        mock_suggest.return_value = [CiteSuggestion(
            line=target_line,
            source_id=sid,
            evidence_quote="A cited fact appears in source one.",
            unambiguous=True,
            evidence_verified=True,
        )]
        result = finalize_batch(execute=True, suggest=True)

    assert result.success
    front_after, body_after = fm.parse(page.read_text())
    assert "draft" not in front_after
    assert f"[[sources/{sid}]]" in body_after


def test_ambiguous_suggestion_not_applied(kb_root):
    sid1 = "web-2026-01-01-yyy"
    page = _write_draft_concept_with_unresolved(kb_root, "concept-amb", sid1)

    with patch("gateway.ops.finalize_batch.suggest_cites") as mock_suggest:
        mock_suggest.return_value = [
            CiteSuggestion(line=6, source_id=sid1, evidence_quote="q1",
                           unambiguous=False, evidence_verified=True,
                           skip_reason="multi-candidate line"),
            CiteSuggestion(line=6, source_id="other",
                           evidence_quote="q2",
                           unambiguous=False, evidence_verified=True,
                           skip_reason="multi-candidate line"),
        ]
        result = finalize_batch(execute=True, suggest=True)

    assert result.success
    front_after, body_after = fm.parse(page.read_text())
    assert front_after.get("draft") is True  # not finalized
    assert "[[sources/" not in body_after  # no cite applied


def test_report_file_written_with_outcome_categories(kb_root):
    _write_draft_entity(kb_root, "rep-co", age_days=12, unresolved=0)

    result = finalize_batch(execute=True, suggest=False)

    assert result.success
    report_dir = kb_root / ".knowledge" / "finalize-batch"
    assert report_dir.is_dir()
    reports = list(report_dir.glob("*.md"))
    assert len(reports) == 1
    text = reports[0].read_text()
    assert "rep-co" in text
    assert "cat_a" in text or "Cat A" in text


def test_cite_succeeds_but_finalize_fails_records_half_mutated_state(kb_root):
    """When cite_one applies the citation successfully but finalize_one
    rejects the page (e.g. some OTHER claim on the page is still unresolved),
    the page is in a half-mutated state: cite is in the body, but draft: true
    remains. The escalation note must signal this so a future operator knows
    git rollback is needed."""
    sid = "web-2026-01-01-half"
    # Wiki source + raw source so cite_one accepts the cite.
    wiki_src = kb_root / "wiki" / "sources" / f"{sid}.md"
    wiki_src.parent.mkdir(parents=True, exist_ok=True)
    wiki_src.write_text(fm.serialize(
        {"type": "source", "source_id": sid, "source_type": "web",
         "title": "Half", "domains": ["test-domain"]},
        "# Half\n",
    ))
    raw = kb_root / "raw" / "web" / f"{sid}.md"
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(fm.serialize(
        {"id": sid, "type": "web", "title": "Half",
         "url": "https://example.com/half", "domains": ["test-domain"]},
        "Specific claim that gets cited.\n",
    ))

    # Build a concept draft with TWO claim lines:
    # - claim A gets a cite from suggest (will succeed)
    # - claim B remains uncited (so finalize_one rejects on B's grounding rule)
    # Use the helper's conformant-body structure so finalize gets past
    # frontmatter/schema and only fails on the citation-grounding rule.
    page = _write_draft_concept_with_unresolved(kb_root, "concept-half", sid)
    # Append an uncited claim line.
    text = page.read_text()
    page.write_text(text.rstrip() + "\nA second uncited claim that finalize must reject.\n")

    # Find the line that suggest will cite.
    text = page.read_text()
    target_line = next(
        i + 1
        for i, line in enumerate(text.splitlines())
        if "A cited fact appears" in line
    )

    with patch("gateway.ops.finalize_batch.suggest_cites") as mock_suggest:
        mock_suggest.return_value = [CiteSuggestion(
            line=target_line,
            source_id=sid,
            evidence_quote="A cited fact appears in source one.",
            unambiguous=True,
            evidence_verified=True,
        )]
        result = finalize_batch(execute=True, suggest=True)

    assert result.success  # batch op itself doesn't fail
    front_after, body_after = fm.parse(page.read_text())
    # Cite WAS applied (body now contains [[sources/...]])
    assert f"[[sources/{sid}]]" in body_after
    # But draft remains (finalize rejected)
    assert front_after.get("draft") is True
    # Escalation note must signal the half-mutated state.
    haystack = "\n".join([result.summary, *result.warnings])
    assert "cite applied" in haystack
    assert "half-mutated" in haystack or "git" in haystack
