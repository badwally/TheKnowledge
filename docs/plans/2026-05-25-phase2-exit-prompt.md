# Phase 2 Exit — Driver Prompt

**Date:** 2026-05-25
**Purpose:** Self-contained briefing to drive Phase 2 exit criteria closeout after M59. Designed to be pasted into a fresh Claude Code session (recommended model: `claude-sonnet-4-6`).
**Authoritative scope baseline:** `docs/reviews/2026-05-23-knowledge-system-review.md` § 14 Phase 2 exit criteria.
**Prior phase artifacts:** `docs/plans/2026-05-25-phase1-remainder-prompt.md` (Phase 1 driver), `docs/phase1-closeout.md` (Phase 1 summary), `docs/plans/2026-05-25-phase2-plan.md` (Phase 2 full plan).

---

You are picking up engineering work on the knowledge wiki at `~/code/knowledge`. M59 (Phase 2 Round E — ARCHITECTURE.md, per-package READMEs, CONTRIBUTING.md, 15 ADRs) is the most recent committed milestone. Phase 1 is fully complete (closeout at `docs/phase1-closeout.md`). The session-state discipline (PreCompact + SessionStart hooks, ADR-009) is active. Verify with `git log --oneline -10`, `pytest -x`, `cat docs/session-state.md` before beginning any new work. Expect ~1100+ tests passing.

## Section 1 — Canonical references (read first, in this order)

