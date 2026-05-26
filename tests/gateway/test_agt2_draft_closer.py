"""Tests for AGT-2 — draft-closer agent.

Acceptance criteria:
- Easy-win page (1:1 attribution, synthesizes: lists exactly one source per claim):
  finalize() called, page no longer draft
- Hard-case page (multi-source claim or multiple synthesizes sources):
  escalation entry written to log.md; page stays draft
- No autonomous filter-correct call
- Per-domain summary written to log.md after run
- NEVER finalizes when synthesizes: lists >1 candidate for a claim
- Scheduler entry registered (or constant exists)
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from gateway import frontmatter as fm, log, paths
from gateway.agents.draft_closer import (
    run_draft_closer,
    DraftCloserResult,
    DRAFT_CLOSER_SCHEDULE,
)


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def _started(days_ago: int) -> str:
    dt = datetime.now(timezone.utc) - timedelta(days=days_ago)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _write_entity_draft(
    kb_root: Path,
    slug: str,
    *,
    age_days: int = 10,
    synthesizes: list[str] | None = None,
    body_claims: int = 1,
) -> Path:
    page = kb_root / "wiki" / "entities" / f"{slug}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    started = _started(age_days)
    title = slug.replace("-", " ").title()
    front: dict = {
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
        "draft_unresolved_claims": 1,
    }
    if synthesizes:
        # synthesizes entries must be sources/<slug> or synthesis/<slug>
        front["synthesizes"] = [f"sources/{s}" if "/" not in s else s for s in synthesizes]

    # One claim line per body_claims, each backed by exactly one [[sources/...]]
    raw_sid = (synthesizes or ["web-2026-01-01-src"])[0]
    source_id = raw_sid.split("/")[-1]  # strip sources/ prefix if present
    claim_lines = [
        f"- A factual claim about {i}. [[sources/{source_id}]]"
        for i in range(body_claims)
    ]
    body = (
        f"# {title}\n\n"
        f"## Summary\n\n{chr(10).join(claim_lines)}\n\n"
        f"## Key facts\n\n- Type: organization\n\n"
        f"## Sources\n\nNone.\n\n"
        f"## Related\n\nNone.\n"
    )
    page.write_text(fm.serialize(front, body))
    return page


def _write_hard_case_draft(
    kb_root: Path,
    slug: str,
    *,
    age_days: int = 10,
    synthesizes: list[str] | None = None,
) -> Path:
    """Write a draft with a claim that has ZERO citations (hard case: no 1:1)."""
    page = kb_root / "wiki" / "entities" / f"{slug}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    started = _started(age_days)
    title = slug.replace("-", " ").title()
    front: dict = {
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
        "draft_unresolved_claims": 1,
    }
    if synthesizes and len(synthesizes) > 1:
        front["synthesizes"] = [f"sources/{s}" if "/" not in s else s for s in synthesizes]

    # Claim with NO citation (or multi-source that can't be unambiguously attributed)
    sid_a = "web-2026-01-01-a"
    sid_b = "web-2026-01-01-b"
    body = (
        f"# {title}\n\n"
        "## Summary\n\n"
        f"- An uncited claim without provenance.\n"
        f"- Another claim citing two sources. [[sources/{sid_a}]] [[sources/{sid_b}]]\n\n"
        "## Key facts\n\n- Type: organization\n\n"
        "## Sources\n\nNone.\n\n"
        "## Related\n\nNone.\n"
    )
    page.write_text(fm.serialize(front, body))
    return page


def _log_text(kb_root: Path) -> str:
    lp = kb_root / "log.md"
    return lp.read_text() if lp.exists() else ""


# ---------------------------------------------------------------------------
# easy-win path
# ---------------------------------------------------------------------------


def test_easy_win_single_source_finalizes_page(kb_root):
    page = _write_entity_draft(
        kb_root, "easy-co",
        age_days=10,
        body_claims=1,
    )

    result = run_draft_closer()

    assert result.pages_finalized >= 1
    front_after, _ = fm.parse(page.read_text())
    assert "draft" not in front_after, "easy-win page should be finalized"
    assert "finalized_at" in front_after


def test_easy_win_writes_per_domain_summary_to_log(kb_root):
    _write_entity_draft(
        kb_root, "easy-log-co",
        age_days=10,
    )

    run_draft_closer()

    log_text = _log_text(kb_root)
    assert "draft-closer" in log_text


# ---------------------------------------------------------------------------
# hard-case path
# ---------------------------------------------------------------------------


def test_hard_case_multi_citation_stays_draft(kb_root):
    page = _write_hard_case_draft(
        kb_root, "hard-co",
        age_days=10,
        synthesizes=["web-2026-01-01-a", "web-2026-01-01-b"],
    )

    result = run_draft_closer()

    assert result.pages_escalated >= 1
    front_after, _ = fm.parse(page.read_text())
    assert front_after.get("draft") is True, "hard-case page must remain draft"


def test_hard_case_escalation_written_to_log(kb_root):
    _write_hard_case_draft(
        kb_root, "hard-log-co",
        age_days=10,
        synthesizes=["web-2026-01-01-a", "web-2026-01-01-b"],
    )

    run_draft_closer()

    log_text = _log_text(kb_root)
    assert "escalat" in log_text.lower() or "hard" in log_text.lower()


def test_never_finalizes_when_body_has_multi_citation_per_line(kb_root):
    """A body line citing 2+ sources is ambiguous — NEVER finalize."""
    page = _write_hard_case_draft(
        kb_root, "multi-src-co",
        age_days=10,
    )

    run_draft_closer()

    front_after, _ = fm.parse(page.read_text())
    assert front_after.get("draft") is True


# ---------------------------------------------------------------------------
# fresh drafts skipped (not stale yet)
# ---------------------------------------------------------------------------


def test_fresh_draft_below_threshold_not_touched(kb_root):
    """Drafts below the stale threshold never appear in stale_drafts.run() — untouched."""
    page = _write_entity_draft(
        kb_root, "fresh-co",
        age_days=2,  # below 7-day stale threshold
    )

    result = run_draft_closer()

    assert result.pages_finalized == 0
    assert result.pages_escalated == 0
    front_after, _ = fm.parse(page.read_text())
    assert front_after.get("draft") is True


# ---------------------------------------------------------------------------
# scheduler entry
# ---------------------------------------------------------------------------


def test_draft_closer_schedule_constant_defined():
    """DRAFT_CLOSER_SCHEDULE is a dict with required scheduler fields."""
    assert isinstance(DRAFT_CLOSER_SCHEDULE, dict)
    assert "name" in DRAFT_CLOSER_SCHEDULE
    assert "cron" in DRAFT_CLOSER_SCHEDULE
    assert DRAFT_CLOSER_SCHEDULE["name"] == "draft-closer"
