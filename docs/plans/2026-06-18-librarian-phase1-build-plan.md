# Librarian Phase 1 — Commit foundation — build plan — 2026-06-18

Scoped, bite-sized implementation plan for **Phase 1 only** of the Librarian
multi-agent RAG build. Derived from the roadmap
(`2026-06-18-librarian-multi-agent-rag-build-plan.md` § "Phase 1"), the ledger
(`2026-06-18-librarian-multi-agent-rag-checkpoints.md` §4/§1.1/§5) and the design
(§2 integrity boundary, §3 deposit/intent lifecycle, §5 commit protocol, §14
placement/start-boring).

**Baseline (Step 0).** `pytest tests/gateway` → **1960 passed**.
`wiki eval-retrieval --compare` → recall@5 0.852 / **recall@10 0.926** / MRR 0.690.
Green-gate = no NEW failures vs 1960 + new Phase-1 tests pass + recall@10 ≥ 0.90
(unmoved — Phase 1 touches no retrieval code).

## Global Constraints

- Branch MUST be `docs/librarian-rag-design`. Never commit to main. Verify with
  `git branch --show-current` before every commit.
- `.venv/bin/python` and `.venv/bin/wiki` ONLY.
- NEVER `git add -A` / `git add -u`. Stage explicit file lists only. Leave the
  watcher-owned `log.md` change unstaged.
- All wiki/raw writes go through the gateway. Phase 1 adds gateway *internals*
  (queue, gate, provenance) — it does not bypass the gateway.
- TDD per task: write failing test → run (confirm RED) → implement minimally → run
  (confirm GREEN) → run broader suite → commit with explicit `git add --`.
- Pre-decided forks (do NOT deviate):
  - Commit gate = a **commit MUTEX**: add `"librarian-commit"` to
    `locking.LOCK_NAMES`; serialize commit with `locking.file_lock("librarian-commit")`.
  - Async return = **extend `OperationResult`** with optional `intent_id`,
    `disposition`, `retry_after`, `canonical_path` (default `None`); extend
    `mcp_server._serialize`. No separate IntentReceipt class.
  - Intent queue = a **durable directory** under `.knowledge/intents/<state>/`
    (subdirectory-per-state lifecycle), NOT in-memory, NOT SQLite.
- New state lives under `.knowledge/` (gitignored internal), addressed via new
  `paths` helpers. Intent files are JSON (content-addressed payload + metadata).

## Interfaces overview (exact signatures produced this phase)

```python
# src/gateway/intent_queue.py
@dataclass(frozen=True)
class Intent:
    intent_id: str
    payload: dict            # the declarative deposit body
    identity: dict           # {agent, project, session} — self-declared
    head_oid: str | None     # HEAD ref the intent was authored against
    depends_on: str | None   # antecedent intent_id (C6), optional

@dataclass(frozen=True)
class Claim:
    intent: Intent
    fencing_token: int       # monotonic per intent_id (C3)
    lease_deadline: float    # epoch seconds (C3, «commit.lease_ttl»)

STATES = ("submitted", "claimed", "authored", "committed", "rejected", "dead_lettered")

def compute_intent_id(payload, identity, *, semantics="deposit") -> str
class IntentQueue:
    def __init__(self, root: Path | None = None)
    def submit(self, intent: Intent) -> str                 # returns intent_id, durable before return
    def claim(self, *, lease_ttl: float = 120.0, now: float | None = None) -> Claim | None
    def renew(self, intent_id: str, *, lease_ttl=120.0, now=None) -> bool
    def set_state(self, intent_id: str, state: str) -> None
    def get_state(self, intent_id: str) -> str | None
    def load(self, intent_id: str) -> Intent | None
    def fencing_token(self, intent_id: str) -> int | None
    def reclaim_expired(self, *, now=None) -> list[str]      # claimed→submitted on lease expiry

# src/gateway/core.py — OperationResult gains optional fields (default None)
#   intent_id, disposition, retry_after, canonical_path

# src/gateway/ops/intent_status.py
def intent_status(intent_id: str, *, queue: IntentQueue | None = None) -> OperationResult

# src/gateway/commit_gate.py
@dataclass(frozen=True)
class AuthoredIntent:
    intent: Intent
    writes: dict[str, str]   # {relative_path: file_content}
    base_oid: str            # blob/HEAD snapshot authored against
class CommitGate:
    def __init__(self, root=None, queue=None, provenance=None,
                 max_rebase_attempts=8)
    def commit(self, authored: AuthoredIntent, fencing_token: int) -> OperationResult
    def recover(self) -> list[str]   # reset tree + reclaim expired

# src/gateway/provenance.py
def record(intent_id, decision_basis: dict, *, root=None) -> str   # node_id
def coverage_gap(root=None) -> list[str]                            # commits w/o a node
class ProducerTelemetry:  # A7 stub — counters only
    def incr(self, identity, kind): ...
    def snapshot(self) -> dict: ...
```

