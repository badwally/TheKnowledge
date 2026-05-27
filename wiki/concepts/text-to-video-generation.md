---
schema_version: 1
type: concept
slug: text-to-video-generation
canonical_name: Text-to-video generation
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Text-to-video generation

## Summary

A class of generative AI systems that synthesize high-fidelity, temporally coherent video clips from natural-language prompts; in the open-source ecosystem these are typically latent diffusion systems whose inference cost is dominated by a Diffusion Transformer iterating over many denoising steps [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Key claims

- Recent advances in text-to-video (T2V) generation have produced systems that synthesize high-fidelity, temporally coherent clips from natural-language prompts; proprietary examples include OpenAI's Sora and DeepMind's Veo, while a fast-growing open-source ecosystem is closing the gap with models that can run on commodity GPUs [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Generating even a few seconds of coherent video typically requires dozens of denoising steps, high spatial resolutions, and hundreds of frames, leading to substantial energy consumption and long inference times [[sources/pdf-julien-delavande-2025-video-killed-the]].
- T2V evaluations have historically emphasized perceptual metrics such as sample fidelity, FID scores, and motion smoothness, while largely overlooking latency and energy efficiency [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Modern open-source T2V systems share a common latent-diffusion architecture: a pretrained text encoder for conditioning, a timestep embedding MLP, a large Diffusion Transformer for spatio-temporal denoising, and a VAE decoder mapping latent tensors back to pixel space [[sources/pdf-julien-delavande-2025-video-killed-the]].
- The paper benchmarks six diverse open-source T2V models — AnimateDiff (lightweight motion-layer diffusion), CogVideoX-2b/5b (cascaded base+refiner), LTX-Video-0.9.7-dev (autoregressive temporal modeling), Mochi-1-preview (large-scale diffusion optimized for motion realism), and WAN2.1-T2V-1.3B/14B (high-resolution latent diffusion with DiT backbone) — under default generation settings [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Prior work on Open-Sora (Li et al., 2024) found that video generation is significantly more energy-intensive than text generation, that the primary source of emissions is iterative diffusion denoising, and that energy requirements scale near-quadratically with video resolution [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Sources

- [[sources/pdf-julien-delavande-2025-video-killed-the]]

## Related

- [[concepts/diffusion-transformer]]
- [[concepts/compute-bound-execution]]
- [[concepts/t2v-scaling-laws]]
- [[concepts/generative-ai-energy-footprint]]
- [[entities/wan21-t2v]]
- [[entities/hugging-face]]
