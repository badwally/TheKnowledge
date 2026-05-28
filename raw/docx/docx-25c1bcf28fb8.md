---
schema_version: 1
id: docx-25c1bcf28fb8
type: docx
title: orita-marketing-automation-plan
url: ''
authors: []
ingested_at: '2026-05-28T02:04:42Z'
content_hash: sha256:2e0aea74a6729293d394a74ff3361ccf93e978b17e7e702c7fae928492d0e73a
source_path: raw/docx/docx-25c1bcf28fb8.docx
domains:
- orita-cmo
nlm_corpus_ids:
- adc34eb9-c798-4530-8b0d-4b166a0bc38a
wiki_pages:
- wiki/entities/orita.md
- wiki/entities/klaviyo.md
- wiki/entities/apollo.md
- wiki/entities/hubspot.md
- wiki/entities/storeleads.md
- wiki/entities/claude-code.md
- wiki/concepts/aeo-geo.md
- wiki/concepts/workflow-resource-agent-architecture.md
- wiki/concepts/agency-channel-gtm.md
- wiki/concepts/hubspot-data-hygiene.md
- wiki/entities/spanx.md
- wiki/entities/caraway.md
- wiki/entities/postpilot.md
meta:
  paragraph_count: 253
  table_count: 14
  extraction_tool: python-docx
  original_filename: orita-marketing-automation-plan.docx
  subject: ''
published_at: '2026'
filter:
  score: 0.85
  policy_version: orita-cmo-v1
  rationale: 'Primary company document from Orita.ai detailing seed-stage B2B SaaS
    GTM strategy and Claude-Code-based agent architecture patterns at small-team scale,
    strongly matching inclusion criteria #2 (GTM motion), #4 (HubSpot/RevOps), and
    #5 (agent architecture). Limited competitive positioning analysis prevents higher
    score, but the strategic planning specificity, named tool stacks (Apollo, HubSpot
    MCP, Klaviyo, Google Workspace), and detailed agent decomposition provide high-authority
    operational intelligence for the CMO''s knowledge base.'
  decided_at: '2026-05-28T02:05:14Z'
  user_correction: null
---
# Orita.ai: Marketing Automation Platform Plan

Working Draft v0.3 | April 3, 2026

## 1. Business Summary

Orita is an AI-powered audience intelligence layer for ecommerce brands. The core technology uses machine learning models trained on engagement data to score every customer profile daily for purchase intent, then executes smart suppressions, reactivations, bot detection, and audience expansion. The result is higher revenue per send, protected sender reputation, and reduced waste across communication channels. The technology is platform-agnostic at the algorithmic level.

Orita has made a strategic decision to prioritize Klaviyo customers as their primary target. This is a GTM choice, not a technical constraint, driven by two factors: (a) Klaviyo dominates US ecommerce email marketing, concentrating the addressable market, and (b) Klaviyo cannot replicate what Orita does at a technical level today, which creates a durable complementarity. Prioritizing Klaviyo also simplifies integration for the largest customer pool and has earned Orita Premier Partner status (Klaviyo’s highest tier). Growth has been 5x year-over-year, driven by event marketing (eTail conferences, Klaviyo ecosystem events) and word-of-mouth through the agency partner network. No paid advertising. The company is expanding from email into SMS and direct mail, with advertising audience optimization as a natural next surface.

Current tooling: HubSpot (CRM), Apollo (prospecting/enrichment), Klaviyo (channel partner), Google Workspace, Claude Code with MCP integrations. One existing automated skill (event attendee list enrichment) demonstrates the pattern of using Claude Code + external APIs to replace manual workflows.

Voice (initial characterization): Technical but accessible. Data-driven authority anchored to revenue outcomes. Confident claims backed by specific metrics (31% revenue lift for Spanx, $1M recovered for Caraway). No hype. Conversational professional tone.

## 2. TAM/SAM: US Market

Email deliverability tools (global): $1.48B in 2026, growing to $2.22B by 2030 at 10.6% CAGR. US share ~$630M.

Orita’s broader technology (AI audience intelligence across channels): The ML scoring engine is channel-agnostic. Applied across email, SMS, direct mail, and advertising audience optimization, the relevant US TAM is conservatively $2B-$4B.

Klaviyo-focused SAM (US, current beachhead):

Klaviyo is the initial target, not the ceiling. The technology works with any ESP that exposes engagement data. But Klaviyo’s market concentration makes it the rational starting point: 167,000+ customers globally, 44.9% (~75,000-79,000) US-based, fastest growth in the $5M-$50M GMV cohort, ~25,850 Shopify Plus stores US-based. Expanding to Iterable, Braze, Salesforce Marketing Cloud, or Ometria customers is a future growth vector that widens the SAM without requiring core technology changes.

| Segment | Est. US Count | Est. ACV Range | Segment Value |
| --- | --- | --- | --- |
| Enterprise ($50M+ GMV) | 3,000-5,000 | $24K-$60K | $72M-$300M |
| Mid-market ($5M-$50M GMV) | 15,000-25,000 | $6K-$24K | $90M-$600M |
| Growth ($1M-$5M GMV) | 20,000-30,000 | $2.4K-$6K | $48M-$180M |
| Total SAM | 38,000-60,000 |  | $210M-$1.08B |

Midpoint SAM: ~$400M-$500M. The constraint is not market size but go-to-market velocity.

Omnichannel multiplier: Each new channel surface (SMS, direct mail, ad audiences) expands the per-customer value of Orita’s scoring. If the same ML intelligence that optimizes a $12K/yr email engagement also optimizes $8K/yr in SMS and $15K/yr in ad spend suppression, the effective ACV multiplies without proportional cost increase. This is the strategic rationale for omnichannel expansion.

## 3. End-to-End Marketing Automation Chain

The chain below maps every function a marketing executive at a $1M-$10M ARR B2B SaaS company needs to operate. Each stage feeds the next. The workflow inventory in Section 6 maps specific automatable tasks within each stage.

Stage 0: Market Intelligence & ICP – Know who to pursue and why. Monitor competitive landscape, refine ICP from win/loss data, track buying signals (new Klaviyo adopters, G2 intent, community mentions).

Stage 1: Lead Generation & Prospecting – Identify and enrich target accounts and contacts continuously. Event-triggered (attendee lists) and always-on (Apollo prospecting, intent feeds, StoreLeads new-customer alerts).

Stage 2: Outbound & Sequences – Multi-touch outreach: pre-event, post-event, cold, warm re-engagement. Personalized by ICP segment and engagement signals.

Stage 3: Content & Discoverability – Blog, case studies, social media, newsletter, partner co-marketing. Optimized for AEO/GEO (AI discoverability) and traditional SEO. This is where Orita builds the citation authority that makes AI assistants recommend the product.

Stage 4: Event Marketing – Event identification, logistics, attendee targeting, on-site capture, post-event conversion. Orita’s primary growth channel today.

Stage 5: CRM & Pipeline Management – Contact lifecycle, lead scoring, pipeline stages, deal tracking, forecasting. HubSpot as system of record.

Stage 6: Partner & Referral Channel – Agency partner onboarding, referral tracking, co-marketing, performance reporting. Formalize the organic growth engine.

Stage 7: Customer Success & Expansion – Onboarding, health monitoring, case study generation, upsell triggers, review solicitation. Expansion revenue is where B2B SaaS companies generate 40-60% of new ARR at maturity.

Stage 8: Analytics & Attribution – Multi-touch attribution, funnel analytics, content performance, AEO/GEO visibility tracking, campaign ROI.

