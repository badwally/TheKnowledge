# WIKI.md — Conventions Reference

Contract for everything that reads or writes the knowledge base. Pair with `CLAUDE.md` (agent control surface). Every component — gateway, validator, watcher, converters, filter, lint, agents — codes against this document.

## Table of contents

1. Architecture
2. Directory layout
3. Frontmatter schema
4. Page types and templates
5. Citation format and rules
6. Slug conventions
7. `index.md` format
8. `log.md` format
9. Gateway operations (CLI + MCP)
10. Filter and learning
11. Validator rules
12. Lint operations
13. NotebookLM integration
14. Forward-looking notes

---

## 1. Architecture

Three layers (per the LLM Wiki pattern):

- **Raw sources** (`raw/`) — immutable, normalized to markdown + YAML frontmatter. Owned by converters and the watcher. Never edited after ingest except for pipeline-stage frontmatter updates (filter result, NotebookLM corpus IDs, wiki backlinks).
- **Wiki** (`wiki/`) — LLM-authored knowledge. Six page types (entity, concept, source, synthesis, MOC, artifact). All writes go through the gateway and pass the validator.
- **Schema** (`CLAUDE.md` + `WIKI.md`) — control surface. Co-evolves with the system; changes propagate via `wiki migrate` (see § Migration).

Synthesis is hybrid:

- **Wiki canonical** — single source of truth. Every NotebookLM artifact is filed back as a wiki page with citations into wiki source pages and a link back to the live NotebookLM resource.
- **NotebookLM as service** — invoked for large-corpus synthesis (>~30–50 sources). All invocation goes through the gateway. The wiki and the NotebookLM corpora cannot drift because every NotebookLM operation has a wiki side effect.

Authorship is hybrid:

- **Incremental (agent-driven)** — single source, low-stakes. Agent reads source + schema + relevant existing pages, proposes updates through gateway. Used for Web Clipper, voice notes, ad-hoc PDFs.
- **Batch (code-driven)** — research-notebook pipeline writes canonical-schema pages directly. Used for new research domains with 50+ sources and citation-fidelity requirements.

## 2. Directory layout

```
~/code/knowledge/
├── CLAUDE.md
├── WIKI.md
├── index.md
├── log.md
├── raw/
│   ├── web/                # Web Clipper, manual URL imports
│   ├── youtube/            # transcripts + metadata
│   ├── arxiv/              # extracted text + sidecar PDF
│   ├── pubmed/
│   ├── pdf/                # extracted text + sidecar PDF
│   ├── voice/              # whisper transcript + sidecar audio
│   ├── audiobook/          # transcript + sidecar audio
│   ├── note/               # imported notes (Apple Notes, Notion via pollers)
│   └── inbox/              # drop zone — unsorted files awaiting routing
├── wiki/
│   ├── entities/
│   ├── concepts/
│   ├── sources/
│   ├── synthesis/
│   ├── mocs/
│   └── artifacts/
│       ├── slides/
│       ├── audio/
│       └── briefings/
├── nlm/
│   └── notebooks.yaml      # domain ↔ NotebookLM notebook ID map
└── .knowledge/             # internal state (gitignored where appropriate)
    ├── policies/           # editorial policies per domain
    │   └── <domain>/
    │       ├── policy.yaml
    │       ├── policy_versions/
    │       └── examples/   # filter example bank
    ├── locks/              # write locks for concurrency safety
    └── lint/               # lint reports
```

## 3. Frontmatter schema

Every source in `raw/` and every wiki page begins with YAML frontmatter delimited by `---`. Two layers: stable core fields (same across all source types), and a type-specific `meta:` block.

### 3.1 Core fields (sources, all types)

```yaml
---
id: <type>-<short-id>          # stable, unique across raw/. Examples below.
type: youtube|arxiv|pubmed|pdf|web|voice|audiobook|note|csv|other
title: "<source title>"
url: "<canonical URL, optional>"
authors: ["<name>", ...]
published_at: "YYYY-MM-DD"      # optional if unknown
ingested_at: "YYYY-MM-DDThh:mm:ssZ"
content_hash: "sha256:<hex>"    # over the body, used for idempotency
source_path: "raw/<type>/<id>.<ext>"  # path to sidecar binary, optional
filter:
  score: 0.92                   # 0.0–1.0
  policy_version: "<domain>-vN"
  rationale: "<one-sentence explanation>"
  decided_at: "YYYY-MM-DDThh:mm:ssZ"
  user_correction:              # null if no correction; populated when user overrides
    decided_at: "..."
    score: 1.0                  # corrected to 'include' or 0.0 'exclude'
    rationale: "<why the original decision was wrong>"
domains: ["<domain-slug>", ...]  # which domain policies applied
nlm_corpus_ids: ["<notebook-id>", ...]  # NotebookLM notebooks containing this source
wiki_pages: ["wiki/sources/<id>", ...]  # wiki pages referencing this source (backlink integrity)
meta:                           # type-specific, see § 3.2
  ...
---

<body content — markdown>
```

### 3.2 Type-specific `meta:` blocks

