---
schema_version: 1
type: concept
slug: nonlinear-structural-identification
canonical_name: Nonlinear Structural Identification
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T18:02:17Z'
draft_unresolved_claims: 1
created_at: '2026-05-20T19:35:32Z'
last_updated: '2026-05-20T19:35:32Z'
---

# Nonlinear Structural Identification

## Summary

Nonlinear structural identification is the inverse problem of inferring nonlinear stiffness, hysteretic, and damage parameters of a multi-degree-of-freedom structure from its measured dynamic response, often under severe loading such as earthquake excitation.

## Key claims

- Post-earthquake damage assessment of a reinforced concrete bridge pier can be formulated as a nonlinear multi-degree-of-freedom (MDOF) structural identification problem [[sources/web-2025-06-07-869]].
- Yamaguchi (2025) proposes solving this nonlinear MDOF identification problem with a physics-informed neural network whose loss function encodes governing equations, the Newmark-β integration scheme, and hysteresis information [[sources/web-2025-06-07-869]].
- A stacked bilinear rotational spring model can serve as the underlying nonlinear structural representation whose parameters — elastic stiffnesses and ductility factors along the pier height — are identified [[sources/web-2025-06-07-869]].

## Sources

- [[sources/web-2025-06-07-869]]

## Related

- [[entities/pinn-rc-bridge-pier-damage-paper]]
- [[concepts/physics-informed-neural-network]]
- [[concepts/stacked-bilinear-rotational-spring-model]]
- [[concepts/structural-health-monitoring]]
