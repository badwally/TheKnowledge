# Tutorial

A first-time user's guide to `~/code/knowledge/`. Take twenty minutes to walk through this top to bottom; come back for the cheat sheet at the end.

## 1. What this system does

You drop in sources — PDFs, URLs, voice memos, spreadsheets, images. The system extracts canonical markdown, files it under `raw/`, and lets you ask questions of the resulting corpus. Every answer is a markdown page where every claim links back to the source it came from. There is no separate database, no embedding store, no vendor lock-in: the corpus is a directory tree.

Three layers cooperate:

- **The wiki** (this directory) is canonical storage. Markdown files with YAML frontmatter, organized into `raw/` (sources, immutable) and `wiki/` (authored pages: summaries, concepts, syntheses).
- **NotebookLM** is the heavy-synthesis service for whole-corpus questions. The gateway calls it on your behalf and files every artifact (briefing, audio, slides) back as a wiki page. You never use NotebookLM directly.
- **Obsidian** is an optional viewer. Open this directory as an Obsidian vault and the wikilinks the system writes turn into a navigable graph.

You interact with the system three ways: the `wiki` command-line tool, the local web app (`wiki serve`), or the MCP server (so other Claude Code projects can call it). Pick whichever fits the task; they all hit the same gateway.

## 2. Install and verify

