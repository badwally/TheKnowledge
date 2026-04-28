"""Tests for M21: transcription module + voice / audiobook converters.

The mlx-whisper and pyannote calls are mocked — the actual model load is
multi-second and gated by HF auth, neither of which belongs in unit tests.
"""

from __future__ import annotations

import struct
import wave
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from gateway import frontmatter as fm, paths
from gateway.converters import dispatch, reset_registry_for_tests
from gateway.converters.audiobook import AudiobookConverter
from gateway.converters.voice import VoiceConverter
from gateway.transcription import (
    DEFAULT_DIARIZATION_PIPELINE,
    DEFAULT_MODEL,
    Segment,
    TranscriptionError,
    TranscriptionResult,
    _attach_speakers,
    _ensure_hf_token,
    _timestamp_anchor,
    render_transcript,
    transcribe,
)


# --- helpers ---------------------------------------------------------------


def _stub_audio(tmp_path: Path, name: str = "clip.wav", seconds: float = 0.1) -> Path:
    """Write a tiny silent WAV file (real bytes; converters open it)."""
    target = tmp_path / name
    sample_rate = 8000
    n_samples = int(sample_rate * seconds)
    with wave.open(str(target), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sample_rate)
        w.writeframes(struct.pack(f"<{n_samples}h", *([0] * n_samples)))
    return target


def _stub_whisper_payload(*segments: tuple[float, float, str]) -> dict:
    return {
        "text": " ".join(s[2] for s in segments).strip(),
        "language": "en",
        "segments": [
            {"start": s[0], "end": s[1], "text": s[2]} for s in segments
        ],
    }


# --- transcription.transcribe / render -------------------------------------


def test_transcribe_returns_structured_result(tmp_path):
    audio = _stub_audio(tmp_path)
    payload = _stub_whisper_payload((0.0, 1.5, "hello world"), (1.5, 3.0, "second turn"))

    with patch(
        "gateway.transcription._mlx_whisper_transcribe", return_value=payload
    ) as call:
        result = transcribe(audio, model=DEFAULT_MODEL, diarize=False)

    call.assert_called_once()
    assert result.text == "hello world second turn"
    assert result.language == "en"
    assert result.diarized is False
    assert [s.text for s in result.segments] == ["hello world", "second turn"]
    assert result.duration_s == 3.0
    assert result.model == DEFAULT_MODEL


def test_transcribe_audio_missing_raises(tmp_path):
    with pytest.raises(TranscriptionError, match="audio not found"):
        transcribe(tmp_path / "nope.wav")


def test_transcribe_diarize_calls_pyannote(tmp_path):
    audio = _stub_audio(tmp_path)
    payload = _stub_whisper_payload((0.0, 2.0, "alpha"), (2.0, 4.0, "beta"))

    fake_diarization = MagicMock()
    # Two turns: one per segment.
    fake_diarization.itertracks.return_value = [
        (MagicMock(start=0.0, end=2.0), None, "SPEAKER_00"),
        (MagicMock(start=2.0, end=4.0), None, "SPEAKER_01"),
    ]

    with (
        patch("gateway.transcription._mlx_whisper_transcribe", return_value=payload),
        patch(
            "gateway.transcription._pyannote_diarize", return_value=fake_diarization
        ) as diar,
        patch("gateway.transcription._ensure_hf_token", return_value="hf_xxx"),
    ):
        result = transcribe(audio, diarize=True)

    diar.assert_called_once()
    assert result.diarized is True
    assert [s.speaker for s in result.segments] == ["SPEAKER_00", "SPEAKER_01"]


def test_transcribe_diarize_without_token_raises(tmp_path, monkeypatch):
    audio = _stub_audio(tmp_path)
    monkeypatch.delenv("HF_TOKEN", raising=False)
    monkeypatch.delenv("HUGGING_FACE_HUB_TOKEN", raising=False)

    # Point the cached-token lookup at an empty dir.
    monkeypatch.setenv("HOME", str(tmp_path))

    with patch("gateway.transcription._mlx_whisper_transcribe", return_value=_stub_whisper_payload((0.0, 1.0, "x"))):
        with pytest.raises(TranscriptionError, match="HF_TOKEN"):
            transcribe(audio, diarize=True)


