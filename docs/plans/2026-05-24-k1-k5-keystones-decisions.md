# K1–K5 Keystone Implementation — Decision Transcript

**Date:** 2026-05-24
**Companion to:** `docs/reviews/2026-05-23-knowledge-system-review.md` (the comprehensive review that surfaced K1–K5) and `docs/plans/2026-05-24-k1-k5-keystones.md` (the implementation plan, distilled below in § 7).
**Purpose:** Capture the full decision-making provenance for the K1–K5 keystone unlocks — exploration findings, alternatives considered, recommendations made and challenged, gating decisions locked, and the late amendment. Intended as a learning asset to review offline and as a reference for future hires asking "why did we choose this path?"

---

## 0. How to read this doc

This is not a plan; it's a *transcript* of how the plan was reached. It's structured chronologically so the reasoning unfolds in the order it actually happened. Each decision section names:

- **The question.** What had to be decided and why it mattered.
- **The options on the table.** Every alternative that was considered, with the rough cost/benefit shape.
- **My recommendation** and the reasoning for it.
- **What you said.** Including any pushback or clarification dialogue.
- **The locked decision.** What we're now committed to.
- **What I'd do differently if asked again.** Honest reflection where applicable.

§ 1 sets context. §§ 2–3 are the exploration phase. § 4 is the gating-question dialogue (the heart of the document). § 5 covers the decisions I committed without consultation. § 6 is the iOS Shortcut amendment. § 7 is the plan that resulted. § 8 is meta-observations and the lessons I'd extract for next time.

---

## 1. Context: how K1–K5 came to be

The 2026-05-23 comprehensive review identified five keystones — small-to-medium-effort changes that unlock disproportionate downstream work:

- **K1.** Gateway edit-path: `wiki cite-add` + `wiki edit --section`. Unblocks draft closer, contradiction resolution, semantic quality fixes, capture-to-cite. (`ARCH-5`, `QUAL-11`, `AGT-10`)
- **K2.** MCP-CLI parity sweep. Unblocks every agent recommendation. (`ARCH-7`, `TOOL-1`, `AGT-11`)
- **K3.** Cloud shim: Tailscale + bound `wiki serve` + bearer-token `/api/ingest`. Unblocks mobile, browser, voice, agent loops from outside the laptop. (`TOOL-2`, `TOOL-3`)
- **K4.** Scheduler substrate. Unblocks every scheduled agent + nightly hygiene jobs. (`TOOL-7`)
- **K5.** Token telemetry. Unblocks any cost/perf decision. (`TOK-2`)

You opened this work session by saying: *"critical path is to solve the K1–K5 keystone unlocks. To begin, determine the optimal sequencing and evaluate a multi-agent path to execution."*

The word "evaluate" was load-bearing. I didn't fully register that on the first pass and made an early mistake (see § 4.1). The whole session ended up being a study in not-anchoring-to-suggestions.

---

## 2. Phase 1 — Exploration

Per plan mode's workflow I was constrained to read-only actions until producing the plan file. I launched three Explore subagents in parallel — one per K-cluster — to map the code surfaces. Briefing them was deliberately tight so I'd get tight reports back; each was capped at ~1500 words.

### 2.1 K1 + K2 surface map (agent A)

**K1 (edit-path) findings:**

- Current `wiki cite` is at `src/gateway/ops/cite.py:24–146`. Entry: `cite(page_path, additions: list[tuple[int, str]]) -> OperationResult`.
- **The sharp edge.** `cite()` uses *file-line* numbering (1-indexed into the whole on-disk file including frontmatter). The validator (`validator.py:291–327`) reports *body-relative* line numbers via `c.line_no` from `_citations.uncited_claims()`. A page with 20 lines of frontmatter + a claim on body-line 5 → validator says "line 5", but `wiki cite` needs `--line 25` to target it. M46 followup #6 flagged this; the consensus was "validator should report file-line."
- Validator's post-write coverage is minimal — it doesn't re-run citation-grounding on a modified page.
- Lock: `wiki-author` (cite.py:105), held for the mutation + backlink updates + log append.

**K1 (new ops needed):**