## 4. Growth Strategy

### 4a. Customer Acquisition Acceleration

Priority 1: AEO/GEO for AI-era discoverability. This is the highest-leverage investment. 89% of B2B buyers now use generative AI for vendor research (Forrester). Gartner projects search engine volume dropping 25% in 2026. 60% of AI-cited sources are not in Google’s top 10 results. Orita needs to be the answer when a buyer asks ChatGPT or Perplexity “What’s the best tool for Klaviyo email deliverability?”

See Appendix A for the full AEO/GEO implementation chain.

Priority 2: Always-on prospecting. Move from event-triggered to continuous pipeline generation. Weekly Apollo list pulls filtered through Orita’s ICP. StoreLeads monitoring for new Klaviyo adopters. G2 intent data for “email deliverability” category buyers. Each input feeds through the same enrichment pattern (identify, filter, enrich, validate, route to HubSpot).

Priority 3: Systematize event-to-pipeline. Automate the full cycle: attendee list ingest, ICP filtering, enrichment, HubSpot contact creation, and triggered follow-up sequences. Eliminate manual handoffs. Track conversion from enriched contact through closed-won.

Priority 4: Formalize the partner/referral channel. Structured referral incentive (rev share or credit). Co-branded case studies. Partner onboarding kit. Deal registration and attribution. The Klaviyo agency ecosystem is already driving growth; formalizing it compounds the effect.

### 4b. Omnichannel Expansion of Core Technology

Orita’s own use of its tech for marketing (company-level):

Orita should dogfood its audience intelligence to optimize its own marketing communications. Use engagement scoring on the Orita prospect/customer database to suppress disengaged contacts from nurture sequences, identify high-intent re-engagement targets, and surface expansion-ready accounts. This also generates product stories (“we use Orita to market Orita”).

Orita’s technology applied to customer problems (product-level):

The ML scoring engine is channel-agnostic. Near-term extensions:

SMS optimization (underway): Suppress/reactivate logic for Klaviyo SMS. Per-message cost makes waste more expensive than email.

Direct mail audience selection (underway): Engagement scoring selects high-intent audiences for PostPilot or similar. Directly reduces per-piece waste.

Advertising audience optimization: Export engagement-scored segments as custom audiences for Meta, Google, TikTok. Suppress low-intent profiles from retargeting; seed lookalikes from high-intent segments. The data exists in Orita already; the gap is the export path.

Medium-term (18-36 months):

Predictive LTV scoring for acquisition channels: Score net-new prospects at point of acquisition by engagement likelihood. Turns Orita from retention/optimization into acquisition intelligence.

AEO/GEO intelligence for ecommerce customers (productized): See Appendix B for the full product concept.

Cross-brand audience intelligence: At sufficient scale, engagement patterns across brands become a data-network-effect moat.

## 5. Agent Architecture

The 56 workflows in the inventory don’t map cleanly to a single hierarchy of Function -> Agent -> Feature. Two decomposition axes are in play, and they cross-cut each other:

Organizational axis: What marketing function does this workflow serve? (Content, Pipeline, Events, etc.)

Architectural axis: What knowledge base and decision model does this workflow require?

Agents should be drawn along the architectural axis – grouped by shared state and decision boundary – not by org chart. A function like “content development” requires multiple agents with different knowledge bases (market research vs. brand voice vs. distribution). And a capability like “enrichment” serves multiple functions (prospecting, event processing, CRM hygiene).

### 5.1 Hierarchy

CMO (Human)
 |
 |-- Sets strategy, approves high-stakes decisions, manages relationships
 |-- Interacts with agents via natural language (Claude Code / Cowork)
 |
 +-- Marketing Operations Orchestrator (Coordination Agent)
      |
      |-- Maintains marketing calendar, priorities, cross-agent dependencies
      |-- Routes work to domain agents; consolidates reporting for CMO
      |-- Knowledge base: calendar, priorities, budget, active campaigns
      |
      +-- WORKFLOW AGENTS (execute multi-step workflows end-to-end)
      |    |
      |    +-- Market Intelligence Agent
      |    |    Knowledge: competitor profiles, ICP definition, market signals, intent data
      |    |    Decides: what's changed, what matters, what to escalate
      |    |    Tools: WebSearch, Google Sheets, HubSpot (read)
      |    |    Cadence: continuous / scheduled (daily-weekly)
      |    |    Workflows: 0.1, 0.2, 0.4, 0.5, A.1, A.9, A.11
      |    |
      |    +-- Pipeline Agent
      |    |    Knowledge: HubSpot contact/deal state, ICP criteria, enrichment history
      |    |    Decides: who to prospect, how to score, when to escalate stale deals
      |    |    Tools: Apollo API, HubSpot MCP, enrichment APIs (PDL, ZeroBounce)
      |    |    Cadence: continuous + weekly batch
      |    |    Workflows: 1.1, 1.2, 1.3, 1.4, 1.6, 2.1, 2.4, 4.2, 4.5, 5.1, 5.2, 5.3, 5.4
      |    |
      |    +-- Engagement Agent
      |    |    Knowledge: contact engagement history, sequence templates, case study library, calendar
      |    |    Decides: what to say to whom, when, via which channel; meeting prep priorities
      |    |    Tools: HubSpot sequences, Gmail MCP, Google Calendar MCP
      |    |    Cadence: triggered (new contact, stale lead, upcoming meeting) + scheduled
      |    |    Workflows: 2.2, 2.3, 2.5, 2.6, 3.5, 4.3 (assist), 6.3
      |    |
      |    +-- Content Production Agent
      |    |    Knowledge: content calendar, AEO strategy, keyword gaps, performance data
      |    |    Decides: what to produce, how to structure for AI citation, when to update
      |    |    Tools: WebSearch, CMS, Google Sheets, schema validators
      |    |    Cadence: weekly production cycle + quarterly audits
      |    |    Workflows: 3.1, 3.2, 3.4, 3.8, 3.9, A.2, A.3, A.4, A.8
      |    |
      |    +-- Customer Success Agent
      |    |    Knowledge: customer usage/health data, expansion signals, success metrics, churn patterns
      |    |    Decides: who's at risk, who's ready for expansion, who to ask for case study
      |    |    Tools: Orita product APIs, HubSpot MCP, Slack MCP, Klaviyo API
      |    |    Cadence: weekly health checks + triggered alerts
      |    |    Workflows: 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7
      |    |
      |    +-- Analytics Agent
      |         Knowledge: HubSpot pipeline data, content metrics, attribution models, benchmarks
      |         Decides: what to measure, how to attribute, what to flag as anomalous
      |         Tools: HubSpot MCP, Google Sheets, Google Analytics
      |         Cadence: weekly dashboards + monthly deep analysis + quarterly reviews
      |         Workflows: 2.5, 4.6, 5.5, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6
      |
      +-- RESOURCE AGENTS (provide capabilities called by workflow agents)
           |
           +-- Brand Voice Agent
           |    Knowledge: brand guidelines, tone examples, messaging hierarchy, competitive positioning
           |    Provides: voice-consistent copy generation for any agent that produces customer-facing text
           |    Called by: Engagement Agent, Content Production Agent, Customer Success Agent, Partner workflows
           |    Not a workflow executor -- a quality gate and generative resource
           |
           +-- Enrichment Agent
           |    Knowledge: ICP filter criteria, enrichment API capabilities, dedup logic, validation rules
           |    Provides: contact enrichment, Klaviyo detection, email validation, deduplication
           |    Called by: Pipeline Agent, Engagement Agent (for meeting prep), Market Intelligence Agent
           |    This is the existing `/enrich` skill pattern generalized as a callable service
           |
           +-- Citation Authority Agent
                Knowledge: off-site citation targets, partner blog network, publication contacts, community accounts
                Provides: outreach drafting, placement tracking, citation graph maintenance
                Called by: Content Production Agent, Engagement Agent (for partner co-marketing)
                Workflows: 3.3, 3.6, 3.10, A.5, A.6, A.7, 6.1, 6.4, 6.5

