---
id: docx-bf4965d0d33a
type: docx
title: condo_capital_infra_synthesis_2026-05-08
url: ''
authors:
- python-docx
ingested_at: '2026-05-09T19:38:09Z'
content_hash: sha256:b3bd42d61f34d920cc36e50c5ab94d98fd7423c4f1a6fe843330d89bf3b80001
source_path: raw/docx/docx-bf4965d0d33a.docx
domains:
- condo-capital-infra
nlm_corpus_ids:
- effe1f58-e6ce-4ff0-8728-35c885bff6f4
wiki_pages:
- wiki/entities/florida-sirs.md
- wiki/entities/smartproperty.md
- wiki/entities/propfusion.md
- wiki/entities/solume.md
- wiki/entities/reservewise.md
- wiki/entities/facilio.md
- wiki/entities/cai-reserve-study-standards.md
- wiki/concepts/probabilistic-reserve-modeling.md
- wiki/concepts/six-probabilistic-components.md
- wiki/concepts/tech-enabled-reserve-study-firm.md
- wiki/concepts/regime-switching-cost-escalation.md
- wiki/concepts/cmms-workorder-covariates.md
meta:
  paragraph_count: 283
  table_count: 29
  extraction_tool: python-docx
  original_filename: condo_capital_infra_synthesis_2026-05-08.docx
  subject: ''
published_at: '2026'
filter:
  score: 1.0
  policy_version: condo-capital-infra-v1
  rationale: This is the canonical engagement synthesis defining the entire condo-capital-infra
    domain — vendor landscape across all three tiers (industrial APM, smart building,
    reserve-study-native), explicit FL SIRS / HB 913 regulatory framing, the six probabilistic
    components, and a planned methods stack covering Markov, Weibull, Bayesian hierarchical,
    Monte Carlo with copulas, POMDP, and regime-switching cost escalation. It is the
    source-of-truth document referenced by the project's CLAUDE.md and directly anchors
    inclusion criteria across regulation, methods, vendors, and CMMS ingest.
  decided_at: '2026-05-09T19:38:19Z'
  user_correction: null
---
Condo Capital Infrastructure

AI-Native Predictive Maintenance & Probabilistic Capital Forecasting

Engagement Synthesis — Vendor Landscape, Strategic Recommendation, Year-1 Business Plan, Multi-Year Financial Model, Bootstrap Variant

Date: 2026-05-08

# Executive Summary

This synthesis covers a consulting engagement scoping the state-of-the-art in software, services, and hardware for predictive proactive maintenance of capital infrastructure and probabilistic n-period capital requirement forecasting, with a primary focus on condo association applications. The work spans (1) a vendor landscape scan, (2) strategic recommendation for a 24-month build, (3) minimal capital infrastructure scope to compete credibly against incumbents, (4) a fully-funded Year 1 business plan and financial model, (5) multi-year crossover analysis at 200% YoY growth, and (6) a bootstrap variant on a $100K initial investment.

### Headline Findings

The integrated play does not exist. No vendor in the market today feeds live condition monitoring into a probabilistic reserve fund model. Every "predictive" vendor stops at equipment-level failure prediction; every reserve-study vendor is deterministic.

The regulatory engine is real. Florida SB-4D / SIRS (HB 913, 2025) is forcing every 3+ story condo into mandatory reserve studies with no waivers. CA, NJ, VA bills are following. This created the demand window for the next 5-7 years.

Two reserve-study-native vendors are closest to the wedge — SmartProperty (most mature, 3K studies, 184K assets) and PropFusion (FL SIRS-native, best AI scenario chat). Neither implements probabilistic methods. Methodology is the moat.

Recommended business shape: AI-native, agentic-first, tech-enabled reserve study firm with a proprietary probabilistic engine, software-led delivery (~70%), services (~30%), no hardware in 24 months.

Minimal capital infra scope: probabilistic depth on six components — roof, envelope, plumbing risers, HVAC central plant, elevators, parking deck/podium structure. Match incumbents on the long tail with deterministic CAI-compliant coverage.

Funded plan: ~$471K Year 1 cost, $82K Year 1 revenue, ~$390K Year 1 burn. Crossover at 3× YoY growth lands late Year 5 / early Year 6. Total cumulative funding to crossover: ~$8-10M across seed → Series A → Series B.

Bootstrap on $100K is feasible only with a technical founder, deposits-on-signing pricing, warm Florida pipeline, and a committed 1099 reserve analyst at launch. Cash-flow positive monthly by month 4-5; cumulative break-even month 11-12. Year 1 ends ~break-even with ~10 customers and the option to scale on customer cash from Year 2 onward.

# 1. Engagement Framing

The client is consulting on capital infrastructure management for a condo association. Two distinct domains were bundled in the original ask:

Predictive / proactive maintenance software for capital infrastructure — sensor-driven condition monitoring plus ML failure prediction for physical assets.

Probabilistic capital forecasting — n-period stochastic models of replacement timing and cost for the reserve fund.

### Initial Scoping POV

Three vendor tiers were used to structure the landscape scan:

Industrial APM/CMMS: IBM Maximo, GE APM, AVEVA, Hexagon EAM, Augury, Uptake. Built for plants and utilities. Expensive, overkill for a single condo. Excluded from depth.

Building-specific / smart building: Facilio, Switch Automation, Brainbox AI, Willow, Aquicore. BAS-integrated. Closer fit to commercial real estate than to condo associations.

Reserve-study-native: Association Reserves, SmartProperty, Reserve Data Analyst, PropFusion, ReserveWise, Solume. Domain-correct but mostly deterministic.

The interesting structural gap: industrial-grade tools have predictive maintenance but no reserve-fund framing; reserve-study tools have the financial framing but no live condition signal. The consulting wedge is integration of the two, sized appropriately for residential capital infrastructure economics.

# 2. Vendor Landscape Scan

## 2.1 Executive Summary

The integrated play does not exist. No product feeds live condition monitoring into a probabilistic reserve fund model.

"AI" in reserve-study software (2026) means three things, none of them probabilistic modeling: (1) computer vision for component identification, (2) plain-English LLM Q&A on static study data, (3) scenario sliders on deterministic cash flow.

CAI Reserve Study Standards (2023, 2025) do not require probabilistic methods, so vendors do not build them.

The market is being reset by Florida SB-4D / SIRS (HB 913, 2025): every condo of 3+ habitable stories must have a structural-integrity reserve study every 10 years across eight components, fully funded, no waivers. CA, NJ, VA legislation in motion.