```yaml
# type: youtube
meta:
  channel: "Huberman Lab"
  channel_id: "UC2D2CMWXMOVWx7giW1n3LIg"
  duration_seconds: 7220
  caption_track: "manual" | "auto" | "none"
  captions_path: "raw/youtube/<id>.captions.json"  # optional sidecar

# type: arxiv
meta:
  arxiv_id: "2403.12345"
  categories: ["q-bio.NC", "q-bio.QM"]
  doi: "<doi if available>"
  abstract: "<abstract text>"

# type: pubmed
meta:
  pmid: "39847203"
  doi: "<doi>"
  journal: "Nature Neuroscience"
  mesh_terms: ["Glucagon-Like Peptide 1", "Reward", "Dopamine"]

# type: pdf
meta:
  doi: "<doi if available>"
  page_count: 28
  extraction_tool: "pdfplumber" | "marker" | "manual"

# type: web
meta:
  source_app: "obsidian-web-clipper" | "manual"
  site: "<domain.tld>"
  excerpt: "<2-3 sentence preview>"
  reading_time_minutes: 12

# type: voice
meta:
  device: "iphone" | "macbook"
  duration_seconds: 312
  transcription_model: "whisper-large-v3"

# type: audiobook
meta:
  asin: "<amazon-id>"
  duration_seconds: 36000
  transcription_model: "whisper-large-v3"
  chapter_index: "raw/audiobook/<id>.chapters.json"

# type: note
meta:
  source_app: "apple-notes" | "notion" | "obsidian-vault"
  source_id: "<remote-id-from-source-app>"
  imported_at: "YYYY-MM-DDThh:mm:ssZ"

# type: csv
meta:
  row_count: 1284
  column_count: 12
  columns: ["timestamp", "user_id", "event", ...]   # first 20 column names
  delimiter: "," | "\t" | ";" | "|"
  encoding: "utf-8" | "utf-8-sig" | "latin-1"
  original_filename: "<basename.csv>"
  extraction_tool: "csv (stdlib)"
```

Add new types by extending this list. The validator schema is the source of truth at runtime; this document defines the human-readable contract.

### 3.3 Wiki page frontmatter

Wiki pages have their own frontmatter shape per page type — see § 4.

## 4. Page types and templates

Every wiki page conforms to one of six types. Templates are not optional; the validator enforces required sections and frontmatter fields.

### 4.1 Entity (`wiki/entities/<slug>.md`)

A real-world thing referenced across sources: a drug, person, organization, paper, place. Long-lived; updated as new sources arrive.

```yaml
---
type: entity
slug: semaglutide
canonical_name: "Semaglutide"
aliases: ["Ozempic", "Wegovy", "Rybelsus"]
entity_kind: drug | person | paper | organization | place | other
domains: ["glp1-reward-modulation"]
created_at: "2026-04-27T14:32:00Z"
last_updated: "2026-04-27T18:15:00Z"
sources_count: 14
---

# Semaglutide

**Aliases:** Ozempic, Wegovy, Rybelsus
**Kind:** drug

## Summary
<2–3 sentence canonical description>

## Key facts
- GLP-1 receptor agonist with extended half-life enabling weekly dosing [[sources/yt-LfRiBJgD7sk]]
- Approved for type 2 diabetes (2017) and chronic weight management (2021) [[sources/pubmed-39847203]]
- ...

## Sources
- [[sources/yt-LfRiBJgD7sk]] — Huberman/Lustig discussion of mechanism
- [[sources/pubmed-39847203]] — 2024 review of clinical outcomes
- ...

## Related
- Concepts: [[concepts/glp1-receptor-agonism]], [[concepts/food-noise]]
- Entities: [[entities/tirzepatide]], [[entities/liraglutide]]
```

Required sections: Summary, Key facts (with citations), Sources, Related.

### 4.2 Concept (`wiki/concepts/<slug>.md`)

An abstract idea that recurs across sources: a mechanism, phenomenon, framework, theory.

```yaml
---
type: concept
slug: food-noise
canonical_name: "Food noise"
aliases: ["food chatter", "food preoccupation"]
domains: ["glp1-reward-modulation"]
created_at: "..."
last_updated: "..."
sources_count: 9
---

# Food noise

**Aliases:** food chatter, food preoccupation

## Summary
<2–3 sentence definition>

## Key claims
- Reduction of food noise is the most consistently reported subjective effect of GLP-1 RAs [[sources/yt-LfRiBJgD7sk#1820]]
- Distinct from broader reward blunting; localized to food-related cognition [[sources/arxiv-2403.12345]]
- ...

## Mechanism
<narrative section, citation per claim>

## Sources
- [[sources/<id>]] — <one-line context>
- ...

## Related
- Concepts: [[concepts/reward-blunting]], [[concepts/anhedonia]]
- Entities: [[entities/semaglutide]], [[entities/glp1-receptor]]
```

Required sections: Summary, Key claims (with citations), Sources, Related. Optional: Mechanism, Open questions, Disagreements.

### 4.3 Source (`wiki/sources/<id>.md`)

