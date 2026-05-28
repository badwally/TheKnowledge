---
schema_version: 1
type: concept
slug: agent-escalation-levels
canonical_name: Agent Escalation Levels (0–4)
domains:
- orita-cmo
created_at: '2026-05-28T01:52:47Z'
last_updated: '2026-05-28T02:04:32Z'
---

# Agent Escalation Levels (0–4)

## Summary

The Agent Escalation Levels are a five-tier framework Orita uses to classify any proposed marketing-automation workflow by architectural complexity before deciding what orchestration to build [[sources/docx-b90a5e5fdcc4]]. The core question the framework answers is: at what point does the interaction between Orita's 56 planned workflows force a genuine orchestration framework, and what does that framework actually need to do [[sources/docx-b90a5e5fdcc4]]. The framework starts from the observation that most products marketed as “AI agent platforms” are not multi-agent systems but cron-triggered pipelines that call an LLM with structured prompts, store the output, and present it through a dashboard — “agent” is marketing terminology for a task-specific prompt template [[sources/docx-b90a5e5fdcc4]].

## Key claims

- The escalation is not binary; there are five distinct levels (0 through 4), each triggered by a specific type of coupling between workflows [[sources/docx-b90a5e5fdcc4]].
- Level 0 — Cron + Prompt Templates: each workflow is an independent function (fetch data, call LLM with structured prompt, store output) with no awareness of other workflows; applies when every workflow is advisory and inputs are fully determined before the workflow runs [[sources/docx-b90a5e5fdcc4]].
- Level 0 covers roughly 60% of Orita's 56-workflow plan, including SEO/GEO audits of orita.ai, content calendar generation, competitor monitoring scans, dashboard and report refreshes, Hacker News / Reddit / social media monitoring, brand-voice document generation, and AEO visibility tracking [[sources/docx-b90a5e5fdcc4]].
- Level 0 reference implementation is Okara.ai; the infrastructure required is just a scheduler (cron, Vercel Cron, node-cron), a results database (Postgres), LLM API access, and domain-specific API integrations — no framework [[sources/docx-b90a5e5fdcc4]].
- Level 0 test: if a workflow's inputs are fully determined before it runs and its outputs don't alter another workflow's behavior, it belongs at Level 0 [[sources/docx-b90a5e5fdcc4]].
- Level 1 — Shared Data Store with Implicit Coordination: multiple idempotent steps read and write a shared store; coordination happens through the data (step N reads what step N-1 wrote); no explicit orchestrator is needed because the sequence is fixed [[sources/docx-b90a5e5fdcc4]].
- The reference implementation for Level 1 inside Orita is the existing etail-contact-enrichment pipeline (CSV → ICP filter → dedup → Klaviyo detection → local match → PDL enrich → ZeroBounce → LinkedIn dedup → output), with Google Sheets as the shared data store and main.py as the sequential orchestrator, each step idempotent via sheet-diff skip logic [[sources/docx-b90a5e5fdcc4]].
- Other Level 1 examples in the Orita plan: prospecting pipeline (identify → enrich → score → stage in CRM), partner onboarding (intake → validation → setup → activation), and event-to-pipeline flow (attendee list → filter → enrich → route) [[sources/docx-b90a5e5fdcc4]].
- Level 2 — Conditional Routing Based on Intermediate State: the next step depends on an LLM judgment made during the current step, with non-trivial branching that grows over time; this is the first threshold where a framework might earn its cost [[sources/docx-b90a5e5fdcc4]].
- Canonical Level 2 example is the Pipeline Agent: lead arrives from enrichment, agent scores it, then routes to outbound sequence, Customer Success expansion detection, Market Intelligence, or manual review depending on score, ICP membership, Klaviyo status, and data sufficiency [[sources/docx-b90a5e5fdcc4]].
- Other Level 2 examples include the Customer Success Agent's intervention-trigger routing (engagement decay vs. support ticket volume vs. billing issue) and the Engagement Agent's outbound-sequence selection based on company size, persona, referral source, and prior touchpoints [[sources/docx-b90a5e5fdcc4]].
- Why cron-loops fail at Level 2: deeply nested if/else trees grow with every new route, the logic for “high-value lead” or “churn trigger” drifts across multiple scripts, testing becomes combinatorial, and adding a route requires understanding all existing routes [[sources/docx-b90a5e5fdcc4]].
- LangGraph is the best fit for Level 2: a directed-graph model where each node is a processing step and edges are conditional on node output, with built-in checkpointing and retry logic [[sources/docx-b90a5e5fdcc4]].
- CrewAI hierarchical mode is a weaker fit at Level 2 because the manager LLM does not reliably route (documented coordination-quality issues) and adds latency and cost without corresponding routing intelligence [[sources/docx-b90a5e5fdcc4]].
- A hand-rolled state machine (Python or TypeScript) avoids framework dependency at Level 2 when there are fewer than 5–6 routes and they change infrequently; it becomes unmaintainable beyond that threshold [[sources/docx-b90a5e5fdcc4]].
- Level 2 test: if routing logic grows with each new use case, or if the routing decision itself requires LLM judgment, the workflow belongs at Level 2 [[sources/docx-b90a5e5fdcc4]].
- Level 3 — Cross-Workflow Event Cascades: one workflow's output triggers or modifies the behavior of a different, independently-scheduled workflow with its own state; this is a message-broker problem, not a multi-agent framework problem [[sources/docx-b90a5e5fdcc4]].
- Canonical Level 3 example: Analytics Agent detects sustained engagement drop → Customer Success Agent investigates affected accounts → Content Production Agent adjusts messaging → Brand Voice Agent updates guidelines [[sources/docx-b90a5e5fdcc4]].
- What Level 3 needs is an event bus where workflows publish typed signals (e.g., engagement_drop_detected, deal_closed, competitor_feature_launched) with metadata, and subscribers react; the Orchestrator (Marketing Operations) is the entity that decides which signals to propagate and with what priority [[sources/docx-b90a5e5fdcc4]].
- Level 3 implementation options are Redis Pub/Sub (lightweight, no persistence — acceptable for near-real-time subscribers), Postgres LISTEN/NOTIFY (zero added infrastructure, limited throughput), Kafka / RabbitMQ (durable and replayable but overkill for Orita scale), or an LLM-powered router where the Orchestrator decides which downstream workflows to trigger [[sources/docx-b90a5e5fdcc4]].
- Multi-agent frameworks (CrewAI, LangGraph) are explicitly the wrong tool for Level 3 because the coupling is between workflows, not between agents within a workflow — the framework operates at the wrong level of abstraction [[sources/docx-b90a5e5fdcc4]].
- Level 3 danger signal: cross-workflow pub/sub logic scattered across scripts where no one can draw the full dependency graph from memory [[sources/docx-b90a5e5fdcc4]].
- Level 4 — Collaborative Multi-Agent Reasoning with Shared Memory: multiple specialized agents reason about each other's outputs in a conversational loop, refining a shared artifact through iteration; this is the only level where a true multi-agent framework is irreplaceable, and the level least likely to be needed in the near term [[sources/docx-b90a5e5fdcc4]].
- Speculative Level 4 examples (probably 9+ months out): CMO briefing synthesis (Analytics + Pipeline + Customer Success + Market Intelligence + Content challenging each other's claims), campaign strategy development, and ICP refinement [[sources/docx-b90a5e5fdcc4]].
- A single LLM call that receives all agent outputs in its context window and synthesizes them is simpler and probably produces equivalent quality for the near term; the multi-agent loop only earns its cost when combined context exceeds the window, iterative refinement is demonstrably required, or agents need different tools/APIs during the loop [[sources/docx-b90a5e5fdcc4]].
- Level 4 framework candidates are CrewAI sequential process (simple but rigid), LangGraph cycles (more flexible, supports conditional exits), and AutoGen GroupChat (most natural for the challenge pattern but hardest to control and most expensive since every turn is an LLM call) [[sources/docx-b90a5e5fdcc4]].
- Distribution mapping of Orita's 56-workflow plan: ~60% stay at Level 0–1 indefinitely; ~25% reach Level 2 by month 6–9; ~10% reach Level 3 by month 9–12; Level 4 is a stretch goal, likely satisfiable by single-pass LLM synthesis for the foreseeable future [[sources/docx-b90a5e5fdcc4]].
- Practical recommendations: build Level 0–1 for everything first to establish the data layer; introduce LangGraph per-workflow only (not system-wide) when branching becomes painful; use an event bus (Redis Pub/Sub or Postgres LISTEN/NOTIFY) for cross-workflow signals; reserve multi-agent reasoning for the Orchestrator's synthesis tasks and start with stuffing all outputs into one context window before building conversational loops [[sources/docx-b90a5e5fdcc4]].
- CrewAI has broken backward compatibility multiple times, cited as a reason to avoid system-wide framework adoption [[sources/docx-b90a5e5fdcc4]].
- Symmetric danger signals: too-late orchestration shows up as ad-hoc pub/sub between scripts and an unknowable dependency graph; too-early orchestration shows up as engineering time spent fighting framework abstractions rather than building workflows that deliver value [[sources/docx-b90a5e5fdcc4]].

## Sources

- [[sources/docx-b90a5e5fdcc4]] — Orita Agent Architecture Analysis (2026-04-03)

## Related

- [[concepts/workflow-resource-agent-architecture]]
- [[concepts/claude-code-velocity-model]]
- [[entities/langgraph]]
- [[entities/crewai]]
- [[entities/autogen]]
- [[entities/okara-ai]]
- [[entities/orita]]
