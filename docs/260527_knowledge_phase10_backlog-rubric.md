# Knowledge Phase 10 Backlog Rubric — 2026-05-27

## § 1 — Current state vs. build plan

**Knowledge Base: Phase 9 complete at 102 milestones shipped — the weekly eval is running, but two of four domains are still in degraded-signal territory.**

Phase 9 landed cleanly: question quality improved, `--all-domains` eval is scheduled, `parse_iso` is consolidated. Post-Phase-9 patch work added real weight: condo-capital-infra recovered from 0.100 to 0.459, the ContextTooLargeError blocker is fixed with a `--max-chars` flag, and backfill-synthesizes closed 50 synthesizes ERRORs. The system is now running weekly evals across four domains. The problem is that two of those four scores are ceilinged by domain-context gaps (condo can't reach its q09/q10 goldens; ai-native is at 750k max-chars and still partial), and lint has grown from 225 to 276 schema-drift items because `wiki query` auto-created entity pages are missing required sections — a new category that didn't exist before. Phase 10's job is to run the machinery and close the lint floor, not build more machinery.

---

## § 2 — Unshipped items, bucketed

| Bucket | Items | Count |
|--------|-------|-------|
| **L-effort roadmap** | QUAL-8 (citation coherence judge), ARCH-12 (second NLM backend), ONT-1 (1000 concept reclassifications), ONT-15 (synthesizes rename) | 4 |
| **Eval signal gaps** | condo q09/q10 ceiling (NLM corpus missing 2 sources); synthesizes-coverage 13 ERRORs (legacy short-slug pages, no inline wikilinks); goldens quality unknown for non-glp1 domains | 3 gaps |
| **Operational debt — schema** | schema-drift 276: entity_kind-unknown ~58, missing-sections entities ~68 (legacy), new auto-entity missing-sections ~51 (created by discharge-orphans/query), long slugs ~50, canonical_name ~34 | 276 items / 2 flavors |
| **Operational — orphan discharge** | `discharge-orphans` has never run live on any domain (ANTHROPIC_API_KEY_RESEARCH is the gate) | 1 class |
| **Operational — fine-tune** | glp1: 268/500 (54%); edge-ai: 151/500 (30%); others 0–16% | 11 domains |
| **Technical cleanup** | INT-18/INT-19 hand-tests (live tokens required); `wiki migrate` stub | 3 items |

---

## § 3 — Phase 9 exit criteria

- ✓ `_synthesis_question` includes domain policy + abstract excerpt; test confirms richer question generation
- ✓ `wiki evaluate` run on ≥2 domains beyond glp1 — **4 domains scored** (glp1 0.649, edge-ai 0.690, condo 0.459, ai-native 0.889 at 750k)
- ✓ `_parse_iso` consolidated to single impl in `gateway.core`; 0 regressions
- ✓ 1837 tests, 0 regressions

**Assessment:** All three criteria met. Post-phase patches (condo fix, max-chars, backfill-synthesizes) were necessary and correct — they resolved blockers that would have silently degraded the weekly eval. The 13 residual synthesizes-coverage ERRORs and 51 new schema-drift items are a post-Phase-9 artifact, not a Phase 9 failure.

---

## § 4 — Rubric for backlog decisions

**Reusing Phase 9 rubric verbatim (same-day, within 7 days):**

1. **Does it change daily operational outcomes?** Scheduled agents and monitors compound permanently. Schema fixes and authorship ergonomics help only at write time.
2. **Is the bottleneck engineering or human judgment?** Per-domain calibration, per-page LLM review, and cross-system coordination mean engineering delivers an interface, not an outcome.
3. **Is effort proportionate to the use case that actually exists right now?** L-effort items need a concrete forcing function.
4. **Are dependencies satisfied?** Items blocked on things that have since shipped should be re-evaluated.

**Previously-candidate dimension from Phase 9 — still unadopted:** *Does it advance fine-tune readiness toward an actionable threshold?* glp1 at 268/500 is approaching range, but no domain is at the 400-decision (80%) sub-threshold where effort is clearly warranted. Not adopted for Phase 10.

**New candidate dimension — adopted for Phase 10:** *Does it restore eval signal fidelity for a domain that is structurally ceilinged?* The weekly eval is now live, but condo is capped at ~0.5 by missing NLM corpus entries, and synthesizes-coverage ERRORs mean some pages don't pull source bodies into context. If eval scores are the primary quality signal, structural gaps that suppress scores by 0.2–0.4 points invalidate the signal. Activate when an eval score is provably limited by missing corpus/context entries rather than wiki content quality.

---

## § 5 — Applying the rubric

| Item | Bucket | Trigger to revive | Rubric reason |
|------|--------|-------------------|---------------|
| QUAL-8 (citation-claim coherence) | L-effort roadmap | A propagated wrong claim causes real-world error | Dims 1+3: L-effort LLM judge, no daily-ops value until observable failure |
| ARCH-12 (second NLM backend) | L-effort roadmap | NotebookLM outage >48h OR quota hit | Dim 3: risk not acute |
| ONT-1 (1000 concept reclassifications) | L-effort roadmap | Retrieval failures from misclassification observed in `wiki query` | Dims 2+3: human-bottlenecked, L-effort |
| ONT-15 (synthesizes rename) | L-effort roadmap | CiTO alignment required by downstream tool | Dim 3: cosmetic, 280+ references |
| condo q09/q10 eval ceiling | Eval signal gaps | **Active (new dim):** eval score provably capped at 0.459 by 2 missing corpus entries | New dim + Dim 4: NLM-add is S-effort; direct +0.2–0.3 on weekly signal |
| Synthesizes-coverage 13 ERRORs | Eval signal gaps | **Active:** 13 legacy pages with no inline wikilinks remain ERROR; backfill can't auto-fix them | Dim 1: ERRORs suppress eval context quality; S-effort manual entries |
| Schema-drift legacy editorial 225 | Operational debt — schema | User editorial sprint scheduled | Dim 2: entity_kind, slug length, canonical_name are all human-judgment calls |
| Schema-drift new auto-entity 51 | Operational debt — schema | **Active:** auto-created entities missing `## Key facts` + `## Related`; LLM-assisted fill is automatable | Dims 1+2: LLM can generate from source metadata; S/M effort; compresses on each new discharge run |
| discharge-orphans live run | Operational — orphan discharge | **Active:** ANTHROPIC_API_KEY_RESEARCH is the only gate; M100 question quality now adequate | Dims 1+4: highest-leverage daily-ops item once key is available |
| Fine-tune readiness | Operational — fine-tune | Any domain crosses 400 decisions | Dim 3: 268/500 on best domain; sub-threshold |
| INT-18/INT-19 hand-tests | Technical cleanup | Live NOTION_TOKEN / SLACK_BOT_TOKEN available | Dim 4: token dependency unresolved |
| `wiki migrate` stub | Technical cleanup | User has a migration target | Dim 3: no concrete use case |

---

## § 6 — Proposed Phase 10 scope

**Challenge to session-state candidates:** The session state lists discharge-orphans, editorial tooling, QUAL-8, and fine-tune as Phase 10 candidates. Editorial tooling is challenged as the anchor — the 51 new auto-entity items are automatable (missing sections from LLM-generated entities, not wrong classifications), but the 225-item legacy tail is still Dim 2-fail for the same reasons as Phase 9. The actual Phase 10 anchor is eval signal fidelity + first live discharge run. QUAL-8 remains deferred (no forcing function). Fine-tune is user-paced, not engineering.

| Item | Effort | Rationale |
|------|--------|-----------|
| Fix condo eval ceiling — `wiki nlm-add condo-capital-infra web-2025-10-29-056` + `wiki nlm-add condo-capital-infra web-2022-07-07-3bd` + targeted `wiki query` to generate synthesis pages citing those sources | S | New adopted dim fires: score provably capped at 0.459 by 2 missing corpus entries. S-effort; directly improves the weekly quality signal. |
| Close synthesizes-coverage 13 ERRORs — manually add `synthesizes:` to 13 legacy short-slug pages | S | 13 ERRORs in lint floor; backfill can't fix pages with no inline wikilinks. Closes the ERROR floor permanently. |
| Auto-fill missing sections on LLM-created entities — `wiki repair-entities --scope missing-sections [--domain D] [--dry-run]` generates `## Key facts`, `## Related`, `## Summary` stubs from source metadata for ~51 auto-entity pages | M | Unlike entity_kind reclassification (Dim 2-fail), section content is LLM-generatable from source metadata. Compresses schema-drift 276 → ~220; user approves in batch not per-page. |
| First live discharge-orphans run — once `ANTHROPIC_API_KEY_RESEARCH` is set, run `wiki routine discharge-orphans --domain glp1-reward-modulation --limit 20 --dry-run` then execute; repeat for edge-ai | S | Machinery is production-ready; M100 improved question quality. Highest-leverage daily-ops item — converts raw sources into cited synthesis pages. S-effort once key is available. |

**Phase 10 exit criteria:**
- `wiki evaluate condo-capital-infra` scores ≥ 0.600 (up from 0.459), indicating q09/q10 goldens are reachable from wiki context
- `wiki lint --scope synthesizes-coverage` returns 0 ERRORs
- `wiki routine discharge-orphans` has executed at least one live run on glp1-reward-modulation; results committed
