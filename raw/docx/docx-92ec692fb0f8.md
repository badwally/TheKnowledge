---
schema_version: 1
id: docx-92ec692fb0f8
type: docx
title: orita-claude-md
url: ''
authors: []
ingested_at: '2026-05-28T01:52:47Z'
content_hash: sha256:f7bce073bf8879d263b5df898c4146a900ca4e7f733b1f5d7e934a007b42b59c
source_path: raw/docx/docx-92ec692fb0f8.docx
domains:
- orita-cmo
nlm_corpus_ids:
- adc34eb9-c798-4530-8b0d-4b166a0bc38a
wiki_pages:
- wiki/entities/orita.md
- wiki/entities/klaviyo.md
- wiki/entities/hubspot.md
- wiki/entities/claude-code.md
- wiki/entities/avoma.md
- wiki/entities/adrian.md
- wiki/entities/apollo.md
- wiki/entities/partnerstack.md
- wiki/entities/crossbeam.md
- wiki/entities/storeleads.md
- wiki/concepts/agent-escalation-levels.md
- wiki/concepts/workflow-resource-agent-architecture.md
- wiki/concepts/claude-code-velocity-model.md
- wiki/concepts/aeo-geo.md
meta:
  paragraph_count: 84
  table_count: 2
  extraction_tool: python-docx
  original_filename: orita-claude-md.docx
  subject: ''
published_at: '2026'
filter:
  score: 0.9
  policy_version: orita-cmo-v1
  rationale: First-party strategic and operational documentation with strong authority,
    directly addressing competitive positioning in AI audience-intelligence and ecommerce
    MarTech, detailed LLM-based agent architecture patterns for 10-person team deployment,
    and seed-stage B2B SaaS GTM specifics (event-led pipeline, partner/agency channels,
    Klaviyo complementarity). Matches 5 of 6 inclusion criteria with high content
    depth and recency (2026), though lacks quantified funnel metrics, CAC/LTV analysis,
    and detailed HubSpot configuration that would elevate it to 0.95+.
  decided_at: '2026-05-28T01:53:28Z'
  user_correction: null
---
# CLAUDE.md – Orita Marketing Automation Platform

## Project Overview

Strategic planning and implementation project for Orita.ai’s marketing automation platform. The goal: a single marketing executive, augmented by AI-driven agents, operates the full marketing function with limited engineering demands.

This project also serves as a learning vehicle: we capture architectural analysis, competitive intelligence, and implementation patterns in detail as we go. The knowledge base we build here should be authoritative enough to inform marketing automation and agentic system development for SMBs generally — not just Orita.

## Orita Business Model

Orita is an AI-powered audience intelligence layer for ecommerce brands. The ML technology is platform-agnostic.

Core capability: daily engagement scoring of every customer profile using ML models trained on engagement data. Executes smart suppressions, reactivations, bot detection, and audience expansion.

The Klaviyo focus is a GTM decision (market concentration + complementarity), not a technical constraint. Klaviyo cannot replicate Orita’s capability today, creating durable complementarity.

Expanding to other ESPs (Iterable, Braze, SFMC) is a growth vector, not a pivot.

Orita holds Klaviyo Premier Partner status (highest tier). Growth 5x YoY via event marketing and agency partner network. No paid advertising.

Expanding from email into SMS and direct mail, with advertising audience optimization as a next surface.

## CMO’s Current Tech Stack (Broadly Manual)

| Tool | Category | Current Role |
| --- | --- | --- |
| Framer | Website | Marketing site (orita.ai) |
| Linear | Project management | Engineering tickets, product roadmap |
| Granola | Meeting notes | AI meeting transcription |
| Avoma | Revenue intelligence | Call recording, conversation analytics |
| HubSpot | CRM | Contact and deal management |
| Claude Code | AI development | Enrichment skill, MCP integrations, agentic workflows |
| Notion | Knowledge management | Internal docs, wikis, content planning |
| Figma | Design | Brand assets, marketing collateral |
| Google Suite | Productivity | Sheets, Docs, Slides, Gmail, Calendar, Drive |
| Zoom | Video conferencing | Customer calls, demos, webinars |
| Apollo | Prospecting/enrichment | Contact database, outbound sequences |
| StoreLeads | Data | 418K Klaviyo customer domain list (Google Sheet) |
| PartnerStack | Partner management | Partner program, referral tracking, payouts |
| Crossbeam | Ecosystem data | Account overlap detection with partners and prospects |
| Slack | Communication | Internal comms, partner channels, customer channels |

