---
type: concept
slug: missing-intervention-handling
canonical_name: Handling Missing Intervention Data
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T19:53:56Z'
draft_unresolved_claims: 1
---

# Handling Missing Intervention Data

## Summary

Handling missing intervention data is a set of inference techniques required when extending element-level deterioration models to a full bridge network, addressing three distinct missingness patterns: (1) missing prior knowledge of an intervention's effect, (2) reported date but unreported type, and (3) entirely unreported interventions visible only as inspection jumps.

## Key claims

- At network scale, intervention records may be missing in three distinct ways, and each requires a different treatment [[sources/yt-vx6ATEoEuUE]].
- Case 1 — missing prior knowledge: when the prior effect distribution for a given intervention type on a given element category is unavailable, the missing prior is replaced by the expectation of the effect of the same intervention type on other categories within the same group of structural elements [[sources/yt-vx6ATEoEuUE]].
- Case 2 — unreported intervention type (with known date): the unknown type is handled using a likelihood-based inference step [[sources/yt-vx6ATEoEuUE]].
- Case 3 — entirely unreported intervention: the inspection record shows a jump in condition but neither the intervention's date nor its type is recorded, and both must be inferred from the inspection time series [[sources/yt-vx6ATEoEuUE]].
- Handling these missingness patterns is one of the two prerequisites — alongside an aggregation method — for lifting element-level state-space deterioration models to network scale [[sources/yt-vx6ATEoEuUE]].

## Sources

- [[sources/yt-vx6ATEoEuUE]]

## Related

- [[concepts/intervention-effect-modeling]]
- [[concepts/network-scale-deterioration-analysis]]
- [[concepts/state-space-deterioration-model]]
