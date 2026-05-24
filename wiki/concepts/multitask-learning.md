---
type: concept
slug: multitask-learning
canonical_name: Multitask Learning
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T19:07:43Z'
draft_unresolved_claims: 1
---

# Multitask Learning

## Summary

Multitask learning is an inference strategy in which a set of related predictive tasks are learned jointly so that statistical structure shared across the tasks improves estimation for each, particularly for tasks with limited data.

## Key claims

- A hierarchical Bayesian formulation of multitask learning learns a set of correlated functions over an engineering fleet in a combined inference, producing a population model whose parameters are coupled across asset sub-groups [[sources/arxiv-2204.12404]].
- In the Bull et al. framework, multitask learning was applied to two distinct fleet problems: survival analysis of a truck fleet and power prediction in a wind farm, demonstrating the same hierarchical machinery generalises across asset classes [[sources/arxiv-2204.12404]].
- Multitask learning configured hierarchically allows groups with incomplete data to automatically borrow statistical strength from data-rich groups, which is the mechanism by which the joint inference improves per-task estimates [[sources/arxiv-2204.12404]].
- Domain expertise constrains the multitask model by defining the sub-group structure (use-type, component, operating condition) and the prior distributions, rather than letting the model discover clusters from data alone [[sources/arxiv-2204.12404]].

## Sources

- [[sources/arxiv-2204.12404]]

## Related

- [[concepts/hierarchical-bayesian-modelling]]
- [[concepts/bayesian-transfer-learning]]
- [[concepts/partial-pooling]]

