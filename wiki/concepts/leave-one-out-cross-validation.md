---
schema_version: 1
type: concept
slug: leave-one-out-cross-validation
canonical_name: Leave-one-out cross-validation (LOO)
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:45Z'
draft_unresolved_claims: 1
created_at: '2026-05-20T19:49:54Z'
last_updated: '2026-05-20T19:49:54Z'
---

# Leave-one-out cross-validation (LOO)

## Summary

Leave-one-out cross-validation (LOO) estimates a Bayesian model's expected out-of-sample log predictive density by training the posterior on all but one observation and evaluating the predictive density on the held-out unit, repeated across all observations.

## Key claims

- LOO bases the posterior distribution on the data with one unit removed and evaluates the predictive density for that held-out unit, so the data conditioned on for parameter learning differs from the data used to evaluate predictive density [[sources/yt-WJ1BvfOm-94]].
- Because the conditioning set excludes the held-out unit, LOO does not require penalisation for reusing the data twice as DIC and WAIC do [[sources/yt-WJ1BvfOm-94]].
- Direct implementation of LOO is computationally prohibitive in general because it requires running MCMC for each leave-one-out training data set; it is therefore only really feasible for very small data sets such as the eight-schools example [[sources/yt-WJ1BvfOm-94]].
- In practice, LOO is approximated using importance sampling, which allows running MCMC only once: the full-data posterior is used as a proposal and corrected via an importance ratio between the desired leave-one-out posterior and the proposal [[sources/yt-WJ1BvfOm-94]].
- Naive importance sampling can be very noisy, motivating Pareto-smoothed importance sampling (PSIS) as a standard variance-reduction technique [[sources/yt-WJ1BvfOm-94]].
- LOO and WAIC are asymptotically equivalent because both target minus twice the expected log pointwise predictive density [[sources/yt-WJ1BvfOm-94]].

## Sources

- [[sources/yt-WJ1BvfOm-94]]

## Related

- [[concepts/predictive-information-criteria]]
- [[concepts/widely-applicable-information-criterion]]
- [[concepts/pareto-smoothed-importance-sampling]]
