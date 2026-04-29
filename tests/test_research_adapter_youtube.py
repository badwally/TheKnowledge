"""Tests for the YouTube search adapter (`gateway.research.adapters.youtube`).

The YouTube Data API v3 is exercised entirely through `requests.get`,
which we replace with a small fake that returns canned `search.list`
and `videos.list` payloads keyed by URL. The fake also supports an
HTTP-error mode for the failure-path test.
"""

from __future__ import annotations

import pytest
import requests

from gateway.research.adapters import youtube as yt_mod
from gateway.research.adapters.base import AdapterError, CandidateItem


_SEARCH_RESPONSE = {
    "items": [
        {
            "id": {"videoId": "abc123XYZ_-"},
            "snippet": {
                "title": "How GLP-1 changes appetite",
                "channelTitle": "Endocrine Channel",
                "channelId": "UC_endo",
                "publishedAt": "2024-04-02T12:00:00Z",
                "description": "A walkthrough of GLP-1 effects on hunger.",
            },
        },
        {
            "id": {"videoId": "def456UVW__"},
            "snippet": {
                "title": "Tirzepatide deep dive",
                "channelTitle": "Pharma Lectures",
                "channelId": "UC_pharma",
                "publishedAt": "2024-05-10T08:30:00Z",
                "description": "Mechanism + clinical data overview.",
            },
        },
        {
            "id": {"videoId": "ghi789RST__"},
            "snippet": {
                "title": "Reward circuits primer",
                "channelTitle": "Neuro 101",
                "channelId": "UC_neuro",
                "publishedAt": "2024-06-15T00:00:00Z",
                "description": "Mesolimbic anatomy 101.",
            },
        },
    ]
}

_VIDEOS_RESPONSE = {
    "items": [
        {
            "id": "abc123XYZ_-",
            "contentDetails": {"duration": "PT12M34S"},
            "statistics": {"viewCount": "12345", "likeCount": "678", "commentCount": "42"},
        },
        {
            "id": "def456UVW__",
            "contentDetails": {"duration": "PT45M00S"},
            "statistics": {"viewCount": "9001"},
        },
        {
            "id": "ghi789RST__",
            "contentDetails": {"duration": "PT5M0S"},
            "statistics": {"viewCount": "100"},
        },
    ]
}


class _FakeResponse:
    def __init__(self, payload: dict, status: int = 200):
        self._payload = payload
        self.status_code = status
        self.text = "" if status == 200 else "error body"

    def json(self):
        return self._payload


def _install_fake_requests(monkeypatch: pytest.MonkeyPatch, *, search=None, videos=None):
    """Patch `requests.get` in the youtube module to return canned data."""
    search_payload = _SEARCH_RESPONSE if search is None else search
    videos_payload = _VIDEOS_RESPONSE if videos is None else videos

    def fake_get(url, params=None, timeout=None):
        if "/search" in url:
            return _FakeResponse(search_payload)
        if "/videos" in url:
            return _FakeResponse(videos_payload)
        raise AssertionError(f"unexpected URL {url!r}")

    monkeypatch.setattr(yt_mod.requests, "get", fake_get)


def test_search_raises_when_api_key_missing(monkeypatch):
    monkeypatch.delenv("YOUTUBE_API_KEY", raising=False)
    with pytest.raises(AdapterError) as excinfo:
        yt_mod.YouTubeAdapter().search("GLP-1")
    assert "YOUTUBE_API_KEY" in str(excinfo.value)


