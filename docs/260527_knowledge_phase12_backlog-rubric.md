# Knowledge Phase 12 Backlog Rubric — 2026-05-27

## § 1 — Current state vs. build plan

**Knowledge: Phase 12 at ~35% — 2 engineering milestones shipped; 55 synthesis drafts uncommitted from prior session**

M109 (query slug dedup) and M110 (discharge-orphans skip-already-cited guard) landed cleanly. The substantive operational work — seven consecutive discharge-orphans runs on condo-capital-infra (~70 synthesis pages generated) and one on ai-native-business (11 pages) — happened but was never committed; those 55 pages sit in `wiki/synthesis/` as untracked files. Phase 12 has no written scope. The skew is operational throughput without commit discipline: the session ran discharge-orphans repeatedly on condo without checking whether the skip-already-cited guard (M110) was actually suppressing re-work or whether the synthesis prompt quality was acceptable. `eval --all-domains` is still broken in two different ways for all four domains.

---

## § 2 — Unshipped items, bucketed

| Bucket | Items | Count |
|--------|-------|-------|
| **Code quality (session-review findings)** | `discharge_orphans` limit not enforced across source types (HIGH); synthesis question prompt content-free; `discharge_orphans` no log entry; `_build_inbound_index` no self-citation exclusion; `wiki_pages` unused import in `fix_wikilinks.py` | 5 |
| **Eval infra gaps** | ai-native context 725k > 500k budget; condo context 614k > 500k budget; edge-ai + glp1 need `ANTHROPIC_API_KEY_RESEARCH` | 4 |
| **Lint regressions** | synthesizes-coverage=74 ERRORs (`synthesizes-included-works-drift` on non-draft pages — was 0 at Phase 10 exit) | 74 pages |
| **Uncommitted work** | 55 synthesis draft pages in `wiki/synthesis/` from prior session; `log.md` + trend CSVs modified but unstaged | ~58 files |
| **Operational — finalize** | 359 escalated drafts needing `--suggest` + `ANTHROPIC_API_KEY_RESEARCH`; entity pages for legacy researchers need source ingestion before cite-suggest works | 359 items |
| **Operational — schema drift** | 208 items (entity_kind-unknown ~58, long-slugs ~50, canonical_name ~34, missing-sections finalized ~34, other ~32) | 208 items |
| **Operational — orphan discharge** | 531 wiki-page orphans; source orphans continue accumulating; discharge needs to run on ai-native-business with proper commit workflow | ongoing |
| **L-effort roadmap** | QUAL-8 (citation coherence judge), ARCH-12 (second NLM backend), ONT-1 (1000 reclassifications), ONT-15 (synthesizes rename) | 4 |

---

## § 3 — Phase exit criteria

Phase 12 has no formally written criteria. Derived from session-state carry-forwards and Phase 11's unmet criterion:

- ✗ `wiki evaluate --all-domains` runs cleanly — blocked on ai-native/condo context budget AND edge-ai/glp1 missing `ANTHROPIC_API_KEY_RESEARCH`; eval has been broken since M103 raised the condo context floor but left ai-native uncapped
- ✗ 55 uncommitted synthesis pages committed (or explicitly abandoned) — prior session ended without closing the commit loop
- ✗ synthesizes-coverage ERRORs back to 0 — 74 `synthesizes-included-works-drift` errors appeared, likely from discharge-orphans pages that write `synthesizes:` frontmatter without matching `## Included works` sections
- ◑ discharge-orphans running on ≥2 domains with commit — glp1 and edge-ai committed (5 drafts each); condo ran 7 times but none committed; ai-native ran once, not committed
- ◑ `discharge_orphans` limit bug fixed — M110 shipped the skip-already-cited guard but the outer-loop limit enforcement (session review HIGH finding) is still open

---

## § 4 — Rubric for backlog decisions

Refining Phase 10 rubric (same day, within 7 days). Dimensions 1–5 unchanged:

1. **Does it change daily operational outcomes?** Scheduled agents and monitors compound permanently.
2. **Is the bottleneck engineering or human judgment?** Per-domain calibration, per-page LLM review are human-bottlenecked; engineering delivers an interface, not an outcome.
3. **Is effort proportionate to the actual use case?** L-effort items need a concrete forcing function.
4. **Are dependencies satisfied?** Items blocked on things that have since shipped should be re-evaluated.
5. **Does it restore eval signal fidelity for a structurally ceilinged domain?** Validated by M103 (+0.146 for condo). Still load-bearing: ai-native context ceiling is the same failure mode.

**Candidate Dim 6 — not yet adopted:** *Does it prevent session-boundary data loss?* Surfaces because discharge-orphans generates pages that require manual commit, and the prior session ran 7+ discharge batches without committing. The pattern of `filed=N, skipped=0` on a domain that should have been exhausted after M110 suggests either M110's skip logic has a gap (NLM-only citations vs raw/ citations), or the 55 pages represent genuine new synthesis but were never committed. The cost of losing them or re-generating them is non-trivial. The fix is S-effort: `discharge-orphans` auto-commit after each batch.

