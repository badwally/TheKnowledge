---
type: concept
slug: state-space-deterioration-model
canonical_name: State-Space Deterioration Model
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T19:53:54Z'
draft_unresolved_claims: 1
---

# State-Space Deterioration Model

## Summary

A state-space deterioration model (SSM) describes structural-element deterioration via two coupled components: a transition model that propagates the latent deterioration state through time under a kinematic process, and an observation model that links visual-inspection measurements (with inspector-specific error) to the latent state, enabling Kalman-filter posterior updating.

## Key claims

- The state-space model is composed of two models: a transition model and an observation model [[sources/yt-vx6ATEoEuUE]].
- The transition model is written as `x_t = A x_{t-1} + w_t`, where `x_t` is the deterioration state at time `t`, `A` is the transition matrix, and `w_t` is the process error [[sources/yt-vx6ATEoEuUE]].
- The transition model is built on the kinematic deterioration equations for condition, speed, and acceleration [[sources/yt-vx6ATEoEuUE]].
- The process error `w_t` is modelled with zero mean and covariance matrix `Q_t` [[sources/yt-vx6ATEoEuUE]].
- The observation model is written as `y_t = C x_t + v_t`, where `C` is the observation matrix and `v_t` is the observation error [[sources/yt-vx6ATEoEuUE]].
- The observation error is modelled with zero mean and a variance specific to each individual inspector [[sources/yt-vx6ATEoEuUE]].
- Given a prior estimate at time `t=0`, the transition model is used to advance the estimate, and the observation model is used to update the estimate when an inspection arrives [[sources/yt-vx6ATEoEuUE]].
- Posterior updates are performed primarily through the Kalman-filtering approach [[sources/yt-vx6ATEoEuUE]].

## Sources

- [[sources/yt-vx6ATEoEuUE]]

## Related

- [[concepts/kinematic-deterioration-model]]
- [[concepts/kalman-filtering-deterioration]]
- [[concepts/inspector-uncertainty]]
- [[concepts/ssm-kernel-regression]]
- [[concepts/bounded-unbounded-inspection-transformation]]
