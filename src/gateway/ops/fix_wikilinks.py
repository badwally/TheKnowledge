"""wiki fix-wikilinks — repair broken [[target]] wikilinks in wiki pages (M97).

Strategy:
  - Broken [[sources/...]] citations → removed (dead citation; source does not exist)
  - Broken [[entities/...]] / [[concepts/...]] links → converted to
    [[target|slug]] aliased form (ERROR → WARNING; preserves forward-reference intent)

Idempotent: aliased links are already WARNINGs, not ERRORs, so they are
not re-processed. Source removals leave no trace.
"""

from __future__ import annotations

import re

from gateway import citations, frontmatter as fm, log, paths
from gateway.core import OperationResult, write_atomic
from gateway.lint._walk import walk_wiki_pages

_CHECKABLE_PREFIXES = frozenset(
    {"sources/", "entities/", "concepts/", "mocs/", "synthesis/"}
)
_SOURCE_PREFIX = "sources/"
_DOWNGRADE_PREFIXES = frozenset({"entities/", "concepts/", "mocs/", "synthesis/"})


def _target_exists(target: str, kb_root) -> bool:
    candidate = kb_root / "wiki" / f"{target}.md"
    return candidate.is_file()


def _slug_from_target(target: str) -> str:
    return target.rsplit("/", 1)[-1]


def _fix_body(body: str, kb_root) -> tuple[str, int, int]:
    """Return (fixed_body, removed_count, downgraded_count)."""
    removed = 0
    downgraded = 0

    wikilinks = citations.find_wikilinks(body)
    replacements: list[tuple[str, str]] = []  # (original_raw, replacement)

    seen: set[str] = set()
    for c in wikilinks:
        target = c.target
        if target.startswith("nlm:"):
            continue
        if not any(target.startswith(p) for p in _CHECKABLE_PREFIXES):
            continue
        if "|" in c.raw:
            continue  # already aliased (WARNING, not ERROR) — skip
        if _target_exists(target, kb_root):
            continue
        if target in seen:
            continue
        seen.add(target)

        if target.startswith(_SOURCE_PREFIX):
            replacements.append((c.raw, ""))
            removed += 1
        elif any(target.startswith(p) for p in _DOWNGRADE_PREFIXES):
            slug = _slug_from_target(target)
            replacements.append((c.raw, f"[[{target}|{slug}]]"))
            downgraded += 1

    for original, replacement in replacements:
        body = body.replace(original, replacement)

    # Collapse multiple spaces / blank lines that stray removals may leave
    body = re.sub(r" {2,}", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body)

    return body, removed, downgraded


def fix_wikilinks(*, dry_run: bool = False) -> OperationResult:
    """Repair broken wikilinks across all wiki pages."""
    kb_root = paths.knowledge_root()
    total_removed = 0
    total_downgraded = 0
    pages_touched = 0
    errors: list[str] = []

    for _type, path, front, body in walk_wiki_pages():
        try:
            fixed_body, removed, downgraded = _fix_body(body, kb_root)
        except Exception as e:
            errors.append(f"{path.name}: error — {e!r}")
            continue

        if removed == 0 and downgraded == 0:
            continue

        total_removed += removed
        total_downgraded += downgraded
        pages_touched += 1

        if not dry_run:
            try:
                write_atomic(path, fm.serialize(front, fixed_body))
            except Exception as e:
                errors.append(f"{path.name}: write error — {e!r}")

    if not dry_run and pages_touched:
        log.append(
            op="fix-wikilinks",
            fields={
                "pages": pages_touched,
                "removed": total_removed,
                "downgraded": total_downgraded,
                "errors": len(errors),
            },
            summary=(
                f"fix-wikilinks: {pages_touched} pages — "
                f"{total_removed} source links removed, "
                f"{total_downgraded} links downgraded to WARNING"
            ),
        )

    mode = " (dry-run)" if dry_run else ""
    return OperationResult(
        success=len(errors) == 0,
        errors=errors,
        summary=(
            f"fix-wikilinks{mode}: {pages_touched} pages touched — "
            f"{total_removed} source links removed, "
            f"{total_downgraded} links downgraded to forward-reference (WARNING)"
        ),
    )
