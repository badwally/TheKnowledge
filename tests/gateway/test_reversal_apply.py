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

    # The reversal commit subject keeps the revert( prefix (governance audit:
    # reversal kinds read revert; policy-edit reads policy-edit(<domain>)).
    subject = _git(root, "log", "--format=%s", "-n", "1").stdout.strip()
    assert subject.startswith("revert(librarian-commit):"), (
        f"reversal commit subject must keep the revert( prefix; got {subject!r}"
    )

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


# ===========================================================================
# G8 — REAL merge drives the reattachment record, then reverse (regression guard
# for over-restore of pre-existing aliases). This does NOT fabricate the
# provenance node — it commits A, deposits a same-referent B, lets the real
# dedup/_retarget_to_canonical write the real merge_reattachment, then reverses.
# ===========================================================================

def _authored_entity_richbody(gate, slug, canonical, aliases, body):
    """A same-referent entity deposit with a full body (real-merge driver)."""
    rel = f"wiki/entities/{slug}.md"
    q = gate._queue
    al = "[" + ", ".join(aliases) + "]"
    content = (
        f"---\ntype: entity\ntitle: {canonical}\nentity_kind: drug\n"
        f"canonical_name: {canonical}\naliases: {al}\ndomains: [med]\n---\n{body}"
    )
    payload = {"kind": "entity", "target": rel}
    identity = {
        "agent": "tester", "page_type": "entity", "entity_kind": "drug",
        "canonical_name": canonical, "aliases": list(aliases), "domains": ["med"],
    }
    iid = compute_intent_id(payload, identity, semantics=slug)
    intent = Intent(intent_id=iid, payload=payload, identity=identity, head_oid="HEAD")
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")
    return AuthoredIntent(intent=intent, writes={rel: content}, base_oid="HEAD")


# ===========================================================================
# G6 — de-path applies through the gate (Phase 5 Task 2). The de-path is a
# real CommitGate intent: it removes the page via the commit machinery, records
# a provenanced node, and is REVERSE-applicable (a restore-depath intent brings
# the page back). NO monkeypatch of the core commit path.
# ===========================================================================

def test_depath_removes_page_records_provenance_and_is_reversible(tmp_commit_env):
    """A depath intent through the gate: page gone + provenance node + restorable."""
    from gateway import provenance

    gate, q, root = tmp_commit_env

    # Commit a real orphan page through the gate.
    orphan_rel = "wiki/concepts/orphan.md"
    (root / "wiki" / "concepts").mkdir(parents=True, exist_ok=True)
    orphan_content = (
        "---\ntype: concept\nslug: orphan\ntitle: Orphan\ndomains: [med]\n---\n"
        "# Orphan\n\nNo inbound links and uncited.\n"
    )
    (root / orphan_rel).write_text(orphan_content)
    _git(root, "add", "--", orphan_rel)
    _git(root, "commit", "-qm", "seed orphan")
    assert (root / orphan_rel).exists()

    # Drive the de-path THROUGH the gate.
    payload = {
        "reversal_type": "depath",
        "target_rel": orphan_rel,
        "reversible": True,
        "policy_version": "corpus-rot-depath-policy-v1",
    }
    identity = {"agent": "remediate", "operation": "depath"}
    iid, gate_res = _run_intent_through_gate(gate, q, payload, identity)

    assert gate_res.success, gate_res.errors
    assert gate_res.disposition == "committed"
    # (a) The page is gone from the tree.
    assert not (root / orphan_rel).exists(), "de-path must remove the page"
    # The git tree no longer tracks it.
    tracked = _git(root, "ls-files", "--", orphan_rel).stdout.strip()
    assert tracked == "", f"de-pathed page still tracked: {tracked!r}"

    # (b) A provenance node is recorded for the de-path, carrying the content so a
    #     restore can bring it back (reversibility invariant).
    nodes = provenance.read_nodes()
    depath_nodes = [
        n for n in nodes
        if n["decision_basis"].get("reversal_type") == "depath"
    ]
    assert depath_nodes, f"no de-path provenance node recorded: {nodes}"
    basis = depath_nodes[-1]["decision_basis"]
    assert basis.get("target") == orphan_rel
    assert basis.get("depathed_content"), "node must retain content for restore"

    # (c) A reverse/restore intent restores the page.
    restore_payload = {
        "reversal_type": "restore-depath",
        "target_rel": orphan_rel,
        "content": basis["depathed_content"],
        "policy_version": "corpus-rot-depath-policy-v1",
    }
    restore_identity = {"agent": "remediate", "operation": "restore-depath"}
    riid, restore_res = _run_intent_through_gate(
        gate, q, restore_payload, restore_identity
    )
    assert restore_res.success, restore_res.errors
    assert restore_res.disposition == "committed"
    assert (root / orphan_rel).exists(), "restore-depath must bring the page back"
    restored = (root / orphan_rel).read_text()
    assert "No inbound links and uncited." in restored


