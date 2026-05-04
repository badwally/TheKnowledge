---
type: concept
slug: open-weight-models
canonical_name: Open-weight models
domains:
  - ai-and-agents
---

# Open-weight models

## Summary

A class of AI models that release their learned parameters (weights) publicly; "open" spans a spectrum from fully open-source models (which release code, training data, and weights) to open-weight models (which release only parameters), and is distinct from closed/proprietary models accessible only through a developer's interface or API [[sources/pdf-ngor-luong-2026-two-loops-how]].

## Key claims

- "Open" in modern AI usage spans a spectrum: fully open-source (code + data + weights) at one end, and open-weight (parameters only, with varying licensing) at the other; most models described as "open" in 2025–2026 industry usage are open-weight rather than fully open-source [[sources/pdf-ngor-luong-2026-two-loops-how]].
- Closed models, by contrast, are accessible only through the developer's interface (e.g., ChatGPT) or an approved Application Programming Interface (API), with weights kept proprietary [[sources/pdf-ngor-luong-2026-two-loops-how]].
- Open-weight models have varying degrees of licensing permission, allowing developers to independently understand, audit, or recreate the model to differing extents [[sources/pdf-ngor-luong-2026-two-loops-how]].
- Most Chinese frontier labs publish model source code and weights, while U.S. frontier labs have generally maintained proprietary weights — Meta's Llama family being a notable U.S. exception, though reports from late 2025 suggested Meta may keep its forthcoming "Avocado" flagship model proprietary [[sources/pdf-ngor-luong-2026-two-loops-how]].
- China's open ecosystem creates a feedback loop: permissive licensing and aggressive pricing drive global adoption, which drives iteration, which drives further adoption — exemplified by Alibaba's Qwen accounting for the largest model ecosystem on Hugging Face with over 100,000 derivatives as of March 2026 [[sources/pdf-ngor-luong-2026-two-loops-how]].
- Maintaining proprietary weights helps protect the trade-secret advantages of training know-how, infrastructure design, and data composition that underpin scaling-paradigm competitiveness, reinforcing the closed ecosystem among U.S. frontier labs [[sources/pdf-ngor-luong-2026-two-loops-how]].

## Sources

- [[sources/pdf-ngor-luong-2026-two-loops-how]]

## Related

- [[entities/deepseek]]
- [[entities/qwen]]
- [[entities/alibaba]]
- [[concepts/two-loops-framework]]
