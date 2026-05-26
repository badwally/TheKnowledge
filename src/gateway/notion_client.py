"""Notion API client — thin urllib.request wrapper for wiki gateway ops.

Used by publish-notion (INT-12, write path: wiki → Notion) and
notion-source poller (INT-18, read path: Notion → wiki).

Auth: NOTION_TOKEN env var (Notion Integration token).
      NOTION_PARENT_PAGE_ID env var (Notion page ID that hosts domain databases).

Notion API version: 2022-06-28.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any


_API_BASE = "https://api.notion.com/v1"
_API_VERSION = "2022-06-28"


class NotionError(Exception):
    """Raised on Notion API errors."""


class NotionClient:
    def __init__(self, token: str | None = None) -> None:
        self._token = token or os.environ.get("NOTION_TOKEN", "")
        if not self._token:
            raise NotionError(
                "NOTION_TOKEN environment variable not set. "
                "Create a Notion Integration and set the token."
            )

    def _request(
        self,
        method: str,
        path: str,
        body: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        url = f"{_API_BASE}{path}"
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(
            url,
            data=data,
            method=method,
            headers={
                "Authorization": f"Bearer {self._token}",
                "Notion-Version": _API_VERSION,
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            body_text = e.read().decode(errors="replace")
            raise NotionError(f"Notion API {method} {path} → {e.code}: {body_text}") from e
        except Exception as e:
            raise NotionError(f"Notion API {method} {path} → {e!r}") from e

    # --- database operations ------------------------------------------------

    def create_database(
        self, parent_page_id: str, title: str, domain: str
    ) -> dict[str, Any]:
        return self._request(
            "POST",
            "/databases",
            {
                "parent": {"type": "page_id", "page_id": parent_page_id},
                "title": [{"type": "text", "text": {"content": title}}],
                "properties": {
                    "Name": {"title": {}},
                    "Type": {"select": {"options": [
                        {"name": "entity", "color": "blue"},
                        {"name": "concept", "color": "green"},
                        {"name": "synthesis", "color": "purple"},
                        {"name": "moc", "color": "orange"},
                        {"name": "source", "color": "gray"},
                    ]}},
                    "Slug": {"rich_text": {}},
                    "Domains": {"multi_select": {"options": [{"name": domain}]}},
                    "Last Updated": {"date": {}},
                    "Wiki Path": {"rich_text": {}},
                    "Archived": {"checkbox": {}},
                },
            },
        )

    def query_database(
        self, database_id: str, filter_body: dict | None = None
    ) -> list[dict[str, Any]]:
        body: dict[str, Any] = {"page_size": 100}
        if filter_body:
            body["filter"] = filter_body
        results: list[dict] = []
        while True:
            resp = self._request("POST", f"/databases/{database_id}/query", body)
            results.extend(resp.get("results", []))
            if not resp.get("has_more"):
                break
            body["start_cursor"] = resp["next_cursor"]
        return results

    # --- page operations ----------------------------------------------------

    def create_page(
        self,
        database_id: str,
        title: str,
        page_type: str,
        slug: str,
        domains: list[str],
        last_updated: str,
        wiki_path: str,
        body_md: str = "",
    ) -> dict[str, Any]:
        children = []
        if body_md:
            # Add body as a single code block (Notion markdown import is limited)
            children.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": body_md[:2000]}}]
                },
            })
        return self._request(
            "POST",
            "/pages",
            {
                "parent": {"database_id": database_id},
                "properties": {
                    "Name": {"title": [{"type": "text", "text": {"content": title}}]},
                    "Type": {"select": {"name": page_type}},
                    "Slug": {"rich_text": [{"type": "text", "text": {"content": slug}}]},
                    "Domains": {"multi_select": [{"name": d} for d in domains]},
                    "Last Updated": {"date": {"start": last_updated[:10]}} if last_updated else {"date": None},
                    "Wiki Path": {"rich_text": [{"type": "text", "text": {"content": wiki_path}}]},
                    "Archived": {"checkbox": False},
                },
                "children": children,
            },
        )

    def update_page(
        self,
        page_id: str,
        title: str,
        last_updated: str,
        domains: list[str],
    ) -> dict[str, Any]:
        props: dict[str, Any] = {
            "Name": {"title": [{"type": "text", "text": {"content": title}}]},
            "Domains": {"multi_select": [{"name": d} for d in domains]},
        }
        if last_updated:
            props["Last Updated"] = {"date": {"start": last_updated[:10]}}
        return self._request("PATCH", f"/pages/{page_id}", {"properties": props})

    def archive_page(self, page_id: str) -> dict[str, Any]:
        return self._request(
            "PATCH",
            f"/pages/{page_id}",
            {"properties": {"Archived": {"checkbox": True}}, "archived": True},
        )

    # --- read operations (INT-18 Notion source poller) ---------------------

    def get_page(self, page_id: str) -> dict[str, Any]:
        """Fetch page metadata and properties."""
        return self._request("GET", f"/pages/{page_id}")

    def get_page_blocks(self, page_id: str) -> list[dict[str, Any]]:
        """Fetch all block children of a page (paginated)."""
        results: list[dict[str, Any]] = []
        path = f"/blocks/{page_id}/children?page_size=100"
        while True:
            resp = self._request("GET", path)
            results.extend(resp.get("results", []))
            if not resp.get("has_more"):
                break
            cursor = resp["next_cursor"]
            path = f"/blocks/{page_id}/children?page_size=100&start_cursor={cursor}"
        return results

    def search_pages(
        self, query: str = "", filter_body: dict[str, Any] | None = None
    ) -> list[dict[str, Any]]:
        """Search pages accessible to the integration."""
        body: dict[str, Any] = {"page_size": 100}
        if query:
            body["query"] = query
        if filter_body:
            body["filter"] = filter_body
        results: list[dict[str, Any]] = []
        while True:
            resp = self._request("POST", "/search", body)
            results.extend(resp.get("results", []))
            if not resp.get("has_more"):
                break
            body["start_cursor"] = resp["next_cursor"]
        return results

    # --- content conversion ------------------------------------------------

    @staticmethod
    def blocks_to_markdown(blocks: list[dict[str, Any]]) -> str:
        """Convert a Notion block list to a markdown string.

        Supports: paragraph, heading_1/2/3, bulleted/numbered list,
        to_do, code, quote, callout, divider, image, bookmark.
        Unsupported block types are silently skipped.
        """
        lines: list[str] = []
        for block in blocks:
            btype = block.get("type", "")
            content = block.get(btype, {})
            text = NotionClient._rich_text_to_md(content.get("rich_text", []))

            if btype == "paragraph":
                lines.append(text)
            elif btype in ("heading_1", "heading_2", "heading_3"):
                level = int(btype[-1])
                lines.append(f"{'#' * level} {text}")
            elif btype == "bulleted_list_item":
                lines.append(f"- {text}")
            elif btype == "numbered_list_item":
                lines.append(f"1. {text}")
            elif btype == "to_do":
                checked = content.get("checked", False)
                lines.append(f"- [{'x' if checked else ' '}] {text}")
            elif btype == "code":
                lang = content.get("language", "")
                lines.append(f"```{lang}\n{text}\n```")
            elif btype in ("quote", "callout"):
                lines.append(f"> {text}")
            elif btype == "divider":
                lines.append("---")
            elif btype == "image":
                url = (
                    content.get("external", {}).get("url")
                    or content.get("file", {}).get("url", "")
                )
                caption = NotionClient._rich_text_to_md(content.get("caption", []))
                lines.append(f"![{caption}]({url})")
            elif btype == "bookmark":
                url = content.get("url", "")
                caption = NotionClient._rich_text_to_md(content.get("caption", []))
                lines.append(f"[{caption or url}]({url})")
            else:
                continue
            lines.append("")
        return "\n".join(lines).strip()

    @staticmethod
    def _rich_text_to_md(rich_text: list[dict[str, Any]]) -> str:
        """Convert Notion rich_text array to markdown-formatted string."""
        parts: list[str] = []
        for frag in rich_text:
            text = frag.get("plain_text", "")
            ann = frag.get("annotations", {})
            href = frag.get("href")

            if ann.get("code"):
                text = f"`{text}`"
            if ann.get("bold"):
                text = f"**{text}**"
            if ann.get("italic"):
                text = f"*{text}*"
            if ann.get("strikethrough"):
                text = f"~~{text}~~"
            if href:
                text = f"[{text}]({href})"
            parts.append(text)
        return "".join(parts)
