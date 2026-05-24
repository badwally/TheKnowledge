---
id: csv-7e5affc7bb1b
type: csv
title: hrm-pplc-building-permits
url: ''
authors: []
ingested_at: '2026-05-10T22:50:46Z'
content_hash: sha256:2d56ca251888cc887600ecb9ea93ea6da48ac08416a9016be87f06e45b0c6de6
source_path: raw/csv/csv-7e5affc7bb1b.csv
domains:
- condo-capital-infra
nlm_corpus_ids: []
wiki_pages:
- wiki/entities/hrm-pplc-building-permits-dataset.md
- wiki/entities/halifax-regional-municipality.md
- wiki/entities/ns-active-condo-corporations-dataset.md
meta:
  row_count: 17803
  column_count: 30
  columns:
  - Permit_Number
  - Date_of_Submission
  - Date_of_Permit_Issuance
  - Completed_Date
  - Expiration_Date
  - Permit_Name
  - Work_Type
  - Primary_Work_Scope
  - Permit_Status
  - Civic_ID
  - Civic_Number
  - Street_Name
  - Community
  - PID
  - Estimated_Project_Value
  - Most_Recent_Inspection
  - Type_of_Structure
  - Occupancy_Type
  - Existing_Residential_Units
  - Total_End_Residential_Units
  delimiter: ','
  encoding: utf-8-sig
  original_filename: hrm-pplc-building-permits.csv
  extraction_tool: csv (stdlib)
filter:
  score: 0.85
  policy_version: condo-capital-infra-v1
  rationale: Raw HRM building permits dataset (17,803 rows) covering Halifax Regional
    Municipality — directly load-bearing for the Atlantic Canada market frame per
    ADR-0004 and Brief-0006, providing multi-family/condo-relevant building stock
    vintage, Type_of_Structure (Dwelling - Multiple Units), Occupancy_Type, and Estimated_Project_Value
    data needed to scope the Halifax design-partner engagement and Y1-Y2 expansion.
    Per the calibration precedent (csv-2bfb1a74edee), raw market-sizing data anchoring
    the primary GTM jurisdiction should not be penalized for lacking actuarial methodology.
  decided_at: '2026-05-10T22:50:55Z'
  user_correction: null
---
# hrm-pplc-building-permits

CSV with **17803** data rows × **30** columns.