### 5.2 Why This Decomposition

Workflow agents own end-to-end processes. Each one has a coherent knowledge base (the state it needs to make decisions), a consistent decision model (the kind of judgment it applies), and a well-defined tool surface (the APIs it calls). The Pipeline Agent knows HubSpot state and decides who to pursue. The Content Production Agent knows the AEO strategy and decides what to publish. They don’t need to know each other’s state to do their jobs.

Resource agents are shared capabilities, not workflow executors. The Brand Voice Agent doesn’t run workflows – it’s called by any workflow agent that needs to produce customer-facing text. The Enrichment Agent doesn’t decide who to prospect – it enriches contacts when asked. This prevents duplicating knowledge (brand voice guidelines would otherwise need to live in every agent that writes copy) and keeps workflow agents focused on decisions rather than mechanics.

The Orchestrator coordinates, not executes. It maintains the marketing calendar, resolves cross-agent dependencies (e.g., Content Production Agent needs case study from Customer Success Agent), and consolidates reporting for the CMO. It doesn’t make marketing decisions – it makes sequencing decisions.

The CMO makes three kinds of decisions that agents cannot: (a) strategic direction (which markets, which positioning, which bets), (b) relationship judgment (partner negotiations, key account decisions, hiring), and (c) approval of high-stakes outputs (public content, pricing changes, major campaign launches). Everything else is delegated.

### 5.3 Data / Knowledge Base Map

Each agent draws from specific knowledge sources. This map determines what needs to be built, connected, or maintained.

| Agent | Primary Knowledge Sources | Writeback Targets |
| --- | --- | --- |
| Market Intelligence | WebSearch results, StoreLeads domain list, G2 intent feed, competitor website snapshots, Klaviyo marketplace | Google Sheets (signals log), HubSpot (flagged accounts) |
| Pipeline | HubSpot contacts/deals/activities, Apollo search results, enrichment API responses, ICP config | HubSpot (contacts, deals, scores), Google Sheets (pipeline reports) |
| Engagement | HubSpot contact history, sequence performance data, case study library, Google Calendar | HubSpot (activities, sequences), Gmail (outbound), Calendar (meetings) |
| Content Production | Content calendar (Google Sheets), AEO gap analysis, WebSearch (research), content performance data, schema validator output | CMS (blog posts), Google Sheets (calendar, performance log) |
| Customer Success | Orita product usage data, HubSpot customer records, Klaviyo performance metrics, health score model | HubSpot (health scores, expansion flags), Slack (alerts), Google Sheets (QBR data) |
| Analytics | HubSpot pipeline/deal data, Google Analytics, content metrics, AI visibility monitoring data, financial data (CAC/LTV) | Google Sheets (dashboards, reports), Gmail/Slack (weekly digests) |
| Brand Voice (resource) | Brand guidelines doc, tone examples corpus, approved messaging, competitive positioning matrix | None (read-only resource; outputs are generated text passed back to calling agent) |
| Enrichment (resource) | ICP config (JSON/Sheet), StoreLeads domains, PDL/Apollo/ZeroBounce APIs, master contact list | HubSpot (enriched contacts), Google Sheets (enrichment results) |
| Citation Authority (resource) | Partner contact list, publication editorial calendars, community account credentials, citation tracking sheet | Google Sheets (placement tracking), Gmail (outreach) |
| Orchestrator | Marketing calendar, agent status/output logs, budget tracker, CMO priorities | Google Sheets (calendar, status), Slack/email (CMO briefings) |

### 5.4 Agent Interaction Patterns

Agents don’t operate in isolation. Key interaction patterns:

Pipeline Agent -> Enrichment Agent: Pipeline identifies a target list (from Apollo, event, or inbound); Enrichment Agent processes it (enrich, validate, dedup); result flows back to Pipeline Agent for HubSpot creation and scoring.

Content Production Agent -> Brand Voice Agent: Content Production determines what to write and structures it for AEO; Brand Voice Agent reviews/generates copy in the company’s voice; Content Production handles schema markup and publishing.

Content Production Agent -> Citation Authority Agent: Content Production identifies citation-building opportunities (guest posts, partner content); Citation Authority drafts outreach and tracks placements.

Customer Success Agent -> Content Production Agent: Customer Success identifies case study candidates; Content Production (via Brand Voice) drafts the case study.

Analytics Agent -> Orchestrator -> CMO: Analytics generates weekly dashboards and flags anomalies; Orchestrator consolidates across agents into a single CMO briefing; CMO adjusts priorities.

Market Intelligence Agent -> Pipeline Agent: Market Intelligence detects a new Klaviyo adopter or intent signal; flags the account; Pipeline Agent picks it up for prospecting.

## 6. Workflow Inventory

The complete inventory of workflows, now mapped to their parent agent. Each workflow is classified by automation tier:

A (Full automation): Runs unattended or with minimal approval.

B (AI-assisted): Agent drafts, human reviews/approves/triggers.

C (Human-led, tool-augmented): Strategy and judgment required; agent accelerates execution.

D (Human only): Relationship, negotiation, or creative judgment that can’t be delegated.

### Stage 0: Market Intelligence & ICP

| # | Workflow | Current State | Tier | Automation Approach | Tool Stack |
| --- | --- | --- | --- | --- | --- |
| 0.1 | Competitive landscape monitoring | Manual/ad hoc | A | Scheduled scrape of competitor websites, G2 profiles, app marketplace listings. Weekly digest to Slack or email. | Claude Code scheduled skill + WebSearch + Gmail/Slack MCP |
| 0.2 | New Klaviyo adopter detection | Partial (StoreLeads 418K domains, static) | A | Weekly diff of StoreLeads domain list to detect new Klaviyo customers. Flag companies matching ICP. Route to HubSpot. | Claude Code skill + Google Sheets API + HubSpot MCP |
| 0.3 | ICP refinement from win/loss data | Manual | B | Quarterly pull of closed-won/lost deals from HubSpot. Analyze title, company size, vertical, channel source. Recommend ICP keyword updates. | Claude Code + HubSpot MCP + Google Sheets |
| 0.4 | Industry trend monitoring | Manual | A | Scheduled search for “email deliverability,” “Klaviyo,” “ecommerce retention” topics. Weekly summary of notable developments. | Claude Code scheduled skill + WebSearch |
| 0.5 | G2/intent signal monitoring | Not implemented | B | Ingest G2 Buyer Intent data (API or CSV export) for “email deliverability” category. Score and route to HubSpot. | G2 Intent API + Claude Code + HubSpot MCP |

### Stage 1: Lead Generation & Prospecting

