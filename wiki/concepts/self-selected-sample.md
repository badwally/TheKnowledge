---
type: concept
slug: self-selected-sample
canonical_name: Self-selected sample (in infrastructure effectiveness data)
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T21:01:04Z'
draft_unresolved_claims: 3
---

# Self-selected sample (in infrastructure effectiveness data)

## Summary

A self-selected sample is an observational dataset in which inclusion of units — e.g. highway pavement sections that received a particular maintenance or rehabilitation activity — is not random but is instead determined by an underlying choice process, typically a decision-maker selecting units on which the treatment is believed to be most effective. Modelling treatment effectiveness directly on such a sample yields biased and inconsistent parameter estimates unless the selection mechanism is explicitly modelled jointly with the outcome.

## Key claims

- In observational pavement M&R effectiveness data, the observations used to analyse the effectiveness of a given activity consist mainly of sections for which that activity was believed to be most effective, making the sample non-representative of the population of highway pavement sections [[sources/web-1998-09-20-413]].
- This self-selection explains why separate pavement deterioration models fit per M&R activity have often produced poor fits to data or counterintuitive signs of important variable coefficients [[sources/web-1998-09-20-413]].
- Madanat and Mishalani (1998) argue that explicitly modelling the discrete agency choice of M&R activity alongside the continuous pavement-response equation — i.e. treating the sample as self-selected rather than random — is required to recover consistent effectiveness parameter estimates [[sources/web-1998-09-20-413]].

## Sources

- [[sources/web-1998-09-20-413]]

## Related

- [[entities/pavement-selectivity-bias-paper]]
- [[concepts/selectivity-bias-infrastructure]]
- [[concepts/econometric-switching-model-pavement]]
- [[concepts/pavement-maintenance-rehabilitation-effectiveness]]
