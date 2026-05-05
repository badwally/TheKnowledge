---
id: arxiv-2601.11816
type: arxiv
title: 'POLARIS: Typed Planning and Governed Execution for Agentic AI in Back-Office
  Automation'
url: http://arxiv.org/abs/2601.11816v1
authors:
- Zahra Moslemi
- Keerthi Koneru
- Yen-Ting Lee
- Sheethal Kumar
- Ramesh Radhakrishnan
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:3b44f9b4425213471d7e7ccc7caae98f47fb47064114d32dd474afcd4be286cb
domains:
- edge-ai-agentic
nlm_corpus_ids:
- e7f21255-0787-4091-ab69-5f79669e1501
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2601.11816.md
  legacy_slug: arxiv_2601.11816
published_at: '2026-01-16'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# POLARIS: Typed Planning and Governed Execution for Agentic AI in Back-Office Automation

**Authors:** Zahra Moslemi, Keerthi Koneru, Yen-Ting Lee, Sheethal Kumar, Ramesh Radhakrishnan  
**Published:** 2026-01-16T22:38:21Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2601.11816v1.pdf

## Abstract

Enterprise back office workflows require agentic systems that are auditable, policy-aligned, and operationally predictable, capabilities that generic multi-agent setups often fail to deliver. We present POLARIS (Policy-Aware LLM Agentic Reasoning for Integrated Systems), a governed orchestration framework that treats automation as typed plan synthesis and validated execution over LLM agents. A planner proposes structurally diverse, type checked directed acyclic graphs (DAGs), a rubric guided reasoning module selects a single compliant plan, and execution is guarded by validator gated checks, a bounded repair loop, and compiled policy guardrails that block or route side effects before they occur. Applied to document centric finance tasks, POLARIS produces decision grade artifacts and full execution traces while reducing human intervention. Empirically, POLARIS achieves a micro F1 of 0.81 on the SROIE dataset and, on a controlled synthetic suite, achieves 0.95 to 1.00 precision for an...

## Relevance

**Score:** 3/5  
POLARIS provides governed agentic orchestration with typed DAG plan synthesis, validator-gated execution, and compiled policy guardrails for enterprise workflows; substantive agentic orchestration architecture with empirical results, though no explicit edge deployment.