| # | Workflow | Current State | Tier | Automation Approach | Tool Stack |
| --- | --- | --- | --- | --- | --- |
| 1.1 | Event attendee list enrichment | Automated (existing skill) | A | Ingest CSV, ICP filter, Klaviyo detection, PDL/Apollo enrichment, ZeroBounce validation, deduplicate, output to Google Sheets. | Claude Code /enrich skill (existing) |
| 1.2 | Weekly Apollo prospecting pull | Manual | A | Scheduled Apollo search by ICP criteria. Deduplicate against HubSpot. Enrich. Create contacts in HubSpot with source tag. | Claude Code skill + Apollo API + HubSpot MCP |
| 1.3 | Inbound lead routing | Manual/basic | A | New HubSpot form submission triggers enrichment (firmographic, Klaviyo detection), lead scoring, and assignment. | HubSpot workflows + Claude Code enrichment |
| 1.4 | LinkedIn Sales Navigator export processing | Manual | B | Export from Sales Nav -> CSV -> ICP filter -> enrichment -> HubSpot. Same pattern as 1.1 but different input source. | Claude Code skill + PDL/Apollo + HubSpot MCP |
| 1.5 | Klaviyo community/forum monitoring | Not implemented | B | Monitor Klaviyo community for brands expressing deliverability pain. Capture company name, surface to sales. | Claude Code + WebSearch + HubSpot MCP |
| 1.6 | Website visitor identification | Not implemented | B | Reverse IP or identity resolution on orita.ai visitors. Match to HubSpot accounts. Alert on high-value visits. | Clearbit Reveal or RB2B + HubSpot MCP |

### Stage 2: Outbound & Sequences

| # | Workflow | Current State | Tier | Automation Approach | Tool Stack |
| --- | --- | --- | --- | --- | --- |
| 2.1 | Post-event follow-up sequence | Manual/semi-auto | A | Enrichment pipeline output triggers HubSpot sequence: Day 1 personal intro, Day 3 case study, Day 7 offer, Day 14 nurture. | HubSpot sequences + Claude Code trigger |
| 2.2 | Cold outreach sequence (non-event) | Manual | B | Claude drafts personalized first touch based on HubSpot contact data + Klaviyo detection status. Human reviews, triggers send. | Claude Code + HubSpot MCP + Gmail MCP |
| 2.3 | Pre-event outreach | Manual | B | For confirmed ICP attendees at upcoming events: personalized meeting requests referencing their Klaviyo usage and relevant case study. | Claude Code + HubSpot sequences + Gmail MCP |
| 2.4 | Stale lead re-engagement | Not implemented | A | Monthly HubSpot query for contacts with no activity >60 days. Generate re-engagement email with fresh case study or content. | HubSpot MCP + Claude Code skill |
| 2.5 | Sequence performance reporting | Manual | A | Weekly pull of sequence metrics from HubSpot. Open/reply/meeting rates by sequence. Flag underperformers. | Claude Code + HubSpot MCP + Google Sheets |
| 2.6 | Meeting prep brief | Manual | B | Before scheduled sales call: pull contact’s HubSpot history, company Klaviyo usage, relevant case study, and talking points into a one-page brief. | Claude Code + HubSpot MCP + Google Calendar MCP |

### Stage 3: Content & Discoverability

| # | Workflow | Current State | Tier | Automation Approach | Tool Stack |
| --- | --- | --- | --- | --- | --- |
| 3.1 | AEO/GEO content strategy | Not implemented | C | Research AI-cited sources for target queries. Identify content gaps. Plan calendar of answer-optimized articles. | Claude Code + WebSearch + Google Sheets |
| 3.2 | Blog post drafting (AEO-optimized) | Manual/infrequent | B | Claude drafts article from brief: question-mirroring headers, high fact density, structured data markup, internal/external links. Human edits and approves. | Claude Code + WebSearch (research) + CMS |
| 3.3 | Case study generation | Manual | B | Pull customer metrics from internal data. Claude drafts case study following brand voice template. Customer approves quotes. | Claude Code + HubSpot MCP + Google Docs |
| 3.4 | Social media content scheduling | Manual/sporadic | B | Generate week of social posts from blog content, case studies, and industry news. Schedule via Buffer or native platform. | Claude Code + Buffer API or native scheduling |
| 3.5 | Newsletter production | Manual | B | Monthly newsletter: pull top blog posts, case study highlights, upcoming events, product updates. Claude drafts, human reviews. | Claude Code + HubSpot email tool |
| 3.6 | Partner co-marketing content | Ad hoc | C | Co-branded content with agency partners (blog posts, webinars, case studies). Claude drafts from shared brief. | Claude Code + Google Docs collaboration |
| 3.7 | AEO/GEO visibility monitoring | Not implemented | A | Weekly check: query target terms in ChatGPT, Perplexity, Google AI Overviews. Track whether Orita is cited. Log to spreadsheet. | Claude Code scheduled skill + WebSearch + Google Sheets |
| 3.8 | SEO technical audit | Not implemented | B | Quarterly crawl of orita.ai. Check schema markup, page speed, broken links, sitemap health. Prioritized fix list. | Claude Code + site crawl tools |
| 3.9 | Content repurposing pipeline | Not implemented | B | Take one long-form piece and produce: 5 social posts, 1 email excerpt, 1 slide for sales deck, 1 partner-ready summary. | Claude Code skill |
| 3.10 | AI citation authority building | Not implemented | C | Systematic outreach for guest posts, expert quotes, and mentions in ecommerce publications, Klaviyo partner blogs, and industry roundups. | Manual outreach + Claude Code for drafting |

### Stage 4: Event Marketing

| # | Workflow | Current State | Tier | Automation Approach | Tool Stack |
| --- | --- | --- | --- | --- | --- |
| 4.1 | Event identification & ROI evaluation | Manual | B | Scrape upcoming ecommerce/DTC events. Score by attendee ICP overlap, cost, location. Recommend go/no-go. | Claude Code + WebSearch + Google Sheets |
| 4.2 | Pre-event attendee targeting | Semi-automated | A | Acquire attendee list -> enrichment pipeline -> segment by priority -> pre-event outreach sequence. | Existing enrichment skill + HubSpot sequences |
| 4.3 | Event logistics & scheduling | Manual | D | Booth booking, travel, staffing. Requires human coordination. | Google Calendar + manual |
| 4.4 | On-site lead capture | Manual | C | Badge scan or card collection -> digitize -> route to enrichment pipeline. | Event app + Claude Code ingest |
| 4.5 | Post-event pipeline processing | Semi-automated | A | Day-of: ingest all captured contacts -> enrich -> deduplicate against master -> create HubSpot contacts -> trigger follow-up sequence. | Claude Code skill + HubSpot MCP |
| 4.6 | Event ROI reporting | Manual | A | Post-event: pull all contacts sourced from event -> track through pipeline to closed-won. Calculate cost-per-meeting, cost-per-opportunity, cost-per-customer. | Claude Code + HubSpot MCP + Google Sheets |

### Stage 5: CRM & Pipeline Management

| # | Workflow | Current State | Tier | Automation Approach | Tool Stack |
| --- | --- | --- | --- | --- | --- |
| 5.1 | Contact enrichment on create | Manual | A | When new contact created in HubSpot: auto-enrich with firmographic data, Klaviyo detection, LinkedIn URL. | HubSpot workflow + Claude Code enrichment |
| 5.2 | Lead scoring model | Basic/manual | B | Score contacts by: ICP match, Klaviyo customer status, engagement level, company size, recency. Update HubSpot lead score. | Claude Code + HubSpot MCP |
| 5.3 | CRM hygiene automation | Manual | A | Weekly: deduplicate contacts, normalize company names, flag stale deals, identify contacts with missing fields. | Claude Code scheduled skill + HubSpot MCP |
| 5.4 | Pipeline stage automation | Manual | B | Auto-advance deals based on activity triggers (meeting held, proposal sent, contract viewed). Alert on stalled deals. | HubSpot workflows + Claude Code alerts |
| 5.5 | Weekly pipeline report | Manual | A | Pull HubSpot pipeline data. Summarize: new leads, meetings booked, deals advanced, revenue forecast. Deliver via email or Slack. | Claude Code + HubSpot MCP + Gmail/Slack MCP |
| 5.6 | Deal activity logging | Manual | B | After calls/meetings: Claude generates activity summary from notes. Logs to HubSpot contact timeline. | Claude Code + HubSpot MCP |

