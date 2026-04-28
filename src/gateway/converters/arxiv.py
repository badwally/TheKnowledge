"""arXiv converter: URL or arXiv ID → canonical markdown with abstract.

Uses the public arXiv API (Atom feed) for single-paper lookups. No auth.
Body is the abstract; full PDF text fetch is out of scope here (use the
PDF converter on a downloaded sidecar instead).
"""

from __future__ import annotations

from datetime import datetime, timezone
import re
from xml.etree import ElementTree as ET

import requests

from gateway import frontmatter as fm
from gateway import validator
from gateway.converters.base import ConversionError, Converter


_ARXIV_URL_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})(?:v\d+)?")
_ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def extract_arxiv_id(source: str) -> str | None:
    match = _ARXIV_URL_RE.search(source)
    return match.group(1) if match else None


def _fetch_metadata(arxiv_id: str) -> dict:
    """Hit `export.arxiv.org/api/query?id_list=<id>` and return parsed metadata."""
    response = requests.get(
        "http://export.arxiv.org/api/query",
        params={"id_list": arxiv_id, "max_results": 1},
        timeout=15,
    )
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

    return {
        "title": (title_el.text or "").strip() if title_el is not None else "",
        "abstract": (summary_el.text or "").strip() if summary_el is not None else "",
        "published_at": (published_el.text or "")[:10] if published_el is not None else "",
        "authors": [a for a in authors if a],
        "categories": [c for c in categories if c],
        "doi": doi or "",
    }


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class ArxivConverter(Converter):
    type_name = "arxiv"

    def detect(self, source: str) -> bool:
        if not source.startswith(("http://", "https://")):
            return False
        return extract_arxiv_id(source) is not None

    def convert(self, source: str) -> str:
        arxiv_id = extract_arxiv_id(source)
        if arxiv_id is None:
            raise ConversionError(f"could not extract an arxiv id from {source!r}")

        meta = _fetch_metadata(arxiv_id)
        if not meta["abstract"]:
            raise ConversionError(f"arxiv {arxiv_id} returned no abstract")

        body = (meta["abstract"] + "\n").rstrip("\n") + "\n"
        front = {
            "id": f"arxiv-{arxiv_id}",
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
                "abstract_only": True,
            },
        }
        if meta["published_at"]:
            front["published_at"] = meta["published_at"]
        return fm.serialize(front, body)
