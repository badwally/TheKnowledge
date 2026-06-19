# Design constraints register — Librarian multi-agent RAG

Authoritative must-resolve input to the design-generation prompt
(`2026-06-18-librarian-multi-agent-rag-design-prompt.md`). Each entry is a **concern the
design must land in code with its acceptance criterion — not prose to reproduce**. Derived
from two adversarial review passes; the substrate (git-canonical, derived-rebuildable index,
async-intent) was confirmed sound, so every entry below is about the semantic, operational,
or governance layer riding on it. The design must address each by ID; the generating agent
reports per-ID resolution.

Maps to the design document's output sections (design §N). Where an entry names a file, that
is its codebase attachment point.

---

## A. Concurrency & commit protocol (design §2, §3, §5)

- **C1 — Pre-`git add` torn write.** The N-file merge-reattachment writes precede the atomic git boundary. Crash recovery MUST `git reset --hard HEAD` + `git clean -fd` to HEAD before re-claiming any in-flight intent. *AC: a kill-mid-reattachment integration test leaves `git status` clean post-restart and the intent re-runs from `claimed`.* (`core.write_atomic` is per-file `os.replace`; no multi-file primitive exists.)
- **C2 — Idempotency keyed off committed state, not the queue status file.** Write `intent_id` into the commit itself (commit-message trailer or an `applied_intents` record updated in the same commit); recovery resolves disposition by scanning committed history, not the status file (which can lag the commit by one crash). *AC: redelivering an already-committed intent produces no second write.*
- **C3 — Fencing tokens on the lease.** Issue a monotonic fencing token at claim; the committer rejects any commit whose token is not the highest issued for that `intent_id`; the lease is renewable by a live-worker heartbeat so legitimately-long authorship does not trigger spurious reclaim. *AC: a resurrected slow worker cannot overwrite the reclaimer's commit.*
- **C4 — Hot-entity livelock bound.** The rebase-on-conflict CAS loop needs a bounded retry (`«commit.max_rebase_attempts»` → dead-letter with a "contention" reason) and per-entity rebase-retry + oldest-rebased-intent-age metrics. *AC: sustained contention on one entity makes progress or dead-letters; it never spins forever undetected.*
- **C5 — New-referent write-skew.** Two intents first-minting the same referent under different surface names against the same snapshot must not both commit as distinct pages. The commit-phase re-check searches the entity namespace as updated within the current serialization window plus the in-flight batch's canonical_names/aliases. *AC: two such intents resolve to one canonical page (second merges); zero duplicate-referent pages per `wiki lint --scope dedup`.*
- **C6 — Causal-dependency bounds.** A deferred intent whose antecedent reaches a terminal non-committed state is dead-lettered ("broken-dependency"); dependency cycles are rejected at submit; track deferred-intent age.
- **C7 — Watcher/poller writes bypass the intent graph (convergent, two lenses).** The watcher and pollers write `raw/` directly, with no intent and no operational-provenance node — so "every corpus change has an intent" is false today. Either route source ingest through the deposit API as source-intents (preferred), or synthesize a `provenance: poller/<name>` operational node at ingest. The committer stages explicit file lists, never `git add -A`, and shares the commit mutex / `.git/index.lock` with watcher writes. *AC: no corpus state exists without an operational-provenance ancestor.* (`watcher.py`, `pollers/`)

## B. Identity & retrieval (design §6, §13, §16)

- **I1 — Dedup adjudicator is deterministic and LLM-free at commit (KEYSTONE).** The merge/link/keep-distinct decision at the serial commit phase is a fixed precedence procedure over (entity_kind match, alias/canonical_name exact-or-normalized match, domain overlap, blocking-NN distance band). Any LLM judgment runs on the worker against the snapshot and emits a *recommendation* the committer re-validates deterministically against HEAD — never a model call in the commit critical section. *AC: the commit-phase dedup re-check is LLM-free and reconstructable from logged inputs; same inputs → same verdict (replay test).*
- **I2 — Per-namespace adequacy gate.** One shared encoder serves three operating points (retrieval relevance, dedup co-reference, demand topical-gap), which pull geometry in incompatible directions. Each namespace ships its own golden set and a named fallback if the shared model fails its gate: dedup → alias/lexical blocking as authority with embeddings recall-only; demand → lexical-canonicalized gap-signatures. *AC: each operating point's gate is independently falsifiable; shared encoder is starting infrastructure, not a correctness guarantee.*
- **I3 — Golden merge-map non-circularity.** The recall-resolution merge-map is provenance/tombstone-derived (a record of merges that happened); dedup precision is judged against an independent, human-curated merge/link/distinct golden set. A merge enters the recall map only after the dedup golden confirms it correct — a wrong merge fails the eval rather than laundering itself into a pass. Golden-staleness tracks unresolvable AND unconfirmed-merge `expect` slugs. (`evaluate/retrieval_eval.py` matches `slug in g.expect` literally today.)
- **I4 — Demand recurrence-mass survives re-embedding.** The demand ledger retains raw gap-signature *text*, not only vectors; a model-version bump re-embeds and re-clusters from text, preserving recurrence counts. *AC: a model bump does not reset a near-threshold gap to zero.*

## C. Agent contract & operability (design §3, §7, §12, §16)

