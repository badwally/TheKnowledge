# Session state — 2026-06-10

Last updated: 2026-06-10 (new arc: data-collectives research foundation — loop execution starting)

---

## ▶ STAGE 2 READY (foundation RESOLVED 2026-06-10)

Foundation loop COMPLETE (Tasks 1–10, committed c3eaee04..3989c841). Now on **Stage 2 — condo application leg**, to run in a FRESH session.
Plan: `docs/superpowers/plans/2026-06-11-data-collectives-stage2-condo-application.md`.
Stage 2 is SYNTHESIS (not fan-out) — do NOT run deep-research workflows (unnecessary + spend cap live). Kick off with: `go` (or re-fire the plan) in a clean session.
Still-deferred from foundation: file the citation-grounded wiki synthesis page via `wiki query` on spend-cap reset (analysis already at docs/research/data-collectives/synthesis-policy-market.md).

---

## Open contracts

**data-collectives research foundation — IN PROGRESS (self-paced loop).**
Spec: `docs/superpowers/specs/2026-06-10-data-collectives-research-foundation-design.md`.
Plan: `docs/superpowers/plans/2026-06-10-data-collectives-research-foundation.md`.

New citation-grounded wiki domain `data-collectives`, forked from `condo-capital-infra`.
Policy/market-structure spine; Approach C (agentic dimensional fan-out). Executed as a
self-paced loop, one plan Task per iteration: deep-research → `wiki ingest --with-plan`
the verified sources → author concept/synthesis pages → verify grounding → commit →
checkpoint here → schedule next.

**Task ledger (loop tracks progress here):**
- [x] Task 1 — bootstrap `data-collectives` domain (policy.yaml created, verified)
- [x] Task 2 — Stream 0 precedent census (seed) — 7 source pages + 8 concept pages + entities grounded; analytical note at docs/research/data-collectives/stream-0-precedent-census.md
- [x] Task 3 — Stream 1 economic/incentive — grounded: nonrivalry-of-data, data-shapley, competitor-data-sharing-tradeoff, product-differentiation-collaboration (+ Jones&Tonetti, Tsoy&Konstantinov, Data Shapley sources). Vives 1984 + Farboodi-Veldkamp verified but full-text won't convert (noted in stream-1 note). KEY: substitutes in same market have weak/negative pooling incentive (Vives Cournot PD).
- [x] Task 4 — Stream 2 technical/architecture — GROUNDED. 6 source pages live (FL gradient-inversion, subject MIA, DP-FL, DP survey, Azure Confidential Clean Rooms, NIST US-UK PETs Prize) via filter-correct + re-ingest. ACM-Queue + OPAL chapter still need alt URLs (cited by reference in note). KEY: agentic-layer gap (zero verified precedent — see note).
- [x] Task 5 — Stream 3 legal — GROUNDED. 6 sources: US DOJ safety-zone withdrawal (Arnold&Porter), Canada Competitor Collaboration Guidelines + draft ACCA, PIPEDA/C-27 de-id, property-in-data (Hastings), data-trust entity forms (Ada Lovelace). KEY: Feb-2023 DOJ withdrawal removed US bright-line safe harbors → case-by-case only; Canada two-track clearer (legal-certainty edge for Canada-first). No property in data → rights are contractual.
- [x] Task 6 — Stream 4 regulatory — GROUNDED. 7 sources (Canada Consumer-Driven Banking + PIPEDA data-mobility right, US info-blocking/TEFCA, ISED Voluntary GenAI Code, AIDA-death, Ag Data Transparent, EU Data Act ref). KEY: NO regulation compels/funds cross-competitor pooling — only consumer/holder-directed PORTABILITY exists. AIDA dead; Canada has no binding AI statute; US deregulatory. 'Why Canada' must rest on the economy-wide data-mobility right + strategy/funding, NOT regulatory compulsion.
- [x] Task 7 — Stream 5 governmental/policy (SPINE) — GROUNDED. 7 sources (Sovereign Compute Strategy, Pan-Canadian Phase 2, C.D. Howe missing-pillar, FNIGC/OCAP, Scale AI, NAIRR US-contrast, IAPP data-mobility). VERDICT: Canada funds talent/commercialization/COMPUTE, NOT data infrastructure — no funded mechanism for a data collective. 'Why Canada' rests on (a) CAN/DGSI 100-7 governance standard, (b) economy-wide data-mobility right, (c) data-sovereignty framing — NOT funding/mandate. Compute strategy is a distraction for a data play. Validates user's rhetoric-vs-mechanism skepticism.
- [x] Task 8 — Stream 6 academic — GROUNDED. 6 sources (GKC/Constructing-Commons, Ostrom 8 principles, data-as-labor AEA, Vincent 2025 collective bargaining, Jonker + Duncan critiques). VERDICT: strong theory, near-absent empirics, every org form has a distinct fragility; collectives solving collective-action was REFUTED in verification. Enabling regulation may be a precondition (Jonker). Convergent with S0 failures + S1 substitutes.
- [x] Task 9 — Stream 7 industrial — GROUNDED. 6 sources (Early Warning Services + Cifas = genuine fraud-utility pooling; LexisNexis = aggregation contrast; a16z data-moat debate; Datavault aspirational; Catena-X SME stall ref). KEY: real cross-competitor pooling concentrates in FRAUD/AML utilities (pool the non-rivalrous signal). Agentic zero-precedent now CONFIRMED across 3 streams (0,2,7). Stream 7 verification partly truncated by Anthropic spend cap.
- [x] Task 10 — synthesis COMPLETE (analysis). docs/research/synthesis-policy-market.md answers the north-star + full confidence/uncertainty ledger. DEFERRED (external cap, not blocking): the citation-grounded wiki synthesis PAGE via wiki query — file on Anthropic spend-cap reset. wiki answer stays 401-blocked. Agentic targeted pass cancelled (zero-precedent confirmed 3x).
- Task 11 (condo application leg) is Stage 2 — separate session/loop, NOT this loop.

