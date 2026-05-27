"""Backfill missing sources_count on synthesis pages (M96).

Synthesis pages written before sources_count became a required field lack the
field entirely. This op counts [[sources/...]] wikilinks in the body and stamps
the field. Idempotent: pages that already have sources_count are skipped.
"""

from __future__ import annotations

import re

from gateway import frontmatter as fm, log, paths, wiki_pages
from gateway.core import OperationResult, write_atomic

_SOURCES_LINK_RE = re.compile(r"\[\[sources/[^\]]+\]\]")


def _count_unique_sources(body: str) -> int:
    return len(set(_SOURCES_LINK_RE.findall(body)))


def backfill_sources_count(*, dry_run: bool = False) -> OperationResult:
    """Stamp missing sources_count on synthesis pages by counting [[sources/...]] links."""
    schema = wiki_pages.PAGE_SCHEMAS.get("synthesis")
    if schema is None:
        return OperationResult(success=False, errors=["synthesis page schema not found"])

    synth_dir = paths.knowledge_root() / schema.directory
    if not synth_dir.exists():
        return OperationResult(success=True, summary="backfill-sources-count: no synthesis directory")

    updated = 0
    skipped = 0
    errors: list[str] = []

    for path in sorted(synth_dir.rglob("*.md")):
        try:
            text = path.read_text()
            front, body = fm.parse(text)
        except Exception as e:
            errors.append(f"{path.name}: read/parse error — {e!r}")
            continue

        if front.get("sources_count") is not None:
            skipped += 1
            continue

        count = _count_unique_sources(body)
        new_front = dict(front)
        new_front["sources_count"] = count

        if not dry_run:
            try:
                write_atomic(path, fm.serialize(new_front, body))
            except Exception as e:
                errors.append(f"{path.name}: write error — {e!r}")
                continue

        updated += 1

    if not dry_run:
        log.append(
            op="backfill-sources-count",
            fields={"updated": updated, "skipped": skipped, "errors": len(errors)},
            summary=f"backfill-sources-count: {updated} updated, {skipped} skipped, {len(errors)} errors",
        )

    mode = " (dry-run)" if dry_run else ""
    return OperationResult(
        success=len(errors) == 0,
        errors=errors,
        summary=(
            f"backfill-sources-count{mode}: {updated} updated, "
            f"{skipped} skipped, {len(errors)} errors"
        ),
    )
