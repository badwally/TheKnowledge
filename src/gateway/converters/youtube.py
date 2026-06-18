"""YouTube converter: video URL → canonical markdown with transcript.

Detects standard YouTube URL forms. Fetches:
- Title via the public oEmbed endpoint (no auth required)
- Transcript via youtube-transcript-api (no auth required)

The transcript is rendered as `[<seconds>] text` lines so anchors like
`[[sources/yt-<videoId>#1820]]` resolve to a specific moment.
"""

from __future__ import annotations

from datetime import datetime, timezone
import os
from pathlib import Path
import re

import requests

from gateway import frontmatter as fm
from gateway import paths
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


# --- local transcript cache (IP-throttle fallback) -------------------------
#
# YouTube IP-throttles transcript endpoints (HTTP 429) under heavy use,
# defeating both youtube-transcript-api and yt-dlp. When that happens a
# transcript can be supplied out-of-band — copied from the YouTube web
# "Show transcript" panel (authenticated UI, a different endpoint) or
# downloaded later via yt-dlp through an unthrottled IP — and dropped into
# the cache directory as ``<video_id>.txt`` (plain text, optionally with
# interleaved ``M:SS`` timestamp lines) or ``<video_id>.vtt`` (WebVTT).
# ``convert()`` consults the cache before the network.

_TIMESTAMP_LINE = re.compile(r"^(?:(\d{1,2}):)?(\d{1,2}):(\d{2})(?:\.\d+)?$")
_VTT_TAG = re.compile(r"<[^>]+>")


def _transcript_cache_dir() -> Path:
    override = os.environ.get("WIKI_TRANSCRIPT_CACHE")
    if override:
        return Path(override)
    return paths.knowledge_internal() / "transcripts"


def _hms_to_seconds(token: str) -> float | None:
    match = _TIMESTAMP_LINE.match(token.strip())
    if not match:
        return None
    hours = int(match.group(1) or 0)
    minutes = int(match.group(2))
    seconds = int(match.group(3))
    return float(hours * 3600 + minutes * 60 + seconds)


def _parse_txt_transcript(text: str) -> list[dict]:
    """Parse plain text, honoring interleaved ``M:SS`` / ``H:MM:SS`` lines.

    A line that is only a timestamp sets the start for subsequent text lines
    (the YouTube transcript-panel copy format). Files with no timestamps map
    every line to start 0.
    """
    snippets: list[dict] = []
    current_start = 0.0
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        ts = _hms_to_seconds(line)
        if ts is not None:
            current_start = ts
            continue
        snippets.append({"text": line, "start": current_start, "duration": 0.0})
    return snippets


def _parse_vtt_transcript(text: str) -> list[dict]:
    """Parse WebVTT cues into transcript snippets, deduping rolling repeats."""
    snippets: list[dict] = []
    current_start: float | None = None
    for raw in text.splitlines():
        line = raw.strip()
        if "-->" in line:
            left = line.split("-->", 1)[0].strip()
            current_start = _vtt_time_to_seconds(left)
            continue
        if not line or line == "WEBVTT" or line.startswith("NOTE") or line.isdigit():
            continue
        if current_start is None:
            continue
        cleaned = _VTT_TAG.sub("", line).strip()
        if not cleaned:
            continue
        if snippets and snippets[-1]["text"] == cleaned:
            continue
        snippets.append({"text": cleaned, "start": current_start, "duration": 0.0})
    return snippets


def _vtt_time_to_seconds(token: str) -> float:
    # token like "00:00:05.000" or "00:05.000"
    parts = token.split(":")
    try:
        parts = [float(p.replace(",", ".")) for p in parts]
    except ValueError:
        return 0.0
    if len(parts) == 3:
        h, m, s = parts
    elif len(parts) == 2:
        h, m, s = 0.0, parts[0], parts[1]
    else:
        return 0.0
    return h * 3600 + m * 60 + s


def _load_cached_transcript(video_id: str) -> list[dict] | None:
    """Return cached transcript snippets for ``video_id``, or None if absent."""
    cache_dir = _transcript_cache_dir()
    vtt_path = cache_dir / f"{video_id}.vtt"
    if vtt_path.exists():
        snippets = _parse_vtt_transcript(
            vtt_path.read_text(encoding="utf-8", errors="replace")
        )
        if snippets:
            return snippets
    txt_path = cache_dir / f"{video_id}.txt"
    if txt_path.exists():
        snippets = _parse_txt_transcript(
            txt_path.read_text(encoding="utf-8", errors="replace")
        )
        if snippets:
            return snippets
    return None


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
        cached = _load_cached_transcript(video_id)
        if cached is not None:
            snippets = cached
            caption_track = "cached"
        else:
            snippets = _fetch_transcript(video_id)
            caption_track = "fetched"
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
                "caption_track": caption_track,
                "snippet_count": len(snippets),
            },
        }
        return fm.serialize(front, body)
