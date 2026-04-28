"""YouTube converter: video URL → canonical markdown with transcript.

Detects standard YouTube URL forms. Fetches:
- Title via the public oEmbed endpoint (no auth required)
- Transcript via youtube-transcript-api (no auth required)

The transcript is rendered as `[<seconds>] text` lines so anchors like
`[[sources/yt-<videoId>#1820]]` resolve to a specific moment.
"""

from __future__ import annotations

from datetime import datetime, timezone
import re

import requests

from gateway import frontmatter as fm
from gateway import validator
from gateway.converters.base import ConversionError, Converter


_VIDEO_ID_PATTERNS = [
    re.compile(r"youtube\.com/watch\?(?:[^#]*&)?v=([A-Za-z0-9_-]{6,15})"),
    re.compile(r"youtu\.be/([A-Za-z0-9_-]{6,15})"),
    re.compile(r"youtube\.com/(?:embed|shorts|live)/([A-Za-z0-9_-]{6,15})"),
]


def extract_video_id(url: str) -> str | None:
    for pattern in _VIDEO_ID_PATTERNS:
        match = pattern.search(url)
        if match:
            return match.group(1)
    return None


# --- thin wrappers (monkeypatch targets in tests) --------------------------


def _fetch_oembed(video_id: str) -> dict:
    """Pull title/author/channel via the unauthenticated oEmbed endpoint."""
    response = requests.get(
        "https://www.youtube.com/oembed",
        params={
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "format": "json",
        },
        timeout=15,
    )
    if response.status_code != 200:
        raise ConversionError(f"oEmbed lookup failed: {response.status_code}")
    return response.json()


def _fetch_transcript(video_id: str) -> list[dict]:
    """Pull the transcript via youtube-transcript-api.

    Returns a list of {text, start, duration} entries. Raises ConversionError
    if no transcript exists.
    """
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import (
        NoTranscriptFound,
        TranscriptsDisabled,
        VideoUnavailable,
    )

    try:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id)
        return [
            {"text": s.text, "start": s.start, "duration": s.duration}
            for s in fetched.snippets
        ]
    except (NoTranscriptFound, TranscriptsDisabled, VideoUnavailable) as e:
        raise ConversionError(f"no transcript available for {video_id}: {e}") from e
    except Exception as e:
        raise ConversionError(f"transcript fetch failed for {video_id}: {e}") from e


# -----------------------------------------------------------------------------


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _format_transcript(snippets: list[dict]) -> str:
    """Render transcript as `[<int-seconds>] text` lines for anchor support."""
    lines: list[str] = []
    for s in snippets:
        start = int(round(s.get("start", 0)))
        text = (s.get("text") or "").strip()
        if not text:
            continue
        lines.append(f"[{start}] {text}")
    return "\n".join(lines) + "\n"


class YouTubeConverter(Converter):
    type_name = "youtube"

    def detect(self, source: str) -> bool:
        if not source.startswith(("http://", "https://")):
            return False
        return extract_video_id(source) is not None

    def convert(self, source: str) -> str:
        video_id = extract_video_id(source)
        if video_id is None:
            raise ConversionError(f"could not extract a YouTube video id from {source!r}")

        oembed = _fetch_oembed(video_id)
        snippets = _fetch_transcript(video_id)
        body = _format_transcript(snippets)
        if not body.strip():
            raise ConversionError(f"empty transcript for {video_id}")

        front = {
            "id": f"yt-{video_id}",
            "type": "youtube",
            "title": oembed.get("title") or video_id,
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "authors": [oembed["author_name"]] if oembed.get("author_name") else [],
            "ingested_at": _now_iso(),
            "content_hash": validator.compute_content_hash(body),
            "domains": [],
            "nlm_corpus_ids": [],
            "wiki_pages": [],
            "meta": {
                "channel": oembed.get("author_name", ""),
                "channel_url": oembed.get("author_url", ""),
                "duration_seconds": int(snippets[-1]["start"] + snippets[-1].get("duration", 0))
                if snippets
                else 0,
                "caption_track": "fetched",
                "snippet_count": len(snippets),
            },
        }
        return fm.serialize(front, body)
