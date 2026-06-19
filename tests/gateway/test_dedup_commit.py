"""Adjudicator wired into the CommitGate serial phase (Phase-3 Task 4).

C5 write-skew (both claims survive), phantom collision (attach to canonical, not
mint a duplicate), and commit-time dedup during an embedding rebuild (entry-gate
2 — consistent namespace under a real concurrent rebuild, no monkeypatch).

REAL CommitGate over a REAL temp git repo with a REAL EmbeddingIndex.
"""

from __future__ import annotations

import subprocess
import threading

import pytest

from gateway.commit_gate import AuthoredIntent, CommitGate
from gateway.embedding_index import EmbeddingIndex
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id


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
    q = IntentQueue()
    idx = EmbeddingIndex()
    gate = CommitGate(queue=q, embedding_index=idx)
    return gate, q, idx


def _entity_md(title, aliases, kind, claims):
    al = "[" + ", ".join(aliases) + "]"
    body = "# Overview\nstub.\n"
    if claims:
        body += "\n## Claims\n" + "\n".join(f"- {c}" for c in claims) + "\n"
    return (
        f"---\ntype: entity\ntitle: {title}\nentity_kind: {kind}\n"
        f"aliases: {al}\ndomains: [med]\n---\n{body}"
    )


def _authored_entity(intent_id, slug, kind, canonical, aliases, domains,
                     claims=None, q=None):
    claims = claims or []
    rel = f"wiki/entities/{slug}.md"
    payload = {"kind": "entity", "target": rel}
    identity = {
        "agent": "tester", "page_type": "entity", "entity_kind": kind,
        "canonical_name": canonical, "aliases": list(aliases),
        "domains": list(domains),
    }
    iid = compute_intent_id(payload, identity, semantics=intent_id)
    intent = Intent(intent_id=iid, payload=payload, identity=identity, head_oid="HEAD")
    if q is not None:
        q.submit(intent)
        q.claim(now=1.0)
        q.set_state(iid, "authored")
    return AuthoredIntent(
        intent=intent,
        writes={rel: _entity_md(canonical, aliases, kind, claims)},
        base_oid="HEAD",
    )


def _add_claim_intent(intent_id, slug, claim_line, *, base_snapshot, q, gate):
    """Append a claim to an existing entity page (writes the full merged body),
    based on the page's blob OID as authored (concurrent-edit lineage)."""
    rel = f"wiki/entities/{slug}.md"
    base = base_snapshot.writes[rel]
    base_oid = gate._head_blob_oid(rel)
    if "## Claims" in base:
        new_body = base.rstrip() + f"\n- {claim_line}\n"
    else:
        new_body = base.rstrip() + f"\n\n## Claims\n- {claim_line}\n"
    payload = {"kind": "entity", "target": rel, "claim": claim_line}
    identity = {"agent": "tester", "page_type": "entity"}
    iid = compute_intent_id(payload, identity, semantics=intent_id)
    intent = Intent(intent_id=iid, payload=payload, identity=identity, head_oid=base_oid)
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")
    return AuthoredIntent(intent=intent, writes={rel: new_body},
                          base_oid=base_oid, base_oids={rel: base_oid})


def test_phantom_collision_second_intent_merges_not_mints(tmp_commit_env):
    gate, queue, emb = tmp_commit_env
    a = _authored_entity("A", "ozempic", "drug", "Ozempic",
                         ["Semaglutide"], ["med"], q=queue)
    gate.commit(a, fencing_token=queue.fencing_token(a.intent.intent_id))
    # Second intent: same referent, different surface name + slug, same snapshot.
    b = _authored_entity("B", "semaglutide", "drug", "Semaglutide",
                         ["Ozempic"], ["med"], q=queue)
    res = gate.commit(b, fencing_token=queue.fencing_token(b.intent.intent_id))
    assert res.disposition in ("committed", "merged"), res.summary
    pages = list((gate._root / "wiki/entities").glob("*.md"))
    assert len([p for p in pages if p.stem in ("ozempic", "semaglutide")]) == 1
    assert res.canonical_path.stem == "ozempic"


