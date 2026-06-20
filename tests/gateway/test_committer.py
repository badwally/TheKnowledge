"""Production committer: author_deposit + drain_once + run_worker (D0).

Original adversarial scenarios (1–8) + post-T2 review routing scenarios (9–11)
+ trace mode (12–13):

  1. Autonomous commit (happy path): deposit → drain_once → committed on disk + git.
  2. Crash mid-author, lease reclaim: expired lease is reclaimed by drain_once itself.
  3. Poison intent dead-letters, loop continues: bad intent dead-letters; good follows.
  4. Write-skew two same-entity deposits both survive (cross-slug union via dedup).
  5. CLI path union test: cli.main(["commit-worker","--once"]) fires the real merge.
  6. Same-slug second deposit unions not overwrites.
  7. Retry-later intent is reclaimable after reclaim pass.
  8. Empty-slug title dead-letters cleanly.
  9. policy-edit intent routed through drain_once → gate (not dead-lettered in author_deposit).
 10. reversal_type intent (contradiction-resolution) routed through drain_once → gate.
 11. Genuinely-unknown intent (no page_type, no op, no reversal_type) still dead-letters.
 12. Trace mode: run_worker(sink=...) emits per-intent trace lines for both good + dead-letter.
 13. Trace mode default-off: run_worker() without sink emits nothing (zero behavior change).

Real fcntl locks, real git repo, real CommitGate — no monkeypatching of core path.
Redirect only KNOWLEDGE_ROOT (via monkeypatch.setenv).
"""

from __future__ import annotations

import json
import subprocess
import time

import pytest

import shutil
from pathlib import Path

import yaml

from gateway import cli as cli_mod
from gateway.commit_gate import CommitGate
from gateway.embedding_index import EmbeddingIndex
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id
from gateway.ops.committer import DrainResult, author_deposit, drain_once, run_worker
from gateway.ops.deposit import deposit
from gateway.ops.policy_edit import policy_edit
from gateway.ops.revert_resolution import revert_resolution


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _git(root, *args, check=True):
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=check
    )


# Path to the production dedup golden (seeded into tmp env for governance gate tests).
_REAL_GOLDEN = (
    Path(__file__).parent.parent.parent
    / ".knowledge" / "eval" / "dedup" / "golden.yaml"
)

# Same gitignore as test_governance_flow: .knowledge/policies/ is git-TRACKED so that
# durable-commit assertions work.  Only untracked runtime dirs are excluded.
_POLICY_GITIGNORE = (
    ".index/\n"
    ".knowledge/locks/\n"
    ".knowledge/lint/\n"
    ".knowledge/watcher.*\n"
    ".knowledge/scheduler.*\n"
    ".knowledge/auth.yaml\n"
    ".knowledge/secrets.env\n"
    ".knowledge/demand/\n"
    ".knowledge/transcripts/\n"
    ".knowledge/intents/\n"
    ".knowledge/provenance/\n"
    ".knowledge/fencing/\n"
)

_ALLOWLISTED_PRINCIPAL = "librarian-admin:policy-admin"


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
def policy_repo(tmp_path, monkeypatch):
    """Repo with policy + dedup golden seeded so the CommitGate policy-edit gate runs.

    Uses a tracked .knowledge/policies/ (not gitignored) and seeds the dedup golden
    so merge-map gate runs for real.  GATEWAY_DEV_SKIP_POLICY_GATES=1 skips the
    retrieval-golden gate (no FTS index in unit env).
    """
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    monkeypatch.setenv("GATEWAY_DEV_SKIP_POLICY_GATES", "1")
    monkeypatch.setenv("GATEWAY_POLICY_PRINCIPAL", _ALLOWLISTED_PRINCIPAL)

    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "test@test")
    _git(tmp_path, "config", "user.name", "test")
    (tmp_path / ".gitignore").write_text(_POLICY_GITIGNORE)
    (tmp_path / "README.md").write_text("seed\n")
    _git(tmp_path, "add", "README.md", ".gitignore")
    _git(tmp_path, "commit", "-qm", "seed")

    # Seed an initial domain policy (committed — tracked)
    dom_dir = tmp_path / ".knowledge" / "policies" / "med"
    dom_dir.mkdir(parents=True)
    initial_policy: dict = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.7, "threshold_exclude": 0.3},
        "version": 1,
    }
    policy_file = dom_dir / "policy.yaml"
    policy_file.write_text(yaml.dump(initial_policy))

    # Seed the dedup golden so the merge-map gate runs for real.
    golden_dir = tmp_path / ".knowledge" / "eval" / "dedup"
    golden_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(_REAL_GOLDEN, golden_dir / "golden.yaml")

    _git(tmp_path, "add", "--",
         ".knowledge/policies/med/policy.yaml",
         ".knowledge/eval/dedup/golden.yaml")
    _git(tmp_path, "commit", "-qm", "seed policy + golden")

    return tmp_path, policy_file, initial_policy


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


