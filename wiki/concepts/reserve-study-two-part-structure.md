---
schema_version: 1
type: concept
slug: reserve-study-two-part-structure
canonical_name: Reserve Study Two-Part Structure (Physical Analysis + Funding Analysis)
domains:
- condo-capital-infra
created_at: '2026-05-11T17:46:04Z'
last_updated: '2026-05-11T17:46:04Z'
---
# Reserve Study Two-Part Structure (Physical Analysis + Funding Analysis)

## Summary

The reserve study two-part structure decomposes a reserve study into a Physical Analysis (component inventory, useful and remaining life, replacement cost, maintenance assumptions) and a Funding Analysis (funding goal, reserve fund income, expenditure projection, interest earnings, statement of limitations and assumptions, updating) — a methodological convention codified by the California Department of Real Estate's August 2010 Reserve Study Guidelines and broadly aligned with the CAI and APRA industry-standard practice the Guidelines explicitly defer to [[sources/pdf-dre-2010-reserve-study-guidelines]]. The same two-part decomposition appears in the Newfoundland & Labrador NLR 80/11 regulation (physical analysis + financial analysis) and is the conceptual ancestor of the BC Strata Property Regulation depreciation report's component-inventory + condition-evaluation + financial-forecasting structure — establishing the two-part decomposition as a cross-jurisdictional reserve-study convention rather than a CA-specific framing [[sources/web-2011-08-18-1e7]] [[sources/web-2013-11-28-cda]] [[sources/pdf-dre-2010-reserve-study-guidelines]].

## Key claims

### Physical analysis (DRE Guidelines decomposition)

- The Physical Analysis consists of seven steps: developing criteria for components; developing a component list; specifying the quantity of each component; determining the useful and remaining life of each component; determining the cost of replacement; using component data to develop the funding analysis; and documenting maintenance assumptions [[sources/pdf-dre-2010-reserve-study-guidelines]].
- The Physical Analysis output feeds directly into the Funding Analysis; "using component data to develop the funding analysis" is positioned within the Physical Analysis step list rather than as a Funding Analysis input, reflecting that the per-component vector of remaining life and replacement cost is the handoff artifact between the two halves of the study [[sources/pdf-dre-2010-reserve-study-guidelines]].

### Funding analysis (DRE Guidelines decomposition)

- The Funding Analysis consists of seven steps: determining the funding goal for replacement reserves; setting the desired balance; estimating association reserve fund income; projecting expenditures and reserve funding needs; estimating interest earnings of the reserve account over the funding analysis period; preparing the statement of limitations and assumptions; and updating [[sources/pdf-dre-2010-reserve-study-guidelines]].
- The Guidelines codify operationally specific Funding Analysis exhibits: Calculating the Reserve Deficit (Exhibit 5.2); Determining the Future Cost of Replacement (Exhibit 5.3); Funding Study, Estimated Cash Requirements by Year and Major Component Liability by Year (Exhibit 5.4); and the Funding Study Checklist (Exhibit 5.5) [[sources/pdf-dre-2010-reserve-study-guidelines]].

### Outputs the reserve study must enable

- The reserve study must enable three core determinations: examination of the association's repair and replacement obligations; determination of costs and timing of replacement; and determination of the availability of necessary (reserve) cash resources [[sources/pdf-dre-2010-reserve-study-guidelines]].

### Cross-jurisdictional convention

- The two-part structure parallels NLR 80/11 (Newfoundland & Labrador), which decomposes a reserve fund study into a physical analysis and a financial analysis under sections 4(1)-(8) of the regulation — establishing a cross-jurisdictional methodology convention rather than a CA-specific framing [[sources/web-2011-08-18-1e7]] [[sources/pdf-dre-2010-reserve-study-guidelines]].
- BC SPA's depreciation report requirements (Strata Property Regulation 6.2) similarly mandate a physical component inventory plus a financial forecasting section — the same two-part decomposition under a different statutory framing, with BC additionally requiring a condition evaluation as part of the physical-analysis half [[sources/web-2013-11-28-cda]] [[sources/pdf-dre-2010-reserve-study-guidelines]].
- The cross-jurisdictional persistence of the physical-analysis-plus-funding-analysis decomposition makes it a portable target for engine v1 output schema, allowing the condo-capital-infra engine's deliverable structure to satisfy CA, BC, and NL statutory requirements with shared per-component prior infrastructure [[sources/pdf-dre-2010-reserve-study-guidelines]] [[sources/web-2011-08-18-1e7]] [[sources/web-2013-11-28-cda]].

### Probabilistic methodology gap

- The DRE Guidelines describe both the Physical Analysis and the Funding Analysis methodology in deterministic point-estimate terms — useful life, remaining life, replacement cost, and inflation rate are treated as scalar inputs rather than distributions — consistent with the CAI methodology baseline the Guidelines defer to [[sources/pdf-dre-2010-reserve-study-guidelines]].
- The deterministic framing across the DRE Guidelines, NLR 80/11, and BC SPA is exactly the convention the condo-capital-infra synthesis identifies as the methodology gap the engine is built to exploit: the two-part structure is preserved in the engine's deliverable shape, but the per-step scalar inputs are replaced by posterior distributions that propagate through Monte Carlo aggregation to a funded-status confidence band rather than a single funded-vs-baseline number [[sources/docx-bf4965d0d33a]] [[sources/pdf-dre-2010-reserve-study-guidelines]].

## Sources

- [[sources/pdf-dre-2010-reserve-study-guidelines]]
- [[sources/web-2011-08-18-1e7]]
- [[sources/web-2013-11-28-cda]]
- [[sources/docx-bf4965d0d33a]]

## Related

- [[concepts/probabilistic-reserve-modeling]]
- [[concepts/tech-enabled-reserve-study-firm]]
- [[concepts/six-probabilistic-components]]
- [[concepts/regime-switching-cost-escalation]]
- [[entities/california-davis-stirling-5550]]
- [[entities/cai-reserve-study-standards]]
- [[entities/apra-reserve-preparers]]
- [[entities/dre-reserve-study-guidelines-2010]]
- [[entities/california-dre]]
- [[entities/bc-strata-property-act]]
- [[entities/nl-condominium-regulations-nlr-80-11]]
