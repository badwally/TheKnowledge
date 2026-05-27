---
schema_version: 1
type: concept
slug: approximate-nearest-neighbor-search
canonical_name: Approximate nearest neighbor search
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Approximate nearest neighbor search

## Summary

Approximate nearest neighbor (ANN) search is the operation of retrieving items most similar to a query vector from an embedding index, trading exactness for tractable latency at scale; in agentic memory systems it is the dominant retrieval primitive and the principal source of memory-operation overhead during LLM inference [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Key claims

- ANN is typically implemented through vector databases, where textual information is encoded into vector embeddings and relevance is quantized based on vector similarities [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- The Inverted File (IVF) index is widely used: it partitions vectors into clusters and ranks these clusters by the distance between their centroids and the query, with only the top-nprobe clusters selected for vector-wise search — a tunable accuracy–efficiency trade-off [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- The cluster-selection stage is referred to as coarse search, and the search within selected clusters as fine search; coarse search typically relies on a Flat index or graph-based indexes such as HNSW or Vamana in large-scale settings [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- ANN queries occur repeatedly throughout an agent's step-wise generation, and their latency and accuracy therefore become increasingly critical to the overall performance of modern LLM serving systems [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Most existing vector-database systems fall short for agentic memory: they either optimize only a static index, or rely on batch-oriented updates designed for periodic maintenance in traditional databases, making them ill-suited for highly dynamic, fine-grained memory operations [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Sources

- [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]]

## Related

- [[concepts/agentic-memory]]
- [[concepts/multi-tier-memory-system]]
- [[concepts/scattered-cluster-problem]]
- [[entities/pancake-system]]
