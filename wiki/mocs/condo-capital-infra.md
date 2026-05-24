---
type: moc
slug: condo-capital-infra
domain: condo-capital-infra
last_updated: '2026-05-13T16:25:39Z'
draft: true
draft_started_at: '2026-05-13T16:25:39Z'
draft_unresolved_claims: 14
---
# condo-capital-infra — Map of Content

## Overview

Auto-generated from the corpus-constructive research loop. Anchored on the most recent `wiki research` run.

## Key entities

- [[sources/web-2014-02-02-a8a]] — Planning structural inspection and maintenance policies via
- [[sources/web-2023-08-02-ec3]] — E917 Standard Practice for Measuring Life-Cycle Costs of Buildings ...
- [[sources/web-2002-10-01-eee]] — The Environmental Life Cycle | NIST
- [[sources/web-2014-06-26-215]] — life-cycle costs (LCC) of buildings/building systems, practice
- [[sources/web-2020-03-01-b61]] — Pavement Deterioration Model Using Markov Chain and International Roughness Index

## Key concepts

- **Component-Level Degradation Modeling** — The sources discuss probabilistic models, specifically Markov chains, used to forecast the future condition and deterioration of structural components over time [1, 2].
  - Markov Chain Deterioration: Transition probability matrices developed from historical databases, such as the LTPP database for pavement, can predict conditions after a set number of transition periods [1]., The broader literature includes competing Markov models and Hidden Markov models used for predicting cracking and statistical deterioration in civil structures [3].
  - Corroding and Deteriorating Structures: A 332-state formulation has been applied to model corroding reinforced concrete structures to determine minimum life-cycle costs [2]., Pavement deterioration models track the expansion of distresses like cracks and rutting using condition metrics such as the International Roughness Index (IRI) [1].
- **Cost and Financial Framing (Life-Cycle Cost Analysis)** — The corpus emphasizes evaluating the long-term economic performance of building systems through established standard practices like ASTM E917 [4, 5].
  - ASTM E917 Methodology: The LCC framework includes all relevant costs arising from an investment decision, including designing, purchasing, installing, operating, maintaining, repairing, replacing, and disposing of a system [8, 9]., The methodology is used to determine whether a higher initial cost is economically justified by reductions in future expenses, evaluating projects against "do nothing" alternatives [4, 7].
  - Economic and Environmental Integration: Economic metrics derived via ASTM E917 can be combined with environmental life-cycle assessments (ISO 14040) using the ASTM E1765 standard for Multiattribute Decision Analysis [5].
- **Data Ingestion, Inspection Updating, and Decision Theory** — Data collection and continuous inspection are integrated into stochastic control frameworks to plan optimal maintenance policies based on uncertain structural data [2].
  - POMDP for Inspection and Maintenance Policies: The POMDP framework supports uncertain observations, uncertain action outcomes, non-periodic inspections, and choices among various inspection and monitoring types [2]., Solving POMDPs yields optimal policies involving a complex combination of actions, utilizing point-based value iteration solvers for large state spaces [2].
  - Bayesian Updating and Value of Information: Quasi-Bayes approaches have been cited as a method to optimize inspection and maintenance decisions for infrastructure facilities under performance model uncertainty [10]., Evaluating the value of information is a critical component in planning component inspections and permanent monitoring systems [10].
- **System-Level and Portfolio Aggregation** — The sources discuss optimizing maintenance and rehabilitation policies not just for individual components, but aggregated across larger networks or multi-component systems [10, 11].
  - Multi-Component Optimization: Integrated optimization methodologies address both maintenance interventions and spare part selection for multi-component systems [3]., Dynamic programming models can be extended to handle management optimization at a generalized multi-structure level [10].
  - Infrastructure Network Management: The Pontis system is utilized for maintenance optimization and improvement of entire US bridge networks [11]., Iterative approaches and statewide pavement management systems incorporate joint optimization of maintenance, rehabilitation, and reconstruction planning [10, 11].

## Synthesis pages

_(populated as `wiki research` and `wiki query` runs file syntheses)_
