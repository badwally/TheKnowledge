---
schema_version: 1
type: entity
slug: condo-control
canonical_name: Condo Control
entity_kind: organization
domains:
- condo-software
created_at: '2026-05-24T03:27:39Z'
last_updated: '2026-05-24T03:27:39Z'
---

# Condo Control

## Summary

Condo Control is a condominium and HOA resident-engagement / community-management platform that operates a published Yardi integration to import unit, resident, and contact data from Yardi Voyager 7S installations into the Condo Control platform [[sources/web-2026-05-24-c93]]. The integration is documented on the support.condocontrol.com knowledge base and specifies named Yardi API endpoints, minimum interface versions, and supported Yardi property types as the integration's compatibility envelope [[sources/web-2026-05-24-c93]].

## Key facts

- Operates a public-facing support knowledge base at support.condocontrol.com that documents third-party integration architecture, including the Yardi integration [[sources/web-2026-05-24-c93]].
- Integrates with Yardi by calling two named Yardi Interfaces: the Billing and Payments Interface (for financial data and Unit information / Condo Owner Type) and the Common Data Interface (for Resident information and Alternate Addresses) [[sources/web-2026-05-24-c93]].
- Calls the Yardi "GetCondoUnitInformation_Login" API endpoint from the Billing and Payments Interface to retrieve a list of Unit Numbers, Addresses, and Resident T-codes [[sources/web-2026-05-24-c93]].
- Calls the Yardi "GetResidentData" API endpoint from the Common Data Interface, passing in T-codes from GetCondoUnitInformation_Login, to retrieve Resident Names, Emails, Phone Numbers, Alternate Addresses, and Roommates (R-codes) [[sources/web-2026-05-24-c93]].
- Parses the data returned from the two Yardi Interfaces and imports it into the Condo Control platform [[sources/web-2026-05-24-c93]].
- Compatibility requirements published by Condo Control: Yardi product must be "Voyager 7S" with Interfaces minimum version PIv14.3, Billing & Payments Interface minimum version PIv7, Common Data Interface minimum version PIv14.1, and Yardi property type must be "Condo" or "Residential" [[sources/web-2026-05-24-c93]].
- Yardi property type of "Commercial" is not currently supported by the Condo Control integration [[sources/web-2026-05-24-c93]].
- Directs property managers who cannot determine compatibility to open a Support Ticket with Yardi and supply the version-and-property-type criteria for Yardi to evaluate compatibility [[sources/web-2026-05-24-c93]].

## Sources

- [[sources/web-2026-05-24-c93]] — Condo Control, "Yardi Product/Version Supported with the Yardi — Condo Control Integration" (support.condocontrol.com, May 24, 2026)

## Related

- [[entities/yardi]]
- [[entities/yardi-voyager-7s]]
- [[entities/yardi-billing-and-payments-interface]]
- [[entities/yardi-common-data-interface]]
- [[entities/buildinglink]]