One page per ingested source. Summary + key claims + cross-references. Mirror of `raw/<type>/<id>.md` but knowledge-layer. The agent reads this when answering questions; `raw/` is the source of truth for verbatim content.

```yaml
---
type: source
source_id: yt-LfRiBJgD7sk
source_type: youtube
title: "GLP-1 Mechanisms of Action"
domains: ["glp1-reward-modulation"]
ingested_at: "..."
filter_score: 0.92
nlm_corpus_ids: ["nb_abc123"]
---

# GLP-1 Mechanisms of Action

**Source:** [[raw/youtube/yt-LfRiBJgD7sk]] · youtube · [[https://youtube.com/watch?v=LfRiBJgD7sk|original]] · 2024-08-15
**Authors:** Andrew Huberman, Robert Lustig
**Filter:** 0.92 (glp1-v3) — Detailed receptor pharmacology, cites Alhadeff 2012

## Summary
<2–3 sentence summary>

## Key claims
- GLP-1 neurons in the NTS project to the VTA and NAc to control food intake [[sources/yt-LfRiBJgD7sk#1820]]
- ...

## Cross-references
- Updates: [[entities/semaglutide]], [[concepts/food-noise]], [[concepts/reward-blunting]]
- Cites: Alhadeff et al. 2012 (no source page yet — flagged for ingest)
```

Required sections: Summary, Key claims, Cross-references.

### 4.4 Synthesis (`wiki/synthesis/<slug>.md`)

Cross-source narrative analysis. Compounds from queries — when you ask the wiki a question and the answer is good, file it here.

```yaml
---
type: synthesis
slug: glp1-dose-reward-tradeoff
title: "Dose-response tradeoff between weight efficacy and reward blunting"
domains: ["glp1-reward-modulation"]
question: "How does GLP-1 RA dose affect the tradeoff between weight loss efficacy and reward system side effects?"
created_at: "..."
last_updated: "..."
sources_consulted: 18
nlm_artifact: "wiki/artifacts/briefings/2026-04-27-glp1-dose-tradeoff.md"  # optional
nlm_notebook_id: "nb_abc123"
nlm_artifact_url: "https://notebooklm.google.com/notebook/<id>"  # bidirectional link
---

# Dose-response tradeoff between weight efficacy and reward blunting

**Origin question:** How does GLP-1 RA dose affect the tradeoff between weight loss efficacy and reward system side effects?
**Date:** 2026-04-27
**Sources consulted:** 18

## Synthesis
<narrative answer with inline citations>

## Sources cited
- [[sources/<id>]] — <claim/finding from this source>
- ...

## Open questions
- <unresolved>

## NotebookLM artifact
- Local: [[wiki/artifacts/briefings/2026-04-27-glp1-dose-tradeoff]]
- Live: <URL>
```

Required sections: Synthesis, Sources cited. Optional: Open questions, Disagreements, NotebookLM artifact (when applicable).

### 4.5 MOC — Map of Content (`wiki/mocs/<domain>.md`)

One per domain. Curated entry point. Lists key entities, concepts, syntheses, source clusters, open threads.

```yaml
---
type: moc
slug: glp1-reward-modulation
domain: glp1-reward-modulation
last_updated: "..."
---

# GLP-1 Reward Modulation — Map of Content

## Overview
<short framing of the domain, why it matters, current open thesis>

## Key entities
- [[entities/semaglutide]] — GLP-1 RA, weekly dosing
- [[entities/tirzepatide]] — GIP/GLP-1 dual agonist
- ...

## Key concepts
- [[concepts/food-noise]] — distinct from generalized reward
- [[concepts/reward-blunting]] — broader anhedonic effect
- ...

## Synthesis pages
- [[synthesis/glp1-dose-reward-tradeoff]]
- ...

## Source clusters
- Mechanistic neuroscience: <n> sources, mostly arxiv + pubmed
- Clinical practice: <n> sources, mostly youtube interviews
- ...

## Open threads
- Is microdosing dissociable from full-dose effects on reward circuitry?
- ...
```

Required sections: Overview, Key entities, Key concepts, Synthesis pages.

### 4.6 Artifact (`wiki/artifacts/<type>/<slug>.md`)

Wrapper page for NotebookLM-generated outputs (slides, audio, briefings). Holds local file + live link + sources used + bidirectional reference.

```yaml
---
type: artifact
artifact_type: slides | audio | briefing | report
slug: 2026-04-27-glp1-dose-tradeoff-5slide
title: "GLP-1 dose tradeoff — 5 slides"
domain: glp1-reward-modulation
created_at: "..."
nlm_notebook_id: "nb_abc123"
nlm_artifact_id: "<artifact-id-from-nlm>"
nlm_artifact_url: "https://notebooklm.google.com/notebook/<id>/artifact/<aid>"
local_file: "wiki/artifacts/slides/2026-04-27-glp1-dose-tradeoff-5slide.marp.md"
question: "Put together 5 slides on GLP-1 reward system dose response."
---

# GLP-1 dose tradeoff — 5 slides

**Created:** 2026-04-27
**Domain:** glp1-reward-modulation
**Origin question:** Put together 5 slides on GLP-1 reward system dose response.

## Local file
[[wiki/artifacts/slides/2026-04-27-glp1-dose-tradeoff-5slide.marp]]

## NotebookLM (live, editable)
<URL>

## Sources used
- [[sources/yt-LfRiBJgD7sk]]
- [[sources/pubmed-39847203]]
- ...

## Wiki pages this informs
- [[synthesis/glp1-dose-reward-tradeoff]]
- [[concepts/reward-blunting]]
```

