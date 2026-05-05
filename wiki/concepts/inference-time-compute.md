---
type: concept
slug: inference-time-compute
canonical_name: Inference-time compute scaling
domains:
  - ai-and-agents
---

# Inference-time compute scaling

## Summary

A scaling regime in which model performance is improved by allocating more compute at inference time — by sampling longer reasoning traces or by running search procedures — rather than by enlarging the pre-trained model. Innovation Endeavors' June 2025 "State of Foundation Models" report frames inference-time compute as a new scaling law for foundation models [[sources/pdf-5bec4feeb233]].

## Key claims

- Inference-time compute is presented as a new scaling law for foundation models, distinct from the parameter-count and training-token scaling laws that dominated prior years [[sources/pdf-5bec4feeb233]].
- A 3B-parameter reasoning model can outperform a 70B model when given enough thinking time, indicating that inference compute can substitute for parameter scale [[sources/pdf-5bec4feeb233]].
- Two broad implementation paths are identified: (a) post-training the model on reasoning traces so it produces a single, continuous, long stream of output tokens; and (b) using "search" techniques at inference time, in which a control flow mediates interaction between the model and a secondary verifier or validator [[sources/pdf-5bec4feeb233]].
- Innovation Endeavors infers that o1-pro is "likely 'best of n o1'": multiple o1 responses are sampled and a verifier picks the best [[sources/pdf-5bec4feeb233]].
- Test-time compute is not a new concept; the report cites Cicero as a precursor where models compute extensively at inference [[sources/pdf-5bec4feeb233]].
- Innovation Endeavors lists "inference time scaling" alongside synthetic data and agents (systems engineering) as the explicit answers to the question "What's next?" for foundation-model scaling [[sources/pdf-5bec4feeb233]].

## Sources

- [[sources/pdf-5bec4feeb233]]

## Related

- [[concepts/reasoning-models]]
- [[concepts/foundation-model-training-economics]]