def test_depath_missing_target_dead_letters_no_mutation(tmp_commit_env):
    """Negative control: de-pathing a non-existent page dead-letters; no commit."""
    gate, q, root = tmp_commit_env
    head_before = _git(root, "rev-parse", "HEAD").stdout.strip()

    payload = {
        "reversal_type": "depath",
        "target_rel": "wiki/concepts/does-not-exist.md",
        "reversible": True,
        "policy_version": "corpus-rot-depath-policy-v1",
    }
    identity = {"agent": "remediate", "operation": "depath"}
    iid, gate_res = _run_intent_through_gate(gate, q, payload, identity)

    assert not gate_res.success
    assert gate_res.disposition == "dead_lettered"
    head_after = _git(root, "rev-parse", "HEAD").stdout.strip()
    assert head_after == head_before


def test_real_merge_then_reverse_preserves_preexisting_aliases(tmp_commit_env):
    """CRITICAL regression: a reverse-merge must NOT delete aliases that predated
    the merge. Drives the REAL merge so the REAL merge_reattachment record is
    written, then reverses through the gate."""
    from gateway import frontmatter as fm

    gate, q, root = tmp_commit_env

    # Canonical A with a PRE-EXISTING alias "Semaglutide".
    _commit_entity(
        gate, "ozempic", "Ozempic", ["Semaglutide"],
        "# Overview\nstub.\n\n## Claims\n- claim-X [[sources/s1]]\n",
    )

    # Same-referent deposit B brings its OWN aliases "Wegovy" + a new section.
    rich_body = (
        "# Overview\nstub.\n\n"
        "## Mechanism\nActs as a GLP-1 agonist; see [[entities/glp1]].\n\n"
        "## Claims\n- claim-Y [[sources/s2]]\n"
    )
    dep = _authored_entity_richbody(
        gate, "semaglutide", "Semaglutide", ["Wegovy"], rich_body
    )
    res = gate.commit(dep, q.fencing_token(dep.intent.intent_id))
    # Require the real merge to have happened (else the regression cannot be guarded).
    assert res.disposition == "merged", (
        f"expected real merge, got {res.disposition}: {res.summary}"
    )

    canonical_rel = "wiki/entities/ozempic.md"
    tombstone_rel = "wiki/entities/semaglutide.md"
    assert (root / tombstone_rel).exists(), "no tombstone after real merge"

    # Sanity: pre-existing alias + B's alias both on the canonical post-merge.
    front_pre, _ = fm.parse((root / canonical_rel).read_text())
    assert "Semaglutide" in (front_pre.get("aliases") or [])
    assert "Wegovy" in (front_pre.get("aliases") or [])

    # Reverse-merge THROUGH the gate.
    payload = {
        "reversal_type": "reverse-merge",
        "tombstone_rel": tombstone_rel,
        "policy_version": "contradiction-reversal-policy-v1",
    }
    identity = {"agent": "tester", "operation": "revert-resolution"}
    iid, gate_res = _run_intent_through_gate(gate, q, payload, identity)
    assert gate_res.success, gate_res.errors
    assert gate_res.disposition == "committed"

    # The PRE-EXISTING alias must SURVIVE; B's contributed alias must be removed.
    front_after, body_after = fm.parse((root / canonical_rel).read_text())
    aliases_after = front_after.get("aliases") or []
    assert "Semaglutide" in aliases_after, (
        f"pre-existing alias deleted by reverse-merge: {aliases_after}"
    )
    assert "Wegovy" not in aliases_after, (
        f"B's alias not removed by reverse-merge: {aliases_after}"
    )
    # B's contributed section/claim removed; A's original survives.
    assert "## Mechanism" not in body_after, body_after
    assert "claim-Y" not in body_after, body_after
    assert "claim-X" in body_after
    # Tombstone deleted.
    assert not (root / tombstone_rel).exists()


