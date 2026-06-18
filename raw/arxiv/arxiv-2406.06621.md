---
schema_version: 1
id: arxiv-2406.06621
type: arxiv
title: 'LinkQ: An LLM-Assisted Visual Interface for Knowledge Graph Question-Answering'
url: https://arxiv.org/abs/2406.06621
authors:
- Harry Li
- Gabriel Appleby
- Ashley Suh
ingested_at: '2026-06-17T20:56:24Z'
content_hash: sha256:b8991f77e9f635e44dd59e5aefccfc1ea2962ebdcef15cb188b3875912b27162
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2406.06621'
  categories:
  - cs.CL
  - cs.AI
  - cs.LG
  doi: 10.1109/VIS55277.2024.00031
  primary_category: cs.CL
  journal_ref: 'H. Li, G. Appleby and A. Suh, "LinkQ: An LLM-Assisted Visual Interface
    for Knowledge Graph Question-Answering," 2024 IEEE Visualization and Visual Analytics
    (VIS)'
  comment: 'Open-source code: https://github.com/mit-ll/linkq'
  abstract_only: true
published_at: '2024-06-07'
filter:
  score: 0.75
---
We present LinkQ, a system that leverages a large language model (LLM) to facilitate knowledge graph (KG) query construction through natural language question-answering. Traditional approaches often require detailed knowledge of a graph querying language, limiting the ability for users -- even experts -- to acquire valuable insights from KGs. LinkQ simplifies this process by implementing a multistep protocol in which the LLM interprets a user's question, then systematically converts it into a well-formed query. LinkQ helps users iteratively refine any open-ended questions into precise ones, supporting both targeted and exploratory analysis. Further, LinkQ guards against the LLM hallucinating outputs by ensuring users' questions are only ever answered from ground truth KG data. We demonstrate the efficacy of LinkQ through a qualitative study with five KG practitioners. Our results indicate that practitioners find LinkQ effective for KG question-answering, and desire future LLM-assisted exploratory data analysis systems.