For a single condo, the entire industrial APM tier is irrelevant. Per-user pricing alone runs $45-$126/mo equivalent benchmarks; needs full-time reliability engineers; zero awareness of reserve fund accounting.

Closest to filling the gap: SmartProperty and PropFusion. Both ingest component condition manually, both surface what-if scenarios, both treat the study as a living asset rather than a PDF. Neither has IoT/sensor ingest.

Most overhyped: Brainbox AI for capital infra purposes — the ARIA HVAC agent is real but optimizes operational energy, not capital lifecycle. Willow is impressive engineering but wrong altitude for a single condo association.

PropTech "disruptor" wave (Daisy at $11M Series A, NYC) is mostly tech-enabled management companies, not software vendors.

## 2.2 Tier 1 — Industrial APM / CMMS / EAM (summary only)

Skip entire tier for condo applications. Mention only if the client also owns commercial or industrial assets.

| Vendor | Core Product | Predictive | Forecasting | Condo Fit |
| --- | --- | --- | --- | --- |
| IBM Maximo | Asset management for industrial/utility infra | ML on sensor streams | None for capital reserves | No — enterprise |
| GE Vernova / SmartSignal | Predictive analytics for rotating equipment | Anomaly detection ML | None | No |
| AVEVA APM | Process industry asset performance | Hybrid rule + ML | None | No |
| Augury | Vibration + magnetic sensing for motors | ML; MaintainX partnership 2024 for closed-loop work orders | None | No |
| Senseye (Siemens) | Generative-AI condition monitoring | LLM-augmented PdM | None | No |
| Uptake / C3 AI | Industrial AI platforms | ML at scale | None | No |

## 2.3 Tier 2 — Smart Building / Digital Twin / IoT

None integrate to reserve fund modeling. Multifamily PdM is a real but nascent category; currently focused on operational risk reduction rather than capital lifecycle.

| Vendor | Capability | Forecasting | Condo Fit |
| --- | --- | --- | --- |
| Willow | Building digital twin: knowledge graph + time series + spatial geometry, "Operational AI" | None — no reserve concept | No — enterprise CRE/campus only |
| Facilio | Connected CMMS + maintenance + predictive analytics; FDD on sensor data | None for reserves; work-order forecasting only | Marginal — fits 200+ unit condo with full-time facilities staff |
| BrainBox AI (ARIA) | Autonomous AI agent for HVAC optimization | None | Possibly for HVAC alone |
| Switch Automation | Building data platform + analytics | None | No |
| Aquicore | Energy + performance for commercial RE | None | No |
| KGS Buildings (Clockworks) | FDD analytics on BAS | None | No |
| Coppertree (Kaizen) | FDD analytics layer | None | No |
| HappyCo / Inspectify | Multifamily inspection capture | Feeds capex planning, not native forecasting | Adjacent — captures condition data |

## 2.4 Tier 3 — Reserve-Study-Native and Condo/HOA-Targeted

Where the action is. PropFusion and SmartProperty are the only two with both real customer scale and explicit "study-as-software" positioning. ReserveWise is a credible DIY play. Solume is the dark horse — interesting integrated approach but unproven.

| Vendor | Core Product | Predictive | Forecasting | Condo Fit |
| --- | --- | --- | --- | --- |
| PropFusion | Hybrid: reserve study firm + ReservePulse SaaS | None — relies on RA judgment + visual condition | Deterministic 30-yr; AI chat for scenarios | Strong — built for SIRS |
| SmartProperty | "Living Reserve Study" platform; component inventory + financials | None | Deterministic + scenarios; 184K assets, 3K studies, enterprise logos | Strongest end-to-end platform |
| ReserveWise | DIY reserve study SaaS with AI Vision | Computer vision component ID/RUL | Deterministic | Lightweight; no licensed RA in loop — risky for SIRS |
| Solume | Full HOA management with "dynamic reserve study" | LLM assistant only | Deterministic; "real-time" updates from connected vendors | Promising; less proven |
| Association Reserves / Miller Dodson / Reserve Advisors | Traditional reserve study consulting | None | Deterministic | Industry standard; software is afterthought |
| Yardi Reserve Studies | Reserve module within Yardi | None | Deterministic | Best if client already on Yardi |
| Entrata / RealPage / Buildium / AppFolio | Property accounting with reserve modules | None | Basic deterministic schedules | Workflow-only |
| Planon Capital Planning | Enterprise asset lifecycle planning | None | Deterministic component lifecycle | Heavyweight |
| Daisy | NYC condo/co-op full-service property mgmt | None | Budgeting templates only | Not a software vendor — tech-enabled service |
| FRONTSTEPS / VMS / PayHOA | HOA accounting + comms | None | Reserve tracking only | Adjacent |

## 2.5 Short List — Worth Closer Look

SmartProperty — most mature platform with the largest installed base. If the client wants a single platform that survives a board turnover, this is it.

PropFusion — best for clients who want the reserve analyst engagement and the software in one motion, especially in Florida SIRS jurisdictions.

Solume — only one bundling reserve study into a full HOA operating platform with vendor and budget integration.

ReserveWise — cheapest, modern UX, AI-vision component capture. Valid for small (<50 unit) self-managed condos that need to satisfy state requirements.

Facilio — only if the condo is large enough to justify a connected CMMS (200+ units, $1M+ annual operating budget).

Willow — only if the condo is part of a larger campus or portfolio. Otherwise the ROI math does not pencil.

## 2.6 Notable Absences / Market Gaps

No vendor implements Monte Carlo or Bayesian capital forecasting in production. Every reserve study output is a deterministic point estimate with a fully-funded vs. baseline comparison.

No vendor ingests live condition data into reserve forecasts. SmartProperty and PropFusion treat condition as periodic manual input.

No vendor handles climate or cost-escalation risk explicitly. All deterministic models use a flat inflation assumption (2-4%). Construction cost ran 6-9% in 2022-2025; Florida condo insurance ran 30-100%.

No category leader at the intersection of structural inspection and reserve modeling. Florida SIRS requires both a 25-year milestone inspection and a 10-year reserve study; they are run by separate firms and joined manually.

The CMMS layer (UpKeep, MaintainX, Fiix, Limble) is invisible in reserve software. Work-order history is the best leading indicator of component degradation but no reserve product reads it.