---

## Task 1.1 — Intent queue: durable directory + on-disk lifecycle states

**Files.** Create `src/gateway/intent_queue.py`; modify `src/gateway/paths.py`
(add `intents_dir()`); test `tests/gateway/test_intent_queue.py`.
**Lands:** C3 (fencing token at claim), C7 (queue is the deposit path), decision 14
(start-boring directory), «commit.lease_ttl».

**Interfaces.** Produces `IntentQueue` (signatures above). Consumes `paths`.

**RED→GREEN→commit:**

1. RED — write `test_intent_queue.py`:
   - `test_submit_durable_then_new_instance_sees_submitted`: submit an intent on one
     `IntentQueue`, construct a *fresh* `IntentQueue(root=same)`, assert
     `get_state(id) == "submitted"` and `load(id).payload` round-trips (durability;
     contrast `watcher.py:78` in-memory).
   - `test_compute_intent_id_is_stable_and_content_addressed`: same
     (payload, identity, semantics) → same id; different payload → different id.
   - `test_claim_issues_monotonic_fencing_token_and_lease`: two successive
     claim/reclaim cycles on the same intent issue strictly increasing tokens;
     `claim()` moves state submitted→claimed and returns a `lease_deadline` in the
     future.
   - `test_claim_returns_none_when_empty`.
   - `test_reclaim_expired_returns_claimed_to_submitted`: claim with tiny ttl,
     advance `now`, `reclaim_expired()` returns the id and state is `submitted`.
   - `test_renew_extends_lease_and_blocks_reclaim`.
   - `test_set_get_state_round_trip_all_states`.
   - Run: `pytest tests/gateway/test_intent_queue.py -q` → RED.
2. GREEN — implement `intent_queue.py`. Storage: one JSON file per intent at
   `intents_dir()/<state>/<intent_id>.json` (state = subdirectory). Move on
   transition via `os.replace`. Fencing token persisted in the JSON
   (`fencing_token`), bumped on each `claim`. `lease_deadline` in JSON.
   `compute_intent_id` = `sha256` over canonical-json of `(payload, identity,
   semantics)`, hex, truncated to 16. `submit` writes to `submitted/` atomically
   (`write_atomic`-style temp+rename) before returning. `claim` scans `submitted/`
   sorted by mtime, picks oldest, bumps token, sets lease, moves to `claimed/`.
   `reclaim_expired` scans `claimed/` for `lease_deadline < now` → move to
   `submitted/`. Add `paths.intents_dir()` = `knowledge_internal() / "intents"`.
3. Run task test → GREEN; run `pytest tests/gateway -q` → no new failures.
4. Commit: `git add -- src/gateway/intent_queue.py src/gateway/paths.py tests/gateway/test_intent_queue.py`.

---

## Task 1.2 — Async return type: `OperationResult` ext + `_serialize` ext

**Files.** Modify `src/gateway/core.py` (`OperationResult`),
`src/gateway/mcp_server.py` (`_serialize`); test
`tests/gateway/test_async_return_type.py`; assert `test_mcp_parity.py` stays green.
**Lands:** A5 (async return shape).

**RED→GREEN→commit:**

