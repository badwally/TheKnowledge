---
schema_version: 1
type: concept
slug: roof-component-priors
canonical_name: Roof Component Priors
domains:
- condo-capital-infra
created_at: '2026-05-10T22:46:56Z'
last_updated: '2026-05-10T22:46:56Z'
---
# Roof Component Priors

## Summary

Roof component priors are the calibration inputs — roof-system taxonomy, service-life ranges, inspection cadence, failure-mode taxonomy, and replacement triggers — that feed remaining-useful-life (RUL) distributions for the roof component in the condo-capital-infra probabilistic reserve engine. BC Housing's Maintenance Matters No. 2 bulletin is the primary authoritative Canadian source for these priors, providing roof-system definitions, service-life ranges, inspection cadence, and a structured inspection-item taxonomy usable for prior calibration in the v0.5 → v1 engine transition [[sources/pdf-bc-housing-2020-maintenance-matters-02]].

## Key claims

### Roof-system taxonomy

- There are two main types of roof systems: low-slope and steep-slope roofs; some buildings combine both types [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Most multi-unit residential buildings use some form of low-slope roofing [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Townhouse buildings and single detached houses generally use steep-slope roofing [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Low-slope roofs have a waterproof membrane and a series of drains throughout the roof area to remove water; the membrane is either applied as a liquid that cures or dries to form a waterproof surface, or fabricated from pre-manufactured sheets joined together to create a surface impermeable to water [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Steep-slope roofs use overlapping roofing materials to shed water into a drainage system such as eavestroughs or gutters; materials include asphalt or fiberglass shingles, cedar shakes, slate tiles, concrete or clay tile, or sheet metal panels [[sources/pdf-bc-housing-2020-maintenance-matters-02]].

### Service lives

- Roofing system life expectancies range from 10 years to over 30 years, depending on roof design, exposure, construction, and materials used — wide enough to require an RUL distribution rather than a single point estimate [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Given proper maintenance, roofing systems have an anticipated "leak-free life" during which the roof should not leak if properly designed, constructed, and maintained; after this time the roof may continue to provide many years of service, but leaks should be expected, increasing in frequency and severity until replacement is required [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Eventually, maintenance will no longer be useful or cost-effective in preventing leaks; roofs should be replaced before the risk of complete failure gets too high, to avoid potentially costly interior repairs from water leakage [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Unscheduled maintenance and repairs may be needed to fix damage during severe windstorms or other extreme weather events — a regime-switching driver that breaks the deterministic schedule assumption [[sources/pdf-bc-housing-2020-maintenance-matters-02]].

### Inspection cadence

- Roofs should be inspected twice a year: in the spring to address any winter damage that may have occurred, and in the fall to prepare for the upcoming winter snow and rain [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Roofs should also be inspected after any storm with high winds (checking for loose, broken, or missing shingles), extreme rain or hail, or if construction has taken place on the roof area [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- The inspection should also include the underside of the roof structure or decks and the outside of the building, as these areas may indicate potential problems with the roof [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- All inspections and maintenance should be performed by a qualified professional roofing inspector or contractor familiar with the roofing system used on the building, who knows how to identify potential problems, and who knows how to take the necessary safety precautions [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Residents may visually identify some maintenance concerns (such as ceiling or wall staining indicating possible roof leaks) and should notify the maintenance manager, but should not perform the inspection themselves [[sources/pdf-bc-housing-2020-maintenance-matters-02]].

### Failure-mode taxonomy (for survival / Weibull priors)

- Splitting, ridging, or blistering of the roof membrane on low-slope roofs, typically caused by stress that can occur throughout the roof area; may be an indication of aging, with certain problems more evident in cold or hot weather [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Missing gravel (ballast) on low-slope roofs; ballast protects the membrane from damage caused by ultraviolet light and the weather, and its absence reduces the expected service life of the roof [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Missing granules on asphalt shingles and roll roofing, caused by excessive foot traffic, wind scouring, or scouring caused by tree branches located too close to the roof; lack of granular cover reduces expected service life and affects appearance [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Curled, broken, cracked, or missing shingles, shakes, or tiles; curling may indicate that the shingles have reached the end of their life expectancy, requiring replacement [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Excessive moss or algae growth can lead to premature failure of shakes and shingles on steep-slope roofs, and of certain types of membranes on low-slope roofs; moss accumulation holds moisture on the roof, preventing proper drainage and accelerating the deterioration of roofing components [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Foreign objects on the roof, which should be removed because they could cause a puncture in the roofing material or membrane [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Missing or damaged flashings, eavestroughs, downpipes, caulking/sealants, and drain baskets must be repaired or replaced immediately to avoid larger problems such as damage to other building components including walls [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Standing water (ponding) on the roof, typically the result of blocked or poorly located drains; this water accelerates the degradation of roofing membranes if allowed to remain in place [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Overflowing eavestroughs or backed-up downspouts caused by debris that prevents proper water drainage and may result in water backing up and overflowing against adjacent building walls [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Overflowing scuppers or overflow pipes (intentionally located higher on the parapet than the main roof drains) — a diagnostic signal that the main roof drains are blocked, with water then spilling onto the ground below near entrances or other disruption points [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Staining or damage on the ceiling or walls inside the home (typically a yellow or brown stain on interior drywall) is an indication that moisture is leaking from the roof above; caution is required because the ceiling may be retaining a reservoir of water [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Black staining on wood within the attic is a possible indication of obstructed attic ventilation or air leaking from interior space into the attic; requires detailed investigation because significant damage can occur to the roof structure over time [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Two-ply low-slope membrane blistering: a large blister can cause the membrane to move at the seam, leading to splitting under stress and a blister cavity filled with water [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Built-up low-slope roof gravel migration: the gravel cover can move and expose the membrane to sun, weather, and underlying roofing felts, causing cracking and accelerated deterioration that can lead to localized failure [[sources/pdf-bc-housing-2020-maintenance-matters-02]].

### Maintenance plan and renewals

- A roof inspection and maintenance plan should be developed specifically for the building if one does not already exist; if the building has home warranty insurance, there may be a maintenance manual that describes the required schedule of tasks [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- The maintenance plan should include checklists identifying required reviews and frequency, with records kept and regularly updated to document maintenance — providing background information that is useful for future reviews and maintenance [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- A qualified roofing professional should be retained to develop a maintenance and monitoring plan of all roofing areas of the building [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- A qualified roofing contractor can identify the type of roofing system, its current condition, and its anticipated life [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- To plan for eventual replacement, the building should establish a renewals plan including replacement frequency and approximate cost [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Roofing contractors are generally equipped with the tools and skills to replace damaged materials, clean drains and gutters, re-secure metal flashing, and re-apply any sealant that has failed [[sources/pdf-bc-housing-2020-maintenance-matters-02]].

### Regulatory and warranty context

- In British Columbia, the Strata Property Act requires strata corporations to maintain a contingency reserve fund (CRF) to pay for common expenses that occur less often than once per year, such as roof replacement [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- The regulations under the Homeowner Protection Act contain provisions requiring owners to mitigate and restrict damage to their homes and permitting warranty providers to exclude coverage for damage caused or made worse by negligent or improper maintenance; failure to carry out proper maintenance — either personally or through unqualified personnel — may negatively affect warranty coverage [[sources/pdf-bc-housing-2020-maintenance-matters-02]].

### Professional resources

- The Roofing Contractors Association of British Columbia (RCABC) is a provincial organization of roofing contractors, consultants, manufacturers, and suppliers [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- The Roof Consultants Institute (RCI; now the International Institute of Building Enclosure Consultants, IIBEC) is an international agency whose members are Registered Roof Observers or Registered Roofing Consultants; registration with RCABC or RCI provides an indication of competence when selecting a roofing contractor [[sources/pdf-bc-housing-2020-maintenance-matters-02]].

## Sources

- [[sources/pdf-bc-housing-2020-maintenance-matters-02]]

## Related

- [[concepts/six-probabilistic-components]]
- [[concepts/probabilistic-reserve-modeling]]
- [[concepts/deck-balcony-component-priors]]
- [[concepts/regime-switching-cost-escalation]]
- [[entities/bc-housing]]
- [[entities/bc-housing-maintenance-matters-series]]
- [[entities/bc-strata-property-act]]