def test_attach_speakers_picks_largest_overlap():
    segments = [
        Segment(start=0.0, end=10.0, text="long turn"),
        Segment(start=10.0, end=11.0, text="quick"),
    ]
    fake_diar = MagicMock()
    # SPEAKER_A occupies 0-7, SPEAKER_B occupies 7-15
    fake_diar.itertracks.return_value = [
        (MagicMock(start=0.0, end=7.0), None, "SPEAKER_A"),
        (MagicMock(start=7.0, end=15.0), None, "SPEAKER_B"),
    ]
    out = _attach_speakers(segments, fake_diar)
    assert out[0].speaker == "SPEAKER_A"  # 7s overlap > 3s
    assert out[1].speaker == "SPEAKER_B"  # full overlap


def test_render_transcript_coalesces_consecutive_same_speaker():
    segments = [
        Segment(start=0.0, end=2.0, text="hello", speaker="A"),
        Segment(start=2.0, end=4.0, text="more from A", speaker="A"),
        Segment(start=4.0, end=6.0, text="now B", speaker="B"),
    ]
    result = TranscriptionResult(text="x", language="en", segments=segments, diarized=True)
    out = render_transcript(result)
    a_count = out.count("**A**")
    b_count = out.count("**B**")
    assert a_count == 1  # coalesced into one turn
    assert b_count == 1
    assert "hello more from A" in out
    assert "now B" in out


def test_render_transcript_no_diarization_uses_anchors_only():
    segments = [
        Segment(start=0.0, end=2.0, text="hello"),
        Segment(start=2.0, end=4.0, text="world"),
    ]
    result = TranscriptionResult(text="hello world", language="en", segments=segments)
    out = render_transcript(result, include_timestamps=True)
    assert "**" not in out  # no speaker bold
    assert "[00:00]" in out


def test_timestamp_anchor_formats_correctly():
    assert _timestamp_anchor(5.5) == "`[00:05]`"
    assert _timestamp_anchor(75) == "`[01:15]`"
    assert _timestamp_anchor(3661) == "`[1:01:01]`"


# --- HF token resolution ---------------------------------------------------


def test_ensure_hf_token_reads_env(monkeypatch):
    monkeypatch.setenv("HF_TOKEN", "abc")
    assert _ensure_hf_token() == "abc"


def test_ensure_hf_token_reads_huggingface_hub_token(monkeypatch):
    monkeypatch.delenv("HF_TOKEN", raising=False)
    monkeypatch.setenv("HUGGING_FACE_HUB_TOKEN", "xyz")
    assert _ensure_hf_token() == "xyz"


def test_ensure_hf_token_reads_cached_file(monkeypatch, tmp_path):
    monkeypatch.delenv("HF_TOKEN", raising=False)
    monkeypatch.delenv("HUGGING_FACE_HUB_TOKEN", raising=False)
    cache = tmp_path / ".cache" / "huggingface"
    cache.mkdir(parents=True)
    (cache / "token").write_text("file-token\n")
    monkeypatch.setenv("HOME", str(tmp_path))
    assert _ensure_hf_token() == "file-token"


def test_ensure_hf_token_missing_raises(monkeypatch, tmp_path):
    monkeypatch.delenv("HF_TOKEN", raising=False)
    monkeypatch.delenv("HUGGING_FACE_HUB_TOKEN", raising=False)
    monkeypatch.setenv("HOME", str(tmp_path))
    with pytest.raises(TranscriptionError, match="HF_TOKEN"):
        _ensure_hf_token()


# --- VoiceConverter --------------------------------------------------------


def test_voice_converter_detects_audio_extensions(tmp_path):
    conv = VoiceConverter(diarize=False)
    assert conv.detect(str(tmp_path / "x.m4a"))
    assert conv.detect(str(tmp_path / "x.mp3"))
    assert conv.detect(str(tmp_path / "x.wav"))
    assert conv.detect(str(tmp_path / "x.flac"))
    assert not conv.detect("https://example.com/x.mp3")
    assert not conv.detect(str(tmp_path / "x.pdf"))


