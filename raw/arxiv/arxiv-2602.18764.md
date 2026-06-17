---
schema_version: 1
id: arxiv-2602.18764
type: arxiv
title: The Convergence of Schema-Guided Dialogue Systems and the Model Context Protocol
url: https://arxiv.org/abs/2602.18764
authors:
- Andreas Schlapbach
ingested_at: '2026-06-17T18:52:24Z'
content_hash: sha256:afda803bed3596e1ac3d22e5aa298291158dc8691fdaf69440d137603fc5646d
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2602.18764'
  categories:
  - cs.AI
  - cs.CL
  doi: ''
  primary_category: cs.AI
  journal_ref: ''
  comment: '18 sections, 4 figures, 7 tables, 40 references. Original research presenting:
    (1) formal framework mapping Schema-Guided Dialogue principles to Model Context
    Protocol concepts, (2) five foundational design principles for LLM-native schema
    authoring, (3) architectural patterns for secure, scalable agent orchestration.
    Research supported by SBB (Swiss Federal Railways)'
  abstract_only: true
published_at: '2026-02-21'
filter:
  score: 0.7
---
This paper establishes a fundamental convergence: Schema-Guided Dialogue (SGD) and the Model Context Protocol (MCP) represent two manifestations of a unified paradigm for deterministic, auditable LLM-agent interaction. SGD, designed for dialogue-based API discovery (2019), and MCP, now the de facto standard for LLM-tool integration, share the same core insight -- that schemas can encode not just tool signatures but operational constraints and reasoning guidance. By analyzing this convergence, we extract five foundational principles for schema design: (1) Semantic Completeness over Syntactic Precision, (2) Explicit Action Boundaries, (3) Failure Mode Documentation, (4) Progressive Disclosure Compatibility, and (5) Inter-Tool Relationship Declaration. These principles reveal three novel insights: first, SGD's original design was fundamentally sound and should be inherited by MCP; second, both frameworks leave failure modes and inter-tool relationships unexploited -- gaps we identify and resolve; third, progressive disclosure emerges as a critical production-scaling insight under real-world token constraints. We provide concrete design patterns for each principle. These principles position schema-driven governance as a scalable mechanism for AI system oversight without requiring proprietary system inspection -- central to Software 3.0.
