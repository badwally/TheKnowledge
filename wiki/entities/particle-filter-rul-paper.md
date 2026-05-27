---
schema_version: 1
type: entity
slug: particle-filter-rul-paper
canonical_name: A Data-Driven Particle Filter Approach for System-Level Prediction
  of Remaining Useful Life
entity_kind: paper
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T18:18:42Z'
draft_unresolved_claims: 1
created_at: '2026-05-20T19:22:56Z'
last_updated: '2026-05-20T19:22:56Z'
---

# A Data-Driven Particle Filter Approach for System-Level Prediction of Remaining Useful Life

## Summary

A 2025 DX conference paper by Diaz-Gonzalez, Coursey, Quinones-Grueiro, and Biswas presenting a data-driven Bayesian particle filter framework for predicting the Remaining Useful Life (RUL) of industrial systems and quantifying its uncertainty, validated on a UAV system-level prognostics simulation dataset.

## Key facts

- The paper is authored by Abel Diaz-Gonzalez, Austin Coursey, Marcos Quinones-Grueiro, and Gautam Biswas, and was published on 10 November 2025 in the proceedings of the 36th International Conference on Principles of Diagnosis and Resilient Systems (DX 2025) [[sources/web-2025-11-10-fd9]].
- It appears in Open Access Series in Informatics (OASIcs) volume 136, pages 11:1–11:13, published by Schloss Dagstuhl – Leibniz-Zentrum für Informatik, ISBN 978-3-95977-394-2, ISSN 2190-6807, DOI 10.4230/OASIcs.DX.2025.11, URN urn:nbn:de:0030-drops-248006 [[sources/web-2025-11-10-fd9]].
- The paper frames accurate estimation of the remaining useful life (RUL) of industrial systems as a critical component of predictive maintenance strategies [[sources/web-2025-11-10-fd9]].
- It presents a data-driven RUL prediction method that also quantifies uncertainty, drawing inspiration from model-based particle filtering techniques [[sources/web-2025-11-10-fd9]].
- Instead of simulating system state transitions, the authors model degradation as a stochastic process governed by performance metrics, and use a Bayesian particle filtering framework to infer its underlying parameters [[sources/web-2025-11-10-fd9]].
- The approach is explicitly designed to bypass traditional state-space modeling by directly estimating the end-of-life distribution from observed performance data [[sources/web-2025-11-10-fd9]].
- Key characteristics of the particle filter — including propagation noise and observation correction strength — are adapted over time based on current observations and past predictive performance, which the authors argue enables better capture of future uncertainty [[sources/web-2025-11-10-fd9]].
- The proposed method is evaluated using an unmanned aerial vehicle (UAV) simulation dataset developed for system-level prognostics research, which provides high-fidelity degradation signals and ground-truth system performance metrics for validating predictive accuracy [[sources/web-2025-11-10-fd9]].
- The paper's listed keywords are: remaining useful life, particle filter methods, data-driven methods, system-level prognostics, and performance metrics [[sources/web-2025-11-10-fd9]].

## Sources

- [[sources/web-2025-11-10-fd9]]

## Related

- [[entities/abel-diaz-gonzalez]]
- [[entities/austin-coursey]]
- [[entities/marcos-quinones-grueiro]]
- [[entities/gautam-biswas]]
- [[concepts/remaining-useful-life]]
- [[concepts/particle-filter-methods]]
- [[concepts/system-level-prognostics]]
- [[concepts/data-driven-rul-prediction]]
