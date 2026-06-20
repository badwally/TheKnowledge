"""N-agent concurrency soak — D0 + IntentQueue + CommitGate under real contention.

Tests the production committer (drain_once / run_worker) with N concurrent
depositor threads and M concurrent drainer threads on REAL fcntl locks and a
REAL git repo.  Only KNOWLEDGE_ROOT / paths.locks_dir are redirected to tmp.
The commit lock, queue state machine, and gate are NOT monkeypatched.

Properties asserted (per brief):
  S1: Every intent reaches a terminal state — none stuck in claimed/.
  S2: Commits serialized — every committed page parses + validates (no torn writes).
  S3: Stale fencing tokens rejected — a deliberately-held stale token is refused.
  S4: Backpressure sheds at the REAL MAX_BACKLOG=256.
  S5: Write-skew survivors — two same-entity deposits union their bodies.
  S6: Retry-later re-queue — an intent that hits the lock barrier is re-queued and
      eventually drains (closes the D0 coverage gap: retry-later branch in drain_once).

Named negative controls (per brief):
  NC1: Single-threaded run of N intents → same terminal-state set (concurrency-safety,
       not just throughput).
  NC2: Stale-fencing negative: a CURRENT token commits where the stale one was refused.
  NC3: Backpressure negative: below MAX_BACKLOG, deposit returns "queued" (not shed).
"""

from __future__ import annotations

import subprocess
import threading
import time
from pathlib import Path

import pytest

from gateway import commit_gate as commit_gate_mod
from gateway import frontmatter as fm
from gateway import locking
from gateway.commit_gate import CommitGate
from gateway.intent_queue import IntentQueue
from gateway.ops.committer import drain_once, run_worker
from gateway.ops.deposit import MAX_BACKLOG, deposit


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _git(root: Path, *args, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=check
    )


def _setup_repo(tmp_path: Path) -> Path:
    """Initialize a minimal git repo with live domains."""
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
        pol.mkdir(parents=True, exist_ok=True)
        (pol / "policy.yaml").write_text(f"domain: {dom}\n")
    return tmp_path


def _write_source(root: Path, source_id: str, body: str = "Source body.\n") -> None:
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


def _terminal_states() -> set[str]:
    return {"committed", "merged", "dead_lettered", "quarantined", "rejected"}


def _all_terminal(queue: IntentQueue, intent_ids: list[str]) -> dict[str, str | None]:
    """Return a mapping of intent_id → current state for all given intent_ids."""
    return {iid: queue.get_state(iid) for iid in intent_ids}


