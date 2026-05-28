# Knowledge Phase 8 Backlog Rubric — 2026-05-27

## § 1 — Current state vs. build plan

**Knowledge Base: Phase 7 complete at effective 100% of roadmap — 95 milestones shipped, backlog is L-only or operational debt.**

Phase 7 (M89–M95) skewed correctly toward S/M-effort tooling: inbox triage, tags codification, question page type, ask-corpus, question management. These closed the surface gaps between the gateway's query power and the user's daily interface. What it did not touch — and correctly deferred — is operational debt: 6386 lint findings dominate the signal landscape right now, with schema-drift (4597) burying real quality findings. The project has crossed a threshold where the monitoring infrastructure is more complete than the data it's monitoring, and that imbalance is now the primary constraint on value delivery.

---

## § 2 — Unshipped items, bucketed

| Bucket | Items | Count |
|--------|-------|-------|
| **L-effort roadmap remainders** | QUAL-8 (citation coherence), ARCH-12 (second NLM backend), ONT-1 (1000 concept reclassifications), ONT-15 (synthesizes rename) | 4 |
| **Operational debt — schema** | schema-drift: 4597 entity pages missing `created_at`/`last_updated` | 1 class |
| **Operational debt — citation graph** | orphans: 527 sources with no inbound citations; synthesizes-coverage: 61 synthesis pages missing `synthesizes:` frontmatter | 2 checks |
| **Operational debt — link health** | link-rot: 428 dead/redirected web sources; broken-wikilinks: 277 | 2 checks |
| **Operational debt — content aging** | stale-drafts: 224; stale-claims: 3; stale-verified: 46 | 3 checks |
| **Carry-forward user actions** | Run `wiki backfill-synthesizes` (61 ERRORs); set `ANTHROPIC_API_KEY_RESEARCH`; INT-18/19 hand-tests | 3 |

---

## § 3 — Phase exit criteria

Phase 7 exit criteria (from BUILD.md § 16) — all met:

- ✓ AGT-8 cron registered and idempotent
- ✓ TOOL-11 `/api/inbox` with retry
- ✓ ONT-12 tags validated + lint check
- ✓ ONT-14 question page type with lint checks
- ✓ TOOL-10 shell completion documented
- ✓ TOOL-15 `wiki ask-corpus` + MCP
- ✓ TOOL-16 `wiki question new/list` + MCP auxiliaries
- ✓ 1769 tests, 0 regressions

Phase 8 exit criteria — proposed in § 6.

---

## § 4 — Rubric for backlog decisions

**Reusing prior rubric (2026-05-26, within 7 days) verbatim:**

1. **Does it change daily operational outcomes?** Scheduled agents and monitors compound permanently. Schema fixes and authorship ergonomics help only at write time.
2. **Is the bottleneck engineering or human judgment?** Per-domain calibration, per-page LLM review, and cross-system coordination mean engineering delivers an interface, not an outcome.
3. **Is effort proportionate to the use case that actually exists right now?** L-effort items need a concrete forcing function.
4. **Are dependencies satisfied?** Items listed as blocked on things that have since shipped should be re-evaluated.

**Candidate new dimension — not yet adopted:** At 6386 lint findings, signal-to-noise ratio in `wiki lint` is degraded. A fifth dimension could be: *Does it reduce false-positive lint noise such that real quality signals become actionable?* Surfaces because schema-drift (4597) drowns out the 75 contradictions and 277 broken wikilinks that matter operationally. Worth adopting if Phase 8 bets on operational debt clearance.

---

## § 5 — Applying the rubric

| Item | Bucket | Trigger to revive | Rubric reason |
|------|--------|-------------------|---------------|
| QUAL-8 (citation-claim coherence) | L-effort roadmap | A specific claim is found to have propagated incorrectly into a synthesis page and caused a real-world error | Dims 1+3: L-effort LLM work, no daily-ops value unless coherence failures are observable |
| ARCH-12 (second NLM backend) | L-effort roadmap | NotebookLM outage >48h OR a specific NLM quota limit is hit | Dim 3: L-effort, risk not yet acute |
| ONT-1 (concept reclassifications) | L-effort roadmap | Retrieval failures from concept misclassification are observed in `wiki query` results | Dims 2+3: human-bottlenecked (1000 LLM proposals to review), L-effort |
| ONT-15 (synthesizes rename) | L-effort roadmap | CiTO formal alignment becomes a dependency for a downstream tool | Dim 3: cosmetic, 280+ references, no operational impact |
| Schema-drift 4597 (entity timestamps) | Operational debt — schema | `wiki backfill-timestamps` runs clean on a dry-run | Dim 1: passes (fixing restores lint signal); op already ships in CLI_ONLY — this is an execution problem, not an engineering one |
| Orphans: 527 | Operational debt — citation | Any single domain's orphan count drops to <10 after a synthesis loop | Dim 2: partial bottleneck — `wiki ask-corpus` is the tool, but topic selection per source is human judgment |
| Synthesizes-coverage: 61 | Operational debt — citation | `wiki backfill-synthesizes` user action (carry-forward) | Dim 1: directly reduces lint ERROR count; the op exists — blocked on user running it |
| Link-rot: 428 | Operational debt — link health | Any domain's dead-link count exceeds 20% of its sources | Dim 1: already monitored; no new engineering needed |
| Broken-wikilinks: 277 | Operational debt — citation | A broken wikilink is found in an actively-used synthesis page | Dim 3: partially automatable; many are likely stubs from legacy migration |
| Stale-drafts: 224 | Operational debt — content | A draft page is cited by another page and cannot finalize | Dim 2: human-bottlenecked; `wiki finalize` exists, selection is editorial |

---

## § 6 — Proposed Phase 8 scope

The session-state proposes three options (QUAL-8 with forcing function, orphan discharge, schema backfill). QUAL-8 has no forcing function and stays deferred. Orphan discharge is user-driven editorial work, not engineering. **The right Phase 8 bet is operational debt clearance as an engineering problem** — specifically the items where new code would reduce lint noise and restore signal fidelity, making the monitoring infrastructure built in Phases 1–7 actually useful day-to-day.

| Item | Effort | Rationale |
|------|--------|-----------|
| Schema timestamp backfill runner + validation | S | `backfill-timestamps` exists in CLI_ONLY; verify it handles the 4597-entity case correctly and run it. Reduces schema-drift from 4597 → near-zero. Makes `wiki lint` signal actionable. |
| Broken-wikilink repair op (`wiki fix-wikilinks --scope dead`) | M | 277 broken wikilinks, most from legacy migration. A repair op that detects page-does-not-exist patterns and either removes or flags the link. Reduces noise in the most-cited check. |
| Orphan discharge routine (`wiki routine discharge-orphans --domain <slug> --limit N`) | M | Wraps `wiki ask-corpus` to loop over orphaned sources for a domain and synthesize each one. Converts the manual synthesis loop into a scheduled batch. Dim 1 pass: compounds without prompting. |
| Stale-draft auto-abandonment policy | S | 224 stale drafts; a policy that auto-abandons truly orphaned old drafts (>30 days, no inbound citations) rather than letting them accumulate. Reduces stale-drafts count. |

**Phase 8 exit criteria:**
- `wiki lint --scope schema-drift` findings < 50 (from 4597)
- `wiki lint --scope broken-wikilinks` findings < 100 (from 277)
- `wiki routine discharge-orphans` is a registered scheduled op; at least one domain's orphan count measurably reduced
