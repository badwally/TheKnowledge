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


# --- 429 backoff tests (M46-followup Fix A) ------------------------------


class _Recording429Response:
    def __init__(self, status_code, payload=None, headers=None):
        self.status_code = status_code
        self._payload = payload or {}
        self.text = "" if status_code == 200 else "rate limited"
        self.headers = headers or {}

    def json(self):
        return self._payload


def test_search_videos_retries_on_429_then_succeeds(monkeypatch):
    monkeypatch.setenv("YOUTUBE_API_KEY", "fake-key")
    calls: list[int] = []
    sleeps: list[float] = []

    def fake_get(url, params=None, timeout=None):
        calls.append(1)
        if len(calls) == 1:
            return _Recording429Response(429)
        return _Recording429Response(200, payload=_SEARCH_RESPONSE)

    monkeypatch.setattr(yt_mod.requests, "get", fake_get)
    monkeypatch.setattr(yt_mod.time, "sleep", lambda s: sleeps.append(s))

    items = yt_mod._search_videos("fake-key", "anything", max_results=10)

    assert items  # got search items back
    assert len(calls) == 2
    assert sleeps and sleeps[0] > 0


def test_search_videos_honors_retry_after_header(monkeypatch):
    monkeypatch.setenv("YOUTUBE_API_KEY", "fake-key")
    sleeps: list[float] = []
    calls: list[int] = []

    def fake_get(url, params=None, timeout=None):
        calls.append(1)
        if len(calls) == 1:
            return _Recording429Response(429, headers={"Retry-After": "5"})
        return _Recording429Response(200, payload=_SEARCH_RESPONSE)

    monkeypatch.setattr(yt_mod.requests, "get", fake_get)
    monkeypatch.setattr(yt_mod.time, "sleep", lambda s: sleeps.append(s))

    yt_mod._search_videos("fake-key", "q", max_results=10)

    assert sleeps and sleeps[0] >= 5.0


def test_search_videos_raises_after_429_retries_exhausted(monkeypatch):
    monkeypatch.setenv("YOUTUBE_API_KEY", "fake-key")
    sleeps: list[float] = []

    def fake_get(url, params=None, timeout=None):
        return _Recording429Response(429)

    monkeypatch.setattr(yt_mod.requests, "get", fake_get)
    monkeypatch.setattr(yt_mod.time, "sleep", lambda s: sleeps.append(s))

    with pytest.raises(AdapterError) as excinfo:
        yt_mod._search_videos("fake-key", "q", max_results=10)
    assert "429" in str(excinfo.value)
    assert len(sleeps) >= 1


def test_get_video_details_retries_on_429_then_succeeds(monkeypatch):
    sleeps: list[float] = []
    calls: list[int] = []

    def fake_get(url, params=None, timeout=None):
        calls.append(1)
        if len(calls) == 1:
            return _Recording429Response(429)
        return _Recording429Response(200, payload=_VIDEOS_RESPONSE)

    monkeypatch.setattr(yt_mod.requests, "get", fake_get)
    monkeypatch.setattr(yt_mod.time, "sleep", lambda s: sleeps.append(s))

    details = yt_mod._get_video_details("fake-key", ["abc123XYZ__"])

    assert details
    assert len(calls) == 2
    assert sleeps and sleeps[0] > 0


# --- inter-query throttle ----------------------------------------------------


def test_search_no_sleep_on_first_call(monkeypatch):
    """First search() call on a fresh adapter must not sleep."""
    monkeypatch.setenv("YOUTUBE_API_KEY", "fake-key")
    _install_fake_requests(monkeypatch)
    sleeps: list[float] = []
    monkeypatch.setattr(yt_mod.time, "sleep", lambda s: sleeps.append(s))

    adapter = yt_mod.YouTubeAdapter()
    adapter.search("test query", max_results=1)

    assert sleeps == [], f"unexpected sleep on first call: {sleeps}"


def test_search_sleeps_between_rapid_consecutive_calls(monkeypatch):
    """Rapid consecutive calls sleep the remaining inter-query gap."""
    monkeypatch.setenv("YOUTUBE_API_KEY", "fake-key")
    _install_fake_requests(monkeypatch)
    sleeps: list[float] = []
    monkeypatch.setattr(yt_mod.time, "sleep", lambda s: sleeps.append(s))

    # search() calls monotonic() twice: once for the elapsed check, once to
    # stamp _last_search_time.  Use t=100 so the first call sees a large
    # elapsed (100 - 0.0 = 100 s) and skips sleeping; then t=100 again so
    # the second call sees elapsed=0 and must sleep.
    times = iter([100.0, 100.0, 100.0, 100.0])
    monkeypatch.setattr(yt_mod.time, "monotonic", lambda: next(times))

    adapter = yt_mod.YouTubeAdapter()
    adapter.search("query one", max_results=1)   # no sleep (elapsed=100s)
    adapter.search("query two", max_results=1)   # sleep (elapsed=0s)

    assert sleeps, "expected sleep on second rapid call"
    assert sleeps[-1] == pytest.approx(yt_mod._INTER_QUERY_SLEEP_SECONDS, abs=0.01)


def test_search_no_sleep_when_gap_already_large(monkeypatch):
    """No sleep when the caller has already waited longer than the threshold."""
    monkeypatch.setenv("YOUTUBE_API_KEY", "fake-key")
    _install_fake_requests(monkeypatch)
    sleeps: list[float] = []
    monkeypatch.setattr(yt_mod.time, "sleep", lambda s: sleeps.append(s))

    # 2 monotonic() calls per search() × 2 searches = 4 values.
    # t=100 → first call skips sleep (100-0=100 s elapsed).
    # t=110 → second call skips sleep (110-100=10 s elapsed, > threshold).
    times = iter([100.0, 100.0, 110.0, 110.0])
    monkeypatch.setattr(yt_mod.time, "monotonic", lambda: next(times))

    adapter = yt_mod.YouTubeAdapter()
    adapter.search("query one", max_results=1)
    adapter.search("query two", max_results=1)

    assert sleeps == [], f"unexpected sleep when gap > threshold: {sleeps}"
