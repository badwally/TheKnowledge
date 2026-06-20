# Production Committer + Multi-Agent Test Harness — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Each task gets a fresh implementer subagent + an independent reviewer (reviewer ≠ author) per `docs/MULTI-AGENT-BUILD-PLAYBOOK.md`.

**Goal:** Build the production intent-queue COMMITTER (the missing async deposit→commit drainer) and a 6-tier automated test harness that drives the REAL system end-to-end — no simulators.

**Architecture:** Deposits already enqueue durably (`ops/deposit.py` → `IntentQueue.submit()` → `submitted/`), and `CommitGate.commit()` already authors+commits a fully-rendered `AuthoredIntent` under the `librarian-commit` lock with fencing/lease/recovery/backpressure. The gap: nothing in production connects `claim()` → render → `commit()`. This plan adds (1) `author_deposit()` to render a deposit payload into an `AuthoredIntent`, (2) a drain loop that claims→authors→commits→handles disposition, (3) a `wiki commit-worker` CLI + daemon entry, plus a `wiki demand-cluster` driver — then drives all of it through a 6-tier test harness (markers, integration flows, N-agent soak, MCP+CLI surface E2E, inert-in-production property tests, pre-merge gate script).

**Tech Stack:** Python 3 (`.venv/bin/python` / `.venv/bin/wiki` ONLY), pytest, FastMCP, fcntl file locks, git-as-database.

## Global Constraints

- **`.venv/bin/python` and `.venv/bin/wiki` ONLY** — never system `python`.
- **Never `git add -A` / `git add -u`.** Stage explicit paths only. Guard `git branch --show-current` == `test/multi-agent-test-harness` before EVERY commit. Never stage watcher-owned `index.md` / `log.md` / `.knowledge/.index` / `.knowledge/` runtime state.
- **No monkeypatching the core path under test.** Real fcntl locks, real git repos, real gate commits, real encoders. Redirect only `paths.*` dirs / `KNOWLEDGE_ROOT` to tmp.
- **Merge/transform/reattachment/reverse tests use REALISTIC payloads** — full multi-section body, frontmatter aliases, inbound + body wikilinks, non-empty preamble — never claims-only stubs.
- **Adversarial tests with named negative controls** for every concurrency / destructive / idempotency / merge path. Negative control must go RED on pre-fix code.
- **Scoped lints only** (`orphans` / `schema-drift` / `broken-wikilinks`) — never unscoped (it hangs ~1h28m).
- **Eval floor:** `retrieval_eval.evaluate("fts").recall_at(10) ≥ 0.90` (baseline 0.926, must not regress); `merge_map_eval` no regressions; `embedding_eval.evaluate_all()` all namespaces pass.
- **No `timeout`/`gtimeout` wrapping fast scoped commands** (absent on darwin; wasted calls in Phase-5).
- A failing eval **or** review **HALTS** — no advance.

## Verified Interfaces (from contp appendix — reuse, do NOT re-verify)

