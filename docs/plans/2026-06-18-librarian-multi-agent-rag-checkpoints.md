# Librarian multi-agent RAG — checkpoint & threshold ledger — 2026-06-18

Companion to the evergreen design `docs/plans/2026-06-18-librarian-multi-agent-rag-design.md`.

**This file is NOT evergreen.** It holds the mutable, empirically-tuned material — threshold
values, corpus-health and liveness targets, phase-boundary gates, and live build progress —
and is **edited freely during the build, including by the build agent**. That lifecycle
difference (frequently-mutated vs change-only-on-architecture-change) is why the two files are
separate. The design document must carry none of this. It sits beside `docs/session-state.md`
and mirrors the `docs/*backlog-rubric.md` idiom (§-sections, tables, checkboxes).

**Threshold values are policy** (design §14): they live in `.knowledge/policies/<domain>/policy.yaml`
and inherit `policy_versions/` git-versioning. Initial values below are **starting hypotheses**,
not measured optima; the rationale states why the starting point, and the revisit trigger says
what moves it. Embedding operating points are **calibrated in Phase 2 against per-namespace
golden sets** and bound to «embed.model_version» — their numeric starts are placeholders until
calibration.

**Change-control vocabulary** (design §14, G7): *build-time* = tunable during development by the
builder; *guarded runtime* = changeable only through the CommitGate as a privileged, allowlisted
intent gated by `eval-retrieval --compare` + golden-merge re-eval; *operator-monitored* = a
measured signal a human watches, not a knob.

---

## § 1 — Tunable thresholds

Every «guillemet key» in the design appears here as a row (self-check 2). Direction-of-effect is
in the rationale; the design states the role.

### 1.1 Commit & queue (design §3, §5)

| Key | Initial value | Rationale for start | Revisit trigger | Change-control · blast radius |
|---|---|---|---|---|
| «commit.max_rebase_attempts» | 8 | High enough to clear normal same-entity contention via rebase-merge; low enough to bound livelock before dead-lettering `contention` (C4). | Dead-letter `contention` rate rises, or oldest-rebased-intent age grows. | build-time · commit liveness only |
| «commit.lease_ttl» | 120 s, heartbeat-renewable | Longer than typical worker authorship so live work is not reclaimed; short enough to reclaim a crashed worker promptly (C3). | Spurious reclaims (legit authorship > TTL) OR slow crashed-worker recovery. | build-time · worker-reclaim correctness |
| «deposit.max_wait» | 30 s | Bounded total poll before an agent proceeds on carried-forward content (A1); covers a typical commit-queue drain without starving the agent. | Agents starve waiting, OR proceed-too-early causes stale grounding. | build-time (per-agent overridable) · agent-side latency only |
| «deposit.max_backlog» | 256 (`deposit.MAX_BACKLOG`, Phase 4) | Server-side shed ceiling: `deposit()` returns `rejected:overloaded`+`retry_after` when `submitted/` depth ≥ this, so producers back off rather than growing an unbounded queue (A1 backpressure). Design names backpressure but not its mechanism — queue-depth shed is the async-clean, deterministically-testable choice (deposit holds no commit lock; authoring is concurrent). | `rejected:overloaded` rate rises under normal load (raise), OR queue grows unboundedly before shedding (lower). One producer starving others → see backlog `librarian-deposit-per-producer-fairness` (per-producer sub-ceiling). | build-time · deposit admission only |

### 1.2 Dedup & identity (design §6, §13)