Required sections: Local file, NotebookLM (live), Sources used.

## 5. Citation format and rules

### 5.1 Citation primitive

`[[sources/<id>]]` — link to the wiki source page for `<id>`.

For span-level citations, append an anchor:

- YouTube: `[[sources/yt-LfRiBJgD7sk#1820]]` (timestamp in seconds)
- PDF / arXiv: `[[sources/arxiv-2403.12345#p7]]` (page) or `#L142` (line)
- Voice / audiobook: `[[sources/voice-2026-04-27#312]]` (seconds)
- PubMed (text): `[[sources/pubmed-39847203#para3]]` (paragraph)
- Web: `[[sources/web-2026-04-27-3a9f#para3]]`

### 5.2 Citation grounding rule

Every claim in entity, concept, source, and synthesis pages must be followed by at least one citation. Validator rejects pages that fail in normal mode. In draft mode (`--draft` flag on gateway writes; `draft: true` in page frontmatter), the rule is downgraded to a lint warning so an agent can write a partial draft and refine citations later. See § 5.5 for the draft lifecycle. Examples of "claim" subject to the rule:

- Statement of fact about the world ("GLP-1 binds receptor X")
- Statement of empirical finding ("Trial Y showed Z")
- Statement of mechanism ("Mechanism A causes B")
- Quoted or paraphrased view from a source

Examples NOT subject to the rule:

- Page metadata in frontmatter
- Section headers
- Cross-reference lists ("Related concepts: ...")
- Open questions (which are *un*answered claims)

### 5.3 Citation density

Lint warns when claim-density-per-citation exceeds threshold (configurable, default: more than 2 consecutive claim-shaped sentences without a citation).

### 5.4 Bidirectional integrity

When an agent updates a wiki page to cite source `<id>`, the gateway also updates `raw/<type>/<id>.md` frontmatter `wiki_pages:` to include the wiki page path. Backlink integrity is enforced — broken in either direction triggers lint.

### 5.5 Draft mode and lifecycle

Draft mode lets an agent commit a page with incomplete citations. It applies to entity, concept, source, and synthesis pages — the four types subject to the citation grounding rule. MOC and artifact pages have no draft mode (they have nothing to soften).

**Entering draft mode.** Pass `--draft` to a gateway write operation (`wiki ingest --draft`, `wiki query --draft`, `wiki nlm-* --draft`). The gateway sets `draft: true` in the page frontmatter and adds a `draft_started_at` ISO datetime. The validator downgrades the citation grounding rule from rejection to warning. All other validator rules (frontmatter shape, link resolution, slug uniqueness, source immutability, page-shape, plan-before-write) remain hard rejections — drafts are *partial* not *unstructured*.

**While in draft mode.** Subsequent writes to the same page may be done in either mode. Lint reports list drafts and the count of unresolved claim sentences. Drafts older than the staleness threshold (default 7 days; configurable per domain) are surfaced in lint as `stale_drafts`.

**Finalizing.** `wiki finalize <page-path>` re-runs the full validator with the citation rule restored to rejection. If validation passes, the gateway clears `draft: true` and `draft_started_at`, sets `finalized_at`, and logs the transition. If validation fails, the page stays in draft and the operation returns the failing rule(s).

**Forced abandonment.** `wiki finalize <page-path> --abandon` deletes the draft page and removes its backlinks. Logged.

**Frontmatter shape during draft:**

```yaml
draft: true
draft_started_at: "2026-04-27T18:30:00Z"
draft_unresolved_claims: 4   # set by validator on each write
```

After finalize:

```yaml
finalized_at: "2026-04-29T10:15:00Z"
# draft, draft_started_at, draft_unresolved_claims removed
```

