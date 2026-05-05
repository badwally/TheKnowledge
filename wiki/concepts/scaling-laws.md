---
type: concept
slug: scaling-laws
canonical_name: Scaling laws (AI training)
domains:
  - ai-and-agents
---

# Scaling laws (AI training)

## Summary

The empirical finding that AI model performance improves predictably with increases in parameters, training compute, and dataset size; foundational to the U.S. frontier-lab strategy of capital-intensive proprietary AI development, but encountering diminishing returns by 2025 [[sources/pdf-ngor-luong-2026-two-loops-how]].

## Key claims

- Scaling laws are the empirical finding that model performance improves predictably with increases in parameters, training compute, and dataset size [[sources/pdf-ngor-luong-2026-two-loops-how]].
- The premise that bigger models trained on more data yield better performance has reinforced a capital-intensive, proprietary approach to AI development among U.S. frontier labs [[sources/pdf-ngor-luong-2026-two-loops-how]].
- Applying scaling laws requires complex and expensive training: multi-million-dollar training runs engineered to extract maximum learning per unit of compute, with thousands of GPUs running in parallel and training pipelines designed with enough redundancy to absorb localized hardware failures [[sources/pdf-ngor-luong-2026-two-loops-how]].
- Competitive advantage under the scaling paradigm depends not just on model size but also on training know-how, infrastructure design, and data composition, which AI firms have strong incentives to guard as trade secrets [[sources/pdf-ngor-luong-2026-two-loops-how]].
- In 2025, several factors began to challenge scaling-centered strategies: successive model generations require ever-more compute for incremental gains (diminishing returns); returns from scaling are non-uniform across tasks because prompting and task-specific optimization let small models match large ones on some tasks; and 2025 architectural and post-training advances delivered performance gains without relying on increased model size [[sources/pdf-ngor-luong-2026-two-loops-how]].
- OpenAI described its February 2025 GPT-4.5 as its largest model to date and its last to rely primarily on scaling pre-training rather than reasoning — a public marker of the scaling regime's reaching diminishing returns [[sources/pdf-ngor-luong-2026-two-loops-how]].
- For 2025, U.S. AI capital expenditure by Microsoft, Amazon, Meta, and Google was at least $350 billion (Bloomberg Intelligence), versus less than $40 billion for China's major cloud providers — a differential that reflects U.S. prioritization of scaling [[sources/pdf-ngor-luong-2026-two-loops-how]].

## Sources

- [[sources/pdf-ngor-luong-2026-two-loops-how]]

## Related

- [[concepts/open-weight-models]]
- [[concepts/two-loops-framework]]
- [[entities/openai]]