- `deposit()` `ops/deposit.py:133`; payload fields `page_type` (entity/concept/source/synthesis), `title`, `body` (markdown), `aliases`, `domains`, `synthesizes`, `durable`, `volatile` (`ops/deposit.py:80-123`).
- `IntentQueue.submit()` `intent_queue.py:215`; `IntentQueue.claim(*, lease_ttl=120.0, now=None) -> Claim | None` `intent_queue.py:222` (atomic `os.replace` → `claimed/`, advances fencing); `IntentQueue.depth()`.
- `CommitGate.commit(authored: AuthoredIntent, fencing_token: int) -> OperationResult` `commit_gate.py:298` (takes `file_lock("librarian-commit", timeout=30.0)`). `AuthoredIntent.writes: dict[rel, str]` = already-rendered content; `commit()` does NOT render.
- **Mirror target for `author_deposit`:** `_authored_entity` fixture in `tests/gateway/test_dedup_commit.py` encodes deposit→page logic. Use `fm.serialize` + slug logic.
- `DemandLedger.cluster(self) -> list[GapCluster]` `demand_ledger.py:175` (GapCluster: `centroid_text`/`member_texts`/`recurrence_mass`/`triggered`); `record_gap(self, text, *, caller=None) -> GapRecord` `:162`; trigger submits `page_type=synthesis` + `demand_trigger=True` via `submit()` `:323`.
- **CLI op registration** — mirror `remediate`: `SUBCOMMANDS` dict `cli.py:117`, `IMPLEMENTED` set `:195`, `CLI_ONLY` set, `build_parser` add_parser `:463`, `main()` dispatch `:1661`, `_run_remediate` handler `:2945` (`from gateway.ops.X import X; result = X(...); return _emit_result(result)`). `cli.main(argv: list[str] | None) -> int`.
- **MCP E2E:** `mcp` (build server) `mcp_server.py:37`; `build_read_tier_server()` `:1444`; `from mcp.shared.memory import create_connected_server_and_client_session` (pass FastMCP directly). Read allowlist = `tier.read_tier_tool_names()` (`tier.py:30` READ_OPS + READ_AUX_TOOLS).
- **CLI E2E:** `cli.main([...]) -> int`; patterns `test_smoke.py:35`, `test_agents_cli.py:113`; git-repo fixture `test_commit_gate.py:57-69` (`repo` fixture).
- **Concurrency pattern:** `threading.Event` rendezvous — `test_bounded_acquire.py:13`; commit-barrier-under-load `test_commit_gate.py:134`; concurrent-deposit `test_deposit.py:51`.
- **Lifecycle entries (T2):** dedup INSIDE commit (`_dedup_recheck` `:615`, `_retarget_to_canonical` `:664`; `dedup.adjudicate(identity, candidates, *, blocking_band, identity_threshold) -> Verdict` `dedup.py:61`); `retraction.cascade(retracted_source_ids: set, *, root=None) -> CascadeResult(flagged, terminated_on_cycle, depth)` `retraction.py:221`; `retraction.reverse_merge_plan(tombstone_rel, *, root) -> ReverseMergePlan` `:332`; `revert_resolution(act_id, identity, *, queue=None)` `ops/revert_resolution.py:26`; `remediate(*, root=None, dry_run=False, queue=None)` `ops/remediate.py:99`. CommitGate dispatch routes on `payload["reversal_type"]` `:339` then `payload["op"]=="policy-edit"` `:349` else CAS pipeline.
- **Eval gate (G1):** `retrieval_eval.evaluate(retriever="fts", *, goldens=None, k=10) -> EvalReport`; `EvalReport.recall_at(k) -> float`; `merge_map_eval(golden_path, *, root=None, adjudicator=None, blocking_band=0.15, identity_threshold=0.30) -> MergeMapResult(precision, recall, regressions)`; `embedding_eval.evaluate_all(encoder=None) -> dict[ns, NamespaceGateReport(passed)]`; `RECALL_FLOOR=0.90` (`commit_gate.py:1129`).

---

## Task ordering & dependency

```
D0 (committer) ──┬─> T2 (integration) ──┐
                 ├─> T3 (soak)          │
D1 (cluster) ────┘                      ├─> G1 (gate script)
M1 (markers) ───────> T4 (surface E2E)  │
                      T6 (property)  ────┘
```

D0 is the keystone — T2/T3/T4/T6 all drive it. Build D0 → D1 → M1 → T2 → T3 → T4 → T6 → G1.

---

### Task D0: Production committer (`author_deposit` + drain loop + `wiki commit-worker`)

**KEYSTONE. Highest risk — destructive/concurrency/privileged. Opus reviewer + security review mandatory.**

**Files:**
- Create: `src/gateway/ops/committer.py` (`author_deposit`, `drain_once`, `run_worker`)
- Modify: `src/gateway/cli.py` (register `commit-worker` per `remediate` pattern)
- Create: `bin/` or scheduler entry mirroring `wiki watch` daemon (confirm launchd vs on-demand with user — default on-demand `wiki commit-worker --once` / `--loop`)
- Test: `tests/gateway/test_committer.py`

