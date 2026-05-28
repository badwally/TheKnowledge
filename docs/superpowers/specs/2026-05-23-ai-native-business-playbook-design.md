# AI-Native Operator Playbook — Research Design

**Status:** Design / pre-execution
**Date:** 2026-05-23
**Author:** Andrew Grant (with research lead pairing)
**Output:** A new wiki domain `ai-native-business` filed to `wiki/`, grounded in `raw/`

---

## 1. Problem framing

Define what it means to build an **"AI-native" business** in concrete technical, operational, and economic terms — concrete enough to be an **operator playbook** for a solo founder + AI working with substrate-first assumptions. "Substrate-first" means AI is the operating substrate the business runs on; the *offering* may or may not be AI itself.

The playbook must answer the questions a solo operator actually faces — org shape, economics, tech defaults, GTM and defensibility — and must do so for three concrete archetypes a solo operator can plausibly build.

This is not a market thesis, not an investor framework, and not a comparative benchmark of incumbents. It's a build-side reference document.

## 2. Scope locks (from interview)

| Decision | Value | Reason |
|---|---|---|
| Primary use case | Operator playbook | Actionable; will be referenced when actually building |
| Starting position | Solo / founder + AI | Tiny team, max AI leverage, bootstrapped or pre-seed |
| Sense of "AI-native" | Both, **substrate-first** | Substrate framing leads; product framing is a specialization |
| Priority dimensions | All four pillars (org, economics, tech, GTM) | Each gets a full pillar synthesis; none demoted to appendix |
| Tailoring level | Generic framework + 3-4 archetype specializations | Most reusable; supports comparative reading across archetypes |
| Archetypes | Indie SaaS / vertical agent · Services firm · Marketplace / aggregator | Productized expertise explicitly excluded |
| Cadence | Heavy batch ingest | Highest fidelity; matches CLAUDE.md "Batch. Fidelity > convenience" |
| Time horizon | 2026 snapshot + per-pillar "12-month frontier" subsection | Stance-taking, but grounded |
| Substack-from-inbox layer | Use Gmail MCP for **discovery only**, ingest via web converter on canonical Substack URLs | No Gmail poller yet; respects gateway contract |
| Inbox discovery timing | After spec approval, as execution step | Clean separation of design from source curation |

## 3. Output structure

### 3.1 Wiki domain

New domain slug: **`ai-native-business`**.

Bootstrap via `wiki bootstrap-domain "<description>" ai-native-business` so the domain comes with:
- A `wiki/mocs/ai-native-business.md` MoC
- A `.knowledge/policies/ai-native-business/` policy
- A NotebookLM corpus registered in `nlm/notebooks.yaml`
- Filter/seed examples ready for `wiki finetune` later

### 3.2 Page layout (target final state)

```
wiki/
├── mocs/
│   └── ai-native-business.md                              # Top-level MoC + framework + navigation
├── concepts/
│   └── ai-native-substrate.md                             # Definitional concept page (AI-as-substrate vs feature vs product)
├── synthesis/
│   ├── ai-native-org-and-operating-model.md               # Pillar 1
│   ├── ai-native-economics-and-capital.md                 # Pillar 2
│   ├── ai-native-tech-stack-and-build-vs-buy.md           # Pillar 3
│   ├── ai-native-gtm-pricing-defensibility.md             # Pillar 4
│   ├── archetype-indie-saas-vertical-agent.md             # Archetype A specialization
│   ├── archetype-services-firm.md                         # Archetype B specialization
│   └── archetype-marketplace-aggregator.md                # Archetype C specialization
├── entities/
│   └── <20-30 named companies and operators>              # E.g., anysphere, harvey, cognition, sierra, lindy, mercor, crosby, decagon, elevenlabs, perplexity, pieter-levels, marc-lou, etc.
└── sources/
    └── <one page per ingested source, ~85-110 total>
```

Total LLM-authored pages: ~8 syntheses + 1 MoC + 1 concept + 20-30 entities ≈ **30-40 wiki pages** plus auto-generated source pages.

### 3.3 Pillar synthesis structure (internal template, all four follow this)

1. **Substrate framing** — the pillar viewed through AI-as-substrate (independent of archetype).
2. **What "good" looks like in 2026** — concrete numbers, named-company exemplars, benchmark ranges.
3. **Archetype deltas** — how the pillar shifts per archetype (indie SaaS / services firm / marketplace).
4. **12-month frontier** — stance-taking subsection on where this is heading, explicitly demarcated from the snapshot.
5. **Citations** — every claim followed by `[[sources/<id>]]` per the citation grounding hard rule.

### 3.4 Archetype synthesis structure (all three follow this)

1. **Archetype definition** — what this archetype is, what it isn't, who's built it well.
2. **Four pillars, archetype-specific** — sections that *cite back* into the four pillar pages with archetype-specific deltas and elaborations.
3. **Go/no-go signals** — what conditions make this archetype right or wrong for a solo founder.
4. **Worked example** — one named-company case study walked through the four pillars.

