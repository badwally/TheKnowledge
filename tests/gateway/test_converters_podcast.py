"""INT-3: PodcastConverter tests."""

from __future__ import annotations

import hashlib
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from gateway import frontmatter as fm, paths, validator
from gateway.converters import podcast as podcast_mod
from gateway.converters.base import ConversionError
from gateway.converters.podcast import PodcastConverter, _url_slug
from gateway.transcription import Segment, TranscriptionResult


# --- helper: fake TranscriptionResult ----------------------------------------


def _fake_result(text: str = "Hello world.") -> TranscriptionResult:
    seg = Segment(start=0.0, end=2.0, text=text, speaker="SPEAKER_00")
    return TranscriptionResult(
        text=text,
        language="en",
        segments=[seg],
        duration_s=2.0,
        model="mlx-community/whisper-large-v3-turbo",
        diarized=True,
    )


_FAKE_MP3 = b"\xff\xfb" + b"\x00" * 100  # minimal fake mp3 header bytes


# --- unit tests for helpers --------------------------------------------------


def test_url_slug_extracts_stem():
    slug = _url_slug("https://feeds.example.com/episodes/lex-fridman-ep-450.mp3")
    assert slug == "lex-fridman-ep-450"


def test_url_slug_strips_query():
    slug = _url_slug("https://cdn.example.com/ep-100.mp3?token=abc&t=0")
    assert slug == "ep-100"


def test_url_slug_clamps_to_five_words():
    slug = _url_slug("https://example.com/a-very-long-episode-title-that-exceeds-limit.mp3")
    assert len(slug.split("-")) <= 5


def test_url_slug_is_always_nonempty():
    slug = _url_slug("https://example.com/")
    assert slug  # any non-empty string is acceptable


# --- detect() ----------------------------------------------------------------


def test_detect_mp3_url():
    assert PodcastConverter().detect("https://feeds.example.com/ep-001.mp3")


def test_detect_m4a_url():
    assert PodcastConverter().detect("https://cdn.example.com/episode.m4a?token=xyz")


def test_detect_ogg_url():
    assert PodcastConverter().detect("http://example.com/episode.ogg")


def test_detect_rejects_local_path():
    assert not PodcastConverter().detect("/local/file.mp3")


def test_detect_rejects_non_audio_url():
    assert not PodcastConverter().detect("https://example.com/page.html")


def test_detect_rejects_youtube_url():
    assert not PodcastConverter().detect("https://www.youtube.com/watch?v=abc")


# --- convert() ---------------------------------------------------------------


def _run_convert(url: str, audio_bytes: bytes = _FAKE_MP3) -> tuple[dict, str]:
    """Helper: patches download + transcribe, runs convert, returns (front, body)."""
    result = _fake_result()

    def _fake_urlretrieve(url, dest):
        Path(dest).write_bytes(audio_bytes)

    with (
        patch.object(podcast_mod, "urllib") as mock_urllib,
        patch.object(podcast_mod, "transcribe", return_value=result),
        patch.object(podcast_mod, "load_transcript_cache", return_value=None),
        patch.object(podcast_mod, "save_transcript_cache"),
    ):
        mock_urllib.request.urlretrieve.side_effect = _fake_urlretrieve
        text = PodcastConverter().convert(url)

    return fm.parse(text)


def test_convert_produces_canonical(kb_root):
    url = "https://feeds.example.com/episodes/ep-001.mp3"
    front, body = _run_convert(url)

    assert front["type"] == "podcast"
    assert front["id"].startswith("podcast-ep-001-")
    assert front["url"] == url
    assert front["meta"]["episode_url"] == url
    assert front["meta"]["extraction_tool"] == "mlx-whisper"
    assert front["meta"]["diarized"] is True
    assert len(front["id"]) == len("podcast-ep-001-") + 10


def test_convert_content_hash_matches_body(kb_root):
    url = "https://feeds.example.com/episodes/ep-hash.mp3"
    front, body = _run_convert(url)

    expected_hash = validator.compute_content_hash(body)
    assert front["content_hash"] == expected_hash


def test_convert_sidecar_written(kb_root):
    url = "https://feeds.example.com/episodes/ep-sidecar.mp3"
    _run_convert(url)

    podcast_dir = paths.raw_dir_for("podcast")
    sidecars = list(podcast_dir.glob("podcast-*.mp3"))
    assert len(sidecars) == 1


