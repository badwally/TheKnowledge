---
type: concept
slug: posterior-predictive-distribution
canonical_name: Posterior predictive distribution
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:45Z'
draft_unresolved_claims: 1
---

# Posterior predictive distribution

## Summary

The posterior predictive distribution gives the predictive density for new observations conditional on cluster-level latent variables learned from the existing data. In hierarchical Bayesian models it answers the question: 'how well does the model predict a new unit drawn from one of the clusters I already have data on?'

## Key claims

- The posterior predictive distribution for a hierarchical Bayesian model is obtained by taking the conditional predictive distribution given the latent variables ζ and integrating over the posterior of ω and ζ given y [[sources/yt-WJ1BvfOm-94]].
- The hyperparameter ψ can be marginalised out of this expression, leaving a predictive distribution that still depends on the cluster-level latent variables [[sources/yt-WJ1BvfOm-94]].
- Even after conditioning on ω and ψ, the cluster-level latent variables ζ are themselves learned from the observed responses in cluster j, so the posterior predictive distribution effectively answers the question of how predictive the model is for new units drawn from the existing clusters [[sources/yt-WJ1BvfOm-94]].
- For posterior predictive checking based on the posterior predictive distribution, one uses the posterior samples of ζ to generate new data y [[sources/yt-WJ1BvfOm-94]].

## Sources

- [[sources/yt-WJ1BvfOm-94]]

## Related

- [[concepts/hierarchical-bayesian-modelling]]
- [[concepts/mixed-predictive-distribution]]
- [[concepts/widely-applicable-information-criterion]]
