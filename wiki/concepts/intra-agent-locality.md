---
schema_version: 1
type: concept
slug: intra-agent-locality
canonical_name: Intra-agent locality
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Intra-agent locality

## Summary

Intra-agent locality is the empirical observation that requests within a single agentic workflow insert memory items that remain highly coherent across steps and across requests of the same agent — a property Pancake exploits by clustering each agent's memory together to mitigate the scattered-cluster problem of in-place insertion [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Key claims

- Across requests of the same agent, the distances between each memory item and (i) the centroid of the memory items in the request and (ii) the aggregated centroid of all the agent's memory items are both substantially smaller than for cross-agent items [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- A naive solution that maintains a dedicated cluster per agent works for simple workflows but is insufficient to capture the step-wise structures observed in more complicated multi-tool / multi-step agentic scenarios [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Pancake explicitly incorporates intra-agent and inter-request locality into index construction and maintenance, using a multi-level cache index that progressively promotes related vectors to upper levels [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Sources

- [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]]

## Related

- [[concepts/step-wise-memory-locality]]
- [[concepts/scattered-cluster-problem]]
- [[concepts/multi-tier-memory-system]]
- [[entities/pancake-system]]
