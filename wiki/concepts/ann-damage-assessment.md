---
schema_version: 1
type: concept
slug: ann-damage-assessment
canonical_name: ANN-based damage assessment
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T18:57:58Z'
draft_unresolved_claims: 1
created_at: '2026-05-20T19:44:55Z'
last_updated: '2026-05-20T19:44:55Z'
---

# ANN-based damage assessment

## Summary

ANN-based damage assessment uses Artificial Neural Networks trained on simulated damage scenarios — derived from a calibrated finite element model — to detect the presence of damage and predict its severity in civil infrastructure, as instantiated for the Rio Claro Viaduct in the 2025 ITcon paper by Porto Oliveira and Dominguez Sotelino.

## Key claims

- ANNs are trained on simulated damage scenarios generated from a calibrated finite element model of the target structure [[sources/web-2025-10-14-bcb]].
- The ANNs use modal curvature damage indices as input features for both damage detection (classification) and severity assessment (regression) [[sources/web-2025-10-14-bcb]].
- On the Rio Claro Viaduct case study, the ANNs achieved an average precision of 85% in damage classification [[sources/web-2025-10-14-bcb]].
- On the same case study, the ANNs achieved an R² of 0.96 in damage severity prediction [[sources/web-2025-10-14-bcb]].
- The ANN outputs are integrated into an enriched BIM model for visualization and decision-making [[sources/web-2025-10-14-bcb]].
- Validation using a decade-separated dataset confirmed the robustness of the ANN-based assessment, showing negligible structural deterioration over that decade for the case-study viaduct [[sources/web-2025-10-14-bcb]].

## Sources

- [[sources/web-2025-10-14-bcb]]

## Related

- [[concepts/structural-health-monitoring]]
- [[concepts/building-information-modelling]]
- [[concepts/modal-curvature-damage-indices]]
- [[concepts/finite-element-model-calibration]]
- [[entities/bim-shm-ann-viaduct-paper]]
- [[entities/rio-claro-viaduct]]