def test_write_skew_two_claims_one_entity_both_survive(tmp_commit_env):
    gate, queue, emb = tmp_commit_env
    base = _authored_entity("A", "ozempic", "drug", "Ozempic",
                            ["Semaglutide"], ["med"],
                            claims=["claim-X [[sources/s1]]"], q=queue)
    gate.commit(base, queue.fencing_token(base.intent.intent_id))
    i1 = _add_claim_intent("C1", "ozempic", "claim-Y [[sources/s2]]",
                           base_snapshot=base, q=queue, gate=gate)
    i2 = _add_claim_intent("C2", "ozempic", "claim-Z [[sources/s3]]",
                           base_snapshot=base, q=queue, gate=gate)
    gate.commit(i1, queue.fencing_token(i1.intent.intent_id))
    gate.commit(i2, queue.fencing_token(i2.intent.intent_id))
    body = (gate._root / "wiki/entities/ozempic.md").read_text()
    assert "claim-Y" in body and "claim-Z" in body and "claim-X" in body, body


def test_genuinely_conflicting_claims_still_dead_letter(tmp_commit_env):
    # Same claim subject, contradictory object → NOT auto-merged; dead-letter.
    gate, queue, emb = tmp_commit_env
    base = _authored_entity("A", "ozempic", "drug", "Ozempic",
                            ["Semaglutide"], ["med"],
                            claims=["onset is rapid [[sources/s1]]"], q=queue)
    gate.commit(base, queue.fencing_token(base.intent.intent_id))
    # A claim intent that REWRITES the body's existing claim to a contradictory
    # object, against the real committed base → not a pure add/add → the claim
    # union refuses it and the gate dead-letters (contradiction handled in Task 7).
    rel = "wiki/entities/ozempic.md"
    base_oid = gate._head_blob_oid(rel)
    conflicting = base.writes[rel].replace("onset is rapid", "onset is slow")
    payload = {"kind": "entity", "target": rel, "claim": "onset is slow"}
    identity = {"agent": "tester", "page_type": "entity"}
    iid = compute_intent_id(payload, identity, semantics="C1")
    intent = Intent(intent_id=iid, payload=payload, identity=identity, head_oid=base_oid)
    queue.submit(intent)
    queue.claim(now=1.0)
    queue.set_state(iid, "authored")
    # Make HEAD diverge from base so the rebase path runs (a separate committed
    # claim addition), then the contradictory rewrite cannot cleanly union.
    sep = _add_claim_intent("SEP", "ozempic", "half-life noted [[sources/s2]]",
                            base_snapshot=base, q=queue, gate=gate)
    gate.commit(sep, queue.fencing_token(sep.intent.intent_id))
    i1 = AuthoredIntent(intent=intent, writes={rel: conflicting},
                        base_oid=base_oid, base_oids={rel: base_oid})
    r1 = gate.commit(i1, queue.fencing_token(iid))
    assert r1.disposition == "dead_lettered", r1.summary


def _seed_entity_pages(gate, queue, n):
    for i in range(n):
        a = _authored_entity(f"seed{i}", f"seed-entity-{i}", "drug",
                             f"SeedDrug{i}", [f"AliasA{i}", f"AliasB{i}"],
                             ["med"], q=queue)
        gate.commit(a, queue.fencing_token(a.intent.intent_id))


def test_commit_time_dedup_during_rebuild_sees_consistent_namespace(tmp_commit_env):
    """Entry gate 2: a commit-time dedup that runs while an embedding rebuild is
    swapping must read either old-complete or new-complete — never a half-state.
    Real EmbeddingIndex, real rebuild, no monkeypatch of os.replace."""
    gate, queue, emb = tmp_commit_env
    # Seed Ozempic first so the dedup MUST find it (merge), plus bulk to make the
    # rebuild take measurable time.
    a = _authored_entity("OZ", "ozempic", "drug", "Ozempic",
                         ["Semaglutide"], ["med"], q=queue)
    gate.commit(a, queue.fencing_token(a.intent.intent_id))
    _seed_entity_pages(gate, queue, n=40)

    errors = []

    def rebuild():
        try:
            emb.rebuild_from_canonical()
        except Exception as e:  # noqa: BLE001
            errors.append(("rebuild", e))

    def dedup_commit():
        try:
            b = _authored_entity("Z", "semaglutide", "drug", "Semaglutide",
                                 ["Ozempic"], ["med"], q=queue)
            res = gate.commit(b, queue.fencing_token(b.intent.intent_id))
            assert res.disposition in ("committed", "merged"), res.summary
        except Exception as e:  # noqa: BLE001
            errors.append(("commit", e))

    t1 = threading.Thread(target=rebuild)
    t2 = threading.Thread(target=dedup_commit)
    t1.start(); t2.start(); t1.join(); t2.join()
    assert not errors, errors
    pages = [p for p in (gate._root / "wiki/entities").glob("*.md")
             if p.stem in ("ozempic", "semaglutide")]
    assert len(pages) == 1, [p.name for p in pages]