### Stage 6: Partner & Referral Channel

| # | Workflow | Current State | Tier | Automation Approach | Tool Stack |
| --- | --- | --- | --- | --- | --- |
| 6.1 | Partner onboarding kit generation | Not implemented | B | Generate customized partner packet: pitch deck, ROI calculator, demo script, case studies relevant to partner’s client vertical. | Claude Code + templates |
| 6.2 | Referral tracking & attribution | Informal | B | Track referral source on HubSpot deals. Monthly partner performance report: referrals, conversion rate, revenue attributed. | HubSpot MCP + Claude Code reporting |
| 6.3 | Partner communication cadence | Ad hoc | B | Monthly partner newsletter: product updates, new case studies, referral leaderboard, co-marketing opportunities. | Claude Code + Gmail/HubSpot MCP |
| 6.4 | Co-marketing campaign coordination | Ad hoc | C | Joint webinars, co-branded content, shared case studies with agency partners. | Manual coordination + Claude Code for content |
| 6.5 | Partner prospect identification | Not implemented | B | Identify Klaviyo agencies not yet partnered with Orita. Enrich agency contacts. Outreach sequence. | Apollo + Claude Code + HubSpot MCP |

### Stage 7: Customer Success & Expansion

| # | Workflow | Current State | Tier | Automation Approach | Tool Stack |
| --- | --- | --- | --- | --- | --- |
| 7.1 | Onboarding workflow triggers | Manual | A | New customer signed -> trigger onboarding email sequence, Slack notification to CS, calendar invite for kickoff. | HubSpot workflows + Slack MCP + Calendar MCP |
| 7.2 | Customer health scoring | Manual | B | Weekly: pull Orita product usage data + Klaviyo performance metrics. Score customer health. Flag at-risk accounts. | Claude Code + internal APIs + HubSpot MCP |
| 7.3 | Case study candidate identification | Manual | B | Monthly: query for customers with strong metrics (revenue lift >20%, engagement improvement). Draft outreach requesting case study participation. | Claude Code + HubSpot MCP + Gmail MCP |
| 7.4 | Expansion trigger detection | Not implemented | A | Monitor for signals: customer added new Klaviyo channels (SMS), GMV growth, increased profile count. Flag for upsell conversation. | Claude Code + Klaviyo API + HubSpot MCP |
| 7.5 | Review & testimonial solicitation | Manual | B | At 90-day and success milestones: automated request for G2 review, testimonial quote, or NPS response. | HubSpot workflows + Claude Code personalization |
| 7.6 | Churn risk intervention | Not implemented | B | Customer health score drops below threshold -> alert CS -> draft re-engagement plan with specific recommendations. | Claude Code + HubSpot MCP + Slack MCP |
| 7.7 | QBR preparation | Manual | B | Before quarterly business review: pull customer metrics, engagement trends, benchmark against cohort. Generate slide deck. | Claude Code + internal APIs + PPTX skill |

### Stage 8: Analytics & Attribution

| # | Workflow | Current State | Tier | Automation Approach | Tool Stack |
| --- | --- | --- | --- | --- | --- |
| 8.1 | Weekly marketing dashboard | Not implemented | A | Automated weekly pull: leads generated (by source), meetings booked, pipeline created, content published, AEO visibility score. | Claude Code + HubSpot MCP + Google Sheets |
| 8.2 | Multi-touch attribution report | Not implemented | B | Monthly: trace closed-won deals back through all touchpoints (event, content, outreach, partner). Identify highest-ROI channels. | HubSpot attribution + Claude Code analysis |
| 8.3 | Content performance analysis | Not implemented | A | Monthly: blog traffic, engagement, AEO citations, conversion to lead. Rank content by pipeline influence. | Claude Code + Google Analytics + Google Sheets |
| 8.4 | Event ROI comparison | Not implemented | A | Cross-event comparison: cost-per-lead, cost-per-meeting, cost-per-customer by event. Inform future event selection. | Claude Code + HubSpot MCP + Google Sheets |
| 8.5 | Funnel conversion analysis | Not implemented | B | Monthly: conversion rates between funnel stages. Identify bottlenecks. Recommend interventions. | Claude Code + HubSpot MCP |
| 8.6 | CAC/LTV tracking | Not implemented | B | Monthly: customer acquisition cost by channel, LTV by cohort, payback period. Compare to SaaS benchmarks. | Claude Code + HubSpot MCP + finance data |

### Cross-Cutting: Orita Product Strategy Workflows

| # | Workflow | Current State | Tier | Automation Approach | Tool Stack |
| --- | --- | --- | --- | --- | --- |
| 9.1 | Dogfood Orita for own marketing | Not implemented | C | Apply Orita’s engagement scoring to Orita’s own prospect/customer database. Suppress disengaged from nurture. Surface high-intent. | Orita product + HubSpot integration |
| 9.2 | Ad audience export pilot | Not implemented | C | Select 3-5 customers. Export engagement-scored segments as Meta custom audiences. Measure retargeting waste reduction. | Orita product + Meta Ads API |
| 9.3 | SMS optimization beta tracking | Underway | C | Track SMS channel performance for early adopters. Collect metrics for case studies. | Orita product + Klaviyo SMS data |
| 9.4 | Direct mail audience selection tracking | Underway | C | Track direct mail ROI for customers using Orita scoring vs. standard segmentation. | Orita product + PostPilot integration |
| 9.5 | Competitive positioning refresh | Quarterly/manual | B | Quarterly: scrape competitor feature pages, pricing, case studies. Update positioning matrix. Inform sales messaging. | Claude Code + WebSearch + Google Sheets |

## 7. Implementation Roadmap

### Phase 1: Foundation (Months 1-2)

Wire the core systems together. Every subsequent workflow depends on clean data flow between HubSpot, Apollo, Google Sheets, and Claude Code.

Connect HubSpot MCP to Claude Code (official connector available in public beta)

Set up Apollo API integration for prospecting pulls

Build Google Sheets <-> HubSpot contact sync (replace manual handoff)

Implement workflows: 0.1, 0.2, 1.2, 2.1, 5.1, 5.3, 5.5, 8.1

Estimated new automations: 8 | Tier A (fully automated)

### Phase 2: Pipeline Acceleration (Months 2-4)

Activate always-on prospecting and systematize outbound.

Implement workflows: 1.3, 1.6, 2.2, 2.3, 2.4, 2.5, 2.6, 4.2, 4.5, 5.2

Launch AEO/GEO content strategy (3.1) and begin producing optimized content (3.2)

Build AEO visibility monitoring (3.7)

Estimated new automations: 12 | Mix of Tier A and B

### Phase 3: Content & Discoverability Engine (Months 4-6)

Scale content production and establish AI citation authority.

Implement workflows: 3.2 (regularize cadence), 3.3, 3.4, 3.5, 3.8, 3.9, 3.10

Formalize partner channel: 6.1, 6.2, 6.3, 6.5

Launch customer expansion workflows: 7.1, 7.3, 7.4, 7.5

Estimated new automations: 14 | Mix of Tier A, B, and C

### Phase 4: Full Platform (Months 6-9)

Complete the automation chain. Measure everything.