- `wiki cite-add <page> "<claim>" <source-id>` — resolve claim text to a line, then delegate to `cite()`.
- `wiki edit <page> --section <name> --body <new>` — constrained section-replace; never general-purpose edit.

**K2 (MCP parity gap):** 13 of ~28 implemented CLI ops have MCP wrappers. Missing: `wiki_research`, `wiki_lint`, `wiki_batch_ingest`, `wiki_bootstrap_domain`, `wiki_discover_domains`, `wiki_promote_domain`, `wiki_demote_domain`, `wiki_reject_proposal`, `wiki_cite`, `wiki_backfill_examples`, `wiki_finetune`, `wiki_poll`. Plus K1's two new ops. ~12 wrappers + a parity test.

**Pattern to reuse:** `mcp_server.py:66–274`. Every existing tool follows:
```python
@mcp.tool()
def wiki_<op>(<args>) -> dict[str, Any]:
    from gateway.ops.<module> import <op_func>
    return _serialize(<op_func>(<resolved_args>))
```

### 2.2 K3 + K4 surface map (agent B)

**K3 findings:**

- `wiki serve` entry: `cli.py:988–998` → `uvicorn.run("gateway.web.app:app", host=ns.bind, port=ns.port)`. CLI parser already accepts `--bind` (default `127.0.0.1`) and `--port` (default `7474`). `--bind 0.0.0.0` works with zero code changes.
- FastAPI app: `web/app.py` (58 lines). Six routers mounted: status, domains, ops, tasks, research, review, nlm. `POST /api/ops/ingest` already exists and demonstrates the async-via-TaskStore pattern (`routes/ops.py:72–90`).
- Existing TaskStore (`web/tasks.py:82–99`): spawns daemon thread; tasks transition queued → running → done; poll via `GET /api/tasks/{id}`. **This pattern is exactly what K3 needs to reuse.**
- No existing auth layer. K3 introduces one (per-route opt-in dependency rather than global middleware, to avoid behavior change on existing routes).

**K4 findings:**

- Watcher launchd pattern: `scripts/install_watcher.sh:45–82`. Plist with `Label`, `ProgramArguments`, `WorkingDirectory`, `EnvironmentVariables` (PATH + KNOWLEDGE_ROOT), `RunAtLoad=true`, `KeepAlive=true`, log paths.
- Watcher (`watcher.py:282`) invoked via `wiki watch`. Writes `.knowledge/watcher.pid` + `.knowledge/watcher.heartbeat`.
- **No cron dep in pyproject.toml.** Recommendation: add `croniter>=2.0` (lightweight, stdlib-only deps).
- Lock pattern: `gateway/locking.py:14+`; use `file_lock(f"schedule-{job.name}")` to prevent overlapping runs of the same job.
- Subprocess shell-out is the right execution model (not in-process op dispatch) so arbitrary commands work, not just `wiki *`.

### 2.3 K5 surface map (agent C)

**Current state:**

- `ClaudeCLIClient.call()` returns plain `str`. No `--output-format=json` in use today.
- Three wrapper classes (`ClaudeCLIFilterClient`, `ClaudeCLIPlanClient`, `ClaudeCLIVLMClient`) each have `call()` / `call_split(system, user)`. M44 introduced this split.
- `log.append()` writes markdown headers (`## [ISO-ts] <op> | k=v | ...`); racy under concurrent writers (ARCH-1 finding). K5 should fix the lock as a side-effect.
- `wiki status` (`ops/status.py:17–46`) currently tails the last 5 log entries; perfect insertion point for a "7-day LLM usage" block.

**Key risk:** `claude -p --output-format=json` flag availability on the installed CLI version. K5 needs a graceful-degrade path (warn once, fall back to plain text) detected via stderr parse on first probe call.

**Call sites to migrate:** 5 (`filter/semantic.py`, `plan.py`, `vlm.py`, `research/orchestrator.py`, `research/analysis.py`).

---

## 3. Phase 2 — Plan agents skipped (judgment call)

The plan-mode workflow defaults to launching at least one Plan agent. I chose to skip that step. Reasoning:

