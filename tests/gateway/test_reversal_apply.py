"""CommitGate apply-path for reversal-type intents — Phase 5 Task 1 (G1, G3, G8).

End-to-end, real-gate tests (NO monkeypatch of the core commit path). The
reversal must APPLY, not merely enqueue: a contradiction-resolution reversal
removes the materialized ## Contested edge and re-opens the act; a reverse-merge
restores the canonical to its pre-merge state and deletes the tombstone.

Schemas asserted are the REAL ones verified in Step 0 (see retraction.py header).
"""

from __future__ import annotations

import json
import subprocess

import pytest

from gateway.commit_gate import AuthoredIntent, CommitGate
from gateway.embedding_index import EmbeddingIndex
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id
from gateway import contradictions_log
from gateway.ops.revert_resolution import revert_resolution


def _git(root, *args, check=True):
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=check
    )


@pytest.fixture
def tmp_commit_env(tmp_path, monkeypatch):
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
    q = IntentQueue()
    gate = CommitGate(queue=q, embedding_index=EmbeddingIndex())
    return gate, q, tmp_path


_PAGE = (
    "---\ntype: entity\ntitle: Ozempic\nentity_kind: drug\n"
    "aliases: [Semaglutide]\ndomains: [med]\n---\n# Overview\nstub.\n\n## Claims\n"
)


def _commit_claim(gate, slug, claim_line, *, source_type, subject="onset"):
    """Commit a claim onto the entity page (mirrors test_contradiction_resolve)."""
    rel = f"wiki/entities/{slug}.md"
    q = gate._queue
    abs_path = gate._root / rel
    if abs_path.exists():
        body = abs_path.read_text().rstrip() + f"\n- {claim_line}\n"
        base_oid = gate._head_blob_oid(rel)
    else:
        body = _PAGE + f"- {claim_line}\n"
        base_oid = "HEAD"
    payload = {"kind": "entity", "target": rel, "claim": claim_line, "subject": subject}
    identity = {
        "agent": "tester", "page_type": "entity", "entity_kind": "drug",
        "canonical_name": "Ozempic", "aliases": ["Semaglutide"],
        "domains": ["med"], "source_type": source_type, "claim_subject": subject,
    }
    iid = compute_intent_id(payload, identity, semantics=claim_line)
    intent = Intent(intent_id=iid, payload=payload, identity=identity, head_oid=base_oid)
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")
    base_oids = {rel: base_oid} if base_oid != "HEAD" else {}
    a = AuthoredIntent(intent=intent, writes={rel: body}, base_oid=base_oid,
                       base_oids=base_oids)
    return gate.commit(a, q.fencing_token(iid))


def _run_intent_through_gate(gate, q, payload, identity):
    """Submit + claim + author + commit an intent through the real gate."""
    iid = compute_intent_id(payload, identity, semantics="revert")
    intent = Intent(intent_id=iid, payload=payload, identity=identity)
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")
    a = AuthoredIntent(intent=intent, writes={}, base_oid=None)
    return iid, gate.commit(a, q.fencing_token(iid))


# ===========================================================================
# G1 + G3 — contradiction-resolution reversal applies through the gate
# ===========================================================================

def test_contradiction_revert_removes_contested_edge_and_reopens_act(tmp_commit_env):
    gate, q, root = tmp_commit_env
    # Two contradictory claims → auto_resolve writes ## Contested
    _commit_claim(gate, "ozempic", "onset is rapid [[sources/pubmed-1]]",
                  source_type="pubmed")
    _commit_claim(gate, "ozempic", "onset is slow [[sources/web-9]]",
                  source_type="web")

    body_before = (root / "wiki/entities/ozempic.md").read_text()
    assert "## Contested" in body_before
    assert "disputes" in body_before

    acts = contradictions_log.read_resolution_acts()
    assert len(acts) == 1
    act = acts[0]
    act_id = act["act_id"]  # stable id added at write time

    # Submit the revert through the op, then run it THROUGH the gate
    res = revert_resolution(act_id, {"agent": "tester"})
    assert res.disposition == "queued"
    payload = {
        "reversal_type": "contradiction-resolution",
        "reverts_act": act_id,
        "policy_version": "contradiction-reversal-policy-v1",
    }
    identity = {"agent": "tester", "operation": "revert-resolution"}
    iid, gate_res = _run_intent_through_gate(gate, q, payload, identity)

    assert gate_res.success, gate_res.errors
    assert gate_res.disposition == "committed"

    # The ## Contested edge is gone; both claims remain on the page
    body_after = (root / "wiki/entities/ozempic.md").read_text()
    assert "## Contested" not in body_after, body_after
    assert "disputes" not in body_after, body_after
    assert "onset is rapid" in body_after
    assert "onset is slow" in body_after

    # The act is re-opened: acts_to_reopen no longer returns it (reverted marker)
    from gateway import retraction
    reverted_acts = contradictions_log.read_resolution_acts()
    matched = [a for a in reverted_acts if a.get("act_id") == act_id]
    assert matched and matched[0].get("reverts_act") == iid

    # A provenance node links the reverts_act
    from gateway import provenance
    nodes = provenance.read_nodes()
    assert any(n["decision_basis"].get("reverts_act") == act_id for n in nodes), nodes