Implement remaining workflows: 0.3, 0.5, 1.4, 1.5, 4.1, 4.6, 5.4, 5.6, 6.4, 7.2, 7.6, 7.7

Full analytics suite: 8.2, 8.3, 8.4, 8.5, 8.6

Omnichannel product pilots: 9.1, 9.2

Estimated new automations: 17 | Full tier range

### Total workflow count: 56

Tier A (full automation): ~18 workflows

Tier B (AI-assisted): ~26 workflows

Tier C (human-led, tool-augmented): ~9 workflows

Tier D (human only): ~3 workflows

At full build-out, a single marketing executive spends the majority of their time on Tier C and D activities (strategy, relationship building, creative judgment) while the automated and AI-assisted layers handle execution, reporting, and routine decisions.

## 8. Recommended Tool Stack

| Function | Tool | Role |
| --- | --- | --- |
| CRM & pipeline | HubSpot | System of record. MCP-connected to Claude. |
| Prospecting & enrichment | Apollo | Always-on ICP prospecting. API access required (not Basic plan). |
| Email validation | ZeroBounce | Batch validation for enriched contacts. |
| Klaviyo detection | StoreLeads (Google Sheet) | 418K domain reference for instant customer identification. |
| Automation orchestrator | Claude Code + MCP | Skills, scheduled tasks, and agentic workflows. |
| Content & AEO | Claude Code + WebSearch | Research, drafting, optimization, visibility monitoring. |
| Email sending | HubSpot / Gmail | Sequences and one-off sends. |
| Social scheduling | Buffer or native | Post scheduling from Claude-generated content. |
| Calendar | Google Calendar (MCP) | Meeting scheduling, event planning. |
| Analytics | HubSpot reporting + Google Sheets | Pipeline, attribution, content performance. |
| Intent signals | G2 Buyer Intent (future) | In-market account identification. |
| Visitor identification | Clearbit Reveal or RB2B (future) | Website visitor -> account matching. |
| Partner management | HubSpot (deal source tracking) | Referral attribution and reporting. |

## 9. Open Questions

What is Orita’s current pricing structure? ACV ranges determine SAM precision and influence which customer segments to prioritize in automation.

How deeply is HubSpot configured today? Active workflows, sequences, reporting, or primarily contact storage?

What does the sales cycle look like? Length, stages, typical objections, win rate?

What Apollo plan tier is active? API access is required for automated prospecting.

What is the current blog publishing cadence and who produces content?

Is there a formal partner referral structure, or is it purely organic?

Where are SMS and direct mail in the product roadmap? GA, beta, or planned?

Has Orita explored ad audience optimization with any customers, even informally?

What is the marketing budget as % of ARR? Determines which tool additions are feasible.

Is there a single marketing executive in place, or is this role being hired?

## Appendix A: AEO/GEO Implementation Chain (Orita’s Own Discoverability)

This appendix details the step-by-step implementation of answer engine optimization and generative engine optimization for Orita as a company. The objective: when a B2B buyer asks any AI assistant a question in Orita’s domain, Orita is cited, recommended, or named in the response.

### A.1 Why This Matters More Than Traditional SEO

The discoverability landscape has shifted structurally. Traditional search engine volume is projected to drop 25% in 2026 (Gartner). AI-referred traffic to retail sites grew 693% during the 2025 holiday season. For B2B, Forrester found 89% of buyers use generative AI as a key research source throughout the buying journey. Critically, 60% of sources cited by AI are not in Google’s top 10 results, which means the competitive field is different. Sites with high topical authority and structured, answer-ready content get cited regardless of traditional search ranking.

For Orita specifically: a buyer evaluating email deliverability tools will likely ask ChatGPT, Perplexity, or Claude something like “What’s the best tool to improve Klaviyo email deliverability?” or “How do I reduce unsubscribes on Klaviyo?” If Orita’s content is structured to answer these questions with specificity, authority, and schema markup, AI systems will cite it. If it isn’t, competitors or generic guides will capture the citation.

### A.2 Implementation Chain

The chain has seven links. Each is a distinct workstream with its own workflows (mapped to Section 5 numbers where applicable).

Link 1: AI Visibility Audit (Week 1-2)

Establish the baseline. Before optimizing, measure where Orita stands today.

Execution: - Query 20-30 target prompts across ChatGPT, Perplexity, Claude, Google AI Overviews, and Gemini. Target prompts fall into three categories: (a) brand queries (“What is Orita?”, “Orita vs [competitor]”), (b) category queries (“best Klaviyo deliverability tool,” “how to improve email sender reputation ecommerce”), and (c) problem queries (“why are my Klaviyo emails going to spam?”, “how to reduce email unsubscribes Shopify”). - Record whether Orita is cited, mentioned, recommended, or absent for each query on each platform. - Run the same queries for 3-5 competitors to establish relative Share of AI Voice. - Log results in a Google Sheet that becomes the ongoing tracking artifact.

Automation: Workflow 3.7 (AEO/GEO visibility monitoring, Tier A). Build as a Claude Code scheduled skill that runs weekly after the initial manual baseline. Tools like Otterly.AI or OpenLens (free) can supplement with continuous monitoring.

Link 2: Query-Gap Analysis (Week 2-3)

Map the gap between what buyers ask and what Orita’s content answers.

Execution: - From the audit, identify queries where Orita is absent but competitors are cited. - From HubSpot sales call notes and lost-deal reasons, extract the actual questions prospects ask during evaluation. - From Klaviyo community forums, extract recurring deliverability questions. - Cross-reference these against existing orita.ai/blog content. The gap is the content calendar.

Output: A prioritized list of 15-25 target queries, each mapped to a content piece that needs to exist. Prioritize by: (a) commercial intent (category/problem queries over informational), (b) current competitive gap (queries where no one has a strong answer), (c) Orita’s ability to answer with proprietary data or unique insight.

Automation: Workflow 3.1 (AEO/GEO content strategy, Tier C). The research phase is AI-assisted; the prioritization requires human judgment about what Orita can credibly claim authority on.

Link 3: Content Production Pipeline (Ongoing, starting Week 3)

Produce answer-optimized content at a sustainable cadence.

Each content piece follows a structural template designed for AI citation:

Question-mirroring H1/H2 headers: Headers should mirror the exact query a buyer would type. “How to improve Klaviyo email deliverability” rather than “Our Approach to Deliverability.”

Answer-first structure: The direct answer appears in the first 40-60 words. AI systems frequently extract opening sentences for citations.

Fact density: Specific numbers, named methodologies, quantified outcomes. “31% increase in campaign revenue” rather than “significant improvement.” AI systems prefer content with concrete, citable claims.

Topical depth via clusters: Build pillar pages (e.g., “The Complete Guide to Klaviyo Email Deliverability”) surrounded by supporting articles (sender reputation, bot detection, re-engagement strategies, list hygiene). Connect the cluster with internal links. Topical clusters build authority that isolated posts cannot.

Schema markup: FAQPage schema on every article with embedded Q&A pairs. FAQ schema has one of the highest citation rates in AI-generated answers. HowTo schema on instructional content. Organization and Product schema on key pages.

Freshness signals: Update dates, current-year statistics, references to recent platform changes. AI systems weight recency.

Target cadence: 2-3 AEO-optimized articles per month, plus quarterly updates to existing high-value pages.

Automation: Workflow 3.2 (Blog post drafting, Tier B). Claude researches and drafts; human edits for brand voice, verifies claims, and approves. The drafting time drops from days to hours. Workflow 3.9 (Content repurposing, Tier B) then generates social, email, and partner derivatives from each piece.

