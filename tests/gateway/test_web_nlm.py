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
