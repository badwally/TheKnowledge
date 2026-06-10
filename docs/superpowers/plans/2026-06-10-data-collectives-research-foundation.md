# Data Collectives Research Foundation — Implementation Plan

> **For agentic workers:** This plan is executed as a **self-paced loop**: one
> Task per iteration, checkpoint to `docs/session-state.md`, commit, schedule
> the next. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up the citation-grounded `data-collectives` wiki domain and
execute the Approach-C agentic research program (precedent-first seed → parallel
dimensional streams → policy/market synthesis) defined in
`docs/superpowers/specs/2026-06-10-data-collectives-research-foundation-design.md`.

**Architecture:** Each research stream runs via the **deep-research** skill
(web fan-out + adversarial verification → cited findings), then the verified
key sources are ingested into the domain via `wiki ingest --with-plan`, then a
concept/synthesis page is authored citing them. NotebookLM (`wiki query`) is
reserved for the final synthesis, gated on corpus quality. Markdown stays
canonical; the FTS index is derived.

**Tech Stack:** `~/code/knowledge/.venv/bin/wiki` gateway (bootstrap-domain,
ingest, query, lint, retrieve, finalize), the `deep-research` skill, web search.

**Execution mechanism:** `/loop` self-paced. The loop prompt re-enters this
plan, reads `docs/session-state.md` to find the next unchecked Task, executes
it, commits, checkpoints, and schedules the next iteration.

---

## Conventions for every Task

- **Domain neutrality (hard):** foundation pages must NOT contain reserve-study
  vocabulary, condo jurisdictions, or Longspan framing. That is Stage 2.
- **Citation grounding:** every claim ends with `[[sources/<id>]]`. Ingest with
  `--draft` while provenance settles; `wiki finalize` within 7 days.
- **Adversarial verification:** before a load-bearing claim is filed, the
  deep-research pass must have surfaced and recorded the strongest
  counter-evidence.
- **Recency:** date every precedent; flag pre-2023 sources when used for an
  AI-model claim.
- **Context discipline:** use `wiki retrieve` / `wiki context`; never read
  `index.md` or `log.md` wholesale.
- **Per-Task commit** of all new/changed files under `wiki/`, `raw/`,
  `.knowledge/`, plus the session-state checkpoint.

---

## Task 1: Bootstrap the `data-collectives` domain

**Files:**
- Create: `.knowledge/policies/data-collectives/` (gateway-generated)

- [ ] **Step 1: Bootstrap the domain**

```bash
cd /Users/andrewgrant/code/knowledge
.venv/bin/wiki bootstrap-domain "Data collectives: the mechanism by which otherwise-competing or complementary stakeholders commit proprietary data to a shared model or service that all members use to compete in a market. Covers the economic/incentive, technical/architectural, legal, regulatory, governmental/policy, academic, and industrial dimensions, with emphasis on the US and Canada (Canada primary) and on agentic vertical-AI models built on pooled proprietary data. Includes data cooperatives, data trusts, data commons, federated-learning consortia, data clean rooms, and industry data exchanges. Excludes generic open data, open source, and pure data-resale marketplaces except as contrast." data-collectives
```

- [ ] **Step 2: Verify the policy exists and inspect thresholds**

```bash
ls .knowledge/policies/data-collectives/ && cat .knowledge/policies/data-collectives/policy.* 2>/dev/null | head -40
```
Expected: a policy file exists. If bootstrap produced a *proposal* instead,
run `.venv/bin/wiki promote-domain data-collectives` and re-verify.

- [ ] **Step 3: Lint**

```bash
.venv/bin/wiki lint 2>&1 | tail -20
```
Expected: no new errors attributable to the bootstrap.

- [ ] **Step 4: Checkpoint + commit**

Update `docs/session-state.md` (mark Task 1 done, Task 2 next), then:
```bash
git add .knowledge/policies/data-collectives docs/session-state.md
git commit -m "feat(data-collectives): bootstrap domain"
```

---

## Task 2: Stream 0 — Precedent census (seed)

**Goal:** taxonomy + case file of real pooled-data ventures. Runs first; seeds
all later streams.