1. RED — `test_async_return_type.py`:
   - `test_operation_result_new_fields_default_none`: `OperationResult(success=True)`
     has `intent_id is None`, `disposition is None`, `retry_after is None`,
     `canonical_path is None`.
   - `test_serialize_omits_none_new_fields_for_legacy_consumer`: `_serialize` of a
     plain result still has exactly the legacy keys plus no surprise — legacy keys
     present; new keys present only when set (or always present but None).
   - `test_serialize_surfaces_new_fields_when_set`: result with
     `intent_id="abc", disposition="queued", retry_after=30,
     canonical_path=Path("wiki/x.md")` round-trips through `_serialize` (canonical_path
     stringified).
   - Run → RED.
2. GREEN — add four optional fields (default `None`) to `OperationResult`. Extend
   `_serialize` to always include `intent_id`, `disposition`, `retry_after`, and
   `canonical_path` (stringified path or None). Keep legacy keys unchanged.
3. Run `test_async_return_type.py` + `test_mcp_parity.py` + full suite → GREEN.
4. Commit: `git add -- src/gateway/core.py src/gateway/mcp_server.py tests/gateway/test_async_return_type.py`.

---

## Task 1.3 — Status-query op: intent_id → typed disposition + poll hint

**Files.** Create `src/gateway/ops/intent_status.py`; modify
`src/gateway/cli.py` (add `intent-status` to `IMPLEMENTED`, parser stub, dispatch
+ `_run_intent_status`), `src/gateway/mcp_server.py` (register `wiki_intent_status`);
test `tests/gateway/test_intent_status.py`.
**Lands:** A1 (consumer wait-contract), A5 (terminal union), «deposit.max_wait».

**Note (parity).** Adding `wiki_intent_status` requires `intent-status` in
`cli.IMPLEMENTED` and a CLI dispatch, else `test_mcp_parity.py` fails (no orphan MCP
tools). We add both. `SUBCOMMANDS` needs an entry too (parser help). Disposition map
per design §3: committed→path, merged→canonical_path, rejected→rule,
quarantined→queue, dead_lettered→reason; non-terminal → retry_after.

**RED→GREEN→commit:**

1. RED — `test_intent_status.py`:
   - For each terminal state, seed a queue intent in that state and assert
     `intent_status(id, queue=q)` returns `disposition` = that state and the right
     field (committed → `canonical_path` set to the committed page path stored on the
     intent; merged → `canonical_path` ≠ deposited target; rejected/dead_lettered →
     `summary`/`disposition` carries the reason).
   - `test_non_terminal_returns_retry_after`: `submitted`/`claimed`/`authored` →
     `retry_after` set (== «deposit.max_wait» default 30) and `disposition` the
     non-terminal state.
   - `test_unknown_intent_id_returns_failure`.
   - Run → RED.
2. GREEN — implement `intent_status`. Read state from queue; map to
   `OperationResult` with `intent_id` + `disposition` + (`canonical_path` |
   `retry_after`). Store terminal metadata (committed path, merge canonical path,
   reject/dead-letter reason) in the intent JSON `result` field, written by the gate
   (T4). Wire CLI: `_run_intent_status(ns)` prints `_serialize`-style JSON; register
   `wiki_intent_status` MCP tool; add `"intent-status"` to `IMPLEMENTED` and
   `SUBCOMMANDS`.
3. Run task test + `test_mcp_parity.py` + full suite → GREEN.
4. Commit: `git add -- src/gateway/ops/intent_status.py src/gateway/cli.py src/gateway/mcp_server.py tests/gateway/test_intent_status.py`.

---

## Task 1.4 — CommitGate: serial commit + MVCC CAS + idempotency + crash recovery

**Files.** Create `src/gateway/commit_gate.py`; modify `src/gateway/locking.py`
(add `"librarian-commit"` to `LOCK_NAMES`); test
`tests/gateway/test_commit_gate.py`, `tests/gateway/test_commit_gate_recovery.py`.
**Lands:** C1, C2, C3, C4, decision 1 (single serialization point), §4 migration
delta (commit mutex), «commit.max_rebase_attempts», «commit.lease_ttl».

