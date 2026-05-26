"""Notion API client — thin urllib.request wrapper for wiki publish-notion.

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
