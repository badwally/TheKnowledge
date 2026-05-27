---
schema_version: 1
type: concept
slug: optimal-trading-thresholds
canonical_name: Optimal trading thresholds (HJB)
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Optimal trading thresholds (HJB)

## Summary

The optimal trading thresholds are two time-dependent threshold curves on the conditional bull-market probability that trigger buy and sell decisions in Dai, Yang, Zhang, and Zhu's (2015) trend-following rule; they are obtained by solving a system of Hamilton-Jacobi-Bellman equations associated with the partially observed bull-bear switching model [[sources/pdf-05df32dcb03e]].

## Key claims

- The optimal trading strategy can be described in terms of the conditional probability of a bull market and two threshold levels; a buying or selling decision is triggered when the conditional probability crosses these thresholds [[sources/pdf-05df32dcb03e]].
- The thresholds are obtained by solving a system of associated Hamilton-Jacobi-Bellman (HJB) equations [[sources/pdf-05df32dcb03e]].
- The optimal strategy involves only a finite number of trades almost surely (Lemma 2 in the paper) — a result that removes a technical condition imposed in the Dai et al. [5] companion paper [[sources/pdf-05df32dcb03e]].
- Because the solution to the HJB equation is not smooth enough to apply the Itô lemma, the verification theorem (Theorem 4) is proved using an approximation approach [[sources/pdf-05df32dcb03e]].
- The paper shows (Theorem 5) that for the optimal trading strategy the upper limit involved in defining the reward function is in fact a true limit, so the reward function makes sense in practice [[sources/pdf-05df32dcb03e]].
- The theoretical characterization of the optimal strategy obtained in Dai et al. [5] is shown (Theorem 1) to remain valid in the present self-financing model [[sources/pdf-05df32dcb03e]].
- Theorems 2 and 3 give sufficient conditions for the optimal trading boundaries to be attainable; although the conditions are not sharp, they show that under certain scenarios the boundaries are always attainable for sufficiently small transaction costs [[sources/pdf-05df32dcb03e]].
- Bounds on the value functions (Lemma 1): ρ(T−t) ≤ V_0(p,t) ≤ (μ_1 − σ²/2)(T−t) for the flat-initial case, and log(1−K_s) + ρ(T−t) ≤ V_1(p,t) ≤ log(1−K_s) + (μ_1 − σ²/2)(T−t) for the long-initial case, where K_s is the selling slippage [[sources/pdf-05df32dcb03e]].

## Sources

- [[sources/pdf-05df32dcb03e]]

## Related

- [[concepts/trend-following-trading-rule]]
- [[concepts/bull-bear-switching-model]]
- [[concepts/wonham-filter]]
- [[concepts/all-in-all-out-strategy]]
