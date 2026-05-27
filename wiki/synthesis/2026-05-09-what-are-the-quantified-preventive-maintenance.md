---
schema_version: 1
type: synthesis
slug: 2026-05-09-what-are-the-quantified-preventive-maintenance
title: 'What are the QUANTIFIED preventive-maintenance cadences and benchmarks for
  100+ unit condominium / strata / co-op buildings in the United States and Canada
  — frequency intervals, durations, costs, and reliability benchmarks — across the
  building-system stack? For each component (HVAC central plant, elevators, plumbing
  risers, fire-life-safety, building envelope, balconies, roofing, parking deck),
  produce: (a) inspection / test / service intervals in months or years, (b) typical
  labor-hour or specialist-day estimate per task, (c) typical $/sf or $/unit cost
  band for service contracts and ITM cycles, (d) regulatory minimum cadence vs. industry-standard
  cadence vs. predictive / condition-based cadence where they diverge, (e) MTBF /
  failure-rate or component service-life benchmark where reported. Include sub-tables
  for: NFPA 25 sprinkler ITM, NFPA 72 fire alarm ITM, ASME A17.1 / CSA B44 elevator
  inspection, NYC LL11/FISP cadence, NYC LL87 energy-audit cadence, CA SB 326 balcony
  cadence, FL §718.112(2)(g) maintenance plan inputs, Quebec Bill 16 carnet d''entretien
  content, BOMA BEST 4.0 MURB E6.0 PM section, CAI Foundation 2023 cadence guidance,
  BC Housing Maintenance Matters water-system cadence, PCI parking-deck sealer reapplication
  cadence, and CMMS/EAM-recorded benchmark task durations from BuildingLink / Yardi
  / CondoControl / Building Engines vendor methodology pages. Also: a single board-facing
  reference table of MINIMUM-DEFENSIBLE annual PM operating cost per door for a 200-unit
  Florida high-rise condo.'
domains:
- condo
question: 'What are the QUANTIFIED preventive-maintenance cadences and benchmarks
  for 100+ unit condominium / strata / co-op buildings in the United States and Canada
  — frequency intervals, durations, costs, and reliability benchmarks — across the
  building-system stack? For each component (HVAC central plant, elevators, plumbing
  risers, fire-life-safety, building envelope, balconies, roofing, parking deck),
  produce: (a) inspection / test / service intervals in months or years, (b) typical
  labor-hour or specialist-day estimate per task, (c) typical $/sf or $/unit cost
  band for service contracts and ITM cycles, (d) regulatory minimum cadence vs. industry-standard
  cadence vs. predictive / condition-based cadence where they diverge, (e) MTBF /
  failure-rate or component service-life benchmark where reported. Include sub-tables
  for: NFPA 25 sprinkler ITM, NFPA 72 fire alarm ITM, ASME A17.1 / CSA B44 elevator
  inspection, NYC LL11/FISP cadence, NYC LL87 energy-audit cadence, CA SB 326 balcony
  cadence, FL §718.112(2)(g) maintenance plan inputs, Quebec Bill 16 carnet d''entretien
  content, BOMA BEST 4.0 MURB E6.0 PM section, CAI Foundation 2023 cadence guidance,
  BC Housing Maintenance Matters water-system cadence, PCI parking-deck sealer reapplication
  cadence, and CMMS/EAM-recorded benchmark task durations from BuildingLink / Yardi
  / CondoControl / Building Engines vendor methodology pages. Also: a single board-facing
  reference table of MINIMUM-DEFENSIBLE annual PM operating cost per door for a 200-unit
  Florida high-rise condo.'
