---
schema_version: 1
type: concept
slug: differential-privacy
canonical_name: Differential Privacy
domains:
- data-collectives
created_at: '2026-06-10T22:25:30Z'
last_updated: '2026-06-10T22:25:30Z'
draft: true
draft_started_at: '2026-06-10T22:25:30Z'
draft_unresolved_claims: 0
---

# Differential Privacy

## Summary

Differential privacy (DP) is a formal privacy-protection framework originally proposed by Dwork (2006) for data publishing, in which a randomized mechanism guarantees that no fragment of data can be reliably traced back to an individual by introducing calibrated noise into query results [[sources/web-2025-08-21-f21]]. A DP mechanism is required to produce statistically similar outputs on any two neighboring datasets — datasets that differ in only one record — so that an observer of the output cannot confidently determine whether any particular record was in the input [[sources/web-2025-08-21-f21]]. DP is the dominant privacy framework for protecting deep learning models because of its solid mathematical foundation and its ability to bound information leakage regardless of attacker capabilities [[sources/web-2025-08-21-f21]].

## Key claims

- Formal definition: a mechanism M satisfies (ε, δ)-DP if, for any pair of neighboring datasets D and D′ and any possible output O, the probability that M outputs O on D is within a factor of e^ε of the probability on D′, up to an additive δ slack [[sources/web-2025-08-21-f21]].
- Two neighboring datasets are datasets D, D′ that differ in exactly one record under a distance metric d(·) [[sources/web-2025-08-21-f21]].
- ε is the privacy budget (ε ≥ 0): a smaller ε enhances privacy protection but increases the noise introduced during the query/training process [[sources/web-2025-08-21-f21]].
- DP can be applied to deep learning by treating the model as a complex data-querying system, with random perturbation injected in either the training phase or the prediction phase [[sources/web-2025-08-21-f21]].
- Beyond formal privacy, DP has been shown to mitigate overfitting and improve the generalization of deep neural networks [[sources/web-2025-08-21-f21]].
- DP can encourage unfairness in neural networks, but proper technical interventions exist to mitigate this effect [[sources/web-2025-08-21-f21]].
- DP provides defense against adversarial attacks (with guarantees that hold regardless of the specific attack implementation) and is more robust to data poisoning than alternative privacy-preserving approaches [[sources/web-2025-08-21-f21]].
- DP is distinct from prior privacy techniques such as *k*-anonymity, *l*-diversity, homomorphic encryption, and secure multiparty computation; the latter two encrypt data into ciphertext, while DP perturbs query outputs [[sources/web-2025-08-21-f21]].

## Sources

- [[sources/web-2025-08-21-f21]] — Zhang, X. & Zhang, Q. (2025). Defending against attacks in deep learning with differential privacy: a survey.

## Related

- [[concepts/privacy-budget]]
- [[concepts/privacy-utility-tradeoff]]
- [[concepts/membership-inference-attack]]
- [[concepts/model-inversion-attack]]
- [[concepts/model-extraction-attack]]
- [[concepts/dynamic-model-perturbation]]
- [[concepts/gradient-inversion-defense]]
- [[entities/zhang-2025-dp-survey]]
