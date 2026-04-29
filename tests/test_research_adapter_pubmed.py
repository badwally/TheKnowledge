"""Tests for `gateway.research.adapters.pubmed.PubMedAdapter`.

The adapter wraps NCBI E-utilities. All HTTP is mocked — these tests
never reach the network. We assert:

- esearch + efetch are wired together correctly.
- CandidateItem fields are parsed from the PubMed XML response.
- max_results is respected.
- Network and HTTP failures surface as AdapterError.
"""

from __future__ import annotations

from typing import Any
from unittest.mock import patch

import pytest
import requests

from gateway.research.adapters.base import AdapterError, CandidateItem
from gateway.research.adapters.pubmed import PubMedAdapter


# --- fixtures --------------------------------------------------------------


_TWO_ARTICLE_XML = """<?xml version="1.0"?>
<PubmedArticleSet>
  <PubmedArticle>
    <MedlineCitation>
      <PMID>11111111</PMID>
      <Article>
        <Journal>
          <Title>Journal of Experimental Medicine</Title>
        </Journal>
        <ArticleTitle>Effect of foo on bar in mice</ArticleTitle>
        <Abstract>
          <AbstractText Label="BACKGROUND">Mice were studied.</AbstractText>
          <AbstractText Label="RESULTS">Foo affects bar.</AbstractText>
        </Abstract>
        <AuthorList>
          <Author>
            <LastName>Smith</LastName>
            <ForeName>Jane</ForeName>
          </Author>
          <Author>
            <LastName>Doe</LastName>
            <Initials>J</Initials>
          </Author>
        </AuthorList>
      </Article>
      <MeshHeadingList>
        <MeshHeading>
          <DescriptorName>Mice</DescriptorName>
        </MeshHeading>
        <MeshHeading>
          <DescriptorName>Foo Receptors</DescriptorName>
        </MeshHeading>
      </MeshHeadingList>
    </MedlineCitation>
    <PubmedData>
      <History>
        <PubMedPubDate><Year>2024</Year><Month>3</Month><Day>15</Day></PubMedPubDate>
      </History>
      <ArticleIdList>
        <ArticleId IdType="doi">10.1234/jem.2024.001</ArticleId>
      </ArticleIdList>
    </PubmedData>
    <PubDate>
      <Year>2024</Year>
      <Month>Mar</Month>
      <Day>15</Day>
    </PubDate>
  </PubmedArticle>
  <PubmedArticle>
    <MedlineCitation>
      <PMID>22222222</PMID>
      <Article>
        <Journal>
          <Title>Nature Reviews Foo</Title>
        </Journal>
        <ArticleTitle>A review of foo</ArticleTitle>
        <Abstract>
          <AbstractText>Plain abstract without label.</AbstractText>
        </Abstract>
        <AuthorList>
          <Author>
            <LastName>Lee</LastName>
            <ForeName>Alice</ForeName>
          </Author>
        </AuthorList>
      </Article>
    </MedlineCitation>
    <PubDate>
      <Year>2023</Year>
    </PubDate>
  </PubmedArticle>
</PubmedArticleSet>
"""


class _FakeResponse:
    def __init__(
        self,
        *,
        status_code: int = 200,
        json_payload: Any = None,
        text: str = "",
    ) -> None:
        self.status_code = status_code
        self._json = json_payload
        self.text = text

    def json(self) -> Any:
        if self._json is None:
            raise ValueError("no json payload set")
        return self._json


def _esearch_response(ids: list[str]) -> _FakeResponse:
    return _FakeResponse(
        status_code=200,
        json_payload={"esearchresult": {"idlist": ids}},
    )


def _efetch_response(xml: str = _TWO_ARTICLE_XML) -> _FakeResponse:
    return _FakeResponse(status_code=200, text=xml)


# --- tests -----------------------------------------------------------------