---

## § 5 — Applying the rubric

| Item | Bucket | Trigger to revive | Rubric reason |
|------|--------|-------------------|---------------|
| Commit the 55 uncommitted synthesis pages | Uncommitted work | **Active** — prior session work is in limbo; blocks accurate lint/eval measurement | Dim 1: daily ops can't measure against uncommitted state; Dim 4: dependency for everything else |
| Fix `eval --all-domains` — ai-native/condo context budget | Eval infra | **Active** — `wiki evaluate --all-domains` fails with budget error; last clean run was Phase 11 | Dim 5: same ceiling fix as M103; Dims 1+4: eval cron is broken for these two domains |
| Configure `ANTHROPIC_API_KEY_RESEARCH` for edge-ai/glp1 eval | Eval infra | **Active** — two domains ungradeable; user must set env var | Dim 4: key not set is a config dependency, not engineering; Dim 1: evaluate-weekly cron silently failing |
| Fix `discharge_orphans` limit (outer loop) | Code quality | **Active (HIGH)** — sessions with 5 source types can overshoot limit 5× | Dim 1: discharge batches exceed quota unexpectedly; S-effort fix |
| Improve synthesis question prompt (include domain + abstract) | Code quality | Observed NLM responses are too generic to confirm | Dim 3: current prompt is title-only; fix is S-effort with direct eval impact |
| Fix synthesizes-included-works-drift (74 ERRORs) | Lint regression | **Active** — 74 ERRORs appeared in lint; was 0 at Phase 10 exit | Dim 1: ERRORs in lint are noise in daily ops signal; identify if discharge-orphans is the source |
| `discharge_orphans` auto-commit after each batch | Code quality | Second session ends without committing discharge output | Candidate Dim 6: session-boundary loss pattern; S-effort; high recurrence |
| `discharge_orphans` write log entry | Code quality | Next audit of discharge operations finds gap | Dim 1: low; log entry is housekeeping, not daily-ops blocker |
| `_build_inbound_index` self-citation exclusion | Code quality | Stale draft page spared by self-citation observed | Dim 3: no observed failure yet; Dim 2: test case is S-effort |
| `wiki_pages` unused import | Code quality | Lint or type-check flags it | Dim 3: cosmetic; S-effort but zero daily-ops value |
| 359 escalated finalize-batch drafts | Operational — finalize | `ANTHROPIC_API_KEY_RESEARCH` configured + `wiki finalize-batch --suggest --execute` | Dim 2: entity researcher pages need human source ingestion first; engineering unblocked only by API key |
| Schema-drift 208 | Operational — schema | User editorial sprint scheduled; entity_kind errors spike above 100 | Dim 2: entity_kind, slug length, canonical_name are human-judgment calls |
| QUAL-8, ARCH-12, ONT-1, ONT-15 | L-effort roadmap | Existing triggers (outage, retrieval failure, CiTO tool) | Dims 2+3 fail: L-effort, no current forcing function |

---

## § 6 — Proposed Phase 12 scope

The session state's position — "Phase 12 is in human-editorial territory" — is wrong on the evidence. Three of the five most impactful items are pure engineering, and the eval infrastructure is broken for all four domains. The right framing is: Phase 12 closes the commit + eval + lint debt opened by Phase 11's discharge-orphans work, then re-runs eval with clean signal.

| Item | Effort | Rationale |
|------|--------|-----------|
| Commit (or audit + abandon) the 55 uncommitted synthesis pages | S | Gate item: lint/eval measurements are meaningless until working tree is clean |
| Fix `discharge_orphans` outer-loop limit enforcement | S | Session-review HIGH; prevents quota overshoot; test already described in review |
| Add `discharge_orphans` auto-commit after each batch | S | Prevents session-boundary loss; addresses candidate Dim 6 pattern directly |
| Fix synthesizes-included-works-drift: determine root cause (discharge-orphans author template); add `## Included works` section to discharge-authored pages | S | 74 ERRORs appeared after discharge runs; synthesis pages generated without the section; S-effort once root cause confirmed |
| Improve synthesis question prompt in `discharge_orphans` | S | Session-review finding; title-only prompt → generic NLM responses; include domain + source abstract |
| Fix eval context for ai-native-business (apply M103 pattern: per-source body cap + domain cleanup) | S | Same fix that lifted condo 0.459 → 0.605; ai-native at 725k chars, same failure mode; Dim 5 |
| Document `ANTHROPIC_API_KEY_RESEARCH` setup in RUNBOOK.md; confirm evaluate-weekly cron handles missing key gracefully | S | edge-ai and glp1 eval blocked; RUNBOOK gap is engineering even if the key is a config action |

**Phase 12 exit criteria:**
- `wiki evaluate --all-domains` runs cleanly for all four domains (no context-budget or API-key errors)
- `wiki lint --scope synthesizes-coverage` returns 0 ERRORs
- Working tree clean: no uncommitted synthesis pages; `discharge_orphans` auto-commits its output
