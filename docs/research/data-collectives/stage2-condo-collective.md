# Stage 2 — Condo Reserve-Study Data Collective: Feasibility & Design Position

> Stage 2 of the data-collectives project. Applies the foundation verdict
> (`synthesis-policy-market.md`) to the condo market, reusing the
> `condo-capital-infra` domain's established facts. Synthesis/design only — no
> new research. Date: 2026-06-11. Every claim traces to the foundation
> (`data-collectives`) or to `condo-capital-infra`.

## Verdict (one paragraph)

**Qualified GO — and the condo market is the strongest application of the
foundation's pattern that the project has surfaced, because the reserve-study
engine is *data-bound* in a way the general case is not.** The engine's
differentiation is a function of how many buildings' component-failure
observations it has calibrated on: a single engineering firm sees a few hundred
buildings, a pool sees thousands [[concepts/six-probabilistic-components]]
[[concepts/ml-fault-detection-mechanical-systems]]. That converts the
foundation's abstract instruction — *pool the non-rivalrous signal, not the
competitive one* — into a concrete, self-reinforcing input: component
degradation rates (how fast a low-slope roof membrane fails) are exactly
non-rivalrous, while client relationships, bids, and fee schedules are the
competitive layer firms keep. The fit on every foundation success condition is
strong. The GO is qualified by three load-bearing assumptions (below) and is
explicitly **not** a bet on agentic demand — the P&L must close on reserve-study
value that boards, insurers, and lenders pay for today.

---

## (a) Fit test against the foundation's success conditions

