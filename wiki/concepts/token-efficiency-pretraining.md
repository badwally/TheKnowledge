---
type: concept
slug: token-efficiency-pretraining
canonical_name: Token efficiency in pre-training
domains:
  - ai-and-agents
---

# Token efficiency in pre-training

## Summary

Token efficiency, in the framing of the Kimi K2 technical report, is the amount of model-quality improvement obtained per training token consumed; under increasingly limited supplies of high-quality human data, the Kimi Team treats it as a critical scaling coefficient and pursues two complementary levers — a token-efficient optimizer (Muon, stabilized as MuonClip) and a synthetic rephrasing pipeline that increases the effective learning signal per token — to maximize it [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Key claims

- The Kimi Team posits that, given the increasingly limited availability of high-quality human data, token efficiency is emerging as a critical coefficient in the scaling of large language models [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- They distinguish "token utility" (the effective learning signal each token contributes) from naive multi-epoch repetition, noting that repeated exposure to the same tokens can lead to overfitting and reduced generalization [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Lever 1: a token-efficient optimizer. The Muon optimizer outperforms AdamW under matched compute and model size, and Muon's training-instability problem at scale is addressed via QK-Clip, yielding the MuonClip optimizer [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Lever 2: synthetic data generation. A rephrasing pipeline with style- and perspective-diverse prompting, chunk-wise autoregressive generation, and fidelity verification is used to increase the effective volume of high-quality knowledge tokens without inducing significant overfitting [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- In a SimpleQA accuracy ablation on an early Kimi K2 checkpoint, three strategies are compared on the same knowledge corpus: (1) repeating the original dataset for 10 epochs, (2) rephrasing the data once and repeating it for 10 epochs, and (3) rephrasing the data 10 times with a single training pass; accuracy improves consistently across these three strategies, demonstrating the efficacy of rephrasing-based augmentation [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- The same rephrasing approach is extended to other large-scale knowledge corpora, with each corpus rephrased at most twice [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Sources

- [[sources/pdf-kimi-team-2026-kimi-k2-open]]

## Related

- [[concepts/muonclip-optimizer]]
- [[concepts/muon-optimizer]]
- [[entities/kimi-k2]]