- Exploration was thorough (~4500 words of structured findings across three agents).
- The design decisions were architecturally clear; the gating questions were locatable from the exploration alone.
- A Plan agent would either re-derive what was already known or get sucked into a specific design subtlety, neither of which justified the extra context cost.

This was the right call in retrospect. But it's worth naming: the plan-mode default is "use Plan agents" precisely because skipping can introduce blind spots. The mitigation here was that gating questions surfaced any remaining ambiguity directly to you.

---

## 4. Phase 3 — Gating-question dialogue

This is the heart of the transcript. Each subsection captures one gating decision with the full alternatives, my reasoning, your pushback, and the locked answer.

### 4.1 D1 — Sequencing strategy

**The question.** How should K1–K5 be sequenced and executed? You explicitly asked me to "evaluate a multi-agent path to execution."

**Options I offered:**

1. **Five parallel implementation agents** (one per Kn) — I marked this as "Recommended."
2. **Two waves: K5+K2 foundation, then K1+K4+K3 functionality.**
3. **Strict sequential (K5 → K2 → K1 → K4 → K3).**
4. **Hybrid: K1+K2 paired stream, K3+K4+K5 individual parallel.**

**My initial recommendation: option 1 (five parallel agents).** The rationale I offered: fastest wall-clock; matches "agent teams" framing.

**Your first answer: option 1 (the recommendation).**

**Your pushback.** A turn later, after I'd asked clarifying questions on the remaining decisions: *"why 1 over 2?"*

I re-evaluated and gave an honest answer:

| Where option 1 wins | Where option 2 wins (and these are weightier) |
|---|---|
| Fastest wall-clock if all five run truly independently | K1 + K2 share `mcp_server.py` — parallel agents would collide or duplicate |
| Matches "agent teams" framing | K5 should observe K1–K4, not be observed by them — putting K5 last in option 1 misses the first weeks of telemetry coverage |
| Worktree isolation prevents live merge conflicts | K2 establishes a CI parity test that forces K1 to ship with MCP wrappers — that's discipline you want **before** K1 lands |
| | Context cost: 5 concurrent agents × ~30–50k tokens = 150–250k in flight vs ~60–100k for two-at-a-time |

I concluded option 2 was the technically better choice and asked if you wanted me to flip to it.

**Your response.** *"What I said in the prompt was *evaluate* a multi-agent process, I did not mandate that approach. I expected that to be considered and resolved based on technical reality as part of the planning process."*

**The locked decision: option 2 (two waves).**

**What I'd do differently.** I anchored to the framing in your original prompt ("spin up agent teams") rather than evaluating the technical coupling that made option 2 better. Your correction was process-shaped, not just decision-shaped: when given a suggestion or framing, weigh it on technical merit rather than treating it as a brief to fulfill. This is now a feedback memory I want to preserve. See § 8 for the meta-observation.

### 4.2 D2 — Cite line-number bug fix direction

**The question.** Validator reports body-relative line numbers; `cite.py` expects file-relative. How to resolve?

**Options I offered:**

1. **Change validator to report file-line numbers.** (Recommended.) Single fix point. M46 followup #6 had stated this as the preferred direction.
2. Add `--body-line` flag to `wiki cite`.
3. Switch `cite.py` to body-line convention (back-compat break for any external scripts).
4. Document the gap, change nothing.

**My recommendation: option 1.** Aligns with prior M46 stated preference; one change point; no caller breakage.

**Your answer: option 1.** No clarification needed.

**Why this was easy.** The original M46 followup item had already recorded the preferred direction; I was effectively confirming an existing decision rather than making a new one.

### 4.3 D3 — `wiki_research` MCP surface shape

**The question.** The CLI version has `--dry-run`, `--review`, `--execute <session>`, `--queries <path>`, `--domain`, `--max-results`, `--no-plan` with mutual-exclusivity rules. How should the MCP version look?

**Options I offered:**

1. **Mirror all CLI flags as one `wiki_research` tool.** (Recommended.) Matches every other tool's convention (one CLI op = one MCP tool). Mutual-exclusivity enforced server-side.
2. **Three-tool polling model:** `wiki_research_start` / `wiki_research_status` / `wiki_research_review`. More ergonomic for agentic loops; diverges from CLI shape; new shape to learn.
3. Two tools: `wiki_research_run` + `wiki_research_status`.

