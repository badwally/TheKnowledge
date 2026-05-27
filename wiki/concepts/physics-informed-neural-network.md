---
schema_version: 1
type: concept
slug: physics-informed-neural-network
canonical_name: Physics-informed Neural Network (PINN)
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T18:02:17Z'
draft_unresolved_claims: 1
created_at: '2026-05-20T19:35:32Z'
last_updated: '2026-05-20T19:35:32Z'
---

# Physics-informed Neural Network (PINN)

## Summary

A physics-informed neural network (PINN) is a deep neural network whose loss function embeds governing physical equations and other physics-based constraints, enabling the network to solve forward and inverse problems while remaining consistent with known physics.

## Key claims

- A physics-informed neural network (PINN) can be applied to solve a nonlinear multi-degree-of-freedom (MDOF) structural identification problem in order to localize and quantify damage in a reinforced concrete bridge pier after an earthquake [[sources/web-2025-06-07-869]].
- In Yamaguchi (2025), governing equations, the Newmark-β time-integration method, and hysteresis information are incorporated into the loss function of a deep-layered neural network to enforce dynamical and constitutive consistency with seismic response data [[sources/web-2025-06-07-869]].
- When trained on real seismic responses from full-scale shaking table experiments, this PINN formulation successfully estimated distributions of elastic stiffnesses and ductility factors along the pier height in different deterioration cases [[sources/web-2025-06-07-869]].

## Sources

- [[sources/web-2025-06-07-869]]

## Related

- [[entities/pinn-rc-bridge-pier-damage-paper]]
- [[entities/takahiro-yamaguchi]]
- [[concepts/nonlinear-structural-identification]]
- [[concepts/structural-health-monitoring]]
- [[concepts/newmark-beta-method]]
