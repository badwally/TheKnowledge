# ~/code/knowledge/

A personal knowledge base. Sources land as markdown + YAML on the local filesystem. Ranked retrieval (`wiki retrieve`) returns bounded, cited context blocks; queries return cited synthesis pages. NotebookLM artifacts file back to the same vault. Obsidian renders the citation graph.

Implements the LLM Wiki pattern (Karpathy gist `442a6bf555914893e9891c11519de94f`).

## New here?

Pick the track that matches your goal.

**A. Doing knowledge work** (ingesting sources, querying, browsing)

1. [TUTORIAL.md](TUTORIAL.md) — workflow walkthrough; after this you can ingest a source and run a query end-to-end.
2. `wiki --help` and `wiki <subcommand> --help` — flags and usage examples for every op.
3. [WIKI.md](WIKI.md) § 1–2 — terminology and the page-type schema; after this you can read any wiki page and understand its frontmatter.

**B. Contributing code** (adding converters, ops, lint checks, tests)

1. [CLAUDE.md](CLAUDE.md) — agent control surface, hard rules, operation guide; after this you know what you may and may not do directly.
2. [WIKI.md](WIKI.md) — full conventions reference; after this you can add a new source type or gateway op without breaking the validator.
3. [BUILD.md](BUILD.md) § 9–10 — per-milestone delivery record; after this you understand what shipped and in what order.
4. [GLOSSARY.md](GLOSSARY.md) — one-line definitions for every term used in code, docs, and commit messages.
5. `pytest -x` to confirm your environment is green before touching anything.

**C. Agents being briefed** (Claude Code, MCP clients, automation)

1. [CLAUDE.md](CLAUDE.md) — load first; it is the authoritative agent control surface.
2. `wiki status` — live snapshot of watcher state, domain counts, and fine-tune readiness.
3. `wiki retrieve "<question>" [--domain X]` — the default grounding call: a ranked, bounded context block of the most relevant sections, citations preserved. Prefer over reading `index.md` or grepping.
4. `wiki context <slug> --caller <you>` — fetch a known wiki page plus N-hop neighbors (budget-aware) as a structured LLM context block.
5. [WIKI.md](WIKI.md) § Gateway operations table — every available op, its CLI form, and its MCP equivalent.

---

## Architecture

Three layers, one substrate.

- **Wiki** — canonical. Markdown + YAML, citation graph enforced by the gateway.
- **NotebookLM** — heavy-synthesis service called *through* the gateway. Artifacts file back to `wiki/artifacts/` with bidirectional links.
- **Obsidian** — visualization over the same vault. Same wikilinks, same markdown. (A derived FTS5 retrieval index lives at `.index/wiki.db` — gitignored, rebuildable, never canonical; markdown remains the source of truth.)

The validator rejects any claim missing `[[sources/<id>]]`, so authored content cannot drift into hallucination. Drafts (`--draft`) downgrade the rule to a lint warning until `wiki finalize` runs.

All writes go through the gateway. Direct edits to `raw/` or `wiki/` are blocked by validator + pre-commit hook.

## Workflow

