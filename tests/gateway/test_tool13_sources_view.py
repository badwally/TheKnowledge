"""TOOL-13: /api/sources endpoint tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from fastapi.testclient import TestClient

from gateway import frontmatter as fm, paths, validator
from gateway.web.app import create_app  # noqa: F401


def _make_raw_source(
    source_id: str,
    domain: str = "test-domain",
    source_type: str = "web",
    title: str = "",
    filter_score: float | None = None,
    link_status: str | None = None,
) -> Path:
    body = f"Body text for {source_id}. Some interesting content."
    p = paths.raw_source_path(source_type, source_id)
    p.parent.mkdir(parents=True, exist_ok=True)
    front: dict[str, Any] = {
        "id": source_id,
        "title": title or f"Title for {source_id}",
        "type": source_type,
        "ingested_at": "2026-05-26T06:00:00Z",
        "content_hash": validator.compute_content_hash(body),
        "domains": [domain] if domain else [],
    }
    if filter_score is not None:
        front["filter"] = {"score": filter_score, "decision": "include"}
    if link_status:
        front["link_status"] = link_status
    p.write_text(fm.serialize(front, body))
    return p


# --- basic endpoint ---------------------------------------------------------


def test_sources_empty(client, kb_root):
    resp = client.get("/api/sources")
    assert resp.status_code == 200
    assert resp.json() == []


def test_sources_returns_record(client, kb_root):
    _make_raw_source("web-2026-05-26-aaa", domain="glp1")
    resp = client.get("/api/sources")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 1
    rec = data[0]
    assert rec["source_id"] == "web-2026-05-26-aaa"
    assert rec["source_type"] == "web"
    assert "glp1" in rec["domains"]


def test_sources_multiple(client, kb_root):
    _make_raw_source("web-2026-05-26-a1")
    _make_raw_source("web-2026-05-26-a2")
    resp = client.get("/api/sources")
    assert resp.status_code == 200
    assert len(resp.json()) == 2


# --- query filter -----------------------------------------------------------


def test_sources_query_title_match(client, kb_root):
    _make_raw_source("web-2026-05-26-b1", title="GLP1 receptor study")
    _make_raw_source("web-2026-05-26-b2", title="Unrelated paper")
    resp = client.get("/api/sources?q=glp1")
    data = resp.json()
    assert len(data) == 1
    assert data[0]["source_id"] == "web-2026-05-26-b1"


def test_sources_query_id_match(client, kb_root):
    _make_raw_source("web-2026-05-26-unique")
    _make_raw_source("web-2026-05-26-other")
    resp = client.get("/api/sources?q=unique")
    data = resp.json()
    assert len(data) == 1
    assert data[0]["source_id"] == "web-2026-05-26-unique"


def test_sources_query_no_match(client, kb_root):
    _make_raw_source("web-2026-05-26-c1")
    resp = client.get("/api/sources?q=zzznomatch")
    assert resp.json() == []


# --- domain filter ----------------------------------------------------------


def test_sources_domain_filter(client, kb_root):
    _make_raw_source("web-2026-05-26-d1", domain="domain-a")
    _make_raw_source("web-2026-05-26-d2", domain="domain-b")
    resp = client.get("/api/sources?domain=domain-a")
    data = resp.json()
    assert len(data) == 1
    assert data[0]["source_id"] == "web-2026-05-26-d1"


def test_sources_domain_filter_no_match(client, kb_root):
    _make_raw_source("web-2026-05-26-e1", domain="domain-x")
    resp = client.get("/api/sources?domain=domain-z")
    assert resp.json() == []


# --- type filter ------------------------------------------------------------


def test_sources_type_filter(client, kb_root):
    _make_raw_source("web-2026-05-26-f1", source_type="web")
    resp = client.get("/api/sources?type=web")
    assert len(resp.json()) == 1


# --- metadata fields --------------------------------------------------------


def test_sources_filter_score_returned(client, kb_root):
    _make_raw_source("web-2026-05-26-g1", filter_score=0.82)
    data = client.get("/api/sources").json()
    assert abs(data[0]["filter_score"] - 0.82) < 0.01


def test_sources_link_status_returned(client, kb_root):
    _make_raw_source("web-2026-05-26-h1", link_status="dead")
    data = client.get("/api/sources").json()
    assert data[0]["link_status"] == "dead"


def test_sources_word_count_positive(client, kb_root):
    _make_raw_source("web-2026-05-26-i1")
    data = client.get("/api/sources").json()
    assert data[0]["word_count"] > 0


# --- limit ------------------------------------------------------------------


def test_sources_limit(client, kb_root):
    for i in range(5):
        _make_raw_source(f"web-2026-05-26-lim{i}")
    resp = client.get("/api/sources?limit=3")
    assert len(resp.json()) == 3
