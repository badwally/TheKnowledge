# Librarian Phase 4 — Tiered Agent Surface — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split the MCP surface into a provably-safe read tier and a build tier, give the deposit consumer its bounded-acquire + backpressure contract, and wire the three per-producer telemetry alarms.

**Architecture:** Three independent tasks landing on `main`-merged Phases 1–3. T1 adds an op→tier classification table (`tier.py`) and a second `FastMCP` entrypoint registering exactly the read-classified set — default-deny: an op is `read` only if it is provably side-effect-free AND token-free, everything else is `build`. T2 makes `locking.file_lock` capable of bounded acquisition (off the current no-timeout `flock(LOCK_EX)`), wires the commit barrier to use it, and adds queue-depth backpressure to `deposit`. T3 adds an alarm surface over the existing `ProducerTelemetry` counters.

**Tech Stack:** Python 3, `pytest`, `mcp.server.fastmcp.FastMCP`, POSIX `fcntl.flock`. Always `.venv/bin/python` / `.venv/bin/pytest` / `.venv/bin/wiki`.

## Global Constraints

- **No direct writes to `wiki/` or `raw/`** — all corpus writes go through the gateway. (This phase touches none.)
- **No ranking/retrieval code touched** — `eval-retrieval --compare` must stay ≥ 0.90 (baseline recall@10 = 0.926); it is a confirm-only gate here.
- **Adversarial tests with negative controls on every concurrency / destructive / idempotency path; do NOT monkeypatch the core path under test** (standing build rule, Phases 1–3). T2 lock tests use a real second holder, real `fcntl`.
- **Merge/transform tests use realistic payloads, not minimal stubs** (Phase-3 session-review finding).
- Language: never the "honest" family or throat-clearing intros in code, comments, or docstrings.
- One commit per task. `.venv/bin/python -m pytest` is the suite runner. Baseline suite = **2163 passed**; no regression.
- Branch: `docs/librarian-phase4` (already created off `main` @ `d931e568`). Verify with `git branch --show-current` before each commit.

---

### Task 1: Op→tier classification + read-tier MCP entrypoint (A2, decision 7)

**Files:**
- Create: `src/gateway/tier.py`
- Modify: `src/gateway/mcp_server.py` (add a read-tier server factory near the bottom, after all `wiki_*` defs)
- Test: `tests/gateway/test_tier_parity.py`

**Interfaces:**
- Consumes: `gateway.cli.IMPLEMENTED` (set of op names), `gateway.mcp_server.CLI_ONLY` (frozenset), the module-level `wiki_*` callables in `mcp_server`, and `mcp_server.mcp._tool_manager.list_tools()` (returns objects with `.name`).
- Produces:
  - `tier.READ_OPS: frozenset[str]` — op names (hyphenated CLI form) that are provably side-effect-free AND token-free.
  - `tier.READ_AUX_TOOLS: frozenset[str]` — auxiliary `wiki_*` tool names (no CLI op) that are read-tier (`wiki_poll_list`, `wiki_question_list`).
  - `tier.classify(op: str) -> str` — returns `"read"` or `"build"` for any MCP-exposed op (`IMPLEMENTED - CLI_ONLY`); `KeyError` if `op` is not MCP-exposed.
  - `tier.read_tier_tool_names() -> frozenset[str]` — the full set of `wiki_*` tool names the read-tier server must register = `{f"wiki_{op.replace('-','_')}" for op in READ_OPS} | READ_AUX_TOOLS`.
  - `mcp_server.build_read_tier_server() -> FastMCP` — a fresh `FastMCP` registering exactly `tier.read_tier_tool_names()` by re-using the existing `wiki_*` functions.

**Classification rule (default-deny).** An op is `read` **iff** it performs no write (no gateway write op, no file write to `wiki/`/`raw/`/`index`/derived-canonical state, no external send) AND makes no model call (no Claude/judge/NLM token spend). Every other MCP-exposed op is `build`. When in doubt → `build`; the read tier must be a provably-safe subset, because over-including a side-effecting op on the "read" mount is a security hole while under-including only costs convenience.