| Permit_Number | Date_of_Submission | Date_of_Permit_Issuance | Completed_Date | Expiration_Date | Permit_Name | Work_Type | Primary_Work_Scope | Permit_Status | Civic_ID | Civic_Number | Street_Name | Community | PID | Estimated_Project_Value | Most_Recent_Inspection | Type_of_Structure | Occupancy_Type | Existing_Residential_Units | Total_End_Residential_Units |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BPRES-2022-10581 | 7/29/2022 12:00:00 PM | 8/31/2022 12:00:00 PM |  | 8/20/2026 12:00:00 PM | Residential Building Permit | New Building | New Building | Issued | 35492 | 68 | LIVELY RD | MIDDLE SACKVILLE | 40139974 | 25000 |  | Accessory Structure | Residential Use |  |  |
| BPCOM-2024-08561 | 6/28/2024 12:00:00 PM | 7/24/2024 12:00:00 PM |  | 7/24/2026 12:00:00 PM | Mixed Use & Commercial Building Permit | Renovation | Renovation | Issued | 66294 | 3601 | JOSEPH HOWE DR | HALIFAX | 00181461 | 98000 |  | Commercial | Retail Use |  |  |
| BPRES-2024-09805 | 7/23/2024 12:00:00 PM | 7/26/2024 12:00:00 PM | 11/4/2024 12:00:00 PM | 7/26/2026 12:00:00 PM | Residential Building Permit | Renovation | Renovation | Completed | 104688 | 7 | CRAIGBURN DR | DARTMOUTH | 00274605 | 44000 | Building - Part 9 - Final | Dwelling - Single Detached | Residential Use | 1 | 1 |
| BP-2021-09989 | 5/28/2021 12:00:00 PM | 11/4/2021 12:00:00 PM | 11/26/2025 12:00:00 PM | 12/13/2027 12:00:00 PM | Residential Building Permit | New Building | New Building | Completed | 177255 | 26 | WESLYNN GATE | BEDFORD | 00359885 | 600000 | Building - Part 9 - Final | Dwelling - Townhouse | Residential Use |  | 3 |
| BPRES-2021-17179 | 1/4/2022 12:00:00 PM | 1/26/2022 12:00:00 PM |  | 1/26/2024 12:00:00 PM | Residential Building Permit | Renovation | Renovation | Expired | 15713 | 3638 | DEAL ST | HALIFAX | 00181370 | 39000 | Building - Plumbing - Prior to Occupancy | Dwelling - Single Detached | Residential Use | 1 | 2 |
| BPRES-2023-11028 | 8/31/2023 12:00:00 PM | 9/5/2025 12:00:00 PM |  | 9/5/2027 12:00:00 PM | Residential Building Permit | New Building | New Building | Issued | 80544 | 1172 | ROCKCLIFFE ST | HALIFAX | 00078519 | 1000000 |  | Dwelling - Multiple Units | Residential Use |  | 2 |
| BPRES-2025-08157 | 5/28/2025 12:00:00 PM | 6/30/2025 12:00:00 PM | 4/9/2026 12:00:00 PM | 6/30/2027 12:00:00 PM | Residential Building Permit | New Building | New Building | Completed | 190704 | 212 | SAILORS TRL | EASTERN PASSAGE | 00401182 | 300000 | Building - Part 9 - Final | Dwelling - Semi-Detached | Residential Use |  | 2 |
| BP-2021-04385 | 3/23/2021 12:00:00 PM | 5/6/2021 12:00:00 PM | 6/13/2022 12:00:00 PM | 5/6/2023 12:00:00 PM | Residential Building Permit | New Building | New Building | Completed | 172245 | 140 | CORTLAND RG | HALIFAX | 41485913 | 250000 | Building - Part 9 - Final | Dwelling - Semi-Detached | Residential Use |  | 2 |
| BPCOM-2023-00884 | 1/29/2023 12:00:00 PM | 3/8/2023 12:00:00 PM |  | 3/8/2025 12:00:00 PM | Mixed Use & Commercial Building Permit | Renovation | Renovation | Expired | 80556 | 36 | KELLY ST | HALIFAX | 00306191 | 432169 |  | Dwelling - Multiple Units | Residential Use | 48 | 48 |
| BPCOM-2026-00194 | 1/8/2026 12:00:00 PM | 1/16/2026 12:00:00 PM |  | 1/16/2028 12:00:00 PM | Mixed Use & Commercial Building Permit | Renovation | Renovation | Issued | 49566 | 21 | MICMAC BLVD | DARTMOUTH | 00100446 | 280000 | Building - Commercial - Prior to Drywall | Commercial | Retail Use |  |  |
| BPRES-2022-03630 | 3/21/2022 12:00:00 PM | 4/7/2022 12:00:00 PM | 1/17/2024 12:00:00 PM | 4/7/2024 12:00:00 PM | Residential Building Permit | Renovation | Renovation | Completed | 64297 | 5861 | LIVINGSTONE ST | HALIFAX | 00173013 | 200000 | Building - Part 9 - Final | Dwelling - Single Detached | Residential Use | 1 | 1 |
| BPRES-2023-02718 | 3/14/2023 12:00:00 PM | 3/28/2023 12:00:00 PM |  | 2/23/2027 12:00:00 PM | Residential Building Permit | Addition | Addition | Issued | 94438 | 20021 | HIGHWAY 7 | SPRY BAY | 40810004 | 86000 |  | Dwelling - Single Detached | Residential Use | 1 | 1 |
| BPRES-2024-02358 | 3/28/2024 12:00:00 PM | 4/18/2024 12:00:00 PM | 1/20/2026 12:00:00 PM | 4/18/2026 12:00:00 PM | Residential Building Permit | New Building | New Building | Cancelled | 104655 | 2187 | HIGHWAY 7 | EAST PRESTON | 40144099 | 250000 |  | Dwelling - Single Detached | Residential Use |  | 1 |
| BPRES-2025-00205 | 1/7/2025 12:00:00 PM | 2/12/2025 12:00:00 PM |  | 2/12/2027 12:00:00 PM | Residential Building Permit | Renovation | Renovation | Issued | 62535 | 6024 | LADY HAMMOND RD | HALIFAX | 00019133 | 50000 |  | Dwelling - Multiple Units | Secondary Suite | 2 | 3 |
| BPRES-2025-16420 | 10/23/2025 12:00:00 PM | 10/31/2025 12:00:00 PM |  | 10/31/2027 12:00:00 PM | Residential Building Permit | New Building | New Building | Issued | 123851 | 26 | HAVERSTOCK DR | HAMMONDS PLAINS | 40834756 | 15000 |  | Accessory Structure | Residential Use |  |  |
| BP-2021-01748 | 3/18/2021 12:00:00 PM | 5/13/2021 12:00:00 PM |  | 7/12/2025 12:00:00 PM | Residential Building Permit | New Building | New Building | Expired | 167851 | 251 | NOTTING HILL RD | MINEVILLE | 41397381 | 350000 | Building - Part 9 - Final | Dwelling - Single Detached | Residential Use |  | 1 |
| BP-2021-07016 | 4/21/2021 12:00:00 PM | 5/10/2021 12:00:00 PM | 7/27/2022 12:00:00 PM | 5/10/2023 12:00:00 PM | Residential Building Permit | New Building | New Building | Completed | 162033 | 289 | THICKET DR | BROOKSIDE | 41379579 | 400000 | Building - Part 9 - Final | Dwelling - Single Detached | Residential Use |  | 1 |
| BPCOM-2022-03337 | 3/30/2022 12:00:00 PM | 4/12/2022 12:00:00 PM | 4/24/2023 12:00:00 PM | 4/12/2024 12:00:00 PM | Mixed Use & Commercial Building Permit | Renovation | Renovation | Completed | 47871 | 202 | BROWNLOW AVE | DARTMOUTH | 40354375 | 453000 | Building - Commercial - Final | Commercial | Retail Use |  |  |
| BPCOM-2023-14751 | 11/10/2023 12:00:00 PM | 12/20/2023 12:00:00 PM | 7/10/2025 12:00:00 PM | 12/20/2025 12:00:00 PM | Mixed Use & Commercial Building Permit | Renovation | Renovation | Completed | 62709 | 86 | GASTON RD | DARTMOUTH | 00242743 |  | Building - Commercial - Final | Dwelling - Multiple Units | Residential Use | 50 | 53 |
| BPCOM-2025-03635 | 3/20/2025 12:00:00 PM | 3/25/2025 12:00:00 PM |  | 3/25/2027 12:00:00 PM | Mixed Use & Commercial Building Permit | Renovation | Renovation | Issued | 164102 | 11 | CUDDY LANE | DARTMOUTH | 41350471 | 500000 |  | Commercial | Restaurant |  |  |
| BPRES-2021-13019 | 7/13/2021 12:00:00 PM | 8/12/2021 12:00:00 PM | 10/12/2022 12:00:00 PM | 8/12/2023 12:00:00 PM | Residential Building Permit | New Building | New Building | Completed | 35678 | 21 | BRACKENDALE LANE | BEAVER BANK | 40688178 | 36000 | Building - Part 9 - Accessory Final | Accessory Structure | Garage |  |  |
| BPRES-2022-00586 | 1/17/2022 12:00:00 PM | 5/10/2022 12:00:00 PM | 4/20/2023 12:00:00 PM | 5/10/2024 12:00:00 PM | Residential Building Permit | New Building | New Building | Completed | 175244 | 104 | HALL RD | WAVERLEY | 41351255 | 164000 | Building - Part 9 - Final | Dwelling - Backyard Suite | Residential Use |  | 1 |
| BPRES-2022-06864 | 5/17/2022 12:00:00 PM |  |  |  | Residential Building Permit | New Building | New Building | Applicant Revisions | 145874 | 85 | TROUTWATER TERR | PORTUGUESE COVE | 41307687 | 995000 |  | Dwelling - Single Detached | Residential Use |  | 1 |
| BPRES-2022-14266 | 11/23/2022 12:00:00 PM | 12/9/2022 12:00:00 PM | 11/6/2024 12:00:00 PM | 12/9/2024 12:00:00 PM | Residential Building Permit | New Building | New Building | Completed | 176150 | 35 | DAISYWAY LANE | LAWRENCETOWN | 41501412 | 155000 | Building - Part 9 - Final | Dwelling - Single Detached | Residential Use |  | 1 |
| BPRES-2023-06694 | 5/27/2023 12:00:00 PM | 3/21/2024 12:00:00 PM |  | 3/21/2026 12:00:00 PM | Residential Building Permit | Renovation | Renovation | Expired | 120429 | 1674 | COW BAY RD | COW BAY | 40127201 | 25000 | Building - Part 9 - Final | Dwelling - Multiple Units | Secondary Suite | 1 | 2 |
| BPRES-2023-14764 | 11/9/2023 12:00:00 PM |  |  |  | Residential Building Permit | Renovation | Renovation | Application Incomplete | 43759 | 48 | SACKVILLE CROSS RD | LOWER SACKVILLE | 40001760 | 200000 |  | Dwelling - Semi-Detached | Secondary Suite | 2 | 3 |
| BPRES-2024-05928 | 5/13/2024 12:00:00 PM | 9/4/2024 12:00:00 PM |  | 9/4/2026 12:00:00 PM | Residential Building Permit | Addition | Addition | Issued | 95966 | 23 | GUILDWOOD DR | FALL RIVER | 40380586 | 150000 | Building - Part 9 - Prior to Drywall | Dwelling - Multiple Units | Residential Use | 1 | 2 |
| BPRES-2024-15244 | 10/9/2024 12:00:00 PM | 10/17/2024 12:00:00 PM |  | 10/17/2026 12:00:00 PM | Residential Building Permit | New Building | New Building | Issued | 101440 | 34 | PORTERFIELD DR | PORTERS LAKE | 40505844 | 53000 |  | Accessory Structure | Residential Use |  |  |
| BPRES-2025-04421 | 3/31/2025 12:00:00 PM | 9/11/2025 12:00:00 PM |  | 9/11/2027 12:00:00 PM | Residential Building Permit | New Building | New Building | Issued | 52959 | 61 | FARRELL ST | DARTMOUTH | 41556846 | 750000 |  | Dwelling - Multiple Units | Residential Use |  | 7 |
| BPRES-2025-12368 | 8/7/2025 12:00:00 PM | 8/21/2025 12:00:00 PM |  | 8/21/2027 12:00:00 PM | Residential Building Permit | New Building | New Building | Issued | 186436 | 164 | TERRASTONE RG | DARTMOUTH | 41544297 | 500000 | Building - Part 9 - Footing | Dwelling - Single Detached | Residential Use |  | 1 |
| BPRES-2026-01746 | 2/20/2026 12:00:00 PM | 2/26/2026 12:00:00 PM |  | 2/26/2028 12:00:00 PM | Residential Building Permit | New Building | New Building | Issued | 191638 | 96 | GARVEY CRT | BEDFORD | 41548249 | 450000 | Building - Part 9 - Below Grade Insulation | Dwelling - Single Detached | Residential Use |  | 1 |
| BP-2021-00578 | 2/1/2021 12:00:00 PM | 5/20/2021 12:00:00 PM | 11/19/2021 12:00:00 PM | 5/20/2023 12:00:00 PM | Mixed Use & Commercial Building Permit | Renovation | Renovation | Completed | 172823 | 80 | HOGAN CRT | BEDFORD | 00360511 | 1500000 | Building - Commercial - Final | Commercial | Restaurant |  |  |
| BP-2021-03128 | 3/1/2021 12:00:00 PM | 6/23/2021 12:00:00 PM |  | 7/11/2025 12:00:00 PM | Residential Building Permit | New Building | New Building | Expired | 141003 | 2506 | PURCELLS COVE RD | HALIFAX | 41250721 | 1000000 | Building - Part 9 - Final | Dwelling - Single Detached | Residential Use |  | 1 |
| BP-2021-05719 | 1/11/2023 12:00:00 PM | 6/27/2023 12:00:00 PM |  | 7/15/2027 12:00:00 PM | Residential Building Permit | New Building | New Building | Issued | 127217 | 91 | MCGUIRE LANE | WINDSOR JUNCTION | 40744492 | 268400 | Building - Part 9 - Framing | Dwelling - Single Detached | Residential Use |  | 1 |
| BP-2021-08465 | 5/12/2021 12:00:00 PM | 7/28/2021 12:00:00 PM | 11/26/2024 12:00:00 PM | 10/11/2025 12:00:00 PM | Residential Building Permit | New Building | New Building | Completed | 170738 | 73 | ADELCHI CRT | MONTAGUE GOLD MINES | 41455874 | 305000 | Building - Part 9 - Final | Dwelling - Single Detached | Residential Use |  | 1 |
| BPCOM-2021-17142 | 10/8/2021 12:00:00 PM | 11/29/2021 12:00:00 PM | 11/30/2023 12:00:00 PM | 11/29/2023 12:00:00 PM | Mixed Use & Commercial Building Permit | Renovation | Renovation | Expired (Closed) | 71947 | 7001 | MUMFORD RD | HALIFAX | 00017681 | 10000 |  | Commercial | Retail Use |  |  |
| BPCOM-2022-10404 | 7/26/2022 12:00:00 PM | 8/9/2022 12:00:00 PM | 11/3/2022 12:00:00 PM | 8/9/2024 12:00:00 PM | Mixed Use & Commercial Building Permit | Renovation | Renovation | Completed | 137646 | 320 | WRIGHT AVE | DARTMOUTH | 41177478 | 50000 | Building - Commercial - Final | Commercial | Laboratory / Research Use |  |  |
| BPCOM-2023-07235 | 6/7/2023 12:00:00 PM | 7/11/2023 12:00:00 PM | 1/8/2024 12:00:00 PM | 7/11/2025 12:00:00 PM | Mixed Use & Commercial Building Permit | Renovation | Renovation | Completed | 130695 | 5269 | MORRIS ST | HALIFAX | 40848822 | 646849 | Building - Commercial - Final | Institutional and Governmental | Post-Secondary Institution |  |  |
| BPCOM-2024-02968 | 3/19/2024 12:00:00 PM | 4/24/2024 12:00:00 PM |  | 4/24/2026 12:00:00 PM | Mixed Use & Commercial Building Permit | Renovation | Renovation | Expired | 60476 | 109 | CONNOR LANE | HALIFAX | 00061945 | 39000 | Building - Commercial - Final | Mixed Use - Residential & Other Use(s) | Residential Use | 36 | 36 |
| BPCOM-2024-17122 | 11/27/2024 12:00:00 PM | 7/7/2025 12:00:00 PM |  | 7/7/2027 12:00:00 PM | Mixed Use & Commercial Building Permit | New Building | New Building | Issued | 187339 | 1075 | FALL RIVER RD | FALL RIVER | 41541640 | 62750000 | Building - Plumbing - Underground | Institutional and Governmental | Parking Structure |  |  |
| BPCOM-2025-12593 |  |  |  |  | Mixed Use & Commercial Building Permit | Renovation | Renovation | Application Incomplete | 44102 | 85 | SACKVILLE CROSS RD | LOWER SACKVILLE | 40001653 | 120000 |  | Commercial | Residential Use | 1 | 4 |
| BPRES-2021-10733 | 7/13/2021 12:00:00 PM |  | 1/18/2023 12:00:00 PM |  | Residential Building Permit | New Building | New Building | Withdrawn | 131045 | 1098 | WEST PORTERS LAKE RD | WEST PORTERS LAKE | 41105107 | 125000 |  | Dwelling - Semi-Detached | Residential Use |  | 2 |
| BPRES-2021-15170 | 8/29/2021 12:00:00 PM | 10/20/2021 12:00:00 PM | 6/30/2023 12:00:00 PM | 10/20/2023 12:00:00 PM | Residential Building Permit | New Building | New Building | Completed | 14112 | 2 | CREWS CRT | BOUTILIERS POINT | 40731572 | 245000 | Building - Part 9 - Final | Dwelling - Single Detached | Residential Use |  | 1 |
| BPRES-2021-19025 | 12/2/2021 12:00:00 PM | 12/22/2021 12:00:00 PM | 2/3/2022 12:00:00 PM | 12/22/2023 12:00:00 PM | Residential Building Permit | Renovation | Renovation | Completed | 111305 | 14 | ELLEN DR | DARTMOUTH | 00213280 | 30000 | Building - Plumbing - Prior to Occupancy | Dwelling - Multiple Units | Residential Use | 1 | 2 |
| BPRES-2022-02208 | 2/28/2022 12:00:00 PM | 3/16/2022 12:00:00 PM | 3/19/2024 12:00:00 PM | 3/19/2026 12:00:00 PM | Residential Building Permit | Renovation | Renovation | Completed | 14610 | 55 | CHRISTIES RD | BOUTILIERS POINT | 40579971 | 32000 | Building - Part 9 - Framing | Dwelling - Single Detached | Residential Use | 1 | 1 |
| BPRES-2022-05274 | 6/13/2022 12:00:00 PM | 2/23/2023 12:00:00 PM |  | 2/23/2025 12:00:00 PM | Residential Building Permit | New Building | New Building | Expired | 171619 | 45 | ROSE ST | DARTMOUTH | 41461963 | 500000 | Building - Part 9 - Prior to Drywall | Dwelling - Multiple Units | Secondary Suite |  | 2 |
| BPRES-2022-08818 | 6/21/2022 12:00:00 PM |  |  |  | Residential Building Permit | New Building | New Building | Applicant Revisions | 145832 | 1137 | WILDERNESS DR | PORTUGUESE COVE | 41306291 | 550000 |  | Dwelling - Single Detached | Residential Use |  | 1 |
| BPRES-2022-12560 | 9/14/2022 12:00:00 PM | 9/23/2022 12:00:00 PM | 3/14/2023 12:00:00 PM | 9/23/2024 12:00:00 PM | Residential Building Permit | New Building | New Building | Completed | 141843 | 221 | BLACKBEAR CIR | LEWIS LAKE | 41258799 | 36000 | Building - Part 9 - Framing | Accessory Structure | Residential Use |  |  |
| BPRES-2023-00591 | 3/31/2023 12:00:00 PM | 4/6/2023 12:00:00 PM |  | 10/23/2027 12:00:00 PM | Residential Building Permit | New Building | New Building | Amendment Application Incomplete | 170885 | 5645 | HIGHWAY 7 | HEAD OF CHEZZETCOOK | 40711954 | 42000 | Building - Part 9 - Accessory Final | Accessory Structure | Residential Use |  |  |
| BPRES-2023-04740 | 4/21/2023 12:00:00 PM | 1/4/2024 12:00:00 PM |  | 1/4/2026 12:00:00 PM | Residential Building Permit | Addition | Addition | Expired | 34676 | 32 | MAXWELL AVE | UPPER SACKVILLE | 00478594 | 100000 | Building - Part 9 - Prior to Drywall | Dwelling - Single Detached | Residential Use | 1 | 1 |

_17753 additional rows omitted from preview; 10 additional columns omitted from preview. Full data in sidecar._
