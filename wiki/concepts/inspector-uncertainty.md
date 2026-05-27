---
schema_version: 1
type: concept
slug: inspector-uncertainty
canonical_name: Inspector-Specific Observation Uncertainty
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T19:53:55Z'
draft_unresolved_claims: 1
created_at: '2026-05-20T19:53:56Z'
last_updated: '2026-05-20T19:53:56Z'
---

# Inspector-Specific Observation Uncertainty

## Summary

Inspector-specific observation uncertainty is the modelling choice — within a state-space deterioration framework — of representing visual-inspection observation error with a zero-mean Gaussian whose variance is unique to each inspector, capturing differences in inspector calibration across a network.

## Key claims

- In the observation model `y_t = C x_t + v_t`, the observation error `v_t` is modelled with zero mean and a variance associated with each individual inspector [[sources/yt-vx6ATEoEuUE]].
- The observation is treated as dependent on the inspector who performed it, so different inspectors contribute different uncertainty levels to the posterior update [[sources/yt-vx6ATEoEuUE]].
- The variance for each inspector is itself estimated within the same state-space framework as part of the inference procedure [[sources/yt-vx6ATEoEuUE]].
- Inspector-specific uncertainty estimates are visualised together with the inspection data to show how each inspector's observations contribute to the deterioration trajectory [[sources/yt-vx6ATEoEuUE]].

## Sources

- [[sources/yt-vx6ATEoEuUE]]

## Related

- [[concepts/state-space-deterioration-model]]
- [[concepts/visual-inspection-monitoring]]
- [[concepts/kalman-filtering-deterioration]]