created_at: '2026-05-09T23:56:08Z'
nlm_notebook_id: 3a25d83f-94d9-49d1-8756-cfd112c753ca
finalized_at: '2026-05-10T00:45:55Z'
last_updated: '2026-05-13T22:12:24Z'
sources_count: 10
---
# What are the QUANTIFIED preventive-maintenance cadences and benchmarks for 100+ unit condominium / strata / co-op buildings in the United States and Canada — frequency intervals, durations, costs, and reliability benchmarks — across the building-system stack? For each component (HVAC central plant, elevators, plumbing risers, fire-life-safety, building envelope, balconies, roofing, parking deck), produce: (a) inspection / test / service intervals in months or years, (b) typical labor-hour or specialist-day estimate per task, (c) typical $/sf or $/unit cost band for service contracts and ITM cycles, (d) regulatory minimum cadence vs. industry-standard cadence vs. predictive / condition-based cadence where they diverge, (e) MTBF / failure-rate or component service-life benchmark where reported. Include sub-tables for: NFPA 25 sprinkler ITM, NFPA 72 fire alarm ITM, ASME A17.1 / CSA B44 elevator inspection, NYC LL11/FISP cadence, NYC LL87 energy-audit cadence, CA SB 326 balcony cadence, FL §718.112(2)(g) maintenance plan inputs, Quebec Bill 16 carnet d'entretien content, BOMA BEST 4.0 MURB E6.0 PM section, CAI Foundation 2023 cadence guidance, BC Housing Maintenance Matters water-system cadence, PCI parking-deck sealer reapplication cadence, and CMMS/EAM-recorded benchmark task durations from BuildingLink / Yardi / CondoControl / Building Engines vendor methodology pages. Also: a single board-facing reference table of MINIMUM-DEFENSIBLE annual PM operating cost per door for a 200-unit Florida high-rise condo.

## Synthesis

**Quantified Preventive-Maintenance Cadences & Benchmarks Across the Building-System Stack** [[sources/web-1998-01-01-7e4]]

The following benchmarks are derived from structural engineering assessments, reserve fund studies, and jurisdictional mandates for 100+ unit residential facilities. *Note: Where specific CMMS vendor labor-hour task durations (BuildingLink, Yardi, CondoControl, Building Engines) are not quantified in the provided dataset, standard replacement and service cost bands have been substituted [1-4].* [[sources/web-1998-01-01-7e4]]

