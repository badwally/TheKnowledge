---
id: arxiv-2507.06520
type: arxiv
title: 'Gradientsys: A Multi-Agent LLM Scheduler with ReAct Orchestration'
url: http://arxiv.org/abs/2507.06520v1
authors:
- Xinyuan Song
- Zeyu Wang
- Siyi Wu
- Tianyu Shi
- Lynn Ai
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:9ae639e694003ffb10e258af7975279d31f0f2c6cf0e59ff995551b0a2587a2b
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2507.06520.md
  legacy_slug: arxiv_2507.06520
published_at: '2025-07-09'
filter:
  score: 0.8
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Gradientsys: A Multi-Agent LLM Scheduler with ReAct Orchestration

**Authors:** Xinyuan Song, Zeyu Wang, Siyi Wu, Tianyu Shi, Lynn Ai  
**Published:** 2025-07-09T03:40:56Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2507.06520v1.pdf

## Abstract

We present Gradientsys, a next-generation multi-agent scheduling framework that coordinates diverse specialized AI agents using a typed Model-Context Protocol (MCP) and a ReAct-based dynamic planning loop. At its core, Gradientsys employs an LLM-powered scheduler for intelligent one-to-many task dispatch, enabling parallel execution of heterogeneous agents such as PDF parsers, web search modules, GUI controllers, and web builders. The framework supports hybrid synchronous/asynchronous execution, respects agent capacity constraints, and incorporates a robust retry-and-replan mechanism to handle failures gracefully. To promote transparency and trust, Gradientsys includes an observability layer streaming real-time agent activity and intermediate reasoning via Server-Sent Events (SSE). We offer an architectural overview and evaluate Gradientsys against existing frameworks in terms of extensibility, scheduling topology, tool reusability, parallelism, and observability. Experiments on the...

## Relevance

**Score:** 4/5  
Presents Gradientsys, a multi-agent scheduler using typed Model Context Protocol (MCP) and ReAct-based dynamic planning for parallel orchestration of heterogeneous agents. Directly addresses MCP protocol design, agent scheduling topology, hybrid sync/async execution, and observability — core agentic workflow architecture topics.
