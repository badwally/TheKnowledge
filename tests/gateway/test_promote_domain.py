"""Tests for `wiki promote-domain` and `wiki demote-domain` (M36)."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import yaml

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops.demote_domain import demote_domain
from gateway.ops.promote_domain import promote_domain
from gateway.ops.reject_proposal import reject_proposal


# --- helpers ---------------------------------------------------------------


def _seed_source(source_id: str, *, source_type: str = "pdf", title: str = "T") -> tuple[Path, Path]:
    """Write both a raw source and a wiki/sources page; return paths."""
    raw_front = {
        "id": source_id,
        "type": source_type,
        "title": title,
        "url": "",
        "authors": [],
        "ingested_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "content_hash": "sha256:" + "0" * 64,
        "domains": [],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {},
    }
    raw_body = "Source body content for the test.\n"
    raw_path = paths.raw_source_path(source_type, source_id)
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.write_text(fm.serialize(raw_front, raw_body))

    wiki_front = {
        "type": "source",
        "source_id": source_id,
        "source_type": source_type,
        "title": title,
        "ingested_at": raw_front["ingested_at"],
        "domains": [],
    }
    wiki_body = (
        f"# {title}\n\n## Summary\n\nstub\n\n## Key claims\n\nstub\n\n"
        f"## Cross-references\n\n(none)\n"
    )
    wiki_path = paths.wiki_source_path(source_id)
    wiki_path.parent.mkdir(parents=True, exist_ok=True)
    wiki_path.write_text(fm.serialize(wiki_front, wiki_body))
    return raw_path, wiki_path


def _seed_proposal(
    *,
    slug: str = "proposal-test",
    proposed_domain: str = "test-domain",
    member_sources: list[str] | None = None,
    status: str = "draft",
) -> Path:
    members = member_sources or ["pdf-aaa", "pdf-bbb"]
    front = {
        "type": "domain-proposal",
        "slug": slug,
        "title": "Test cluster",
        "proposed_domain": proposed_domain,
        "status": status,
        "member_sources": members,
        "rationale": "Test cluster for promotion.",
    }
    refs = "\n".join(f"- [[sources/{s}]]: member" for s in members)
    body = f"# Test cluster\n\n## Rationale\n\nbody\n\n## Member sources\n\n{refs}\n"
    path = paths.wiki_dir() / "proposals" / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(fm.serialize(front, body))
    return path


# --- promote_domain --------------------------------------------------------


def test_promote_domain_writes_policy_and_back_tags(kb_root):
    _seed_source("pdf-aaa")
    _seed_source("pdf-bbb")
    _seed_proposal(member_sources=["pdf-aaa", "pdf-bbb"], proposed_domain="test-domain")

    result = promote_domain("proposal-test")

    assert result.success, result.errors

    # Policy file exists with expected structure
    policy_path = paths.policies_dir() / "test-domain" / "policy.yaml"
    assert policy_path.exists()
    policy = yaml.safe_load(policy_path.read_text())
    assert policy["domain"]["slug"] == "test-domain"
    assert policy["auto_generated"] is True

    # Member sources back-tagged in BOTH raw/ and wiki/sources/
    for sid in ("pdf-aaa", "pdf-bbb"):
        raw = paths.raw_source_path("pdf", sid)
        front, _ = fm.parse(raw.read_text())
        assert "test-domain" in (front.get("domains") or [])

        wiki = paths.wiki_source_path(sid)
        front, _ = fm.parse(wiki.read_text())
        assert "test-domain" in (front.get("domains") or [])

    # Proposal status flipped to blessed
    front, _ = fm.parse((paths.wiki_dir() / "proposals" / "proposal-test.md").read_text())
    assert front["status"] == "blessed"


def test_promote_domain_rejects_unknown_proposal(kb_root):
    result = promote_domain("proposal-does-not-exist")
    assert not result.success
    assert any("does-not-exist" in e for e in result.errors)


def test_promote_domain_rejects_already_blessed_proposal(kb_root):
    _seed_source("pdf-aaa")
    _seed_proposal(member_sources=["pdf-aaa"], status="blessed")
    result = promote_domain("proposal-test")
    assert not result.success
    assert any("status" in e and "blessed" in e for e in result.errors)


def test_promote_domain_rejects_when_policy_exists(kb_root):
    _seed_source("pdf-aaa")
    _seed_proposal(member_sources=["pdf-aaa"], proposed_domain="test-domain")
    # Pre-create a policy at the target slug
    policy_path = paths.policies_dir() / "test-domain" / "policy.yaml"
    policy_path.parent.mkdir(parents=True, exist_ok=True)
    policy_path.write_text("version: v1\ndomain:\n  slug: test-domain\n")
    result = promote_domain("proposal-test")
    assert not result.success
    assert any("policy" in e and "exists" in e for e in result.errors)


def test_promote_domain_atomicity_when_member_source_missing(kb_root):
    """If any listed member source is missing, NO files should change."""
    _seed_source("pdf-aaa")
    # pdf-bbb intentionally not seeded
    _seed_proposal(member_sources=["pdf-aaa", "pdf-bbb"])

    result = promote_domain("proposal-test")
    assert not result.success

    # Policy must NOT exist
    assert not (paths.policies_dir() / "test-domain" / "policy.yaml").exists()
    # The seeded member must NOT have been tagged
    front, _ = fm.parse(paths.raw_source_path("pdf", "pdf-aaa").read_text())
    assert front.get("domains") == []
    # Proposal must remain in draft state
    front, _ = fm.parse((paths.wiki_dir() / "proposals" / "proposal-test.md").read_text())
    assert front["status"] == "draft"


def test_promote_domain_preserves_source_body_immutability(kb_root):
    _seed_source("pdf-aaa")
    _seed_proposal(member_sources=["pdf-aaa"])

    raw_before = paths.raw_source_path("pdf", "pdf-aaa").read_text()
    _, body_before = fm.parse(raw_before)

    promote_domain("proposal-test")

    raw_after = paths.raw_source_path("pdf", "pdf-aaa").read_text()
    _, body_after = fm.parse(raw_after)
    assert body_before == body_after


# --- demote_domain ---------------------------------------------------------


def test_demote_domain_reverses_promotion(kb_root):
    _seed_source("pdf-aaa")
    _seed_source("pdf-bbb")
    _seed_proposal(member_sources=["pdf-aaa", "pdf-bbb"], proposed_domain="test-domain")

    promote_domain("proposal-test")
    # Sanity
    assert (paths.policies_dir() / "test-domain" / "policy.yaml").exists()

    result = demote_domain("test-domain")
    assert result.success, result.errors

    # Policy gone
    assert not (paths.policies_dir() / "test-domain" / "policy.yaml").exists()

    # Member sources untagged
    for sid in ("pdf-aaa", "pdf-bbb"):
        front, _ = fm.parse(paths.raw_source_path("pdf", sid).read_text())
        assert "test-domain" not in (front.get("domains") or [])
        front, _ = fm.parse(paths.wiki_source_path(sid).read_text())
        assert "test-domain" not in (front.get("domains") or [])

    # Proposal flipped back to draft
    front, _ = fm.parse((paths.wiki_dir() / "proposals" / "proposal-test.md").read_text())
    assert front["status"] == "draft"


def test_demote_domain_rejects_unknown_domain(kb_root):
    result = demote_domain("never-promoted")
    assert not result.success


# --- reject_proposal -------------------------------------------------------


def test_reject_proposal_deletes_draft(kb_root):
    _seed_proposal(slug="proposal-junk")
    path = paths.wiki_dir() / "proposals" / "proposal-junk.md"
    assert path.exists()

    result = reject_proposal("proposal-junk")
    assert result.success, result.errors
    assert not path.exists()


def test_reject_proposal_refuses_blessed(kb_root):
    _seed_proposal(slug="proposal-was-blessed", status="blessed")
    result = reject_proposal("proposal-was-blessed")
    assert not result.success
    assert any("blessed" in e for e in result.errors)
    # File still on disk
    assert (paths.wiki_dir() / "proposals" / "proposal-was-blessed.md").exists()


def test_reject_proposal_unknown(kb_root):
    result = reject_proposal("never-existed")
    assert not result.success
