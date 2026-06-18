# Session review — 2026-06-17

Scope: scoped the `agentic-data-layer` research domain, ran a 3-plan corpus build, diagnosed a YouTube-yield problem down to a filter regression, and shipped the fix (merged `a4b11ac2`). Evidence: commits `1a63b1bc`..`a4b11ac2`, the code diff (`559412b7..a4b11ac2`, 103 lines src/tests/policy), and the conversation tool-call sequence.

Test state: 220 passing in the `filter or research or planner` set on merged `main`; zero regressions.

---

## § 1 — Code and coding quality

**Finding 1.1 — Behavioral validation is deferred; tests prove prompt *content*, not prompt *effect*. (Medium — test gap)**
`tests/gateway/test_filter.py:530-563` and `tests/gateway/test_research_query_planner.py:247-266` assert that the guidance text and channel-authority signals *appear in the rendered prompt*. No test verifies the actual outcome — that a YouTube candidate with a thin description but an authoritative channel now scores ≥ `threshold_include`. This is an inherent limit (the scoring is an LLM call, not unit-testable), and the plan acknowledged it, but the consequence is that the whole fix is unvalidated behaviorally until the deferred empirical re-run. Fix: treat the YouTube-heavy re-run in `agentic-data-layer` (when the S2 key is idle) as a required acceptance gate, not an optional follow-up; capture the before/after `accepted` count in the run log.

**Finding 1.2 — Two source-type-keyed guidance maps now exist and can drift. (Medium — coupling)**
`src/gateway/filter/semantic.py:154-172` (`_SOURCE_TYPE_GUIDANCE`) and `src/gateway/research/query_planner.py:48-70` (`_ADAPTER_GUIDANCE`) both encode per-source-type instructions, in different files, with no shared key set or cross-reference. Adding a new source type now requires editing source-type guidance in two places, and nothing flags if one is forgotten. They serve different stages (query-gen vs scoring) so unifying them is not warranted, but a one-line comment in each pointing at the other would prevent silent drift. Fix: add a cross-reference comment; or, later, a test asserting both maps cover the same `paths.SOURCE_TYPES` set.

**Finding 1.3 — `**youtube / video**` references a non-existent source type. (Low — dead vocabulary)**
`src/gateway/filter/semantic.py:159`. The enum (per CLAUDE.md and `paths.SOURCE_TYPES`) is `youtube`; there is no `video` type, and the user payload only ever carries `type: youtube`. Harmless as a model synonym, but it could mislead a future reader into thinking a `video` type exists. Fix: trim to `**youtube**`, or leave as an intentional synonym (one-word call).

**Finding 1.4 — `speaker_expertise` policy signal largely restates `content_depth`. (Low — redundancy)**
`.knowledge/policies/agentic-data-layer/policy.yaml` (new `speaker_expertise` block). Its positive signals ("references specific systems, papers, or benchmarks by name"; "discusses mechanisms with precision") overlap the existing `content_depth` signal. Tolerated by the policy dump and biases in the intended direction, but it is prompt redundancy. Fix: in a future policy refinement, narrow `speaker_expertise` to *speaker/credential* signals distinct from *content* depth.

**Finding 1.5 — New tests use intra-function imports. (Low — convention drift)**
`test_filter.py:532,550` use `from gateway.filter import semantic` inside the test body. Inconsistent with the module-level imports elsewhere, though it matches the pre-existing `test_score_prebuilt_system...` at line ~506. Fix: hoist to module level, or leave for consistency with the one prior instance.

Root-cause check: the fix addresses the actual root cause (the port dropped per-source-type filter knowledge), not a symptom — verified by tracing `body_head = item.description or item.title` (`orchestrator.py:287`) and `_candidate_front` omitting representative content for video. No symptom-papering.

---

## § 2 — Token efficiency

**Finding 2.1 — zsh word-split retry. (1 wasted call)**
The first word-count loop used `for id in $ids` with a space-joined string; zsh does not word-split unquoted scalars, so the whole list was treated as one filename → "NOT FOUND". Re-ran with a zsh array. The environment banner states the shell is zsh; this precondition was known. Alternative: use an array (`ids=(...)`) or `${(s: :)ids}` from the start. Excess: 1 tool call.

**Finding 2.2 — corpus-sampling detour via mtime. (≈1-2 wasted calls)**
First attempt to identify the session's materialized sources used `find -newermt '15 minutes ago'` (returned 0 — files were older than the wall-clock window) and `find -newermt '60 minutes ago'` (0). Then pivoted to the authoritative method: source IDs cited in the session's synthesis pages. The parallel project's concurrent writes made mtime/git-status unreliable anyway. Alternative: go straight to "grep `[[sources/...]]` in the session's synthesis pages" as the source-of-truth for which sources belong to the run. Excess: ~1-2 calls.

**Finding 2.3 — bootstrap-domain retry was unavoidable. (0 avoidable)**
`wiki bootstrap-domain` failed once on an LLM parse/truncation, succeeded on retry. Transient (shared LLM adapter under load); no precondition check would have prevented it. Noted as not-a-finding for completeness.

Strengths checked: subagent handoffs used files (briefs/reports/diffs) rather than pasted context — the controller's context stayed lean; model tiering was correct (haiku for transcription implementers, sonnet for task reviews, opus for the final whole-branch review); reads were mostly targeted greps and sed ranges, not full-file dumps. Net token discipline was good; the two findings above are minor.

---

## § 3 — Prompt and context engineering