**My recommendation: option 1.** Convention consistency. The flag set isn't *that* large. Mutual-exclusivity is a small server-side check.

**Your answer: option 1.**

**Trade I want named.** Option 2 (polling) would have been nicer for agentic loops in Phase 3 (`AGT-3` research orchestrator wrapper). But that wrapper is a follow-up skill that can poll over option-1's single call with reasonable cost. If agentic research becomes a hot path, revisit.

### 4.4 D4 — `/api/ingest` mode

**The question.** What should `POST /api/ingest` do?

**Options I offered:**

1. **Synchronous via TaskStore** (mirror `/api/ops/ingest`). (Recommended.) Endpoint accepts multipart file or `{url}`, calls `ingest()` in TaskStore daemon thread, returns 202 + task_id. iOS Shortcut polls `/api/tasks/{id}` for completion. Pattern already validated.
2. **Drop-to-inbox; watcher picks up.** Endpoint writes to `raw/inbox/` and returns 200 immediately. Simpler endpoint; fire-and-forget UX; no immediate signal if ingest fails downstream.
3. Both endpoints.

**My recommendation: option 1.**

**Your answer initially: skipped (unanswered in first AskUserQuestion call).** You wanted to clarify other questions first. When I re-asked on the second round, you picked option 1.

**Why I recommended option 1.** Sync via TaskStore gives the iOS Shortcut a real success/failure signal (the user sees if ingest worked). Drop-to-inbox is "throw it over the fence" — fine for high-volume capture, but the user can't tell if their share-from-Safari actually became a wiki page until much later. The TaskStore pattern is already validated by `/api/ops/ingest`; reusing it costs almost nothing.

### 4.5 D5 — `wiki cite-add` claim-resolution strategy

**This was the most interesting exchange of the session.** It surfaced a KISS-vs-robustness tension and resulted in an architecture better than any of the original options.

**The question.** How should `wiki cite-add` resolve a claim sentence to a line number?

**Options I offered initially:**

1. **Exact-text match only** (require disambiguation on multiple hits). I marked this Recommended.
2. **Substring match with normalization** (whitespace + case).
3. **Fuzzy match with LLM disambiguation.**
4. **Multiple strategies via flag** (`--match exact|substring|fuzzy`).

**Your pushback.** *"I am of the mind that fuzzy or multiple is the move here, as opposed to sync via taskstore. Am I violating my KISS principles? What is the cost/benefit of the multiple approach?"*

This was a great question — you were self-checking whether you were being inconsistent (picking the simple option for `/api/ingest` and a complex one for `cite-add`).

**My response.** I laid out the actual cost/benefit on a single axis (input forgiveness):

| Mode | Code | Tests | Runtime cost | Determinism | Recovers from |
|---|---|---|---|---|---|
| Exact-only | ~30 LOC | 4–5 fixtures | Free | Yes | Nothing |
| Substring + normalization | ~80 LOC | 8–10 fixtures | Free | Yes | Whitespace, smart quotes, em-dash drift (~90% of real failures) |
| Fuzzy (LLM-judged) | ~150 LOC + LLM dep | 10+ fixtures | ~1–3 s + ~$0.001 | **No** | Paraphrase, agent-reconstructed claims (residual ~10%) |
| Flag-all-three | All above + dispatch + docs | 3× | Variable | Mixed | "User has to know which flag" |

**My honest take.** The "multiple strategies via flag" option *is* the KISS violation — three modes the caller picks between, three test surfaces, three doc passages, optionality for its own sake. The two axes (UX feedback for `/api/ingest`, input robustness for `cite-add`) are not comparable; picking simple for one and forgiving for the other isn't inconsistent.

I then recommended **substring + normalization** as the KISS-compliant sweet spot.

**Your follow-up.** *"For wiki cite-add"* — you wanted me to commit to a concrete recommendation for cite-add specifically.

**My revised recommendation.** Internal escalation pipeline, not a flag-of-three:

