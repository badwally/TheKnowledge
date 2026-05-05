"""Tests for M42 Review console endpoints."""

from __future__ import annotations

import pytest
import yaml
from fastapi.testclient import TestClient

from gateway import frontmatter as fm
from gateway import paths
from gateway.web.app import create_app


@pytest.fixture
def client(kb_root):
    return TestClient(create_app())


def _seed_draft(slug, *, type_dir, draft_started_at, claims_count=0):
    """Write a draft wiki page under wiki/<type_dir>/<slug>.md."""
    path = paths.wiki_dir() / type_dir / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": type_dir.rstrip("s"),  # "concepts" → "concept", "entities" → "entity"
        "slug": slug,
        "draft": True,
        "draft_started_at": draft_started_at,
        "draft_unresolved_claims": claims_count,
    }
    body = f"# {slug}\n\nplaceholder\n"
    path.write_text(fm.serialize(front, body))


def test_drafts_empty_when_no_drafts(client, kb_root):
    resp = client.get("/api/review/drafts")
    assert resp.status_code == 200
    assert resp.json() == []


def test_drafts_returns_drafts_sorted_oldest_first(client, kb_root):
    _seed_draft("recent", type_dir="concepts",
                draft_started_at="2026-05-04T00:00:00Z", claims_count=2)
    _seed_draft("ancient", type_dir="synthesis",
                draft_started_at="2026-04-01T00:00:00Z", claims_count=5)
    _seed_draft("middle", type_dir="entities",
                draft_started_at="2026-04-25T00:00:00Z", claims_count=0)

    resp = client.get("/api/review/drafts")
    assert resp.status_code == 200
    drafts = resp.json()
    assert len(drafts) == 3
    # Oldest first
    assert drafts[0]["slug"] == "ancient"
    assert drafts[1]["slug"] == "middle"
    assert drafts[2]["slug"] == "recent"
    # Path includes wiki/ prefix
    assert drafts[0]["path"].startswith("wiki/synthesis/ancient")
    # age_days populated and >= 0, sorted descending
    assert drafts[0]["age_days"] >= drafts[1]["age_days"]


def test_drafts_skips_non_draft_pages(client, kb_root):
    # A non-draft page should not appear
    path = paths.wiki_dir() / "concepts" / "non-draft.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(fm.serialize(
        {"type": "concept", "slug": "non-draft"},
        "## Summary\n\nx\n",
    ))
    _seed_draft("is-draft", type_dir="concepts", draft_started_at="2026-04-01T00:00:00Z")

    resp = client.get("/api/review/drafts")
    drafts = resp.json()
    slugs = [d["slug"] for d in drafts]
    assert "is-draft" in slugs
    assert "non-draft" not in slugs