1. **Ingest.** Drop a file or URL into `raw/inbox/` (watched), or run `wiki ingest <input>`. Type-specific converters dispatch on filename / URL pattern. API-only sources (Apple Notes today) ingest via `wiki poll <name>`.
2. **Retrieve.** `wiki retrieve "<question>" [--domain X]` returns a ranked, bounded context block (FTS5/BM25 + graph authority), citations preserved — the default way to ground an answer in the wiki. `wiki answer` adds one local grounded-synthesis LLM call on top; `wiki search` is ranked keyword lookup.
3. **Query at corpus scale.** `wiki query "<question>" [--domain X]` synthesizes over a domain's *raw corpus* through NotebookLM and files a synthesis page grounded in `[[sources/<id>]]` citations. Use when the authored wiki layer isn't enough.
4. **Synthesize artifacts.** `wiki nlm-briefing | nlm-audio | nlm-slides` route to NotebookLM and file the artifact back as a wiki page.
5. **Browse.** Open the vault in Obsidian, or run `wiki serve` for the [web UI](#web-ui).

**Start here:** [TUTORIAL.md](TUTORIAL.md).

## Web UI

`wiki serve` runs a local FastAPI + React app at `http://127.0.0.1:7474`. Every long-running gateway op (ingest, query, research execution, NotebookLM generation) submits to an in-memory task store and the UI polls for completion — the browser stays responsive while work runs server-side.

| Route | Surface |
|---|---|
| `/` | Dashboard — watcher heartbeat, inbox queue, source / draft / domain counts, recent activity |
| `/ops/ingest`, `/ops/query`, `/ops/finalize`, `/ops/filter-correct` | Forms for the per-source operations |
| `/ops/bootstrap`, `/ops/discover`, `/ops/promote` | Domain authorship (top-down + bottom-up paths) |
| `/ops/lint` | Run health checks, view the report inline |
| `/research` | Multi-adapter research orchestration. Sessions list + detail; structured per-adapter plan editor; per-step progress streamed from `log.md` |
| `/review` | Curation queues: drafts (inline finalize / abandon), contradictions (severity-tagged, expandable), orphans (discharge via query), filter-band (rationale-driven include / exclude) |
| `/domains/artifacts` | NotebookLM artifact triggers per domain — confirmation modals on every LLM-calling op, per-slide revise modal |

Async ops surface their `task_id` in the UI; refreshing or navigating away does not lose state. Confirmation modals gate every NotebookLM call (cost-sensitive, opt-in by design).

The UI is built into `web/dist/` and served as static files by FastAPI; no separate frontend dev server is required for users. Source for the SPA lives at `web/src/` (Vite + React 18 + TypeScript).

## Source types

Markdown converters dispatch on filename / URL pattern. Each lives at `src/gateway/converters/<type>.py` and emits canonical markdown to `raw/<type>/<slug>.md`.

| Type | Source | Extraction |
|---|---|---|
| `web` | Any URL | Firecrawl + boilerplate strip |
| `youtube`, `arxiv`, `pubmed` | Domain-matched URLs | Per-source API + transcript / abstract |
| `pdf` | Local file | `pdfminer.six` |
| `voice` | `.m4a` / `.mp3` / `.wav` | `mlx-whisper` + pyannote diarization (Apple Silicon) |
| `audiobook` | `.m4b` | Same as voice with chapter-aware segmentation |
| `note` | Apple Notes (poller) | JXA bridge → markdown |
| `csv` / `docx` / `xlsx` / `pptx` | Local file | `csv` (stdlib) / `python-docx` / `openpyxl` / `python-pptx` |
| `image` | `.png` / `.jpg` / `.heic` / etc. | Pillow + Claude vision (structured description) |

Adding a new type: see [CLAUDE.md](CLAUDE.md) § "Adding a new source type". Pollers for additional API-only sources (Notion, Slack, Gmail) share the `Poller` framework.

## Documentation

| Doc | Purpose |
|---|---|
| [TUTORIAL.md](TUTORIAL.md) | Day-1 workflow guide |
| [CLAUDE.md](CLAUDE.md) | Agent control surface — auto-loaded by Claude Code in this directory |
| [WIKI.md](WIKI.md) | Conventions reference — the contract every component codes against |
| [ARCHITECTURE.md](ARCHITECTURE.md) | System diagram, layer descriptions, invariant table, data flow |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Environment setup, how to add converters/pollers/ops/lint, PR checklist |
| [GLOSSARY.md](GLOSSARY.md) | Term definitions for gateway, domain model, and ontology vocabulary |
| [BUILD.md](BUILD.md) | Gateway build plan and per-milestone delivery record |
| [MIGRATION.md](MIGRATION.md) | Legacy Obsidian vault migration plan |
| [SESSION_TRANSCRIPT.md](SESSION_TRANSCRIPT.md) | Chronological narrative of the v1 design-and-build session |
| [docs/adr/README.md](docs/adr/README.md) | Architecture decision records — what was decided and what was rejected |

## Layout

```
~/code/knowledge/
├── src/gateway/    gateway implementation (Python package)
├── tests/gateway/  pytest suite
├── migrations/     schema and content migration scripts
├── scripts/        operational scripts (watcher, MCP, pre-commit hook)
├── web/            Vite + React + TypeScript SPA (built artifacts in web/dist/)
├── raw/            immutable sources (markdown + frontmatter, optional binary sidecars)
├── wiki/           LLM-authored knowledge layer (entities, concepts, sources, synthesis, MOCs, artifacts)
├── nlm/            NotebookLM bookkeeping (notebooks.yaml, query plans, source maps)
├── index.md        content index
├── log.md          chronological event log (append-only)
└── .knowledge/     runtime state (policies, examples, locks, lint reports, watcher / poller cursors)
```

## Install

```sh
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

For voice / audiobook converters and speaker diarization (Apple Silicon recommended; ~3 GB of model weights):

```sh
pip install -e ".[whisper]"
hf auth login                 # paste a Hugging Face token (Read scope)
# Accept terms once at https://huggingface.co/pyannote/speaker-diarization-3.1
```

`wiki` is now on PATH. Optional integrations:

```sh
scripts/install_watcher.sh           # launchd agent: raw/inbox/ → auto-ingest
scripts/install_mcp.sh               # ~/.claude/mcp_servers.json: wiki_* tools in any project
scripts/install_pre_commit_hook.sh   # blocks commits on schema-drift or raw `nlm` calls
```

## CLI

```sh
wiki --help
```

### Retrieve and search (RAG)

The wiki is a relevance-rankable RAG substrate (FTS5/BM25 + graph authority). Preferred call order for grounding an answer: `retrieve` → `context` → `answer` → `query`.

| Command | What it does |
|---|---|
| `wiki retrieve "<question>" [--domain X] [--k N] [--budget CHARS]` | **Default RAG call.** One LLM-free call → bounded, ranked context block of the most relevant sections, each wrapped in `<page>` with `[[sources/<id>]]` preserved |
| `wiki answer "<question>" [--domain X] [--file]` | Retrieve + one grounded Claude call; cites only retrieved sources (ungrounded citations stripped). NotebookLM-independent. `--file` drafts a synthesis page |
| `wiki search "<query>" [--domain X] [--type T] [--order tiered\|bm25]` | Ranked full-text search (SQLite FTS5/BM25) over `wiki/` + `raw/` |
| `wiki context <slug> --caller <id> [--depth N] [--budget CHARS]` | Fetch a known page + N-hop wikilink neighbors; over budget, neighbors are authority-ranked and truncated, not dropped |
| `wiki related "<slug>" [--limit N]` | Co-citation graph neighbors of a page (shared sources), LLM-free |
| `wiki eval-retrieval [--compare] [--k N]` | Score retrieval against the golden set (recall@k, MRR) — governs ranking changes |

### Ingest, query, research

| Command | What it does |
|---|---|
| `wiki ingest <input> [--domain X] [--with-plan] [--draft]` | Ingest a URL or local file. `--with-plan` runs the wiki authorship agent in the same call. `--draft` allows partial citations. |
| `wiki batch-ingest <vault> --legacy-import --domain <slug>` | Migrate a research-notebook Obsidian vault |
| `wiki filter <input>` | Read-only filter score against the domain policy (no writes) |
| `wiki filter-correct <id>` | Override a past filter decision; pin as a `user-correction` example |
| `wiki query "<question>" [--domain X] [--draft]` | Synthesize over a domain's raw corpus via NotebookLM; files a synthesis page grounded in `[[sources/<id>]]` citations |
| `wiki finalize <page> [--abandon]` | Promote a draft to strict (or delete it) |
| `wiki research "<prompt>" [--domain X] [--review] [--execute ID] [--no-draft]` | Multi-adapter search with per-adapter query expansion. Filter routes to Haiku 4.5 in parallel (`WIKI_FILTER_MAX_WORKERS`, default 8). Synthesis pages commit with `draft: true` by default (`--no-draft` for strict citation grounding at apply_plan). `--review` pauses for plan editing. |

### Domain authorship

| Command | What it does |
|---|---|
| `wiki bootstrap-domain "<description>" <slug> [--force]` | Author a starter `policy.yaml` from a natural-language description (top-down) |
| `wiki discover-domains [--scope GLOB] [--since DATE] [--untagged]` | Cluster untagged sources into draft proposals (bottom-up) |
| `wiki promote-domain <proposal-slug>` | Bless a proposal — write policy, back-tag member sources |
| `wiki demote-domain <domain-slug>` | Reverse a promotion — remove tags, delete auto-generated policy |
| `wiki reject-proposal <proposal-slug>` | Delete a draft proposal |

### NotebookLM

| Command | What it does |
|---|---|
| `wiki nlm-add <domain> <source-id>` | Add a raw source to the domain's NotebookLM corpus |
| `wiki nlm-sync <domain> [--limit N] [--dry-run]` | Bulk-add every raw source tagged with the domain; idempotent and resumable |
| `wiki nlm-briefing <domain>` | Briefing doc → `wiki/artifacts/...` |
| `wiki nlm-audio <domain> "<topic>"` | Audio overview → `wiki/artifacts/` |
| `wiki nlm-slides <domain> "<topic>"` | Slide deck → `wiki/artifacts/` |
| `wiki nlm-revise <slug> --slide N "<instructions>"` | Revise an existing artifact |

### Operations

| Command | What it does |
|---|---|
| `wiki backfill-examples --domain X --legacy-config <yaml> --json <staged.json>` | Populate policy + example bank from legacy artifacts |
| `wiki finetune [--check \| --domain X --distill [--force]]` | Inspect example-bank readiness or distill a v2 policy candidate |
| `wiki poll <name> [--list]` | Run a registered poller (e.g. `apple-notes`) for API-only sources |
| `wiki lint [--scope <check>]` | Run health checks; report at `.knowledge/lint/<timestamp>.md` |
| `wiki status` | Watcher heartbeat, inbox queue, recent activity |
| `wiki watch` | Inbox watcher daemon (foreground; launchd usually runs this) |
| `wiki serve [--port 7474] [--bind 127.0.0.1]` | Local browser [web UI](#web-ui) |
| `wiki mcp-serve` | Start the MCP server (stdio) — exposes every gateway op as `wiki_*` tools |

`wiki index --rebuild` regenerates both `index.md` and the derived FTS5 retrieval index (`.index/wiki.db`). `wiki migrate <name>` remains a stub.

## State

Live state lives at runtime, not in this file:

- `wiki status` — watcher heartbeat, queue depth, recent activity
- `index.md` — content index
- [BUILD.md](BUILD.md) — per-milestone delivery record (commits, tests, hand-tests)

## License

MIT — see [LICENSE](LICENSE).
