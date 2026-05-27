---
schema_version: 1
type: synthesis
slug: 2026-05-20-risksystems-04-foundation-models-causal-retrospective-intervention-effect-estimation-and-maintenance
title: Retrospective Intervention Effect Estimation and Maintenance Optimization —
  investigation (2026-05-20-risksystems-04-foundation-models-causal)
domains:
- risksystems
question: 'Risksystems Q4 of 4 — foundation-model / LLM approaches to structured extraction

  from engineering and reserve-study documents, decision-narrative generation for

  licensed-professional sign-off, and causal inference / counterfactual reasoning

  for capital-project overrun attribution. Frame: Longspan v1.1 produces P10/P50/P90

  bands but no causal narrative; the question is what role LLM/foundation-model

  approaches play (extraction yes, methodology no) and which causal-inference

  primitives become a v3 deliverable for board-facing retrospective questions.

  Specifically: LLM-as-judge + LLM-with-tools for structured extraction;

  constrained decoding (Outlines, Pydantic-AI, Instructor, BAML); RAG quality +

  hallucination controls (RAGAS, RAGTruth, citation-grounded retrieval); LLM

  narrative on top of a probabilistic engine including the "AI narrative is table

  stakes" competitive frame; causal inference under DoWhy / EconML / CausalML;

  target trial emulation (Hernan); difference-in-differences and regression

  discontinuity for retrospective maintenance-intervention effect estimation;

  double-ML; POMDP + Bayesian decision theory for inspect-repair-replace with

  quantified value-of-information.

  '
created_at: '2026-05-20T18:44:57Z'
synthesizes:
- sources/web-2026-01-13-6bf
draft: true
draft_started_at: '2026-05-20T18:44:58Z'
draft_unresolved_claims: 6
last_updated: '2026-05-20T18:44:58Z'
sources_count: 3
---
# Retrospective Intervention Effect Estimation and Maintenance Optimization — investigation

**Origin question:** Risksystems Q4 of 4 — foundation-model / LLM approaches to structured extraction
from engineering and reserve-study documents, decision-narrative generation for
licensed-professional sign-off, and causal inference / counterfactual reasoning
for capital-project overrun attribution. Frame: Longspan v1.1 produces P10/P50/P90
bands but no causal narrative; the question is what role LLM/foundation-model
approaches play (extraction yes, methodology no) and which causal-inference
primitives become a v3 deliverable for board-facing retrospective questions.
Specifically: LLM-as-judge + LLM-with-tools for structured extraction;
constrained decoding (Outlines, Pydantic-AI, Instructor, BAML); RAG quality +
hallucination controls (RAGAS, RAGTruth, citation-grounded retrieval); LLM
narrative on top of a probabilistic engine including the "AI narrative is table
stakes" competitive frame; causal inference under DoWhy / EconML / CausalML;
target trial emulation (Hernan); difference-in-differences and regression
discontinuity for retrospective maintenance-intervention effect estimation;
double-ML; POMDP + Bayesian decision theory for inspect-repair-replace with
quantified value-of-information.

**Session:** 2026-05-20-risksystems-04-foundation-models-causal
**Branch:** Retrospective Intervention Effect Estimation and Maintenance Optimization

## Synthesis

### Specifics

## Retrospective Intervention Effect Estimation and Maintenance Optimization

Based on the provided sources, the corpus approaches maintenance optimization and retrospective effect estimation through physical parameter tracking of visual inspections and advanced reinforcement learning frameworks.

*   **Name and key claim:** Log-Likelihood Maximization for Unreported Interventions
    *   **The core approach, mechanism, or supporting evidence:** When historical records lack both the date and the type of an intervention, the framework first identifies a structural upward trend in physical condition to ensure the observed jump is not merely statistical noise [1]. Because the model operates with a limited, predefined set of potential interventions for a given structural category, it systematically tests the theoretical effect of each known repair type [1]. The system ultimately deduces the missing intervention by selecting the repair type that maximizes the log-likelihood estimate for that specific element [1].
    *   **Any concrete details:** The initial trend identification relies on a mathematical $\Delta$ criterion, which is calculated as the ratio of the sum of positive condition improvements to the sum of all changes in absolute value [1]. By doing this, the system explicitly models the mathematical "jump" in the bounded condition space (scaled from 25 to 100) and the subsequent alteration to the asset's deterioration speed [1]. This retrospective estimation framework was practically demonstrated on a database comprising approximately 10,000 bridges located in the province of Quebec [1].

*   **Name and key claim:** Double Deep Q-Network (DDQN) for Increasingly Imperfect Repairs
    *   **The core approach, mechanism, or supporting evidence:** To optimize inspect-repair policies, researchers developed a reinforcement learning agent that operates on top of a continuous gamma degradation process [2]. The core mechanism introduces a novel maintenance model characterizing interventions as "increasingly imperfect," which explicitly reflects the real-world phenomenon where the beneficial impact of system repairs inherently decreases as an asset undergoes more repairs over its lifetime [2]. 
    *   **Any concrete details:** The framework specifically utilizes a Double Deep Q-Network (DDQN) architecture to formulate these maintenance policies [2]. The text highlights two major advantages of this DDQN agent: it successfully functions without relying on any predefined preventive maintenance thresholds, and it natively operates within a continuous degradation state space [2]. An analysis of how changes in the environment parameters affect the agent's proposed policy shows that this approach significantly improves long-run costs when compared against other common maintenance strategies [2].

[^2]: [[sources/2]]
[^3]: [[sources/3]]

[^1]: [[sources/web-2026-01-13-6bf]] [^2]: [[sources/web-2026-01-13-6bf]]

### Comparisons

