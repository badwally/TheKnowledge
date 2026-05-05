---
type: concept
slug: multi-tier-memory-system
canonical_name: Multi-tier memory system
domains:
  - ai-and-agents
---

# Multi-tier memory system

## Summary

A multi-tier memory system organizes agentic memory into multiple coordinated layers — a workload-aware single-agent index, a cross-agent coordinated index, and a CPU–GPU execution tier — to handle the simultaneous pressure of large-scale storage, frequent updates, and multiple coexisting agents in LLM serving; introduced as Pancake's core architectural pattern [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Key claims

- Pancake is described as the first multi-tier memory management system tailored for multi-agent applications, exploiting agent workload characteristics across three tiers: single-agent update strategy, multi-agent cluster construction, and dynamic CPU–GPU collaborative execution [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- At the single-agent tier, the system exploits both intra-agent and inter-request locality through a multi-level cache index that progressively promotes related vectors to upper levels, improving search ordering and enabling early termination [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- At the multi-agent tier, the system addresses the inefficiency of maintaining separate per-agent indexes with a hybrid graph that connects multiple agents' indexes into a unified structure, enabling upper-level coarse search through a single graph traversal [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- At the execution tier, the system implements CPU–GPU coordinated index management with an insertion buffer and asynchronous transfers, motivated by the observation that frequent memory updates make static caching techniques infeasible and that the coexistence of large memory bases with LLM inference engines severely restricts available GPU memory [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Sources

- [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]]

## Related

- [[concepts/agentic-memory]]
- [[concepts/approximate-nearest-neighbor-search]]
- [[concepts/intra-agent-locality]]
- [[concepts/step-wise-memory-locality]]
- [[entities/pancake-system]]
