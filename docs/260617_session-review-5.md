# Session review — 2026-06-17 (semantic-models streams 3+4 + YouTube transcript recovery + git reconciliation)

Scope: applied the improved YouTube protocol, ran research streams 3 & 4, built a YouTube
transcript-cache seam (TDD), recovered 25 transcripts, shipped to `origin/main` via PR #20,
then reconciled and cleaned up a shared-tree git tangle. Read-only review.

Session commits (now on `origin/main`): `fd2acd09` (cache seam), `23037bb2` (streams 3+4 corpus),
`6f6c9a33` (session-state). Merged via PR #20 → `a7f4275e`.

---

## § 1 — Code and coding quality

**[High] `wiki research` NLM-synthesis output is not finalize-compatible — a whole-workflow defect (existing code, discovered this session).**
`src/gateway/citations.py` `uncited_claims()` + `_STRUCTURAL_FRAME_LABEL_RE` (~line 110) and
`src/gateway/data/citations_allowlist.yaml`. NLM emits structural labels as
`*   **Name and Key Claim**: X` (title-case, colon *outside* the bold, bullet-prefixed), but the
regex expects `**Label:** ` and the allowlist has lowercase `"Name and key claim"` — so they're
flagged as uncited claims. Separately, the aggregate-opener exemption ("Based on the provided
sources…") is gated on `synthesizes:` frontmatter that `wiki research` pages don't carry. Net:
every research-synthesis page is un-finalizable, even though its substantive bullets *are* grounded
via footnote refs (`[N]` + `[^N]: [[sources/id]]`, which the validator accepts). **Fix:** scoped
TDD change to `citations.py` (match the bulleted `**X**:` label form; ungate aggregate openers for
synthesizes-less pages) + `cite-add` the ~15 genuinely uncited cross-cutting prose sentences. This
fixes all future syntheses, not just the 12 drafts left `draft: true` this session. Already logged
in `docs/session-state.md` with the trigger.

**[Medium] Cache-seam test gaps.** `tests/gateway/test_converters_youtube_cache.py` covers txt-plain,
txt-interleaved-timestamps, vtt, cache-hit-skips-network, fallthrough, and none-when-absent (6 tests,
good). Untested: (a) `_parse_vtt_transcript` rolling-duplicate dedup, (b) `.vtt` preferred over `.txt`
when both exist, (c) empty/whitespace cache file → `None` → network fallthrough. Add 3 tests.

**[Low] `_parse_txt_transcript` timestamp/content ambiguity.** `src/gateway/converters/youtube.py` —
a content line that is exactly a bare timestamp (`"1:30"`) is consumed as a timestamp marker, not
text. And `_parse_vtt_transcript` drops any line where `line.isdigit()` (cue-index skip), so a
transcript line that is purely a number (`"2024"`) is dropped. Both negligible for ASR auto-captions;
note only.

**[Low] `_vtt_time_to_seconds` silent 0.0 fallback.** Malformed VTT timestamps map to start 0 with no
warning. Acceptable degradation; flag for awareness.

**Positive (checked, clean):** `_fetch_transcript` preserved as the pure API path / monkeypatch target
(existing tests untouched); `convert()` wiring is minimal; `caption_track` now records provenance
(`cached`/`fetched`); matches existing converter conventions; cache dir gitignored; TDD RED→GREEN
followed (6 RED then GREEN, converter regression green). The 311-file corpus commit is generated
markdown — synthesis pages correctly carry `draft: true`.

---

## § 2 — Token efficiency

**[High] Self-inflicted git-reconciliation arc.** The largest token sink was the cherry-pick that
assumed `4bcf938f` was a foreign concurrent branch and skipped it — which diverged local `main` from
`origin/main` (4 ahead / 2 behind) and triggered a multi-turn survey → PR → cleanup → branch-rename
sequence. One `git fetch origin && git log --oneline origin/main` *before* reconciling would have
shown `4bcf938f` was the user's own merged PR #19. Estimated excess: ~10–15 tool calls + ~4–5
conversation turns of survey/repair that the work itself did not require.

**[Medium] Redundant IP-block confirmation probe.** After yt-dlp's no-cookies attempt returned a clear
HTTP 429 (IP-level block proven), the follow-up `--cookies-from-browser` probe added marginal
information and then hung on the keychain, requiring a `pkill`. ~2 tool calls + a stuck background
task. The first 429 was conclusive; the cookies probe was skippable.

**[Low] Overlapping `git status` / `git branch` surveys.** Several read-only branch/status checks. Most
were justified — the shared working tree was branch-switched *twice* mid-session by other sessions, so
re-verifying state was correct discipline — but a couple were re-confirmations of unchanged state.

**Positive (checked):** Good upfront batching (session-state + plan + youtube adapter read together);
streams run in background with a single completion-wait rather than busy-polling; the 45KB stream log
was handled via the persisted-output file instead of re-dumping; `wiki finalize` was probed on one page
before concluding rather than attempting all 12.

---

## § 3 — Prompt and context engineering

**[High] Assumption-inheritance / framing drift caused the §2 waste.** The "`4bcf938f` = concurrent
session's refactor branch" label was carried from an *earlier* session-state note and acted on (a
history-rewriting cherry-pick) without verification against `origin`. It was the user's PR #19. This is
classic surface-anchor leakage: a prior-context label treated as ground truth. Encoded as durable
fixes: new memory `feedback_defer_to_git_best_practices` + extended
`feedback_verify_branch_before_commit_shared_tree` (rule: verify shared-tree/branch assumptions against
`origin` before any history operation; prefer push-branch+PR over local surgery).

