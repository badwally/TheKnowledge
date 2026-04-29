"""YouTube search adapter for `wiki research`.

Uses the YouTube Data API v3 REST endpoints directly via `requests`
(rather than the `google-api-python-client` SDK the research-notebook
port used) to avoid pulling a new dependency. Two endpoints are
called per `search()` invocation:

- `search.list` — returns matching videos (snippet only).
- `videos.list` — batched details (contentDetails + statistics) for
  every returned video ID.

`YOUTUBE_API_KEY` is read from the environment lazily; missing-key
errors surface only when `search()` runs, so the adapter can sit in
the registry without crashing the orchestrator at import time.
Caption-availability checks are intentionally skipped (50 quota units
per call); per-video transcript material is fetched downstream by
`gateway.converters.youtube` when an item passes the filter.
"""

from __future__ import annotations

import os

import requests

from gateway.research.adapters.base import (
    AdapterError,
    CandidateItem,
    SearchAdapter,
)


YOUTUBE_API_BASE = "https://www.googleapis.com/youtube/v3"


def _get_api_key() -> str:
    """Return the API key or raise `AdapterError` if it is missing."""
    api_key = os.environ.get("YOUTUBE_API_KEY")
    if not api_key:
        raise AdapterError("YOUTUBE_API_KEY not set")
    return api_key


def _search_videos(
    api_key: str,
    query: str,
    *,
    max_results: int,
    extra_params: dict | None = None,
) -> list[dict]:
    """Call `search.list` and return the raw `items` list."""
    params: dict = {
        "key": api_key,
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": min(max_results, 50),
    }
    if extra_params:
        params.update(extra_params)

    try:
        response = requests.get(f"{YOUTUBE_API_BASE}/search", params=params, timeout=30)
    except requests.RequestException as exc:
        raise AdapterError(f"youtube search request failed: {exc}") from exc
    if response.status_code != 200:
        raise AdapterError(
            f"youtube search returned HTTP {response.status_code}: {response.text[:200]}"
        )
    try:
        payload = response.json()
    except ValueError as exc:
        raise AdapterError(f"youtube search returned non-JSON: {exc}") from exc
    return payload.get("items", [])


def _get_video_details(api_key: str, video_ids: list[str]) -> dict[str, dict]:
    """Call `videos.list` and return a dict keyed by video ID."""
    if not video_ids:
        return {}
    params = {
        "key": api_key,
        "part": "contentDetails,statistics",
        # YouTube's videos.list takes up to 50 IDs per call.
        "id": ",".join(video_ids[:50]),
    }
    try:
        response = requests.get(f"{YOUTUBE_API_BASE}/videos", params=params, timeout=30)
    except requests.RequestException as exc:
        raise AdapterError(f"youtube videos.list request failed: {exc}") from exc
    if response.status_code != 200:
        raise AdapterError(
            f"youtube videos.list returned HTTP {response.status_code}: {response.text[:200]}"
        )
    try:
        payload = response.json()
    except ValueError as exc:
        raise AdapterError(f"youtube videos.list returned non-JSON: {exc}") from exc
    return {item["id"]: item for item in payload.get("items", []) if "id" in item}


def _truncate(text: str, max_length: int = 500) -> str:
    if not text:
        return ""
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."


def _to_candidate(search_item: dict, details: dict | None) -> CandidateItem | None:
    """Map (search-item, details) to a `CandidateItem`.

    Returns None when the search item is missing the video ID (defensive
    against API shape drift).
    """
    id_field = search_item.get("id") or {}
    video_id = id_field.get("videoId") if isinstance(id_field, dict) else None
    if not video_id:
        return None

    snippet = search_item.get("snippet") or {}
    details = details or {}
    content_details = details.get("contentDetails", {}) or {}
    statistics = details.get("statistics", {}) or {}

    try:
        view_count = int(statistics.get("viewCount", 0))
    except (TypeError, ValueError):
        view_count = 0

    channel_title = snippet.get("channelTitle", "")
    return CandidateItem(
        item_id=f"yt:{video_id}",
        source_type="youtube",
        url=f"https://www.youtube.com/watch?v={video_id}",
        title=snippet.get("title", "") or video_id,
        authors=[channel_title] if channel_title else [],
        publish_date=snippet.get("publishedAt") or None,
        description=_truncate(snippet.get("description", ""), 500),
        content_type="video",
        source_metadata={
            "video_id": video_id,
            "channel_id": snippet.get("channelId", ""),
            "channel_name": channel_title,
            "duration": content_details.get("duration", ""),
            "view_count": view_count,
            "like_count": _maybe_int(statistics.get("likeCount")),
            "comment_count": _maybe_int(statistics.get("commentCount")),
        },
    )


def _maybe_int(value: object) -> int | None:
    if value is None:
        return None
    try:
        return int(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


class YouTubeAdapter:
    """`SearchAdapter` for YouTube videos via the Data API v3."""

    name = "youtube"

    def search(
        self,
        query: str,
        *,
        filter_hints: dict | None = None,
        max_results: int = 50,
    ) -> list[CandidateItem]:
        api_key = _get_api_key()
        hints = filter_hints or {}
        # Pass-through keys the YouTube API understands directly.
        passthrough = {
            k: hints[k]
            for k in ("publishedAfter", "publishedBefore", "videoDuration", "relevanceLanguage", "regionCode", "order")
            if k in hints
        }

        search_items = _search_videos(
            api_key,
            query,
            max_results=max_results,
            extra_params=passthrough or None,
        )
        if not search_items:
            return []

        video_ids: list[str] = []
        for item in search_items:
            id_field = item.get("id") or {}
            vid = id_field.get("videoId") if isinstance(id_field, dict) else None
            if vid:
                video_ids.append(vid)

        details_map = _get_video_details(api_key, video_ids) if video_ids else {}

        candidates: list[CandidateItem] = []
        for item in search_items:
            id_field = item.get("id") or {}
            vid = id_field.get("videoId") if isinstance(id_field, dict) else None
            if not vid:
                continue
            candidate = _to_candidate(item, details_map.get(vid))
            if candidate is not None:
                candidates.append(candidate)
        return candidates[:max_results]


# Type-checker assurance the class satisfies the protocol.
_: SearchAdapter = YouTubeAdapter()
