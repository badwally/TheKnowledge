---
schema_version: 1
type: concept
slug: graph-neural-networks-pavement
canonical_name: Graph neural networks for pavement deterioration modeling
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T21:00:25Z'
draft_unresolved_claims: 2
created_at: '2026-05-20T21:18:17Z'
last_updated: '2026-05-20T21:18:17Z'
---

# Graph neural networks for pavement deterioration modeling

## Summary

Graph neural networks (GNNs) are deep-learning models that operate over graph-structured data. Applied to pavement deterioration modeling, they treat the road network as a graph so that the prediction of a pavement segment's future condition can leverage information about the structure and condition of neighboring segments rather than treating each segment in isolation.

## Key claims

- GNNs are introduced into pavement performance modeling specifically because of their ability to easily and directly exploit the rich structural information in the road network [[sources/arxiv-2508.02749]].
- Incorporating the spatial dependence of a road network into pavement deterioration modeling via a GNN is presented as a way to improve over models that ignore network structure [[sources/arxiv-2508.02749]].
- In a study using more than half a million pavement condition observations from the Texas Department of Transportation's PMIS, GNN-based pavement deterioration prediction models perform better when the spatial relationship is considered, according to comparison results reported by Gao, Yu, and Lu [[sources/arxiv-2508.02749]].

## Sources

- [[sources/arxiv-2508.02749]]

## Related

- [[concepts/spatial-structure-road-network]]
- [[concepts/pavement-deterioration-modeling]]
- [[entities/pavement-deterioration-gnn-paper]]
- [[entities/pmis]]