```
exact match
  ↓ 0 hits
normalized substring (NFKC + casefold + whitespace + trailing-punctuation)
  ↓ 0 hits
fuzzy LLM (opt-in via --fuzzy, OFF by default)
  ↓ 0 hits
error: claim not found, here are 3 nearest by edit distance
```

At any step: 1 hit → cite; 2+ hits → ambiguity error requiring `--line N` tiebreaker.

**Why this shape was better than any original option.**

- One default code path (exact → normalized). Deterministic. ~80 LOC of mainline behavior.
- Fuzzy is a *fallback*, not a *mode* — caller doesn't pick between three. They get the deterministic pipeline by default; `--fuzzy=true` adds an LLM-judged final stage.
- The agentic capture-to-cite work in Phase 3 (`AGT-7`) and the draft closer (`AGT-2`) will pass `--fuzzy=true` when they invoke cite-add via MCP. Human callers leave it off.
- Fuzzy code stays cleanly behind a boolean — you can comment it out and the deterministic path keeps working. KISS isn't "smallest first cut"; it's "complexity that doesn't earn its keep." This earns its keep the moment `AGT-7` ships.

**Your answer.** *"Yes. That is the best hybrid approach."*

**Meta-observation.** This was the highest-leverage exchange of the session. Your willingness to push back on my too-simple initial recommendation forced a better shape than any of the original options. The lesson for me: when offering options, include a "neither of these — here's a hybrid" possibility, especially when the options are points on a single axis. I missed that on the first pass.

### 4.6 D6 — iOS Shortcut deliverable scope (and amendment in § 6)

**The question.** What's the iOS Shortcut deliverable as part of K3?

**Options I offered:**

1. **Setup doc only in TUTORIAL.md.** (Recommended.) ~15 min on phone following the doc. Verifiable end-to-end with curl before phone work.
2. **Defer iOS Shortcut entirely to a separate post-K3 task.**
3. Generate a `.shortcut` binary + doc. I called this hard-to-infeasible from a Claude Code session — Shortcuts app is GUI-only, `shortcuts` CLI can run but not really build.

**Your initial answer: option 2 (defer).** Clean K3 scope; one more thing on the queue.

**The amendment** (after plan approval): *"I want the iOS Shortcut as a discrete item in this cycle."*

See § 6 for the full reasoning of the revised split-delivery model.

### 4.7 D7 — Token telemetry rollout posture

**The question.** How should K5 telemetry roll out?

**Options I offered:**

1. **New `call_with_usage()` method alongside `call()`; migrate every call site in this milestone.** (Recommended.) Existing `call()` stays returning str. New method returns `CallResult`. All 5 known call sites migrate in M47. Zero risk of breaking existing behavior; uniform coverage from day one.
2. **Replace `call()` return type globally to (text, usage).** Higher PR surface; if `--output-format=json` has edge cases, every LLM call site hits them simultaneously.
3. **Add telemetry only to filter (M44.1 parallel hot path); defer plan/VLM.** Smallest cut; leaves "what does plan-authorship cost?" unanswered.

**My recommendation: option 1.**

**Your answer: option 1.**

**Why option 1 over option 2.** The wrapper classes (`FilterClient`, `PlanClient`, `VLMClient`) implement a Protocol that other code injects mocks against in tests. Replacing the return type forces every mock to change in the same milestone. Adding a new method is additive — old mocks keep working, new mocks add the usage path only if tests need it. Cleaner blast radius.

### 4.8 What I did *not* ask about (committed unilaterally with rationale)

After the four "truly gating" questions you answered (D1–D7), I had ~10 more on my candidate list. Per your earlier feedback ("evaluate, don't anchor") and to respect your time, I committed the rest in the plan as C1–C10 with rationale, expecting you to object on review if any were wrong. None were objected to. Listed in § 5.

---

## 5. Decisions I committed without asking (C1–C10)

These were not asked because the answer was either obvious from prior context (memory entries, hard rules) or unambiguously a default. Each carries a rationale so the choice is auditable.

