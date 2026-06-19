# Librarian multi-agent RAG — master build roadmap — 2026-06-18

**Goal.** Sequence the 5-phase build of the Librarian multi-agent runtime-RAG surface
(turn the wiki into a no-HITL grounded read/write substrate for a fleet of agents)
against the real attachment points in `src/gateway/`.

**Provenance of this plan.** It derives mechanically from two persisted inputs and
adds no design:

- the dependency partial order + 5-phase cut in the evergreen design §0
  (`docs/plans/2026-06-18-librarian-multi-agent-rag-design.md`), and
- the per-phase green-gates in the ledger §4
  (`docs/plans/2026-06-18-librarian-multi-agent-rag-checkpoints.md`).

Constraint IDs (C1–C7, I1–I4, A1–A7, G1–G8, F1–F2) trace to the register
(`docs/plans/2026-06-18-librarian-multi-agent-rag-constraints.md`). «guillemet keys»
are ledger §1 rows.

**This roadmap is the loop program.** The ledger §5 live-progress table is the
cursor (which component is `not-started` / `in-progress` / `green`).
`docs/session-state.md` is the resume pointer (next atomic step). This file does not
change as the build runs; the ledger and session-state do.

---

## Loop protocol

The build runs as one **fresh session per phase** — mandatory. Re-entering the same
window across phases accumulates context and pays a cold-cache reload; clearing loses
nothing because everything needed to resume is in the ledger + session-state + this
roadmap's per-phase section.

**Context budget ceiling: 50% — never exceed.** If a phase session approaches 50%,
checkpoint and `/clear`; the phase is resumable from its continuation prompt.

