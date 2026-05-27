---
schema_version: 1
type: concept
slug: transformed-gamma-process
canonical_name: Transformed gamma (TG) process
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T21:00:53Z'
draft_unresolved_claims: 2
created_at: '2026-05-20T21:09:31Z'
last_updated: '2026-05-20T21:09:31Z'
---

# Transformed gamma (TG) process

## Summary

The transformed gamma (TG) process is a stochastic degradation model proposed by Fouladirad, Giorgio, and Pulcini (2022) to describe degradation phenomena subject to an upper bound that lies near the failure threshold. Unlike the standard (unbounded) gamma process, the TG process must have dependent increments to accommodate the bound, and it treats the upper bound itself as an unknown parameter to be estimated from data.

## Key claims

- The TG process is proposed as a new bounded stochastic process intended to adequately describe bounded degradation phenomena and predict their future evolution [[sources/web-2022-07-07-ac2]].
- A bounded degradation process must have dependent increments — a property that distinguishes the TG process from the classical gamma process, which is defined by independent increments [[sources/web-2022-07-07-ac2]].
- Differently from other existing gamma-process-based bounded degradation models, the TG process treats the upper bound as an unknown parameter that must be estimated from the available degradation data, rather than being specified a priori [[sources/web-2022-07-07-ac2]].
- TG process parameters can be estimated by the maximum likelihood (ML) method [[sources/web-2022-07-07-ac2]].
- The TG process is shown applicable to wear measures of cylinder liners equipping a diesel engine for marine propulsion, where its fitting ability is compared with that of a previously adopted unbounded gamma process on the same data [[sources/web-2022-07-07-ac2]].

## Sources

- [[sources/web-2022-07-07-ac2]]

## Related

- [[concepts/gamma-degradation-process]]
- [[concepts/bounded-degradation-phenomena]]
- [[concepts/cylinder-liner-wear]]
- [[concepts/maximum-likelihood-estimation]]
- [[entities/transformed-gamma-process-bounded-paper]]
- [[entities/mitra-fouladirad]]
- [[entities/massimiliano-giorgio]]
- [[entities/gianpaolo-pulcini]]
