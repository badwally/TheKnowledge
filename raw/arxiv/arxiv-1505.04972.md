---
schema_version: 1
id: arxiv-1505.04972
type: arxiv
title: Recursion in RDF Data Shape Languages
url: https://arxiv.org/abs/1505.04972
authors:
- Arthur Ryman
ingested_at: '2026-06-17T18:07:56Z'
content_hash: sha256:5213c09d363a3653331c3702e3ceb87b82f89513e0f6c417381dc3b5f64f6bb6
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '1505.04972'
  categories:
  - cs.DB
  - cs.AI
  doi: ''
  primary_category: cs.DB
  journal_ref: ''
  comment: 31 pages, 2 figures, invited expert contribution to the W3C RDF Data Shapes
    Working Group
  abstract_only: true
published_at: '2015-05-19'
filter:
  score: 0.9
---
An RDF data shape is a description of the expected contents of an RDF document (aka graph) or dataset. A major part of this description is the set of constraints that the document or dataset is required to satisfy. W3C recently (2014) chartered the RDF Data Shapes Working Group to define SHACL, a standard RDF data shape language. We refer to the ability to name and reference shape language elements as recursion. This article provides a precise definition of the meaning of recursion as used in Resource Shape 2.0. The definition of recursion presented in this article is largely independent of language-specific details. We speculate that it also applies to ShEx and to all three of the current proposals for SHACL. In particular, recursion is not permitted in the SHACL-SPARQL proposal, but we conjecture that recursion could be added by using the definition proposed here as a top-level control structure.
