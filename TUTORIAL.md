# Tutorial — using ~/code/knowledge/

How to actually use this knowledge base. Covers the day-1 mental model,
the three ways to add a source, the synthesis loop, cross-project use,
and operational habits. Skim top-to-bottom once; come back for the
cheat sheet at the end.

## 1. The mental model

A personal knowledge base where every authored claim ties to a real
source you ingested. Three load-bearing pieces work together:

- The **wiki** (this repo) is canonical storage — local markdown +
  YAML frontmatter under a single root.
- **NotebookLM** is the heavy-synthesis service for whole-corpus
  questions. The gateway invokes it via `wiki nlm-*`; every artifact
  files back to `wiki/artifacts/` with bidirectional links so nothing
  ends up siloed inside NotebookLM.
- **Obsidian** is the knowledge-graph visualization engine. Open this
  directory as an Obsidian vault and the `[[wikilinks]]` the gateway
  enforces become a navigable graph of sources, concepts, and
  syntheses.

The repo is two layers stacked under a single root:

```
~/code/knowledge/
├── raw/              ← immutable sources (one .md + frontmatter per source)
│                       PDFs / audio kept as binary sidecars
├── wiki/             ← LLM-authored knowledge layer
│   ├── sources/        per-source summary pages, one to one with raw/
│   ├── concepts/       drugs, mechanisms, phenomena, techniques
│   ├── entities/       people, organizations, datasets, papers as entities
│   ├── synthesis/      cross-source analyses (the answer pages)
│   └── mocs/           maps of content per domain (entry points)
├── nlm/              ← NotebookLM bookkeeping (notebook IDs per domain)
└── .knowledge/       ← runtime state — policies, examples, locks, lint reports
```

**One-line rule:** raw sources are append-only; everything in `wiki/` is
authored (or re-authored) through the gateway, which enforces citation
grounding via `[[sources/<id>]]` wikilinks.

**Why it's like this:** filesystem-as-database. Markdown + YAML
frontmatter is canonical, every retrieval primitive (`grep`, file walk,
ripgrep, your editor) just works, no SDK required. The gateway is a thin
discipline layer; the data is the README.

## 2. Day 1 — read what's already there

Open these in order with your editor or `bat`/`less`:

1. **`index.md`** — live content index. The fastest "what's in here" view.
2. **`wiki/mocs/`** — domain entry points (one MOC per topic area).
3. **`wiki/synthesis/`** — answer pages. Pick any one as a worked example
   of the format: claim sentences anchored by `[[sources/<id>]]`
   wikilinks, with frontmatter declaring the domain and any draft state.
4. **`wiki/sources/<canonical-id>.md`** — summary card per source.
   Click any `[[sources/...]]` wikilink in a synthesis to land here.
5. **`raw/<type>/<canonical-id>.md`** — the immutable origin. Wiki
   summaries link here via `[[raw/<type>/<id>]]`.

For the live counts and per-domain breakdown, run `wiki status` and
read `index.md`.

**Navigation shortcuts:**

```sh
rg --type md "VTA" wiki/                  # ripgrep across the wiki layer
ls wiki/synthesis/                        # list every synthesis page
fd -e md . wiki/concepts/glp1*            # find concept pages by pattern
```

## 3. Add a source

Three input shapes. All go through `wiki ingest`; the converter
dispatcher routes by URL pattern or file extension.

### 3a. A web page or paper URL

```sh
wiki ingest https://www.nature.com/articles/s41586-024-07444-7 --domain glp1-reward-modulation
```

Behind the scenes: web converter pulls the article (trafilatura),
filter scores it against the policy, the wiki summary page is created.
For arxiv / pubmed / youtube URLs, a domain-specific converter handles
metadata extraction.

### 3b. A local document — PDF, Word, Excel, PowerPoint, CSV

```sh
# Drop into the watcher inbox; the launchd agent ingests automatically
cp ~/Downloads/paper.pdf ~/code/knowledge/raw/inbox/
cp ~/Downloads/notes.docx ~/code/knowledge/raw/inbox/
cp ~/Downloads/budget.xlsx ~/code/knowledge/raw/inbox/
cp ~/Downloads/deck.pptx ~/code/knowledge/raw/inbox/
cp ~/Downloads/data.csv ~/code/knowledge/raw/inbox/

# Or invoke directly
wiki ingest ~/Downloads/paper.pdf --domain glp1-reward-modulation
wiki ingest ~/Downloads/notes.docx
```

