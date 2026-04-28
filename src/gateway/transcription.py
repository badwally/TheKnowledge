"""Audio transcription + speaker diarization for the voice / audiobook converters.

Backends:
- **mlx-whisper** (Apple MLX, Metal-accelerated) — required.
  Default model: `mlx-community/whisper-large-v3-turbo`.
- **pyannote.audio** — optional diarization.
  Default pipeline: `pyannote/speaker-diarization-3.1` (gated; requires a
  Hugging Face access token and one-time acceptance of the model's terms).

Imports are lazy so that the rest of the gateway works on installs that
omit the `[whisper]` extra. Functions raise `TranscriptionError` with an
actionable message if a dependency or token is missing.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


DEFAULT_MODEL = "mlx-community/whisper-large-v3-turbo"
DEFAULT_DIARIZATION_PIPELINE = "pyannote/speaker-diarization-3.1"


class TranscriptionError(RuntimeError):
    """Raised when transcription or diarization cannot proceed."""


@dataclass(frozen=True)
class Segment:
    start: float       # seconds
    end: float
    text: str
    speaker: str = ""  # empty string when diarization disabled / unmatched


@dataclass
class TranscriptionResult:
    text: str
    language: str
    segments: list[Segment] = field(default_factory=list)
    duration_s: float = 0.0
    model: str = ""
    diarized: bool = False

    def to_dict(self) -> dict:
        return {
            "text": self.text,
            "language": self.language,
            "duration_s": self.duration_s,
            "model": self.model,
            "diarized": self.diarized,
            "segments": [
                {"start": s.start, "end": s.end, "text": s.text, "speaker": s.speaker}
                for s in self.segments
            ],
        }


# --- mlx-whisper transcription --------------------------------------------


def _mlx_whisper_transcribe(audio_path: Path, *, model: str) -> dict:
    try:
        import mlx_whisper  # type: ignore
    except ImportError as e:
        raise TranscriptionError(
            "mlx-whisper not installed; run: pip install -e \".[whisper]\""
        ) from e
    try:
        return mlx_whisper.transcribe(
            str(audio_path), path_or_hf_repo=model, fp16=False
        )
    except Exception as e:
        raise TranscriptionError(f"mlx-whisper transcribe failed on {audio_path}: {e}") from e


# --- pyannote diarization --------------------------------------------------


def _ensure_hf_token(env_var: str = "HF_TOKEN") -> str:
    token = os.environ.get(env_var) or os.environ.get("HUGGING_FACE_HUB_TOKEN")
    if token:
        return token
    cached = Path.home() / ".cache" / "huggingface" / "token"
    if cached.is_file():
        try:
            value = cached.read_text().strip()
            if value:
                return value
        except OSError:
            pass
    raise TranscriptionError(
        "diarization requires a Hugging Face access token. "
        "Set $HF_TOKEN or run `huggingface-cli login`. "
        "You must also accept the terms at "
        f"https://huggingface.co/{DEFAULT_DIARIZATION_PIPELINE} once."
    )


def _pyannote_diarize(audio_path: Path, *, pipeline_name: str, hf_token: str):
    try:
        from pyannote.audio import Pipeline  # type: ignore
    except ImportError as e:
        raise TranscriptionError(
            "pyannote.audio not installed; run: pip install -e \".[whisper]\""
        ) from e
    try:
        pipeline = Pipeline.from_pretrained(pipeline_name, token=hf_token)
    except Exception as e:
        raise TranscriptionError(
            f"failed to load diarization pipeline {pipeline_name!r}: {e}. "
            "Confirm the HF token is valid and that you have accepted the model's "
            f"terms at https://huggingface.co/{pipeline_name}."
        ) from e
    if pipeline is None:
        raise TranscriptionError(
            f"Pipeline.from_pretrained({pipeline_name!r}) returned None — "
            "auth or model-acceptance issue."
        )
    try:
        return pipeline(str(audio_path))
    except Exception as e:
        raise TranscriptionError(f"diarization run failed on {audio_path}: {e}") from e


def _attach_speakers(segments: list[Segment], diarization) -> list[Segment]:
    """Annotate each whisper segment with the speaker that overlaps it most.

    `diarization` is a pyannote `Annotation` instance; we iterate its
    timeline once per whisper segment.
    """
    out: list[Segment] = []
    for seg in segments:
        best_speaker = ""
        best_overlap = 0.0
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            overlap_start = max(seg.start, turn.start)
            overlap_end = min(seg.end, turn.end)
            overlap = max(0.0, overlap_end - overlap_start)
            if overlap > best_overlap:
                best_overlap = overlap
                best_speaker = str(speaker)
        out.append(
            Segment(start=seg.start, end=seg.end, text=seg.text, speaker=best_speaker)
        )
    return out


# --- public API ------------------------------------------------------------


def transcribe(
    audio_path: str | Path,
    *,
    model: str = DEFAULT_MODEL,
    diarize: bool = False,
    diarization_pipeline: str = DEFAULT_DIARIZATION_PIPELINE,
    hf_token: str | None = None,
) -> TranscriptionResult:
    """Transcribe `audio_path` with mlx-whisper; optionally diarize.

    With `diarize=True`, requires `pyannote.audio` and a Hugging Face access
    token (passed in `hf_token`, or read from `$HF_TOKEN` /
    `$HUGGING_FACE_HUB_TOKEN` / `~/.cache/huggingface/token`).
    """
    audio_path = Path(audio_path).expanduser().resolve()
    if not audio_path.is_file():
        raise TranscriptionError(f"audio not found: {audio_path}")

    raw = _mlx_whisper_transcribe(audio_path, model=model)

    raw_segments = raw.get("segments") or []
    segments: list[Segment] = [
        Segment(
            start=float(s.get("start", 0.0)),
            end=float(s.get("end", 0.0)),
            text=str(s.get("text", "")).strip(),
            speaker="",
        )
        for s in raw_segments
        if isinstance(s, dict)
    ]
    duration = max((s.end for s in segments), default=0.0)

    if diarize:
        token = hf_token or _ensure_hf_token()
        diarization = _pyannote_diarize(
            audio_path, pipeline_name=diarization_pipeline, hf_token=token
        )
        segments = _attach_speakers(segments, diarization)

    return TranscriptionResult(
        text=str(raw.get("text", "")).strip(),
        language=str(raw.get("language", "")),
        segments=segments,
        duration_s=duration,
        model=model,
        diarized=diarize,
    )


# --- helpers for converters -----------------------------------------------


def render_transcript(result: TranscriptionResult, *, include_timestamps: bool = True) -> str:
    """Render a TranscriptionResult as wiki body markdown.

    Speaker turns are coalesced — consecutive segments sharing a speaker
    are joined into a single paragraph. Timestamps are anchor-friendly
    (`#t-mm-ss`) on each turn so the wiki page can deep-link into a
    recording.
    """
    if not result.segments:
        return result.text + "\n"

    # Coalesce consecutive same-speaker segments.
    turns: list[tuple[float, float, str, str]] = []
    cur_speaker = result.segments[0].speaker
    cur_start = result.segments[0].start
    cur_end = result.segments[0].end
    cur_texts: list[str] = [result.segments[0].text]
    for s in result.segments[1:]:
        if s.speaker == cur_speaker:
            cur_end = s.end
            cur_texts.append(s.text)
        else:
            turns.append((cur_start, cur_end, cur_speaker, " ".join(cur_texts).strip()))
            cur_speaker, cur_start, cur_end = s.speaker, s.start, s.end
            cur_texts = [s.text]
    turns.append((cur_start, cur_end, cur_speaker, " ".join(cur_texts).strip()))

    lines: list[str] = []
    for start, _end, speaker, text in turns:
        anchor = _timestamp_anchor(start) if include_timestamps else ""
        prefix = ""
        if speaker:
            prefix = f"**{speaker}**"
            if anchor:
                prefix += f" {anchor}"
            prefix += ": "
        elif anchor:
            prefix = f"{anchor} "
        lines.append(f"{prefix}{text}")
        lines.append("")  # blank line between turns
    return "\n".join(lines).rstrip() + "\n"


def _timestamp_anchor(seconds: float) -> str:
    total = int(seconds)
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    if h:
        return f"`[{h:d}:{m:02d}:{s:02d}]`"
    return f"`[{m:02d}:{s:02d}]`"
