---
schema_version: 1
type: entity
slug: halifax-regional-municipality
canonical_name: Halifax Regional Municipality
entity_kind: organization
domains:
- condo-capital-infra
created_at: '2026-05-10T22:54:48Z'
last_updated: '2026-05-10T22:54:48Z'
---
# Halifax Regional Municipality

## Summary

Halifax Regional Municipality (HRM) is the Nova Scotia municipal jurisdiction whose building-permit issuance is captured in the 17,803-record HRM PPLC Building Permits Dataset — the per-permit data feed of work classification, structure type, occupancy type, location, estimated project value, and residential unit counts spanning 2021-2026 used as the municipal-tier construction-pipeline anchor for the condo-capital-infra Year-1 NS market frame [[sources/csv-7e5affc7bb1b]].

## Key facts

- Issuing authority for the building-permit records compiled in the HRM PPLC Building Permits Dataset, with permit-issuance dates observed across 2021 through early 2026 [[sources/csv-7e5affc7bb1b]].
- HRM permit numbering uses three observed prefix conventions: `BP-` (legacy), `BPRES-` (residential building permit), and `BPCOM-` (mixed-use & commercial building permit) [[sources/csv-7e5affc7bb1b]].
- HRM's permit lifecycle taxonomy includes Issued, Completed, Expired, Cancelled, Withdrawn, Applicant Revisions, Application Incomplete, Amendment Application Incomplete, and Expired (Closed) statuses [[sources/csv-7e5affc7bb1b]].
- Communities recorded in HRM building-permit records span an urban-suburban-rural gradient: urban core (Halifax, Dartmouth, Bedford); suburban (Lower / Middle / Upper Sackville, Beaver Bank, Hammonds Plains, Fall River, Waverley, Windsor Junction); rural / coastal (Eastern Passage, Brookside, Mineville, Cow Bay, Spry Bay, East Preston, Head of Chezzetcook, Lawrencetown, Porters Lake, West Porters Lake, Boutiliers Point, Portuguese Cove, Lewis Lake, Montague Gold Mines) [[sources/csv-7e5affc7bb1b]].
- HRM uses the NS Property Identifier (`PID`) on its permit records, providing a direct join key into the provincial NS Active Condominium Corporations Dataset published by the Service Nova Scotia Registrar of Condominiums [[sources/csv-7e5affc7bb1b]].

## Sources

- [[sources/csv-7e5affc7bb1b]]

## Related

- [[entities/hrm-pplc-building-permits-dataset]]
- [[entities/ns-active-condo-corporations-dataset]]
- [[entities/ns-registrar-condominiums]]