def test_voice_converter_round_trips_with_mocked_transcription(kb_root, tmp_path):
    audio = _stub_audio(tmp_path, "Voice memo.m4a")
    payload = _stub_whisper_payload((0.0, 1.5, "hello"), (1.5, 3.0, "world"))

    with patch("gateway.transcription._mlx_whisper_transcribe", return_value=payload):
        out = VoiceConverter(diarize=False).convert(str(audio))

    front, body = fm.parse(out)
    assert front["type"] == "voice"
    assert front["id"].startswith("voice-voice-memo-")
    assert front["meta"]["extraction_tool"] == "mlx-whisper"
    assert front["meta"]["language"] == "en"
    assert front["meta"]["diarized"] is False
    assert front["meta"]["segment_count"] == 2
    assert "hello" in body and "world" in body
    sidecar = paths.knowledge_root() / front["source_path"]
    assert sidecar.exists()


def test_voice_converter_falls_back_when_diarization_token_missing(kb_root, tmp_path, monkeypatch):
    audio = _stub_audio(tmp_path, "memo.m4a")
    payload = _stub_whisper_payload((0.0, 1.0, "x"))
    monkeypatch.delenv("HF_TOKEN", raising=False)
    monkeypatch.delenv("HUGGING_FACE_HUB_TOKEN", raising=False)
    monkeypatch.setenv("HOME", str(tmp_path))

    with patch("gateway.transcription._mlx_whisper_transcribe", return_value=payload):
        out = VoiceConverter(diarize=True).convert(str(audio))

    front, _body = fm.parse(out)
    assert front["meta"]["diarized"] is False  # graceful fallback


def test_voice_converter_propagates_non_diarization_errors(kb_root, tmp_path):
    audio = _stub_audio(tmp_path)

    def _fail(*_a, **_k):
        raise TranscriptionError("mlx-whisper transcribe failed: backend down")

    with patch("gateway.transcription._mlx_whisper_transcribe", side_effect=_fail):
        with pytest.raises(Exception):  # ConversionError
            VoiceConverter(diarize=False).convert(str(audio))


# --- AudiobookConverter ---------------------------------------------------


def test_audiobook_converter_detects_m4b_only(tmp_path):
    conv = AudiobookConverter()
    assert conv.detect(str(tmp_path / "book.m4b"))
    # mp3/m4a fall through to voice; not handled by audiobook
    assert not conv.detect(str(tmp_path / "x.mp3"))
    assert not conv.detect(str(tmp_path / "x.m4a"))


def test_audiobook_converter_renders_chapters(kb_root, tmp_path):
    """Use a stubbed mutagen.File response so the test doesn't need a real m4b."""
    audio = tmp_path / "book.m4b"
    audio.write_bytes(b"fake")  # not a real m4b — mutagen call is mocked
    payload = _stub_whisper_payload(
        (0.0, 30.0, "Once upon a time."),
        (30.0, 90.0, "The middle of chapter one."),
        (90.0, 150.0, "Chapter two opens here."),
    )

    with (
        patch("gateway.converters.audiobook._read_metadata", return_value=(
            {"title": "Test Book", "author": "Author Name", "album": "Album",
             "year": "2026-04-01", "narrator": "Narrator", "duration_s": 150.0},
            [(0.0, "Chapter One"), (90.0, "Chapter Two")],
        )),
        patch("gateway.transcription._mlx_whisper_transcribe", return_value=payload),
    ):
        out = AudiobookConverter(diarize=False).convert(str(audio))

    front, body = fm.parse(out)
    assert front["type"] == "audiobook"
    assert front["title"] == "Test Book"
    assert front["authors"] == ["Author Name"]
    assert front["meta"]["chapter_count"] == 2
    assert front["meta"]["narrator"] == "Narrator"
    assert front["published_at"] == "2026-04-01"
    assert "## Chapter One" in body
    assert "## Chapter Two" in body
    assert "Once upon a time" in body


# --- dispatch wiring ------------------------------------------------------


def test_dispatch_routes_m4b_to_audiobook(tmp_path):
    reset_registry_for_tests()
    p = str(tmp_path / "x.m4b")
    conv = dispatch(p)
    assert conv.type_name == "audiobook"


def test_dispatch_routes_m4a_to_voice(tmp_path):
    reset_registry_for_tests()
    p = str(tmp_path / "x.m4a")
    conv = dispatch(p)
    assert conv.type_name == "voice"
