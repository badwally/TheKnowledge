"""Tests for the arXiv search adapter (`gateway.research.adapters.arxiv`).

Network calls are stubbed by monkeypatching `_fetch_feed` with a canned
Atom XML payload modeled on a real arXiv API response. The HTTP-error
path is exercised via a `requests`-level monkeypatch so we exercise the
adapter's own error wrapping.
"""

from __future__ import annotations

import pytest
import requests

from gateway.research.adapters import arxiv as arxiv_mod
from gateway.research.adapters.base import AdapterError, CandidateItem


_ATOM_RESPONSE = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2403.12345v1</id>
    <title>GLP-1 receptor agonism in mesolimbic circuitry</title>
    <summary>
      We show that GLP-1 receptor agonists modulate
      dopamine signaling in mesolimbic circuits.
    </summary>
    <published>2024-04-02T00:00:00Z</published>
    <author>
      <name>J. Liu</name>
      <arxiv:affiliation>MIT</arxiv:affiliation>
    </author>
    <author>
      <name>P. Rondard</name>
    </author>
    <category term="q-bio.NC"/>
    <category term="cs.LG"/>
    <arxiv:primary_category term="q-bio.NC"/>
    <arxiv:doi>10.1234/example.2024</arxiv:doi>
    <arxiv:journal_ref>Nature Neuroscience 2024</arxiv:journal_ref>
    <arxiv:comment>10 pages</arxiv:comment>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2404.99999v2</id>
    <title>Reward blunting and tirzepatide</title>
    <summary>Tirzepatide blunts reward signaling.</summary>
    <published>2024-05-10T00:00:00Z</published>
    <author>
      <name>S. Chen</name>
    </author>
    <category term="q-bio.NC"/>
    <arxiv:primary_category term="q-bio.NC"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2406.11111v1</id>
    <title>Third paper</title>
    <summary>Third abstract.</summary>
    <published>2024-06-01T00:00:00Z</published>
    <author><name>A. Author</name></author>
    <category term="cs.LG"/>
    <arxiv:primary_category term="cs.LG"/>
  </entry>
</feed>
"""


def _patch_feed(monkeypatch: pytest.MonkeyPatch, xml: str = _ATOM_RESPONSE) -> None:
    monkeypatch.setattr(
        arxiv_mod,
        "_fetch_feed",
        lambda query, *, max_results, sort_by, start=0: xml,
    )


def test_search_parses_canned_response_into_candidate_items(monkeypatch):
    _patch_feed(monkeypatch)

    items = arxiv_mod.ArxivAdapter().search("GLP-1 reward")

    assert len(items) == 3
    first = items[0]
    assert isinstance(first, CandidateItem)
    assert first.item_id == "arxiv:2403.12345"
    assert first.source_type == "arxiv"
    assert first.url == "https://arxiv.org/abs/2403.12345"
    assert first.title == "GLP-1 receptor agonism in mesolimbic circuitry"
    assert first.authors == ["J. Liu", "P. Rondard"]
    assert first.publish_date == "2024-04-02T00:00:00Z"
    assert "GLP-1 receptor agonists" in first.description
    # Whitespace in the source XML should be normalized away.
    assert "\n" not in first.description
    # journal_ref is present, so this is classified as a journal article.
    assert first.content_type == "journal_article"
    meta = first.source_metadata
    assert meta["arxiv_id"] == "2403.12345"
    assert meta["categories"] == ["q-bio.NC", "cs.LG"]
    assert meta["primary_category"] == "q-bio.NC"
    assert meta["pdf_url"] == "https://arxiv.org/pdf/2403.12345.pdf"
    assert meta["doi"] == "10.1234/example.2024"
    assert meta["journal_ref"] == "Nature Neuroscience 2024"
    assert meta["comment"] == "10 pages"

    # The second entry has no journal_ref, so it should be a preprint.
    assert items[1].content_type == "preprint"
    assert items[1].item_id == "arxiv:2404.99999"


def test_search_respects_max_results(monkeypatch):
    _patch_feed(monkeypatch)

    items = arxiv_mod.ArxivAdapter().search("anything", max_results=2)

    assert len(items) == 2
    assert items[0].item_id == "arxiv:2403.12345"
    assert items[1].item_id == "arxiv:2404.99999"


def test_search_passes_filter_hints_to_query_builder(monkeypatch):
    captured: dict = {}

    def fake_fetch(query, *, max_results, sort_by, start=0):
        captured["query"] = query
        captured["sort_by"] = sort_by
        return _ATOM_RESPONSE

    monkeypatch.setattr(arxiv_mod, "_fetch_feed", fake_fetch)

    arxiv_mod.ArxivAdapter().search(
        "reward",
        filter_hints={"categories": ["q-bio.NC", "cs.LG"], "sort_by": "submittedDate"},
    )

    assert "all:reward" in captured["query"]
    assert "cat:q-bio.NC" in captured["query"]
    assert "cat:cs.LG" in captured["query"]
    assert captured["sort_by"] == "submittedDate"


def test_search_raises_adapter_error_on_http_failure(monkeypatch):
    class _FakeResponse:
        status_code = 503
        text = "service unavailable"

    monkeypatch.setattr(
        arxiv_mod.requests,
        "get",
        lambda url, params=None, timeout=None: _FakeResponse(),
    )

    with pytest.raises(AdapterError) as excinfo:
        arxiv_mod.ArxivAdapter().search("anything")
    assert "503" in str(excinfo.value)


def test_search_raises_adapter_error_on_network_exception(monkeypatch):
    def boom(*_args, **_kwargs):
        raise requests.ConnectionError("dns failed")

    monkeypatch.setattr(arxiv_mod.requests, "get", boom)

    with pytest.raises(AdapterError):
        arxiv_mod.ArxivAdapter().search("anything")


def test_search_raises_adapter_error_on_malformed_xml(monkeypatch):
    monkeypatch.setattr(
        arxiv_mod,
        "_fetch_feed",
        lambda query, *, max_results, sort_by, start=0: "<not-valid-xml",
    )

    with pytest.raises(AdapterError):
        arxiv_mod.ArxivAdapter().search("anything")
