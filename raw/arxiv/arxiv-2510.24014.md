---
schema_version: 1
id: arxiv-2510.24014
type: arxiv
title: 'TEXT2DB: Integration-Aware Information Extraction with Large Language Model
  Agents'
url: https://arxiv.org/abs/2510.24014
authors:
- Yizhu Jiao
- Sha Li
- Sizhe Zhou
- Heng Ji
- Jiawei Han
ingested_at: '2026-06-17T18:16:51Z'
content_hash: sha256:f8771763072079c1e9de693c518fe14eefcc387cb623bb2d3377e9cd10684210
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2510.24014'
  categories:
  - cs.CL
  doi: ''
  primary_category: cs.CL
  journal_ref: ''
  comment: 'Source code: https://github.com/yzjiao/Text2DB'
  abstract_only: true
published_at: '2025-10-28'
filter:
  score: 0.77
---
The task of information extraction (IE) is to extract structured knowledge from text. However, it is often not straightforward to utilize IE output due to the mismatch between the IE ontology and the downstream application needs. We propose a new formulation of IE TEXT2DB that emphasizes the integration of IE output and the target database (or knowledge base). Given a user instruction, a document set, and a database, our task requires the model to update the database with values from the document set to satisfy the user instruction. This task requires understanding user instructions for what to extract and adapting to the given DB/KB schema for how to extract on the fly. To evaluate this new task, we introduce a new benchmark featuring common demands such as data infilling, row population, and column addition. In addition, we propose an LLM agent framework OPAL (Observe-PlanAnalyze LLM) which includes an Observer component that interacts with the database, the Planner component that generates a code-based plan with calls to IE models, and the Analyzer component that provides feedback regarding code quality before execution. Experiments show that OPAL can successfully adapt to diverse database schemas by generating different code plans and calling the required IE models. We also highlight difficult cases such as dealing with large databases with complex dependencies and extraction hallucination, which we believe deserve further investigation. Source code: https://github.com/yzjiao/Text2DB