**Interfaces:**
- Consumes: `IntentQueue.claim`, `CommitGate.commit`, `deposit` payload schema, `fm.serialize`, slug logic (all verified above).
- Produces:
  - `author_deposit(intent: dict | IntentRecord) -> AuthoredIntent` — renders deposit payload `{page_type, title, body, aliases, domains, synthesizes}` into `AuthoredIntent.writes = {canonical_rel: "<frontmatter>\n\n<body>"}`. Mirror `_authored_entity` in `test_dedup_commit.py`.
  - `drain_once(queue, gate, *, lease_ttl=120.0) -> DrainResult | None` — claim one → author → commit → return disposition; `None` if nothing to claim.
  - `run_worker(*, once=False, poll_interval=2.0)` — loop: `drain_once` until empty (once) or until signalled (loop); each iteration independent; a poison intent dead-letters and the loop CONTINUES.

- [ ] **Step 1 (Verify-Before-Act): Read the real mirror sources.** Read `tests/gateway/test_dedup_commit.py` `_authored_entity` fixture, `fm.serialize` signature, the slug helper it uses, and `AuthoredIntent` dataclass in `commit_gate.py`. Confirm the exact `writes` rel-path convention (`wiki/<page_type-dir>/<slug>.md`) and frontmatter keys per `page_type`. Record the real signatures in your implementer report BEFORE writing code.

- [ ] **Step 2: Write the failing end-to-end test (real loop, real gate, real queue).**

```python
def test_deposited_intent_is_autonomously_committed(repo, queue, gate):
    # realistic payload — full body, aliases, inbound-style wikilink, preamble
    intent_id = deposit(
        page_type="entity", title="Tirzepatide",
        body="Tirzepatide is a dual GIP/GLP-1 agonist. [[concepts/incretin]]\n\n"
             "## Mechanism\nActs on ... [[sources/pubmed-123]]\n",
        aliases=["Mounjaro", "Zepbound"], domains=["glp1"], queue=queue,
    )
    res = drain_once(queue, gate)
    assert res.disposition == "committed"
    # drive the REAL on-disk + git outcome
    page = repo / "wiki" / "entities" / "tirzepatide.md"
    assert page.exists()
    text = page.read_text()
    assert "Mounjaro" in text and "Zepbound" in text          # aliases rendered
    assert "[[sources/pubmed-123]]" in text                    # body preserved verbatim
    assert intent_id not in _queue_ids(queue, "submitted")     # left submitted/
    assert _git_committed(repo, "wiki/entities/tirzepatide.md")
```

Run: `.venv/bin/python -m pytest tests/gateway/test_committer.py::test_deposited_intent_is_autonomously_committed -v` — Expected: FAIL (`author_deposit`/`drain_once` not defined).

- [ ] **Step 3: Implement `author_deposit`** — render frontmatter via `fm.serialize` (keys per `page_type`, mirror `_authored_entity`), slug from title, `writes={rel: f"{frontmatter}\n\n{body}"}`. Body passed through verbatim (agent-supplied). Return `AuthoredIntent`.

- [ ] **Step 4: Implement `drain_once`** — `claim = queue.claim(lease_ttl=lease_ttl)`; if `None` return `None`; `authored = author_deposit(claim.payload)`; `result = gate.commit(authored, claim.fencing_token)`; map `result` → `DrainResult(disposition, intent_id, detail)`. Do NOT catch the commit's own disposition handling — committed/merged/dead_lettered/retry-later come back IN `OperationResult`.

- [ ] **Step 5: Run the test — Expected PASS.**

- [ ] **Step 6: Adversarial — crash mid-author, lease reclaim.**

```python
def test_crash_midauthor_lease_expiry_reclaims(repo, queue, gate):
    deposit(page_type="entity", title="X", body="b [[sources/s1]]", queue=queue)
    claim = queue.claim(lease_ttl=0.01)            # claim then "crash" (drop claim)
    time.sleep(0.05)
    res = drain_once(queue, gate)                  # fresh worker reclaims expired lease
    assert res.disposition == "committed"
```
Negative control: with `lease_ttl=120`, the second `drain_once` returns `None` (still leased) — proves reclaim depends on expiry, not on re-claiming live leases.

- [ ] **Step 7: Adversarial — poison/invalid intent dead-letters, loop continues.**

