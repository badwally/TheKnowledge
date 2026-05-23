"""arXiv search adapter for `wiki research`.

Hits the public arXiv API (Atom feed) at `export.arxiv.org/api/query`,
parses entries with the stdlib XML parser (avoids a feedparser dep —
the existing `gateway.converters.arxiv` module follows the same
pattern), and returns `CandidateItem`s.

Ported from `~/code/research-notebook/src/search/arxiv.py`. The
search-side adapter mirrors the per-paper converter's parsing logic so
the same fields (arxiv_id, categories, doi, primary_category) populate
`source_metadata`. Pagination, rate-limiting, and category-filter
support are kept; `categories` and `sort_by` are read from
`filter_hints` when supplied.
"""

from __future__ import annotations

import time
from xml.etree import ElementTree as ET

import requests

from gateway.research.adapters.base import (
    AdapterError,
    CandidateItem,
    SearchAdapter,
)


ARXIV_API_URL = "http://export.arxiv.org/api/query"
_ARXIV_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}
_VALID_SORTS = {"relevance", "lastUpdatedDate", "submittedDate"}

# 429-aware retry. Mirrors the `semantic_scholar` adapter pattern (commit
# 1dd03ff). arXiv's published rate limit is ~1 request per 3 seconds; the
# orchestrator's parallel fan-out routinely trips it, so we back off
# (honoring Retry-After when present) and retry rather than failing hard.
_MAX_RETRIES_ON_429 = 4
_BACKOFF_BASE_SECONDS = 3.0


def _build_query(search_terms: str, categories: list[str] | None) -> str:
    """Build an arXiv API query string.

    Combines free-text terms (searched against title + abstract via
    `all:`) with optional category filters using arXiv query syntax.
    """
    query = f"all:{search_terms}"
    if categories:
        cat_query = " OR ".join(f"cat:{cat}" for cat in categories)
        query = f"({query}) AND ({cat_query})"
    return query


def _fetch_feed(
    query: str,
    *,
    max_results: int,
    sort_by: str,
    start: int = 0,
) -> str:
    """Hit the arXiv API and return the raw Atom XML body.

    Isolated so tests can monkeypatch a canned response without going
    over the network.
    """
    sort_param = sort_by if sort_by in _VALID_SORTS else "relevance"
    params = {
        "search_query": query,
        "start": start,
        # arXiv caps a single response page at 100 entries.
        "max_results": min(max_results, 100),
        "sortBy": sort_param,
        "sortOrder": "descending",
    }
    last_429: Exception | None = None
    for attempt in range(_MAX_RETRIES_ON_429 + 1):
        try:
            response = requests.get(ARXIV_API_URL, params=params, timeout=30)
        except requests.RequestException as exc:  # network-level failure
            raise AdapterError(f"arxiv API request failed: {exc}") from exc
        if response.status_code == 429:
            retry_after_header = response.headers.get("Retry-After")
            try:
                retry_after = float(retry_after_header) if retry_after_header else 0.0
            except (TypeError, ValueError):
                retry_after = 0.0
            backoff = max(retry_after, _BACKOFF_BASE_SECONDS * (2 ** attempt))
            last_429 = AdapterError(
                f"arxiv API returned HTTP 429 on attempt "
                f"{attempt + 1}/{_MAX_RETRIES_ON_429 + 1}; backing off {backoff:.1f}s"
            )
            if attempt < _MAX_RETRIES_ON_429:
                time.sleep(backoff)
                continue
            raise AdapterError(
                "arxiv API returned HTTP 429 after retries exhausted"
            ) from last_429
        if response.status_code != 200:
            raise AdapterError(f"arxiv API returned HTTP {response.status_code}")
        return response.text
    raise AdapterError("arxiv API returned HTTP 429 after retries exhausted") from last_429