## Retrospective Intervention Effect Estimation and Maintenance Optimization: Framework Comparisons

Based on the provided sources, comparing approaches to intervention estimation and maintenance optimization reveals a fundamental split between retrospective data imputation frameworks and prescriptive, continuous-state reinforcement learning agents.

**Items Compared:**
* Retrospective Data Imputation (Log-Likelihood Maximization) vs. Prescriptive Maintenance Policy Generation (Double Deep Q-Network)
* Bounded State-Space Jump Estimation vs. Continuous Degradation (Gamma Process) Modeling
* Handling of Missing Historical Data vs. Handling of "Increasingly Imperfect" Repair Dynamics

The Log-Likelihood maximization approach is explicitly designed for retrospective effect estimation when historical intervention records are completely missing or unreported [1]. It identifies structural upward trends using a mathematical ratio (the $\Delta$ criterion) and tests the theoretical effects of known repair types, ultimately selecting the intervention that maximizes the log-likelihood estimate for that specific structural element [1]. A key strength of this framework is its proven application on a massive real-world dataset of approximately 10,000 bridges in Quebec, allowing for the imputation of missing data across a bounded visual inspection scale [1]. However, a notable constraint is its strict reliance on a limited, predefined set of potential intervention types to successfully calculate and maximize the likelihood [1].

In contrast, the Double Deep Q-Network (DDQN) approach shifts the focus from retrospective estimation to prescriptive maintenance optimization [2]. Rather than deducing missing past interventions from bounded visual inspection scores, the DDQN acts as a reinforcement learning agent that formulates long-run optimal policies over a continuous gamma degradation process [2]. A major stated claim and strength of the DDQN is its ability to operate dynamically without relying on any predefined preventive maintenance thresholds [2].

Furthermore, these frameworks differ significantly in how they conceptualize the physical efficacy of a repair over time. The retrospective Log-Likelihood model estimates a singular, quantifiable mathematical "jump" in asset condition and a subsequent alteration to the deterioration speed based on historical expectations [1]. Conversely, the DDQN framework natively accommodates a novel model of "increasingly imperfect repairs," meaning the agent explicitly accounts for the real-world dynamic where the beneficial effect of an intervention systematically decreases as a system undergoes more repairs over its lifecycle [2]. Ultimately, while the state-space log-likelihood approach serves as a critical mechanism for estimating the effects of unrecorded historical interventions [1], the DDQN agent demonstrates a significant ability to adapt to complex degradation environments and improve long-run operational costs [2].

[^1]: [[sources/2]]
[^2]: [[sources/3]]

[^1]: [[sources/web-2026-01-13-6bf]] [^2]: [[sources/web-2026-01-13-6bf]]

### Gaps

## Unresolved Questions and Limitations in Retrospective Intervention Effect Estimation and Maintenance Optimization

Based on the provided sources, several critical gaps emerge when evaluating the available retrospective estimation and maintenance optimization frameworks against the specific causal inference and narrative generation requirements of the research question.

**Gaps in Coverage and Unanswered Tensions:**

*   **Absence of Formal Econometric Causal Inference Primitives**
    While the research question explicitly queries the use of econometric causal inference tools—such as difference-in-differences, regression discontinuity, double-ML, and target trial emulation—the provided documents do not implement or mention these formal methods for retrospective effect estimation [1]. Instead, the kinematic framework identifies structural upward trends using a mathematical $\Delta$ criterion and estimates the mathematical "jump" in bounded visual inspection scores to deduce historical impacts [1]. The corpus fails to address how these purely physical, state-space parameter estimates might be translated or integrated into formal causal inference libraries like DoWhy, EconML, or CausalML [1, 2].
*   **Omission of LLM Narrative Integration for Policy Decisions**
    The prompt emphasizes the necessity of decision-narrative generation for licensed-professional sign-off, situating "AI narrative as table stakes" atop the probabilistic engine. However, the specific sources detailing retrospective intervention estimation and maintenance optimization completely omit any discussion of Large Language Models or narrative generation [1, 2]. While the Double Deep Q-Network (DDQN) successfully formulates long-run continuous maintenance policies and the kinematic model provides aggregated confidence bands for missing historical data, neither text provides a mechanism to translate these quantitative outputs into structured, board-facing causal narratives [1, 2].
*   **Handling of Novel, Concurrent, or Uncatalogued Interventions**
    The mechanism for imputing missing historical interventions explicitly relies on testing the theoretical effect of predefined, known repair types for a given structural category to maximize the log-likelihood estimate [1]. This explicitly constrained approach leaves a significant gap regarding how the model would behave if an entirely novel or uncatalogued intervention was applied to an asset [1]. Furthermore, the corpus does not explain how the system would accurately disaggregate or estimate effects if multiple distinct interventions were performed simultaneously between two visual inspection dates [1].
*   **Missing Value-of-Information and POMDP Frameworks**
    The research prompt specifically targets the use of Partially Observable Markov Decision Processes (POMDPs) and Bayesian decision theory to establish inspect-repair-replace policies with a quantified "value-of-information." The provided literature advances a Double Deep Q-Network (DDQN) reinforcement learning agent that operates on a continuous gamma degradation process to handle increasingly imperfect repairs [2]. However, the text does not explicitly formulate the problem using POMDPs, nor does it address how to mathematically quantify the value-of-information gained by inspecting the asset prior to executing the RL-generated maintenance policy [2].

[^1]: [[sources/2]]
[^2]: [[sources/3]]

[^1]: [[sources/web-2026-01-13-6bf]] [^2]: [[sources/web-2026-01-13-6bf]]

## Sources cited

- [[sources/web-2026-01-13-6bf]]

## Included works

- [[sources/web-2026-01-13-6bf]]
