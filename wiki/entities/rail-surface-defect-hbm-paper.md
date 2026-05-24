---
type: entity
slug: rail-surface-defect-hbm-paper
canonical_name: Rail surface defect prediction and inspection planning using limited
  maintenance data – a hierarchical Bayesian approach
entity_kind: paper
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:46Z'
draft_unresolved_claims: 1
---

# Rail surface defect prediction and inspection planning using limited maintenance data – a hierarchical Bayesian approach

## Summary

A 2026 paper by Saeed Khalaj, Huy Truong-Ba, Michael E Cholette, Sinda Rebello, and Tommy H T Chan proposing a Homogeneous Poisson Process (HPP) defect-arrival model fit by Hierarchical Bayesian Modelling (HBM) with MCMC to predict rail surface defect arrivals across networks with sparse visual inspection data, and using the fitted models to support inspection planning by trading off the age of the oldest unobserved defect against inspection frequency.

## Key facts

- The paper is authored by Saeed Khalaj, Huy Truong-Ba, Michael E Cholette, Sinda Rebello, and Tommy H T Chan and was published 4 March 2026 with DOI 10.1080/23248378.2025.2508803 [[sources/web-2026-03-04-157]].
- The paper proposes a Homogeneous Poisson Process (HPP) identified via a Hierarchical Bayesian Modelling (HBM) approach that uses partial pooling of unevenly distributed inspection data to improve parameter estimates [[sources/web-2026-03-04-157]].
- Posteriors of the model parameters are estimated using Markov Chain Monte Carlo (MCMC) techniques, and metrics are developed to compare the posteriors from different areas of the network [[sources/web-2026-03-04-157]].
- In the absence of cost data, the fitted HPP models are used to examine the trade-off between the oldest unobserved defect (treated as a proxy for risk) and the inspection frequency [[sources/web-2026-03-04-157]].
- The authors choose HPP over a non-homogeneous Poisson process because modelling the non-homogeneous behaviour of the defect arrival process is highly dependent on the precise rail installation date, which is poorly known for long-lived tracks [[sources/web-2026-03-04-157]].
- The model uses Million Gross Tonnes (MGT) in place of time, following prior practice in surface-defect modelling [[sources/web-2026-03-04-157]].
- The methodology is demonstrated on visual inspection data covering a combination of suburban and regional tracks in Australia with varying traffic patterns and track lengths [[sources/web-2026-03-04-157]].
- Surface defect types considered include squats, rolling contact fatigue, gauge corner cracking, wheel burn, and corrugation, with squats identified as the most frequently recorded surface defect [[sources/web-2026-03-04-157]].
- The paper restricts attention to visual inspection data despite its subjectivity because non-destructive testing techniques such as ultrasonic and Eddy current inspection are relatively new compared to the life of the asset and come with considerable costs [[sources/web-2026-03-04-157]].

## Sources

- [[sources/web-2026-03-04-157]]

## Related

- [[entities/saeed-khalaj]]
- [[entities/huy-truong-ba]]
- [[entities/michael-cholette]]
- [[entities/sinda-rebello]]
- [[entities/tommy-chan]]
- [[concepts/homogeneous-poisson-process]]
- [[concepts/hierarchical-bayesian-modelling]]
- [[concepts/markov-chain-monte-carlo]]
- [[concepts/partial-pooling]]
- [[concepts/rail-surface-defects]]
- [[concepts/visual-inspection]]
- [[concepts/inspection-planning-decision-support]]
