---
type: concept
slug: ssm-kernel-regression
canonical_name: SSM-KR (State-Space Model with Kernel Regression)
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T19:53:54Z'
draft_unresolved_claims: 1
---

# SSM-KR (State-Space Model with Kernel Regression)

## Summary

SSM-KR is a variant of the state-space deterioration model that augments the underlying state-space model (SSM) with kernel regression, providing an alternative parameterisation for modelling element-level deterioration from visual-inspection data.

## Key claims

- SSM-KR refers to the use of kernel regression alongside the state-space model (SSM) deterioration framework [[sources/yt-vx6ATEoEuUE]].
- SSM-KR has been described in prior published work by the same research group [[sources/yt-vx6ATEoEuUE]].
- The SSM-KR deterioration model produces a deterioration-state estimate at time `t` for a particular structural element, which is then back-transformed into the bounded inspection space for interpretation [[sources/yt-vx6ATEoEuUE]].
- Unbounded observations produced by the bounded-unbounded transformation are passed into either SSM or SSM-KR for inference [[sources/yt-vx6ATEoEuUE]].

## Sources

- [[sources/yt-vx6ATEoEuUE]]

## Related

- [[concepts/state-space-deterioration-model]]
- [[concepts/bounded-unbounded-inspection-transformation]]
- [[entities/bayesworks]]