**Affirmative READ_OPS** (each verified side-effect-free + token-free against its op implementation — `status`/`lint`/`agents` were initially listed but DROPPED at review: `status` conditionally writes finetune milestones + log, `lint` writes a timestamped report + log, `agents` runs write-effecting/token-spending batch agents):
`retrieve`, `search`, `context`, `related`, `intent-status`, `list-concepts`, `list-domains`, `agent-log`.
All other ops in `IMPLEMENTED - CLI_ONLY` → `build` (includes `answer`, `filter`, `query`, `ask-corpus`, `evaluate`, `cite`, `contradiction`, `triage`, `agenda`, `daily`, `digest`, `routine`, `skill-emit`, and every write/ingest/nlm op). `wiki_deposit` and `wiki_question_new` auxiliaries → `build`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/gateway/test_tier_parity.py
from __future__ import annotations

import pytest

from gateway import cli as cli_mod
from gateway import mcp_server, tier


def _mcp_exposed_ops() -> set[str]:
    return set(cli_mod.IMPLEMENTED) - set(mcp_server.CLI_ONLY)


def test_every_mcp_exposed_op_is_classified():
    """Totality: classify() returns read|build for every MCP-exposed op, none unclassified."""
    for op in _mcp_exposed_ops():
        assert tier.classify(op) in {"read", "build"}, op


def test_classify_rejects_non_mcp_exposed_op():
    """A CLI_ONLY op (or unknown op) is not classifiable — it has no tier."""
    with pytest.raises(KeyError):
        tier.classify("demote-domain")  # CLI_ONLY


def test_read_ops_are_subset_of_mcp_exposed():
    assert tier.READ_OPS <= _mcp_exposed_ops()


def test_read_tier_server_registers_exactly_the_read_classified_set():
    """Parity: the read-tier server's registered tools == the read-classified set."""
    server = mcp_server.build_read_tier_server()
    registered = {t.name for t in server._tool_manager.list_tools()}
    assert registered == set(tier.read_tier_tool_names())


def test_read_tier_excludes_build_tools_negative_control():
    """A read-tier mount does NOT register build tools — calling one is tool-not-found,
    not a silent no-op. Pin the highest-risk build tools explicitly."""
    server = mcp_server.build_read_tier_server()
    registered = {t.name for t in server._tool_manager.list_tools()}
    for build_tool in ("wiki_ingest", "wiki_query", "wiki_deposit", "wiki_filter", "wiki_edit"):
        assert build_tool not in registered


def test_full_server_still_registers_everything():
    """The full server (mcp_server.mcp) is unchanged — superset of the read tier."""
    full = {t.name for t in mcp_server.mcp._tool_manager.list_tools()}
    assert set(tier.read_tier_tool_names()) <= full
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/gateway/test_tier_parity.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'gateway.tier'` (and `build_read_tier_server` missing).

- [ ] **Step 3: Create `src/gateway/tier.py`**

```python
"""Op→tier classification — Librarian Phase 4 (A2, decision 7).

The MCP surface splits into a runtime READ tier (LLM-free, bounded, idempotent,
side-effect-free) and a BUILD tier (everything that writes or spends model
tokens). The split is DEFAULT-DENY: an op is read-tier only if it is provably
side-effect-free AND token-free; every other MCP-exposed op is build. Over-
including a side-effecting op on the read mount is a security hole, so the read
set is an explicit allowlist, not a derived complement.
"""

from __future__ import annotations

from gateway import cli as _cli
from gateway import mcp_server as _mcp


# Provably side-effect-free AND token-free ops (hyphenated CLI form). Each was
# verified to perform no corpus/derived write and make no Claude/judge/NLM call.
READ_OPS: frozenset[str] = frozenset(
    {
        "retrieve",      # FTS/BM25 retrieval ladder — LLM-free
        "search",        # FTS5/BM25 ranked search
        "context",       # page + ranked neighbors
        "related",       # co-citation neighbors
        "status",        # watcher heartbeat / pending queue
        "intent-status", # intent_id -> disposition (A1 read-tier status op)
        "lint",          # read-only health check (reports, does not fix)
        "list-concepts",
        "list-domains",
        "agent-log",     # reads operational-provenance log
        "agents",        # lists agent registry
    }
)

