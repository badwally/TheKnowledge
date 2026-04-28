"""Per-vault migration orchestrator per MIGRATION.md.

`migrate_vault(legacy_vault_path, domain_slug, dry_run=False)` does the
following for one legacy Obsidian vault:

1. Walks `<vault>/sources/`, builds a slug map (legacy → canonical).
2. (dry-run halts here, returning the slug-map preview)
3. For each legacy source, writes `raw/<type>/<id>.md` + `wiki/sources/<id>.md`
   in canonical schema. Body is the legacy summary (lossy, flagged with
   `meta.legacy_recovery: "summary-only"`).
4. For each legacy concept page, ports the body verbatim with citation
   wikilinks rewritten to canonical IDs; fills missing required sections
   with empty placeholders; commits as `draft: true` so strict citation
   grounding does not block the migration.
5. Same for synthesis pages and MOCs (with appropriate per-type schema fixes).
6. Writes the slug map audit artifact under
   `.knowledge/migrations/<domain>-slug-map.yaml`.
7. Logs a summary entry to `log.md`.

NOT in scope here:
- Re-fetching original source bodies (defer to a `--refetch` flag in M10).
- Concept-vs-entity LLM classification (everything stays as concept; user
  reclassifies later via `wiki finalize` workflow + manual edits).
- NotebookLM corpus mapping (use `wiki nlm-add` to (re-)register sources).
- Filter example bank backfill from JSON checkpoints (the JSONs need a
  scored variant; will land in a follow-up milestone).
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from gateway import citations, frontmatter as fm
from gateway import log, paths, validator, wiki_pages
from gateway import slugmap
from gateway.core import OperationResult, write_atomic
from gateway.locking import file_lock


_LEGACY_RECOVERY_NOTE = (
    "_(legacy import — body is the original summary; full source content "
    "is not re-fetched in v1)_"
)


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def migrate_vault(
    legacy_vault_path: Path,
    domain_slug: str,
    *,
    dry_run: bool = False,
) -> OperationResult:
    legacy_vault_path = Path(legacy_vault_path).expanduser().resolve()
    if not legacy_vault_path.is_dir():
        return OperationResult(
            success=False,
            errors=[f"legacy vault not found or not a directory: {legacy_vault_path}"],
        )

    slug_map = slugmap.build_slug_map(legacy_vault_path)
    if not slug_map:
        return OperationResult(
            success=False,
            errors=[f"no legacy sources detected under {legacy_vault_path}/sources"],
        )

    audit_dir = paths.knowledge_internal() / "migrations"
    citation_map = slugmap.citation_mapping(slug_map)

    if dry_run:
        audit_path = slugmap.save_slug_map(domain_slug, slug_map, audit_dir)
        type_counts = _type_counts(slug_map)
        summary = (
            f"DRY RUN: {len(slug_map)} sources mapped "
            f"({_format_counts(type_counts)}); slug map at {audit_path.relative_to(paths.knowledge_root())}"
        )
        return OperationResult(success=True, summary=summary, paths_touched=[audit_path])

    paths_touched: list[Path] = []

    with file_lock(f"migrate-{domain_slug}"):
        # Save audit slug map first so a partial run is debuggable.
        audit_path = slugmap.save_slug_map(domain_slug, slug_map, audit_dir)
        paths_touched.append(audit_path)

        # 1. Sources
        for ls in slug_map.values():
            raw_path, wiki_path = _migrate_source(ls, domain_slug)
            paths_touched.extend([raw_path, wiki_path])

        # 2. Concepts (also covers entities — user reclassifies later)
        concepts_dir = legacy_vault_path / "concepts"
        for path in sorted(concepts_dir.glob("*.md")) if concepts_dir.is_dir() else []:
            target = _migrate_concept(path, citation_map, domain_slug)
            if target is not None:
                paths_touched.append(target)

        # 3. Synthesis
        synthesis_dir = legacy_vault_path / "synthesis"
        for path in sorted(synthesis_dir.glob("*.md")) if synthesis_dir.is_dir() else []:
            target = _migrate_synthesis(path, citation_map, domain_slug)
            if target is not None:
                paths_touched.append(target)

        # 4. MOCs
        for moc_dir in (legacy_vault_path / "mocs", legacy_vault_path / "moc"):
            if moc_dir.is_dir():
                for path in sorted(moc_dir.glob("*.md")):
                    target = _migrate_moc(path, citation_map, domain_slug)
                    if target is not None:
                        paths_touched.append(target)

        log.append(
            op="migrate",
            fields={
                "domain": domain_slug,
                "vault": str(legacy_vault_path),
                "sources": len(slug_map),
            },
            summary=_format_counts(_type_counts(slug_map)),
        )

    type_counts = _type_counts(slug_map)
    return OperationResult(
        success=True,
        summary=f"migrated {legacy_vault_path.name} → {domain_slug}: {_format_counts(type_counts)}",
        paths_touched=paths_touched + [paths.log_path()],
    )


# --- helpers ---------------------------------------------------------------


def _type_counts(slug_map: dict[str, slugmap.LegacySource]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for ls in slug_map.values():
        counts[ls.source_type] = counts.get(ls.source_type, 0) + 1
    return counts


def _format_counts(counts: dict[str, int]) -> str:
    if not counts:
        return "(empty)"
    return ", ".join(f"{t}={n}" for t, n in sorted(counts.items()))


def _coerce_authors(value) -> list[str]:
    """Legacy authors come as strings, dicts {"name": ...}, or None. Normalize."""
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    out: list[str] = []
    for item in value:
        if isinstance(item, str) and item:
            out.append(item)
        elif isinstance(item, dict):
            name = item.get("name")
            if name:
                out.append(str(name))
    return out


def _legacy_meta(legacy_front: dict, source_type: str) -> dict:
    """Type-specific `meta:` block for canonical raw frontmatter."""
    meta: dict = {"source_app": "legacy-research-notebook", "legacy_recovery": "summary-only"}
    if source_type == "youtube":
        if legacy_front.get("channel"):
            meta["channel"] = legacy_front["channel"]
        if legacy_front.get("duration"):
            meta["duration"] = legacy_front["duration"]
    elif source_type == "arxiv":
        if legacy_front.get("categories"):
            meta["categories"] = legacy_front["categories"]
        if legacy_front.get("doi"):
            meta["doi"] = legacy_front["doi"]
    elif source_type == "pubmed":
        if legacy_front.get("pmid"):
            meta["pmid"] = legacy_front["pmid"]
        if legacy_front.get("journal"):
            meta["journal"] = legacy_front["journal"]
    return meta


def _legacy_relevance_to_filter(legacy_front: dict, domain_slug: str) -> dict | None:
    """Convert legacy `relevance_score: 1-5` to a canonical `filter:` block."""
    score = legacy_front.get("relevance_score")
    if score is None:
        return None
    try:
        normalized = float(score) / 5.0
    except (TypeError, ValueError):
        return None
    return {
        "score": round(normalized, 3),
        "policy_version": f"{domain_slug}-legacy-v1",
        "rationale": legacy_front.get("inclusion_rationale", "(legacy filter score)"),
        "decided_at": _now_iso(),
        "user_correction": None,
    }


def _migrate_source(ls: slugmap.LegacySource, domain_slug: str) -> tuple[Path, Path]:
    legacy_front = ls.legacy_front
    body = ls.legacy_body.lstrip("\n")
    if _LEGACY_RECOVERY_NOTE not in body:
        body = f"{_LEGACY_RECOVERY_NOTE}\n\n{body}"

    canonical_front = {
        "id": ls.canonical_id,
        "type": ls.source_type,
        "title": legacy_front.get("title", ls.canonical_id),
        "url": legacy_front.get("url", ""),
        "authors": _coerce_authors(legacy_front.get("authors")),
        "ingested_at": _now_iso(),
        "content_hash": validator.compute_content_hash(body),
        "domains": [domain_slug],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": _legacy_meta(legacy_front, ls.source_type),
        "legacy_provenance": {
            "imported_at": _now_iso(),
            "legacy_path": str(ls.legacy_path),
            "legacy_slug": ls.legacy_slug,
        },
    }
    if pub := legacy_front.get("publish_date") or legacy_front.get("published_at"):
        canonical_front["published_at"] = str(pub).split("T", 1)[0]
    filt = _legacy_relevance_to_filter(legacy_front, domain_slug)
    if filt is not None:
        canonical_front["filter"] = filt

    raw_target = paths.raw_source_path(ls.source_type, ls.canonical_id)
    raw_target.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(raw_target, fm.serialize(canonical_front, body))

    wiki_target = paths.wiki_source_path(ls.canonical_id)
    write_atomic(wiki_target, _make_wiki_source_page(canonical_front))

    return raw_target, wiki_target


def _make_wiki_source_page(front: dict) -> str:
    page_front = {
        "type": "source",
        "source_id": front["id"],
        "source_type": front["type"],
        "title": front["title"],
        "domains": front.get("domains", []),
        "ingested_at": front["ingested_at"],
        "legacy_provenance": front.get("legacy_provenance"),
    }
    if "filter" in front and isinstance(front["filter"], dict):
        page_front["filter_score"] = front["filter"].get("score")

    raw_link = f"raw/{front['type']}/{front['id']}"
    url = front.get("url", "")
    authors = ", ".join(front.get("authors", [])) or "(unknown)"
    published = front.get("published_at", "")

    header_bits = [f"[[{raw_link}]]", front["type"]]
    if url:
        header_bits.append(f"[original]({url})")
    if published:
        header_bits.append(str(published))

    body = "\n".join([
        f"# {front['title']}",
        "",
        "**Source:** " + " · ".join(header_bits),
        f"**Authors:** {authors}",
        "",
        "## Summary",
        "",
        "_(legacy migration — see raw frontmatter for the original summary text)_",
        "",
        "## Key claims",
        "",
        "_(claims not yet extracted from legacy)_",
        "",
        "## Cross-references",
        "",
        "_(no cross-references yet)_",
        "",
    ])
    return fm.serialize(page_front, body)


def _ensure_required_sections(body: str, required: tuple[str, ...]) -> str:
    """Append placeholder `## <section>` blocks for any required sections missing."""
    missing = wiki_pages.missing_sections(body, required)
    if not missing:
        return body
    suffix = "\n\n" + "\n\n".join(
        f"## {s}\n\n_(needs population from legacy import)_" for s in missing
    ) + "\n"
    return body.rstrip() + suffix


def _migrate_concept(path: Path, citation_map: dict[str, str], domain_slug: str) -> Path | None:
    try:
        legacy_front, body = fm.parse(path.read_text())
    except fm.FrontmatterError:
        return None

    body = citations.rewrite_wikilinks(body, citation_map)
    schema = wiki_pages.PAGE_SCHEMAS["concept"]
    body = _ensure_required_sections(body, schema.required_sections)

    canonical_front = {
        "type": "concept",
        "slug": path.stem,
        "canonical_name": legacy_front.get("title") or path.stem.replace("-", " ").title(),
        "domains": [domain_slug],
        "draft": True,
        "draft_started_at": _now_iso(),
        "legacy_provenance": {
            "imported_at": _now_iso(),
            "legacy_path": str(path),
            "legacy_slug": path.stem,
            "legacy_concept_type": legacy_front.get("concept_type"),
        },
    }
    if tags := legacy_front.get("tags"):
        canonical_front["tags"] = tags

    target = paths.wiki_dir() / "concepts" / f"{path.stem}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(target, fm.serialize(canonical_front, body))
    return target


def _migrate_synthesis(path: Path, citation_map: dict[str, str], domain_slug: str) -> Path | None:
    try:
        legacy_front, body = fm.parse(path.read_text())
    except fm.FrontmatterError:
        return None

    body = citations.rewrite_wikilinks(body, citation_map)
    schema = wiki_pages.PAGE_SCHEMAS["synthesis"]
    body = _ensure_required_sections(body, schema.required_sections)

    canonical_front = {
        "type": "synthesis",
        "slug": path.stem,
        "title": legacy_front.get("title") or path.stem.replace("-", " ").title(),
        "domains": [domain_slug],
        "question": legacy_front.get("question") or f"(legacy synthesis: {path.stem})",
        "draft": True,
        "draft_started_at": _now_iso(),
        "legacy_provenance": {
            "imported_at": _now_iso(),
            "legacy_path": str(path),
            "legacy_slug": path.stem,
        },
    }

    target = paths.wiki_dir() / "synthesis" / f"{path.stem}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(target, fm.serialize(canonical_front, body))
    return target


def _migrate_moc(path: Path, citation_map: dict[str, str], domain_slug: str) -> Path | None:
    try:
        legacy_front, body = fm.parse(path.read_text())
    except fm.FrontmatterError:
        return None

    body = citations.rewrite_wikilinks(body, citation_map)
    schema = wiki_pages.PAGE_SCHEMAS["moc"]
    body = _ensure_required_sections(body, schema.required_sections)

    canonical_front = {
        "type": "moc",
        "slug": path.stem,
        "domain": domain_slug,
        "legacy_provenance": {
            "imported_at": _now_iso(),
            "legacy_path": str(path),
            "legacy_slug": path.stem,
        },
    }

    target = paths.wiki_dir() / "mocs" / f"{path.stem}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(target, fm.serialize(canonical_front, body))
    return target
