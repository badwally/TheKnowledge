---
schema_version: 1
type: concept
slug: compute-bound-execution
canonical_name: Compute-bound vs memory-bound execution
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Compute-bound vs memory-bound execution

## Summary

A distinction from the roofline performance model: a kernel is compute-bound when its execution is limited by arithmetic throughput (FLOP/s) and memory-bound when limited by memory bandwidth; large-scale text-to-video transformer inference on modern GPUs is predominantly compute-bound, which is the foundational assumption behind the analytical model in "Video Killed the Energy Budget" [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Key claims

- On modern GPUs such as the NVIDIA H100, inference kernels can be either compute-bound (limited by arithmetic throughput) or memory-bound (limited by memory bandwidth), following the roofline formulation of Williams et al. (2009) [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Profiling of WAN2.1 inference shows that its main operators — self-attention, cross-attention, MLPs, and VAE convolutions — are predominantly compute-bound, with saturated GPU utilization and negligible CPU-induced idle time [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Under a compute-bound model, total latency D_total ≈ F_total / (µ · π_peak), where π_peak is the GPU's peak dense throughput and µ is an empirical efficiency capturing hardware under-utilization (tile misalignment, kernel overheads, memory-bound ops) and modeling approximations [[sources/pdf-julien-delavande-2025-video-killed-the]].
- For WAN2.1 on an H100 (π_peak = 989 TFLOP/s in dense BF16), the calibrated efficiency is µ ≈ 0.456 with R² = 0.998, consistent with the 30–63% sustained FLOP utilization range reported elsewhere for large-scale transformer inference on H100s [[sources/pdf-julien-delavande-2025-video-killed-the]].
- On the H100, WAN2.1's self-attention and MLP blocks become compute-bound above sequence lengths of ω ≈ 295 and ω ≈ 590 respectively; since typical T2V configurations operate at ω in the 10⁴–10⁵ range, these blocks are firmly compute-bound in practice [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Sources

- [[sources/pdf-julien-delavande-2025-video-killed-the]]

## Related

- [[concepts/diffusion-transformer]]
- [[concepts/text-to-video-generation]]
- [[concepts/t2v-scaling-laws]]
- [[concepts/generative-ai-energy-footprint]]
