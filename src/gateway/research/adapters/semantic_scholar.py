"""Semantic Scholar search adapter for `wiki research`.

Wraps the S2 Academic Graph API at `api.semanticscholar.org/graph/v1/`.
225M papers across all fields, 2.8B citation edges, pre-computed SPECTER
embeddings, TLDRs, and citation-intent classification.

Auth: reads `S2_API_KEY` from env. Free to obtain at
  https://www.semanticscholar.org/product/api#Partner-Form
Without a key the API works but at lower rate limits.

Unique capabilities no other adapter provides:
- Cross-disciplinary search (economics, business, law, education, etc.)
- Citation graph traversal (`citations_of`, `references_of`)
- TLDRs and influential-citation flags in candidate metadata

Source-type routing: when an S2 result has an arXiv or PubMed ID, the
candidate's `source_type` and `url` point at the native source so the
existing converter handles materialization. Papers with only a DOI or
no external ID fall through to `web` type with the S2 or DOI URL.
"""

from __future__ import annotations

import os
import threading
import time
from typing import Any

import requests

from gateway.research.adapters.base import (
    AdapterError,
    CandidateItem,
    SearchAdapter,
)


_BASE_URL = "https://api.semanticscholar.org/graph/v1"
_TIMEOUT_SECONDS = 30

_MIN_INTERVAL_SECONDS = 1.1
_MAX_RETRIES_ON_429 = 4
_BACKOFF_BASE_SECONDS = 2.0
_rate_lock = threading.Lock()
_last_call_at: list[float] = [0.0]


def _throttle() -> None:
    with _rate_lock:
        elapsed = time.monotonic() - _last_call_at[0]
        if elapsed < _MIN_INTERVAL_SECONDS:
            time.sleep(_MIN_INTERVAL_SECONDS - elapsed)
        _last_call_at[0] = time.monotonic()

_SEARCH_FIELDS = ",".join([
    "paperId",
    "externalIds",
    "title",
    "abstract",
    "authors",
    "year",
    "citationCount",
    "influentialCitationCount",
    "tldr",
    "fieldsOfStudy",
    "publicationTypes",
    "publicationDate",
])

_CITATION_FIELDS = ",".join([
    "paperId",
    "externalIds",
    "title",
    "abstract",
    "authors",
    "year",
    "citationCount",
    "influentialCitationCount",
    "fieldsOfStudy",
])


def _headers() -> dict[str, str]:
    key = os.environ.get("S2_API_KEY", "")
    h: dict[str, str] = {"Accept": "application/json"}
    if key:
        h["x-api-key"] = key
    return h


def _get(path: str, params: dict[str, Any] | None = None) -> dict:
    url = f"{_BASE_URL}{path}"
    last_429: Exception | None = None
    for attempt in range(_MAX_RETRIES_ON_429 + 1):
        _throttle()
        try:
            resp = requests.get(url, params=params, headers=_headers(), timeout=_TIMEOUT_SECONDS)
        except requests.RequestException as e:
            raise AdapterError(f"S2 API request failed: {e}") from e
        if resp.status_code == 429:
            retry_after_header = resp.headers.get("Retry-After")
            try:
                retry_after = float(retry_after_header) if retry_after_header else 0.0
            except (TypeError, ValueError):
                retry_after = 0.0
            backoff = max(retry_after, _BACKOFF_BASE_SECONDS * (2 ** attempt))
            last_429 = AdapterError(
                f"S2 API rate limit (429) on attempt {attempt + 1}/{_MAX_RETRIES_ON_429 + 1}; backing off {backoff:.1f}s"
            )
            if attempt < _MAX_RETRIES_ON_429:
                time.sleep(backoff)
                continue
            raise AdapterError("S2 API rate limit exceeded after retries; set S2_API_KEY for higher limits") from last_429
        if resp.status_code != 200:
            raise AdapterError(f"S2 API returned HTTP {resp.status_code}: {resp.text[:300]}")
        return resp.json()
    raise AdapterError("S2 API rate limit exceeded after retries") from last_429


def _truncate(text: str, max_length: int = 1000) -> str:
    if not text:
        return ""
    text = " ".join(text.split())
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."


