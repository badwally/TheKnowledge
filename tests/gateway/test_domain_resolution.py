"""Multi-label domain resolution + quarantine-on-empty (Phase-3 Task 5, decision 6).

A deposit resolves to one-or-more LIVE domains. An unresolvable deposit (no named
domain is live) is QUARANTINED — never committed untagged.
"""

from __future__ import annotations

import subprocess

import pytest

from gateway.domain_resolve import resolve_domains
from gateway.commit_gate import AuthoredIntent, CommitGate
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id


def test_resolves_all_live_domains_named():
    got = resolve_domains({"domains": ["med", "econ"]}, live_domains=["med", "econ", "law"])
    assert sorted(got) == ["econ", "med"]


def test_unknown_domain_dropped_known_kept():
    got = resolve_domains({"domains": ["med", "ghost"]}, live_domains=["med"])
    assert got == ["med"]


def test_empty_resolution_signals_quarantine():
    assert resolve_domains({"domains": ["ghost"]}, live_domains=["med"]) == []


def test_legacy_single_domain_key_folds_in():
    got = resolve_domains({"domain": "med"}, live_domains=["med", "econ"])
    assert got == ["med"]


def test_dedup_preserves_stable_order():
    got = resolve_domains({"domains": ["econ", "med", "econ"]},
                          live_domains=["med", "econ"])
    assert got == ["econ", "med"]


# --- quarantine integration -------------------------------------------------


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
    # one live domain: med
    pol = tmp_path / ".knowledge" / "policies" / "med"
    pol.mkdir(parents=True)
    (pol / "policy.yaml").write_text("domain: med\n")
    q = IntentQueue()
    gate = CommitGate(queue=q)
    return gate, q, tmp_path


def _authored_source(intent_id, rel, domains, q):
    payload = {"kind": "source", "target": rel}
    identity = {"agent": "tester", "page_type": "source", "domains": list(domains)}
    iid = compute_intent_id(payload, identity, semantics=intent_id)
    intent = Intent(intent_id=iid, payload=payload, identity=identity, head_oid="HEAD")
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")
    content = "---\ntype: source\ntitle: X\n---\n# X\nbody\n"
    return AuthoredIntent(intent=intent, writes={rel: content}, base_oid="HEAD")


def test_no_resolvable_domain_quarantines_not_commits(tmp_commit_env):
    gate, queue, root = tmp_commit_env
    a = _authored_source("Q", "raw/web/x.md", ["ghost"], queue)
    res = gate.commit(a, queue.fencing_token(a.intent.intent_id))
    assert res.disposition == "quarantined", res.summary
    assert not (root / "raw/web/x.md").exists()  # not committed untagged


def test_resolvable_domain_commits(tmp_commit_env):
    gate, queue, root = tmp_commit_env
    a = _authored_source("OK", "raw/web/y.md", ["med"], queue)
    res = gate.commit(a, queue.fencing_token(a.intent.intent_id))
    assert res.disposition == "committed", res.summary
    assert (root / "raw/web/y.md").exists()