```python
def test_poison_intent_dead_letters_loop_continues(repo, queue, gate):
    bad = deposit(page_type="entity", title="", body="", queue=queue)   # invalid: empty title
    good = deposit(page_type="entity", title="Good", body="b [[sources/s1]]", queue=queue)
    run_worker(once=True, queue=queue, gate=gate)   # drains BOTH
    assert _terminal_state(queue, bad) == "dead-lettered"
    assert (repo / "wiki" / "entities" / "good.md").exists()   # loop did not abort on poison
```

- [ ] **Step 8: Adversarial — write-skew, two same-entity deposits both survive.**

```python
def test_write_skew_two_same_entity_deposits_both_survive(repo, queue, gate):
    deposit(page_type="entity", title="Ozempic",
            body="Claim A. [[sources/a]]", aliases=["Ozempic"], queue=queue)
    deposit(page_type="entity", title="Ozempic",
            body="Claim B. [[sources/b]]", aliases=["Ozempic"], queue=queue)
    run_worker(once=True, queue=queue, gate=gate)
    text = (repo / "wiki" / "entities" / "ozempic.md").read_text()
    assert "Claim A." in text and "Claim B." in text   # union, not last-writer-wins
```
(This exercises the real `_dedup_recheck` + `_claim_union` merge path inside `commit()`.)

- [ ] **Step 9: Implement `run_worker`** — loop calling `drain_once`; per-iteration try/except so one poison intent can't kill the loop (it dead-letters via the gate, not via the loop catching exceptions — the loop's except is a backstop that logs + continues). `once=True` drains until `drain_once` returns `None`.

- [ ] **Step 10: Register `wiki commit-worker` CLI** — mirror `remediate`: add to `SUBCOMMANDS`, `IMPLEMENTED`, `build_parser` (`--once` / `--loop` / `--poll-interval`), `main()` dispatch, `_run_commit_worker` handler. Build-tier (privileged/destructive) — NOT in read allowlist.

- [ ] **Step 11: Run full file + commit.** `.venv/bin/python -m pytest tests/gateway/test_committer.py -v` — all PASS. Commit explicit paths only.

