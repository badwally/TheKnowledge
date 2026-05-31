# Session review — 2026-05-29

Session scope: R3 orita-cmo research (3 failed runs), PR #11 (slug bounding + YouTube throttle), iOS Shortcut / Tailscale setup.

---

## § 1 — Code and coding quality

**[High] `_MAX_SYNTHESIS_SLUG = 80` duplicates `validator._MAX_SLUG_LEN` without importing it**
`src/gateway/research/orchestrator.py:1424`

The constant is defined with the comment "must match validator._MAX_SLUG_LEN" — a hand-maintained invariant that will silently drift if the validator limit ever changes. The fix is to import `_MAX_SLUG_LEN` from `validator.py` directly rather than duplicating the value. Currently a latent correctness risk rather than an active bug.

**[Medium] Degenerate truncation path in `_bounded_synthesis_slug` is untested**
`src/gateway/research/orchestrator.py:1443` (`return combined[:_MAX_SYNTHESIS_SLUG]`)

The `available < 4` branch (session_id itself is near 80 chars) has no test. Reachable only with a pathologically long session_id — `make_session_id` caps at 6 words so the real maximum is ~60 chars — but the untested branch is a reliability gap if session ID generation changes. A single unit test with a 77-char session_id would cover it.

**[Medium] `_bounded_synthesis_slug` unit test uses a synthetic 61-char session_id that can't occur in practice**
`tests/gateway/test_research_orchestrator.py:test_bounded_synthesis_slug_trims_suffix_to_fit`

`"2026-05-28-" + "a" * 50` is 61 chars — impossible from `make_session_id` (6 words, max ~50 chars in practice). The real offending case (49 chars) is only exercised end-to-end via `test_branch_synthesis_slug_bounded_for_long_session_id`. Swapping the unit test to use the actual failing session_id (`2026-05-28-multi-user-gcp-deployment-patterns-for`) ties the unit test to the real failure rather than a synthetic one.

**[Medium] `synthesizes:` back-references in cross-cutting page could diverge from branch slugs if truncation is asymmetric**
`src/gateway/research/orchestrator.py:598`

`_bounded_synthesis_slug` is called in both `_make_branch_synthesis_update` (to name the file and set `slug:`) and `_make_cross_cutting_update` (to build the `synthesizes:` list). Because both calls use the same function with identical arguments, the slugs will match. But there is no test asserting that the cross-cutting `synthesizes:` entries actually match the branch page slugs produced — a regression could silently break the bidirectional link. A single integration test covering this would close the gap.

**[Low] YouTube throttle `test_search_no_sleep_on_first_call` has an implicit wall-clock dependency**
`tests/test_research_adapter_youtube.py:test_search_no_sleep_on_first_call`

The test doesn't mock `time.monotonic`. It relies on the real monotonic clock returning a value much larger than 0.0 (which it always will in practice, since monotonic measures uptime). Technically correct but fragile framing — a reader unfamiliar with the implementation has to reason about wall-clock behavior to understand why the first call skips sleep. Mocking monotonic to return `[100.0, 100.0]` (as the other two throttle tests do) would make the intent self-documenting.

---

## § 2 — Token efficiency

**Three R3 research runs burned daily YouTube API quota before the query strategy was validated**

Run 1 failed on slug-too-long (purely a gateway bug, no adapter calls needed to diagnose). Runs 2 and 3 burned ~4,000 YouTube quota units to discover that the query strategy was correct but transient infrastructure (Firecrawl 502, YouTube 429/403) blocked results. The third run exhausted the daily quota, making same-day verification impossible. The inefficiency: the slug-too-long fix required creating a new YAML file (2 tool calls) but led to an immediate re-run that consumed scarce quota. A `--dry-run` pass after fixing the plan would have validated the query plan shape without touching any adapter.

Estimated excess: ~2 wasted adapter fan-outs × ~20 YouTube search calls = 2,000 units of irreplaceable daily quota.

**PR merge took 6 tool calls due to predictable divergent-history conflict**

The feature branch was created after committing to main (`git checkout -b ... && git cherry-pick`), which produced an empty cherry-pick since the commit was already on the branch. The subsequent `git pull` → rebase → conflict → abort → stash → merge → conflict resolve cycle used 6 tool calls. Creating the branch before the first commit would have eliminated this entirely.

