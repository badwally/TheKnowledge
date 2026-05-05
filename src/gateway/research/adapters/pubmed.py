"""PubMed search adapter for `wiki research`.

Wraps NCBI E-utilities (`esearch` + `efetch`) for query-driven retrieval.
The companion converter at `gateway.converters.pubmed` is responsible for
materializing a single PubMed URL into canonical markdown; this adapter's
job is the *discovery* step that produces a list of candidate PMIDs (and
their metadata) for the orchestrator's semantic filter.

NCBI honors a per-IP rate limit (3 req/s without a key, 10 req/s with one).
We honor the `NCBI_API_KEY` env var for the higher tier and additionally
send `KNOWLEDGE_NCBI_EMAIL` if set, matching the converter's contract.
"""

from __future__ import annotations

import os
from typing import Any
from xml.etree import ElementTree as ET

import requests

from gateway.research.adapters.base import AdapterError, CandidateItem


_ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
_EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
_TIMEOUT_SECONDS = 15


_MONTH_MAP = {
    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
    "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
    "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
}


def _normalize_month(value: str) -> str:
    if value.isdigit():
        try:
            return f"{int(value):02d}"
        except ValueError:
            return "01"
    return _MONTH_MAP.get(value[:3], "01")


def _common_params() -> dict[str, str]:
    """Shared E-utilities params: API key + email if configured."""
    params: dict[str, str] = {}
    api_key = os.environ.get("NCBI_API_KEY", "").strip()
    if api_key:
        params["api_key"] = api_key
    email = os.environ.get("KNOWLEDGE_NCBI_EMAIL", "").strip()
    if email:
        params["email"] = email
    return params


def _esearch(query: str, max_results: int) -> list[str]:
    """Resolve a free-text query to a list of PMIDs (capped)."""
    params: dict[str, Any] = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": str(max(1, max_results)),
    }
    params.update(_common_params())
    try:
        response = requests.get(_ESEARCH_URL, params=params, timeout=_TIMEOUT_SECONDS)
    except requests.RequestException as e:
        raise AdapterError(f"PubMed esearch request failed: {e}") from e

    if response.status_code != 200:
        raise AdapterError(
            f"PubMed esearch returned HTTP {response.status_code}"
        )

    try:
        payload = response.json()
    except ValueError as e:
        raise AdapterError(f"PubMed esearch returned non-JSON body: {e}") from e

    ids = (
        payload.get("esearchresult", {}).get("idlist", [])
        if isinstance(payload, dict)
        else []
    )
    if not isinstance(ids, list):
        return []
    return [str(pmid) for pmid in ids if pmid]


def _efetch(pmids: list[str]) -> list[CandidateItem]:
    """Fetch metadata for a batch of PMIDs and return CandidateItems."""
    if not pmids:
        return []

    params: dict[str, Any] = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "rettype": "abstract",
        "retmode": "xml",
    }
    params.update(_common_params())
    try:
        response = requests.get(_EFETCH_URL, params=params, timeout=_TIMEOUT_SECONDS)
    except requests.RequestException as e:
        raise AdapterError(f"PubMed efetch request failed: {e}") from e

    if response.status_code != 200:
        raise AdapterError(
            f"PubMed efetch returned HTTP {response.status_code}"
        )

    try:
        root = ET.fromstring(response.text)
    except ET.ParseError as e:
        raise AdapterError(f"could not parse PubMed XML response: {e}") from e

    items: list[CandidateItem] = []
    for article in root.findall(".//PubmedArticle"):
        item = _parse_article(article)
        if item is not None:
            items.append(item)
    return items


def _parse_article(article: ET.Element) -> CandidateItem | None:
    """Build a CandidateItem from a PubmedArticle XML element."""
    pmid = (article.findtext(".//PMID") or "").strip()
    if not pmid:
        return None

    title = (article.findtext(".//ArticleTitle") or "").strip()
    journal = (article.findtext(".//Journal/Title") or "").strip()

    pub_year = (article.findtext(".//PubDate/Year") or "").strip()
    pub_month = (article.findtext(".//PubDate/Month") or "").strip()
    pub_day = (article.findtext(".//PubDate/Day") or "").strip()
    publish_date: str | None = None
    if pub_year:
        publish_date = pub_year
        if pub_month:
            publish_date = f"{pub_year}-{_normalize_month(pub_month)}"
            if pub_day:
                try:
                    publish_date = f"{publish_date}-{int(pub_day):02d}"
                except ValueError:
                    pass

    doi = ""
    for el in article.findall(".//ArticleId"):
        if (el.attrib.get("IdType") or "").lower() == "doi":
            doi = (el.text or "").strip()
            break

    mesh_terms = [
        (mh.findtext("DescriptorName") or "").strip()
        for mh in article.findall(".//MeshHeading")
    ]
    mesh_terms = [m for m in mesh_terms if m]

    authors: list[str] = []
    for author in article.findall(".//Author"):
        last = (author.findtext("LastName") or "").strip()
        first = (
            author.findtext("ForeName")
            or author.findtext("Initials")
            or ""
        ).strip()
        if last or first:
            authors.append(f"{first} {last}".strip())

    abstract_parts: list[str] = []
    for abs_el in article.findall(".//Abstract/AbstractText"):
        label = abs_el.attrib.get("Label", "")
        text = (abs_el.text or "").strip()
        if not text:
            continue
        abstract_parts.append(f"{label}. {text}" if label else text)
    description = "\n\n".join(abstract_parts)

    return CandidateItem(
        item_id=pmid,
        source_type="pubmed",
        url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        title=title or f"PMID:{pmid}",
        authors=authors,
        publish_date=publish_date,
        description=description,
        content_type="article",
        source_metadata={
            "pmid": pmid,
            "journal": journal,
            "doi": doi,
            "mesh_terms": mesh_terms,
        },
    )


class PubMedAdapter:
    """Query-driven discovery against PubMed E-utilities.

    The adapter is safe to instantiate without credentials. Network
    failures and non-200 responses surface as `AdapterError` so the
    orchestrator can downgrade them to per-adapter warnings.
    """

    name = "pubmed"

    def search(
        self,
        query: str,
        *,
        filter_hints: dict | None = None,
        max_results: int = 50,
    ) -> list[CandidateItem]:
        if not query or not query.strip():
            return []
        cap = max(1, int(max_results))
        pmids = _esearch(query.strip(), cap)
        if not pmids:
            return []
        # esearch already honors retmax, but cap defensively.
        pmids = pmids[:cap]
        return _efetch(pmids)


__all__ = ["PubMedAdapter"]
