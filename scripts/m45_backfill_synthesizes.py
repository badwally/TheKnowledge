#!/usr/bin/env python3
"""M45 one-off: retrofit `synthesizes:` + `## Included works` onto draft
synthesis pages produced by earlier research runs (before M45 landed).

Given a research session-id prefix, finds all `wiki/synthesis/<prefix>*.md`
pages, computes the constituent set for each from the wikilinks already
present in the body, and rewrites the frontmatter + body to add the M45
fields. Per-theme branches get `synthesizes: [sources/...]`; the
cross-cutting page (matched by ``-cross-cutting`` suffix) gets
``synthesizes: [synthesis/...]`` pointing to its sibling per-theme pages.

Idempotent: pages that already have `synthesizes:` are left untouched.

Usage::

    .venv/bin/python scripts/m45_backfill_synthesizes.py <session-id-prefix>
    # e.g. scripts/m45_backfill_synthesizes.py 2026-05-11-what-is-the-established-methodology-stack
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from gateway import frontmatter as fm
from gateway import paths
from gateway.core import write_atomic


_SOURCES_RE = re.compile(r"\[\[(sources/[A-Za-z0-9][A-Za-z0-9_-]*)(?:#[^\]]*)?\]\]")


def _collect_source_constituents(body: str) -> list[str]:
    return sorted({m.group(1) for m in _SOURCES_RE.finditer(body)})


def _insert_included_works(body: str, constituents: list[str]) -> str:
    """Append a `## Included works` section to the body, after the
    `## Sources cited` section if present, otherwise at the very end.
    """
    section_lines = ["## Included works", ""]
    for target in constituents:
        section_lines.append(f"- [[{target}]]")
    section_lines.append("")
    section = "\n".join(section_lines)

    body = body.rstrip() + "\n\n"
    if "## Included works" in body:
        return body  # already present; caller should have skipped
    return body + section


def _is_cross_cutting(slug: str) -> bool:
    return slug.endswith("-cross-cutting")


def backfill(session_prefix: str) -> int:
    synth_dir = paths.knowledge_root() / "wiki" / "synthesis"
    targets = sorted(synth_dir.glob(f"{session_prefix}*.md"))
    if not targets:
        print(f"no synthesis pages found matching {session_prefix!r}", file=sys.stderr)
        return 1

    # First pass: classify per-theme vs cross-cutting, collect slug list
    classified: list[tuple[Path, dict, str, bool]] = []  # (path, front, body, is_cross_cutting)
    per_theme_slugs: list[str] = []
    for path in targets:
        text = path.read_text()
        front, body = fm.parse(text)
        if not isinstance(front, dict):
            print(f"skip (no frontmatter): {path.name}", file=sys.stderr)
            continue
        if front.get("type") != "synthesis":
            continue
        slug = str(front.get("slug", ""))
        if not slug:
            continue
        is_cc = _is_cross_cutting(slug)
        if not is_cc:
            per_theme_slugs.append(slug)
        classified.append((path, front, body, is_cc))

    if not classified:
        print(f"no synthesis pages with valid frontmatter under {session_prefix!r}", file=sys.stderr)
        return 1

    print(f"found {len(classified)} synthesis page(s) under {session_prefix!r}:")
    for path, front, _, is_cc in classified:
        kind = "cross-cutting" if is_cc else "per-theme"
        already = "synthesizes" in front
        print(f"  {kind:13s} {'(has synthesizes)' if already else '(will backfill) ':17s} {path.name}")

    written = 0
    for path, front, body, is_cc in classified:
        if "synthesizes" in front and front["synthesizes"]:
            continue  # idempotent: skip already-backfilled pages

        if is_cc:
            sibling_slugs = [s for s in per_theme_slugs if s != front.get("slug")]
            if len(sibling_slugs) < 2:
                print(f"  skip (cross-cutting needs ≥2 sibling per-theme pages): {path.name}", file=sys.stderr)
                continue
            constituents = sorted({f"synthesis/{s}" for s in sibling_slugs})
        else:
            constituents = _collect_source_constituents(body)
            if len(constituents) < 2:
                print(f"  skip (per-theme needs ≥2 source citations to enable exemption): {path.name}", file=sys.stderr)
                continue

        front["synthesizes"] = constituents
        new_body = _insert_included_works(body, constituents)
        new_text = fm.serialize(front, new_body)
        write_atomic(path, new_text)
        written += 1
        print(f"  wrote {len(constituents)} entries → {path.name}")

    print(f"\nbackfilled {written} page(s)")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    sys.exit(backfill(sys.argv[1]))