What each converter does:
- **PDF** (`pdfplumber`): page-by-page text extraction; sidecar `.pdf` preserved.
- **Word `.docx`** (`python-docx`): paragraphs and tables in document order; `Heading 1-6` styles map to `#`/`##`/`###`/etc. Author / title / created date pulled from core properties.
- **Excel `.xlsx`** (`openpyxl`, read-only mode for streaming over large workbooks): each sheet becomes a `## <sheet-name>` section with a preview table (first 50 rows × 20 columns; full data in the sidecar).
- **PowerPoint `.pptx`** (`python-pptx`): each slide becomes `## Slide N: <title>`; speaker notes when present render as `> **Speaker notes:** ...` block.
- **CSV / TSV** (stdlib): dialect-sniffed delimiter, preview-row (50) and preview-col (20) truncation, pipe-character escaping for markdown safety.

Embedded images inside Office documents and PDFs are intentionally skipped — for prose-heavy sources (scientific papers, technical writing) the author's text typically describes figures more accurately than a VLM would, and the original file is preserved as a sidecar so on-demand inspection works via the citation chain. If a specific figure carries primary content, extract it and ingest it separately as an image (§ 3d).

### 3c. A voice memo or audiobook

```sh
wiki ingest ~/Documents/Voice\ Memos/idea.m4a
wiki ingest ~/Audiobooks/thinking-fast-slow.m4b
```

Voice memos transcribe via mlx-whisper (`large-v3-turbo`, ~5× real-time
on M3 Max) and diarize via pyannote — output is a speaker-labeled
markdown body with timestamp anchors. Audiobooks (`.m4b`) split by
embedded chapters.

### 3d. An image — chart, diagram, screenshot, photo

```sh
wiki ingest ~/Downloads/q1-sales-chart.png
wiki ingest ~/Pictures/whiteboard-2026-04-29.heic
```

Multimodal ingest. Pillow extracts metadata (dimensions, format, mode); Claude vision runs a structured prompt to produce a citable description with four sections (Overview / Visible text / Key elements / Domain-specific content). The image becomes searchable and linkable just like any other source — `[[sources/image-<YYYY-MM-DD>-<hash>]]` resolves to the description page; the original is preserved as a sidecar at `raw/image/<id>.<ext>`.

Cost is real: ~1¢ per image, ~10–30s per call. Fine for one-off ingests; consider whether you actually need image-by-image VLM for a folder of hundreds of screenshots.

Supported extensions: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.tiff`, `.bmp`, `.heic`, `.heif`. Vector formats (SVG) are out of scope in v1.

### 3e. A note you wrote in another tool

If it's already markdown with reasonable frontmatter, just put it in
`raw/inbox/`. Otherwise, voice-memo it.

### 3f. An API-only source — pollers

For sources without a watchable filesystem (Apple Notes today; Notion / Slack / Gmail queued), pollers fetch new items on a schedule and write them to `raw/note/`:

```sh
wiki poll --list                # see registered pollers
wiki poll apple-notes           # fetch new notes since last cursor
```

Each poller maintains its own cursor under `.knowledge/pollers/<name>/cursor.yaml`, so re-runs only fetch what's new. The first run for Apple Notes prompts macOS for Automation access to Notes.app; subsequent runs are silent. Pollers don't bypass the pipeline — they only produce canonical markdown in `raw/note/`, and the filter / validator / citation-grounding rules apply unchanged downstream.

The watcher writes the new file to `raw/<type>/<id>.<ext>` and a
canonical markdown to `raw/<type>/<id>.md`. Failed ingests land in
`raw/inbox/_failed/` with an error sidecar.

## 4. Ask a question — the synthesis loop

This is the load-bearing flow. Every answer ends up as a wiki page
grounded in canonical sources.

```sh
wiki query "what is known about GLP-1 modulation of mesolimbic dopamine?" \
  --domain glp1-reward-modulation \
  --draft
