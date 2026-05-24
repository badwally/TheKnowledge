---
id: note-2026-05-11-seed-deck-brief
type: note
title: Seed Deck Brief — Halifax-Chair / Seed-Investor
url: ''
authors:
- Condo Capital Infrastructure project
ingested_at: '2026-05-11T21:45:11Z'
content_hash: sha256:2205750346a6acfd06a62a154f691a72485fb84c4a4f26a6dd4585880a8882ed
source_path: gtm/seed-deck-brief.md
domains:
- condo-capital-infra
filter:
  score: 0.2
  policy_version: condo-capital-infra-v1
  rationale: This is an internal GTM/seed-deck brief authored by the project itself,
    not an external primary source on reserve-study methodology, regulation, or vendor
    competitive intelligence. While it references in-scope material (NS Bill 38, six-component
    engine, vendor landscape), it is a derivative artifact that cites the corpus rather
    than contributing new evidence to it — appropriate for the project repo, not for
    the condo-capital-infra knowledge wiki.
  decided_at: '2026-05-11T21:45:39Z'
  user_correction:
    decided_at: '2026-05-11T21:46:04Z'
    score: 1.0
    rationale: Project-internal canonical seed-deck brief, sibling to elevator pitch.
      Halifax-chair / seed-investor specific framing. Filed alongside elevator pitch
      for citation continuity across pitch artifacts.
nlm_corpus_ids:
- effe1f58-e6ce-4ff0-8728-35c885bff6f4
---

---
id: GTM-SEED-DECK-BRIEF-001
date: 2026-05-11
status: v1-draft
audience: Halifax HOA incoming board chair (also a prospective seed investor)
target_format: 12–15 slide intro deck, executed by Claude Design
parent_docs:
  - gtm/elevator-pitch.md
  - gtm/canada-first-revenue-model.md
  - gtm/exit-thesis-acquirer-mapping.md
  - gtm/halifax/04-board-pitch-deck-outline.md
  - regulatory/ns-condominium-act-summary.md
  - engine/v0_calibration/v0_5_update.md
  - synthesis/addendum-sequence-reorder-2026-05-10.md
  - decisions/0004-sequence-reorder-canada-first-gtm.md
---

# Seed Deck Brief — Halifax-Chair / Seed-Investor

## 0. Framing for Claude Design

One reader, two hats. The audience is a single individual who will, in the same month, (a) be asked to back our seed and (b) chair the board of our warm-lead Halifax HOA. The deck has to read as truthful from both seats simultaneously. Investor curiosity wants methodology depth, exit math, acquirer landscape; chair fiduciary duty wants the seal, the data terms, the price, and the assurance that we will not embarrass the board.

Three rules that fall out of that:

1. The Halifax engagement is the wedge in the GTM and the deliverable to the chair's building. Treat it as both — but make the alignment explicit on the slide that introduces it. No hiding.
2. Methodology jargon is permitted (Markov, Weibull, Bayesian, Monte Carlo, copulas, regime-switching) because the investor warrants it. Each technical slide must close with the picture (P50/P90 fan) and the seal (NS-licensed P.Eng.) so the chair has a non-technical handhold.
3. We are pre-revenue, single-founder, with a probabilistic engine validated on one cohort. Do not over-claim. Honesty raises the multiple here — the audience will be inside the data within ninety days and will catch hand-waving.

Length target: 12–15 slides plus a one-slide appendix index. Speaking time 18–22 minutes; Q&A 25+ minutes.

## 1. Strategic frame (the spine the slides hang on)

### Opportunity

North American condominium boards spend $8K–$30K every 3–5 years on reserve fund studies that produce a single deterministic line per component — "your roof will fail in year 12 and cost $400K." Reality is a distribution: P10 year 8 / P50 year 12 / P90 year 17, with explicit dependence on weather, deferred maintenance, and correlated component failures. Boards need that distribution to defend special assessments to owners, lenders, and insurers. No incumbent ships it.

