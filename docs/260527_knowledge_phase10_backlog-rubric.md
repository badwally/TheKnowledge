# Knowledge Phase 10 Backlog Rubric — 2026-05-27 (revised post-M103/M104/M105)

## § 1 — Current state vs. build plan

**Knowledge Base: Phase 10 at 75% — 3 of 4 items shipped; discharge-orphans blocked on NLM auth.**

Phase 10 delivered its three engineering items in rapid succession: M103 fixed the condo eval context explosion (1.04M → 566k chars via 30k per-source cap), M104 extended the draft-exemption pattern to synthesizes-coverage lint (13 ERRORs → 0 ERRORs, 13 WARNINGs), and M105 applied the same pattern to section-missing in the validator itself (schema-drift 276 → 208). The condo eval reached 0.605, clearing the 0.600 exit criterion. The skew is clear: all three shipped items were pure engineering (lint rules + validator params), and the one operational item — first live discharge-orphans run — is blocked entirely on NLM re-authentication, not on anything we built. Phase 10 is one `nlm login` away from its third exit criterion.

---

## § 2 — Unshipped items, bucketed

| Bucket | Items | Count |
|--------|-------|-------|
| **L-effort roadmap** | QUAL-8 (citation coherence judge), ARCH-12 (second NLM backend), ONT-1 (1000 concept reclassifications), ONT-15 (synthesizes rename) | 4 |
| **Eval signal gaps** | goldens quality unknown for edge-ai/ai-native/condo sub-questions; discharge-orphans hasn't run live | 2 gaps |
| **Operational debt — schema** | schema-drift 208: entity_kind-unknown ~58, missing-sections finalized entities ~34 (was ~68 before M105 cleared draft exemptions), long slugs ~50, canonical_name ~34, other ~32 | 208 items |
| **Operational — orphan discharge** | First live run blocked on NLM auth (user action: `nlm login`) | 1 run |
| **Operational — fine-tune** | glp1: 268/500 (54%); edge-ai: ~151/500 (30%); others low | multi-domain |
| **Technical cleanup** | INT-18/INT-19 hand-tests (live tokens required); `wiki migrate` stub; discharge-orphans dry-run doesn't validate NLM auth (misleading "N drafted" before auth check) | 3 items |

---

## § 3 — Phase 10 exit criteria

- ✓ `wiki evaluate condo-capital-infra` ≥ 0.600 — **DONE: 0.605** (q09=1.00, q03=1.00, q08=1.00)
- ✓ `wiki lint --scope synthesizes-coverage` returns 0 ERRORs — **DONE: 0 ERRORs** (13 WARNINGs for draft pages, correct behavior)
- ✗ `wiki routine discharge-orphans` has executed at least one live run — **BLOCKED: NLM session expired**

**Assessment:** Two of three criteria met. The third is a one-command user action (`nlm login`), not an engineering gap. Phase 10 should not close until discharge-orphans runs live — the value of shipping M103-M105 first was specifically to make that run succeed in a clean context environment.

---

## § 4 — Rubric for backlog decisions

**Reusing Phase 10 rubric verbatim (same-day, within 7 days):**

1. **Does it change daily operational outcomes?** Scheduled agents and monitors compound permanently. Schema fixes and authorship ergonomics help only at write time.
2. **Is the bottleneck engineering or human judgment?** Per-domain calibration, per-page LLM review, and cross-system coordination mean engineering delivers an interface, not an outcome.
3. **Is effort proportionate to the use case that actually exists right now?** L-effort items need a concrete forcing function.
4. **Are dependencies satisfied?** Items blocked on things that have since shipped should be re-evaluated.

**Adopted Phase 10 dimension (retained):** *Does it restore eval signal fidelity for a domain that is structurally ceilinged?* Still load-bearing for condo, now validated — the 30k body cap + domain cleanup recovered 0.146 score points.

