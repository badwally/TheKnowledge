---
schema_version: 1
type: concept
slug: hierarchical-bayesian-modelling
canonical_name: Hierarchical Bayesian modelling
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:45Z'
draft_unresolved_claims: 2
created_at: '2026-05-20T19:49:54Z'
last_updated: '2026-05-20T19:49:54Z'
---

# Hierarchical Bayesian modelling

## Summary

Hierarchical Bayesian models are multi-stage probability models in which priors on lower-level (cluster-specific) parameters depend on hyperparameters that are themselves assigned priors and learned from the data. They underlie multilevel models, structural equation models, and item response theory.

## Key claims

- Hierarchical Bayesian models are defined in stages; a canonical three-stage multilevel example has, at the observation stage, the response y_ij for unit i within cluster j as normal with mean α + ζ_j and variance σ², a normal prior on the cluster-specific parameter ζ_j with mean 0 and variance ψ, and a hyperprior on ψ [[sources/yt-WJ1BvfOm-94]].
- What makes a model hierarchical Bayesian is that the prior for the cluster-level latent parameter (e.g. ζ) depends on a hyperparameter (e.g. ψ) about which the analyst learns from the data [[sources/yt-WJ1BvfOm-94]].
- Canonical examples of hierarchical Bayesian models include mixed/multilevel models, structural equation models (SEM), and item response theory (IRT) models [[sources/yt-WJ1BvfOm-94]].
- In IRT, the cluster corresponds to a person and the units to items, so y becomes a multivariate vector of responses to different items for each person [[sources/yt-WJ1BvfOm-94]].
- In a Bayesian setting it is ambiguous whether cluster-level latent variables ζ_j should be regarded as parameters or as latent variables; the speaker notes that they are typically treated as parameters [[sources/yt-WJ1BvfOm-94]].
- From a non-Bayesian perspective, the latent variables ζ_j would be treated as random variables rather than parameters because they are unobserved [[sources/yt-WJ1BvfOm-94]].
- Two versions of the likelihood exist for hierarchical Bayesian models: the conditional likelihood (conditional on the latent variables, factorising as a product of cluster contributions and within each cluster as a product of unit contributions because units within a cluster are conditionally independent given the latent variable) and the marginal likelihood (integrating out the latent variables, used in maximum likelihood estimation as in R's lme4) [[sources/yt-WJ1BvfOm-94]].
- The conditional likelihood is the natural definition in software such as Stan, where the model block expresses the likelihood of y conditional on the latent variables [[sources/yt-WJ1BvfOm-94]].

## Sources

- [[sources/yt-WJ1BvfOm-94]]

## Related

- [[concepts/marginal-vs-conditional-likelihood]]
- [[concepts/multilevel-models]]
- [[concepts/item-response-theory]]
- [[concepts/predictive-information-criteria]]
- [[concepts/posterior-predictive-distribution]]
- [[concepts/mixed-predictive-distribution]]
