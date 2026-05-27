# Knowledge Phase 9 Backlog Rubric — 2026-05-27

## § 1 — Current state vs. build plan

**Knowledge Base: Phase 8 complete at 99 milestones shipped — engineering has outpaced validation of its own outputs.**

Phase 8 correctly bet on operational debt clearance and won on 3 of 4 exit criteria: 4372 auto-fixable schema-drift items cleared, wikilink errors eliminated, orphan-discharge and stale-draft machinery shipped. The fourth criterion (schema-drift < 50) is a nominal miss — the 225 remaining items are irreducibly editorial, not a failure of engineering. What Phase 8 did not do is run the machinery it built: `discharge-orphans` has never been executed against a live NLM corpus, the eval framework has a single baseline run (glp1, mean=0.566), and `_synthesis_question` generates questions from source titles alone — a content-free prompt that will produce mediocre synthesis pages at scale. Phase 9 is a put-the-tools-to-work phase, not a build-more-tools phase.

---

## § 2 — Unshipped items, bucketed

| Bucket | Items | Count |
|--------|-------|-------|
| **L-effort roadmap remainders** | QUAL-8 (citation coherence), ARCH-12 (second NLM backend), ONT-1 (1000 concept reclassifications), ONT-15 (synthesizes rename) | 4 |
| **Operational quality gap** | `_synthesis_question` content-free prompt; eval framework only run once (glp1 baseline); no multi-domain quality signal | 2 classes |
| **Operational debt — schema** | schema-drift: 225 (entity_kind unknown 58, missing-sections 68, required-field 34, long-slug 50, other 15) — all editorial | 1 class / 225 items |
| **Operational debt — orphans** | Source-orphan count unknown per domain; `discharge-orphans` exists but never run live | 1 class |
| **Operational debt — fine-tune** | glp1: 268/500 (53%); edge-ai: 151/500 (30%); 9 other domains at 0–16% | 11 domains |
| **Technical cleanup** | `_parse_iso` 5 duplicate impls; INT-18/INT-19 hand-tests (need live tokens) | 2 items |
| **Carry-forward user actions** | `wiki backfill-synthesizes` (61 ERRORs); `ANTHROPIC_API_KEY_RESEARCH`; `wiki migrate` stub | 3 items |

---

## § 3 — Phase exit criteria

Phase 8 exit criteria (from BUILD.md § 18 and proposed in Phase 8 rubric § 6):

- ✗ `wiki lint --scope schema-drift` findings < 50 — **225** (automatable 4372 cleared; irreducible editorial tail)
- ✓ `wiki lint --scope broken-wikilinks` findings < 100 — **82** WARNINGs, 0 ERRORs (down from 277)
- ✓ `wiki routine discharge-orphans` registered as scheduled op and operational
- ✓ 1812 tests, 0 regressions

**Assessment:** Phase 8 met its intent. The schema-drift criterion was set before the composition of remaining items was known — it was a measurement error, not a delivery failure. The `< 50` target assumed the tail was automatable; it wasn't.

---

## § 4 — Rubric for backlog decisions

**Reusing Phase 8 rubric verbatim (same-day, within 7 days):**

1. **Does it change daily operational outcomes?** Scheduled agents and monitors compound permanently. Schema fixes and authorship ergonomics help only at write time.
2. **Is the bottleneck engineering or human judgment?** Per-domain calibration, per-page LLM review, and cross-system coordination mean engineering delivers an interface, not an outcome.
3. **Is effort proportionate to the use case that actually exists right now?** L-effort items need a concrete forcing function.
4. **Are dependencies satisfied?** Items listed as blocked on things that have since shipped should be re-evaluated.

**Previously-candidate dimension — now adopted for Phase 9:** *Does it improve the quality of synthesized outputs from existing machinery?* The Phase 8 candidate ("reduce lint false-positive noise") drove Phase 8 correctly and is now resolved. Phase 9 faces a successor problem: the synthesis and evaluation infrastructure exists but its output quality is unvalidated. This dimension activates for `_synthesis_question` quality and eval scheduling, where engineering can directly improve what the system produces.

**New candidate dimension — not yet adopted:** *Does it advance fine-tune readiness toward an actionable threshold?* glp1 at 268/500 is within reach of the 500-decision threshold where fine-tuning becomes viable. Worth adopting if Phase 9 includes a targeted ingest push; premature if ingest rate stays at natural pace.

---

## § 5 — Applying the rubric

