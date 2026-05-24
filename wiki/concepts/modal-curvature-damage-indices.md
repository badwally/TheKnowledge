---
type: concept
slug: modal-curvature-damage-indices
canonical_name: Modal curvature damage indices
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T18:57:58Z'
draft_unresolved_claims: 1
---

# Modal curvature damage indices

## Summary

Modal curvature damage indices are vibration-based damage features derived from a structure's modal curvatures; in the 2025 ITcon framework by Porto Oliveira and Dominguez Sotelino they serve as the input feature set fed to ANNs for both damage detection and severity assessment of viaducts.

## Key claims

- Modal curvature damage indices are used as the input feature set for ANN-based damage detection and severity assessment in the 2025 ITcon framework [[sources/web-2025-10-14-bcb]].
- The indices are derived from dynamic behaviour data captured via ambient vibration analysis and a calibrated finite element model [[sources/web-2025-10-14-bcb]].
- Using modal curvature damage indices, the ANNs achieved an average precision of 85% in damage classification and an R² of 0.96 in severity prediction on the Rio Claro Viaduct case study [[sources/web-2025-10-14-bcb]].

## Sources

- [[sources/web-2025-10-14-bcb]]

## Related

- [[concepts/ann-damage-assessment]]
- [[concepts/structural-health-monitoring]]
- [[concepts/ambient-vibration-analysis]]
- [[concepts/finite-element-model-calibration]]
- [[entities/bim-shm-ann-viaduct-paper]]
