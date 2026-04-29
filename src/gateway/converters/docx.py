"""Word document converter: .docx → canonical markdown.

Uses python-docx to extract paragraphs (preserving heading-level styles),
tables, and core document properties (author, title, created date).
Original .docx file preserved as a sidecar at raw/docx/<id>.docx.

Canonical ID per WIKI § 6.1: docx-<author>-<year>-<short> if metadata
allows, else docx-<sha256-prefix-12> fallback.
"""

from __future__ import annotations

import hashlib
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

from docx import Document
from docx.opc.exceptions import PackageNotFoundError

from gateway import frontmatter as fm
from gateway import paths, validator
from gateway.converters.base import ConversionError, Converter

_NON_ALNUM = re.compile(r"[^a-z0-9]+")
_HEADING_RE = re.compile(r"^heading\s*(\d+)$", re.IGNORECASE)


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _slugify_short(value: str, max_words: int = 4) -> str:
    cleaned = _NON_ALNUM.sub("-", value.lower()).strip("-")
    parts = [p for p in cleaned.split("-") if p]
    return "-".join(parts[:max_words])


def _hash_id_from_bytes(data: bytes, max_chars: int = 12) -> str:
    digest = hashlib.sha256(data).hexdigest()[:max_chars]
    return f"docx-{digest}"


def _build_id(author: str, title: str, year: str, raw_bytes: bytes) -> str:
    if author and year and title:
        author_slug = _slugify_short(author.split(",")[0], max_words=2)
        title_slug = _slugify_short(title, max_words=3)
        if author_slug and title_slug:
            return f"docx-{author_slug}-{year}-{title_slug}"
    return _hash_id_from_bytes(raw_bytes)


def _heading_level(style_name: str) -> int | None:
    """Return heading level (1-6) for a paragraph style, or None for body."""
    if not style_name:
        return None
    m = _HEADING_RE.match(style_name.strip())
    if not m:
        return None
    level = int(m.group(1))
    return level if 1 <= level <= 6 else None


def _md_escape_cell(value: str) -> str:
    return (
        str(value)
        .replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("\r", " ")
        .replace("\n", " ")
    )


def _table_to_markdown(table) -> str:
    """Render a python-docx Table as a markdown table."""
    rows: list[list[str]] = []
    for row in table.rows:
        rows.append([cell.text or "" for cell in row.cells])
    if not rows:
        return ""
    headers = rows[0]
    body_rows = rows[1:]
    width = len(headers)
    sep = ["---"] * width
    out = ["| " + " | ".join(_md_escape_cell(h) for h in headers) + " |",
           "| " + " | ".join(sep) + " |"]
    for r in body_rows:
        padded = list(r[:width])
        while len(padded) < width:
            padded.append("")
        out.append("| " + " | ".join(_md_escape_cell(c) for c in padded) + " |")
    return "\n".join(out)


def _extract_body(doc) -> tuple[str, int, int]:
    """Walk the document body in order, rendering paragraphs and tables.

    Returns (markdown_body, paragraph_count, table_count).
    """
    parts: list[str] = []
    para_count = 0
    table_count = 0

    # Walk the document body in order. python-docx's `body` element
    # yields paragraphs and tables in document order via `iter_inner_content`.
    for child in doc.iter_inner_content():
        # Paragraph
        if hasattr(child, "style") and hasattr(child, "text"):
            text = (child.text or "").strip()
            if not text:
                continue
            para_count += 1
            level = _heading_level(child.style.name if child.style else "")
            if level:
                parts.append(f"{'#' * level} {text}")
            else:
                parts.append(text)
        # Table
        elif hasattr(child, "rows"):
            md = _table_to_markdown(child)
            if md:
                table_count += 1
                parts.append(md)
    body = "\n\n".join(parts)
    if body:
        body = body.rstrip("\n") + "\n"
    return body, para_count, table_count


class DocxConverter(Converter):
    type_name = "docx"

    def detect(self, source: str) -> bool:
        if source.startswith(("http://", "https://")):
            return False
        try:
            return Path(source).suffix.lower() == ".docx"
        except (TypeError, ValueError):
            return False

    def convert(self, source: str) -> str:
        path = Path(source).expanduser().resolve()
        if not path.exists():
            raise ConversionError(f"docx not found: {path}")

        raw_bytes = path.read_bytes()
        try:
            doc = Document(str(path))
        except (PackageNotFoundError, ValueError, KeyError) as e:
            raise ConversionError(f"python-docx failed on {path}: {e}") from e

        body, para_count, table_count = _extract_body(doc)
        if not body.strip():
            raise ConversionError(f"no extractable content in {path}")

        cp = doc.core_properties
        author = (cp.author or "").strip()
        title = (cp.title or path.stem).strip()
        created = cp.created
        year = created.strftime("%Y") if isinstance(created, datetime) else ""

        canonical_id = _build_id(author, cp.title or "", year, raw_bytes)

        sidecar_dir = paths.raw_dir_for("docx")
        sidecar_dir.mkdir(parents=True, exist_ok=True)
        sidecar_target = sidecar_dir / f"{canonical_id}.docx"
        if not sidecar_target.exists():
            shutil.copy2(path, sidecar_target)

        front: dict = {
            "id": canonical_id,
            "type": "docx",
            "title": title,
            "url": "",
            "authors": _split_authors(author),
            "ingested_at": _now_iso(),
            "content_hash": validator.compute_content_hash(body),
            "source_path": str(sidecar_target.relative_to(paths.knowledge_root())),
            "domains": [],
            "nlm_corpus_ids": [],
            "wiki_pages": [],
            "meta": {
                "paragraph_count": para_count,
                "table_count": table_count,
                "extraction_tool": "python-docx",
                "original_filename": path.name,
                "subject": (cp.subject or "").strip(),
            },
        }
        if year:
            front["published_at"] = year
        return fm.serialize(front, body)


def _split_authors(value: str) -> list[str]:
    if not value:
        return []
    parts = [p.strip() for p in re.split(r"[,;]| and ", value)]
    return [p for p in parts if p]
