---
id: arxiv-2511.16402
type: arxiv
title: 'Trustworthy AI in the Agentic Lakehouse: from Concurrency to Governance'
url: http://arxiv.org/abs/2511.16402v1
authors:
- Jacopo Tagliabue
- Federico Bianchi
- Ciro Greco
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:f98b78965f5d380382259cfab3be165416a6f1fee26d62254f4233774d9a6b0f
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2511.16402.md
  legacy_slug: arxiv_2511.16402
published_at: '2025-11-20'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Trustworthy AI in the Agentic Lakehouse: from Concurrency to Governance

**Authors:** Jacopo Tagliabue, Federico Bianchi, Ciro Greco  
**Published:** 2025-11-20T14:21:34Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2511.16402v1.pdf

## Abstract

Even as AI capabilities improve, most enterprises do not consider agents trustworthy enough to work on production data. In this paper, we argue that the path to trustworthy agentic workflows begins with solving the infrastructure problem first: traditional lakehouses are not suited for agent access patterns, but if we design one around transactions, governance follows. In particular, we draw an operational analogy to MVCC in databases and show why a direct transplant fails in a decoupled, multi-language setting. We then propose an agent-first design, Bauplan, that reimplements data and compute isolation in the lakehouse. We conclude by sharing a reference implementation of a self-healing pipeline in Bauplan, which seamlessly couples agent reasoning with all the desired guarantees for correctness and trust.

## Relevance

**Score:** 3/5  
Argues that trustworthy agentic workflows require agent-first data infrastructure and proposes Bauplan, a lakehouse reimplemented with MVCC-like isolation for agents; provides a reference self-healing pipeline implementation with concrete correctness guarantees.
