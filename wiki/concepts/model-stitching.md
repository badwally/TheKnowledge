---
schema_version: 1
type: concept
slug: model-stitching
canonical_name: Model Stitching
domains:
- convergent-ai-brain
created_at: '2026-05-30T18:48:10Z'
last_updated: '2026-05-30T18:48:10Z'
draft: true
draft_started_at: '2026-05-30T18:48:10Z'
draft_unresolved_claims: 0
---

# Model Stitching

## Summary

Model stitching is a technique for measuring representational similarity by integrating an intermediate representation from one neural network into another via a learned affine stitching layer, then evaluating whether the combined model retains task performance [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].

## Key claims

- Formally: given f = f_1 ∘ … ∘ f_n and g = g_1 ∘ … ∘ g_m, an intermediate representation from f at layer k is passed through a learned affine stitching layer h into g, producing F = f_1 ∘ … ∘ f_k ∘ h ∘ g_{k+1} ∘ … ∘ g_m; good performance of F indicates compatible representations at layer k up to the transform h [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- Introduced by Lenc & Vedaldi (2015), who showed that (i) a vision model trained on ImageNet can be aligned with one trained on Places-365 while maintaining good performance and (ii) early convolutional layers are more interchangeable than later layers [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- Bansal et al. (2021) extended stitching to show that self-supervised models align closely with their supervised counterparts [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- Moschella et al. (2022) demonstrated "zero-shot" model stitching without learning a stitching layer, showing that an encoder trained in one language (e.g., English) can be used with a decoder in another (e.g., French) [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- Cross-modal: Merullo et al. (2022) showed a single linear projection suffices to stitch a vision model to an LLM for good VQA/captioning performance; Koh et al. (2023) showed linear stitching also works in the opposite direction (text inputs to visual outputs) [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].

## Sources

- [[sources/pdf-minyoung-huh-2024-the-platonic-representation]]

## Related

- [[concepts/representational-convergence]]
- [[concepts/representational-alignment]]
- [[concepts/platonic-representation-hypothesis]]