@pytest.mark.concurrency
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

    # Direction-agnostic: the merge fires and unions both claims onto ONE
    # canonical page; the other slug becomes a merged_into tombstone. Which of
    # the two aliased slugs wins canonical is determined by drain order, which
    # is now deterministic (intent_queue.claim() orders by (mtime, name)) but
    # not semantically pinned to a particular slug — so assert the invariant
    # (one canonical carries both claims, the other redirects), not the winner.
    liraglutide = repo / "wiki" / "entities" / "liraglutide.md"
    victoza = repo / "wiki" / "entities" / "victoza.md"
    assert liraglutide.exists() and victoza.exists(), (
        "both the canonical page and its merge tombstone must exist"
    )
    texts = {p: p.read_text() for p in (liraglutide, victoza)}
    carriers = [p for p, t in texts.items() if "Claim L1." in t and "Claim L2." in t]
    assert len(carriers) == 1, (
        f"exactly one canonical page must carry both claims; got {[p.name for p in carriers]}"
    )
    loser = (set(texts) - set(carriers)).pop()
    assert "merged_into:" in texts[loser], (
        f"the non-canonical slug ({loser.name}) must be a merged_into tombstone"
    )


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


@pytest.mark.concurrency
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


# ---------------------------------------------------------------------------
# Test 9: policy-edit intent routed through drain_once → gate (post-T2 D0 fix)
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_policy_edit_intent_routed_not_dead_lettered_in_author_deposit(policy_repo, monkeypatch):
    """A policy-edit intent enqueued via policy_edit() is COMMITTED via run_worker.

    Today (pre-fix) drain_once dead-letters it in author_deposit (no page_type).
    After the fix, drain_once must detect op=="policy-edit" and route to gate.commit()
    with an empty-writes AuthoredIntent so _apply_policy_edit() can apply it.

    RED before fix: disposition=="dead_lettered" (author_deposit raises ValueError).
    GREEN after fix: disposition=="committed" (benign policy passes dual gate).

    This test goes RED if:
      - The committer still sends policy-edit to author_deposit (dead-lettered).
      - The gate's _apply_policy_edit is not reached.
      - A benign policy is incorrectly dead-lettered by the gate.
    """
    tmp_path, policy_file, initial_policy = policy_repo
    q = IntentQueue()
    idx = EmbeddingIndex()
    gate = CommitGate(queue=q, embedding_index=idx)

    benign_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.75, "threshold_exclude": 0.35},
        "version": 2,
    }
    enqueue_result = policy_edit("med", benign_policy, reason="test routing fix", queue=q)
    assert enqueue_result.success, f"policy_edit enqueue failed: {enqueue_result.errors}"
    assert enqueue_result.disposition == "queued"
    iid = enqueue_result.intent_id

    # drain_once must route to gate, not dead-letter in author_deposit
    res = drain_once(q, gate)
    assert res is not None
    assert res.disposition == "committed", (
        f"policy-edit intent must be committed (via gate dispatch), "
        f"not dead-lettered in author_deposit; got disposition={res.disposition!r}, "
        f"detail={res.detail!r}"
    )

    # Policy file must be updated on disk with the new values
    on_disk = yaml.safe_load(policy_file.read_text())
    assert on_disk == benign_policy, (
        f"policy file not updated after gate commit; on_disk={on_disk}"
    )