```sh
cd ~/code/knowledge/
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

The `wiki` command is now on your PATH (inside the venv).

**Optional — voice and audiobook ingest** (Apple Silicon recommended; ~3 GB of model weights):

```sh
pip install -e ".[whisper]"
hf auth login                 # paste a Hugging Face token (Read scope)
# Accept terms once at https://huggingface.co/pyannote/speaker-diarization-3.1
```

**Optional — three integrations worth installing on day one:**

```sh
scripts/install_watcher.sh           # auto-ingests anything dropped into raw/inbox/
scripts/install_mcp.sh               # exposes wiki_* tools to other Claude Code projects
scripts/install_pre_commit_hook.sh   # blocks accidental schema-drift or raw NotebookLM calls
```

Verify the install:

```sh
wiki status
```

You should see a watcher heartbeat (if you installed it), the inbox queue depth, source / draft / domain counts, and the last few activity entries. If `wiki status` runs without error, you are ready to go.

## 3. Add your first source

Three ways to ingest a source. They all converge on the same pipeline.

**Drop into the watched inbox.** Easiest if you have the watcher installed:

```sh
cp ~/Downloads/paper.pdf ~/code/knowledge/raw/inbox/
```

Within a few seconds the watcher converts the PDF to markdown, files it at `raw/pdf/<id>.md` (with the binary preserved alongside as `<id>.pdf`), and creates a summary page at `wiki/sources/<id>.md`.

**Run `wiki ingest` directly.** Works for both URLs and local files:

```sh
wiki ingest https://www.nature.com/articles/s41586-024-07444-7
wiki ingest ~/Downloads/paper.pdf
wiki ingest ~/Documents/Voice\ Memos/idea.m4a
```

**Use the web app.** Run `wiki serve`, navigate to `/ops/ingest`, paste a URL or file path. The browser submits and polls for completion (see § 5).

### Tag with a domain (optional but useful)

```sh
wiki ingest paper.pdf --domain glp1-reward-modulation
```

Tagging a source with a domain runs it through that domain's filter policy — a Claude-authored ruleset that scores relevance. Sources scoring below threshold are flagged for review rather than rejected. You don't need a domain on day one; the system works fine with untagged sources, and § 7 covers how to create domains later.

### See what got ingested

```sh
ls -la raw/pdf/                        # the canonical extraction
cat raw/pdf/<id>.md | head -40         # YAML frontmatter + body
ls wiki/sources/                       # one summary page per source
cat wiki/sources/<id>.md               # human-readable summary
```

## 4. Ask your first question

This is the load-bearing flow. The answer is itself a wiki page.

```sh
wiki query "what does the corpus say about GLP-1 effects on dopamine?" --draft
```

What happens:

1. The gateway searches `wiki/` (not `raw/`) for keyword-relevant pages, takes the top matches, and includes them in a prompt.
2. Claude drafts a synthesis — sentences making claims, each anchored by a `[[sources/<id>]]` wikilink to the source the claim came from.
3. The validator checks that every claim is cited. With `--draft`, missing citations downgrade to warnings; without it, missing citations cause the write to fail.
4. The synthesis lands at `wiki/synthesis/<auto-slug>.md`.

```sh
cat wiki/synthesis/<slug>.md
```

You will see prose with `[[sources/...]]` interspersed. Click any of those links if you have the file open in Obsidian, or `cat` the target path; you arrive at the source the claim came from.

### Finalize when ready

If the draft has untyped claims (`draft_unresolved_claims: N` in the frontmatter), do a follow-up authoring pass: add citations, or remove claims you can't ground. Then:

```sh
wiki finalize wiki/synthesis/<slug>.md
```

This re-runs the strict validator. If everything is cited, the `draft: true` flag is cleared. To delete a stuck draft outright: `wiki finalize <path> --abandon`.

### Pick the right tool

| You want | Use |
|---|---|
| An answer drawn from existing wiki content | `wiki query "..."` |
| To ingest a source and write the synthesis in one call | `wiki ingest <url> --with-plan` |
| A whole-corpus answer across dozens of sources | `wiki nlm-briefing <domain>` (see § 8) |
| Slides, audio, or a document for a meeting | `wiki nlm-slides`, `wiki nlm-audio`, `wiki nlm-briefing` |

## 5. The web app

```sh
wiki serve
# → http://127.0.0.1:7474
```

A local FastAPI + React app. Everything you can do from the CLI you can do from the browser, plus a few things that are awkward in a terminal (multi-step research orchestration, contradiction triage, plan editing).

The app uses a submit-then-poll pattern: long-running operations (ingest, query, NotebookLM generation, research execution) submit to a server-side task store and the browser polls until completion. You can navigate away and come back without losing state.

### Routes

| Route | What it does |
|---|---|
| `/` | Dashboard — watcher heartbeat, queue depth, source / draft / domain counts, recent activity |
| `/ops/ingest` | Form to ingest a URL or file. Watch the task progress without leaving the page. |
| `/ops/query` | Form to ask a question and write a synthesis page |
| `/ops/finalize` | Promote a draft synthesis to strict (or abandon it) |
| `/ops/filter-correct` | Override a past filter decision and pin it as a learning example |
| `/ops/bootstrap` | Author a new domain policy from a natural-language description |
| `/ops/discover` | Cluster untagged sources into draft domain proposals |
| `/ops/promote` | Bless a draft proposal as a real domain |
| `/ops/lint` | Run health checks across the wiki and view the report inline |
| `/research` | Multi-adapter research orchestration (see § 7). Sessions list and detail; structured per-adapter plan editor; per-step progress streamed from `log.md`. |
| `/review` | Curation queues. Four tabs: drafts (inline finalize / abandon), contradictions (severity-tagged, expandable), orphans (sources nothing cites, dischargeable via query), filter-band (rationale-driven include / exclude). |
| `/domains/artifacts` | NotebookLM artifact triggers per domain. Confirmation modals on every cost-incurring call; per-slide revise modal. |

### When to use the app vs. the CLI

| Task | Better in |
|---|---|
| Quick ingest of a single file | CLI (drop into `raw/inbox/`) |
| Asking a one-shot question | Either; web is nicer if you want to read the result |
| Reviewing a backlog of drafts | Web — the Review console is built for this |
| Running a multi-adapter research session | Web — the plan editor is structured |
| Triaging contradictions | Web — severity / expand UX is essential |
| Generating NotebookLM artifacts | Web — the confirmation modals prevent expensive accidents |
| Scripting / automation | CLI |

## 6. Source types

The converter dispatcher routes by URL pattern or file extension. You don't need to know which converter runs; it picks for you.

| Type | Source | What you get |
|---|---|---|
| `web` | Any URL | Article body extracted via Firecrawl, boilerplate stripped |
| `youtube` | YouTube URL | Title, channel, transcript |
| `arxiv` | arXiv URL or ID | Title, authors, abstract, full text |
| `pubmed` | PubMed URL or PMID | Title, authors, abstract |
| `pdf` | `.pdf` | Page-by-page text via `pdfminer.six`; binary preserved as sidecar |
| `voice` | `.m4a` / `.mp3` / `.wav` | Speaker-diarized transcript with timestamps (mlx-whisper + pyannote) |
| `audiobook` | `.m4b` | Same as voice, split by embedded chapters |
| `note` | Apple Notes | Pulled by `wiki poll apple-notes` (see below) |
| `csv` / `tsv` | Tabular file | Preview rows + column metadata; full data in sidecar |
| `docx` / `xlsx` / `pptx` | Office documents | Headings preserved; speaker notes included; first 50 rows × 20 cols of any sheet |
| `image` | `.png` / `.jpg` / `.heic` / etc. | Structured description from Claude vision (overview, visible text, key elements, domain content) |

A note on Office documents and PDFs: embedded images are intentionally skipped. For prose-heavy sources the author's text usually describes figures more accurately than vision would, and the original is preserved as a sidecar so you can inspect it on demand. If a specific figure carries primary content, extract and ingest it as an image separately.

A note on cost: image ingest uses Claude vision (~1¢ per image, ~10–30 seconds each). Voice and audiobook transcription is free but slow on CPU; on Apple Silicon mlx-whisper runs roughly 5× real-time.

### API-only sources: pollers

For sources you can't drop into a folder (Apple Notes today; Notion, Slack, Gmail planned), pollers fetch new items on demand:

```sh
wiki poll --list                # see registered pollers
wiki poll apple-notes           # fetch new notes since last cursor
```

Pollers maintain their own cursor under `.knowledge/pollers/<name>/cursor.yaml` and only fetch what's new on subsequent runs. The first run for Apple Notes will prompt macOS for Automation access.

## 7. Domains and research

A **domain** is a topical scope: GLP-1 reward modulation, edge AI inference, cycling and fitness. Domains have a `policy.yaml` (filter rules, quality signals, search queries) and optionally a NotebookLM notebook attached. Tagging a source with a domain runs it through the policy filter; tagging a wiki page links it to the domain's MOC (map of content).

You don't need domains to use the system — single-source ingest and one-off queries work fine without them. Create a domain when you have an ongoing research interest and want focused filtering, multi-source research, or NotebookLM artifacts scoped to one topic.

### Two ways to create a domain

**Top-down: you have a question, no sources yet.** Describe the domain to the system and let it author a starter policy:

```sh
wiki bootstrap-domain \
  "On-device LLM inference for autonomous agentic workflows: edge runtimes,
   quantization, and inter-agent protocols. Focus on production deployment
   patterns and competitive ecosystem analysis." \
  edge-ai-agentic
