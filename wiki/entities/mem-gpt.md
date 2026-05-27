---
schema_version: 1
type: entity
slug: mem-gpt
canonical_name: Mem-GPT
entity_kind: paper
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Mem-GPT

## Summary

A memory-based agent framework that maintains its own memory implementation; cited by Hu et al. (2026) as a representative existing memory-based agent that emphasizes functional support over performance, and as a target system into which Pancake can be directly integrated [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Key facts

- Identified by Hu et al. (2026) as one of the existing memory-based agents that provide their own memory implementation, alongside A-Mem [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Characterized as emphasizing functionality and relying on suboptimal indexing and searching implementations, with query latency reaching more than 99% of end-to-end runtime as memory size grows [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Pancake is reported to be directly integrable into agent workflows like Mem-GPT, exposing its multi-tier memory primitives through Mem-GPT's interface [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Sources

- [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]]

## Related

- [[entities/pancake-system]]
- [[entities/a-mem]]
- [[concepts/agentic-memory]]