```

What happens:
1. Gateway searches `wiki/` (not `raw/`) for keyword-matching pages,
   takes up to 30.
2. Builds a prompt with the question + matched page contents.
3. Calls `claude -p` (single LLM call, ~80 s wall clock).
4. Parses the agent's `Plan` response.
5. `apply_plan()` validates every claim has a `[[sources/<id>]]`
   citation and writes the synthesis page atomically. Without
   `--draft`, claims missing citations cause the write to fail.

Output lands at `wiki/synthesis/<auto-slug>.md` with `draft: true` and
`draft_unresolved_claims: N` recording how many lines need citations
before finalize.

### Finalize a draft

After a follow-up authoring pass adds citations (or removes
unresolvable meta-claims):

```sh
wiki finalize wiki/synthesis/<slug>.md
```

This re-runs the strict validator. If all claims are now cited, the
`draft: true` flag is cleared. Use `--abandon` to delete a stuck draft.

### When to use what

| Need | Command |
|---|---|
| Quick answer based on existing wiki content | `wiki query "..." --domain X` |
| Full corpus answer using NotebookLM | `wiki nlm-briefing <domain>` (see § 7 — large-scale path) |
| One-shot ingest + query in a single turn | `wiki ingest <url> --with-plan --domain X` |
| Slides for a meeting | `wiki nlm-slides <domain> "topic"` |

## 5. Use this KB from another project

The wiki paths are stable. Reference them from any other `~/code/*`
project's CLAUDE.md, README, or notes:

```markdown
The reward-circuit synthesis lives at
`~/code/knowledge/wiki/synthesis/<slug>.md`.
```

For agent access from another Claude Code session, the MCP server is
already registered globally (see `~/.claude/mcp_servers.json`). Tools
appear as `wiki_query`, `wiki_ingest`, `wiki_nlm_*`, etc. in any CC
project. **Restart Claude Code** once after install for them to load.

## 6. Open a new research domain

Two paths, depending on what you have:

**Top-down (you have a question, no sources yet).** Describe the domain
to Claude in a sentence or two and let `wiki bootstrap-domain` author a
starter `policy.yaml`:

```sh
wiki bootstrap-domain \
  "On-device LLM inference for autonomous agentic workflows: edge runtimes,
   quantization, and inter-agent protocols. Focus on production deployment
   patterns and competitive ecosystem analysis." \
  edge-ai-agentic
```

This writes `.knowledge/policies/edge-ai-agentic/policy.yaml` with topic,
field, description, inclusion/exclusion criteria, and quality signals —
all derived from your description. Claude validates against a strict
schema (≥3 inclusion criteria, ≥1 exclusion, ≥2 quality-signal categories);
under-specified responses trigger one retry, then save a
`policy.draft.yaml` for hand-editing.

Refuses on collisions:
- Existing promoted policy → run `wiki demote-domain <slug>` first
- Existing draft proposal → run `wiki promote-domain` or `wiki reject-proposal`
- Existing non-promoted policy → pass `--force` to overwrite

**Bottom-up (you've accumulated sources without a domain yet).** Cluster
untagged sources into draft proposals, then bless one:

```sh
wiki discover-domains --untagged
wiki promote-domain <proposal-slug>
```

This produces a minimal auto-generated policy with empty inclusion
criteria — you'll hand-edit them or run bootstrap-domain `--force` to
re-author from a description.

**Either way**, once a policy exists, `wiki research` can populate the
domain:

```sh
wiki research "<your research question>" --domain <slug> --review
# review/edit the per-adapter query plan in nlm/query_plans/<session-id>.yaml
wiki research --execute <session-id>
```

This fans out across arXiv/YouTube/PubMed/web/Semantic Scholar, runs
each candidate through the semantic filter, materializes accepted
sources to `raw/`, builds a NotebookLM session, and files synthesis
pages to `wiki/synthesis/`.

## 7. NotebookLM workflow (for whole-domain synthesis)

Use NotebookLM when the question spans dozens of sources and a single
in-context call would lose detail. The gateway treats NotebookLM as a
synthesis service:

```sh
wiki nlm-add glp1-reward-modulation pubmed-22128031   # add source to corpus
wiki nlm-briefing glp1-reward-modulation              # full briefing doc
wiki nlm-audio glp1-reward-modulation "reward circuit primer"
wiki nlm-slides glp1-reward-modulation "alcohol use disorder evidence"
```

Every artifact is filed back to `wiki/artifacts/` with bidirectional
links to the sources used. **Discipline gate:** the bare `nlm` CLI is
forbidden in committed wiki content; the pre-commit hook (M9) blocks
commits that contain raw `nlm ` invocations. Always go through
`wiki nlm-*`.

## 8. Operational habits

```sh
wiki status            # watcher heartbeat, inbox queue, recent activity
wiki lint              # all checks; full report at .knowledge/lint/
wiki lint --scope orphans                    # cheap; just the orphan list
wiki finetune --check                         # example-bank state per domain
wiki finetune --domain X --distill --force    # produce a v2 policy candidate
```

**Daily:** `wiki status` to confirm the watcher is alive. The launchd
agent restarts it on crash, but a stale heartbeat (no beat for several
minutes) means investigate.

**Weekly:** `wiki lint`. Look for new orphans, stale drafts older than
7 days, citation-density warnings on synthesis pages. The output is
markdown — stash it in your weekly review notes if you keep them.

**Monthly:** `wiki finetune --check`. Once a domain crosses ~500
high-quality decisions, run `--distill --force` to get a candidate
v2 policy under `.knowledge/policies/<domain>/policy_versions/`.
Review and copy to `policy.yaml` if good — the candidate never
overwrites the live policy.

## 9. The watcher

The launchd agent runs `wiki watch` continuously and ingests anything
dropped in `raw/inbox/`.

```sh
launchctl list | grep knowledge.watcher        # confirm loaded
tail -f ~/code/knowledge/.knowledge/watcher.out.log
scripts/install_watcher.sh --uninstall         # stop + remove
scripts/install_watcher.sh                      # reinstall
```

If the watcher dies and doesn't restart, kill its pid via
`pkill -f "wiki watch"` and rerun the install script.

## 10. Troubleshooting

| Symptom | Diagnosis |
|---|---|
| `wiki ingest` fails with `no converter handles ...` | URL/extension isn't recognized; check `gateway/converters/` |
| `wiki query` returns "no wiki pages matched" | Question doesn't keyword-match any page; use `--domain` to scope or `wiki ingest` first |
| Pre-commit hook blocks commit on `wiki/*.md` | You wrote raw `nlm ` somewhere; replace with `wiki nlm-*` |
| `wiki nlm-*` errors on auth | Run `nlm login` (the upstream NotebookLM CLI's auth, not HF) |
| Voice converter `TranscriptionError: HF_TOKEN` | Diarization needs HF auth; falls back to transcript-only or run `hf auth login` |
| MCP `wiki_*` tools not visible in another CC session | Restart Claude Code after `scripts/install_mcp.sh` |
| Lint reports 215+ source orphans | Expected — legacy migrations don't wikilink sources from MOCs; discharge via `wiki query` synthesis loops |

## 11. Cheat sheet

```sh
# Read
ls wiki/synthesis/                                 # answer pages
rg "<term>" wiki/                                  # grep wiki layer
cat wiki/concepts/<slug>.md

# Write (always through the gateway)
wiki ingest <path-or-url> [--domain X] [--with-plan] [--draft]
wiki query "<question>" --domain X [--draft]
wiki filter <path>                                 # read-only score
wiki filter-correct <source-id>                    # pin a corrected example
wiki finalize <page-path> [--abandon]

# New domain
wiki bootstrap-domain "<description>" <slug>       # top-down policy from a description
wiki discover-domains [--untagged]                  # bottom-up clustering of orphan sources
wiki promote-domain <proposal-slug>                 # bless a draft proposal
wiki research "<prompt>" --domain <slug> [--review] [--execute ID]

# NotebookLM (gateway-mediated)
wiki nlm-add <domain> <source-id>
wiki nlm-briefing <domain>
wiki nlm-audio <domain> "<topic>"
wiki nlm-slides <domain> "<topic>"
wiki nlm-revise <slug> --slide <n> "<instructions>"

# Operate
wiki status
wiki serve [--port 7474]                           # local browser UI; /research · /review · /domains/artifacts
wiki watch                                         # foreground; usually launchd runs this
wiki lint [--scope <check>]
wiki poll <name>                                   # run a registered poller (e.g. apple-notes)
wiki poll --list                                   # show registered pollers
wiki backfill-examples --domain X --legacy-config <yaml> --json <staged.json>
wiki finetune [--check | --domain X --distill [--force]]

# Migrate
wiki batch-ingest <vault> --legacy-import --domain <slug> [--dry-run]
```

## 12. Where to read more

- `CLAUDE.md` — agent control surface (auto-loaded by every CC session here)
- `WIKI.md` — full schema reference for frontmatter, page types, lint rules
- `BUILD.md` § 9 — per-milestone delivery record (every commit linked)
- `MIGRATION.md` — how the legacy research-notebook vaults were converted
- `SESSION_TRANSCRIPT.md` — chronological narrative of the v1 build session
