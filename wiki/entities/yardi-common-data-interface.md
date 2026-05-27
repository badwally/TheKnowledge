---
schema_version: 1
type: entity
slug: yardi-common-data-interface
canonical_name: Yardi Common Data Interface
entity_kind: product
domains:
- condo-software
created_at: '2026-05-24T03:27:39Z'
last_updated: '2026-05-24T03:27:39Z'
---

# Yardi Common Data Interface

## Summary

The Yardi Common Data Interface is one of two named Yardi API interfaces that the Condo Control integration calls to import data from Yardi Voyager 7S; the Common Data Interface is the resident-contact-data surface, returning Resident Names, Emails, Phone Numbers, Alternate Addresses, and Roommates (R-codes) when called with T-codes obtained from the Billing and Payments Interface [[sources/web-2026-05-24-c93]]. The Condo Control integration requires the Common Data Interface to be at minimum version PIv14.1 [[sources/web-2026-05-24-c93]].

## Key facts

- Named Yardi API interface used by the Condo Control integration for retrieving Resident information and Alternate Addresses [[sources/web-2026-05-24-c93]].
- Exposes the "GetResidentData" API endpoint, which accepts T-codes as input and returns Resident Names, Emails, Phone Numbers, Alternate Addresses, and Roommates (R-codes) [[sources/web-2026-05-24-c93]].
- T-codes passed to GetResidentData are obtained from a prior call to the Yardi Billing and Payments Interface's GetCondoUnitInformation_Login endpoint [[sources/web-2026-05-24-c93]].
- The Condo Control integration requires Common Data Interface minimum version PIv14.1 for compatibility [[sources/web-2026-05-24-c93]].

## Sources

- [[sources/web-2026-05-24-c93]] — Condo Control, "Yardi Product/Version Supported with the Yardi — Condo Control Integration" (support.condocontrol.com, May 24, 2026)

## Related

- [[entities/yardi]]
- [[entities/yardi-voyager-7s]]
- [[entities/yardi-billing-and-payments-interface]]
- [[entities/condo-control]]