| Key | Initial value | Rationale for start | Revisit trigger | Change-control · blast radius |
|---|---|---|---|---|
| «dedup.blocking_nn_threshold» | cosine dist ≤ 0.15 (generous) | Stage-1 blocking is recall-oriented — over-generate candidates; the LLM-free adjudicator (I1) prunes for precision. A tight block would miss true merges no later stage can recover. | Dedup recall misses true merges, OR candidate sets explode. | guarded runtime · dedup recall |
| «embed.dedup_identity_threshold» | cosine dist ≤ 0.30 *(calibrated Phase 2 for `lexical-fallback-v1`; entity gate precision 1.0, merges 0.05–0.19 vs no-merges 0.83–1.08)* | Co-reference identity must be strict — a false merge is silent corruption (§16 taxonomy), worse than a missed merge. | Golden merge/no-merge precision drops, OR the densification canary shifts. | guarded runtime + eval gate · dedup precision |
| «embed.retrieval_relevance_threshold» | cosine ≤ 0.55 *(calibrated Phase 2 for `lexical-fallback-v1`; section gate recall@1 1.0)* | Query→passage asymmetric relevance operating point for section-grained retrieval. | Model-version bump, OR retrieval recall regresses on the golden set. | guarded runtime · retrieval recall |
| «embed.demand_gap_threshold» | cosine ≤ 0.70 (coarse) *(calibrated Phase 2 for `lexical-fallback-v1`; question gate purity 1.0, within-cluster max 0.591 vs cross-cluster min 0.748)* | Topical-gap clustering tolerates breadth — paraphrases of one gap should co-cluster. | Demand-cluster purity drops (§16 axis). | build-time · demand clustering |
| «embed.model_version» | `lexical-fallback-v1` (dim 256) *(set Phase 2; I2 active lexical fallback, pure-numpy hashed token-set + char-3-gram — neural encoder pluggable behind the `Encoder` protocol)* | Binds all three operating points; a change requires re-embedding the entity namespace and re-calibrating before new thresholds take effect (§13). | Encoder upgrade or replacement. | guarded runtime · ALL embedding namespaces (re-embed + recalibrate) |

### 1.3 Demand aggregation (design §11)

| Key | Initial value | Rationale for start | Revisit trigger | Change-control · blast radius |
|---|---|---|---|---|
| «demand.proximity_radius» | = «embed.demand_gap_threshold» membership band (~0.40) | Cluster-membership radius for online gap-signature clustering. | Demand-cluster purity drops; clusters too broad/narrow. | build-time · demand clustering |
| «demand.recurrence_mass» | 5 | A gap must recur 5× before triggering a synthesis intent — balances responsiveness against synthesis spend. | Triggers fire too eagerly (spend), OR real gaps persist untriggered. | build-time · synthesis spend |
| «demand.cold_start_min_recurrences» | 3 | First occurrences are logged, not clustered away (decision 11); 3 before a gap is eligible to accumulate mass. | Tune jointly with «demand.recurrence_mass». | build-time · demand sensitivity |

### 1.4 Trust & contradiction (design §6, §9)

| Key | Initial value | Rationale for start | Revisit trigger | Change-control · blast radius |
|---|---|---|---|---|
| «trust.weight_coefficient» | 0.5 (in `_authority_key` units) | A down-weight tiebreaker that must not dominate — smaller than `_W_TIER`=2.0 / `_W_AUTHORITY`=1.5 in `search_index.py:414`. Trust adjusts, never overrides, lexical+graph signal. | `eval-retrieval --compare` shows ranking drift; rich-get-richer suppression observed. | guarded runtime + **mandatory** eval gate · ALL retrieval ranking |
| «trust.retrieval_eligibility_floor» | every committed, non-quarantined page is retrievable (floor = no exclusion) | The rich-get-richer brake (decision 6): trust is a tiebreaker, never a gate, so a low-trust page never drops out of the candidate set. | Low-trust pages observed suppressed below visibility despite the floor. | guarded runtime · retrieval coverage |
| «contradiction.precedence» | ordered: server-derived trust-tier desc, then recency desc | The owner decision (auto-resolve by policy rule); server-derived trust (G5) then recency. | Auto-resolution mis-resolution rate climbs (G2). | guarded runtime + eval · every auto-resolution |
| «retraction.cascade_trigger» | retracted → quarantine dependents; superseded → flag/downgrade | Which propagation action per source state (design §9); retraction is stronger than supersession. | Quarantine too aggressive (false-positive retractions), OR flagged-but-live claims cause errors. | guarded runtime · dependent claims + synthesis |

### 1.5 Option-B gating signals (design §15; POR `docs/backlog/librarian-cascade-revert-automation.md`)

These are **operator-monitored** measured triggers; crossing any one is the signal to build
Option B (automatic transitive cascade-revert). They are also corpus-health metrics (§2).

| Key | Initial alarm | Rationale for start | Revisit trigger | Change-control · blast radius |
|---|---|---|---|---|
| «reversal.auto_resolution_reversal_rate» | > 5% of auto-resolutions reversed / 30 d | Bad auto-resolutions becoming frequent is the primary Option-B signal. | Re-tune once a baseline rate is observed. | operator-monitored · gates Option B build |
| «reversal.cross_project_override_rate» | > 10% of resolutions override another project's claim / 30 d | Cross-project poisoning is the specific risk of the open shared corpus (§1). | Re-tune on baseline. | operator-monitored · gates Option B build |
| «reversal.observed_cascade_depth» | > 3 levels | Deep manual layer-by-layer cleanup under Option A is the pain Option B removes. | Re-tune on baseline. | operator-monitored · gates Option B build |