**Guardrails (every Task):** foundation pages domain-neutral (no reserve-study /
condo / Longspan terms — that is Stage 2); citations mandatory (`[[sources/<id>]]`,
`--draft` then `wiki finalize`); adversarial verification before filing load-bearing
claims; date precedents, flag pre-2023 for AI-model claims; `wiki retrieve`/`context`
only, never dump index.md/log.md.

**Per-stream recipe (learned in Task 2 — REUSE):**
1. deep-research workflow → verified findings + source URLs.
2. `wiki ingest "<url>" --with-plan --draft --domain data-collectives` per source
   (authorship path = Max-OAuth `claude -p`, WORKS).
3. For obviously-in-domain sources the strict filter put in review/rejected:
   `wiki filter-correct <id> --include --rationale "…" --domain data-collectives`
   then RE-INGEST `--with-plan` (correction alone does not author the source page).
4. Grounded concept/entity/source pages = the canonical stream deliverable.
5. Preserve the analytical findings + adversarial caveats + open questions in
   `docs/research/data-collectives/stream-N-*.md` (project doc, NOT wiki — avoids
   direct-write violation; feeds Task 10 + condo Stage 2).
6. Verify with `wiki retrieve`; commit. STAGING DISCIPLINE: never `git add -u wiki/`
   or `git add wiki/` — the working tree has a pre-existing condo backlog of
   modified/untracked pages (leave alone). Stage ONLY this stream's files by content
   match: `git ls-files --others --exclude-standard wiki/ raw/ | grep -lE data-collectives`
   plus the specific source IDs; add docs/research note + session-state + index.md +
   log.md + .knowledge/policies/data-collectives explicitly.

**AUTH CONSTRAINT (blocks `wiki answer` / SDK path):** `ANTHROPIC_API_KEY_RESEARCH`
returns 401 (invalid). So `wiki answer` and any SDK-cached call FAIL. Do NOT use
`wiki answer` per stream. The Max-OAuth `claude -p` path (filter / plan / --with-plan
authorship) WORKS. Final synthesis (Task 10) goes through `wiki query` (NotebookLM,
separate browser auth) once the corpus is rich — corpus-quality gate first.
Known authorship friction: the LLM sometimes picks entity_kind values outside the
controlled enum (consortium/proposal/project) → that entity page fails but the
source + other pages still commit. Not blocking.

---

## RESOLVED

**RAG retrieval build — DONE and MERGED to main (2026-06-09).** All 6 workstreams
landed; 2002 tests pass; recall@5 0.889 / recall@10 0.926 / MRR 0.722. Deferred WS7
hybrid vector retrieval (trigger: golden recall@10 < ~0.8 or ~10k pages — unmet).
`main` was 9 ahead of `origin/main` at that checkpoint; push remains the user's call.

Carry-forward (pre-existing, untouched): schema-drift ~208; finalize-batch ~460;
orphans (condo-capital-infra, glp1-reward-modulation, ai-native-business); edge-ai
notebook quota; `wiki migrate` stub; orita-cmo R3/R2; iOS Shortcut; web-API hardening.

---

## Files mid-edit

None. Working tree carries pre-existing untracked gateway-managed `nlm/`/`raw/`/`wiki/`
content (gateway-owned — leave alone).

---

## Next atomic step

**Loop is PAUSED (see top block).** On explicit user "go":

1. Task 4 GROUNDED (done). Optionally backfill ACM-Queue + OPAL alt URLs later.
2. Task 6 (CURRENT) — Stream 4 regulatory: sector data-sharing mandates & safe harbors; AI-regulation status (Canada AIDA — note it died with C-27; US federal EO + state AI laws); open-banking/data-portability mandates as structural precedent for compelled/incentivized pooling.
Loop COMPLETE. Remaining (explicit user trigger only): (1) on Anthropic spend-cap reset, file the citation-grounded wiki synthesis page (wiki query over domain, corpus-quality gate first) from docs/research/synthesis-policy-market.md; finalize drafts (wiki finalize). (2) Stage 2 condo application leg — separate session/loop per the spec's child prompt.
4. **Before Task 10**, run ONE targeted deep-research on agentic-AI / vertical-AI on
   pooled proprietary data (2024–2026) — both Stream 0 and Stream 2 found ZERO verified
   agentic precedent; this gap is load-bearing for the "why now" synthesis.
5. Task 10 synthesis via `wiki query` (NLM, corpus-quality gate first; `wiki answer`
   stays blocked on the 401 research key).

**Recurring agentic-gap finding (carry to Task 10):** privacy-preserving pooling
substrate is mature; the agentic layer on top is greenfield — no verified 2023–2026
precedent. Opportunity vs warning is the central "why now" tension.
