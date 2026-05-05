"""Tests for M43 NLM artifacts endpoints."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from gateway import frontmatter as fm
from gateway import paths
from gateway.web.app import create_app


@pytest.fixture
def client(kb_root):
    return TestClient(create_app())


def _seed_artifact(slug, *, artifact_type, domain, created_at, title="t"):
    """Write an artifact wiki page under wiki/artifacts/<artifact_type>/<slug>.md."""
    type_dir = artifact_type  # uses singular: 'briefing', 'audio', 'slides'
    path = paths.wiki_dir() / "artifacts" / type_dir / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "artifact",
        "artifact_type": artifact_type,
        "slug": slug,
        "title": title,
        "domain": domain,
        "created_at": created_at,
        "nlm_artifact_url": f"https://notebooklm.google.com/notebook/x/artifact/{slug}",
    }
    body = f"# {title}\n\nplaceholder\n"
    path.write_text(fm.serialize(front, body))


def test_nlm_add_returns_error_for_unknown_source(client, kb_root):
    """nlm-add wraps the existing op; missing source → 400."""
    resp = client.post(
        "/api/nlm/domains/d-test/add",
        json={"source_id": "yt-nonexistent"},
    )
    assert resp.status_code == 400


def test_artifacts_list_empty_when_no_artifacts(client, kb_root):
    resp = client.get("/api/nlm/domains/d-test/artifacts")
    assert resp.status_code == 200
    assert resp.json() == []


def test_artifacts_list_filters_by_domain(client, kb_root):
    _seed_artifact("alpha-slides", artifact_type="slides",
                   domain="d-test", created_at="2026-05-01T00:00:00Z", title="alpha")
    _seed_artifact("beta-briefing", artifact_type="briefing",
                   domain="d-test", created_at="2026-05-04T00:00:00Z", title="beta")
    _seed_artifact("other-domain", artifact_type="slides",
                   domain="d-other", created_at="2026-05-02T00:00:00Z", title="other")

    resp = client.get("/api/nlm/domains/d-test/artifacts")
    assert resp.status_code == 200
    artifacts = resp.json()
    slugs = {a["slug"] for a in artifacts}
    assert slugs == {"alpha-slides", "beta-briefing"}
    # Newest first
    assert artifacts[0]["slug"] == "beta-briefing"


import time


def test_briefing_returns_task_id(client, kb_root, monkeypatch):
    """POST /api/nlm/domains/{slug}/briefing returns 202 + task_id."""
    from gateway.ops import nlm as _nlm
    from gateway.core import OperationResult

    def fake_briefing(domain, **kwargs):
        return OperationResult(success=True, summary=f"stubbed briefing for {domain}")

    monkeypatch.setattr(_nlm, "nlm_briefing", fake_briefing)

    resp = client.post("/api/nlm/domains/d-test/briefing", json={})
    assert resp.status_code == 202
    body = resp.json()
    assert "task_id" in body
    assert body["status"] == "queued"


def test_audio_takes_topic(client, kb_root, monkeypatch):
    from gateway.ops import nlm as _nlm
    from gateway.core import OperationResult

    captured = {}

    def fake_audio(domain, topic, **kwargs):
        captured["domain"] = domain
        captured["topic"] = topic
        return OperationResult(success=True, summary="stub")

    monkeypatch.setattr(_nlm, "nlm_audio", fake_audio)

    resp = client.post(
        "/api/nlm/domains/d-test/audio",
        json={"topic": "endurance training"},
    )
    assert resp.status_code == 202

    task_id = resp.json()["task_id"]
    for _ in range(20):
        time.sleep(0.1)
        if client.get(f"/api/tasks/{task_id}").json()["status"] in ("done", "failed"):
            break
    assert captured["domain"] == "d-test"
    assert captured["topic"] == "endurance training"


def test_slides_takes_topic(client, kb_root, monkeypatch):
    from gateway.ops import nlm as _nlm
    from gateway.core import OperationResult

    def fake_slides(domain, topic, **kwargs):
        return OperationResult(success=True, summary=f"stubbed slides {domain}/{topic}")

    monkeypatch.setattr(_nlm, "nlm_slides", fake_slides)

    resp = client.post(
        "/api/nlm/domains/d-test/slides",
        json={"topic": "test topic"},
    )
    assert resp.status_code == 202


def test_sync_takes_optional_args(client, kb_root, monkeypatch):
    from gateway.ops import nlm as _nlm
    from gateway.core import OperationResult

    captured = {}

    def fake_sync(domain, *, dry_run=False, limit=None, **kwargs):
        captured["domain"] = domain
        captured["dry_run"] = dry_run
        captured["limit"] = limit
        return OperationResult(success=True, summary="stub sync")

    monkeypatch.setattr(_nlm, "nlm_sync", fake_sync)

    resp = client.post(
        "/api/nlm/domains/d-test/sync",
        json={"dry_run": True, "limit": 10},
    )
    assert resp.status_code == 202

    task_id = resp.json()["task_id"]
    for _ in range(20):
        time.sleep(0.1)
        if client.get(f"/api/tasks/{task_id}").json()["status"] in ("done", "failed"):
            break
    assert captured["domain"] == "d-test"
    assert captured["dry_run"] is True
    assert captured["limit"] == 10


def test_revise_takes_artifact_slug_and_instructions(client, kb_root, monkeypatch):
    from gateway.ops import nlm as _nlm
    from gateway.core import OperationResult

    captured = {}

    def fake_revise(artifact_slug, instructions, **kwargs):
        captured["slug"] = artifact_slug
        captured["instructions"] = instructions
        return OperationResult(success=True, summary="stub revise")

    monkeypatch.setattr(_nlm, "nlm_revise", fake_revise)

    resp = client.post(
        "/api/nlm/artifacts/some-slides/revise",
        json={"instructions": ["slide 2: tighten the mechanism diagram"]},
    )
    assert resp.status_code == 202

    task_id = resp.json()["task_id"]
    for _ in range(20):
        time.sleep(0.1)
        if client.get(f"/api/tasks/{task_id}").json()["status"] in ("done", "failed"):
            break
    assert captured["slug"] == "some-slides"
    assert captured["instructions"] == ["slide 2: tighten the mechanism diagram"]
