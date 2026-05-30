---
schema_version: 1
type: concept
slug: prediction-error
canonical_name: Prediction Error
domains:
- convergent-ai-brain
created_at: '2026-05-30T18:48:35Z'
last_updated: '2026-05-30T18:48:35Z'
draft: true
draft_started_at: '2026-05-30T18:48:35Z'
draft_unresolved_claims: 0
---

# Prediction Error

## Summary

In hierarchical predictive coding, prediction error is the residual mismatch between a top-down prediction and the actual signal at a lower level — and it is the only quantity that needs to be propagated upward through the cortical hierarchy [[sources/pdf-5f41a1d2e45f]]. Prediction error functions as a "proxy" (Feldman & Friston 2010) for sensory information itself within the predictive-processing framework [[sources/pdf-5f41a1d2e45f]].

## Key claims

- The strategy originated as a data-compression technique in signal processing, driven by James Flanagan and others at Bell Labs in the 1950s; transmitting only the divergence between actual and predicted pixel values produced major bandwidth savings, and descendants of the technique are used today in JPEGs, lossless audio compression, and motion-compressed video coding [[sources/pdf-5f41a1d2e45f]].
- Transposed to the neural domain, prediction error reports the "surprise" induced by a mismatch between predicted and actual sensory signals — formally **surprisal** (Tribus 1961), distinguished from experientially loaded surprise [[sources/pdf-5f41a1d2e45f]].
- Prediction error drives two timescales of change in the model: rapid perceptual inference (adjusting probabilistic representations so that top-down predictions cancel the error at the lower level) and slower perceptual learning (adjusting the model itself so as to reduce future discrepancies) [[sources/pdf-5f41a1d2e45f]].

## Sources

- [[sources/pdf-5f41a1d2e45f]] — Whatever next? Predictive brains, situated agents, and the future of cognitive science (BBS 2013)

## Related

- [[concepts/hierarchical-predictive-coding]]
- [[concepts/predictive-processing]]
- [[concepts/surprisal]]
- [[concepts/generative-model-brain]]