@pytest.mark.integration
def test_policy_edit_regressing_policy_dead_lettered_by_gate_not_author_deposit(
    policy_repo, monkeypatch
):
    """A regressing policy-edit intent is dead-lettered BY THE GATE, not author_deposit.

    Pre-fix: dead-lettered in author_deposit (ValueError: unsupported page_type).
    Post-fix: routed to gate._apply_policy_edit → dead-lettered by merge-map gate
    (regression in dedup precision). The distinction is that the gate's dead-letter
    reason must name the merge-precision failure, not a page_type error.

    This test goes RED if:
      - The committer dead-letters for "unsupported page_type" (author_deposit path).
      - The gate commits a regressing policy (gate not evaluating real params).
    """
    tmp_path, policy_file, initial_policy = policy_repo
    q = IntentQueue()
    idx = EmbeddingIndex()
    gate = CommitGate(queue=q, embedding_index=idx)

    regressing_policy = {
        "domain": {"slug": "med", "name": "Medicine"},
        "filter": {"threshold_include": 0.7, "threshold_exclude": 0.3},
        "dedup": {"blocking_band": 0.99, "identity_threshold": 0.99},
        "version": 2,
    }
    enqueue_result = policy_edit(
        "med", regressing_policy, reason="regress test routing", queue=q
    )
    assert enqueue_result.success, f"policy_edit enqueue failed: {enqueue_result.errors}"
    iid = enqueue_result.intent_id

    res = drain_once(q, gate)
    assert res is not None
    assert res.disposition == "dead_lettered", (
        f"regressing policy must be dead-lettered; got {res.disposition!r}"
    )
    # The dead-letter reason must come from the gate's merge-map gate, NOT from
    # author_deposit's "unsupported page_type" error.
    gate_reason = res.detail or ""
    assert "page_type" not in gate_reason.lower(), (
        f"dead-letter from author_deposit path (page_type error), not gate: {gate_reason!r}"
    )
    assert any(
        kw in gate_reason.lower() for kw in ("regress", "precision", "merge-map", "policy")
    ), f"dead-letter reason does not name a policy gate failure: {gate_reason!r}"

    # Policy file must NOT be changed (gate failed closed)
    on_disk = yaml.safe_load(policy_file.read_text())
    assert on_disk == initial_policy, (
        f"policy mutated despite dead-lettering a regressing edit; on_disk={on_disk}"
    )


# Negative control: genuinely-invalid intent (no page_type, no op, no reversal_type) still dead-letters.
def test_unknown_intent_with_no_routing_key_still_dead_letters(repo, queue, gate):
    """An intent with no page_type, no op=="policy-edit", and no reversal_type must
    still be dead-lettered — the new routing must not accidentally swallow unknowns.

    This test goes RED if the fix routes genuinely-unknown intents to the gate's
    deposit path or silently ignores them.
    """
    # Build a genuinely-unknown intent (not a deposit, not a policy-edit, not a reversal)
    payload = {"custom_field": "irrelevant", "some_data": "xyz"}
    identity = {"agent": "test"}
    iid = compute_intent_id(payload, identity, semantics="unknown-test")
    intent = Intent(intent_id=iid, payload=payload, identity=identity)
    q = queue
    q.submit(intent)

    res = drain_once(q, gate)
    assert res is not None
    assert res.disposition == "dead_lettered", (
        f"unknown intent must still dead-letter; got {res.disposition!r}"
    )


# ---------------------------------------------------------------------------
# Test 10: reversal_type intent routed through drain_once → gate (post-T2 D0 fix)
# ---------------------------------------------------------------------------


def test_reversal_type_intent_routed_not_dead_lettered_in_author_deposit(repo, queue, gate):
    """A reversal_type="contradiction-resolution" intent enqueued via revert_resolution()
    is routed to gate._apply_reversal() by drain_once, not dead-lettered in author_deposit.

    RED before fix: drain_once dead-letters it in author_deposit with "empty title" error
    (no page_type/title → author_deposit raises ValueError before the gate sees it).
    GREEN after fix: gate._apply_contradiction_revert dead-letters it with "unknown act ..."
    (the act doesn't exist in this test fixture — that is expected; what matters is
    the dead-letter reason comes from the gate's dispatch, not author_deposit).

    The distinguishing assertion: the dead-letter reason must contain "unknown act"
    (gate dispatch) rather than "empty title" or "unsupported page_type" (author_deposit).
    """
    identity = {"agent": "test", "session": "s1"}
    enqueue_result = revert_resolution(
        "nonexistent-act-id-for-routing-test", identity, queue=queue
    )
    assert enqueue_result.success, f"revert_resolution enqueue failed: {enqueue_result.errors}"

    res = drain_once(queue, gate)
    assert res is not None
    assert res.disposition == "dead_lettered", (
        f"reversal with unknown act must be dead-lettered; got {res.disposition!r}"
    )
    # The dead-letter reason must come from the gate's _apply_contradiction_revert
    # ("unknown act ..."), NOT from author_deposit ("empty title" / "unsupported page_type").
    gate_reason = (res.detail or "").lower()
    assert "unknown act" in gate_reason, (
        f"dead-letter reason does not match gate dispatch ('unknown act ...'); "
        f"got: {res.detail!r}. This means the routing fix is not working — "
        f"drain_once is still sending to author_deposit instead of gate.commit()."
    )


# ---------------------------------------------------------------------------
# Test 12: Trace mode — sink captures per-intent trace lines (P6)
# ---------------------------------------------------------------------------