def test_search_parses_canned_response_into_candidate_items(monkeypatch):
    monkeypatch.setenv("YOUTUBE_API_KEY", "fake-key")
    _install_fake_requests(monkeypatch)

    items = yt_mod.YouTubeAdapter().search("GLP-1 reward")

    assert len(items) == 3
    first = items[0]
    assert isinstance(first, CandidateItem)
    assert first.item_id == "yt:abc123XYZ_-"
    assert first.source_type == "youtube"
    assert first.url == "https://www.youtube.com/watch?v=abc123XYZ_-"
    assert first.title == "How GLP-1 changes appetite"
    assert first.authors == ["Endocrine Channel"]
    assert first.publish_date == "2024-04-02T12:00:00Z"
    assert first.description == "A walkthrough of GLP-1 effects on hunger."
    assert first.content_type == "video"
    meta = first.source_metadata
    assert meta["video_id"] == "abc123XYZ_-"
    assert meta["channel_id"] == "UC_endo"
    assert meta["channel_name"] == "Endocrine Channel"
    assert meta["duration"] == "PT12M34S"
    assert meta["view_count"] == 12345
    assert meta["like_count"] == 678
    assert meta["comment_count"] == 42

    # Second item: only viewCount is in statistics; like/comment fall back to None.
    second = items[1]
    assert second.item_id == "yt:def456UVW__"
    assert second.source_metadata["view_count"] == 9001
    assert second.source_metadata["like_count"] is None
    assert second.source_metadata["comment_count"] is None


def test_search_respects_max_results(monkeypatch):
    monkeypatch.setenv("YOUTUBE_API_KEY", "fake-key")
    captured: dict = {}

    def fake_get(url, params=None, timeout=None):
        if "/search" in url:
            captured["search_params"] = dict(params or {})
            return _FakeResponse(_SEARCH_RESPONSE)
        return _FakeResponse(_VIDEOS_RESPONSE)

    monkeypatch.setattr(yt_mod.requests, "get", fake_get)

    items = yt_mod.YouTubeAdapter().search("anything", max_results=2)

    # The caller's cap is enforced post-parse...
    assert len(items) == 2
    # ...and forwarded to the API as `maxResults`.
    assert captured["search_params"]["maxResults"] == 2


def test_search_returns_empty_list_when_api_returns_no_items(monkeypatch):
    monkeypatch.setenv("YOUTUBE_API_KEY", "fake-key")
    _install_fake_requests(monkeypatch, search={"items": []})

    assert yt_mod.YouTubeAdapter().search("nothing") == []


def test_search_raises_adapter_error_on_http_failure(monkeypatch):
    monkeypatch.setenv("YOUTUBE_API_KEY", "fake-key")

    def fake_get(url, params=None, timeout=None):
        return _FakeResponse({"error": {"code": 403, "message": "quota exceeded"}}, status=403)

    monkeypatch.setattr(yt_mod.requests, "get", fake_get)

    with pytest.raises(AdapterError) as excinfo:
        yt_mod.YouTubeAdapter().search("anything")
    assert "403" in str(excinfo.value)


def test_search_raises_adapter_error_on_network_exception(monkeypatch):
    monkeypatch.setenv("YOUTUBE_API_KEY", "fake-key")

    def boom(*_args, **_kwargs):
        raise requests.ConnectionError("dns failed")

    monkeypatch.setattr(yt_mod.requests, "get", boom)

    with pytest.raises(AdapterError):
        yt_mod.YouTubeAdapter().search("anything")


def test_search_forwards_filter_hints_to_search_params(monkeypatch):
    monkeypatch.setenv("YOUTUBE_API_KEY", "fake-key")
    captured: dict = {}

    def fake_get(url, params=None, timeout=None):
        if "/search" in url:
            captured["params"] = dict(params or {})
            return _FakeResponse(_SEARCH_RESPONSE)
        return _FakeResponse(_VIDEOS_RESPONSE)

    monkeypatch.setattr(yt_mod.requests, "get", fake_get)

    yt_mod.YouTubeAdapter().search(
        "GLP-1",
        filter_hints={
            "publishedAfter": "2024-01-01T00:00:00Z",
            "videoDuration": "long",
            "relevanceLanguage": "en",
            # Unknown hint should be dropped, not forwarded.
            "ignored_hint": "ignore-me",
        },
    )

    params = captured["params"]
    assert params["publishedAfter"] == "2024-01-01T00:00:00Z"
    assert params["videoDuration"] == "long"
    assert params["relevanceLanguage"] == "en"
    assert "ignored_hint" not in params