def _route_source(external_ids: dict) -> tuple[str, str, str]:
    """Determine (source_type, url, item_id) from S2's externalIds map.

    Prefers the most specific native source so existing converters handle
    materialization. Falls back to DOI → S2 URL.
    """
    arxiv_id = external_ids.get("ArXiv")
    if arxiv_id:
        return "arxiv", f"https://arxiv.org/abs/{arxiv_id}", f"arxiv:{arxiv_id}"

    pmid = external_ids.get("PubMed")
    if pmid:
        return "pubmed", f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", f"pubmed:{pmid}"

    doi = external_ids.get("DOI")
    if doi:
        return "web", f"https://doi.org/{doi}", f"doi:{doi}"

    s2_id = external_ids.get("CorpusId")
    if s2_id:
        return "web", f"https://www.semanticscholar.org/paper/{s2_id}", f"s2:{s2_id}"

    return "web", "", ""


def _paper_to_candidate(paper: dict) -> CandidateItem | None:
    """Convert an S2 API paper object to a CandidateItem."""
    if not paper or not paper.get("title"):
        return None

    external_ids = paper.get("externalIds") or {}
    source_type, url, item_id = _route_source(external_ids)
    if not url:
        return None

    authors = [
        a.get("name", "")
        for a in (paper.get("authors") or [])
        if a.get("name")
    ]

    tldr = paper.get("tldr") or {}
    tldr_text = tldr.get("text", "") if isinstance(tldr, dict) else ""
    abstract = paper.get("abstract") or ""
    description = tldr_text or _truncate(abstract)

    pub_date = paper.get("publicationDate")
    if not pub_date and paper.get("year"):
        pub_date = str(paper["year"])

    pub_types = paper.get("publicationTypes") or []
    content_type = pub_types[0] if pub_types else "paper"

    return CandidateItem(
        item_id=item_id,
        source_type=source_type,
        url=url,
        title=" ".join((paper.get("title") or "").split()),
        authors=authors,
        publish_date=pub_date,
        description=description,
        content_type=content_type,
        source_metadata={
            "s2_paper_id": paper.get("paperId"),
            "s2_corpus_id": external_ids.get("CorpusId"),
            "external_ids": external_ids,
            "citation_count": paper.get("citationCount"),
            "influential_citation_count": paper.get("influentialCitationCount"),
            "fields_of_study": paper.get("fieldsOfStudy") or [],
            "tldr": tldr_text,
        },
    )


class SemanticScholarAdapter:
    """`SearchAdapter` for the Semantic Scholar Academic Graph."""

    name = "semantic_scholar"

    def search(
        self,
        query: str,
        *,
        filter_hints: dict | None = None,
        max_results: int = 50,
    ) -> list[CandidateItem]:
        hints = filter_hints or {}
        params: dict[str, Any] = {
            "query": query,
            "fields": _SEARCH_FIELDS,
            "limit": min(max_results, 100),
        }
        fos = hints.get("fields_of_study")
        if fos:
            params["fieldsOfStudy"] = ",".join(fos) if isinstance(fos, list) else fos

        year = hints.get("year")
        if year:
            params["year"] = year

        pub_types = hints.get("publication_types")
        if pub_types:
            params["publicationTypes"] = (
                ",".join(pub_types) if isinstance(pub_types, list) else pub_types
            )

        data = _get("/paper/search", params)
        papers = data.get("data") or []
        candidates = []
        for p in papers:
            c = _paper_to_candidate(p)
            if c:
                candidates.append(c)
        return candidates[:max_results]

    # --- citation graph (not part of SearchAdapter protocol) ----------------

    def citations_of(
        self,
        paper_id: str,
        *,
        max_results: int = 100,
    ) -> list[CandidateItem]:
        """Papers that cite `paper_id` (S2 ID, DOI, ArXiv:id, etc.)."""
        data = _get(
            f"/paper/{paper_id}/citations",
            {"fields": _CITATION_FIELDS, "limit": min(max_results, 1000)},
        )
        candidates = []
        for edge in data.get("data") or []:
            citing = edge.get("citingPaper")
            if citing:
                c = _paper_to_candidate(citing)
                if c:
                    candidates.append(c)
        return candidates[:max_results]

    def references_of(
        self,
        paper_id: str,
        *,
        max_results: int = 100,
    ) -> list[CandidateItem]:
        """Papers that `paper_id` cites."""
        data = _get(
            f"/paper/{paper_id}/references",
            {"fields": _CITATION_FIELDS, "limit": min(max_results, 1000)},
        )
        candidates = []
        for edge in data.get("data") or []:
            cited = edge.get("citedPaper")
            if cited:
                c = _paper_to_candidate(cited)
                if c:
                    candidates.append(c)
        return candidates[:max_results]


_: SearchAdapter = SemanticScholarAdapter()