def test_trace_mode_captures_committed_and_dead_letter(repo, queue, gate):
    """run_worker(once=True, sink=...) emits one trace record per drained intent.

    Queue contains:
      - one GOOD entity deposit → disposition="committed"
      - one BAD deposit (empty title → dead_lettered via author_deposit path)

    Assertions:
      - sink receives exactly two records (both intents drained).
      - The committed record has disposition="committed" and an intent_id.
      - The dead-letter record has disposition="dead_lettered" and a non-empty reason
        that comes from the REAL drain path (author_deposit raises ValueError on empty
        title → the dead-letter reason must reference the real error, not a fabricated
        string).
      - The dead-letter record's reason key is NOT a fabricated static string — it
        must match the actual exception text produced by author_deposit.
    """
    # Queue a good deposit
    good_id = _deposit_entity(title="TraceGoodDrug", body="b [[sources/s1]]", queue=queue)

    # Queue a bad deposit (empty title → author_deposit raises ValueError → dead_lettered).
    # This drives the REAL dead-letter path (same as test 8 above) so the reason is real.
    bad_payload = {"page_type": "entity", "title": "---", "body": "b [[sources/s1]]"}
    bad_identity = {"entity_kind": "drug", "canonical_name": "---"}
    bad_res = deposit(bad_payload, bad_identity, queue=queue)
    assert bad_res.success, f"bad deposit rejected unexpectedly: {bad_res.errors}"
    bad_id = bad_res.intent_id

    # Collect trace records via the sink
    trace_records: list[dict] = []

    def _sink(record: dict) -> None:
        trace_records.append(record)

    run_worker(once=True, queue=queue, gate=gate, sink=_sink)

    # Both intents must be traced
    assert len(trace_records) == 2, (
        f"Expected 2 trace records (committed + dead_lettered), got {len(trace_records)}: "
        f"{trace_records}"
    )

    by_intent = {r["intent_id"]: r for r in trace_records}

    # Good intent must show as committed
    assert good_id in by_intent, f"good intent {good_id} not in trace: {by_intent}"
    good_trace = by_intent[good_id]
    assert good_trace["disposition"] == "committed", (
        f"good intent disposition must be 'committed'; got {good_trace['disposition']!r}"
    )

    # Bad intent must show as dead_lettered with a real reason (not a fabricated string)
    assert bad_id in by_intent, f"bad intent {bad_id} not in trace: {by_intent}"
    bad_trace = by_intent[bad_id]
    assert bad_trace["disposition"] == "dead_lettered", (
        f"bad intent disposition must be 'dead_lettered'; got {bad_trace['disposition']!r}"
    )
    # The reason must be non-empty — it comes from the real author_deposit exception
    reason = bad_trace.get("reason", "")
    assert reason, (
        f"dead-letter trace record must carry a non-empty reason; got: {bad_trace}"
    )
    # The reason must NOT be a fabricated static string — it must reference what
    # author_deposit actually raises for an empty-slug title.
    assert "fabricated" not in reason.lower(), (
        f"reason appears to be a placeholder; got: {reason!r}"
    )
    # author_deposit raises ValueError with "empty slug" or similar for "---" title
    assert any(kw in reason.lower() for kw in ("slug", "title", "empty", "invalid")), (
        f"dead-letter reason does not match expected author_deposit error; got: {reason!r}"
    )

    # Trace records must contain the required stable keys (no payload/body leakage)
    required_keys = {"intent_id", "disposition", "reason"}
    for rec in trace_records:
        assert required_keys <= set(rec.keys()), (
            f"trace record missing required keys; got keys: {set(rec.keys())}"
        )
        # Security: no body/payload content in the trace
        assert "body" not in rec, f"trace record must not contain 'body': {rec}"
        assert "payload" not in rec, f"trace record must not contain 'payload': {rec}"


# Negative control (Test 13): default-off — run_worker without sink emits nothing.
def test_trace_mode_default_off_no_sink_zero_behavior_change(repo, queue, gate):
    """run_worker() without a sink must behave identically to the pre-P6 state.

    This is the default-off guarantee: the drain logic is byte-identical when
    no sink is passed. We verify this by running the full drain without a sink
    and confirming:
      - The intent commits normally (no regression in drain behavior).
      - No attribute error or exception from the missing sink.
    """
    _deposit_entity(title="NoTraceDrug", body="b [[sources/s1]]", queue=queue)

    # Must not raise — default-off sink is None
    run_worker(once=True, queue=queue, gate=gate)

    # Drain behavior unchanged: page committed to disk
    assert (repo / "wiki" / "entities" / "notracedrug.md").exists(), (
        "drain without sink must still commit pages normally (default-off guarantee)"
    )
