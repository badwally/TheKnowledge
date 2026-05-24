"""arXiv converter: URL or arXiv ID → canonical markdown with abstract.

Uses the public arXiv API (Atom feed) for single-paper lookups. No auth.
Body is the abstract; full PDF text fetch is out of scope here (use the
PDF converter on a downloaded sidecar instead).
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re
import time
from xml.etree import ElementTree as ET

import requests

from gateway import frontmatter as fm
from gateway import paths, validator
from gateway.converters.base import ConversionError, Converter


# arXiv has two ID schemes:
#   - new-style (post-2007): YYMM.NNNNN, e.g. "2403.12345"
#   - old-style (pre-2007):  <archive>(.<class>)?/YYMMNNN, e.g. "cond-mat/0207270"
_NEW_ID = r"[0-9]{4}\.[0-9]{4,5}"
_OLD_ID = r"[a-z][a-z\-]+(?:\.[A-Z]{2})?/\d{7}"
_ARXIV_ID = rf"(?:{_NEW_ID}|{_OLD_ID})"

_ARXIV_URL_RE = re.compile(rf"arxiv\.org/(?:abs|pdf)/({_ARXIV_ID})(?:v\d+)?")
_ARXIV_SHORT_RE = re.compile(rf"^arxiv:({_ARXIV_ID})(?:v\d+)?$")
_ARXIV_BARE_RE = re.compile(rf"^({_ARXIV_ID})(?:v\d+)?$")
_ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def extract_arxiv_id(source: str) -> str | None:
    if not source:
        return None
    if (m := _ARXIV_URL_RE.search(source)):
        return m.group(1)
    if (m := _ARXIV_SHORT_RE.match(source)):
        return m.group(1)
    if (m := _ARXIV_BARE_RE.match(source)):
        return m.group(1)
    return None


# arXiv TOU: 1 request per 3 seconds, single connection, applies across all our
# machines. Both metadata fetches and PDF downloads count against the same
# budget (same arxiv.org host).
_RATE_LIMIT_SECONDS = 3.0
_last_request_at: float = 0.0


def _enforce_rate_limit() -> None:
    """Sleep if needed to respect the 3-second arXiv API rate limit."""
    global _last_request_at
    elapsed = time.monotonic() - _last_request_at
    wait = _RATE_LIMIT_SECONDS - elapsed
    if wait > 0:
        time.sleep(wait)
    _last_request_at = time.monotonic()


def _reset_rate_limit_for_tests() -> None:
    """Test-only: reset the rate-limit state to zero."""
    global _last_request_at
    _last_request_at = 0.0


def _fetch_metadata(arxiv_id: str) -> dict:
    """Hit `export.arxiv.org/api/query?id_list=<id>` and return parsed metadata."""
    _enforce_rate_limit()
    try:
        response = requests.get(
            "http://export.arxiv.org/api/query",
            params={"id_list": arxiv_id, "max_results": 1},
            timeout=15,
        )
    except requests.exceptions.RequestException as e:
        raise ConversionError(f"arxiv API network error for {arxiv_id}: {e}") from e
    if response.status_code != 200:
        raise ConversionError(f"arxiv API lookup failed: {response.status_code}")

    try:
        root = ET.fromstring(response.text)
    except ET.ParseError as e:
        raise ConversionError(f"could not parse arxiv API response: {e}") from e

    entry = root.find("atom:entry", _ARXIV_NS)
    if entry is None:
        raise ConversionError(f"no arxiv entry found for {arxiv_id}")

    title_el = entry.find("atom:title", _ARXIV_NS)
    summary_el = entry.find("atom:summary", _ARXIV_NS)
    published_el = entry.find("atom:published", _ARXIV_NS)
    authors = [a.findtext("atom:name", default="", namespaces=_ARXIV_NS) for a in entry.findall("atom:author", _ARXIV_NS)]
    categories = [c.attrib.get("term", "") for c in entry.findall("atom:category", _ARXIV_NS)]
    doi = entry.findtext("arxiv:doi", default="", namespaces=_ARXIV_NS)
    journal_ref = entry.findtext("arxiv:journal_ref", default="", namespaces=_ARXIV_NS)
    comment = entry.findtext("arxiv:comment", default="", namespaces=_ARXIV_NS)
    primary_cat_el = entry.find("arxiv:primary_category", _ARXIV_NS)
    primary_category = primary_cat_el.attrib.get("term", "") if primary_cat_el is not None else ""

    return {
        "title": (title_el.text or "").strip() if title_el is not None else "",
        "abstract": (summary_el.text or "").strip() if summary_el is not None else "",
        "published_at": (published_el.text or "")[:10] if published_el is not None else "",
        "authors": [a for a in authors if a],
        "categories": [c for c in categories if c],
        "doi": doi or "",
        "primary_category": primary_category,
        "journal_ref": (journal_ref or "").strip(),
        "comment": (comment or "").strip(),
    }


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _id_to_slug(arxiv_id: str) -> str:
    """Sanitize an arxiv id for use in filenames (old-style ids contain '/')."""
    return arxiv_id.replace("/", "-")


def _download_pdf(arxiv_id: str, target: Path) -> None:
    """Download the PDF for `arxiv_id` to `target`. Raises on HTTP failure."""
    _enforce_rate_limit()
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    try:
        response = requests.get(url, timeout=60)
    except requests.exceptions.RequestException as e:
        raise ConversionError(f"PDF download network error for {arxiv_id}: {e}") from e
    if response.status_code != 200:
        raise ConversionError(
            f"PDF download failed for {arxiv_id}: HTTP {response.status_code}"
        )
    target.write_bytes(response.content)


def _build_frontmatter(
    arxiv_id: str,
    meta: dict,
    body: str,
    *,
    abstract_only: bool,
    source_path: str | None,
) -> dict:
    front = {
        "id": f"arxiv-{_id_to_slug(arxiv_id)}",
        "type": "arxiv",
        "title": meta["title"] or f"arXiv:{arxiv_id}",
        "url": f"https://arxiv.org/abs/{arxiv_id}",
        "authors": meta["authors"],
        "ingested_at": _now_iso(),
        "content_hash": validator.compute_content_hash(body),
        "domains": [],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {
            "arxiv_id": arxiv_id,
            "categories": meta["categories"],
            "doi": meta["doi"],
            "primary_category": meta.get("primary_category", ""),
            "journal_ref": meta.get("journal_ref", ""),
            "comment": meta.get("comment", ""),
            "abstract_only": abstract_only,
        },
    }
    if meta.get("published_at"):
        front["published_at"] = meta["published_at"]
    if source_path:
        front["source_path"] = source_path
    return front


class ArxivConverter(Converter):
    type_name = "arxiv"

    def detect(self, source: str) -> bool:
        return extract_arxiv_id(source) is not None

    def convert(self, source: str) -> str:
        arxiv_id = extract_arxiv_id(source)
        if arxiv_id is None:
            raise ConversionError(f"could not extract an arxiv id from {source!r}")

        meta = _fetch_metadata(arxiv_id)
        if not meta["abstract"]:
            raise ConversionError(f"arxiv {arxiv_id} returned no abstract")

        body = meta["abstract"].rstrip("\n") + "\n"
        front = _build_frontmatter(arxiv_id, meta, body, abstract_only=True, source_path=None)
        return fm.serialize(front, body)

    def convert_with_pdf(self, source: str) -> str:
        """Like convert, but downloads the PDF and uses its full text as body.

        The PDF is saved as a sidecar at `raw/arxiv/<id>.pdf` (referenced via
        `source_path` frontmatter) so the original is always retrievable.
        """
        arxiv_id = extract_arxiv_id(source)
        if arxiv_id is None:
            raise ConversionError(f"could not extract an arxiv id from {source!r}")

        meta = _fetch_metadata(arxiv_id)

        sidecar_dir = paths.raw_dir_for("arxiv")
        sidecar_dir.mkdir(parents=True, exist_ok=True)
        sidecar_path = sidecar_dir / f"arxiv-{_id_to_slug(arxiv_id)}.pdf"
        _download_pdf(arxiv_id, sidecar_path)

        # Reuse the PDF converter's text extraction (pdfplumber under the hood).
        from gateway.converters.pdf import _extract_pdf
        body, _pdf_meta = _extract_pdf(sidecar_path)
        if not body.strip():
            raise ConversionError(f"no extractable text from PDF for arxiv {arxiv_id}")
        body = body.rstrip("\n") + "\n"

        rel_sidecar = str(sidecar_path.relative_to(paths.knowledge_root()))
        front = _build_frontmatter(
            arxiv_id, meta, body, abstract_only=False, source_path=rel_sidecar,
        )
        return fm.serialize(front, body)
