---
type: entity
slug: transformed-gamma-process-bounded-paper
canonical_name: A transformed gamma process for bounded degradation phenomena
entity_kind: paper
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T21:00:53Z'
draft_unresolved_claims: 2
---

# A transformed gamma process for bounded degradation phenomena

## Summary

A 2022 paper by Mitra Fouladirad, Massimiliano Giorgio, and Gianpaolo Pulcini proposing a new bounded transformed gamma (TG) process for degradation phenomena whose upper bound is not far from the failure threshold, with the upper bound itself treated as an unknown parameter to be estimated from data. The model is fitted by maximum likelihood and applied to cylinder liner wear data from a marine diesel engine, with its fit compared to that of a previously adopted unbounded gamma process.

## Key facts

- The paper is authored by Mitra Fouladirad, Massimiliano Giorgio, and Gianpaolo Pulcini and was deposited at HAL (hal-04063942v1) on 7 July 2022 [[sources/web-2022-07-07-ac2]].
- The paper observes that most stochastic models of degradation phenomena of technological units assume the degradation level can increase indeterminately, while in reality these phenomena are subject to obvious bounds, if only because technological units have finite size [[sources/web-2022-07-07-ac2]].
- The paper notes that this inconsistency usually does not significantly affect the effectiveness of unbounded degradation models, because units are typically assumed to fail at thresholds far below the obvious physical bounds [[sources/web-2022-07-07-ac2]].
- The authors argue that in some cases, due to the nature of the underlying degradation mechanism, less obvious bounds exist that are not necessarily far from the failure thresholds, and that using a bounded degradation model in these situations could be beneficial [[sources/web-2022-07-07-ac2]].
- The paper argues that a bounded degradation process must have dependent increments [[sources/web-2022-07-07-ac2]].
- The paper proposes a new bounded transformed gamma (TG) process to describe bounded degradation phenomena and predict their future evolution [[sources/web-2022-07-07-ac2]].
- Differently from other existing gamma-process-based bounded degradation models, the proposed model treats the upper bound as an unknown parameter that has to be estimated from the available degradation data [[sources/web-2022-07-07-ac2]].
- A numerical example is presented in which the parameters of the proposed model are estimated from simulated data [[sources/web-2022-07-07-ac2]].
- The model is then applied to a set of wear measures of cylinder liners that equip a diesel engine for marine propulsion, which also motivated the study [[sources/web-2022-07-07-ac2]].
- Model parameters are estimated using the maximum likelihood (ML) method [[sources/web-2022-07-07-ac2]].
- The fitting ability of the proposed new bounded process is compared to that of an unbounded gamma process previously adopted to analyze the same liner wear data [[sources/web-2022-07-07-ac2]].

## Sources

- [[sources/web-2022-07-07-ac2]]

## Related

- [[entities/mitra-fouladirad]]
- [[entities/massimiliano-giorgio]]
- [[entities/gianpaolo-pulcini]]
- [[concepts/transformed-gamma-process]]
- [[concepts/bounded-degradation-phenomena]]
- [[concepts/gamma-degradation-process]]
- [[concepts/cylinder-liner-wear]]
- [[concepts/maximum-likelihood-estimation]]