# Auxiliary wiki_* tools with no CLI op (see mcp_server parity test) that are
# read-tier. wiki_poll_list / wiki_question_list are read-only enumerations.
READ_AUX_TOOLS: frozenset[str] = frozenset({"wiki_poll_list", "wiki_question_list"})


def _mcp_exposed_ops() -> frozenset[str]:
    return frozenset(_cli.IMPLEMENTED) - _mcp.CLI_ONLY


def classify(op: str) -> str:
    """Return 'read' or 'build' for an MCP-exposed op. KeyError if not exposed."""
    if op not in _mcp_exposed_ops():
        raise KeyError(f"{op!r} is not an MCP-exposed op (CLI_ONLY or unknown)")
    return "read" if op in READ_OPS else "build"


def read_tier_tool_names() -> frozenset[str]:
    """wiki_* tool names the read-tier server must register."""
    return frozenset(f"wiki_{op.replace('-', '_')}" for op in READ_OPS) | READ_AUX_TOOLS
```

- [ ] **Step 4: Add `build_read_tier_server` to `mcp_server.py`**

Append after the last `wiki_*` definition (module end). It builds a fresh `FastMCP` and re-registers only the read-tier functions by looking them up on this module:

```python
def build_read_tier_server() -> "FastMCP":
    """A read-tier MCP server: registers EXACTLY the read-classified tool set
    (gateway.tier.read_tier_tool_names()). Build tools are absent — a read-tier
    mount calling a build tool gets tool-not-found, not a silent no-op (A2)."""
    from gateway import tier  # local import: tier imports mcp_server

    read = FastMCP("knowledge-gateway-read", instructions=_INSTRUCTIONS)
    import sys
    module = sys.modules[__name__]
    for name in sorted(tier.read_tier_tool_names()):
        fn = getattr(module, name, None)
        if fn is None or not callable(fn):
            raise RuntimeError(f"read-tier tool {name!r} has no implementation in mcp_server")
        read.tool()(fn)
    return read
```

Note: the existing `wiki_*` functions are decorated with `@mcp.tool()`, which registers them on `mcp` AND returns the original function, so `getattr(module, name)` is the plain callable — safe to re-register on `read`.

- [ ] **Step 5: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/gateway/test_tier_parity.py tests/gateway/test_mcp_parity.py -v`
Expected: PASS (new tier tests + existing parity tests unaffected).

- [ ] **Step 6: Commit**

```bash
git add src/gateway/tier.py src/gateway/mcp_server.py tests/gateway/test_tier_parity.py
git commit -m "feat(librarian-tier): op->tier classification + read-tier MCP entrypoint (A2, decision 7)"
```

---

### Task 2: Bounded lock acquisition + deposit backpressure (A1, A3)

**Files:**
- Modify: `src/gateway/locking.py` (`file_lock` gains bounded mode; new `LockTimeout`)
- Modify: `src/gateway/commit_gate.py:294` (commit barrier uses bounded acquire)
- Modify: `src/gateway/intent_queue.py` (add `depth()`)
- Modify: `src/gateway/ops/deposit.py` (queue-depth backpressure → `rejected:overloaded`)
- Test: `tests/gateway/test_bounded_acquire.py`, `tests/gateway/test_backpressure.py`

**Interfaces:**
- Consumes: `OperationResult(success, disposition, intent_id, retry_after, errors, summary)` (`core.py:84`); `IntentQueue.submit()` writes to `submitted/`.
- Produces:
  - `locking.LockTimeout(TimeoutError)` — raised when a bounded acquire misses its deadline.
  - `locking.file_lock(name, *, timeout: float | None = None)` — `timeout=None` keeps the current blocking `LOCK_EX` (back-compat: all existing call sites unchanged); a float bounds acquisition via `LOCK_EX | LOCK_NB` polling, raising `LockTimeout` on the deadline.
  - `IntentQueue.depth() -> int` — count of intents in `submitted/`.
  - `deposit(...)` returns `disposition="rejected:overloaded"` + `retry_after` when `queue.depth() >= deposit.MAX_BACKLOG`, else `disposition="queued"`.