Market shape: a regulated boom (Florida SIRS) is dragging reserve software from PDF-era to SaaS-era right now, but analytical sophistication is still 1990s — deterministic component schedules with a 30-year horizon. The gap between what is possible (probabilistic + sensor-aware + climate-adjusted) and what is productized is the consulting wedge.

# 3. Methods Landscape (Scan Pending)

The methods scan was scoped and prompt-drafted but had not been executed at the time of this synthesis. The structure below captures the planned scope; results from the scan, when run, will refine the technical implementation roadmap but do not change the strategic recommendation in this document.

## 3.1 Method Families to Cover

### Component-level degradation modeling

Markov chain deterioration (DOT bridge/pavement legacy: Madanat, Golabi, Mishalani)

Weibull / exponential / lognormal survival models

Bayesian hierarchical degradation for sparse component data

Physics-based (corrosion, fatigue, envelope thermal)

Hybrid physics-ML (PINNs, gray-box)

Gaussian process regression for condition trajectories

Hidden Markov / state-space when condition is partially observed

### Time-to-failure / replacement timing

Hazard functions, competing risks

Cox PH, AFT models with covariates

Renewal processes for repeatedly-replaced components

Deep RUL (LSTM, transformer) and their data requirements

### Cost / financial

LCCA framing (ASTM E917)

Cost escalation: ENR indices, autoregressive forecasts, regime-switching for insurance shocks

Real options for repair-vs-replace decisions

### Portfolio aggregation

Monte Carlo over component distributions → fund-level cash flow

Copulas for correlated failures (cohort effects)

Stochastic optimization for replacement scheduling

Bayesian decision theory: inspect vs repair vs replace

### Data ingestion and updating

Sensor fusion (BAS, IoT, vibration, thermal)

Bayesian updating with inspection events

POMDP framing for inspection scheduling

Digital twin standards (NIST, ISO 23247)

Work-order / CMMS history as covariates in survival models

### Validation and calibration

Backtesting against realized expenditures

CRPS, PIT, reliability diagrams for probabilistic forecasts

Out-of-sample testing under data scarcity

## 3.2 Planned Output Sections

Executive summary: where the methods leverage is for a condo engagement, where "AI predictive" claims break down

Method family deep-dives with citations

Recommended methods stack for a condo reference architecture

Methods to avoid recommending and why (data hungry, brittle, no payoff at this scale)

Data acquisition priorities — what the client should start collecting now to unlock better methods later

# 4. Strategic Recommendation

Tech-enabled reserve study firm with a proprietary probabilistic engine. Software-led, services-delivered, no hardware. Mix: ~70% software, ~30% services, 0% hardware in a 24-month window.

## 4.1 Why This and Not Alternatives

The vendor scan made the wedge unmistakable: every reserve study shipping today is a deterministic point estimate, the regulatory engine (FL SIRS, CA/NJ/VA following) is forcing thousands of buildings into mandatory studies, and the variance reserve studies miss — construction cost ran 6-9% while plans assumed 2-4%, FL insurance ran 30-100% — is exactly what a probabilistic model captures. The boards getting hit with $50-100K special assessments after "fully funding" their reserves are buyers in pain. PropFusion is closest, but their methodology is still deterministic with an LLM scenario chat layered on. Methodology is the moat.

## 4.2 Concrete Shape

Year 1: 2-3 licensed reserve analysts + a small eng team. Build core: component RUL distributions with Bayesian priors from RSMeans/BOMA/FFC, Monte Carlo aggregation, regime-switching cost-escalation model, automated ingest of CMMS work-order history (UpKeep/MaintainX/Buildium) as covariates. Ship 50-100 studies in Florida at $8-15K each.

Year 2: Expand to CA and NJ as their bills land. 200-400 studies. Productize the engine as a $99-299/mo subscription tail. Begin insurer/reinsurer conversations.

## 4.3 Why Software-Led, Not Service-Led

Pure service firms cannot escape the 3-5 year repurchase cycle. The subscription tail (re-forecasting, scenario tools, board-facing dashboard) converts a transactional study into recurring revenue and creates the data flywheel that makes the engine better over time. This is Daisy's playbook applied to reserve studies instead of property management.

## 4.4 Why No Hardware in 24 Months

The data needed to beat incumbents already exists and is unused — work-order history, accounting transactions, inspection PDFs, milestone reports. Adding leak/vibration/strain sensors is a premium tier 3 years out. Hardware also blows the 2-year horizon: condo board procurement plus retrofit deployment plus warranty exposure pushes past 24 months before revenue. Build the software flywheel first; sensors become a later upsell that funnels into the same probabilistic engine.

## 4.5 Honest Risks

PropFusion or SmartProperty bolt on Monte Carlo themselves. Defensible only by building the licensed-RA-in-the-loop service motion they do not have, locking in the FL channel through that motion.

Reserve studies are a low-frequency purchase. Without the subscription tail this is not a venture-scale business. The subscription has to be real, not a wrapper.

Condo boards are slow buyers. Initial sales cycle 3-6 months. Year-1 revenue assumptions must bake this in.

# 5. Hardware Analysis — The Nest Question

Verdict: Nest-per-unit is a defensible pilot but a sub-optimal hardware allocation. Marginal velocity gain, wrong assets. Better cheap-hardware alternatives exist for similar dollars.

## 5.1 What Nest-per-Unit Actually Gives You

Indoor temp/humidity, HVAC runtime, setpoints, outdoor-weather-correlated load

Useful for inferring building-envelope degradation from aggregated heat-loss residuals across many units, and for estimating central HVAC plant load

Not useful for roof, plumbing risers, elevators, garage decks, structural, fire/life-safety, electrical risers, domestic hot water — i.e., ~75-85% of the reserve fund

Critically: in most condo complexes the in-unit HVAC equipment is unit-owner property, not a reserve-fund line item. You would be instrumenting assets you do not model.

## 5.2 Velocity Impact on Native Model Dev

The v1 engine bottleneck is not real-time telemetry — it is priors and historical truth. The fastest-velocity moves are:

Buy/scrape reserve study histories. In FL/CA, milestone inspections and reserve studies are increasingly public records. A few hundred digitized studies give informative priors per component class — far more leverage per dollar than telemetry from one pilot site.

Industry priors are sitting on the shelf. BOMA, FFC BUILDER, RSMeans, ASHRAE service-life databases. These calibrate component RUL distributions before collecting a single byte of sensor data.

Work-order ingest from incumbent CMMS. A pilot board's UpKeep/MaintainX export is richer reserve signal than thermostat data, costs $0 in hardware, and arrives on day one.

