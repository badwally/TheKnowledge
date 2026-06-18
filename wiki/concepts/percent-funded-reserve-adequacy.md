---
schema_version: 1
type: concept
slug: percent-funded-reserve-adequacy
canonical_name: Percent-Funded Reserve Adequacy Assessment
domains:
- condo-capital-infra
created_at: '2026-06-10T05:00:38Z'
last_updated: '2026-06-10T05:00:38Z'
---

# Percent-Funded Reserve Adequacy Assessment

## Summary

Percent-funded reserve adequacy assessment is a deterministic methodology class for reserve fund analysis that expresses the current funded balance as a percentage of the fully-funded target balance, producing a single adequacy score and threshold-based risk classifications. REcollab's RECOStudy™ exemplifies this approach: its primary output is a percent-funded gauge (documented example: 17% = "low") paired with a special-assessment risk year flag (documented example: 2029, "High Risk"). [[sources/web-2026-01-01-84c]] This methodology class is structurally distinct from probabilistic reserve fund analysis, which produces P10/P50/P90 confidence intervals and Monte Carlo expenditure distributions rather than a single adequacy score.

## Key claims

- RECOStudy™ (REcollab) presents a percent-funded gauge as its primary financial health indicator; a documented example shows 17% flagged as "low" [[sources/web-2026-01-01-84c]]
- RECOStudy™ derives a special-assessment risk year flag from the adequacy score — a deterministic single-year projection of when a special assessment becomes likely; documented example: 2029, "High Risk" [[sources/web-2026-01-01-84c]]
- Percent-funded adequacy framing does not produce confidence intervals (P10/P50/P90) and does not incorporate Monte Carlo simulation [[sources/web-2026-01-01-84c]]
- A percent-funded adequacy system can be implemented without a manual site inspection, relying on document upload and an expert-built dataset to derive component inventory and cost estimates [[sources/web-2026-01-01-84c]]
- The adequacy score and risk flag together constitute the complete probabilistic-risk surface exposed to boards and property managers in this methodology class, contrasting with distribution-based outputs in Monte Carlo approaches [[sources/web-2026-01-01-84c]]

## Sources

- [[sources/web-2026-01-01-84c]] — RECOStudy™ core product page; establishes percent-funded gauge UI and SA risk year flag as primary deterministic adequacy outputs

## Related

- [[concepts/monte-carlo-reserve-confidence-intervals]] — probabilistic alternative; produces P10/P50/P90 confidence intervals and full expenditure distributions
- [[concepts/reserve-fund-contribution-smoothing]] — contribution optimization layer that sits above adequacy assessment in reserve planning
- [[concepts/living-reserve-study]] — SmartProperty's branded live reserve study; also deterministic in output framing
- [[entities/recollab]] — vendor whose RECOStudy™ product implements percent-funded adequacy framing
- [[entities/smartproperty]] — vendor with a comparable live reserve study dashboard
- [[entities/propfusion]] — U.S. reserve-study SaaS; adequacy-based framing
