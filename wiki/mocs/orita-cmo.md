---
schema_version: 1
type: moc
slug: orita-cmo
title: orita-cmo — Map of Content
domain: orita-cmo
created_at: '2026-06-16T02:50:33Z'
last_updated: '2026-06-16T02:50:33Z'
---
## Overview

`orita-cmo` is the strategic and operational knowledge base for the **CMO of [[entities/orita]]** — a seed-stage AI **audience-intelligence** company selling into the Klaviyo / Shopify ecommerce MarTech ecosystem. The policy (`.knowledge/policies/orita-cmo/policy.yaml`) scopes it to five intelligence pillars: competitive intelligence (incl. M&A signals), GTM/growth execution (agency channel, events, AEO/GEO, outbound), funnel/marketing-ROI (HubSpot, ICP-vs-closed-won, SMB benchmarks), the AI-native operating model (Claude-Code agent/skill architectures at ~10-user scale on GCP), and synthesized voice-of-the-customer.

Two research arcs run through the domain. The **competitive-landscape** arc maps where Orita sits; the **AI-native operating-model** arc asks how one executive runs a full CMO function at seed-stage capital efficiency. They are welded by a single idea: **Orita's CMO function is itself the test case for the compute-over-headcount, judgment-gated, agent-fleet operating model the domain documents.**

The load-bearing strategic fact: Orita is **upstream-only** — it scores first-party Shopify data into predictive purchase-intent audiences daily and executes **smart suppression**, then routes audiences **downstream** into channel platforms (Klaviyo as beachhead) rather than owning execution. Everything competitive turns on one fork: **own execution, or make the channel partnership the moat** — pressured hardest by agentic consolidators (the OuterSignal–Monocle merger) collapsing the upstream/downstream split.

## Key entities

**Company, team & stack**
- [[entities/orita]] — AI audience-intelligence layer; daily ML purchase-intent scoring + smart suppression; seed-stage *(still `draft: true`)*
- [[entities/aaron]] — CEO · [[entities/adrienne]] — CMO
- [[entities/klaviyo]] — dominant email/SMS lifecycle platform; Orita's primary channel partner and GTM beachhead
- [[entities/hubspot]] — CRM / source of truth (customers + prospects) · [[entities/storeleads]] — 418K Klaviyo-domain prospect list

**Incumbent channel platforms** (partners *and* indirect pressure — they sell segmentation natively)
- [[entities/attentive]] — SMS/email, Shopify-skewed · [[entities/postscript]] — SMS-first, Shopify-native, 50+ integrations
- [[entities/bloomreach]] — email/SMS/engagement, mid-market→enterprise · [[entities/omnisend]] — email/SMS SMB
- [[entities/drip]] — email-only automation · [[entities/yotpo]] — reviews/loyalty/SMS/email, same buyer as Orita
- [[entities/simon-ai]] — multi-channel on a CDP, predictive analytics · [[entities/listrak]] — cross-channel (thin data)