Link 4: Schema Markup & Technical Foundation (Week 3-4, then ongoing)

Structured data is the machine-readable signal layer that tells AI systems what your content means and how to use it.

Implementation: - FAQPage schema on every blog post and landing page with Q&A content. Each question should be concise (~15 words) with a direct answer (30-50 words). - HowTo schema on instructional content (setup guides, troubleshooting articles). Define steps, tools, expected outcomes. - Organization schema on the homepage and about page: founding date, description, founder, social profiles. - Product schema on the product page: name, description, features, pricing tier information (if public), aggregateRating. - Review/AggregateRating schema linking to G2 or Klaviyo marketplace reviews. - Entity-level schema connecting Orita-as-organization to Orita-as-product to key people to the Klaviyo ecosystem.

Validation: Use Google’s Rich Results Test and Schema.org validator after each deployment.

Automation: Workflow 3.8 (SEO technical audit, Tier B). Quarterly validation that schema is deployed correctly, hasn’t broken, and covers new content.

Link 5: Off-Site Citation Authority (Ongoing, starting Month 2)

AI systems weight sources that are cited, linked, and mentioned across multiple authoritative domains. On-site optimization alone is insufficient; Orita needs to appear in the reference graph that AI systems build from the open web.

Channels, ranked by effort-to-impact ratio:

Klaviyo partner blog network: Orita’s existing agency partners (Flowium, ATTN Agency, etc.) already write about Orita. Formalize this: provide partners with co-brandable content briefs, data points, and case study excerpts. Every partner blog post that mentions Orita with a link adds a citation node. Target: 2-3 partner posts per quarter.

Klaviyo community contributions: Direct answers to deliverability questions in the Klaviyo community forum, attributed to Orita team members. Not promotional – genuinely helpful, with links to detailed resources on orita.ai where appropriate. AI systems index community content.

Ecommerce trade publications: Guest posts or expert quotes in publications like Practical Ecommerce, eCommerce Fastlane, Shopify Plus blogs, and DTC newsletters. Target the specific queries from the gap analysis. One authoritative guest post per month.

Industry roundups and comparison pages: Ensure Orita is included in “best of” lists for email deliverability, Klaviyo tools, and ecommerce marketing optimization. These pages are heavily cited by AI. Proactively submit for inclusion where editorial processes allow.

Data-driven original research: Publish annual or semi-annual reports using aggregate (anonymized) data from Orita’s customer base. “State of Ecommerce Email Deliverability 2026” with real benchmarks is exactly the kind of content AI systems cite as authoritative. High effort, high citation value.

Automation: Workflow 3.10 (AI citation authority building, Tier C). The outreach and relationship management is human-led; Claude drafts the content, briefs, and pitches.

Link 6: Monitoring & Iteration Loop (Ongoing, starting Week 4)

Track visibility across AI platforms and iterate based on what’s working.

Metrics: - Share of AI Voice: Percentage of target queries where Orita is cited vs. competitors. Measured weekly. - Citation frequency: How often Orita appears across all monitored queries. Trending up/down/flat. - Attributed referral traffic: Visits to orita.ai from AI platform referral sources (track via UTM or referrer analysis). - Query coverage: What percentage of the 15-25 target queries produce an Orita citation on at least one platform. - Sentiment quality: When AI mentions Orita, is it positive, neutral, or qualified? Track qualitative shifts.

Tools: Otterly.AI for automated monitoring across ChatGPT, Perplexity, Google AI Overviews, Gemini, and Copilot. OpenLens (free) as a supplementary tracker. Internal Claude Code skill (workflow 3.7) for custom query monitoring not covered by tools.

Feedback loop: Monthly review of visibility data feeds back into the content calendar (Link 3) and outreach priorities (Link 5). Double down on content patterns that generate citations; retire or restructure patterns that don’t.

Automation: Workflow 3.7 (Tier A) for the monitoring. Workflow 8.3 (Content performance analysis, Tier A) for the analytics layer.

Link 7: Competitor Response Tracking (Ongoing)

As AEO/GEO becomes mainstream, competitors will optimize too. Track their moves.

Execution: - Monthly: check whether competitors have added schema markup, restructured content, or published new answer-optimized pages. - Track shifts in Share of AI Voice relative to competitors. - Identify queries where Orita had citations but lost them – diagnose why (competitor published better content, information went stale, source fell out of AI index).

Automation: Subsumed into Workflow 0.1 (Competitive landscape monitoring, Tier A).

### A.3 AEO/GEO Workflow Summary

| # | Workflow | Link | Tier | Cadence |
| --- | --- | --- | --- | --- |
| A.1 | Initial AI visibility audit | 1 | B | One-time (Week 1-2) |
| A.2 | Query-gap analysis | 2 | C | Quarterly refresh |
| A.3 | AEO content production | 3 | B | 2-3 articles/month |
| A.4 | Schema markup deployment | 4 | B | Per-publish + quarterly audit |
| A.5 | Partner citation outreach | 5 | C | 2-3 partner posts/quarter |
| A.6 | Community contributions | 5 | C | Weekly (15 min/day) |
| A.7 | Trade publication placement | 5 | C | 1 placement/month |
| A.8 | Original research publication | 5 | C | Semi-annual |
| A.9 | AI visibility monitoring | 6 | A | Weekly (automated) |
| A.10 | Content performance review | 6 | B | Monthly |
| A.11 | Competitor AEO tracking | 7 | A | Monthly (automated) |

### A.4 Expected Timeline to Impact

AEO/GEO is not instant. AI systems re-index at varying cadences (Google AI Overviews is near-real-time for indexed pages; ChatGPT and Claude update training data and retrieval indices on slower cycles, though Perplexity indexes fresh content rapidly).

Weeks 1-4: Audit, gap analysis, schema deployment, first 2-3 optimized articles published.

Months 2-3: First citation appearances on Perplexity and Google AI Overviews (fastest to index new content). Partner content pipeline producing 2-3 external mentions. Monitoring cadence established.

Months 4-6: Citation frequency measurable across 3+ platforms. Share of AI Voice baseline established. Content cluster building topical authority. First original research piece published.

Months 6-12: Compounding effect: topical authority + citation graph + schema + freshness signals create a reinforcing cycle. Target: Orita cited in >50% of target queries on at least 2 platforms.

## Appendix B: AEO/GEO Intelligence for Ecommerce Customers (Product Concept)

This appendix sketches a potential product offering where Orita applies its audience intelligence to help ecommerce brands optimize their own discoverability in AI-driven shopping experiences. This is a medium-term opportunity (18-36 months) that depends on Orita first building internal AEO/GEO competence (Appendix A).

### B.1 The Ecommerce AI Discoverability Problem

The same structural shift affecting B2B discoverability is now hitting ecommerce. AI shopping assistants are becoming a significant discovery channel: traffic to US retail sites from AI sources grew 693% during the 2025 holiday season. Morgan Stanley projects that nearly half of online shoppers will use AI shopping agents by 2030, accounting for ~25% of their spending. The global agentic commerce market is projected to grow from $547M (2025) to $5.2B (2033).

When a consumer asks ChatGPT “What’s the best moisturizer for dry skin under $40?” or Perplexity “running shoes for flat feet,” the AI assistant synthesizes recommendations from product reviews, editorial content, structured product data, and brand authority signals. The brands that appear in these recommendations capture consideration without paying for it. The brands that don’t are invisible in a growing channel.

