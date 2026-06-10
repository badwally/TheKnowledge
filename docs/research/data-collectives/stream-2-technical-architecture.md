# Stream 2 — Technical / architecture (analytical working note)

> Working note, not canonical wiki. Date: 2026-06-10. Deep-research verified
> (111 agents; peer-reviewed/standards/primary). **Wiki grounding PENDING** —
> all sources landed filter-rejected/review (the filter reads FL/DP/MPC papers
> as generic ML-privacy, not competitive-infrastructure); resume must
> `filter-correct --include` + re-ingest. Raw sources are committed.

## The privacy-preserving pooling stack (no single layer suffices)

Three layered mechanisms, each with an intrinsic limit:

1. **Federated / cross-silo learning** — shares gradients, not raw data. **Leaks**
   via gradient-inversion (DLG; Zhu NeurIPS 2019) and **subject-level**
   membership-inference across orgs (Suri et al. arXiv:2206.03317 — neither
   item- nor user-level DP protects a subject whose records span multiple
   participants, e.g. a person across several firms). Reconstruction collapses
   beyond batch size 1–2; secure aggregation blocks server-side per-update
   access (NVIDIA arXiv:2202.06924). Source: arxiv-2206.07284, arxiv-2206.03317.
2. **Differential privacy (DP-SGD)** — provably bounds per-record leakage at
   (ε,δ); **intrinsic, unremovable utility penalty** governed by ε. De-facto
   standard (Opacus, TF-Privacy). Source: web-2025-08-21-f21 (Springer AIR
   2025), arxiv-2409.13004 (NIST co-author).
3. **Cryptographic protection of updates** — MPC + (multiparty) homomorphic
   encryption hide individual inputs from the aggregator; **MPC leaks via the
   OUTPUT under n−1 collusion; HE is compute/communication-expensive.**

**Substrate layer:** **TEE / confidential clean rooms** (Azure Confidential
Clean Rooms, web-2026-06-03-4ff) — the strongest *deployed commercial* pooling
substrate: attested hardware enclaves hide raw data from collaborators AND the
cloud operator. **Caveats:** side-channel attacks (TEEfail, 2025) and
preview-maturity.

**Governance precedent:** US–UK PETs Prize Challenges (NIST, web-2023-05-09-53f)
— a real government-run benchmark of privacy-preserving pooling; useful "why
now / policy" bridge to Stream 5.

**Synthesis pattern:** no single mechanism is sufficient; the research frontier
is **hybrid composition** (MPC + secure-aggregation, transciphering HE,
heterogeneous-noise DP) that re-balances where cost and residual leakage land.

## ⚠ THE AGENTIC-LAYER GAP (most important finding for the thesis)

**Item 7 of the research brief — the agentic layer — produced ZERO surviving
verified claims.** No published architecture or commercial precedent for
agent-mediated data collectives (agents as contributors / consumers / governors
of a pooled substrate) survived adversarial verification. Same gap appeared in
Stream 0 (no 2023–2026 agentic/vertical-AI-on-pooled-data case verified).

**This is now a two-stream pattern and a substantive finding, not a search
miss:** the privacy-preserving substrate is mature and well-evidenced, but the
**agentic layer on top is genuinely greenfield** — little-to-no peer-reviewed or
documented commercial precedent as of mid-2026. Directly answers the user's "is
this a recent-precedent shape?" question: the *mechanism* has precedent; the
*agentic-AI-on-pooled-proprietary-data* shape does not yet. Whether that is
opportunity (first-mover) or warning (pattern hasn't materialized for a reason)
is the central tension for Task 10's "why now" synthesis.

**ACTION:** run one targeted deep-research pass specifically on agentic AI +
vertical-AI-on-pooled-data (2024–2026 commercial + arXiv) before Task 10, and
have Stream 7 (industrial) hunt the commercial angle. Also unresolved: OPAL
move-code-to-data (PDF won't convert) and distributed-ledger attribution/
provenance (no verified claims).

## Open questions

1. Agent-mediated data-collective architecture — any real precedent? (→ targeted pass + S7)
2. OPAL move-code-to-data vs model-sharing on the privacy-utility-cost frontier; where deployed? (find alt source)
3. Attribution/access governance + ledger provenance — any commercial deployment?
4. A composable end-to-end privacy budget across FL+MPC+DP+TEE — empirically validated combined guarantee?

## Source → status

| Topic | Source ID | Status |
|---|---|---|
| Gradient-inversion / FL leakage survey | arxiv-2206.07284 | raw committed; needs filter-correct |
| Subject MIA in cross-silo FL | arxiv-2206.03317 | raw committed; needs filter-correct |
| DP-FL (NIST) | arxiv-2409.13004 | raw committed; needs filter-correct |
| DP survey 2025 | web-2025-08-21-f21 | raw committed; needs filter-correct |
| Azure Confidential Clean Rooms (deployed TEE) | web-2026-06-03-4ff | raw committed; needs filter-correct |
| US–UK PETs Prize (NIST gov benchmark) | web-2023-05-09-53f | raw committed; needs filter-correct |
| Confidential computing (ACM Queue) | — | 403; find alt URL |
| OPAL move-code-to-data (MIT) | — | PDF won't convert; find alt (trust.mit.edu / MIT Press) |
