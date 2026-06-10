---
title: Data Collectives — Research Foundation Design
date: 2026-06-10
status: APPROVED
domain: data-collectives
forks_from: ~/code/condo (condo-capital-infra)
spine: policy & market structure
program_shape: C — agentic dimensional fan-out
---

# Data Collectives — Research Foundation Design

## Purpose

Establish a citation-grounded research foundation on **data collectives** — the
mechanism by which otherwise-competing or complementary stakeholders commit
proprietary data to a shared model that all members use to compete in a market.
The foundation is a reusable substrate; the first application is the condo /
reserve-fund-study collective forked from `~/code/condo`.

This is a **business-development** project executed **agentically** and **from
first principles**. The deliverable that follows from this spec is a **master
research prompt** (Anthropic prompt/context-engineering best practice) plus a
stubbed child prompt for the application leg.

## Interview-derived decisions

| Decision | Resolution |
|---|---|
| Telos | **Both, staged** — generalizable mechanism foundation first; condo case derived as application #1. |
| Spine | **Policy & market structure** — "why now / why Canada / who captures the market." Economics + architecture are *instruments*; legal/regulatory is the *constraint envelope*. |
| Agentic bias governs | **All three** — (a) the system being designed is agent-architected; (b) the *why-now* thesis is that agents need trustworthy pooled domain data to act; (c) the research/build is executed agentically. |
| Substrate | **New wiki domain `data-collectives`**, citation-grounded; condo leg cites both this domain and `condo-capital-infra`. |
| Program shape | **C — agentic dimensional fan-out**: precedent-first seed → parallel per-dimension streams → policy/market synthesis → condo application leg. |
| Staging | Foundation = primary deliverable. Condo application leg = **Stage 2**, defined here, executed after synthesis. |
| EU constructs | **Reference precedent only** (Gaia-X, Catena-X, data spaces) — not in-scope policy. |
| AI-precedent recency | Industry-specific / agentic-AI claims weighted to **2023–2026**; mechanism/governance/legal/economic precedents may be foundational. |

## North-star question

> Is there a policy- and market-structure opening — emphatically in Canada,
> benchmarked against the US — for stakeholder-pooled, industry-specific AI
> built on proprietary data committed by otherwise-competing firms? If so, who
> captures that market, and what does the agentic shift change about the answer?

The spine is the **synthesis target**, not a starting assumption. Stream 0
grounds the empirical base *before* the spine is applied — this is the
confirmation-bias guard.

## Scope boundary

**In scope:** the pooled-proprietary-data → shared-model mechanism among
competing/complementary stakeholders; US + Canada (Canada primary); agentic
vertical-AI emphasis.

**Out of scope (except as explicit contrast):** generic open data, open-source,
and pure data-resale marketplaces where nothing is pooled into a shared model.

**Reference-only:** EU data-space constructs (Gaia-X, Catena-X) — cited as
precedent, never treated as in-scope policy.

## Program (Approach C)

**Stream 0 — Precedent census (seed, runs first).** Taxonomy + case file of real
pooled-data ventures: data cooperatives, data trusts, data commons,
federated-learning consortia, data clean rooms / collaboratives, industry data
exchanges, agentic vertical-AI models. Per case: structure, contributors, the
incentive that overcame the "give up my edge" problem, governance, outcome
(including failures).

**Streams 1–7 — parallel agentic fan-out** (each files grounded
`concepts`/`entities`/`synthesis` pages):

1. **Economic/incentive** — cooperative game theory, data-as-asset valuation,
   value distribution (Shapley-style data pricing), free-rider/defection, the
   contribute-your-edge paradox and documented resolutions.
2. **Technical/architecture** — federation, differential privacy, secure
   multiparty computation, clean rooms, model-sharing vs data-sharing, and the
   agentic architecture (agents as contributors / consumers / governors).
3. **Legal** — data ownership & trade-secret in pooled data; antitrust /
   competition law on competitor data-sharing (US DOJ/FTC + Canada Competition
   Bureau); privacy (PIPEDA, Québec Law 25, US state regimes; GDPR reference);
   liability.
4. **Regulatory** — sector data-sharing mandates & safe harbors; AI-regulation
   status (Canada AIDA, US federal/state); open-banking-style portability
   mandates as structural precedent.
5. **Governmental/policy** *(spine core)* — Pan-Canadian AI Strategy, sovereign
   compute, data-sovereignty & data-governance standardization, federal/
   provincial data-collaborative funding; the explicit "why Canada" argument;
   US contrast.
6. **Academic** — data-cooperative literature (data dignity / RadicalxChange /
   MIT), federated learning, Ostrom commons governance, mechanism design,
   data-market / platform economics.
7. **Industrial** — who is doing this now, by sector (health, finance, mobility,
   manufacturing); vertical-AI startups monetizing pooled proprietary data;
   competitive-moat dynamics.