## 4. The four pillars (content scope)

### 4.1 Org & operating model
- Role taxonomy for solo + N agents (e.g., founder, operator-agents, builder-agents, evaluator-agents)
- What gets automated first, in what order, and why
- Agent-in-the-loop patterns: review gates, eval discipline, human escalation
- Decision cadence: async-default, what stays sync, weekly/daily rhythm
- "When to add a human vs. add an agent" decision rule

### 4.2 Economics & capital path
- Cost structure: compute, vendor primitives (model APIs, infra, embeddings, search), data, human time
- Gross margin profile vs. legacy SaaS / legacy services / legacy marketplace
- Revenue-per-human benchmarks (Anysphere, Midjourney, Telegram, Plenty of Fish, Craigslist as comparators)
- Time-to-revenue norms for each archetype
- Bootstrapped vs. revenue-financed vs. seed — when each makes sense for an AI-native solo
- The "AI compute as variable cost" reshaping of unit economics

### 4.3 Tech stack & build-vs-buy
- Model selection discipline: frontier vs. cheap-and-fast vs. open-weight; orchestration patterns
- Evals as a core operating function (not a side project)
- Observability defaults for agentic systems
- The "compose vendor primitives until proven wrong" default — when proprietary is actually warranted
- Data flywheels: when they're real moats vs. cope
- AI-native infra defaults (e.g., serverless, vector stores, queueing, log/trace tooling) — but resist becoming a tool list; focus on selection criteria

### 4.4 GTM, pricing & defensibility
- Acquisition channels that work for a solo AI-native (PLG, founder-led content, embedded distribution, agent-marketplace listings)
- Pricing axes: per-seat vs. usage vs. outcome — when each fits which archetype
- Where moats actually form when models are commoditized: workflow lock-in, data flywheels, distribution, brand, switching cost, integration depth
- The "thin wrapper" critique — when it's fair and when it's lazy
- Defensibility for services-firm and marketplace archetypes, where moats look very different from SaaS

## 5. Three archetype specializations

### 5.1 Indie SaaS / vertical agent
- Cursor / Anysphere, Cognition / Devin, Lindy, Crosby, Decagon, Sierra as referents
- Solo-buildable variant: Pieter Levels, Marc Lou, single-operator vertical agents
- Defensibility: workflow lock-in, integration depth, eval moat
- Pricing: seat → usage → outcome trajectory

### 5.2 Services firm (AI-native)
- AI-native marketing studio, bookkeeping shop, recruiting firm, paralegal services, content production
- Mercor, Harvey, Crosby, Decagon — though "services firm" here is the lean-operator version, not the funded version
- Economics: hourly/retainer collapse as AI substrate replaces hours; pricing pivot to outcomes
- Defensibility: client relationships + workflow integration + reputation; not data

### 5.3 Marketplace / aggregator
- AI mediates supply/demand or aggregates fragmented work
- Examples: AI-mediated recruiting, freelance-work brokering, supplier matching, content-rights aggregation
- Operator runs the platform; AI does matching, vetting, ops, dispute resolution
- Defensibility: liquidity moat + integration depth + workflow lock-in
- Hardest archetype for solo operators — explicit go/no-go signals will lean conservative

## 6. Source diet (heavy batch ingest)

Target: **85-110 sources** in one batch ingest pass.

### 6.1 Categories and counts

| Category | Count | Source type | Notes |
|---|---:|---|---|
| Named company case studies | 20-30 | `web`, `youtube` | Blog posts, press, financial disclosures, founder podcast appearances. Cursor/Anysphere, Harvey, Cognition, Sierra, Decagon, Mercor, Crosby, Lindy, Cresta, ElevenLabs, Perplexity, Glean, Hebbia, Anthropic-as-business, plus 2-3 solo operators per archetype. |
| VC & operator essays | 15-20 | `web` | a16z, Sequoia, Benchmark, Felicis pieces on AI-native economics. Lenny Rachitsky. First Round. Operator essays from Substack/Medium/personal blogs. |
| Books | 5 | `audiobook`, `pdf` | Mollick *Co-Intelligence*; Suleyman *The Coming Wave*; Hoffman *Superagency*; one ops/org book; one capital-efficiency book TBD during curation. |
| Academic / productivity research | 10 | `arxiv`, `pdf` | Brynjolfsson; Mollick group; GitHub Copilot productivity studies; BCG×Harvard AI experiment; Stanford HAI org-design reports. |
| YouTube — founder/operator interviews | 12-15 | `youtube` | Acquired (Anysphere, Anthropic episodes), Lenny's, Latent Space, 20VC, AI Native Dojo, Lex AI builder eps, Greg Isenberg, BG2 Pod. |
| YouTube — conference/keynote talks | 6-10 | `youtube` | AI Engineer Summit, YC AI demos, a16z AI Revolution Summit, NeurIPS-adjacent operator talks. |
| Solo-operator primary signal | 5-10 | `web` | Pieter Levels (Nomad List, Photo AI), Marc Lou, other selected single-operator AI-native builders. |
| Substack-from-inbox layer | 10-20 | `web` (via Gmail discovery) | Discovered via Gmail MCP enumeration of subscriptions during execution; ingested via web converter on canonical Substack URLs. |