def test_contradiction_revert_unknown_act_dead_letters_no_mutation(tmp_commit_env):
    """Negative control: reverting an unknown act dead-letters; no corpus change."""
    gate, q, root = tmp_commit_env
    _commit_claim(gate, "ozempic", "onset is rapid [[sources/pubmed-1]]",
                  source_type="pubmed")
    head_before = _git(root, "rev-parse", "HEAD").stdout.strip()

    payload = {
        "reversal_type": "contradiction-resolution",
        "reverts_act": "nonexistent-act-id",
        "policy_version": "contradiction-reversal-policy-v1",
    }
    identity = {"agent": "tester", "operation": "revert-resolution"}
    iid, gate_res = _run_intent_through_gate(gate, q, payload, identity)

    assert not gate_res.success
    assert gate_res.disposition == "dead_lettered"
    # No new commit (corpus unchanged)
    head_after = _git(root, "rev-parse", "HEAD").stdout.strip()
    assert head_after == head_before


# ===========================================================================
# G8 — reverse-merge restores pre-merge state through the gate (realistic)
# ===========================================================================

def _entity_md(title, aliases, kind, body_sections):
    al = "[" + ", ".join(aliases) + "]"
    return (
        f"---\ntype: entity\ntitle: {title}\nentity_kind: {kind}\n"
        f"aliases: {al}\ndomains: [med]\n---\n{body_sections}"
    )


def _commit_entity(gate, slug, title, aliases, body_sections):
    rel = f"wiki/entities/{slug}.md"
    q = gate._queue
    payload = {"kind": "entity", "target": rel}
    identity = {
        "agent": "tester", "page_type": "entity", "entity_kind": "drug",
        "canonical_name": title, "aliases": list(aliases), "domains": ["med"],
    }
    iid = compute_intent_id(payload, identity, semantics=slug)
    intent = Intent(intent_id=iid, payload=payload, identity=identity, head_oid="HEAD")
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")
    a = AuthoredIntent(
        intent=intent,
        writes={rel: _entity_md(title, aliases, "drug", body_sections)},
        base_oid="HEAD",
    )
    return gate.commit(a, q.fencing_token(iid))


