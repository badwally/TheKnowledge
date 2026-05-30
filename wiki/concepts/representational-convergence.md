---
schema_version: 1
type: concept
slug: representational-convergence
canonical_name: Representational Convergence
domains:
- convergent-ai-brain
created_at: '2026-05-30T18:48:08Z'
last_updated: '2026-05-30T18:48:08Z'
draft: true
draft_started_at: '2026-05-30T18:48:08Z'
draft_unresolved_claims: 0
---

# Representational Convergence

## Summary

Representational convergence is the observed phenomenon that different neural networks — trained with varied architectures, objectives, datasets, and even data modalities — are coming to represent data in increasingly similar ways over time [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].

## Key claims

- Convergence spans modalities: vision models and language models, as they scale up, measure distance between datapoints in increasingly similar ways [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- Across 78 vision models with varying architectures, training objectives, and datasets, models with higher transfer performance on VTAB form a tightly clustered set of representations while weaker models exhibit more variable representations [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- Paraphrasing Tolstoy: "all strong models are alike, each weak model is weak in its own way" [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- Alignment increases with model scale and dataset size — Kornblith et al. (2019) and Roeder et al. (2021) report this empirically; Balestriero & Baraniuk (2018) show theoretically that models with similar outputs also have similar internal activations [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- Convergence can extend to weights: models sharing an architecture often converge to the same basin of weights up to permutation (Nagarajan & Kolter 2019; Garipov et al. 2018; Lubana et al. 2023; Ainsworth et al. 2022), enabling separately trained models to be merged (Stoica et al. 2023; Jordan et al. 2022; Wortsman et al. 2022) [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- Cross-modal convergence: a single linear projection suffices to stitch a vision model to an LLM and achieve good VQA/captioning performance (Merullo et al. 2022); auditory models also align with LLMs up to a linear transformation (Ngo & Kim 2024); LLMs trained only on text contain rich visual structural knowledge (Sharma et al. 2024) [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].
- CLIP models — trained with explicit language supervision — exhibit higher language–vision alignment, but this alignment decreases after fine-tuning on ImageNet classification [[sources/pdf-minyoung-huh-2024-the-platonic-representation]].

## Sources

- [[sources/pdf-minyoung-huh-2024-the-platonic-representation]]

## Related

- [[concepts/platonic-representation-hypothesis]]
- [[concepts/representational-alignment]]
- [[concepts/model-stitching]]
- [[concepts/anna-karenina-scenario]]
- [[concepts/foundation-models]]