**Finding 3.1 — Recommended fixes before seeding the code context; reversed twice on evidence. (High — the session's main process lesson)**
The fix recommendation went through three rounds before landing right:
1. "Drop YouTube" — made from the *yield number alone*, before reading any filter code.
2. "Score post-materialization" — a full re-architecture (pre-gate → fetch → re-score), designed and user-approved, before verifying how the filter scores candidates or how NLM ingestion works.
3. "Restore YouTube-aware filter" — the correct fix, reached only after reading `semantic.py` (`body_head`), `orchestrator.py` (`_candidate_front`, `source_add_url`), and the research-notebook comparison.
Each earlier recommendation was refuted by evidence that was cheaply available up front. The decisive facts — the filter scores pre-transcript metadata, and NLM already gets the transcript via URL — would have produced answer #3 directly in one evidence pass. This is the [[feedback_evaluate_dont_anchor]] / verify-before-recommend pattern: a design recommendation on a load-bearing pipeline should follow a read of the relevant code, not precede it. Cost: ~3 AskUserQuestion rounds + one discarded approved design.

**Finding 3.2 — The fix-approach question was asked before checking the legacy system. (Medium)**
The `AskUserQuestion` offering "score post-materialization vs transcript-head vs channel-boost" was presented, and the user *rejected it to clarify* and then sent the agent to check `research-notebook` — which flipped the entire answer (proved metadata-first filtering works; the gap was the prompt, not the pipeline ordering). The legacy-system check should have preceded the fork. Lesson: when the user references a prior working system ("research-notebook was effective"), read it *before* framing the options, not after.

**Finding 3.3 — Subagent dispatch prompts were precise and pre-empted known traps. (Strength)**
The Task 2 dispatch warned the implementer the regression-guard test passes immediately (not RED→GREEN); the Task 3 dispatch flagged the intentional `"tutorial"` inside `"avoid tutorial..."`. Both pre-empted predictable confusion. File-based handoff + verbatim-code briefs kept implementers on-rails. No correction rounds were needed on any of the three implementer subagents.

**Finding 3.4 — Drift self-correction worked, late but real. (Mixed)**
The agent caught its own surface-anchor-leakage ("drop YouTube" would have entrenched the bug) and reversed it — the right instinct. But the catch came only because the user pushed back with a concrete counter-example (4/5 legit results from a manual YouTube query). The drift wasn't self-detected; it was user-detected. Pairs with 3.1.

---

## § 4 — Session-state checkpoint

**In-flight / open contracts:**
- None blocking. Feature merged to `main` (`a4b11ac2`); branch `feat/youtube-aware-filter` deleted; SDD ledger at `.git/sdd/progress.md` (transient briefs/reports/diffs removed).
- The working tree still holds the **parallel project's** uncommitted `wiki/` + `raw/` files and pre-existing session-start edits (condo/quebec wiki, gateway converters, docx). These are NOT this session's work — do not `git add -A` / `git add -u`; leave for their owners.

**Decisions made:**
- New domain `agentic-data-layer` (sibling to `semantic-models`), vertical-agnostic — anchoring to longspan would bias the filter/example bank. Bootstrapped + committed `559412b7`.
- 3 query plans; Plans 1+2 run as fan-outs, Plan 3 as post-hoc `wiki query` synthesis. All landed.
- YouTube fix = restore metadata-based YouTube-awareness (per-source-type guidance + `channel_authority`/`speaker_expertise` signals + lecture/talk query register), NOT score-post-materialization — research-notebook proved metadata-first filtering works and NLM gets the transcript via URL regardless.

**Rejected approaches:**
- "Drop YouTube" — disproven; 0-accepts was a filter regression, not absent signal.
- "Score post-materialization" — over-engineered; the transcript already reaches NLM via `source_add_url`, so fetching it earlier buys nothing.

**Current system state:**
- Verified working: `agentic-data-layer` domain live (27-source NLM corpus, 13 synthesis pages, MOC); filter now carries source-type guidance + channel-authority signals; planner emits lecture/talk YouTube queries; 220 tests pass on `main`.
- Known-not-yet-validated: the YouTube fix is validated at prompt-construction only, not behaviorally (Finding 1.1).
- Adapter note: semantic_scholar 429s under concurrent use of the shared `S2_API_KEY` (~1 req/s authenticated tier) — Plan 2's academic branch is missing.

**Next atomic step:**
- Re-run a YouTube-heavy `agentic-data-layer` query plan when the parallel run is idle (frees the S2 key); confirm authoritative talks now appear in `accepted` (acceptance gate for the fix) and recover Plan 2's academic branch. Drop YouTube? No — keep it, with the restored filter.

**Pending (awaiting user OK):** two memory entries — (1) S2 shared-key concurrency 429; (2) filter lost per-source-type awareness in the port (links [[feedback_general_purpose_inherits_surface_anchors]]).

---

## Priority table

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | Prompt/context (§3.1) | Design recommendations preceded reading the relevant code; reversed twice | Make "read the load-bearing code (and any referenced prior system) before recommending a fix" an explicit gate; save memory entry #2 |
| 2 | Code/test (§1.1) | YouTube fix validated at prompt-construction only, not behaviorally | Run the YouTube-heavy `agentic-data-layer` re-run as an acceptance gate; log before/after `accepted` counts |
| 3 | Code/coupling (§1.2) | Two source-type guidance maps (`semantic.py`, `query_planner.py`) can drift | Add cross-reference comments now; later a test asserting both cover `paths.SOURCE_TYPES` |
| 4 | Token (§2.1–2.2) | zsh word-split retry + mtime-sampling detour | Default to zsh arrays for list iteration; identify session sources via synthesis-page citations, not mtime |
| 5 | Code (§1.3) | `**youtube / video**` references a non-existent type | One-word trim to `**youtube**` (or keep as deliberate synonym) |