# ===========================================================================
# BLOCKER 2 (High, defense-in-depth) — reversal/de-path delete-path containment
# Named negative controls: a traversal rel must DEAD-LETTER, never delete a file
# outside the root. The destructive path (_commit_reversal_writes) must reject
# `..`/absolute and assert resolved-path containment under self._root.
# ===========================================================================

def test_depath_traversal_target_rel_dead_letters_no_delete(tmp_commit_env):
    """A traversal target_rel through _apply_depath must dead-letter, not delete.

    PoC: target_rel="../VICTIM.md" resolves OUTSIDE the root. The de-path delete
    path must reject it (fail closed) and leave the sentinel intact.
    """
    gate, q, root = tmp_commit_env

    # Sentinel file OUTSIDE the root (sibling dir), the traversal target.
    victim = root.parent / "VICTIM.md"
    victim.write_text("do not delete me\n")
    assert victim.exists()

    # The traversal rel must point at the victim from inside the root.
    # _apply_depath reads target_rel and (if it exists) routes to the delete path.
    # Pre-create an in-root file so the existence check passes, then the rel
    # escapes — OR point straight at the victim via "..". We point at the victim:
    payload = {
        "reversal_type": "depath",
        "target_rel": "../VICTIM.md",
        "policy_version": "v1",
    }
    identity = {"agent": "remediate", "operation": "depath"}
    iid, gate_res = _run_intent_through_gate(gate, q, payload, identity)

    assert gate_res.disposition == "dead_lettered", (
        f"traversal de-path must dead-letter; got {gate_res.disposition} "
        f"({gate_res.summary})"
    )
    assert victim.exists(), "traversal de-path DELETED a file outside the root!"
    assert victim.read_text() == "do not delete me\n"


def test_reverse_merge_traversal_tombstone_dead_letters_no_delete(tmp_commit_env):
    """A traversal tombstone through _commit_reversal_writes deletes must be rejected.

    We drive _commit_reversal_writes directly with a traversal delete rel (the
    shared destructive boundary all reversal kinds use), proving the containment
    guard sits at the boundary, not only at one caller.
    """
    gate, q, root = tmp_commit_env

    victim = root.parent / "VICTIM2.md"
    victim.write_text("also do not delete\n")
    assert victim.exists()

    # Register an intent so set_declared_writes/set_state have a record.
    payload = {"reversal_type": "reverse-merge", "tombstone_rel": "x"}
    identity = {"agent": "tester"}
    iid = compute_intent_id(payload, identity, semantics="trav-tombstone")
    intent = Intent(intent_id=iid, payload=payload, identity=identity)
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")

    # Drive the shared destructive boundary with a traversal delete rel.
    result = gate._commit_reversal_writes(
        iid, {}, ["../VICTIM2.md"], {"reversal_type": "reverse-merge"},
        summary="traversal tombstone delete",
    )

    assert result.disposition == "dead_lettered", (
        f"traversal delete must dead-letter; got {result.disposition} ({result.summary})"
    )
    assert victim.exists(), "traversal delete DELETED a file outside the root!"
    assert victim.read_text() == "also do not delete\n"