```

The result is `.knowledge/policies/edge-ai-agentic/policy.yaml` — topic, field, inclusion / exclusion criteria, quality signals, search queries, all derived from your description. The system retries once if the first draft is under-specified, then saves a `policy.draft.yaml` for hand-editing.

The same operation is available in the web app at `/ops/bootstrap`.

**Bottom-up: you've accumulated sources without a domain.** Cluster them and bless one:

```sh
wiki discover-domains --untagged       # propose draft domains from untagged sources
wiki promote-domain <proposal-slug>     # turn a proposal into a real domain
```

The proposals land at `wiki/proposals/`. The web app's `/ops/discover` and `/ops/promote` flows show them visually.

### Multi-source research

Once a domain exists, run a research session against it:

```sh
wiki research "<your question>" --domain <slug> --review
```

This drafts a per-adapter query plan (which queries to run against arXiv, PubMed, YouTube, web, Semantic Scholar) and saves it to `nlm/query_plans/<session-id>.yaml`. With `--review` the session pauses so you can edit the plan; without it the session executes immediately.

The web app at `/research` is the right place for this work. You see the plan as a structured editor, run execution from the UI, and watch per-step progress (search → filter → materialize → NotebookLM session → analysis → synthesis) stream in from the activity log.

```sh
wiki research --execute <session-id>   # run a paused session from the CLI
```

**Filter and synthesis behavior (M44 / M45):**

- **Filter routes to Haiku 4.5 in parallel.** A 200-candidate run finishes in 5–10 minutes (8 workers × ~16 s per Haiku call). Tune via `WIKI_FILTER_MAX_WORKERS=4` if you hit Max-plan rate limits.
- **Synthesis pages commit as drafts by default.** NotebookLM's synthesis prose routinely emits interpretive framing (*"The provided sources detail…"*, *"There is an unanswered tension…"*) that fails strict per-claim citation grounding. The `wiki research` command therefore defaults to `--draft` — pages land with `draft: true` and `draft_unresolved_claims: N` so you can finish citations later. Pass `--no-draft` to opt into strict validation (recommended only for narrow firm-explainer queries where every claim is single-source).
- **Finishing a draft** (M45 chain). Pages produced by `wiki research` carry `synthesizes:` frontmatter (an explicit list of constituent `sources/<id>` or `synthesis/<slug>`) and a `## Included works` body section, modeled on Cochrane's "Characteristics of included studies" convention. After the run, attribute any remaining uncited claims via `wiki cite <page>` (adds `[[sources/<id>]]` tokens to specific lines), then `wiki finalize <page>` to clear `draft: true`. `wiki lint --scope citation-chains` reports dangling refs and pages that aggregate without an enumerated set.