| Foundation condition | Condo verdict | Basis |
|---|---|---|
| **Non-rivalrous signal exists** | **Strong yes.** Component condition/failure data (RUL distributions per component class) is non-rivalrous — firms do not compete on how fast a roof degrades. | Foundation's load-bearing design rule (fraud-utility pattern) [[data-collectives/stream-7-industrial]] [[data-collectives/stream-1-economics-incentive]]; condo signal shape [[concepts/six-probabilistic-components]] [[concepts/weibull-component-failure-distribution]] |
| **Holder-directed on-ramp** | **Strong yes.** Condo corporations own their reserve studies + building/maintenance data and can direct it in. In NS the Registrar dataset and board comments are already quasi-public-record — unusually low-friction. | Data-mobility right [[data-collectives/stream-4-regulatory]]; NS public-record studies [[entities/ns-active-condo-corporations-dataset]] [[sources/pdf-da86bd51429b]] |
| **Pooled data is complementary, not substitutable** | **Yes, conditionally.** The condition signal is a near-pure public good (pooling improves everyone's priors). The competitive data (clients/bids/fees) must be excluded — this is the scope discipline, not a property of the market. | Substitutes problem [[data-collectives/stream-1-economics-incentive]]; six-component scope-lock [[concepts/six-probabilistic-components]] |
| **Governance scaffold available** | **Yes.** CAN/DGSI 100-7 fiduciary-cooperative standard; Canada-first aligns with condo's existing Halifax Year-1 GTM under ADR-0004. | CAN/DGSI 100-7 [[data-collectives/stream-5-governmental-policy]]; Canada-first GTM [[entities/summer-gardens-condo]] |

**Why condo beats the general case:** the foundation found that for most markets
the non-rivalrous signal is a *nice-to-have* whose pooling incentive is weak. In
condo the non-rivalrous signal is the *binding input to the product's accuracy
ceiling*. The Weibull priors and ML failure-refinement layer are explicitly
trained on "historical failure data from thousands of similar buildings"
[[concepts/ml-fault-detection-mechanical-systems]]; below that scale the priors
are wide and the methodology is not defensible against incumbents
[[concepts/six-probabilistic-components]]. So contribution is rational on
narrow self-interest, not altruism — the single hardest thing to manufacture in
a data collective [[data-collectives/stream-1-economics-incentive]].

**The honest ceiling.** The foundation is firm that raw data scale is *not* a
durable moat — failure-rate calibration has diminishing returns once you have
enough buildings per component class to fit a stable Weibull
[[data-collectives/stream-7-industrial]] [[data-collectives/synthesis-policy-market]].
So data scale bootstraps the engine's quality to a threshold; past that, the moat
reverts to **network + neutral governance + workflow integration**, exactly as
the foundation prescribes. The data-network-effect is the on-ramp, not the
permanent defense.

---

## (b) Design

**What is pooled.** Only the six-component condition/failure signal: as-built
attributes, observed component ages, condition assessments, and — the highest-value
contribution — *post-replacement failure observations* (a component reached
end-of-life at year N under conditions X). Pooled to calibrate per-class RUL
distributions and the ML failure-refinement layer
[[concepts/weibull-component-failure-distribution]]
[[concepts/ml-fault-detection-mechanical-systems]]. **Hard-excluded** by charter:
client lists, bid prices, fee schedules, proposal pipelines — the competitive
layer. Crossing that boundary re-triggers the Vives substitutes problem and
destroys the non-rivalrous property [[data-collectives/stream-1-economics-incentive]].

**Entity form.** Fiduciary **data cooperative** governed per CAN/DGSI 100-7
[[data-collectives/stream-5-governmental-policy]] [[data-collectives/stream-3-legal]].
Members = contributing engineering firms; condo corporations are data-holders who
*direct* their data in under the data-mobility right rather than members of the
co-op. A **neutral administrator** operates the pooled calibration engine and
returns improved priors + benchmarking to members — it does not trade in the raw
contributions. This neutral-administration design is also the antitrust-safe
design: it is the fraud-utility structure (Early Warning Services / Cifas)
transposed [[data-collectives/stream-7-industrial]].

**Antitrust posture.** Pool a non-competitive signal through an independent
administrator; never exchange price/bid/client information. The US DOJ's Feb-2023
withdrawal of its information-sharing safety zones removed the bright-line safe
harbor and put cross-competitor data sharing under case-by-case review with
explicit AI-disaggregation warnings; Canada's two-track regime is clearer — a
genuine legal-certainty reason to build the governance scaffold in Canada first
[[data-collectives/stream-3-legal]].

**Per-stakeholder contribution incentive.**

- **Engineering firms (members).** Contribute component-condition + post-replacement
  failure observations → receive RUL distributions calibrated across thousands of
  buildings, beating their in-house few-hundred-building base, plus a methodology
  defensible against incumbents and cross-firm benchmarking
  [[concepts/six-probabilistic-components]] [[concepts/ml-fault-detection-mechanical-systems]].
  **Free-riding throttle:** contribution-weighted access (richer contributors get
  richer priors / earlier model versions) — the engineered asymmetric value
  capture the foundation requires to make pooling rational among near-substitutes
  [[data-collectives/stream-1-economics-incentive]].
- **Property managers.** Portfolio-level reserve-risk visibility and fewer
  special-assessment surprises; role-appropriate dashboards (the multi-stakeholder
  access model REcollab already ships) [[entities/recollab]]. They direct the
  corporations' work-order/maintenance logs in.
- **Condo corporations / HOAs / boards (data-holders).** Better funding plans and
  lower special-assessment risk; in jurisdictions where studies are quasi-public
  the marginal disclosure cost is near zero [[entities/ns-active-condo-corporations-dataset]].
  They are the holder-directed on-ramp [[data-collectives/stream-4-regulatory]].
- **Insurers and lenders (adjacent demand anchor).** Downstream consumers of the
  calibrated risk signal — the structural analog of the banks that anchor a fraud
  utility. An insurer/lender who values the pooled signal *before the firm network
  is dense* is the most credible cold-start de-risker [[data-collectives/stream-7-industrial]]
  [[entities/recollab]].

**Data-mobility on-ramp.** Bootstrapped by condo corporations directing their own
reserve studies and maintenance records into the collective under Canada's
economy-wide data-mobility right — not by any pooling mandate (none exists)
[[data-collectives/stream-6-regulatory]] [[data-collectives/stream-4-regulatory]].

**Agentic positioning (stated as a bet).** Position the calibrated pool as
*agent-ready reserve-study ground truth* — the trustworthy, current, domain-grounded
substrate an agent would act on. This is a bet: there is zero verified commercial
precedent for an AI agent acting on a pooled cross-firm data substrate across
three independent streams [[data-collectives/synthesis-policy-market]]
[[data-collectives/stream-2-technical-architecture]]. It is the best demand
argument and the thinnest evidentiary one. The business must stand without it.

---

## (c) Go / no-go signal + load-bearing assumptions

**Signal: GO**, scoped as governance-and-network infrastructure pooling the
non-rivalrous condition signal, Canada-first, with the reserve-study value (not
agentic demand) carrying the P&L.

Three assumptions decide it. If any fails, the verdict flips:

1. **The data-network-effect is real and salable.** Pooled cross-firm failure
   observations must materially tighten RUL/Weibull calibration beyond any single
   firm's in-house base, and that accuracy delta must be something firms,
   insurers, or boards will pay for. *If false → no contribution incentive, and
   the play collapses back into the substitutes problem.*
   [[concepts/ml-fault-detection-mechanical-systems]] [[data-collectives/stream-1-economics-incentive]]
2. **Firms will treat condition data as non-rivalrous and clients/bids/fees as
   the competitive layer.** The whole design depends on this boundary holding in
   practice, not just on paper. *If firms conflate the two and withhold condition
   data as "proprietary," cold-start fails.* [[data-collectives/stream-1-economics-incentive]]
3. **Reserve-study value closes the business on its own.** Boards, insurers, and
   lenders must pay for better funding plans and risk signals *today*, with
   agentic demand as upside. *If the model only works under agentic demand → no-go*
   (you would be funding an unproven bet as the base case)
   [[data-collectives/synthesis-policy-market]].

---

## (d) Risks

- **Cold-start / SME onboarding (the chief execution risk).** Engineering firms
  are small, fragmented, and protective of their study databases — the Catena-X
  SME stall is the warning [[data-collectives/stream-7-industrial]]. Two
  mitigations stack: (i) seed the engine with holder-directed condo-corporation
  data (quasi-public NS studies) so the priors are credible before any firm
  joins; (ii) sign an anchor insurer/lender who values the signal early, so the
  collective has a paying demand side before the firm network is dense. **Do not
  require firm-to-firm trust on day one.**
- **The self-as-first-member bridge.** Condo's existing GTM is to build a *single*
  tech-enabled reserve-study firm and sell it [[entities/summer-gardens-condo]]
  [[concepts/proptech-valuation-multiples]]. That is in tension with organizing a
  *collective across* firms — but the tension resolves into a sequencing: operate
  as the tech-enabled firm first to seed calibration data from your own studies,
  then open the contributory layer once the engine is credible. You become your
  own first member. This is the most realistic cold-start path and it reconciles
  the two domains rather than choosing between them.
- **Downstream-model liability (unresolved in the foundation, sharper in condo).**
  A reserve study drives a fiduciary funding decision and carries professional-
  engineering liability. If the pooled engine's RUL/funding output proves wrong
  (a roof fails early, a special assessment lands), who is liable — the firm of
  record, the co-op, the administrator? The foundation left this open
  [[data-collectives/synthesis-policy-market]]; condo cannot. **Charter rule: the
  engine *informs*, the PEng firm of record *certifies and owns the stamp*.** The
  co-op supplies calibrated priors, not a certified study.
- **Substitutes trap on scope drift.** The moment scope creeps from condition data
  into client/bid/fee data, the non-rivalrous property is gone and Vives' Cournot
  prisoner's dilemma returns [[data-collectives/stream-1-economics-incentive]].
  The six-component scope-lock [[concepts/six-probabilistic-components]] and a hard
  data-taxonomy boundary in the charter are the only guardrails.
- **Agentic-demand bet.** Already flagged; restated as a risk because it is the
  project's "why now" and has no precedent [[data-collectives/stream-2-technical-architecture]].

---

## (e) Market capture / exit (cross-referenced to condo's acquirer thesis)

**Who captures it.** Not the firm with the most studies — the foundation is firm
that raw data scale is not the moat [[data-collectives/stream-7-industrial]]. The
capturer is whoever first assembles (a) the member network around the
non-rivalrous condition signal, (b) trustworthy neutral fiduciary governance per
CAN/DGSI 100-7, and (c) deep workflow integration into firms' and PMs' operations
[[data-collectives/synthesis-policy-market]]. The named alternative capturer is an
**incumbent platform** (CINC Systems is condo's primary acquirer target; Associa /
FirstService / Yardi / AppFolio are the backups) bolting a contributory layer onto
its existing footprint [[entities/associa]] [[concepts/proptech-valuation-multiples]].
Speed to the governance-and-network position is therefore the strategic variable —
the same conclusion as the foundation, applied to condo's named acquirers.

**How the collective reshapes the exit.** Condo's ADR-0004 exit models a tech-enabled
reserve-study *firm* at ~$5M revenue, 3-5x = $15-25M, against an 8.8x PropTech macro
multiple, with an "AI & Data-Driven PropTech" premium niche
[[concepts/proptech-valuation-multiples]]. The collective changes the asset being
sold: from a services/SaaS firm to a **governed data-network with a calibration
moat** — which maps directly onto that premium niche and is harder for an incumbent
to replicate by acquisition-plus-bolt-on.

**The structural complication worth flagging.** A neutral fiduciary co-op is
*harder to acquire* than a company — the members own the pooled data, so an
acquirer cannot simply buy it. The realistic exit is the **operating company around
the co-op** (the administrator, the engine, the workflow integrations, plus a
long-term data-services agreement with the co-op), not the pooled data itself. The
governance that makes contribution rational also caps what an acquirer can capture.
This is a genuine trade-off, not a flaw: it is the same reason the network is
defensible against an incumbent in the first place. Plan the exit as a sale of the
administrator/workflow layer, not of the data.

---

## Provenance

- Foundation: [[data-collectives/synthesis-policy-market]] and stream notes
  (stream-1 economics, stream-3 legal, stream-4/6 regulatory, stream-5
  governmental, stream-7 industrial, stream-2 technical).
- Condo facts (reused, not re-researched): [[concepts/six-probabilistic-components]],
  [[concepts/weibull-component-failure-distribution]],
  [[concepts/monte-carlo-reserve-confidence-intervals]],
  [[concepts/ml-fault-detection-mechanical-systems]],
  [[concepts/reserve-fund-contribution-smoothing]], [[entities/recollab]],
  [[entities/summer-gardens-condo]], [[entities/ns-active-condo-corporations-dataset]],
  [[entities/associa]], [[concepts/proptech-valuation-multiples]],
  [[entities/california-davis-stirling-5550]], [[sources/pdf-da86bd51429b]].

## Stage 2 wiki-grounding status

The required deliverable is this analysis doc. Filing a parallel grounded wiki
synthesis page (via `wiki answer --file` / `wiki query`) is the optional,
cap-gated Task 3. Consistent with how the foundation's Task 10 was handled —
analysis note primary, gateway page filed on cap headroom — wiki grounding is
**deferred** here to avoid spending against the live Anthropic monthly cap on a
synthesis that adds no new source-grounded claims (it recombines two already-grounded
domains). Revival trigger: explicit user request or cap reset. `ANTHROPIC_API_KEY_RESEARCH`
is valid, so `wiki answer --file` is available when that trigger fires.
