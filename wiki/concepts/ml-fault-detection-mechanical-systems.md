---
schema_version: 1
type: concept
slug: ml-fault-detection-mechanical-systems
canonical_name: Machine Learning Fault Detection for Building Mechanical Systems
domains:
- condo-capital-infra
created_at: '2026-05-11T22:04:18Z'
last_updated: '2026-05-11T22:04:18Z'
---
# Machine Learning Fault Detection for Building Mechanical Systems

## Summary

Supervised machine-learning models — including XGBoost, Random Forest, Artificial Neural Networks, and Logistic Regression — are used to refine component-failure probability estimates by analyzing sensor data from Building Management Systems (BMS) and IoT integrations [[sources/docx-818ed0a0ce55]]. In the condo-capital-infra engine architecture, ML fault detection is the empirical refinement layer that complements the Weibull statistical prior: where the Weibull captures the population-level hazard rate of a component class, an ML model trained on historical failure data from thousands of similar buildings refines per-asset failure probabilities by detecting early-stage anomalies in sensor streams [[sources/docx-818ed0a0ce55]]. The approach is the operational bridge between the engine's static six-probabilistic-component priors and its work-order ingest design, and the methodological anchor for the year-3 sensor-upsell roadmap.

## Key claims

- Recent advancements in building management systems (BMS) and IoT integration have enabled the use of supervised machine-learning models to refine component-failure probability estimates [[sources/docx-818ed0a0ce55]].
- XGBoost has demonstrated 95% accuracy and 0.93 F1-score on detecting HVAC damper / valve anomalies in multi-unit residential buildings [[sources/docx-818ed0a0ce55]].
- Random Forest uses ensemble voting to generalize across diverse component libraries [[sources/docx-818ed0a0ce55]].
- Artificial Neural Networks (ANN) provide non-linear mapping suitable for modeling complex interactions in building envelopes [[sources/docx-818ed0a0ce55]].
- Logistic Regression provides probability output for predicting binary failure / non-failure states [[sources/docx-818ed0a0ce55]].
- Training these models on historical failure data from thousands of similar buildings allows the software to account for variables that a single engineer might overlook [[sources/docx-818ed0a0ce55]].
- The "Damper_Open_No_Occupancy" fault — a damper held open in the absence of occupancy, causing excessive wear on ventilation motors — can be detected by correlating CO2 sensors with damper position data, allowing the software to adjust the failure probability for the motor accordingly [[sources/docx-818ed0a0ce55]].
- ML fault detection refines but does not replace the Weibull statistical prior: the Weibull captures population-level hazard rates by component class; the ML model refines per-asset probabilities by detecting early-stage anomalies in sensor data [[sources/docx-818ed0a0ce55]].
- The approach requires structured covariates (BMS sensor data, work-order records, occupancy patterns) — making it operationally dependent on the work-order ingest layer of the condo-capital-infra engine and on year-3 sensor deployments for buildings without pre-existing BMS coverage [[sources/docx-818ed0a0ce55]].

## Sources

- [[sources/docx-818ed0a0ce55]]

## Related

- [[concepts/weibull-component-failure-distribution]]
- [[concepts/probabilistic-reserve-modeling]]
- [[concepts/six-probabilistic-components]]
- [[concepts/cmms-workorder-covariates]]
- [[concepts/monte-carlo-reserve-confidence-intervals]]
- [[concepts/tech-enabled-reserve-study-firm]]
