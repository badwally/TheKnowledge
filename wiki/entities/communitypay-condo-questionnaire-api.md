---
type: entity
slug: communitypay-condo-questionnaire-api
canonical_name: CommunityPay Condo Questionnaire API
entity_kind: product
domains:
  - condo-software
---

# CommunityPay Condo Questionnaire API

## Summary

The CommunityPay Condo Questionnaire API is the company's load-bearing programmatic interface for auto-filling the Fannie Mae 1076 / Freddie Mac 1077 Condominium Project Questionnaire from a live general ledger [[sources/web-2026-02-11-4eb]]. The API populates all 8 sections of the questionnaire by pulling data from named CommunityPay data models at the moment of the API call rather than from a cached export, and is positioned by CommunityPay as the structural fix to closing-delay errors that arise when boards manually reconcile insurance, financial, AR aging, governance, and legal data across disparate systems [[sources/web-2026-02-11-4eb]]. Access is consent-gated through the CARI (Community Association Risk Index) consent framework under the questionnaire:read scope, metered at 5 credits per query, and logged with a full audit trail [[sources/web-2026-02-11-4eb]].

## Key facts

### Architecture and access

- Programmatic interface — addressable by lenders, title companies, and management companies via the CARI API using an association identifier [[sources/web-2026-02-11-4eb]].
- Access is consent-gated through the CARI (Community Association Risk Index) consent framework: the HOA must authorize access [[sources/web-2026-02-11-4eb]].
- Scope name: questionnaire:read [[sources/web-2026-02-11-4eb]].
- Metering: 5 credits per query [[sources/web-2026-02-11-4eb]].
- Each query is logged with a full audit trail [[sources/web-2026-02-11-4eb]].
- Data is pulled from the live general ledger at the moment of the request, not from a cached export — described by CommunityPay as "never stale" [[sources/web-2026-02-11-4eb]].

### Section-to-data-model mapping (all 8 Form 1076 sections)

- Section 2 (Insurance) → HOAInsurancePolicy model: carrier, policy number, coverage limits, deductibles, expiration [[sources/web-2026-02-11-4eb]].
- Section 3 (Financial) → Budget + Fund models: annual budget, assessment income, operating and reserve balances [[sources/web-2026-02-11-4eb]].
- Section 4 (Delinquency) → AR Invoice model: units 30+ days past due, total amount, percentage calculation [[sources/web-2026-02-11-4eb]].
- Section 3 (Reserves portion) → Fund model + ReserveComponentService: current balance, funding target, percent funded, study date [[sources/web-2026-02-11-4eb]].
- Section 5 (Units) → Unit model: total count, types, occupancy status [[sources/web-2026-02-11-4eb]].
- Section 6 (Governance) → BoardMemberTenure + GovernanceAttestation: board composition, meeting frequency, management status [[sources/web-2026-02-11-4eb]].
- Section 7 (Special Assessments) → SpecialAssessmentRecord model: pending/approved amounts, purpose, timeline [[sources/web-2026-02-11-4eb]].
- Section 8 (Disclosures) → various models: litigation, environmental, restrictions [[sources/web-2026-02-11-4eb]].

### Response shape

- Returns a weighted data completeness score indicating how much of the questionnaire could be auto-filled [[sources/web-2026-02-11-4eb]].
- Weighting: delinquency and reserves weighted at 20% each; budget and insurance weighted at 15% each [[sources/web-2026-02-11-4eb]].
- Items that cannot be auto-filled — for example, pending litigation, which requires board confirmation — are flagged as requiring manual input [[sources/web-2026-02-11-4eb]].

### Marketed throughput comparison

- Manual process: 1–3 weeks to gather data from multiple sources; API response is immediate (seconds) [[sources/web-2026-02-11-4eb]].
- Manual data may be days or weeks old; API data is current as of the API call [[sources/web-2026-02-11-4eb]].
- Manual delinquency is calculated from a stale AR aging report; API delinquency is calculated from live invoices [[sources/web-2026-02-11-4eb]].
- Manual insurance details require manual lookup; API insurance is auto-populated from policy records [[sources/web-2026-02-11-4eb]].

## Sources

- [[sources/web-2026-02-11-4eb]] — Scott Vuilleumier, "Fannie Mae 1076 Condo Questionnaire: Why Manual Completion Fails and How Auto-Fill Changes Everything" (communitypay.us blog, February 11, 2026)

## Related

- [[entities/communitypay]]
- [[entities/cari-framework]]
- [[entities/fannie-mae-form-1076]]
- [[entities/freddie-mac-form-1077]]
- [[concepts/live-ledger-auto-fill-pattern]]
- [[concepts/fannie-mae-15-percent-delinquency-threshold]]
- [[concepts/fannie-mae-condo-project-eligibility]]
