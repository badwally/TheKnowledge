# Stage 2 — Condo Application Leg Implementation Plan

> **For agentic workers:** Execute in a FRESH session (this plan + the foundation
> synthesis are the inputs; all state is on disk). This is a SYNTHESIS/DESIGN
> task, not a research fan-out — author analysis over two existing grounded
> domains. Do NOT run deep-research workflows (a) they are unnecessary here and
> (b) the Anthropic monthly spend cap is live. Steps use `- [ ]` tracking.

**Goal:** Derive a feasibility + design position for a data collective among
engineering firms, property managers, and HOAs that produces a unified
reserve-fund-study data service all members use — by applying the
`data-collectives` foundation to the condo market.

**Architecture:** Pure synthesis. Inputs = (1) `docs/research/data-collectives/
synthesis-policy-market.md` + the 8 stream notes; (2) what `condo-capital-infra`
already establishes (reserve-study market, vendors/acquirers, NS/ON/BC/QC
regulation, the probabilistic engine, Canada-first GTM). Output = an analysis
doc + (if cap allows) grounded wiki pages citing BOTH domains. **Reuse condo
facts; do NOT re-research them.**

**Tech stack:** read-only `wiki retrieve`/`wiki context` over both domains;
authoring via docs/ note first, then gateway pages if/when cap + auth allow.

---

## Inherited design constraints (from the foundation synthesis — do not re-derive)

1. **Pool the non-rivalrous signal, not the competitive one.** The only durable
   commercial pooling pattern is the fraud/AML utility. For condo: pool
   **asset-condition / component-failure data** (firms don't compete on how fast
   a roof degrades), NOT client relationships, bids, or fee schedules. This
   directly answers Stream 1's substitutes problem — it is the load-bearing
   design decision.
2. **Holder-directed data mobility is the legal on-ramp.** Condo corporations own
   their building/reserve data and can *direct* it into the collective — ride
   Canada's economy-wide data-mobility right rather than any pooling mandate.
3. **Fiduciary data cooperative/trust, governed per CAN/DGSI 100-7.** Neutral
   administration is also the antitrust-safe design (the fraud-utility lesson).
4. **Canada-first** for the governance scaffold + antitrust certainty (US lost
   its 2023 safety zones) + data-sovereignty resonance — aligns with condo's
   existing Canada-first GTM.
5. **Agentic = stated bet, not trend.** Zero precedent (3 streams). Position as
   agent-ready reserve-study ground truth, but flag it as the core unproven bet.
6. **Moat = network + governance + workflow integration**, not data scale.
7. **Cold-start is the chief execution risk** (Catena-X's SME stall) — plus
   liability for downstream model harms (unresolved in the foundation).

---

## Tasks

### Task 1: Gather inputs (read-only)
- [ ] Read `docs/research/data-collectives/synthesis-policy-market.md` (the spine).
- [ ] `wiki retrieve` over `condo-capital-infra` for: reserve-study data shape,
      the six probabilistic components, stakeholder roles (engineering firms /
      PMs / HOAs), and the Canada-first GTM/acquirer thesis. Do not load condo
      wholesale — targeted retrieves only.
- [ ] List the concrete reuse points (what condo already proves) vs the net-new
      design questions Stage 2 must answer.

### Task 2: Author the feasibility + design position
- [ ] Write `docs/research/data-collectives/stage2-condo-collective.md` covering:
  (a) **Fit test** — does the condo market satisfy the foundation's success
      conditions? (non-rivalrous signal? holder-directed on-ramp? complementary
      not-substitute data? governance scaffold available?)
  (b) **Design** — what is pooled (condition/failure data), entity form
      (fiduciary co-op/trust per CAN/DGSI 100-7), the incentive each stakeholder
      type has to contribute, antitrust-safe administration, the data-mobility
      on-ramp.
  (c) **Go / no-go signal** + the 2–3 load-bearing assumptions that decide it.
  (d) **Risks** — cold-start/SME-onboarding, the agentic-demand bet, downstream
      liability, the substitutes trap if scope drifts to competitive data.
  (e) **Market capture / exit** implication, cross-referenced to condo's existing
      acquirer thesis.
  Every claim cites the foundation (`[[...]]` to data-collectives pages/notes) or
  condo-capital-infra. Domain-neutral foundation terms stay; condo specifics live
  only here.

### Task 3: (Optional, cap-gated) Ground into the wiki
- [ ] If spend cap + auth allow: file grounded synthesis/concept pages via the
      gateway citing both domains. Else: leave as the docs analysis + note the
      deferral. Do NOT force `wiki query` if it risks confabulation/cap.

### Task 4: Checkpoint + commit
- [ ] Update `docs/session-state.md`; commit. Diff predictions vs git.

---

## Done criteria
A defensible condo-collective feasibility position (go/no-go + structure +
incentive design + risks + capture), cross-cited to the foundation, authored
without re-researching condo and without tripping the spend cap.
