---
type: concept
slug: bayesian-filtering-deterioration
canonical_name: Bayesian filtering for uncertainty quantification of structural deterioration
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T18:57:56Z'
draft_unresolved_claims: 2
---

# Bayesian filtering for uncertainty quantification of structural deterioration

## Summary

Bayesian filtering, applied to structural deterioration, is the use of monitoring data to sequentially update the posterior distribution of time-invariant parameters of a stochastic deterioration model. It comes in two principal flavours: off-line (batch) Bayesian inference, which reprocesses all data at every step (typically via MCMC), and on-line (recursive) filtering, which updates the posterior incrementally as each new observation arrives.

## Key claims

- Data-informed predictive maintenance planning largely relies on stochastic deterioration models whose time-invariant parameters must be estimated from monitoring data, motivating the use of Bayesian filtering [[sources/arxiv-2205.03478]].
- Monitoring information can be used to update sequentially the knowledge on time-invariant deterioration model parameters either within an off-line (batch) or an on-line (recursive) Bayesian framework [[sources/arxiv-2205.03478]].
- Three filters of interest for this problem are an on-line particle filter, an on-line iterated batch importance sampling (IBIS) filter that performs MCMC move steps, and an off-line MCMC-based sequential Monte Carlo filter [[sources/arxiv-2205.03478]].
- A Gaussian mixture model can be used to approximate the posterior distribution within the resampling process across all three filters, with a view to capturing multimodality and non-Gaussian features in the parameter posterior [[sources/arxiv-2205.03478]].
- The relative performance of off-line and on-line filters depends on problem characteristics including dimensionality, linearity/Gaussianity, and the amount of sensor information available [[sources/arxiv-2205.03478]].
- A tailored implementation of the on-line particle filter can be competitive with computationally demanding MCMC-based filters on representative deterioration problems [[sources/arxiv-2205.03478]].
- The choice between off-line and on-line filtering for deterioration model parameters should be guided by problem characteristics rather than a single dominant method [[sources/arxiv-2205.03478]].

## Sources

- [[sources/arxiv-2205.03478]]

## Related

- [[concepts/iterated-batch-importance-sampling]]
- [[concepts/data-informed-predictive-maintenance]]
- [[entities/offline-online-bayesian-filtering-paper]]