**Seed sub-topics (use as deep-research scope):** data cooperatives (e.g.
Driver's Seat, Salus Coop, MIDATA, Swash); data trusts (ODI data trusts, UK
Data Trust pilots); data commons (Ostrom-style, MOBILITYDATA/GBFS, Genomic
Data Commons); federated-learning consortia (MELLODDY pharma, Owkin, NVIDIA
FLARE deployments); data clean rooms / collaboratives (GDC, advertising clean
rooms); industry data exchanges; **agentic vertical-AI models on pooled data
(2023–2026)**. Per case: structure, contributors, the incentive that overcame
"give up my edge," governance, outcome incl. failures.

- [ ] **Step 1: Run the deep-research pass** — invoke the `deep-research` skill
  with the seed sub-topics above, scoped to US + Canada (EU reference-only),
  instructing it to return per-case structured findings with source URLs and
  recorded counter-evidence.

- [ ] **Step 2: Ingest the 6–10 strongest verified sources**

```bash
cd /Users/andrewgrant/code/knowledge
.venv/bin/wiki ingest "<url>" --with-plan --draft --domain data-collectives
# repeat per source
```

- [ ] **Step 3: Author the taxonomy synthesis page** via the wiki authorship
  path (the `--with-plan` ingest will draft entity/concept pages; ensure a
  `synthesis` page titled "Pooled-data venture taxonomy" exists and cites the
  ingested `[[sources/<id>]]`). Verify each case row has provenance.

- [ ] **Step 4: Verify pages + grounding**

```bash
.venv/bin/wiki retrieve "pooled data venture taxonomy" --domain data-collectives | head -40
.venv/bin/wiki lint --scope orphans 2>&1 | tail -10
```
Expected: taxonomy page returned; ingested sources have inbound citations.

- [ ] **Step 5: Checkpoint + commit**

```bash
git add wiki/ raw/ .knowledge/ docs/session-state.md
git commit -m "feat(data-collectives): Stream 0 precedent census"
```

---

## Tasks 3–9: Streams 1–7 (parallel dimensions)

Each stream repeats the Task-2 pattern (deep-research → ingest verified sources
→ author concept/synthesis pages → verify → commit). Stream-specific scope:

### Task 3 — Stream 1: Economic / incentive
Scope: cooperative game theory; data-as-asset valuation; value-distribution
mechanisms (Shapley-value data pricing, data Shapley); free-rider & defection
dynamics; the contribute-your-edge paradox and documented resolutions
(complementary-not-substitute data, delayed/aggregated release, tiered access).
Commit: `feat(data-collectives): Stream 1 economic/incentive`

### Task 4 — Stream 2: Technical / architecture
Scope: federated learning, differential privacy, secure multiparty computation,
data clean rooms, model-sharing vs data-sharing trade-offs; **agentic
architecture** — agents as contributors, consumers, and governors of the pool.
Cross-link `edge-ai-agentic`, `ai-and-agents`.
Commit: `feat(data-collectives): Stream 2 technical/architecture`

### Task 5 — Stream 3: Legal
Scope: data ownership & trade-secret status of pooled data; **antitrust /
competition law on competitor data-sharing** (US DOJ/FTC guidance, Canada
Competition Bureau); privacy (PIPEDA, Québec Law 25, US state regimes; GDPR
reference); liability allocation among contributors.
Commit: `feat(data-collectives): Stream 3 legal`

### Task 6 — Stream 4: Regulatory
Scope: sector data-sharing mandates & safe harbors; AI-regulation status
(Canada AIDA, US federal EO + state AI laws); open-banking / data-portability
mandates as structural precedent for compelled or incentivized pooling.
Commit: `feat(data-collectives): Stream 4 regulatory`

### Task 7 — Stream 5: Governmental / policy (SPINE CORE)
Scope: Pan-Canadian AI Strategy, sovereign-compute strategy, data-sovereignty &
data-governance standardization (CIO Strategy Council / SCC), federal &
provincial data-collaborative funding programs; build the explicit **"why
Canada"** argument; contrast with US posture. Cross-link `ai-native-business`.
Commit: `feat(data-collectives): Stream 5 governmental/policy`