## 5.3 Friction You Are Underweighting

Per-unit consent. 100 units = 100 separate owner approvals, 100 install appointments, 100 wifi configurations, 100 privacy conversations. The deployment-ops cost dwarfs the $20K hardware bill, and you carry it for every new client. That kind of friction is exactly the wrong shape in a 24-month build window.

## 5.4 Better Cheap Hardware First Step

Same ~$20-30K, but on shared infrastructure the association already owns:

1-2 vibration/temp sensors per chiller, boiler, primary pump, cooling tower (~$300-800 ea industrial-grade, or $50-150 with hobbyist accelerometers + a Pi gateway for a pilot)

Riser-entry flow meters and pressure sensors on domestic water and recirc loops (leak signal, plumbing-riser corrosion proxy)

Vibration on the elevator machine room equipment

4-6 indoor temp/humidity loggers in common areas + 1 outdoor station for envelope inference

Strain gauges or crack monitors on 2-4 known-issue structural elements if the SIRS milestone inspection flagged any

Instruments the actual reserve-fund assets, needs only board approval (one decision-maker), deploys in days, produces signals that map directly to component-level RUL models.

## 5.5 Where Nest Could Earn Its Keep

Marketing/narrative value with boards and insurers. "Sensored building" is a sellable story. If the client's sales motion needs a visible smart-building artifact, Nest is the cheapest one. But that is a GTM line item, not an R&D one — fund it separately, do not justify it on model quality.

# 6. Minimal Capital Infrastructure Scope

Six components. Probabilistic depth on these, deterministic-and-CAI-compliant on everything else.

## 6.1 The Six

Roof systems

Building envelope (cladding, windows, sealants, balconies/railings)

Plumbing risers and domestic water (cold, hot, recirc)

HVAC central plant (chillers, boilers, cooling towers, primary pumps)

Elevators

Parking deck / podium / structural concrete (mid- and high-rise only)

## 6.2 Why Six, Not Three

Three would not move enough fund variance to justify replacing a SmartProperty study. Six covers ~70-80% of typical condo reserve dollars and all eight SIRS-mandated component classes. Six is also small enough to actually engineer well in 12-18 months — each component class needs its own degradation model, prior calibration, telemetry adapter, and validation set. Going broader dilutes the AI-native claim into the same shallow component-list everyone else ships.

## 6.3 Why These Six

These are the components that dominate variance in actual reserve outcomes:

Roof life ranging 18-30 years is a $200-500K swing on a 100-unit building

Balcony concrete is the post-Surfside variable redrawing FL insurance

A full re-pipe is $5-15K/unit

A chiller is $200-500K

Elevator modernization is $80-200K each

Podium repairs run $500K-$5M

Lower-variance line items (paving, paint, pool, finishes, fire-life-safety) eat reserve-study pages but do not move fund-level uncertainty enough for probabilistic methods to pay off. Cover them deterministically — same as SmartProperty — and do not waste eng cycles modeling them.

## 6.4 SIRS Alignment

SIRS-mandated components: roof, structure, fireproofing/fire protection, plumbing, electrical, waterproofing/exterior painting, windows, foundation. Five of six map directly. Electrical and fire-life-safety covered deterministically. The story becomes: "for every SIRS-critical component, you get a P50/P90 forecast and a probability-of-failure-by-year curve, not a single number."

## 6.5 Three-Layer Evidence Stack Per Component

| Component | Priors (day 1) | Historical truth (acquirable) | Telemetry (v2) |
| --- | --- | --- | --- |
| Roof | Manufacturer service life by membrane, ASHRAE, RSMeans, NRCA | Reserve study comps, replacement records, insurance claims | Drone IR moisture surveys, leak sensors at penetrations |
| Envelope | AAMA window service life, sealant degradation, concrete cover-corrosion | Milestone inspections, repair work orders, photo archives | Balcony strain gauges, sealant-joint monitors, periodic IR scans |
| Plumbing risers | Copper/PEX/galvanized RUL by water chemistry, AWWA data | Leak history from work orders, prior re-pipe records, water bills | Riser-entry flow + pressure, recirc temp, leak detection |
| HVAC central plant | ASHRAE service life, manufacturer MTBF, BOMA | Maintenance contracts, work orders, refrigerant loss logs | Vibration, runtime, kWh, fault codes from BAS |
| Elevators | NEII modernization timelines, code-cycle data | Service contracts, mechanic call-back records, state inspection reports | Door cycle counters, machine-room vibration, fault codes |
| Parking deck / podium | DOT bridge-deck deterioration, chloride-ingress curves, ACI | Engineer reports, milestone inspection findings, repair history | Chloride probes, crack/strain monitors, post-tension load cells |

## 6.6 Where You Beat SmartProperty

Per-component probabilistic output: P50/P90/P99 fund-need curves, probability-of-special-assessment-by-year, sensitivity to escalation regime

Bayesian updating from work-order ingest — invisible in SmartProperty

Cohort priors. Buildings cluster by vintage, climate zone, construction type. Hierarchical models pool strength across the cohort, beating one-building-at-a-time studies

Climate- and insurance-aware cost escalation. Component-specific escalation regimes (FL exterior coatings escalate differently than Midwest plumbing)

Telemetry-ready by design. Every component has a defined sensor adapter from day 1 — SmartProperty has no telemetry path

## 6.7 What You Explicitly Do Not Try to Do Better

Component identification UX (ReserveWise has computer vision; not the moat)

Accounting integration (Yardi/AppFolio/QuickBooks; commodity)

Funding-plan presentation (CAI-standard tables; commodity)

Coverage of the long tail of low-variance line items (match the standard, do not innovate)

# 7. Year 1 Business Plan — Funded Version

## 7.1 Business in One Paragraph

AI-native, probabilistic reserve studies for condo associations under regulated reserve-study mandates (FL SIRS first, CA/NJ next). Two-product structure: a one-time CAI-compliant study with a probabilistic addendum (P50/P90 fund-need curves, work-order-conditioned RULs on the six high-variance components) and a recurring subscription that re-runs the forecast as new evidence lands. Lean human team — one licensed reserve analyst, one founding engineer, fractional PE-of-record — with agentic systems doing PDF/inspection ingest, work-order parsing, study drafting, scenario generation, board Q&A, and internal QA. Year 1 is a design-partner year: 5 buildings, real cash flow, but the deliverable is the engine and the historical-truth corpus.

## 7.2 Pricing

