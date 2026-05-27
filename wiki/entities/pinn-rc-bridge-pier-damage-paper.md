---
schema_version: 1
type: entity
slug: pinn-rc-bridge-pier-damage-paper
canonical_name: Damage Identification of a Reinforced Concrete Bridge Pier after an
  Earthquake based on a Physics-informed Neural Network
entity_kind: paper
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T18:02:17Z'
draft_unresolved_claims: 1
created_at: '2026-05-20T19:35:32Z'
last_updated: '2026-05-20T19:35:32Z'
---

# Damage Identification of a Reinforced Concrete Bridge Pier after an Earthquake based on a Physics-informed Neural Network

## Summary

A 2025 IABSE Symposium Tokyo conference paper by Takahiro Yamaguchi (University of Tokyo) proposing a physics-informed neural network (PINN) for post-earthquake condition assessment of reinforced concrete bridge piers, framed as a nonlinear multi-degree-of-freedom structural identification problem that localizes and quantifies damage by jointly estimating elastic stiffnesses and ductility factors along the pier height.

## Key facts

- The paper is authored solely by Takahiro Yamaguchi of the University of Tokyo and was presented at the IABSE Symposium Tokyo 2025 (18-21 May 2025), appearing in the proceedings on pages 1902-1909 with DOI 10.2749/tokyo.2025.1902 [[sources/web-2025-06-07-869]].
- The paper addresses condition assessment of a reinforced concrete (RC) bridge pier after an earthquake based on seismic responses [[sources/web-2025-06-07-869]].
- The paper proposes a physics-informed neural network (PINN) for solving a nonlinear multi-degree-of-freedom (MDOF) structural identification problem in order to localize and quantify damage [[sources/web-2025-06-07-869]].
- The approach adopts a stacked bilinear rotational spring model to represent the pier [[sources/web-2025-06-07-869]].
- Governing equations, the Newmark-β method, and hysteresis information are incorporated into the loss function of the deep-layered neural network [[sources/web-2025-06-07-869]].
- The method was validated using real seismic responses obtained from full-scale shaking table experiments [[sources/web-2025-06-07-869]].
- The method successfully estimated distributions of elastic stiffnesses and ductility factors (DFs) along the pier height in different deterioration cases [[sources/web-2025-06-07-869]].
- The estimated parameter distributions revealed local decreases and increases corresponding to observed concrete and rebar damage [[sources/web-2025-06-07-869]].
- Keywords for the paper are earthquakes, structural health monitoring (SHM), Physics-informed Neural Network (PINN), Reinforced Concrete (RC) Bridge Pier, and Nonlinear Structural Identification [[sources/web-2025-06-07-869]].
- The paper is published under © 2025 International Association for Bridge and Structural Engineering (IABSE) [[sources/web-2025-06-07-869]].

## Sources

- [[sources/web-2025-06-07-869]]

## Related

- [[entities/takahiro-yamaguchi]]
- [[entities/iabse]]
- [[concepts/physics-informed-neural-network]]
- [[concepts/structural-health-monitoring]]
- [[concepts/nonlinear-structural-identification]]
- [[concepts/stacked-bilinear-rotational-spring-model]]
- [[concepts/newmark-beta-method]]
- [[concepts/ductility-factor]]
- [[concepts/shaking-table-experiment]]
