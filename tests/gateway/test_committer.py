"""Production committer: author_deposit + drain_once + run_worker (D0).

Four original adversarial scenarios + four fix-driven scenarios:

  1. Autonomous commit (happy path): deposit → drain_once → committed on disk + git.
  2. Crash mid-author, lease reclaim: expired lease is reclaimed by drain_once itself.
  3. Poison intent dead-letters, loop continues: bad intent dead-letters; good follows.
  4. Write-skew two same-entity deposits both survive (cross-slug union via dedup).
  5. CLI path union test: cli.main(["commit-worker","--once"]) fires the real merge.
  6. Same-slug second deposit unions not overwrites.
  7. Retry-later intent is reclaimable after reclaim pass.
  8. Empty-slug title dead-letters cleanly.

Real fcntl locks, real git repo, real CommitGate — no monkeypatching of core path.
Redirect only KNOWLEDGE_ROOT (via monkeypatch.setenv).
"""

from __future__ import annotations

import json
import subprocess
import time

import pytest

from gateway import cli as cli_mod
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


def _deposit_entity(*, title, body, aliases=None, domains=None, queue, entity_kind="drug"):
    """Thin wrapper: call deposit() with the keyword-arg style used in the brief.

    Passes entity_kind in BOTH payload (so author_deposit includes it in frontmatter)
    and identity (so _dedup_recheck's cross-kind guard sees consistent values).
    """
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
# Test 2: Crash mid-author, lease reclaim — via PRODUCTION CODE PATH
# ---------------------------------------------------------------------------


def test_crash_midauthor_lease_expiry_reclaims(repo, queue, gate):
    # drain_once calls queue.reclaim_expired() BEFORE claim() — so the expired
    # lease is returned to submitted/ by the production drain path, not manually.
    _deposit_entity(
        title="X", body="b [[sources/s1]]", queue=queue,
    )
    _prior_claim = queue.claim(lease_ttl=0.001)   # claim then "crash" (drop claim)
    assert _prior_claim is not None
    time.sleep(0.05)
    # NO manual queue.reclaim_expired() here — drain_once must do it internally
    res = drain_once(queue, gate)           # fresh worker: reclaims then claims
    assert res is not None
    assert res.disposition == "committed"


# Negative control: with lease_ttl=120, drain_once finds nothing in submitted/ (still leased).
def test_crash_reclaim_negative_live_lease_not_reclaimed(repo, queue, gate):
    _deposit_entity(
        title="Y", body="b [[sources/s1]]", queue=queue,
    )
    _live_claim = queue.claim(lease_ttl=120.0)    # claim with long lease
    assert _live_claim is not None
    # Do NOT expire; drain_once must NOT steal a live lease
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
    _deposit_entity(
        title="Good",
        body="b [[sources/s1]]",
        queue=queue,
    )
    # Corrupt the bad intent's payload so author_deposit will raise
    bad_path = queue._state_dir("submitted") / f"{bad}.json"
    rec = json.loads(bad_path.read_text())
    rec["payload"]["title"] = ""   # empty title → author_deposit raises ValueError
    bad_path.write_text(json.dumps(rec))

    run_worker(once=True, queue=queue, gate=gate)

    # bad intent is dead-lettered
    bad_state = _terminal_state(queue, bad)
    assert bad_state == "dead_lettered", f"bad intent in state: {bad_state}"
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
# Test 4: Write-skew — two same-referent different-slug deposits both survive
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
    assert "Claim B." not in text


# ---------------------------------------------------------------------------
# Test 5: CLI path — cli.main(["commit-worker","--once"]) fires the real merge
# ---------------------------------------------------------------------------


def test_cli_commit_worker_once_drives_real_union(repo, queue, gate):
    # Drive the union through the REAL cli.main(["commit-worker","--once"]) path
    # (not the fixture-injected gate) to prove EmbeddingIndex is wired in production.
    _deposit_entity(
        title="Liraglutide",
        body="## Claims\n- Claim L1. [[sources/a]]\n",
        aliases=["Victoza"],
        domains=["glp1"],
        queue=queue,
    )
    _deposit_entity(
        title="Victoza",
        body="## Claims\n- Claim L2. [[sources/b]]\n",
        aliases=["Liraglutide"],
        domains=["glp1"],
        queue=queue,
    )
    # Call the REAL CLI path — this uses the production EmbeddingIndex() wiring
    rc = cli_mod.main(["commit-worker", "--once"])
    assert rc == 0

    # Both claims must be present — proves dedup/merge fired through the CLI path
    canonical = repo / "wiki" / "entities" / "liraglutide.md"
    assert canonical.exists(), "canonical liraglutide.md should exist"
    text = canonical.read_text()
    assert "Claim L1." in text and "Claim L2." in text


