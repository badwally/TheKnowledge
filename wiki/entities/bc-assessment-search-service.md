---
schema_version: 1
type: entity
slug: bc-assessment-search-service
canonical_name: BC Assessment Search Service
entity_kind: dataset
domains:
- condo-capital-infra
created_at: '2026-05-19T14:51:42Z'
last_updated: '2026-05-27T19:12:45Z'
finalized_at: '2026-05-27T19:12:45Z'
---
# BC Assessment Search Service

## Summary

The BC Assessment Search Service is the publicly available online property-information service operated by BC Assessment, providing per-property assessed value, property description, building attributes, and additional information across most taxable British Columbia properties [[sources/web-2026-05-19-00f]]. The service is explicitly restricted to private, personal, non-commercial use by a Terms of Use legal agreement between BC Assessment and any user of the service, with commercial access requiring direct engagement with BC Assessment — making the commercial-use prohibition the load-bearing legal constraint for any automated covariate adapter built against the condo-capital-infra engine's BC wave under ADR-0004 [[sources/web-2026-05-19-00f]]. The service exposes a per-property data schema — civic address, area / jurisdiction / roll number, parcel ID, total assessed value with land and building value breakdown plus prior-year comparators, building-attribute fields (year built, description, bedrooms, bathrooms, carports, garages, land size, first-floor area, second-floor area, basement finish area), strata-specific additional fields (strata area, building storeys, number of apartment units), commercial-property additional fields (gross leasable area, net leasable area), manufactured-home dimensions, and 3-year sales history — that defines the BC covariate ingest schema available without commercial-license negotiation [[sources/web-2026-05-19-00f]]. The Search Service ToS is one of two BC Assessment surfaces codifying the commercial-use prohibition: the data-product-inventory page operated by BC Assessment (see `[[entities/bc-assessment]]`) carries a parallel Privacy Notification with the same commercial-use prohibition framing, confirming a multi-surface ToS posture across BC Assessment's per-property and province-aggregate data products [[sources/web-2026-01-02-6fe]].

## Key facts

### Service identity and access

- Publicly available online service operated by BC Assessment [[sources/web-2026-05-19-00f]].
- Restricted to private, personal, non-commercial use — businesses wishing to learn more about commercial access to assessment information are directed to contact BC Assessment at 1-866-valueBC (1-866-825-8322 Ext. 00118) [[sources/web-2026-05-19-00f]].
- Service use is governed by a Terms of Use legal agreement between BC Assessment and any user of the service; it is assumed by BC Assessment that use of the service provides agreement with the terms of use [[sources/web-2026-05-19-00f]].
- The Terms of Use can be reviewed and printed from the main page of the service by clicking the link available under the search bar [[sources/web-2026-05-19-00f]].
- The Terms of Use specify, among other things, the legal use of the service which the user must adhere to [[sources/web-2026-05-19-00f]].

### Coverage scope

- Provides easy access to property information about most taxable properties across British Columbia [[sources/web-2026-05-19-00f]].
- Coverage exclusions: some Indigenous properties; properties with certain use codes including recreational properties such as parks and playing fields; major industrial properties such as pulp mills and utilities [[sources/web-2026-05-19-00f]].
- Inclusion of Indigenous-community property information requires special agreements negotiated by BC Assessment prior to inclusion; agreements do not exist for every Indigenous community, and some Indigenous communities with an agreement have not yet submitted their property information [[sources/web-2026-05-19-00f]].
- Property owners do not have the authority to request that their BC Assessment information be removed from the Assessment Search service [[sources/web-2026-05-19-00f]].

### Search inputs (per-property identifiers)

- Address: typed using the format provided at the bottom of the assessment notice, including special characters and spaces [[sources/web-2026-05-19-00f]].
- Roll number: requires entry of jurisdiction number (located above the roll number at the top right of the assessment notice) first, followed by the roll number — example: jurisdiction 308 + roll 519500059 [[sources/web-2026-05-19-00f]].
- Plan: not a unique identifier — requires combination of plan number, lot number, jurisdiction number (without city/town), and roll number — example: plan VIP4888 and lot 5 [[sources/web-2026-05-19-00f]].
- PID (Parcel Identifier): located in the Property Location & Description box on the assessment notice; dashes are not required when searching by PID — example: 012345678 [[sources/web-2026-05-19-00f]].
- Search bar offers auto-complete with the first 10 matching options [[sources/web-2026-05-19-00f]].