**Execution model.** Each phase is executed via the
`superpowers:subagent-driven-development` skill: a fresh subagent per task, two-stage
review (a reviewer subagent that does not see the implementer's chat). The main window
holds the plan and the gate — never task-level code. This keeps the 50% ceiling
reachable for a multi-task phase.

**Per-phase cycle: PLAN → EXECUTE → GATE.**

1. **PLAN** — run `superpowers:writing-plans` scoped to **this phase only** (the
   bite-sized, bullet-proof plan with complete test/impl code per task). Every phase —
   including Phase 1 — writes its plan at the start of its own session (via that phase's
   contp below), to `docs/plans/2026-06-18-librarian-phaseN-build-plan.md`; later-phase
   code can only be pinned once earlier phases exist.
2. **EXECUTE** — run `superpowers:subagent-driven-development` over that plan. One
   subagent per task; each task carries its own RED→GREEN→commit cycle and a reviewer
   gate before the next task starts.
3. **GATE** — four steps, **all must pass before advancing**. A failing eval or a
   failing code review **HALTS the loop** (do not advance, do not paper over — a
   disagreement between predicted and observed state is a quality incident, §16):

   - **(1) Eval gate.** Run the ledger §4 green-gate for the phase: the named tests
     pass; `.venv/bin/wiki eval-retrieval --compare` reports **≥ recall.floor_at_k**
     (recall@10 ≥ 0.90, merge-map-resolved — never regress the live 0.926 baseline);
     `.venv/bin/wiki lint` is clean for the phase's scopes; and every named
     failure-mode detector test (the §16 taxonomy rows the phase lands) passes.
   - **(2) Code review.** Run the `code-review` skill on the phase diff. Resolve every
     **blocking** finding before advancing (non-blocking findings may be logged to
     session-state for a later pass).
   - **(3) Session review.** Run `/session-review` to capture token / quality / process
     findings for the phase. Fold actionable findings into the next phase's contp.
   - **(4) Handoff.** Run `/contp` to write the next phase's continuation prompt; then
     update ledger §5 (flip the phase's component rows to `green`) + `docs/session-state.md`
     (record completed deliverable + next atomic step); commit (branch-guarded, explicit
     `git add --` of only the touched files, never `-A`/`-u`); `/clear`.

**Stop condition.** Phase 5 gate green — all five ledger §4 checklists checked, every
constraint ID landed, `eval-retrieval --compare` non-regressed.

**Dependency discipline.** A phase begins only when every component it depends on (per
design §0 mermaid graph) is `green` in ledger §5. A plan that contradicts the §0 graph
is a defect — do not reorder phases.

---

## Phase 1 — Commit foundation

**Goal.** Make committing an intent to canonical state a serial, crash-safe,
idempotent, provenanced operation on the gateway write path — the gate every later
invariant rides on.

**Components** (ledger §5 rows, Phase 1):
- Intent queue — durable dir + on-disk lifecycle states (§3, §14)
- Async return type — IntentReceipt / OperationResult ext + status-query (§3)
- CommitGate — serial commit, MVCC CAS, fencing, crash recovery (§5)
- Operational-provenance log + per-producer telemetry stub (§3)

**Intra-phase build order** (respects §0: `Q → CG`, `R → CG`, `CG → PROV`):
1. Intent queue (durable dir + lifecycle states) — no dependency.
2. Async return type (`OperationResult` ext + `_serialize` ext) — no dependency.
3. Status-query op — depends on (1) + (2).
4. CommitGate (serial commit, MVCC CAS, fencing, crash recovery, idempotency) —
   depends on (1), (2).
5. Operational-provenance log + C7 ingest routing — depends on (4).

**Green-gate** (verbatim from ledger §4, Phase 1):
- [ ] Never-regress invariants hold: writes serialized at one gate; reads non-blocking against a committed ref; validator rejects ungrounded claims. *Evidence:* the three invariant tests pass.
- [ ] Torn-write recovery: kill-mid-reattachment leaves `git status` clean post-restart; intent re-runs from `claimed`. *Evidence:* C1 integration test.
- [ ] Idempotency from committed state: redelivering a committed `intent_id` writes nothing. *Evidence:* C2 test scanning committed history.
- [ ] Fencing: a resurrected slow worker cannot overwrite the reclaimer's commit. *Evidence:* C3 test.
- [ ] Every committed corpus change has an operational-provenance ancestor (incl. watcher/poller ingest, C7). *Evidence:* provenance-coverage check.

**Tasks** (titles + files + interfaces + test surface + traceability; bite-sized
steps live in the Phase 1 plan):

- **T1 — Intent queue: durable directory + on-disk lifecycle states.**
  - Create: `src/gateway/intent_queue.py`; Test: `tests/gateway/test_intent_queue.py`.
  - Interfaces: produces `IntentQueue` with `submit(intent) → intent_id`,
    `claim() → (intent, fencing_token, lease)`, `set_state(intent_id, state)`; states
    `submitted/claimed/authored/committed/rejected/dead_lettered` as on-disk facts
    (subdirs or status frontmatter under `.knowledge/intents/`). Consumes: `paths`.
  - Test surface: enqueue → restart (new instance) → state survives (durability); no
    in-memory-only state (contrast `watcher.py:78`).
  - Lands: C3 (fencing token issue at claim), C7 (queue is the deposit path),
    decision 14 (start-boring directory); «commit.lease_ttl».

- **T2 — Async return type: `OperationResult` extension + `_serialize` extension.**
  - Modify: `src/gateway/core.py` (line 84 `OperationResult`),
    `src/gateway/mcp_server.py` (line 101 `_serialize`); Test:
    `tests/gateway/test_async_return_type.py` + assert `tests/gateway/test_mcp_parity.py` green.
  - Interfaces: produces `OperationResult` with optional `intent_id` / `disposition` /
    `retry_after` / `canonical_path` (default `None`); `_serialize` surfaces them.
    Consumes: existing fixed field set (must tolerate absence).
  - Test surface: an existing consumer reading the old fields is unaffected; new fields
    round-trip through `_serialize`; parity test still passes.
  - Lands: A5 (foundational async return shape).

- **T3 — Status-query op: `intent_id` → typed terminal disposition + poll hint.**
  - Create: `src/gateway/ops/intent_status.py`; Modify: register in `mcp_server.py`
    (read-tier-eligible); Test: `tests/gateway/test_intent_status.py`.
  - Interfaces: consumes `intent_id`; produces `OperationResult` carrying the typed
    disposition union (`committed→path`, `merged→canonical_path`, `rejected→rule`,
    `quarantined→queue`, `dead_lettered→reason`) and `retry_after` on non-terminal.
  - Test surface: every terminal state returns its typed disposition; `merged` returns
    a canonical path different from the deposited target; non-terminal returns
    `retry_after`.
  - Lands: A1 (consumer wait-contract), A5 (terminal union); «deposit.max_wait».

- **T4 — CommitGate: serial commit + MVCC compare-and-swap + idempotency + crash recovery.**
  - Create: `src/gateway/commit_gate.py`; Modify: `src/gateway/locking.py` (add
    `librarian-commit` to `LOCK_NAMES`); Test: `tests/gateway/test_commit_gate.py`,
    `tests/gateway/test_commit_gate_recovery.py`.
  - Interfaces: produces `CommitGate.commit(authored_intent, fencing_token) → OperationResult`;
    consumes `core.write_atomic` (per-file, C1), the `discharge_orphans` git-shell pattern
    (`git add -- <explicit>` then `git commit`, never `-A`), `intent_queue` (T1),
    `OperationResult` (T2). Holds the new `librarian-commit` mutex; CAS = content-hash /
    blob-OID at authored snapshot vs HEAD (three cases: no-overlap→commit,
    mergeable→rebase, contradictory→dead-letter); idempotency keyed off committed state
    via commit-message `Intent-Id:` trailer + `applied_intents` record; recovery =
    `git reset --hard HEAD` + `git clean -fd` then re-claim.
  - Test surface: writes serialize at one gate (never-regress); CAS three cases;
    redeliver committed `intent_id` → no second write (scan committed history, not the
    status file); resurrected slow worker (stale fencing token) rejected; kill
    mid-reattachment → `git status` clean post-restart, intent re-runs from `claimed`.
  - Lands: C1, C2, C3, C4 (bounded rebase → dead-letter), decision 1 (single
    serialization point), §4 migration delta (commit mutex replaces global `wiki-author`
    barrier for the commit step); «commit.max_rebase_attempts», «commit.lease_ttl».

- **T5 — Operational-provenance log + C7 ingest routing + per-producer telemetry stub.**
  - Create: `src/gateway/provenance.py`; Modify: `src/gateway/watcher.py` and a
    pollers entry to emit a provenance node on ingest (or route through the deposit
    path); Test: `tests/gateway/test_provenance.py`, `tests/gateway/test_provenance_coverage.py`.
  - Interfaces: produces `ProvenanceLog.record(intent_id, decision_basis) → node_id`
    (decision basis = policy/threshold version, dedup score + candidates, the
    merge/rebase branch); consumes CommitGate commit events (T4). Adds-alongside
    `log.md` — does not replace it.
  - Test surface: every committed corpus change resolves to exactly one provenance node;
    watcher/poller ingest also produces a node (C7 coverage check, no corpus state
    without an ancestor); a canonicalization replays from the node without an LLM call.
  - Lands: C7, decision 3 (operational-provenance graph + decision-basis recording),
    A7 (per-producer telemetry — counters stubbed here, alarms in Phase 4).

**Continuation prompt (contp) — Phase 1:**

```
Fresh session. Branch: docs/librarian-rag-design (verify; if not, STOP).
You are executing PHASE 1 — Commit foundation of the Librarian build.

Read ONLY (not the whole design):
  - docs/session-state.md (resume pointer)
  - docs/plans/2026-06-18-librarian-multi-agent-rag-checkpoints.md §4 Phase 1 + §5 + §1
  - docs/plans/2026-06-18-librarian-multi-agent-rag-build-plan.md  → "Phase 1" section

Verify each ledger §5 Phase-1 component status against the working tree before acting.
Context ceiling 50% — checkpoint and /clear if approached.

Run PLAN→EXECUTE→GATE for Phase 1:
  PLAN  = write docs/plans/2026-06-18-librarian-phase1-build-plan.md via superpowers:writing-plans
          (scoped to Phase 1 only; bite-sized, complete code per task, no placeholders).
  EXECUTE = superpowers:subagent-driven-development over that plan (one subagent/task,
            two-stage review, main window holds no task code).
  GATE  = (1) ledger §4 Phase-1 green-gate tests + `.venv/bin/wiki eval-retrieval --compare`
              (≥ recall@10 0.90) + `.venv/bin/wiki lint` + C1/C2/C3/C7 detector tests;
          (2) code-review skill on the phase diff, resolve blocking;
          (3) /session-review; (4) /contp for Phase 2, update ledger §5 + session-state,
              branch-guarded commit (git add -- specific files; never -A/-u; leave log.md),
              /clear.
A failing eval or code review HALTS — do not advance.
Use .venv/bin/python and .venv/bin/wiki. All writes via the gateway.
```

---

## Phase 2 — Identity substrate

**Goal.** Stand up the embedding index (three namespaces) with incremental
upsert-on-commit and shadow-swap rebuild, so commit-time dedup, demand clustering, and
gap pre-flight have the identity geometry they depend on.

**Components** (ledger §5): Embedding index — three namespaces, upsert-on-commit,
shadow-swap rebuild (§13).

**Intra-phase build order** (§0: `EMB` depends only on the markdown; freshness depends
on the CommitGate from Phase 1):
1. Embedding store + three namespaces (section / entity / question) — adds alongside
   `search_index.py`.
2. Per-namespace golden sets + adequacy gate + named fallbacks (I2).
3. Incremental upsert-on-commit hook (the committer upserts) + shadow-swap rebuild (A6).
4. Threshold calibration against the golden sets; bind «embed.model_version».

**Green-gate** (verbatim from ledger §4, Phase 2):
- [ ] Each embedding namespace's adequacy gate passes against its own golden set, or its named fallback is active and falsifiable (I2). *Evidence:* per-namespace gate report.
- [ ] Rebuild-from-canonical produces a complete index via shadow-swap; no half-state visible to a concurrent `retrieve`; wall-time recorded (A6, F2). *Evidence:* rebuild + concurrent-read test; ledger §3 rebuild-time row populated.
- [ ] Commit-time freshness: a deposit dedups against pages committed earlier in the same serialization window. *Evidence:* freshness test.

**Tasks:**

- **T1 — Embedding store + three namespaces.**
  - Create: `src/gateway/embedding_index.py`; Test: `tests/gateway/test_embedding_index.py`.
  - Interfaces: produces `EmbeddingIndex` with per-namespace `upsert(page)` /
    `nn(text, namespace, k)`; namespaces `section` (retrieval), `entity` (dedup),
    `question` (demand). Gitignored, derived, never canonical.
  - Test surface: each namespace embeds + NN-searches; index is rebuildable from
    markdown; deleting the store + reading self-recovers.
  - Lands: decision 13 (one model, three spaces); «embed.model_version».

- **T2 — Per-namespace adequacy gate + golden sets + fallbacks.**
  - Create: `src/gateway/evaluate/embedding_eval.py`, golden fixtures under
    `tests/gateway/fixtures/`; Test: `tests/gateway/test_embedding_adequacy.py`.
  - Interfaces: consumes each namespace's golden set; produces a per-namespace pass/fail
    + active-fallback flag (dedup → alias/lexical blocking; demand → lexical-canonicalized
    gap-signatures).
  - Test surface: each operating point's gate is independently falsifiable; a forced
    encoder failure activates the named fallback.
  - Lands: I2; «embed.retrieval_relevance_threshold», «embed.dedup_identity_threshold»,
    «embed.demand_gap_threshold».

- **T3 — Incremental upsert-on-commit + shadow-swap rebuild.**
  - Modify: `src/gateway/commit_gate.py` (upsert on commit), `src/gateway/embedding_index.py`
    (shadow location + atomic swap, quiesce/pin during rebuild); Test:
    `tests/gateway/test_embedding_rebuild.py`, `tests/gateway/test_commit_freshness.py`.
  - Interfaces: consumes CommitGate commit events; produces a current-as-of-HEAD entity
    namespace before the dedup check.
  - Test surface: a deposit dedups against a page committed earlier in the same window
    (freshness); a `retrieve` during rebuild returns complete results (no half-state);
    rebuild-from-canonical is byte/row-equivalent; rebuild wall-time recorded to ledger §3.
  - Lands: A6, F2 (rebuild-and-diff equivalence detector); ledger §3 rebuild-time rows.

**Continuation prompt (contp) — Phase 2:**

```
Fresh session. Branch: docs/librarian-rag-design (verify; if not, STOP).
PHASE 2 — Identity substrate.

Read ONLY: docs/session-state.md; ledger §4 Phase 2 + §5 + §1.2/§1.7/§3;
  build-plan.md → "Phase 2" section. Do NOT read the whole design.
Confirm Phase 1 components are `green` in ledger §5 before starting (EMB depends on the
committer for upsert-on-commit). Context ceiling 50%.

PLAN  = superpowers:writing-plans scoped to Phase 2 only (bite-sized, complete code).
EXECUTE = superpowers:subagent-driven-development over that plan.
GATE  = (1) ledger §4 Phase-2 gate: per-namespace adequacy report, rebuild+concurrent-read
            (A6/F2), freshness test, eval-retrieval --compare ≥ 0.90, lint;
        (2) code-review on the diff; (3) /session-review;
        (4) /contp Phase 3, ledger §5 + session-state, branch-guarded commit, /clear.
Calibrate the three operating points against their golden sets and bind «embed.model_version».
A failing eval/review HALTS. .venv/bin/python + .venv/bin/wiki; writes via gateway.
```

---

## Phase 3 — Commit-time invariants

**Goal.** Add the typed deposit tool + authorship workers and the four commit-time
invariants (multi-label domain, LLM-free dedup adjudication, claim-level contradiction
auto-resolve, trust/quality tiering) so concurrent same-entity deposits resolve
correctly and the corpus does not silently rot.

**Components** (ledger §5):
- Deposit API — typed intent tool + authorship workers (§3, §4)
- Commit-time invariants — domain, dedup (I1), contradiction, trust (§6)

**Intra-phase build order** (§0: `CG,R,INV → DEP`; `EMB → INV`):
1. Two-stage dedup (Stage 1 blocking-NN on worker; Stage 2 LLM-free adjudicator
   re-validated at commit) — keystone I1.
2. Multi-label domain resolution; trust/quality tiering (`_authority_key` down-weight).
3. Claim-level contradiction detect + auto-resolve-by-policy.
4. Typed deposit tool + authorship workers (consumes 1–3 + Phase-1 CommitGate).

**Green-gate** (verbatim from ledger §4, Phase 3):
- [ ] Two concurrent same-entity intents both survive (write-skew, C5/F1). *Evidence:* write-skew test, zero broken wikilinks.
- [ ] Phantom collision attaches citations to the canonical page, no duplicate minted. *Evidence:* colliding-intent integration test.
- [ ] Commit-phase dedup is LLM-free and replayable: same logged inputs → same verdict (I1). *Evidence:* replay test.
- [ ] Multi-label domain resolution commits all resolved domains; empty-set quarantines. *Evidence:* domain test.
- [ ] Any `_authority_key` change passes `eval-retrieval --compare` (≥ recall.floor_at_k). *Evidence:* eval-gate run.

**Tasks:**

- **T1 — Two-stage dedup adjudicator (KEYSTONE I1).**
  - Create: `src/gateway/dedup.py`; Modify: `src/gateway/commit_gate.py` (serial
    re-check), `src/gateway/validator.py` (alongside `validate_slug_uniqueness:663`);
    Test: `tests/gateway/test_dedup_adjudicator.py`, `tests/gateway/test_dedup_replay.py`.
  - Interfaces: Stage 1 produces merge candidates (entity-namespace NN +
    alias/slug exact); Stage 2 deterministic precedence over (entity_kind, alias/
    canonical_name match, domain overlap, NN distance band) → {merge, link, distinct}.
    LLM recommendation runs on worker only; committer re-validates against HEAD.
  - Test surface: same logged inputs → same verdict (replay); cross-kind never merged;
    write-skew (two same-entity intents survive); phantom collision attaches citations,
    no duplicate; zero broken wikilinks per `wiki lint --scope dedup`.
  - Lands: I1, C5, F1; «dedup.blocking_nn_threshold», «embed.dedup_identity_threshold».

- **T2 — Multi-label domain resolution + trust/quality tiering.**
  - Modify: `src/gateway/commit_gate.py`, `src/gateway/search_index.py`
    (`_authority_key:422` trust down-weight + eligibility floor); Test:
    `tests/gateway/test_domain_resolution.py`, `tests/gateway/test_trust_tiering.py`.
  - Interfaces: produces resolved `domains:` set (one-or-more; empty→quarantine);
    server-derived trust tier (source-type default + filter score) as a down-weight,
    self-report advisory only; retrieval-eligibility floor (no exclusion).
  - Test surface: multi-domain deposit commits all domains; no-domain → quarantine not
    untagged; self-reported trust never sets precedence tier (G5); low-trust page stays
    retrievable (floor); `_authority_key` change passes `eval-retrieval --compare`.
  - Lands: domain (decision 6), G5; «trust.weight_coefficient»,
    «trust.retrieval_eligibility_floor», recall.floor_at_k.

- **T3 — Claim-level contradiction detect + auto-resolve-by-policy.**
  - Modify: `src/gateway/ops/contradiction*.py` / `contradictions_log.py`,
    `src/gateway/commit_gate.py`; Test: `tests/gateway/test_contradiction_resolve.py`.
  - Interfaces: produces a CiTO `disputes`/`confirms` edge + an auditable
    auto-resolution provenance act (inputs, rule, policy version), resolving by
    trust-tier then recency.
  - Test surface: claim-level contradiction materializes a `disputes` edge + resolution
    act naming rule + policy version; down-weighted loser stays retrievable.
  - Lands: contradiction (decision 6); «contradiction.precedence».

- **T4 — Typed deposit tool + authorship workers.**
  - Create: `src/gateway/ops/deposit.py`; Modify: `mcp_server.py` (register
    build-tier), authorship reuse of `plan.apply_plan` / `ops/ingest.py` on a worker;
    Test: `tests/gateway/test_deposit.py`.
  - Interfaces: consumes typed Intent (source/entity/synthesis shapes); produces an
    acceptance receipt (T2 of Phase 1's async type) — `intent_id`, `disposition: queued`,
    `retry_after`; enqueues durably before ack; authoring runs concurrently (no global
    `wiki-author` lock), only commit serial.
  - Test surface: two source intents for different domains author concurrently
    (overlapping spans in provenance); a synthesis intent's committed page cites only
    submitted sources (canonicalization, not re-synthesis).
  - Lands: decision 3 (deposit API), decision 4 (thin authorship); §4 migration delta.

**Continuation prompt (contp) — Phase 3:**

```
Fresh session. Branch: docs/librarian-rag-design (verify; if not, STOP).
PHASE 3 — Commit-time invariants.

Read ONLY: docs/session-state.md; ledger §4 Phase 3 + §5 + §1.2/§1.4/§1.7;
  build-plan.md → "Phase 3" section. Do NOT read the whole design.
Confirm Phases 1+2 components `green` (DEP depends on CommitGate; INV depends on EMB).
Context ceiling 50%.

PLAN  = writing-plans scoped to Phase 3 only. Build order: dedup keystone → domain+trust
        → contradiction → deposit tool.
EXECUTE = subagent-driven-development.
GATE  = (1) write-skew, phantom-collision, dedup-replay (I1), domain, and
            eval-retrieval --compare ≥ 0.90 (authority-change gate) + lint;
        (2) code-review; (3) /session-review;
        (4) /contp Phase 4, ledger §5 + session-state, branch-guarded commit, /clear.
Any _authority_key change MUST pass eval-retrieval --compare before merge.
A failing eval/review HALTS. .venv/bin/python + .venv/bin/wiki; writes via gateway.
```

---

## Phase 4 — Tiered agent surface

**Goal.** Split the MCP surface into a read tier and a build/deposit tier (two
entrypoints), give the deposit consumer its wait/backpressure contract, and wire
per-producer telemetry alarms.

**Components** (ledger §5):
- Read/build tier split — two MCP entrypoints + op-to-tier table (§7)
- Deposit consumer contract — wait/backpressure (§3, §12)

**Intra-phase build order** (§0: `CG,DEP → TIER`; consumer contract uses the Phase-1
status-query):
1. Op-to-tier classification table (A2) + the parity-style test.
2. Two MCP entrypoints (read-tier server + full server).
3. Deposit consumer contract (wait hint, backpressure signal, bounded lock acquire).
4. Per-producer telemetry alarms (A7).

**Green-gate** (verbatim from ledger §4, Phase 4):
- [ ] Read-tier server registers exactly the read-classified op set (A2). *Evidence:* parity-style test.
- [ ] An agent author can code the deposit wait-loop from the spec; status-query returns the typed disposition union with `retry_after` (A1). *Evidence:* consumer-contract test / worked example.
- [ ] Lock acquisition is bounded, never indefinite (A3). *Evidence:* bounded-acquire test (migration off `flock` no-timeout).
- [ ] Per-producer telemetry alarms fire on rejection-spike / dedup-merge-spike / deposit-silence (A7). *Evidence:* detector tests.

**Tasks:**

- **T1 — Op-to-tier classification + two MCP entrypoints.**
  - Create: `src/gateway/tier.py` (classification rule + table), a read-tier server
    entrypoint; Modify: `mcp_server.py`; Test: extend `tests/gateway/test_mcp_parity.py`
    with `tests/gateway/test_tier_parity.py`.
  - Interfaces: produces a read/build label per registered `wiki_*` tool by the rule
    "side-effect-free AND token-free → read, else build" (`filter`, `answer` without
    `--file` → build); a read-tier server whose registered set equals exactly the
    read-classified set. `CLI_ONLY` is not a tier.
  - Test surface: read-tier set == read-classified set (parity); a read-tier mount
    calling a build tool gets tool-not-found, not a silent no-op; no tool unclassified.
  - Lands: A2, decision 7.

- **T2 — Deposit consumer contract: bounded lock acquire + backpressure signal.**
  - Modify: `src/gateway/locking.py` (`file_lock` bounded acquisition, off the
    `flock(LOCK_EX)` no-timeout at `locking.py:75`), `src/gateway/ops/deposit.py`
    (load signal); Test: `tests/gateway/test_bounded_acquire.py`,
    `tests/gateway/test_backpressure.py`.
  - Interfaces: produces `queued` vs `rejected:overloaded` + `retry_after`; bounded
    lock acquisition (never indefinite block).
  - Test surface: lock acquisition is bounded (times out / returns, never hangs);
    deposit under load returns `rejected:overloaded` + `retry_after`; an agent can code
    the wait loop from the contract alone.
  - Lands: A1, A3; «deposit.max_wait».

- **T3 — Per-producer telemetry alarms.**
  - Modify: `src/gateway/provenance.py` (counters from Phase 1) + an alarm surface;
    Test: `tests/gateway/test_producer_telemetry.py`.
  - Interfaces: consumes per-producer accept/reject/merge counts + time-in-queue;
    produces alarms on rejection-spike, dedup-merge-to-existing spike, deposit-silence.
  - Test surface: each of the three alarms fires on its synthetic signal.
  - Lands: A7 (named §16 detector).

**Continuation prompt (contp) — Phase 4:**

```
Fresh session. Branch: docs/librarian-rag-design (verify; if not, STOP).
PHASE 4 — Tiered agent surface.

Read ONLY: docs/session-state.md; ledger §4 Phase 4 + §5 + §1.1/§3;
  build-plan.md → "Phase 4" section. Do NOT read the whole design.
Confirm Phases 1+3 components `green` (TIER depends on CG + DEP). Context ceiling 50%.

PLAN  = writing-plans scoped to Phase 4 only.
EXECUTE = subagent-driven-development.
GATE  = (1) tier parity test (read set == read-classified set), consumer-contract test,
            bounded-acquire test (off flock no-timeout), A7 detector tests,
            eval-retrieval --compare ≥ 0.90, lint;
        (2) code-review; (3) /session-review;
        (4) /contp Phase 5, ledger §5 + session-state, branch-guarded commit, /clear.
A failing eval/review HALTS. .venv/bin/python + .venv/bin/wiki; writes via gateway.
```

---

## Phase 5 — Lifecycle & demand governance

**Goal.** Close the loop: un-canonicalization (retraction cascade + resolution
reversal), corpus-rot remediation, the DemandLedger + canonicalization trigger, the
gap-routing ladder + keep-worthiness, and the planner/executor pre-flight.

**Components** (ledger §5):
- Corpus-rot governance — remediation + fragmentation lint (§8)
- Lifecycle & retraction cascade — Option A (§9)
- Gap-routing & keep-worthiness (§10)
- DemandLedger — clustering + trigger (§11)
- Planner/executor pre-flight (§12)

**Intra-phase build order** (§0: `INV,PROV,CG → ROT/LIFE`; `TIER,DEP → GAP`;
`GAP → DEM`; `DEM,EMB → PEX`):
1. Retraction cascade + `synthesizes:` closure + resolution-act re-open + `revert-resolution` (Option A).
2. Corpus-rot remediation sweep (de-path-as-intent) + fragmentation lint + lost-update claim-conservation pass.
3. Gap-routing ladder + keep-worthiness gates + corpus-miss telemetry.
4. DemandLedger (clustering + trigger) + planner/executor pre-flight.

**Green-gate** (verbatim from ledger §4, Phase 5):
- [ ] Retraction flags/quarantines transitive `synthesizes:` dependents to a fixpoint, terminating on cycles (G4). *Evidence:* source→A→B chain test.
- [ ] Retracting a winning source re-opens its resolution acts (G3); `revert-resolution` is provenanced + reversible (G1); reversed merge restores from the reattachment set (G8). *Evidence:* G3/G1/G8 tests.
- [ ] Lost-update claim-conservation accounts for every committed intent's payload claims (F1). *Evidence:* reconciliation pass.
- [ ] Demand clusters meet the purity gate; cold-start and re-embedding-survival hold (I4). *Evidence:* purity + I4 tests.
- [ ] Remediation de-paths nothing reachable from the provenance graph (G6); de-path is a provenanced, reversible intent. *Evidence:* citation-target survival test.

**Tasks:**

- **T1 — Retraction cascade + resolution reversal (Option A).**
  - Create: `src/gateway/ops/revert_resolution.py`; Modify: `src/gateway/ops/lint.py`
    (extend `stale-claims`/`retracted-citations`), the retraction propagation path,
    `validator.py` (`validate_synthesizes_integrity:594` walk); Test:
    `tests/gateway/test_retraction_cascade.py`, `tests/gateway/test_revert_resolution.py`.
  - Interfaces: consumes `retracted`/`superseded_by` frontmatter + the
    `[[sources/<id>]]` + `synthesizes:` graphs; produces a fixpoint cascade (G4), a
    resolution-act re-open (G3), `revert-resolution <act-id>` as a CommitGate intent
    (G1), merge un-do from the recorded reattachment set (G8).
  - Test surface: source→A→B chain flags both (terminates on cycles); winner retraction
    re-opens resolution acts; `revert-resolution` provenanced + reversible; reversed
    merge restores pre-merge inbound links.
  - Lands: G1, G3, G4, G8; «retraction.cascade_trigger», «contradiction.precedence».

- **T2 — Corpus-rot remediation sweep + fragmentation lint + claim-conservation pass.**
  - Create: `src/gateway/ops/remediate.py`; Modify: `src/gateway/ops/lint.py`
    (fragmentation lint, claim-conservation reconciliation); Test:
    `tests/gateway/test_remediation.py`, `tests/gateway/test_claim_conservation.py`.
  - Interfaces: consumes `inbound_counts`/`related_pages` (wikilinks) + raw
    `wiki_pages:` backlinks + the provenance graph; produces de-path-as-intent
    (provenanced, reversible) that never touches a reachable page; a fragmentation lint
    over high-mutual-similarity concept clusters; a claim-conservation pass.
  - Test surface: de-paths a genuinely orphaned uncited page but leaves a
    zero-inbound-wikilink live-citation-target in place (G6); de-path is a provenance
    node + reversible; claim-conservation reports zero unaccounted payload claims (F1).
  - Lands: G6, F1; corpus.orphan_pct_ceiling, corpus.untagged_pct_ceiling.

- **T3 — Gap-routing ladder + keep-worthiness + corpus-miss telemetry.**
  - Modify: `src/gateway/ops/retrieve.py`, `src/gateway/ops/answer.py`,
    `src/gateway/ops/deposit.py` (keep-worthiness fields); Test:
    `tests/gateway/test_gap_routing.py`, `tests/gateway/test_keep_worthiness.py`.
  - Interfaces: produces the corpus-first ladder (`retrieve`→`answer`→web fallback,
    never blocks the librarian) with corpus-miss logging; orient-vs-ground gate
    (durable claim needs an ingested source); keep-worthiness gates (half-life,
    load-bearing self-report + audit, domain-core, recurrence).
  - Test surface: a durable claim with only a non-ingested URL is rejected at deposit;
    a web fall-through logs a corpus-miss; an agent re-querying its own outstanding
    deposit logs none (A4); volatile-flagged deposit not canonicalized.
  - Lands: decision 10, A4.

- **T4 — DemandLedger + planner/executor pre-flight.**
  - Create: `src/gateway/demand_ledger.py`, `src/gateway/ops/preflight.py`; Test:
    `tests/gateway/test_demand_ledger.py`, `tests/gateway/test_preflight.py`.
  - Interfaces: consumes logged corpus-misses + the demand embedding namespace;
    produces online gap clustering (radius + recurrence-mass + cold-start), a
    canonicalization trigger (one build-tier synthesis intent per cluster), retaining
    raw gap-text (I4); the read-tier plan-time gap pre-flight + enrichment-status check.
  - Test surface: a recurring gap triggers exactly one canonicalization intent
    (dedup-by-cluster); first-occurrence logged not triggered (cold-start); model-bump
    re-clusters from text without resetting recurrence (I4); purity (paraphrases →
    one cluster, distinct gaps → two); pre-flight emits enrichment then executor runs
    after commit.
  - Lands: decision 11, decision 12, I4; «demand.proximity_radius»,
    «demand.recurrence_mass», «demand.cold_start_min_recurrences», «embed.demand_gap_threshold».

**Continuation prompt (contp) — Phase 5:**

```
Fresh session. Branch: docs/librarian-rag-design (verify; if not, STOP).
PHASE 5 — Lifecycle & demand governance (final phase).

Read ONLY: docs/session-state.md; ledger §4 Phase 5 + §5 + §1.3/§1.4/§1.5/§2;
  build-plan.md → "Phase 5" section. Do NOT read the whole design.
Confirm Phases 1-4 components `green`. Context ceiling 50%.

PLAN  = writing-plans scoped to Phase 5 only. Build order: cascade/reversal →
        remediation+claim-conservation → gap-routing → demand+pre-flight.
EXECUTE = subagent-driven-development.
GATE  = (1) G4 chain, G3/G1/G8, F1 claim-conservation, demand purity + cold-start + I4,
            G6 citation-target survival, eval-retrieval --compare ≥ 0.90, lint;
        (2) code-review; (3) /session-review;
        (4) ledger §5 all rows green, session-state STOP-condition reached,
            branch-guarded commit. NO Phase 6 — build complete at Phase 5 gate green.
A failing eval/review HALTS. .venv/bin/python + .venv/bin/wiki; writes via gateway.
```

---

## Traceability check — phase → constraint IDs

Cross-cutting constraints (policy keys / verification harness) are landed where they
first attach and verified at each phase's eval gate.

| Phase | Constraint IDs landed |
|---|---|
| 1 — Commit foundation | C1, C2, C3, C4, C6 (causal-dependency dead-letter), C7, A5, A1 (status-query), A7 (telemetry stub) |
| 2 — Identity substrate | I2, A6, F2 |
| 3 — Commit-time invariants | I1, C5, F1 (write-skew survival), G5 |
| 4 — Tiered agent surface | A2, A3, A4 (carry-forward suppression seam), A7 (alarms) |
| 5 — Lifecycle & demand governance | G1, G2, G3, G4, G6, G7, G8, I3, I4, F1 (claim-conservation), A4 |

**Every constraint ID accounted for:** C1·C2·C3·C4·C5·C6·C7 (C6 causal-dependency lands
with the CommitGate, Phase 1 T4 — broken-dependency dead-letter + cycle-reject);
I1·I2·I3·I4 (I3 merge-map non-circularity lands with the verification harness in Phase
5's eval gate against the merge-map golden); A1·A2·A3·A4·A5·A6·A7;
G1·G2·G3·G4·G5·G6·G7·G8 (G2 reversal detectors + G7 policy change-control both land in
Phase 5 alongside the reversal primitive and the privileged-intent path); F1·F2. No
constraint ID is unassigned.

**Cross-cutting components** (ledger §5): *Policy keys + change-control (§14, G7)* —
keys are introduced per phase as their consumers land; the enforced change-control path
(privileged intent through the CommitGate gated by `eval-retrieval --compare`) lands in
Phase 5. *Verification harness — merge-map golden, eval axes, taxonomy detectors (§16)*
— each phase's eval gate adds its detector tests; the merge-map golden (I3) + dedup
precision/recall + demand-cluster purity + grounding faithfulness axes complete in Phase 5.
