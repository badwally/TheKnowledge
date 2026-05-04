---
type: entity
slug: kimi-k2
canonical_name: Kimi K2
entity_kind: paper
domains:
  - ai-and-agents
---

# Kimi K2

## Summary

A 1.04-trillion-parameter Mixture-of-Experts (MoE) large language model with 32 billion activated parameters, released by the Kimi Team and described in the technical report "Kimi K2: Open Agentic Intelligence"; designed as an open-source agentic-intelligence foundation model that achieves state-of-the-art performance among open-source non-thinking models on agentic, coding, math, and reasoning benchmarks [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Key facts

- Architecture is an ultra-sparse Mixture-of-Experts transformer with multi-head latent attention (MLA), similar in form to DeepSeek-V3 and derived from empirical scaling-law analysis [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Pre-trained on 15.5 trillion high-quality tokens with zero loss spikes across the entire training run, using the MuonClip optimizer with QK-Clip threshold τ = 100 [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Post-training is a multi-stage process highlighted by a large-scale agentic data synthesis pipeline and a joint reinforcement learning stage that combines verifiable rewards (RLVR) with a self-critique rubric reward mechanism [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Reports 66.1 on Tau2-Bench, 76.5 on ACEBench (En), 65.8 on SWE-bench Verified, and 47.3 on SWE-bench Multilingual under non-thinking evaluation, surpassing most open- and closed-source baselines and closing the gap with Claude 4 Opus and Sonnet on those benchmarks [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Reports 53.7 on LiveCodeBench v6, 27.1 on OJBench, 49.5 on AIME 2025, and 75.1 on GPQA-Diamond, all without extended thinking [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- On the LMSYS Arena leaderboard (July 17, 2025), Kimi K2 ranked first among open-source models and fifth overall based on more than 3,000 user votes [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Both base and post-trained model checkpoints are open-sourced; the Instruct checkpoint is published at huggingface.co/moonshotai/Kimi-K2-Instruct [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Pre-training uses a synthetic-data rephrasing pipeline with style- and perspective-diverse prompting, chunk-wise autoregressive generation, and fidelity verification; in a SimpleQA ablation on an early K2 checkpoint, rephrasing once and repeating ten epochs and rephrasing ten times in a single pass both outperform raw ten-epoch repetition [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Sources

- [[sources/pdf-kimi-team-2026-kimi-k2-open]] — Kimi K2: Open Agentic Intelligence (Technical Report)

## Related

- [[entities/moonshot-ai]]
- [[concepts/muonclip-optimizer]]
- [[concepts/qk-clip]]
- [[concepts/muon-optimizer]]
- [[concepts/multi-head-latent-attention]]
- [[concepts/mixture-of-experts]]
- [[concepts/agentic-data-synthesis]]
- [[concepts/verifiable-rewards-rl]]
- [[concepts/self-critique-rubric-reward]]
- [[concepts/token-efficiency-pretraining]]
