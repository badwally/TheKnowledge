---
schema_version: 1
id: arxiv-2602.14486
type: arxiv
title: 'Revisiting the Platonic Representation Hypothesis: An Aristotelian View'
url: https://arxiv.org/abs/2602.14486
authors:
- Fabian Gröger
- Shuo Wen
- Maria Brbić
ingested_at: '2026-05-30T20:00:52Z'
content_hash: sha256:12ea09beef5b3b618ea074acaa8284fb52a16dbe70d6b61cabbf916f3644e099
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2602.14486'
  categories:
  - cs.LG
  - cs.AI
  - cs.CV
  - cs.NE
  doi: ''
  primary_category: cs.LG
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2026-02-16'
filter:
  score: 0.85
---
The Platonic Representation Hypothesis suggests that representations from neural networks are converging to a common statistical model of reality. We show that the existing metrics used to measure representational similarity are confounded by network scale: increasing model depth or width can systematically inflate representational similarity scores. To correct these effects, we introduce a permutation-based null-calibration framework that transforms any representational similarity metric into a calibrated score with statistical guarantees. We revisit the Platonic Representation Hypothesis with our calibration framework, which reveals a nuanced picture: the apparent convergence reported by global spectral measures largely disappears after calibration, while local neighborhood similarity, but not local distances, retains significant agreement across different modalities. Based on these findings, we propose the Aristotelian Representation Hypothesis: representations in neural networks are converging to shared local neighborhood relationships.
