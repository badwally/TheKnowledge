# Session state — 2026-06-10

Last updated: 2026-06-10 (new arc: data-collectives research foundation — loop execution starting)

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
- [ ] Task 4 — Stream 2 technical/architecture
- [ ] Task 5 — Stream 3 legal
- [ ] Task 6 — Stream 4 regulatory
- [ ] Task 7 — Stream 5 governmental/policy (spine core)
- [ ] Task 8 — Stream 6 academic
- [ ] Task 9 — Stream 7 industrial
- [ ] Task 10 — corpus-quality gate + policy/market synthesis + uncertainty ledger
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
6. Verify with `wiki retrieve`; commit.

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

Execute **Task 4** — Stream 2 technical/architecture. deep-research over federated
learning, differential privacy, secure multiparty computation, data clean rooms,
model-sharing vs data-sharing, and the AGENTIC architecture (agents as contributors /
consumers / governors of the pool; how agentic AI changes the trust/contribution
calculus). Then per-stream recipe. Cross-link edge-ai-agentic, ai-and-agents. Advance
to Task 5 (Stream 3 legal).
