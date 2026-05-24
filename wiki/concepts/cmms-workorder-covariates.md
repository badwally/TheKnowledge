---
type: concept
slug: cmms-workorder-covariates
canonical_name: CMMS Work-Order Covariates
domains:
- condo-capital-infra
---
# CMMS Work-Order Covariates

## Summary

CMMS work-order covariates are the use of historical work-order records — from systems like UpKeep, MaintainX, Fiix, Limble, and Buildium — as input features in component-level survival and degradation models, allowing reserve forecasts to update from real-world maintenance signal rather than visual inspection alone [[sources/docx-bf4965d0d33a]]. The condo-capital-infra synthesis identifies CMMS work-order history as the best leading indicator of component degradation today and notes that no reserve product currently reads it — making it a high-leverage data integration for an AI-native reserve study firm [[sources/docx-bf4965d0d33a]].

## Key claims

- Work-order history from CMMS platforms is the best leading indicator of component degradation, but no reserve-study product today reads it [[sources/docx-bf4965d0d33a]].
- The CMMS layer (UpKeep, MaintainX, Fiix, Limble) is invisible in current reserve software [[sources/docx-bf4965d0d33a]].
- The recommended Year 1 build includes automated ingest of CMMS work-order history (UpKeep, MaintainX, Buildium) as covariates feeding the component RUL distributions [[sources/docx-bf4965d0d33a]].
- This is part of the broader rationale for excluding hardware in the 24-month window: the data needed to beat incumbents already exists and is unused [[sources/docx-bf4965d0d33a]].
- Work-order / CMMS history is named in the planned methods scan as a covariate in survival models, alongside sensor fusion and POMDP framing for inspection scheduling [[sources/docx-bf4965d0d33a]].
- BC provincial guidance (BC Housing Maintenance Matters #11) recommends stratas administer a "central and organized database of all pertinent reference information" capturing completed maintenance tasks and inspection results, both to ensure continuity across strata council turnover and to demonstrate due diligence to warranty providers and prospective purchasers — providing regulatory-context grounding for the engine's CMMS work-order ingest [[sources/pdf-bc-housing-2020-maintenance-matters-11]].
- BC Housing's bulletin assigns the "program administrator" role primary responsibility for documenting completion of maintenance tasks, recording inspection results, gathering long-term maintenance and renewals information, developing annual task lists informed by a building envelope specialist, developing and tracking budgets, and reporting findings (including recommended next-year budget and an updated project schedule of key priorities) to the strata council — structuring the work-order record-keeping that becomes input to a survival model [[sources/pdf-bc-housing-2020-maintenance-matters-11]].
- BC Housing frames the maintenance-and-renewals program as a Plan-Do-Check-Adjust cycle: as the program is implemented the strata learns more about the building and its maintenance and renewals needs, the plan is refined and updated, and over time this cyclical pattern produces an efficient and reliable program — operationally, the data-flywheel pattern the engine relies on for prior updating [[sources/pdf-bc-housing-2020-maintenance-matters-11]].

## Sources

- [[sources/docx-bf4965d0d33a]]
- [[sources/pdf-bc-housing-2020-maintenance-matters-11]]

## Related

- [[concepts/probabilistic-reserve-modeling]]
- [[concepts/six-probabilistic-components]]
- [[concepts/tech-enabled-reserve-study-firm]]
- [[concepts/strata-maintenance-renewals-program]]
- [[entities/facilio]]
- [[entities/bc-strata-property-act]]
