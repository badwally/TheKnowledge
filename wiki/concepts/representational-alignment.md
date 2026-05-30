---
schema_version: 1
type: concept
slug: representational-alignment
canonical_name: Representational Alignment
domains:
- convergent-ai-brain
created_at: '2026-05-30T18:48:08Z'
last_updated: '2026-05-30T18:48:08Z'
draft: true
draft_started_at: '2026-05-30T18:48:08Z'
draft_unresolved_claims: 0
---

# Representational Alignment

## Summary

Representational alignment is the measurement of similarity between the similarity structures induced by two neural-network representations — formally, a similarity metric defined over kernels [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].

## Key claims

- A representation is defined as a function f: X → R^n that assigns a feature vector to each input in a data domain X [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- A kernel K: X × X → R characterizes how a representation measures distance/similarity between datapoints, with K(x_i, x_j) = ⟨f(x_i), f(x_j)⟩ [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- A kernel-alignment metric m: K × K → R measures how similar the distance measure induced by one representation is to that induced by another [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- Established kernel-alignment metrics include Centered Kernel Alignment (CKA; Kornblith et al. 2019), SVCCA (Raghu et al. 2017), and nearest-neighbor metrics (Klabunde et al. 2023) [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- Kernels are commonly used to assess representations because they capture relative structure among data samples — the same signal that drives many ML algorithms (Aronszajn 1950; Smola & Schölkopf 1998) [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].

## Sources

- [[sources/pdf-minyoung-huh-2024-the-platonic-representation]]

## Related

- [[concepts/mutual-nearest-neighbor-alignment]]
- [[concepts/representational-convergence]]
- [[concepts/platonic-representation-hypothesis]]
- [[concepts/model-stitching]]
