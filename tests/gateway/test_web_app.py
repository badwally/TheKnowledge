"""Tests for the M40 FastAPI web app."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from gateway.web.app import create_app


@pytest.fixture
def client(kb_root):
    app = create_app()
    return TestClient(app)


def test_app_returns_health_ok(client):
    resp = client.get("/api/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_get_status(client, kb_root):
    """Status endpoint returns watcher state, inbox, drafts, sources."""
    from gateway import paths

    raw = paths.raw_source_path("youtube", "yt-statusTest_AB")
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(
        "---\nid: yt-statusTest_AB\ntype: youtube\ntitle: t\n"
        "url: https://x\nauthors: []\ningested_at: 2026-01-01T00:00:00Z\n"
        "content_hash: sha256:abc\ndomains: []\nnlm_corpus_ids: []\n"
        "wiki_pages: []\nmeta: {}\n---\nbody\n"
    )

    resp = client.get("/api/status")
    assert resp.status_code == 200
    body = resp.json()
    assert "watcher" in body
    assert "inbox" in body
    assert "drafts" in body
    assert "sources" in body
    assert "domains" in body
    assert body["sources"] >= 1


def test_get_log(client, kb_root):
    """Log endpoint tails log.md."""
    from gateway import paths

    log_path = paths.log_path()
    log_path.write_text(
        "# log\n\n"
        "## [2026-05-04T20:00:00Z] ingest | id=yt-1\n\nx\n\n"
        "## [2026-05-04T20:01:00Z] query | domain=d\n\ny\n"
    )

    resp = client.get("/api/log?lines=10")
    assert resp.status_code == 200
    entries = resp.json()
    assert isinstance(entries, list)
    assert len(entries) == 2
    assert entries[0]["op"] == "query"  # newest first
    assert entries[1]["op"] == "ingest"


def test_get_lint(client, kb_root):
    """Lint endpoint runs lint and returns a structured report."""
    resp = client.get("/api/lint?scope=schema-drift")
    assert resp.status_code == 200
    body = resp.json()
    assert "summary" in body
