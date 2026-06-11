---
schema_version: 1
type: entity
slug: zhang-2025-dp-survey
canonical_name: 'Defending Against Attacks in Deep Learning with Differential Privacy:
  A Survey (Zhang & Zhang, 2025)'
entity_kind: paper
domains:
- data-collectives
created_at: '2026-06-10T22:25:30Z'
last_updated: '2026-06-10T22:25:30Z'
draft: true
draft_started_at: '2026-06-10T22:25:30Z'
draft_unresolved_claims: 0
---

# Defending Against Attacks in Deep Learning with Differential Privacy: A Survey (Zhang & Zhang, 2025)

## Summary

"Defending against attacks in deep learning with differential privacy: a survey" is a 2025 review article in *Artificial Intelligence Review* by Xiangfei Zhang and Qingchen Zhang [[sources/web-2025-08-21-f21]]. It systematically reviews the cross-applications of differential privacy (DP) and deep learning, with the goal of using DP to defend deep learning models against privacy attacks such as membership inference, model inversion, and model extraction [[sources/web-2025-08-21-f21]]. The survey covers literature retrieved from Google Scholar and Web of Science over 2020–2025, using search keywords including "Differential Privacy AND Neural Networks/Deep Learning", "Membership Inference Attack", "Model Inversion Attack", "Model Extraction Attack", and "Differential Privacy AND Overfitting/Robustness/Fairness" [[sources/web-2025-08-21-f21]].

## Key facts

- Published online 2025-08-21 in *Artificial Intelligence Review* (Springer), DOI 10.1007/s10462-025-11350-3 [[sources/web-2025-08-21-f21]].
- Distinguishes privacy attacks targeting training data (e.g., membership inference) from those targeting models (e.g., model extraction) [[sources/web-2025-08-21-f21]].
- Reviews DP's application both to centralized deep learning and to multi-party regimes, using the example of multiple hospitals jointly training an online medical service system via federated learning [[sources/web-2025-08-21-f21]].
- Explicitly extends the analysis beyond privacy to DP's broader effects on deep neural networks: overfitting, fairness, and robustness [[sources/web-2025-08-21-f21]].
- Reports that DP has been demonstrated to enhance generalization and mitigate overfitting in deep neural networks [[sources/web-2025-08-21-f21]].
- Reports that DP can encourage unfairness in neural networks but that this issue is amenable to technical interventions [[sources/web-2025-08-21-f21]].
- Reports that the DP mechanism is more robust to poisoning attacks than other approaches, and provides robustness guarantees against adversarial attacks regardless of the specific attack implementation [[sources/web-2025-08-21-f21]].
- Argues the field should visually demonstrate the defense effects of proposed approaches rather than relying solely on rigorous mathematical proofs [[sources/web-2025-08-21-f21]].
- Situates DP relative to other privacy methods reviewed in the introduction: *k*-anonymity, *l*-diversity, homomorphic encryption, and secure multiparty computation, the latter two of which encrypt data into ciphertext rather than perturbing query outputs [[sources/web-2025-08-21-f21]].

## Sources

- [[sources/web-2025-08-21-f21]] — Zhang, X. & Zhang, Q. (2025). Defending against attacks in deep learning with differential privacy: a survey. *Artificial Intelligence Review*.

## Related

- [[concepts/differential-privacy]]
- [[concepts/privacy-budget]]
- [[concepts/membership-inference-attack]]
- [[concepts/model-inversion-attack]]
- [[concepts/model-extraction-attack]]
- [[concepts/privacy-utility-tradeoff]]
- [[concepts/dynamic-model-perturbation]]
- [[concepts/cross-silo-federated-learning]]
