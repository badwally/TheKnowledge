---
type: entity
slug: wan21-t2v
canonical_name: WAN2.1-T2V
entity_kind: paper
domains:
  - ai-and-agents
---

# WAN2.1-T2V

## Summary

Open-source text-to-video diffusion model released by Wan et al. (2025); used as the reference architecture for the latency and energy analysis in "Video Killed the Energy Budget," and reported as the most-downloaded text-to-video model on the Hugging Face Hub at the time of that study [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Key facts

- Released in two scales — WAN2.1-T2V-1.3B and WAN2.1-T2V-14B — both with default generation settings of 50 denoising steps, 720×1280 resolution, 81 frames, and 15 FPS [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Architecture is a latent text-to-video diffusion system: a pretrained text encoder for conditioning, a timestep embedding MLP that injects the diffusion step index, a large Diffusion Transformer (DiT) performing the bulk of spatio-temporal denoising, and a VAE decoder mapping latent tensors back to pixel space [[sources/pdf-julien-delavande-2025-video-killed-the]].
- WAN2.1-T2V-1.3B is the specific reference architecture used to derive the compute-bound analytical model in the paper, decomposing FLOPs by operator (self-attention, cross-attention, MLP, VAE, text encoder, timestep MLP) [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Reported as the most-downloaded text-to-video model on the Hugging Face Hub at the time of writing, motivating its selection for in-depth study [[sources/pdf-julien-delavande-2025-video-killed-the]].
- On an NVIDIA H100, WAN2.1-T2V exhibits an empirical sustained-throughput efficiency µ ≈ 0.456 (R² = 0.998), consistent with the 30–63% sustained FLOP utilization range reported elsewhere for large-scale transformer inference on H100s [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Empirical scaling on WAN2.1-T2V-1.3B confirms quadratic growth of latency and energy with spatial resolution and with temporal length, and linear growth with the number of denoising steps [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Sources

- [[sources/pdf-julien-delavande-2025-video-killed-the]]

## Related

- [[entities/hugging-face]]
- [[concepts/text-to-video-generation]]
- [[concepts/diffusion-transformer]]
- [[concepts/compute-bound-execution]]
- [[concepts/t2v-scaling-laws]]
- [[concepts/generative-ai-energy-footprint]]
