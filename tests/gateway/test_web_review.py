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


def test_contradictions_returns_empty_when_no_log(client, kb_root):
    resp = client.get("/api/review/contradictions")
    assert resp.status_code == 200
    assert resp.json() == []


def test_contradictions_returns_log_records_newest_first(client, kb_root):
    log_path = paths.knowledge_root() / ".knowledge" / "contradictions" / "log.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(
        '{"source_id": "yt-old", "existing_page": "wiki/concepts/a.md", '
        '"existing_claim": "old claim", "new_claim": "new claim", '
        '"severity": "minor", "recorded_at": "2026-04-01T00:00:00Z"}\n'
        '{"source_id": "yt-new", "existing_page": "wiki/concepts/b.md", '
        '"existing_claim": "another old", "new_claim": "another new", '
        '"severity": "major", "recorded_at": "2026-05-04T00:00:00Z"}\n'
    )

    resp = client.get("/api/review/contradictions")
    assert resp.status_code == 200
    records = resp.json()
    assert len(records) == 2
    # Newest first
    assert records[0]["source_id"] == "yt-new"
    assert records[0]["severity"] == "major"
    assert records[1]["source_id"] == "yt-old"


def test_contradictions_skips_malformed_lines(client, kb_root):
    log_path = paths.knowledge_root() / ".knowledge" / "contradictions" / "log.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(
        'this is not json\n'
        '{"source_id": "yt-good", "existing_page": "wiki/concepts/x.md", '
        '"existing_claim": "a", "new_claim": "b", "severity": "moderate", '
        '"recorded_at": "2026-05-04T00:00:00Z"}\n'
        '{}\n'  # Empty object passes JSON parse but lacks expected fields; still returned as-is
    )

    resp = client.get("/api/review/contradictions")
    assert resp.status_code == 200
    records = resp.json()
    # Two valid JSON lines (empty object is JSON; non-json line skipped)
    assert len(records) == 2


def test_orphans_returns_sources_without_wiki_pages(client, kb_root, make_source):
    """A source with empty `wiki_pages` is an orphan."""
    # Seed an orphan
    orphan_text = make_source(id_="yt-orphan_AB", domains=["d-test"])
    orphan_path = paths.raw_source_path("youtube", "yt-orphan_AB")
    orphan_path.parent.mkdir(parents=True, exist_ok=True)
    orphan_path.write_text(orphan_text)

    # Seed a non-orphan (has wiki_pages populated)
    text = make_source(
        id_="yt-cited_CD",
        domains=["d-test"],
        extra_front={"wiki_pages": ["wiki/concepts/x.md"]},
    )
    cited_path = paths.raw_source_path("youtube", "yt-cited_CD")
    cited_path.write_text(text)

    resp = client.get("/api/review/orphans")
    assert resp.status_code == 200
    orphans = resp.json()
    ids = {o["source_id"] for o in orphans}
    assert "yt-orphan_AB" in ids
    assert "yt-cited_CD" not in ids


def test_orphans_empty_when_no_sources(client, kb_root):
    resp = client.get("/api/review/orphans")
    assert resp.status_code == 200
    assert resp.json() == []


def test_filter_band_returns_sources_between_thresholds(client, kb_root, make_source):
    """A source with filter.score between threshold_review and threshold_include shows up."""
    # Seed a policy with thresholds
    policy_yaml = paths.policies_dir() / "d-band" / "policy.yaml"
    policy_yaml.parent.mkdir(parents=True, exist_ok=True)
    policy_yaml.write_text(
        "version: v1\n"
        "domain:\n"
        "  slug: d-band\n"
        "  topic: t\n"
        "  field: f\n"
        "  description: d\n"
        "filter:\n"
        "  threshold_include: 0.7\n"
        "  threshold_review: 0.5\n"
        "inclusion_criteria: [a]\nexclusion_criteria: [b]\n"
    )

    # Source in the band (score 0.6, between 0.5 and 0.7)
    in_band_text = make_source(
        id_="yt-band_AB",
        domains=["d-band"],
        extra_front={"filter": {"score": 0.6, "policy_version": "v1", "rationale": "x", "decided_at": "2026-05-01T00:00:00Z"}},
    )
    (paths.raw_source_path("youtube", "yt-band_AB")).write_text(in_band_text)

    # Source above threshold_include (score 0.9 — included, not in band)
    above_text = make_source(
        id_="yt-above_AB",
        domains=["d-band"],
        extra_front={"filter": {"score": 0.9, "policy_version": "v1", "rationale": "x", "decided_at": "2026-05-01T00:00:00Z"}},
    )
    (paths.raw_source_path("youtube", "yt-above_AB")).write_text(above_text)

    # Source below threshold_review (score 0.3 — rejected, not in band)
    below_text = make_source(
        id_="yt-below_AB",
        domains=["d-band"],
        extra_front={"filter": {"score": 0.3, "policy_version": "v1", "rationale": "x", "decided_at": "2026-05-01T00:00:00Z"}},
    )
    (paths.raw_source_path("youtube", "yt-below_AB")).write_text(below_text)

    resp = client.get("/api/review/filter-band")
    assert resp.status_code == 200
    band = resp.json()
    ids = {b["source_id"] for b in band}
    assert "yt-band_AB" in ids
    assert "yt-above_AB" not in ids
    assert "yt-below_AB" not in ids


def test_filter_band_empty_when_no_policies(client, kb_root):
    resp = client.get("/api/review/filter-band")
    assert resp.status_code == 200
    assert resp.json() == []
