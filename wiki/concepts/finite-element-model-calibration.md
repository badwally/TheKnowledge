---
type: concept
slug: finite-element-model-calibration
canonical_name: Finite element model calibration
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T18:57:58Z'
draft_unresolved_claims: 1
---

# Finite element model calibration

## Summary

Finite element model calibration is the process of tuning a structural finite-element model so that its predicted responses match measured field data; in the 2025 ITcon framework by Porto Oliveira and Dominguez Sotelino it bridges ambient-vibration field measurements and the simulated damage scenarios used to train ANN damage-assessment models.

## Key claims

- In the 2025 ITcon framework, the finite element model of the Rio Claro Viaduct was calibrated using dynamic behaviour data captured via ambient vibration analysis [[sources/web-2025-10-14-bcb]].
- The calibrated finite element model is then used to generate simulated damage scenarios that serve as the training data for ANN-based damage detection and severity-assessment models [[sources/web-2025-10-14-bcb]].
- Calibration is the bridge that allows monitoring-derived dynamic data to be expressed as physically meaningful damage indices (e.g., modal curvature damage indices) for ANN training [[sources/web-2025-10-14-bcb]].

## Sources

- [[sources/web-2025-10-14-bcb]]

## Related

- [[concepts/structural-health-monitoring]]
- [[concepts/ambient-vibration-analysis]]
- [[concepts/ann-damage-assessment]]
- [[concepts/modal-curvature-damage-indices]]
- [[entities/rio-claro-viaduct]]
- [[entities/bim-shm-ann-viaduct-paper]]