**Synthesis layer** — orders 1–7 under the spine to answer the north-star,
including the agentic market thesis (agents need trustworthy pooled domain data
to act → the collective is agent-era infrastructure).

**Application leg (Stage 2).** Derive the specific collective (engineering firms
+ property managers + HOAs → unified reserve-study data service) from the
foundation. Cite `condo-capital-infra` for everything already established there
(reserve-study market, vendor landscape, NS/ON/BC regulation, engine, GTM) —
do **not** re-research it. The foundation supplies the *mechanism, incentive
design, legal/antitrust envelope, and Canada-policy fit*; condo supplies the
*market specifics*.

## Guardrails

- **Surface-anchor-leakage guard.** The general foundation must NOT inherit
  condo's reserve-study vocabulary, jurisdictions, or Longspan acquirer thesis.
  Foundation pages are domain-neutral; condo terms appear only in the Stage-2
  leg.
- **Confirmation-bias guard.** Ground (Stream 0) before spining (synthesis).
- **Recency weighting.** Per the recency rule above.
- **Corpus-quality gate.** Before any NotebookLM synthesis, sample word counts
  per `~/code/knowledge/CLAUDE.md` research preconditions; sparse corpora
  confabulate.
- **Citation grounding mandatory.** Every claim → `[[sources/<id>]]`. Drafts
  (`--draft`) tolerated ≤ 7 days.
- **Context discipline.** Use `wiki retrieve` / `wiki context`; never dump
  `index.md` or `log.md` into an LLM prompt.

## Definition of done

- Each stream: grounded pages filed, load-bearing claims adversarially verified,
  open questions logged.
- Synthesis: north-star answered with a defensible "why now / why Canada / who
  captures" position **plus an explicit confidence / uncertainty ledger**.
- Stage 2 (later): a condo-collective feasibility position derived from and
  cross-cited to the foundation.

---

## DELIVERABLE — Master research prompt

> Run via the `deep-research` skill or `wiki research`, executed agentically.
> Stream 0 first; then 1–7 fan out; then synthesis. The condo child prompt
> (below) is Stage 2.