## Related Repositories

~/code/etail-contact-enrichment: Contact enrichment pipeline (codename: Velvet Thunder). One automated workflow demonstrating the Claude Code + API pattern. Transforms trade show attendee lists into validated, outreach-ready contacts. Not a strategic asset; representative of the workflow automation approach.

## Project Documents

| Document | Purpose | Status |
| --- | --- | --- |
| orita_marketing_automation_plan.md (v0.3) | Master plan: business summary, TAM/SAM, 8-stage chain, agent architecture (6+3+1), 56-workflow inventory, 4-phase roadmap, AEO/GEO appendices | Complete draft |
| competitive_landscape_and_gap_analysis.md | Okara deep dive, commercial market survey (6 companies), GitHub open-source survey (3 projects), gap analysis table (10 dimensions) | Complete draft |
| okara_architecture_reverse_engineering.md | Reverse-engineered Okara architecture: 10 primitives with alternatives tables, cost model, primitive-to-feature map, escalation level classification | Complete |
| agent_architecture_analysis.md | Level 0-4 escalation framework for agent orchestration complexity, workflow-to-level mapping, practical recommendations on when to introduce frameworks | Complete |
| prompts/cmo_proposal_prompt.md | Continuation prompt for generating the CMO proposal in a new session | Ready to use |
| prompts/architecture_analysis_prompt.md | Reusable prompt for analyzing additional competitors using the same methodology | Ready to use |
| competitive_intelligence_agent_spec.md | Source taxonomy, signal ontology, weighting framework, action recommendation logic, digest format for the CI research agent. Subsumes workflows 0.1, 9.5, A.11. | Draft — awaiting CMO input on competitor registry and weight calibration |
| prompts/aeo_geo_research_scan_prompt.md | Spec and prompt for the AEO/GEO best practices research scan agent | Ready to use |
| aeo_geo_indexing_guide.md | AEO/GEO best practices research: source analysis, indexing timelines, citation authority factors, content structure recommendations | Complete |
| orita_marketing_automation_proposal.md (v2.0) | CMO proposal: functional cluster architecture, compressed timeline, build/maturation cost separation | Complete — do not modify |
| orita_marketing_automation_proposal_v201.md (v2.0.1) | Updated proposal with expanded executive summary (vision, scope, path, dependencies, operations, business impact) | Current working version |

### Agent Architecture Summary

The 56 workflows are organized by shared state and decision boundary, not by org-chart function:

Workflow Agents (execute end-to-end processes): - Market Intelligence Agent – competitor monitoring, new adopter detection, intent signals, AEO visibility - Pipeline Agent – prospecting, enrichment, CRM hygiene, lead scoring, pipeline management - Engagement Agent – outbound sequences, meeting prep, partner communications - Content Production Agent – AEO/GEO content, blog, schema markup, content calendar - Customer Success Agent – health scoring, expansion detection, case studies, churn intervention - Analytics Agent – dashboards, attribution, funnel analysis, CAC/LTV tracking

Resource Agents (shared capabilities called by workflow agents): - Brand Voice Agent – voice-consistent copy generation across all customer-facing output - Enrichment Agent – contact enrichment, Klaviyo detection, email validation, dedup (generalized from /enrich skill) - Citation Authority Agent – off-site placement, partner content, citation graph maintenance

Orchestrator: Marketing Operations – calendar, cross-agent dependencies, CMO briefings.

CMO (Human): Strategy, relationship judgment, high-stakes approval.

### Escalation Levels (Architecture Complexity)

When deciding how to build any workflow, classify it first:

Level 0: Cron + prompt templates — Independent, scheduled, advisory. No framework needed. ~60% of workflows.

Level 1: Shared data store, implicit coordination — Linear pipeline, idempotent steps. Existing enrichment pipeline is this. No framework needed.