### 1.6 Liveness operating points (design §2, §15)

| Key | Initial alarm | Rationale for start | Revisit trigger | Change-control · blast radius |
|---|---|---|---|---|
| «liveness.commit_p50» | > 500 ms | The serial gate is the throughput ceiling by design (decision 1) — p50 tracks healthy commit cost, NOT asserted sub-second. | Sustained breach under normal load. | operator-monitored / build-time · write latency |
| «liveness.commit_p99» | > 2 s | Tail latency; also the §15 trigger for committer-vs-mutex substrate choice. | Sustained breach → evaluate dedicated-committer substrate. | operator-monitored · write latency + substrate decision |

### 1.7 Additional mandated thresholds (prose-referenced in design §8, §16)

Required by the ledger spec; referenced by role in the design (not as `«»` keys).

| Key | Initial value | Rationale | Revisit trigger | Change-control · blast radius |
|---|---|---|---|---|
| recall.floor_at_k | recall@10 ≥ 0.90 (merge-map-resolved) | Non-regression floor below the live baseline (recall@10 0.926); guards ranking changes. | Any `_authority_key`/ranking change. | eval gate (merge precondition) · retrieval |
| corpus.untagged_pct_ceiling | ≤ 2% of sources | Tagging-drift ceiling (§8); multi-label resolution should keep untagged near zero. | Sustained breach → investigate resolver. | build/ops · corpus health |
| corpus.orphan_pct_ceiling | ≤ 5% of sources | Orphaning ceiling (§8); excludes live citation targets (G6). | Sustained breach → discharge/quarantine sweep. | build/ops · corpus health |

---

## § 2 — Corpus-health metrics

Each with a target and the current reading. Current readings are pre-build unless noted;
populate as the build lands. Today's whole-corpus snapshot (`wiki status`, 2026-06-18):
schema-drift = 191; golden recall@5 0.852 / recall@10 0.926 / MRR 0.690 (n=27, fts).

| Metric | Target | Current reading |
|---|---|---|
| Untagged-source % | ≤ corpus.untagged_pct_ceiling | — (pre-build; domain assigned at ingest today) |
| Orphan % | ≤ corpus.orphan_pct_ceiling | high (legacy backlog; e.g. phase-8 rubric noted 527 orphan sources) |
| Dedup-merge rate | stable; alarm on spike (A7) | n/a (no dedup at commit yet) |
| Taxonomic-fragmentation candidate count | trend ↓ | — (fragmentation lint not built) |
| Draft-age distribution | bounded; no >7 d stale tail | historically ~224 stale drafts (legacy) |
| Golden-staleness % (unresolvable + unconfirmed-merge `expect`) | ≈ 0 | 0 today (literal `slug in g.expect`; merge-map not yet built) |
| Demand-ledger hit rate (triggered/total gaps) | meaningful, non-zero once live | n/a (DemandLedger not built) |
| «reversal.auto_resolution_reversal_rate» | < alarm (§1.5) | n/a (no auto-resolution yet) |
| «reversal.cross_project_override_rate» | < alarm (§1.5) | n/a |
| «reversal.observed_cascade_depth» | < alarm (§1.5) | n/a |

---

## § 3 — Liveness / backpressure

Real signals for the async-coupling poll-or-proceed decision (design §12) and the recovery
posture (§16). Each with an alarm threshold.

| Signal | Alarm threshold | Current |
|---|---|---|
| Queue depth (submitted+claimed) | > 50 sustained | n/a |
| Oldest-unprocessed-intent age | > 5 min | n/a |
| Dead-letter count / rate | any sustained rate > 0; total > 10 | n/a |
| Commit-gate p50 | «liveness.commit_p50» (>500 ms) | n/a |
| Commit-gate p99 | «liveness.commit_p99» (>2 s) | n/a |
| Backpressure: `rejected:overloaded` rate | > 1% of deposits | n/a |
| Lock-acquisition wait (bounded, never indefinite — A3) | > «deposit.max_wait» | n/a (today `flock(LOCK_EX)` has NO timeout — `locking.py:75`) |

