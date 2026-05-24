---
id: note-2026-05-11-elevator-pitch
type: note
title: Elevator Pitch — Condo Capital Infrastructure
url: ''
authors:
- Condo Capital Infrastructure project
ingested_at: '2026-05-11T21:45:11Z'
content_hash: sha256:c7015eddb3369a57449e0b6977e0a6c2a4b734b7cad569bb7826b8bd57dc7229
source_path: gtm/elevator-pitch.md
domains:
- condo-capital-infra
filter:
  score: 0.15
  policy_version: condo-capital-infra-v1
  rationale: Internal GTM elevator pitch / investor narrative for the Condo Capital
    Infrastructure project itself — it summarizes the project's own thesis, methodology,
    and exit plan rather than providing primary statutory text, peer-reviewed methods
    research, vendor competitive intel with verifiable detail, or component-level
    deterioration data. It's a project artifact, not a knowledge-base source, and
    falls under the exclusion criterion for marketing/thought-leadership material
    lacking independent methodology disclosure or verifiable case data.
  decided_at: '2026-05-11T21:45:32Z'
  user_correction:
    decided_at: '2026-05-11T21:46:04Z'
    score: 1.0
    rationale: Project-internal canonical pitch document for Condo Capital Infrastructure.
      Synthesizes ADR-0004 sequence reorder + acquirer mapping + engine v0.5 validation
      + Brief-0004 Halifax wedge into a single 60-second-to-7-section narrative used
      for investor + acquirer + co-founder conversations. Filed for citation grounding
      from future project artifacts (deck variants, prospect-call notes, board memos).
nlm_corpus_ids:
- effe1f58-e6ce-4ff0-8728-35c885bff6f4
---

---
id: GTM-PITCH-001
date: 2026-05-11
status: v1-draft
governing_adr: decisions/0004-sequence-reorder-canada-first-gtm.md
related:
  - gtm/canada-first-revenue-model.md
  - gtm/exit-thesis-acquirer-mapping.md
  - synthesis/addendum-sequence-reorder-2026-05-10.md
---

# Elevator Pitch — Condo Capital Infrastructure

## 0. Spoken version (90 seconds, board / partner conversation)

North American condo boards pay $8K to $30K every three to five years for a binder that says "your roof will fail in year 12 and cost $400K." But the real answer isn't a single number — it's a probability distribution. Year 8 if the next two winters are bad. Year 17 if the elevator overhaul that's already overdue gets done first. Boards need that distribution to defend special assessments to owners, lenders, and insurers. Surfside was the consequence of getting that math wrong — $1B and 98 deaths. Every regulator from Florida to British Columbia is now structurally over-correcting.

We're an AI-native reserve study firm with a proprietary probabilistic engine across the six load-bearing components — roof, envelope, plumbing risers, HVAC, elevators, parking deck. 70% software, 30% services. The licensed reserve analyst stays human for E&O sign-off; everything else is the engine. We ship calibrated uncertainty bands across a 30-year horizon. No incumbent does — SmartProperty and PropFusion ship deterministic spreadsheets with an LLM wrapper. We ship the actual posterior.

Our first design partner is a 100+ unit Halifax condo whose board is in hand through a warm lead. Engine v0.5 is already validated on BC concrete-highrise data. From Halifax we go Atlantic Canada to Ontario by referral, then Florida through a management-company channel partner in year two. $5M revenue in three years. Strategic acquihire at $15 to $25M — CINC Systems, FirstService Residential, or Yardi.

---

## 1. The 60-second pitch

North American condo boards spend $8K–$30K every 3–5 years to receive a deterministic spreadsheet that says, in effect, "your roof will fail in year 12 and cost $400K." The actual answer is a probability distribution: P10 year 8 at $320K, P50 year 12 at $400K, P90 year 17 at $560K, with explicit dependence on the next three winters and the elevator overhaul that's already overdue. Boards need that distribution to defend special-assessment decisions to owners, lenders, and insurers. No incumbent ships it.

We are an **AI-native, agentic-first, tech-enabled reserve study firm** with a proprietary probabilistic engine over the six load-bearing components — roof, building envelope, plumbing risers, HVAC central plant, elevators, parking deck. 70% software, 30% services. The licensed reserve analyst stays human (E&O sign-off); everything else is the engine.