| Line | Price | Notes |
| --- | --- | --- |
| Initial reserve study (one-time) | $15,000 per 100-unit assoc. | Premium to deterministic incumbents (~$8-12K), discount to enterprise PE-attested SIRS work (~$20-25K). Year-2 list moves to $18-20K. |
| Live Forecast subscription | $299/mo per assoc. | 12-mo minimum. Includes work-order ingest, monthly re-forecast, board dashboard, scenario chat. Auto-renew. |
| One-time onboarding fee | Bundled | Do not separate; reduces close friction. |

## 7.3 Year 1 Revenue (5 customers, staggered)

| Customer | Study Fee | Sub Months in Y1 | Sub Revenue |
| --- | --- | --- | --- |
| #1 (mo 2) | $15,000 | 9 | $2,691 |
| #2 (mo 4) | $15,000 | 7 | $2,093 |
| #3 (mo 6) | $15,000 | 5 | $1,495 |
| #4 (mo 8) | $15,000 | 3 | $897 |
| #5 (mo 10) | $15,000 | 1 | $299 |
| Total | $75,000 | — | $7,475 |

Total Year 1 gross revenue: ~$82,475.

## 7.4 Cost Structure

### Startup / one-time

| Item | Cost |
| --- | --- |
| Entity formation, contracts (NDA, MSA, sub-processor terms, deliverable license) | $20,000 |
| E&O / GL / cyber insurance binders | $15,000 |
| Brand identity + marketing site + content infrastructure | $10,000 |
| Laptops, monitors, office equipment (3 people) | $10,000 |
| Initial domain corpus acquisition (purchased reserve study comps, milestone PDFs, FOIA) | $10,000 |
| State licensure & registration (FL, CA business + reserve analyst affiliations) | $3,000 |
| Initial cloud setup, SOC2-ready baseline | $5,000 |
| Subtotal | $73,000 |

### Fixed annual — people

| Role | Headcount | Loaded Cost | Notes |
| --- | --- | --- | --- |
| Founder / CEO | 1.0 FTE | $0 cash | Equity-only Year 1 |
| Founding engineer (full-stack + ML/agentic) | 1.0 FTE | $170,000 | $140K base + benefits/payroll |
| Reserve analyst (licensed RS-RA) | 0.5 FTE | $65,000 | Fractional/employment hybrid; necessary for CAI-compliant signature |
| W2 subtotal | — | $235,000 | — |

### Fixed annual — contractors & insurance

| Item | Annual |
| --- | --- |
| Fractional FL PE-of-record (5 studies × 12 hrs × $250) | $15,000 |
| Field inspection tech (5 visits × $1K) | $5,000 |
| Bookkeeping / fractional CFO | $8,000 |
| E&O insurance ongoing | $10,000 |
| GL + cyber insurance ongoing | $4,000 |
| Legal retainer (post-formation) | $6,000 |
| Subtotal | $48,000 |

### Variable per-engagement (5 studies)

| Item | Per Study | 5 Studies |
| --- | --- | --- |
| AI inference (PDF ingest, drafting, QA) | $400 | $2,000 |
| Drone IR roof survey (contracted) | $1,000 | $5,000 |
| Inspection materials, printing, deliverable binding | $200 | $1,000 |
| Travel / per diem for site visit | $600 | $3,000 |
| Subtotal variable | $2,200 | $11,000 |

### External SW Stack — AI / Agentic

| Tool | Purpose | Annual |
| --- | --- | --- |
| Anthropic API (Claude) | Primary LLM for agents | $24,000 |
| OpenAI / Voyage embeddings | RAG | $2,000 |
| Vector DB (Pinecone or Weaviate Cloud) | Retrieval over historical studies + work-orders | $5,000 |
| Langfuse or LangSmith | Agent tracing, eval, prompt versioning | $1,500 |
| Replicate / Modal | On-demand GPU for CV jobs | $2,000 |
| AI subtotal | — | $34,500 |

### External SW Stack — Dev Infrastructure

| Tool | Annual |
| --- | --- |
| AWS or GCP (compute, storage, RDS, S3) | $14,000 |
| Cloudflare | $1,200 |
| Auth (Clerk or WorkOS) | $1,500 |
| Sentry | $600 |
| GitHub Team + Copilot | $600 |
| Linear | $500 |
| Subtotal | $18,400 |

### External SW Stack — GTM and Domain Data

| Tool | Annual |
| --- | --- |
| HubSpot Starter | $3,600 |
| Google Workspace | $720 |
| Notion + Slack | $1,200 |
| DocuSign | $480 |
| Stripe (2.9%) | $2,400 |
| QuickBooks | $1,200 |
| Calendly + 1Password + misc | $400 |
| RSMeans (cost data) | $3,500 |
| BOMA Experience Exchange | $1,200 |
| ASHRAE / ACI / NRCA memberships | $1,000 |
| Bluebeam Revu (3 seats) | $900 |
| Subtotal | $16,600 |

Total external SW: ~$69,500/year. ~5% of total Year 1 cost, ~85% of Year 1 revenue.

### Marketing & Sales

| Line | Annual |
| --- | --- |
| CAI conferences (Florida + national, booth + travel) | $12,000 |
| Content (writer contractor, SEO infra) | $10,000 |
| Paid LinkedIn (board members, property managers) | $8,000 |
| Sales travel & on-site meetings | $5,000 |
| Subtotal | $35,000 |

## 7.5 Year 1 P&L

| Line | Amount |
| --- | --- |
| Revenue | $82,475 |
| One-time startup costs | ($73,000) |
| W2 salaries (loaded) | ($235,000) |
| Contractors + insurance + bookkeeping | ($48,000) |
| Variable per-engagement | ($11,000) |
| External SW | ($69,500) |
| Marketing & sales | ($35,000) |
| Total operating cost | ($471,500) |
| Net Year 1 | ($389,025) |

Cash funding requirement: ~$425-475K to fund Year 1 with a 1-2 month working-capital buffer into Year 2. Realistic seed target: $750K-$1M to cover Year 1 plus 6-9 months of Year 2 ramp.

## 7.6 Sensitivities

| Variable | Base | Downside | Upside |
| --- | --- | --- | --- |
| Customers acquired Year 1 | 5 | 3 | 8 |
| Study price | $15K | $12K | $18K |
| Subscription attach | 100% | 60% | 100% + add-ons |
| Y1 revenue range | $82K | $38K | $155K |

## 7.7 Where Agentic Pays Off in Year 1