The market is not "reserve studies" — it is the **structured-capital-planning compliance market**: a recurring, regulator-mandated purchase across BC (depreciation reports every 3 years per Strata Property Act), ON (Condo Act §94, every 3 years), AB (Condominium Property Act, every 5 years), QC (Bill 16 *carnet d'entretien*, in force August 2025), NS (R.S.N.S. 1989 c.85 + Bill 38 2023 — every 5 years for 10+ unit corporations), FL (HB 913 SIRS post-Surfside), CA (Davis-Stirling §5550), NJ, NY. Penetration of probabilistic methodology is effectively zero today.

Underfunded reserves at Champlain Towers South priced at $1B and 98 lives. Every regulator in scope is now structurally over-correcting. The buying mandate is statutory, not discretionary.

### Tech thesis

A six-component probabilistic engine plus CAI-compliant deterministic long-tail. The six components — roof, building envelope, plumbing risers, HVAC central plant, elevators, parking deck / podium structure — carry roughly 70% of reserve-fund variance in concrete high-rise stock. The stack:

- Weibull / lognormal survival for component-level failure timing.
- Markov chain deterioration over inspection states.
- Bayesian hierarchical priors keyed to structure-type cohorts (concrete high-rise, wood-frame mid-rise, podium hybrid). Every fielded study tightens the next one. **This is the data flywheel and the moat.**
- Monte Carlo aggregation with copulas for correlated failures — roof and envelope share weather covariates; HVAC and elevators share electrical-system covariates. Deterministic engines treat these as independent and systematically under-state P90 tail risk.
- Regime-switching cost-escalation. Not flat 3% — explicit modeling of construction-inflation regimes, labor-supply regimes, materials-supply regimes.
- CMMS work-order covariates ingested from the property's operational stack (BuildingLink, Yardi Maintenance, CondoControl, Building Engines, Facilio). Work-order history turns priors into posteriors.
- Hybrid physics-ML for envelope deterioration where domain physics outperforms pure black-box ML.

Output: P10 / P50 / P90 funding bands across a 30-year horizon, component-level sensitivity, regime-conditional scenarios. **Engine v0.5.1 already validated on Coopers Pointe (86-unit, 15-floor, 2007 BC concrete high-rise): per-unit Year-30 P50 of ~$212K, inside the empirical band of $150K–$300K for the class.** [`engine/v0_calibration/v0_5_update.md` §v0.5.1]

Software-led delivery (~70%), services (~30%). The licensed reserve analyst stays human — E&O sign-off, statutory seal. Everything else is the engine. No hardware in 24 months.

### USP

The differentiator is **calibrated uncertainty inside a regulator-aligned product surface**, not model complexity. Concretely:

1. **We ship the posterior, not the point.** Incumbents (SmartProperty *Living Reserve Study*, PropFusion, Solume, ReserveWise) publish deterministic single-line forecasts. None publish calibrated uncertainty bands. "AI reserve study" claims in market today are OCR-plus-spreadsheet with a thin LLM wrapper. We ship the actual posterior.
2. **Jurisdiction-agnostic engine, jurisdiction-specific seal.** Methodology was built on BC concrete-highrise data and validates without rework in NS, ON, AB, FL. The seal is local-licensed (NS P.Eng. in Halifax; ON P.Eng. or RCM in GTA; FL P.E. in channel-partnered work). The engine doesn't know which province it's in; the deliverable does.
3. **The cadence is the moat.** Regulators wrote the recurring purchase into statute. Every customer is a 3–5-year re-engagement annuity, not a one-shot.
4. **Data flywheel.** Every study fielded adds rows to the structure-type cohort prior. Cohort priors are the asset an internal team at CINC or Yardi would take 18–24 months to replicate. By month 18, our priors are tighter than anything an incumbent could re-derive without us.

### ICP

Primary ICP, Year 1: **Atlantic Canada condominium corporations, 60–150 units, concrete or hybrid structure, building age 15+ years.** Statutorily required to produce a reserve fund study every 5 years (NS) or 3 years (ON for Y2 expansion). Buying committee is the board (5–9 directors). The decision-maker is the board chair or treasurer. Trigger event is the 5-year cycle anniversary or a recent special-assessment friction with owners.

Buyer pain in their words: "We just hit owners with a $14K-per-unit special assessment for the roof and the windows. We have no idea what's coming next, and we can't tell owners what's coming next." Probabilistic forecasts produce that answer in a defensible form.

Secondary ICP, Year 2: **Ontario GTA highrise (200–400 units), and FL beachfront 100+ units via management-company channel partnership.**

Buying influencers: property management company (for handoff of work-order data and operational records), corporation's lawyer (for status-certificate language), corporation's accountant (for adequacy opinion). We do not displace any of them — we feed them better numbers.

### GTM paths

Operative sequence is **Canada-first** per ADR-0004 (2026-05-10), reversing the original synthesis's FL-anchored plan. Rationale: (1) the Halifax warm-lead asymmetry — a family-mediated, statutorily-mandated, willing-to-share-data design partner — has no FL analogue and degrades over time; (2) FL HB 913 enforcement risk creates a worse first-customer environment than NS's stable Bill-38 regime; (3) Atlantic Canada referral velocity off a NS case study is plausibly faster than cold FL outbound.

| Stage | Window | Concrete shape | Gating asset |
|---|---|---|---|
| Halifax wedge | M1–6 | Warm-lead 100+ unit Halifax HOA, paid pilot at $0 (data + case study + 3 referrals in trade), NS-licensed P.Eng. seal, engine v0.5 → v1 calibration on Atlantic concrete-highrise data | LOI signed; NS P.Eng. named |
| Atlantic Canada referral | M6–12 | Word-of-mouth + small-conference channel. 5–10 NS / Atlantic Canada HOAs | First 3 referral conversions |
| Ontario expansion | M12–24 | ON-licensed RA or P.Eng. ACMO + CCI relationships. Cumulative 80–150 customers across Canada by EOY2 | ON RA hired or partnered |
| FL channel partnership | M12+ | Management-company channel deal (PropFusion's playbook). They provide FL compliance + book; we provide the engine. Revenue share | FL channel partner signed |
| CA / NY follow-on | Y3 | Davis-Stirling §5550 and NYC condo/co-op stock. Optional if exit conversations accelerate | Y2 revenue base hit |

The engine is jurisdiction-agnostic; the geography is sequenced; FL is a channel ramp, not a methodology rework.

### Exit thesis

**Target: $5M revenue Year 3, strategic acquihire at $15–25M (3–5× revenue) Q3–Q4 2029.** Per `gtm/exit-thesis-acquirer-mapping.md`:

- **Primary: CINC Systems** — Hg Capital + Spectrum Equity backed, largest pure-play CAM SaaS in North America, $7.8B in payments processed annually, PE-controlled with explicit M&A growth mandate, already partnered with SmartProperty, Cephai+ AI suite already shipping. The only buyer with capital + distribution + an announced AI thesis that maps cleanly onto a probabilistic engine.
- **Secondary: FirstService Residential (NASDAQ: FSV)** — $107M in 2025 acquisition spend; acquired Edmonton-based Core Real Estate Group May 2025 (250K+ Canadian units under management). Methodology + Atlantic Canada installed base slots into reserve-services line as Associa differentiator.
- **Tertiary: Yardi** — 23 acquisitions to date; new CEO Rob Teel taking over January 2026. CEO transition is the densest M&A signal in the set. Already ships a deterministic Reserve Studies module inside Voyager.

Deliberately excluded from primary outreach: SmartProperty (methodology overlap caps the multiple). Largest single risk to liquidity: CINC builds the module internally using SmartProperty data. Counter: keep cohort priors and the workflow integration in artifacts an internal team would take 18–24 months to replicate.

## 2. Per-slide outline

### Slide 1 — Cover / one-line thesis

**Purpose.** Set the room. Investor + chair both know within 10 seconds what this is.

**Key message.** A probabilistic reserve study, fielded software-first, sealed by a licensed P.Eng., wedge customer in Halifax — venturing as a regulator-mandated SaaS-plus-services play.

**Content.**
- Company name + tagline. Working: *Probabilistic reserve studies. Built on cohort data. Sealed by P.Eng.*
- One-sentence positioning: *We build the reserve fund study that tells boards the range, not just the line.*
- Footer: founder name, date, "Seed introduction — Halifax."

**Visual.** Single hero image: the P50/P90/P99 fan chart from `engine/v0_calibration/v0_5_update.md` v0.5.1, anonymized building label. Muted palette (navy / slate / one accent). No icons. No stock photography. No emoji.

**Citations.** `gtm/elevator-pitch.md` §1.

---

### Slide 2 — The structural problem

**Purpose.** Anchor the audience in the right problem. Board chair recognizes the lived experience; investor recognizes the category-level pattern.

**Key message.** Surprise capital calls are not a board failure. They are the mathematical consequence of forecasting single-line replacement schedules on components that follow distributions.

**Content.**
- "Most reserve fund studies project one number per component per year." (cite NS Reg. 60/71 s. 79(2): RUL + replacement cost as point estimates)
- "Roofs last 17 or 23 years, not 20. HVAC central plants fail in a 4-year window, not a date."
- "When reality misses the line, the gap shows up as a special assessment."
- "Champlain Towers South: $1B and 98 lives — the worst case of a category-wide structural problem."

**Visual.** Two overlaid charts side by side. Left: a typical deterministic single-line CAI-style replacement schedule. Right: the same components rendered as overlapping probability distributions. The point is visual — even the chair, who has never seen a Weibull, reads "single line vs. cloud" immediately.

**Citations.** `regulatory/ns-condominium-act-summary.md` §2 (statutory requirement language); `gtm/elevator-pitch.md` §1, §2.

---

### Slide 3 — Why now: three convergent forces

**Purpose.** Establish the market window is open, in force, and accelerating. Investor needs to see this is not speculative.

**Key message.** Regulatory mandate, aging stock, methodology gap — all three are in force today, none speculative.

**Content.** Three columns:

1. **Regulatory tailwind, already in force.** BC Strata Property Act depreciation reports (every 3 years). ON Condo Act §94 (every 3 years). AB CPA (every 5). QC Bill 16 *carnet d'entretien* (in force Aug 2025). NS Bill 38 (proclaimed May 2023, every 5 years for 10+ units, NS-licensed P.Eng. required). FL HB 913 SIRS (post-Surfside). CA Davis-Stirling §5550 + SB 326. NJ S2760. NYC LL11/FISP.
2. **Aging stock hitting the wall.** 100+ unit condo buildings built 1970s–1990s reaching simultaneous major-component replacement age. Surfside priced the consequence at $1B + 98 lives. Regulators structurally over-correcting.
3. **Methodology gap.** SmartProperty, PropFusion, Solume, ReserveWise — all deterministic. None publish calibrated uncertainty bands. Category-defining product hasn't been built.

**Visual.** Three vertical lanes, each with a single statistic in display type, supported by 2–3 short proof points. No bullet-soup; treat each column as a billboard.

**Citations.** `gtm/elevator-pitch.md` §2; `regulatory/ns-condominium-act-summary.md` §2.1–§2.3 for NS specifics.

---

### Slide 4 — The incumbent gap (competitive landscape)

**Purpose.** Show what's on the market and why it does not solve the problem.

**Key message.** Every incumbent ships a deterministic single-line forecast. Each is a candidate acquirer, not a competitor we have to displace — because boards still need a seal, and we keep the seal human.

**Content.** Comparison strip across four incumbents:

| Vendor | Methodology | Uncertainty bands | Work-order ingest | License/seal model |
|---|---|---|---|---|
| SmartProperty (*Living Reserve Study*) | Deterministic + cycle-update workflow | No | Limited (CAM-integrated) | RA per jurisdiction |
| PropFusion | Deterministic spreadsheet | No | No | FL P.E. partner network |
| Solume | Deterministic + light scenario | No | No | Channel-partnered |
| ReserveWise | Deterministic + actuarial | No | No | Internal RA |
| **Us** | **Probabilistic w/ cohort priors** | **P10/P50/P90 fan** | **Yes — CMMS-conditioned** | **Licensed P.Eng. seal** |

**Visual.** Five-row comparison matrix, last row visually distinguished (accent color in the "Probabilistic" cell). Avoid logos at this stage — keep the visual analytical.

**Citations.** `vendors/` folder profiles; `gtm/elevator-pitch.md` §2.3; synthesis §2 vendor landscape.

---

### Slide 5 — The methodology: one picture, six components

**Purpose.** Show the engine in a single frame without becoming a methods seminar.

**Key message.** Six probabilistic components carry the variance. Long tail is deterministic and CAI-compliant. The output is a fan, not a line.

**Content.**
- The six load-bearing components named, with one-line per-component note.
- Methodology stack in five short bullets: Markov / Weibull survival; Bayesian hierarchical cohort priors; Monte Carlo with copulas (correlated failures); regime-switching cost-escalation; CMMS work-order covariates.
- Output specification: P10 / P50 / P90 funding bands across 30 years, component-level sensitivity, regime-conditional scenarios.

**Visual.** Center: the P50/P90/P99 fan from Coopers Pointe v0.5.1, anonymized. Annotated with the per-unit Year-30 P50 callout (~$212K, inside the BC empirical band $150K–$300K). Left margin: the six component icons in a vertical stack. Right margin: a small inset showing the deterministic CAI long-tail line, labeled "Components 7+ (long-tail) — CAI-compliant deterministic."

**Citations.** `engine/v0_calibration/v0_5_update.md` §v0.5.1 (validated numbers); `gtm/elevator-pitch.md` §3.

---

### Slide 6 — Validation already in hand

**Purpose.** Establish that this is not a deck about an idea. The engine ran, magnitudes pencil, the scripts are reproducible.

**Key message.** v0.5.1 calibrated on a real BC concrete high-rise. Magnitudes inside the empirical band. Two mechanical calibration bugs found and fixed. Path to v1 is incremental.

**Content.**
- Building studied: 86-unit, 15-floor, 2007 BC concrete high-rise (Coopers Pointe, `bcs2646`).
- Dataset: 519 structured component rows from BC + ON reserve study corpus.
- Headline result: 30-year cumulative P50 fund need $18.3M; per-unit Year-30 P50 ~$212K.
- BC concrete-highrise empirical band per Brief-0001 corpus survey: $150K–$300K/unit at Year 30.
- P99/P50 ratio at Year 30: 2.93 — tail-heavy in the realistic way.
- Verdict per validation report: **PROCEED-WITH-MODIFICATION**, with the modification scope collapsed to cohort-by-structure-type (v1) and operational covariate corpus (Brief-0003 in flight).

**Visual.** A small table with the v0 → v0.5 → v0.5.1 result deltas (P50 Year 30: $17.2M → $18.3M, ±2%). Below, a single line: *Coopers Pointe, 86 units, 2007 — inside the empirical band of comparable BC reserve studies.*

**Citations.** `engine/v0_calibration/v0_5_update.md` (entire); `data/structured/components.csv` (519 rows).

---

### Slide 7 — USP, distilled

**Purpose.** Compress the four sources of differentiation onto a single slide that a board chair can repeat to the rest of the board verbatim, and an investor can repeat to a partner.

**Key message.** Posterior, not point. Local seal, agnostic engine. Cadence is the moat. Data flywheel is the asset.

**Content.** Four numbered statements, each one line:

1. **We ship the posterior, not the point.** Calibrated uncertainty bands, not a single line.
2. **Jurisdiction-agnostic engine, locally-sealed deliverable.** One engine, NS P.Eng. / ON P.Eng. / FL P.E. seals depending on the building.
3. **The cadence is the moat.** Regulators wrote the recurring purchase into statute. Every customer is a 3–5-year re-engagement.
4. **Data flywheel.** Every fielded study tightens the next one's priors. Cohort priors take 18–24 months to replicate without us.

**Visual.** Four equal-weight cards, monospace or display type, no decoration. The slide should feel like a billboard.

**Citations.** `gtm/elevator-pitch.md` §3; `gtm/exit-thesis-acquirer-mapping.md` (data-flywheel-as-moat argument).

---

### Slide 8 — ICP and buying context

**Purpose.** Show that the wedge customer is statutorily required to buy, has a named decision-maker, and the audience IS that named decision-maker.

**Key message.** Atlantic Canada condominium corporations, 60–150 units, building age 15+, on the 5-year statutory cycle. The board chair signs.

**Content.**
- Primary ICP (Y1): NS / Atlantic Canada concrete or hybrid-frame condo corporations, 60–150 units, age 15+.
- Decision-maker: board chair or treasurer.
- Trigger event: 5-year reserve-fund-study cycle anniversary, recent special-assessment friction with owners, or recent insurance non-renewal.
- Buying committee: 5–9 board directors.
- Buying influencers we feed (not displace): property management company, corporation's lawyer, corporation's accountant.
- Secondary ICP (Y2): ON GTA highrise 200–400 units; FL beachfront 100+ via management-company channel.

**Visual.** A simple decision-tree from "5-year cycle anniversary" to "board RFP" to "vendor selection" to "study fielded." Annotate each step with where we engage. The audience should see themselves on this diagram.

**Citations.** `regulatory/ns-condominium-act-summary.md` §2.1, §2.2; Brief-0004 customer-archetype work.

---

### Slide 9 — GTM sequence: Canada-first, then channel-partnered FL

**Purpose.** Show the path from Halifax to $5M. Demonstrate the sequencing is deliberate and the geography is solved.

**Key message.** Halifax wedge → Atlantic Canada referral → Ontario expansion → FL channel-partnered Y2. Engine jurisdiction-agnostic from day one.

**Content.** A horizontal stage-gate diagram with five stages:

| Stage | Window | Volume target | Gating asset |
|---|---|---|---|
| Halifax wedge | M1–6 | 1 design partner (data + case study + 3 referrals) | LOI signed + NS P.Eng. named |
| Atlantic Canada referral | M6–12 | 5–10 paying customers | First 3 referral conversions |
| Ontario expansion | M12–24 | 80–150 cumulative customers | ON P.Eng. or RCM hired / partnered |
| FL channel partnership | M12+ | 2 channels signed by EOY2; 4–5 by EOY3 | First channel deal signed |
| CA / NY follow-on | Y3 | Optional ramp | Y2 revenue base hit |

**Visual.** A horizontal Gantt-style band, color-graded from Canada-blue to FL-coral. Overlay quarterly customer count target as a thin upper trace.

**Citations.** `decisions/0004-sequence-reorder-canada-first-gtm.md`; `synthesis/addendum-sequence-reorder-2026-05-10.md`; `gtm/canada-first-revenue-model.md` §3.

---

### Slide 10 — The Halifax engagement, named honestly

**Purpose.** Address the conflict-of-interest scent directly. The chair-to-be will see this slide as the test of whether we are straight with them.

**Key message.** Halifax is our wedge customer AND your building. The terms are public: free study, free 12-month subscription, exchange of data rights + case-study consent + 3 referrals. NS-licensed P.Eng. seal. The board sees the LOI before anything else moves.

**Content.**
- Engagement shape: 12-week paid pilot at $0 cash.
- What the corporation gets: probabilistic forecast (P50/P90/P99 over 30 years), remediation plan with cost ranges, scenario tool, benchmarking against 9 comparable buildings, three years of free annual updates, sealed by an NS-licensed P.Eng. independent of the corporation and declarant per N.S. Reg. 60/71 s. 77(5).
- What we get: data-sharing rights per LOI, case-study consent at engagement end, 3 named referrals to Atlantic Canada HOAs.
- Hard data line: we will not collect, retain, or process owner contact lists, owner financial information, owner-by-owner disputes, or tenant data. PIPEDA-aligned by design.
- Termination: either party, 30 days, on any material delivery. Corporation keeps all reports delivered to date. We keep deidentified building-and-component rows already absorbed.

**Visual.** One column: "What the corporation gets." Second column: "What we get." Third column, set apart: "What we will not take." The third column is the trust slide. Treat it as such — slightly elevated weight, no decoration.

**Citations.** `gtm/halifax/02-loi-template.md`; `gtm/halifax/04-board-pitch-deck-outline.md` slides 3–4; `regulatory/ns-condominium-act-summary.md` §2.2 (independence), §2.3 (owner-access right), §3 (PIPEDA).

---

### Slide 11 — Revenue model: $5M Y3, honest sensitivity

**Purpose.** Show the revenue math with the honest sensitivity band. Investor needs the range; chair needs to see we are not overpromising.

**Key message.** BASE case lands $4.21M Y3. STRETCH (co-founder by M3 + FL channel by M9) lands $5.85M. The advertised $5M ± 20% band closes between them. Canada-only ceiling is ~$2.6M — FL channel is half the Y3 number.

**Content.** Two stacked tables.

Y3 standalone revenue under three cases:

| Case | Y3 revenue | Recurring mix | Defensible multiple |
|---|---|---|---|
| BASE | $4.21M | 16.5% | 3.0–3.5× |
| BASE + subscription acceleration | $4.21M | 26% | 3.5–4.0× |
| STRETCH + subscription acceleration | $5.85M | 30.8% | 3.5–4.5× |

Pricing:

| Tier | Building size | Canada price | FL list price (channel-shared) |
|---|---|---|---|
| Small | 20–60 units | C$8,000 | US$9,000 |
| Mid | 60–150 units | C$13,000 | US$15,000 |
| Large | 150–400+ units | C$22,000 | US$24,000 |
| Subscription | All | C$299/mo | US$299/mo (25–30% channel share) |

**Visual.** A horizontal "fan" of Y3 revenue scenarios (P10/P50/P90 styled to match Slide 5's chart language — the visual echo is intentional: we forecast our own revenue the way we forecast a roof). Annotate the $5M target line.

**Citations.** `gtm/canada-first-revenue-model.md` §2 (pricing), §3 (ramp), §4 (ARR mix), §6 (sensitivity).

---

### Slide 12 — Exit thesis and acquirer landscape

**Purpose.** Investor reads this slide hardest. Chair reads it to understand we have an opt-out path that doesn't require them to be on the hook past Year 3.

**Key message.** $15–25M strategic acquihire in 2029, central case $20M (4× on $5M Y3). Primary acquirer CINC Systems; secondary FirstService Residential and Yardi. SmartProperty excluded by design.

**Content.**
- Target: 3–5× revenue, $15–25M, Q3–Q4 2029.
- Primary acquirer: **CINC Systems** — Hg + Spectrum Equity backed, $7.8B in payments processed annually, PE-controlled with explicit M&A mandate, already partnered with SmartProperty, Cephai+ AI suite shipping. Buying signal: Cephai+ names predictive reserve forecasting in a roadmap update.
- Secondary: **FirstService Residential** (NASDAQ: FSV) — $107M 2025 acquisition spend, acquired Core Real Estate Group (Edmonton) May 2025, 250K+ Canadian units under management.
- Tertiary: **Yardi** — 23 acquisitions, new CEO Rob Teel January 2026, already ships deterministic Reserve Studies module.
- Excluded from primary outreach: SmartProperty (overlap caps the multiple).
- Largest single risk to liquidity thesis: CINC builds internally with SmartProperty data. Counter: cohort priors are the artifact that take 18–24 months to replicate.

**Visual.** Three logo cards (CINC, FirstService Residential, Yardi) with one-line rationale under each. Below: a small "buying signal" callout per acquirer. Set SmartProperty aside in a smaller, greyed card labeled *deliberately excluded — methodology overlap.*

**Citations.** `gtm/exit-thesis-acquirer-mapping.md` (entire); `gtm/canada-first-revenue-model.md` §8.

---

### Slide 13 — Capital ask + use of funds

**Purpose.** Make the ask explicit and the dilution-to-value mapping defensible.

**Key message.** $250K pre-seed at $4M post-money. 6.25% dilution. Buys the co-founder + working-capital cushion that moves BASE from $3.45M Y3 to $4.21M Y3.

**Content.**
- Bootstrap floor under Canada-first sequence: $150–175K (revised up from synthesis's $100K because Halifax is unpaid).
- Recommended pre-seed: **$250K at $4M post-money (6.25% dilution).**
- Use of funds: co-founder runway (M6–M12 salary buffer); legal cross-border (Canadian operating co + US holdco for FL revenue routing per ADR-0003); 1099 NS P.Eng. + 1099 reserve analyst for Halifax + first 8 paying customers; lean SW stack ($17K); E&O + GL insurance ($13K); marketing + travel for Atlantic Canada conference circuit.
- Why not more: $500K → $1M rounds give marginal Y3 revenue gain ($0.45M, $0.6M) at materially worse dilution-to-return (12.5%, 25%). Founder-return math at $20M exit prefers the $250K path.
- Why not less: the pure-bootstrap path requires $150K personal capital from the founder and pushes the co-founder to month 9 with equity-only comp. Reduces Y3 revenue to ~$3.45M.

**Visual.** A small dilution-vs-Y3-revenue scatter (four points: $0, $250K, $500K, $1M). The $250K point should sit on the efficient frontier.

**Citations.** `gtm/canada-first-revenue-model.md` §7.1–§7.3, §8.3 (founder-return math); `decisions/0001-bootstrap-vs-funded-open.md`.

---

### Slide 14 — Team, risks, and load-bearing assumptions

**Purpose.** Show we know what can break the plan. Investor reads this slide for honesty; chair reads it to understand operational risk for the Halifax engagement.

**Key message.** Three load-bearing assumptions per ADR-0004. Each has a named mitigation and a recovery move. If any breaks materially, the timeline slips to Year 4 and the exit thesis erodes.

**Content.** Three risks in priority order:

1. **Co-founder or sales partner within 6 months.** Founder time is the binding constraint. Three concurrent searches in flight (technical / sales / commercial-counterpart). Recovery: if M6 pipeline is dry, raise $500K instead of $250K and fund a senior hire (VP Sales at $180K + 8% equity, or VP Engineering at $200K + 8%).
2. **80–150 customers across NS → Atlantic Canada → Ontario by end of Y2.** Halifax wedge alone is not revenue. Recovery: ON 1099 commission-only sales rep working off the CAO 2024 dataset as a prospect list.
3. **FL channel partnership signed by month 12.** Without it, Y3 revenue caps at ~$2.6M. Recovery: direct-FL-sales motion via 1099 FL rep funded by agentic-dividend; volume lower but recoverable to $3.4–3.6M Y3.

Also flag:

- NS-licensed P.Eng. for Halifax engagement is critical-path. LOI cannot be finalized without the P.Eng. named. (Brief-0004a longlist in flight.)
- Methodology IP not patentable in the conventional sense — Markov/Weibull/Bayesian/Monte Carlo are decades-old DOT bridge work. The moat is the system + data flywheel + regulator-aligned product surface, not core math.
- We are not promising hardware (sensors are a Year-3 upsell, not an R&D line) and we are not promising an IPO (the exit is an acquihire, the synthesis's funding-to-crossover IPO thesis is superseded by ADR-0004).

**Visual.** Three "risk cards" stacked, each with risk / mitigation / recovery. Below, a "what we are NOT promising" line in a single sentence, italicized, in a muted color.

**Citations.** `decisions/0004-sequence-reorder-canada-first-gtm.md`; `gtm/canada-first-revenue-model.md` §9 (what breaks the model); `gtm/elevator-pitch.md` §7.

---

### Slide 15 — Close: what we want from this conversation

**Purpose.** Dual ask, named explicitly so neither hat is left implicit.

**Key message.** Two asks, one room.

**Content.**

**From the investor seat:**
- Indicative interest at the $250K pre-seed at $4M post-money structure within 30 days.
- One advisor-tier introduction to a Canadian condo-management firm in NS or ON (FirstService Residential ATL Canada, Crossbridge, Bentall GreenOak property management) if relationships exist.

**From the board chair seat:**
- Discovery call with the full Halifax board within 30 days, per Brief-0004 Phase 2.
- If discovery is positive, board vote on the LOI within 45 days, per Brief-0004 Phase 3.
- Three-year free annual re-runs of the forecast as actuals come in, plus optional scenario-tool usage. The relationship ends when the corporation says it ends.

Close line: *We will not embarrass you in either seat. The data line stays where it is. The seal stays human.*

**Visual.** Two columns, equal weight, "Investor" and "Board chair." Quiet. No call-to-action button styling.

**Citations.** `gtm/halifax/04-board-pitch-deck-outline.md` slide 5; `research/briefs/0004-halifax-design-partner-engagement.md` Phase 2–3.

---

### Appendix slide (16, hidden by default)

**Purpose.** Single-slide index of supporting artifacts the audience can request post-meeting.

**Content.**
- Engine validation report: `engine/v0_calibration/v0_5_update.md`
- Canada-first revenue model with sensitivity: `gtm/canada-first-revenue-model.md`
- Exit thesis / acquirer mapping: `gtm/exit-thesis-acquirer-mapping.md`
- NS Condominium Act regulatory summary: `regulatory/ns-condominium-act-summary.md`
- ADR-0004 (Canada-first sequence reorder): `decisions/0004-sequence-reorder-canada-first-gtm.md`
- Halifax engagement brief, LOI template, board pitch deck outline: `gtm/halifax/` (Brief-0004 series)

**Visual.** A plain list, no decoration. This slide is for the post-meeting follow-up email's "as discussed" line.

## 3. Design direction for Claude Design

### Voice and register

The deck is read by a numerate, skeptical audience with both money and fiduciary duty on the line. Default register: declarative, specific, evergreen. No claims of "AI-first" or "AI-native" on a slide — those terms appear nowhere in the visible slide copy, even though they are accurate descriptors of the engineering organization (`gtm/elevator-pitch.md` uses them; the deck should not). They invite the investor to assume vaporware and invite the chair to assume hype.

Avoid on slides: *Monte Carlo*, *stochastic*, *Bayesian* — name the math in speaker notes if asked, not on the visible slide. (Slide 5 names the methodology stack as five short bullets in deliberately plain language; the chart does the heavy lifting.)

Use on slides: *probabilistic*, *posterior*, *uncertainty bands*, *cohort priors*, *seal*, *cadence*, *flywheel*. These are precise without being jargon-coded.

### Palette

Navy (#1a2438 or close) + slate (#4a5568) + one accent (suggest a muted teal #2c7a7b for the probabilistic-band callouts; absolutely NOT red — red on a reserve-fund chart reads as alarm). Background white or near-white. No gradients. No drop shadows. No glassmorphism.

### Typography

One serif for display headlines, one sans for body. Display: Tiempos / Source Serif / Georgia. Body: Inter / Helvetica Neue / IBM Plex Sans. Numerals in tabular figures throughout (the financial tables MUST align decimals).

### Chart standards

- The P50/P90/P99 fan chart is the visual spine. It appears on slides 1, 5, 11 (revenue version), 13 (dilution-vs-Y3 scatter shares the visual language). Consistency across these four panels is the deck's strongest design choice.
- Axis labels in plain English, not "P50" alone — "Median (P50)" or "90th percentile (P90)" the first time each appears.
- All currency clearly labeled CAD vs. USD. Year-30 numbers in millions; per-unit in thousands.
- One data origin per chart, named in a footnote in 8-pt type.

### What to avoid

- No stock photography of buildings, suits, handshakes, lightbulbs, gears, brain icons, or rocket imagery.
- No "vision / mission" slide. The deck's thesis is on slide 1; we do not have a vision slide.
- No team slide before the close. (Single-founder pre-co-founder; a "team" slide is structurally weaker than naming the load-bearing assumption directly on slide 14.)
- No bullet points longer than 12 words. If a bullet runs longer, it becomes a sentence in the speaker notes.
- No company logos on slide 4 (incumbent comparison). Logos signal a fight we're not picking.

### Source files Claude Design should read before building

In order of priority:

1. This brief.
2. `engine/v0_calibration/v0_5_update.md` — for the v0.5.1 numbers and the chart shape.
3. `gtm/canada-first-revenue-model.md` — for revenue and exit math.
4. `gtm/halifax/04-board-pitch-deck-outline.md` — for what the chair-side of the audience has already been told about the engagement structure (consistency check).
5. `regulatory/ns-condominium-act-summary.md` §1, §2 — for the regulatory language to match verbatim on slide 3 and slide 10.

### Production notes

- Slide count target: 15 + 1 appendix. If the deck runs to 17, cut slide 7 (USP) — its content can be folded into slide 5's caption and slide 12's lead-in. Do not cut slide 10 (Halifax engagement, named honestly) — that slide is the trust hinge.
- Speaker notes: ≤ 60 words per slide. The deck is the live conversation; the brief above is the long version.
- File format: `.pptx` for handoff (founder will adapt locally), with a parallel `.pdf` for the post-meeting follow-up. No Keynote.
