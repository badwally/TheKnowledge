---
schema_version: 1
type: concept
slug: step-wise-memory-locality
canonical_name: Step-wise memory locality
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Step-wise memory locality

## Summary

Step-wise memory locality is the empirical observation, in tool-augmented and multi-step agentic workflows, that memory items belonging to the same reasoning step across different requests cluster together — exhibiting higher similarity than intra-request and intra-agent items — and therefore that effective indexing must group memory by reasoning step rather than only by agent identity [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Key claims

- In tool-augmented agents, the planning, tool-calling, and reflection steps across different requests tend to access similar regions of memory, so step-wise grouping captures structure that per-agent grouping misses [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Memory items belonging to the same reasoning step across different requests demonstrate higher similarity than intra-request or intra-agent similarity [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- 2-dimensional PCA visualization of memory items in a tool-calling dataset with 100 requests reveals three clusters, each corresponding to an individual step of the workflow [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Step-wise organization induces frequent transitions across multiple clusters, which makes a single dedicated per-agent cluster semantically unrepresentative and degrades both accuracy and search efficiency in complex workflows [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Pancake aims to optimize agent memory management considering both intra-agent and step-wise locality jointly [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Sources

- [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]]

## Related

- [[concepts/intra-agent-locality]]
- [[concepts/multi-tier-memory-system]]
- [[entities/pancake-system]]
