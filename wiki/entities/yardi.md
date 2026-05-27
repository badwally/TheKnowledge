---
schema_version: 1
type: entity
slug: yardi
canonical_name: Yardi
entity_kind: organization
domains:
- condo-software
created_at: '2026-05-24T04:51:04Z'
last_updated: '2026-05-24T04:51:04Z'
---

# Yardi

## Summary

Yardi is a property management software vendor whose Voyager Condo, Co-op & HOA product is positioned as an enterprise-tier platform consolidating accounting, operations, and maintenance management for condominiums, co-operatives, and homeowner associations on a single platform with real-time analytics [[sources/web-2026-02-18-d33]]. Yardi's condo/HOA product family is organized as a multi-module stack: the Voyager Condo core, the CondoCafe resident portal, and three named add-on modules — Yardi Payment Processing, Yardi Procure to Pay, and Yardi Aspire — together marketed as the components of a "comprehensive condo, co-op and HOA management solution" [[sources/web-2026-02-18-d33]]. Yardi also operates Yardi Breeze as a distinct product line from Voyager, with a dedicated Canadian condo/strata-segment landing page at yardibreeze.ca/condo-strata-features/ marketing a base product plus regular Add-Ons and Breeze Premier Add-Ons tiers [[sources/web-2025-10-15-25b]]. Yardi is integrated with the BuildingLink resident-engagement platform, with a 24-hour resident-information sync and — uniquely among BuildingLink's 17 named accounting-integration partners — a real-time work-order sync from BuildingLink back into Yardi [[sources/web-2022-01-01-3fa]]. Yardi additionally exposes two named API interfaces — the Billing and Payments Interface and the Common Data Interface — through which the Condo Control resident-engagement platform imports unit, resident, and contact data from Yardi Voyager 7S installations of property type Condo or Residential [[sources/web-2026-05-24-c93]]. At the broader platform level, Yardi publishes a dedicated Interface Partners directory marketing 450+ trusted partners offering standard interfaces against Voyager, organized into 13 named API categories spanning the full operational surface (collections, commercial, construction, internet listing service, maintenance, master data, payables, receivables, renters insurance, revenue, screening, senior living EHR) — five of which (Collections, ILS/Guest Card, Receivables, Renters Insurance, Screening) are explicitly designated as MITS-compliant interfaces [[sources/web-2025-04-23-889]].

## Key facts

- Operates the yardi.com web domain and publishes its condo/HOA product positioning under the URL yardi.com/product/voyager-condo-co-op-hoa/ [[sources/web-2026-02-18-d33]].
- Markets Yardi Voyager Condo, Co-op & HOA as comprehensive property management software for condominiums, co-ops, and homeowner associations [[sources/web-2026-02-18-d33]].
- Operates a four-module condo/HOA product family under Voyager: Voyager Condo (core), CondoCafe (resident portal), Yardi Payment Processing, Yardi Procure to Pay, and Yardi Aspire [[sources/web-2026-02-18-d33]].
- Offers comprehensive customer support to Voyager Condo users, including live chat, phone support, and email assistance [[sources/web-2026-02-18-d33]].
- Assigns each Voyager Condo customer a dedicated account manager during the setup process [[sources/web-2026-02-18-d33]].
- Frames its Voyager Condo platform under the marketing tagline "Energized for tomorrow" [[sources/web-2026-02-18-d33]].

### Yardi Breeze product line

- Operates Yardi Breeze as a separately-branded product line distinct from the enterprise-tier Voyager platform, with its own yardibreeze.ca web domain [[sources/web-2025-10-15-25b]].
- Markets Breeze to the Canadian condo/strata segment via a dedicated landing page at yardibreeze.ca/condo-strata-features/ [[sources/web-2025-10-15-25b]].
- Positions Breeze under the marketing line "refreshingly simple condo management and HOA software" [[sources/web-2025-10-15-25b]].
- Sells Breeze as a base product with both a regular Add-Ons tier ("Power your business with optional tools") and a higher Breeze Premier Add-Ons tier ("Go further with add-ons for Breeze Premier") [[sources/web-2025-10-15-25b]].
- Markets four named Breeze Premier Add-On modules: a professional business website module, an Investor Relations module (capital-commitment tracking + CRM + investor portals), an Invoice Processing module (vendors submit invoices to Yardi for scanning and entry into Breeze Premier for customer approval), and a Vendor Payments module (paper cheque and EFT AP processing) [[sources/web-2025-10-15-25b]].

