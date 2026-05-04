---
type: concept
slug: generative-ai-energy-footprint
canonical_name: Generative AI energy footprint
domains:
  - ai-and-agents
---

# Generative AI energy footprint

## Summary

The energy and carbon costs of running generative AI inference workloads; a growing field of scholarship that began with training-cost studies (Strubell et al., 2019) and has shifted toward inference, where video generation now appears as the most expensive modality measured per output [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Key claims

- The environmental costs of machine learning are a new but growing field of scholarship, beginning with Strubell et al. (2019), the first study to quantify the carbon footprint of training a large language model [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Subsequent work expanded coverage of ML model types and influencing factors (Patterson et al. 2021; Luccioni et al. 2022; Gupta et al. 2021; Wu et al. 2022), and recent work has shifted increasingly toward inference given the ubiquity of deployed ML models [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Luccioni et al. (2024) carried out the first large-scale study of energy and carbon costs across different ML tasks and approaches, including image generation [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Li et al. (2024), studying the Open-Sora model on 2-second 240p videos, found that video generation is significantly more energy-intensive than text generation, that the primary source of emissions stems from iterative diffusion denoising, and that energy requirements scale near-quadratically with video resolution [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Because sustained GPU power remains close to its maximum (≈700 W for an H100) during inference, total energy E_total ≈ P_max · D_total, so energy and latency scale proportionally for compute-bound text-to-video workloads [[sources/pdf-julien-delavande-2025-video-killed-the]].
- For WAN2.1-T2V-1.3B on an H100, the GPU accounts for 80–90% of total energy consumption during inference, dominating CPU and RAM contributions [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Sources

- [[sources/pdf-julien-delavande-2025-video-killed-the]]

## Related

- [[concepts/text-to-video-generation]]
- [[concepts/compute-bound-execution]]
- [[concepts/t2v-scaling-laws]]
- [[entities/codecarbon]]
- [[entities/sasha-luccioni]]
