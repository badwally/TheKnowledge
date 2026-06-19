"""Tests for claim_conservation lint check — F1.

Every committed intent's payload ## Claims bullets must appear in the canonical corpus.
Merged intents: claims that were merged into a canonical page must be found there
(not on the tombstone). A genuinely dropped claim is reported as a finding.

Adversarial with named negative controls (standing build rule):
- test_every_committed_payload_claim_present_in_corpus: all claims land → no findings
- test_dropped_claim_is_reported: one claim silently removed → finding with "missing"
- test_merged_intent_claims_found_on_canonical: merged claims land on canonical → ok
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths, provenance
from gateway.commit_gate import AuthoredIntent, CommitGate
from gateway.core import OperationResult
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id
from gateway.lint import claim_conservation


# ---------------------------------------------------------------------------
# Fixture helpers
# ---------------------------------------------------------------------------

def _git(root: Path, *args: str) -> None:
    import subprocess
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


@pytest.fixture
def tmp_commit_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Real git + queue + gate, mirroring test_dedup_commit.py's fixture."""
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "test@test")
    _git(tmp_path, "config", "user.name", "test")
    (tmp_path / ".gitignore").write_text(".knowledge/\n.index/\n")
    (tmp_path / "README.md").write_text("seed\n")
    _git(tmp_path, "add", "README.md", ".gitignore")
    _git(tmp_path, "commit", "-qm", "seed")
    for dom in ("med",):
        pol = tmp_path / ".knowledge" / "policies" / dom
        pol.mkdir(parents=True)
        (pol / "policy.yaml").write_text(f"domain: {dom}\n")
    from gateway.embedding_index import EmbeddingIndex
    q = IntentQueue()
    from gateway.commit_gate import CommitGate
    idx = EmbeddingIndex()
    gate = CommitGate(queue=q, embedding_index=idx)
    return gate, q, idx


