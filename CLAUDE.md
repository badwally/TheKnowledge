# ~/code/knowledge/ — Personal Knowledge Base

Canonical knowledge base for all `~/code/*` projects. Implements the LLM Wiki pattern (Karpathy gist `442a6bf555914893e9891c11519de94f`) with three load-bearing integrations:

- The **wiki** (this repo) is canonical — markdown + YAML frontmatter, citation-graph enforced by the gateway.
- **NotebookLM** is the heavy-synthesis service called *through* the gateway (`wiki nlm-*`); artifacts file back to `wiki/artifacts/`.
- **Obsidian** is the knowledge-graph visualization engine on top of the vault — same wikilink format, same markdown.

This file is the agent control surface. `WIKI.md` is the conventions reference. Read `WIKI.md` before designing converters, page types, gateway operations, validator rules, or editorial policies. Read `index.md` and run `wiki status` to orient on live content. For human-facing usage, read `TUTORIAL.md`. For per-milestone delivery history, read `BUILD.md § 9`.

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
| Ingest single source (URL, PDF, audio, m4b) | `wiki ingest <path-or-url> [--domain X] [--with-plan] [--draft]` |
| Ingest a whole vault | `wiki batch-ingest <vault> --legacy-import --domain <slug>` |
| Query the wiki and file a synthesis | `wiki query "<question>" [--domain X] [--draft]` |
| Generate slides from corpus | `wiki nlm-slides <domain> "<topic>"` |
| Generate audio overview | `wiki nlm-audio <domain> "<topic>"` |
| Generate briefing doc | `wiki nlm-briefing <domain>` |
| Revise an artifact | `wiki nlm-revise <slug> --slide N "<instructions>"` |
| Add a source to a NotebookLM corpus | `wiki nlm-add <domain> <source-id>` |
| Bulk-sync every raw source tagged with a domain into its corpus | `wiki nlm-sync <domain> [--limit N] [--dry-run]` |
| Run filter on a source | `wiki filter <path>` |
| Pin a corrected filter decision | `wiki filter-correct <id>` |
| Finalize a draft page | `wiki finalize <page-path>` (`--abandon` to delete) |
| Backfill policy + example bank from legacy | `wiki backfill-examples --domain X --legacy-config <yaml> --json <staged.json>` |
| Inspect / distill the example bank | `wiki finetune [--check \| --domain X --distill [--force]]` |
| Bootstrap a new domain from a natural-language description | `wiki bootstrap-domain "<description>" <slug>` |
| Discover candidate domains in an unsorted corpus | `wiki discover-domains [--scope GLOB] [--since DATE] [--untagged]` |
| Bless a draft proposal as a real domain | `wiki promote-domain <proposal-slug>` |
| Reverse a promotion (undo policy + back-tags) | `wiki demote-domain <domain-slug>` |
| Delete a draft proposal | `wiki reject-proposal <proposal-slug>` |
| Multi-adapter research search | `wiki research "<prompt>" [--domain X] [--review] [--execute ID]` |
| Start the local web UI (FastAPI + React) | `wiki serve [--port 7474] [--bind 127.0.0.1]` (visit `/research`, `/review`, `/domains/artifacts`) |
| Run a registered poller (e.g. Apple Notes) | `wiki poll <name>` (`wiki poll --list` to see registered) |
| Health check | `wiki lint [--scope <check>]` |
| Status / watcher heartbeat / pending queue | `wiki status` |

`wiki index --rebuild`, `wiki search`, `wiki migrate <name>` remain stubs (operational sugar). Full reference: `WIKI.md` § Gateway operations.

## Adding a new source type

Write a converter under `src/gateway/converters/<type>.py` that outputs canonical markdown to `raw/<type>/<slug>.md` per the frontmatter schema in `WIKI.md`. Six steps lock the pattern (M29 onward):