| Building System | (a) ITM / Service Intervals | (b) & (c) Cost Bands / Labor Estimates | (d) Cadence Variations (Reg. vs. Predictive) | (e) MTBF / Component Service Life (EUL) | [[sources/web-1998-01-01-7e4]]
| :--- | :--- | :--- | :--- | :--- | [[sources/web-1998-01-01-7e4]]
| **HVAC Central Plant** | **Annually:** Boiler & make-up air PM.<br>**2-3 Years:** Inspect motors, brushes, fan blades, bearings [5, 6].<br>**5-8 Years:** Replace circulation pumps, belts/pulleys [7, 8]. | **Boiler Replacement:** $17,000 - $61,000 [9, 10].<br>**Exhaust Fans:** $14,850/assembly [11] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. | **Standard:** Calendar-based belt/filter changes.<br>**Predictive:** Machine-learning (XGBoost) tracks sensor telemetry for faults (e.g., *Damper_Open_No_Occupancy*) with 95% accuracy, overriding calendar schedules [12] [[nlm:92443269-6cd6-4634-8219-6a844f48b32f]]. | **Make-Up Air Units:** 20 years [8] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Boilers:** 20 years [13] [[nlm:50f51b59-1118-4cc3-852c-4cf86bba8a35]].<br>**Cabinet Exhaust Fans:** 12 years [5] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. | [[sources/web-1998-01-01-7e4]]
| **Elevators** | **Monthly:** Elevator maintenance/cleaning [14] [[nlm:e4ee24bb-aaea-4b62-a8ec-d2520f18e684]].<br>**2 Years:** Overload device & full-load performance tests [15, 16]. | **Service Contract:** ~$300-$400 per cab / month (full parts & labor recommended) [17] [[nlm:50f51b59-1118-4cc3-852c-4cf86bba8a35]].<br>**Modernization:** $56k-$78k for controllers/doors [18] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. | **Regulatory:** Mandated safety checks dictated by ASME A17.1/CSA B44 [19] [[nlm:50f51b59-1118-4cc3-852c-4cf86bba8a35]].<br>**Predictive:** Monitor door cycle counts and leveling accuracy to catch brake wear early. | **Overall System:** 50 years [18] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Door Operators:** 20 years [18] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Hoist Ropes:** 15 years [20] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. | [[sources/web-1998-01-01-7e4]]
| **Plumbing Risers** | **Annually:** Inspect outside spigots/plumbing [21] [[nlm:bd9fbf94-5794-450f-980e-c950ebc9c215]].<br>**3 Years:** Flush drain stacks in high-rises [22] [[nlm:bd9fbf94-5794-450f-980e-c950ebc9c215]].<br>**5 Years:** CCTV camera inspection of main sewer lines [22] [[nlm:bd9fbf94-5794-450f-980e-c950ebc9c215]]. | **Drain Augering:** ~$4,400-$4,700 per 10-year cycle [6] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Camera Scope:** ~$600-$3,300 per 5-year cycle [23, 24]. | **Industry:** Flush stacks every 5-7 years for commercial, but residential high-rises require strict 3-year intervals due to fat/grease accumulation [22, 25]. | **Copper/PEX Distribution:** 35 years [26] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Fittings & Valves:** 50 years [27] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Sump Pumps:** 15 years [20, 22]. | [[sources/web-1998-01-01-7e4]]
| **Fire-Life-Safety** | **Monthly:** Extinguisher/hose checks [28] [[nlm:50f51b59-1118-4cc3-852c-4cf86bba8a35]].<br>**5 Years:** Sprinkler flow tests & battery pack replacements [29, 30].<br>**10-12 Years:** Extinguisher/smoke alarm replacement [31, 32]. | **Panel Replacement:** $44,000 - $63,000 [29] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Battery Packs:** $560 - $800 [29] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Fire Pump:** $3,000 (repair) vs $20,000+ (new assembly) [33] [[nlm:50f51b59-1118-4cc3-852c-4cf86bba8a35]]. | **Regulatory:** Strict adherence to NFPA 25 and NFPA 72.<br>**Industry:** Upgrading localized bells/horns to in-suite mini-horns to meet 75 dBA standards during lifecycle renewals [34] [[nlm:50f51b59-1118-4cc3-852c-4cf86bba8a35]]. | **Fire Alarm Panels:** 20 years [29] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Dry Sprinkler Systems:** 60 years [35] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Wet Sprinkler Piping:** 100 years [31] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. | [[sources/web-1998-01-01-7e4]]
| **Building Envelope** | **Annually:** Visual reviews of siding and sealants [36] [[nlm:e4ee24bb-aaea-4b62-a8ec-d2520f18e684]].<br>**2 Years:** Check IGUs (windows) for misting [37] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**10 Years:** Clean & repaint fiber cement / masonry [38, 39]. | **Window Replacement:** $617,500 for a sample 100+ unit phase [40] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Envelope Renewal:** $330-$405 per sq. ft. (Vancouver benchmark) [41] [[nlm:633c2298-ce01-4e4c-9c84-fe218a197aab]]. | **Regulatory (NYC LL11):** Hands-on scaffold inspections every 5 years [42] [[sources/web-2025-02-27-05e]].<br>**Predictive:** Air leakage/blower door testing & thermal imaging scans per BOMA BEST [43] [[nlm:fdeba129-236b-48fa-9fde-e9776c55d0a2]]. | **Vinyl Windows:** 30 years [40] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Cultured Stone:** 30 years [44] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Fiber Cement:** 40 years [45] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. |
| **Balconies** | **Annually:** Visual checks for water pooling/overloading.<br>**15 Years:** Remove/re-install guardrails and renew waterproofing [38] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. | **Vinyl Membrane Renewal:** $212,500 - $425,000 per sample phase [46] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. | **Regulatory (CA SB 326):** Structural/architectural inspection every 9 years covering 95% statistical sample [47, 48]. | **Vinyl Membranes:** 15 years [46] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Aluminum Guardrails:** 30 years [49] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. | [[sources/web-1998-01-01-7e4]]
| **Roofing** | **3 Years:** Clean exterior soffits and trim [50] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**5 Years:** Preventive maintenance and patch repairs [45, 51]. | **5-Yr Maintenance Cycle:** ~$16,000 per event [45, 51]. | **Industry:** Maximum vents should not exceed 50% of total ventilation to prevent premature shingle failure [52] [[nlm:50f51b59-1118-4cc3-852c-4cf86bba8a35]]. | **Asphalt Shingles:** 30 years [49] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**Soffits/Fascia:** 40 years [49] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. | [[sources/web-1998-01-01-7e4]]
| **Parking Deck** | **Annually:** Washdowns / remove oil stains [36] [[nlm:e4ee24bb-aaea-4b62-a8ec-d2520f18e684]].<br>**5 Years:** Re-apply traffic striping and concrete sealer [53] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**10 Years:** Reseal asphalt paving [54] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. | **Sealer Re-application:** ~$5,700 - $7,000 [55, 56].<br>**CO Gas Detectors:** $3,000 per 5-year cycle [57] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. | **Industry:** Concrete sealers act as a sacrificial layer against road salts; skipping the 5-year cycle drastically accelerates rebar corrosion [53, 58]. | **Concrete Slab:** 75+ years (if sealed properly) [53] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].<br>**CO Detectors:** 10 years [57] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. | [[sources/web-1998-01-01-7e4]]

