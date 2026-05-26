"""Readwise v3 poller (INT-9).

Fetches documents + highlights from the Readwise v3 Export API and writes one
canonical note file per document to raw/note/.

Auth: READWISE_TOKEN env var.
Cursor: .knowledge/pollers/readwise/cursor.yaml → last_updated_after (ISO-8601).
Pagination: follows `next` URL until null.
"""

from __future__ import annotations

import os
from datetime import datetime, timezone

import requests

from gateway import frontmatter as fm
from gateway import paths, validator
from gateway.pollers.base import Poller, PollerResult


_INITIAL_CURSOR = "2020-01-01T00:00:00Z"
_API_URL = "https://readwise.io/api/v3/list/"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _build_body(doc: dict) -> str:
    """Build the markdown body from a Readwise document dict."""
    title = doc.get("title") or ""
    author = doc.get("author") or ""
    category = doc.get("category") or ""
    highlights = doc.get("highlights") or []

    lines: list[str] = [title, ""]
    if author:
        lines += [f"Author: {author}", ""]
    if category:
        lines += [f"Category: {category}", ""]

    lines += ["## Highlights", ""]
    for h in highlights:
        text = (h.get("text") or "").strip()
        note = (h.get("note") or "").strip()
        if note:
            lines.append(f"- {text} _(note: {note})_")
        else:
            lines.append(f"- {text}")
    lines.append("")
    return "\n".join(lines)


def _fetch_all_documents(token: str, updated_after: str) -> list[dict]:
    """Fetch all pages from the Readwise v3 API and return combined results."""
    results: list[dict] = []
    url: str | None = _API_URL
    params: dict = {"updatedAfter": updated_after}
    headers = {"Authorization": f"Token {token}"}

    while url:
        resp = requests.get(url, headers=headers, params=params if url == _API_URL else {})
        resp.raise_for_status()
        data = resp.json()
        results.extend(data.get("results") or [])
        url = data.get("next") or None

    return results


class ReadwisePoller(Poller):
    """Poll Readwise v3 API and write one raw/note/ file per document."""

    name = "readwise"
    source_type = "note"

    def run(self) -> PollerResult:
        token = os.environ.get("READWISE_TOKEN", "")
        if not token:
            return PollerResult(
                success=False,
                errors=["READWISE_TOKEN env var is not set; cannot poll Readwise"],
            )

        cursor = self.read_cursor()
        updated_after = cursor.get("last_updated_after", _INITIAL_CURSOR)

        try:
            documents = _fetch_all_documents(token, updated_after)
        except Exception as e:
            return PollerResult(success=False, errors=[f"Readwise API fetch failed: {e}"])

        if not documents:
            if not cursor.get("last_updated_after"):
                self.write_cursor({"last_updated_after": _INITIAL_CURSOR})
            return PollerResult(
                success=True,
                fetched=0,
                summary="readwise: fetched=0 (no new documents)",
            )

        fetched = 0
        max_updated = updated_after

        for doc in documents:
            readwise_id = str(doc.get("id") or "")
            if not readwise_id:
                continue

            slug = f"note-readwise-{readwise_id}"
            body = _build_body(doc)
            content_hash = validator.compute_content_hash(body)

            # Check if the file exists and hash matches (idempotent update)
            existing_path = paths.raw_source_path("note", slug)
            if existing_path.exists():
                existing_text = existing_path.read_text()
                try:
                    existing_front, _ = fm.parse(existing_text)
                    if existing_front.get("content_hash") == content_hash:
                        continue  # highlights unchanged — skip
                except Exception:
                    pass

            source_url = doc.get("source_url") or ""
            highlights = doc.get("highlights") or []
            first_highlighted_at = highlights[0].get("highlighted_at", "") if highlights else ""
            last_highlighted_at = max(
                (h.get("highlighted_at") or "" for h in highlights), default=""
            )

            front: dict = {
                "id": slug,
                "type": "note",
                "title": doc.get("title") or readwise_id,
                "url": source_url,
                "authors": [doc.get("author")] if doc.get("author") else [],
                "published_at": first_highlighted_at,
                "ingested_at": _now_iso(),
                "content_hash": content_hash,
                "domains": [],
                "nlm_corpus_ids": [],
                "wiki_pages": [],
                "meta": {
                    "source_app": "readwise",
                    "readwise_id": readwise_id,
                    "readwise_category": doc.get("category") or "",
                    "source_url": source_url,
                    "highlighted_at": last_highlighted_at,
                },
            }
            self.write_raw(slug, fm.serialize(front, body))
            fetched += 1

            doc_updated = str(doc.get("updated") or "")
            if doc_updated > max_updated:
                max_updated = doc_updated

        self.write_cursor({"last_updated_after": max_updated})
        return PollerResult(
            success=True,
            fetched=fetched,
            summary=f"readwise: fetched={fetched}",
        )
