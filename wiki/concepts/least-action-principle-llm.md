---
schema_version: 1
type: concept
slug: least-action-principle-llm
canonical_name: Least-action principle for LLM agent potentials
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Least-action principle for LLM agent potentials

## Summary

A method, proposed by Song, Cao, Luo, and Zhu (2026), for estimating the underlying potential function V_T of an LLM-driven agent by minimizing a global "action" S that integrates a convex violation K(V(f) − V(g)) of the potential's ordering against the LLM's measured transition kernel T(g→f), yielding a variational condition whose solution describes the agent's global cognitive ordering of its state space [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].

## Key claims

- The action is defined as S[V] = ∫_{f∈C} ∫_{g∈C} T(g→f) K(V(f) − V(g)) Df Dg, the global average violation of the potential ordering by the agent's transitions, weighted by the transition kernel [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- The convex violation function chosen in the paper is K(x) = exp(−β x / 2), describing the extent to which a transition from state f to state g violates the ordering of the scalar potential V [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- The most suitable potential function V_T for describing an LLM-based agent in a given state space is defined as the one that minimizes S — the agent's transitions and the potential function are made to agree as much as possible [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- The variational condition δS = 0 is shown to be equivalent to the least-action principle when K(x) is convex (Supplemental Material A) [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- The variational condition is equivalent to the equilibrium condition ∫ T(g→f) K′(V_T(f) − V_T(g)) Dg − ∫ T(f→h) K′(V_T(h) − V_T(f)) Dh = 0 holding for all states f in the state space [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- For equilibrium systems satisfying detailed balance, substituting the detailed-balance form into the equilibrium condition recovers the same V_T, so the least-action principle yields a consistent estimate of the underlying potential function in those cases (Supplemental Material B) [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- When transitions are completely ordered — V(f) > V(g) whenever T(g→f) > 0 — V serves as a Lyapunov function for the agent's dynamics; the least-action principle thus contains both deterministic-planning and equilibrium regimes as limiting cases [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].

## Sources

- [[sources/pdf-zhuo-yang-2026-detailed-balance-in]]

## Related

- [[concepts/detailed-balance-in-llm-agents]]
- [[concepts/potential-function-llm]]
- [[concepts/macroscopic-dynamics-of-llms]]
- [[entities/zhuo-yang-song]]