**Interfaces.** `CommitGate.commit(authored, fencing_token) -> OperationResult`;
`CommitGate.recover() -> list[str]`. Consumes `core.write_atomic`, the
`discharge_orphans` git-shell pattern (`git add -- <explicit>` then `git commit`,
never `-A`), `intent_queue` (T1), `OperationResult` (T2).

**Mechanics.**
- Commit serialized by `locking.file_lock("librarian-commit")` (the mutex).
- Tests run against a throwaway git repo (`tmp_path` with `git init`,
  `KNOWLEDGE_ROOT` monkeypatched to it). Helper in test builds the repo.
- CAS = compare authored `base_oid` per written path vs current
  blob OID at HEAD (via `git hash-object` of the working file or
  `git rev-parse HEAD:<path>`). Three cases:
  1. No overlap (path unchanged since base, or new path) → write + commit.
  2. Same path, mergeable (base differs but authored content can be re-applied) →
     rebase: re-read HEAD content, re-apply (for Phase 1, "mergeable" = authored
     content already equals HEAD content OR a no-conflict union; minimal: re-run up
     to «commit.max_rebase_attempts», then dead-letter `contention`). Phase 1 ships
     the bounded-attempt loop + dead-letter; full claim-merge is Phase 3.
  3. Same path, contradictory → dead-letter with reason.
- Idempotency (C2): write `Intent-Id: <id>` trailer into the commit message AND an
  `applied_intents` record (a line in `.knowledge/intents/applied_intents.log`
  committed in the same commit). `commit()` first scans committed history
  (`git log --grep="Intent-Id: <id>"`) — if found, no-op, return prior disposition
  (`no_op=True`, `disposition="committed"`, `canonical_path` from the record).
- Fencing (C3): reject commit whose `fencing_token` < the highest token issued for
  that intent_id (read from queue). Returns failure `disposition="rejected"` reason
  `stale-fencing-token`.
- Crash recovery (C1): `recover()` = `git reset --hard HEAD` + `git clean -fd`, then
  `queue.reclaim_expired()`; returns reclaimed ids.

**RED→GREEN→commit:**