**[Medium] Context-seeding done right on finalize (the counter-example).** Before advising defer-vs-fix,
`validator.py` + `citations.py` + `citations_allowlist.yaml` were read first — so the diagnosis (footnote
refs are accepted; the blockers are format-mismatch + synthesizes-gating) was correct on the first pass.
Where context was seeded before the call, the output needed no correction; where it wasn't (the git
assumption), it caused rework. Same session, both sides of the lesson.

**[Medium] AskUserQuestion used well for genuine forks.** YouTube recovery path, commit grouping, and
finalize path each had real trade-offs the user needed to own (esp. given the protected backlog and the
user's stated non-expertise in git). Framing was decision-bearing, not busywork.

**Positive (checked):** YouTube query-register rewrite deliberately avoided tutorial-register
surface-anchor leakage (conference/lecture register); the oembed title-fetch and cache-seam TDD prompts
were precise and worked first try; durable lessons captured to memory rather than left in chat.

---

## § 4 — Session-state checkpoint

- **Workstream status:** COMPLETE and shipped. Semantic-models research loop (streams 1–4), improved
  YouTube protocol (policy `channel_authority`/`speaker_expertise` signals + conference/lecture query
  register), transcript-cache seam, and 25 recovered transcripts are all merged to `origin/main` via
  **PR #20 → `a7f4275e`**.
- **Branch topology (verified clean):** `main` = `origin/main` (0/0). `wip/condo-orita-restore` =
  current working tree, holds other-projects' WIP (condo/orita/quebec, ~227 files vs main) restored from
  the pre-cleanup snapshot. `keep/local-main-20260617` preserves the parallel session's unpushed
  `89a63954` (acceptance-gate contp doc) — not yet on origin.
- **Decisions:** (1) YouTube protocol gaps fixed by hand-editing policy + plan YAMLs, not regenerating
  (avoids re-adding pubmed/broad queries). (2) Transcripts landed in local RAG layer only; NLM syntheses
  NOT regenerated (rough ASR > confabulation risk). (3) Finalize DEFERRED — gateway-fix-gated. (4) Git
  reconciled via push-branch+PR, not local rebase/reset (user defers to git best practices). (5) Cleanup
  done via temp worktree / pointer ops; backups kept.
- **Rejected:** local cherry-pick reconciliation (caused the divergence); deleting the `backup/`+`keep/`
  branches (they hold the only copies of other-project WIP + a parallel unpushed commit — must persist).
- **Current system state working:** `main` clean and pushed; converter suite green (cache seam 6 tests +
  64 regression). Known-deferred: 12 synthesis drafts stay `draft: true` until the gateway finalize fix.
- **Next atomic step (when triggered):** implement the gateway finalize-compat fix in
  `src/gateway/citations.py` (TDD) per § 1 High, then finalize the 12 S3/S4 drafts. Independent thread:
  resume condo/orita work on `wip/condo-orita-restore`; the parallel session decides whether to push
  `keep/local-main-20260617`'s `89a63954`.

---

## Priority table

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | §1 High | `wiki research` syntheses are un-finalizable (citations.py format mismatch + synthesizes-gating) | Scoped TDD fix in `citations.py` + allowlist; then finalize the 12 drafts. Unblocks the whole research→finalize path. |
| 2 | §3 High | Acted on an inherited "foreign branch" assumption without checking `origin` → diverged `main` | Always `git fetch` + check `origin/main` before any history op; prefer push-branch+PR. Encoded in memory — verify it sticks next shared-tree session. |
| 3 | §1 Med | Cache-seam test gaps (vtt dedup, vtt>txt precedence, empty-file fallthrough) | Add 3 tests to `test_converters_youtube_cache.py`. |
| 4 | §2 Med | Redundant confirmation probe (yt-dlp cookies after a conclusive 429) | Stop at the first conclusive result; skip belt-and-suspenders probes that can hang. |
