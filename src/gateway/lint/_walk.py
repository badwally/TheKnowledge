"""Shared filesystem walkers for lint checks.

Centralized so each check stays small. The wiki/raw walkers handle
malformed frontmatter gracefully (those errors are reported by
schema-drift, not by the using check).
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterator

from gateway import frontmatter as fm
from gateway import paths
from gateway import wiki_pages


def walk_wiki_pages() -> Iterator[tuple[str, Path, dict, str]]:
    """Yield (page_type, path, frontmatter, body) for every wiki page.

    Skips pages with malformed frontmatter (returns nothing for them; the
    schema-drift check reports those separately).
    """
    wiki = paths.wiki_dir()
    if not wiki.exists():
        return

    for type_name, schema in wiki_pages.PAGE_SCHEMAS.items():
        d = paths.knowledge_root() / schema.directory
        if not d.exists():
            continue
        for path in sorted(d.glob("**/*.md")):
            try:
                front, body = fm.parse(path.read_text())
            except (fm.FrontmatterError, OSError):
                continue
            yield type_name, path, front, body


def walk_raw_sources() -> Iterator[tuple[str, Path, dict, str]]:
    """Yield (source_type, path, frontmatter, body) for every raw source."""
    raw = paths.raw_dir()
    if not raw.exists():
        return

    for source_type in paths.SOURCE_TYPES:
        d = raw / source_type
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")):
            try:
                front, body = fm.parse(path.read_text())
            except (fm.FrontmatterError, OSError):
                continue
            yield source_type, path, front, body