1. `docs/session-state.md` — current invariants, files mid-edit, next atomic step. Re-read if mtime newer than this session start.
2. `CLAUDE.md` — hard rules + Session-state discipline section.
3. `docs/reviews/2026-05-23-knowledge-system-review.md` — authoritative scope baseline. Specifically:
   - § 14 Phase 2 exit criteria (the line at end of Phase 2 table)
   - § 14 Phase 3 entry table (NOT in scope for this session, but read to know what you're NOT doing)
   - § 9 AGT-* findings (acceptance for AGT-1, AGT-2, AGT-9, AGT-14)
   - § 8 QUAL-* findings (acceptance for QUAL-12 expansion)
   - § 11 INT-* findings (INT-8, INT-9 — relevant for capture-coverage decision)
   - § 15 open decisions (some still gate work)
4. `docs/plans/2026-05-25-phase2-plan.md` — the Phase 2 plan as written.
5. `docs/milestones/M52.md` through `M59.md` — what's shipped and the patterns to reuse.
6. `docs/phase1-closeout.md` — phase summary, includes any open follow-ups.
7. `docs/adr/README.md` — index of 15 ADRs. **ADR-013 (Readwise over separate pollers) and ADR-009 (session-state discipline) are load-bearing for this session.**

## Section 2 — Scope (Phase 2 exit criteria closeout)

**Phase 1 status:** COMPLETE. All Phase 1 items shipped through M54. Do not re-implement; verify the suite passes and the artifacts are intact during the session-start sanity check.

**Phase 2 exit criteria from § 14 (verbatim):**

> "at least 3 agents running on a schedule, drafts plateauing or declining, eval framework producing per-milestone scores, Gmail+podcast+repo pollers in production, hires can contribute via CONTRIBUTING.md"

**Status of each clause against the M55–M59 deliverables:**

```
✓  hires can contribute via CONTRIBUTING.md  (DOC-2, M59)
✓  eval framework exists                     (QUAL-12, M50)
✓  Gmail+podcast+repo pollers                (INT-8 repo + INT-9 Readwise;
                                              user is a Readwise customer
                                              per § 15 #6; ADR-013 records
                                              the supersession decision)
◐  3 agents on a schedule
      — AGT-1 (inbox-triage), AGT-2 (draft-closer), AGT-14 (agent-log
        digest) are IMPLEMENTED at src/gateway/agents/ but their
        .knowledge/schedule.yaml registration must be verified
      — AGT-9 (event bus) is implemented; verify subscribers fire
◐  drafts plateauing or declining
      — requires measurement against the trend
◐  per-milestone scores
      — M50 ran 0.566 on glp1-reward-modulation; no post-M59 run exists
```

**Work to close:**

**Round A (M60) — agent scheduling + eval baseline + domain expansion**

- A1. Wire AGT-1, AGT-2, AGT-14 into `.knowledge/schedule.yaml`.
- A2. Verify AGT-9 event-bus subscribers fire end-to-end.
- A3. Run `wiki evaluate glp1-reward-modulation` for post-M59 baseline.
- A4. Author `goldens.yaml` for two additional domains; run evaluate.
- A5. Confirm draft trend (`wiki status` draft count vs prior runs).

**Round B (M61) — Phase 2 closeout**

- B1. Verify INT-9 (Readwise) is producing expected newsletter + podcast volume; document in closeout as ratification of ADR-013.
- B2. Translate A5's draft trend into a narrative paragraph for the closeout.
- B3. Write `docs/phase2-closeout.md` (template mirrors `phase1-closeout.md`).
- B4. Tag the commit (suggested: `m61-phase2-closeout`).
- B5. Update `docs/session-state.md` to reflect Phase 3 readiness or next-action recommendation.

**Out of scope this session:** Phase 3 items (days 91–180 per § 14). The ontology consolidation (ONT-1, ONT-5, ONT-7, ONT-9, ONT-11, ONT-13), the temporal-quality cluster (QUAL-1+QUAL-13, QUAL-7, QUAL-8, QUAL-9, QUAL-10, QUAL-14), the Phase 3 agent cluster (AGT-4, AGT-5, AGT-6, AGT-7, AGT-12, AGT-13), the outbound surfaces (INT-11 consumers, INT-12), and the Phase 3 ergonomics items (TOOL-8, TOOL-12, TOOL-13, TOOL-14) all remain queued for the next phase. Do not pull any forward without explicit user direction.

## Section 3 — Per-item briefs (Round A)

### A1 — Wire agents into the scheduler

- **Reference:** K4 / TOOL-7 (scheduler substrate, M48); AGT-1 § 9; AGT-2 § 9; AGT-14 § 9.
- **Files:** `.knowledge/schedule.yaml` + `src/gateway/agents/*.py` + `tests/gateway/test_scheduler.py` (extend if needed)
- **Acceptance:** Three new entries in `.knowledge/schedule.yaml` registered via `wiki schedule add`:
  - `inbox-triage` (suggested cadence: every 15 minutes, cooldown 300s)
  - `draft-closer` (already partially scheduled at 04:30 UTC per M49; verify it now invokes the AGT-2 agent wrapper, not just the deterministic engine)
  - `agent-log-digest` (suggested cadence: daily 07:00 local)
  
  Each job points at a `wiki agents run <name>` command (add the CLI surface if it doesn't exist; preserve K2 parity by adding the corresponding MCP tool or `CLI_ONLY` entry).
- **Pattern:** `wiki schedule add` per M48 K4 + the existing 04:30 daily-finalize-batch entry. The K2 parity test will flag missing MCP coverage if you add a CLI op.
- **Gotcha:** The Phase 2 plan likely names a `wiki agents` CLI namespace. If it exists, use it. If not, add it as part of A1 — single subcommand surface for all agent invocations is cleaner than per-agent CLI bloat.

### A2 — Verify AGT-9 event-bus subscribers fire

- **Reference:** AGT-9 § 9, M56 deliverable
- **Files:** `src/gateway/events.py` + `.knowledge/agents/*.yaml` (subscription registry) + `tests/gateway/test_events.py`
- **Acceptance:** Hand-test the full chain: drop a file into `raw/inbox/`, confirm watcher fires, confirm inbox-triage subscriber picks it up via the event bus (not via direct watcher coupling), confirm a wiki ingest event lands in `log.md` tagged with the agent name. Document the exact sequence in M60.md hand-test results.
- **Pattern:** Existing AGT-9 design per M56 commits `49a7412`, `bf84837`. Use real files in `raw/inbox/` as the test fixture; do not mock the watcher.

### A3 — Post-M59 eval baseline on glp1-reward-modulation

- **Reference:** QUAL-12 § 8 + M50 hand-test (mean 0.566 was M50 baseline)
- **Files:** `.knowledge/eval/glp1-reward-modulation/runs/<ts>.yaml` + `trend.csv`
- **Acceptance:** Run `wiki evaluate glp1-reward-modulation` (no `--scaffold`). Expect a new row in `trend.csv` with `mean_score` and delta vs M50 baseline. Record the wall time, total input/output tokens, `cache_read` tokens (should be > 0 post-M50.1 fix), `cost_usd` in M60.md.
  
  If `mean_score` regresses by more than 0.05 from the M50 baseline of 0.566, **STOP**. Investigate the regression before proceeding (this is the eval framework doing its job — the regression gate is its primary value).
- **Gotcha:** The M50 baseline was run before the parser fix at `24aae19`. The same goldens against the same wiki state should now score equal or slightly higher because of judge-parser robustness improvements, not just because the corpus grew. If the score drops, look at corpus changes (the ai-native-business and condo-capital-infra ingest work) for accidental concept reclassification.

### A4 — Author goldens for two additional domains

- **Reference:** QUAL-12 § 8 + M50 "Subsequent milestones add ... more domains" + § 14 Phase 2 exit criterion "eval framework producing per-milestone scores"
- **Files:** `.knowledge/eval/<domain>/goldens.yaml` × 2 + M60.md
- **Acceptance:** Two new domains' `goldens.yaml` authored, each with 10–15 Q/A pairs matching the M50 glp1 template schema (`id`, `question`, `must_cite`, `must_assert`, `must_not_assert`, `rubric_weight`). `wiki evaluate <domain>` runs successfully for each. Scores recorded in `trend.csv` (first row per domain = baseline).
  
  Suggested domains, in priority order:
  - `ai-native-business` (richest recent corpus per M55–M59 ingest work; tests the substrate against current state)
  - `condo-capital-infra` (largest legacy domain; tests coverage at corpus depth, not freshness)
  - alternative: `edge-ai-agentic` (M50 reported 30% fine-tune readiness; the eval will inform what to invest in)
  
  Choose the two you think give the best signal; document the rationale in M60.md § Hand-test results.
- **Pattern:** Use `wiki evaluate --scaffold <domain>` to write the placeholder template, then hand-edit the Q/A pairs. The scaffold path is the M50 acceptance pathway and is tested.
- **Gotcha:** Q/A authorship is the load-bearing step. The questions must hit the domain's actual content surface, not generic domain knowledge. Spend time reading the MoC and recent syntheses before drafting. 10 good Q/A pairs beat 15 shallow ones.

### A5 — Draft trend snapshot

- **Reference:** QUAL-2 / ARCH-11 § 8 + Phase 2 exit criterion "drafts plateauing or declining"
- **Files:** M60.md § Draft trend
- **Acceptance:** Capture today's draft count by domain (`wiki status` output) and the count from before the daily-finalize-batch started running (search `log.md` for the M49-era count; around 2026-05-23 should be 540+). Compute the delta; record it in M60.md.
  
  If still rising, this exit-criterion clause is not met and Round B should flag it. If plateauing or declining, document the actual cadence.
- **Gotcha:** The "plateauing" judgment is qualitative. Pick a defensible threshold: if drafts decreased OR rose by less than 5% over the period the daily job has been running, call it met. Document the threshold so future eval is consistent.

## Section 4 — Per-item briefs (Round B)

### B1 — Ratify ADR-013 (Readwise as inbound-capture coverage)

- **Reference:** Phase 2 exit criterion "Gmail+podcast+repo pollers"; INT-1, INT-3, INT-9 § 11; ADR-013 (Readwise over separate pollers); § 15 #6 (resolved — user is a Readwise customer).
- **Acceptance:** This decision is already made. § 15 #6 is resolved (user confirmed Readwise membership in the M55–M59 session). ADR-013 records the architectural decision to use Readwise in place of separate Gmail / podcast / Twitter / Kindle / Pocket / Instapaper pollers. Your job is verification + ratification, not redecision:
  - Query INT-9's recent output (e.g. `wiki status` or grep `raw/readwise/` for entries in the last 7 days). Expect non-zero ingest from newsletter + podcast highlight channels.
  - If volume is zero, escalate: either the Readwise account has no recent activity (user-side, document it) or INT-9 is misconfigured (engineering-side, debug it before closing Phase 2).
  - In `docs/phase2-closeout.md`, frame the Gmail+podcast+repo exit clause as met by INT-8 + INT-9 with explicit reference to ADR-013.
- **Gotcha:** Do not re-pose this as an open question. The decision exists; the closeout records the rationale and verifies the substrate is working.

### B2 — Draft cadence narrative

- **Reference:** A5 produced the snapshot
- **Acceptance:** Translate A5's number into a one-paragraph narrative for the closeout: opening draft count, current draft count, daily auto-finalize throughput (count of Cat A finalized by the M49 daily job per day, from `.knowledge/finalize-batch/*.md`), expected exhaustion date at current rate. This is the metric the user will look at in the closeout.

### B3 — docs/phase2-closeout.md

- **Reference:** `docs/phase1-closeout.md` as the template
- **Acceptance:** Mirror the phase1-closeout template. Sections:
  - Scope baseline reference
  - Exit criteria checklist (each clause + status + which milestone closed it)
  - Items shipped (M55 through M61 with one-line summary each; cross-reference to milestone docs)
  - Items deferred (with rationale; INT-1 + INT-3 ratified-out per ADR-013; the Phase 2 § 14 items not pulled forward; any § 15 decisions still open)
  - Eval framework state (post-M59 baseline + the two new domains from A4)
  - Draft trend narrative (from B2)
  - Open follow-ups for Phase 3
  - One-line "Where to read next" pointing at the Phase 3 plan that doesn't yet exist (note that gap explicitly).
- **Gotcha:** The closeout is the artifact your replacement will read first. Bias toward clarity over completeness — every sentence is load-bearing, no padding.

### B4 — Tag the milestone

- **Acceptance:** `git tag m61-phase2-closeout` after B3 is committed. Push only if the user requests; tagging locally is sufficient.

### B5 — session-state.md update + Phase 3 next-action surfacing

- **Acceptance:** Update `docs/session-state.md` to reflect:
  - Open contracts: (none if everything closed cleanly)
  - Files mid-edit: (none)
  - Decisions made this session: (one line per round)
  - Rejected approaches: (only if any)
  - Next atomic step: depends on whether the user wants to proceed to Phase 3. Default recommendation: "Author `docs/plans/<date>-phase3-plan.md` following the Phase 2 plan as template; surface § 15 open decisions blocking Phase 3 start."
  
  This file is the resume contract for whoever runs next.

## Section 5 — § 15 decisions to surface (do NOT decide)

If you encounter friction on any item below, escalate to the user. Do not work around or pre-empt:

- **#1** Hard rule #1 enforcement posture (ARCH-14). Defaulted to social + git review through Phase 2. Phase 3 work may force the issue.
- **#4** ONT-10 source-page stubs (fill vs demote). Gates ONT-1 work in Phase 3.
- **#5** TOOL-2 cloud sleep tolerance.
- **#8** Docs depth target (DOC-1+). Possibly now calibratable post-M59.
- **#9** Wedge vertical for Track B. Independent of this session.
- **#10** Open-source posture for Track B. Independent of this session.

§ 15 #6 (Readwise membership) is resolved — user is a Readwise customer; INT-9 is in production; ADR-013 records the decision.

## Section 6 — Engineering discipline (carry into every change)

Identical to the Phase 1 prompt's Section 5. Summarized:

- Smallest reasonable change per item.
- Plan-before-write for any item touching the validator, gateway choke-point, citation grammar, or scheduler invariants.
- Confirm before any irreversible operation.
- Never recap completed work unless asked.
- Match surrounding code; local consistency trumps external standards.
- Naming tells the domain story; no temporal markers.
- Test-first; tests cover real logic, not mocks; clean test output.
- Debug root causes, not symptoms.
- No emojis; em-dash sparingly.

## Section 7 — Gateway + session-state discipline (CLAUDE.md hard rules)

- No direct writes to `wiki/` or `raw/`.
- No direct NotebookLM calls; route through `wiki nlm-*`.
- Citation grounding mandatory.
- Re-read `docs/session-state.md` before any plan-or-write action if its mtime is newer than this session's earliest user message.
- Proactively checkpoint to `session-state.md` at the end of each round AND before any context-heavy operation. Do not wait for the PreCompact hook.
- Diff `session-state.md` predictions against `git diff` + `pytest` output at each milestone seam.

## Section 8 — Per-round milestone protocol

Treat each Round (A, B) as a milestone (M60, M61). For each round:

1. Branch: `m60-phase2-exit-a` or `m61-phase2-exit-b` off main.
2. Read `session-state.md`; update the `## Files mid-edit` and `## Open contracts` sections before starting work.
3. Implement items in any order within the round. They have light dependencies (A3 → A4 if the eval framework needs debugging).
4. Each item: failing test (or hand-test plan) → minimal implementation → test passes → incremental commit.
5. After all items in the round pass: full suite (`pytest -x --tb=short`). Expect a net positive test delta.
6. Hand-test each item against real data. Record results in `docs/milestones/M<N>.md`.
7. Write the milestone doc following M52–M59 template.
8. Update `WIKI.md` § Gateway operations table if new ops were added (A1's `wiki agents` namespace if added is the candidate).
9. Update `BUILD.md` § 10 with the milestone delivery row.
10. Update `docs/session-state.md` with the round's completion. Move anything from `## Open contracts` to `## Resolved this milestone`.
11. Tag the commit. Merge to main only after K2 parity green.

Two rounds → two milestones (M60 and M61).

## Section 9 — Verification protocol (before declaring Phase 2 closed)

After Round B:

1. `pytest -x` — full green, no skipped tests except documented deferred-hand-test ones.
2. `wiki lint` — review all scopes; no NEW errors introduced; warnings documented.
3. `wiki status` shows:
   - Fine-tune readiness line per domain (M52 QUAL-5)
   - LLM usage block (M47 K5)
   - Evaluation scores block with at least 3 domains (post-A4)
   - Draft count by domain (matches B2 narrative)
4. `wiki schedule list` shows at least 3 agent-driven jobs registered and enabled.
5. K2 parity test green: `pytest tests/gateway/test_mcp_parity.py`.
6. Hand-execute one event-bus round trip end-to-end (raw file → watcher → triage → ingest → log entry) to prove A2's wiring.
7. Confirm `phase2-closeout.md` exists and references all M55–M61 milestone docs.
8. Confirm `session-state.md` `## Next atomic step` is populated and points at Phase 3 planning (or a § 15 decision needed first).

If any of 1–8 fail, the milestone is not closed — investigate, fix, re-run.

## Section 10 — Out of scope (do not touch unless explicitly asked)

- All Phase 3 items (§ 14 Phase 3 table).
- Track B (`kg-core/` extraction, Postgres substrate, multi-tenant).
- § 15 open decisions other than the surfacing step in Section 5.
- Any rewrite of M47–M59 deliverables.
- Eval framework upgrades beyond running it + adding 2 domains' goldens (CI hook, mode-A variant, judge prompt tuning, trend visualization all deferred to Phase 3).
- Building INT-1 (Gmail) or INT-3 (Podcast) as standalone pollers — ADR-013 supersedes.

If you find yourself reaching for any of the above, stop and ask.

## Section 11 — Reporting cadence

- After each round: one paragraph summary in chat. Test delta, items done, what surprised you.
- Mid-round: only if blocked. Do not narrate progress.
- Final closeout: the doc described in B3, plus a one-paragraph chat summary linking to it.

Begin with the session-start sanity check (Section 1 references + the verification grep `git grep -l "write_text" src/gateway/ | grep -v atomic`), then Round A starting with A1. A1 + A2 are the highest-risk because they touch the scheduler and event bus — sequence them first inside Round A so any compaction risk later in the round doesn't fall on the most invariant-adjacent code.