**Per-component derived-index rebuild-time + last-successful-rebuild timestamp** (design §16 —
every derived component ships a tested, time-bounded rebuild):

| Component | Rebuild-time target | Last successful rebuild |
|---|---|---|
| FTS index (`search_index.refresh(rebuild=True)`) | bounded; record wall-time | — |
| Embedding namespaces (all three, `EmbeddingIndex.rebuild_from_canonical`, shadow-swap) | bounded; record | 2026-06-18 · 7.26 s · 4023 pages / 19255 rows · `lexical-fallback-v1` (section + entity in one canonical walk; question is DemandLedger-fed, Phase 5) |
| Backlink graph | bounded; record | — (not built) |

**Per-failure-mode occurrence counts** (design §16 taxonomy — each a tracked counter with an
alarm). All n/a pre-build:

| Failure mode | Alarm |
|---|---|
| Torn multi-store write | any |
| Lost update on concurrent same-entity merge | any (claim-conservation, F1) |
| Stale-index dedup miss | any (rebuild-and-diff, F2) |
| Dangling wikilink / de-pathed citation target | any (`wiki lint`, G6) |
| Poison / dead-lettered intent | rate > baseline |
| Orphaned citation | > corpus.orphan_pct_ceiling |
| Orphaned-correct-claim after winner retraction (G3) | any |
| Mis-resolved contradiction (G1/G2) | «reversal.auto_resolution_reversal_rate» |
| Index-rebuild divergence (F2) | any |
| Silent/compounding producer failure (A7) | per-producer alarm |

---

## § 4 — Phase-boundary checkpoints

Keyed to the design §0 phase names. Each phase lists what must be green and the observable
evidence before the next phase begins.

### Phase 1 — Commit foundation
- [x] Never-regress invariants hold: writes serialized at one gate; reads non-blocking against a committed ref; validator rejects ungrounded claims. *Evidence:* `test_commit_gate.py::test_writes_serialized_at_one_gate`, `::test_status_query_does_not_block_on_commit_mutex`; validator unchanged (full suite 1994 green).
- [x] Torn-write recovery: kill-mid-reattachment leaves `git status` clean post-restart; intent re-runs from `claimed`. *Evidence:* `test_commit_gate_recovery.py::test_recover_resets_dirty_tree_and_reclaims` (C1).
- [x] Idempotency from committed state: redelivering a committed `intent_id` writes nothing. *Evidence:* `test_commit_gate.py::test_redeliver_committed_intent_is_noop_from_history` (C2; scans `git log --grep`, survives queue-record deletion).
- [x] Fencing: a resurrected slow worker cannot overwrite the reclaimer's commit. *Evidence:* `test_commit_gate.py::test_stale_fencing_token_rejected` (C3).
- [x] Every committed corpus change has an operational-provenance ancestor (incl. watcher/poller ingest, C7). *Evidence:* `test_provenance_coverage.py::test_every_committed_change_has_ancestor` + `::test_watcher_ingest_emits_provenance_node`.