Headcount is the pressure point. A traditional reserve firm needs ~1 analyst per 30-40 studies/year. Throughput target is 50-80 studies/year per analyst, achieved by:

Ingest agent parses inspection PDFs, milestone reports, work-order exports, building plans into structured component inventory — saves ~6 hrs/study

Drafting agent generates narrative sections of CAI-compliant deliverable from structured data — saves ~4 hrs/study

QA agent runs internal red-team checks (numerical consistency, missing components, escalation sanity) before analyst review — saves ~2 hrs/study and prevents the most common errors driving E&O claims

Board Q&A agent handles ongoing questions in subscription product, deflecting ~70% of post-delivery support load

Internal dev agents (Claude Code, Copilot) drive ~2-3x engineering velocity, making 1 founding engineer plausible for a real probabilistic system

The licensed reserve analyst still owns sign-off — agentic does not buy a way around licensure or E&O exposure. Agents reduce the analyst's cost per study, not the analyst's existence.

## 7.8 Year 1 Milestones

End of Q1: Engine v1 (priors-only probabilistic forecasts on the six components) shipped to first customer

End of Q2: Work-order ingest live; first Bayesian update from real customer data

End of Q3: 3 customers live, subscription churn ≤0%, first board-level case study published

End of Q4: 5 customers live, ≥3 with ≥6 months of subscription data, first re-forecast cycle completed showing the value of the live-update product

Concurrent: SOC 2 Type 1 by month 9; channel pilot signed with one management company by month 10

# 8. Multi-Year Financial Model & Crossover Analysis

Crossover lands late Year 5 / early Year 6 at 200% YoY growth (3× the prior year). At 2× (doubling), crossover slips to Year 7+.

## 8.1 Customer Ramp at 3× YoY

| Year | New Customers | Active Subs (EOY, 90% retention) |
| --- | --- | --- |
| 1 | 5 | 5 |
| 2 | 15 | 20 |
| 3 | 45 | 63 |
| 4 | 135 | 191 |
| 5 | 405 | 577 |
| 6 | 1,215 | 1,734 |

## 8.2 Revenue Model

Assumes study fee rises with brand pricing power ($15K Y1 → $20K Y3+), 100% subscription attach, $299/mo, 90% gross retention. New-customer subscription accrues 6 months in year of acquisition.

| Year | Study Fee | Study Revenue | Sub Revenue | Total Revenue |
| --- | --- | --- | --- | --- |
| 1 | $15K | $75K | $9K | $84K |
| 2 | $18K | $270K | $45K | $315K |
| 3 | $20K | $900K | $151K | $1.05M |
| 4 | $20K | $2.70M | $468K | $3.17M |
| 5 | $20K | $8.10M | $1.42M | $9.52M |
| 6 | $20K | $24.3M | $4.41M | $28.7M |

## 8.3 Cost Model

Headcount scales but agentic ops keeps the people-per-study ratio flat. Reserve analyst throughput holds at 60 studies/analyst/year. E&O insurance scales aggressively with portfolio — this line item is the single biggest threat to crossover.

| Cost Line | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 |
| --- | --- | --- | --- | --- | --- | --- |
| Salaries (loaded) | $235K | $620K | $1.34M | $2.41M | $4.50M | $8.20M |
| Founder/exec comp (post-seed) | $0 | $150K | $180K | $220K | $260K | $300K |
| PE + field contractors | $20K | $60K | $180K | $400K | $900K | $2.0M |
| Insurance (E&O + GL + cyber) | $14K | $30K | $80K | $200K | $450K | $900K |
| Per-study variable | $11K | $33K | $99K | $297K | $891K | $2.67M |
| External SW (AI + dev + GTM + domain) | $70K | $130K | $280K | $600K | $1.30M | $2.50M |
| Marketing & sales | $35K | $150K | $400K | $900K | $1.60M | $2.80M |
| Legal / G&A / ops | $20K | $60K | $120K | $250K | $400K | $700K |
| One-time / startup | $73K | $0 | $0 | $0 | $0 | $0 |
| Total cost | $478K | $1.23M | $2.68M | $5.28M | $10.30M | $20.07M |

## 8.4 Net Cash Result

| Year | Revenue | Cost | Net | Cumulative Burn |
| --- | --- | --- | --- | --- |
| 1 | $84K | $478K | ($394K) | ($394K) |
| 2 | $315K | $1.23M | ($915K) | ($1.31M) |
| 3 | $1.05M | $2.68M | ($1.63M) | ($2.94M) |
| 4 | $3.17M | $5.28M | ($2.11M) | ($5.05M) |
| 5 | $9.52M | $10.30M | ($780K) | ($5.83M) |
| 6 | $28.7M | $20.1M | +$8.6M | (burn arrested, ramp positive) |

Crossover: Year 6, roughly month 60-66. Year 5 ends modestly negative; the inflection happens as the subscription book passes ~600 active and study throughput passes ~400/year, while the fixed-cost base only roughly doubles.

## 8.5 What Drives the Crossover

Subscription book, not study fees. Y6 sub revenue is $4.4M against ~$1M cost-to-serve. That ~75% gross-margin recurring layer is what tips the model. If sub attach drops to 60% or retention to 80%, crossover slips a full year.

Reserve-analyst leverage. Throughput of 60 studies/analyst/year is the agentic dividend. At traditional throughput (30/yr), need 2× the analyst headcount and the model never crosses at this growth rate without raising prices.

CAC compression through channel. Sized assuming 1-2 management-company channel deals signed by end of Y2. Without channel, direct sales costs blow through assumptions by Y3-Y4.

E&O insurance. Scales nonlinearly. A single large claim Y3-Y4 can reset premiums and erase the crossover.

## 8.6 Sensitivity Table

| Scenario | Crossover |
| --- | --- |
| Base case (3× YoY, 100% sub attach, 90% retention) | Y6 mid-year |
| 2× YoY growth | Y7-Y8 |
| 3× growth + 70% sub attach | Y7 |
| 3× growth + price holds at $15K | Y6 late |
| 3× growth + channel partner Y2 (CAC ↓40%) | Y5 mid-year |
| 3× growth + in-house PE at $250K loaded from Y3 | Y6 early |
| Major E&O claim in Y4, premiums 3× | Y7+ |

## 8.7 Funding Implication

Cumulative cash need to crossover: ~$6M at burn, plus ~$2-3M working-capital and runway buffer = ~$8-10M total funding before profitability.

Pre-seed / seed (now): $1-1.5M to fund Y1 + start of Y2

