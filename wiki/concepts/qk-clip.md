---
type: concept
slug: qk-clip
canonical_name: QK-Clip
domains:
  - ai-and-agents
---

# QK-Clip

## Summary

QK-Clip is a weight-clipping mechanism, introduced in the Kimi K2 technical report, that explicitly constrains attention-logit growth by rescaling the query and key projection weights post-update whenever the per-head maximum logit exceeds a target threshold τ; it is the stability-enhancing component that turns the token-efficient Muon optimizer into MuonClip [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Key claims

- For each attention head h with input X and projections Q^h = X W_q^h, K^h = X W_k^k, QK-Clip tracks the per-head max logit S^h_max = max over a batch of (1/√d) Q^h K^h⊤; whenever S^h_max > τ, it rescales W_q^h and W_k^h so the next forward step's logits are bounded by τ [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- QK-Clip does not alter the forward or backward computation in the current step; the max logit is used only as a guiding signal to determine the magnitude of the post-update weight rescaling [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- A naive variant scales all heads uniformly by η = min(1, τ / S_max); the Kimi Team instead applies per-head scaling η_h = min(1, τ / S^h_max), motivated by the empirical observation that only a small subset of heads exhibits exploding logits [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- For multi-head latent attention (MLA), QK-Clip is applied only to unshared components: head-specific qC and kC are each scaled by √η_h, the head-specific rotary qR is scaled by η_h, while the shared rotary kR is left untouched to avoid effects across heads [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- QK-Clip is preferred to existing alternatives in this regime: logit soft-cap clips after dot products are computed and so allows them to grow excessively before capping, while Query-Key Normalization (QK-Norm) does not apply to MLA because its key matrices are not fully materialized during inference [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- For Kimi K2, QK-Clip was applied with τ = 100; the max attention logit rapidly rose to the cap and then decayed to a stable range after roughly 30% of training steps, demonstrating effective regulation without ongoing intervention [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Sources

- [[sources/pdf-kimi-team-2026-kimi-k2-open]]

## Related

- [[concepts/muonclip-optimizer]]
- [[concepts/muon-optimizer]]
- [[concepts/multi-head-latent-attention]]
- [[entities/kimi-k2]]
