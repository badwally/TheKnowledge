# Phase 1 Closeout

**Date:** 2026-05-25
**Milestones:** M47–M54
**Baseline:** `docs/reviews/2026-05-23-knowledge-system-review.md § 14 Phase 1 table`

Phase 1 delivered all 18 items from the planning table, plus three items pulled forward from Phase 2 and Phase 3. Test count grew from ~793 (pre-M47 baseline) to 1038 (+245 net across eight milestones).

---

## Completed items vs planning table

| Planning ID | Title | Milestone | Notes |
|---|---|---|---|
| K1 / ARCH-5 + AGT-10 | Gateway edit-path: `wiki cite-add` + `wiki edit --section` | M48 | |
| K2 / ARCH-7 + AGT-11 + TOOL-1 | MCP-CLI parity sweep | M47 | 4/4 parity test green throughout |
| K3 / TOOL-2 + TOOL-3 | Tailscale + `wiki serve` + iOS Shortcut | M48 | |
| K4 / TOOL-7 | Scheduled-jobs substrate | M48 | |
| K5 / TOK-2 | Token telemetry (per-call usage to log.md) | M47 | |
| ARCH-1 | Lock `log.md` and `index.md` writes | M47 side-effect | |
| ARCH-2 | Validator-enforce frontmatter mutation allowlist | M52 | |
| ARCH-4 | Research orchestrator per-source lock + filter writeback | M52 | |
| ARCH-6 | `register_session` idempotency | M52 | |
| QUAL-4 | Validate non-source wikilink targets | M52 | |
| QUAL-5 | Per-domain fine-tune readiness in `wiki status` | M52 | |
| TOK-1 | Diagnose `cache_read=0` / decide API-key path | M53 (doc) + M50.1 (fix) | Root cause: 60-token system prompt below 1024-token floor. Fix already shipped M50.1; billing decision (separate API key, $50/month cap) made prior to Phase 1 execution. |
| TOK-3 | Memoize filter system-prompt build | M53 | |
| TOK-6 | Transcription cache | M53 | |
| TOK-7 | "Don't load log.md/index.md" guard | M53 | |
| TOOL-10 | Shell completion + `--help` examples | M54 | |
| DOC-1 | "New here?" reading order in README | M54 | |
| DOC-6 | GLOSSARY.md | M54 | |

**Items pulled forward from Phase 2/3 (delivered early):**

| Planning ID | Title | Milestone |
|---|---|---|
| QUAL-12 | Eval framework (golden sets, `wiki evaluate`, LLM-as-judge) | M50 |
| QUAL-2 + ARCH-11 | Draft-debt batch finalizer + per-domain cap | M49 |
| INT-11 | `wiki context` read-side op | M51 |

---

## Test delta by milestone

| Milestone | Description | Tests |
|---|---|---|
| Pre-M47 | Baseline | ~793 |
| M47 | MCP-CLI parity, token telemetry, log lock | ~830 |
| M48 | K1–K4 keystones | ~870 |
| M49 | AnthropicAPIClient, draft batch closer | ~900 |
| M50 | Eval framework, filter fine-tune loop | ~977 |
| M50.1 | cache_control on wiki_context judge block | ~977 |
| M51 | `wiki context` INT-11 | 985 |
| M52 | Phase 1 Round A (ARCH-2/4/6, QUAL-4/5) | 1020 |
| M53 | Phase 1 Round B (TOK-1/3/6/7) | 1027 |
| M54 | Phase 1 Round C (TOOL-10, DOC-1/6) | 1038 |

---

## Verification (Section 8 protocol)

**`pytest -x`:** 1038 passing, 0 skipped.

**`wiki lint`:** All scopes active including `broken-wikilinks` (QUAL-4, M52) and `idempotency` (ARCH-6, M52). No new errors vs pre-Phase-1 baseline in non-generated content.

**`wiki status`:** Fine-tune readiness block present (QUAL-5). Evaluation scores block present (M50). LLM-usage block present (K5/M47).

**K2 parity test:** `pytest tests/gateway/test_mcp_parity.py` — 4/4 green at M54 merge.

**`git grep -n "write_text" src/gateway/`:** All results are either inside the gateway's atomic-write helper or allowlisted non-`wiki/raw/` paths. ARCH-14 (not in scope) remains clean.

**Phase 1 table:** 18 of 18 items done. TOK-1 is the one the planning doc marked as "billing decision + engineering": billing decision made (separate API key, $50/month cap), code fix shipped M50.1, diagnosis doc in M53.

**Session-state diff:** `docs/session-state.md` recorded "Phase 1 Round C next" before this closeout. Actual state: M54 tagged, merged to main, 1038 tests. No disagreement.

---

## Infrastructure delivered alongside Phase 1

- **Session-state discipline** (`docs/session-state.md`, PreCompact/SessionStart hooks, CLAUDE.md rule) — M53 branch, `a24d9b5`.
- **Correct hook format** in `.claude/settings.json` — post-M54 fix.
- **TOK-1 diagnosis doc** at `docs/M52-tok1-cache-diagnosis.md`.

---

## Follow-ups for Phase 2

Items from the Phase 1 table that were explicitly deferred:
- TOK-1 billing path: separate API key is active; monitor cache_creation vs cache_read ratio in the first 30-day window.
- ARCH-14 (CI grep enforcing gateway-write discipline) — not in Phase 1 scope, still clean by grep.
- All Phase 2 items from `docs/reviews/2026-05-23-knowledge-system-review.md § 14 Phase 2` remain.
- § 15 open decisions (ONT-10, Track B wedge vertical, hard-rule enforcement posture) remain user-gated.
