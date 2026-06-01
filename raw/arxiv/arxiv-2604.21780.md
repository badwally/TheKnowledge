---
schema_version: 1
id: arxiv-2604.21780
type: arxiv
title: 'Only Brains Align with Brains: Cross-Region Alignment Patterns Expose Limits
  of Normative Models'
url: https://arxiv.org/abs/2604.21780
authors:
- Larissa Höfling
- Matthias Tangemann
- Lotta Piefke
- Susanne Keller
- Katrin Franke
- Matthias Bethge
ingested_at: '2026-06-01T19:55:30Z'
content_hash: sha256:42146edb61c763f3ece51b6207d47dbd4b140756b9fd3fcc60b9b18595dd5eda
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2604.21780'
  categories:
  - q-bio.NC
  doi: ''
  primary_category: q-bio.NC
  journal_ref: The Fourteenth International Conference on Learning Representations,
    ICLR 2026, Rio de Janeiro, April 23-27, 2026
  comment: Code is available at https://github.com/bethgelab/alignment-pattern-analysis
  abstract_only: true
published_at: '2026-04-23'
filter:
  score: 0.85
---
Neuroscientists and computer vision researchers use model-brain alignment benchmarks to compare artificial and biological vision systems. These benchmarks rank models according to alignment measures such as the similarity of representational geometry or the predictability of neural responses from model activations. However, recent works have identified a number of problems with these rankings, among them their lack of discriminative power and robustness, raising the conceptual question of what it means for a model to be brain-aligned. Here we introduce alignment patterns -- characteristic functional relationship profiles of each brain region to all others -- and propose that models should reproduce these patterns to qualify as brain-aligned. First, we apply a standard benchmarking pipeline to a broad spectrum of vision models of the BOLD Moments video fMRI dataset across visual regions of interest (ROIs). We find diverse models appear equivalent in their brain alignment, reflecting the lack of discriminative power of conventional alignment benchmarking pipelines. In contrast, alignment pattern analysis (APA) is a second-order structural consistency test: a model aligned to a given ROI should reproduce that ROI's characteristic cross-region alignment profile. Applying APA, we find that, while these patterns are highly stable across brains of different subjects, even top-ranked models often fail to capture them. Finally, we argue for a clearer distinction between the criteria a model must meet to serve as a tool versus as a computational model for human visual cortex. Conventional alignment measures may be sufficient for identifying neurally predictive models, but claims about computational or algorithmic similarity may require a stronger basis of evidence, including the reproducibility of relational alignment patterns.
