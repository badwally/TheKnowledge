"""Image converter: image file → canonical markdown with VLM description.

Reads metadata via Pillow (dimensions, format, mode) and gets a structured
description from the injected `VLMClient`. The description is the body of
the canonical markdown — what makes images searchable and citable like any
other source. The original image is preserved as a sidecar at
raw/image/<id>.<ext>.

Supported extensions: .png, .jpg, .jpeg, .gif, .webp, .tiff, .tif, .bmp,
.heic, .heif. (HEIC/HEIF require pillow-heif at runtime; without it,
Pillow can still detect format but not decode pixels — the VLM call still
gets the file path and may handle decoding upstream.)

Canonical ID per WIKI § 6.1: image-<YYYY-MM-DD>-<sha256-prefix-12>.
The date prefix uses the ingest date so chronological browsing of
raw/image/ matches the order images were added.

VLM client is injected via constructor for test stubbing; default is
ClaudeCLIVLMClient (uses `claude -p` and the user's Max-plan auth).
"""

from __future__ import annotations

import hashlib
import shutil
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, UnidentifiedImageError

from gateway import frontmatter as fm
from gateway import paths, validator
from gateway.converters.base import ConversionError, Converter
from gateway.vlm import ClaudeCLIVLMClient, VLMClient, VLMError

_IMAGE_EXTENSIONS = frozenset({
    ".png", ".jpg", ".jpeg", ".gif", ".webp",
    ".tiff", ".tif", ".bmp", ".heic", ".heif",
})

_DESCRIPTION_PROMPT = """\
Describe this image in detail. Provide:

1. **Overview** — one sentence summarizing the subject or scene.
2. **Visible text** — any text content in the image, transcribed verbatim. Write "None" if no text is visible.
3. **Key elements** — the main visual components, objects, or features.
4. **Domain-specific content** — if the image is a chart, diagram, code, screenshot, or other technical artifact, describe its specific content.

Be factual and specific. Do not speculate about meaning or intent. Use markdown formatting with the four section headings above.
""".strip()


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _read_image_metadata(path: Path) -> dict:
    """Return {width, height, format, mode} for the image.

    Raises ConversionError if the file is not a recognizable image.
    """
    try:
        with Image.open(path) as img:
            return {
                "width": img.width,
                "height": img.height,
                "format": img.format or "unknown",
                "mode": img.mode or "unknown",
            }
    except (UnidentifiedImageError, OSError) as e:
        raise ConversionError(f"Pillow could not identify {path}: {e}") from e


class ImageConverter(Converter):
    type_name = "image"

    def __init__(self, vlm_client: VLMClient | None = None):
        self._vlm: VLMClient = vlm_client or ClaudeCLIVLMClient()

    def detect(self, source: str) -> bool:
        if source.startswith(("http://", "https://")):
            return False
        try:
            return Path(source).suffix.lower() in _IMAGE_EXTENSIONS
        except (TypeError, ValueError):
            return False

    def convert(self, source: str) -> str:
        path = Path(source).expanduser().resolve()
        if not path.exists():
            raise ConversionError(f"image not found: {path}")

        meta = _read_image_metadata(path)
        raw_bytes = path.read_bytes()

        try:
            description = self._vlm.describe(str(path), _DESCRIPTION_PROMPT)
        except VLMError as e:
            raise ConversionError(f"VLM failed on {path}: {e}") from e

        body = description.rstrip("\n") + "\n"

        digest = hashlib.sha256(raw_bytes).hexdigest()[:12]
        canonical_id = f"image-{_today_str()}-{digest}"

        sidecar_dir = paths.raw_dir_for("image")
        sidecar_dir.mkdir(parents=True, exist_ok=True)
        sidecar_target = sidecar_dir / f"{canonical_id}{path.suffix.lower()}"
        if not sidecar_target.exists():
            shutil.copy2(path, sidecar_target)

        front: dict = {
            "id": canonical_id,
            "type": "image",
            "title": path.stem,
            "url": "",
            "authors": [],
            "ingested_at": _now_iso(),
            "content_hash": validator.compute_content_hash(body),
            "source_path": str(sidecar_target.relative_to(paths.knowledge_root())),
            "domains": [],
            "nlm_corpus_ids": [],
            "wiki_pages": [],
            "meta": {
                "width": meta["width"],
                "height": meta["height"],
                "format": meta["format"],
                "mode": meta["mode"],
                "original_filename": path.name,
                "extraction_tool": "Pillow + claude-vision",
            },
        }
        return fm.serialize(front, body)