## 8. NotebookLM workflow

Use NotebookLM when the question spans dozens of sources and a single in-context call would lose detail. The gateway treats NotebookLM as a synthesis service — you never invoke `nlm` directly (the pre-commit hook blocks committed content that contains raw `nlm ` invocations).

**One-time auth setup:**

```sh
nlm login                              # opens a browser; signs into Google
```

The token is cached locally; subsequent commands run without prompts.

**Add sources to a domain's corpus, then synthesize:**

```sh
wiki nlm-add glp1-reward-modulation pubmed-22128031     # one source at a time
wiki nlm-sync glp1-reward-modulation                     # bulk-add every source tagged with the domain
wiki nlm-briefing glp1-reward-modulation                 # full briefing doc
wiki nlm-audio glp1-reward-modulation "reward circuit primer"
wiki nlm-slides glp1-reward-modulation "alcohol use disorder evidence"
wiki nlm-revise <artifact-slug> --slide 3 "tighten the conclusion"
```

`nlm-sync` is idempotent and resumable — re-running it skips sources that are already in the corpus and picks up where it left off if interrupted. Pass `--limit N` to do a partial run, or `--dry-run` to preview without writing.

Every artifact files back to `wiki/artifacts/` with bidirectional links: the artifact links to the sources it cites, and each source page lists the artifacts that used it. Nothing ends up trapped inside NotebookLM's UI.

**The web app** at `/domains/artifacts` is the recommended interface for this workflow. NotebookLM calls cost real money and time; the confirmation modals on every trigger prevent accidental clicks. Per-slide revise lives in a modal next to each artifact.

## 9. Use this knowledge base from other projects

Wiki paths are stable. Reference them from any other project's CLAUDE.md, README, or notes:

```markdown
The reward-circuit synthesis lives at
~/code/knowledge/wiki/synthesis/<slug>.md.
```

For programmatic access from another Claude Code session, the MCP server (installed in § 2) exposes every gateway operation as a `wiki_*` tool: `wiki_query`, `wiki_ingest`, `wiki_nlm_briefing`, etc. After running `scripts/install_mcp.sh`, **restart Claude Code** once for the tools to load. From then on, any project's session can write to the knowledge base without leaving its own working directory.

## 10. Operate the system

```sh
wiki status                                        # watcher heartbeat, queue, recent activity
wiki lint                                          # all checks; report at .knowledge/lint/
wiki lint --scope orphans                          # cheap; just the orphan list
wiki finetune --check                              # example-bank readiness per domain
wiki finetune --domain X --distill --force         # produce a v2 policy candidate
```

**Daily**: `wiki status` to confirm the watcher is alive. The launchd agent restarts it on crash, but a stale heartbeat (no beat for several minutes) means investigate.

**Weekly**: `wiki lint`, or open `/review` in the web app. Look for new orphans, drafts older than seven days, and citation-density warnings on synthesis pages.