Canada-first GTM via a warm-lead Halifax design partner (already in hand), then Atlantic Canada → Ontario referral, then a US FL channel-partner ramp in Year 2. **Target: $5M revenue in 3 years, strategic acquihire at $15–25M** to a CMMS or community-management consolidator (CINC Systems is the primary acquirer; FirstService Residential and Yardi secondary).

## 2. Market thesis

Three convergent forces, none speculative:

1. **Regulatory tailwind, already in force.** BC Strata Property Act depreciation reports (every 3 years), ON Condo Act §94 (every 3 years), AB Condominium Property Act (every 5 years), Quebec Bill 16 *carnet d'entretien* (in force August 2025), FL HB 913 SIRS (post-Surfside, 2025), CA Davis-Stirling §5550 + SB 326 balcony, NJ S2760, NYC LL11/FISP. Each jurisdiction mandates a structured forecast that aging stock can't manually scale to deliver.

2. **Aging stock hitting the wall.** 100+ unit condo buildings built 1970s–1990s are reaching simultaneous major-component replacement age. Surfside priced the consequence of underfunded reserves at $1B and 98 deaths. Every regulator in scope is now structurally over-correcting.

3. **Methodology gap.** Incumbents (SmartProperty's *Living Reserve Study*, PropFusion, Solume, ReserveWise) ship deterministic single-point forecasts. None publish calibrated uncertainty bands. The category-defining product hasn't been built. Brief-0003 confirmed: outside reserve studies, the *operational PM layer* between cycles is also undocumented as a single primary source — boards have no public best-practice playbook anywhere in North America.

The TAM is not "the reserve-study market." It's "the structured-capital-planning compliance market" — boards forced into a recurring purchase, software-replaceable services, regulator-defined cadence. Penetration of probabilistic methodology is effectively zero today.

## 3. Technology thesis

The engine is six probabilistic components plus a deterministic long-tail (CAI-compliant):

- **Markov chain deterioration** + **Weibull / lognormal survival** for component failure timing.
- **Bayesian hierarchical priors** keyed to structure-type cohorts (concrete high-rise, wood-frame mid-rise, podium hybrid) — every fielded study tightens the next one. The data flywheel is the moat.
- **Monte Carlo aggregation with copulas** for correlated failures (roof + envelope share weather covariates; HVAC + elevator share electrical-system covariates).
- **Regime-switching cost-escalation** for capex — not a flat 3% inflator. Construction inflation, labor-supply regimes, materials-supply regimes are modeled explicitly.
- **CMMS work-order covariates** ingested from the property's existing operational stack (BuildingLink, Yardi Maintenance, CondoControl, Building Engines, Facilio) — what Brief-0003 confirmed as the operational layer between reserve cycles. Work-order history turns priors into posteriors.
- **Hybrid physics-ML** for envelope deterioration where domain physics adds informativeness over pure black-box ML.

What the engine outputs: P10 / P50 / P90 funding bands across a 30-year horizon, component-level sensitivity, regime-conditional scenarios. Validation in hand: engine v0.5 calibrated on Coopers Pointe (BC concrete high-rise) lands per-unit Year-30 P50 at ~$212K, inside the empirical band of $150K–$300K/unit for the class.

The differentiator is **calibrated uncertainty**, not model complexity. Vendors who claim "AI reserve study" today are OCR-and-spreadsheet plus a thin LLM wrapper. We ship the actual posterior. Software-led delivery (70%) means a study fielded in days, not weeks. Services (30%) is the licensed RA's sign-off — required by E&O insurance, kept human by design. **No hardware in 24 months.** Sensors are a Year-3 upsell, not an R&D line.

## 4. GTM paths

Per ADR-0004 (Canada-first sequence reorder, 2026-05-10):

| Stage | Window | Concrete shape | Gating asset |
|---|---|---|---|
| **Halifax wedge** | Months 1–6 | Warm-lead 100+ unit Halifax HOA (father → board). Paid pilot. NS-licensed RA. Engine v0.5 → v1 calibration on Atlantic concrete-highrise data. | Halifax engagement signed; co-founder or sales partner identified. |
| **Atlantic Canada referral** | Months 6–12 | Word-of-mouth + small-conference channel. 5–10 NS / Atlantic Canada HOAs. | First 3 referral conversions. |
| **Ontario expansion** | Months 12–24 | ON-licensed RA. ACMO + CCI relationships. Condo Act §94 every 3 years = re-engagement annuity. Cumulative 80–150 customers. | ON RA hired or partnered. |
| **FL channel partnership** | Month 12+ | Management-company channel deal (PropFusion's playbook). They provide FL compliance sign-off and book of business; we provide the engine. Revenue share. Reactivates the original synthesis's FL anchor. | FL channel partner signed. |
| **CA / NY follow-on** | Y3 | Davis-Stirling §5550 and NYC condo + co-op stock. Lower priority unless exit conversations accelerate. | Y2 revenue base hit. |

The geography is sequenced; the **engine is jurisdiction-agnostic from day one** (v0.5 validation already on Canadian data). FL is a channel ramp, not a methodology rework.

## 5. Probable operational paths

**Bootstrap-leaning (default).** ADR-0001 reopened under the $5M / 3yr / 3–5× framing. Revenue-funded growth: founder + one co-founder/sales partner + 1–2 1099 licensed RAs + 1 engineer. Capital injection only if a strategic distribution opportunity demands speed (e.g., FL channel-partner wants exclusivity, or a competitor announces Canadian expansion).

**Funded variant (held).** $8–10M to crossover under the original synthesis framing was reopened — under the new framing, likely $1–2M seed at most, not a multi-million round. Most plausible at month 12–18 if the Halifax wedge proves but referral conversion stalls.

**Entity structure (ADR-0003, held).** Canadian operating company (NS or ON registered) + US holdco for FL revenue routing. NOT Delaware LLC as the synthesis originally assumed. Cross-border tax review pending before incorporation.

**Three load-bearing assumptions (per ADR-0004). If any breaks, timeline slips to Y4 and the exit thesis erodes:**

1. Co-founder or sales partner within 6 months. Founder time is the binding constraint.
2. 80–150 customers across NS → AtCa → ON by end of Y2. Halifax wedge alone is not revenue.
3. FL channel partnership signed by month 12. Direct FL sales from Halifax is too slow.

## 6. Probable liquidity paths

**Primary: strategic acquihire at $15–25M (3–5× $5M Y3 revenue) Q3–Q4 2029.** Per `gtm/exit-thesis-acquirer-mapping.md`:

1. **CINC Systems (Hg Capital + Spectrum Equity backed).** Largest pure-play association-management SaaS in North America, $7.8B in payments processed annually, PE-controlled with explicit M&A growth mandate, already partnered with SmartProperty. The only buyer with capital + distribution + announced AI thesis (Cephai+) that maps cleanly onto a probabilistic engine. Engage when Cephai+ names predictive reserve forecasting in a roadmap update.
2. **FirstService Residential (NASDAQ: FSV).** $107M in 2025 acquisition spend; acquired Edmonton-based Core Real Estate Group in May 2025 (now 250K+ Canadian units under management). Largest Canadian operator in target market. Methodology + installed base slots into reserve-services line as Associa differentiator. Buying signal: "data-driven capital planning" or "predictive maintenance" in earnings or press.
3. **Yardi.** 23 acquisitions to date; new CEO Rob Teel taking over January 2026. Founder-transition + CEO-change is the densest M&A signal in the set. Yardi already ships a deterministic Reserve Studies module inside Voyager — a "Yardi Capital Forecast AI" launch built on our engine is a low-risk first acquisition for Teel.

Deliberately deprioritized: SmartProperty (direct competitive overlap, boxed into CINC channel — would view us as depressed-multiple feature acquisition); PropFusion (FL-native, smaller, weaker pricing power); MaintainX (industrial CMMS thesis, residential outside ICP).

**Secondary: PE roll-up.** Community-association management roll-ups (FirstService, Associa) acquiring tech enablement. Lower multiple but liquid exit.

**Largest single risk to the liquidity thesis:** CINC builds a reserve-modelling module internally with SmartProperty data + their own engineering and never needs to buy. Counter: keep the data flywheel and cohort priors in artifacts that an internal team would take 18–24 months to replicate.

## 7. What this pitch is not promising

- **Not promising hardware.** Sensors are a Year-3 upsell, not an R&D line, not in the pitch.
- **Not promising an IPO.** The exit is an acquihire; the synthesis's funding-to-crossover IPO thesis is explicitly superseded by ADR-0004.
- **Not promising methodology novelty in core math.** Markov, Weibull, Bayesian hierarchical, Monte Carlo with copulas are decades-old DOT bridge / pavement work transferred to condos. The novelty is the **system** — integrated engine + licensed-RA workflow + data flywheel + regulator-aligned product surface. That's the moat, and it's defensible because the regulators write the cadence into law.
