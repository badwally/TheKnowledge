"""Tests for M41 research orchestration UI endpoints."""

from __future__ import annotations

import pytest
import yaml
from fastapi.testclient import TestClient

from gateway import paths
from gateway.web.app import create_app


@pytest.fixture
def client(kb_root):
    return TestClient(create_app())


def _seed_query_plan(session_id, *, domain, prompt, queries=None, generated_at=None):
    from datetime import datetime, timezone

    if generated_at is None:
        generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    plans_dir = paths.knowledge_root() / "nlm" / "query_plans"
    plans_dir.mkdir(parents=True, exist_ok=True)
    data = {
        "version": 1,
        "session_id": session_id,
        "domain": domain,
        "prompt": prompt,
        "generated_at": generated_at,
        "plan_client_model": None,
        "target_counts": {"arxiv": 8, "youtube": 20, "web": 15, "pubmed": 5},
        "queries": queries or {"arxiv": ["q1", "q2"], "youtube": [], "web": [], "pubmed": []},
    }
    (plans_dir / f"{session_id}.yaml").write_text(yaml.safe_dump(data, sort_keys=False))


def test_list_sessions_returns_empty_when_no_plans(client):
    resp = client.get("/api/research/sessions")
    assert resp.status_code == 200
    assert resp.json() == []


def test_list_sessions_returns_plan_only_state(client, kb_root):
    _seed_query_plan("2026-05-01-test-session", domain="d-test", prompt="x")
    resp = client.get("/api/research/sessions")
    assert resp.status_code == 200
    sessions = resp.json()
    assert len(sessions) == 1
    s = sessions[0]
    assert s["session_id"] == "2026-05-01-test-session"
    assert s["state"] == "plan_only"
    assert s["domain"] == "d-test"
    assert s["query_count"] == 2  # 2 arxiv, 0 elsewhere


def test_list_sessions_sorted_newest_first(client, kb_root):
    _seed_query_plan("2026-05-01-old", domain="d-test", prompt="old", generated_at="2026-05-01T12:00:00Z")
    _seed_query_plan("2026-05-04-new", domain="d-test", prompt="new", generated_at="2026-05-04T12:00:00Z")

    resp = client.get("/api/research/sessions")
    sessions = resp.json()
    assert sessions[0]["session_id"] == "2026-05-04-new"
    assert sessions[1]["session_id"] == "2026-05-01-old"
