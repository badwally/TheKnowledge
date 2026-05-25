# Session state — 2026-05-25

Last updated: 2026-05-25 (Phase 1 Round B, post-TOK-6)

---

## Open contracts

- TOK-7 not yet implemented: `assert_safe_for_prompt()` guard in `paths.py`, module-level warnings in `log.py` and `index.py`, CLAUDE.md rule already added, tests, commit as `perf(tok-7)`. Branch `phase1-round-b`.

---

## Files mid-edit

None — TOK-7 was interrupted before any edits were made.

---

## Decisions made this session

- M52 Phase 1 Round A complete: ARCH-2, ARCH-4, ARCH-6, QUAL-4, QUAL-5. 985 → 1020 tests. Merged to main as `a6b8f05`.
- Round B branch `phase1-round-b` created off main post-M52.
- TOK-1: `cache_read=0` diagnosed as 60-token system prompt below 1024-token floor; M50.1 (`7ad5996`) already fixed it by moving wiki_context to `user_prompt_prefix`. No code change needed; doc at `docs/M52-tok1-cache-diagnosis.md`.
- TOK-3: `build_system_prompt()` now called once per `_run_filter` batch via `_build_filter_system_prompt` pre-computed before ThreadPoolExecutor. `_prebuilt_system` param added to `semantic.score()`.
- TOK-6: transcription cache at `raw/<type>/_transcripts/<sha256hex>.json`. `TranscriptionResult.from_dict()` added. Voice and audiobook converters check cache before calling mlx-whisper.
- Test count post-TOK-6: 1024 passing.

---

## Rejected approaches this session

- TOK-3: monkeypatching `semantic.build_system_prompt` to count calls in the orchestrator test — fails because `_build_filter_system_prompt` is bound at import time; must patch `orch._build_filter_system_prompt` instead.
- TOK-6: adding cache helpers to a new `converters/_transcript_cache.py` — skipped; added to `transcription.py` instead since that's where `TranscriptionResult` lives.

---

## Next atomic step

Implement TOK-7 on branch `phase1-round-b`:
1. Add `PromptGuardError` + `assert_safe_for_prompt(path)` to `src/gateway/paths.py` — raises if `path` resolves to `log.md` or `index.md`.
2. Add module-level docstring warning to `src/gateway/log.py` and `src/gateway/index.py`.
3. Write 3 tests in `tests/gateway/test_log_and_locking.py`: guard raises for log.md, raises for index.md, passes for a wiki page.
4. Commit as `perf(tok-7): assert_safe_for_prompt guard for log.md and index.md`.
5. Then: full pytest -x (expect 1027 passing), write M53 milestone doc, update BUILD.md, tag `m53-phase1-round-b`, merge to main.
