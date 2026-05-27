---
schema_version: 1
type: concept
slug: multi-principal-decision-problem
canonical_name: Multi-Principal Decision Problem (LLM Agents)
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Multi-Principal Decision Problem (LLM Agents)

## Summary

A formalization, introduced by Yang et al. (2026), in which a single LLM-based agent jointly serves a set of users U = {u_1, ..., u_N} who each act as independent principals with distinct utility functions, authority personas, and private contexts, requiring the agent to reason over potentially conflicting objectives under access-control constraints rather than to optimize a single utility [[sources/pdf-shu-yang-2026-multi-user-large]].

## Key claims

- Each user u_i is characterized by an authority persona (or privilege level) p_i, a private context C_i, and a user-specific utility function U_i capturing task success, privacy preservation, and preference satisfaction [[sources/pdf-shu-yang-2026-multi-user-large]].
- The agent observes a selectively shared context C_share, obtained from {C_i} under an access-control policy, and outputs an action a (a response, tool call, or information disclosure decision) [[sources/pdf-shu-yang-2026-multi-user-large]].
- The interaction is modeled as a multi-objective decision problem in which the agent maximizes a weighted social objective max_a Σ_i w_i U_i(a; C_i, p_i), where w_i ≥ 0 is an externally specified priority weight that can be set based on each user's role or authority level — for example, assigning higher weight to a CEO or manager than to an intern [[sources/pdf-shu-yang-2026-multi-user-large]].
- The optimization is further subject to access-control constraints that restrict which information from a user's private context C_i may be revealed through the agent's action a [[sources/pdf-shu-yang-2026-multi-user-large]].
- The formulation aggregates user-specific desiderata into a social-welfare-like objective, citing Bakker et al. (2022) and Keeney and Kirkwood (1975) as a precedent for treating cross-user trade-offs as utility aggregation [[sources/pdf-shu-yang-2026-multi-user-large]].
- The agent in this setting is no longer a simple delegate of one principal but a coordinator that must arbitrate among multiple principals in a consistent and scalable manner [[sources/pdf-shu-yang-2026-multi-user-large]].
- The authors note that while real-world deployments may rely on more complex, implicit, or learned mechanisms for resolving conflicts, this abstraction allows clear reasoning about the coordination and trade-offs required in multi-user settings [[sources/pdf-shu-yang-2026-multi-user-large]].

## Sources

- [[sources/pdf-shu-yang-2026-multi-user-large]]

## Related

- [[concepts/multi-user-llm-agents]]
- [[concepts/principal-agent-problem]]
- [[concepts/selective-context-visibility]]
- [[entities/michiel-bakker]]
