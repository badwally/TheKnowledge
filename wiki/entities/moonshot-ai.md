---
type: entity
slug: moonshot-ai
canonical_name: Moonshot AI (Kimi Team)
entity_kind: organization
domains:
  - ai-and-agents
---

# Moonshot AI (Kimi Team)

## Summary

AI lab, publishing under the byline "Kimi Team," that developed and open-sourced the Kimi K2 trillion-parameter Mixture-of-Experts language model and authored its technical report "Kimi K2: Open Agentic Intelligence" [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Key facts

- Released the base and post-trained Kimi K2 checkpoints on Hugging Face under the organization handle moonshotai (e.g., huggingface.co/moonshotai/Kimi-K2-Instruct) [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Kimi K2 is a 1.04 trillion-parameter MoE LLM with 32 billion activated parameters, pre-trained on 15.5 trillion tokens with the MuonClip optimizer and zero loss spikes [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- The Kimi K2 report introduces the MuonClip optimizer (Muon + QK-Clip), a large-scale agentic data synthesis pipeline, and a general RL framework combining verifiable rewards (RLVR) with self-critique rubric rewards [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Builds on the team's prior "Moonlight" work (cited as reference 46 in the report), which established Muon with weight decay and consistent update RMS scaling as more token-efficient than AdamW under matched compute and model size [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Kimi K2 is presented as the successor to Kimi K1.5, with the rephrasing-based synthetic-data pipeline cited as a key advance over K1.5's pre-training data [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Sources

- [[sources/pdf-kimi-team-2026-kimi-k2-open]]

## Related

- [[entities/kimi-k2]]
- [[concepts/muonclip-optimizer]]
- [[concepts/agentic-data-synthesis]]