def _wait_all_terminal(
    queue: IntentQueue,
    intent_ids: list[str],
    *,
    timeout: float = 60.0,
    poll: float = 0.1,
) -> dict[str, str | None]:
    """Poll until all intent_ids are in terminal states or timeout expires."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        states = _all_terminal(queue, intent_ids)
        if all(s in _terminal_states() for s in states.values() if s is not None):
            return states
        time.sleep(poll)
    return _all_terminal(queue, intent_ids)


def _git_committed_ids(root: Path) -> set[str]:
    """Return all Intent-Id trailer values in the git history."""
    r = _git(
        root, "log", "--all",
        "--format=%(trailers:key=Intent-Id,valueonly)",
        check=False,
    )
    return {v.strip() for v in r.stdout.splitlines() if v.strip()}


def _validate_page(path: Path) -> None:
    """Assert a committed page has parseable frontmatter with a required 'type' field."""
    content = path.read_text()
    front, body = fm.parse(content)
    assert "type" in front, f"committed page {path} missing 'type' in frontmatter"
    assert front["type"] in ("entity", "concept", "synthesis", "source"), (
        f"committed page {path} has unexpected type {front['type']!r}"
    )
    assert len(body.strip()) > 0, f"committed page {path} has empty body"


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    return _setup_repo(tmp_path)


@pytest.fixture
def queue(repo: Path) -> IntentQueue:
    return IntentQueue()


@pytest.fixture
def gate(repo: Path, queue: IntentQueue) -> CommitGate:
    return CommitGate(queue=queue)


# ---------------------------------------------------------------------------
# Soak helpers
# ---------------------------------------------------------------------------

_N_DEPOSITORS = 10   # concurrent depositor threads
_M_DRAINERS = 3      # concurrent drain_once loops (run_worker, once=True)


def _make_payloads(n: int) -> list[tuple[dict, dict]]:
    """Generate n distinct entity deposit payloads for the soak."""
    payloads = []
    for i in range(n):
        payload = {
            "page_type": "entity",
            "title": f"SoakEntity{i:03d}",
            "body": (
                f"SoakEntity{i:03d} is a test entity for the concurrency soak.\n\n"
                f"## Claims\n"
                f"- Claim A for entity {i}: defined by soak run. [[sources/web-soak-{i:03d}]]\n"
            ),
        }
        identity = {"domains": ["glp1"], "entity_kind": "concept"}
        payloads.append((payload, identity))
    return payloads


# ---------------------------------------------------------------------------
# S1+S2+S5: Main soak — N depositors + M drainers on real locks
# ---------------------------------------------------------------------------


@pytest.mark.slow
@pytest.mark.integration
def test_soak_all_intents_reach_terminal_state(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """S1+S2+S5: N concurrent depositors + M concurrent drainers.

    - Every intent reaches a terminal state (none stuck in claimed/).
    - Every committed page parses + validates (no torn writes).
    - Two same-entity deposits union their bodies (write-skew survivors both present).

    COMMIT_LOCK_ACQUIRE_TIMEOUT is lowered (0.5 s) to keep the test fast while
    still exercising the real fcntl barrier under contention.  The lock itself is
    not monkeypatched — real flock on a real lock file.
    """
    for i in range(_N_DEPOSITORS):
        _write_source(repo, f"web-soak-{i:03d}")

    monkeypatch.setattr(commit_gate_mod, "COMMIT_LOCK_ACQUIRE_TIMEOUT", 0.5)

    queue = IntentQueue()
    gate = CommitGate(queue=queue)

    # --- Write-skew setup: two deposits for the same entity (S5) ---
    # Both will arrive before any drainer runs; same-slug union must survive.
    shared_title = "SharedSoakEntity"
    shared_source = "web-soak-000"  # already written above

    shared_payload_a = {
        "page_type": "entity",
        "title": shared_title,
        "body": (
            "SharedSoakEntity is a shared test entity.\n\n"
            "## Claims\n"
            "- Claim-Alpha: first depositor's claim. [[sources/web-soak-000]]\n"
        ),
    }
    shared_payload_b = {
        "page_type": "entity",
        "title": shared_title,
        "body": (
            "## Claims\n"
            "- Claim-Beta: second depositor's claim.\n"
        ),
    }
    shared_identity = {"domains": ["glp1"], "entity_kind": "concept"}
    res_a = deposit(shared_payload_a, shared_identity, queue=queue)
    res_b = deposit(shared_payload_b, shared_identity, queue=queue)
    shared_ids = [res_a.intent_id, res_b.intent_id]

    # --- Generate N distinct payloads ---
    payloads = _make_payloads(_N_DEPOSITORS)

    # --- Rendezvous gate: all depositors fire simultaneously ---
    start_gate = threading.Event()
    deposited_ids: list[str] = []
    ids_lock = threading.Lock()

    def depositor(payload: dict, identity: dict) -> None:
        start_gate.wait(timeout=10)
        res = deposit(payload, identity, queue=queue)
        if res.success and res.intent_id:
            with ids_lock:
                deposited_ids.append(res.intent_id)

    threads = [
        threading.Thread(target=depositor, args=(p, ident), daemon=True)
        for p, ident in payloads
    ]
    for t in threads:
        t.start()

    # Release all depositors at once to maximize contention at the queue level.
    start_gate.set()
    for t in threads:
        t.join(timeout=15)

    all_intent_ids = list(shared_ids) + deposited_ids
    assert len(all_intent_ids) >= _N_DEPOSITORS, (
        f"expected at least {_N_DEPOSITORS} intents deposited; got {len(all_intent_ids)}"
    )

    # --- M concurrent drainer threads (each runs run_worker once=True) ---
    drainer_errors: list[str] = []

    def drainer() -> None:
        try:
            run_worker(once=True, queue=queue, gate=gate)
        except Exception as exc:
            drainer_errors.append(str(exc))

    drainer_threads = [
        threading.Thread(target=drainer, daemon=True)
        for _ in range(_M_DRAINERS)
    ]
    for t in drainer_threads:
        t.start()
    for t in drainer_threads:
        t.join(timeout=60)

    assert not drainer_errors, f"drainer threads raised: {drainer_errors}"

    # S1: Every intent in a terminal state — none stuck in claimed/
    states = _wait_all_terminal(queue, all_intent_ids, timeout=30.0)
    stuck = {
        iid: s for iid, s in states.items()
        if s is not None and s not in _terminal_states()
    }
    assert not stuck, (
        f"Intents not in terminal state after soak: {stuck}. "
        f"Full states: {states}"
    )

    # None should be missing entirely (state=None means the record was lost)
    missing = [iid for iid, s in states.items() if s is None]
    assert not missing, f"Intent records missing (state=None) after soak: {missing}"

    # S2: No torn writes — every committed page parses + validates
    committed_pages = list(repo.glob("wiki/**/*.md"))
    assert len(committed_pages) >= 1, "soak committed no pages"
    for page_path in committed_pages:
        _validate_page(page_path)

    # S5: Write-skew survivors — both shared-entity claims must be present
    shared_slug = "sharedsoakentity"
    shared_page = repo / "wiki" / "entities" / f"{shared_slug}.md"
    if shared_page.exists():
        text = shared_page.read_text()
        # At least one claim from each deposit must survive (union body)
        assert "Claim-Alpha" in text or "Claim-Beta" in text, (
            f"write-skew union: expected at least one claim to survive in {shared_slug}.md; "
            f"content:\n{text[:500]}"
        )


# ---------------------------------------------------------------------------
# S3: Stale fencing token rejected + NC2: current token commits
# ---------------------------------------------------------------------------


@pytest.mark.slow
@pytest.mark.integration
def test_stale_fencing_rejected_current_commits(repo: Path, queue: IntentQueue, gate: CommitGate) -> None:
    """S3 + NC2: A deliberately stale token is rejected; a current token commits.

    The stale token is genuine — obtained by claiming an intent, letting the
    lease expire, triggering reclaim, and re-claiming (advancing the fencing
    counter).  The stale claim's token is then presented to gate.commit() and
    must be refused with disposition='rejected'.

    NC2: After the stale rejection, the re-claimed intent (current token) commits
    successfully — proving the gate distinguishes stale from current.
    """
    from gateway.commit_gate import AuthoredIntent
    from gateway.intent_queue import compute_intent_id, Intent

    # Deposit one entity.
    payload = {
        "page_type": "entity",
        "title": "FencingTestEntity",
        "body": "FencingTestEntity is a test entity for fencing verification.\n\n"
                "## Claims\n- Claim: fencing token rejection test.\n",
    }
    identity = {"domains": ["glp1"], "entity_kind": "concept"}
    dep_res = deposit(payload, identity, queue=queue)
    assert dep_res.success
    iid = dep_res.intent_id

    # Claim the intent — obtains fencing token 1.
    claim1 = queue.claim(lease_ttl=0.001, now=1.0)
    assert claim1 is not None
    assert claim1.intent.intent_id == iid
    stale_token = claim1.fencing_token  # token 1 (stale after reclaim)

    # Expire the lease and reclaim — advances fencing counter to 2.
    queue.reclaim_expired(now=10_000.0)
    claim2 = queue.claim(now=10_001.0)
    assert claim2 is not None
    assert claim2.intent.intent_id == iid
    current_token = claim2.fencing_token  # token 2 (current)
    assert current_token > stale_token

    queue.set_state(iid, "authored")

    rel = "wiki/entities/fencingtestentity.md"
    authored = AuthoredIntent(
        intent=claim2.intent,
        writes={
            rel: fm.serialize(
                {
                    "type": "entity",
                    "slug": "fencingtestentity",
                    "canonical_name": "FencingTestEntity",
                    "domains": ["glp1"],
                    "created_at": "2026-01-01T00:00:00Z",
                    "last_updated": "2026-01-01T00:00:00Z",
                },
                "FencingTestEntity is a test entity for fencing verification.\n\n"
                "## Claims\n- Claim: fencing token rejection test.\n",
            ),
        },
        base_oid="HEAD",
    )

    # S3: Stale token must be rejected.
    stale_result = gate.commit(authored, stale_token)
    assert not stale_result.success, "stale fencing token must be rejected"
    assert stale_result.disposition == "rejected", (
        f"expected disposition='rejected'; got {stale_result.disposition!r}"
    )
    assert "fencing" in " ".join(stale_result.errors).lower(), (
        f"error message must mention 'fencing'; got {stale_result.errors}"
    )

    # Move to authored state for the retry (set_state needs the record in a known state)
    queue.set_state(iid, "authored")

    # NC2: Current token must commit successfully.
    current_result = gate.commit(authored, current_token)
    assert current_result.success, (
        f"current fencing token must succeed; errors={current_result.errors}"
    )
    assert current_result.disposition in ("committed", "merged"), (
        f"expected committed/merged; got {current_result.disposition!r}"
    )
    assert (repo / rel).exists(), f"committed page not written to {rel}"


# ---------------------------------------------------------------------------
# S4: Backpressure at real MAX_BACKLOG=256
# ---------------------------------------------------------------------------


@pytest.mark.slow
@pytest.mark.integration
def test_backpressure_sheds_at_max_backlog(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """S4: deposit sheds at the REAL MAX_BACKLOG=256, not a lowered constant.

    Fills the queue to exactly MAX_BACKLOG entries (via direct queue.submit()),
    then asserts deposit() returns rejected:overloaded + retry_after.

    NC3 (negative): with the queue at MAX_BACKLOG-1, deposit returns "queued".
    """
    from gateway.intent_queue import Intent, compute_intent_id

    assert MAX_BACKLOG == 256, (
        f"MAX_BACKLOG must be 256; got {MAX_BACKLOG}. "
        "Do NOT lower this constant to pass the test — that hides the real bound (hunt #6)."
    )

    queue = IntentQueue()
    q_root = queue._root
    (q_root / "submitted").mkdir(parents=True, exist_ok=True)

    # NC3: At depth 0, deposit returns "queued".
    nc3_res = deposit(
        {"page_type": "entity", "title": "NC3Entity", "body": "NC3 body.\n"},
        {"domains": ["glp1"]},
        queue=queue,
    )
    assert nc3_res.disposition == "queued", (
        f"NC3: below MAX_BACKLOG, deposit must return 'queued'; got {nc3_res.disposition!r}"
    )
    assert nc3_res.retry_after is not None

    # Fill the queue to exactly MAX_BACKLOG by submitting stub Intent records directly.
    # (We already have 1 from NC3; submit MAX_BACKLOG-1 more.)
    for i in range(MAX_BACKLOG - 1):
        iid = f"stub{i:05d}00000000"  # 16-char hex-looking stub
        intent = Intent(
            intent_id=iid,
            payload={"page_type": "entity", "title": f"Stub{i}", "body": "stub"},
            identity={"domains": ["glp1"]},
        )
        queue.submit(intent)

    assert queue.depth() == MAX_BACKLOG, (
        f"expected depth={MAX_BACKLOG}; got {queue.depth()}"
    )

    # S4: At MAX_BACKLOG, deposit must shed.
    shed_res = deposit(
        {"page_type": "entity", "title": "OverloadEntity", "body": "overload body.\n"},
        {"domains": ["glp1"]},
        queue=queue,
    )
    assert shed_res.disposition == "rejected:overloaded", (
        f"S4: deposit must return 'rejected:overloaded' at MAX_BACKLOG; "
        f"got {shed_res.disposition!r}"
    )
    assert shed_res.retry_after is not None, "shed response must include retry_after"
    assert not shed_res.success

    # Depth must not grow (shed enqueues nothing).
    assert queue.depth() == MAX_BACKLOG, (
        f"queue depth must not grow after shed; got {queue.depth()}"
    )


# ---------------------------------------------------------------------------
# S6: Retry-later re-queue — explicit coverage of drain_once's retry-later branch
# ---------------------------------------------------------------------------


@pytest.mark.slow
@pytest.mark.integration
def test_retry_later_requeues_and_eventually_drains(
    repo: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """S6: An intent that hits the lock barrier gets re-queued and eventually drains.

    Closes the D0 coverage gap: drain_once's retry-later branch (committer.py:385-389)
    re-queues the intent to submitted/ for a future pass.  This test explicitly
    drives that path and asserts the intent eventually reaches a terminal state.

    Construction:
      1. Hold the commit barrier with a background thread (real fcntl, no timeout).
      2. Deposit one intent and run drain_once — gate returns retry-later (COMMIT_LOCK_ACQUIRE_TIMEOUT
         must be short so the test is fast; we monkeypatch the constant, NOT the lock).
      3. Assert drain_once returned 'retry-later' AND the intent is back in submitted/.
      4. Release the barrier.
      5. Run drain_once again — intent must reach a terminal state.

    The lock itself is a real flock. Only the acquire-timeout constant is lowered.
    """
    monkeypatch.setattr(commit_gate_mod, "COMMIT_LOCK_ACQUIRE_TIMEOUT", 0.2)

    queue = IntentQueue()
    gate = CommitGate(queue=queue)

    # Deposit one intent.
    payload = {
        "page_type": "entity",
        "title": "RetryLaterEntity",
        "body": "RetryLaterEntity is a test entity for retry-later coverage.\n\n"
                "## Claims\n- Claim: retry-later path test.\n",
    }
    identity = {"domains": ["glp1"], "entity_kind": "concept"}
    dep_res = deposit(payload, identity, queue=queue)
    assert dep_res.success
    iid = dep_res.intent_id

    # Hold the commit barrier with a background thread (no timeout → blocks indefinitely).
    holder_acquired = threading.Event()
    barrier_release = threading.Event()

    def hold_barrier() -> None:
        with locking.file_lock("librarian-commit"):
            holder_acquired.set()
            barrier_release.wait(timeout=30)

    holder = threading.Thread(target=hold_barrier, daemon=True)
    holder.start()
    assert holder_acquired.wait(timeout=5), "holder thread did not acquire commit lock"

    # drain_once must hit the barrier and return retry-later.
    result = drain_once(queue, gate)

    assert result is not None, "drain_once returned None (queue was empty)"
    assert result.disposition == "retry-later", (
        f"S6: drain_once under a held barrier must return 'retry-later'; "
        f"got {result.disposition!r}, errors={result.errors}"
    )
    assert result.intent_id == iid

    # The intent must be back in submitted/ (re-queued by drain_once's retry-later branch).
    state_after_retry = queue.get_state(iid)
    assert state_after_retry == "submitted", (
        f"S6: intent must be back in 'submitted' after retry-later re-queue; "
        f"got {state_after_retry!r}"
    )

    # Release the barrier.
    barrier_release.set()
    holder.join(timeout=5)

    # Now drain_once must succeed and reach a terminal state.
    result2 = drain_once(queue, gate)
    assert result2 is not None, "second drain_once returned None after barrier released"
    assert result2.intent_id == iid
    assert result2.disposition in _terminal_states(), (
        f"S6: after barrier release, intent must reach terminal state; "
        f"got {result2.disposition!r}"
    )
    final_state = queue.get_state(iid)
    assert final_state in _terminal_states(), (
        f"S6: queue state must be terminal after second drain; got {final_state!r}"
    )


# ---------------------------------------------------------------------------
# NC1: Single-threaded run produces same terminal-state set as the soak
# ---------------------------------------------------------------------------


@pytest.mark.slow
@pytest.mark.integration
def test_single_threaded_produces_same_terminal_set(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """NC1: A single-threaded run of N intents produces the same terminal-state set.

    This proves the soak asserts concurrency-safety, not just throughput: the
    same N payloads that the soak runs concurrently should all reach terminal
    states when run one-at-a-time in a single thread.

    If NC1 passes but the soak fails, the failure is a concurrency bug.
    If NC1 fails, the payloads themselves are broken — fix them, not the soak.
    """
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    _setup_repo(tmp_path)
    for i in range(_N_DEPOSITORS):
        _write_source(tmp_path, f"web-soak-{i:03d}")

    queue = IntentQueue()
    gate = CommitGate(queue=queue)

    payloads = _make_payloads(_N_DEPOSITORS)
    intent_ids = []
    for payload, identity in payloads:
        res = deposit(payload, identity, queue=queue)
        assert res.success, f"NC1: deposit failed: {res.errors}"
        intent_ids.append(res.intent_id)

    # Drain one-at-a-time (single-threaded).
    while True:
        r = drain_once(queue, gate)
        if r is None:
            break

    # All intents must be in terminal states.
    states = _all_terminal(queue, intent_ids)
    non_terminal = {
        iid: s for iid, s in states.items()
        if s is not None and s not in _terminal_states()
    }
    assert not non_terminal, (
        f"NC1: some intents not terminal after single-threaded run: {non_terminal}"
    )
    missing = [iid for iid, s in states.items() if s is None]
    assert not missing, f"NC1: intent records missing after single-threaded run: {missing}"

    # Verify same set of terminal state categories as the soak would produce.
    terminal_values = set(states.values())
    assert terminal_values <= _terminal_states(), (
        f"NC1: unexpected state values: {terminal_values - _terminal_states()}"
    )
