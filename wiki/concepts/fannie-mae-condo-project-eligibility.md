---
schema_version: 1
type: concept
slug: fannie-mae-condo-project-eligibility
canonical_name: Fannie Mae Condo Project Eligibility Classification
domains:
- condo-software
created_at: '2026-05-24T03:40:38Z'
last_updated: '2026-05-24T03:40:38Z'
---

# Fannie Mae Condo Project Eligibility Classification

## Summary

Fannie Mae classifies condominium projects into one of four eligibility categories — Established, New, Two-to-Four Unit, or Ineligible — based on the answers reported on the Form 1076 Condominium Project Questionnaire, and assigns underwriting consequences to each [[sources/web-2026-02-11-4eb]]. The classification is gated by six named red flags (delinquency >15%, missing/inadequate master insurance, pending litigation, single-entity >10% ownership, budget with negative cash flow, no reserve study or inadequate reserves) that can downgrade a project to Ineligible or trigger enhanced review [[sources/web-2026-02-11-4eb]].

## Key claims

### Four eligibility categories

- Established: developer turnover complete, budgets adopted, reserves funded → standard underwriting [[sources/web-2026-02-11-4eb]].
- New: developer still in control, project recently completed → enhanced review required [[sources/web-2026-02-11-4eb]].
- Two-to-Four Unit: small projects → simplified review [[sources/web-2026-02-11-4eb]].
- Ineligible: >15% delinquency, pending litigation affecting habitability, or inadequate insurance → loan denied [[sources/web-2026-02-11-4eb]].

### Six named red flags

- Delinquency >15%: the project is presumptively ineligible; the lender cannot make the loan without a waiver [[sources/web-2026-02-11-4eb]].
- No master insurance policy, or a policy with inadequate coverage: the lender requires specific minimums [[sources/web-2026-02-11-4eb]].
- Pending litigation: depending on nature and amount, may make the project ineligible [[sources/web-2026-02-11-4eb]].
- Single entity >10% ownership: investor concentration risk; may require enhanced review [[sources/web-2026-02-11-4eb]].
- Budget with negative cash flow: operating expenses exceeding income signals financial distress [[sources/web-2026-02-11-4eb]].
- No reserve study, or reserves below a reasonable threshold (typically 10% of budget) [[sources/web-2026-02-11-4eb]].

## Sources

- [[sources/web-2026-02-11-4eb]] — Scott Vuilleumier, "Fannie Mae 1076 Condo Questionnaire: Why Manual Completion Fails and How Auto-Fill Changes Everything" (communitypay.us blog, February 11, 2026)

## Related

- [[entities/fannie-mae-form-1076]]
- [[entities/freddie-mac-form-1077]]
- [[concepts/fannie-mae-15-percent-delinquency-threshold]]
- [[entities/communitypay-condo-questionnaire-api]]
