"""PDF converter: local PDF path → canonical markdown with extracted text.

Uses pdfplumber for text extraction. Preserves the original PDF as a
sidecar at `raw/pdf/<id>.pdf` so the original is always retrievable.

Canonical ID per WIKI § 6.1: `pdf-<author>-<year>-<short>` if metadata
allows, else `pdf-<sha256-prefix-12>` fallback.
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import re
import shutil
from pathlib import Path

import pdfplumber

from gateway import frontmatter as fm
from gateway import paths, validator
from gateway.converters.base import ConversionError, Converter


_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def _slugify_short(value: str, max_words: int = 4) -> str:
    cleaned = _NON_ALNUM.sub("-", value.lower()).strip("-")
    parts = [p for p in cleaned.split("-") if p]
    return "-".join(parts[:max_words])


def _hash_id_from_bytes(data: bytes, max_chars: int = 12) -> str:
    digest = hashlib.sha256(data).hexdigest()[:max_chars]
    return f"pdf-{digest}"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _extract_pdf(path: Path) -> tuple[str, dict]:
    """Return (body_text, pdf_metadata) using pdfplumber."""
    text_parts: list[str] = []
    metadata: dict = {}
    try:
        with pdfplumber.open(str(path)) as pdf:
            metadata = dict(pdf.metadata or {})
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                if page_text.strip():
                    text_parts.append(page_text.strip())
    except Exception as e:
        raise ConversionError(f"pdfplumber failed on {path}: {e}") from e

    body = "\n\n".join(text_parts)
    return body, metadata


def _build_id(metadata: dict, raw_bytes: bytes) -> str:
    """Prefer author-year-short slug; fall back to hash."""
    author = (metadata.get("Author") or "").strip()
    title = (metadata.get("Title") or "").strip()
    creation = (metadata.get("CreationDate") or "")
    year = ""
    year_match = re.search(r"(\d{4})", str(creation))
    if year_match:
        year = year_match.group(1)
    if author and year and title:
        author_slug = _slugify_short(author.split(",")[0], max_words=2)
        title_slug = _slugify_short(title, max_words=3)
        if author_slug and title_slug:
            return f"pdf-{author_slug}-{year}-{title_slug}"
    return _hash_id_from_bytes(raw_bytes)


class PDFConverter(Converter):
    type_name = "pdf"

    def detect(self, source: str) -> bool:
        if source.startswith(("http://", "https://")):
            return False
        try:
            return Path(source).suffix.lower() == ".pdf"
        except (TypeError, ValueError):
            return False

    def convert(self, source: str) -> str:
        path = Path(source).expanduser().resolve()
        if not path.exists():
            raise ConversionError(f"PDF not found: {path}")

        raw_bytes = path.read_bytes()
        body, metadata = _extract_pdf(path)
        if not body.strip():
            raise ConversionError(f"no extractable text in {path}")
        body = body.rstrip("\n") + "\n"

        canonical_id = _build_id(metadata, raw_bytes)

        # Persist the PDF as a sidecar next to the canonical raw markdown
        sidecar_dir = paths.raw_dir_for("pdf")
        sidecar_dir.mkdir(parents=True, exist_ok=True)
        sidecar_target = sidecar_dir / f"{canonical_id}.pdf"
        if not sidecar_target.exists():
            shutil.copy2(path, sidecar_target)

        front = {
            "id": canonical_id,
            "type": "pdf",
            "title": (metadata.get("Title") or path.stem).strip(),
            "url": "",
            "authors": _split_authors(metadata.get("Author") or ""),
            "ingested_at": _now_iso(),
            "content_hash": validator.compute_content_hash(body),
            "source_path": str(sidecar_target.relative_to(paths.knowledge_root())),
            "domains": [],
            "nlm_corpus_ids": [],
            "wiki_pages": [],
            "meta": {
                "page_count": len(body.split("\n\n")),
                "extraction_tool": "pdfplumber",
                "pdf_metadata_subject": metadata.get("Subject", ""),
                "pdf_metadata_keywords": metadata.get("Keywords", ""),
                "original_path": str(path),
            },
        }
        creation = metadata.get("CreationDate") or ""
        if isinstance(creation, str):
            year_match = re.search(r"(\d{4})", creation)
            if year_match:
                front["published_at"] = year_match.group(1)
        return fm.serialize(front, body)


def _split_authors(value: str) -> list[str]:
    if not value:
        return []
    parts = [p.strip() for p in re.split(r"[,;]| and ", value)]
    return [p for p in parts if p]