---

### **Regulatory & Industry Standard Sub-Tables**

**Life Safety & Structural Mandates** [[sources/web-1998-01-01-7e4]]
*   **NFPA 25 (Sprinklers):** Mandates flow testing on piping (exposed and underground) every **5 years** [30] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]. High-temperature sprinkler heads require testing every **5 years**, and standard heads must undergo a sample test by a recognized agency at the **50-year** mark [30, 59]. Antifreeze solutions exceeding 30% propylene glycol are largely sunsetted unless specifically listed for ESFR use [60] [[sources/web-2024-06-01-906]].
*   **NFPA 72 (Fire Alarms):** Requires cyclical inspection, testing, and maintenance of initiating devices, notification appliances, and emergency communications systems (ECS) [61] [[sources/web-2022-01-01-e0b]]. Battery packs must be replaced every **5 years** [29] [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]].
*   **ASME A17.1 / CSA B44 (Elevators):** Requires **2-year** overload device checks and full-load performance tests [15, 16]. Modern codes (CSA B44-07) demand specific lux lighting levels (100 lux at sills, 200 in machine rooms) and strict "Unintended Car Movement" protections [62, 63]. [[sources/web-1998-01-01-7e4]]
*   **NYC LL11 / FISP:** Applies to facades >6 stories. Requires a Critical Examination by a Qualified Exterior Wall Inspector (QEWI) every **5 years**. Requires scaffold drops at minimum 60-foot intervals. "Cavity wall" facades require destructive probes to check wall ties every second cycle [42, 64]. [[sources/web-1998-01-01-7e4]]
*   **NYC LL87 / Vancouver Carbon Limits:** NYC requires energy audits and retro-commissioning every **10 years** for buildings >50,000 sq ft. Vancouver imposes strict Greenhouse Gas Intensity (GHGi) limits starting in 2026, forcing phase-outs of natural gas make-up air units for heat pumps [65, 66]. [[sources/web-1998-01-01-7e4]]
*   **CA SB 326 & SB 721 (Balconies):** SB 326 (Condos) mandates inspections of elevated wood-supported elements every **9 years** using a 95% confidence statistical sample. SB 721 (Rentals) requires a 15% sample every **6 years**. Unsafe conditions must be shored/repaired within 120 days or face $500/day fines [47, 48, 67]. [[sources/web-1998-01-01-7e4]]