ChatGPT selects product recommendations based on authoritative list mentions (41% of recommendations), awards (18%), and review volume (16%). Structured data quality – not SEO seniority – determines which SKUs get cited. The two emerging commerce protocols (OpenAI/Stripe’s Agentic Commerce Protocol and Google’s Universal Commerce Protocol) formalize how AI agents discover and transact with merchants.

This is a problem Orita’s customers face directly. The ecommerce brands using Orita to optimize email engagement are the same brands that need to appear in AI shopping recommendations. And Orita already has the data layer that could inform it.

### B.2 What Orita Knows That Others Don’t

Orita’s engagement scoring engine processes hundreds of billions of engagement signals daily across its customer base. This data reveals:

Which products drive engagement: Products that generate clicks, repeat purchases, and re-engagement signals are the products that resonate. This is a signal of which products to prioritize for AI discoverability optimization.

Which customer segments engage with which content: Engagement patterns reveal which product stories, descriptions, and value propositions actually work. AI-optimized product content should reflect what real customers respond to, not what marketing teams assume will work.

Lifecycle timing: Orita knows when customers are most receptive to discovery (early lifecycle) vs. loyalty (mature lifecycle). This informs when and how to surface products in AI-accessible channels.

Cross-category interest patterns: For brands with broad catalogs, Orita’s scoring reveals which product categories cluster together in customer engagement. This informs how to structure product content clusters for topical authority.

No competitor has this combination of engagement depth + ESP integration + daily scoring cadence applied to the AI discoverability problem. The Klaviyo integration is the current instantiation, but the data advantage generalizes to any ESP that exposes engagement signals.

### B.3 Product Concept: Orita AI Visibility

Working name: Orita AI Visibility (or similar)

Core premise: Use Orita’s engagement intelligence to help ecommerce brands get their products recommended by AI shopping assistants.

Feature set (conceptual):

Product Discoverability Scoring: For each product in a brand’s catalog, score its likelihood of appearing in AI shopping recommendations. Based on: structured data quality, review volume and sentiment, editorial mention frequency, engagement signal strength (from Orita’s scoring), and competitive density for the product category.

Engagement-Informed Content Recommendations: Surface which product attributes, descriptions, and value propositions drive the most engagement in Orita’s scoring model. Recommend content optimizations that align high-engagement signals with AI-discoverable structured data. Example: “Your customers engage most with [product X] when messaging emphasizes [attribute Y] – but your product schema doesn’t include [attribute Y]. Adding it would improve AI discoverability.”

Schema Markup Audit & Generation: Audit the brand’s product pages for structured data quality (Product schema, Review schema, FAQ schema, Offer schema). Generate corrected/enhanced schema markup. This is the most tactically immediate value – structured data quality is the single highest-leverage factor in AI product citation.

AI Visibility Monitoring: Track which of the brand’s products appear in AI shopping recommendations for target queries. Monitor competitors. Report Share of AI Voice at the product and category level. Same monitoring approach as Appendix A, applied to shopping queries rather than B2B queries.

Content Gap Analysis: Identify product categories where the brand has strong engagement data (from Orita scoring) but weak AI discoverability. Prioritize content and structured data investments where the engagement signal says there’s demand but the discoverability signal says AI assistants aren’t finding the product.

Integration model: Plugs into the existing ESP + Shopify stack via Orita’s current integrations (Klaviyo today, extensible to other ESPs). No additional merchant engineering required. Uses existing Orita engagement data + reads product catalog from Shopify + monitors AI platforms externally.

### B.4 Market Sizing (Rough)

The addressable market is Orita’s existing customer base plus the broader set of ecommerce brands concerned about AI discoverability.

Orita’s existing customers (who already pay for engagement scoring) would be the first adopters. Upsell ACV: $3K-$12K/yr depending on catalog size.

The broader market: every mid-market and enterprise ecommerce brand with a Shopify or Klaviyo presence. The $5M-$50M GMV segment (~15,000-25,000 US Klaviyo customers) is the sweet spot – large enough to care about discoverability, not large enough to have in-house teams solving it.

The agentic commerce market itself ($547M in 2025, growing to $5.2B by 2033) is the TAM for tools that help merchants participate in this channel.

### B.5 Dependencies & Sequencing

This product concept depends on several preconditions:

Internal AEO/GEO competence (Appendix A): Orita needs to have successfully implemented AEO/GEO for its own discoverability before credibly selling it to customers. The internal implementation generates the expertise, playbooks, and case data that become the product.

Engagement-to-discoverability correlation validation: The hypothesis that Orita’s engagement signals predict AI discoverability success needs testing. Pilot with 3-5 existing customers: run engagement-informed content optimizations and measure whether AI citation rates improve. If the correlation holds, the product thesis is validated.

Monitoring infrastructure: The AI visibility monitoring capability (tracking product citations across ChatGPT, Perplexity, Google AI Mode, etc.) needs to be built once and can serve both the internal use case (Appendix A) and the customer-facing product.

Schema generation capability: Automated generation of correct Product, Review, and FAQ schema markup for Shopify stores. This is a well-scoped engineering problem.

Recommended sequencing: - Months 1-6: Build internal AEO/GEO capability (Appendix A). Validate the approach. - Months 4-8: Build monitoring infrastructure that serves both internal and customer use cases. - Months 6-9: Run pilot with 3-5 customers. Test engagement-to-discoverability hypothesis. - Months 9-12: If pilot validates, package as product. Launch to existing customer base as upsell. - Months 12-18: Expand to non-Orita customers as standalone offering or bundled with core product.

### B.6 Strategic Implications

If this product concept validates, it fundamentally repositions Orita. The company moves from “AI segmentation for email deliverability” to “AI audience intelligence for customer communications and discoverability.” The omnichannel narrative expands from “email + SMS + direct mail + advertising” to include “AI-driven commerce discovery” as a channel surface.

This positioning aligns with the market’s direction. The ecommerce brands Orita serves will increasingly face the question: “How do I get my products recommended by AI?” Having a credible answer – grounded in engagement data that Orita already collects – is a durable competitive advantage.

The risk is premature investment. The agentic commerce market is still early ($547M). The protocols (ACP, UCP) are still evolving. Orita should invest in building the internal AEO/GEO capability (Appendix A) regardless, because that capability serves the company’s own acquisition needs. The product extension should wait until the pilot data confirms the engagement-to-discoverability correlation.

## Sources

Orita Homepage

Orita + Klaviyo: Smarter Segmentation

Orita Named Klaviyo Premier Partner

Spanx x Orita x Klaviyo Case Study

Email Deliverability Tools Market Report 2026

Klaviyo 2025 10-K Filing

Klaviyo Q2 2025 Investor Presentation

Shopify Statistics 2026

GEO for B2B SaaS Playbook

AEO Guide for B2B

HubSpot MCP Server

HubSpot Connector for Claude

Apollo.io Prospecting Platform

B2B SaaS Marketing Benchmarks 2025

AI Marketing for B2B SaaS: Scale Pipeline 2026

AEO Content Audit Checklist - Stackmatix

Complete AEO Guide - Frase.io

AEO Guide: Brand AI Visibility - NoGood

FAQ Schema for AI Search - Frase.io

Schema Markup for AEO - AirOps

Otterly.AI - AI Search Monitoring

OpenLens - Free AI Visibility Platform

AI Visibility Tools 2026 - Evertune

AI Shopping Assistant Guide 2026 - Opascope

Perplexity Shopping Optimization - Shopify

AI Visibility for Ecommerce - VisualSEOPro

Product Data Enrichment for AI Discoverability - Nudge

Agentic Commerce - Shopify