**Reviewer dispatch (opus):** spec-compliance + code-quality + the inert-in-production hunt list. Specifically trace: does `drain_once` actually commit on real data (hunt #1 apply-branch)? Does the poison test's bad intent ACTUALLY reach the gate's dead-letter (hunt #4 producer-consumer)? Is the write-skew union real or did the test stub the body (B1 realistic-payload)? Run the crash-reclaim negative control RED on a `lease_ttl=120` variant. **Security review (background):** the committer is a new privileged surface that authors+commits arbitrary deposit bodies — check for path traversal in slug/rel-path, body injection into frontmatter, and unbounded loop resource use.

---

### Task D1: Demand-cluster driver (`wiki demand-cluster`)

**Files:**
- Create: `src/gateway/ops/demand_cluster.py` (thin op calling `DemandLedger.cluster()`)
- Modify: `src/gateway/cli.py` (register per `remediate` pattern)
- Test: `tests/gateway/test_demand_cluster.py`

**Interfaces:**
- Consumes: `DemandLedger.cluster() -> list[GapCluster]`, `record_gap`, `submit()`.
- Produces: `demand_cluster(*, root=None, trigger=False) -> OperationResult` — returns clusters; if `trigger=True`, submits a `page_type=synthesis`, `demand_trigger=True` intent for each `triggered` cluster.

- [ ] **Step 1: Failing test — clustering recurring gaps surfaces a cluster.**

```python
def test_demand_cluster_surfaces_recurring_gap(repo):
    ledger = DemandLedger(root=repo)
    for _ in range(4):
        ledger.record_gap("what is the half-life of semaglutide", caller="agent-1")
    result = demand_cluster(root=repo)
    assert any(c.triggered for c in result.clusters)
```
Run: `.venv/bin/python -m pytest tests/gateway/test_demand_cluster.py -v` — Expected FAIL.

- [ ] **Step 2: Implement** `demand_cluster` calling `DemandLedger(root).cluster()`, returning `_emit_result`-compatible `OperationResult`.

- [ ] **Step 3: Test passes; add `--trigger` path test** — asserts a `demand_trigger=True` synthesis intent lands in `submitted/` for a triggered cluster, and (negative control) NO intent submitted when `trigger=False`.

- [ ] **Step 4: Register `wiki demand-cluster` CLI** (build-tier; mirror `remediate`). Closes backlog I1.

- [ ] **Step 5: Run file + commit.**

**Reviewer dispatch (sonnet — additive):** confirm `cluster()` is called on the real ledger (not re-implemented), `--trigger` actually submits (hunt #1), and the no-trigger negative control proves the submit is conditional.

---

### Task M1: pytest markers + fast/full split

**Files:**
- Modify: `pyproject.toml` (`[tool.pytest.ini_options]` `:55-57`)
- Create: `docs/TESTING.md` (the marker contract + invocation recipes) — or append to existing testing docs if present
- Test: marker registration verified by `pytest --markers` + a smoke `-m` selection

**Interfaces:**
- Produces: markers `unit`, `integration`, `e2e`, `slow`; convention: unmarked == unit (fast inner loop); `-m "not slow and not e2e"` == fast; full == no filter.

- [ ] **Step 1: Add `markers =` to `[tool.pytest.ini_options]`** with the four markers + descriptions. Add `--strict-markers` to `addopts` so an unregistered marker is an error (prevents silent typo'd markers — a gate-tests-what-ships guard).

- [ ] **Step 2: Verify** `.venv/bin/python -m pytest --markers` lists all four; `.venv/bin/python -m pytest -m "not slow" --co -q` collects (no errors).

- [ ] **Step 3: Mark the new-tier tests** as they're written (T2 `integration`, T3 `slow`+`integration`, T4 `e2e`, T6 `unit`/`integration`). (This step is completed incrementally by T2–T6; M1 only establishes the registry + docs.)

- [ ] **Step 4: Write `docs/TESTING.md`** — the fast/full recipes, what each tier covers, the eval-floor reminder. Commit.

**Reviewer dispatch (sonnet):** `--strict-markers` is set (else markers are decorative — hunt #2); the fast split actually excludes the slow tier (run both, confirm count differs).

---

### Task T2: Integration flow tests (drive the REAL committer)

**Files:**
- Create: `tests/integration/test_lifecycle_flow.py`, `test_demand_flow.py`, `test_governance_flow.py`
- Test: themselves (marked `integration`)

**Interfaces:** Consumes D0 (`drain_once`/`run_worker`), D1 (`demand_cluster`), and the real lifecycle entries (verified above). No new production code.

- [ ] **Step 1: Lifecycle chain test (realistic payloads).** `deposit → run_worker commits → second deposit same entity → dedup-merge inside commit → retract source → retraction.cascade flags dependents → reverse_merge_plan restores`. Assert each on-disk/git transition. Use full multi-section bodies with aliases + inbound + body wikilinks (B1).

- [ ] **Step 2: Run RED→GREEN; confirm the cascade flags a REAL dependent** (negative control: an unrelated page is NOT flagged).

- [ ] **Step 3: Demand-loop test.** `corpus-miss → record_gap ×N → demand_cluster(trigger=True) → synthesis intent submitted → run_worker commits the canonicalization page`. Assert the committed page exists and cites. Negative control: a single non-recurring gap does NOT trigger.

- [ ] **Step 4: Governance test.** Policy-edit intent via the gate → gate runs eval + merge-map → **dead-letters on a regressing policy**, **commits on a benign one**. Drive BOTH branches (hunt #5: the gate must evaluate the real proposed policy, not a string match). Negative control: the regressing policy must go to dead-letter, not commit.

- [ ] **Step 5: Mark all `integration`; run the integration tier; commit.**

**Reviewer dispatch (opus — drives destructive lifecycle):** for EACH flow, confirm the test drives the REAL op (real `cascade`, real gate commit, real `demand_cluster`) and the assertion depends on what changed (hunt #3 — not a tautology). Confirm the governance dead-letter fires on a genuinely-regressing policy (revert to a string-match gate, watch it wrongly commit → RED).

---

### Task T3: N-agent concurrency soak

**Files:**
- Create: `tests/integration/test_soak.py` (marked `slow` + `integration`)

**Interfaces:** Consumes D0 + `IntentQueue` + `CommitGate`. Mirror the `threading.Event` rendezvous pattern (`test_bounded_acquire.py:13`). Real fcntl; only `paths.locks_dir`/`KNOWLEDGE_ROOT` redirected.

- [ ] **Step 1: Soak test** — N (≥8) concurrent depositor threads + M (≥2) `run_worker` drainers on real locks. Rendezvous all depositors on a `threading.Event` to maximize contention. Assert:
  - every intent reaches a terminal state (committed/merged/dead-lettered) — none stuck in `claimed/`;
  - commits serialized (no torn writes — every committed page parses + validates);
  - stale fencing tokens rejected (a deliberately-held stale claim's commit is refused);
  - backpressure sheds at `MAX_BACKLOG=256` (`deposit` returns `rejected:overloaded` + `retry_after` past the cap);
  - write-skew survivors both present (two same-entity deposits → union body).
- [ ] **Step 2: Negative control** — a single-threaded run of the same N intents produces the same terminal-state set (proves the soak asserts concurrency-safety, not just throughput). Stale-fencing control: a current token commits where the stale one was refused.
- [ ] **Step 3: Run the slow tier; commit.**

**Reviewer dispatch (opus — concurrency):** confirm NO monkeypatch of the lock/gate; the fencing-rejection assertion uses a genuinely stale token (not a fabricated one); backpressure shed is observed at the real `MAX_BACKLOG`, not a lowered test constant that hides the real bound (hunt #6).

---

### Task T4: Surface E2E (MCP protocol + CLI)

**Files:**
- Create: `tests/e2e/test_mcp_surface.py`, `tests/e2e/test_cli_surface.py` (marked `e2e`)

**Interfaces:** Consumes `mcp_server.mcp`, `build_read_tier_server()`, `tier.read_tier_tool_names()`, `cli.main`. Pattern: `create_connected_server_and_client_session` (pass FastMCP directly); CLI git-repo fixture (`test_commit_gate.py:57-69`).

- [ ] **Step 1: MCP read-tier E2E** — boot `build_read_tier_server()`, `await session.list_tools()`, assert the tool set == `tier.read_tier_tool_names()` EXACTLY and that build-only tools (`deposit`, `commit-worker`, `remediate`, `policy-edit`) are ABSENT. Negative control: boot `mcp` (build) and assert those tools ARE present (proves the read server filters, not that the tools don't exist).

- [ ] **Step 2: MCP deposit round-trip** — via the build server, `call_tool("deposit", {...})`, then `run_worker(once=True)`, assert the page commits. (Drives the real protocol path, not the Python fn directly.)

- [ ] **Step 3: CLI E2E** — `cli.main([...])` against a real git repo for `remediate`, `revert-resolution`, `policy-edit`, `demand-cluster`, `commit-worker`; assert on-disk + git state after each. Use the real `repo` fixture.

- [ ] **Step 4: Mark `e2e`; run the e2e tier; commit.**

**Reviewer dispatch (sonnet):** the read-allowlist assertion is exact-set (not subset — a subset assertion would pass even if a build tool leaked); the deposit round-trip actually commits (not just enqueues); CLI asserts git state, not just exit code 0.

---

### Task T6: Inert-in-production property tests (hunt list as executable invariants)

**Files:**
- Create: `tests/integration/test_inert_invariants.py` (marked `integration`)

**Interfaces:** Introspects the real registries — lint checks, detectors, gate handlers, intent types, MCP tool consumers. No new production code (but MAY surface a real gap to file as triggered backlog — that is the point).

- [ ] **Step 1: Every registered lint check fires on a synthesized real signal.** Parametrize over the lint-check registry; for each, construct a real on-disk condition it should flag and assert it flags (hunt #4: producer writes what consumer reads). Negative control per check: a clean repo does NOT flag.

- [ ] **Step 2: Every detector fires on a real signal.** Parametrize over `provenance.alarms()` detectors + retraction/reversal/anomaly detectors; feed each its real producer's output, assert it trips; clean input does not.

- [ ] **Step 3: Every gate dead-letters a real bad input.** For each gate branch (CAS conflict, policy regression, reversal containment), construct the real bad input and assert dead-letter (hunt #5).

- [ ] **Step 4: EVERY consumer's data source has a producer.** The structural check that would've caught the cascade-depth sidecar (hunt #4): enumerate sidecar/state files read by detectors; assert a production code path writes each. **If a consumer has no producer, that is a real defect — file `docs/backlog/<name>.md` with a concrete trigger and FAIL the test (or xfail with the backlog link) — do NOT delete the assertion.**

- [ ] **Step 5: No apply-branch-less intent type** (hunt #1) — enumerate intent `reversal_type`/`op` values the gate dispatches on; assert each has a non-dead-letter apply branch.

- [ ] **Step 6: Run; commit.** Document any surfaced gap in the implementer report.

**Reviewer dispatch (opus — this IS the meta-gate):** confirm each parametrized case drives the REAL producer (not a fabricated fixture — the test fabricating its own consumer-data is exactly the anti-pattern this task exists to kill, per hunt-list general rule). Confirm step 4 actually enumerates the real detector set, not a hardcoded list that could go stale.

---

### Task G1: Pre-merge gate script

**Files:**
- Create: `scripts/pre-merge-gate.sh` (or `.venv/bin/python -m gateway.scripts.gate`)
- Modify: `docs/MULTI-AGENT-BUILD-PLAYBOOK.md` (document the gate as the standing pre-merge step), `CLAUDE.md` (point to it)
- Test: `tests/test_gate_script.py` (asserts the script's eval-floor logic; the script itself is the integration)

**Interfaces:** Consumes `retrieval_eval.evaluate`, `EvalReport.recall_at`, `merge_map_eval`, `embedding_eval.evaluate_all` (verified above).

- [ ] **Step 1: Write the gate script** — runs in sequence, FAILS (non-zero exit) on first failure:
  1. full suite: `.venv/bin/python -m pytest -q`
  2. fast tiers + new tiers green (M1 split)
  3. `retrieval_eval.evaluate("fts").recall_at(10) >= 0.90`
  4. `merge_map_eval(...).regressions == []`
  5. `embedding_eval.evaluate_all()` all `passed`
  6. scoped lints (`orphans`/`schema-drift`/`broken-wikilinks`) at baseline.
- [ ] **Step 2: Test the eval-floor logic** — a unit test that feeds a below-floor recall and asserts the gate's check function returns failure (negative control: at-floor passes). Do NOT re-run the full suite inside the unit test.
- [ ] **Step 3: Capture eval output in ONE pass** (`grep -iE "Retriever:|recall@|MRR"`) — don't `tail` (truncates numbers).
- [ ] **Step 4: Document in playbook + CLAUDE.md; commit.**

**Reviewer dispatch (sonnet):** the recall floor is `>= 0.90` exactly (not a different constant); each eval is actually invoked (not stubbed); the script exits non-zero on first failure (a gate that always exits 0 is inert — hunt #1).

---

## Self-Review (run after drafting — done)

**1. Spec coverage:** D0 (committer a/b/c) ✓; D1 (demand-cluster, backlog I1) ✓; M1 (markers + split) ✓; T2 (lifecycle/demand/governance integration) ✓; T3 (N-agent soak) ✓; T4 (MCP + CLI E2E) ✓; T6 (inert-in-production property) ✓; G1 (pre-merge gate) ✓. All 8 contp tasks mapped.

**2. Placeholder scan:** Step 1 of D0 is a real Verify-Before-Act read (point to real fixtures), not a "TODO". Test bodies are concrete. The launchd-vs-on-demand decision is flagged as a user question (BACKLOG in contp), not a placeholder.

**3. Type consistency:** `author_deposit -> AuthoredIntent`, `drain_once -> DrainResult`, `run_worker`, `demand_cluster -> OperationResult` used consistently across D0/D1/T2/T3/T4/G1. `read_tier_tool_names()` consistent T4↔playbook.

**Open user decision (non-blocking, surfaced in contp BACKLOG):** should `wiki commit-worker` install as a launchd daemon (like `com.knowledge.watcher`) or stay on-demand? Default: on-demand CLI (`--once`/`--loop`); launchd install deferred to a triggered backlog item.