**Monthly** (if you're using domain policies): `wiki finetune --check`. Once a domain crosses ~500 high-quality filter decisions, run `--distill --force` to get a candidate v2 policy under `.knowledge/policies/<domain>/policy_versions/`. Review and copy to `policy.yaml` if good — the candidate never overwrites the live policy.

### The watcher

The launchd agent runs `wiki watch` continuously. It picks up anything dropped into `raw/inbox/` and runs the full ingest pipeline.

```sh
launchctl list | grep knowledge.watcher        # confirm loaded
tail -f .knowledge/watcher.out.log              # live log
scripts/install_watcher.sh --uninstall         # stop and remove
scripts/install_watcher.sh                      # reinstall
```

Failed ingests land in `raw/inbox/_failed/` with an error sidecar. Check there if a file disappears from the inbox without showing up in `raw/<type>/`.

## 11. Troubleshooting

| Symptom | Diagnosis |
|---|---|
| `wiki ingest` fails with `no converter handles ...` | URL or extension not recognized. Check the supported types in § 6. |
| `wiki query` returns "no wiki pages matched" | The question doesn't keyword-match any wiki page. Use `--domain` to scope, or ingest more sources first. |
| Pre-commit hook blocks a commit | You wrote a raw `nlm ` invocation somewhere. Replace with `wiki nlm-*`. |
| `wiki nlm-*` errors on auth | Run `nlm login` — that's NotebookLM's auth, separate from Hugging Face. |
| Voice converter `TranscriptionError: HF_TOKEN` | Speaker diarization needs Hugging Face auth. Run `hf auth login` and accept the pyannote model terms. |
| MCP `wiki_*` tools missing in another Claude Code session | Restart Claude Code after running `scripts/install_mcp.sh`. |
| Lint reports many source orphans | Expected if you migrated a legacy vault. Discharge via `wiki query` synthesis loops over time. |
| The web app loads but routes 404 | `web/dist/` may be stale. Rebuild with `cd web && npm install && npm run build`. |

## 12. Cheat sheet

```sh
# Read
ls wiki/synthesis/                                 # answer pages
rg "<term>" wiki/                                  # grep wiki layer
cat wiki/concepts/<slug>.md

# Ingest
wiki ingest <path-or-url> [--domain X] [--with-plan] [--draft]
wiki poll <name>                                   # API-only sources (apple-notes, etc.)
wiki poll --list

# Query and finalize
wiki query "<question>" [--domain X] [--draft]
wiki filter <path>                                 # read-only score
wiki filter-correct <source-id>                    # pin a corrected example
wiki finalize <page-path> [--abandon]

# Domains
wiki bootstrap-domain "<description>" <slug>       # top-down policy
wiki discover-domains [--untagged]                  # bottom-up clustering
wiki promote-domain <proposal-slug>
wiki demote-domain <domain-slug>
wiki reject-proposal <proposal-slug>

# Research
wiki research "<prompt>" --domain <slug> [--review]
wiki research --execute <session-id>

# NotebookLM
wiki nlm-add <domain> <source-id>
wiki nlm-sync <domain> [--limit N] [--dry-run]
wiki nlm-briefing <domain>
wiki nlm-audio <domain> "<topic>"
wiki nlm-slides <domain> "<topic>"
wiki nlm-revise <slug> --slide <n> "<instructions>"

# Operate
wiki status
wiki serve [--port 7474]                           # local browser UI
wiki watch                                         # foreground watcher (launchd usually runs this)
wiki lint [--scope <check>]
wiki backfill-examples --domain X --legacy-config <yaml> --json <staged.json>
wiki finetune [--check | --domain X --distill [--force]]

# Migrate
wiki batch-ingest <vault> --legacy-import --domain <slug> [--dry-run]

# MCP (other Claude Code projects)
wiki mcp-serve                                     # stdio; usually invoked by ~/.claude/mcp_servers.json
```

## 13. Where to read more

- `README.md` — top-level overview and architecture
- `CLAUDE.md` — agent control surface, auto-loaded by every Claude Code session in this directory
- `WIKI.md` — full schema reference for frontmatter, page types, and lint rules
- `BUILD.md` — gateway build plan and per-milestone delivery record
- `MIGRATION.md` — legacy Obsidian vault migration plan
