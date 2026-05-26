# Session state — 2026-05-26

Last updated: 2026-05-26 (M65 complete; Phase 4 Round A merged)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- `ANTHROPIC_API_KEY_RESEARCH` needed for condo-capital-infra and edge-ai-agentic eval runs.
- ai-native-business goldens context too large (607K > 500K budget).
- ONT-11 backfill: 56/94 synthesis pages lack `synthesizes:` — lint warns; escalate to error after backfill pass.
- WIKI.md § 9 should document the hard-rule-1 write invariant explicitly (deferred from ARCH-14).

---

## Files mid-edit

None.

---

## Decisions made this session

- M65: QUAL-9 + AGT-6 + AGT-12 all clean.
- ARCH-14 caught `briefing_cron.py` using `.write_text()` with `raw_dir()` — fixed by using `write_atomic` for the hash store.
- AGT-6 test patching: local `from ... import nlm_briefing` inside function requires patching `gateway.ops.nlm.nlm_briefing` not `gateway.ops.briefing_cron.nlm_briefing`.
- `briefing-cron` added to MCP `CLI_ONLY` (agents must not trigger corpus-wide NLM runs).
- Skills live at `.claude/skills/<name>/SKILL.md` following ai-tutor pattern.

---

## Rejected approaches this session

- Patching `gateway.ops.briefing_cron.nlm_briefing`: doesn't exist at module level (local import). Must patch source module.

---

## Next atomic step

M66 — Phase 4 Round B. Create `phase4-round-b` branch. Read docs/reviews/2026-05-23-knowledge-system-review.md § QUAL-1 and § AGT-4 before writing any code. QUAL-1 (link-rot poller + lint) first, then AGT-4 (contradiction sweeper). For AGT-4: check if NLM client is available before designing — if not, use wiki context + LLM judge instead.
