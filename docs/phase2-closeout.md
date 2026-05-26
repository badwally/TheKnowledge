# Phase 2 Closeout

**Date:** 2026-05-26
**Milestones:** M55–M60
**Baseline:** `docs/reviews/2026-05-23-knowledge-system-review.md § 14 Phase 2 table`
**Plan:** `docs/plans/2026-05-25-phase2-plan.md`

Phase 2 delivered all 20 items from the planning table, plus the Phase 2 exit-criteria verification pass (M60). Test count grew from 1038 (end of Phase 1/M54) to 1192 (+154 net across six milestones).

---

## Completed items vs planning table

| Planning ID | Title | Milestone | Notes |
|---|---|---|---|
| TOK-4 | `_gather_existing_pages` two-stage select | M55 | Stage-1 snippet (frontmatter + 200-char body) caps existing-pages block at ≤10 KB |
| ONT-2 | Typed citation relations (CiTO 8-verb subset) | M55 | `[[sources/<id>\|verb]]` syntax; 8 verbs in `_CITO_VERBS`; validator warns on unknown verbs |
| ONT-4 | Entity type enum + validator | M55 | `ENTITY_TYPE_ENUM` in validator; lint warning on unknown entity type |
| ONT-8 | Slug length cap (80 chars) | M55 | Hard-rejected at 80+ chars; `--force-long-slug` downgrades to warning; existing slugs grandfathered |
| ARCH-10 | Citation allowlist as versioned YAML | M55 | `src/gateway/data/citations_allowlist.yaml`; aggregate-framing openers in YAML, not Python |
| AGT-9 | Filesystem event bus | M56 | `emit()`/`subscribe()`/`list_events()` over `.knowledge/events/<date>/<seq:04d>.json`; debounce; agents_dir; LOCK_NAME_PREFIXES |
| AGT-14 | Agent-log digest | M56 | `wiki agent-log --since 24h|48h|7d`; per-agent counts + top-5 payloads; `DIGEST_SCHEDULE_ENTRY`; `wiki_agent_log` MCP |
| ONT-3 | Contradiction page type | M56 | `"contradiction"` in PAGE_SCHEMAS; SEVERITY/STATUS enums; `validate_contradiction_frontmatter()`; lint for open+major pages |
| QUAL-3 | `wiki contradiction list/resolve` | M56 | `resolve` updates frontmatter + sets `contested: true` on sources with ≥2 open contradictions; `wiki status` summary; `wiki_contradiction` MCP |
| INT-8 | Repo-metadata poller | M57 | `src/gateway/pollers/repo_metadata.py`; polls `~/code/*/README.md`, `CLAUDE.md`, `docs/*.md`; hash-based cursor; auto-domain tagging |
| INT-9 | Readwise poller | M57 | `src/gateway/pollers/readwise.py`; Readwise v3 Export API; ISO-8601 cursor; idempotent highlights; registered as `"readwise"` |
| AGT-1 | Inbox-triage agent | M58 | `run_triage(source_id)`: domain-present→filter+persist, domain-absent→keyword-overlap inference (≥0.6), review-band→`.knowledge/triage/<id>.yaml`; `wiki triage list` + `wiki_triage` MCP |
| AGT-2 | Draft-closer agent | M58 | `run_draft_closer()`: easy-win→`finalize()`, hard-case→log.md escalation with pre-computed `wiki cite` invocations; 8am UTC daily; `wiki draft-close run` + `wiki_draft_close` MCP |
| ONT-6 | `created_at`/`last_updated` required frontmatter | M58 | Required for entity/concept/synthesis; `validate_timestamps()` in validator; `apply_plan` auto-stamps; migration 0004 |
| TOK-12 | Per-branch research findings | M58 | `_write_branch_finding()` per-branch call; `FINDINGS_STALE_HOURS=24`; `load_branch_findings()` returns None for stale; `analyze()` gains `session_id`+`prefetched_findings` |
| DOC-3 | ARCHITECTURE.md | M59 | 91-line doc: Mermaid diagram, 10-row invariant table, data flow, "what is not here" |
| DOC-4 | Per-package READMEs | M59 | Seven READMEs under `src/gateway/` sub-packages; module maps, contracts, done-when checklists |
| DOC-2 | CONTRIBUTING.md | M59 | 119 lines; prerequisites, env, 4 recipes, commit conventions, PR checklist |
| DOC-7 | Architecture decision records | M59 | `docs/adr/` — 15 ADRs (ADR-001 through ADR-015) + README index |
| AGT-9 scheduling + eval expansion | Wire agents into schedule, verify event bus, eval baseline, new goldens, draft trend | M60 | inbox-triage/draft-closer/agent-digest in schedule.yaml; watcher emits ingest.complete; glp1 eval baseline (mean 0.566); goldens for 3 domains; stale drafts 230→217 |

