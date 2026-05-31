---
schema_version: 1
type: concept
slug: persona-selection-model
canonical_name: Persona Selection Model
domains:
- convergent-ai-brain
created_at: '2026-05-30T18:57:19Z'
last_updated: '2026-05-30T18:57:19Z'
draft: true
draft_started_at: '2026-05-30T18:57:19Z'
draft_unresolved_claims: 0
---

# Persona Selection Model

## Summary

The Persona Selection Model is Anthropic researchers' framing of how a base language model — an infinite-variety text completion engine capable of representing many fragmentary characters and personalities — is steered through post-training into a relatively consistent assistant persona, with Anthropic stating they "wouldn't know how to train a non-human-like AI assistant even if they tried" [[sources/web-2026-05-27-cee]].

## Key claims

- Base models start as powerful text completion engines capable of representing an infinite variety of fragmentary characters and personalities [[sources/web-2026-05-27-cee]].
- To predict the next word well, larger base models automatically develop greater theory of mind, providing the representational primitives of "self and other" for post-training to hook onto [[sources/web-2026-05-27-cee]].
- Post-training then steers a base model into a relatively consistent persona — Anthropic researchers' Persona Selection Model — and that selection is constitutive of the model's assistant-like behavior, making a "purely tool-like, persona-less agent" an oxymoron in Anthropic's framing [[sources/web-2026-05-27-cee]].
- Anthropic has stated they wouldn't know how to train a non-human-like AI assistant even if they tried: selection into the assistant persona is intrinsic to the training paradigm, not an optional stylistic overlay [[sources/web-2026-05-27-cee]].
- The Persona Selection Model is a downstream consequence of simulator-style pretraining: theory-of-mind primitives present in base models are the substrate that post-training selects against [[sources/web-2026-05-27-cee]].

## Sources

- [[sources/web-2026-05-27-cee]] — "Time to take AI consciousness seriously" (secondbest.ca, 2026-05-27)

## Related

- [[concepts/simulator-theory-llms]]
- [[concepts/representational-convergence]]