### BuildingLink integration

- Yardi syncs with BuildingLink every 24 hours; updates to resident info in Yardi appear in BuildingLink the next day [[sources/web-2022-01-01-3fa]].
- Work orders created in BuildingLink sync into Yardi in real time — the only real-time maintenance-integration cadence among BuildingLink's 17 named accounting integration partners (all other named partners use 24-hour or daily syncs) [[sources/web-2022-01-01-3fa]].
- The 24-hour resident-sync eliminates the need for staff to add or remove residents on both platforms manually [[sources/web-2022-01-01-3fa]].
- BuildingLink is independently listed by Yardi as an Interface Partner under both the Maintenance API (as "BuildingLink.com") and the Receivables API (as "BuildingLink.com Billing") [[sources/web-2025-04-23-889]].

### Condo Control integration

- Yardi exposes two named API interfaces used by the Condo Control integration: the Billing and Payments Interface (financial data and Unit information / Condo Owner Type Renter or Owner based on T-code) and the Common Data Interface (Resident information and Alternate Addresses) [[sources/web-2026-05-24-c93]].
- Condo Control calls the "GetCondoUnitInformation_Login" API endpoint from the Billing and Payments Interface, which returns Unit Numbers, Addresses, and Resident T-codes [[sources/web-2026-05-24-c93]].
- Condo Control then passes the T-codes from GetCondoUnitInformation_Login into the "GetResidentData" API endpoint from the Common Data Interface to retrieve Resident Names, Emails, Phone Numbers, Alternate Addresses, and Roommates (R-codes) [[sources/web-2026-05-24-c93]].
- For a Yardi property to be compatible with the Condo Control integration, the Yardi product must be "Voyager 7S" with Interfaces minimum version PIv14.3 [[sources/web-2026-05-24-c93]].
- The Billing & Payments Interface must be at minimum version PIv7 [[sources/web-2026-05-24-c93]].
- The Common Data Interface must be at minimum version PIv14.1 [[sources/web-2026-05-24-c93]].
- The Yardi property type must be "Condo" or "Residential"; property type "Commercial" is not currently supported by the Condo Control integration [[sources/web-2026-05-24-c93]].
- Condo Control directs property managers who cannot determine integration compatibility to open a Support Ticket with Yardi and provide the version and property-type criteria for assessment [[sources/web-2026-05-24-c93]].
- Condo Control is independently listed by Yardi as an Interface Partner under the Receivables API [[sources/web-2025-04-23-889]].

### Interface Partners ecosystem

