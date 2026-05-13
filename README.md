# ~/code/knowledge/

A personal knowledge base. Sources land as markdown + YAML on the local filesystem. Queries return cited synthesis pages. NotebookLM artifacts file back to the same vault. Obsidian renders the citation graph.

Implements the LLM Wiki pattern (Karpathy gist `442a6bf555914893e9891c11519de94f`).

## Architecture

Three layers, one substrate.

- **Wiki** — canonical. Markdown + YAML, citation graph enforced by the gateway.
- **NotebookLM** — heavy-synthesis service called *through* the gateway. Artifacts file back to `wiki/artifacts/` with bidirectional links.
- **Obsidian** — visualization over the same vault. Same wikilinks, same markdown, no separate index.

The validator rejects any claim missing `[[sources/<id>]]`, so authored content cannot drift into hallucination. Drafts (`--draft`) downgrade the rule to a lint warning until `wiki finalize` runs.

All writes go through the gateway. Direct edits to `raw/` or `wiki/` are blocked by validator + pre-commit hook.

## Workflow

1. **Ingest.** Drop a file or URL into `raw/inbox/` (watched), or run `wiki ingest <input>`. Type-specific converters dispatch on filename / URL pattern. API-only sources (Apple Notes today) ingest via `wiki poll <name>`.
2. **Query.** `wiki query "<question>" [--domain X]` runs semantic retrieval across mixed media and files a synthesis page grounded in `[[sources/<id>]]` citations.
3. **Synthesize at corpus scale.** `wiki nlm-briefing | nlm-audio | nlm-slides` route to NotebookLM and file the artifact back as a wiki page.
4. **Browse.** Open the vault in Obsidian, or run `wiki serve` for the [web UI](#web-ui).

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
| [BUILD.md](BUILD.md) | Gateway build plan and per-milestone delivery record |
| [MIGRATION.md](MIGRATION.md) | Legacy Obsidian vault migration plan |
| [SESSION_TRANSCRIPT.md](SESSION_TRANSCRIPT.md) | Chronological narrative of the v1 design-and-build session |

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

### Ingest and query

| Command | What it does |
|---|---|
| `wiki ingest <input> [--domain X] [--with-plan] [--draft]` | Ingest a URL or local file. `--with-plan` runs the wiki authorship agent in the same call. `--draft` allows partial citations. |
| `wiki batch-ingest <vault> --legacy-import --domain <slug>` | Migrate a research-notebook Obsidian vault |
| `wiki filter <input>` | Read-only filter score against the domain policy (no writes) |
| `wiki filter-correct <id>` | Override a past filter decision; pin as a `user-correction` example |
| `wiki query "<question>" [--domain X] [--draft]` | Search the wiki and file a synthesis page grounded in `[[sources/<id>]]` citations |
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

`wiki index --rebuild`, `wiki search`, and `wiki migrate <name>` remain stubs.

## State

Live state lives at runtime, not in this file:

- `wiki status` — watcher heartbeat, queue depth, recent activity
- `index.md` — content index
- [BUILD.md](BUILD.md) — per-milestone delivery record (commits, tests, hand-tests)

## License

MIT — see [LICENSE](LICENSE).