### Per-property data schema (when available and applicable)

- **Property information**: civic address (apt/house #, street name, city, postal code); area, jurisdiction, roll number; street front or Google image; legal description; parcel ID (PID) [[sources/web-2026-05-19-00f]].
- **Assessment information**: total assessed value; property assessment date; land value; building(s) value; previous total value; previous land value; previous building(s) value [[sources/web-2026-05-19-00f]].
- **Building information**: year built; description (type of building plus descriptive information); number of bedrooms; number of bathrooms; carports; garages; land size; first floor area; second floor area; basement finish area [[sources/web-2026-05-19-00f]].
- **Strata-specific additional fields (when applicable)**: strata area; building storeys; number of apartment units [[sources/web-2026-05-19-00f]].
- **Commercial-property additional fields (when applicable)**: gross leasable area; net leasable area [[sources/web-2026-05-19-00f]].
- **Manufactured-home additional fields (when applicable)**: width, length, total area [[sources/web-2026-05-19-00f]].
- **Sales history**: within the last 3 full calendar years [[sources/web-2026-05-19-00f]].
- **Comments**: e.g., property has more than one structure [[sources/web-2026-05-19-00f]].
- Basement area, while calculated into assessed value, is NOT reported in Assessment Search for Townhouses [[sources/web-2026-05-19-00f]].

### Strata-property search semantics

- A strata building is searched using the same address-search interface as any other property [[sources/web-2026-05-19-00f]].
- When the address search determines that a strata building is being searched on, the service displays a subset of the units and indicates on the first line or two the option to list all of the strata units [[sources/web-2026-05-19-00f]].
- Selecting "select to see all units…" navigates to a page with the full list of strata units within the building, from which individual units can be selected [[sources/web-2026-05-19-00f]].

### Description-field building-quality taxonomy

- The description field describes the primary structure on the property and defines the type of building (e.g., strata apartment, retail store, house) with additional descriptive information [[sources/web-2026-05-19-00f]].
- For houses, the description includes the number of storeys and a quality rating to assist in finding appropriate comparable properties [[sources/web-2026-05-19-00f]].
- Quality ratings (lowest to highest): Basic (modest, economical housing of its era, minimal design features); Standard (typical for its era, basic building code compliance, average quality materials); Semi custom (more complex design features, better-than-average materials and amenities); Custom (considerable attention to architectural design and decorative features, good-quality building materials) [[sources/web-2026-05-19-00f]].
- The particular characteristics used to categorize a dwelling depend on the era when it was built [[sources/web-2026-05-19-00f]].
- Number of storeys is the number of distinct levels of living space above the basement, crawl space, or slab foundation; the level containing the living room and kitchen is typically counted as the first storey; a half storey level has exterior walls less than full height [[sources/web-2026-05-19-00f]].

### Update cadence

- Assessments are updated annually and represent the property value as of July 1st of the prior assessment year [[sources/web-2026-05-19-00f]].
- A second, smaller update occurs in April of each year to reflect the decisions of the Property Assessment Review Panels (PARP) [[sources/web-2026-05-19-00f]].
- Property details are updated on January 1st (before property assessment notices are sent out) and again in early April [[sources/web-2026-05-19-00f]].
- Owner-submitted updates received between April and November are reflected in Assessment Search in the January update [[sources/web-2026-05-19-00f]].
- Properties under construction (not renovations) do not show updated information until construction has been completed [[sources/web-2026-05-19-00f]].
- The province-wide aggregate roll is published in early January each year (the 2026 roll was released January 2, 2026 reflecting July 1, 2025 market values), consistent with the per-property January 1 details update cadence surfaced through the Search Service [[sources/web-2026-01-02-6fe]].

### Property images

- Nearly 80% of properties include images [[sources/web-2026-05-19-00f]].
- Three kinds of property images displayed: BC Assessment street front images; Google Maps API street front images; and BC Assessment images that are not street front images but are posted at property owner request (the third option is available only if strict conditions are met) [[sources/web-2026-05-19-00f]].
- Images are taken from a vantage point accessible to members of the public (street or sidewalk); BC Assessment blurs portions of images including vehicle license plates and faces of people [[sources/web-2026-05-19-00f]].
- Each image obtained through the street front program has been confirmed to comply with British Columbia's privacy legislation [[sources/web-2026-05-19-00f]].
- Property owners do not have the authority to request that their property not display an image, but Google provides a separate process for requesting that Google Street View images of a property be blurred [[sources/web-2026-05-19-00f]].

### Registered accounts

- Two types of registered accounts: BC Assessment Account (requires valid email address and password) and BC Services Card account [[sources/web-2026-05-19-00f]].
- When logged in with any registered account, users can access enhanced features including adding favourites, comparing properties, and using the interactive map [[sources/web-2026-05-19-00f]].

### Scheduled maintenance

- BC Assessment performs scheduled maintenance on Sunday between 6am and 9am Pacific; during this window the Assessment Search service and other portions of the BC Assessment website may be unresponsive for short periods [[sources/web-2026-05-19-00f]].

### Parallel ToS surface (data-product inventory page)

- BC Assessment's data-product inventory page (the property-information-trends surface operated by BC Assessment for province-wide aggregate statistics) carries a distinct Privacy Notification with parallel commercial-use prohibition framing: "Any commercial use of this data in whole or in part, directly or indirectly, including the use of such data for business, residential address or telephone directory services or any solicitation service is specifically prohibited" [[sources/web-2026-01-02-6fe]].
- The data-product inventory page exposes province-aggregate data products (Top 500 Highest Residential Properties, Assessment Roll Total Value, Assessment Roll Total Value by Property Class, Assessment Roll Total Value by Area and Property Class, BC Property Count, Property Count by Subclass, New Construction) — a different data surface from the Search Service's per-property records, but governed by the same commercial-use-prohibition posture [[sources/web-2026-01-02-6fe]].
- The two-surface commercial-use prohibition (Search Service Terms of Use + data-product inventory Privacy Notification) confirms BC Assessment operates a multi-surface ToS posture across both per-property and province-aggregate data products; the can-pilot Vancouver wave tos.py adapter must encode both prohibition notices to remain defensibly compliant [[sources/web-2026-01-02-6fe]] [[sources/web-2026-05-19-00f]].

### Implication for condo-capital-infra GTM

- The per-property data schema defines the BC covariate ingest layer available for any BC-wave reserve-study adapter under ADR-0004's Canada-first sequence: year_built, building_storeys, number_of_apartment_units, strata_area, building description, and 3-year sales history are the highest-value building-stock-characterization fields for strata-property targeting [[sources/web-2026-05-19-00f]].
- The commercial-use prohibition forces any automated covariate-acquisition pipeline to choose between three paths: (a) commercial-access licensing negotiated directly with BC Assessment via Ext. 00118; (b) authorized-user upload model (the Eli Report data-acquisition pattern, where users with legal access to documents drive ingest); or (c) substitution from municipal permit feeds, open-data sources, and other public datasets — the project's can-pilot ToS adapter must operate under one of these three paths and cannot rely on uncontracted automated scraping [[sources/web-2026-05-19-00f]].
- The April PARP-driven update cycle is a refresh-cadence input for any BC adapter design: appeals filed January 1-31 are resolved by PARP and reflected in Assessment Search in April, making April-refreshed data more authoritative than January-refreshed data for prior-year-disputed properties [[sources/web-2026-05-19-00f]].
- The residual-method strata land valuation (total market value minus depreciated building value equals land value) is a methodological data point for understanding how BC Assessment depreciates buildings in the context of strata properties — the depreciation framework is upstream of the per-strata building-value field exposed in the service, but the underlying method is published in a separate BC Assessment fact sheet on valuation of residential strata properties [[sources/web-2026-05-19-00f]].

## Sources

- [[sources/web-2026-05-19-00f]]
- [[sources/web-2026-01-02-6fe]]

## Related

- [[entities/bc-assessment]]
- [[entities/bc-strata-property-act]]