Series A (mid-Y2): $5-7M to fund Y2-Y3 ramp

Series B (Y4): $10-15M to push through Y5 and into crossover

## 8.8 POV — Is 3× YoY Achievable

3× from 5→15→45 is normal for a regulated-tailwind seed-stage company. 45→135 (Y3→Y4) is hard but possible with channel partners and FL+CA running concurrently. 135→405 (Y4→Y5) is where the model breaks if still selling direct — that is roughly one new customer every business day, with concurrent inspection, study, and onboarding ops. Y5 is the year channel needs to be doing 60%+ of acquisition or the people-cost line explodes and pushes crossover to Y7.

Honest read: plan for crossover in Y6, raise as if it is Y7, treat any earlier outcome as upside. The math at 3× is tight enough that one bad assumption — sub attach, retention, or insurance — gives back the entire margin at the inflection.

# 9. Bootstrap Variant — $100K Initial Investment

Doable but tight. $100K survives Year 1 only if (a) the founder is technical, (b) you charge 50% deposits upfront, (c) you have a warm FL pipeline at launch, (d) you ship v1 in 90 days. Cash-flow neutral monthly by month 4-5, cumulative break-even month 11-12, real cash starts in Year 2.

## 9.1 What Changes Structurally

| Dimension | Funded Plan | Bootstrap |
| --- | --- | --- |
| Founder role | Strategy/sales | Strategy + sales + 60-70% engineering with agentic tooling |
| Engineering | 1 US founding eng FTE ($170K) | 1 offshore part-time at 20 hrs/wk + contract eng for spikes |
| Reserve analyst | 0.5 FTE W2 ($65K) | 1099 contractor paid per study (~$4K/study) |
| PE-of-record | Fractional W2-style retainer | 1099 per study (~$2.5K/study) |
| v1 ship cadence | Engine pre-built before customer 1 | Engine built alongside customers 1-3; first delivery is hybrid |
| Pricing | $15K flat | Tiered: $12K design partners 1-3, $18-20K customers 4-10 |
| Payment terms | Net 30 on delivery | 50% deposit on signing, 50% on delivery |
| Subscription | $299/mo, 12-mo minimum | Same — explicitly bundled, not opt-in |
| Marketing | Conferences + content + paid LinkedIn | Founder direct outreach + 1 CAI FL event + LinkedIn organic |
| Insurance | Full E&O + GL + cyber | Minimum viable E&O + GL only; cyber added Y2 |

## 9.2 Revised Pricing

The deposit structure is the load-bearing piece. Reserve studies do not typically take deposits, but the value-add framing ("AI-native, probabilistic, longer engagement") justifies it and the contract template should make it standard.

| Cohort | Study Fee | Deposit | Balance | Sub Bundled |
| --- | --- | --- | --- | --- |
| Design partners 1-3 (case study + data rights) | $12,000 | $6,000 on signing | $6,000 on delivery | $299/mo, 12-mo, first 3 mo free |
| Customers 4-10 | $18,000 | $9,000 on signing | $9,000 on delivery | $299/mo, 12-mo, no free months |

Year 1 average study fee: ~$16K. Average sub commitment: ~$3,000/customer over Y1.

## 9.3 Lean Cost Structure (Annualized)

### Fixed

| Line | Annual | Notes |
| --- | --- | --- |
| Founder salary | $0 | Equity / personal runway |
| Offshore eng (LATAM senior, 20 hrs/wk, $35/hr) | $35,000 | Or India/SE Asia at 30 hrs/wk |
| Contract eng bench (specialist spikes) | $5,000 | Reserve, drawn as needed |
| Bookkeeper / CPA (fractional) | $3,000 | — |
| E&O + GL insurance | $13,000 | Cyber deferred |
| Legal (incorp + templates + privacy) | $7,000 | One-time loaded into Y1 |
| Subtotal | $63,000 | — |

### Variable per study (10 studies)

| Item | Per Study | 10 Studies |
| --- | --- | --- |
| Reserve analyst (1099, licensed RS-RA) | $4,000 | $40,000 |
| FL PE-of-record (1099) | $2,500 | $25,000 |
| Field tech site visit | $1,000 | $10,000 |
| AI inference per study (with prompt caching) | $300 | $3,000 |
| Materials, deliverable production | $200 | $2,000 |
| Subtotal | $8,000 | $80,000 |

### External SW Stack (Lean)

| Tool | Annual |
| --- | --- |
| Anthropic API (Claude, with prompt caching) | $6,000 |
| OpenAI/Voyage embeddings + Postgres pgvector (skip Pinecone) | $1,200 |
| Supabase or Railway (DB + auth + storage) | $1,500 |
| Vercel (frontend) | $300 |
| Cursor + Claude Code | $720 |
| GitHub Team | $200 |
| DocuSign personal | $300 |
| Stripe fees (2.9% on $172K) | $5,000 |
| QuickBooks Online | $1,200 |
| Google Workspace | $400 |
| Subtotal | $16,820 |

Drops $50K vs the funded plan. Pinecone, Langfuse, full HubSpot, paid Notion, Linear, Clerk all deferred. Postgres pgvector replaces Pinecone, free-tier observability replaces Langfuse, Notion replaces Linear. The agentic stack still works — just on cheaper substrate.

### Marketing & Travel

| Line | Annual |
| --- | --- |
| CAI Florida chapter membership + 1 chapter event booth | $3,000 |
| Sales + site-visit travel (founder, FL trips) | $5,000 |
| Subtotal | $8,000 |

Total Year 1 cost: ~$168,000.

## 9.4 Year 1 Revenue (Bootstrap)

| Source | Amount |
| --- | --- |
| Studies (3 × $12K + 7 × $18K) | $162,000 |
| Subscription (avg 4 mo × 10 customers × $299, with 3 mo free for design partners) | $9,500 |
| Total Y1 revenue | $171,500 |

Net Y1 P&L: roughly break-even (+$3,500).

## 9.5 Monthly Cash Flow — The Actual Question

P&L break-even hides what matters: does $100K survive the first 3-4 months before deposits and balance payments stack? Modeling with 1 new customer signed per month starting M2, study delivered ~8 weeks later:

