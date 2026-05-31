# AI-Native Operator Playbook Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `ai-native-business` wiki domain — a substrate-first operator playbook for a solo founder + AI — with 4 pillar syntheses, 3 archetype specializations, a definitional concept anchor, an MoC, and 85-110 grounded sources.

**Architecture:** Domain-scoped gateway workflow. Bootstrap the domain (1 step). Use `wiki research --review` + `--execute` per pillar/archetype to discover sources, build the NotebookLM corpus, and file draft syntheses (7 research sessions). Use Gmail MCP for Substack-subscription discovery, then `wiki ingest <url>` per discovered URL. Use `wiki query` for the definitional concept page. Finalize drafts, backfill entities, write the MoC, lint-clean.

**Tech Stack:** `wiki` CLI (gateway), NotebookLM via gateway, Gmail MCP (read-only discovery), git for local-artifact commits. All wiki/raw writes flow through the gateway — never directly.

**Reference spec:** `docs/superpowers/specs/2026-05-23-ai-native-business-playbook-design.md`

**Approval gates:** Tasks 1, 2, 3-9 (per research session), 10, 11, 13, 14 require user approval before execution proceeds. These are explicitly marked.

**Hard rules in force throughout:** No direct writes to `wiki/` or `raw/`; all changes go through the gateway. Citation grounding mandatory (drafts permitted via `--draft`, must be finalized within 7 days). Lookup before create. Plan before write. Sources in `raw/` are immutable.

---

## File / artifact map

Final state after plan execution:

| Artifact | Path | Source of write |
|---|---|---|
| Domain policy | `.knowledge/policies/ai-native-business/policy.yaml` | `wiki bootstrap-domain` |
| MoC | `wiki/mocs/ai-native-business.md` | `wiki query` (Task 13) |
| Concept anchor | `wiki/concepts/ai-native-substrate.md` | `wiki query` (Task 10) |
| Pillar syntheses (4) | `wiki/synthesis/ai-native-{org-and-operating-model,economics-and-capital,tech-stack-and-build-vs-buy,gtm-pricing-defensibility}.md` | `wiki research --execute` (Tasks 2-5) |
| Archetype syntheses (3) | `wiki/synthesis/archetype-{indie-saas-vertical-agent,services-firm,marketplace-aggregator}.md` | `wiki research --execute` (Tasks 6-8) |
| Entity pages (~20-30) | `wiki/entities/<slug>.md` | Auto-backfilled during research + Task 12 |
| Source pages (~85-110) | `wiki/sources/<id>.md` | Auto-generated during research / ingest |
| Raw sources | `raw/{web,youtube,arxiv,pdf,audiobook}/...` | `wiki research`, `wiki ingest` |
| Query plan YAMLs (7) | `nlm/query_plans/2026-05-23-ai-native-*.yaml` | `wiki research --review` (Tasks 2-8) |

---

## Task 1: Bootstrap the `ai-native-business` domain

**Files:** policy created at `.knowledge/policies/ai-native-business/policy.yaml`; MoC stub at `wiki/mocs/ai-native-business.md`; NLM notebook entry added to `nlm/notebooks.yaml`.

- [ ] **Step 1: Draft the domain description**

Use this text verbatim as the `description` argument:

```
The technical, operational, and economic substrate of an "AI-native"
business — what it means to build a company where AI is the operating
substrate rather than a bolt-on feature. Focus is on the solo-founder
and tiny-team archetype: one operator + many AI agents, bootstrapped
or pre-seed. Covers four pillars: org and operating model (roles for
humans vs. agents, automation order, decision cadence); economics
and capital (cost structure, gross margin, revenue-per-human,
bootstrapped vs. revenue-financed vs. seed paths); tech stack and
build-vs-buy (model selection, evals as a core function, observability,
vendor-primitive composition); GTM, pricing, and defensibility (PLG
and founder-led acquisition, seat/usage/outcome pricing, where moats
form when models are commoditized). Three archetype specializations:
AI-native indie SaaS / vertical agent (solo software builders, e.g.,
Cursor/Anysphere class plus solo-buildable variants like Pieter Levels);
AI-native services firm (one operator + agents running client work in
domains like marketing, bookkeeping, paralegal, recruiting); AI-native
marketplace/aggregator (operator runs the platform, AI does matching,
vetting, and ops). Substrate-first framing: the offering may or may
not be AI itself, but the operating model assumes AI is the substrate
the business runs on. Sources are case studies of named AI-native
companies, VC and operator essays, books on AI in business, academic
productivity research, founder podcasts and conference talks, and
selected solo-operator primary signal.
```

