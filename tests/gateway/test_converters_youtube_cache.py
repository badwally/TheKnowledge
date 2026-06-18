"""Transcript-cache seam for the YouTube converter.

When YouTube IP-throttles transcript fetches (HTTP 429 across both
``youtube-transcript-api`` and ``yt-dlp``), the converter falls back to a
local transcript cache: a user (or a future yt-dlp fallback) drops
``<video_id>.txt`` or ``<video_id>.vtt`` into ``.knowledge/transcripts/``
(or a dir named by ``WIKI_TRANSCRIPT_CACHE``) and ``convert()`` uses it
instead of hitting the network.
"""

from __future__ import annotations

import pytest

from gateway import frontmatter as fm
from gateway.converters import youtube as yt_mod
from gateway.converters.base import ConversionError


@pytest.fixture
def cache_dir(tmp_path, monkeypatch):
    d = tmp_path / "transcripts"
    d.mkdir()
    monkeypatch.setenv("WIKI_TRANSCRIPT_CACHE", str(d))
    return d


def test_load_cached_returns_none_when_absent(cache_dir):
    assert yt_mod._load_cached_transcript("missingVID01") is None


def test_load_cached_plain_txt(cache_dir):
    (cache_dir / "vidPLAIN01.txt").write_text(
        "Welcome to the keynote.\nWe discuss knowledge graphs.\n",
        encoding="utf-8",
    )
    snippets = yt_mod._load_cached_transcript("vidPLAIN01")
    assert snippets is not None
    assert [s["text"] for s in snippets] == [
        "Welcome to the keynote.",
        "We discuss knowledge graphs.",
    ]
    assert all(s["start"] == 0.0 for s in snippets)


def test_load_cached_txt_with_interleaved_timestamps(cache_dir):
    # The format you get copying the YouTube "Show transcript" panel.
    (cache_dir / "vidTS00001.txt").write_text(
        "0:00\nIntro to SPARQL.\n0:05\nReasoning at scale.\n1:02\nWrap up.\n",
        encoding="utf-8",
    )
    snippets = yt_mod._load_cached_transcript("vidTS00001")
    assert [(s["start"], s["text"]) for s in snippets] == [
        (0.0, "Intro to SPARQL."),
        (5.0, "Reasoning at scale."),
        (62.0, "Wrap up."),
    ]


def test_load_cached_vtt(cache_dir):
    (cache_dir / "vidVTT0001.vtt").write_text(
        "WEBVTT\n\n"
        "00:00:01.000 --> 00:00:03.000\n"
        "First cue line.\n\n"
        "00:00:03.000 --> 00:00:06.500\n"
        "Second cue line.\n",
        encoding="utf-8",
    )
    snippets = yt_mod._load_cached_transcript("vidVTT0001")
    assert [(s["start"], s["text"]) for s in snippets] == [
        (1.0, "First cue line."),
        (3.0, "Second cue line."),
    ]


def test_convert_uses_cache_and_skips_network(cache_dir, monkeypatch):
    monkeypatch.setattr(
        yt_mod,
        "_fetch_oembed",
        lambda vid: {"title": "KG Keynote", "author_name": "KGC"},
    )

    def _boom(vid):  # network path must not be reached
        raise ConversionError("network should not be called when cache hits")

    monkeypatch.setattr(yt_mod, "_fetch_transcript", _boom)

    (cache_dir / "abc123XYZ_-.txt").write_text(
        "Cached transcript body.\n", encoding="utf-8"
    )
    text = yt_mod.YouTubeConverter().convert(
        "https://www.youtube.com/watch?v=abc123XYZ_-"
    )
    front, body = fm.parse(text)
    assert front["id"] == "yt-abc123XYZ_-"
    assert "Cached transcript body." in body
    assert front["meta"]["caption_track"] == "cached"


def test_convert_falls_through_to_network_when_no_cache(cache_dir, monkeypatch):
    monkeypatch.setattr(
        yt_mod, "_fetch_oembed", lambda vid: {"title": "x", "author_name": "y"}
    )
    monkeypatch.setattr(
        yt_mod,
        "_fetch_transcript",
        lambda vid: [{"text": "from network", "start": 0.0, "duration": 1.0}],
    )
    text = yt_mod.YouTubeConverter().convert(
        "https://www.youtube.com/watch?v=nocacheVID1"
    )
    _, body = fm.parse(text)
    assert "from network" in body
