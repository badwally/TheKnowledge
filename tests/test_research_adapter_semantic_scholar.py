"""Tests for the Semantic Scholar search adapter."""

from __future__ import annotations

from unittest.mock import patch

import pytest

from gateway.research.adapters.semantic_scholar import (
    SemanticScholarAdapter,
    _paper_to_candidate,
    _route_source,
)


# --- source-type routing ---------------------------------------------------


def test_route_prefers_arxiv():
    source_type, url, item_id = _route_source({"ArXiv": "2301.10140", "DOI": "10.x/y"})
    assert source_type == "arxiv"
    assert "arxiv.org/abs/2301.10140" in url
    assert item_id == "arxiv:2301.10140"


def test_route_prefers_pubmed_when_no_arxiv():
    source_type, url, item_id = _route_source({"PubMed": "12345678", "DOI": "10.x/y"})
    assert source_type == "pubmed"
    assert "pubmed.ncbi.nlm.nih.gov/12345678" in url


def test_route_falls_back_to_doi():
    source_type, url, item_id = _route_source({"DOI": "10.1234/test"})
    assert source_type == "web"
    assert "doi.org/10.1234/test" in url
    assert item_id == "doi:10.1234/test"


def test_route_falls_back_to_s2_corpus_id():
    source_type, url, item_id = _route_source({"CorpusId": "999"})
    assert source_type == "web"
    assert "semanticscholar.org/paper/999" in url


def test_route_returns_empty_on_no_ids():
    source_type, url, item_id = _route_source({})
    assert url == ""


# --- paper_to_candidate ----------------------------------------------------


_SAMPLE_PAPER = {
    "paperId": "abc123",
    "externalIds": {"ArXiv": "2301.10140", "DOI": "10.x/y", "CorpusId": "999"},
    "title": "The Semantic Scholar Open Data Platform",
    "abstract": "The volume of scientific output...",
    "authors": [{"authorId": "1", "name": "Rodney Kinney"}],
    "year": 2023,
    "citationCount": 150,
    "influentialCitationCount": 20,
    "tldr": {"model": "tldr@v2", "text": "S2 is the largest open scholarly graph."},
    "fieldsOfStudy": ["Computer Science"],
    "publicationTypes": ["JournalArticle"],
    "publicationDate": "2023-01-24",
}


def test_paper_to_candidate_happy_path():
    c = _paper_to_candidate(_SAMPLE_PAPER)
    assert c is not None
    assert c.source_type == "arxiv"
    assert c.item_id == "arxiv:2301.10140"
    assert "Rodney Kinney" in c.authors
    assert c.description == "S2 is the largest open scholarly graph."
    assert c.source_metadata["citation_count"] == 150
    assert c.source_metadata["influential_citation_count"] == 20
    assert c.source_metadata["tldr"] == "S2 is the largest open scholarly graph."


def test_paper_to_candidate_uses_abstract_when_no_tldr():
    paper = dict(_SAMPLE_PAPER, tldr=None)
    c = _paper_to_candidate(paper)
    assert "scientific output" in c.description


def test_paper_to_candidate_skips_empty_title():
    assert _paper_to_candidate({"title": "", "externalIds": {}}) is None
    assert _paper_to_candidate(None) is None


# --- search (mocked API) ---------------------------------------------------


_MOCK_SEARCH_RESPONSE = {
    "total": 1,
    "data": [_SAMPLE_PAPER],
}


@patch("gateway.research.adapters.semantic_scholar._get")
def test_search_returns_candidates(mock_get):
    mock_get.return_value = _MOCK_SEARCH_RESPONSE
    adapter = SemanticScholarAdapter()
    results = adapter.search("semantic scholar", max_results=10)
    assert len(results) == 1
    assert results[0].title == "The Semantic Scholar Open Data Platform"
    mock_get.assert_called_once()
    path, params = mock_get.call_args[0]
    assert path == "/paper/search"
    assert params["query"] == "semantic scholar"


@patch("gateway.research.adapters.semantic_scholar._get")
def test_search_passes_fields_of_study_hint(mock_get):
    mock_get.return_value = {"data": []}
    adapter = SemanticScholarAdapter()
    adapter.search("test", filter_hints={"fields_of_study": ["Economics", "Business"]})
    _, params = mock_get.call_args[0]
    assert params["fieldsOfStudy"] == "Economics,Business"


@patch("gateway.research.adapters.semantic_scholar._get")
def test_search_passes_year_hint(mock_get):
    mock_get.return_value = {"data": []}
    adapter = SemanticScholarAdapter()
    adapter.search("test", filter_hints={"year": "2020-2025"})
    _, params = mock_get.call_args[0]
    assert params["year"] == "2020-2025"


# --- citation traversal (mocked) -------------------------------------------


_MOCK_CITATIONS_RESPONSE = {
    "data": [
        {"citingPaper": _SAMPLE_PAPER},
    ],
}


@patch("gateway.research.adapters.semantic_scholar._get")
def test_citations_of(mock_get):
    mock_get.return_value = _MOCK_CITATIONS_RESPONSE
    adapter = SemanticScholarAdapter()
    results = adapter.citations_of("abc123", max_results=10)
    assert len(results) == 1
    mock_get.assert_called_once()
    assert "/paper/abc123/citations" in mock_get.call_args[0][0]


_MOCK_REFERENCES_RESPONSE = {
    "data": [
        {"citedPaper": _SAMPLE_PAPER},
    ],
}


@patch("gateway.research.adapters.semantic_scholar._get")
def test_references_of(mock_get):
    mock_get.return_value = _MOCK_REFERENCES_RESPONSE
    adapter = SemanticScholarAdapter()
    results = adapter.references_of("abc123", max_results=10)
    assert len(results) == 1
    assert "/paper/abc123/references" in mock_get.call_args[0][0]


# --- adapter registration --------------------------------------------------


def test_semantic_scholar_in_enabled_adapters():
    from gateway.research.adapters import enabled_adapters

    adapters = enabled_adapters()
    names = [a.name for a in adapters]
    assert "semantic_scholar" in names