```text
<role>
You are the principal researcher for a citation-grounded knowledge program on
DATA COLLECTIVES, operating inside the ~/code/knowledge wiki. You work
agentically: you fan out parallel sub-investigations, adversarially verify
load-bearing claims before filing, and synthesize. You build from first
principles and you do not pad findings to seem complete — you log what you do
not yet know.
</role>

<objective>
Answer one north-star question and file the supporting evidence as grounded
wiki pages in the `data-collectives` domain:

  Is there a policy- and market-structure opening — emphatically in Canada,
  benchmarked against the US — for stakeholder-pooled, industry-specific AI
  built on proprietary data committed by otherwise-competing firms? If so, who
  captures that market, and what does the agentic shift change about the answer?

The policy/market-structure question is the SYNTHESIS TARGET. Do not assume its
answer. Ground the empirical precedent base first; let the evidence shape the
position.
</objective>

<context>
- This domain forks from ~/code/condo (`condo-capital-infra`), a reserve-study
  venture whose stakeholders (engineering firms, property managers, HOAs) are a
  pooled-data example. The condo specifics are Stage 2 — keep this foundation
  domain-neutral.
- REUSE, do not re-research, anything already grounded in `condo-capital-infra`.
- Retrieval discipline: to pull existing wiki knowledge use
  `wiki retrieve "<question>"` (default) or `wiki context "<slug>"`. NEVER load
  `index.md` or `log.md` wholesale into a prompt — they are unbounded.
- All writes go through the gateway (`wiki <subcommand>` / `wiki_*`). No direct
  writes to wiki/ or raw/.
</context>

<scope>
IN: the mechanism by which competing/complementary stakeholders commit
proprietary data to a shared model all members use to compete. US + Canada
(Canada primary). Agentic vertical-AI emphasis.

OUT (except as explicit contrast): generic open data, open-source, pure
data-resale marketplaces where nothing is pooled into a shared model.

REFERENCE-ONLY: EU data-space constructs (Gaia-X, Catena-X, data spaces) — cite
as precedent, never treat as in-scope policy.

RECENCY: claims about industry-specific or agentic AI models built on pooled
data must be weighted to 2023–2026. Mechanism / governance / legal / economic
precedents may be foundational (older is fine) — but date them.
</scope>

<program>
Execute in this order.

STREAM 0 — PRECEDENT CENSUS (run first; seeds the rest).
  Build a taxonomy and case file of real pooled-data ventures: data
  cooperatives, data trusts, data commons, federated-learning consortia, data
  clean rooms / collaboratives, industry data exchanges, and agentic
  vertical-AI models. For each case capture: structure, who contributed, the
  incentive that overcame the "give up my edge" problem, governance model,
  outcome (INCLUDING failures and why). Output: one `synthesis` taxonomy page +
  `entity` pages per significant case.

STREAMS 1–7 — PARALLEL FAN-OUT (each files grounded concept/entity/synthesis
pages with a per-stream open-questions list).
  1. ECONOMIC/INCENTIVE — cooperative game theory, data valuation,
     value-distribution mechanisms (e.g. Shapley-style data pricing),
     free-rider/defection, the contribute-your-edge paradox + resolutions.
  2. TECHNICAL/ARCHITECTURE — federation, differential privacy, secure
     multiparty computation, clean rooms, model-sharing vs data-sharing, and
     the AGENTIC architecture (agents as contributors / consumers / governors
     of the pool).
  3. LEGAL — data ownership & trade-secret in pooled data; antitrust/
     competition law on competitor data-sharing (US DOJ/FTC; Canada Competition
     Bureau); privacy (PIPEDA, Québec Law 25, US state regimes; GDPR as
     reference); liability allocation.
  4. REGULATORY — sector data-sharing mandates & safe harbors; AI-regulation
     status (Canada AIDA, US federal/state); open-banking-style data-portability
     mandates as structural precedent.
  5. GOVERNMENTAL/POLICY (spine core) — Pan-Canadian AI Strategy, sovereign
     compute, data-sovereignty & data-governance standardization, federal/
     provincial data-collaborative funding; build the explicit "why Canada"
     argument; contrast with US posture.
  6. ACADEMIC — data-cooperative literature (data dignity / RadicalxChange /
     MIT), federated learning, Ostrom commons governance, mechanism design,
     data-market / platform economics.
  7. INDUSTRIAL — who is doing this now by sector (health, finance, mobility,
     manufacturing); vertical-AI startups monetizing pooled proprietary data;
     competitive-moat dynamics.

SYNTHESIS — order streams 1–7 under the spine to answer the north-star.
  Include the AGENTIC MARKET THESIS: agents need trustworthy, domain-grounded,
  pooled data to act, so the collective is infrastructure for an agent-driven
  economy — test this claim against the evidence, do not assert it. Produce a
  defensible "why now / why Canada / who captures the market" position AND an
  explicit confidence / uncertainty ledger.
</program>

<guardrails>
- SURFACE-ANCHOR-LEAKAGE: keep foundation pages domain-neutral. Do not import
  reserve-study vocabulary, condo jurisdictions, or any Longspan framing into
  the general foundation.
- CONFIRMATION BIAS: Stream 0 (ground) precedes synthesis (spine). No reordering.
- ADVERSARIAL VERIFICATION: before filing a load-bearing claim, try to refute
  it from independent sources; record the strongest counter-evidence found.
- CITATION GROUNDING: every claim ends with [[sources/<id>]]. Use --draft if
  provenance is pending; finalize within 7 days.
- CORPUS QUALITY: before any NotebookLM synthesis, sample source word counts;
  block on sparse corpora (they confabulate).
- CONTEXT: wiki retrieve / wiki context only; never dump index.md or log.md.
</guardrails>

<execution>
- Fan out one sub-investigation per stream; within a stream, parallelize by
  sub-topic.
- Date every precedent. Flag anything pre-2023 when used for an AI-model claim.
- File incrementally and validate each page before moving to the next.
- End each stream with an open-questions list that seeds the next pass.
</execution>

<success>
DONE when: every stream has grounded pages with verified load-bearing claims and
a logged open-questions list; AND the synthesis answers the north-star with a
defensible position + an explicit confidence/uncertainty ledger. "I don't know
yet, here's what would resolve it" is a valid and required output where the
evidence is thin.
</success>
```

---

## DELIVERABLE (stub) — Condo application child prompt (Stage 2)

> Executed after the foundation synthesis exists. Cites both `data-collectives`
> and `condo-capital-infra`.

```text
<role>Principal researcher deriving a specific data collective from the
data-collectives foundation.</role>

<objective>
Assess feasibility of, and design the incentive/governance/legal structure for,
a data collective among engineering firms, property managers, and HOAs that
produces a unified reserve-fund-study data service all members use to compete.
</objective>

<context>
- REUSE from `condo-capital-infra` (cite, do not re-research): reserve-study
  market, vendor landscape, NS/ON/BC/QC regulation, the probabilistic engine,
  the Canada-first GTM and acquirer thesis.
- REUSE from `data-collectives` (cite): the mechanism, incentive-design
  patterns, antitrust/privacy envelope, technical/agentic architecture, and the
  Canada-policy "why now" thesis.
- This leg supplies ONLY the application: which foundation pattern fits this
  market, the specific incentive that gets engineering firms / PMs / HOAs to
  contribute, the antitrust-safe value-distribution design, and the fit to
  Canada's AI goals.
</context>

<success>
A condo-collective feasibility position: go / no-go signal, the recommended
structure, the incentive mechanism, the legal envelope, and the
market-capture/exit implication — each cross-cited to the foundation.
</success>
```

## Next step

After spec approval, transition to the writing-plans skill to produce the
execution plan (bootstrap domain → Stream 0 → parallel streams → synthesis),
then run it.