def _parse_entries(xml_text: str) -> list[dict]:
    """Parse the Atom feed into a list of normalized entry dicts.

    Returns the same shape `feedparser` would give us for the fields we
    actually consume — keeps the downstream mapping logic identical to
    research-notebook's port.
    """
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        raise AdapterError(f"could not parse arxiv response: {exc}") from exc

    entries: list[dict] = []
    for entry in root.findall("atom:entry", _ARXIV_NS):
        entry_id = (entry.findtext("atom:id", default="", namespaces=_ARXIV_NS) or "").strip()
        if not entry_id:
            continue
        title = (entry.findtext("atom:title", default="", namespaces=_ARXIV_NS) or "").strip()
        summary = (entry.findtext("atom:summary", default="", namespaces=_ARXIV_NS) or "").strip()
        published = (entry.findtext("atom:published", default="", namespaces=_ARXIV_NS) or "").strip()

        authors: list[dict] = []
        for author_el in entry.findall("atom:author", _ARXIV_NS):
            name = (author_el.findtext("atom:name", default="", namespaces=_ARXIV_NS) or "").strip()
            affiliation = author_el.findtext("arxiv:affiliation", default=None, namespaces=_ARXIV_NS)
            if name:
                authors.append({"name": name, "affiliation": affiliation})

        categories: list[str] = []
        for cat_el in entry.findall("atom:category", _ARXIV_NS):
            term = cat_el.attrib.get("term")
            if term:
                categories.append(term)

        primary_el = entry.find("arxiv:primary_category", _ARXIV_NS)
        primary_category = primary_el.attrib.get("term", "") if primary_el is not None else ""

        comment = entry.findtext("arxiv:comment", default=None, namespaces=_ARXIV_NS)
        journal_ref = entry.findtext("arxiv:journal_ref", default=None, namespaces=_ARXIV_NS)
        doi = entry.findtext("arxiv:doi", default=None, namespaces=_ARXIV_NS)

        entries.append(
            {
                "id": entry_id,
                "title": title,
                "summary": summary,
                "published": published,
                "authors": authors,
                "categories": categories,
                "primary_category": primary_category,
                "comment": comment,
                "journal_ref": journal_ref,
                "doi": doi,
            }
        )
    return entries


def _truncate(text: str, max_length: int = 1000) -> str:
    if not text:
        return ""
    text = " ".join(text.split())
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."


def _entry_to_candidate(entry: dict) -> CandidateItem:
    """Map a parsed Atom entry to a `CandidateItem`."""
    raw_id = entry["id"].split("/abs/")[-1]
    arxiv_id_clean = raw_id.split("v")[0] if "v" in raw_id else raw_id
    abs_url = f"https://arxiv.org/abs/{arxiv_id_clean}"
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id_clean}.pdf"

    journal_ref = entry.get("journal_ref")
    content_type = "journal_article" if journal_ref else "preprint"
    author_names = [a["name"] for a in entry.get("authors", []) if a.get("name")]

    return CandidateItem(
        item_id=f"arxiv:{arxiv_id_clean}",
        source_type="arxiv",
        url=abs_url,
        title=" ".join((entry.get("title") or "").split()),
        authors=author_names,
        publish_date=(entry.get("published") or None),
        description=_truncate(entry.get("summary", ""), 1000),
        content_type=content_type,
        source_metadata={
            "arxiv_id": arxiv_id_clean,
            "categories": entry.get("categories", []),
            "primary_category": entry.get("primary_category", ""),
            "pdf_url": pdf_url,
            "comment": entry.get("comment"),
            "journal_ref": journal_ref,
            "doi": entry.get("doi"),
            "authors_with_affiliation": entry.get("authors", []),
        },
    )


class ArxivAdapter:
    """`SearchAdapter` for arXiv preprints."""

    name = "arxiv"

    def search(
        self,
        query: str,
        *,
        filter_hints: dict | None = None,
        max_results: int = 50,
    ) -> list[CandidateItem]:
        hints = filter_hints or {}
        categories = hints.get("categories") or hints.get("arxiv_categories")
        sort_by = hints.get("sort_by", "relevance")

        api_query = _build_query(query, categories)
        xml_text = _fetch_feed(api_query, max_results=max_results, sort_by=sort_by)
        entries = _parse_entries(xml_text)
        candidates = [_entry_to_candidate(e) for e in entries]
        return candidates[:max_results]


# Type-checker assurance the class satisfies the protocol.
_: SearchAdapter = ArxivAdapter()
