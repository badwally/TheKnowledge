---
type: concept
slug: selectivity-bias-infrastructure
canonical_name: Selectivity bias in infrastructure deterioration modelling
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T21:01:04Z'
draft_unresolved_claims: 2
---

# Selectivity bias in infrastructure deterioration modelling

## Summary

Selectivity bias in infrastructure deterioration modelling is the systematic distortion of estimated maintenance and rehabilitation (M&R) effectiveness that arises when observational samples consist primarily of pavement (or other infrastructure) sections for which the activity in question was believed to be most effective. Because the sample is not representative of the underlying population, per-activity deterioration models fit on such data tend to exhibit poor fits or counterintuitive coefficient signs; correcting for the bias requires explicit joint modelling of the discrete agency choice and the continuous infrastructure response.

## Key claims

- Engineers selecting an M&R activity for highway pavement sections rely on estimates of how effective each activity is at slowing pavement deterioration and improving condition, making the effectiveness model a load-bearing input to highway-agency decision-making [[sources/web-1998-09-20-413]].
- Researchers have historically attempted to quantify M&R effectiveness by fitting a separate pavement deterioration model for each type of M&R activity, but the resulting models have often produced poor fits to data or counterintuitive signs of important variable coefficients [[sources/web-1998-09-20-413]].
- Madanat and Mishalani (1998) attribute these poor results to selectivity bias: observations used to analyse a given M&R activity consist mainly of sections for which that activity was believed to be most effective, and so are not representative of the population of highway pavement sections [[sources/web-1998-09-20-413]].
- Selectivity bias in M&R effectiveness modelling is a special case of the wider econometric literature on selectivity bias in models combining discrete and continuous choice, exemplified by Mannering's 1987 *Transportation Research Record* paper on selectivity bias in discrete and continuous choice models [[sources/web-1998-09-20-413]].
- A standard correction is a structured econometric system that pairs a discrete model of the agency's choice of M&R activity with a set of continuous pavement-response equations, one per activity; jointly estimating these accounts for the self-selected sample and yields consistent parameter estimates [[sources/web-1998-09-20-413]].

## Sources

- [[sources/web-1998-09-20-413]]

## Related

- [[entities/pavement-selectivity-bias-paper]]
- [[entities/samer-madanat]]
- [[entities/rabi-mishalani]]
- [[concepts/self-selected-sample]]
- [[concepts/econometric-switching-model-pavement]]
- [[concepts/pavement-maintenance-rehabilitation-effectiveness]]