def test_convert_sidecar_not_duplicated(kb_root):
    url = "https://feeds.example.com/episodes/ep-dup.mp3"
    _run_convert(url)
    _run_convert(url)

    podcast_dir = paths.raw_dir_for("podcast")
    sidecars = list(podcast_dir.glob("podcast-*.mp3"))
    assert len(sidecars) == 1


def test_convert_body_contains_transcript(kb_root):
    url = "https://feeds.example.com/episodes/ep-body.mp3"
    front, body = _run_convert(url, _FAKE_MP3)
    assert len(body.strip()) > 0


def test_convert_download_failure_raises(kb_root):
    def _bad_urlretrieve(url, dest):
        raise OSError("timeout")

    with (
        patch.object(podcast_mod, "urllib") as mock_urllib,
    ):
        mock_urllib.request.urlretrieve.side_effect = _bad_urlretrieve
        with pytest.raises(ConversionError, match="download failed"):
            PodcastConverter().convert("https://bad.example.com/ep.mp3")


def test_convert_empty_download_raises(kb_root):
    def _empty_urlretrieve(url, dest):
        Path(dest).write_bytes(b"")

    with (
        patch.object(podcast_mod, "urllib") as mock_urllib,
    ):
        mock_urllib.request.urlretrieve.side_effect = _empty_urlretrieve
        with pytest.raises(ConversionError, match="empty file"):
            PodcastConverter().convert("https://bad.example.com/ep.mp3")


def test_convert_uses_transcript_cache(kb_root):
    url = "https://feeds.example.com/episodes/ep-cache.mp3"
    cached_result = _fake_result("Cached transcript text.")

    def _fake_urlretrieve(url, dest):
        Path(dest).write_bytes(_FAKE_MP3)

    with (
        patch.object(podcast_mod, "urllib") as mock_urllib,
        patch.object(podcast_mod, "load_transcript_cache", return_value=cached_result),
        patch.object(podcast_mod, "transcribe") as mock_transcribe,
        patch.object(podcast_mod, "save_transcript_cache"),
    ):
        mock_urllib.request.urlretrieve.side_effect = _fake_urlretrieve
        PodcastConverter().convert(url)
        mock_transcribe.assert_not_called()


def test_convert_diarization_fallback(kb_root):
    url = "https://feeds.example.com/episodes/ep-diarize.mp3"
    no_diarize_result = _fake_result()
    no_diarize_result.diarized = False

    def _fake_urlretrieve(url, dest):
        Path(dest).write_bytes(_FAKE_MP3)

    from gateway.transcription import TranscriptionError

    def _transcribe_side_effect(path, model, diarize):
        if diarize:
            raise TranscriptionError("diarization token missing")
        return no_diarize_result

    with (
        patch.object(podcast_mod, "urllib") as mock_urllib,
        patch.object(podcast_mod, "load_transcript_cache", return_value=None),
        patch.object(podcast_mod, "transcribe", side_effect=_transcribe_side_effect),
        patch.object(podcast_mod, "save_transcript_cache"),
    ):
        mock_urllib.request.urlretrieve.side_effect = _fake_urlretrieve
        front, _ = fm.parse(PodcastConverter().convert(url))

    assert front["meta"]["diarized"] is False


# --- validator integration ---------------------------------------------------


def test_podcast_type_in_allowed_source_types():
    assert "podcast" in validator.ALLOWED_SOURCE_TYPES


def test_podcast_id_matches_pattern():
    pattern = validator.ID_PATTERNS["podcast"]
    assert pattern.match("podcast-lex-fridman-ep-450-a1b2c3d4ef")
    assert not pattern.match("yt-abc123")
    assert not pattern.match("podcast")


def test_podcast_in_source_types():
    assert "podcast" in paths.SOURCE_TYPES


# --- registry integration ---------------------------------------------------


def test_podcast_converter_registered():
    from gateway import converters
    converters.reset_registry_for_tests()
    try:
        from gateway.converters.podcast import PodcastConverter as PC
        converters.register(PC())
        c = converters.dispatch("https://feeds.example.com/ep.mp3")
        assert isinstance(c, PC)
    finally:
        converters.reset_registry_for_tests()
