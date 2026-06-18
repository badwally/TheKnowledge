---
schema_version: 1
id: arxiv-2509.08381
type: arxiv
title: Low-Resource Fine-Tuning for Multi-Task Structured Information Extraction with
  a Billion-Parameter Instruction-Tuned Model
url: https://arxiv.org/abs/2509.08381
authors:
- Yu Cheng Chih
- Yong Hao Hou
ingested_at: '2026-06-17T18:14:59Z'
content_hash: sha256:cf1d38f353ba8eb7b4df396ffa98d8c2037df5de5effdbf0466878404bf95204
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2509.08381'
  categories:
  - cs.CL
  - cs.AI
  doi: ''
  primary_category: cs.CL
  journal_ref: ''
  comment: 13 pages, 8 figures, includes experiments on JSON extraction, knowledge
    graph extraction, and NER
  abstract_only: true
published_at: '2025-09-10'
filter:
  score: 0.7
---
Deploying large language models (LLMs) for structured data extraction in domains such as financial compliance reporting, legal document analytics, and multilingual knowledge base construction is often impractical for smaller teams due to the high cost of running large architectures and the difficulty of preparing large, high-quality datasets. Most recent instruction-tuning studies focus on seven-billion-parameter or larger models, leaving limited evidence on whether much smaller models can work reliably under low-resource, multi-task conditions. This work presents ETLCH, a billion-parameter LLaMA-based model fine-tuned with low-rank adaptation on only a few hundred to one thousand samples per task for JSON extraction, knowledge graph extraction, and named entity recognition. Despite its small scale, ETLCH outperforms strong baselines across most evaluation metrics, with substantial gains observed even at the lowest data scale. These findings demonstrate that well-tuned small models can deliver stable and accurate structured outputs at a fraction of the computational cost, enabling cost-effective and reliable information extraction pipelines in resource-constrained environments.
