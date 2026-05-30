---
schema_version: 1
id: arxiv-2403.06204
type: arxiv
title: Identifying and interpreting non-aligned human conceptual representations using
  language modeling
url: https://arxiv.org/abs/2403.06204
authors:
- Wanqian Bao
- Uri Hasson
ingested_at: '2026-05-30T20:39:57Z'
content_hash: sha256:5d540d6a9acabf33baa17fb0ecb5b2cd7b0a90392d0c50796db396edda5cbd44
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2403.06204'
  categories:
  - cs.CL
  doi: ''
  primary_category: cs.CL
  journal_ref: ''
  comment: To appear at the ICLR 2024 Workshop on Representational Alignment (Re-Align)
  abstract_only: true
published_at: '2024-03-10'
filter:
  score: 0.75
---
The question of whether people's experience in the world shapes conceptual representation and lexical semantics is longstanding. Word-association, feature-listing and similarity rating tasks aim to address this question but require a subjective interpretation of the latent dimensions identified. In this study, we introduce a supervised representational-alignment method that (i) determines whether two groups of individuals share the same basis of a certain category, and (ii) explains in what respects they differ. In applying this method, we show that congenital blindness induces conceptual reorganization in both a-modal and sensory-related verbal domains, and we identify the associated semantic shifts. We first apply supervised feature-pruning to a language model (GloVe) to optimize prediction accuracy of human similarity judgments from word embeddings. Pruning identifies one subset of retained GloVe features that optimizes prediction of judgments made by sighted individuals and another subset that optimizes judgments made by blind. A linear probing analysis then interprets the latent semantics of these feature-subsets by learning a mapping from the retained GloVe features to 65 interpretable semantic dimensions. We applied this approach to seven semantic domains, including verbs related to motion, sight, touch, and amodal verbs related to knowledge acquisition. We find that blind individuals more strongly associate social and cognitive meanings to verbs related to motion or those communicating non-speech vocal utterances (e.g., whimper, moan). Conversely, for amodal verbs, they demonstrate much sparser information. Finally, for some verbs, representations of blind and sighted are highly similar. The study presents a formal approach for studying interindividual differences in word meaning, and the first demonstration of how blindness impacts conceptual representation of everyday verbs.