def test_reverse_merge_restores_canonical_and_deletes_tombstone(tmp_commit_env):
    """Realistic payload: A canonical + B merged onto it; reverse-merge restores."""
    gate, q, root = tmp_commit_env

    # Canonical A — full multi-section body with body wikilinks
    a_body = (
        "# Semaglutide\n\n"
        "Semaglutide is a GLP-1 receptor agonist [[sources/pubmed-1]].\n\n"
        "## Mechanism\n\nActs on GLP-1R [[sources/pubmed-2]].\n\n"
        "## Claims\n- Reduces HbA1c [[sources/pubmed-1]]\n"
    )
    _commit_entity(gate, "semaglutide", "Semaglutide", ["GLP-1 agonist"], a_body)

    # A separate page B that links INTO the deposit page (inbound wikilink to be restored)
    inbound_rel = "wiki/synthesis/glp1-review.md"
    (root / "wiki" / "synthesis").mkdir(parents=True, exist_ok=True)
    inbound_body = (
        "---\ntype: synthesis\nslug: glp1-review\ntitle: GLP-1 Review\n"
        "domains: [med]\nsynthesizes: [entities/ozempic-brand]\n---\n"
        "# GLP-1 Review\n\nSee [[entities/ozempic-brand]] for the brand entity.\n"
    )
    (root / inbound_rel).write_text(inbound_body)
    _git(root, "add", "--", inbound_rel)
    _git(root, "commit", "-qm", "seed inbound")

    # Simulate the merge of B onto A: write the merged canonical + tombstone, and
    # record the merge_reattachment provenance node — exactly as commit_gate does.
    canonical_rel = "wiki/entities/semaglutide.md"
    tombstone_rel = "wiki/entities/ozempic-brand.md"
    merged_body = (
        "# Semaglutide\n\n"
        "Semaglutide is a GLP-1 receptor agonist [[sources/pubmed-1]].\n\n"
        "## Mechanism\n\nActs on GLP-1R [[sources/pubmed-2]].\n\n"
        "## Claims\n- Reduces HbA1c [[sources/pubmed-1]]\n"
        "- Nausea in 20% of patients [[sources/pubmed-4]]\n\n"
        "## Side Effects\n\nInjection-site reactions [[sources/pubmed-5]].\n"
    )
    merged_front = (
        "---\ntype: entity\ntitle: Semaglutide\nentity_kind: drug\n"
        "aliases: [GLP-1 agonist, Ozempic, semaglutide injection]\ndomains: [med]\n---\n"
    )
    (root / canonical_rel).write_text(merged_front + merged_body)
    tomb = (
        "---\ntype: entity\ntitle: Ozempic Brand\nmerged_into: semaglutide\n"
        "redirect: '[[entities/semaglutide]]'\n---\n"
        "# Ozempic Brand\n\nMerged into [[entities/semaglutide]] (dedup §5.3). "
        "This page is a redirect tombstone.\n"
    )
    (root / tombstone_rel).write_text(tomb)
    _git(root, "add", "--", canonical_rel, tombstone_rel)
    _git(root, "commit", "-qm", "merge B onto A")

    from gateway import provenance
    provenance.record("merge-intent-001", {
        "merge_reattachment": {
            "target": canonical_rel,
            "tombstone": tombstone_rel,
            "aliases_unioned": ["Ozempic", "semaglutide injection"],
            "sections_carried": ["## Side Effects"],
            "claims_unioned": ["- Nausea in 20% of patients [[sources/pubmed-4]]"],
        }
    })

    head_before = _git(root, "rev-parse", "HEAD").stdout.strip()

    # Run the reverse-merge through the gate
    payload = {
        "reversal_type": "reverse-merge",
        "tombstone_rel": tombstone_rel,
        "policy_version": "contradiction-reversal-policy-v1",
    }
    identity = {"agent": "tester", "operation": "revert-resolution"}
    iid, gate_res = _run_intent_through_gate(gate, q, payload, identity)

    assert gate_res.success, gate_res.errors
    assert gate_res.disposition == "committed"

    # Canonical no longer carries B's aliases / sections / claims
    canon_after = (root / canonical_rel).read_text()
    assert "Ozempic" not in canon_after, canon_after
    assert "semaglutide injection" not in canon_after, canon_after
    assert "## Side Effects" not in canon_after, canon_after
    assert "Nausea in 20%" not in canon_after, canon_after
    # The original content survives
    assert "## Mechanism" in canon_after
    assert "Reduces HbA1c" in canon_after

    # The tombstone is deleted
    assert not (root / tombstone_rel).exists()

    # A new commit was made
    head_after = _git(root, "rev-parse", "HEAD").stdout.strip()
    assert head_after != head_before

    # A provenance node records the reverse-merge
    nodes = provenance.read_nodes()
    assert any(
        n["decision_basis"].get("reversal_type") == "reverse-merge"
        for n in nodes
    ), nodes


def test_reverse_merge_non_target_dead_letters_no_mutation(tmp_commit_env):
    """Negative control: reverse-merge on a page that was never a merge target."""
    gate, q, root = tmp_commit_env
    a_body = "# Semaglutide\n\nA drug [[sources/pubmed-1]].\n"
    _commit_entity(gate, "semaglutide", "Semaglutide", ["GLP-1 agonist"], a_body)
    head_before = _git(root, "rev-parse", "HEAD").stdout.strip()

    payload = {
        "reversal_type": "reverse-merge",
        "tombstone_rel": "wiki/entities/semaglutide.md",  # NOT a tombstone
        "policy_version": "contradiction-reversal-policy-v1",
    }
    identity = {"agent": "tester", "operation": "revert-resolution"}
    iid, gate_res = _run_intent_through_gate(gate, q, payload, identity)

    assert not gate_res.success
    assert gate_res.disposition == "dead_lettered"
    head_after = _git(root, "rev-parse", "HEAD").stdout.strip()
    assert head_after == head_before
    # The page is untouched
    assert (root / "wiki/entities/semaglutide.md").exists()
