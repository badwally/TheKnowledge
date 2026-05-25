"""Voice converter: local audio file → canonical markdown with transcript.

Uses `gateway.transcription` (mlx-whisper + optional pyannote diarization).
Preserves the original audio as a sidecar at `raw/voice/<id>.<ext>`.

Canonical ID: `voice-<filename-slug>-<sha-prefix>`. Filename slug aids
discovery; the hash prefix prevents collisions when the same nominal
title is recorded twice.
"""

from __future__ import annotations

import hashlib
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import ClassVar

from gateway import frontmatter as fm, paths, validator
from gateway.converters.base import ConversionError, Converter
from gateway.transcription import (
    DEFAULT_MODEL,
    TranscriptionError,
    load_transcript_cache,
    render_transcript,
    save_transcript_cache,
    transcribe,
)


_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def _slug(name: str, max_words: int = 5) -> str:
    cleaned = _NON_ALNUM.sub("-", name.lower()).strip("-")
    parts = [p for p in cleaned.split("-") if p]
    return "-".join(parts[:max_words]) or "voice"


def _sha_prefix(data: bytes, n: int = 10) -> str:
    return hashlib.sha256(data).hexdigest()[:n]


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class VoiceConverter(Converter):
    type_name: ClassVar[str] = "voice"

    AUDIO_SUFFIXES: ClassVar[tuple[str, ...]] = (
        ".m4a", ".mp3", ".wav", ".flac", ".ogg", ".aac", ".opus",
    )

    def __init__(
        self,
        *,
        model: str = DEFAULT_MODEL,
        diarize: bool = True,
    ):
        self._model = model
        self._diarize = diarize

    def detect(self, source: str) -> bool:
        if source.startswith(("http://", "https://")):
            return False
        try:
            return Path(source).suffix.lower() in self.AUDIO_SUFFIXES
        except (TypeError, ValueError):
            return False

    def convert(self, source: str) -> str:
        path = Path(source).expanduser().resolve()
        if not path.is_file():
            raise ConversionError(f"audio not found: {path}")

        raw_bytes = path.read_bytes()
        sha256hex = hashlib.sha256(raw_bytes).hexdigest()
        cache_dir = paths.raw_dir_for("voice") / "_transcripts"

        result = load_transcript_cache(cache_dir, sha256hex, self._model)
        if result is None:
            try:
                result = transcribe(path, model=self._model, diarize=self._diarize)
            except TranscriptionError as e:
                # Soft-fall back to transcript-only when diarization auth fails.
                if self._diarize and "diarization" in str(e).lower():
                    result = transcribe(path, model=self._model, diarize=False)
                    result.diarized = False
                else:
                    raise ConversionError(str(e)) from e
            save_transcript_cache(cache_dir, sha256hex, result)

        body_text = render_transcript(result, include_timestamps=True)
        if not body_text.strip():
            raise ConversionError(f"no transcript produced for {path}")

        canonical_id = f"voice-{_slug(path.stem)}-{_sha_prefix(raw_bytes)}"

        sidecar_dir = paths.raw_dir_for("voice")
        sidecar_dir.mkdir(parents=True, exist_ok=True)
        sidecar_target = sidecar_dir / f"{canonical_id}{path.suffix.lower()}"
        if not sidecar_target.exists():
            shutil.copy2(path, sidecar_target)

        body = body_text.rstrip("\n") + "\n"
        sidecar_rel = sidecar_target.relative_to(paths.knowledge_root())
        speaker_count = len({s.speaker for s in result.segments if s.speaker})

        front = {
            "id": canonical_id,
            "type": "voice",
            "title": path.stem,
            "url": "",
            "authors": [],
            "ingested_at": _now_iso(),
            "content_hash": validator.compute_content_hash(body),
            "source_path": str(sidecar_rel),
            "domains": [],
            "nlm_corpus_ids": [],
            "wiki_pages": [],
            "meta": {
                "extraction_tool": "mlx-whisper",
                "model": result.model,
                "language": result.language,
                "duration_s": round(result.duration_s, 2),
                "diarized": result.diarized,
                "speaker_count": speaker_count,
                "segment_count": len(result.segments),
                "original_path": str(path),
            },
        }
        return fm.serialize(front, body)
