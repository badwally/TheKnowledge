---
type: concept
slug: mixture-of-experts
canonical_name: Mixture-of-Experts (MoE)
domains:
  - ai-and-agents
---

# Mixture-of-Experts (MoE)

## Summary

Mixture-of-Experts (MoE) is a sparse-transformer pattern (originating in Shazeer et al.) in which only a small fraction of total parameters is activated for any given input, allowing very large total parameter counts while keeping per-token compute bounded; Kimi K2 is one of the largest open-source instantiations, with 1.04 trillion total parameters and 32 billion activated per token under an ultra-sparse design [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Key claims

- Kimi K2 is a 1.04 trillion-parameter Mixture-of-Experts large language model with 32 billion activated parameters [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Kimi K2's architecture is described as an "ultra-sparse MoE with multi-head latent attention," with topology choices derived from empirical scaling-law analysis [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- The Kimi Team also reports a mid-scale MoE configuration of 9B activated / 53B total parameters used to study Muon-induced training instability before scaling to K2 [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Sources

- [[sources/pdf-kimi-team-2026-kimi-k2-open]]

## Related

- [[concepts/multi-head-latent-attention]]
- [[concepts/transformer-architecture]]
- [[entities/kimi-k2]]