def test_search_parses_two_articles():
    calls: list[tuple[str, dict]] = []

    def fake_get(url: str, params: dict | None = None, timeout: int = 0):
        calls.append((url, dict(params or {})))
        if "esearch" in url:
            return _esearch_response(["11111111", "22222222"])
        return _efetch_response()

    with patch("gateway.research.adapters.pubmed.requests.get", side_effect=fake_get):
        items = PubMedAdapter().search("foo bar")

    assert len(items) == 2
    first, second = items

    assert isinstance(first, CandidateItem)
    assert first.item_id == "11111111"
    assert first.source_type == "pubmed"
    assert first.url == "https://pubmed.ncbi.nlm.nih.gov/11111111/"
    assert first.title == "Effect of foo on bar in mice"
    assert first.authors == ["Jane Smith", "J Doe"]
    assert first.publish_date == "2024-03-15"
    assert "Mice were studied" in first.description
    assert "Foo affects bar" in first.description
    assert first.source_metadata["doi"] == "10.1234/jem.2024.001"
    assert first.source_metadata["journal"] == "Journal of Experimental Medicine"
    assert "Mice" in first.source_metadata["mesh_terms"]

    assert second.item_id == "22222222"
    assert second.publish_date == "2023"
    assert second.source_metadata["mesh_terms"] == []

    # The query reaches esearch.
    assert any("esearch" in url for url, _ in calls)
    esearch_params = next(p for u, p in calls if "esearch" in u)
    assert esearch_params["term"] == "foo bar"
    assert esearch_params["db"] == "pubmed"


def test_search_caps_at_max_results():
    captured: dict[str, Any] = {}

    def fake_get(url: str, params: dict | None = None, timeout: int = 0):
        if "esearch" in url:
            captured["retmax"] = params["retmax"]
            # NCBI may still return more; the adapter must cap defensively.
            return _esearch_response(["1", "2", "3", "4", "5"])
        captured["efetch_ids"] = params["id"]
        return _efetch_response("<PubmedArticleSet></PubmedArticleSet>")

    with patch("gateway.research.adapters.pubmed.requests.get", side_effect=fake_get):
        PubMedAdapter().search("query", max_results=2)

    assert captured["retmax"] == "2"
    # Defensive cap before efetch.
    assert captured["efetch_ids"].split(",") == ["1", "2"]


def test_search_uses_api_key_when_set(monkeypatch):
    monkeypatch.setenv("NCBI_API_KEY", "secret-key")
    monkeypatch.setenv("KNOWLEDGE_NCBI_EMAIL", "u@example.com")
    seen_params: list[dict] = []

    def fake_get(url: str, params: dict | None = None, timeout: int = 0):
        seen_params.append(dict(params or {}))
        if "esearch" in url:
            return _esearch_response(["11111111"])
        return _efetch_response()

    with patch("gateway.research.adapters.pubmed.requests.get", side_effect=fake_get):
        PubMedAdapter().search("foo")

    for params in seen_params:
        assert params["api_key"] == "secret-key"
        assert params["email"] == "u@example.com"


def test_search_returns_empty_for_empty_query():
    # No HTTP call should happen for empty queries.
    with patch("gateway.research.adapters.pubmed.requests.get") as mocked:
        items = PubMedAdapter().search("   ")
    assert items == []
    mocked.assert_not_called()


def test_search_returns_empty_when_esearch_finds_nothing():
    def fake_get(url: str, params: dict | None = None, timeout: int = 0):
        assert "esearch" in url
        return _esearch_response([])

    with patch("gateway.research.adapters.pubmed.requests.get", side_effect=fake_get):
        items = PubMedAdapter().search("nothing matches")

    assert items == []


def test_esearch_http_failure_raises_adapter_error():
    def fake_get(url: str, params: dict | None = None, timeout: int = 0):
        return _FakeResponse(status_code=503, text="service unavailable")

    with patch("gateway.research.adapters.pubmed.requests.get", side_effect=fake_get):
        with pytest.raises(AdapterError, match="esearch"):
            PubMedAdapter().search("foo")


def test_efetch_http_failure_raises_adapter_error():
    def fake_get(url: str, params: dict | None = None, timeout: int = 0):
        if "esearch" in url:
            return _esearch_response(["11111111"])
        return _FakeResponse(status_code=500, text="boom")

    with patch("gateway.research.adapters.pubmed.requests.get", side_effect=fake_get):
        with pytest.raises(AdapterError, match="efetch"):
            PubMedAdapter().search("foo")


def test_network_exception_raises_adapter_error():
    def fake_get(url: str, params: dict | None = None, timeout: int = 0):
        raise requests.ConnectionError("dns")

    with patch("gateway.research.adapters.pubmed.requests.get", side_effect=fake_get):
        with pytest.raises(AdapterError, match="esearch"):
            PubMedAdapter().search("foo")


def test_efetch_invalid_xml_raises_adapter_error():
    def fake_get(url: str, params: dict | None = None, timeout: int = 0):
        if "esearch" in url:
            return _esearch_response(["11111111"])
        return _FakeResponse(status_code=200, text="not xml")

    with patch("gateway.research.adapters.pubmed.requests.get", side_effect=fake_get):
        with pytest.raises(AdapterError, match="parse"):
            PubMedAdapter().search("foo")
