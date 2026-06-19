"""Production committer: author_deposit + drain_once + run_worker (D0).

Four adversarial scenarios — each with a named negative control:

  1. Autonomous commit (happy path): deposit → drain_once → committed on disk + git.
  2. Crash mid-author, lease reclaim: expired lease is reclaimed by next worker.
  3. Poison intent dead-letters, loop continues: bad intent dead-letters; good follows.
  4. Write-skew two same-entity deposits both survive: union, not last-writer-wins.

Real fcntl locks, real git repo, real CommitGate — no monkeypatching of core path.
Redirect only KNOWLEDGE_ROOT (via monkeypatch.setenv).
"""

from __future__ import annotations

import subprocess
import time

import pytest

from gateway.commit_gate import CommitGate
from gateway.embedding_index import EmbeddingIndex
from gateway.intent_queue import IntentQueue
from gateway.ops.committer import DrainResult, author_deposit, drain_once, run_worker
from gateway.ops.deposit import deposit


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _git(root, *args, check=True):
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=check
    )


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
    # live domains so commit-time domain resolution does not quarantine
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
# Test helpers
# ---------------------------------------------------------------------------


def _queue_ids(queue: IntentQueue, state: str) -> set[str]:
    """Return the set of intent IDs currently in ``state``."""
    state_dir = queue._state_dir(state)
    if not state_dir.exists():
        return set()
    return {p.stem for p in state_dir.glob("*.json") if not p.name.startswith(".")}


def _git_committed(repo, rel_path: str) -> bool:
    """Return True if ``rel_path`` appears in any git commit in this repo."""
    r = _git(repo, "log", "--all", "--name-only", "--format=", "--", rel_path, check=False)
    return bool(r.stdout.strip())


def _terminal_state(queue: IntentQueue, intent_id: str) -> str | None:
    """Return the queue state of ``intent_id``, or None if not found."""
    return queue.get_state(intent_id)


def _deposit_entity(*, title, body, aliases=None, domains=None, queue):
    """Thin wrapper: call deposit() with the keyword-arg style used in the brief."""
    payload = {
        "page_type": "entity",
        "title": title,
        "body": body,
    }
    if aliases:
        payload["aliases"] = aliases
    if domains:
        payload["domains"] = domains
    identity = {"entity_kind": "drug", "canonical_name": title}
    if domains:
        identity["domains"] = domains
    res = deposit(payload, identity, queue=queue)
    assert res.success, f"deposit rejected: {res.errors}"
    return res.intent_id


# ---------------------------------------------------------------------------
# Test 1: Autonomous commit (happy path)
# ---------------------------------------------------------------------------


def test_deposited_intent_is_autonomously_committed(repo, queue, gate):
    # realistic payload — full body, aliases, inbound-style wikilink, preamble
    intent_id = _deposit_entity(
        title="Tirzepatide",
        body=(
            "Tirzepatide is a dual GIP/GLP-1 agonist. [[concepts/incretin]]\n\n"
            "## Mechanism\nActs on ... [[sources/pubmed-123]]\n"
        ),
        aliases=["Mounjaro", "Zepbound"],
        domains=["glp1"],
        queue=queue,
    )
    res = drain_once(queue, gate)
    assert res is not None
    assert res.disposition == "committed"
    # drive the REAL on-disk + git outcome
    page = repo / "wiki" / "entities" / "tirzepatide.md"
    assert page.exists()
    text = page.read_text()
    assert "Mounjaro" in text and "Zepbound" in text          # aliases rendered
    assert "[[sources/pubmed-123]]" in text                   # body preserved verbatim
    assert intent_id not in _queue_ids(queue, "submitted")    # left submitted/
    assert _git_committed(repo, "wiki/entities/tirzepatide.md")


# Negative control: with nothing in the queue, drain_once returns None.
def test_drain_once_on_empty_queue_returns_none(repo, queue, gate):
    res = drain_once(queue, gate)
    assert res is None


# ---------------------------------------------------------------------------
# Test 2: Crash mid-author, lease reclaim
# ---------------------------------------------------------------------------


