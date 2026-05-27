---
schema_version: 1
type: concept
slug: kalman-filtering-deterioration
canonical_name: Kalman Filtering for Deterioration State Estimation
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T19:53:55Z'
draft_unresolved_claims: 1
created_at: '2026-05-20T19:53:56Z'
last_updated: '2026-05-20T19:53:56Z'
---

# Kalman Filtering for Deterioration State Estimation

## Summary

Kalman filtering is the inference procedure used to recursively combine a kinematic deterioration transition model with bounded visual-inspection observations under inspector-specific Gaussian noise, alternating predict steps from the transition model with update steps from the observation model.

## Key claims

- Posterior updating of the deterioration state estimate is performed primarily through the Kalman-filtering approach [[sources/yt-vx6ATEoEuUE]].
- Starting from a prior estimate at time `t=0`, the transition model is used to obtain the predicted estimate at `t=1` [[sources/yt-vx6ATEoEuUE]].
- When an inspection arrives, the observation model is used to update the prior into a posterior deterioration-state estimate [[sources/yt-vx6ATEoEuUE]].
- The recursive predict-update cycle is iterated for each subsequent time step, producing a sequential posterior estimate over the element's lifetime [[sources/yt-vx6ATEoEuUE]].
- The element-level Kalman-filter scheme is supplemented by additional modifications, including bounded-unbounded transformation of observations and optional kernel-regression extensions [[sources/yt-vx6ATEoEuUE]].

## Sources

- [[sources/yt-vx6ATEoEuUE]]

## Related

- [[concepts/state-space-deterioration-model]]
- [[concepts/inspector-uncertainty]]
- [[concepts/bounded-unbounded-inspection-transformation]]
