---
type: entity
slug: hrm-pplc-building-permits-dataset
canonical_name: HRM PPLC Building Permits Dataset
entity_kind: dataset
domains:
- condo-capital-infra
---
# HRM PPLC Building Permits Dataset

## Summary

The HRM PPLC Building Permits Dataset is a 17,803-row tabular extract of Halifax Regional Municipality building-permit records covering construction, renovation, and addition activity across the HRM with per-permit work classification, occupancy type, location (community, civic address, NS Property Identifier), estimated project value, and residential unit counts [[sources/csv-7e5affc7bb1b]]. It is the primary HRM-municipal-tier complement to the provincial NS Active Condominium Corporations Dataset in the condo-capital-infra Year-1 NS market frame: where the Registrar's dataset bounds today's active corporation universe, this permits dataset surfaces the new-construction and renovation pipeline that becomes the addressable market in subsequent years [[sources/csv-7e5affc7bb1b]].

## Key facts

### Scale and shape

- 17,803 permit records across 30 columns [[sources/csv-7e5affc7bb1b]].
- Source filename `hrm-pplc-building-permits.csv` with comma delimiter and `utf-8-sig` encoding, extracted via the CSV stdlib tool [[sources/csv-7e5affc7bb1b]].
- Permit numbers carry three observed prefixes: `BP-` (legacy), `BPRES-` (residential), and `BPCOM-` (mixed-use & commercial) [[sources/csv-7e5affc7bb1b]].
- Visible permit dates span 2021 through 2026, with permit-issuance dates from early 2021 to early 2026 [[sources/csv-7e5affc7bb1b]].

### Schema (30 columns)

- Permit identification: `Permit_Number`, `Date_of_Submission`, `Date_of_Permit_Issuance`, `Completed_Date`, `Expiration_Date`, `Permit_Name`, `Permit_Status` [[sources/csv-7e5affc7bb1b]].
- Work classification: `Work_Type` (e.g., New Building, Renovation, Addition), `Primary_Work_Scope` [[sources/csv-7e5affc7bb1b]].
- Location: `Civic_ID`, `Civic_Number`, `Street_Name`, `Community`, `PID` (NS Property Identifier) [[sources/csv-7e5affc7bb1b]].
- Project value and inspection: `Estimated_Project_Value`, `Most_Recent_Inspection` [[sources/csv-7e5affc7bb1b]].
- Structure and occupancy: `Type_of_Structure`, `Occupancy_Type` [[sources/csv-7e5affc7bb1b]].
- Residential unit counts: `Existing_Residential_Units`, `Total_End_Residential_Units` [[sources/csv-7e5affc7bb1b]].

### Permit-status taxonomy (observed)

- Issued, Completed, Expired, Cancelled, Withdrawn, Applicant Revisions, Application Incomplete, Amendment Application Incomplete, Expired (Closed) [[sources/csv-7e5affc7bb1b]].

### Structure-type taxonomy (observed)

- Dwelling - Single Detached, Dwelling - Semi-Detached, Dwelling - Townhouse, Dwelling - Multiple Units, Dwelling - Backyard Suite, Accessory Structure, Mixed Use - Residential & Other Use(s), Commercial, Institutional and Governmental [[sources/csv-7e5affc7bb1b]].
- `Type_of_Structure` = "Dwelling - Multiple Units" is the structure-type filter that maps to multi-unit residential — the addressable population for future condo corporations [[sources/csv-7e5affc7bb1b]].

### Occupancy-type taxonomy (observed)

- Residential Use, Secondary Suite, Retail Use, Restaurant, Parking Structure, Garage, Laboratory / Research Use, Post-Secondary Institution [[sources/csv-7e5affc7bb1b]].

### Geographic scope (observed communities)

- Urban core: Halifax, Dartmouth, Bedford [[sources/csv-7e5affc7bb1b]].
- Suburban: Lower Sackville, Middle Sackville, Upper Sackville, Beaver Bank, Hammonds Plains, Fall River, Waverley, Windsor Junction [[sources/csv-7e5affc7bb1b]].
- Rural / coastal: Eastern Passage, Brookside, Mineville, Cow Bay, Spry Bay, East Preston, Head of Chezzetcook, Lawrencetown, Porters Lake, West Porters Lake, Boutiliers Point, Portuguese Cove, Lewis Lake, Montague Gold Mines [[sources/csv-7e5affc7bb1b]].

### Estimated project value (observed range)

- Smallest observed value $10,000 (commercial renovation, Halifax) [[sources/csv-7e5affc7bb1b]].
- Largest observed value $62,750,000 (institutional & governmental new building with parking-structure occupancy, Fall River) [[sources/csv-7e5affc7bb1b]].
- Intermediate residential multi-unit values include $432,169 (48-unit renovation, Halifax), $500,000 (7-unit new-build, Dartmouth), and $300,000 (semi-detached new-build, Eastern Passage) [[sources/csv-7e5affc7bb1b]].

### Cross-reference value

- The `PID` column (NS Property Identifier) is the join key against the NS Active Condominium Corporations Dataset's `pid` and `pid_corp` columns, enabling permit-history attribution to specific registered corporations [[sources/csv-7e5affc7bb1b]].
- The `Type_of_Structure` = "Dwelling - Multiple Units" filter combined with `Work_Type` = "New Building" surfaces the new-condominium-eligible construction pipeline; the same structure filter combined with `Work_Type` = "Renovation" or "Addition" surfaces capital-renewal activity on existing multi-unit stock [[sources/csv-7e5affc7bb1b]].
- `Total_End_Residential_Units` minus `Existing_Residential_Units` yields net unit additions per permit — the unit-addition pipeline metric for the HRM market frame [[sources/csv-7e5affc7bb1b]].

## Sources

- [[sources/csv-7e5affc7bb1b]]

## Related

- [[entities/halifax-regional-municipality]]
- [[entities/ns-active-condo-corporations-dataset]]
- [[entities/ns-registrar-condominiums]]