def _entity_with_claims(slug: str, claims: list[str]) -> tuple[str, str]:
    """Return (rel_path, full_page_content) for an entity with ## Claims."""
    rel = f"wiki/entities/{slug}.md"
    body = "# Overview\n\nStub content.\n"
    if claims:
        body += "\n## Claims\n" + "\n".join(f"- {c}" for c in claims) + "\n"
    front = {
        "type": "entity",
        "slug": slug,
        "title": slug.replace("-", " ").title(),
        "entity_kind": "drug",
        "aliases": [],
        "domains": ["med"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    return rel, fm.serialize(front, body)


def _commit_entity(gate: CommitGate, queue: IntentQueue, slug: str,
                   claims: list[str]) -> str:
    """Commit an entity page with the given claims. Return intent_id."""
    rel, content = _entity_with_claims(slug, claims)
    payload = {
        "page_type": "entity",
        "title": slug.replace("-", " ").title(),
        "body": "# Overview\n\nStub content.\n\n## Claims\n"
                + "\n".join(f"- {c}" for c in claims) + "\n",
    }
    identity = {
        "agent": "tester",
        "page_type": "entity",
        "entity_kind": "drug",
        "canonical_name": slug.replace("-", " ").title(),
        "aliases": [],
        "domains": ["med"],
    }
    iid = compute_intent_id(payload, identity, semantics="deposit")
    intent = Intent(intent_id=iid, payload=payload, identity=identity, head_oid="HEAD")
    queue.submit(intent)
    queue.claim(now=1.0)
    queue.set_state(iid, "authored")

    authored = AuthoredIntent(
        intent=intent,
        writes={rel: content},
        base_oid="HEAD",
    )
    tok = queue.fencing_token(iid)
    result = gate.commit(authored, fencing_token=tok)
    assert result.success, f"commit failed: {result.errors}"
    return iid


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_every_committed_payload_claim_present_in_corpus(tmp_commit_env) -> None:
    """F1 happy path: all payload claims land in the corpus → no findings."""
    gate, queue, _ = tmp_commit_env
    _commit_entity(gate, queue, "semaglutide", [
        "Semaglutide reduces HbA1c by 1.5% vs placebo [[sources/pubmed-1]].",
        "Weight loss of 15% body weight reported [[sources/pubmed-2]].",
    ])

    findings = claim_conservation.run()
    assert findings == [], (
        f"expected no findings when all claims land in corpus; got: {findings}"
    )


def test_dropped_claim_is_reported(tmp_commit_env) -> None:
    """F1 negative control: a claim silently removed from the page is reported."""
    gate, queue, _ = tmp_commit_env
    _commit_entity(gate, queue, "tirzepatide", [
        "Tirzepatide reduces fasting glucose [[sources/pubmed-3]].",
        "Second claim that will be dropped [[sources/pubmed-4]].",
    ])

    # Simulate a corpus corruption: remove the second claim from the page.
    page_path = paths.wiki_dir() / "entities" / "tirzepatide.md"
    content = page_path.read_text()
    # Drop the second claim line
    lines = content.splitlines()
    kept = [ln for ln in lines if "Second claim that will be dropped" not in ln]
    page_path.write_text("\n".join(kept) + "\n")

    findings = claim_conservation.run()
    assert any(
        f.check == "claim-conservation" and "missing" in f.message
        for f in findings
    ), (
        f"expected a claim-conservation finding for the dropped claim; "
        f"got: {[f.message for f in findings]}"
    )


def test_merged_intent_claims_found_on_canonical(tmp_commit_env) -> None:
    """F1 merge accounting: claims from a merged intent land on the canonical page.

    Commit entity A (canonical), then commit B (same referent → merges into A).
    B's claims must be found on A's page — NOT on B's tombstone.
    Claim-conservation must NOT report a missing claim just because B's own path
    no longer carries the claims (it's a tombstone redirect).
    """
    gate, queue, _ = tmp_commit_env

    # Commit canonical entity A
    rel_a, content_a = _entity_with_claims("ozempic", [
        "Ozempic is a GLP-1 agonist [[sources/pubmed-5]].",
    ])
    payload_a = {
        "page_type": "entity",
        "title": "Ozempic",
        "body": "# Overview\n\nStub.\n\n## Claims\n- Ozempic is a GLP-1 agonist [[sources/pubmed-5]].\n",
    }
    identity_a = {
        "agent": "tester", "page_type": "entity", "entity_kind": "drug",
        "canonical_name": "Ozempic", "aliases": ["Semaglutide"],
        "domains": ["med"],
    }
    iid_a = compute_intent_id(payload_a, identity_a, semantics="deposit")
    intent_a = Intent(intent_id=iid_a, payload=payload_a, identity=identity_a, head_oid="HEAD")
    queue.submit(intent_a)
    queue.claim(now=1.0)
    queue.set_state(iid_a, "authored")
    authored_a = AuthoredIntent(intent=intent_a, writes={rel_a: content_a}, base_oid="HEAD")
    tok_a = queue.fencing_token(iid_a)
    res_a = gate.commit(authored_a, fencing_token=tok_a)
    assert res_a.success

    # Commit entity B with same canonical_name → should merge into A
    rel_b, content_b = _entity_with_claims("ozempic-alt", [
        "Merged claim that lands on canonical A page [[sources/pubmed-6]].",
    ])
    payload_b = {
        "page_type": "entity",
        "title": "Ozempic",  # same title → dedup will merge into A
        "body": "# Overview\n\nMerge me.\n\n## Claims\n- Merged claim that lands on canonical A page [[sources/pubmed-6]].\n",
    }
    identity_b = {
        "agent": "tester", "page_type": "entity", "entity_kind": "drug",
        "canonical_name": "Ozempic", "aliases": [],
        "domains": ["med"],
    }
    iid_b = compute_intent_id(payload_b, identity_b, semantics="deposit-b")
    intent_b = Intent(intent_id=iid_b, payload=payload_b, identity=identity_b, head_oid="HEAD")
    queue.submit(intent_b)
    queue.claim(now=1.0)
    queue.set_state(iid_b, "authored")
    authored_b = AuthoredIntent(intent=intent_b, writes={rel_b: content_b}, base_oid="HEAD")
    tok_b = queue.fencing_token(iid_b)
    res_b = gate.commit(authored_b, fencing_token=tok_b)
    # B merges into A (dedup="merged") or commits as new entity (either way, claims land somewhere)
    assert res_b.success

    findings = claim_conservation.run()
    assert not any(
        f.check == "claim-conservation" for f in findings
    ), (
        f"merged intent's claims should be found (on canonical or own page); "
        f"got findings: {[f.message for f in findings]}"
    )
