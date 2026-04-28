---
id: arxiv-2508.02866
type: arxiv
title: 'PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic
  Workflows'
url: http://arxiv.org/abs/2508.02866v3
authors:
- Renan Souza
- Amal Gueroudji
- Stephen DeWitt
- Daniel Rosendo
- Tirthankar Ghosal
- Robert Ross
- Prasanna Balaprakash
- Rafael Ferreira da Silva
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:b6906c80a0fa22a03798ccc1bd39f1f645edf765bdcd7dfe2369f5c181a19550
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2508.02866.md
  legacy_slug: arxiv_2508.02866
published_at: '2025-08-04'
filter:
  score: 0.8
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows

**Authors:** Renan Souza, Amal Gueroudji, Stephen DeWitt, Daniel Rosendo, Tirthankar Ghosal, Robert Ross, Prasanna Balaprakash, Rafael Ferreira da Silva  
**Published:** 2025-08-04T19:54:40Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2508.02866v3.pdf

## Abstract

Large Language Models (LLMs) and other foundation models are increasingly used as the core of AI agents. In agentic workflows, these agents plan tasks, interact with humans and peers, and influence scientific outcomes across federated and heterogeneous environments. However, agents can hallucinate or reason incorrectly, propagating errors when one agent's output becomes another's input. Thus, assuring that agents' actions are transparent, traceable, reproducible, and reliable is critical to assess hallucination risks and mitigate their workflow impacts. While provenance techniques have long supported these principles, existing methods fail to capture and relate agent-centric metadata such as prompts, responses, and decisions with the broader workflow context and downstream outcomes. In this paper, we introduce PROV-AGENT, a provenance model that extends W3C PROV and leverages the Model Context Protocol (MCP) and data observability to integrate agent interactions into end-to-end work...

## Relevance

**Score:** 4/5  
Introduces PROV-AGENT, a provenance model extending W3C PROV that leverages Model Context Protocol (MCP) and data observability to track agent interactions across federated, heterogeneous agentic workflows. Directly addresses MCP in agentic pipeline observability with peer-reviewed publication at IEEE e-Science 2025.
