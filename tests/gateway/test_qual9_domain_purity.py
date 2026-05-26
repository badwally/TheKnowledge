"""QUAL-9: domain_purity lint check + promote-domain contamination pre-flight."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.lint.domain_purity import run
from gateway.ops.promote_domain import _check_contamination, promote_domain


# --- helpers ----------------------------------------------------------------


def _make_policy(kb_root: Path, domain: str) -> None:
    p = paths.policies_dir() / domain / "policy.yaml"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"domain:\n  slug: {domain}\n")


def _make_wiki_source(kb_root: Path, source_id: str, domains: list[str]) -> Path:
    p = paths.wiki_dir() / "sources" / f"{source_id}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "source",
        "source_id": source_id,
        "source_type": "web",
        "title": f"Source {source_id}",
        "ingested_at": "2026-01-01T00:00:00Z",
        "domains": domains,
    }
    p.write_text(fm.serialize(front, "## Summary\n\nstub\n\n## Key claims\n\nstub\n"))
    return p


def _make_raw_source(kb_root: Path, source_id: str, domains: list[str]) -> Path:
    p = paths.raw_dir() / "web" / f"{source_id}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "id": source_id,
        "type": "web",
        "title": f"Source {source_id}",
        "url": "https://example.com",
        "authors": [],
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": "sha256:" + "0" * 64,
        "domains": domains,
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {},
    }
    p.write_text(fm.serialize(front, "Body content.\n"))
    return p


def _make_proposal(
    kb_root: Path,
    slug: str,
    proposed_domain: str,
    member_sources: list[str],
) -> Path:
    p = paths.wiki_dir() / "proposals" / f"{slug}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "domain-proposal",
        "slug": slug,
        "title": "Test",
        "proposed_domain": proposed_domain,
        "status": "draft",
        "member_sources": member_sources,
        "rationale": "test",
    }
    refs = "\n".join(f"- [[sources/{s}]]" for s in member_sources)
    p.write_text(fm.serialize(front, f"# Test\n\n## Rationale\n\ntest\n\n## Member sources\n\n{refs}\n"))
    return p


# --- domain_purity lint tests -----------------------------------------------


def test_no_blessed_domains_returns_empty(kb_root: Path) -> None:
    _make_wiki_source(kb_root, "src-a", ["alpha", "beta"])
    assert run() == []


def test_single_blessed_domain_no_overlap(kb_root: Path) -> None:
    _make_policy(kb_root, "alpha")
    _make_wiki_source(kb_root, "src-a", ["alpha"])
    assert run() == []


def test_source_in_one_blessed_no_finding(kb_root: Path) -> None:
    _make_policy(kb_root, "alpha")
    _make_policy(kb_root, "beta")
    _make_wiki_source(kb_root, "src-a", ["alpha"])
    assert run() == []


def test_source_in_two_blessed_flagged(kb_root: Path) -> None:
    _make_policy(kb_root, "alpha")
    _make_policy(kb_root, "beta")
    _make_wiki_source(kb_root, "src-a", ["alpha", "beta"])
    findings = run()
    assert len(findings) == 1
    assert findings[0].check == "domain-purity"
    assert findings[0].severity == "warning"
    assert "alpha" in findings[0].message
    assert "beta" in findings[0].message
    assert findings[0].metadata["source_id"] == "src-a"


def test_only_shared_blessed_flagged_unblessed_ignored(kb_root: Path) -> None:
    _make_policy(kb_root, "alpha")
    _make_wiki_source(kb_root, "src-a", ["alpha", "unrelated-non-blessed"])
    assert run() == []


def test_multiple_contaminated_sources(kb_root: Path) -> None:
    _make_policy(kb_root, "alpha")
    _make_policy(kb_root, "beta")
    _make_wiki_source(kb_root, "src-a", ["alpha", "beta"])
    _make_wiki_source(kb_root, "src-b", ["alpha", "beta"])
    _make_wiki_source(kb_root, "src-c", ["alpha"])
    findings = run()
    assert len(findings) == 2


# --- contamination pre-flight tests -----------------------------------------


def test_check_contamination_no_outliers(kb_root: Path) -> None:
    _make_raw_source(kb_root, "web-aaa", ["target-domain"])
    _make_raw_source(kb_root, "web-bbb", [])
    assert _check_contamination(["web-aaa", "web-bbb"], "target-domain") == []


def test_check_contamination_flags_foreign_tagged(kb_root: Path) -> None:
    _make_raw_source(kb_root, "web-aaa", ["other-domain"])
    outliers = _check_contamination(["web-aaa"], "target-domain")
    assert "web-aaa" in outliers


def test_check_contamination_not_flagged_if_includes_proposed(kb_root: Path) -> None:
    _make_raw_source(kb_root, "web-aaa", ["other-domain", "target-domain"])
    assert _check_contamination(["web-aaa"], "target-domain") == []


def test_promote_domain_writes_contamination_warnings(kb_root: Path) -> None:
    _make_raw_source(kb_root, "web-aaa", ["foreign-domain"])
    _make_raw_source(kb_root, "web-bbb", [])
    _make_wiki_source(kb_root, "web-aaa", [])
    _make_wiki_source(kb_root, "web-bbb", [])
    _make_proposal(kb_root, "test-proposal", "new-domain", ["web-aaa", "web-bbb"])

    result = promote_domain("test-proposal")
    assert result.success

    proposal_path = paths.wiki_dir() / "proposals" / "test-proposal.md"
    front, _ = fm.parse(proposal_path.read_text())
    assert front.get("status") == "blessed"
    warnings = front.get("contamination_warnings") or []
    assert "web-aaa" in warnings
    assert "web-bbb" not in warnings