**Design note (resolved from design §3.1/§3.3 + §4 migration delta).** A3 (bounded acquisition) protects the **commit consumer**: `commit_gate.py:294`'s `file_lock("librarian-commit")` — the no-timeout block called out at `locking.py:75` — becomes bounded so the committer never hangs. A1 (backpressure) is **producer-facing**: an async `deposit` sheds load by **queue depth** (it holds no commit lock — authoring is concurrent by design), returning `rejected:overloaded` + `retry_after` so the producer backs off. `«deposit.max_wait»` remains the agent-side total-wait bound surfaced as a documented constant; `«deposit.max_backlog»` (NEW key) governs the server-side shed ceiling.

- [ ] **Step 1: Write the failing bounded-acquire tests**

```python
# tests/gateway/test_bounded_acquire.py
from __future__ import annotations

import threading
import time

import pytest

from gateway import locking


def test_bounded_acquire_times_out_when_held(tmp_path, monkeypatch):
    """A real second holder blocks; a bounded acquire raises LockTimeout, never hangs.
    No monkeypatch of fcntl — real flock on a real lock file."""
    monkeypatch.setattr(locking.paths, "locks_dir", lambda: tmp_path)
    holder_has_lock = threading.Event()
    release = threading.Event()

    def hold():
        with locking.file_lock("librarian-commit"):
            holder_has_lock.set()
            release.wait(timeout=5)

    t = threading.Thread(target=hold)
    t.start()
    assert holder_has_lock.wait(timeout=5)

    start = time.monotonic()
    with pytest.raises(locking.LockTimeout):
        with locking.file_lock("librarian-commit", timeout=0.2):
            pass
    elapsed = time.monotonic() - start
    assert elapsed < 2.0, "bounded acquire must return near its deadline, not hang"

    release.set()
    t.join(timeout=5)


def test_bounded_acquire_succeeds_when_free(tmp_path, monkeypatch):
    """Negative control: a free lock acquires immediately under a bounded timeout."""
    monkeypatch.setattr(locking.paths, "locks_dir", lambda: tmp_path)
    with locking.file_lock("librarian-commit", timeout=0.2):
        pass  # no raise


def test_no_timeout_is_back_compatible_blocking(tmp_path, monkeypatch):
    """timeout=None preserves blocking LOCK_EX: it waits, then succeeds on release."""
    monkeypatch.setattr(locking.paths, "locks_dir", lambda: tmp_path)
    release = threading.Event()
    acquired = threading.Event()

    def hold():
        with locking.file_lock("x"):
            acquired.set()
            release.wait(timeout=5)

    t = threading.Thread(target=hold)
    t.start()
    assert acquired.wait(timeout=5)

    got = threading.Event()

    def waiter():
        with locking.file_lock("x"):  # no timeout -> blocks until release
            got.set()

    w = threading.Thread(target=waiter)
    w.start()
    assert not got.wait(timeout=0.3)  # still blocked while held
    release.set()
    assert got.wait(timeout=5)  # unblocks after release
    t.join(timeout=5)
    w.join(timeout=5)
```

- [ ] **Step 2: Run to verify they fail**

Run: `.venv/bin/python -m pytest tests/gateway/test_bounded_acquire.py -v`
Expected: FAIL — `AttributeError: module 'gateway.locking' has no attribute 'LockTimeout'` / `file_lock() got an unexpected keyword argument 'timeout'`.

- [ ] **Step 3: Implement bounded acquisition in `locking.py`**

Replace the `file_lock` context manager (and add the exception + a sleep import):

