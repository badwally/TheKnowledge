---
id: arxiv-2009.04547
type: arxiv
title: Optimal Inspection and Maintenance Planning for Deteriorating Structural Components
  through Dynamic Bayesian Networks and Markov Decision Processes
url: https://arxiv.org/abs/2009.04547
authors:
- P. G. Morato
- K. G. Papakonstantinou
- C. P. Andriotis
- J. S. Nielsen
- P. Rigo
ingested_at: '2026-05-11T21:31:32Z'
content_hash: sha256:52e22bfa74fdd24b2f9a89272a0a96b97857895a8452607e20c09fced4c4225b
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2009.04547'
  categories:
  - cs.AI
  - eess.SY
  - stat.AP
  doi: 10.1016/j.strusafe.2021.102140
  primary_category: cs.AI
  journal_ref: Structural Safety, Volume 94, 2022,
  comment: ''
  abstract_only: true
published_at: '2020-09-09'
---
Civil and maritime engineering systems, among others, from bridges to offshore platforms and wind turbines, must be efficiently managed as they are exposed to deterioration mechanisms throughout their operational life, such as fatigue or corrosion. Identifying optimal inspection and maintenance policies demands the solution of a complex sequential decision-making problem under uncertainty, with the main objective of efficiently controlling the risk associated with structural failures. Addressing this complexity, risk-based inspection planning methodologies, supported often by dynamic Bayesian networks, evaluate a set of pre-defined heuristic decision rules to reasonably simplify the decision problem. However, the resulting policies may be compromised by the limited space considered in the definition of the decision rules. Avoiding this limitation, Partially Observable Markov Decision Processes (POMDPs) provide a principled mathematical methodology for stochastic optimal control under uncertain action outcomes and observations, in which the optimal actions are prescribed as a function of the entire, dynamically updated, state probability distribution. In this paper, we combine dynamic Bayesian networks with POMDPs in a joint framework for optimal inspection and maintenance planning, and we provide the formulation for developing both infinite and finite horizon POMDPs in a structural reliability context. The proposed methodology is implemented and tested for the case of a structural component subject to fatigue deterioration, demonstrating the capability of state-of-the-art point-based POMDP solvers for solving the underlying planning optimization problem. Within the numerical experiments, POMDP and heuristic-based policies are thoroughly compared, and results showcase that POMDPs achieve substantially lower costs as compared to their counterparts, even for traditional problem settings.
