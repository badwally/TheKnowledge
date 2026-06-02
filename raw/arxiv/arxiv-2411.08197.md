---
schema_version: 1
id: arxiv-2411.08197
type: arxiv
title: What Representational Similarity Measures Imply about Decodable Information
url: https://arxiv.org/abs/2411.08197
authors:
- Sarah E. Harvey
- David Lipshutz
- Alex H. Williams
ingested_at: '2026-06-01T23:58:24Z'
content_hash: sha256:a39240480898824b08d1cc66106ae603a2accddd31c10b495bca04a583bf6adb
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2411.08197'
  categories:
  - stat.ML
  - cs.AI
  - cs.LG
  doi: ''
  primary_category: stat.ML
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2024-11-12'
filter:
  score: 0.7
---
Neural responses encode information that is useful for a variety of downstream tasks. A common approach to understand these systems is to build regression models or ``decoders'' that reconstruct features of the stimulus from neural responses. Popular neural network similarity measures like centered kernel alignment (CKA), canonical correlation analysis (CCA), and Procrustes shape distance, do not explicitly leverage this perspective and instead highlight geometric invariances to orthogonal or affine transformations when comparing representations. Here, we show that many of these measures can, in fact, be equivalently motivated from a decoding perspective. Specifically, measures like CKA and CCA quantify the average alignment between optimal linear readouts across a distribution of decoding tasks. We also show that the Procrustes shape distance upper bounds the distance between optimal linear readouts and that the converse holds for representations with low participation ratio. Overall, our work demonstrates a tight link between the geometry of neural representations and the ability to linearly decode information. This perspective suggests new ways of measuring similarity between neural systems and also provides novel, unifying interpretations of existing measures.