### Phase 2 — Identity substrate
- [x] Each embedding namespace's adequacy gate passes against its own golden set, or its named fallback is active and falsifiable (I2). *Evidence:* `test_embedding_adequacy.py` — all three pass at floor 1.0 (section recall@1, entity precision, question purity) for the active `lexical-fallback-v1`, each falsifiable (flipped-label probe + constant-encoder negative control).
- [x] Rebuild-from-canonical produces a complete index via shadow-swap; no half-state visible to a concurrent `retrieve`; wall-time recorded (A6, F2). *Evidence:* `test_embedding_rebuild.py::test_concurrent_read_during_rebuild_no_half_state` (real reader thread during a real slow-encoder rebuild, `os.replace` not monkeypatched; non-atomic negative control proves the detector); `RebuildStats.wall_seconds` recorded; `test_rebuild_and_diff_detects_divergence` (F2).
- [x] Commit-time freshness: a deposit dedups against pages committed earlier in the same serialization window. *Evidence:* `test_commit_freshness.py::test_commit_upserts_entity_namespace_freshness` (real CommitGate + real EmbeddingIndex; earlier-in-window page visible to the next intent's entity-NN; `embedding_index=None` negative control proves the upsert is the cause, not a lazy rebuild).

### Phase 3 — Commit-time invariants
- [x] Two concurrent same-entity intents both survive (write-skew, C5/F1). *Evidence:* `test_dedup_commit.py::test_write_skew_two_claims_one_entity_both_survive` (real CommitGate + real EmbeddingIndex, no monkeypatch; `_claim_union` three-way add/add); zero broken wikilinks; negative control `::test_genuinely_conflicting_claims_still_dead_letter`.
- [x] Phantom collision attaches citations to the canonical page, no duplicate minted. *Evidence:* `test_dedup_commit.py::test_phantom_collision_second_intent_merges_not_mints` (second same-referent intent merges; exactly one canonical page survives); merge-reattachment preserves aliases/non-Claims body/wikilinks/preamble + writes a `merged_into:` tombstone, heading/body collision → `needs-manual-merge` (no silent drop — review B1/N1).
- [x] Commit-phase dedup is LLM-free and replayable: same logged inputs → same verdict (I1). *Evidence:* pure `dedup.adjudicate` (no model call, no index access); `test_dedup_replay.py::test_same_inputs_same_verdict_replay` (reversed candidate order → identical verdict via total `(round(nn,6), slug)` order). Merge authority = alias/canonical exact-or-normalized + same kind; NN recall-only; cross-kind never merges. Independent dedup golden `test_dedup_golden.py` + geometry-only falsifiability control.
- [x] Multi-label domain resolution commits all resolved domains; empty-set quarantines. *Evidence:* `test_domain_resolution.py` (multi-domain commit; unknown dropped; empty → `quarantined`, writes nothing untagged).
- [x] Any `_authority_key` change passes `eval-retrieval --compare` (≥ recall.floor_at_k). *Evidence:* trust down-weight `_W_TRUST*(trust-0.5)`, `_W_TRUST=0.5` < `_W_TIER`/`_W_AUTHORITY`; `eval-retrieval --compare` fts recall@10 = 0.926 (== baseline, ≥ 0.90 floor); eligibility floor keeps low-trust pages retrievable; `server_trust_tier` takes no self-report arg (G5).

### Phase 4 — Tiered agent surface — GATE PASSED 2026-06-19
- [x] Read-tier server registers exactly the read-classified op set (A2). *Evidence:* `test_tier_parity.py` — `build_read_tier_server()` registered set == `tier.read_tier_tool_names()`; default-deny allowlist (8 read ops + 2 aux); negative control pins `wiki_ingest/query/deposit/filter/edit` absent. Review dropped `agents`/`lint`/`status` (not side-effect-free) → build tier.
- [x] An agent author can code the deposit wait-loop from the spec; status-query returns the typed disposition union with `retry_after` (A1). *Evidence:* `test_backpressure.py` — `deposit()` returns `queued`+`retry_after` below `«deposit.max_backlog»`, `rejected:overloaded`+`retry_after` at/above (enqueues nothing); `intent-status` (read-tier) returns terminal disposition.
- [x] Lock acquisition is bounded, never indefinite (A3). *Evidence:* `test_bounded_acquire.py` — `file_lock(name, *, timeout=…)` bounded via `LOCK_EX|LOCK_NB`+deadline→`LockTimeout` (real holder, real fcntl, no monkeypatch); `timeout=None` byte-identical blocking back-compat for 30+ call sites; `commit_gate` barrier uses 30s bound and returns `disposition="retry-later"` on timeout (no queue-state mutation, intent stays durable).
- [x] Per-producer telemetry alarms fire on rejection-spike / dedup-merge-spike / deposit-silence (A7). *Evidence:* `test_producer_telemetry.py` — `provenance.alarms()` (pure over snapshots) fires each detector on its synthetic signal; negative controls (healthy traffic fires none; below-`min_volume` cannot trip a spike).

*Gate: full suite 2182 passed (2163 baseline + 19); `eval-retrieval --compare` fts recall@10 0.926 (== baseline, no retrieval code touched); per-scope lint at pre-existing baseline (orphans 758 / schema-drift 191 / broken-wikilinks 1 / link-rot 733 — none Phase-4); independent whole-branch review (opus) GO; independent security review (opus) ship-it (F1 doc overstatement fixed; F2 deposit per-producer fairness + F3 file_lock path-traversal → backlog with triggers).*

### Phase 5 — Lifecycle & demand governance — GATE PASSED 2026-06-19
- [x] Retraction flags/quarantines transitive `synthesizes:` dependents to a fixpoint, terminating on cycles (G4). *Evidence:* `test_retraction_cascade.py` source→A→B chain + cycle-termination + unrelated-page negative control.
- [x] Retracting a winning source re-opens its resolution acts (G3); `revert-resolution` is provenanced + reversible (G1); reversed merge restores from the reattachment set (G8). *Evidence:* `test_revert_resolution.py` + `test_reversal_apply.py` — reversals APPLY end-to-end through the real gate (remove `## Contested`/restore claims; reverse-merge restores B-only aliases/sections/claims + deletes tombstone). Review caught + fixed a reverse-merge alias over-restore (Critical) + a latent unrecorded-reattachment gap.
- [x] Lost-update claim-conservation accounts for every committed intent's payload claims (F1). *Evidence:* `test_claim_conservation.py` reconciliation over committed/merged intent records (merge-aware via `merged_into`) + dropped-claim negative control.
- [x] Demand clusters meet the purity gate; cold-start and re-embedding-survival hold (I4). *Evidence:* `test_demand_ledger.py` purity (paraphrase→1, distinct→2) + cold-start (one-off contributes 0 mass; param flips a borderline trigger) + I4 (real different-dimension encoder; clustering survives the bump). Review caught + fixed dead cold-start + a tautological I4 test (Criticals).
- [x] Remediation de-paths nothing reachable from the provenance graph (G6); de-path is a provenanced, reversible intent. *Evidence:* `test_remediation.py` — de-path runs through the real gate (git rm + provenance + restore-applicable); reachability recurses nested `merge_reattachment` paths; negative controls (active merge tombstone, zero-inbound citation target) → `skipped_reachable`. Review caught + fixed an inert de-path op + nested-reachability data loss (Criticals).
- [x] Reversal/anomaly detectors trip on the §1.5 signals, quiet on healthy traffic (G2). *Evidence:* `test_reversal_detectors.py` — three detectors fire on real data (cascade-depth computed live from `retraction.cascade` over retracted-source graph; cross-project from real `domains:` frontmatter; reversal-rate from `reverts_act`) + negative controls. Review caught + fixed an inert cascade-depth sidecar + wrong-signal cross-project (Criticals).
- [x] Policy edits route through a privileged CommitGate intent (server-sourced `GATEWAY_POLICY_PRINCIPAL`, fail-closed; CLI-only, off all MCP surfaces); merge-map-regressing edit dead-lettered without writing (G7). *Evidence:* `test_policy_change_control.py` — gate derives dedup params from the PROPOSED policy + dead-letters on any golden regression; commits the tracked policy through the gate w/ Intent-Id trailer. Security review caught + fixed fail-open gate + path-traversal + spoofable identity (2 HIGH + 1 Critical). Existing-op migration = triggered backlog.
- [x] Merge-map golden re-eval guards dedup precision; geometry-only adjudication shows regressions (I3). *Evidence:* `test_merge_map_golden.py` real `adjudicate` over the curated golden + falsifiability control (geometry-only regresses).

*Gate: full suite 2354+ passed; `eval-retrieval --compare` fts recall@10 0.926 (== baseline, ≥0.90 floor); scoped lints at baseline (orphans 758 / schema-drift 191 / broken-wikilinks 1); 6 independent per-task reviews + whole-branch review (GO/READY) + security review (SHIP IT). The reviewer≠author gate caught a silent-corruption or inert-in-production defect in EVERY task (T1 alias over-restore, T2 inert de-path, T3 bool-as-int, T4 dead cold-start + tautological I4, T5 inert cascade-depth, T6 inert gate + 2 HIGH security) — all fixed TDD.*

---

## § 5 — Live progress

Per-component status, updated by the build agent. Status ∈ {not-started, in-progress, green}.

> **Phase-1 hardened (2026-06-18).** Independent review found blocking and
> silent-corruption defects in the Phase-1 commit foundation; all fixed TDD
> (RED-before, GREEN-after), full gateway suite 2000 green, retrieval recall@10
> unmoved (0.926). Specifically: (1) crash recovery is now scoped to the failed
> intent's durably-recorded declared write set (`git checkout --` tracked,
> `rm` untracked) — never a tree-wide `reset --hard` / `clean -fd` that destroys
> other sessions' and the watcher's uncommitted/untracked work; (2) the MVCC CAS
> compares real per-path blob OIDs (`git rev-parse HEAD:<path>`), not the literal
> string `"HEAD"`; (3) idempotency resolves the `Intent-Id` trailer value exactly
> (no unanchored substring `--grep`, prefix-collision-safe); (4) the Phase-1
> merge scaffold fails safe — a real overlap dead-letters `needs-merge` instead
> of silently dropping a concurrent change (F1); (5) the rebase loop re-CASes the
> whole write set per-path against fresh HEAD; (6) the fencing token is durable
> per-intent state surviving queue-record loss; (7) `claim()` is atomic via
> `os.replace` with monotonic durable tokens (no double-claim race); (9) the
> watcher provenance node carries a producer marker with repo-relative paths so a
> real watcher commit is not falsely flagged as a `coverage_gap`.

