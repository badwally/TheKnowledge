"""Claim-level contradiction detect + auto-resolve-by-policy (Phase-3 Task 7).

When a deposit's claim contradicts a committed claim on the same referent, the
gate auto-resolves by policy (server-trust-tier desc, then recency desc), records
a reversible provenance act, materializes a CiTO `disputes` edge, and keeps the
down-weighted loser retrievable (eligibility floor). Self-reported trust can NEVER
flip the winner (G5).
"""

from __future__ import annotations

import json
import subprocess

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
    for dom in ("med",):
        pol = tmp_path / ".knowledge" / "policies" / dom
        pol.mkdir(parents=True)
        (pol / "policy.yaml").write_text(f"domain: {dom}\n")
    q = IntentQueue()
    gate = CommitGate(queue=q, embedding_index=EmbeddingIndex())
    return gate, q, EmbeddingIndex()


_PAGE = (
    "---\ntype: entity\ntitle: Ozempic\nentity_kind: drug\n"
    "aliases: [Semaglutide]\ndomains: [med]\n---\n# Overview\nstub.\n\n## Claims\n"
)


def _commit_claim(gate, slug, claim_line, *, source_type, self_reported_trust=None,
                  subject="onset"):
    """Commit a claim onto the entity page. First call mints the page with the
    claim; later calls add a contradicting claim (same subject prefix)."""
    rel = f"wiki/entities/{slug}.md"
    q = gate._queue
    abs_path = gate._root / rel
    if abs_path.exists():
        body = abs_path.read_text().rstrip() + f"\n- {claim_line}\n"
        base_oid = gate._head_blob_oid(rel)
    else:
        body = _PAGE + f"- {claim_line}\n"
        base_oid = "HEAD"
    payload = {"kind": "entity", "target": rel, "claim": claim_line,
               "subject": subject}
    identity = {
        "agent": "tester", "page_type": "entity", "entity_kind": "drug",
        "canonical_name": "Ozempic", "aliases": ["Semaglutide"],
        "domains": ["med"], "source_type": source_type,
        "claim_subject": subject,
    }
    if self_reported_trust is not None:
        identity["self_reported_trust"] = self_reported_trust
    iid = compute_intent_id(payload, identity, semantics=claim_line)
    intent = Intent(intent_id=iid, payload=payload, identity=identity,
                    head_oid=base_oid)
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")
    base_oids = {rel: base_oid} if base_oid != "HEAD" else {}
    a = AuthoredIntent(intent=intent, writes={rel: body},
                       base_oid=base_oid, base_oids=base_oids)
    return gate.commit(a, q.fencing_token(iid))


def _read_resolution_acts(root):
    p = root / ".knowledge" / "contradictions" / "resolution_acts.jsonl"
    if not p.exists():
        return []
    return [json.loads(ln) for ln in p.read_text().splitlines() if ln.strip()]


def test_claim_contradiction_auto_resolves_with_reversible_act(tmp_commit_env):
    gate, queue, emb = tmp_commit_env
    _commit_claim(gate, "ozempic", "onset is rapid [[sources/pubmed-1]]",
                  source_type="pubmed")
    _commit_claim(gate, "ozempic", "onset is slow [[sources/web-9]]",
                  source_type="web")
    acts = _read_resolution_acts(gate._root)
    assert len(acts) == 1, acts
    act = acts[0]
    assert act["rule"] == "trust-tier-then-recency"
    assert act["policy_version"]
    assert act["winner"]["source"] == "pubmed-1"  # higher server trust wins
    body = (gate._root / "wiki/entities/ozempic.md").read_text()
    assert "disputes" in body, body
    # loser stays retrievable (eligibility floor) — not deleted, only down-weighted
    assert "onset is slow" in body, body
    assert "onset is rapid" in body, body


def test_self_reported_trust_cannot_flip_contradiction_winner(tmp_commit_env):
    gate, queue, emb = tmp_commit_env
    _commit_claim(gate, "ozempic", "onset is rapid [[sources/pubmed-1]]",
                  source_type="pubmed")
    # web source self-reports trust=1.0 in its intent payload — must be IGNORED.
    _commit_claim(gate, "ozempic", "onset is slow [[sources/web-9]]",
                  source_type="web", self_reported_trust=1.0)
    act = _read_resolution_acts(gate._root)[-1]
    assert act["winner"]["source"] == "pubmed-1"  # server tier wins; self-report ignored


def test_disputes_edge_points_at_loser_when_new_claim_wins(tmp_commit_env):
    """Review I1: when the NEW claim is the higher-trust winner, the materialized
    CiTO `disputes` edge must point at the EXISTING (loser) source, not the new
    one. The hardcoded `loser_src = new` mislabels the winner as contested."""
    gate, queue, emb = tmp_commit_env
    # Existing claim is low-trust (web); the incoming claim is high-trust (pubmed)
    # and WINS by server trust → the loser is the existing web source.
    _commit_claim(gate, "ozempic", "onset is slow [[sources/web-9]]",
                  source_type="web")
    _commit_claim(gate, "ozempic", "onset is rapid [[sources/pubmed-1]]",
                  source_type="pubmed")
    act = _read_resolution_acts(gate._root)[-1]
    assert act["winner"]["source"] == "pubmed-1"  # new claim wins
    assert act["loser"]["source"] == "web-9"
    body = (gate._root / "wiki/entities/ozempic.md").read_text()
    # The disputes edge cites the LOSER (web-9), not the winner (pubmed-1).
    assert "[[sources/web-9|disputes]]" in body, body
    assert "[[sources/pubmed-1|disputes]]" not in body, body


def test_non_contradicting_claims_do_not_auto_resolve(tmp_commit_env):
    # Negative control: two claims with DIFFERENT subjects union cleanly, no
    # contradiction act recorded.
    gate, queue, emb = tmp_commit_env
    _commit_claim(gate, "ozempic", "onset is rapid [[sources/pubmed-1]]",
                  source_type="pubmed", subject="onset")
    _commit_claim(gate, "ozempic", "half-life is long [[sources/web-9]]",
                  source_type="web", subject="half-life")
    assert _read_resolution_acts(gate._root) == []
    body = (gate._root / "wiki/entities/ozempic.md").read_text()
    assert "onset is rapid" in body and "half-life is long" in body
