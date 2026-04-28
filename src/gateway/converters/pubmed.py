"""PubMed converter: URL or PMID URL → canonical markdown with abstract.

Uses NCBI E-utilities (efetch) to pull the abstract. No auth required for
low-volume use; NCBI requests an `email` parameter, which we send if the
KNOWLEDGE_NCBI_EMAIL env var is set.
"""

from __future__ import annotations

from datetime import datetime, timezone
import os
import re
from xml.etree import ElementTree as ET

import requests

from gateway import frontmatter as fm
from gateway import validator
from gateway.converters.base import ConversionError, Converter


_PUBMED_URL_RE = re.compile(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)")
_EUTILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def extract_pmid(source: str) -> str | None:
    match = _PUBMED_URL_RE.search(source)
    return match.group(1) if match else None


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _fetch_metadata(pmid: str) -> dict:
    params = {
        "db": "pubmed",
        "id": pmid,
        "rettype": "abstract",
        "retmode": "xml",
    }
    email = os.environ.get("KNOWLEDGE_NCBI_EMAIL", "")
    if email:
        params["email"] = email

    response = requests.get(_EUTILS_URL, params=params, timeout=15)
    if response.status_code != 200:
        raise ConversionError(f"PubMed efetch failed: {response.status_code}")

    try:
        root = ET.fromstring(response.text)
    except ET.ParseError as e:
        raise ConversionError(f"could not parse PubMed XML response: {e}") from e

    article = root.find(".//PubmedArticle")
    if article is None:
        raise ConversionError(f"no PubMed article found for PMID {pmid}")

    title = article.findtext(".//ArticleTitle") or ""
    journal = article.findtext(".//Journal/Title") or ""
    pub_year = article.findtext(".//PubDate/Year") or ""
    pub_month = article.findtext(".//PubDate/Month") or ""
    pub_day = article.findtext(".//PubDate/Day") or ""
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
        first = (author.findtext("ForeName") or author.findtext("Initials") or "").strip()
        if last or first:
            authors.append(f"{first} {last}".strip())

    abstract_parts: list[str] = []
    for abs_el in article.findall(".//Abstract/AbstractText"):
        label = abs_el.attrib.get("Label", "")
        text = (abs_el.text or "").strip()
        if not text:
            continue
        abstract_parts.append(f"**{label}.** {text}" if label else text)
    abstract = "\n\n".join(abstract_parts)

    published_at = pub_year
    if pub_year and pub_month:
        published_at = f"{pub_year}-{_normalize_month(pub_month)}"
        if pub_day:
            try:
                published_at = f"{published_at}-{int(pub_day):02d}"
            except ValueError:
                pass

    return {
        "title": title.strip(),
        "abstract": abstract,
        "journal": journal.strip(),
        "published_at": published_at,
        "doi": doi,
        "mesh_terms": mesh_terms,
        "authors": authors,
    }


_MONTH_MAP = {
    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
    "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
}


def _normalize_month(value: str) -> str:
    if value.isdigit():
        try:
            return f"{int(value):02d}"
        except ValueError:
            return "01"
    return _MONTH_MAP.get(value[:3], "01")


class PubMedConverter(Converter):
    type_name = "pubmed"

    def detect(self, source: str) -> bool:
        if not source.startswith(("http://", "https://")):
            return False
        return extract_pmid(source) is not None

    def convert(self, source: str) -> str:
        pmid = extract_pmid(source)
        if pmid is None:
            raise ConversionError(f"could not extract a PMID from {source!r}")

        meta = _fetch_metadata(pmid)
        if not meta["abstract"]:
            raise ConversionError(f"PubMed PMID {pmid} returned no abstract")

        body = meta["abstract"].rstrip("\n") + "\n"
        front = {
            "id": f"pubmed-{pmid}",
            "type": "pubmed",
            "title": meta["title"] or f"PMID:{pmid}",
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "authors": meta["authors"],
            "ingested_at": _now_iso(),
            "content_hash": validator.compute_content_hash(body),
            "domains": [],
            "nlm_corpus_ids": [],
            "wiki_pages": [],
            "meta": {
                "pmid": pmid,
                "journal": meta["journal"],
                "doi": meta["doi"],
                "mesh_terms": meta["mesh_terms"],
                "abstract_only": True,
            },
        }
        if meta["published_at"]:
            front["published_at"] = meta["published_at"]
        return fm.serialize(front, body)