Level 2: Conditional routing — Next step depends on LLM judgment. LangGraph or hand-rolled state machine for specific workflows only. Pipeline Agent lead routing, Customer Success intervention triggers.

Level 3: Cross-workflow event cascades — Event bus (Redis Pub/Sub or Postgres LISTEN/NOTIFY), not a multi-agent framework. Signal propagation across independent workflows.

Level 4: Collaborative multi-agent reasoning — Iterative synthesis across agents. Defer until single-pass LLM synthesis is demonstrably insufficient.

Default approach: Build Level 0-1 for everything. Add complexity per-workflow only when branching logic justifies it. Do NOT adopt a framework system-wide.

### Implementation Velocity Model (Claude Code + MCP)

The dominant cost in building this system is spec writing and CMO knowledge extraction, not implementation labor. Claude Code with Opus 4.6 agents collapses traditional engineering timelines by roughly 10x:

MCP connectors (HubSpot, Google Workspace, Slack, Notion): configuration, not engineering. Minutes per connector.

REST API integrations (Apollo, ZeroBounce, StoreLeads via Sheets API): Claude Code implements from documented endpoints in a single session. The enrichment pipeline demonstrates this pattern.

Level 0 skills: each is a structured prompt + cron trigger + one or two API calls. Claude Code scaffolds these directly. The variable is prompt tuning iterations — re-running with adjustments until output quality is acceptable — not architecture.

Prompt iteration cadence: simple skills (pipeline reports, CRM hygiene) converge in 1-2 iterations. Skills with judgment calls (competitive monitoring, enrichment-on-create, content generation) need more rounds. Each round is minutes, not hours.

Calibration: a focused technical person with Claude Code can wire four core integrations in an afternoon and scaffold 8 Level 0 skills in 1-2 additional days. Estimate 2-3 focused days for a full Phase 1 equivalent, not weeks or months. When multiple Opus 4.6 agents work independent clusters in parallel, calendar time compresses further. The binding constraints are human: CMO interviews (4-6 hours), brand voice formalization, and quality review cycles.

When estimating effort: measure spec writing hours and stakeholder input hours. Present cost as one-time build sprint + monthly operating. Never frame as weekly engineering hours over months.

## Working Relationship

When the user proposes a framework or architecture, evaluate it critically. If the decomposition conflates axes, the hierarchy is wrong, or the framing misweights components, say so directly with a specific correction and rationale.

Surface structural problems in the user’s thinking before building on a flawed foundation. Don’t proceed with implementation on an unchallenged assumption. Clearly present potential structural misunderstandings to the user in advance of any subsequent step and wait for guidance.

When correcting, propose the alternative structure, not just the objection.

Design decisions with multiple valid approaches require consultation: present analysis and get user agreement BEFORE writing code or committing to a direction.

## Key Decisions Made

Agent decomposition by shared state, not org chart. The user initially proposed User→Function→Agent→Features. This conflated organizational and architectural axes. Corrected to two-tier: workflow agents (execute processes) + resource agents (shared capabilities). Rationale: prevents knowledge duplication, keeps workflow agents focused on decisions.

Enrichment pipeline is one workflow, not a strategic asset. Early framing overweighted the etail-contact-enrichment skill. It’s workflow 1.1 in a 56-workflow inventory — representative of a pattern, not the core of the system.

Klaviyo is a GTM choice, not a technical constraint. Corrected in 4 places across documents. Orita’s ML is platform-agnostic; Klaviyo focus reflects market concentration and complementarity.

No premature framework adoption. Competitive analysis (Okara at Level 0, open-source projects) confirms that most marketing automation workflows are achievable with cron + structured LLM prompts. Multi-agent frameworks (CrewAI, LangGraph) introduce abstraction tax and breaking-change risk. Add orchestration complexity per-workflow when the branching logic demands it.

PartnerStack and Crossbeam are in the stack. These were not in the original plan but the CMO confirmed them. PartnerStack replaces informal referral tracking (Stage 6 workflows). Crossbeam adds account overlap data for Market Intelligence and Pipeline agents.

