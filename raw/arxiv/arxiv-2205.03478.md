---
id: arxiv-2205.03478
type: arxiv
title: On off-line and on-line Bayesian filtering for uncertainty quantification of
  structural deterioration
url: https://arxiv.org/abs/2205.03478
authors:
- Antonios Kamariotis
- Luca Sardi
- Iason Papaioannou
- Eleni Chatzi
- Daniel Straub
ingested_at: '2026-05-20T18:57:56Z'
content_hash: sha256:d36b034d42f95cdfb87dcc5ce614ab8fbdb516e79af51933b00992eaacb4079b
domains: []
nlm_corpus_ids: []
wiki_pages:
- wiki/entities/offline-online-bayesian-filtering-paper.md
- wiki/entities/antonios-kamariotis.md
- wiki/entities/luca-sardi.md
- wiki/entities/iason-papaioannou.md
- wiki/entities/eleni-chatzi.md
- wiki/entities/daniel-straub.md
- wiki/concepts/bayesian-filtering-deterioration.md
- wiki/concepts/iterated-batch-importance-sampling.md
- wiki/concepts/data-informed-predictive-maintenance.md
meta:
  arxiv_id: '2205.03478'
  categories:
  - stat.CO
  doi: 10.1017/dce.2023.13
  primary_category: stat.CO
  journal_ref: Data-Centric Engineering, Volume 4, 2023, e17
  comment: ''
  abstract_only: true
published_at: '2022-05-06'
---
Data-informed predictive maintenance planning largely relies on stochastic deterioration models. Monitoring information can be utilized to update sequentially the knowledge on time-invariant deterioration model parameters either within an off-line (batch) or an on-line (recursive) Bayesian framework. With a focus on the quantification of the full parameter uncertainty, we review, adapt and investigate selected Bayesian filters for parameter estimation: an on-line particle filter, an on-line iterated batch importance sampling filter, which performs Markov chain Monte Carlo (MCMC) move steps, and an off-line MCMC-based sequential Monte Carlo filter. A Gaussian mixture model is used to approximate the posterior distribution within the resampling process in all three filters. Two numerical examples serve as the basis for a comparative assessment of off-line and on-line Bayesian estimation of time-invariant deterioration model parameters. The first case study considers a low-dimensional, nonlinear, non-Gaussian probabilistic fatigue crack growth model that is updated with sequential crack monitoring measurements. The second high-dimensional, linear, Gaussian case study employs a random field to model corrosion deterioration across a beam, which is updated with sequential measurements from sensors. The numerical investigations provide insights into the performance of off-line and on-line filters in terms of the accuracy of posterior estimates and the computational cost, when applied to problems of different nature, increasing dimensionality and varying sensor information amount. Importantly, they show that a tailored implementation of the on-line particle filter proves competitive with the computationally demanding MCMC-based filters. Suggestions on the choice of the appropriate method in function of problem characteristics are provided.
