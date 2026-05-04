---
type: concept
slug: agentic-memory
canonical_name: Agentic memory
domains:
  - ai-and-agents
---

# Agentic memory

## Summary

Agentic memory is the mechanism by which an LLM-driven agent maintains an external database of essential information — external knowledge, action history, user profile, runtime state, and intermediate results — and retrieves the most relevant items to guide each step of generation, distinguishing it from static-database Retrieval-Augmented Generation (RAG) [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Key claims

- Agent memory differs from prior RAG methods, which rely on a static knowledge database and lack the ability to capture an agent's runtime state, results, and other dynamic information [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- The information stored typically includes external knowledge, action history, and user profile, and the agent must retrieve the most relevant memory items to guide generation throughout LLM inference while dynamically inserting newly generated items for future reference [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- A memory-based agent typically performs three operations: LLM Generation, Memory Search (retrieving items relevant to the current context), and Memory Update (inserting, deleting, or modifying items in the memory store) [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Different agent roles induce different operation patterns: multi-turn dialogue agents search and update at every step, context-summarization agents search and generate for several rounds and then insert a compressed memory item, personalized-generation agents perform a single search with multiple updates, and knowledge retrievers perform search-only workflows [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- In popular memory-based workflows, the memory operational cost grows sharply with memory size, reaching more than 82% of total execution time without performance-oriented optimization [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Agent memory operations inherently introduce requirements for approximate-nearest-neighbor (ANN) queries, typically implemented through embedding vector indexes [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Sources

- [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]]

## Related

- [[concepts/approximate-nearest-neighbor-search]]
- [[concepts/multi-tier-memory-system]]
- [[concepts/intra-agent-locality]]
- [[concepts/step-wise-memory-locality]]
- [[entities/mem-gpt]]
- [[entities/a-mem]]
- [[entities/pancake-system]]
