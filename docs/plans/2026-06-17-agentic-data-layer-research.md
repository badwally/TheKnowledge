# agentic-data-layer — research project plan

Date: 2026-06-17
Status: scoped, pending execution

## Purpose

Build a foundational, vertical-agnostic research corpus on the **runtime interface
between AI agents and semantic data structures** — how agents consume and produce
semantic models at runtime, and what architecture, tool-design, and validation
patterns make that interface reliable.

The corpus is meant to be queried repeatedly when making architecture, design, and
business decisions for *arbitrary* opportunities (longspan is the first consumer, not
the anchor). Anchoring the corpus to longspan / civil engineering / reserve studies
was explicitly rejected: a specialization framing propagates beyond the prompt into
which sources the filter accepts and which examples seed the bank, paying a
general-corpus cost for a vertical-shaped corpus.

## Domain decision

Bootstrap a **new domain `agentic-data-layer`**, sibling to `semantic-models`.

Rationale:
- `semantic-models` already excludes this material by design — its exclusion criteria
  name "sources scoped exclusively to the agentic application layer ... without
  grounding in the representation formalism." That boundary is the seam for a sibling.
- `ai-and-agents` is an unfleshed stub (`v0.1.0-auto`, empty inclusion/exclusion
  criteria); absorbing a precise intersection there gives the filter nothing to
  discriminate on.
- A new domain gets its own filter threshold, example bank, and MOC, and pairs cleanly
  with `semantic-models` as the operator-architect layer above the foundational one.

Layering:
- `semantic-models` — foundational: KR formalism, ontology theory, the model itself.
- `agentic-data-layer` — operator-architect: the agent-facing runtime contract.
- longspan's own corpus — domain-specific AEC / BIM / reserve-study ontologies.

## Altitude

Operator-architect, pattern-level, reusable across domains. Vertical framing stripped.
The operator-architect *properties* are kept, stated abstractly: long-lived / mutable
model, write-path safety, provenance, reliability under change. These are what
separate this corpus from a generic "agents + knowledge graphs" survey.

## Bootstrap description (sets the filter)

> The runtime interface between AI agents and semantic data structures: how agents
> *consume* semantic structures (knowledge-graph RAG / GraphRAG, text-to-SPARQL/
> Cypher/GQL, ontology-grounded retrieval, semantic and metrics layers exposed as
> agent tools, MCP/function-calling over graph and triple-store backends) and how
> agents *produce and maintain* them (LLM-driven entity/relation extraction, ontology
> population, schema- and SHACL-constrained generation, automated KG construction from
> documents, verification and provenance of agent-generated triples). Operator-architect
> altitude: assumes the formalism exists (that is `semantic-models`' concern) and
> studies the agent-facing runtime contract, tool/affordance design, evaluation, and
> failure modes. Excludes pure KR formalism and ontology theory (→ semantic-models)
> and domain-specific ontologies such as AEC/BIM/reserve-study schemas (→ longspan's
> own corpus).

## Research plans

Pre-split into three. Plans 1 and 2 run as fan-outs; Plan 3 is held as a potential
post-hoc synthesis over the accumulated corpus, not a fresh fan-out.

### Plan 1 — Consumption & interface (`agents-consume-semantic-structures`)

> How do AI agents retrieve and query semantic data structures at runtime? Cover
> knowledge-graph RAG and GraphRAG (Microsoft GraphRAG and successors), text-to-query
> generation (SPARQL, Cypher/GQL, SQL-over-semantic-layer), ontology-grounded
> retrieval, and exposing semantic layers / metrics layers / triple stores to agents
> as tools via MCP and function-calling. When does a semantic or graph layer outperform
> plain vector RAG for an agent? Cover tool/affordance design, read-path caching, and
> accuracy/faithfulness benchmarks for text-to-query and GraphRAG. Operator-architect,
> pattern-level, reusable across domains. Prioritize 2024–2026 arXiv and substantive
> engineering write-ups from graph-DB and semantic-layer vendors.

### Plan 2 — Production, maintenance & validation (`agents-produce-semantic-structures`)

> How do AI agents construct, populate, and maintain semantic data structures, and how
> is their output validated against the model? Cover LLM-driven entity and relation
> extraction into knowledge graphs, ontology population, automated KG construction from
> unstructured documents, and agentic schema evolution. Cover validation and grounding:
> SHACL/ShEx/JSON-Schema-constrained generation, ontology grounding to reduce
> hallucination, and verification and provenance of agent-generated triples or records.
> Emphasize write-path safety and correctness for long-lived, mutable knowledge models.
> Operator-architect, pattern-level. Prioritize 2024–2026 arXiv and substantive vendor
> engineering material.

### Plan 3 — Architecture & failure modes (`agentic-data-layer-architecture`) — HELD

> What architecture patterns govern the semantic or canonical data layer as the
> contract between AI agents and heterogeneous data systems, and how does that
> interface fail? Cover the semantic layer as agent-facing contract, separation of read
> vs. write paths, consistency and provenance for long-lived models, and documented
> failure modes at the agent↔model boundary (hallucinated entities, schema drift, stale
> retrieval, unsafe writes). Synthesize design guidance for a reliable agentic data
> layer independent of any vertical. Operator-architect altitude.

Run Plan 3 as a `wiki query` synthesis over the corpus from Plans 1+2, only after a
corpus-quality check.

## Execution sequence

1. `wiki bootstrap-domain "<description>" agentic-data-layer`
2. Plan 1: `wiki research "<plan 1>" --domain agentic-data-layer --review`, inspect
   candidates, then `--execute <id>`.
3. Plan 2: same flow.
4. **Corpus-quality gate** (per CLAUDE.md research preconditions): sample word counts
   on 5–10 accepted candidates; check convert-failure rate in query-plan logs; check
   `step=index_settle` distinct_sources after the run. Sparse corpus → fix source
   access before committing NLM quota.
5. Plan 3 as `wiki query` synthesis if the corpus warrants it.

## Open decisions resolved

- Domain home → bootstrap new (`agentic-data-layer`).
- Altitude → reusable patterns only; operator properties stated abstractly.
- longspan framing → stripped from prompts.
- Split → 3 plans; 1+2 fan-out, 3 held as synthesis.
