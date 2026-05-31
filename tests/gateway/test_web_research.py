"""Tests for M41 research orchestration UI endpoints."""

from __future__ import annotations

import pytest
import yaml
from fastapi.testclient import TestClient

from gateway import paths
from gateway.web.app import create_app  # noqa: F401


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


def test_get_session_returns_full_plan(client, kb_root):
    _seed_query_plan(
        "2026-05-04-detail",
        domain="d-test",
        prompt="detail test prompt",
        queries={"arxiv": ["a1", "a2"], "youtube": ["y1"], "web": [], "pubmed": []},
    )
    resp = client.get("/api/research/sessions/2026-05-04-detail")
    assert resp.status_code == 200
    body = resp.json()
    assert body["session_id"] == "2026-05-04-detail"
    assert body["domain"] == "d-test"
    assert body["prompt"] == "detail test prompt"
    assert body["plan"]["queries"]["arxiv"] == ["a1", "a2"]
    assert body["plan"]["queries"]["youtube"] == ["y1"]
    assert body["state"] == "plan_only"


def test_get_unknown_session_returns_404(client):
    resp = client.get("/api/research/sessions/nonexistent")
    assert resp.status_code == 404


def test_create_session_returns_task_id(client, kb_root, monkeypatch):
    """POST /api/research/sessions starts a planner task and returns 202."""
    import time
    from gateway.research import query_planner

    # Stub plan_per_adapter_queries (the planner) so we don't need a real Claude
    class StubResult:
        queries = {"arxiv": ["stub q"], "youtube": [], "web": [], "pubmed": []}
        target_counts = {"arxiv": 8, "youtube": 20, "web": 15, "pubmed": 5}
        plan_client_model = None

    def fake_plan(*args, **kwargs):
        return StubResult()

    monkeypatch.setattr(query_planner, "plan_per_adapter_queries", fake_plan)

    # Stub policy.load_policy too — no real policy file exists in the test KB
    from gateway.filter import policy as _policy

    class StubPolicy:
        domain_slug = "d-test"
        domain_topic = "test"
        domain_field = "test"
        domain_description = "test"
        inclusion_criteria = ["a", "b", "c"]

    monkeypatch.setattr(_policy, "load_policy", lambda domain: StubPolicy())

    resp = client.post(
        "/api/research/sessions",
        json={"prompt": "test prompt", "domain": "d-test"},
    )
    assert resp.status_code == 202
    body = resp.json()
    assert "task_id" in body
    assert body["status"] == "queued"

    # Wait for the task to complete
    task_id = body["task_id"]
    for _ in range(30):
        time.sleep(0.1)
        t_resp = client.get(f"/api/tasks/{task_id}")
        if t_resp.json()["status"] in ("done", "failed"):
            break
    final = client.get(f"/api/tasks/{task_id}").json()
    assert final["status"] == "done", final


def test_put_plan_updates_yaml(client, kb_root):
    _seed_query_plan(
        "2026-05-04-update",
        domain="d-test",
        prompt="x",
        queries={"arxiv": ["original"], "youtube": [], "web": [], "pubmed": []},
    )
    resp = client.put(
        "/api/research/sessions/2026-05-04-update/plan",
        json={
            "queries": {
                "arxiv": ["updated 1", "updated 2"],
                "youtube": ["new"],
                "web": [],
                "pubmed": [],
            },
        },
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["plan"]["queries"]["arxiv"] == ["updated 1", "updated 2"]
    assert body["plan"]["queries"]["youtube"] == ["new"]


def test_put_plan_unknown_session_returns_404(client, kb_root):
    resp = client.put(
        "/api/research/sessions/nonexistent/plan",
        json={"queries": {"arxiv": [], "youtube": [], "web": [], "pubmed": []}},
    )
    assert resp.status_code == 404


def test_execute_returns_task_id(client, kb_root, monkeypatch):
    """POST /api/research/sessions/{id}/execute returns 202 + task_id."""
    _seed_query_plan(
        "2026-05-04-exec",
        domain="d-test",
        prompt="x",
        queries={"arxiv": ["q"], "youtube": [], "web": [], "pubmed": []},
    )

    # Stub the orchestrator's research() to avoid real network/NLM calls.
    from gateway.research import orchestrator
    from gateway.core import OperationResult

    captured_kwargs = {}

    def fake_research(prompt=None, **kwargs):
        captured_kwargs.update(kwargs)
        return OperationResult(
            success=True,
            summary=f"stubbed research (execute_session={kwargs.get('execute_session')})",
            paths_touched=[],
        )

    monkeypatch.setattr(orchestrator, "research", fake_research)

    resp = client.post(
        "/api/research/sessions/2026-05-04-exec/execute",
        json={"dry_run": False, "draft": False},
    )
    assert resp.status_code == 202
    body = resp.json()
    assert "task_id" in body
    assert body["status"] == "queued"


def test_progress_returns_step_states(client, kb_root):
    """Progress endpoint parses log.md for the session and returns step states."""
    _seed_query_plan("2026-05-04-prog", domain="d-test", prompt="x")

    log_path = paths.log_path()
    log_path.write_text(
        "# log\n\n"
        "## [2026-05-04T12:00:00Z] research | session_id=2026-05-04-prog | step=start | domain=d-test\n\n"
        "started\n\n"
        "## [2026-05-04T12:00:05Z] research | session_id=2026-05-04-prog | step=search | adapter=arxiv | n=10\n\n"
        "arxiv: 10 candidates\n\n"
        "## [2026-05-04T12:00:10Z] research | session_id=2026-05-04-prog | step=search | adapter=youtube | n=20\n\n"
        "youtube: 20 candidates\n\n"
        "## [2026-05-04T12:00:15Z] research | session_id=2026-05-04-prog | step=merge | n=28\n\n"
        "deduped\n\n"
    )

    resp = client.get("/api/research/sessions/2026-05-04-prog/progress")
    assert resp.status_code == 200
    body = resp.json()
    assert "steps" in body
    steps = {s["name"]: s["status"] for s in body["steps"]}
    assert steps["start"] == "done"
    assert steps["search.arxiv"] == "done"
    assert steps["search.youtube"] == "done"
    assert steps["merge"] == "done"
    # Steps not yet observed remain queued
    assert steps["filter"] == "queued"
    assert steps["materialize"] == "queued"


def test_progress_unknown_session_returns_empty(client, kb_root):
    """Unknown session returns 200 with all steps queued (not 404)."""
    resp = client.get("/api/research/sessions/nonexistent/progress")
    assert resp.status_code == 200
    body = resp.json()
    assert all(s["status"] == "queued" for s in body["steps"])
