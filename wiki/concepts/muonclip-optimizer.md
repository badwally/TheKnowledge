---
type: concept
slug: muonclip-optimizer
canonical_name: MuonClip optimizer
domains:
  - ai-and-agents
---

# MuonClip optimizer

## Summary

MuonClip is an optimizer introduced by the Kimi Team that combines the token-efficient Muon optimizer (with weight decay and consistent update RMS scaling) with a novel weight-clipping mechanism, QK-Clip, that bounds attention-logit growth in order to make Muon training stable at trillion-parameter scale [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Key claims

- MuonClip is defined as Muon plus weight decay, plus consistent RMS matching, plus QK-Clip — packaged as a single optimizer for large-scale training [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- MuonClip preserves the optimization characteristics of Muon: ablations show QK-Clip does not degrade model performance and does not adversely affect the loss trajectory [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- MuonClip was used to pre-train Kimi K2 — a 1.04T-parameter MoE with 32B activated parameters — on 15.5 trillion tokens with zero loss spikes over the entire run [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- For Kimi K2, the Muon component is paired with QK-Clip threshold τ = 100; the maximum attention logit is initially capped at 100 by QK-Clip, then gradually decays to a typical operating range without any τ adjustment over the course of training [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- The motivation for MuonClip is empirical: in mid-scale Muon training (9B activated / 53B total MoE), maximum attention logits rapidly exceed 1000, producing instability that AdamW does not exhibit at the same scale in the team's experiments [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Sources

- [[sources/pdf-kimi-team-2026-kimi-k2-open]]

## Related

- [[concepts/muon-optimizer]]
- [[concepts/qk-clip]]
- [[concepts/token-efficiency-pretraining]]
- [[entities/kimi-k2]]