```python
import time

POLL_INTERVAL = 0.01  # seconds between non-blocking acquire attempts


class LockTimeout(TimeoutError):
    """A bounded file_lock acquisition missed its deadline."""

    def __init__(self, name: str, timeout: float) -> None:
        super().__init__(f"could not acquire lock {name!r} within {timeout}s")
        self.name = name
        self.timeout = timeout


@contextlib.contextmanager
def file_lock(name: str, *, timeout: float | None = None) -> Iterator[None]:
    """Acquire an exclusive lock identified by `name`.

    `timeout=None` blocks indefinitely (LOCK_EX) — the historical behavior, kept
    for every existing call site. A float bounds the acquisition: poll with
    LOCK_EX|LOCK_NB until acquired or the deadline passes, then raise LockTimeout
    (A3 — the commit barrier must never block indefinitely).
    """
    locks = paths.locks_dir()
    locks.mkdir(parents=True, exist_ok=True)
    lock_path = locks / f"{name}.lock"

    with open(lock_path, "a") as f:
        if timeout is None:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        else:
            deadline = time.monotonic() + timeout
            while True:
                try:
                    fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    break
                except OSError:
                    if time.monotonic() >= deadline:
                        raise LockTimeout(name, timeout)
                    time.sleep(POLL_INTERVAL)
        try:
            yield
        finally:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
```

- [ ] **Step 4: Run bounded-acquire tests — expect PASS**

Run: `.venv/bin/python -m pytest tests/gateway/test_bounded_acquire.py -v`
Expected: PASS.

- [ ] **Step 5: Wire the commit barrier to bounded acquire**

In `commit_gate.py`, near the top add a module constant and change line 294's acquisition. First read the surrounding `commit` method to confirm the failure path (it already has a rejection/dead-letter return shape). Add:

```python
# Bounded acquisition for the serial commit barrier (A3): the committer must
# never block indefinitely. On timeout the intent is left for a later pass
# (re-queue / retry), not hung.
COMMIT_LOCK_ACQUIRE_TIMEOUT = 30.0  # «commit.lock_acquire_timeout»
```

Change:
```python
        with locking.file_lock("librarian-commit"):
```
to:
```python
        with locking.file_lock("librarian-commit", timeout=COMMIT_LOCK_ACQUIRE_TIMEOUT):
```

Wrap the `with` in the caller so a `LockTimeout` surfaces as a bounded, retryable outcome rather than an exception escaping the commit op. Add a test in `test_bounded_acquire.py`:

```python
def test_commit_gate_acquires_commit_lock_bounded(monkeypatch):
    """The commit barrier passes a bounded timeout (not None) — never the no-timeout block."""
    import inspect
    from gateway import commit_gate
    src = inspect.getsource(commit_gate)
    assert 'file_lock("librarian-commit", timeout=' in src, (
        "commit barrier must use bounded acquisition (A3)"
    )
    assert commit_gate.COMMIT_LOCK_ACQUIRE_TIMEOUT > 0
```