1. RED — `test_commit_gate.py`:
   - `test_lock_name_registered`: `"librarian-commit" in locking.LOCK_NAMES`.
   - `test_commit_no_overlap_writes_and_commits`: commit an authored intent writing
     `wiki/sources/x.md`; assert file present, `git log -1` message contains
     `Intent-Id: <id>`, result `success`, `disposition="committed"`,
     `canonical_path` set, intent state `committed`.
   - `test_redeliver_committed_intent_is_noop_from_history`: commit, then commit the
     same intent_id again → `no_op=True`, no second commit (HEAD unchanged),
     disposition `committed`. (C2 — scans committed history, not status file: prove
     by deleting the queue intent's status file before redelivery and still no-op.)
   - `test_stale_fencing_token_rejected`: issue token 1 then reclaim→token 2; commit
     with token 1 → failure `rejected`/`stale-fencing-token`, HEAD unchanged. (C3)
   - `test_contradictory_edit_dead_letters`: base_oid stale + content conflicts →
     state `dead_lettered`, reason recorded.
   - `test_bounded_rebase_dead_letters_contention`: force rebase to exceed
     `max_rebase_attempts=2` → `dead_lettered` reason `contention`. (C4)
   - `test_writes_serialized_at_one_gate` (never-regress): two threads each call
     `commit()` on distinct intents/paths; both succeed, git history linear, no
     `.git/index.lock` error. (decision 1)
   - Run → RED.
2. RED — `test_commit_gate_recovery.py`:
   - `test_recover_resets_dirty_tree_and_reclaims`: dirty the working tree (write a
     stray file + modify a tracked file), claim an intent with expired lease,
     `recover()` → `git status --porcelain` empty, reclaimed id returned, state
     `submitted`. (C1)
   - Run → RED.
3. GREEN — implement `commit_gate.py` + add lock name.
4. Run both gate tests + full suite → GREEN.
5. Commit: `git add -- src/gateway/commit_gate.py src/gateway/locking.py tests/gateway/test_commit_gate.py tests/gateway/test_commit_gate_recovery.py`.

---

## Task 1.5 — Operational-provenance log + C7 ingest routing + telemetry stub

**Files.** Create `src/gateway/provenance.py`; modify `src/gateway/commit_gate.py`
(record a provenance node on every commit), `src/gateway/watcher.py` (emit a
provenance node on ingest, C7); test `tests/gateway/test_provenance.py`,
`tests/gateway/test_provenance_coverage.py`.
**Lands:** C7, decision 3 (operational-provenance graph + decision-basis recording),
A7 (per-producer telemetry counters stubbed).

**Interfaces.** `provenance.record(intent_id, decision_basis, *, root) -> node_id`
appends a JSON line to `.knowledge/provenance/nodes.jsonl` (adds-alongside `log.md`,
not a replacement). `coverage_gap(root) -> list[str]` = committed corpus changes with
no provenance node (scan `git log` for corpus-touching commits, cross-ref node
`commit`/`intent_id`). `ProducerTelemetry` counters (A7 stub).

**RED→GREEN→commit:**

1. RED — `test_provenance.py`:
   - `test_record_appends_node_with_decision_basis`: record returns a node_id; node
     read back carries `intent_id`, `decision_basis` (policy version, dedup score +
     candidates, merge/rebase branch), `timestamp`.
   - `test_commit_records_exactly_one_node`: a CommitGate commit produces exactly one
     provenance node referencing the commit SHA. (decision 3)
   - `test_replay_from_node_without_llm`: the node carries enough to re-derive the
     committed canonical path without an LLM call (assert canonical_path replays).
   - `test_producer_telemetry_counters`: `incr`/`snapshot` count accept/reject/merge
     per identity. (A7)
   - Run → RED.
2. RED — `test_provenance_coverage.py`:
   - `test_every_committed_change_has_ancestor`: after N gate commits,
     `coverage_gap()` is empty.
   - `test_watcher_ingest_emits_provenance_node` (C7): drive
     `WatcherDaemon._process` with a stub ingest returning success + a touched path;
     assert a provenance node is recorded for that ingest (identity `watcher`), so a
     watcher ingest is not a corpus change without an ancestor.
   - Run → RED.
3. GREEN — implement `provenance.py`; have `CommitGate.commit` call
   `provenance.record(...)` inside the mutex with the decision basis; have
   `watcher._process` record a provenance node on successful ingest (alongside the
   existing `ingest.complete` event). Telemetry counters incremented at commit
   accept/reject/merge.
4. Run both tests + full suite → GREEN.
5. Commit: `git add -- src/gateway/provenance.py src/gateway/commit_gate.py src/gateway/watcher.py tests/gateway/test_provenance.py tests/gateway/test_provenance_coverage.py`.

---

## Never-regress invariant tests (green-gate roll-up)

Covered across tasks; collate the three §4 invariants explicitly:
- writes serialized at one gate → `test_writes_serialized_at_one_gate` (T4).
- reads non-blocking against a committed ref → `intent_status` reads never take the
  commit mutex: `test_intent_status` runs with no lock held; add
  `test_status_query_does_not_block_on_commit_mutex` (acquire `librarian-commit` in a
  thread, assert `intent_status` still returns) in `test_commit_gate.py`.
- validator still rejects ungrounded claims → existing validator suite unchanged
  (no Phase-1 edit to `validator.py`); assert by the full suite staying green.

## EVAL GATE

- `pytest tests/gateway -q` → ≥ 1960 passed, no new failures, all new tests pass.
- `wiki eval-retrieval --compare` → recall@10 ≥ 0.90 (unmoved from 0.926).
- `wiki lint` → no new errors in touched scopes.
- C1 (`test_recover_resets_dirty_tree_and_reclaims`), C2
  (`test_redeliver_committed_intent_is_noop_from_history`), C3
  (`test_stale_fencing_token_rejected`), C7
  (`test_watcher_ingest_emits_provenance_node`) all pass.

## Cursor update (end of phase)

- Ledger §5: flip the four Phase-1 component rows to `green` (or `in-progress`).
- `docs/session-state.md`: one line — Phase 1 status + next atomic step (Phase 2).
- Commit cursor edits with explicit `git add --`.
