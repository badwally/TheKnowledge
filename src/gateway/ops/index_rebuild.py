"""wiki index --rebuild: regenerate index.md from current wiki + raw state.

Produces the domain-grouped catalog described in WIKI.md § 7.
Replaces the incremental "Recent ingests" flat list with a structured,
navigable snapshot of the full knowledge base.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from gateway import frontmatter as fm, paths
from gateway.core import OperationResult, write_atomic


_MAX_LINKS_PER_SECTION = 12  # truncate long lists in index for readability


@dataclass
class _DomainEntry:
    slug: str
    source_count: int = 0
    entity_slugs: list[str] = field(default_factory=list)
    concept_slugs: list[str] = field(default_factory=list)
    synthesis_slugs: list[str] = field(default_factory=list)
    artifact_slugs: list[str] = field(default_factory=list)
    source_slugs: list[str] = field(default_factory=list)


def rebuild(*, dry_run: bool = False) -> OperationResult:
    """Regenerate index.md with current wiki + raw state.

    Scans wiki/ and raw/ to build a domain-grouped catalog per WIKI.md § 7.
    Writes index.md atomically (unless dry_run=True).
    Returns OperationResult with counts in `data`.
    """
    domains = _collect_domains()
    raw_totals = _count_raw_sources()
    wiki_totals = _collect_wiki_pages()

    total_sources = sum(raw_totals.values())
    total_raw = total_sources

    entries: dict[str, _DomainEntry] = {}
    for domain_slug in sorted(domains.union(raw_totals.keys()).union(wiki_totals.keys())):
        entry = _DomainEntry(slug=domain_slug)
        entry.source_count = raw_totals.get(domain_slug, 0)
        for page_type, slug_list in wiki_totals.get(domain_slug, {}).items():
            if page_type == "entity":
                entry.entity_slugs = slug_list
            elif page_type == "concept":
                entry.concept_slugs = slug_list
            elif page_type == "synthesis":
                entry.synthesis_slugs = slug_list
            elif page_type == "artifact":
                entry.artifact_slugs = slug_list
            elif page_type == "source":
                entry.source_slugs = slug_list
        entries[domain_slug] = entry

    # compute cross-domain: wiki pages appearing in 2+ domains
    cross_domain_pages = _find_cross_domain_pages()

    orphan_count = _lint_orphan_count()

    content = _render_index(
        entries=entries,
        cross_domain_pages=cross_domain_pages,
        orphan_count=orphan_count,
        total_raw=total_raw,
    )

    fts_stats = None
    if not dry_run:
        index_path = paths.index_path()
        write_atomic(index_path, content)
        # WS1: rebuild the derived FTS5 retrieval index alongside index.md.
        from gateway import search_index
        fts_stats = search_index.refresh(rebuild=True)

    summary = f"index rebuilt: {len(entries)} domains, {total_raw} raw sources"
    if fts_stats is not None:
        summary += f"; search index: {fts_stats.total_pages} pages"

    return OperationResult(
        success=True,
        summary=summary,
        data={
            "domains": len(entries),
            "raw_sources": total_raw,
            "dry_run": dry_run,
            "search_index_pages": fts_stats.total_pages if fts_stats else None,
        },
    )


def _collect_domains() -> set[str]:
    """Return domain slugs that have a MOC page."""
    moc_dir = paths.wiki_dir() / "mocs"
    if not moc_dir.exists():
        return set()
    return {p.stem for p in moc_dir.glob("*.md")}


def _get_page_domains(front: dict[str, Any]) -> list[str]:
    """Extract domain list from a frontmatter dict (handles singular and plural)."""
    domains = front.get("domains", [])
    if isinstance(domains, list):
        return [str(d) for d in domains if d]
    if domains:
        return [str(domains)]
    singular = front.get("domain", "")
    if singular:
        return [str(singular)]
    return []


def _count_raw_sources() -> dict[str, int]:
    """Count raw source files per domain."""
    counts: dict[str, int] = defaultdict(int)
    raw = paths.raw_dir()
    if not raw.exists():
        return counts
    for md_path in raw.rglob("*.md"):
        try:
            text = md_path.read_text(errors="replace")
            front, _ = fm.parse(text)
        except Exception:
            continue
        for domain in _get_page_domains(front):
            counts[domain] += 1
        if not _get_page_domains(front):
            counts["__untagged__"] += 1
    return counts


_DIR_TO_TYPE: dict[str, str] = {
    "entities": "entity",
    "concepts": "concept",
    "synthesis": "synthesis",
    "mocs": "moc",
    "sources": "source",
    "artifacts": "artifact",
    "proposals": "proposal",
}


def _collect_wiki_pages() -> dict[str, dict[str, list[str]]]:
    """Collect wiki page slugs by domain and type.

    Returns: {domain_slug: {page_type: [slug, ...]}}
    """
    result: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    wiki = paths.wiki_dir()
    if not wiki.exists():
        return result

    for subdir in wiki.iterdir():
        if not subdir.is_dir():
            continue
        page_type = _DIR_TO_TYPE.get(subdir.name, subdir.name)
        for md_path in sorted(subdir.glob("*.md")):
            try:
                text = md_path.read_text(errors="replace")
                front, _ = fm.parse(text)
            except Exception:
                continue
            slug = md_path.stem
            for domain in _get_page_domains(front):
                result[domain][page_type].append(slug)
            if not _get_page_domains(front):
                result["__untagged__"][page_type].append(slug)
    return result


def _find_cross_domain_pages() -> dict[str, list[str]]:
    """Find wiki pages tagged with 2+ domains.

    Returns: {page_type: [slug, ...]} for cross-domain pages.
    """
    cross: dict[str, list[str]] = defaultdict(list)
    wiki = paths.wiki_dir()
    if not wiki.exists():
        return cross
    for subdir in wiki.iterdir():
        if not subdir.is_dir():
            continue
        page_type = _DIR_TO_TYPE.get(subdir.name, subdir.name)
        for md_path in subdir.glob("*.md"):
            try:
                text = md_path.read_text(errors="replace")
                front, _ = fm.parse(text)
            except Exception:
                continue
            domains = _get_page_domains(front)
            if len(domains) >= 2:
                cross[page_type].append(md_path.stem)
    return cross


def _lint_orphan_count() -> int:
    """Count raw sources with no inbound wiki citations (fast path)."""
    try:
        from gateway.lint import orphans as _orphans
        findings = _orphans.run()
        return len(findings)
    except Exception:
        return -1  # unavailable


def _wikilink(path: str, slug: str) -> str:
    return f"[[{path}/{slug}]]"


def _render_section_links(slugs: list[str], path: str, max_shown: int = _MAX_LINKS_PER_SECTION) -> str:
    shown = slugs[:max_shown]
    links = " · ".join(_wikilink(path, s) for s in shown)
    if len(slugs) > max_shown:
        links += f" · … ({len(slugs) - max_shown} more)"
    return links


def _render_index(
    *,
    entries: dict[str, "_DomainEntry"],
    cross_domain_pages: dict[str, list[str]],
    orphan_count: int,
    total_raw: int,
) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    total_entities = sum(len(e.entity_slugs) for e in entries.values())
    total_concepts = sum(len(e.concept_slugs) for e in entries.values())
    total_synthesis = sum(len(e.synthesis_slugs) for e in entries.values())

    lines: list[str] = [
        "# Knowledge Index",
        "",
        f"Last rebuilt: {now}",
        f"Sources: {total_raw} | Entities: {total_entities} | Concepts: {total_concepts} | Synthesis: {total_synthesis}",
        "",
        "## Domains",
        "",
    ]

    for domain_slug, entry in entries.items():
        if domain_slug == "__untagged__":
            continue
        lines.append(f"### {domain_slug}")
        moc_link = _wikilink("mocs", domain_slug)
        lines.append(f"{moc_link} · {entry.source_count} sources")
        lines.append("")

        if entry.entity_slugs:
            links = _render_section_links(sorted(entry.entity_slugs), "entities")
            lines.append(f"- Entities: {links}")
        if entry.concept_slugs:
            links = _render_section_links(sorted(entry.concept_slugs), "concepts")
            lines.append(f"- Concepts: {links}")
        if entry.synthesis_slugs:
            links = _render_section_links(sorted(entry.synthesis_slugs), "synthesis")
            lines.append(f"- Synthesis: {links}")
        if entry.artifact_slugs:
            links = _render_section_links(sorted(entry.artifact_slugs), "artifacts")
            lines.append(f"- Artifacts: {links}")
        lines.append("")

    # Untagged section
    untagged = entries.get("__untagged__")
    if untagged and untagged.source_count > 0:
        lines.append("### (untagged)")
        lines.append(f"{untagged.source_count} sources without a domain tag")
        lines.append("")

    # Cross-domain section
    cross_items = [(t, slugs) for t, slugs in sorted(cross_domain_pages.items()) if slugs]
    if cross_items:
        lines.append("## Cross-domain")
        lines.append("")
        for page_type, slugs in cross_items:
            dir_name = f"{page_type}s" if not page_type.endswith("s") else page_type
            links = _render_section_links(sorted(slugs), dir_name)
            lines.append(f"- {page_type.capitalize()}: {links}")
        lines.append("")

    # Health summary
    lines.append("## Health")
    lines.append("")
    orphan_str = str(orphan_count) if orphan_count >= 0 else "unknown"
    lines.append(f"- Orphans: {orphan_str} — see `wiki lint --scope orphans`")
    try:
        inbox = paths.raw_inbox_dir()
        inbox_count = len(list(inbox.glob("*"))) if inbox.exists() else 0
    except Exception:
        inbox_count = 0
    lines.append(f"- Untriaged inbox: {inbox_count} — see `raw/inbox/`")
    lines.append("")

    return "\n".join(lines)
