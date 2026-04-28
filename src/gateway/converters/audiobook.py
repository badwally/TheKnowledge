"""Audiobook converter: local audiobook file → canonical markdown.

Targets `.m4b` (Audible-style audiobooks with embedded chapter metadata),
plus `.mp3`/`.m4a` files long enough to look like books. Uses mutagen to
extract title/author/chapters; uses the transcription module to render
text. Diarization is OFF by default — audiobooks are usually
single-narrator and diarization adds cost without much value.

Sidecar: `raw/audiobook/<id>.<ext>`. Body emits a `## Chapter NN` section
per detected chapter, each followed by the transcript text within that
chapter's time range.
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
    Segment,
    TranscriptionError,
    transcribe,
)


_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def _slug(name: str, max_words: int = 5) -> str:
    cleaned = _NON_ALNUM.sub("-", name.lower()).strip("-")
    parts = [p for p in cleaned.split("-") if p]
    return "-".join(parts[:max_words]) or "audiobook"


def _sha_prefix(data: bytes, n: int = 10) -> str:
    return hashlib.sha256(data).hexdigest()[:n]


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _read_metadata(path: Path) -> tuple[dict, list[tuple[float, str]]]:
    """Return (tags, chapters) where chapters is a sorted list of
    (start_seconds, title)."""
    try:
        from mutagen import File as MFile  # type: ignore
        from mutagen.mp4 import MP4  # type: ignore
    except ImportError as e:
        raise ConversionError(
            "mutagen not installed; run: pip install -e \".[whisper]\""
        ) from e

    audio = MFile(str(path))
    if audio is None:
        raise ConversionError(f"unsupported audio format: {path}")

    tags: dict = {}
    if isinstance(audio, MP4):
        # MP4-style atoms.
        meta = audio.tags or {}
        tags["title"] = (meta.get("\xa9nam") or [""])[0]
        tags["author"] = (meta.get("\xa9ART") or meta.get("\xa9wrt") or [""])[0]
        tags["album"] = (meta.get("\xa9alb") or [""])[0]
        tags["year"] = (meta.get("\xa9day") or [""])[0]
        tags["narrator"] = (meta.get("----:com.apple.iTunes:NARRATOR") or [b""])
        if isinstance(tags["narrator"], list) and tags["narrator"]:
            v = tags["narrator"][0]
            tags["narrator"] = v.decode("utf-8", "ignore") if isinstance(v, (bytes, bytearray)) else str(v)
        else:
            tags["narrator"] = ""
    else:
        # Generic ID3-ish tags via mutagen.File.
        tags["title"] = str((audio.tags or {}).get("title", [""])[0]) if audio.tags else ""
        tags["author"] = str((audio.tags or {}).get("artist", [""])[0]) if audio.tags else ""
        tags["album"] = str((audio.tags or {}).get("album", [""])[0]) if audio.tags else ""
        tags["year"] = str((audio.tags or {}).get("date", [""])[0]) if audio.tags else ""
        tags["narrator"] = ""

    tags["duration_s"] = float(getattr(audio.info, "length", 0.0) or 0.0)

    chapters: list[tuple[float, str]] = []
    chapter_attr = getattr(audio, "chapters", None)
    if chapter_attr:
        for ch in chapter_attr:
            try:
                chapters.append((float(ch.start), str(ch.title or "Chapter")))
            except (AttributeError, ValueError, TypeError):
                continue
    chapters.sort(key=lambda c: c[0])
    return tags, chapters


def _split_segments_by_chapter(
    segments: list[Segment], chapters: list[tuple[float, str]], total_s: float
) -> list[tuple[str, list[Segment]]]:
    if not chapters:
        return [("Transcript", segments)]
    boundaries = [(c[0], c[1]) for c in chapters]
    boundaries.append((total_s + 1.0, "_sentinel_"))
    out: list[tuple[str, list[Segment]]] = []
    for i in range(len(boundaries) - 1):
        start, title = boundaries[i]
        end = boundaries[i + 1][0]
        bucket = [s for s in segments if s.start >= start and s.start < end]
        if bucket:
            out.append((title, bucket))
    if not out:
        return [("Transcript", segments)]
    return out


def _format_timestamp(seconds: float) -> str:
    total = int(seconds)
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    if h:
        return f"{h:d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def _render_audiobook_body(
    chapter_groups: list[tuple[str, list[Segment]]],
    *,
    diarized: bool,
) -> str:
    lines: list[str] = []
    for chapter_title, segs in chapter_groups:
        if not segs:
            continue
        lines.append(f"## {chapter_title}")
        lines.append("")
        lines.append(f"_(starts at {_format_timestamp(segs[0].start)})_")
        lines.append("")
        for s in segs:
            speaker_prefix = f"**{s.speaker}**: " if diarized and s.speaker else ""
            lines.append(f"{speaker_prefix}{s.text}".rstrip())
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


class AudiobookConverter(Converter):
    type_name: ClassVar[str] = "audiobook"

    SUFFIXES: ClassVar[tuple[str, ...]] = (".m4b",)
    LONG_AUDIO_SUFFIXES: ClassVar[tuple[str, ...]] = (".mp3", ".m4a")
    LONG_AUDIO_THRESHOLD_S: ClassVar[float] = 60 * 60.0  # 1 hour

    def __init__(
        self,
        *,
        model: str = DEFAULT_MODEL,
        diarize: bool = False,
    ):
        self._model = model
        self._diarize = diarize

    def detect(self, source: str) -> bool:
        if source.startswith(("http://", "https://")):
            return False
        try:
            suffix = Path(source).suffix.lower()
        except (TypeError, ValueError):
            return False
        if suffix in self.SUFFIXES:
            return True
        # Long .mp3 / .m4a files can also be audiobooks; a downstream check
        # in convert() falls back to voice if duration is short.
        return False

    def convert(self, source: str) -> str:
        path = Path(source).expanduser().resolve()
        if not path.is_file():
            raise ConversionError(f"audiobook not found: {path}")

        tags, chapters = _read_metadata(path)
        try:
            result = transcribe(path, model=self._model, diarize=self._diarize)
        except TranscriptionError as e:
            raise ConversionError(str(e)) from e

        chapter_groups = _split_segments_by_chapter(
            result.segments, chapters, total_s=result.duration_s
        )
        body_text = _render_audiobook_body(chapter_groups, diarized=result.diarized)
        if not body_text.strip():
            raise ConversionError(f"no transcript produced for {path}")

        raw_bytes = path.read_bytes()
        title = tags.get("title") or path.stem
        author = tags.get("author") or ""
        canonical_id = "audiobook-" + _slug(
            f"{author}-{title}" if author else title, max_words=6
        ) + f"-{_sha_prefix(raw_bytes)}"

        sidecar_dir = paths.raw_dir_for("audiobook")
        sidecar_dir.mkdir(parents=True, exist_ok=True)
        sidecar_target = sidecar_dir / f"{canonical_id}{path.suffix.lower()}"
        if not sidecar_target.exists():
            shutil.copy2(path, sidecar_target)

        sidecar_rel = sidecar_target.relative_to(paths.knowledge_root())
        body = body_text.rstrip("\n") + "\n"

        front = {
            "id": canonical_id,
            "type": "audiobook",
            "title": title,
            "url": "",
            "authors": [author] if author else [],
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
                "duration_s": round(result.duration_s or tags.get("duration_s", 0.0), 2),
                "diarized": result.diarized,
                "chapter_count": len(chapters),
                "narrator": tags.get("narrator", ""),
                "album": tags.get("album", ""),
                "original_path": str(path),
            },
        }
        if tags.get("year"):
            front["published_at"] = str(tags["year"])[:10]
        return fm.serialize(front, body)
