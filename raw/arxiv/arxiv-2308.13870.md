---
schema_version: 1
id: arxiv-2308.13870
type: arxiv
title: Brain-like representational straightening of natural movies in robust feedforward
  neural networks
url: https://arxiv.org/abs/2308.13870
authors:
- Tahereh Toosi
- Elias B. Issa
ingested_at: '2026-06-01T19:55:24Z'
content_hash: sha256:5921ffcdbb58bc7d13504bdb7432275bae72b22a746a009893b774f17c4a6baa
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2308.13870'
  categories:
  - q-bio.NC
  - cs.CV
  - cs.LG
  doi: ''
  primary_category: q-bio.NC
  journal_ref: International Conference on Learning Representations (ICLR), 2023
  comment: 21 pages, 15 figures, published in ICLR 2023
  abstract_only: true
published_at: '2023-08-26'
filter:
  score: 0.75
---
Representational straightening refers to a decrease in curvature of visual feature representations of a sequence of frames taken from natural movies. Prior work established straightening in neural representations of the primate primary visual cortex (V1) and perceptual straightening in human behavior as a hallmark of biological vision in contrast to artificial feedforward neural networks which did not demonstrate this phenomenon as they were not explicitly optimized to produce temporally predictable movie representations. Here, we show robustness to noise in the input image can produce representational straightening in feedforward neural networks. Both adversarial training (AT) and base classifiers for Random Smoothing (RS) induced remarkably straightened feature codes. Demonstrating their utility within the domain of natural movies, these codes could be inverted to generate intervening movie frames by linear interpolation in the feature space even though they were not trained on these trajectories. Demonstrating their biological utility, we found that AT and RS training improved predictions of neural data in primate V1 over baseline models providing a parsimonious, bio-plausible mechanism -- noise in the sensory input stages -- for generating representations in early visual cortex. Finally, we compared the geometric properties of frame representations in these networks to better understand how they produced representations that mimicked the straightening phenomenon from biology. Overall, this work elucidating emergent properties of robust neural networks demonstrates that it is not necessary to utilize predictive objectives or train directly on natural movie statistics to achieve models supporting straightened movie representations similar to human perception that also predict V1 neural responses.
