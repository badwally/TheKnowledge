---
schema_version: 1
type: concept
slug: kinematic-deterioration-model
canonical_name: Kinematic Deterioration Model
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T19:53:54Z'
draft_unresolved_claims: 1
created_at: '2026-05-20T19:53:56Z'
last_updated: '2026-05-20T19:53:56Z'
---

# Kinematic Deterioration Model

## Summary

The kinematic deterioration model describes the temporal evolution of a structural element's deterioration using kinematic equations for the condition, the speed of deterioration, and the acceleration of deterioration, enabling joint estimation of all three quantities from visual-inspection data.

## Key claims

- Deterioration behaviour is described using a kinematic model with separate kinematic equations for condition, speed, and acceleration [[sources/yt-vx6ATEoEuUE]].
- The kinematic equations can be written in matrix form `x_t = A x_{t-1} + w_t`, where `x_t` is the deterioration state at time `t`, `A` is the transition matrix, and `w_t` is the process error [[sources/yt-vx6ATEoEuUE]].
- Using the kinematic model allows the analyst to characterise both the condition trajectory and the deterioration speed of a structural element [[sources/yt-vx6ATEoEuUE]].
- The kinematic deterioration speed can be modelled jointly with the effect of interventions on both condition and speed [[sources/yt-vx6ATEoEuUE]].

## Sources

- [[sources/yt-vx6ATEoEuUE]]

## Related

- [[concepts/state-space-deterioration-model]]
- [[concepts/intervention-effect-modeling]]
