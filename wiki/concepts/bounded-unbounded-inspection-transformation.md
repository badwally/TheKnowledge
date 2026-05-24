---
type: concept
slug: bounded-unbounded-inspection-transformation
canonical_name: Bounded-Unbounded Inspection Transformation
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T19:53:55Z'
draft_unresolved_claims: 1
---

# Bounded-Unbounded Inspection Transformation

## Summary

The bounded-unbounded inspection transformation is a step-function mapping that converts visual-inspection condition ratings from their natural bounded reporting scale (e.g., 25 = poor, 100 = perfect) into an unbounded space suitable for a Gaussian state-space deterioration model, and back-transforms posterior deterioration estimates into the bounded space for interpretation.

## Key claims

- Visual inspections in reality are bounded and refer to explicit anchor values for poor condition (e.g., 25) and perfect condition (e.g., 100) [[sources/yt-vx6ATEoEuUE]].
- A transformation function — described as a step function and labelled `O` — is applied to map bounded inspections into an unbounded observation space [[sources/yt-vx6ATEoEuUE]].
- The unbounded observations are passed into the deterioration state-space model (SSM, or SSM-KR with kernel regression) for inference [[sources/yt-vx6ATEoEuUE]].
- The posterior deterioration estimate is back-transformed through the same step function into the bounded inspection space for interpretability [[sources/yt-vx6ATEoEuUE]].
- The transformation lets analysts present results within the bounds familiar to inspectors while keeping the inference machinery operating in an unbounded space [[sources/yt-vx6ATEoEuUE]].

## Sources

- [[sources/yt-vx6ATEoEuUE]]

## Related

- [[concepts/visual-inspection-monitoring]]
- [[concepts/state-space-deterioration-model]]
- [[concepts/ssm-kernel-regression]]
