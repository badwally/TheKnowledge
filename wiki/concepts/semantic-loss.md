---
schema_version: 1
type: concept
slug: semantic-loss
canonical_name: Semantic Loss
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Semantic Loss

## Summary

A technique for constraining the loss function of a neural network with symbolic knowledge under a probabilistic interpretation of the output labels (Gajowniczek et al. 2020); cited by Belle and Marcus (AAAI-26) as one of two canonical examples — alongside MultiplexNet — in the "training neural networks with logic formulas" line of neuro-symbolic AI [[sources/pdf-vaishak-belle-2026-the-future-is]].

## Key claims

- Semantic loss constrains the loss function of a neural network with symbolic knowledge, based on a probabilistic interpretation of the output labels (Gajowniczek et al. 2020) [[sources/pdf-vaishak-belle-2026-the-future-is]].
- Constraining loss functions with symbolic knowledge is useful in a wide range of applications from physics (Stewart and Ermon 2017) to robotics (Innes and Ramamoorthy 2020) [[sources/pdf-vaishak-belle-2026-the-future-is]].
- There is a close relation between loss-function constraints and high-level knowledge representation; semantic loss and DeepProbLog perform essentially similar functions when computing gradients [[sources/pdf-vaishak-belle-2026-the-future-is]].
- MultiplexNet (Hoernle et al. 2022) is an alternative in the same line of research, but uses a fuzzy (real-valued) truth interpretation of the labels rather than a probabilistic one [[sources/pdf-vaishak-belle-2026-the-future-is]].

## Sources

- [[sources/pdf-vaishak-belle-2026-the-future-is]]

## Related

- [[concepts/neuro-symbolic-ai]]
- [[entities/deepproblog]]
- [[entities/logic-tensor-networks]]
