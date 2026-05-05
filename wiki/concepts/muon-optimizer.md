---
type: concept
slug: muon-optimizer
canonical_name: Muon optimizer
domains:
  - ai-and-agents
---

# Muon optimizer

## Summary

Muon is a token-efficient deep-learning optimizer (Jordan et al.; reused with weight decay and consistent update RMS scaling in the Kimi Team's earlier Moonlight work) which, in the Kimi K2 technical report, is shown to outperform AdamW at matched compute and model size — but to suffer from training instability driven by exploding attention logits when scaled up, motivating the QK-Clip extension that yields MuonClip [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Key claims

- Under matched compute budget and matched model size — and therefore matched amounts of training data — Muon substantially outperforms AdamW in the Kimi Team's experiments, making it a strong choice for improving token efficiency in large language model training [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Scaling up Muon training surfaces a stability problem: attention logits explode, an issue that occurs more frequently with Muon than with AdamW in the team's experiments [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- In a mid-scale 9B-activated / 53B-total MoE training run, vanilla Muon drives maximum attention logits past a magnitude of 1000, which typically yields significant loss spikes and occasional divergence [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Existing mitigations are insufficient in this regime: logit soft-cap clips logits only after the QK dot product, allowing growth before capping; QK-Norm is not applicable to multi-head latent attention because its key matrices are not fully materialized during inference [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- The Kimi Team's resolution is to wrap Muon (with weight decay and consistent RMS matching) with QK-Clip into the MuonClip optimizer, which is then used to train Kimi K2 to 15.5 trillion tokens with no loss spikes [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Sources

- [[sources/pdf-kimi-team-2026-kimi-k2-open]]

## Related

- [[concepts/muonclip-optimizer]]
- [[concepts/qk-clip]]
- [[concepts/token-efficiency-pretraining]]