def test_crash_midauthor_lease_expiry_reclaims(repo, queue, gate):
    _deposit_entity(
        title="X", body="b [[sources/s1]]", queue=queue,
    )
    claim = queue.claim(lease_ttl=0.01)   # claim then "crash" (drop claim)
    assert claim is not None
    time.sleep(0.05)
    queue.reclaim_expired()               # expire the lease back to submitted/
    res = drain_once(queue, gate)         # fresh worker reclaims expired lease
    assert res is not None
    assert res.disposition == "committed"


# Negative control: with lease_ttl=120, the second drain_once returns None (still leased).
def test_crash_reclaim_negative_live_lease_not_reclaimed(repo, queue, gate):
    _deposit_entity(
        title="Y", body="b [[sources/s1]]", queue=queue,
    )
    claim = queue.claim(lease_ttl=120.0)  # claim with long lease
    assert claim is not None
    # Do NOT expire; a second drain should find nothing in submitted/
    res = drain_once(queue, gate)
    assert res is None  # still leased — not claimable


# ---------------------------------------------------------------------------
# Test 3: Poison intent dead-letters, loop continues
# ---------------------------------------------------------------------------


def test_poison_intent_dead_letters_loop_continues(repo, queue, gate):
    bad = _deposit_entity(
        title="PoisonDrug",
        body="b [[sources/s1]]",
        queue=queue,
    )
    good_id = _deposit_entity(
        title="Good",
        body="b [[sources/s1]]",
        queue=queue,
    )
    # Corrupt the bad intent's payload so author_deposit will raise
    bad_path = queue._state_dir("submitted") / f"{bad}.json"
    import json
    rec = json.loads(bad_path.read_text())
    rec["payload"]["title"] = ""   # empty title → author_deposit raises ValueError
    bad_path.write_text(json.dumps(rec))

    run_worker(once=True, queue=queue, gate=gate)

    # bad intent is dead-lettered (or committed to dead_lettered state in queue)
    bad_state = _terminal_state(queue, bad)
    assert bad_state in ("dead_lettered",), f"bad intent in state: {bad_state}"
    # loop did not abort on poison — good intent committed
    assert (repo / "wiki" / "entities" / "good.md").exists()


# Negative control: without poisoning, both intents commit normally.
def test_poison_negative_both_good_intents_commit(repo, queue, gate):
    _deposit_entity(title="Alpha", body="b [[sources/s1]]", queue=queue)
    _deposit_entity(title="Beta", body="b [[sources/s1]]", queue=queue)
    run_worker(once=True, queue=queue, gate=gate)
    assert (repo / "wiki" / "entities" / "alpha.md").exists()
    assert (repo / "wiki" / "entities" / "beta.md").exists()


# ---------------------------------------------------------------------------
# Test 4: Write-skew — two same-entity deposits both survive (union)
# ---------------------------------------------------------------------------


def test_write_skew_two_same_entity_deposits_both_survive(repo, queue, gate):
    # Two deposits for the same drug referent (Ozempic / Semaglutide) with
    # different titles → different slugs. Dedup at commit time merges the second
    # onto the first via _retarget_to_canonical + _claim_union.
    # Both claims survive: union, not last-writer-wins.
    _deposit_entity(
        title="Ozempic",
        body="## Claims\n- Claim A. [[sources/a]]\n",
        aliases=["Semaglutide"],
        domains=["glp1"],
        queue=queue,
    )
    _deposit_entity(
        title="Semaglutide",
        body="## Claims\n- Claim B. [[sources/b]]\n",
        aliases=["Ozempic"],
        domains=["glp1"],
        queue=queue,
    )
    run_worker(once=True, queue=queue, gate=gate)
    # The canonical page (committed first, ozempic.md) must contain both claims
    canonical = repo / "wiki" / "entities" / "ozempic.md"
    assert canonical.exists(), "canonical ozempic.md should exist"
    text = canonical.read_text()
    assert "Claim A." in text and "Claim B." in text   # union, not last-writer-wins


# Negative control: single deposit only has its own claim.
def test_write_skew_negative_single_deposit(repo, queue, gate):
    _deposit_entity(
        title="Wegovy",
        body="Only claim. [[sources/x]]",
        queue=queue,
    )
    run_worker(once=True, queue=queue, gate=gate)
    text = (repo / "wiki" / "entities" / "wegovy.md").read_text()
    assert "Only claim." in text
    # No second claim magically appeared
    assert "Claim B." not in text
