---
schema_version: 1
type: concept
slug: hierarchical-predictive-coding
canonical_name: Hierarchical Predictive Coding
domains:
- convergent-ai-brain
created_at: '2026-05-30T18:48:35Z'
last_updated: '2026-05-30T18:48:35Z'
draft: true
draft_started_at: '2026-05-30T18:48:35Z'
draft_unresolved_claims: 0
---

# Hierarchical Predictive Coding

## Summary

Hierarchical predictive coding is the class of cortical models in which top-down connections within a multi-level bidirectional system encode a probabilistic generative model of the activities of units at lower levels, with each level attempting to predict and "explain away" the driving sensory signal so that only residual prediction errors propagate forward [[sources/pdf-5f41a1d2e45f]]. The canonical references are Rao and Ballard (1999), Lee and Mumford (2003), and Friston (2005), with extensions to action by Friston and Stephan (2007), Friston (2010), and Brown et al. (2011) [[sources/pdf-5f41a1d2e45f]].

## Key claims

- Forward connections between cortical levels carry the "residual errors" (Rao & Ballard 1999, p. 79) separating predictions from actual lower-level activity, while backward connections — which do most of the "heavy lifting" — carry the predictions themselves [[sources/pdf-5f41a1d2e45f]].
- Rao and Ballard's (1999) model of predictive coding in the visual cortex is the classic early example: when top-down predictions match lower-level activity, no further action ensues; when there is a mismatch, the propagated error rapidly adjusts the higher-level representation (rapid perceptual inference) and more slowly adjusts the model itself (perceptual learning) [[sources/pdf-5f41a1d2e45f]].
- The bidirectional, reciprocally connected structure of the model has an appealing mapping to known facts about the hierarchical wiring of cortex (Friston 2005; Lee & Mumford 2003) [[sources/pdf-5f41a1d2e45f]].
- Hierarchical predictive coding combines top-down probabilistic generative models with the efficient-encoding strategy of transmitting only the unexpected variation — a strategy originally developed as a data-compression technique in signal processing [[sources/pdf-5f41a1d2e45f]].

## Sources

- [[sources/pdf-5f41a1d2e45f]] — Whatever next? Predictive brains, situated agents, and the future of cognitive science (BBS 2013)

## Related

- [[concepts/predictive-processing]]
- [[concepts/prediction-error]]
- [[concepts/generative-model-brain]]
- [[concepts/bayesian-brain]]
- [[concepts/active-inference]]
- [[entities/karl-friston]]
