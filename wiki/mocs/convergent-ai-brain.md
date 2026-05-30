---
schema_version: 1
type: moc
slug: convergent-ai-brain
title: convergent-ai-brain — Map of Content
domain: convergent-ai-brain
created_at: '2026-05-30T18:58:04Z'
last_updated: '2026-05-30T18:58:04Z'
draft: true
draft_started_at: '2026-05-30T18:58:04Z'
---
Map of content for the **convergent-ai-brain** domain: how biological brains and artificial neural networks come to learn similar functions and representations.

## Overview

**Driving hypothesis (H1 — convergence under shared pressure):** Biological brains and artificial neural networks converge toward a shared, modality-agnostic representation of the world because both are subject to the same selective pressures — task generality, capacity, and a simplicity/compression bias — operating over the common statistical structure of reality. Representational alignment between a brain and an ANN should therefore **increase with the ANN's competence and capacity**, converging toward a **ceiling set by the mutual information between the two systems' inputs.**

Falsifiable sub-claims:

- **(a) Scaling** — better/larger ANNs align more closely with neural data.
- **(b) Ceiling** — alignment is bounded by the mutual information between brain inputs and ANN inputs; it never exceeds it.
- **(c) Cross-modal** — convergence holds across vision ↔ language ↔ neural, since all are projections of the same latent reality.
- **(d) Mechanism** — each pressure (task/data, capacity, simplicity) independently predicts alignment.

The project is wrong if bigger/better models do **not** align more, if alignment exceeds the mutual-information ceiling, or if convergence proves architecture-specific rather than pressure-driven.

**Out of scope:** machine consciousness and phenomenal experience; agentic AI, multi-agent systems and delegation; ML scaling work with no comparison to biological brains.

## Key concepts

**Why convergence happens (mechanism):**

- [[concepts/platonic-representation-hypothesis]] — convergence toward a shared statistical model of reality
- [[concepts/representational-convergence]]
- [[concepts/universality-ml]] — universality / compression as a convergence driver
- [[concepts/anna-karenina-scenario]] — "all strong models are alike"
- [[concepts/foundation-models]]

**The shared learning objective (predictive brain):**

- [[concepts/predictive-processing]]
- [[concepts/bayesian-brain]]
- [[concepts/hierarchical-predictive-coding]]
- [[concepts/prediction-error]] · [[concepts/surprisal]]
- [[concepts/active-inference]]
- [[concepts/generative-model-brain]] · [[concepts/analysis-by-synthesis]]
- [[concepts/helmholtz-machine]] — the ML ancestor bridging brains and generative ANNs

**Measuring & observing alignment (evidence):**

- [[concepts/representational-alignment]]
- [[concepts/mutual-nearest-neighbor-alignment]]
- [[concepts/model-stitching]] · [[concepts/rosetta-neurons]]
- [[concepts/functional-brain-networks]]

## Key entities

- [[entities/andy-clark]] — predictive-processing / Bayesian-brain
- [[entities/karl-friston]] — free-energy principle, active inference
- [[entities/hermann-von-helmholtz]] — perception as unconscious inference
- [[entities/minyoung-huh]] · [[entities/phillip-isola]] — Platonic Representation Hypothesis
- [[entities/samuel-hammond]] — bridge essayist
- [[entities/steven-byrnes]] — brain-as-learning-algorithm account
- [[entities/goldstein-2022-ecog]] — ECoG: shared compute between brain and autoregressive LMs *(stub — primary paper awaiting ingest)*
- [[entities/topolm]] — cortical topography from a spatial-smoothness loss *(stub — primary paper awaiting ingest)*

## Synthesis pages

*None yet. First synthesis queries to run (multi-adapter research):*

1. What is the evidence that brain↔ANN representational alignment scales with model competence? *(sub-claim a)*
2. What sets the ceiling on brain↔ANN representational convergence? *(sub-claim b)*
3. Do predictive/generative objectives align with neural data better than discriminative ones at matched performance? *(thread: objective ↔ measurement)*

## Anchor sources

- [[sources/pdf-minyoung-huh-2024-the-platonic-representation]] — Huh, Cheung, Wang, Isola (ICML 2024)
- [[sources/pdf-5f41a1d2e45f]] — Clark, "Whatever next?" (BBS 2013)
- [[sources/web-2026-05-27-cee]] — Hammond, "Time to take AI consciousness seriously" (bridge/entry hub; consciousness layer excluded)

## Editorial notes

- `simulator-theory-llms` and `persona-selection-model` (from the Hammond pass) drift toward the excluded consciousness/alignment layer — review for scope at finalization.
- Empirical-spine primary papers (Yamins, Schrimpf/Brain-Score, Goldstein ECoG, TopoLM, Olshausen & Field) are expected to enter via multi-adapter research once the domain runs; the policy is tuned to surface them.