| # | Decision | Choice | Why I didn't ask |
|---|---|---|---|
| C1 | `wiki edit` scope | Constrained section-replace only | No current caller needs broader; you can object later if a use case appears |
| C2 | Bearer-token storage | Hashed in `.knowledge/auth.yaml`; plaintext printed once on `wiki auth add`; gitignored | Standard hygiene; matches your global CLAUDE.md secrets rule |
| C3 | Default scheduler jobs | Empty `.knowledge/schedule.yaml`; TUTORIAL documents a recommended starter set | Avoids surprise scheduled runs; you explicitly enable each |
| C4 | Expose destructive MCP ops | Expose `wiki_reject_proposal` (drafts only); **omit** `wiki_demote_domain` (cross-page write impact) | Matches Message Send Gate spirit for destructive cross-state actions |
| C5 | Cost-USD in `wiki status` | Tokens always; USD behind `--cost` flag | Tokens are factual; USD is an estimate that diverges from Max-plan billing |
| C6 | `wiki_cite` MCP additions signature | `list[{line: int, source_id: str}]` | JSON-friendly; types are typed |
| C7 | Branch strategy | Two feature branches, one per wave; rebase wave-2 on merged wave-1 | Two PRs total; reviewable; matches sequencing |
| C8 | Test discipline | TDD for new ops (`cite_add`, `edit_section`, scheduler, telemetry parsing); test-after for mechanical MCP wrappers | Cost-of-tests matches risk |
| C9 | Hand-tests per Kn | Each Kn ships with hand-test notes in `docs/milestones/M47.md` (wave 1) and `M48.md` (wave 2) | Per memory entry `collaboration_style.md` |
| C10 | Locking discipline | All new write paths use `file_lock(...)`; new lock names registered in `LOCK_NAMES`; closes `ARCH-1`/`ARCH-8` opportunistically | Avoid silently inheriting the racy log/index bug while we're in the area |

---

## 6. Late amendment: D6 reversed (iOS Shortcut moves in-scope)

**Your message after plan approval.** *"I want the iOS Shortcut as a discrete item in this cycle."*

**Why this matters.** D6 had been "defer to post-K3 follow-up." You reversed it. The interesting subtext: bringing iOS Shortcut into the cycle means K3 becomes a *complete* mobile-capture deliverable rather than a half-shipped one. The risk of deferral is the user (you) loses momentum on the mobile pipeline — and the whole point of K3 is mobile capture.

**The realistic delivery constraint.** I genuinely cannot construct a trusted `.shortcut` binary file from a Claude Code session. The Shortcuts app is GUI-only on macOS; the `shortcuts` CLI runs Shortcuts but does not author them. The `.shortcut` file format is a binary plist that's trust-prompted on import — hand-construction isn't reliable.

**The split-delivery model I committed to.**

- **What I deliver in this cycle:**
  - `TUTORIAL.md § "Remote capture from iOS"` — step-by-step build doc: trigger config (Share Sheet input types), HTTP action config (URL, method, headers, JSON body), task_id notification, export instructions
  - `scripts/test-ingest-curl.sh` — curl invocation matching the Shortcut's HTTP call exactly; verifies the endpoint contract from any machine before you ever touch the phone; configurable for Tailscale hostname via env vars
- **What you deliver in this cycle:**
  - Build the Shortcut on your iPhone following the TUTORIAL
  - Test it end-to-end (Safari Share → Wiki Capture → task_id notification → file appears in `raw/`)
  - Export the Shortcut via iOS Share → Save to Files → repo `scripts/` directory
  - Commit `scripts/wiki-capture.shortcut` to the repo
- **Net.** The Shortcut becomes installable by anyone who clones the repo (one-tap import on iOS).

**Plan file updated.** D6 row flipped from "deferred" to "in scope this cycle, split delivery." K3 section gained an "iOS Shortcut sub-deliverable" subsection. Hand-test step 7 now requires the end-to-end iPhone test. Out-of-scope trimmed to just "iOS Shortcut multipart file uploads" (v1 supports URL + text only — covers Safari share + Notes selection).

---

## 7. The plan that resulted (distilled)

The full implementation plan is at `~/.claude/plans/critical-path-is-to-playful-panda.md`. The essential structure:

### Sequencing

```
Wave 1 (K5 + K2 foundation)
  ↓ merge
Wave 2 (K1 + K4 + K3 parallel)
```

