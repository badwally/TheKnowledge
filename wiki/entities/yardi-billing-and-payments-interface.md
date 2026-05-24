---
type: entity
slug: yardi-billing-and-payments-interface
canonical_name: Yardi Billing and Payments Interface
entity_kind: product
domains:
  - condo-software
---

# Yardi Billing and Payments Interface

## Summary

The Yardi Billing and Payments Interface is one of two named Yardi API interfaces that the Condo Control integration calls to import data from Yardi Voyager 7S; the Billing and Payments Interface is the financial-data and unit-information surface, returning Unit Numbers, Addresses, and Resident T-codes (with Condo Owner Type — Renter or Owner — derived from the T-code) [[sources/web-2026-05-24-c93]]. The Condo Control integration requires the Billing and Payments Interface to be at minimum version PIv7 [[sources/web-2026-05-24-c93]].

## Key facts

- Named Yardi API interface used by the Condo Control integration for financial data and for retrieving Unit information as well as Condo Owner Type (Renter or Owner) based on the T-code [[sources/web-2026-05-24-c93]].
- Exposes the "GetCondoUnitInformation_Login" API endpoint, which returns Unit Numbers, Addresses, and Resident T-codes to the Condo Control integration [[sources/web-2026-05-24-c93]].
- T-codes returned by GetCondoUnitInformation_Login are subsequently passed by Condo Control into the Yardi Common Data Interface's GetResidentData endpoint to retrieve full resident contact data [[sources/web-2026-05-24-c93]].
- The Condo Control integration requires Billing & Payments Interface minimum version PIv7 for compatibility [[sources/web-2026-05-24-c93]].

## Sources

- [[sources/web-2026-05-24-c93]] — Condo Control, "Yardi Product/Version Supported with the Yardi — Condo Control Integration" (support.condocontrol.com, May 24, 2026)

## Related

- [[entities/yardi]]
- [[entities/yardi-voyager-7s]]
- [[entities/yardi-common-data-interface]]
- [[entities/condo-control]]
