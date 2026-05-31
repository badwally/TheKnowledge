"""Tests for the M40 FastAPI web app."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from gateway.web.app import create_app


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


def test_list_domains(client, kb_root):
    """GET /api/domains returns each policy as a summary."""
    from gateway import paths

    pol = paths.policies_dir() / "test-domain" / "policy.yaml"
    pol.parent.mkdir(parents=True, exist_ok=True)
    pol.write_text(
        "version: v1\npolicy_schema_version: 1\n"
        "domain:\n  slug: test-domain\n  topic: Test\n  field: T\n  description: d\n"
        "filter:\n  threshold_include: 0.7\n  threshold_review: 0.5\n"
        "inclusion_criteria: [a, b, c]\nexclusion_criteria: [x]\n"
        "quality_signals: {q: {positive_signals: [p, q], negative_signals: [n, m]}}\n"
    )

    resp = client.get("/api/domains")
    assert resp.status_code == 200
    domains = resp.json()
    assert any(d["slug"] == "test-domain" for d in domains)


def test_list_proposals(client, kb_root):
    """GET /api/proposals returns draft proposals."""
    from gateway import frontmatter as fm
    from gateway import paths

    prop = paths.wiki_dir() / "proposals" / "test-prop.md"
    prop.parent.mkdir(parents=True, exist_ok=True)
    prop.write_text(
        fm.serialize(
            {
                "type": "domain-proposal",
                "slug": "test-prop",
                "title": "Test prop",
                "proposed_domain": "test-prop",
                "status": "draft",
                "member_sources": ["yt-1"],
                "rationale": "r",
            },
            "## Rationale\n\nr\n## Member sources\n\n- [[sources/yt-1]]\n",
        )
    )

    resp = client.get("/api/proposals")
    assert resp.status_code == 200
    proposals = resp.json()
    assert any(p["slug"] == "test-prop" for p in proposals)


def test_promote_domain_returns_error_for_missing_proposal(client, kb_root):
    resp = client.post("/api/domains/nonexistent/promote")
    assert resp.status_code == 400


def test_finalize_endpoint_rejects_missing_path(client, kb_root):
    resp = client.post(
        "/api/ops/finalize",
        json={"page_path": "wiki/concepts/nonexistent.md", "abandon": False},
    )
    assert resp.status_code == 400


def test_filter_correct_endpoint_returns_error_for_missing_source(client, kb_root):
    resp = client.post(
        "/api/ops/filter-correct",
        json={"source_id": "yt-nonexistent", "decision": "include", "rationale": "r"},
    )
    assert resp.status_code == 400


import time


def test_async_ingest_returns_task_id(client, kb_root, make_source):
    """Multipart upload to /api/ingest returns 202 + task_id; GET /api/tasks/{id}
    reports completion. (Local-path ingest over the API is rejected — finding
    #3 — so file ingest goes through the sanctioned multipart upload path.)"""
    content = make_source(id_="yt-asyncTest_AB")

    resp = client.post(
        "/api/ingest",
        files={"file": ("input.md", content, "text/markdown")},
    )
    assert resp.status_code == 202
    body = resp.json()
    assert "task_id" in body
    assert body["status"] == "queued"

    task_id = body["task_id"]
    for _ in range(50):
        time.sleep(0.1)
        get_resp = client.get(f"/api/tasks/{task_id}")
        if get_resp.json()["status"] in ("done", "failed"):
            break
    final = client.get(f"/api/tasks/{task_id}").json()
    assert final["status"] == "done", final


def test_get_unknown_task_returns_404(client, kb_root):
    resp = client.get("/api/tasks/nonexistent")
    assert resp.status_code == 404


def test_async_bootstrap_domain_returns_task_id(client, kb_root):
    """Bootstrap with invalid slug should fail-fast inside the op."""
    resp = client.post(
        "/api/ops/bootstrap-domain",
        json={
            "description": "x",
            "slug": "Bad_Slug",
            "force": False,
        },
    )
    assert resp.status_code == 202
    task_id = resp.json()["task_id"]
    for _ in range(20):
        time.sleep(0.1)
        if client.get(f"/api/tasks/{task_id}").json()["status"] in ("done", "failed"):
            break
    final = client.get(f"/api/tasks/{task_id}").json()
    assert final["status"] in ("done", "failed")


def test_root_serves_index_html(client, kb_root):
    """The root path serves the React app's index.html when the build exists."""
    resp = client.get("/")
    # If web/dist/index.html exists, expect 200; if not, expect 404 (SPA fallback not mounted)
    assert resp.status_code in (200, 404)
    if resp.status_code == 200:
        assert "<html" in resp.text.lower() or "<!doctype" in resp.text.lower()
