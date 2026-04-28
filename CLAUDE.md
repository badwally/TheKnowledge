# ~/code/knowledge/ — Personal Knowledge Base

Canonical knowledge base for all `~/code/*` projects. Implements the LLM Wiki pattern (Karpathy gist `442a6bf555914893e9891c11519de94f`) with a hybrid synthesis substrate — wiki canonical, NotebookLM as a synthesis service behind a gateway.

This file is the agent control surface. `WIKI.md` is the conventions reference. Read `WIKI.md` before designing converters, page types, gateway operations, validator rules, or editorial policies. Read `index.md` first to orient on content.

## What you may do here

- Read any file in `wiki/`, `raw/`, `nlm/`, `index.md`, `log.md`. Reading is unrestricted.
- Propose wiki updates and source ingests **only via the gateway** — never write directly to `wiki/` or `raw/`.
- Read sources to answer questions, then file good answers back into the wiki via `wiki query`, which writes the answer as a wiki page.
- Cite into the wiki from any other `~/code/*` project — wiki paths are stable references.

## Hard rules (no exceptions)

1. **No direct writes to `wiki/` or `raw/`.** All writes go through the gateway: `wiki <subcommand>` (CLI) or `wiki_*` (MCP). Direct file writes are caught by the validator and `git diff` review.
2. **No direct calls to `nlm` or NotebookLM MCP tools.** All NotebookLM operations go through the gateway. The gateway guarantees every NotebookLM artifact is filed back to the wiki with bidirectional links — Discipline Gate.
3. **Citation grounding is mandatory.** Every claim in every wiki page must be followed by `[[sources/<id>]]` linking to the source page. Validator rejects pages with claims lacking provenance. Exception: pages written with `--draft` are committed with `draft: true` and the rule is downgraded to a lint warning until `wiki finalize` is run. Drafts older than 7 days are flagged in lint.
4. **Lookup before create.** Search `index.md` and existing pages before creating a new entity or concept. Validator warns on slug similarity.
5. **Plan before write.** For any incremental ingest, produce a written plan in your response: pages you will create, pages you will update, cross-references you will add. Gateway logs the plan to `log.md`.
6. **Sources in `raw/` are immutable.** Frontmatter may be updated by pipeline stages (filter score, NotebookLM corpus IDs, wiki backlinks). Body content is never modified after ingest.

## When to use which authorship path

| Situation | Path |
|---|---|
| Single source, low-stakes (Web Clipper, voice note, ad-hoc PDF) | Incremental, agent-driven via `wiki ingest` |
| New research domain with 50+ sources, citation fidelity required, output will be referenced externally | Batch, code-driven via `wiki batch-ingest` |
| Unsure | Batch. Fidelity > convenience. |

## Operation guide

| Task | Command |
|---|---|
| Ingest single source | `wiki ingest <path-or-url>` |
| Ingest research domain (batch) | `wiki batch-ingest <domain-config>` |
| Query the wiki | `wiki query "<question>"` |
| Generate slides from corpus | `wiki nlm-slides <domain> "<topic>"` |
| Generate audio overview | `wiki nlm-audio <domain> "<topic>"` |
| Generate briefing doc | `wiki nlm-briefing <domain>` |
| Revise an artifact | `wiki nlm-revise <artifact-id> "<instructions>"` |
| Run filter on a source | `wiki filter <path>` |
| Finalize a draft page | `wiki finalize <page-path>` (`--abandon` to delete) |
| Health check | `wiki lint` |
| Rebuild index | `wiki index --rebuild` |
| Search wiki + raw | `wiki search "<query>"` |
| Status / pending queue | `wiki status` |

Full reference: `WIKI.md` § Gateway operations.

## Adding a new source type

Write a converter under `~/code/research-notebook/src/search/` that outputs canonical markdown to `raw/<type>/<slug>.md` per the frontmatter schema in `WIKI.md`. No pipeline changes required. Pollers (for API-only sources like Apple Notes, Notion) follow the same contract — they write to `raw/` on a schedule.

## Where things live

```
~/code/knowledge/
├── CLAUDE.md          # this file
├── WIKI.md            # conventions reference
├── index.md           # content index — read first to orient
├── log.md             # chronological event log, append-only
├── raw/               # immutable sources (markdown + frontmatter, optional sidecars)
├── wiki/              # LLM-authored knowledge layer
│   ├── entities/      # drugs, people, papers, organizations
│   ├── concepts/      # food-noise, reward-blunting, etc.
│   ├── sources/       # one summary page per ingested source
│   ├── synthesis/     # cross-source analyses (compound from queries)
│   ├── mocs/          # maps of content per domain
│   └── artifacts/     # NotebookLM-generated outputs (slides, audio, briefings)
└── nlm/
    └── notebooks.yaml # domain ↔ NotebookLM notebook ID map
```

## Forward-looking notes

- **API-only-source pollers** (Apple Notes, Notion, Slack, Gmail) get bolt-on schedulers writing to `raw/<source>/` in the canonical format. Same downstream pipeline.
- **Fine-tuning loop for the semantic filter** is on the roadmap. Trigger threshold ~500–1000 high-quality decisions per domain. Output: small fine-tuned classifier or distilled prompt extracted from accumulated examples. Replaces the prompt-based filter behind the same CLI/MCP interface. See `WIKI.md` § Filter and learning.
- **qmd or similar BM25/vector index** gets dropped in if/when the wiki crosses ~10k pages. Markdown remains canonical; the index is derived state.
- **Existing legacy vaults** (`~/code/research-notebook/data/obsidian/` and `data/obsidian_glp1/`) need migration into this canonical schema. Migration plan is separate work; until done, those vaults remain authoritative for their domains.

## When to consult `WIKI.md`

Before: writing or evolving frontmatter, creating a new page type, designing a converter, modifying gateway operations, updating the validator, evolving an editorial policy, designing a lint pass.
