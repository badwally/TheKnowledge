# Stream 1 — Economic / incentive (analytical working note)

> Working note, not canonical wiki. Canonical layer = the `data-collectives`
> concept/entity/source pages. Preserves adversarially-verified deep-research
> findings (102 agents; peer-reviewed/NBER/NeurIPS sources; no blog-only claims
> survived). Date: 2026-06-10.

## The decisive result (answers Stream 0's open question)

**Whether pooling is individually rational depends jointly on substitutability,
the mode of competition, and what is shared.**

- **Vives (1984), "Duopoly Information Equilibrium," JET 34(1):71–94** — under
  **Cournot (quantity) competition with substitutes, NOT sharing is a dominant
  strategy → Prisoner's Dilemma**; under **Bertrand (price) competition with
  substitutes, full pooling is dominant** even when your information is far
  better than your rival's; **reverses for complements.** Generalized by Raith
  (1996), JET 71:260–288. *[Verified 3-0 in deep-research. Free full-text would
  not convert (IESE PDF / paywalled JET) — source page not yet in wiki; cite by
  reference until an ingestable copy is found.]*
- **Tsoy & Konstantinov (2023), "Strategic Data Sharing between Competitors,"
  NeurIPS / arXiv:2305.16052** — contributed data also improves rivals' models,
  so collaboration can lower profits; sharing becomes rational specifically when
  products are **MORE differentiated**. → `[[sources/arxiv-2305.16052]]`,
  `[[concepts/competitor-data-sharing-tradeoff]]`,
  `[[concepts/product-differentiation-collaboration]]`.

**Implication: direct substitutes in the same local market have weak-to-negative
naive incentives to pool.** Asymmetric value capture survives mainly when
(a) contributed data is structurally **complementary**, (b) competition is on
**price** not quantity, or (c) an **architecture/side-payment** mechanism
manufactures the asymmetry. MELLODDY's measured gains concentrated where assays
**overlapped** across partners — i.e. the data was complementary even though the
firms are commercial substitutes — exactly what Vives predicts.

## Foundational economics

- **Data is nonrival** (usable by many firms at once) → increasing returns and
  large potential social gains, but the rational equilibrium is **hoarding**
  (creative-destruction fear). Jones & Tonetti, AER 110(9), 2020. →
  `[[sources/web-...aeaweb...]]` `[[concepts/nonrivalry-of-data]]`,
  `[[concepts/data-property-rights]]`, `[[entities/jones-tonetti-2020]]`.
- **Farboodi & Veldkamp, "Data and the Aggregate Economy," JEL 62(2), 2024** —
  sharing/selling more data raises modeled exit probability (competitiveness
  loss); purely business-stealing data produces zero aggregate growth.
  *[Verified 2-1. Columbia PDF would not convert — cite by reference; the
  nonrivalry core is already grounded via Jones & Tonetti.]*

## Measuring & distributing contributed value

- **Data Shapley** (Ghorbani & Zou, ICML 2019, arXiv:1904.02868): per-datum
  marginal contribution; unique payoff scheme **given** the efficiency/symmetry/
  null-player/additivity axioms. → `[[sources/arxiv-1904.02868]]`,
  `[[concepts/data-shapley]]`.
- **Caveat (verified):** uniqueness is **axiom-set-relative, not absolute** — an
  unconditional-canonicity claim was REFUTED 0-3. Semivalue successors (Beta
  Shapley, Data Banzhaf, Asymmetric Data Shapley) and "semivalue valuation is
  arbitrary and gameable" (arXiv:2506.12619, 2025) mean a gameable valuation can
  **re-open defection incentives** the Shapley axioms were meant to close.
  Computation is O(2^N) + retraining; value depends on algorithm/metric/dataset.

## Coalition stability

- **Liu & Chow (2022), Transportation Research Part B 163:64–87** — models data
  sharing as coalition partitions; **the grand coalition is NOT a foregone
  conclusion even among complements**; service complementarity does not guarantee
  market-wide sharing. *[Vertical-specific (transit); aligns with Vives & Tsoy.]*

## Adversarial caveats (carry forward)

- The Jones&Tonetti / Farboodi-Veldkamp models concern firms **selling** data
  broadly or modeled exit/business-stealing — **not peer-to-peer pooling among
  direct competitors**. Applying them to consortium pooling is an extrapolation;
  the δ-exit and business-stealing-cancellation results are **structural
  modeling assumptions, not empirical estimates**.
- The refuted "privacy/federation was THE mechanism" claim (1-2) means **custody
  preservation alone does not make contribution rational** — the *asymmetric
  ownership* design did the work, not the privacy tech.

## Open questions (seed later streams + Stage 2)

1. Any documented pool among **direct substitutes in the same local market**
   (not complementary/overlapping data, not Bertrand) that stayed individually
   rational **after subsidy ended**? Surviving evidence supplies none. (→ S7, Stage 2)
2. Which contractual/pricing mechanisms (membership pricing, tiered access,
   delayed/aggregated release, side payments) empirically convert a non-grand
   into a stable grand coalition, and at what failure rate? (→ S3 legal, Stage 2)
3. Did any MELLODDY-successor consortium reach **self-funded durability**? (→ S7)
4. Does a gameable valuation re-open defection among substitute competitors? (→ S2/S3)

## Source → wiki mapping

| Topic | Source ID | Status |
|---|---|---|
| Nonrivalry economics | (aeaweb Jones&Tonetti) | grounded |
| Substitutes/differentiation (ML) | arxiv-2305.16052 | grounded |
| Data valuation (Shapley) | arxiv-1904.02868 | grounded |
| Vives 1984 (Cournot/Bertrand result) | — | verified 3-0; full-text won't convert |
| Farboodi-Veldkamp 2024 | — | verified 2-1; PDF won't convert |
| Coalition stability (transit) | (ScienceDirect S0191261522001126) | 403 paywall; verified 3-0 |