def test_reversal_writes_traversal_write_rel_dead_letters(tmp_commit_env):
    """A traversal WRITE rel through _commit_reversal_writes must be rejected too."""
    gate, q, root = tmp_commit_env

    escape_target = root.parent / "ESCAPED_WRITE.md"
    assert not escape_target.exists()

    payload = {"reversal_type": "restore-depath", "target_rel": "x"}
    identity = {"agent": "tester"}
    iid = compute_intent_id(payload, identity, semantics="trav-write")
    intent = Intent(intent_id=iid, payload=payload, identity=identity)
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")

    result = gate._commit_reversal_writes(
        iid, {"../ESCAPED_WRITE.md": "pwned\n"}, [], {"reversal_type": "restore-depath"},
        summary="traversal write",
    )

    assert result.disposition == "dead_lettered", (
        f"traversal write must dead-letter; got {result.disposition} ({result.summary})"
    )
    assert not escape_target.exists(), "traversal write CREATED a file outside the root!"


# ===========================================================================
# Producer ops for the two recovery reversal kinds (backlog: reverse-merge /
# restore-depath have no producer op). These drive the REAL producer ->
# REAL committer drain -> REAL gate apply, closing the operator-reachability gap.
# ===========================================================================


def test_reverse_merge_producer_drains_to_restore(tmp_commit_env):
    """`reverse_merge(tombstone_rel)` submits an intent the real committer drains
    into a gate reverse-merge — restoring the canonical and deleting the tombstone.
    Drives a REAL merge first so the reattachment record is genuine."""
    from gateway import frontmatter as fm
    from gateway.ops.reverse_merge import reverse_merge
    from gateway.ops.committer import drain_once

    gate, q, root = tmp_commit_env

    _commit_entity(
        gate, "ozempic", "Ozempic", ["Semaglutide"],
        "# Overview\nstub.\n\n## Claims\n- claim-X [[sources/s1]]\n",
    )
    rich_body = (
        "# Overview\nstub.\n\n## Mechanism\nGLP-1 agonist [[entities/glp1]].\n\n"
        "## Claims\n- claim-Y [[sources/s2]]\n"
    )
    dep = _authored_entity_richbody(gate, "semaglutide", "Semaglutide", ["Wegovy"], rich_body)
    res = gate.commit(dep, q.fencing_token(dep.intent.intent_id))
    assert res.disposition == "merged", f"need a real merge: {res.disposition} {res.summary}"

    canonical_rel = "wiki/entities/ozempic.md"
    tombstone_rel = "wiki/entities/semaglutide.md"
    assert (root / tombstone_rel).exists()

    # PRODUCER submits; REAL committer drains it.
    prod = reverse_merge(tombstone_rel, queue=q)
    assert prod.success, prod.errors
    dr = drain_once(q, gate)
    assert dr is not None and dr.disposition == "committed", dr

    front_after, body_after = fm.parse((root / canonical_rel).read_text())
    aliases_after = front_after.get("aliases") or []
    assert "Semaglutide" in aliases_after  # pre-existing alias survives
    assert "Wegovy" not in aliases_after    # B's alias removed
    assert "claim-Y" not in body_after
    assert "claim-X" in body_after
    assert not (root / tombstone_rel).exists()


def test_reverse_merge_producer_rejects_traversal_rel(tmp_commit_env):
    """Producer-layer containment: a `..`/absolute tombstone_rel is rejected
    BEFORE submission — nothing reaches the queue."""
    from gateway.ops.reverse_merge import reverse_merge

    gate, q, root = tmp_commit_env
    depth_before = q.depth()
    for bad in ("../escape.md", "/etc/passwd", "wiki/../.git/config", "wiki\\..\\.git\\config"):
        out = reverse_merge(bad, queue=q)
        assert not out.success, bad
    assert q.depth() == depth_before, "a rejected producer call must not enqueue"


