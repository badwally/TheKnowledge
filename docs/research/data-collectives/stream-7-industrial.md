# Stream 7 — Industrial (analytical working note)

> Working note, not canonical wiki. Date: 2026-06-10. Deep-research (107 agents);
> verification PARTIALLY truncated by the Anthropic monthly spend limit — the
> findings below were verified BEFORE the cap; some health-sector duplicates
> (Truveta, Datavant, Sonar) went unverified (logged as open). Grounded via
> filter-correct + re-ingest.

## Who actually pools competitor data right now

**Genuine cross-competitor pooling exists — concentrated in fraud / financial-
crime utilities:**
- **Early Warning Services** (US, bank-owned since 2006 by 7 largest banks) —
  rivals contribute proprietary deposit-risk/fraud data to a shared queryable
  utility; screened $10.8T payments in 2024. Structurally a contributory
  credit-bureau model. → `[[sources/web-2026-04-03-04f]]`.
- **Cifas** (UK non-profit, 500+ members incl. direct bank competitors) —
  National Fraud Database (~2M records). → `[[sources/web-2026-05-21-5db]]`.

**The pattern:** the durable, real cross-competitor pool is the **fraud/AML
utility** — where the pooled signal is *non-rivalrous to compete on* (no bank
competes on "who got defrauded"), contribution is mutually protective, and the
data is complementary not substitutable. This is the **single most transferable
precedent** for a condo collective: pool the data nobody competes on (asset
condition / failure history), not the data they do (client relationships, bids).
It is also the live embodiment of Stream 1's result — pooling works where
contributed data is complementary, not a competitive substitute.

## What is NOT pooling (critical distinctions)

- **LexisNexis Telematics Exchange** — consumer-permissioned **aggregation**:
  insurers *buy* opt-in driver data, they don't *contribute* proprietary data.
  Not a competitor pool. → `[[sources/web-2026-01-01-dec]]`.
- **Datavault AI "Data Unions"** (Oct 2025) — PR-stage, going-concern-flagged,
  no demonstrated ARR; aspirational tokenized model. → `[[sources/web-2025-10-27-5da]]`.

## Moat dynamics (the data-moat debate)

- **a16z "The Empty Promise of Data Moats"** + corroborating analyses: pooled/
  scale data is **frequently NOT a durable moat** — diminishing returns,
  commoditization, prediction-error floors. → `[[sources/web-2019-05-09-487]]`.
  Implication: a collective's defensibility is **governance + network membership
  + workflow integration**, not the raw data scale itself.

## Reference: EU data spaces

- **Catena-X** — real large-enterprise auto adoption (8 of 10 largest suppliers;
  BMW mandates participation) BUT **network effects stalled at the SME level**,
  needing €23M German public funding for cold-start/onboarding. → `[[sources/web-2026-06-08-406]]`.
  Lesson: even a well-backed data space struggles with the **cold-start /
  SME-onboarding** problem — directly relevant to bootstrapping a collective of
  small engineering firms / HOAs.

## ⚠ AGENTIC ANGLE — zero precedent CONFIRMED (now a 3-stream finding)

This stream specifically hunted for a commercial AI agent acting on a pooled
cross-firm data substrate, or a vertical-AI "data co-op" positioned for the
agentic era. **None found.** The only agentic vertical-AI evidence (Harvey) was
**refuted** as single-firm custom training, not cross-competitor pooling. Adding
to Stream 0 (no 2023–2026 agentic pooled-data case) and Stream 2 (no agentic-
layer architecture), the **zero-commercial-precedent finding for agentic-AI-on-
pooled-proprietary-data is now robust across three independent streams.** The
shape the project proposes is genuinely unprecedented commercially as of mid-2026.

## Open questions (→ Task 10)

1. Health sector unresolved (Truveta/Datavant/Sonar) — genuine pooling vs
   aggregation? (verification truncated by spend cap)
2. Is any 2023–2026 vertical-AI startup bootstrapping a model from MANY competing
   contributors' data (contributory cold-start)? None verified.
3. Fraud-utility moat durability vs real-time fraud-API entrants.
4. Will Catena-X's €23M SME push beat the cold-start stall by end-2026?

## Source → status

| Topic | Source ID | Status |
|---|---|---|
| Early Warning Services (genuine pool) | web-2026-04-03-04f | grounded |
| Cifas (genuine pool) | web-2026-05-21-5db | grounded |
| LexisNexis (aggregation contrast) | web-2026-01-01-dec | grounded |
| a16z data-moat debate | web-2019-05-09-487 | grounded |
| Datavault Data Unions (aspirational) | web-2025-10-27-5da | grounded |
| Catena-X SME accelerator (reference) | web-2026-06-08-406 | grounded |
