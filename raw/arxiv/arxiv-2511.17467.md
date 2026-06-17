---
schema_version: 1
id: arxiv-2511.17467
type: arxiv
title: 'PersonaAgent with GraphRAG: Community-Aware Knowledge Graphs for Personalized
  LLM'
url: https://arxiv.org/abs/2511.17467
authors:
- Siqi Liang
- Yudi Zhang
- Yue Guo
ingested_at: '2026-06-17T18:16:48Z'
content_hash: sha256:e065c1896de8120f8be43a5a779053df0d1e0597c9b782b59e8f5837c495a346
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2511.17467'
  categories:
  - cs.LG
  - cs.AI
  doi: ''
  primary_category: cs.LG
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2025-11-21'
filter:
  score: 0.75
---
We propose a novel framework for persona-based language model system, motivated by the need for personalized AI agents that adapt to individual user preferences. In our approach, the agent embodies the user's "persona" (e.g. user profile or taste) and is powered by a large language model (LLM). To enable the agent to leverage rich contextual information, we introduce a Knowledge-Graph-enhanced Retrieval-Augmented Generation (Graph RAG) mechanism that constructs an LLM-derived graph index of relevant documents and summarizes communities of related information. Our framework generates personalized prompts by combining: (1) a summary of the user's historical behaviors and preferences extracted from the knowledge graph, and (2) relevant global interaction patterns identified through graph-based community detection. This dynamic prompt engineering approach allows the agent to maintain consistent persona-aligned behaviors while benefiting from collective knowledge. On the LaMP benchmark, our method improves news categorization F1 by 11.1%, movie tagging F1 by 56.1%, and reduces product rating MAE by 10.4% over prior methods. Our code is available at https://anonymous.4open.science/r/PersonaAgentwGraphRAG-DE6F
