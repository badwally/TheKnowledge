---
schema_version: 1
id: arxiv-2605.26874
type: arxiv
title: Knowledge Graphs as the Missing Data Layer for LLM-Based Industrial Asset Operations
url: https://arxiv.org/abs/2605.26874
authors:
- Madhulatha Mandarapu
- Sandeep Kunkunuru
ingested_at: '2026-06-17T20:56:12Z'
content_hash: sha256:3796c1f668a448c59fa0efa1701ac948a389233e34e0bf678c71c211fafe20ef
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2605.26874'
  categories:
  - cs.DB
  - cs.AI
  - cs.LG
  doi: ''
  primary_category: cs.DB
  journal_ref: ''
  comment: 'v2: reframed around the knowledge graph as a grounding substrate with
    a 3-tier router (text-to-Cypher; native graph/optimization primitives; generation-augmented
    knowledge, GAK). Adds a benchmark-grounded GAK evaluation on 88 real non-deterministic
    AssetOpsBench scenarios with provenance-tagged enrichment. 18 pages. Code: github.com/samyama-ai/assetops-kg'
  abstract_only: true
published_at: '2026-05-26'
filter:
  score: 0.85
---
LLM-based agents for industrial asset operations show limited accuracy when reasoning over flat document stores. AssetOpsBench (KDD 2026) establishes that GPT-4 agents achieve 65% on 139 industrial maintenance scenarios, and compares LLM orchestration paradigms (Agent-As-Tool vs. Plan-Execute) on a fixed data layer. We ask the orthogonal question: how much does the data model behind the tools matter?
  We treat a typed knowledge graph as a grounding substrate and route each question by how it is best answered: (i) LLM-generated Cypher for structured retrieval, which lifts the same GPT-4 model from 65% to 82-83%; (ii) native graph and optimization primitives, with no LLM, reaching 99% on graph-answerable scenarios; and (iii) generation-augmented knowledge (GAK) for answers absent from the data -- the engine's agent materializes the missing facts as provenance-tagged graph nodes, then answers. A recurring theme is inverted LLM usage: we constrain the LLM to query generation or one-shot enrichment from a typed schema and let the graph execute deterministically.
  On the 88 real AssetOpsBench failure-mode scenarios the benchmark itself flags non-deterministic -- ten equipment types absent from the graph -- GAK lifts answerability from zero to 100% of equipment types and answers 81.8% of scenarios, every materialized fact tagged source:LLM-derived for auditability. We also contribute 40 graph-native scenarios. For structured operational domains the data layer -- not the LLM orchestration -- is the primary lever, and a typed knowledge graph serves as a grounding substrate between raw industrial data and LLM reasoning.
