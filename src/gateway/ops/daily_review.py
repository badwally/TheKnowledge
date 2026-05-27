"""TOOL-8: wiki daily — morning triage list.

run_daily_review() returns a DailyReviewResult with:
  - stale_drafts: wiki pages with draft: true older than stale_days
  - orphan_sources: raw sources with no wiki coverage (wiki_pages: [])
  - recently_ingested: raw sources ingested within lookback_hours
  - inbox_count / inbox_failed: watcher inbox state
  - triage_queue_depth: pending triage YAML files

Read-only; never writes or sends.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

from gateway import frontmatter as fm, paths
from gateway.core import OperationResult


_DEFAULT_LOOKBACK_HOURS = 24
_DEFAULT_STALE_DAYS = 7
_DEFAULT_ORPHAN_LIMIT = 30


# --------------------------------------------------------------------------- #
# Result types                                                                 #
# --------------------------------------------------------------------------- #


@dataclass
class DraftItem:
    slug: str
    title: str
    age_days: int
    wiki_path: str


@dataclass
class OrphanSourceItem:
    source_id: str
    title: str
    source_type: str
    ingested_at: str


@dataclass
class IngestedSourceItem:
    source_id: str
    title: str
    source_type: str
    domains: list[str]
    ingested_at: str


@dataclass
class DailyReviewResult:
    stale_drafts: list[DraftItem] = field(default_factory=list)
    orphan_sources: list[OrphanSourceItem] = field(default_factory=list)
    recently_ingested: list[IngestedSourceItem] = field(default_factory=list)
    inbox_count: int = 0
    inbox_failed: int = 0
    triage_queue_depth: int = 0
    as_of: str = ""


# --------------------------------------------------------------------------- #
# Data collectors                                                              #
# --------------------------------------------------------------------------- #


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _parse_iso(s: str) -> datetime | None:
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(s, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue
    return None


def _collect_stale_drafts(*, now: datetime, stale_days: int) -> list[DraftItem]:
    threshold = timedelta(days=stale_days)
    results: list[DraftItem] = []
    wiki = paths.wiki_dir()
    if not wiki.exists():
        return results
    for sub in ("entities", "concepts", "synthesis", "mocs", "sources", "proposals"):
        d = wiki / sub
        if not d.exists():
            continue
        for path in d.glob("*.md"):
            try:
                front, _ = fm.parse(path.read_text())
            except Exception:
                continue
            if not front.get("draft"):
                continue
            started_raw = front.get("draft_started_at") or front.get("created_at")
            if started_raw:
                started = _parse_iso(str(started_raw))
            else:
                started = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
            if started is None:
                continue
            age = now - started
            if age > threshold:
                results.append(DraftItem(
                    slug=path.stem,
                    title=str(front.get("title", path.stem)),
                    age_days=age.days,
                    wiki_path=str(path.relative_to(paths.knowledge_root())),
                ))
    results.sort(key=lambda x: x.age_days, reverse=True)
    return results


def _collect_orphan_sources(*, limit: int) -> list[OrphanSourceItem]:
    """Raw sources where wiki_pages is empty — no wiki coverage yet."""
    results: list[OrphanSourceItem] = []
    for source_type in paths.SOURCE_TYPES:
        source_dir = paths.raw_dir() / source_type
        if not source_dir.exists():
            continue
        for p in source_dir.glob("*.md"):
            if len(results) >= limit:
                break
            try:
                front, _ = fm.parse(p.read_text())
            except Exception:
                continue
            wiki_pages = front.get("wiki_pages", [])
            if wiki_pages:
                continue
            results.append(OrphanSourceItem(
                source_id=str(front.get("id", p.stem)),
                title=str(front.get("title", p.stem))[:120],
                source_type=source_type,
                ingested_at=str(front.get("ingested_at", "")),
            ))
    return results


def _collect_recently_ingested(*, since: datetime) -> list[IngestedSourceItem]:
    results: list[IngestedSourceItem] = []
    for source_type in paths.SOURCE_TYPES:
        source_dir = paths.raw_dir() / source_type
        if not source_dir.exists():
            continue
        for p in source_dir.glob("*.md"):
            try:
                front, _ = fm.parse(p.read_text())
            except Exception:
                continue
            ingested_raw = str(front.get("ingested_at", ""))
            dt = _parse_iso(ingested_raw) if ingested_raw else None
            if dt and dt >= since:
                domains = front.get("domain") or front.get("domains") or []
                if isinstance(domains, str):
                    domains = [domains]
                results.append(IngestedSourceItem(
                    source_id=str(front.get("id", p.stem)),
                    title=str(front.get("title", p.stem))[:120],
                    source_type=source_type,
                    domains=list(domains),
                    ingested_at=ingested_raw,
                ))
    results.sort(key=lambda x: x.ingested_at, reverse=True)
    return results


def _triage_queue_depth() -> int:
    triage_dir = paths.knowledge_internal() / "triage"
    if not triage_dir.exists():
        return 0
    return sum(1 for _ in triage_dir.glob("*.yaml"))


# --------------------------------------------------------------------------- #
# Public API                                                                   #
# --------------------------------------------------------------------------- #


def run_daily_review(
    *,
    lookback_hours: float = _DEFAULT_LOOKBACK_HOURS,
    stale_days: int = _DEFAULT_STALE_DAYS,
    orphan_limit: int = _DEFAULT_ORPHAN_LIMIT,
) -> DailyReviewResult:
    """Collect the triage list. Read-only."""
    from gateway.watcher import watcher_state

    now = _utcnow()
    since = now - timedelta(hours=lookback_hours)
    state = watcher_state()

    return DailyReviewResult(
        stale_drafts=_collect_stale_drafts(now=now, stale_days=stale_days),
        orphan_sources=_collect_orphan_sources(limit=orphan_limit),
        recently_ingested=_collect_recently_ingested(since=since),
        inbox_count=state.get("inbox_pending", 0),
        inbox_failed=state.get("inbox_failed", 0),
        triage_queue_depth=_triage_queue_depth(),
        as_of=now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    )


def format_daily_review(result: DailyReviewResult, *, lookback_hours: float = 24, stale_days: int = 7) -> str:
    """Format a DailyReviewResult as a terminal-friendly triage list."""
    lines: list[str] = [f"Daily triage — {result.as_of[:10]}", ""]

    # Inbox
    lines.append(f"Inbox: {result.inbox_count} pending · {result.inbox_failed} failed")
    if result.triage_queue_depth:
        lines.append(f"Triage queue: {result.triage_queue_depth} awaiting domain assignment (`wiki triage list`)")
    lines.append("")

    # Recently ingested
    lines.append(f"New sources (last {int(lookback_hours)}h): {len(result.recently_ingested)}")
    for item in result.recently_ingested[:10]:
        domain_tag = f"[{item.domains[0]}] " if item.domains else ""
        lines.append(f"  + {domain_tag}{item.source_id}  {item.title[:60]}")
    if len(result.recently_ingested) > 10:
        lines.append(f"  … and {len(result.recently_ingested) - 10} more")
    lines.append("")

    # Stale drafts
    lines.append(f"Stale drafts (>{stale_days}d): {len(result.stale_drafts)}")
    for item in result.stale_drafts[:10]:
        lines.append(f"  ! {item.wiki_path}  ({item.age_days}d)  {item.title[:50]}")
    if len(result.stale_drafts) > 10:
        lines.append(f"  … and {len(result.stale_drafts) - 10} more")
    if result.stale_drafts:
        lines.append("  → run `wiki finalize-batch --suggest` to review")
    lines.append("")

    # Orphan sources
    lines.append(f"Orphan sources (no wiki coverage): {len(result.orphan_sources)}")
    for item in result.orphan_sources[:10]:
        lines.append(f"  ? {item.source_id}  [{item.source_type}]  {item.title[:60]}")
    if len(result.orphan_sources) > 10:
        lines.append(f"  … and {len(result.orphan_sources) - 10} more (--orphan-limit to expand)")
    if result.orphan_sources:
        lines.append("  → run `wiki ingest <id> --with-plan` or `wiki query` to build coverage")
    lines.append("")

    return "\n".join(lines)


def run_daily_review_op(
    *,
    lookback_hours: float = _DEFAULT_LOOKBACK_HOURS,
    stale_days: int = _DEFAULT_STALE_DAYS,
    orphan_limit: int = _DEFAULT_ORPHAN_LIMIT,
) -> OperationResult:
    result = run_daily_review(
        lookback_hours=lookback_hours,
        stale_days=stale_days,
        orphan_limit=orphan_limit,
    )
    return OperationResult(
        success=True,
        summary=format_daily_review(result, lookback_hours=lookback_hours, stale_days=stale_days),
    )
