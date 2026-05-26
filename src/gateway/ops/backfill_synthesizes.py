"""ONT-11: backfill `synthesizes:` frontmatter on synthesis pages.

Walks wiki/synthesis/*.md, finds pages that lack `synthesizes:`, extracts
`[[sources/<id>]]` and `[[synthesis/<slug>]]` wikilinks from the body, and
proposes them as the `synthesizes:` list.

Rules:
- Skips pages that already have `synthesizes:` (non-empty list).
- Skips pages where no qualifying wikilinks are found in the body.
- Mixed tiers (sources/ + synthesis/) default to sources/ tier only (the
  lower-level tier), since mixed is invalid per validator.
- Writes via write_atomic — ARCH-14 compliant.
- Idempotent: re-running is safe.
"""

from __future__ import annotations

import re

from gateway import frontmatter as fm, paths
from gateway.citations import find_wikilinks
from gateway.core import OperationResult, write_atomic

_SYNTHESIZES_ENTRY_RE = re.compile(
    r"^(sources|synthesis)/[A-Za-z0-9][A-Za-z0-9_-]*$"
)


def _extract_candidates(body: str) -> list[str]:
    """Return sorted unique `sources/<id>` and `synthesis/<slug>` wikilink targets."""
    refs: set[str] = set()
    for citation in find_wikilinks(body):
        target = citation.target
        if target.startswith("sources/") or target.startswith("synthesis/"):
            if _SYNTHESIZES_ENTRY_RE.match(target):
                refs.add(target)
    return sorted(refs)


def _preferred_tier(candidates: list[str]) -> list[str]:
    """When candidates span both tiers, return sources/ only (mixed is invalid)."""
    sources = [c for c in candidates if c.startswith("sources/")]
    synths = [c for c in candidates if c.startswith("synthesis/")]
    if sources and synths:
        return sources  # prefer lower-level citations over meta-synthesis
    return candidates


def backfill_synthesizes(*, dry_run: bool = False) -> OperationResult:
    """Backfill `synthesizes:` from body wikilinks on synthesis pages.

    Summary encodes: updated / skipped / errors counts.
    """
    synth_dir = paths.wiki_dir() / "synthesis"
    if not synth_dir.exists():
        return OperationResult(
            success=True,
            summary="backfill-synthesizes: no synthesis dir",
        )

    updated = 0
    skipped = 0
    errors: list[str] = []

    for page in sorted(synth_dir.glob("*.md")):
        try:
            text = page.read_text(encoding="utf-8")
            front, body = fm.parse(text)
        except Exception as e:
            errors.append(f"{page.name}: parse error — {e!r}")
            continue

        existing = front.get("synthesizes")
        if existing and isinstance(existing, list) and len(existing) > 0:
            skipped += 1
            continue

        candidates = _extract_candidates(body)
        if not candidates:
            skipped += 1
            continue

        candidates = _preferred_tier(candidates)

        if not dry_run:
            front["synthesizes"] = candidates
            new_text = fm.serialize(front, body)
            write_atomic(page, new_text)

        updated += 1

    mode = " (dry-run)" if dry_run else ""
    return OperationResult(
        success=len(errors) == 0,
        errors=errors,
        summary=(
            f"backfill-synthesizes{mode}: {updated} updated, "
            f"{skipped} skipped, {len(errors)} errors"
        ),
    )
