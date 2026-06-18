---
schema_version: 1
id: arxiv-2501.14300
type: arxiv
title: 'Fast Think-on-Graph: Wider, Deeper and Faster Reasoning of Large Language
  Model on Knowledge Graph'
url: https://arxiv.org/abs/2501.14300
authors:
- Xujian Liang
- Zhaoquan Gu
ingested_at: '2026-06-17T20:58:06Z'
content_hash: sha256:257d48f4281f733763a7e8b5cf6c5688756ca743597902572d0410ce59b3ecef
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2501.14300'
  categories:
  - cs.AI
  - cs.CL
  - cs.LG
  - cs.SI
  doi: ''
  primary_category: cs.AI
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2025-01-24'
filter:
  score: 0.7
---
Graph Retrieval Augmented Generation (GRAG) is a novel paradigm that takes the naive RAG system a step further by integrating graph information, such as knowledge graph (KGs), into large-scale language models (LLMs) to mitigate hallucination. However, existing GRAG still encounter limitations: 1) simple paradigms usually fail with the complex problems due to the narrow and shallow correlations capture from KGs 2) methods of strong coupling with KGs tend to be high computation cost and time consuming if the graph is dense. In this paper, we propose the Fast Think-on-Graph (FastToG), an innovative paradigm for enabling LLMs to think ``community by community" within KGs. To do this, FastToG employs community detection for deeper correlation capture and two stages community pruning - coarse and fine pruning for faster retrieval. Furthermore, we also develop two Community-to-Text methods to convert the graph structure of communities into textual form for better understanding by LLMs. Experimental results demonstrate the effectiveness of FastToG, showcasing higher accuracy, faster reasoning, and better explainability compared to the previous works.
