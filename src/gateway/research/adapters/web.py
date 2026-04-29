"""Web search adapter backed by Firecrawl's `/search` endpoint.

Firecrawl exposes a JSON HTTP API for general-web search; we use it as
the v1 web adapter because the dependency footprint is one HTTP call
(`requests` is already in the dependency tree).

The adapter is a thin wrapper: query in, normalized `CandidateItem`s
out. Auth happens at call time, not construction time, so a missing
`FIRECRAWL_API_KEY` only fails the web slice of a research run rather
than aborting the orchestrator (per `SearchAdapter` Protocol contract).
"""

from __future__ import annotations

import hashlib
import os
from typing import Any

import requests

from gateway.research.adapters.base import AdapterError, CandidateItem


FIRECRAWL_SEARCH_URL = "https://api.firecrawl.dev/v1/search"
DEFAULT_TIMEOUT_SECONDS = 30


class WebAdapter:
    """General-web search adapter using Firecrawl's `/search` endpoint."""

    name = "web"

    def __init__(self, *, api_key: str | None = None) -> None:
        # Resolve at construction for convenience but don't validate; the
        # Protocol contract requires a missing key to surface only when
        # `search()` is called so the orchestrator can downgrade to a
        # per-adapter warning instead of aborting the run.
        self._api_key = api_key if api_key is not None else os.environ.get("FIRECRAWL_API_KEY")

    def search(
        self,
        query: str,
        *,
        filter_hints: dict | None = None,  # noqa: ARG002 - reserved for future use
        max_results: int = 50,
    ) -> list[CandidateItem]:
        """Run a Firecrawl search and return normalized candidates.

        Raises
        ------
        AdapterError
            If `FIRECRAWL_API_KEY` is unset or the HTTP call fails.
        """
        # Re-read the env at call time so tests using `monkeypatch.setenv`
        # after construction still work; instance value wins if set.
        api_key = self._api_key or os.environ.get("FIRECRAWL_API_KEY")
        if not api_key:
            raise AdapterError("FIRECRAWL_API_KEY not set")

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload: dict[str, Any] = {
            "query": query,
            "limit": max_results,
        }

        try:
            response = requests.post(
                FIRECRAWL_SEARCH_URL,
                json=payload,
                headers=headers,
                timeout=DEFAULT_TIMEOUT_SECONDS,
            )
            response.raise_for_status()
        except requests.RequestException as exc:
            raise AdapterError(f"Firecrawl search HTTP error: {exc}") from exc

        try:
            body = response.json()
        except ValueError as exc:
            raise AdapterError(f"Firecrawl search returned non-JSON response: {exc}") from exc

        results = _extract_results(body)

        items: list[CandidateItem] = []
        for result in results[:max_results]:
            url = result.get("url")
            if not url:
                # Skip rows without a URL — nothing downstream can dedup
                # or fetch them.
                continue
            items.append(_to_candidate(result, url=url))
        return items


def _extract_results(body: Any) -> list[dict]:
    """Pull the result list out of a Firecrawl search response.

    Firecrawl's `/v1/search` returns `{"success": true, "data": [...]}`.
    Older / alternate shapes have surfaced `{"results": [...]}`; accept
    both so we don't break on a minor schema rev.
    """
    if not isinstance(body, dict):
        return []
    for key in ("data", "results"):
        value = body.get(key)
        if isinstance(value, list):
            return [row for row in value if isinstance(row, dict)]
    return []


def _to_candidate(result: dict, *, url: str) -> CandidateItem:
    """Normalize one Firecrawl search row into a `CandidateItem`."""
    item_id = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
    title = (result.get("title") or "").strip()
    description = (
        result.get("description")
        or result.get("snippet")
        or ""
    )
    publish_date = result.get("published_date") or result.get("publishedDate") or None

    return CandidateItem(
        item_id=item_id,
        source_type="web",
        url=url,
        title=title,
        authors=[],
        publish_date=publish_date,
        description=description,
        content_type="web",
        source_metadata=dict(result),
    )
