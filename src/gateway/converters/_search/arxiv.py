"""arXiv search adapter using the arXiv API (Atom feed)."""

import time
import requests
import feedparser
from src.search.normalize import make_item_id, truncate_description, empty_scores

ARXIV_API_URL = "http://export.arxiv.org/api/query"
RATE_LIMIT_SECONDS = 3  # polite crawling per arXiv guidelines


def build_query(search_terms: str, categories: list[str] = None) -> str:
    """Build an arXiv API query string.

    Combines search terms (searched in title and abstract) with optional
    category filters using arXiv query syntax.

    Args:
        search_terms: Free-text search query.
        categories: Optional list of arXiv categories, e.g. ["cs.CV", "cs.AI"].

    Returns:
        arXiv query string.
    """
    # Search in title and abstract
    query = f"all:{search_terms}"
    if categories:
        cat_query = " OR ".join(f"cat:{cat}" for cat in categories)
        query = f"({query}) AND ({cat_query})"
    return query


def normalize_paper(entry: dict) -> dict:
    """Normalize a feedparser entry into the pipeline's item format.

    Args:
        entry: A single entry dict from feedparser's parsed Atom feed.

    Returns:
        Normalized item dict matching ITEM_REQUIRED_FIELDS.
    """
    # Extract arxiv_id from the entry id URL (e.g. "http://arxiv.org/abs/2401.12345v1")
    arxiv_id = entry["id"].split("/abs/")[-1]
    # Strip version suffix for clean ID (2401.12345v1 -> 2401.12345)
    arxiv_id_clean = arxiv_id.split("v")[0] if "v" in arxiv_id else arxiv_id

    # Extract authors
    authors = []
    for author in entry.get("authors", []):
        name = author.get("name", "Unknown")
        affiliation = None
        if "arxiv_affiliation" in author:
            affiliation = author["arxiv_affiliation"]
        authors.append({"name": name, "affiliation": affiliation})

    # Extract categories
    categories = [tag["term"] for tag in entry.get("tags", []) if "term" in tag]
    primary_category = entry.get("arxiv_primary_category", {}).get("term", "")

    # Build PDF URL from abstract URL
    pdf_url = entry["id"].replace("/abs/", "/pdf/") + ".pdf"

    # Determine content_type based on journal_ref
    journal_ref = entry.get("arxiv_journal_ref")
    content_type = "journal_article" if journal_ref else "preprint"

    return {
        "item_id": make_item_id("arxiv", arxiv_id_clean),
        "source_type": "arxiv",
        "url": entry["id"],
        "title": " ".join(entry.get("title", "").split()),
        "authors": authors,
        "publish_date": entry.get("published", ""),
        "description": truncate_description(entry.get("summary", "").replace("\n", " ").strip(), 1000),
        "content_type": content_type,
        "full_text_available": True,  # arXiv always has PDFs
        "source_metadata": {
            "arxiv_id": arxiv_id_clean,
            "categories": categories,
            "pdf_url": pdf_url,
            "primary_category": primary_category,
            "comment": entry.get("arxiv_comment"),
            "journal_ref": journal_ref,
        },
        **empty_scores(),
    }


def search_arxiv(query: str, max_results: int = 50, sort_by: str = "relevance", start: int = 0) -> list[dict]:
    """Execute an arXiv API search and return raw feedparser entries.

    Args:
        query: arXiv query string (from build_query).
        max_results: Maximum results to return.
        sort_by: Sort order — "relevance", "lastUpdatedDate", or "submittedDate".
        start: Starting index for pagination.

    Returns:
        List of feedparser entry dicts.
    """
    sort_map = {
        "relevance": "relevance",
        "lastUpdatedDate": "lastUpdatedDate",
        "submittedDate": "submittedDate",
    }
    params = {
        "search_query": query,
        "start": start,
        "max_results": min(max_results, 100),  # arXiv API max per request
        "sortBy": sort_map.get(sort_by, "relevance"),
        "sortOrder": "descending",
    }

    response = requests.get(ARXIV_API_URL, params=params, timeout=30)
    response.raise_for_status()

    feed = feedparser.parse(response.text)
    return feed.entries


def search_and_normalize(
    query: str, max_results: int = 50, categories: list[str] = None, sort_by: str = "relevance"
) -> list[dict]:
    """Search arXiv and return normalized items.

    Args:
        query: Free-text search terms.
        max_results: Maximum results to return.
        categories: Optional arXiv category filter, e.g. ["cs.CV", "cs.AI"].
        sort_by: Sort order — "relevance", "lastUpdatedDate", or "submittedDate".

    Returns:
        List of normalized item dicts.
    """
    arxiv_query = build_query(query, categories)
    entries = search_arxiv(arxiv_query, max_results=max_results, sort_by=sort_by)
    if not entries:
        return []
    time.sleep(RATE_LIMIT_SECONDS)  # respect arXiv rate limit
    return [normalize_paper(entry) for entry in entries]