### Task 8 — Stream 6: Academic
Scope: data-cooperative literature (data dignity / RadicalxChange / MIT data
co-ops), federated-learning research, Ostrom commons governance, mechanism
design for data, data-market & two-sided-platform economics.
Commit: `feat(data-collectives): Stream 6 academic`

### Task 9 — Stream 7: Industrial
Scope: who is doing this now by sector (health, finance, mobility,
manufacturing); vertical-AI startups monetizing pooled proprietary data;
competitive-moat dynamics; EU data spaces (Gaia-X, Catena-X) as reference
precedent only.
Commit: `feat(data-collectives): Stream 7 industrial`

Each of Tasks 3–9, concretely:
- [ ] deep-research pass on the stream scope (US+Canada, recency-weighted,
  counter-evidence recorded)
- [ ] `wiki ingest "<url>" --with-plan --draft --domain data-collectives` per
  verified source (4–8 sources)
- [ ] ensure a stream `synthesis` page + supporting `concept`/`entity` pages
  exist and cite `[[sources/<id>]]`; end with an open-questions list
- [ ] `wiki retrieve "<stream topic>" --domain data-collectives | head -40` and
  `wiki lint --scope orphans` to verify grounding
- [ ] checkpoint `docs/session-state.md` + commit with the message above

---

## Task 10: Corpus-quality gate + policy/market synthesis

**Goal:** answer the north-star with a defensible position + uncertainty ledger.

- [ ] **Step 1: Corpus-quality gate**

```bash
cd /Users/andrewgrant/code/knowledge
.venv/bin/wiki search "data collective" --domain data-collectives --order tiered | head -30
# sample word counts on 5–10 ingested raw sources; if median body < ~800 words
# OR majority are stubs, ingest more full-text sources before synthesis.
```
Expected: median source body ≥ ~800 words; if not, loop back and ingest before
proceeding (sparse corpora confabulate under NotebookLM).

- [ ] **Step 2: Run the synthesis**

```bash
.venv/bin/wiki query "Is there a policy- and market-structure opening, emphatically in Canada and benchmarked against the US, for stakeholder-pooled industry-specific AI built on proprietary data committed by otherwise-competing firms? Who captures that market, and what does the agentic shift change about the answer? Ground the answer in the data-collectives streams; order the economic, technical, legal, regulatory, academic, and industrial findings under the policy/market-structure spine." --domain data-collectives --draft
```

- [ ] **Step 3: Add the confidence / uncertainty ledger.** Append an explicit
  `## Confidence & open questions` section to the synthesis page enumerating
  load-bearing claims, their evidence strength, and what would resolve the
  thin ones. Attribute framing prose with `wiki cite`, then `wiki finalize`
  the page.

- [ ] **Step 4: Verify**

```bash
.venv/bin/wiki retrieve "why Canada stakeholder-pooled industry AI" --domain data-collectives | head -50
.venv/bin/wiki lint 2>&1 | tail -20
```
Expected: synthesis returned; no grounding errors; no stale drafts.

- [ ] **Step 5: Checkpoint + commit**

```bash
git add wiki/ raw/ .knowledge/ docs/session-state.md
git commit -m "feat(data-collectives): policy/market synthesis + uncertainty ledger"
```

---

## Task 11 (Stage 2 — separate session): Condo application leg

Out of scope for this loop. When triggered, execute the stubbed child prompt in
the design spec: derive the engineering-firm + PM + HOA reserve-study collective
from the foundation, citing both `data-collectives` and `condo-capital-infra`.
Do **not** re-research condo specifics. New plan, new loop.

---

## Done criteria for this loop

- Tasks 1–10 checked.
- `data-collectives` domain holds: a precedent taxonomy, seven dimensional
  synthesis pages (each with an open-questions list), and one policy/market
  synthesis answering the north-star with an uncertainty ledger.
- `wiki lint` clean; no stale drafts; every claim grounded.
- `docs/session-state.md` reflects completion; Stage 2 logged as the next arc.