Wave 1 must merge before wave 2 starts because:

- K5 establishes the `call_with_usage()` contract that wave-2 ops use when making LLM calls
- K2 establishes the MCP-parity CI test that force-fails K1 if K1 omits MCP wrappers
- K2 cleans up `mcp_server.py` so K1 can append two new tool registrations without merge conflict

### Wave 1 — K5 + K2

**K5 — Token telemetry.** New `CallResult` dataclass in `llm/telemetry.py`. New `call_with_usage()` method on `ClaudeCLIClient`. Per-call log line in `log.md` (single-line, pipe-delimited, grep-friendly). 7-day usage block in `wiki status`. `--cost` flag adds USD estimate via new `gateway/costs.py`. All 5 call sites migrated this milestone. Lock-registry update closes ARCH-1 racy-log bug opportunistically.

**K2 — MCP parity.** 12 new MCP tools mirroring CLI ops 1:1. `wiki_research` mirrors all CLI flags as one tool (D3). `wiki_demote_domain` explicitly omitted (C4). `wiki_cite` additions signature is typed objects (C6). New `tests/gateway/test_mcp_parity.py` asserts every entry in `cli.IMPLEMENTED` has a `wiki_*` tool (the forcing function for K1).

### Wave 2 — K1 + K4 + K3 (parallel, file-disjoint)

**K1 — Edit-path.** New `ops/cite_add.py` with the internal escalation pipeline from D5 (exact → normalized → optional fuzzy LLM). New `ops/edit_section.py` (constrained section-replace per C1). `validator.py` line-number fix per D2. CLI `cite-add` and `edit` subcommands. K1's MCP wrappers land last because the K2 parity test enforces them.

**K4 — Scheduler substrate.** New `scheduler.py` (cron via `croniter`, per-job `file_lock`, subprocess shell-out, cooldown guard for failing jobs). New launchd installer at `scripts/install_scheduler.sh` (60s tick, KeepAlive, mirrors watcher pattern). `wiki schedule add/list/run/...` CLI subcommands. UTC-only in v1.

**K3 — Cloud shim.** New `web/auth.py` (bearer-token verification, hashed in `.knowledge/auth.yaml`). New `web/routes/cloud.py` (`POST /api/ingest`, multipart or JSON, sync via TaskStore per D4). `wiki auth add/list/revoke` CLI subcommands. **iOS Shortcut sub-deliverable per D6 amendment:** TUTORIAL doc + curl verification script delivered by Claude Code; `.shortcut` binary built and exported by Andrew, committed to `scripts/`.

### Cross-cutting

- Locking: every write path acquires `file_lock(...)`. New lock names registered in `LOCK_NAMES`.
- Log format: per-LLM-call entries are single-line `## [ts] llm-call | k=v | ...`.
- Test discipline: TDD for new ops; test-after for mechanical wrappers.
- Hand-tests: `docs/milestones/M47.md` (wave 1), `docs/milestones/M48.md` (wave 2).

### Verification

End-to-end checks post-merge: telemetry on a real research run; parity test green; K1 edit-path closes one stale draft; K4 test job runs on schedule; K3 curl from laptop POSTs to `/api/ingest` and lands a wiki source.

---

## 8. Meta-observations and lessons

### 8.1 "Evaluate, don't anchor" — the core feedback

The most important moment of the session was your correction: *"What I said in the prompt was *evaluate* a multi-agent process, I did not mandate that approach. I expected that to be considered and resolved based on technical reality as part of the planning process."*

The pattern I fell into: take a framing or suggestion from a previous message as a brief to fulfill, rather than as a hypothesis to weigh. When you said "spin up agent teams and an orchestrator" in the original review prompt, you were describing a *capability* to use; you weren't saying every future planning task must use the same shape.

This generalizes beyond multi-agent sequencing. Any time you offer a framing ("we should…", "I'm thinking…", "what about…"), the right response is to weigh it on its technical merits and counter-propose if better options exist — not to absorb it as constraint.

**I'm proposing this as a feedback memory entry:** `feedback_evaluate_dont_anchor.md` — when given a suggestion or framing, weigh on technical merit. Counter-propose if technical reality favors a different answer. Don't treat framings as briefs.

