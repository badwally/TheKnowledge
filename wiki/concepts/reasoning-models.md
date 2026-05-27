---
schema_version: 1
type: concept
slug: reasoning-models
canonical_name: Reasoning models
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Reasoning models

## Summary

A class of foundation models trained to "think before they speak" — producing extensive internal reasoning before emitting a final answer. Innovation Endeavors' June 2025 "State of Foundation Models" report characterizes reasoning models as the dominant new direction for foundation-model R&D, with post-training potentially becoming more important than pre-training [[sources/pdf-5bec4feeb233]].

## Key claims

- Reasoning models trained to think before responding "likely represent a new scaling law," and training them "requires significant advances in post-training, including reinforcement learning & reward models" [[sources/pdf-5bec4feeb233]].
- Post-training "may become more important than pre-training" as a result of reasoning-model development [[sources/pdf-5bec4feeb233]].
- Three open challenges with reasoning models are flagged: how well easily-constructed synthetic datasets generalize; whether synthetic math and coding data translate to other domains; and what the optimal reinforcement-learning algorithm or approach is — including sampling strategy, process vs outcome rewards, noisy and sparse reward signals in complex tasks, and computational cost [[sources/pdf-5bec4feeb233]].
- Data acquisition is a binding constraint: "high-end reasoning traces" are reportedly worth approximately $3,000 each, and OpenAI is reported to be paying $2–3k per individual reasoning trace [[sources/pdf-5bec4feeb233]].
- Verifiers and reward models are identified as essential infrastructure: procedural verifiers (compilers + unit tests for code, theorem provers for math, majority voting in domains with precise answers) and learned verifiers (process reward models, outcome reward models, learned domain-specific verifiers, generalist reward models) [[sources/pdf-5bec4feeb233]].
- Generalist reward models are framed as the "holy grail" but difficult to build [[sources/pdf-5bec4feeb233]].
- The post-training algorithm landscape includes Proximal Policy Optimization (PPO) for reinforcement-learning rewards, Direct Preference Optimization (DPO) for supervised training on preference pairs, and Guided Reinforcement Preference Optimization (GRPO) which combines a trained reward model with reinforcement learning [[sources/pdf-5bec4feeb233]].
- Specialized fine-tuning may become increasingly autonomous and self-supervised, following a four-step loop: take sample inputs; generate sample responses via test-time compute; use a reward model to score responses; run a reinforcement-learning loop to fine-tune the model [[sources/pdf-5bec4feeb233]].

## Sources

- [[sources/pdf-5bec4feeb233]]

## Related

- [[concepts/inference-time-compute]]
- [[concepts/foundation-model-training-economics]]
