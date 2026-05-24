---
type: concept
slug: deviance-information-criterion
canonical_name: Deviance Information Criterion (DIC)
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:45Z'
draft_unresolved_claims: 1
---

# Deviance Information Criterion (DIC)

## Summary

The Deviance Information Criterion (DIC) is a Bayesian model-selection criterion that estimates expected out-of-sample prediction error by combining a plug-in deviance computed at the posterior mean of the parameters with a penalty for the effective number of parameters.

## Key claims

- DIC plugs the posterior mean of the parameter vector θ into the deviance for new data, yielding the plug-in deviance: minus twice the log-likelihood at the posterior means [[sources/yt-WJ1BvfOm-94]].
- Because the in-sample plug-in deviance is overly optimistic about prediction error (the data are used both to estimate θ and to evaluate fit), DIC adds a penalty term equal to the effective number of parameters pD [[sources/yt-WJ1BvfOm-94]].
- pD is defined as the posterior expectation of the deviance minus the deviance evaluated at the posterior expectation of the parameters [[sources/yt-WJ1BvfOm-94]].
- In practice these posterior expectations are evaluated as sample averages across MCMC draws [[sources/yt-WJ1BvfOm-94]].
- For hierarchical Bayesian models there are two versions of DIC corresponding to the two available likelihoods: a conditional DIC, in which the conditional likelihood (given latent variables) is plugged in, and a marginal DIC, in which the marginal likelihood (integrating out the latent variables) is plugged in [[sources/yt-WJ1BvfOm-94]].
- Conditional DIC is what most Bayesian software produces by default; marginal DIC requires additional computation because the marginal likelihood is more complex and is not typically available in standard Bayesian software [[sources/yt-WJ1BvfOm-94]].
- A marginal-likelihood implementation suitable for structural equation models has been developed in the R package blavaan by Edgar Merkle [[sources/yt-WJ1BvfOm-94]].

## Sources

- [[sources/yt-WJ1BvfOm-94]]

## Related

- [[concepts/predictive-information-criteria]]
- [[concepts/widely-applicable-information-criterion]]
- [[concepts/marginal-vs-conditional-likelihood]]
- [[concepts/hierarchical-bayesian-modelling]]
- [[entities/edgar-merkle]]