1. Add the type string to `paths.SOURCE_TYPES`
2. Add it to `validator.ALLOWED_SOURCE_TYPES` and define an `ID_PATTERNS` regex
3. Implement the converter as a `Converter` subclass with `detect()` + `convert()`
4. Register it in `gateway.converters.__init__._ensure_registered`
5. Update `WIKI.md` § 3.1 (type enum), § 3.2 (meta block), § 6.1 (ID format)
6. Tests at `tests/gateway/test_converters_<type>.py` (mirror an existing converter's shape)

No pipeline changes required.

Source types currently supported: `web`, `youtube`, `arxiv`, `pubmed`, `pdf`, `voice`, `audiobook`, `note`, `csv`, `docx`, `xlsx`, `pptx`, `image`.

Pollers (API-only sources without a watchable filesystem — Apple Notes, Notion, Slack, Gmail) follow a parallel contract under `src/gateway/pollers/<name>.py`: subclass `Poller`, implement `run()`, register in `pollers.__init__._REGISTRY`. Pollers write canonical markdown to `raw/<type>/` on a schedule (or on-demand via `wiki poll <name>`); the watcher / `wiki ingest` picks up from there.

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
│   ├── proposals/     # domain proposals from discover-domains (draft → blessed → promoted)
│   └── artifacts/     # NotebookLM-generated outputs (slides, audio, briefings)
└── nlm/
    ├── notebooks.yaml # domain ↔ NotebookLM notebook ID map
    ├── query_plans/   # persistent per-session research query plans
    └── source_maps/   # NLM title → source-id resolution maps
```

## Forward-looking notes

- **API-only-source pollers.** Apple Notes shipped (M34). Notion, Slack, Gmail queued. All bolt onto the same downstream pipeline — pollers only produce canonical markdown in `raw/`.
- **Filter fine-tuning loop** is shipped: trigger detection + distilled-prompt extraction (`wiki finetune`). Default threshold is 500 high-quality decisions per domain. Open-weight classifier fine-tune (the second WIKI § 10.4 option) is deferred until a domain crosses ~1000 decisions.
- **qmd or similar BM25/vector index** gets dropped in if/when the wiki crosses ~10k pages. Markdown remains canonical; the index is derived state.
- **Legacy migration** (M11–M14) is the only path that imports research-notebook Obsidian vaults. The vaults at `~/code/research-notebook/data/obsidian*/` are read-only inputs to the migrate script.
- **Source-orphan tail** discharges via `wiki query` synthesis loops, not manual claim extraction. Each query produces a draft synthesis page citing N sources via `[[sources/<id>]]`. Run `wiki lint --scope orphans` to see how many sources still lack inbound citations.

## Session-state discipline

`docs/session-state.md` is load-bearing. It records open contracts, in-flight edits, session decisions, and the next atomic step across context compactions and session boundaries.

**Rules (no exceptions):**

- Before any plan-or-write action in a new session, re-read `docs/session-state.md` if its mtime is newer than the current chat's earliest user message. Verify each `## Open contract` and `## File mid-edit` against the working tree. Flag any disagreement to the user before proceeding.
- At natural seams — end of milestone, before merging to main, before any refactor touching the validator or gateway choke-point — checkpoint proactively. Do not wait for the PreCompact hook.
- The PreCompact hook writes a templated instruction to stdout; the agent responds by writing `docs/session-state.md` and committing it. Never edit the file manually except to mark a section `RESOLVED` when an open contract closes.
- At the end of every milestone, diff `docs/session-state.md` predictions against `git diff` and `pytest` output. Any disagreement is a quality incident — investigate before tagging.
- **Do not load `log.md` or `index.md` wholesale into any LLM prompt.** Both files are unbounded in size. `log.md` may be read as a display aggregate (last N entries via `_tail_log_entries`); `index.md` is reference-only. If gateway code needs to build LLM context from wiki content, use `evaluate.wiki_context.load_wiki_context()` or `ops.context_op.context_op()` — never raw file reads of these two files.

## When to consult `WIKI.md`

Before: writing or evolving frontmatter, creating a new page type, designing a converter, modifying gateway operations, updating the validator, evolving an editorial policy, designing a lint pass.
