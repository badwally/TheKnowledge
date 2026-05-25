# Session state — 2026-05-25

Last updated: 2026-05-25 (Phase 1 Round B, post-M53, merged to main)

---

## Open contracts

None. Phase 1 Round B is complete and merged.

---

## Files mid-edit

None.

---

## Decisions made this session

- M52 Phase 1 Round A complete: ARCH-2, ARCH-4, ARCH-6, QUAL-4, QUAL-5. 985 → 1020 tests. Merged to main as `a6b8f05`.
- Round B branch `phase1-round-b` created off main post-M52.
- TOK-1: `cache_read=0` diagnosed as 60-token system prompt below 1024-token floor; M50.1 (`7ad5996`) already fixed it by moving wiki_context to `user_prompt_prefix`. No code change needed; doc at `docs/M52-tok1-cache-diagnosis.md`.
- TOK-3: `build_system_prompt()` now called once per `_run_filter` batch via `_build_filter_system_prompt` pre-computed before ThreadPoolExecutor. `_prebuilt_system` param added to `semantic.score()`.
- TOK-6: transcription cache at `raw/<type>/_transcripts/<sha256hex>.json`. `TranscriptionResult.from_dict()` added. Voice and audiobook converters check cache before calling mlx-whisper.
- TOK-7: `PromptGuardError` + `assert_safe_for_prompt(path)` added to `paths.py`. Raises for `log.md` or `index.md`. 3 tests.
- M53 tagged `m53-phase1-round-b`, merged to main. 1027 tests passing.
- Session-state discipline infrastructure: `docs/session-state.md`, PreCompact/SessionStart hooks, CLAUDE.md rule.

---

## Rejected approaches this session

- TOK-3: monkeypatching `semantic.build_system_prompt` to count calls in the orchestrator test — fails because `_build_filter_system_prompt` is bound at import time; must patch `orch._build_filter_system_prompt` instead.
- TOK-6: adding cache helpers to a new `converters/_transcript_cache.py` — skipped; added to `transcription.py` instead since that's where `TranscriptionResult` lives.

---

## Pending / known issues

- `.claude/settings.json` hook format still wrong (`matcher+hooks` wrapper missing). User must apply manually — hard block on self-modification. Current file has flat `[{"type": "command", ...}]` instead of `[{"matcher": "", "hooks": [{"type": "command", ...}]}]`.

---

## Next atomic step

Phase 1 Round C (multi-model routing) — not yet planned. Await user direction.
