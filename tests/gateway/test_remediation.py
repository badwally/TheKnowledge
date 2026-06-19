"""Tests for remediate — G6: de-path never touches a reachable/cited page.

Adversarial tests with named negative controls (standing build rule):
- orphan: zero inbound links, zero provenance references → de-path candidate
- target: zero inbound wiki-links BUT reachable from a provenance node → MUST be skipped
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths, provenance
from gateway.ops.remediate import remediate


def _concept(slug: str, body: str) -> None:
    d = paths.wiki_dir() / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": slug,
        "title": slug,
        "domains": ["med"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    (d / f"{slug}.md").write_text(fm.serialize(front, body))


def _seed_provenance_node(kb_root: Path, rel_path: str) -> None:
    """Write a provenance node whose decision_basis references the given rel_path.

    This makes the page reachable from the provenance graph — remediate must not
    de-path it even if it has zero inbound wiki-links.
    """
    abs_path = str(kb_root / rel_path)
    provenance.record(
        "test-intent-target",
        {"canonical_path": abs_path, "policy_version": "test-v1"},
    )


def test_depaths_orphan_but_keeps_zero_inbound_citation_target(kb_root: Path) -> None:
    """G6 core: orphan is de-pathed; zero-inbound provenance-reachable page is skipped."""
    from gateway import search_index

    # 'orphan' has no inbound wiki-links and no provenance reference → candidate
    _concept("orphan", "# orphan\n\nNo links here.\n")
    # 'target' has ZERO inbound wikilinks but is reachable from the provenance graph.
    # A committed intent recorded its canonical_path → it MUST NOT be de-pathed.
    _concept("target", "# target\n\nReal content [[sources/pubmed-1]].\n")
    _seed_provenance_node(kb_root, "wiki/concepts/target.md")

    search_index.refresh(rebuild=True)
    res = remediate(dry_run=True)

    assert res.success, f"remediate failed: {res.errors}"
    assert "wiki/concepts/orphan.md" in res.data["depathed"], (
        "orphan page with no inbound links and no provenance reference "
        "must be a de-path candidate"
    )
    assert "wiki/concepts/target.md" in res.data["skipped_reachable"], (
        "zero-inbound page that IS reachable from provenance graph "
        "must be in skipped_reachable, not depathed"
    )
    assert "wiki/concepts/target.md" not in res.data["depathed"]


def test_page_with_inbound_link_is_not_depathed(kb_root: Path) -> None:
    """Negative control: a page with at least one inbound wiki-link is not de-pathed."""
    from gateway import search_index

    # Create a concept page that another page links to
    _concept("linked-target", "# linked-target\n\nHas an inbound link.\n")
    # Create a linker page that references linked-target
    d = paths.wiki_dir() / "concepts"
    front = {
        "type": "concept",
        "slug": "linker",
        "title": "linker",
        "domains": ["med"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    (d / "linker.md").write_text(
        fm.serialize(front, "# linker\n\nSee [[concepts/linked-target]].\n")
    )
    search_index.refresh(rebuild=True)
    res = remediate(dry_run=True)

    assert res.success
    assert "wiki/concepts/linked-target.md" not in res.data["depathed"], (
        "page with at least one inbound wikilink must never be de-pathed"
    )


def test_dry_run_does_not_submit_intents(kb_root: Path) -> None:
    """dry_run=True must collect candidates but submit NO CommitGate intents."""
    from gateway import search_index

    _concept("stale-orphan", "# stale-orphan\n\nNothing links here.\n")
    search_index.refresh(rebuild=True)

    # Count intents before
    intents_dir = kb_root / ".knowledge" / "intents" / "submitted"
    before = len(list(intents_dir.glob("*.json"))) if intents_dir.exists() else 0

    res = remediate(dry_run=True)

    after = len(list(intents_dir.glob("*.json"))) if intents_dir.exists() else 0
    assert res.success
    assert after == before, (
        f"dry_run=True must not submit any intents; "
        f"submitted count went from {before} to {after}"
    )
    assert "wiki/concepts/stale-orphan.md" in res.data["depathed"]


def test_non_dry_run_submits_depath_intent(kb_root: Path) -> None:
    """non-dry-run submits a provenanced, reversible de-path CommitGate intent."""
    from gateway import search_index
    from gateway.intent_queue import IntentQueue

    _concept("truly-orphaned", "# truly-orphaned\n\nNothing.\n")
    search_index.refresh(rebuild=True)

    res = remediate(dry_run=False)

    assert res.success
    assert "wiki/concepts/truly-orphaned.md" in res.data["depathed"]

    # Verify that an intent was submitted for the de-path
    q = IntentQueue()
    submitted_dir = paths.intents_dir() / "submitted"
    submitted = list(submitted_dir.glob("*.json")) if submitted_dir.exists() else []
    assert len(submitted) >= 1, "de-path intent must be submitted to the intent queue"

    import json
    payloads = [json.loads(p.read_text())["payload"] for p in submitted]
    depath_payloads = [p for p in payloads if p.get("op") == "depath"]
    assert len(depath_payloads) >= 1, "submitted intent must have op='depath'"
    target_payload = next(
        (p for p in depath_payloads
         if p.get("target_rel") == "wiki/concepts/truly-orphaned.md"),
        None,
    )
    assert target_payload is not None, (
        "depath intent must carry target_rel='wiki/concepts/truly-orphaned.md'"
    )
    assert target_payload.get("reversible") is True, "depath intent must be reversible=True"
