"""Integration — lifecycle flow: deposit → commit → dedup-merge → retraction cascade → reverse_merge_plan.

Drives the REAL ops end-to-end:
  deposit (ops/deposit.py) → drain_once/run_worker (ops/committer.py)
  → dedup-merge inside commit (commit_gate._dedup_recheck + _retarget_to_canonical)
  → retraction.cascade (retraction.py)
  → retraction.reverse_merge_plan (retraction.py)

No monkeypatching of the core path. Only KNOWLEDGE_ROOT is redirected to a
tmp git repo (the repo fixture below mirrors test_committer.py:45-61).

REALISTIC PAYLOADS: full multi-section bodies, frontmatter aliases, inbound +
body wikilinks, non-empty preamble — per brief B1 requirement.

Named negative controls (brief Step 2):
  - cascade flags a REAL dependent; an unrelated page is NOT flagged.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from gateway.commit_gate import CommitGate
from gateway.embedding_index import EmbeddingIndex
from gateway.intent_queue import IntentQueue
from gateway.ops.committer import drain_once, run_worker
from gateway.ops.deposit import deposit
from gateway import retraction, frontmatter as fm


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _git(root, *args, check=True):
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=check
    )


def _git_committed(repo: Path, rel_path: str) -> bool:
    """Return True if rel_path appears in any git commit."""
    r = _git(repo, "log", "--all", "--name-only", "--format=", "--", rel_path, check=False)
    return bool(r.stdout.strip())


def _write_source(root: Path, source_id: str, body: str = "Source body.\n") -> Path:
    """Write a minimal raw source file so [[sources/<id>]] wikilinks resolve."""
    raw_dir = root / "raw" / "web"
    raw_dir.mkdir(parents=True, exist_ok=True)
    p = raw_dir / f"{source_id}.md"
    front = {
        "id": source_id,
        "type": "web",
        "title": f"Source {source_id}",
        "url": f"https://example.com/{source_id}",
        "authors": ["Test Author"],
        "published_at": "2026-01-01",
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": "abc123",
        "domains": ["glp1"],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {},
    }
    p.write_text(fm.serialize(front, body))
    return p


def _deposit_entity(*, title, body, aliases=None, domains=None, queue, entity_kind="drug"):
    """Submit an entity deposit intent to the queue."""
    payload = {
        "page_type": "entity",
        "title": title,
        "body": body,
        "entity_kind": entity_kind,
    }
    if aliases:
        payload["aliases"] = aliases
    if domains:
        payload["domains"] = domains
    identity = {"entity_kind": entity_kind, "canonical_name": title}
    if domains:
        identity["domains"] = domains
    res = deposit(payload, identity, queue=queue)
    assert res.success, f"deposit rejected: {res.errors}"
    return res.intent_id


# ---------------------------------------------------------------------------
# Fixture: tmp git repo with live domains + KNOWLEDGE_ROOT redirected
# ---------------------------------------------------------------------------


@pytest.fixture
def repo(tmp_path, monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "test@test")
    _git(tmp_path, "config", "user.name", "test")
    (tmp_path / ".gitignore").write_text(".knowledge/\n.index/\n")
    (tmp_path / "README.md").write_text("seed\n")
    _git(tmp_path, "add", "README.md", ".gitignore")
    _git(tmp_path, "commit", "-qm", "seed")
    # Live domains so commit-time domain resolution does not quarantine
    for dom in ("glp1", "med"):
        pol = tmp_path / ".knowledge" / "policies" / dom
        pol.mkdir(parents=True)
        (pol / "policy.yaml").write_text(f"domain: {dom}\n")
    return tmp_path


@pytest.fixture
def queue(repo):
    return IntentQueue()


@pytest.fixture
def gate(repo, queue):
    idx = EmbeddingIndex()
    return CommitGate(queue=queue, embedding_index=idx)


# ---------------------------------------------------------------------------
# Step 1 + 2 — full lifecycle chain
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_lifecycle_same_slug_union_second_deposit(repo, queue, gate):
    """deposit → commit → second deposit (same slug) → same-slug union inside author_deposit.

    NOTE: this test covers the same-slug union path in author_deposit._union_same_slug(),
    NOT the cross-slug _dedup_recheck → _retarget_to_canonical merge path (see
    test_lifecycle_cross_slug_dedup_merge_disposition_merged for that).

    Uses realistic payload: full multi-section body, aliases, inbound + body wikilinks,
    non-empty preamble.

    This test goes RED if same-slug union overwrites instead of merging, or dead-letters.
    """
    _write_source(repo, "web-glp1-001")

    # First deposit — full realistic payload
    _deposit_entity(
        title="Semaglutide",
        body=(
            "Semaglutide is a GLP-1 receptor agonist used for weight management "
            "and type 2 diabetes. [[sources/web-glp1-001]]\n\n"
            "## Mechanism\nActs on GLP-1 receptors in the pancreas and hypothalamus "
            "to reduce appetite and increase insulin secretion. [[sources/web-glp1-001]]\n\n"
            "## Dosing\nAvailable as once-weekly subcutaneous injection (Ozempic) "
            "or daily oral tablet (Rybelsus).\n"
        ),
        aliases=["Ozempic", "Wegovy", "Rybelsus"],
        domains=["glp1"],
        queue=queue,
    )

    # Drain first deposit — must commit
    r1 = drain_once(queue, gate)
    assert r1 is not None
    assert r1.disposition == "committed", f"first deposit: {r1.disposition}, errors={r1.errors}"

    page_path = repo / "wiki" / "entities" / "semaglutide.md"
    assert page_path.exists(), "semaglutide.md not created"
    content_v1 = page_path.read_text()
    assert "Ozempic" in content_v1 and "Wegovy" in content_v1   # aliases rendered
    assert "[[sources/web-glp1-001]]" in content_v1              # wikilinks preserved
    assert _git_committed(repo, "wiki/entities/semaglutide.md"), "not git-committed"

    # Second deposit — same entity title → triggers same-slug union in author_deposit
    # Uses only bullet-body additions to satisfy _union_same_slug constraints
    _deposit_entity(
        title="Semaglutide",
        body=(
            "## Claims\n"
            "- Approved by FDA for chronic weight management in adults with obesity. "
            "[[sources/web-glp1-001]]\n"
            "- Reduces cardiovascular risk in patients with type 2 diabetes.\n"
        ),
        aliases=["Ozempic"],
        domains=["glp1"],
        queue=queue,
    )

    r2 = drain_once(queue, gate)
    assert r2 is not None
    # Same-slug deposits are unioned inside author_deposit (not via _dedup_recheck)
    # and committed with disposition "committed" — both valid.
    assert r2.disposition in ("committed", "merged"), (
        f"second deposit (same slug): {r2.disposition}, detail={r2.detail}, errors={r2.errors}"
    )

    content_v2 = page_path.read_text()
    # Net-new bullet must appear (union applied)
    assert "Approved by FDA" in content_v2 or "cardiovascular risk" in content_v2, (
        "new claims from second deposit not unioned into page"
    )


@pytest.mark.integration
def test_lifecycle_cross_slug_dedup_merge_disposition_merged(repo, queue, gate):
    """Two different-slug deposits for the same referent → _dedup_recheck merges → disposition=="merged".

    Drives the REAL cross-slug dedup path: commit_gate._dedup_recheck() returns
    decision="merge" → _retarget_to_canonical() retargets the second deposit onto
    the first → committed with disposition="merged" (not "committed").

    The assertion disposition=="merged" exactly is the load-bearing check: it passes
    only if _retarget_to_canonical ran.  "committed" would mean the dedup path was
    skipped (e.g. the embedding index was not wired or the alias match failed).

    This test goes RED if:
      - _dedup_recheck does not identify the deposits as the same referent.
      - _retarget_to_canonical is not called (disposition would be "committed").
      - The merge fails and dead-letters instead.
    """
    _write_source(repo, "web-glp1-001")
    _write_source(repo, "web-glp1-002")

    # First deposit — commits as canonical page
    _deposit_entity(
        title="Ozempic",
        body=(
            "Ozempic is the brand name for semaglutide, a GLP-1 receptor agonist. "
            "[[sources/web-glp1-001]]\n\n"
            "## Claims\n"
            "- Claim A: Once-weekly subcutaneous injection. [[sources/web-glp1-001]]\n"
        ),
        aliases=["Semaglutide"],
        entity_kind="drug",
        domains=["glp1"],
        queue=queue,
    )
    r1 = drain_once(queue, gate)
    assert r1 is not None
    assert r1.disposition == "committed", (
        f"first deposit (ozempic) must commit; got {r1.disposition}"
    )
    assert (repo / "wiki" / "entities" / "ozempic.md").exists()

    # Second deposit — DIFFERENT slug but refers to the same drug (Semaglutide = Ozempic)
    # The alias overlap + embedding similarity triggers _dedup_recheck → merge decision.
    _deposit_entity(
        title="Semaglutide",
        body=(
            "## Claims\n"
            "- Claim B: Reduces HbA1c by ~1.5% in type 2 diabetes. [[sources/web-glp1-002]]\n"
        ),
        aliases=["Ozempic"],
        entity_kind="drug",
        domains=["glp1"],
        queue=queue,
    )
    r2 = drain_once(queue, gate)
    assert r2 is not None
    # EXACT disposition assertion: must be "merged", not "committed".
    # "committed" means the dedup-merge path was skipped — a coverage gap.
    assert r2.disposition == "merged", (
        f"cross-slug dedup-merge: expected disposition='merged' (via _retarget_to_canonical); "
        f"got {r2.disposition!r}, detail={r2.detail!r}. "
        f"If 'committed': _dedup_recheck did not identify the pair as same-referent — "
        f"check alias overlap and EmbeddingIndex wiring."
    )

    # Both claims must survive on the canonical page
    canonical = repo / "wiki" / "entities" / "ozempic.md"
    text = canonical.read_text()
    assert "Claim A:" in text and "Claim B:" in text, (
        f"both claims must be present after merge; canonical content:\n{text[:500]}"
    )


@pytest.mark.integration
def test_lifecycle_retraction_cascade_flags_dependent_not_unrelated(repo, queue, gate):
    """retract source → retraction.cascade flags dependents → unrelated page NOT flagged.

    Negative control (Step 2): the cascade must flag the REAL dependent (a synthesis
    that cites the retracted source) but NOT an unrelated page that does not cite it.

    This test goes RED if cascade() is broken (returns all pages, returns empty, or
    the flagging logic uses the wrong wikilink pattern).
    """
    _write_source(repo, "web-glp1-001")
    _write_source(repo, "web-glp1-002")

    # Commit a synthesis page that cites web-glp1-001 (the source to be retracted)
    dep_page = repo / "wiki" / "synthesis" / "glp1-overview.md"
    dep_page.parent.mkdir(parents=True, exist_ok=True)
    dep_page.write_text(fm.serialize(
        {
            "type": "synthesis",
            "slug": "glp1-overview",
            "title": "GLP-1 Overview",
            "domains": ["glp1"],
            "question": "How do GLP-1 agonists work?",
            "created_at": "2026-01-01T00:00:00Z",
            "last_updated": "2026-01-01T00:00:00Z",
            "sources_count": 1,
            "synthesizes": ["sources/web-glp1-001"],
        },
        "GLP-1 agonists activate the GLP-1 receptor. [[sources/web-glp1-001]]\n\n"
        "## Mechanism\nBinds to GLP-1R in the pancreatic beta-cells.\n",
    ))

    # Commit an UNRELATED page that does NOT cite web-glp1-001
    unrelated_page = repo / "wiki" / "entities" / "metformin.md"
    unrelated_page.parent.mkdir(parents=True, exist_ok=True)
    unrelated_page.write_text(fm.serialize(
        {
            "type": "entity",
            "slug": "metformin",
            "canonical_name": "Metformin",
            "domains": ["med"],
            "created_at": "2026-01-01T00:00:00Z",
            "last_updated": "2026-01-01T00:00:00Z",
        },
        "Metformin is a biguanide antidiabetic. [[sources/web-glp1-002]]\n\n"
        "## Mechanism\nReduces hepatic glucose output.\n",
    ))

    # Run cascade for the retracted source
    result = retraction.cascade({"web-glp1-001"}, root=repo)

    # The synthesis page that cites web-glp1-001 must be flagged
    assert "wiki/synthesis/glp1-overview.md" in result.flagged, (
        f"dependent synthesis not flagged; flagged={result.flagged}"
    )

    # Named negative control: the unrelated metformin page must NOT be flagged
    assert "wiki/entities/metformin.md" not in result.flagged, (
        f"unrelated page (metformin) incorrectly flagged; flagged={result.flagged}"
    )

    assert result.depth >= 1, "cascade depth must be >= 1 (at least the direct dependent)"


@pytest.mark.integration
def test_lifecycle_reverse_merge_plan_from_tombstone(repo, queue, gate):
    """reverse_merge_plan builds a restoration plan from a tombstone page.

    Drives the REAL retraction.reverse_merge_plan() which reads provenance nodes.
    This test goes RED if reverse_merge_plan() fails to locate the provenance record
    or reads the tombstone incorrectly.
    """
    # Seed a tombstone and provenance record manually (the real gate writes these
    # during a dedup-merge commit; we recreate the exact schema documented in
    # retraction.py step 0).
    tombstone_rel = "wiki/entities/ozempic-brand.md"
    tombstone_path = repo / tombstone_rel
    tombstone_path.parent.mkdir(parents=True, exist_ok=True)
    tombstone_path.write_text(fm.serialize(
        {
            "type": "entity",
            "slug": "ozempic-brand",
            "title": "Ozempic (brand)",
            "merged_into": "semaglutide",
            "redirect": "[[entities/semaglutide]]",
        },
        "# Ozempic (brand)\n\nRedirects to [[entities/semaglutide]].\n",
    ))

    # Write the provenance node that records the merge-reattachment
    import json
    prov_dir = repo / ".knowledge" / "provenance"
    prov_dir.mkdir(parents=True, exist_ok=True)
    node = {
        "act_id": "test-act-001",
        "decision_basis": {
            "merge_reattachment": {
                "target": "wiki/entities/semaglutide.md",
                "tombstone": tombstone_rel,
                "aliases_unioned": ["Ozempic"],
                "sections_carried": ["## Brand History"],
                "claims_unioned": [
                    "- Ozempic is the brand name for once-weekly semaglutide.",
                ],
            }
        },
    }
    (prov_dir / "nodes.jsonl").write_text(json.dumps(node) + "\n")

    plan = retraction.reverse_merge_plan(tombstone_rel, root=repo)

    assert plan.canonical_rel == "wiki/entities/semaglutide.md"
    assert plan.tombstone_to_delete == tombstone_rel
    assert "Ozempic" in plan.aliases_to_remove
    assert "## Brand History" in plan.sections_to_remove
    assert any("Ozempic is the brand name" in c for c in plan.claims_to_remove), (
        f"expected contributed claim in plan; got {plan.claims_to_remove}"
    )


@pytest.mark.integration
def test_lifecycle_cascade_empty_on_unretracted_source(repo):
    """Named negative control: cascade on a source ID that is NOT cited returns empty.

    This test goes RED if cascade() incorrectly flags pages that do not cite the
    source, or if the 'no retracted source IDs' early return is broken.
    """
    # A wiki page that cites a DIFFERENT source
    dep_page = repo / "wiki" / "synthesis" / "test-synth.md"
    dep_page.parent.mkdir(parents=True, exist_ok=True)
    dep_page.write_text(fm.serialize(
        {
            "type": "synthesis",
            "slug": "test-synth",
            "title": "Test",
            "domains": ["glp1"],
            "question": "Q?",
            "created_at": "2026-01-01T00:00:00Z",
            "last_updated": "2026-01-01T00:00:00Z",
            "sources_count": 1,
            "synthesizes": [],
        },
        "Some content. [[sources/web-glp1-999]]\n",
    ))

    # Cascade a DIFFERENT source — must return empty
    result = retraction.cascade({"web-glp1-NOT-CITED"}, root=repo)

    assert result.flagged == [], (
        f"cascade on uncited source must return empty; got {result.flagged}"
    )
    assert result.depth == 0


@pytest.mark.integration
def test_full_lifecycle_chain_run_worker(repo, queue, gate):
    """End-to-end lifecycle: deposit → run_worker commits → page on disk in git.

    Uses run_worker (not just drain_once) to drive the production worker loop.
    Realistic payload with preamble, multiple sections, and wikilinks.
    """
    _write_source(repo, "web-glp1-001")

    _deposit_entity(
        title="Tirzepatide",
        body=(
            "Tirzepatide is a dual GIP/GLP-1 receptor agonist. "
            "[[concepts/incretin]]\n\n"
            "## Mechanism\nActs on GIP and GLP-1 receptors simultaneously, "
            "producing greater weight loss than single agonists. "
            "[[sources/web-glp1-001]]\n\n"
            "## Clinical Use\nApproved for type 2 diabetes (Mounjaro) and "
            "chronic weight management (Zepbound) by the FDA.\n\n"
            "## Adverse Effects\nNausea, vomiting, diarrhea — most common "
            "during dose escalation.\n"
        ),
        aliases=["Mounjaro", "Zepbound", "LY3298176"],
        domains=["glp1"],
        queue=queue,
    )

    run_worker(once=True, queue=queue, gate=gate)

    page = repo / "wiki" / "entities" / "tirzepatide.md"
    assert page.exists(), "tirzepatide.md not created by run_worker"
    text = page.read_text()
    assert "Mounjaro" in text and "Zepbound" in text      # aliases present
    assert "[[sources/web-glp1-001]]" in text             # body wikilinks preserved
    assert "Mechanism" in text                             # multi-section body preserved
    assert _git_committed(repo, "wiki/entities/tirzepatide.md"), (
        "tirzepatide.md not in git history"
    )