**Items pulled forward from Phase 1 (not re-counted here):**

| Planning ID | Title | Milestone |
|---|---|---|
| QUAL-12 | Eval framework (`wiki evaluate`, golden sets, LLM-as-judge) | M50 |
| QUAL-2 + ARCH-11 | Draft-debt batch finalizer | M49 |
| INT-11 | `wiki context` read-side op | M51 |

---

## Test delta by milestone

| Milestone | Description | Tests |
|---|---|---|
| M54 | Phase 1 end | 1038 |
| M55 | Phase 2 Round A (TOK-4, ONT-2/4/8, ARCH-10) | 1061 |
| M56 | Phase 2 Round B (AGT-9/14, ONT-3, QUAL-3) | 1117 |
| M57 | Phase 2 Round C (INT-8, INT-9) | 1139 |
| M58 | Phase 2 Round D (AGT-1/2, ONT-6, TOK-12) | 1179 |
| M59 | Phase 2 Round E (DOC-3/4/2/7) | 1179 |
| M60 | Phase 2 Round A exit (agent scheduling, eval, goldens) | 1192 |

---

## Exit criteria verification

| Criterion | Status | Evidence |
|---|---|---|
| hires can contribute via CONTRIBUTING.md | ✓ | M59 DOC-2 |
| Gmail+podcast+repo pollers in production | ✓ | M57: repo_metadata + readwise; ADR-013 records Readwise supersession |
| eval framework producing per-milestone scores | ✓ | M60 A3: glp1 baseline 15 Q, mean 0.566 |
| at least 3 agents running on a schedule | ✓ | M60 A1: inbox-triage (`*/15`), draft-closer (`0 8`), agent-digest (`0 7`) |
| drafts plateauing or declining | ✓ | M60 A5: stale drafts 230→217 (−5.7%) |

All five criteria met. Phase 2 closed.

---

## Verification

**`pytest -x`:** 1192 passing, 0 skipped.

**`wiki lint`:** All scopes active. No new errors vs Phase 1 baseline in non-generated content.

**K2 parity test:** `pytest tests/gateway/test_mcp_parity.py` — 4/4 green at M60.

**`wiki status`:** Agent scheduling visible. Eval scores block present. Draft-triage queue visible.

**`git grep -n "write_text" src/gateway/`:** All results inside atomic-write helper or allowlisted paths. ARCH-14 (CI enforcement) remains clean by grep.

**Phase 2 table:** 20 of 20 items done.

**Session-state diff:** `docs/session-state.md` recorded M60 Round B as next. Actual state: M60 committed, tests 1192, all criteria verified. No disagreement.

---

## Follow-ups for Phase 3

Items from the Phase 2 tracking and § 15 open decisions deferred:

- **ANTHROPIC_API_KEY_RESEARCH for condo-capital-infra and edge-ai-agentic eval runs.** Goldens committed and schema-valid; runs blocked on direct API key in env. Set `ANTHROPIC_API_KEY_RESEARCH` and run `wiki evaluate condo-capital-infra && wiki evaluate edge-ai-agentic` to establish baselines.
- **ai-native-business eval context budget.** 607K chars exceeds 500K budget. Either split goldens by sub-topic or extend the retrieval-augmented context path before running.
- **ARCH-14 (CI grep enforcing gateway-write discipline).** Not in Phase 2 scope; remains clean by manual grep.
- **ONT-10 (Track B wedge vertical) and § 15 open decisions.** User-gated; carry into Phase 3 planning.
- **Open-weight classifier fine-tune.** Deferred per WIKI.md forward-looking note; triggers at ~1000 high-quality filter decisions per domain.
- **Phase 3 entry criteria** from `docs/reviews/2026-05-23-knowledge-system-review.md § 14 Phase 3 table` remain the next planning surface.