- [ ] **Step 2: APPROVAL GATE — confirm description with user before running**

Show the description to the user. Ask: "Approve this domain description before bootstrap, or do you want to edit it?"

- [ ] **Step 3: Run bootstrap-domain**

```bash
.venv/bin/wiki bootstrap-domain "<paste approved description>" ai-native-business
```

Expected: writes `.knowledge/policies/ai-native-business/policy.yaml`, creates `wiki/mocs/ai-native-business.md` stub, adds entry to `nlm/notebooks.yaml`.

- [ ] **Step 4: Verify outputs**

```bash
ls .knowledge/policies/ai-native-business/
cat nlm/notebooks.yaml | grep -A 2 ai-native-business
ls wiki/mocs/ai-native-business.md
git status
```

Expected: policy file exists; notebooks.yaml has an entry; MoC stub created.

- [ ] **Step 5: Commit local artifacts**

```bash
git add nlm/notebooks.yaml .knowledge/policies/ai-native-business/
git commit -m "domain: bootstrap ai-native-business policy + notebook"
```

(`.knowledge/` and `nlm/` are tracked. `wiki/` is also tracked — the MoC stub will get committed in Task 13 once it's authored.)

---

## Task 2: Pillar 1 — Org & operating model (research + draft synthesis)

**Files:** query plan at `nlm/query_plans/2026-05-23-ai-native-org-and-operating-model.yaml`; sources land in `raw/`; draft synthesis at `wiki/synthesis/ai-native-org-and-operating-model.md`.

- [ ] **Step 1: Generate query plan via `--review`**

```bash
.venv/bin/wiki research \
  --domain ai-native-business \
  --review \
  --max-results 30 \
  "What does the org and operating model of an AI-native solo-founder / tiny-team business look like in 2026? Cover: role taxonomy for humans vs. agents, what gets automated first and in what order, agent-in-the-loop patterns (review gates, evals, escalation), decision cadence (async-default, sync exceptions), and the 'when to add a human vs. add an agent' decision rule. Include case studies of named AI-native companies (Anysphere/Cursor, Cognition, Sierra, Lindy, Crosby, Mercor, Harvey, Decagon) and solo operators (Pieter Levels, Marc Lou). Include academic productivity research (Brynjolfsson, Mollick, GitHub Copilot studies, BCG×Harvard AI experiment) and founder podcast appearances (Acquired, Lenny's, Latent Space, 20VC, AI Native Dojo)."
```

Expected: persists `nlm/query_plans/2026-05-23-ai-native-org-and-operating-model.yaml` and stops (review mode).

- [ ] **Step 2: APPROVAL GATE — user reviews and edits the query plan**

Open the YAML, review per-adapter queries (web, youtube, arxiv, etc.), edit if needed. User confirms: "ready to execute" or returns edits.

- [ ] **Step 3: Execute the plan**

```bash
.venv/bin/wiki research --execute 2026-05-23-ai-native-org-and-operating-model
```

Expected: fans out queries → filter → ingest to `raw/` → sync to NLM corpus → file `wiki/synthesis/ai-native-org-and-operating-model.md` with `draft: true`.

- [ ] **Step 4: Spot-check outputs**

```bash
.venv/bin/wiki status
ls raw/web/ raw/youtube/ raw/arxiv/ 2>/dev/null | wc -l
head -50 wiki/synthesis/ai-native-org-and-operating-model.md
git status
```

Expected: new sources in `raw/`, new source pages in `wiki/sources/`, new entity pages auto-generated, draft synthesis exists.

- [ ] **Step 5: Filter triage (only if needed)**

Review filter decisions for anything obviously miscategorized:

```bash
.venv/bin/wiki status --filter-decisions 2>/dev/null || true
# For each clear miscategorization:
.venv/bin/wiki filter-correct <source-id>
```

Skip this step if filter scores look reasonable.

- [ ] **Step 6: Commit query plan**

```bash
git add nlm/query_plans/2026-05-23-ai-native-org-and-operating-model.yaml
git commit -m "research(ai-native-business): pillar 1 — org & operating model query plan"
```

(Source pages, raw files, and synthesis are auto-committed by the gateway watcher / not git-tracked depending on path — check `git status` to see what's pending and either commit or note the local-only nature.)

---

## Task 3: Pillar 2 — Economics & capital (research + draft synthesis)

**Files:** query plan at `nlm/query_plans/2026-05-23-ai-native-economics-and-capital.yaml`; draft synthesis at `wiki/synthesis/ai-native-economics-and-capital.md`.

- [ ] **Step 1: Generate query plan via `--review`**

```bash
.venv/bin/wiki research \
  --domain ai-native-business \
  --review \
  --max-results 30 \
  "What are the economics and capital path of an AI-native solo-founder / tiny-team business in 2026? Cover: cost structure (compute, vendor primitives like model APIs and embeddings, data, human time), gross margin profile vs. legacy SaaS / legacy services / legacy marketplace, revenue-per-human benchmarks (Anysphere, Midjourney, Telegram, Plenty of Fish, Craigslist as comparators), time-to-revenue norms, and bootstrapped vs. revenue-financed vs. seed-funding paths. Include the 'AI compute as variable cost' reshaping of unit economics. Sources: VC pieces (a16z, Sequoia, Benchmark, Felicis) on AI-native economics, operator essays on capital efficiency, Stripe/First Round / Lenny content on AI-native unit economics, academic work on AI productivity gains (Brynjolfsson, BCG×Harvard), and named-company financial disclosures."
```

- [ ] **Step 2: APPROVAL GATE — user reviews and edits the query plan**

- [ ] **Step 3: Execute the plan**

```bash
.venv/bin/wiki research --execute 2026-05-23-ai-native-economics-and-capital
```

- [ ] **Step 4: Spot-check outputs**

```bash
.venv/bin/wiki status
head -50 wiki/synthesis/ai-native-economics-and-capital.md
git status
```

- [ ] **Step 5: Commit query plan**

```bash
git add nlm/query_plans/2026-05-23-ai-native-economics-and-capital.yaml
git commit -m "research(ai-native-business): pillar 2 — economics & capital query plan"
```

---

## Task 4: Pillar 3 — Tech stack & build-vs-buy (research + draft synthesis)

**Files:** query plan at `nlm/query_plans/2026-05-23-ai-native-tech-stack-and-build-vs-buy.yaml`; draft synthesis at `wiki/synthesis/ai-native-tech-stack-and-build-vs-buy.md`.

- [ ] **Step 1: Generate query plan via `--review`**

```bash
.venv/bin/wiki research \
  --domain ai-native-business \
  --review \
  --max-results 30 \
  "What is the AI-native technical stack and build-vs-buy default in 2026 for a solo or tiny-team operator? Cover: model selection discipline (frontier vs. cheap-and-fast vs. open-weight, orchestration patterns), evals as a core operating function, observability for agentic systems, the 'compose vendor primitives until proven wrong' default, when proprietary infra is actually warranted, data flywheels (real moats vs. cope), and AI-native infra defaults (serverless, vector stores, queueing, trace tooling). Resist becoming a tool list — focus on selection criteria. Sources: AI Engineer Summit talks, Latent Space episodes on production AI, operator blogs on evals and observability, vendor case studies (Anthropic, OpenAI, LangSmith, Braintrust), AI Engineer essays."
```

- [ ] **Step 2: APPROVAL GATE — user reviews and edits the query plan**

- [ ] **Step 3: Execute the plan**

```bash
.venv/bin/wiki research --execute 2026-05-23-ai-native-tech-stack-and-build-vs-buy
```

- [ ] **Step 4: Spot-check outputs**

```bash
.venv/bin/wiki status
head -50 wiki/synthesis/ai-native-tech-stack-and-build-vs-buy.md
git status
```

- [ ] **Step 5: Commit query plan**

```bash
git add nlm/query_plans/2026-05-23-ai-native-tech-stack-and-build-vs-buy.yaml
git commit -m "research(ai-native-business): pillar 3 — tech stack & build-vs-buy query plan"
```

---

## Task 5: Pillar 4 — GTM, pricing & defensibility (research + draft synthesis)

**Files:** query plan at `nlm/query_plans/2026-05-23-ai-native-gtm-pricing-defensibility.yaml`; draft synthesis at `wiki/synthesis/ai-native-gtm-pricing-defensibility.md`.

- [ ] **Step 1: Generate query plan via `--review`**

```bash
.venv/bin/wiki research \
  --domain ai-native-business \
  --review \
  --max-results 30 \
  "How does an AI-native solo or tiny-team business approach GTM, pricing, and defensibility in 2026? Cover: acquisition channels that work for a solo AI-native (PLG, founder-led content, embedded distribution, agent-marketplace listings); pricing axes (per-seat vs. usage vs. outcome) and when each fits which archetype; where moats actually form when foundation models are commoditized (workflow lock-in, data flywheels, distribution, brand, switching cost, integration depth); the 'thin wrapper' critique and when it's fair vs. lazy; defensibility for services-firm and marketplace archetypes (where moats differ from SaaS). Sources: VC essays on AI moats (a16z, Sequoia, Benchmark), operator essays on AI pricing (Kyle Poyar, Lenny, First Round, ProductLed), named-company pricing disclosures, AI-native services / marketplace case studies."
```

- [ ] **Step 2: APPROVAL GATE — user reviews and edits the query plan**

- [ ] **Step 3: Execute the plan**

```bash
.venv/bin/wiki research --execute 2026-05-23-ai-native-gtm-pricing-defensibility
```

- [ ] **Step 4: Spot-check outputs**

```bash
.venv/bin/wiki status
head -50 wiki/synthesis/ai-native-gtm-pricing-defensibility.md
git status
```

- [ ] **Step 5: Commit query plan**

```bash
git add nlm/query_plans/2026-05-23-ai-native-gtm-pricing-defensibility.yaml
git commit -m "research(ai-native-business): pillar 4 — GTM, pricing & defensibility query plan"
```

---

## Task 6: Archetype A — Indie SaaS / vertical agent

**Files:** query plan at `nlm/query_plans/2026-05-23-archetype-indie-saas-vertical-agent.yaml`; draft synthesis at `wiki/synthesis/archetype-indie-saas-vertical-agent.md`.

- [ ] **Step 1: Generate query plan via `--review`**

```bash
.venv/bin/wiki research \
  --domain ai-native-business \
  --review \
  --max-results 25 \
  "What is the AI-native indie SaaS / vertical agent archetype for a solo founder in 2026? Cover: definition (what this archetype is and isn't), funded exemplars (Cursor/Anysphere, Cognition/Devin, Lindy, Crosby, Decagon, Sierra) and solo-buildable variants (Pieter Levels with Nomad List and Photo AI, Marc Lou's portfolio, other single-operator vertical agents); how the four pillars (org, economics, tech, GTM) specialize for this archetype; defensibility specific to vertical agents (workflow lock-in, integration depth, eval moat); pricing trajectory (seat → usage → outcome); go/no-go signals for a solo founder. Include a worked example walked through the four pillars."
```

- [ ] **Step 2: APPROVAL GATE — user reviews and edits the query plan**

- [ ] **Step 3: Execute the plan**

```bash
.venv/bin/wiki research --execute 2026-05-23-archetype-indie-saas-vertical-agent
```

- [ ] **Step 4: Spot-check outputs**

```bash
.venv/bin/wiki status
head -50 wiki/synthesis/archetype-indie-saas-vertical-agent.md
git status
```

- [ ] **Step 5: Commit query plan**

```bash
git add nlm/query_plans/2026-05-23-archetype-indie-saas-vertical-agent.yaml
git commit -m "research(ai-native-business): archetype A — indie SaaS / vertical agent query plan"
```

---

## Task 7: Archetype B — Services firm

**Files:** query plan at `nlm/query_plans/2026-05-23-archetype-services-firm.yaml`; draft synthesis at `wiki/synthesis/archetype-services-firm.md`.

- [ ] **Step 1: Generate query plan via `--review`**

```bash
.venv/bin/wiki research \
  --domain ai-native-business \
  --review \
  --max-results 25 \
  "What is the AI-native services firm archetype for a solo or tiny-team operator in 2026? Cover: definition (AI-native marketing studio, bookkeeping shop, recruiting firm, paralegal services, content production); referents at the funded end (Mercor, Harvey, Crosby, Decagon) and the lean-operator end (one-person agencies, AI-leveraged consultancies, productized services); how the four pillars (org, economics, tech, GTM) specialize — especially economics (hourly/retainer collapse as AI substrate replaces hours, pricing pivot to outcomes) and defensibility (client relationships, workflow integration, reputation — not data); go/no-go signals; worked example. Include the 'service as software' framing and the productized-service vs. project-services spectrum."
```

- [ ] **Step 2: APPROVAL GATE — user reviews and edits the query plan**

- [ ] **Step 3: Execute the plan**

```bash
.venv/bin/wiki research --execute 2026-05-23-archetype-services-firm
```

- [ ] **Step 4: Spot-check outputs**

```bash
.venv/bin/wiki status
head -50 wiki/synthesis/archetype-services-firm.md
git status
```

- [ ] **Step 5: Commit query plan**

```bash
git add nlm/query_plans/2026-05-23-archetype-services-firm.yaml
git commit -m "research(ai-native-business): archetype B — services firm query plan"
```

---

## Task 8: Archetype C — Marketplace / aggregator

**Files:** query plan at `nlm/query_plans/2026-05-23-archetype-marketplace-aggregator.yaml`; draft synthesis at `wiki/synthesis/archetype-marketplace-aggregator.md`.

- [ ] **Step 1: Generate query plan via `--review`**

```bash
.venv/bin/wiki research \
  --domain ai-native-business \
  --review \
  --max-results 25 \
  "What is the AI-native marketplace / aggregator archetype for a solo or tiny-team operator in 2026? Cover: definition (AI mediates supply/demand or aggregates fragmented work; operator runs the platform, AI does matching, vetting, ops, dispute resolution); examples in AI-mediated recruiting, freelance-work brokering, supplier matching, content-rights aggregation; how the four pillars specialize — especially economics (variable cost per transaction, take rate vs. SaaS subscription) and defensibility (liquidity moat, integration depth, workflow lock-in); why this is the hardest archetype for solo operators (cold-start problem, two-sided liquidity); explicit conservative go/no-go signals; worked example. Include comparison to pre-AI marketplaces (Craigslist, Thumbtack, Upwork) to clarify what 'AI-native' adds."
```

- [ ] **Step 2: APPROVAL GATE — user reviews and edits the query plan**

- [ ] **Step 3: Execute the plan**

```bash
.venv/bin/wiki research --execute 2026-05-23-archetype-marketplace-aggregator
```

- [ ] **Step 4: Spot-check outputs**

```bash
.venv/bin/wiki status
head -50 wiki/synthesis/archetype-marketplace-aggregator.md
git status
```

- [ ] **Step 5: Commit query plan**

```bash
git add nlm/query_plans/2026-05-23-archetype-marketplace-aggregator.yaml
git commit -m "research(ai-native-business): archetype C — marketplace / aggregator query plan"
```

---

## Task 9: Substack-from-inbox discovery and ingest

**Files:** discovery notes (local, untracked); sources land in `raw/web/` via `wiki ingest`.

- [ ] **Step 1: Enumerate Substack subscriptions via Gmail MCP**

Use `mcp__claude_ai_Gmail__search_threads` with queries like:
- `from:substack.com`
- `list:substack.com`
- `from:*.substack.com newer_than:90d`

Aggregate distinct sender domains / publication names.

- [ ] **Step 2: Filter to AI-native-business-relevant subscriptions**

Cross-reference against the four pillars (org, economics, tech, GTM) and three archetypes. Drop subscriptions that are clearly off-topic (e.g., investing, hobbies). Keep AI-operator, founder, VC, AI-product, AI-engineering subscriptions.

- [ ] **Step 3: For each relevant subscription, extract canonical URLs of recent (last 90 days) high-relevance posts**

Use `mcp__claude_ai_Gmail__get_thread` to read each email and extract the canonical Substack URL (the "View in browser" / "Read in browser" link).

Target: 10-20 URLs across all relevant subscriptions.

- [ ] **Step 4: APPROVAL GATE — user reviews the URL list before ingest**

Present the list to the user with one-line context per URL (publication, post title, why it's in-scope). User approves the final list or requests trimming.

- [ ] **Step 5: Ingest each approved URL**

For each URL in the approved list:

```bash
.venv/bin/wiki ingest <substack-url> --domain ai-native-business
```

If a URL appears off-topic by the filter, use `.venv/bin/wiki filter-correct <source-id>` only after user concurs.

- [ ] **Step 6: Verify ingest**

```bash
.venv/bin/wiki status
# Count newly ingested web sources
ls -lt raw/web/ | head -25
```

- [ ] **Step 7: Add to NLM corpus**

```bash
.venv/bin/wiki nlm-sync ai-native-business
```

Expected: any newly ingested sources tagged with `ai-native-business` get added to the corresponding NotebookLM notebook.

- [ ] **Step 8: Commit any local artifacts**

The discovery notes can be committed if useful (or left untracked). Source pages and raw files follow the normal gateway-write flow.

---

## Task 10: Definitional concept page — `concepts/ai-native-substrate.md`

**Files:** `wiki/concepts/ai-native-substrate.md` (new).

- [ ] **Step 1: Lookup-before-create check**

```bash
grep -ril "ai.native.substrate\|ai-as-substrate\|ai-native " wiki/concepts/ wiki/entities/ 2>/dev/null
.venv/bin/wiki search "AI as substrate" 2>/dev/null || true
```

Expected: no existing page with overlapping scope. If a near-duplicate exists, surface to user before creating.

- [ ] **Step 2: Run `wiki query` to draft the concept page**

```bash
.venv/bin/wiki query \
  --domain ai-native-business \
  --draft \
  "Define 'AI as substrate' precisely as a concept, contrasted with 'AI as feature' and 'AI as product'. Cite the corpus. Output should be authored as wiki/concepts/ai-native-substrate.md and cite-back into the four pillar syntheses and three archetype pages. Keep it under 800 words. Substrate-first framing: the offering may or may not be AI itself, but the operating model assumes AI is the substrate the business runs on. Distinguish from 'AI-augmented' (bolt-on) and 'AI-as-product' (the offering is itself an AI product)."
```

- [ ] **Step 3: Review the drafted page**

```bash
cat wiki/concepts/ai-native-substrate.md
```

Verify: definition is precise; contrast with feature and product is explicit; citations present (or marked `draft: true`); cross-references to pillar syntheses exist.

- [ ] **Step 4: APPROVAL GATE — user reviews the concept page**

If user requests changes, re-run `wiki query` with refined prompt or use `wiki cite` to add missing citations.

- [ ] **Step 5: Finalize the page**

```bash
.venv/bin/wiki finalize wiki/concepts/ai-native-substrate.md
```

Expected: `draft: true` removed; validator re-runs with strict citation rule; page passes.

If validator rejects (uncited claims), use `wiki cite` to attach citations to flagged lines, then re-run `wiki finalize`.

- [ ] **Step 6: Commit**

```bash
git add wiki/concepts/ai-native-substrate.md wiki/sources/ 2>/dev/null
git commit -m "concept(ai-native-business): ai-native-substrate definitional anchor"
```

---

## Task 11: Finalize the four pillar + three archetype syntheses

**Files:** all seven drafts under `wiki/synthesis/ai-native-*.md` and `wiki/synthesis/archetype-*.md`.

Drafts produced by Tasks 2-8 have `draft: true`. The citation rule was downgraded to a warning during research. This task closes the loop.

- [ ] **Step 1: List all draft pages**

```bash
.venv/bin/wiki lint --scope drafts 2>/dev/null || grep -lr "^draft: true" wiki/synthesis/ai-native-*.md wiki/synthesis/archetype-*.md
```

Expected: 7 draft pages.

- [ ] **Step 2: Iterate over each draft — review + cite + finalize**

For each of the 7 pages in this order: 4 pillars, then 3 archetypes (pillars first so archetypes can cite into them).

```
wiki/synthesis/ai-native-org-and-operating-model.md
wiki/synthesis/ai-native-economics-and-capital.md
wiki/synthesis/ai-native-tech-stack-and-build-vs-buy.md
wiki/synthesis/ai-native-gtm-pricing-defensibility.md
wiki/synthesis/archetype-indie-saas-vertical-agent.md
wiki/synthesis/archetype-services-firm.md
wiki/synthesis/archetype-marketplace-aggregator.md
```

For each:

  - [ ] Read the draft. Identify uncited claims (typically interpretive openers, mid-section aggregate framing).
  - [ ] APPROVAL GATE — surface the uncited lines and proposed source attribution to the user. User approves citations.
  - [ ] Apply citations:

```bash
.venv/bin/wiki cite wiki/synthesis/<page>.md <LINE>:<source-id> [<LINE>:<source-id> ...]
```

  - [ ] Finalize:

```bash
.venv/bin/wiki finalize wiki/synthesis/<page>.md
```

  - [ ] If finalize fails, repeat cite step with additional sources or surface to user.

- [ ] **Step 3: Verify no drafts remain**

```bash
grep -lr "^draft: true" wiki/synthesis/ai-native-*.md wiki/synthesis/archetype-*.md 2>/dev/null
```

Expected: empty result.

- [ ] **Step 4: Commit**

```bash
git add wiki/synthesis/ai-native-*.md wiki/synthesis/archetype-*.md
git commit -m "synthesis(ai-native-business): finalize 4 pillar + 3 archetype syntheses"
```

---

## Task 12: Entity backfill — named companies and operators

**Files:** `wiki/entities/<slug>.md` for each referenced named entity (some auto-generated during research, some need manual attention).

The research adapter auto-generates entity stubs when sources mention named entities. This task audits and completes them.

- [ ] **Step 1: List entities created during the research sessions**

```bash
git log --diff-filter=A --name-only --since="2026-05-23" -- wiki/entities/ | sort -u
```

- [ ] **Step 2: Cross-reference against the target list**

Target list (entities the playbook should have grounded pages for; this is the reasonable-coverage bar):

```
anysphere, harvey, cognition, sierra-ai, decagon, mercor, crosby-ai,
lindy, cresta, elevenlabs, perplexity, glean, hebbia,
pieter-levels, marc-lou,
ethan-mollick, erik-brynjolfsson,
anthropic, openai
```

Plus any entities the syntheses themselves cite that aren't auto-generated.

- [ ] **Step 3: For each missing target, create the entity stub via `wiki ingest --with-plan` of a canonical source**

```bash
.venv/bin/wiki ingest <canonical-url> --domain ai-native-business --with-plan
```

The `--with-plan` flag triggers the wiki authorship agent to create/update entity + concept + synthesis pages from the new source.

- [ ] **Step 4: Spot-check the entity pages**

```bash
for slug in anysphere harvey cognition sierra-ai decagon mercor; do
  ls wiki/entities/${slug}.md 2>/dev/null && echo "  ✓ ${slug}"
done
```

- [ ] **Step 5: APPROVAL GATE — present the entity-coverage summary to user**

Show: count of auto-generated entities, count of target entities, gaps remaining. User approves moving on or requests specific additions.

- [ ] **Step 6: Commit**

```bash
git add wiki/entities/
git commit -m "entities(ai-native-business): backfill named-entity coverage"
```

---

## Task 13: MoC — `wiki/mocs/ai-native-business.md`

**Files:** `wiki/mocs/ai-native-business.md` (stub created in Task 1; fully authored here).

- [ ] **Step 1: Draft MoC via `wiki query`**

```bash
.venv/bin/wiki query \
  --domain ai-native-business \
  --draft \
  "Author the map-of-content (MoC) page at wiki/mocs/ai-native-business.md for the ai-native-business domain. Structure: (1) one-paragraph definition citing concepts/ai-native-substrate; (2) the four-pillar framework with one-sentence summary + link per pillar synthesis page; (3) the three archetype specializations with one-sentence summary + link per archetype synthesis page; (4) navigation map (named entities, key sources, related concepts); (5) reading order recommendation (concept anchor → pillars in order → archetype of interest). Cite the concept page and each pillar/archetype synthesis. Under 600 words."
```

- [ ] **Step 2: Review the MoC**

```bash
cat wiki/mocs/ai-native-business.md
```

Verify: links to all 4 pillar syntheses and all 3 archetype syntheses; links to concept anchor; navigation feels usable.

- [ ] **Step 3: APPROVAL GATE — user reviews MoC**

If user requests structural changes, re-run with refined prompt.

- [ ] **Step 4: Finalize**

```bash
.venv/bin/wiki finalize wiki/mocs/ai-native-business.md
```

- [ ] **Step 5: Commit**

```bash
git add wiki/mocs/ai-native-business.md
git commit -m "moc(ai-native-business): top-level map of content"
```

---

## Task 14: Lint pass and cleanup

**Files:** none directly; may produce small follow-up commits.

- [ ] **Step 1: Run domain-scoped lint**

```bash
.venv/bin/wiki lint
```

Expected: zero ERRORs. WARNINGs may include orphan sources, stale-draft flags (none should remain), or schema drift.

- [ ] **Step 2: Triage orphans**

```bash
.venv/bin/wiki lint --scope orphans
```

For sources tagged `ai-native-business` that lack inbound citations from any synthesis: decide per source whether to (a) cite into an existing synthesis via `wiki cite`, (b) accept as background-only material, or (c) untag from the domain.

- [ ] **Step 3: APPROVAL GATE — present lint report and triage plan to user**

Show: lint counts (errors / warnings / orphans). For each non-trivial finding, propose action. User approves.

- [ ] **Step 4: Apply approved fixes**

For each approved citation-fill:

```bash
.venv/bin/wiki cite wiki/synthesis/<page>.md <LINE>:<source-id>
```

- [ ] **Step 5: Re-run lint**

```bash
.venv/bin/wiki lint
```

Expected: lint is clean or only known-acceptable warnings remain.

- [ ] **Step 6: Final commit**

```bash
git add -u wiki/
git commit -m "lint(ai-native-business): close orphans, attach final citations" 2>/dev/null || echo "Nothing to commit"
```

- [ ] **Step 7: Update log.md**

```bash
.venv/bin/wiki status
```

Append one line to `log.md`:

```
2026-05-23  domain shipped  ai-native-business — 4 pillars + 3 archetypes + concept anchor + MoC; ~N sources, ~M entities
```

(Run via gateway helper if available; otherwise commit a manual edit.)

```bash
git add log.md
git commit -m "log: ship ai-native-business domain"
```

---

## Out of scope (deferred to user-triggered follow-ups)

Per the spec's non-goals (§ 8) and the "artifact generation is opt-in" memory, the following are **explicitly NOT** in this plan:

- `wiki nlm-briefing ai-native-business` (briefing doc)
- `wiki nlm-audio ai-native-business "<topic>"` (audio overview)
- `wiki nlm-slides ai-native-business "<topic>"` (slide deck)

These are user-triggered after the wiki content is settled. If the user wants any of them, request it explicitly post-plan.

Also explicitly deferred:
- Investor framework / diligence sibling domain
- Comparative benchmark vs. incumbents
- Productized-expertise archetype (user declined)
- Primary research / interviews
- Long-horizon (>12 month) projections
