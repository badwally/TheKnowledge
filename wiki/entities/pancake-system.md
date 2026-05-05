---
type: entity
slug: pancake-system
canonical_name: Pancake
entity_kind: paper
domains:
  - ai-and-agents
---

# Pancake

## Summary

A multi-tier agentic memory management system from UC San Diego that addresses the approximate-nearest-neighbor (ANN) bottleneck in multi-agent LLM serving by unifying multi-level index caching for single agents, coordinated index management across agents, and CPU–GPU collaborative execution; reported to deliver more than 4.29× average end-to-end throughput improvement over existing memory libraries [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Key facts

- Introduced in "Pancake: Hierarchical Memory System for Multi-Agent LLM Serving" (Hu et al., 2026) and described as the first multi-tier memory management system tailored for multi-agent applications [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Unifies three techniques: (i) multi-level index caching for single agents, (ii) coordinated index management across multiple agents, and (iii) collaborative GPU–CPU acceleration [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Models each agent's memory access pattern as a finite-state machine (FSM) with continuous updating and merging, in order to align index cluster construction with the agent's workload [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Uses a hybrid graph that connects multiple agents' indexes into a unified structure, enabling upper-level coarse search through a single graph traversal and recording agent-specific access patterns per cluster to reduce cross-agent search overhead caused by inconsistent access patterns [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Implements CPU–GPU coordinated index management with an insertion buffer and asynchronous transfers to accelerate hotspot cluster computation under low-latency online updates [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Exposes a Python interface that supports operations over arbitrary memory scopes, including different shared and local memory parts; demonstrated in a multi-agent code-generation setup with knowledge, code, and history memories [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Can be directly integrated into agent workflows like Mem-GPT and is compatible with mainstream agentic frameworks such as LangChain and LlamaIndex [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Achieves more than 4.29× average end-to-end throughput improvement over existing memory libraries on realistic agent workloads [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Reduces the memory-operation share of total execution time to an average of 3.2% under large-scale databases, compared with the more than 82% share that memory operations can reach in popular memory-based workflows without such optimization [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Sources

- [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]] — Pancake: Hierarchical Memory System for Multi-Agent LLM Serving (2026)

## Related

- [[entities/zhengding-hu]]
- [[entities/yufei-ding]]
- [[entities/steven-swanson]]
- [[entities/uc-san-diego]]
- [[entities/mem-gpt]]
- [[entities/a-mem]]
- [[concepts/agentic-memory]]
- [[concepts/approximate-nearest-neighbor-search]]
- [[concepts/multi-tier-memory-system]]
- [[concepts/intra-agent-locality]]
- [[concepts/step-wise-memory-locality]]
- [[concepts/scattered-cluster-problem]]