Avoma/Granola add call intelligence. These map to deal activity logging (5.6) and meeting prep (2.6) workflows — the Engagement Agent and Pipeline Agent benefit from structured call data.

Claude Code is the implementation layer, not a helper tool. MCP connectors are configuration. REST API integrations are single-session Claude Code tasks. Level 0 skills are prompt + cron + API call, scaffolded directly by Claude Code. Original 2-month Phase 1 estimate collapsed to 2-3 focused days when calibrated to actual Claude Code velocity. All timeline estimates must reflect this.

## Priority Workstreams

### Immediate (This Week)

Generate and deliver the CMO proposal. Use prompts/cmo_proposal_prompt.md in a new session. Output: orita_marketing_automation_proposal.md — a professional, deliverable document mapping the staged build to Orita’s actual stack.

### Near-Term (Next 2 Weeks)

Analyze 2-3 additional competitors using prompts/architecture_analysis_prompt.md. Priority targets: Clay (enrichment + workflows), Relevance AI (multi-agent builder), HubSpot Breeze (incumbent AI agents). Each analysis appends to agent_architecture_analysis.md.

Resolve open questions from plan Section 9. Several affect the proposal: HubSpot configuration depth, Apollo plan tier, sales cycle details, current blog cadence. These should come from the CMO or be surfaced in the proposal as assumptions.

### Medium-Term (Months 1-2)

Begin Phase 1 implementation. Wire HubSpot MCP, Apollo API, Google Sheets sync. Build first 8 Tier A workflows. This is the foundation everything else depends on.

Develop the learning capture document (see below).

## Learning Capture

We aim to capture learnings in detail as we go, building a reference that cements understanding of marketing automation workflow development and agentic system architecture for SMBs. This serves two purposes: (a) inform Orita’s own implementation decisions with precedent, and (b) build transferable knowledge about what works, what doesn’t, and why.

Where learnings live: - agent_architecture_analysis.md — Escalation framework, per-company architecture analysis, open-source patterns. Append after each competitor analysis round. - okara_architecture_reverse_engineering.md — Template for detailed primitive-level analysis. The alternatives tables (10 primitives × multiple options each) are the reusable reference for any build. - A future learnings.md (or Notion page) for implementation-phase observations: what worked, what broke, integration gotchas, LLM prompt patterns that reliably produce good output, cost benchmarks from real usage. Create this document when Phase 1 implementation begins.

What to capture: - Architectural patterns: which Level 0-4 choices proved right, which were premature - Integration specifics: HubSpot MCP limitations, Apollo API quirks, Google Sheets rate limits (already documented in etail-contact-enrichment) - LLM economics: actual token costs vs. estimates, quality/cost tradeoffs by model - Prompt patterns: structured prompts that reliably produce good output for specific workflow types (enrichment, content generation, meeting prep, reporting) - Failure modes: what goes wrong and how to recover (API limits, stale data, LLM hallucination in customer-facing output)

## Key Strategic Context

### TAM/SAM

Email deliverability tools: $1.48B global (2026), ~$630M US

Orita’s broader tech (AI audience intelligence across channels): $2B-$4B US TAM

Klaviyo-focused SAM (current beachhead): ~$400M-$500M midpoint. Constraint is GTM velocity, not market size.

### Growth Priorities (ordered)

AEO/GEO for AI-era discoverability (highest leverage)

Always-on prospecting (move from event-triggered to continuous)

Systematize event-to-pipeline flow

Formalize partner/referral channel

### Omnichannel Expansion (product-level)

SMS optimization (underway)

Direct mail audience selection (underway)

Advertising audience optimization (next)

Predictive LTV scoring for acquisition channels (medium-term)

AEO/GEO intelligence for ecommerce customers (medium-term, see Appendix B)

## Code Style

Follow conventions in user preferences (see system prompt): pragmatic over clever, YAGNI, smallest reasonable change, naming tells domain story.

Python 3.10+ where applicable. Use orita/etail-enrichment/venv/bin/python3 in the enrichment repo.

No test framework yet; validate with real data before formalizing tests.

Design decisions require consultation: present analysis and get user agreement BEFORE writing code.
