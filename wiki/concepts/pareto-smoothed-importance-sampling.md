---
schema_version: 1
type: concept
slug: pareto-smoothed-importance-sampling
canonical_name: Pareto-smoothed importance sampling (PSIS)
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:45Z'
draft_unresolved_claims: 2
created_at: '2026-05-20T19:49:54Z'
last_updated: '2026-05-20T19:49:54Z'
---

# Pareto-smoothed importance sampling (PSIS)

## Summary

Pareto-smoothed importance sampling (PSIS) is a variance-reduction technique that stabilises importance-sampling estimators by smoothing extreme importance ratios via a generalised Pareto distribution fit to the tail. It is the standard way to approximate Bayesian leave-one-out cross-validation from a single MCMC run.

## Key claims

- Importance sampling allows leave-one-out cross-validation to be approximated from a single MCMC run by using the full-data posterior as a proposal and correcting via importance ratios — the desired leave-one-out posterior divided by the proposal posterior [[sources/yt-WJ1BvfOm-94]].
- Naive (non-smoothed) importance-ratio estimation of leave-one-out predictive densities can be very noisy, motivating the use of Pareto smoothing of the importance ratios [[sources/yt-WJ1BvfOm-94]].
- The Pareto-smoothed importance-sampling approach to leave-one-out cross-validation is presented in detail in Vehtari, Gelman, and Gabry 2017 [[sources/yt-WJ1BvfOm-94]].

## Sources

- [[sources/yt-WJ1BvfOm-94]]

## Related

- [[concepts/leave-one-out-cross-validation]]
- [[concepts/predictive-information-criteria]]
- [[concepts/widely-applicable-information-criterion]]
