---
type: concept
slug: diffusion-transformer
canonical_name: Diffusion Transformer (DiT)
domains:
  - ai-and-agents
---

# Diffusion Transformer (DiT)

## Summary

A transformer-based denoiser used as the central component of modern latent text-to-video diffusion models; in WAN2.1-T2V-1.3B the DiT performs the bulk of spatio-temporal denoising and dominates inference FLOPs, with self-attention, cross-attention, and MLP blocks scaling with the latent token length set by spatial resolution and temporal frames [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Key claims

- In modern latent text-to-video diffusion systems such as WAN2.1, a large DiT performs the bulk of spatio-temporal denoising, sitting between a text encoder/timestep MLP for conditioning and a VAE decoder that maps latent tensors back to pixels [[sources/pdf-julien-delavande-2025-video-killed-the]].
- The DiT token length ω in WAN2.1 grows linearly with spatial resolution H, W and temporal length T, following ω = (T/4) · ⌈H/16⌉ · ⌈W/16⌉ + 1 [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Per denoising step, an N-layer DiT contributes self-attention FLOPs of N(8ωd² + 4ω²d), cross-attention FLOPs of N(4ωd² + 4md² + 4ωmd), and MLP FLOPs of N(4fωd²), where d is hidden size, f is the MLP expansion factor, and m is the text-conditioning length [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Because attention contributes O(ω²) FLOPs while ω grows linearly with H, W, and T, DiT inference scales quadratically with spatial and temporal dimensions and linearly with denoising steps [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Empirically, the DiT dominates total inference cost so completely that VAE-decoder contributions remain minor across the studied range, and the predicted quadratic regimes hold across configurations [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Sources

- [[sources/pdf-julien-delavande-2025-video-killed-the]]

## Related

- [[concepts/text-to-video-generation]]
- [[concepts/compute-bound-execution]]
- [[concepts/t2v-scaling-laws]]
- [[entities/wan21-t2v]]
