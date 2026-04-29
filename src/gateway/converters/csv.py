"""CSV / TSV converter: tabular file → canonical markdown with preview table.

Reads the file with the stdlib `csv` module, sniffs the dialect, renders
the first rows and columns as a markdown table for the body, and preserves
the original file as a sidecar at `raw/csv/<id>.<ext>`. The sidecar is the
canonical reference for the full data; the body is a preview only.

Canonical ID per WIKI § 6.1: `csv-<sha256-prefix-12>` (content-hash based).
"""

from __future__ import annotations

import csv as csvlib
import hashlib
import shutil
from datetime import datetime, timezone
from pathlib import Path

from gateway import frontmatter as fm
from gateway import paths, validator
from gateway.converters.base import ConversionError, Converter

_PREVIEW_ROWS = 50
_PREVIEW_COLS = 20


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _read_text(path: Path) -> tuple[str, str]:
    """Return (text, encoding). Try utf-8 (with optional BOM), fall back to latin-1."""
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1", errors="replace"), "latin-1"


def _sniff_dialect(sample: str, suffix: str) -> type[csvlib.Dialect] | csvlib.Dialect:
    """Sniff the delimiter; default to excel-tab for .tsv, excel for .csv."""
    if suffix == ".tsv":
        return csvlib.excel_tab
    try:
        return csvlib.Sniffer().sniff(sample, delimiters=",\t;|")
    except csvlib.Error:
        return csvlib.excel


def _md_escape_cell(value: str) -> str:
    return (
        str(value)
        .replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("\r", " ")
        .replace("\n", " ")
    )


def _render_table(headers: list[str], rows: list[list[str]]) -> str:
    if not headers:
        return ""
    header_line = "| " + " | ".join(_md_escape_cell(h) for h in headers) + " |"
    sep_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    body_lines = []
    for row in rows:
        padded = list(row[: len(headers)])
        while len(padded) < len(headers):
            padded.append("")
        body_lines.append("| " + " | ".join(_md_escape_cell(c) for c in padded) + " |")
    return "\n".join([header_line, sep_line, *body_lines])


class CSVConverter(Converter):
    type_name = "csv"

    def detect(self, source: str) -> bool:
        if source.startswith(("http://", "https://")):
            return False
        try:
            return Path(source).suffix.lower() in (".csv", ".tsv")
        except (TypeError, ValueError):
            return False

    def convert(self, source: str) -> str:
        path = Path(source).expanduser().resolve()
        if not path.exists():
            raise ConversionError(f"CSV not found: {path}")

        text, encoding = _read_text(path)
        sample = text[:8192]
        dialect = _sniff_dialect(sample, path.suffix.lower())

        reader = csvlib.reader(text.splitlines(), dialect=dialect)
        all_rows = [r for r in reader]
        if not all_rows:
            raise ConversionError(f"empty CSV: {path}")

        headers = all_rows[0]
        data_rows = all_rows[1:]
        total_rows = len(data_rows)
        total_cols = len(headers)

        truncated_cols = total_cols > _PREVIEW_COLS
        truncated_rows = total_rows > _PREVIEW_ROWS

        display_headers = headers[:_PREVIEW_COLS]
        display_rows = data_rows[:_PREVIEW_ROWS]
        if truncated_cols:
            display_rows = [r[:_PREVIEW_COLS] for r in display_rows]

        body_parts: list[str] = [
            f"# {path.stem}",
            "",
            f"CSV with **{total_rows}** data rows × **{total_cols}** columns.",
            "",
            _render_table(display_headers, display_rows),
        ]
        if truncated_rows or truncated_cols:
            notes: list[str] = []
            if truncated_rows:
                notes.append(
                    f"{total_rows - _PREVIEW_ROWS} additional rows omitted from preview"
                )
            if truncated_cols:
                notes.append(
                    f"{total_cols - _PREVIEW_COLS} additional columns omitted from preview"
                )
            body_parts.append("")
            body_parts.append(f"_{'; '.join(notes)}. Full data in sidecar._")

        body = "\n".join(body_parts) + "\n"

        raw_bytes = path.read_bytes()
        canonical_id = f"csv-{hashlib.sha256(raw_bytes).hexdigest()[:12]}"

        sidecar_dir = paths.raw_dir_for("csv")
        sidecar_dir.mkdir(parents=True, exist_ok=True)
        sidecar_target = sidecar_dir / f"{canonical_id}{path.suffix.lower()}"
        if not sidecar_target.exists():
            shutil.copy2(path, sidecar_target)

        delimiter = getattr(dialect, "delimiter", ",")

        front = {
            "id": canonical_id,
            "type": "csv",
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
                "row_count": total_rows,
                "column_count": total_cols,
                "columns": headers[:_PREVIEW_COLS],
                "delimiter": delimiter,
                "encoding": encoding,
                "original_filename": path.name,
                "extraction_tool": "csv (stdlib)",
            },
        }
        return fm.serialize(front, body)