- **A1 — Deposit consumer wait-contract.** Status-query returns a `retry_after`/poll-interval hint on non-terminal responses; after a bounded total wait the agent proceeds on carried-forward content (fire-and-forget); state explicitly that no push/callback exists in the stdio MCP surface; optionally a bounded `deposit_and_wait`. *AC: an agent author can code the wait loop from the spec alone.*
- **A2 — Exhaustive op-to-tier table.** Every registered `wiki_*` tool is classified read / build / not-exposed by the rule "side-effect-free AND token-free → read, else build" (so read-only-but-LLM-spending `filter` and `answer`-without-`--file` are build-tier). The read-tier server's registered set equals exactly the read-classified set, verified by a parity-style test. `CLI_ONLY` is not a tier and must not be reused as one. (`mcp_server.py`)
- **A3 — Backpressure has agent-side semantics.** Deposit returns a load signal (`queued` vs `rejected:overloaded` + `retry_after`); lock acquisition is bounded, never an indefinite block (migration delta: `locking.py` `flock(LOCK_EX)` has no timeout); the agent's prescribed response per signal is specified (proceed on carried content; defer non-load-bearing; never tight-retry).
- **A4 — Carry-forward consistency cases.** Distinguish provisional (the agent's own submitted text, flagged pre-canonical, for in-session reasoning) from authoritative (canonical content + path obtained only from terminal status, including `merged` → a different page). Demand-miss logging suppresses misses only for the session's own outstanding/terminal `intent_id`s, never another agent's identical query.
- **A5 — Async return type (foundational, design §0).** Specify the exact shape: either extend `OperationResult` with optional `intent_id`/`disposition`/`retry_after`/`canonical_path` (and confirm existing `_serialize` consumers tolerate absence) or a named `IntentReceipt` sibling; status-query returns the terminal-disposition union as a typed shape.
- **A6 — Rebuild concurrency discipline.** Derived-index rebuild writes to a shadow location and atomically swaps (readers see old-complete or new-complete, never half); because commit-time dedup depends on index freshness, commits are quiesced or read a pinned pre-rebuild snapshot during an embedding-namespace rebuild. *AC: a `retrieve` during rebuild returns complete-index results; no duplicate canonical page is committed during a rebuild.*
- **A7 — Silent-producer / compounding-failure detector.** Per-producer alarms on rejection-rate spike, dedup-merge-to-existing spike (a producer adding only non-novel content), and deposit-silence (a previously-active producer dropping to zero). Named as a taxonomy bad state with this telemetry as its detector.

## D. Governance & lifecycle (design §6, §8, §9, §14, §16) — Option A scope

- **G1 — Resolution-reversal primitive (Option A).** `revert-resolution <act-id>` as a CommitGate intent: un-suppress the loser, re-open the contradiction edge, re-run the rule against current inputs; provenanced. Automatic transitive cascade is DEFERRED (Option B, plan of record — `docs/backlog/librarian-cascade-revert-automation.md`).
- **G2 — Reversal detectors + metrics.** Contested-claims lint (a lower-trust claim auto-overruled); cross-project-override rate; auto-resolution-reversal rate; observed cascade-depth — these are the measured triggers that gate building Option B. The down-weighted loser stays retrievable, never de-pathed.
- **G3 — Retracted-winner un-suppression.** Retraction/supersession of a source traverses the operational-provenance graph for resolution acts where it was the *winning input* and re-opens each (re-run the rule against survivors, which may promote the former loser) — not only the citation graph. Named taxonomy bad state "orphaned-correct-claim after winner retraction" with a standing lint detector.
- **G4 — Retraction cascade is transitive over `synthesizes:` closure.** One-level-strict `synthesizes:` typing means a second-derivative synthesis does not directly cite the retracted source; the cascade walks the closure to a fixpoint with a cycle/termination assertion. *AC: a source → synthesis-A → synthesis-B chain flags/quarantines BOTH on retraction.*
- **G5 — Server-derived trust; self-report advisory only.** The trust tier used in contradiction precedence derives from source-type default + filter score (auditable, server-side). Agent self-reported trust is advisory and never sets the precedence tier; log self-vs-derived divergence per producer. (Closes the buggy-agent-inflates-trust poison vector under cooperative identity.)
- **G6 — No-de-path rule covers the provenance graph.** Remediation never de-paths a page that is a citation target OR a non-reverted resolution-act input OR a tombstone/merge referent with live inbound path-references — "no de-pathing of anything reachable from the operational-provenance graph," not just the citation graph.
- **G7 — Policy change-control is enforced, not documented.** Changes touching dedup/trust/contradiction keys route through the CommitGate as a privileged intent with allowlisted (build-time) identity, gated by `eval-retrieval --compare` and golden-merge re-eval. Migration delta: the validator's lenient mode accepts hand-edited `policy.yaml` today (WIKI.md §10.1).
- **G8 — Merge reversibility.** The merge act records the pre-merge reattachment set (which inbound links/backlinks/`synthesizes:` refs were rewritten B→A) so a reversal can un-merge without git archaeology; otherwise downgrade the "reversible" claim for merges and defer clean un-merge with a trigger.

## E. Failure-mode taxonomy — specific detectors the design §16 taxonomy must bind

- **F1 — Lost-update detector = claim-conservation reconciliation.** Every claim in a committed intent's payload resolves to a claim on the canonical page or to an auditable resolution act; a periodic pass re-derives the claim-set and alarms on any intent whose payload claims are unaccounted-for. (A lost update raises no exception and breaks no link — it must be named to be caught.)
- **F2 — Index-rebuild-divergence detector = rebuild-and-diff equivalence.** Rebuild into a shadow index and diff against live; bind this to the taxonomy row, not just the rebuild-time metric.

---

## Self-check (generating agent)

Report per-ID: resolved (with the design §-anchor) or explicitly deferred (with trigger). Any ID with no detector + bounded recovery, or any «ledger-key» referenced without a ledger row, is a defect.