### 8.2 The KISS-vs-robustness exchange

The cite-add resolver exchange (§ 4.5) produced a better architecture than any of the original options because you pushed back ("am I violating my KISS principles?"). I had initially over-cleaved the design surface into discrete modes (exact / substring / fuzzy / flag-of-three) when the natural architecture was an escalation *pipeline* with one default path and an optional fallback.

**Pattern lesson.** When alternatives are points on a single axis (in this case, input forgiveness), they often combine into a graceful-degradation pipeline rather than mode-select. Look for that shape first before offering them as discrete options. The "flag-of-three" option I offered was a KISS violation I should have flagged myself.

### 8.3 The recommendation-default trap

I marked my preferred option as "Recommended" on every question. You picked the recommendation on most, pushed back on a couple. The risk this surfaces: when the "Recommended" label nudges the user toward the same answer the model would have given alone, the consultation collapses to confirmation theater.

**Mitigation.** When the "Recommended" choice is genuinely close on the merits (option 2 in the sequencing question was technically equivalent or better), don't mark either as Recommended — surface the tradeoff and let the user weigh. Only mark a recommendation when it's a clear default (e.g., "use the existing TaskStore pattern" vs "invent a new async model").

### 8.4 Plan-mode discipline held up

Plan mode constrained me to read-only actions until the plan file was written. This was helpful — it forced exploration → consultation → plan-write in clean phases rather than racing into code. The discipline of *not* being able to edit anything except the plan file made the gating-questions phase tighter.

### 8.5 Where multi-agent execution actually fits

Despite revising D1 from five-parallel-agents to two-waves, the *idea* of multi-agent execution wasn't wrong — just the granularity. Within each wave, the work is parallel-friendly:

- Wave 1: K5 and K2 touch (mostly) disjoint files. They could run as two parallel implementation agents.
- Wave 2: K1, K4, K3 truly touch disjoint files. They can run as three parallel implementation agents rebased on merged wave-1.

So the "multi-agent path" framing was right — just not at the K1–K5 level. It's at the within-wave level. Worth naming because the original prompt's intent ("multi-agent execution") is still fully achievable; we just sequence two waves of multi-agent work rather than one big bang.

### 8.6 Late amendments are a sign the process worked

The iOS Shortcut amendment came *after* plan approval. That's not a bug — it's a sign you trusted the structure enough to scope-add late without rewriting the plan. The amendment was localized (one decision row + one subsection + a few line edits) precisely because the plan was structured to allow it.

The discipline that enabled this: decisions were tabulated (D1–D7, C1–C10), not just narrative. Tables are amendable; prose is not.

---

## 9. Appendix — pointers

- **Plan file:** `~/.claude/plans/critical-path-is-to-playful-panda.md` (canonical) and `docs/plans/2026-05-24-k1-k5-keystones.md` (project copy, if produced)
- **Review that surfaced K1–K5:** `docs/reviews/2026-05-23-knowledge-system-review.md` § 1 (executive summary), § 14 (phased roadmap)
- **M46 followup items referenced:** `docs/M46-followup-items.md` items #1, #3, #5, #6
- **User memory entries referenced:**
  - `feedback_general_purpose_inherits_surface_anchors.md` (relevant for Track B Phase 0)
  - `feedback_hard_rules_are_stop_signals.md` (informed C4 destructive-MCP decision)
  - `gateway_idempotent_convergent.md` (informed K2 + ARCH-6 framing)
  - `gateway_edit_path_open_question.md` (resolved by K1 → propose to retire this memory entry post-K1)
  - `collaboration_style.md` (informed C9 hand-test convention)
  - `docs_describe_invariants.md` (informed why state snapshots in this doc are timestamped)
- **Proposed new feedback memory** (pending your approval): `feedback_evaluate_dont_anchor.md` — when given a suggestion or framing, weigh on technical merit; counter-propose if technical reality favors a different answer; don't treat framings as briefs

---

*End of transcript. Next action: copy the canonical plan from `~/.claude/plans/` to `docs/plans/` (if you want it project-versioned), then kick off Wave 1 with K5 + K2 setup.*