| Month | Cash In | Cash Out | Monthly Net | Cash on Hand |
| --- | --- | --- | --- | --- |
| M1 | $0 | $14K (legal + eng + insurance + SW) | ($14,000) | $86,000 |
| M2 | $6,000 (DP #1 deposit) | $10,000 | ($4,000) | $82,000 |
| M3 | $6,000 (DP #2 deposit) | $9,000 | ($3,000) | $79,000 |
| M4 | $6,000 (DP #1 balance) + $6,000 (DP #3 deposit) | $13,000 | ($1,000) | $78,000 |
| M5 | $6,000 + $9,000 (#4 deposit) + $300 sub | $13,000 | $2,300 | $80,300 |
| M6 | $6,000 + $9,000 (#5 deposit) + $600 sub | $13,000 | $2,600 | $82,900 |
| M7 | $9,000 + $9,000 (#6 deposit) + $1,200 sub | $13,000 | $6,200 | $89,100 |
| M8 | $9,000 + $9,000 + $1,500 sub | $13,000 | $6,500 | $95,600 |
| M9 | $9,000 + $9,000 + $1,800 sub | $13,000 | $6,800 | $102,400 |
| M10 | $9,000 + $9,000 + $2,100 sub | $13,000 | $7,100 | $109,500 |
| M11 | $9,000 + $9,000 + $2,400 sub | $13,000 | $7,400 | $116,900 |
| M12 | $9,000 + $9,000 + $2,700 sub | $13,000 | $7,700 | $124,600 |

Cash low point: ~$78K in M4. Never breaches $100K floor by more than 22%.

Monthly cash-flow positive: M5 onward.

Cumulative cash position above starting capital: M9.

EOY 1 cash: ~$125K (Customer 10 balance ~$9K still receivable into Y2; 10 active subs at ~$3K/mo).

The model only works if the customer-per-month cadence holds. Slip to one customer every six weeks and the M4 cash low drops to ~$60K and cumulative recovery moves to M11. Slip to one every two months and you are insolvent by M9.

## 9.6 What You Give Up vs Funded Plan

Engine sophistication at v1. First three deliveries are deterministic CAI-compliant + Monte Carlo addendum over priors only. No work-order ingest until M5-6. No Bayesian updating from historical truth until M8-9. The "AI-native" claim in months 1-3 is supported by agentic ingest/drafting/QA, not yet by the probabilistic engine. Be honest about this with design partners.

Sales reach. Founder-led only. No paid acquisition. No content marketing infra. Caps Y1 customer acquisition at roughly 12-15 even in best case.

Brand polish. No design system, no podcast, no thought-leadership engine. Revisited Year 2 from cash flow.

Legal robustness. Template contracts, fractional review only. First time facing a real dispute, you will wish you had spent more.

Pre-built engine flexibility. Any v1 architectural mistake propagates through customers 1-5 and is costly to refactor.

Insurance posture. Cyber + portfolio E&O scaling deferred. One incident in Y1 (data breach, deliverable error) can end the company.

## 9.7 The Four Gates

Gate 1 (pre-launch): 3 design-partner LOIs in hand before incorporating. Without these, do not start.

Gate 2 (M3): First study delivered on time, board accepted. If delivery slips past M4, the cash model breaks.

Gate 3 (M6): ≥6 customers signed, deposits collected, no insurance claims, ≥80% subscription attach holding. If subs are opt-out instead of bundled or attach drops below 70%, kill v3 features and double down on study throughput.

Gate 4 (M9): Pipeline of ≥8 customers for first half of Y2 visible. Decide whether to keep bootstrapping or open a small Series Seed off the traction.

## 9.8 POV — What This Plan Actually Is

This is a service business with a software thesis, not a software company. At $100K you cannot build an AI-native software company in this market — the engine + sales + insurance + analyst overhead is too heavy. What you can build is a high-margin, agent-augmented, premium-priced reserve study practice that uses customer revenue to fund the software engine over 18-24 months. By end of Y2 you should have ~30 customers, a real probabilistic engine, ~$500K-700K cash, and the option to either (a) keep bootstrapping at 50-70% YoY growth, (b) raise a Series Seed off proven traction at much better terms than a cold pitch today, or (c) sell the practice to PropFusion/SmartProperty as a methodology + customer-list acquisition.

The single biggest risk is not money — it is founder bandwidth. Selling, delivering, building, recruiting, and managing offshore in parallel is the actual constraint. A second co-founder (technical or sales) is worth more than another $100K of capital here.

The single biggest underappreciated cost is reserve-analyst availability. You need a licensed RS-RA willing to work 1099 with an unproven AI-augmented firm. That person is rare and getting them committed pre-launch is on the same critical path as the design-partner LOIs.

If both — co-founder and a committed contract analyst — are in place at launch, $100K is enough to get to Y2 with a real business. If either is missing, raise a small friends-and-family round to $250K instead.

# 10. Open Questions & Next Steps

## 10.1 Open Questions Surfaced During Engagement

Is the client positioned to actually run a regulated service business (hire/license reserve analysts, carry E&O insurance, build PE relationships in FL), or are they software-only? This collapses the option space — software-only forces an OEM/embedded play under SmartProperty or PropFusion, which is a much weaker hand.

Founder profile: technical or non-technical? Bootstrap viability depends on this.

Does the client have an existing FL pipeline (board relationships, property management firm partnerships) or is this a true cold start? Affects Year 1 customer count assumptions and gate timing.

Methods scan: not yet executed. Should be run before any meaningful engine architecture decisions are committed.

## 10.2 Recommended Immediate Next Steps

Run the methods scan (prompt drafted in Section 3) to validate the technical roadmap before locking eng resourcing.

Decide funded-vs-bootstrap path based on founder profile and capital availability.

If funded: begin pre-seed / seed conversations with proptech-aligned investors. Target $1-1.5M.

If bootstrap: begin design-partner outreach in Florida (target 3 LOIs) and recruit a 1099 RS-RA willing to work pre-launch.

Either path: confirm CAI Reserve Study Standards compliance posture with a licensed RA before scoping the v1 deliverable.

Either path: start acquiring historical-truth corpus immediately — purchasable reserve study databases, FL milestone inspection FOIA, public records. This work is rate-limited by procurement, not engineering, so it should start now regardless of capital path.

## 10.3 Items Not Covered in This Engagement

Detailed methods scan (prompt drafted, scan deferred)

Specific vendor selection for any single tier (e.g., choosing between Pinecone vs pgvector at scale)

Detailed legal/compliance framework for handling reserve-study deliverables across multiple states

Insurance broker shortlist for E&O coverage of a novel AI-augmented service

Exit/M&A landscape analysis (SmartProperty, PropFusion, REIT-side acquirers)

Detailed cohort-level retention modeling beyond the 90% gross retention assumption