**Visibility rules.** Draft pages are searchable, linkable, and lintable like any other page. They appear in `index.md` with a `[draft]` marker. Cross-references *to* a draft page are allowed; cross-references *from* a draft are also allowed. Synthesis pages may cite drafts (the citation grounds in the draft, not in the source — caller's risk).

## 6. Slug conventions

### 6.1 Source IDs (`raw/<type>/<id>.md`)

Stable, type-prefixed, short. Never derived from titles (titles change; IDs must not).

| Type | ID format | Example |
|---|---|---|
| youtube | `yt-<videoId>` | `yt-LfRiBJgD7sk` |
| arxiv | `arxiv-<arxiv_id>` (dot preserved) | `arxiv-2403.12345` |
| pubmed | `pubmed-<pmid>` | `pubmed-39847203` |
| pdf | `pdf-<author-year-shortname>` | `pdf-kaufmann-2024-incretin` |
| web | `web-<YYYY-MM-DD>-<3-char-hash>` | `web-2026-04-27-3a9` |
| voice | `voice-<YYYY-MM-DDThhmm>` | `voice-2026-04-27T1432` |
| audiobook | `audio-<asin-or-shortname>` | `audio-thinking-fast-slow` |
| note | `note-<source-app>-<remote-id-or-hash>` | `note-apple-A1B2` |
| csv | `csv-<sha256-prefix-12>` | `csv-3a9f8e2b1c4d` |

### 6.2 Wiki entity / concept slugs

Lowercase, hyphenated, semantic. Match canonical name. Example: canonical name "Nucleus accumbens" → slug `nucleus-accumbens`.

The validator runs a Levenshtein-distance check against existing slugs at create time. New slugs within distance 2 of an existing slug raise a warning ("did you mean to update [[concepts/food-noise]] instead of creating [[concepts/food_noise_phenomenon]]?"). Override requires explicit `--force-new-slug` flag, which is logged.

### 6.3 Synthesis slugs

Lowercase, hyphenated, scoped to domain when the synthesis is domain-specific: `glp1-dose-reward-tradeoff`, not `dose-reward-tradeoff`. Cross-domain synthesis uses the bare topic.

### 6.4 Artifact slugs

`<YYYY-MM-DD>-<short-topic>-<artifact-type-suffix>`: `2026-04-27-glp1-dose-tradeoff-5slide`.

## 7. `index.md` format

Content-oriented catalog. Rebuilt by `wiki index --rebuild` after every batch ingest and on demand.

```markdown
# Knowledge Index

Last rebuilt: 2026-04-27T18:30:00Z
Sources: 254 | Entities: 87 | Concepts: 53 | Synthesis: 14 | Artifacts: 9

## Domains

### glp1-reward-modulation
[[mocs/glp1-reward-modulation]] · 127 sources

- Entities: [[entities/semaglutide]] · [[entities/tirzepatide]] · [[entities/liraglutide]] · ...
- Concepts: [[concepts/food-noise]] · [[concepts/reward-blunting]] · [[concepts/glp1-receptor-agonism]] · ...
- Synthesis: [[synthesis/glp1-dose-reward-tradeoff]] · ...
- Artifacts: [[artifacts/slides/2026-04-27-glp1-dose-tradeoff-5slide]] · ...

### ai-temporal-video
[[mocs/ai-temporal-video]] · 104 sources
...

## Cross-domain
- Synthesis: [[synthesis/<slug>]]
- Concepts: [[concepts/<slug>]] (used in domains X, Y)

## Health
- Orphans: 3 — see `wiki lint --orphans`
- Untriaged inbox: 7 — see `raw/inbox/`
- Pending NotebookLM corpus syncs: 2

## Recent activity
(Last 20 lines from `log.md`)
```

The agent reads `index.md` first to orient on a query before drilling into specific pages.

## 8. `log.md` format

Append-only chronological record. Grep-friendly entry prefix: `## [<ISO-datetime>] <op> | <key=value>... | <one-line summary>`.

```markdown
# Knowledge Log

## [2026-04-27T15:30:00Z] ingest | id=yt-LfRiBJgD7sk | filter=0.92 | domain=glp1-reward-modulation | pages_touched=12
Plan: created [[entities/glp1-receptor]]; updated [[concepts/food-noise]], [[concepts/dose-response]]; filed [[sources/yt-LfRiBJgD7sk]]; added to nb_abc123.

## [2026-04-27T16:00:00Z] query | scope=glp1-reward-modulation | nlm_invoked=true | sources_consulted=18
Question: "How does dose affect reward blunting?"
Result: [[synthesis/glp1-dose-reward-tradeoff]]

## [2026-04-27T17:00:00Z] nlm-slides | domain=glp1-reward-modulation | artifact=2026-04-27-glp1-dose-tradeoff-5slide
Filed: [[artifacts/slides/2026-04-27-glp1-dose-tradeoff-5slide]]

## [2026-04-27T18:00:00Z] lint | orphans=3 | contradictions=0 | citation_density_warnings=2 | duplicate_slug_warnings=0
Report: .knowledge/lint/2026-04-27T18-00-00Z.md

## [2026-04-27T18:15:00Z] filter-correction | id=web-2026-04-25-7c2 | original_score=0.42 | corrected=include | rationale="Author cites primary literature; misjudged on first read"
Pinned to .knowledge/policies/glp1-reward-modulation/examples/.
```

Tail-friendly: `grep "^## \[" log.md | tail -20`. Entry types listed in § 9.

## 9. Gateway operations (CLI + MCP)

Single Python backend; two thin surfaces. CLI for cron, scripts, research-notebook pipelines. MCP for in-session Claude Code agents. Same operation set, same return shapes.

### 9.1 Operations

| Operation | CLI | MCP tool |
|---|---|---|
| Ingest single source | `wiki ingest <path-or-url>` | `wiki_ingest` |
| Batch ingest from research-notebook | `wiki batch-ingest <domain-config>` | `wiki_batch_ingest` |
| Query the wiki | `wiki query "<question>" [--scope <domain>]` | `wiki_query` |
| Run filter on a candidate (read-only) | `wiki filter <path> [--domain <slug>]` | `wiki_filter` |
| Add source to NotebookLM corpus | `wiki nlm-add <domain> <source-id>` | `wiki_nlm_add` |
| Generate slide deck | `wiki nlm-slides <domain> "<topic>"` | `wiki_nlm_slides` |
| Generate audio overview | `wiki nlm-audio <domain> "<topic>"` | `wiki_nlm_audio` |
| Generate briefing doc | `wiki nlm-briefing <domain>` | `wiki_nlm_briefing` |
| Revise an artifact | `wiki nlm-revise <artifact-id> "<instructions>"` | `wiki_nlm_revise` |
| Lint | `wiki lint [--scope <area>]` | `wiki_lint` |
| Rebuild index | `wiki index --rebuild` | `wiki_index_rebuild` |
| Search | `wiki search "<query>" [--scope wiki|raw|all]` | `wiki_search` |
| Status | `wiki status` | `wiki_status` |
| Filter correction | `wiki filter-correct <source-id> --include\|--exclude --rationale "<why>"` | `wiki_filter_correct` |
| Finalize a draft | `wiki finalize <page-path> [--abandon]` | `wiki_finalize` |
| Bootstrap a new domain (top-down) | `wiki bootstrap-domain "<description>" <slug> [--force]` | (CLI only) |
| Discover candidate domains (bottom-up) | `wiki discover-domains [--scope GLOB] [--since DATE] [--untagged]` | (CLI only) |
| Promote a draft proposal | `wiki promote-domain <proposal-slug>` | (CLI only) |
| Demote a promoted domain | `wiki demote-domain <domain-slug>` | (CLI only) |
| Reject a draft proposal | `wiki reject-proposal <proposal-slug>` | (CLI only) |
| Multi-adapter research | `wiki research "<prompt>" [--domain X] [--review] [--execute ID]` | (CLI only) |
| Migrate frontmatter | `wiki migrate <migration-name>` | (CLI only) |

### 9.2 Operation contract (every operation)

1. Validate inputs against the schema.
2. Acquire write lock if writing (file lock under `.knowledge/locks/`).
3. Execute (call NotebookLM, run filter, generate content, etc.).
4. Validate outputs (frontmatter shape, citation grounding, link resolution, schema compliance). In draft mode (`--draft`), citation grounding is downgraded to a warning; all other rules remain hard rejections.
5. Apply writes atomically (temp file → rename).
6. Update backlinks (`wiki_pages` in raw frontmatter; `index.md` if a new page was created).
7. Append `log.md` entry. Draft entries marked `draft=true`.
8. Release lock.
9. Return structured result (paths touched, IDs created, score, draft status, errors, warnings).

Failed validation → no writes commit, agent gets a structured rejection with the rule violated.

### 9.3 The Discipline Gate

The `wiki nlm-*` family are the only sanctioned NotebookLM entry points. Each one:

1. Calls NotebookLM (query, generate, revise).
2. Downloads the artifact into `wiki/artifacts/<type>/`.
3. Writes a wiki artifact page with bidirectional link.
4. Updates referenced source pages' `wiki_pages:` frontmatter.
5. Logs to `log.md`.

Agents must not call `nlm` CLI or NotebookLM MCP tools directly. The schema doc forbids it; CI greps for violations in committed wiki content.

## 10. Filter and learning

### 10.1 Editorial policy

Per-domain YAML at `.knowledge/policies/<domain>/policy.yaml`. Versioned by Git; archived versions in `policy_versions/`. Schema follows research-notebook's existing pattern (inclusion criteria, exclusion criteria, quality signals: channel/speaker/methodology/venue), extended with:

```yaml
version: v1
policy_schema_version: 1   # added M39; lenient validator allows missing for legacy
domain:
  slug: glp1-reward-modulation
  topic: "GLP-1 receptor agonist effects on reward system and dosing optimization"
  field: "neuroendocrinology and obesity pharmacology"
  description: >
    ...

filter:
  threshold_include: 0.70    # ≥ this, source enters wiki
  threshold_review: 0.50     # between thresholds, queue for human review
                             # < threshold_review, exclude with rationale
  example_count_in_prompt: 12  # how many representative examples to pin
  example_strategy: "balanced" # balanced | recent | corrections-weighted

inclusion_criteria: [...]
exclusion_criteria: [...]
quality_signals:
  channel_authority: {...}
  speaker_expertise: {...}
  content_depth: {...}
  publication_venue: {...}
  methodology_rigor: {...}
```

Three authorship paths produce a `policy.yaml`:

1. **`wiki bootstrap-domain "<description>" <slug>`** (M39, top-down) — Claude drafts the full policy from a natural-language description; output passes the strict validator (≥3 inclusion criteria, ≥1 exclusion, ≥2 quality_signals categories with ≥2 signals each).
2. **`wiki promote-domain <proposal-slug>`** (M36, bottom-up) — minimal policy with empty criteria, marked `auto_generated_from_proposal: true`. User hand-edits or re-bootstraps with `--force` after running `demote-domain`.
3. **Hand-authored** — write the YAML directly. Validator runs in lenient mode on load, so this works even without `policy_schema_version`.

The strict validator (`gateway.ops.policy_validator`) runs only on `bootstrap-domain` output. Existing policies — including legacy auto-generated ones — load through the lenient path without modification.

### 10.2 Example bank

`.knowledge/policies/<domain>/examples/<source-id>.yaml`. One file per pinned example. Schema:

```yaml
source_id: yt-LfRiBJgD7sk
domain: glp1-reward-modulation
decision: include | exclude
score: 0.92
policy_version: glp1-v3
rationale: "<why this decision is correct>"
pinned_at: "2026-04-27T18:15:00Z"
pinned_by: "user-correction" | "high-confidence" | "edge-case"
frontmatter_snapshot:
  type: youtube
  title: "..."
  authors: [...]
  meta: {...}
content_excerpt: "<first 500 chars of source body>"
```

The filter prompt loads `policy.yaml` plus `example_count_in_prompt` examples from the bank, selected per `example_strategy`. Default strategy: 4 corrections + 4 high-confidence includes + 4 high-confidence excludes, biased toward recency.

### 10.3 Filter call contract

Inputs: source path (raw markdown with frontmatter — body may be truncated to first ~4k tokens for cost), domain slug.

Outputs: `{score, rationale, policy_version, decided_at}` written into source frontmatter `filter:` block.

User correction via `wiki filter-correct <source-id>` updates the source's `filter.user_correction` and pins the corrected example to the bank.

### 10.4 Fine-tuning roadmap

Trigger: ~500–1000 high-quality decisions per domain in the example bank.

Output options (decide at trigger time):

- A small fine-tuned classifier (open-weight, e.g., Llama-3-8B-class) deployed locally, replacing the prompt-based filter.
- A distilled prompt extracted from accumulated examples — same Claude call, smaller and tighter.

Required infrastructure:

- Held-out evaluation set (separate examples not used in training).
- Periodic regression test: re-score held-out set with current filter; compare to historical decisions; flag drift.
- Same `wiki filter` interface so callers don't change.

Until the trigger fires, the filter remains prompt-based with the example bank.

## 11. Validator rules

Runs on every gateway write. Rejection halts the operation; nothing commits.

### 11.1 Frontmatter rules

- Required core fields present and well-typed.
- `type` is in the allowed enum.
- `id` matches type-specific format (§ 6.1).
- `id` is unique across `raw/` (collision check via index).
- `content_hash` matches body SHA-256.
- `ingested_at` is ISO-8601 UTC.
- `meta` matches type-specific schema (§ 3.2).
- Wiki pages: `type` matches directory location (page in `wiki/entities/` must have `type: entity`).

### 11.2 Citation rules

- Every claim sentence in entity / concept / source / synthesis pages is followed by `[[sources/<id>]]` (or anchored variant). In draft mode (`draft: true`), this rule is downgraded to a warning surfaced in lint; all other citation rules remain hard rejections.
- Citation targets resolve to existing wiki source pages (which themselves resolve to existing `raw/` files).
- Bidirectional backlink integrity: every citation in a wiki page is reflected in the cited source's `wiki_pages` frontmatter.

### 11.3 Slug rules

- Slug uniqueness within page type.
- Levenshtein-distance check against existing slugs (warning at distance ≤ 2; override requires `--force-new-slug`).
- Slug format (lowercase, hyphenated, no spaces, ASCII).

### 11.4 Page-shape rules

- Required sections per page type (§ 4) present and non-empty.
- No empty placeholder text (`<...>`, `TODO`, `TBD`) in committed content.

### 11.5 Source immutability

- Source body content (everything after frontmatter) cannot change after ingest. Frontmatter mutations are restricted to the `filter:`, `nlm_corpus_ids:`, `wiki_pages:`, `domains:` fields.

### 11.6 Plan-before-write

- Incremental ingest gateway calls require a `plan:` field in the call (list of pages to create + pages to update + cross-references). Plan is logged to `log.md`. Missing plan → rejection.

## 12. Lint operations

Runs after every ingest (cheap checks) and on demand (full pass). Output: `.knowledge/lint/<timestamp>.md` plus `log.md` entry.

### 12.1 Cheap checks (post-every-ingest)

- Broken wikilinks (target page does not exist).
- Frontmatter schema violations (in case of out-of-band edits).
- Source immutability violations.
- Backlink integrity.

### 12.2 Full lint pass (on demand or scheduled weekly)

- **Orphans**: wiki pages with no inbound `[[wikilinks]]` from any other wiki page. Lists for review; does not auto-delete.
- **Stale claims**: wiki claims whose cited source has been superseded by a newer source on the same topic (flagged by entity overlap + recency).
- **Stale drafts**: pages with `draft: true` older than the staleness threshold (default 7 days, configurable per domain). Listed with age and unresolved claim count to drive `wiki finalize` decisions.
- **Contradictions**: LLM-driven scan for contradictory claims across wiki pages, scoped per domain. Returns pairs with offending sentences and source citations.
- **Missing entities/concepts**: terms appearing in 3+ wiki pages without a dedicated entity/concept page.
- **Citation density**: pages exceeding the threshold (§ 5.3). In normal mode, also surfaces unresolved-claim count for drafts.
- **Schema drift**: frontmatter fields not in schema; page sections not matching template.
- **Filter calibration**: random sample of past filter decisions re-scored against current policy version; deltas above threshold flagged.
- **Untriaged inbox**: count of files in `raw/inbox/` waiting for routing.
- **Pending NotebookLM syncs**: sources with `filter.score >= threshold_include` for a domain that has a NotebookLM corpus, but `nlm_corpus_ids` does not include that corpus.

### 12.3 Lint output

```markdown
# Lint Report — 2026-04-27T18:00:00Z

## Summary
- Orphans: 3
- Stale claims: 1
- Stale drafts: 2 (oldest: 11 days)
- Contradictions: 0
- Missing entities: 2
- Citation density warnings: 2
- Schema drift: 0
- Filter calibration drift: 0.04 mean delta (within threshold)
- Untriaged inbox: 7
- Pending NotebookLM syncs: 2

## Details
[per-category, with file paths and remediation suggestions]
```

## 13. NotebookLM integration

### 13.1 Notebook ↔ domain map (`nlm/notebooks.yaml`)

```yaml
notebooks:
  glp1-reward-modulation:
    notebook_id: nb_abc123
    created_at: "2025-..."
    sources_count: 127
    last_sync: "2026-04-27T15:30:00Z"
  ai-temporal-video:
    notebook_id: nb_def456
    ...
```

### 13.2 Sync contract

Source belongs in NotebookLM corpus iff:

- `filter.score >= threshold_include` for the corpus's domain
- domain is listed in source's `domains:`
- corpus accepts the source's `type` (some types may be excluded — voice notes, journal entries — by per-corpus policy)

`wiki nlm-add` enforces this and records `nlm_corpus_ids:` back to the source.

### 13.3 Artifact lifecycle

Every NotebookLM-generated artifact (audio, slides, briefing, report) is wrapped in a wiki artifact page (§ 4.6). The artifact page is the canonical reference. The live NotebookLM URL is recorded for editing/revising. `wiki nlm-revise` updates both the local file and the wiki page; old versions are kept under git history.

## 14. Forward-looking notes

### 14.1 API-only-source pollers

Apple Notes, Notion, Slack, Gmail, etc. — content not available as a watchable filesystem. Each gets a poller that:

1. Runs on a schedule (launchd / cron).
2. Queries the source API for new content since last sync (cursor stored under `.knowledge/pollers/<source>/cursor.yaml`).
3. Converts each item to canonical markdown + frontmatter.
4. Writes to `raw/note/note-<source>-<remote-id>.md`.

The watcher picks up from there. No pipeline changes. New source types are additive.

### 14.2 qmd or similar (BM25/vector index)

When the wiki crosses ~10k pages (or fuzzy search starts feeling slow), drop in qmd or equivalent. The markdown remains canonical; the index is derived state. Migration: zero — the index reads the existing files. Update `wiki search` to delegate to qmd; CLI/MCP surface unchanged.

### 14.3 Migration from research-notebook legacy vaults

`~/code/research-notebook/data/obsidian/` and `data/obsidian_glp1/` contain real wiki content from the AI-temporal-video and GLP-1-reward-modulation domains. Migration plan is separate work. Until done:

- Legacy vaults remain authoritative for their domains.
- New ingests for those domains write to the new canonical wiki at `~/code/knowledge/`.
- Migration script will:
  - Convert legacy source notes into canonical `wiki/sources/` pages.
  - Convert legacy concept/synthesis/MOC pages to canonical schema (slug normalization, frontmatter migration, citation reformat).
  - Build the `raw/` representations from existing JSON checkpoints in `data/staged/`.
  - Backfill the example bank with high-confidence past decisions.

### 14.4 Cross-project reads

Agents in other `~/code/*` projects read the wiki by absolute path. No special interface required. Recommended pattern:

```python
# in any project
KNOWLEDGE = Path.home() / "code" / "knowledge"
moc = (KNOWLEDGE / "wiki" / "mocs" / f"{domain}.md").read_text()
```

For cross-project queries, projects shell out to `wiki query` or call the MCP tool. Wiki contents must never be copied into other project repos — always reference by path or query through the gateway.

### 14.5 Schema evolution

When this document changes, run `wiki migrate <name>` to apply backfill scripts to existing content. Migrations are scripts under `~/code/knowledge/migrations/<NNNN>-<name>.py` (numbered, idempotent). Each migration:

- Updates frontmatter in raw/ and wiki/ in place.
- Updates `WIKI.md` with the new schema.
- Logs to `log.md`.

Schema is versioned via a `schema_version` field at the top of `WIKI.md` (TBD on first migration).