> **Phase-3 review-hardened (2026-06-18).** Independent review (reviewer ≠ author) of
> the dedup keystone returned GO-WITH-FIXES; one BLOCKING + three IMPORTANT findings
> fixed TDD, all on the merge-reattachment path the builder's self-tests under-covered
> (claims-only test bodies hid the defects): **B1** merge silently dropped the deposit's
> non-Claims body / wikilinks / frontmatter aliases with no tombstone (silent corpus
> corruption + dedup-recall regression, since dropped aliases are the surfaces future
> deposits match on) → now unions aliases, carries body+wikilinks, writes a `merged_into:`
> tombstone, and dead-letters `needs-manual-merge` on a heading/body collision; **N1** the
> same silent-drop leaked through the deposit *preamble* → now carried under `## Merged
> context`, inert stub preambles stay inert; **I2** concept merges mis-targeted
> `wiki/entities/` (would mint a duplicate for `wiki/concepts/` candidates) → target now
> derived from the candidate's real rel_path, `_merge_kind` normalization preserves
> cross-kind-never-merge; **I1** the CiTO `disputes` edge pointed at the new claim even
> when policy ruled it the winner → now points at the policy-resolved loser. Full suite
> **2163 passed** (baseline ~2037 + Phase-3 + review-fix tests); eval-retrieval recall@10
> **0.926** (== baseline). One tracked **MINOR (N2)**: the disputes-edge line double-cites
> the loser source (cosmetic; the loser claim already carries its own citation).