**Two sequential partial reads of `orchestrator.py` where one would have done**

`offset=505, limit=80` then `offset=580, limit=40` — these cover a contiguous 115-line window. Issuing both as a single `offset=505, limit=115` read would have saved one tool call and kept the full context together for reasoning.

**Three watcher-driven `chore(log)` commits cluttered the history**

The wiki watcher continuously writes `log.md`. Between commit attempts during the PR merge, log.md was modified three times, producing three noise commits (`85e9fd9`, `34b6381`, `09db002`). Stashing at the start of any merge/rebase flow (before touching git) would have avoided this pattern entirely.

---

## § 3 — Prompt and context engineering

**R3 research prompt was written without reading the domain policy first**

The initial R3 prompt was framed around infrastructure ("Cloud Run vs GKE", "Firebase Auth / Identity Platform", "OAuth 2.0 + PKCE") with no explicit MarTech grounding. The orita-cmo policy's 5th inclusion criterion explicitly requires content "in a marketing or sales-operations context" — visible in `.knowledge/policies/orita-cmo/policy.yaml`. The policy was not read before the prompt was drafted. Result: the filter correctly rejected all candidates on the first run. The fix (reframing queries to tie each infrastructure topic to a marketing/RevOps use case) was sound, but required a full run + diagnosis round to discover a mismatch that a policy-first read would have caught in advance.

Pattern to establish: for any `wiki research` prompt targeting an established domain, read the policy's `inclusion_criteria` and `exclusion_criteria` before drafting the prompt, and verify each adapter query explicitly satisfies at least one criterion.

**iOS Shortcut diagnosis was reactive; the root cause was predictable**

The "invalid HTTP request" error from Shortcuts is a client-side construction error, not a server error — this distinction was not established early enough. The diagnostic loop ran six rounds before arriving at "Shortcut Input is nil when triggered from inside the app." This was predictable: iOS Shortcuts' `Shortcut Input` is only populated from a Share Sheet context, not from in-app execution. Stating this upfront ("always test via Share Sheet, never from inside the app") would have saved several back-and-forth rounds.

Additionally, `scripts/test-ingest-curl.sh` was available and could have been used earlier to confirm the server-side was healthy before any phone-side debugging. The endpoint was confirmed working at tool-call 1 of the Shortcut session — but not until after several manual rounds had already been attempted.

**`_INTER_QUERY_SLEEP_SECONDS = 1.5` is not evidence-grounded**

The value was chosen as a round number that "should be fine" given 20 queries × 1.5s = 30s. YouTube's per-minute quota is not publicly documented as a per-query-per-second limit — the actual constraint is daily units (100 per `search.list` call, 10,000 units/day). The throttle addresses per-minute rate limiting but the session's actual quota failures were daily exhaustion (403), which 1.5s spacing doesn't help. The constant's value should either be documented as "tunable, not empirically validated" or grounded in a specific rate observed and logged.

**Branch-before-commit discipline was not applied**

The implementation pattern was: commit to main → create PR branch → cherry-pick → discover empty cherry-pick → rebase. The correct pattern (branch → commit → push → PR) was known but not applied. This isn't a prompt engineering issue per se, but it represents a procedural gap that generated avoidable tool-call overhead and merge complexity.

---

## Priority table

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | Code | `_MAX_SYNTHESIS_SLUG` duplicates validator constant | Import `_MAX_SLUG_LEN` from `validator.py` instead of re-declaring |
| 2 | Prompt | Domain policy not read before drafting `wiki research` prompt | Add "read inclusion_criteria before prompt" to research workflow; enforce in session-state checklist |
| 3 | Token | R3 re-runs burned daily YouTube quota before strategy was validated | Use `--dry-run` after any plan edit before executing; treat YouTube quota as a scarce daily budget |
| 4 | Code | `synthesizes:` cross-cutting ↔ branch slug consistency untested | Add integration test asserting cross-cutting `synthesizes:` entries match branch page slugs |
| 5 | Token | Branch-after-commit pattern generated 6-call merge cleanup | Always `git checkout -b <branch>` before the first commit on any PR-bound work |
