---
type: concept
slug: iterated-batch-importance-sampling
canonical_name: Iterated Batch Importance Sampling (IBIS)
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T18:57:56Z'
draft_unresolved_claims: 1
---

# Iterated Batch Importance Sampling (IBIS)

## Summary

Iterated Batch Importance Sampling (IBIS) is an on-line Bayesian filter that combines sequential importance sampling for time-invariant parameters with Markov chain Monte Carlo (MCMC) move steps to rejuvenate the particle population when sample degeneracy occurs.

## Key claims

- IBIS is used as an on-line Bayesian filter for estimating time-invariant parameters of stochastic deterioration models from monitoring data [[sources/arxiv-2205.03478]].
- The IBIS filter performs MCMC move steps as part of its on-line updating procedure to maintain a representative parameter sample [[sources/arxiv-2205.03478]].
- Within the resampling process, IBIS can use a Gaussian mixture model to approximate the posterior distribution over parameters [[sources/arxiv-2205.03478]].
- IBIS sits between pure particle filtering and off-line MCMC-based sequential Monte Carlo: it processes data sequentially like a particle filter, but is more computationally demanding than a tailored on-line particle filter because of the embedded MCMC moves [[sources/arxiv-2205.03478]].

## Sources

- [[sources/arxiv-2205.03478]]

## Related

- [[concepts/bayesian-filtering-deterioration]]
- [[concepts/data-informed-predictive-maintenance]]
- [[entities/offline-online-bayesian-filtering-paper]]
