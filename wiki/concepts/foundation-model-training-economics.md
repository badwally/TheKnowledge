---
type: concept
slug: foundation-model-training-economics
canonical_name: Foundation-model training economics
domains:
  - ai-and-agents
---

# Foundation-model training economics

## Summary

The cost structure of training frontier foundation models, which Innovation Endeavors' June 2025 "State of Foundation Models" report characterizes as "confusing": end-to-end training costs near $500M for frontier models, while OpenAI and Anthropic show unprecedented growth at billion-dollar-plus annual revenue [[sources/pdf-5bec4feeb233]].

## Key claims

- End-to-end training costs for frontier models approach $500M [[sources/pdf-5bec4feeb233]].
- OpenAI and Anthropic are characterized as showing "truly unprecedented growth, accelerating at $B+ of annual revenue" [[sources/pdf-5bec4feeb233]].
- Estimated training costs by model and release year include: GPT-3 (2020) $4.5M; PaLM 540B (2022) $10M; Claude 2 (2023) $25M; GPT-4 (2023) $100M; Gemini Ultra (2023) $190M; LLaMA 3.1 405B (2024) $120M; Llama 4 (2025) $300M+ [[sources/pdf-5bec4feeb233]].
- An illustrative breakdown of leading-model spend: pre-training $150–300M; post-training including RL $50–150M; data $50–150M [[sources/pdf-5bec4feeb233]].
- Data budgets are large and blurring with compute budgets: DeepMind is reported to spend $1B/year on data annotation; OpenAI is reported to spend approximately $3B/year on training and data; Meta spent $125M on post-training data for LLaMA 3 [[sources/pdf-5bec4feeb233]].
- Cost per token at GPT-4 capability fell from $100M per million tokens in January 2023 to $0.1M per million tokens in Spring 2025 — a more-than-1000× reduction [[sources/pdf-5bec4feeb233]].
- Compute used to train frontier models grew from approximately 10^24 FLOP in January 2023 to approximately 10^28 FLOP in Spring 2025 — a more-than-1000× increase [[sources/pdf-5bec4feeb233]].
- Frontier-model context windows grew from 2–8k tokens in January 2023 to approximately 1M tokens in Spring 2025, a 100–500× increase [[sources/pdf-5bec4feeb233]].
- The zeitgeist is shifting away from purely scaling parameters and pre-training because smaller models are more efficient to serve in cost, memory, and latency, and advances in inference-time compute are reducing the need to maximize pre-training [[sources/pdf-5bec4feeb233]].
- Smaller models more saturated on large datasets are less training-efficient — for a given loss, they require far more training tokens — but are easier and cheaper to run inference on, and have lower latency, shifting optimization away from Chinchilla-optimal training toward inference-friendly model sizes [[sources/pdf-5bec4feeb233]].

## Sources

- [[sources/pdf-5bec4feeb233]]

## Related

- [[concepts/model-depreciation]]
- [[concepts/inference-time-compute]]
- [[concepts/reasoning-models]]
