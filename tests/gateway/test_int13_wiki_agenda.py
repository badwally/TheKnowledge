"""INT-13: wiki agenda — calendar-aware meeting prep tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.ops.wiki_agenda import build_agenda, write_agenda


def _make_event(
    summary: str = "Team Sync",
    attendees: list[str] | None = None,
    start: str = "2026-05-26T09:00:00Z",
    description: str = "",
) -> dict:
    names = attendees or ["alice@example.com", "bob@example.com"]
    return {
        "summary": summary,
        "start": {"dateTime": start},
        "attendees": [{"email": n, "displayName": n.split("@")[0].replace(".", " ").title()} for n in names],
        "description": description,
    }


def _write_entity(kb_root: Path, slug: str, name: str) -> Path:
    d = kb_root / "wiki" / "entities"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "entity",
        "slug": slug,
        "canonical_name": name,
        "entity_kind": "person",
        "domains": ["test"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, "## Summary\n\nThis is Alice.\n\n## Key facts\n\n- fact\n\n## Sources\n\n- \n\n## Related\n\n-\n"))
    return p


def _write_concept(kb_root: Path, slug: str, name: str) -> Path:
    d = kb_root / "wiki" / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": slug,
        "canonical_name": name,
        "domains": ["test"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, "## Summary\n\nThis concept.\n\n## Key claims\n\n- claim\n\n## Sources\n\n- \n\n## Related\n\n-\n"))
    return p


def test_agenda_header(kb_root: Path) -> None:
    digest = build_agenda("2026-05-26", [])
    assert "# Agenda — 2026-05-26" in digest


def test_agenda_no_events(kb_root: Path) -> None:
    digest = build_agenda("2026-05-26", [])
    assert "No meetings" in digest


def test_agenda_single_attendee_excluded(kb_root: Path) -> None:
    event = {
        "summary": "Solo Work",
        "start": {"dateTime": "2026-05-26T10:00:00Z"},
        "attendees": [{"email": "me@example.com", "displayName": "Me"}],
        "description": "",
    }
    digest = build_agenda("2026-05-26", [event])
    assert "Solo Work" not in digest


def test_agenda_multi_attendee_included(kb_root: Path) -> None:
    event = _make_event("Product Review")
    digest = build_agenda("2026-05-26", [event])
    assert "Product Review" in digest
    assert "Attendees" in digest


def test_agenda_entity_wiki_lookup(kb_root: Path) -> None:
    _write_entity(kb_root, "alice", "Alice")
    event = {
        "summary": "1:1",
        "start": {"dateTime": "2026-05-26T11:00:00Z"},
        "attendees": [
            {"email": "alice@example.com", "displayName": "Alice"},
            {"email": "bob@example.com", "displayName": "Bob"},
        ],
        "description": "",
    }
    digest = build_agenda("2026-05-26", [event])
    assert "entities/alice" in digest
    assert "This is Alice." in digest


def test_agenda_concept_lookup(kb_root: Path) -> None:
    _write_concept(kb_root, "food-noise", "food noise")
    event = _make_event("food-noise reduction research")
    digest = build_agenda("2026-05-26", [event])
    assert "concepts/food-noise" in digest


def test_write_agenda_creates_file(kb_root: Path) -> None:
    event = _make_event("Weekly Sync")
    out = write_agenda("2026-05-26", [event])
    assert out.exists()
    assert out.name == "2026-05-26.md"
    content = out.read_text()
    assert "Weekly Sync" in content
    assert "type: agenda" in content


def test_agenda_description_passthrough(kb_root: Path) -> None:
    event = _make_event(description="Q2 planning review and roadmap discussion")
    digest = build_agenda("2026-05-26", [event])
    assert "Q2 planning review" in digest
