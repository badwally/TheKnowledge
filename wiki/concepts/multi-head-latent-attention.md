---
schema_version: 1
type: concept
slug: multi-head-latent-attention
canonical_name: Multi-head latent attention (MLA)
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Multi-head latent attention (MLA)

## Summary

Multi-head latent attention (MLA) is an attention variant — used in Kimi K2's ultra-sparse MoE architecture, derived from the design space explored in DeepSeek-V3 — in which key matrices are not fully materialized during inference, breaking compatibility with standard Query-Key Normalization (QK-Norm) and motivating per-component clipping schemes such as QK-Clip [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Key claims

- Kimi K2's base model is a trillion-parameter Mixture-of-Experts transformer that uses an ultra-sparse MoE with multi-head latent attention, similar to DeepSeek-V3 and derived from empirical scaling-law analysis [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- In MLA, key matrices are not fully materialized during inference, which is the specific reason Query-Key Normalization is inapplicable as a stability mechanism for MLA-based models [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- MLA decomposes attention into head-specific components qC and kC, a head-specific rotary qR, and a shared rotary kR; QK-Clip in Kimi K2 applies √η_h scaling to qC and kC, η_h scaling to qR, and leaves kR untouched to avoid effects across heads [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Sources

- [[sources/pdf-kimi-team-2026-kimi-k2-open]]

## Related

- [[concepts/qk-clip]]
- [[concepts/mixture-of-experts]]
- [[entities/kimi-k2]]