### 6.2 Discovery mechanics

- **Named companies, books, academic, conferences:** I propose a candidate list during execution; user approves before ingest.
- **YouTube long tail:** `wiki research "<prompt>"` per pillar/archetype surfaces additional videos via the YouTube adapter; `wiki filter` scores them; user reviews high-score candidates.
- **Substack-from-inbox:** Gmail MCP enumerates active subscriptions and recent posts in the user's inbox; canonical Substack URLs extracted; ingested via web converter. Tagged distinctly in metadata so the "your-reading-bias" layer is auditable.

### 6.3 Filter discipline

All sources pass `wiki filter` against the `ai-native-business` domain policy. Filter decisions are reviewable; the user can pin corrections via `wiki filter-correct` to tune the filter over the corpus build.

## 7. Workflow

The build sequence:

1. **Bootstrap domain.** `wiki bootstrap-domain "<description>" ai-native-business`. Confirms MoC stub, policy, NLM notebook, finetune seed.
2. **Curate source list.** Propose enumerated candidate list for each category in §6. User approves before ingest. Substack/inbox layer is enumerated here (post-approval, pre-ingest).
3. **Batch ingest.** `wiki batch-ingest` on the approved list, domain-tagged. Each source flows through filter → `raw/` → NLM corpus. Volume: ~85-110.
4. **Definitional concept page first.** `wiki query "What does it mean for a business to be AI-native (substrate-first)?" --domain ai-native-business` → produces `concepts/ai-native-substrate.md`. This anchors vocabulary for the four pillars.
5. **Pillar syntheses.** Four `wiki query` calls, one per pillar. Each produces a draft pillar synthesis citing the corpus. Drafts are reviewable with `wiki finalize` to commit.
6. **Archetype syntheses.** Three more `wiki query` calls, one per archetype. Each cites back into the pillar pages.
7. **Entity pages.** Auto-generated / backfilled for the named companies and operators referenced.
8. **MoC.** `wiki/mocs/ai-native-business.md` written last, once the structure of the cluster is concrete.

Estimated execution span: **2-3 working sessions** for curation + ingest + pillar/archetype synthesis, plus iteration. NLM artifact generation (briefings, audio, slides) is **opt-in only**, per the memory of "artifact generation is opt-in" — not triggered automatically.

## 8. Non-goals

- **No investor framework.** Diligence questions, valuation framing, market-sizing — out of scope. (Can be split off as a sibling domain later.)
- **No comparative benchmark vs. incumbents.** This is a build-side reference, not a "AI-native vs. legacy SaaS scorecard."
- **No productized-expertise archetype.** User explicitly declined this archetype.
- **No NLM artifact generation by default.** Slides/audio/briefing are user-triggered after the wiki content is settled.
- **No primary research / interviews.** Desk research only.
- **No projection beyond 12 months.** The "frontier" subsections are 12-month stances; longer projections introduce too much speculation for an operator playbook.

## 9. Open questions for execution-time decisions (deferred from design)

1. Exact named-company list — user approval gate during curation.
2. Exact Substack subscriptions to include — depends on Gmail MCP discovery output.
3. Whether to specialize the YouTube long tail by pillar or archetype during `wiki research` — operational choice.
4. Whether the concept page (`concepts/ai-native-substrate.md`) should split into multiple concepts (e.g., separate pages for "AI as substrate," "AI as product," "AI as feature") — defer until first draft surfaces real ambiguity.
5. Whether the MoC needs sub-MoCs per pillar — defer until total page count is known.

## 10. Hard-rule compliance

- **No direct writes to `wiki/` or `raw/`.** All output goes through `wiki bootstrap-domain`, `wiki batch-ingest`, `wiki query`, `wiki finalize`. (§ 7)
- **No direct calls to NotebookLM MCP.** Corpus loading goes through `wiki batch-ingest`'s NLM sync; artifact generation is opt-in via `wiki nlm-*`. (§ 7, § 8)
- **Citation grounding mandatory.** All wiki pages cite `[[sources/<id>]]`. Drafts may be `--draft true` short-term but must be finalized within 7 days. (§ 3.3)
- **Lookup before create.** Definitional concept page `concepts/ai-native-substrate.md` is checked against `index.md` before creation. (§ 7 step 4)
- **Plan before write.** This spec is the plan. The build sequence (§ 7) explicitly enumerates pages-created and cross-references.
- **Sources in `raw/` are immutable.** Confirmed; only frontmatter updates allowed.

---

**Next step after spec approval:** invoke `superpowers:writing-plans` to produce a step-by-step implementation plan for the workflow in § 7.
