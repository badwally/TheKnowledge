"""wiki abandon-stale-drafts — auto-abandon orphaned draft pages (M98).

A draft qualifies for abandonment when:
  1. `draft: true` is set in frontmatter
  2. `draft_started_at` is older than `min_age_days` days
  3. No other wiki page has a [[<type>/<slug>]] wikilink pointing to it

Qualifying drafts are passed to `finalize(path, abandon=True)`, which
deletes the page and removes backlinks from raw source `wiki_pages:` lists.
"""

from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

from gateway import log, paths
from gateway.core import OperationResult, parse_iso
from gateway.lint._walk import walk_wiki_pages

DEFAULT_MIN_AGE_DAYS = 30

_WIKILINK_TARGET_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")


def _wikilink_target(path: Path) -> str | None:
    """Return the wikilink target string for a wiki page path.

    e.g. /kb/wiki/concepts/foo.md → "concepts/foo"
    """
    kb_root = paths.knowledge_root()
    try:
        rel = path.relative_to(kb_root / "wiki")
    except ValueError:
        return None
    return str(rel.with_suffix(""))


def _build_inbound_index(all_pages: list[tuple[str, Path, dict, str]]) -> dict[str, list[Path]]:
    """Build map of wikilink-target → list of OTHER pages that mention it (self-refs excluded)."""
    index: dict[str, list[Path]] = {}
    for _type, path, _front, body in all_pages:
        self_target = _wikilink_target(path)
        for m in _WIKILINK_TARGET_RE.finditer(body):
            target = m.group(1).strip()
            if target == self_target:
                continue
            index.setdefault(target, []).append(path)
    return index


def abandon_stale_drafts(
    *,
    min_age_days: int = DEFAULT_MIN_AGE_DAYS,
    dry_run: bool = False,
) -> OperationResult:
    """Abandon orphaned draft pages older than `min_age_days` days."""
    from gateway.ops.finalize import finalize

    now = datetime.now(timezone.utc)
    threshold = timedelta(days=min_age_days)

    all_pages = list(walk_wiki_pages())
    inbound = _build_inbound_index(all_pages)

    candidates: list[tuple[Path, str]] = []
    for _type, path, front, _body in all_pages:
        if not front.get("draft"):
            continue
        started_raw = front.get("draft_started_at")
        if not started_raw:
            continue
        started = parse_iso(str(started_raw))
        if started is None:
            continue
        age = now - started
        if age <= threshold:
            continue

        target = _wikilink_target(path)
        if target is None:
            continue
        if inbound.get(target):
            continue

        candidates.append((path, target))

    abandoned = 0
    skipped = 0
    errors: list[str] = []

    for path, target in candidates:
        if dry_run:
            abandoned += 1
            continue
        result = finalize(path, abandon=True)
        if result.success:
            abandoned += 1
        else:
            skipped += 1
            errors.extend(result.errors)

    if not dry_run and abandoned:
        log.append(
            op="abandon-stale-drafts",
            fields={
                "abandoned": abandoned,
                "skipped": skipped,
                "min_age_days": min_age_days,
                "errors": len(errors),
            },
            summary=(
                f"abandon-stale-drafts: {abandoned} drafts abandoned "
                f"(>{min_age_days}d, no inbound citations)"
            ),
        )

    mode = " (dry-run)" if dry_run else ""
    return OperationResult(
        success=len(errors) == 0,
        errors=errors,
        summary=(
            f"abandon-stale-drafts{mode}: {abandoned} abandoned, "
            f"{skipped} skipped — threshold {min_age_days} days"
        ),
    )
