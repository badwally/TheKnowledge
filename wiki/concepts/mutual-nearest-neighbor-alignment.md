---
schema_version: 1
type: concept
slug: mutual-nearest-neighbor-alignment
canonical_name: Mutual Nearest-Neighbor Alignment Metric
domains:
- convergent-ai-brain
created_at: '2026-05-30T18:48:09Z'
last_updated: '2026-05-30T18:48:09Z'
draft: true
draft_started_at: '2026-05-30T18:48:09Z'
draft_unresolved_claims: 0
---

# Mutual Nearest-Neighbor Alignment Metric

## Summary

The mutual nearest-neighbor metric measures the mean intersection of the k-nearest-neighbor sets induced by two kernels K_1 and K_2, normalized by k [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].

## Key claims

- The metric is a variant of those proposed in Park et al. (2024), Klabunde et al. (2023), and Oron et al. (2017) [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- Huh et al. use this metric as the primary alignment measure throughout their experiments — including the 78-vision-model VTAB study and the language–vision alignment study on the WIT (Wikipedia caption) dataset [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- The exact definition is given in Appendix A of the paper; comparisons with alternative alignment metrics (CKA, SVCCA) appear in Appendix B [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].

## Sources

- [[sources/pdf-minyoung-huh-2024-the-platonic-representation]]

## Related

- [[concepts/representational-alignment]]
- [[concepts/representational-convergence]]
- [[concepts/platonic-representation-hypothesis]]
