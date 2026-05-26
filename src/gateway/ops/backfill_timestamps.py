"""ONT-6: backfill created_at / last_updated on existing wiki pages.

Entity, concept, and synthesis pages require created_at and last_updated
(enforced by the validator since ONT-6). Pages written before that constraint
was enforced may be missing these fields. This op stamps them using the
file's mtime as a proxy for the creation/update time.

Idempotent: pages that already have both fields are skipped.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from gateway import frontmatter as fm, log, paths, wiki_pages
from gateway.core import OperationResult, write_atomic


_TYPES_TO_BACKFILL = frozenset({"entity", "concept", "synthesis"})


def _mtime_iso(path: Path) -> str:
    """Return file mtime as ISO-8601 UTC string."""
    mtime = path.stat().st_mtime
    return datetime.fromtimestamp(mtime, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backfill_timestamps(*, dry_run: bool = False) -> OperationResult:
    """Stamp missing created_at / last_updated on entity/concept/synthesis pages.

    Uses file mtime as the timestamp proxy. Skips pages that already have
    both fields present.
    """
    updated = 0
    skipped = 0
    errors: list[str] = []

    for type_name, schema in wiki_pages.PAGE_SCHEMAS.items():
        if type_name not in _TYPES_TO_BACKFILL:
            continue
        type_dir = paths.knowledge_root() / schema.directory
        if not type_dir.exists():
            continue

        for path in sorted(type_dir.rglob("*.md")):
            try:
                text = path.read_text()
                front, body = fm.parse(text)
            except Exception as e:
                errors.append(f"{path.name}: read/parse error — {e!r}")
                continue

            has_created = bool(front.get("created_at"))
            has_updated = bool(front.get("last_updated"))
            if has_created and has_updated:
                skipped += 1
                continue

            stamp = _mtime_iso(path)
            new_front = dict(front)
            if not has_created:
                new_front["created_at"] = stamp
            if not has_updated:
                new_front["last_updated"] = stamp

            new_text = fm.serialize(new_front, body)

            if not dry_run:
                try:
                    write_atomic(path, new_text)
                except Exception as e:
                    errors.append(f"{path.name}: write error — {e!r}")
                    continue

            updated += 1

    if not dry_run:
        log.append(
            op="backfill-timestamps",
            fields={"updated": updated, "skipped": skipped, "errors": len(errors)},
            summary=f"backfill-timestamps: {updated} updated, {skipped} skipped, {len(errors)} errors",
        )

    mode = " (dry-run)" if dry_run else ""
    return OperationResult(
        success=len(errors) == 0,
        errors=errors,
        summary=(
            f"backfill-timestamps{mode}: {updated} updated, "
            f"{skipped} skipped, {len(errors)} errors"
        ),
    )