# Negative control: single deposit via cli.main commits without merge.
def test_cli_commit_worker_once_single_deposit(repo, queue, gate):
    _deposit_entity(
        title="Dulaglutide",
        body="Solo claim. [[sources/x]]",
        queue=queue,
    )
    rc = cli_mod.main(["commit-worker", "--once"])
    assert rc == 0
    text = (repo / "wiki" / "entities" / "dulaglutide.md").read_text()
    assert "Solo claim." in text


# ---------------------------------------------------------------------------
# Test 6: Same-slug second deposit unions not overwrites
# ---------------------------------------------------------------------------


def test_same_slug_second_deposit_unions_not_overwrites(repo, queue, gate):
    # First deposit: commit "Ozempic" with Claim A.
    # Second deposit: same title "Ozempic", different body (Claim B).
    # Expected: both claims present (union), not last-writer-wins (Claim A lost).
    _deposit_entity(
        title="Ozempic",
        body="## Claims\n- Claim A. [[sources/a]]\n",
        aliases=["Semaglutide"],
        domains=["glp1"],
        queue=queue,
    )
    # Drain the first so it's committed before the second is deposited
    drain_once(queue, gate)
    assert (repo / "wiki" / "entities" / "ozempic.md").exists()

    # Second deposit: same slug, new claim
    _deposit_entity(
        title="Ozempic",
        body="## Claims\n- Claim B. [[sources/b]]\n",
        aliases=["Semaglutide"],
        domains=["glp1"],
        queue=queue,
    )
    drain_once(queue, gate)

    text = (repo / "wiki" / "entities" / "ozempic.md").read_text()
    assert "Claim A." in text and "Claim B." in text   # union, not overwrite


# Negative control: single same-slug deposit is committed normally.
def test_same_slug_negative_single_deposit(repo, queue, gate):
    _deposit_entity(
        title="Exenatide",
        body="## Claims\n- Only claim. [[sources/x]]\n",
        queue=queue,
    )
    drain_once(queue, gate)
    text = (repo / "wiki" / "entities" / "exenatide.md").read_text()
    assert "Only claim." in text


# ---------------------------------------------------------------------------
# Test 7: Retry-later intent is reclaimable (via reclaim_expired inside drain_once)
# ---------------------------------------------------------------------------


def test_retry_later_intent_is_reclaimable(repo, queue, gate):
    # Simulate a retry-later intent by manually placing a record in claimed/
    # with an expired lease, then verifying drain_once (which calls reclaim_expired)
    # picks it up on the next pass.
    _deposit_entity(
        title="Retryable",
        body="b [[sources/s1]]",
        queue=queue,
    )
    # Claim with a very short lease (simulating the intent being held by a worker
    # that timed out during gate.commit, leaving the record in claimed/)
    expired_claim = queue.claim(lease_ttl=0.001)
    assert expired_claim is not None
    time.sleep(0.05)

    # drain_once must reclaim_expired() internally before claim(), then pick it up
    res = drain_once(queue, gate)
    assert res is not None
    assert res.disposition == "committed"
    assert (repo / "wiki" / "entities" / "retryable.md").exists()


# ---------------------------------------------------------------------------
# Test 8: Empty-slug title dead-letters cleanly
# ---------------------------------------------------------------------------


def test_empty_slug_title_dead_letters_cleanly(repo, queue, gate):
    # An all-punctuation title like "---" produces slug="" → would write wiki/entities/.md
    # The guard must catch this and dead-letter cleanly.
    payload = {"page_type": "entity", "title": "---", "body": "b [[sources/s1]]"}
    identity = {"entity_kind": "drug", "canonical_name": "---"}
    res_dep = deposit(payload, identity, queue=queue)
    assert res_dep.success, f"deposit rejected unexpectedly: {res_dep.errors}"
    # note: deposit validates title as non-empty "---" passes; but slug → ""

    # drain_once must dead-letter this (author_deposit raises ValueError on empty slug)
    res = drain_once(queue, gate)
    assert res is not None
    assert res.disposition == "dead_lettered"
    # Verify no degenerate .md file was written
    dotfile = repo / "wiki" / "entities" / ".md"
    assert not dotfile.exists()


# Negative control: a valid title does NOT trigger the empty-slug guard.
def test_empty_slug_negative_valid_title(repo, queue, gate):
    _deposit_entity(title="ValidDrug", body="b [[sources/s1]]", queue=queue)
    res = drain_once(queue, gate)
    assert res is not None
    assert res.disposition == "committed"
    assert (repo / "wiki" / "entities" / "validdrug.md").exists()