| Component (design §) | Phase | Status |
|---|---|---|
| Intent queue — durable dir + on-disk lifecycle states (§3, §14) | 1 | green |
| Async return type — IntentReceipt / OperationResult ext + status-query (§3) | 1 | green |
| CommitGate — serial commit, MVCC CAS, fencing, crash recovery (§5) | 1 | green (hardened 2026-06-18) |
| Operational-provenance log + per-producer telemetry (§3) | 1 | green (hardened 2026-06-18) |
| Embedding index — three namespaces, upsert-on-commit, shadow-swap rebuild (§13) | 2 | green |
| Deposit API — typed intent tool + authorship workers (§3, §4) | 3 | green |
| Commit-time invariants — domain, dedup (I1), contradiction, trust (§6) | 3 | green (review-hardened 2026-06-18) |
| Read/build tier split — two MCP entrypoints + op-to-tier table (§7) | 4 | green (2026-06-19) |
| Deposit consumer contract — wait/backpressure (§3, §12) | 4 | green (2026-06-19) |
| Corpus-rot governance — remediation + fragmentation lint (§8) | 5 | green (2026-06-19; T2 review-hardened — de-path runs through gate, nested reachability) |
| Lifecycle & retraction cascade — Option A (§9) | 5 | green (2026-06-19; T1 review-hardened — reversals apply end-to-end, B-only alias restore) |
| Gap-routing & keep-worthiness (§10) | 5 | green (2026-06-19; T3) |
| DemandLedger — clustering + trigger (§11) | 5 | green (2026-06-19; T4 review-hardened — live cold-start + real-encoder I4; cluster()-driver = backlog) |
| Planner/executor pre-flight (§12) | 5 | green (2026-06-19; T4 read-tier preflight) |
| Reversal / anomaly detectors — §1.5 signals (G2) | 5 | green (2026-06-19; T5 review-hardened — detectors live on real data) |
| Policy keys + change-control — privileged-intent path (§14, G7) | 5 (mechanism); migration = backlog | green (2026-06-19; T6 review+security-hardened — CLI-only, server-sourced principal, fail-closed) |
| Verification harness — merge-map golden gate (I3), eval axes, taxonomy detectors (§16) | 5 (merge-map gate); rest cross-cutting | green (2026-06-19; T6 merge-map gate live) |

---

_Mutable. Edit freely during the build. The design document is the evergreen counterpart;
keep tunable numbers, targets, and progress here, never there._