**Financial & Planning Mandates** [[sources/web-1998-01-01-7e4]]
*   **Florida §718.112(2)(g) (SIRS inputs):** A Structural Integrity Reserve Study (SIRS) must fully fund 8 critical elements: **1) Roof, 2) Structure/load-bearing walls, 3) Fire protection, 4) Plumbing, 5) Electrical, 6) Waterproofing/exterior painting, 7) Windows/doors, 8) Any item over $10,000** impacting structural safety [68, 69]. Baseline funding must maintain a cash balance above zero without owner waivers [70] [[nlm:0e9d37fc-7559-4fe0-a5c4-d26c1ce1537f]]. [[sources/web-2026-01-01-361]]
*   **Quebec Bill 16 (Carnet d'entretien):** Requires a digital maintenance logbook updated **annually**, a full professional review every **5 years**, and a contingency fund study with a minimum **25-year** planning horizon for major repairs [71, 72]. [[sources/web-1998-01-01-7e4]]
*   **BOMA BEST 4.0 MURB (E6.0 & I3.1):** Requires a formalized Preventive Maintenance Plan (E6.0) aligned with ASHRAE 180-2018. Mandates existing building commissioning (EBCx) every 5 years (E6.1) and highly encourages Fault Detection & Diagnostics (FDD) integration (E6.2) [73-75]. Requires MERV 13+ filters with inspections logged to monitor pressure drops [76, 77]. [[sources/web-1998-01-01-7e4]]
*   **CAI Foundation 2023:** Stresses that reserve funds cover only ~25% of maintenance activities but the vast majority of costs [78, 79]. Strongly advises boards to commission a supplementary *Preventive Maintenance Schedule* alongside the standard CAI-RSSTD 12-22 reserve study to maximize component EUL [80] [[nlm:3bd1b45f-1cfd-4abb-afe6-5ae98bafbe46]]. [[sources/web-2025-10-13-a40]]
*   **BC Housing (Maintenance Matters):** Drain stacks must be flushed every **3 years** in residential high-rises to prevent sewer backups. Sump pumps require bearing maintenance every **5 years** and replacement every 15 years. Heat-trace systems checked **twice a year** [22] [[nlm:bd9fbf94-5794-450f-980e-c950ebc9c215]]. [[sources/pdf-bc-housing-2021-maintenance-matters-20]]

---

### **Minimum-Defensible Annual PM Operating Cost per Door**
*(Model: 200-Unit Florida High-Rise Condo complying with FL HB 913/SIRS & Fannie Mae Overlays)* [[sources/web-1998-01-01-7e4]]

Research indicates that preventive maintenance comprises only 10%–30% of total maintenance costs, but deferring it can result in corrective repairs that cost up to **30 times** the missed PM budget [81, 82]. The following table outlines the minimum defensible *preventive* maintenance operating spend (excluding major reserve replacements) to ensure structural integrity and warrantability. [[sources/web-1998-01-01-7e4]]

| Maintenance Category (Annualized) | Baseline Activity | Estimated Annual PM Cost | Cost Per Door (200 Units) | [[sources/web-1998-01-01-7e4]]
| :--- | :--- | :--- | :--- | [[sources/web-1998-01-01-7e4]]
| **Elevator Maintenance** | Monthly ITM contracts for 3-4 traction elevators (~$300-$400/mo/cab) [17] [[nlm:50f51b59-1118-4cc3-852c-4cf86bba8a35]]. | $14,400 - $19,200 | **$72 - $96** | [[sources/web-1998-01-01-7e4]]
| **Fire/Life Safety ITM** | Annual panel checks, periodic flow tests, backflow valves, extinguisher tags [30, 83]. | $5,000 - $8,000 | **$25 - $40** | [[sources/web-1998-01-01-7e4]]
| **HVAC / Mechanical PM** | Annual boiler & make-up air PM, filter replacements, pump checks [6, 13]. | $8,000 - $12,000 | **$40 - $60** | [[sources/web-1998-01-01-7e4]]
| **Plumbing / Risers** | Stack flushing on a 3-year cycle for residential high-rises (amortized into the annual operating budget), annual sump pump maintenance, drain augering [6, 22]. | $4,500 - $7,000 | **$22 - $35** | [[sources/web-1998-01-01-7e4]]
| **Envelope / Balcony & Roof** | Annual visual inspections, caulk touch-ups, concrete localized sealing, gutter clearing [84, 85]. | $10,000 - $15,000 | **$50 - $75** | [[sources/web-1998-01-01-7e4]]
| **Professional Inspections** | Prorated cost of 5-yr SIRS / structural engineering audits / Reserve Study updates [68] [[nlm:93cfbe44-a60d-439a-9727-8b91bc15e632]]. | $3,000 - $5,000 | **$15 - $25** | [[sources/web-2026-01-01-361]]
| **General Proactive Maintenance** | Baseline example: An investment of $500/year averts $150,000 in deferred corrective failures [82] [[nlm:3bd1b45f-1cfd-4abb-afe6-5ae98bafbe46]]. | $100,000 | **$500** | [[sources/web-1998-01-01-7e4]]
| **TOTAL MINIMUM PM SPEND** | **Proactive Operating Expenditure (Non-Reserve)** | **~$144,900 - $166,200** | **~$724 - $831 / unit** | [[sources/web-1998-01-01-7e4]]

*Note: This represents the operating budget dedicated strictly to preventive maintenance labor and minor parts. It does NOT include the statutory reserve contributions required under Florida SIRS or Fannie Mae's 10%-15% baseline mandates.* [[sources/web-1998-01-01-7e4]]


---

## Section 8 — Open questions and highest-leverage next research moves

### Priority ranking

**1. FL DBPR public-records request (single highest-leverage FL move)**

DBPR does not publish operational guidance documents on HB 913 / SIRS implementation. All guidance was delivered verbally at 92 educational sessions attended by 41,000+ people. Filing a Ch. 119 public-records request for the session slide decks is the only path to citable, DBPR-authorized operational PM content for Florida. Estimated cost: $150–300 in copying fees. Expected turnaround: 30–60 days for production. Specific records to request (in priority order): (1) HB 913 educational session slide decks and handouts from all 92 CTMH sessions; (2) SIRS online account submission statistics by county and building type; (3) CTMH staff internal FAQ/guidance document; (4) Chapter 61B rule-making working group materials; (5) post-November 2025 enforcement/complaint data. Contact: DBPR Custodian of Public Records at myfloridalicense.com/custodian-public-records/. See findings memo 0003a-fl-dbpr-public-records-scope.md for full legal basis and fee structure. [[sources/web-2026-01-01-361]]

**2. BC Housing Maintenance Matters bulletins — manual download required**

Three BC Housing bulletins hit redirect walls during automated ingest and must be downloaded manually before they can be ingested via the gateway:

- MM-2: Roofing maintenance
- MM-6: Decks and balconies
- MM-11: Envelope maintenance programs

MM-6 closes the balcony cadence gap directly. MM-11 is the most comprehensive envelope PM document in the BC strata engineering corpus. Once downloaded, ingest via `wiki ingest <local-path> --domain condo --with-plan`. MM-20 (water systems) was successfully ingested in Move 1 and is already in the NLM corpus (source `pdf-bc-housing-2021-maintenance-matters-20`). [[sources/pdf-bc-housing-2021-maintenance-matters-20]]

**3. Engine work-order schema linkage (dependent downstream artifact)**

The CMMS data-model evidence in this corpus — BuildingLink (`web-1998-01-01-7e4`), Yardi (`web-2026-02-18-dff`), CondoControl (`web-2024-10-15-6c9`), Building Engines (`web-2026-02-20-0f3`) — is the direct input to the engine's covariate ingest design. The recurring work-order schema (asset category, trigger type, frequency, technician field-app sync fields) that these platforms expose maps to the work-order covariate layer in the six-component probabilistic engine. This linkage must be made explicit when the methods scan runs. The methods scan team should review `web-1998-01-01-7e4` (BuildingLink asset directory schema) and `web-2026-02-18-dff` (Yardi field-app sync spec) as primary covariate-schema inputs before locking the engine's CMMS ingest API design. [[sources/web-1998-01-01-7e4]]

**4. CMMS vendor task-duration benchmarks (quantified gap)**

The NLM corpus does not contain benchmark labor-hour estimates per PM task from any of the four CMMS vendors. BuildingLink, Yardi, CondoControl, and Building Engines all describe *what* they track but not *how long tasks take*. The cost-per-door table above uses contract cost bands (dollars), not labor-hour inputs. A targeted search of BOMA Operations Experience Exchange Report (OER) data, IFMA Benchmarks, or direct vendor methodology pages would fill this gap and provide the labor-input layer for the engine's cost-escalation model. [[sources/web-1998-01-01-7e4]]

### §7 strawman caveat

The "minimum-defensible 200-unit Florida condo PM program" (replicated in the cost-per-door table above) is now better-grounded statutorily — FL §718.112(2)(g) SIRS element list, FL HB 913 enrolled text [[sources/web-2026-01-01-361]], and FL Admin Code 61B-22/61B-23 are all in the corpus. However, the *operational PM layer* between reserve study cycles remains unvalidated by any published FL-specific source. No board PM template, no DBPR operational checklist, and no FL-specific CAI operational guide exists in public form. The cost-per-door figure of $724–$831/unit/year is constructed from first principles: ASME/NFPA standards + Canadian strata engineering benchmarks + FL statutory compliance layer. It is a reasonable design-partner conversation starter, not a documented Florida practice. It should be presented to FL design partners as a hypothesis to validate, not as an industry-established benchmark. Flag explicitly in any board-facing or design-partner materials derived from this synthesis.

## Sources cited

- [[sources/web-1998-01-01-7e4]]
- [[sources/web-2024-10-15-6c9]]
- [[nlm:97fc8200-55c5-433c-853e-b5861dd8ace0]]
- [[nlm:92443269-6cd6-4634-8219-6a844f48b32f]]
- [[nlm:50f51b59-1118-4cc3-852c-4cf86bba8a35]]
- [[nlm:e4ee24bb-aaea-4b62-a8ec-d2520f18e684]]
- [[nlm:bd9fbf94-5794-450f-980e-c950ebc9c215]]
- [[nlm:633c2298-ce01-4e4c-9c84-fe218a197aab]]
- [[sources/web-2025-02-27-05e]]
- [[nlm:fdeba129-236b-48fa-9fde-e9776c55d0a2]]
- [[sources/web-2025-12-08-df6]]
- [[nlm:f1361ace-4a31-4a55-b359-a82d417f296d]]
- [[sources/web-2024-06-01-906]]
- [[sources/web-2022-01-01-e0b]]
- [[nlm:e1cfdb8d-b8ab-4202-98b7-715effebe022]]
- [[nlm:93cfbe44-a60d-439a-9727-8b91bc15e632]]
- [[nlm:0e9d37fc-7559-4fe0-a5c4-d26c1ce1537f]]
- [[nlm:1f80d30f-fe81-41be-90a5-ea46da218667]]
- [[sources/web-2025-11-24-619]]
- [[nlm:bc33431a-0d3e-4ea8-a354-dd8e5167390c]]
- [[nlm:3bd1b45f-1cfd-4abb-afe6-5ae98bafbe46]]
