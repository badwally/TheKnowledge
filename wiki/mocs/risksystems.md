---
schema_version: 1
type: moc
slug: risksystems
title: risksystems — Map of Content
domain: risksystems
created_at: '2026-05-29T21:12:33Z'
last_updated: '2026-05-29T21:12:33Z'
---
# risksystems — Map of Content

## Overview

The risksystems domain covers applied AI and probabilistic methods for capital-asset and built-environment risk assessment — the methodological substrate for Longspan's probabilistic reserve study engine. The corpus spans five research threads: (1) stochastic deterioration and survival processes (gamma processes, Weibull, AFT models), (2) Bayesian hierarchical modelling and partial pooling across heterogeneous asset populations, (3) physics-informed and hybrid modelling for structural assessment, (4) GP, state-space, and ensemble methods for remaining useful life prediction, and (5) foundation models and LLM-based approaches to maintenance data processing.

The domain anchors two load-bearing architecture decisions: the BGP (Bounded Gamma Process) for Phase 1 components (envelope, roof, parking deck), and WTNN (Weibull-Tailored Neural Networks) for Phase 2 components (HVAC, elevators, plumbing risers).

## Key entities

**Research groups and institutions**
- [[entities/dan-frangopol]] — lifecycle optimization; load-bearing citations on probabilistic multi-objective infrastructure decisions
- [[entities/michael-faber]] — JCSS; structural reliability and expert elicitation
- [[entities/daniel-straub]] — Bayesian updating and structural reliability; Bayesian filtering for deterioration
- [[entities/eleni-chatzi]] — structural health monitoring and hybrid modelling
- [[entities/jochen-kohler]] — JCSS; structural safety and reliability
- [[entities/ajax-parlikad]] — infrastructure asset management systems and CMMS
- [[entities/nicolas-bousquet]] — WTNN and Weibull-tailored neural networks; Sheffield elicitation framework

**Software and data infrastructure**
- [[entities/aware-p]] — AWARE-P; urban water infrastructure planning platform
- [[entities/care-s]] · [[entities/care-w]] — sewer and water network rehabilitation software
- [[entities/ltpp-program]] — LTPP; long-term pavement performance program; largest public infrastructure deterioration dataset
- [[entities/nasa-prognostics-center-of-excellence]] — PHM benchmark datasets
- [[entities/phm-society]] — PHM Society; prognostics and health management community and data repository

## Key concepts

**Core deterioration models**
- [[concepts/gamma-process]] — the canonical monotonic-degradation stochastic process; the Longspan BGP lineage root
- [[concepts/nonstationary-gamma-process]] — time-transformed gamma process; handles changing deterioration rates
- [[concepts/bounded-nonstationary-gamma-process]] — BNGP; the v3 Phase 1 candidate kernel
- [[concepts/bounded-transformed-gamma-process]] — BTGP per arxiv-2508.13359; bound estimated as a parameter
- [[concepts/transformed-gamma-process]] — bounded degradation phenomena
- [[concepts/weibull-tailored-neural-networks]] — WTNN (Rives/Lopez/Bousquet 2025); Weibull(β,η) as covariate function; v3 Phase 2 candidate

**Bayesian methods**
- [[concepts/bayesian-hierarchical-modelling]] — partial pooling across heterogeneous asset cohorts; the architecture that makes small-n defensible
- [[concepts/hierarchical-bayesian-modelling]] — same; load-bearing for the Mercer P.Eng. credibility argument
- [[concepts/bayesian-filtering-deterioration]] — on-line and off-line Bayesian filtering for deterioration state estimation
- [[concepts/expert-elicitation]] — Sheffield framework; encodes engineer judgement as prior
- [[concepts/sheffield-elicitation-framework]] — SHELF; the formal prior-elicitation protocol

**ML and data-driven**
- [[concepts/graph-neural-networks-pavement]] — Texas DOT PMIS GNN; 500K+ obs; spatial road network dependencies
- [[concepts/explainable-ai]] — XAI for flood-induced pavement deterioration; SHAP covariate impact
- [[concepts/reinforcement-learning-maintenance]] — RL for imperfect-repair maintenance policies; Phase 3 candidate
- [[concepts/data-driven-rul-prediction]] — data-driven RUL prediction; particle filter approaches
- [[concepts/llm-data-cleaning-agents]] — LLM agents for maintenance log cleaning; Phase 4 candidate

**Infrastructure applications**
- [[concepts/pavement-deterioration-modeling]] — network-scale pavement deterioration; the best-documented external dataset for BGP calibration benchmarking
- [[concepts/structural-health-monitoring]] — SHM; sensor-based deterioration monitoring
- [[concepts/infrastructure-asset-management]] — IAM framework; system-centric asset management
- [[concepts/remaining-useful-life]] — RUL prediction; the PHM community's standard prediction target

## Synthesis pages

- [[synthesis/2026-05-20-bounded-gamma-process-bgp-deterioration-kernel]] — BGP kernel for Longspan v3: mathematical lineage (stationary → nonstationary → BTGP → hierarchical), ML implementations at scale, component-readiness table for Longspan's six components
- [[synthesis/2026-05-20-weibull-tailored-neural-networks-wtnn-drilldown]] — WTNN drilldown: mathematical lineage, SOTA implementations, Longspan six-component readiness vs BGP
- [[synthesis/2026-05-20-cross-cutting-comparison-longspan-v1-1]] — Longspan v1.1 vs methodological state of the art: where v1.1 sits at the frontier, top v2 design surfaces, v3 methodological moat candidates
- [[synthesis/2026-05-20-risksystems-01-bayesian-hierarchical-survival-stochastic-deterioration-and-survival-processes]] — Stochastic deterioration and survival processes research thread
- [[synthesis/2026-05-20-risksystems-02-physics-informed-sciml-hybrid-modeling-and-data-driven-structural]] — Hybrid modelling and data-driven structural assessment thread
- [[synthesis/2026-05-20-risksystems-03-gp-state-space-ensembles-state-space-methods-and-particle-filters]] — State-space methods and particle filters thread
- [[synthesis/2026-05-20-risksystems-04-foundation-models-causal-probabilistic-engines-for-asset-deterioration]] — Foundation models and probabilistic engines thread

## Open questions

- What is the minimum-viable n for a defensible BGP fit on building envelope data? (Diesel cylinder liner analog: what did it take?)
- Which of the six Longspan components crosses the BGP-ready threshold from the existing 60-building BC sample?
- Does WTNN outperform BGP on elevator components with non-monotonic failure profiles?
