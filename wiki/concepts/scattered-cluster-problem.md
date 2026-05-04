---
type: concept
slug: scattered-cluster-problem
canonical_name: Scattered cluster problem
domains:
  - ai-and-agents
---

# Scattered cluster problem

## Summary

The scattered cluster problem is the failure mode of in-place insertion in IVF-style vector indexes whereby new vectors inserted under interleaved small-batch agent workloads are dispersed across many clusters despite strong semantic coherence — a consequence of high-dimensional distance concentration that degrades both search efficiency and recall in agentic memory [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Key claims

- Existing dynamic vector databases typically adopt in-place inserts with periodic updates: new vectors are inserted directly into the nearest clusters by centroid distance, with reconstruction triggered only when cluster size or semantic shift reaches a threshold — effective for large-batch scenarios but suboptimal under interleaved small-batch search and insert [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Across 100 requests from several agent datasets, memory items from the same agent are dispersed into up to 175 clusters under in-place insertion, with 38%–100% of these clusters being accessed with frequency less than 5% [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- The dispersion stems from the high-dimensional shell effect: points concentrate near the surface of a hypersphere, causing small semantic variations to translate into large differences in centroid distance calculations, so even highly related memory items may be inserted into different clusters [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].
- Scattered cluster assignments cause two distinct degradations: (i) efficiency loss from scanning a larger number of clusters to retrieve semantically related items, performing extra computation over mostly irrelevant vectors, and (ii) recall loss because items in such scattered clusters become harder to locate by centroid distance and their clusters may be eliminated during the coarse search stage [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]].

## Sources

- [[sources/pdf-zhengding-hu-2026-pancake-hierarchical-memory]]

## Related

- [[concepts/approximate-nearest-neighbor-search]]
- [[concepts/intra-agent-locality]]
- [[concepts/multi-tier-memory-system]]
- [[entities/pancake-system]]
