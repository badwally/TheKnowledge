"""INT-13: wiki agenda — calendar-aware meeting prep.

build_agenda(date_str, events) returns a channel-agnostic markdown briefing for
calendar events with ≥2 attendees.  It reads wiki/entities/ and wiki/concepts/
to surface relevant context — no writes, no external calls.

The caller (CLI or MCP tool) is responsible for fetching calendar events from
Google Calendar MCP before calling this function.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from gateway import frontmatter as fm, paths
from gateway.core import write_atomic


def _slugify(name: str) -> str:
    """Normalize a display name to a wiki entity slug guess."""
    s = name.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s


def _entity_path(slug: str) -> Path:
    return paths.wiki_dir() / "entities" / f"{slug}.md"


def _concept_path(slug: str) -> Path:
    return paths.wiki_dir() / "concepts" / f"{slug}.md"


def _read_summary(p: Path, max_chars: int = 400) -> str:
    """Return the Summary section body of a wiki page, truncated."""
    try:
        _, body = fm.parse(p.read_text())
    except Exception:
        return ""
    m = re.search(r"## Summary\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    if not m:
        return body[:max_chars].strip()
    return m.group(1).strip()[:max_chars]


def _find_entity(name: str) -> tuple[str, str] | None:
    """Return (slug, summary_excerpt) if an entity wiki page matches name."""
    slug = _slugify(name)
    p = _entity_path(slug)
    if p.exists():
        return slug, _read_summary(p)

    # Try first-last reversal (email display names are sometimes "Last, First")
    parts = [x.strip() for x in name.split(",")]
    if len(parts) == 2:
        slug2 = _slugify(f"{parts[1]} {parts[0]}")
        p2 = _entity_path(slug2)
        if p2.exists():
            return slug2, _read_summary(p2)

    return None


def _find_concepts(event_title: str, event_description: str) -> list[tuple[str, str]]:
    """Return [(slug, summary_excerpt)] for concept pages whose slug words appear in event text."""
    combined = f"{event_title} {event_description}".lower()
    concepts_dir = paths.wiki_dir() / "concepts"
    if not concepts_dir.exists():
        return []
    hits = []
    for p in sorted(concepts_dir.glob("*.md")):
        slug = p.stem
        # Match if any hyphen-delimited word from the slug appears in text
        words = slug.split("-")
        if any(len(w) > 3 and w in combined for w in words):
            hits.append((slug, _read_summary(p)))
        if len(hits) >= 5:
            break
    return hits


def _format_time(event: dict[str, Any]) -> str:
    start = event.get("start", {})
    dt_str = start.get("dateTime", start.get("date", ""))
    if not dt_str:
        return ""
    try:
        # strip timezone offset for display
        dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
        return dt.strftime("%-I:%M %p")
    except Exception:
        return dt_str[:16]


def _attendee_names(event: dict[str, Any]) -> list[str]:
    attendees = event.get("attendees", [])
    return [a.get("displayName") or a.get("email", "") for a in attendees if a.get("email")]


def _build_event_section(event: dict[str, Any]) -> str:
    title = event.get("summary", "Untitled event")
    time_str = _format_time(event)
    names = _attendee_names(event)
    description = event.get("description", "") or ""

    lines = [f"### {title}" + (f" — {time_str}" if time_str else ""), ""]

    # Attendees with wiki entity lookup
    lines.append("**Attendees**")
    for name in names:
        result = _find_entity(name)
        if result:
            slug, excerpt = result
            lines.append(f"- [[entities/{slug}]] ({name})")
            if excerpt:
                lines.append(f"  > {excerpt[:200]}")
        else:
            lines.append(f"- {name}")
    lines.append("")

    # Related wiki concepts
    concepts = _find_concepts(title, description)
    if concepts:
        lines.append("**Relevant wiki context**")
        for slug, excerpt in concepts:
            lines.append(f"- [[concepts/{slug}]]")
            if excerpt:
                lines.append(f"  > {excerpt[:200]}")
        lines.append("")

    # Agenda / description passthrough
    if description.strip():
        lines.append("**Agenda notes**")
        lines.append(description.strip()[:600])
        lines.append("")

    return "\n".join(lines)


def build_agenda(date_str: str, events: list[dict[str, Any]]) -> str:
    """Return a markdown meeting-prep briefing. Never writes or sends anything.

    Args:
        date_str: ISO date string (YYYY-MM-DD).
        events: Calendar event dicts (Google Calendar API format).
                Only events with ≥2 attendees are included.
    """
    now = datetime.now(timezone.utc)
    generated = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        f"# Agenda — {date_str}",
        f"_Generated {generated}_",
        "",
    ]

    multi_attendee = [e for e in events if len(_attendee_names(e)) >= 2]

    if not multi_attendee:
        lines.append("_No meetings with multiple attendees found._")
        return "\n".join(lines)

    for event in multi_attendee:
        lines.append(_build_event_section(event))

    return "\n".join(lines)


def write_agenda(date_str: str, events: list[dict[str, Any]]) -> Path:
    """Write the agenda to wiki/agenda/<date>.md and return the path."""
    content = build_agenda(date_str, events)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    front = {"type": "agenda", "date": date_str, "generated_at": now}
    page = fm.serialize(front, content)

    out_dir = paths.agenda_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{date_str}.md"
    write_atomic(out_path, page)
    return out_path
