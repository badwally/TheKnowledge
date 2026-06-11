---
schema_version: 1
type: concept
slug: gradient-inversion-attack
canonical_name: Gradient Inversion Attack
domains:
- data-collectives
created_at: '2026-06-10T22:23:15Z'
last_updated: '2026-06-10T22:23:15Z'
draft: true
draft_started_at: '2026-06-10T22:23:15Z'
draft_unresolved_claims: 0
---

# Gradient Inversion Attack

## Summary

A gradient inversion (GradInv) attack is a class of attacks that recovers training samples from gradients exchanged during distributed model training [[sources/arxiv-2206.07284]]. The existence of such attacks defines the privacy threat model that motivates additional protection mechanisms layered on top of the "share gradients, not raw data" architecture used in federated learning and similar collaborative-training settings [[sources/arxiv-2206.07284]].

## Key claims

- Training samples can be recovered from gradients alone, even when raw data never leaves its owner — this reconstruction capability is what defines the GradInv attack class [[sources/arxiv-2206.07284]].
- GradInv attacks divide into two paradigms: iteration-based attacks and recursion-based attacks [[sources/arxiv-2206.07284]].
- Iteration-based GradInv attacks share three critical ingredients: data initialization, model training, and gradient matching [[sources/arxiv-2206.07284]].
- Surveying GradInv attacks is itself a recognized gap area as of mid-2022, per Zhang et al.'s framing of their survey contribution [[sources/arxiv-2206.07284]].

## Sources

- [[sources/arxiv-2206.07284]] — A Survey on Gradient Inversion: Attacks, Defenses and Future Directions (Zhang et al., 2022).

## Related

- [[concepts/gradient-inversion-defense]]
- [[entities/gradient-inversion-survey]]
- [[concepts/competitor-data-sharing-tradeoff]]
- [[entities/strategic-data-sharing-competitors]]
