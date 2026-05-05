---
type: concept
slug: t2v-scaling-laws
canonical_name: Text-to-video scaling laws
domains:
  - ai-and-agents
---

# Text-to-video scaling laws

## Summary

Empirical and analytical relationships predicting how the latency and energy of text-to-video diffusion inference grow with spatial resolution, temporal length, and denoising steps; the dominant regimes are quadratic in spatial and temporal dimensions and linear in steps, validated on WAN2.1-T2V-1.3B [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Key claims

- A compute-bound analytical model derived for WAN2.1-T2V predicts that latency and energy grow quadratically in the spatial dimensions H, W and the temporal length T, because the DiT token length ω grows linearly in those dimensions while attention contributes O(ω²) FLOPs [[sources/pdf-julien-delavande-2025-video-killed-the]].
- The same model predicts linear scaling in the number of denoising steps S, since each step applies the same sequence of N transformer layers with cost independent of S [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Auxiliary components contribute negligibly: the text encoder runs once per video, the timestep MLP adds only a small per-step overhead, and the VAE decoder scales linearly with voxel count T·H·W and is quickly dominated by the quadratic DiT cost [[sources/pdf-julien-delavande-2025-video-killed-the]].
- The predictions were validated empirically on WAN2.1-T2V-1.3B by sweeping spatial resolution from 256×256 to 3520×1980, frames from 4 to 100 (in increments of 4), and denoising steps from 1 to 200, with strong agreement between theory and measurement and only modest deviations at the highest resolutions [[sources/pdf-julien-delavande-2025-video-killed-the]].
- The text encoder always pads or truncates prompts to a fixed length of 512 tokens, so the specific prompt does not affect runtime — only structural parameters (resolution, frames, steps) drive scaling [[sources/pdf-julien-delavande-2025-video-killed-the]].
- The findings corroborate Li et al. (2024) on Open-Sora, which independently observed near-quadratic scaling of energy with video resolution [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Sources

- [[sources/pdf-julien-delavande-2025-video-killed-the]]

## Related

- [[concepts/text-to-video-generation]]
- [[concepts/diffusion-transformer]]
- [[concepts/compute-bound-execution]]
- [[concepts/generative-ai-energy-footprint]]
- [[entities/wan21-t2v]]
