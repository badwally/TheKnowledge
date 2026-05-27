"""INT-14: wiki digest — daily content brief.

build_wiki_digest() returns a channel-agnostic markdown string summarising:
- New sources ingested in the last N hours (by domain)
- New synthesis pages created in the last N hours
- Stale drafts (draft: true, older than stale_days)
- Filter-correction / triage queue depth

Never sends anything — Message Send Gate is absolute.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

from gateway import frontmatter as fm, paths
from gateway.core import parse_iso


_DEFAULT_HOURS = 24
_DEFAULT_STALE_DAYS = 7


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _new_sources(since: datetime) -> list[dict]:
    """Sources ingested after `since`, sorted newest-first."""
    hits = []
    for source_type in paths.SOURCE_TYPES:
        source_dir = paths.raw_dir() / source_type
        if not source_dir.exists():
            continue
        for p in source_dir.glob("*.md"):
            try:
                front, _ = fm.parse(p.read_text())
            except Exception:
                continue
            ingested = front.get("ingested_at", "")
            dt = parse_iso(ingested) if ingested else None
            if dt and dt >= since:
                hits.append({
                    "source_id": front.get("id", p.stem),
                    "title": front.get("title", p.stem),
                    "type": source_type,
                    "domains": front.get("domain", front.get("domains", [])),
                    "ingested_at": ingested,
                })
    hits.sort(key=lambda x: x["ingested_at"], reverse=True)
    return hits


def _new_synthesis(since: datetime) -> list[dict]:
    """Synthesis pages with created_at after `since`."""
    synth_dir = paths.wiki_dir() / "synthesis"
    if not synth_dir.exists():
        return []
    hits = []
    for p in synth_dir.glob("*.md"):
        try:
            front, _ = fm.parse(p.read_text())
        except Exception:
            continue
        created = front.get("created_at", "")
        dt = parse_iso(created) if created else None
        if dt and dt >= since:
            hits.append({
                "slug": front.get("slug", p.stem),
                "title": front.get("title", p.stem),
                "domains": front.get("domains", []),
                "created_at": created,
            })
    hits.sort(key=lambda x: x["created_at"], reverse=True)
    return hits


def _stale_draft_count(stale_cutoff: datetime) -> int:
    """Count wiki pages with draft: true and mtime older than stale_cutoff."""
    count = 0
    for p in paths.wiki_dir().rglob("*.md"):
        if p.stat().st_mtime < stale_cutoff.timestamp():
            try:
                front, _ = fm.parse(p.read_text())
                if front.get("draft"):
                    count += 1
            except Exception:
                continue
    return count


def _triage_queue_depth() -> int:
    """Count pending triage YAML files."""
    triage_dir = paths.knowledge_internal() / "triage"
    if not triage_dir.exists():
        return 0
    return sum(1 for p in triage_dir.glob("*.yaml"))


def build_wiki_digest(
    *,
    hours: float = _DEFAULT_HOURS,
    stale_days: int = _DEFAULT_STALE_DAYS,
) -> str:
    """Return a markdown digest string. Never writes or sends anything."""
    now = _utcnow()
    since = now - timedelta(hours=hours)
    stale_cutoff = now - timedelta(days=stale_days)
    date_str = now.strftime("%Y-%m-%d")

    sources = _new_sources(since)
    syntheses = _new_synthesis(since)
    stale_count = _stale_draft_count(stale_cutoff)
    triage_depth = _triage_queue_depth()

    lines = [f"# Wiki Digest — {date_str}", ""]

    # --- new sources ---
    lines.append(f"## New sources (last {int(hours)}h)")
    lines.append("")
    if not sources:
        lines.append("_None._")
    else:
        by_domain: dict[str, list[dict]] = {}
        for s in sources:
            domains = s["domains"]
            if isinstance(domains, str):
                domains = [domains]
            key = domains[0] if domains else "untagged"
            by_domain.setdefault(key, []).append(s)
        for domain, items in sorted(by_domain.items()):
            lines.append(f"**{domain}** ({len(items)})")
            for item in items[:5]:
                lines.append(f"  - [{item['source_id']}] {item['title'][:80]}")
            if len(items) > 5:
                lines.append(f"  - … and {len(items) - 5} more")
    lines.append("")

    # --- new synthesis ---
    lines.append(f"## New synthesis (last {int(hours)}h)")
    lines.append("")
    if not syntheses:
        lines.append("_None._")
    else:
        for s in syntheses[:10]:
            domains = s["domains"]
            tag = f"[{domains[0]}] " if domains else ""
            lines.append(f"- {tag}{s['title'][:80]} — `{s['slug']}`")
        if len(syntheses) > 10:
            lines.append(f"- … and {len(syntheses) - 10} more")
    lines.append("")

    # --- stale drafts ---
    lines.append(f"## Stale drafts (>{stale_days}d)")
    lines.append("")
    if stale_count == 0:
        lines.append("_None._")
    else:
        lines.append(
            f"{stale_count} page(s) with `draft: true` older than {stale_days} days."
        )
        lines.append("Run `wiki finalize-batch --suggest` to review.")
    lines.append("")

    # --- triage queue ---
    lines.append("## Triage queue")
    lines.append("")
    if triage_depth == 0:
        lines.append("_Empty._")
    else:
        lines.append(f"{triage_depth} source(s) awaiting domain assignment.")
        lines.append("Run `wiki triage list` to review.")
    lines.append("")

    return "\n".join(lines)