(A source-level assertion is the right granularity here: it pins the migration off the no-timeout block without standing up a full concurrent-commit harness, which Phase-1/3 tests already cover. If the `commit` method's surrounding logic makes a behavioral test cheap, prefer that.)

- [ ] **Step 6: Run commit-gate test + full commit_gate suite**

Run: `.venv/bin/python -m pytest tests/gateway/test_bounded_acquire.py tests/gateway/ -k commit_gate -v`
Expected: PASS, no regression in existing commit-gate tests.

- [ ] **Step 7: Write the failing backpressure tests**

```python
# tests/gateway/test_backpressure.py
from __future__ import annotations

import pytest

from gateway import paths
from gateway.intent_queue import IntentQueue
from gateway.ops import deposit as deposit_mod


@pytest.fixture
def queue(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "knowledge_root", lambda: tmp_path)
    return IntentQueue()


def _payload():
    return {"page_type": "entity", "title": "T", "body": "some body"}


def test_deposit_queues_when_below_backlog(queue):
    """Negative control: with the queue empty, deposit returns queued (+ retry_after)."""
    r = deposit_mod.deposit(_payload(), {"identity": "agent-a"}, queue=queue)
    assert r.disposition == "queued"
    assert r.retry_after is not None
    assert r.intent_id


def test_deposit_sheds_load_when_backlog_exceeded(queue, monkeypatch):
    """Under load (submitted backlog >= MAX_BACKLOG), deposit returns rejected:overloaded
    + retry_after and enqueues nothing new."""
    monkeypatch.setattr(deposit_mod, "MAX_BACKLOG", 3)
    for i in range(3):
        deposit_mod.deposit(
            {"page_type": "entity", "title": f"T{i}", "body": "b"},
            {"identity": "agent-a"},
            queue=queue,
        )
    assert queue.depth() == 3
    r = deposit_mod.deposit(_payload(), {"identity": "agent-a"}, queue=queue)
    assert r.disposition == "rejected:overloaded"
    assert r.retry_after is not None
    assert not r.success
    assert queue.depth() == 3  # nothing new enqueued


def test_queue_depth_counts_submitted(queue):
    assert queue.depth() == 0
    deposit_mod.deposit(_payload(), {"identity": "a"}, queue=queue)
    assert queue.depth() == 1
```

- [ ] **Step 8: Run to verify they fail**

Run: `.venv/bin/python -m pytest tests/gateway/test_backpressure.py -v`
Expected: FAIL — `IntentQueue` has no `depth`; `deposit` module has no `MAX_BACKLOG`.

- [ ] **Step 9: Add `IntentQueue.depth()`**

In `intent_queue.py`, add a method on `IntentQueue` (uses the existing `_state_dir` helper):

```python
    def depth(self) -> int:
        """Number of intents currently in submitted/ (queue backlog, for A1 backpressure)."""
        sub_dir = self._state_dir("submitted")
        if not sub_dir.exists():
            return 0
        return sum(1 for p in sub_dir.glob("*.json"))
```

- [ ] **Step 10: Add backpressure to `deposit`**

In `ops/deposit.py`, add the ceiling constant and the depth check (after validation, before enqueue):

```python
# Server-side shed ceiling «deposit.max_backlog»: when the submitted backlog is at
# or above this, deposit sheds load (A1 backpressure) so producers back off rather
# than growing an unbounded queue. «deposit.max_wait» (agent total-wait bound) is a
# separate, agent-facing contract surfaced via retry_after.
MAX_BACKLOG = 256
```

After the `errors` check and `q = queue or IntentQueue()`, before `compute_intent_id`:

```python
    if q.depth() >= MAX_BACKLOG:
        return OperationResult(
            success=False,
            disposition="rejected:overloaded",
            retry_after=_RETRY_AFTER,
            errors=["deposit queue is at capacity; retry after backoff"],
            summary="deposit shed: queue overloaded",
        )
```

- [ ] **Step 11: Run backpressure + deposit suites — expect PASS**

Run: `.venv/bin/python -m pytest tests/gateway/test_backpressure.py tests/gateway/ -k deposit -v`
Expected: PASS, existing deposit tests unaffected.

- [ ] **Step 12: Commit**

```bash
git add src/gateway/locking.py src/gateway/commit_gate.py src/gateway/intent_queue.py src/gateway/ops/deposit.py tests/gateway/test_bounded_acquire.py tests/gateway/test_backpressure.py
git commit -m "feat(librarian-deposit): bounded commit-lock acquire + queue-depth backpressure (A1, A3)"
```

---

### Task 3: Per-producer telemetry alarms (A7)

**Files:**
- Modify: `src/gateway/provenance.py` (alarm surface over `ProducerTelemetry`)
- Test: `tests/gateway/test_producer_telemetry.py`

**Interfaces:**
- Consumes: `ProducerTelemetry.incr(identity, kind)` where `kind ∈ {"accept","reject","merge"}`; `ProducerTelemetry.snapshot() -> dict[identity, dict[kind, int]]`.
- Produces: `provenance.alarms(snapshot, *, prev_snapshot=None, thresholds=None) -> list[dict]` — one dict per fired alarm: `{"identity": str, "alarm": str, "detail": dict}` with `alarm ∈ {"rejection-spike","dedup-merge-spike","deposit-silence"}`. Pure function over snapshots (no I/O), so it is replayable and unit-testable.
- Produces: `provenance.ALARM_THRESHOLDS` — module dict with `rejection_rate` (default 0.5), `merge_rate` (default 0.8), `min_volume` (default 5). Silence requires `prev_snapshot`.

**Detectors (design §3.3):**
- **rejection-spike** — `reject / (accept+reject+merge) >= rejection_rate` AND total `>= min_volume`.
- **dedup-merge-spike** — `merge / (accept+merge) >= merge_rate` AND `(accept+merge) >= min_volume` (a producer contributing only non-novel content).
- **deposit-silence** — a producer present with activity in `prev_snapshot` whose total is unchanged in the current snapshot (dropped to zero new activity). Requires `prev_snapshot`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/gateway/test_producer_telemetry.py
from __future__ import annotations

from gateway import provenance
from gateway.provenance import ProducerTelemetry


def _fired(alarms, name):
    return {a["identity"] for a in alarms if a["alarm"] == name}


def test_rejection_spike_fires():
    t = ProducerTelemetry()
    for _ in range(8):
        t.incr("bad-agent", "reject")
    for _ in range(2):
        t.incr("bad-agent", "accept")
    alarms = provenance.alarms(t.snapshot())
    assert "bad-agent" in _fired(alarms, "rejection-spike")


def test_dedup_merge_spike_fires():
    t = ProducerTelemetry()
    for _ in range(9):
        t.incr("stale-agent", "merge")
    t.incr("stale-agent", "accept")
    alarms = provenance.alarms(t.snapshot())
    assert "stale-agent" in _fired(alarms, "dedup-merge-spike")


def test_deposit_silence_fires():
    prev = ProducerTelemetry()
    for _ in range(10):
        prev.incr("was-active", "accept")
    prev_snap = prev.snapshot()
    # current: identical totals -> no new activity since prev -> silence
    cur = ProducerTelemetry()
    for _ in range(10):
        cur.incr("was-active", "accept")
    alarms = provenance.alarms(cur.snapshot(), prev_snapshot=prev_snap)
    assert "was-active" in _fired(alarms, "deposit-silence")


def test_healthy_traffic_fires_nothing_negative_control():
    t = ProducerTelemetry()
    for _ in range(20):
        t.incr("good-agent", "accept")
    for _ in range(2):
        t.incr("good-agent", "reject")
    for _ in range(1):
        t.incr("good-agent", "merge")
    # prev with strictly less activity -> not silent
    prev = ProducerTelemetry()
    for _ in range(5):
        prev.incr("good-agent", "accept")
    alarms = provenance.alarms(t.snapshot(), prev_snapshot=prev.snapshot())
    assert alarms == []


def test_low_volume_does_not_trip_spikes_negative_control():
    """A producer below min_volume cannot trip a spike alarm (noise suppression)."""
    t = ProducerTelemetry()
    t.incr("new-agent", "reject")
    t.incr("new-agent", "merge")
    assert provenance.alarms(t.snapshot()) == []
```

- [ ] **Step 2: Run to verify they fail**

Run: `.venv/bin/python -m pytest tests/gateway/test_producer_telemetry.py -v`
Expected: FAIL — `module 'gateway.provenance' has no attribute 'alarms'`.

- [ ] **Step 3: Implement the alarm surface in `provenance.py`**

Append (and update the A7-stub docstring note at the top of the class to say alarms are now wired):

```python
ALARM_THRESHOLDS: dict[str, float] = {
    "rejection_rate": 0.5,  # reject / total
    "merge_rate": 0.8,      # merge / (accept+merge) — only-non-novel producer
    "min_volume": 5,        # below this, spikes are suppressed as noise
}


def alarms(
    snapshot: dict[str, dict[str, int]],
    *,
    prev_snapshot: dict[str, dict[str, int]] | None = None,
    thresholds: dict[str, float] | None = None,
) -> list[dict]:
    """Per-producer alarm detectors (A7). Pure over snapshots — replayable.

    - rejection-spike: reject/total >= rejection_rate, total >= min_volume
    - dedup-merge-spike: merge/(accept+merge) >= merge_rate, (accept+merge) >= min_volume
    - deposit-silence: a producer active in prev_snapshot with no new activity now
    """
    th = {**ALARM_THRESHOLDS, **(thresholds or {})}
    min_volume = th["min_volume"]
    out: list[dict] = []

    for identity, kinds in snapshot.items():
        accept = kinds.get("accept", 0)
        reject = kinds.get("reject", 0)
        merge = kinds.get("merge", 0)
        total = accept + reject + merge

        if total >= min_volume and reject / total >= th["rejection_rate"]:
            out.append({
                "identity": identity,
                "alarm": "rejection-spike",
                "detail": {"reject": reject, "total": total, "rate": reject / total},
            })

        novel_denom = accept + merge
        if novel_denom >= min_volume and merge / novel_denom >= th["merge_rate"]:
            out.append({
                "identity": identity,
                "alarm": "dedup-merge-spike",
                "detail": {"merge": merge, "accept": accept, "rate": merge / novel_denom},
            })

    if prev_snapshot is not None:
        for identity, prev_kinds in prev_snapshot.items():
            prev_total = sum(prev_kinds.values())
            cur_total = sum(snapshot.get(identity, {}).values())
            if prev_total > 0 and cur_total <= prev_total:
                out.append({
                    "identity": identity,
                    "alarm": "deposit-silence",
                    "detail": {"prev_total": prev_total, "cur_total": cur_total},
                })

    return out
```

- [ ] **Step 4: Run to verify they pass**

Run: `.venv/bin/python -m pytest tests/gateway/test_producer_telemetry.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/gateway/provenance.py tests/gateway/test_producer_telemetry.py
git commit -m "feat(librarian-telemetry): per-producer alarms — rejection/merge spike + silence (A7)"
```

---

## Gate (run after all three tasks)

- [ ] Full suite, no regression vs 2163: `.venv/bin/python -m pytest -q`
- [ ] Tier parity + read-tier negative control: `.venv/bin/python -m pytest tests/gateway/test_tier_parity.py tests/gateway/test_mcp_parity.py -v`
- [ ] Bounded acquire (real holder, no fcntl monkeypatch) + backpressure: `.venv/bin/python -m pytest tests/gateway/test_bounded_acquire.py tests/gateway/test_backpressure.py -v`
- [ ] A7 detector tests + negative controls: `.venv/bin/python -m pytest tests/gateway/test_producer_telemetry.py -v`
- [ ] Confirm-only (no retrieval code touched): `.venv/bin/wiki eval-retrieval --compare` — recall@10 ≥ 0.90 (expect 0.926 unmoved).
- [ ] `.venv/bin/wiki lint` clean (no NEW findings vs the pre-existing source-orphan / long-filename baseline).
- [ ] Independent review (reviewer ≠ author) + background security review. A failing eval OR review HALTS.
- [ ] `/session-review`, checkpoint `docs/session-state.md` + ledger §4/§5 Phase-4 rows, branch-guarded commit, push branch + open PR.

## Self-Review

- **Spec coverage:** T1 → A2 + decision 7 (read/build split, two entrypoints, op→tier table); T2 → A1 (backpressure receipt) + A3 (bounded acquire off the no-timeout flock) + «deposit.max_wait»/«deposit.max_backlog»; T3 → A7 (three named §16 detectors). All four Phase-4 green-gate items covered.
- **Deviation flagged:** `«deposit.max_backlog»` is a NEW ledger key (server-side shed ceiling) — the design names backpressure but not its mechanism; queue-depth shed is the async-clean, deterministically-testable choice. Surface at the gate for the ledger §1/§5 update.
- **Type consistency:** `disposition` strings (`queued`, `rejected:overloaded`), `retry_after`, `intent_id` all match `OperationResult` (`core.py:84`). `ProducerTelemetry` kinds (`accept`/`reject`/`merge`) match the alarm denominators. `file_lock(name, *, timeout=None)` keeps every existing positional call site valid.
- **No monkeypatch of the path under test:** bounded-acquire tests use a real second-thread holder + real `fcntl`; only `paths.locks_dir` is redirected to `tmp_path` (test isolation, not the path under test).