**New candidate dimension — surfaces now:** *Does it close a misleading no-op in operational tooling?* The discharge-orphans `--dry-run` reports "N synthesis drafts filed" without checking NLM auth or notebook existence — a false positive that burned debug time. Not adopted (Dim 3: S-effort fix, but low recurrence since auth will be stable once restored).

---

## § 5 — Applying the rubric

| Item | Bucket | Trigger to revive | Rubric reason |
|------|--------|-------------------|---------------|
| QUAL-8 (citation-claim coherence) | L-effort roadmap | A propagated wrong claim causes real-world error | Dims 1+3: L-effort LLM judge, no daily-ops value until observable failure |
| ARCH-12 (second NLM backend) | L-effort roadmap | NotebookLM outage >48h OR quota hit | Dim 3: risk not acute |
| ONT-1 (1000 concept reclassifications) | L-effort roadmap | Retrieval failures from misclassification observed in `wiki query` | Dims 2+3: human-bottlenecked, L-effort |
| ONT-15 (synthesizes rename) | L-effort roadmap | CiTO alignment required by downstream tool | Dim 3: cosmetic, 280+ references |
| Schema-drift legacy editorial 208 | Operational debt — schema | User editorial sprint scheduled; entity_kind errors spike above 100 | Dim 2: entity_kind, slug length, canonical_name are human-judgment calls |
| discharge-orphans live run | Operational — orphan discharge | **Active — user action: `nlm login`** | Dims 1+4: auth is the only gate; machinery is production-ready |
| discharge-orphans dry-run validation bug | Technical cleanup | discharge-orphans fails in CI or wastes a quota call from false positive | Dim 3: low recurrence once auth stable |
| Fine-tune readiness | Operational — fine-tune | Any domain crosses 400 decisions | Dim 3: 268/500 on best domain; sub-threshold |
| INT-18/INT-19 hand-tests | Technical cleanup | Live NOTION_TOKEN / SLACK_BOT_TOKEN available | Dim 4: token dependency unresolved |
| `wiki migrate` stub | Technical cleanup | User has a migration target | Dim 3: no concrete use case |

---

## § 6 — Proposed Phase 11 scope

**Endorsing and updating session state:** The session state's immediate next step (NLM auth → `discharge-orphans --domain condo-capital-infra --limit 10`) is correct. Once that clears Phase 10, Phase 11 should shift from lint/validator engineering toward operational throughput — running discharge-orphans across multiple domains and watching whether the improved eval scores hold as new synthesis pages enter the wiki. The schema-drift 208 tail is largely Dim 2-fail (human editorial); it does not belong in an engineering phase.

| Item | Effort | Rationale |
|------|--------|-----------|
| discharge-orphans multi-domain sweep — run on condo-capital-infra and edge-ai-agentic (both have notebooks); limit 20–50 per domain; review output quality | S | Phase 10 live run confirmed architecture works; Phase 11 scales it to domains where orphan tail is densest |
| Re-run `wiki evaluate --all-domains` and review trend — after discharge adds new synthesis pages, confirm no eval regression on glp1/edge-ai, and check if condo climbs further | S | New synthesis pages could push condo above 0.650; regression guard on glp1 (currently 0.649, fragile) is important |
| Finalize-batch for oldest outstanding drafts — `wiki finalize-batch` on drafts >30 days (strict citation check) OR abandon drafts that are stale and unresolvable | S | Phase 10 cleared draft lint warnings; finalize-batch converts best drafts to hard citations, shrinking the WARNING tail |
| Fix discharge-orphans dry-run: validate NLM auth and notebook existence before reporting success | S | Misleading dry-run results burned debug time twice; fix is a one-function check |

**Phase 11 exit criteria:**
- discharge-orphans has run live on ≥2 domains; ≥20 synthesis drafts committed
- `wiki evaluate --all-domains` shows no regression from Phase 10 scores (condo ≥0.605, glp1 ≥0.640, edge-ai ≥0.680)
- discharge-orphans dry-run correctly fails fast when NLM auth is expired
