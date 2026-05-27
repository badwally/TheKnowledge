---
schema_version: 1
type: entity
slug: offline-online-bayesian-filtering-paper
canonical_name: On off-line and on-line Bayesian filtering for uncertainty quantification
  of structural deterioration
entity_kind: paper
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T18:57:56Z'
draft_unresolved_claims: 1
created_at: '2026-05-20T19:32:52Z'
last_updated: '2026-05-20T19:32:52Z'
---

# On off-line and on-line Bayesian filtering for uncertainty quantification of structural deterioration

## Summary

A 2022 arXiv preprint (subsequently published in *Data-Centric Engineering*, 2023) by Antonios Kamariotis, Luca Sardi, Iason Papaioannou, Eleni Chatzi, and Daniel Straub that reviews, adapts, and comparatively assesses selected off-line and on-line Bayesian filters for estimating time-invariant parameters of stochastic deterioration models from monitoring data, with a focus on quantifying the full posterior parameter uncertainty.

## Key facts

- The paper is authored by Antonios Kamariotis, Luca Sardi, Iason Papaioannou, Eleni Chatzi, and Daniel Straub and was posted as arXiv 2205.03478 on 6 May 2022 [[sources/arxiv-2205.03478]].
- The paper was published in *Data-Centric Engineering*, volume 4, 2023, article e17 (DOI 10.1017/dce.2023.13) [[sources/arxiv-2205.03478]].
- The arXiv preprint is classified under stat.CO as primary category [[sources/arxiv-2205.03478]].
- The motivating premise is that data-informed predictive maintenance planning largely relies on stochastic deterioration models, and that monitoring information can be used to sequentially update knowledge of time-invariant deterioration model parameters either within an off-line (batch) or an on-line (recursive) Bayesian framework [[sources/arxiv-2205.03478]].
- The paper reviews, adapts, and investigates three selected Bayesian filters: an on-line particle filter, an on-line iterated batch importance sampling (IBIS) filter that performs MCMC move steps, and an off-line MCMC-based sequential Monte Carlo filter [[sources/arxiv-2205.03478]].
- All three filters use a Gaussian mixture model to approximate the posterior distribution within the resampling process [[sources/arxiv-2205.03478]].
- Two numerical examples are used for the comparative assessment: a low-dimensional, nonlinear, non-Gaussian probabilistic fatigue crack growth model updated with sequential crack monitoring measurements, and a high-dimensional, linear, Gaussian random-field corrosion deterioration model across a beam updated with sequential sensor measurements [[sources/arxiv-2205.03478]].
- The numerical investigations are designed to provide insight into the performance of off-line and on-line filters in terms of accuracy of posterior estimates and computational cost across problems of varying nature, dimensionality, and sensor information amount [[sources/arxiv-2205.03478]].
- The authors report that a tailored implementation of the on-line particle filter proves competitive with the more computationally demanding MCMC-based filters [[sources/arxiv-2205.03478]].
- The paper provides suggestions on the choice of the appropriate method as a function of problem characteristics [[sources/arxiv-2205.03478]].

## Sources

- [[sources/arxiv-2205.03478]]

## Related

- [[entities/antonios-kamariotis]]
- [[entities/luca-sardi]]
- [[entities/iason-papaioannou]]
- [[entities/eleni-chatzi]]
- [[entities/daniel-straub]]
- [[concepts/bayesian-filtering-deterioration]]
- [[concepts/iterated-batch-importance-sampling]]
- [[concepts/data-informed-predictive-maintenance]]
