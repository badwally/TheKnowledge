# Continuation prompt — YouTube-fix acceptance-gate re-run

Paste the block below into a fresh session (after `/clear`) once BOTH the YouTube API and the semantic_scholar key are idle (≥24h from 2026-06-17). Confirmation re-run only — the fix and all follow-ups are already merged to `main`.

```
Re-run the YouTube-fix acceptance gate for the agentic-data-layer (or semantic-models) research domain in ~/code/knowledge — a confirmation re-run only, gated on the YouTube API + semantic_scholar key both being idle.

Read first (re-anchor):
- docs/session-state.md — the top block "✅ AGENTIC-DATA-LAYER DOMAIN + YOUTUBE-AWARE FILTER (2026-06-17)", specifically line 18 (the acceptance gate that PASSED 2026-06-17: 230 candidates → 77 accepted, 31 YouTube sources materialized, 3 cited with full transcripts). That line IS the success baseline to reproduce.
- docs/plans/2026-06-17-youtube-aware-filter.md — for the filter-fix shape under test.
- git show a4b11ac2 — the merged YouTube-aware-filter fix being validated.

Objective: prove the fix still lands authoritative YouTube talks in `accepted` (not 0) on a fresh YouTube-heavy run. This is acceptance confirmation, not new research and not a redo — the fix and all follow-ups are already merged to main.

Next atomic step:
1. Confirm BOTH gates are clear before any execution: (a) YouTube API not rate-limited (it was overwhelmed by a parallel session on 2026-06-17 and may be timed out 24h), (b) the shared semantic_scholar key is idle (no parallel research run — see memory feedback_s2_shared_key_concurrency; concurrent runs 429 at ~1 req/s). If either is busy, STOP and wait — do not run.
2. Run a YouTube-heavy research plan in a video-drawing domain (agentic-data-layer or semantic-models). Check `step=corpus_quality`, `step=index_settle` (distinct_sources should be ~20, not 1–2), and the accepted-rate.
3. PASS = authoritative talks (Stanford/NeurIPS/KGC/conference keynotes) appear in `accepted` and YouTube sources materialize with full transcripts; acceptance rate in the ~30% range, not ~11%. Record the result in docs/session-state.md line 18's block (append a second-run note) and stop.

Constraints / gotchas (do NOT re-break):
- ALWAYS .venv/bin/python and .venv/bin/wiki — never system python.
- The working tree holds a parallel semantic-models session's uncommitted files (.knowledge/policies/semantic-models/, ~35 raw/youtube/yt-*.md, wiki/mocs/semantic-models.md, a synthesis page, plans). NOT yours — never `git add -A`/`git add -u`; stage only your own files by explicit pathspec. Per session-state "Do NOT touch."
- This is a single confirmation run, not a /loop. If it passes, it's done — a third run adds nothing.
- No direct writes to wiki/ or raw/ (gateway only). session-state.md is the one file you may edit directly (to append the result).

If the prior acceptance-gate result (line 18) already satisfies you on re-read, the correct action may be to skip the re-run entirely — evaluate before spending API budget.
```

Deliberately left out: the per-task TDD history and the merged-branch list — both live in `docs/session-state.md` and reload via the SessionStart hook.
