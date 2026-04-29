"""Tests for the Firecrawl-backed web search adapter.

Network is fully mocked. We patch `requests.post` at the module level
where the adapter imports it (`gateway.research.adapters.web.requests`)
so the real HTTP client is never invoked during the unit run.
"""

from __future__ import annotations

import hashlib
from typing import Any

import pytest
import requests

from gateway.research.adapters.base import AdapterError, CandidateItem
from gateway.research.adapters.web import WebAdapter


# --- helpers ---------------------------------------------------------------


class _FakeResponse:
    """Minimal stand-in for `requests.Response` covering what the adapter uses."""

    def __init__(
        self,
        *,
        json_payload: Any | None = None,
        status_code: int = 200,
        raise_exc: Exception | None = None,
        json_exc: Exception | None = None,
    ) -> None:
        self._json_payload = json_payload
        self.status_code = status_code
        self._raise_exc = raise_exc
        self._json_exc = json_exc

    def raise_for_status(self) -> None:
        if self._raise_exc is not None:
            raise self._raise_exc

    def json(self) -> Any:
        if self._json_exc is not None:
            raise self._json_exc
        return self._json_payload


def _canned_response(num_results: int = 3) -> dict:
    """Build a Firecrawl-shaped /search response with N rows."""
    return {
        "success": True,
        "data": [
            {
                "url": f"https://example.com/article-{i}",
                "title": f"Article {i}",
                "description": f"Snippet for article {i}",
                "published_date": "2026-01-15",
                "markdown": f"# Article {i}\n\nbody",
                "metadata": {"sourceURL": f"https://example.com/article-{i}"},
            }
            for i in range(num_results)
        ],
    }


# --- tests -----------------------------------------------------------------