- Publishes a dedicated Interface Partners directory at yardi.com/company/find-an-interface-partner/ marketing 450+ trusted partners offering standard interfaces against Voyager [[sources/web-2025-04-23-889]].
- Organizes the partner ecosystem into 13 named API categories: Collections API (MITS), Commercial API, Construction API, Internet Listing Service (ILS) and Guest Card (MITS compliant), Maintenance API, Master Data API, Payables API, Receivables API (MITS), Renters Insurance API (MITS), Revenue API, Screening API (MITS), and Senior Living EHR and eMAR [[sources/web-2025-04-23-889]].
- Five of the 13 API categories are explicitly designated as MITS-compliant interfaces (Collections, ILS/Guest Card, Receivables, Renters Insurance, Screening), indicating Yardi's adherence to the industry-standard Multifamily Information and Transactions Standards data interchange specification on those surfaces [[sources/web-2025-04-23-889]].
- The Collections API enables third parties to receive resident, lease, and balances information from Voyager, and to transfer lease documents and files via SFTP [[sources/web-2025-04-23-889]].
- The Commercial API is a web service interface that exports commercial data from Voyager databases including property, unit, lease, and rent roll information [[sources/web-2025-04-23-889]].
- The Construction API exports contract and job information, imports contract and change-order information, and exports job-cost configuration and retention details [[sources/web-2025-04-23-889]].
- The ILS Guest Card API allows ILS vendors to receive unit availability, pricing, floor plan, and amenity information from Voyager; third parties can provide leads, import initial guest-card information, update guest cards, and pull guest and event updates from Voyager; bi-directional web methods are also provided for student housing and senior-specific use cases [[sources/web-2025-04-23-889]].
- The Maintenance API allows third parties to pull resident, unit, and lease information from Voyager; pull work orders and updates; and push new work orders or updates to existing work orders [[sources/web-2025-04-23-889]].
- The Master Data API allows third parties to pull resident/tenant, unit, lease, and property data, and to push updates to some resident data fields [[sources/web-2025-04-23-889]].
- The Payables API allows Voyager to export vendor data, payables, and check information to a third party, and third parties to import updated and new vendors and payables (with or without check information) to Voyager [[sources/web-2025-04-23-889]].
- The Receivables API allows third parties to receive resident, unit, and lease information plus outstanding resident balances from Voyager [[sources/web-2025-04-23-889]].
- The Renters Insurance API allows third parties to pull resident, unit, and lease information; pull renters insurance policy data; and push renters insurance policy data into Voyager [[sources/web-2025-04-23-889]].
- The Revenue API incorporates unit pricing into the leasing workflow, allowing Voyager to export unit status, amenities, and lease information and third parties to import unit pricing [[sources/web-2025-04-23-889]].
- The Screening API directs applicants to the screening agency's login screen; Voyager exports applicant data to prepopulate the screening site; the third party displays the screening report and imports the application decision (accepted, denied, conditional, pending) to Voyager [[sources/web-2025-04-23-889]].
- The Receivables API vendor list explicitly names two Canadian-flagged partners: "Wyse Meter (Canadian Clients only)" and Property Vista, and includes Condo Control and TownSq among the resident-engagement / community-management vendors [[sources/web-2025-04-23-889]].
- The ILS vendor list explicitly names a Canadian variant of Property Vista ("Property Vista-ILS (Canada)"); the Maintenance vendor list separately names "Property Vista-Maintenance (Canada)" — indicating Yardi recognizes Property Vista as a Canadian-segment partner across three of its API surfaces (ILS, Maintenance, Receivables) [[sources/web-2025-04-23-889]].
- The Maintenance API vendor list names BuildingLink.com, MaintainX-adjacent vendors (Latchel, Lessen, Property Meld via Payables), Sensor Industries, SmartRent, SuiteSpot Service Requests, and Mezo among 60+ named maintenance integrations [[sources/web-2025-04-23-889]].
- The Payables API vendor list names AvidXchange, PredictAP, NetVendor, AvidXchange-class spend-management vendors (Nexus Systems, Medius Spend Management, Goby), and compliance/onboarding partners (Compliance Depot/RealPage, NetVendor, VendorPM Compliance, TrustLayer, MY COI) [[sources/web-2025-04-23-889]].

## Sources

- [[sources/web-2026-02-18-d33]] — Yardi, "Voyager Condo, Co-op & HOA" product page (yardi.com/product/voyager-condo-co-op-hoa/, February 18, 2026)
- [[sources/web-2022-01-01-3fa]] — BuildingLink, "Integration Options for Accounting" (buildinglink.com/public/integration-partners/accounting/, 2022)
- [[sources/web-2026-05-24-c93]] — Condo Control, "Yardi Product/Version Supported with the Yardi — Condo Control Integration" (support.condocontrol.com, May 24, 2026)
- [[sources/web-2025-10-15-25b]] — Yardi Breeze, "Condo & Strata Features" (yardibreeze.ca/condo-strata-features/, October 15, 2025)
- [[sources/web-2025-04-23-889]] — Yardi, "Find an Interface Partner" (yardi.com/company/find-an-interface-partner/, April 23, 2025)

## Related

- [[entities/yardi-voyager-condo]]
- [[entities/yardi-voyager-7s]]
- [[entities/yardi-billing-and-payments-interface]]
- [[entities/yardi-common-data-interface]]
- [[entities/condocafe]]
- [[entities/yardi-payment-processing]]
- [[entities/yardi-procure-to-pay]]
- [[entities/yardi-aspire]]
- [[entities/yardi-breeze]]
- [[entities/buildinglink]]
- [[entities/condo-control]]
- [[concepts/yardi-voyager-integration-architecture]]
- [[concepts/mits-data-interchange-standard|mits-data-interchange-standard]]
