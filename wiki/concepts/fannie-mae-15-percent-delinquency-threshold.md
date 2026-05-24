---
type: concept
slug: fannie-mae-15-percent-delinquency-threshold
canonical_name: Fannie Mae 15% Delinquency Eligibility Threshold
domains:
  - condo-software
---

# Fannie Mae 15% Delinquency Eligibility Threshold

## Summary

Fannie Mae applies a 15% delinquency-rate threshold to condominium projects: projects with more than 15% of units 30+ days delinquent on assessments may be presumptively ineligible for conventional financing, and the lender cannot make the loan without a waiver [[sources/web-2026-02-11-4eb]]. The threshold is calculated on a unit basis (units delinquent / total units), not a dollar basis, and incorrectly reporting a dollar-based delinquency rate is one of the named common errors that delays closings [[sources/web-2026-02-11-4eb]].

## Key claims

- Projects with delinquency rates exceeding 15% may be ineligible for conventional financing under Fannie Mae's project-eligibility regime [[sources/web-2026-02-11-4eb]].
- A project that exceeds the threshold is presumptively ineligible; the lender cannot make the loan without a waiver [[sources/web-2026-02-11-4eb]].
- The delinquency percentage must be calculated based on units 30+ days past due, not dollar amounts [[sources/web-2026-02-11-4eb]].
- Boards that report dollar-based delinquency rates — or that use stale AR aging reports — produce incorrect percentages and risk pushing the project over the 15% threshold [[sources/web-2026-02-11-4eb]].
- If the reported rate pushes the project over the 15% threshold, the loan may be denied until corrected [[sources/web-2026-02-11-4eb]].
- The threshold is the single most operationally consequential lender-eligibility input on the Form 1076 / 1077 questionnaire surface and is the per-query weighting reason CommunityPay's API gives delinquency a 20% weight in its data-completeness score (tied with reserves) [[sources/web-2026-02-11-4eb]].

## Sources

- [[sources/web-2026-02-11-4eb]] — Scott Vuilleumier, "Fannie Mae 1076 Condo Questionnaire: Why Manual Completion Fails and How Auto-Fill Changes Everything" (communitypay.us blog, February 11, 2026)

## Related

- [[concepts/fannie-mae-condo-project-eligibility]]
- [[entities/fannie-mae-form-1076]]
- [[entities/freddie-mac-form-1077]]
- [[entities/communitypay-condo-questionnaire-api]]