| Item | Bucket | Trigger to revive | Rubric reason |
|------|--------|-------------------|---------------|
| QUAL-8 (citation-claim coherence) | L-effort roadmap | A specific claim propagated incorrectly into a synthesis page causes a real-world error | Dims 1+3: L-effort LLM judge, no daily-ops value until coherence failures are observable |
| ARCH-12 (second NLM backend) | L-effort roadmap | NotebookLM outage >48h OR quota hit | Dim 3: risk not acute |
| ONT-1 (1000 concept reclassifications) | L-effort roadmap | Retrieval failures from concept misclassification observed in `wiki query` | Dims 2+3: human-bottlenecked review, L-effort |
| ONT-15 (synthesizes rename) | L-effort roadmap | CiTO alignment required by a downstream tool | Dim 3: cosmetic, 280+ references |
| Schema-drift 225 | Operational debt — schema | User editorial sprint scheduled | Dim 2: all items are human-judgment calls; `wiki lint` report already surfaces them |
| `_synthesis_question` content-free prompt | Operational quality gap | **Active:** M99 shipped; discharge-orphans ready to run live | Dim 4 satisfied (M99 deployed); dims 1+2: S-effort fix, direct impact on every future discharge run |
| Multi-domain eval | Operational quality gap | **Active:** eval framework exists; no second domain ever scored | Dim 1: quality signal is a daily-ops input; without it, no feedback loop on synthesis output |
| Source orphans (per-domain count unknown) | Operational debt — orphans | discharge-orphans live run shows non-zero count | Dim 2: partial bottleneck — machinery exists; question quality is the current gate |
| Fine-tune readiness (glp1 53%, others <30%) | Operational debt — fine-tune | Any domain crosses 400 decisions (80% threshold) | Dim 3: fine-tuning workflow not yet validated; crossing threshold still S effort away |
| `_parse_iso` consolidation | Technical cleanup | Next cleanup pass; no urgency | Dims 1+3: purely internal, no operational surface; lowest-cost phase filler |
| INT-18/INT-19 hand-tests | Technical cleanup | Live NOTION_TOKEN / SLACK_BOT_TOKEN available | Dim 4: token dependency unresolved |
| `wiki backfill-synthesizes` | Carry-forward user action | User runs it (61 ERRORs) | Dim 2: op exists; user action only |
| `wiki migrate` stub | Carry-forward | User has a migration target | Dim 3: no concrete use case yet |

---

## § 6 — Proposed Phase 9 scope

The session-state Phase 9 candidates are: editorial schema-drift tooling (225 items), `_synthesis_question` quality, `_parse_iso` consolidation, Phase 9 rubric. The editorial-tooling candidate is challenged as the anchor bet: the 225 items are irreducibly human-judgment, and building tooling to present them interactively is Dim 2-fail. The right Phase 9 anchor is synthesis quality and evaluation expansion — the machinery from Phases 7–8 is now complete but unvalidated, and improving question generation + running multi-domain eval closes the feedback loop that the entire research pipeline depends on.

| Item | Effort | Rationale |
|------|--------|-----------|
| `_synthesis_question` quality improvement — inject domain policy + source abstract/excerpt into question prompt | S | Trigger active (M99 shipped). Current prompt uses source title only — will produce generic questions at scale. S-effort fix with direct multiplier on every future discharge-orphans run. Dim 1+4. |
| Multi-domain evaluation run + eval scheduling — run `wiki evaluate` on edge-ai-agentic and 1–2 other domains; wire AGT-8-style cron for periodic eval re-runs | S/M | Only glp1 scored (mean=0.566, initial only). Eval framework (M50) and LLM usage infrastructure both exist. Producing per-domain quality signals turns `wiki evaluate` from a one-shot tool into an ongoing monitor. Dim 1. |
| `_parse_iso` consolidation — extract to `gateway.core`, remove 5 private duplicate impls | S | Pure cleanup, bounded scope, no user decisions required. Correct to do in any phase. Dim 3. |
| Editorial repair assistant for entity_kind reclassification — `wiki repair-entities [--domain D] [--dry-run]` that batch-suggests `entity_kind` fixes using source metadata + domain policy | M | 58 of 225 schema-drift items are `entity_kind-unknown`. An LLM-assisted batch-suggest (not auto-apply) would let user approve a batch instead of reviewing 58 pages individually. Only include if user confirms editorial backlog is priority. |

**Phase 9 exit criteria:**
- `_synthesis_question` prompt includes domain policy + abstract excerpt; test confirms richer question generation
- `wiki evaluate` has been run on ≥2 domains beyond glp1; results filed in BUILD.md
- `_parse_iso` consolidated to single impl in `gateway.core`; 0 regressions
