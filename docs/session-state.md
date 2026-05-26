# Session state — 2026-05-26

Last updated: 2026-05-26 (M64 complete; Phase 4 scoped)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- `ANTHROPIC_API_KEY_RESEARCH` needed for condo-capital-infra and edge-ai-agentic eval runs.
- ai-native-business goldens context too large (607K > 500K budget).
- ONT-11 backfill: 56/94 synthesis pages lack `synthesizes:` — lint now warns; escalate to error after backfill pass.
- WIKI.md § 9 should document the hard-rule-1 write invariant explicitly (deferred from ARCH-14).

---

## Files mid-edit

None.

---

## Decisions made this session

- M63: INT-13 (wiki agenda) + INT-16 (ai-tutor /wiki-cards). Calendar MCP two-step: agent fetches events then passes to wiki_agenda().
- M64: ARCH-14 + ONT-11 + QUAL-13. Found and fixed real hard-rule-1 violation in ops/contradiction.py (two write_text calls → write_atomic).
- ONT-8 already implemented (validator.py lines 273-337). Skipped to avoid duplicate work.
- Phase 4 scope defined: QUAL-9, AGT-6, AGT-12 (Round A); QUAL-1, AGT-4 (Round B); TOOL-14, INT-12 (Round C).
- Phase 4 model routing: Sonnet (pattern-bound work; Phase 3 failures were verify-before-act gaps, not reasoning gaps).
- Backlog rubric: 4 dimensions — operational leverage, automation factor, effort gate, dependency status.

---

## Rejected approaches this session

- Opus for Phase 4: pattern-bound work, Sonnet sufficient; failure modes were "verify before act" not capability.
- ONT-8 (slug cap 80): already implemented in validator.py lines 273-337.
- ARCH-15 (schema_version: 1): impact 2, chose higher-impact items first.
- Calling Calendar MCP from within wiki_agenda.py Python: MCP tools can't call other MCP tools from Python.

---

## Next atomic step

M65 — Phase 4 Round A. Create `phase4-round-a` branch. Read docs/reviews/2026-05-23-knowledge-system-review.md § QUAL-9 and src/gateway/ops/promote_domain.py before writing any code. Implement QUAL-9 (promote-domain contamination quarantine, S effort) first, then AGT-6, then AGT-12.
