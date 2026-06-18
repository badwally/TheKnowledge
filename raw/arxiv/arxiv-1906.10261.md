---
schema_version: 1
id: arxiv-1906.10261
type: arxiv
title: Datalog Materialisation in Distributed RDF Stores with Dynamic Data Exchange
url: https://arxiv.org/abs/1906.10261
authors:
- Temitope Ajileye
- Boris Motik
- Ian Horrocks
ingested_at: '2026-06-17T23:24:54Z'
content_hash: sha256:15a07d1a3e5bf46e535a9b0b7a19aeb5690df393ef021f0cdaf4f9d88c0f8576
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '1906.10261'
  categories:
  - cs.DB
  - cs.DC
  - cs.LO
  doi: ''
  primary_category: cs.DB
  journal_ref: ''
  comment: 16 pages, ISWC conference
  abstract_only: true
published_at: '2019-06-24'
filter:
  score: 0.88
---
Several centralised RDF systems support datalog reasoning by precomputing and storing all logically implied triples using the wellknown seminaive algorithm. Large RDF datasets often exceed the capacity of centralised RDF systems, and a common solution is to distribute the datasets in a cluster of shared-nothing servers. While numerous distributed query answering techniques are known, distributed seminaive evaluation of arbitrary datalog rules is less understood. In fact, most distributed RDF stores either support no reasoning or can handle only limited datalog fragments. In this paper we extend the dynamic data exchange approach for distributed query answering by Potter et al. [12] to a reasoning algorithm that can handle arbitrary rules while preserving important properties such as nonrepetition of inferences. We also show empirically that our algorithm scales well to very large RDF datasets
