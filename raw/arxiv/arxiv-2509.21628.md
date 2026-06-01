---
schema_version: 1
id: arxiv-2509.21628
type: arxiv
title: Comparing and Integrating Different Notions of Representational Correspondence
  in Neural Systems
url: https://arxiv.org/abs/2509.21628
authors:
- Jialin Wu
- Shreya Saha
- Yiqing Bo
- Meenakshi Khosla
ingested_at: '2026-06-01T19:55:27Z'
content_hash: sha256:f145d54721c1509b081560e09bb3eb0de71ba30f75dc7736acf397ead9edb81d
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2509.21628'
  categories:
  - cs.CV
  - cs.AI
  doi: ''
  primary_category: cs.CV
  journal_ref: ''
  comment: Update title and reframe the contents
  abstract_only: true
published_at: '2025-09-25'
filter:
  score: 0.7
---
The extent to which different biological and artificial neural systems rely on equivalent internal representations to support similar tasks remains a central question in neuroscience and machine learning. Prior work typically compares systems using a single representational similarity metric, even though different metrics emphasize distinct facets of representational correspondence. Here we evaluate a suite of representational similarity measures by asking how well each metric recovers known structure across two domains: for artificial models, whether procedurally dissimilar models (differing in architecture or training paradigm) are assigned lower similarity than procedurally matched models; and for neural data, whether responses from distinct cortical regions are separated while responses from the same region align across subjects. Across both vision models and neural recordings, metrics that preserve representational geometry or tuning structure more reliably separate this structure than more flexible mappings such as linear predictivity. To integrate these complementary facets, we adapt Similarity Network Fusion, originally developed for multi-omics integration, to combine similarity graphs across metrics. The resulting fused similarity yields sharper separation of procedurally defined model families and, when applied to neural data, recovers a clearer hierarchical organization of the ventral visual stream that aligns more closely with established anatomical and functional hierarchies than single metrics. Overall, this approach reveals which dimensions of representational correspondence recover meaningful structure in models and brains, and how complementary notions of similarity can be integrated.