def test_restore_depath_producer_looks_up_provenance_and_restores(tmp_commit_env):
    """`restore_depath(rel)` finds the recorded depathed_content in provenance and
    submits a restore intent the committer drains — bringing the page back. The
    operator supplies only the rel; content is never caller-injected."""
    from gateway.ops.reverse_merge import restore_depath
    from gateway.ops.committer import drain_once

    gate, q, root = tmp_commit_env

    orphan_rel = "wiki/concepts/orphan.md"
    (root / "wiki" / "concepts").mkdir(parents=True, exist_ok=True)
    orphan_content = (
        "---\ntype: concept\nslug: orphan\ntitle: Orphan\ndomains: [med]\n---\n"
        "# Orphan\n\nNo inbound links and uncited.\n"
    )
    (root / orphan_rel).write_text(orphan_content)
    _git(root, "add", "--", orphan_rel)
    _git(root, "commit", "-qm", "seed orphan")

    # Real de-path (records depathed_content in provenance).
    iid, dres = _run_intent_through_gate(
        gate, q,
        {"reversal_type": "depath", "target_rel": orphan_rel, "reversible": True},
        {"agent": "remediate", "operation": "depath"},
    )
    assert dres.disposition == "committed"
    assert not (root / orphan_rel).exists()

    # PRODUCER restores — content pulled from provenance, not passed in.
    prod = restore_depath(orphan_rel, queue=q)
    assert prod.success, prod.errors
    dr = drain_once(q, gate)
    assert dr is not None and dr.disposition == "committed", dr
    assert (root / orphan_rel).exists()
    assert "No inbound links and uncited." in (root / orphan_rel).read_text()


def test_restore_depath_producer_without_recorded_content_fails(tmp_commit_env):
    """No depath provenance for the rel → producer fails and enqueues nothing
    (cannot restore content it never recorded)."""
    from gateway.ops.reverse_merge import restore_depath

    gate, q, root = tmp_commit_env
    depth_before = q.depth()
    out = restore_depath("wiki/concepts/never-depathed.md", queue=q)
    assert not out.success
    assert q.depth() == depth_before


def test_reversal_write_outside_allowlist_dead_letters(tmp_commit_env):
    """Positive-allowlist containment: a reversal write targeting `.git/hooks/`
    (INSIDE the root, so `_rel_escapes_root` passes it) must still dead-letter —
    reversal writes are confined to wiki/ + .knowledge/policies/. No file written."""
    gate, q, root = tmp_commit_env

    payload = {"reversal_type": "restore-depath", "target_rel": ".git/hooks/post-commit"}
    identity = {"agent": "tester"}
    iid = compute_intent_id(payload, identity, semantics="git-hook-write")
    intent = Intent(intent_id=iid, payload=payload, identity=identity)
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")

    result = gate._commit_reversal_writes(
        iid, {".git/hooks/post-commit": "#!/bin/sh\necho pwned\n"}, [],
        {"reversal_type": "restore-depath"}, summary="git hook write",
    )
    assert result.disposition == "dead_lettered", result.summary
    assert not (root / ".git" / "hooks" / "post-commit").exists()


def test_reverse_merge_restore_depath_are_cli_only():
    """The two recovery producers are destructive undo affordances — CLI-only,
    not on the agent MCP surface (mirrors demote-domain / policy-edit)."""
    from gateway import mcp_server

    assert "reverse-merge" in mcp_server.CLI_ONLY
    assert "restore-depath" in mcp_server.CLI_ONLY
    assert not hasattr(mcp_server, "wiki_reverse_merge")
    assert not hasattr(mcp_server, "wiki_restore_depath")