def test_search_parses_firecrawl_results_into_candidate_items(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A canned Firecrawl response is parsed into CandidateItems with all fields."""
    monkeypatch.setenv("FIRECRAWL_API_KEY", "test-key")

    captured: dict[str, Any] = {}

    def fake_post(url: str, *, json: dict, headers: dict, timeout: int) -> _FakeResponse:
        captured["url"] = url
        captured["json"] = json
        captured["headers"] = headers
        captured["timeout"] = timeout
        return _FakeResponse(json_payload=_canned_response(3))

    monkeypatch.setattr(
        "gateway.research.adapters.web.requests.post",
        fake_post,
    )

    adapter = WebAdapter()
    items = adapter.search("semaglutide food noise", max_results=10)

    # HTTP call shape
    assert captured["url"] == "https://api.firecrawl.dev/v1/search"
    assert captured["headers"]["Authorization"] == "Bearer test-key"
    assert captured["headers"]["Content-Type"] == "application/json"
    assert captured["json"] == {"query": "semaglutide food noise", "limit": 10}

    # Parsed shape
    assert len(items) == 3
    first = items[0]
    assert isinstance(first, CandidateItem)
    expected_url = "https://example.com/article-0"
    assert first.url == expected_url
    assert first.source_type == "web"
    assert first.content_type == "web"
    assert first.title == "Article 0"
    assert first.description == "Snippet for article 0"
    assert first.publish_date == "2026-01-15"
    assert first.authors == []
    expected_id = hashlib.sha1(expected_url.encode("utf-8")).hexdigest()[:12]
    assert first.item_id == expected_id
    # Full Firecrawl row is preserved for downstream consumers
    assert first.source_metadata["markdown"] == "# Article 0\n\nbody"
    assert first.source_metadata["metadata"]["sourceURL"] == expected_url


def test_search_falls_back_to_snippet_when_description_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """When `description` is absent the adapter uses `snippet`."""
    monkeypatch.setenv("FIRECRAWL_API_KEY", "test-key")

    payload = {
        "success": True,
        "data": [
            {
                "url": "https://example.com/x",
                "title": "X",
                "snippet": "fallback snippet text",
            }
        ],
    }
    monkeypatch.setattr(
        "gateway.research.adapters.web.requests.post",
        lambda *a, **kw: _FakeResponse(json_payload=payload),
    )

    items = WebAdapter().search("anything")
    assert items[0].description == "fallback snippet text"
    assert items[0].publish_date is None


def test_search_respects_max_results(monkeypatch: pytest.MonkeyPatch) -> None:
    """Even if Firecrawl returns more rows than requested, we cap at max_results."""
    monkeypatch.setenv("FIRECRAWL_API_KEY", "test-key")

    # Server returns 10, caller asked for 4.
    monkeypatch.setattr(
        "gateway.research.adapters.web.requests.post",
        lambda *a, **kw: _FakeResponse(json_payload=_canned_response(10)),
    )

    items = WebAdapter().search("query", max_results=4)
    assert len(items) == 4
    # First four URLs are preserved in order.
    assert [it.url for it in items] == [
        f"https://example.com/article-{i}" for i in range(4)
    ]


def test_search_skips_rows_without_url(monkeypatch: pytest.MonkeyPatch) -> None:
    """Firecrawl rows missing a URL are dropped — they can't be deduped or fetched."""
    monkeypatch.setenv("FIRECRAWL_API_KEY", "test-key")

    payload = {
        "success": True,
        "data": [
            {"title": "no url here"},
            {"url": "https://example.com/ok", "title": "ok"},
        ],
    }
    monkeypatch.setattr(
        "gateway.research.adapters.web.requests.post",
        lambda *a, **kw: _FakeResponse(json_payload=payload),
    )

    items = WebAdapter().search("q")
    assert len(items) == 1
    assert items[0].url == "https://example.com/ok"


def test_search_raises_adapter_error_on_http_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """An HTTP error inside the requests call is wrapped as AdapterError."""
    monkeypatch.setenv("FIRECRAWL_API_KEY", "test-key")

    boom = requests.HTTPError("500 Server Error")

    def fake_post(*a: Any, **kw: Any) -> _FakeResponse:
        return _FakeResponse(raise_exc=boom)

    monkeypatch.setattr("gateway.research.adapters.web.requests.post", fake_post)

    adapter = WebAdapter()
    with pytest.raises(AdapterError, match="Firecrawl search HTTP error"):
        adapter.search("anything")


def test_search_raises_adapter_error_on_request_exception(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Connection-level failures (timeouts, DNS) are wrapped as AdapterError."""
    monkeypatch.setenv("FIRECRAWL_API_KEY", "test-key")

    def fake_post(*a: Any, **kw: Any) -> _FakeResponse:
        raise requests.ConnectionError("dns blew up")

    monkeypatch.setattr("gateway.research.adapters.web.requests.post", fake_post)

    with pytest.raises(AdapterError, match="Firecrawl search HTTP error"):
        WebAdapter().search("q")


def test_search_raises_adapter_error_when_api_key_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Missing FIRECRAWL_API_KEY raises AdapterError at search() time, not __init__."""
    monkeypatch.delenv("FIRECRAWL_API_KEY", raising=False)

    # Construction must succeed even with no key (orchestrator contract).
    adapter = WebAdapter()
    assert adapter.name == "web"

    with pytest.raises(AdapterError, match="FIRECRAWL_API_KEY not set"):
        adapter.search("q")


def test_explicit_api_key_overrides_missing_env(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """An explicit api_key kwarg works even with no env var set."""
    monkeypatch.delenv("FIRECRAWL_API_KEY", raising=False)

    captured: dict[str, Any] = {}

    def fake_post(url: str, *, json: dict, headers: dict, timeout: int) -> _FakeResponse:
        captured["headers"] = headers
        return _FakeResponse(json_payload={"data": []})

    monkeypatch.setattr("gateway.research.adapters.web.requests.post", fake_post)

    adapter = WebAdapter(api_key="explicit-key")
    items = adapter.search("q")
    assert items == []
    assert captured["headers"]["Authorization"] == "Bearer explicit-key"
