"""INT-12: wiki → Notion read-only mirror.

`wiki publish-notion <domain>` upserts wiki pages for a domain into a
Notion database. Idempotent: re-running converges to current state.
Archived rows are written for wiki pages that no longer exist.

DB layout: one database per domain (rationale: domain isolation, per-domain
views, aligns with wiki policy boundaries — documented in M67.md).

Registry: .knowledge/notion/<domain>.json maps wiki_path → notion_page_id.

Auth: NOTION_TOKEN (Notion Integration token, required).
      NOTION_PARENT_PAGE_ID (Notion page that hosts domain databases, required).

Page types synced by default: entities, concepts, synthesis, mocs.
Optional with --include: sources, artifacts.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from gateway import frontmatter as fm, log, paths
from gateway.core import OperationResult, write_atomic


_DEFAULT_PAGE_TYPES = ("entity", "concept", "synthesis", "moc")
_OPTIONAL_PAGE_TYPES = ("source", "artifact")


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _registry_path(domain: str) -> Path:
    return paths.knowledge_internal() / "notion" / f"{domain}.json"


def _load_registry(domain: str) -> dict[str, str]:
    p = _registry_path(domain)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def _save_registry(domain: str, registry: dict[str, str]) -> None:
    p = _registry_path(domain)
    p.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(p, json.dumps(registry, indent=2, sort_keys=True))


def _type_dir(page_type: str) -> Path:
    return paths.wiki_dir() / f"{page_type}s"


def _collect_pages(
    domain: str,
    *,
    include_sources: bool = False,
    include_artifacts: bool = False,
) -> list[dict[str, Any]]:
    """Gather wiki pages for this domain, returning page metadata dicts."""
    type_dirs = list(_DEFAULT_PAGE_TYPES)
    if include_sources:
        type_dirs.append("source")
    if include_artifacts:
        type_dirs.append("artifact")

    pages = []
    for page_type in type_dirs:
        type_dir = paths.wiki_dir() / f"{page_type}s"
        if not type_dir.exists():
            continue
        for p in sorted(type_dir.rglob("*.md")):
            try:
                front, body = fm.parse(p.read_text())
            except Exception:
                continue
            page_domains = list(front.get("domains") or [])
            if front.get("domain"):
                page_domains.append(str(front["domain"]))
            if domain not in page_domains:
                continue
            title = str(
                front.get("title")
                or front.get("name")
                or front.get("slug")
                or p.stem
            )
            last_updated = str(
                front.get("last_updated")
                or front.get("created_at")
                or ""
            )
            wiki_path = str(p.relative_to(paths.wiki_dir()))
            pages.append({
                "wiki_path": wiki_path,
                "title": title,
                "type": page_type,
                "slug": str(front.get("slug") or p.stem),
                "domains": page_domains,
                "last_updated": last_updated,
                "body_excerpt": body[:500],
            })
    return pages


def publish_notion(
    domain: str,
    *,
    include_sources: bool = False,
    include_artifacts: bool = False,
    client=None,  # NotionClient | None — injected for testing
) -> OperationResult:
    """Upsert wiki pages for domain into a Notion database. Idempotent."""
    if client is None:
        try:
            from gateway.notion_client import NotionClient, NotionError
            client = NotionClient()
        except Exception as e:
            return OperationResult(
                success=False,
                errors=[str(e)],
                summary=f"publish-notion: auth failed — {e}",
            )

    parent_page_id = os.environ.get("NOTION_PARENT_PAGE_ID", "")
    if not parent_page_id:
        return OperationResult(
            success=False,
            errors=["NOTION_PARENT_PAGE_ID environment variable not set"],
            summary="publish-notion: missing NOTION_PARENT_PAGE_ID",
        )

    registry = _load_registry(domain)
    pages = _collect_pages(
        domain,
        include_sources=include_sources,
        include_artifacts=include_artifacts,
    )

    if not pages:
        return OperationResult(
            success=True,
            summary=f"publish-notion: no pages found for domain {domain!r}",
        )

    # Resolve or create the domain database
    db_id = registry.get("__database_id__")
    if not db_id:
        try:
            db = client.create_database(
                parent_page_id,
                title=f"Wiki — {domain}",
                domain=domain,
            )
            db_id = db["id"]
            registry["__database_id__"] = db_id
        except Exception as e:
            return OperationResult(
                success=False,
                errors=[f"create database: {e!r}"],
                summary=f"publish-notion: failed to create database for {domain}",
            )

    # Track which wiki paths we saw this run (for archive detection)
    seen_paths: set[str] = set()
    created = 0
    updated = 0
    errors: list[str] = []

    for page in pages:
        wiki_path = page["wiki_path"]
        seen_paths.add(wiki_path)
        notion_id = registry.get(wiki_path)

        try:
            if notion_id:
                client.update_page(
                    notion_id,
                    title=page["title"],
                    last_updated=page["last_updated"],
                    domains=page["domains"],
                )
                updated += 1
            else:
                result = client.create_page(
                    db_id,
                    title=page["title"],
                    page_type=page["type"],
                    slug=page["slug"],
                    domains=page["domains"],
                    last_updated=page["last_updated"],
                    wiki_path=wiki_path,
                    body_md=page["body_excerpt"],
                )
                registry[wiki_path] = result["id"]
                created += 1
        except Exception as e:
            errors.append(f"{wiki_path}: {e!r}")

    # Archive pages that were in the registry but are no longer in wiki
    archived = 0
    for wiki_path, notion_id in list(registry.items()):
        if wiki_path.startswith("__"):
            continue
        if wiki_path not in seen_paths:
            try:
                client.archive_page(notion_id)
                archived += 1
            except Exception as e:
                errors.append(f"archive {wiki_path}: {e!r}")

    _save_registry(domain, registry)

    log.append(
        op="publish-notion",
        fields={
            "domain": domain,
            "created": created,
            "updated": updated,
            "archived": archived,
            "errors": len(errors),
        },
        summary=f"notion mirror: {domain} created={created} updated={updated} archived={archived}",
    )

    return OperationResult(
        success=len(errors) == 0,
        errors=errors,
        paths_touched=[_registry_path(domain), paths.log_path()],
        summary=(
            f"publish-notion {domain}: {created} created, {updated} updated, "
            f"{archived} archived, {len(errors)} errors"
        ),
    )