**Direct AI / purchase-intent competitors** (share Orita's core proposition)
- [[entities/black-crow-ai]] — full-funnel predictive AI, Shopify DTC; Orita's named direct competitor
- [[entities/monocle]] — real-time AI journeys; acquired by [[entities/outersignal]] (2026-05-28) → upstream+downstream consolidation
- [[entities/clustie]] — predictive Shopify audiences, **Meta Ads only** ($79–$499/mo) · [[entities/full-venue]]
- [[entities/enalito]] — AI email/SMS/chatbot (thin evidence) · [[entities/aampe]] — RL "AI Decisioning", deep agentic
- [[entities/offerfit]] · [[entities/movable-ink]] · [[entities/hightouch]] — adjacent AI-decisioning / activation pressure

## Key concepts

**RevOps / HubSpot data infrastructure** (qualification enforced *in the CRM*)
- [[concepts/meddic]] · [[concepts/economic-buyer]] — qualification framework; canonical failure is closing without the check-signer
- [[concepts/hubspot-association-labels]] · [[concepts/hubspot-segments]] · [[concepts/hubspot-deal-tags]] — labels → segments → deal-tags surface a missing economic buyer at a glance
- [[concepts/hubspot-data-hygiene]] · [[concepts/icp-tiering]] — weekly/quarterly cleanup; tier scoring against closed-won

**Agentic architecture / operations**
- [[concepts/workflow-resource-agent-architecture]] — decompose by knowledge+decision boundary: 6 workflow + 3 resource agents + 1 orchestrator
- [[concepts/agent-escalation-levels]] — 5-tier L0–L4 (L0 cron+prompt covers ~60% of workflows)
- [[concepts/claude-code-velocity-model]] — Phase-1 scaffold in 2–3 days; MCP connectors are configuration
- [[concepts/plan-before-execute-after]] — 4-stage CRM-mutation discipline · [[concepts/model-context-protocol]] · [[concepts/retrieval-augmented-generation]] · [[concepts/external-ai-crm-surface]]

**GTM / sales motions**
- [[concepts/agency-channel-gtm]] — agencies-of-record as high-leverage multi-brand nodes
- [[concepts/aeo-geo]] — answer/generative-engine optimization; 89% of B2B buyers use Gen-AI to research; citation authority is the asset
- [[concepts/competitive-positioning]] — agentic competitor-signal digest with weighted scoring · [[concepts/voice-of-the-customer]]

**Category positioning**
- [[concepts/agentic-personalization-platform]] — upstream intelligence + downstream execution in one stack
- [[concepts/martech-consolidation]] — M&A collapsing analytics + CRM + engagement (the sharpest threat to upstream-only vendors)

## Synthesis pages

**Competitive arc**
- [[synthesis/2026-06-16-map-the-competitive-landscape-orita-operates]] — the full landscape map (incumbents, direct AI, consolidators) + where Orita sits; Capterra-benchmark-grounded

**AI-native operating-model arc** — the CMO-as-agent-fleet thesis
- [[synthesis/2026-06-15-how-can-a-single-marketing-executive]] — 1 CMO + 6 workflow + 3 resource agents; the three CMO decision classes
- [[synthesis/2026-05-23-what-does-the-org-and-operating-cross-cutting]] — compute-over-headcount; earned judgment as the bottleneck
- [[synthesis/2026-05-23-what-does-the-org-and-operating-ai-native-go-to-market-gtm]] — momentum-as-moat; products engineered for self-distribution
- [[synthesis/2026-05-23-what-does-the-org-and-operating-role-taxonomy-and-the-human-agent]] — allocating intelligence; player-coach model
- [[synthesis/2026-05-23-what-does-the-org-and-operating-economic-infrastructure-and-capital-efficiency]] — $300–500/mo stack vs $80–120k payroll; credit-based pricing
- [[synthesis/2026-05-23-what-does-the-org-and-operating-execution-strategy-and-automation-sequencing]] — automation triage; oversight-first; minimalist AI injection
- [[synthesis/2026-05-23-what-is-the-ai-native-technical-evals-and-observability-as-core-operating]] — evals/observability as core operating discipline

## Source clusters

- **Competitor benchmarks** — ~10 `web-2026-06-15-*` Capterra pages (Postscript, Yotpo, Drip, Simon AI, Black Crow, plus alternative listings); ratings/features/pricing/integration catalogs, ingested via the firecrawl→Capterra→`wiki ingest --force-include` pipeline that solved the blocked-aggregator problem.
- **M&A / consolidation signal** — `web-2026-05-28-0cb` (OuterSignal–Monocle).
- **Orita primary** — `pdf-4931157e130a` (product/team) and `docx-25c1bcf28fb8` (GTM stack: Klaviyo/HubSpot/StoreLeads/agency channel).
- **Direct-competitor app/listing data** — older Shopify App Store / listing sources for Clustie, Enalito, Aampe (dated, lower competitive depth).
- 20 grounding sources total across `raw/{web,docx,pdf}/`.

## Open threads

- **Prescriptive positioning** (how Orita *should* position) — needs Orita's own strategy material in the corpus; not a retrieval task, deferred until requested.
- **`orita.md` is `draft: true`** — carries citations but never run through `wiki finalize`.
- **Blocked sources** — CB Insights "Orita alternatives" (paid account) and F6S (hCaptcha): the richest curated competitor lists, still unreachable.
- **The strategic fork is unresolved** — own execution vs. deepen the Klaviyo partnership into a moat, against accelerating agentic consolidation.
- **`answer.py` 1500-token cap** limits wide syntheses (worked around in-process; a `--max-tokens` flag would productize it).
