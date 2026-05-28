# Session state — 2026-05-28

Last updated: 2026-05-28 (Phase 12 complete — M111+M112, 1862 tests)

---

## Open contracts

None.

Carry-forward:
- **ANTHROPIC_API_KEY_RESEARCH**: must be set in shell for edge-ai-agentic and glp1-reward-modulation eval runs. See RUNBOOK.md § Evaluation failures for setup instructions. Once set, `wiki evaluate --all-domains` will run cleanly for all four domains.
- **finalize-batch escalated**: 379 escalated drafts (uncited claims). `--suggest` unblocked once API key is set.
- **schema-drift**: 208 remaining (legacy editorial tail — entity_kind, slug, canonical_name — human judgment).
- **orphans**: 531 wiki-page orphans. discharge-orphans now auto-commits; next run on any domain will be clean.
- **INT-18/INT-19 hand-tests**: deferred (live tokens required).
- `wiki migrate` stub remains.

---

## Files mid-edit

None. 1862 tests passing. Phase 12 exit checkpoint in BUILD.md § 26.

---

## Decisions made this session

- Phase 12: M111 (discharge-orphans auto-commit), M112 (eval context budget 500k→750k + RUNBOOK docs).
- 55 uncommitted condo synthesis pages from prior session committed — all were draft: true, no synthesizes: field, zero gateway-unresolved claims.
- synthesizes-coverage=74 is ALL WARNINGs (correct M104 behavior for drafts). The `synthesizes-included-works-drift` ERRORs in the prior lint run were in schema-drift scope — pre-existing legacy pages, not a regression.
- `discharge_orphans` limit enforcement and synthesis prompt were already fixed in M110.
- Eval context budget raised to 750k to match the evaluate-weekly cron (M101 raised it there but left the CLI default at 500k — that inconsistency is now fixed).

---

## Next atomic step

Phase 13 gate: user sets `export ANTHROPIC_API_KEY_RESEARCH=sk-ant-...` in shell, then:
1. `wiki evaluate --all-domains` → confirm all 4 domains score cleanly
2. `wiki finalize-batch --suggest --execute` → attempt citation auto-fill on 379 escalated drafts
3. Run `wiki routine discharge-orphans --domain <domain> --limit 20` on any domain — auto-commit now works
