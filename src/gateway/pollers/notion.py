"""Notion source poller (INT-18).

Reads pages and databases from a Notion workspace and writes each page
to raw/note/ as a canonical note source for the wiki ingest pipeline.

Auth:
  NOTION_TOKEN — Notion Integration token (required)

Config: .knowledge/pollers/notion/config.yaml
  pages:
    - page_id: "abc12345def..."   # Notion page ID (with or without dashes)
      domain: "research"          # optional default domain tag
      title_override: ""          # optional; uses Notion title if absent
  databases:
    - database_id: "xyz789..."    # Notion database ID
      domain: "research"
  max_pages: 50                   # per-run limit across all sources (default 50)

Cursor: .knowledge/pollers/notion/cursor.yaml
  pages:
    <page_id>: <ISO-8601 last_edited_time>
  databases:
    <database_id>: <ISO-8601 last run timestamp>

Slug format: note-notion-<sha256(page_id)[:12]> — matches WIKI.md § 6.1.
"""

from __future__ import annotations

import hashlib
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from gateway import frontmatter as fm, paths, validator
from gateway.notion_client import NotionClient, NotionError
from gateway.pollers.base import Poller, PollerResult


_DEFAULT_MAX = 50


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _page_id_clean(page_id: str) -> str:
    """Remove dashes from Notion page ID."""
    return page_id.replace("-", "")


def _build_note_id(page_id: str) -> str:
    clean = _page_id_clean(page_id)
    digest = hashlib.sha256(clean.encode()).hexdigest()[:12]
    return f"note-notion-{digest}"


def _extract_title(page: dict[str, Any]) -> str:
    """Extract the plaintext title from a Notion page object."""
    props = page.get("properties", {})
    for prop_data in props.values():
        if prop_data.get("type") == "title":
            rt = prop_data.get("title", [])
            return "".join(frag.get("plain_text", "") for frag in rt)
    return "Untitled"


def _page_edited_time(page: dict[str, Any]) -> str:
    return page.get("last_edited_time", "")


def _is_newer(current: str, cursor: str) -> bool:
    """Return True if current ISO timestamp is newer than cursor."""
    if not cursor:
        return True
    return current > cursor


class NotionSourcePoller(Poller):
    """Fetches Notion pages and databases into raw/note/ for wiki ingest."""

    name = "notion"
    source_type = "note"

    def _config_path(self) -> Path:
        return paths.knowledge_internal() / "pollers" / "notion" / "config.yaml"

    def _load_config(self) -> dict[str, Any]:
        p = self._config_path()
        if not p.exists():
            return {"pages": [], "databases": [], "max_pages": _DEFAULT_MAX}
        data = yaml.safe_load(p.read_text()) or {}
        data.setdefault("pages", [])
        data.setdefault("databases", [])
        data.setdefault("max_pages", _DEFAULT_MAX)
        return data

    def run(self, *, client: NotionClient | None = None) -> PollerResult:
        token = os.environ.get("NOTION_TOKEN", "")
        if not token and client is None:
            return PollerResult(
                success=False,
                errors=["NOTION_TOKEN environment variable not set"],
                summary="skipped: no NOTION_TOKEN",
            )

        config = self._load_config()
        max_pages: int = int(config.get("max_pages", _DEFAULT_MAX))
        cursor = self.read_cursor()
        pages_cursor: dict[str, str] = cursor.get("pages", {})
        db_cursor: dict[str, str] = cursor.get("databases", {})

        try:
            nc = client or NotionClient(token)
        except NotionError as e:
            return PollerResult(success=False, errors=[str(e)], summary=str(e))

        fetched = 0
        skipped = 0
        errors: list[str] = []
        run_at = _now_iso()

        # --- individual pages -----------------------------------------------
        for entry in config.get("pages", []):
            if fetched >= max_pages:
                break
            page_id = _page_id_clean(str(entry.get("page_id", "")))
            if not page_id:
                errors.append("config: missing page_id in pages entry")
                continue
            domain = str(entry.get("domain", ""))
            title_override = str(entry.get("title_override", ""))

            try:
                page = nc.get_page(page_id)
            except NotionError as e:
                errors.append(f"get_page({page_id}): {e}")
                continue

            edited = _page_edited_time(page)
            if not _is_newer(edited, pages_cursor.get(page_id, "")):
                skipped += 1
                continue

            try:
                blocks = nc.get_page_blocks(page_id)
            except NotionError as e:
                errors.append(f"get_page_blocks({page_id}): {e}")
                continue

            title = title_override or _extract_title(page)
            body_md = NotionClient.blocks_to_markdown(blocks)
            note_id = _build_note_id(page_id)
            url = page.get("url", "")

            canonical = _render_raw(
                note_id=note_id,
                title=title,
                url=url,
                source_app="notion",
                domain=domain,
                edited_at=edited or run_at,
                body_md=body_md,
            )
            self.write_raw(note_id, canonical)
            pages_cursor[page_id] = edited or run_at
            fetched += 1

        # --- database pages -------------------------------------------------
        for entry in config.get("databases", []):
            if fetched >= max_pages:
                break
            db_id = _page_id_clean(str(entry.get("database_id", "")))
            if not db_id:
                errors.append("config: missing database_id in databases entry")
                continue
            domain = str(entry.get("domain", ""))
            since = db_cursor.get(db_id, "")

            try:
                filter_body = (
                    {
                        "timestamp": "last_edited_time",
                        "last_edited_time": {"after": since},
                    }
                    if since
                    else None
                )
                db_pages = nc.query_database(db_id, filter_body)
            except NotionError as e:
                errors.append(f"query_database({db_id}): {e}")
                continue

            for page in db_pages:
                if fetched >= max_pages:
                    break
                page_id = _page_id_clean(page.get("id", ""))
                if not page_id:
                    continue

                try:
                    blocks = nc.get_page_blocks(page_id)
                except NotionError as e:
                    errors.append(f"get_page_blocks({page_id}): {e}")
                    continue

                title = _extract_title(page)
                body_md = NotionClient.blocks_to_markdown(blocks)
                edited = _page_edited_time(page)
                note_id = _build_note_id(page_id)
                url = page.get("url", "")

                canonical = _render_raw(
                    note_id=note_id,
                    title=title,
                    url=url,
                    source_app="notion",
                    domain=domain,
                    edited_at=edited or run_at,
                    body_md=body_md,
                )
                self.write_raw(note_id, canonical)
                fetched += 1

            db_cursor[db_id] = run_at

        self.write_cursor({"pages": pages_cursor, "databases": db_cursor})

        n_err = len(errors)
        summary = f"fetched {fetched}, skipped {skipped}" + (
            f", {n_err} error(s)" if errors else ""
        )
        return PollerResult(
            success=n_err == 0 or fetched > 0,
            fetched=fetched,
            skipped=skipped,
            errors=errors,
            summary=summary,
        )


def _render_raw(
    *,
    note_id: str,
    title: str,
    url: str,
    source_app: str,
    domain: str,
    edited_at: str,
    body_md: str,
) -> str:
    ingested_at = _now_iso()
    date_str = edited_at[:10] if edited_at else ingested_at[:10]

    meta: dict[str, Any] = {
        "id": note_id,
        "title": title,
        "type": "note",
        "source_app": source_app,
        "content_hash": validator.compute_content_hash(body_md),
        "ingested_at": ingested_at,
        "date": date_str,
    }
    if url:
        meta["url"] = url
    if domain:
        meta["domains"] = [domain]

    return fm.serialize(meta, body_md)
