"""Podcast converter: audio URL → canonical markdown with transcript.

Handles podcast episodes delivered via URL (e.g. from RSS enclosure links).
Downloads the audio, transcribes using the shared transcription module, and
writes a canonical source to raw/podcast/ with a sidecar audio file.

Detection: http/https URLs whose path ends in a supported audio extension.
This cleanly separates podcasts (URL-sourced) from voice notes (local files).

ID format: podcast-<episode-slug>-<sha256[:10]>
"""

from __future__ import annotations

import hashlib
import re
import shutil
import tempfile
import urllib.request
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

_AUDIO_SUFFIXES: tuple[str, ...] = (
    ".mp3", ".m4a", ".wav", ".flac", ".ogg", ".aac", ".opus",
)


def _url_slug(url: str, max_words: int = 5) -> str:
    stem = Path(url.split("?")[0].split("#")[0]).stem
    cleaned = _NON_ALNUM.sub("-", stem.lower()).strip("-")
    parts = [p for p in cleaned.split("-") if p]
    return "-".join(parts[:max_words]) or "episode"


def _sha_prefix(data: bytes, n: int = 10) -> str:
    return hashlib.sha256(data).hexdigest()[:n]


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class PodcastConverter(Converter):
    type_name: ClassVar[str] = "podcast"

    def __init__(
        self,
        *,
        model: str = DEFAULT_MODEL,
        diarize: bool = True,
    ):
        self._model = model
        self._diarize = diarize

    def detect(self, source: str) -> bool:
        if not source.startswith(("http://", "https://")):
            return False
        path = source.split("?")[0].split("#")[0].lower()
        return any(path.endswith(ext) for ext in _AUDIO_SUFFIXES)

    def convert(self, source: str) -> str:
        ext = Path(source.split("?")[0].split("#")[0]).suffix.lower() or ".mp3"

        # Download to a temporary file
        tmp_fd, tmp_name = tempfile.mkstemp(suffix=ext)
        tmp_path = Path(tmp_name)
        try:
            import os
            os.close(tmp_fd)
            try:
                urllib.request.urlretrieve(source, tmp_path)
            except Exception as e:
                raise ConversionError(f"download failed for {source!r}: {e}") from e

            raw_bytes = tmp_path.read_bytes()
            if not raw_bytes:
                raise ConversionError(f"downloaded empty file from {source!r}")

            sha256hex = hashlib.sha256(raw_bytes).hexdigest()
            canonical_id = f"podcast-{_url_slug(source)}-{sha256hex[:10]}"

            sidecar_dir = paths.raw_dir_for("podcast")
            sidecar_dir.mkdir(parents=True, exist_ok=True)
            sidecar_path = sidecar_dir / f"{canonical_id}{ext}"
            if not sidecar_path.exists():
                shutil.copy2(tmp_path, sidecar_path)

            cache_dir = sidecar_dir / "_transcripts"
            result = load_transcript_cache(cache_dir, sha256hex, self._model)
            if result is None:
                try:
                    result = transcribe(sidecar_path, model=self._model, diarize=self._diarize)
                except TranscriptionError as e:
                    if self._diarize and "diarization" in str(e).lower():
                        result = transcribe(sidecar_path, model=self._model, diarize=False)
                        result.diarized = False
                    else:
                        raise ConversionError(str(e)) from e
                save_transcript_cache(cache_dir, sha256hex, result)
        finally:
            tmp_path.unlink(missing_ok=True)

        body_text = render_transcript(result, include_timestamps=True)
        if not body_text.strip():
            raise ConversionError(f"no transcript produced for {source!r}")

        body = body_text.rstrip("\n") + "\n"
        sidecar_rel = sidecar_path.relative_to(paths.knowledge_root())
        speaker_count = len({s.speaker for s in result.segments if s.speaker})

        front = {
            "id": canonical_id,
            "type": "podcast",
            "title": _url_slug(source).replace("-", " ").title(),
            "url": source,
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
                "episode_url": source,
            },
        }
        return fm.serialize(front, body)
