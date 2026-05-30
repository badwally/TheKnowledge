# Obsidian Primer — Knowledge Wiki Integration

A practical guide to getting real value from Obsidian as a retrieval, capture, and orientation layer on top of this knowledge system. The graph view is the least useful thing here.

---

## Contents

1. [What Obsidian actually is in this stack](#1-what-obsidian-actually-is-in-this-stack)
2. [Context window and memory](#2-context-window-and-memory)
3. [Core navigation and retrieval](#3-core-navigation-and-retrieval)
4. [Dataview — zero-LLM inventory queries](#4-dataview--zero-llm-inventory-queries)
5. [Maps of Content (MOCs) as session primers](#5-maps-of-content-mocs-as-session-primers)
6. [Daily notes as a capture surface](#6-daily-notes-as-a-capture-surface)
7. [Canvas — working memory workspace](#7-canvas--working-memory-workspace)
8. [Templater — structured capture](#8-templater--structured-capture)
9. [Callouts and block references](#9-callouts-and-block-references)
10. [Graph view — the right use](#10-graph-view--the-right-use)
11. [Potential expansion areas](#11-potential-expansion-areas)
12. [Plugin stack](#12-plugin-stack)

---

## 1. What Obsidian actually is in this stack

Obsidian opens this directory as a vault. Every `.md` file in `wiki/` and `raw/` becomes a note. Every `[[wikilink]]` the gateway writes becomes a clickable link. Obsidian adds nothing to the data model — it is a read layer and a capture layer on top of the filesystem.

**What Obsidian cannot do here:** write to `wiki/` or `raw/` through the gateway. The gateway's citation grounding and validation rules do not apply to Obsidian's editor. If you write a wiki page directly in Obsidian, it bypasses the validator. Use Obsidian for reading, navigating, capturing notes, and building Dataview dashboards. Use the `wiki` CLI or Claude Code for all authorship.

**Where to open the vault:**
```
File → Open Vault → ~/code/knowledge
```

Set this as your default vault. Every file in the repo is immediately navigable.

---

## 2. Context window and memory

This is the highest-value section.

### The problem

Claude Code sessions have a finite context window. Every `wiki query` call synthesizes from scratch, costs tokens, and creates a new page — even when the answer already exists in 330 synthesis pages and 1194 concept pages. The wiki is a memory store that rarely gets used as one.

### The solution hierarchy

Before firing a `wiki query`, work through this ladder:

**Step 1 — Obsidian search** (instant, zero cost)
`Cmd+Shift+F` → type the topic. If a synthesis or concept page exists, you see it immediately. Read it in Obsidian. Done.

**Step 2 — `wiki context`** (fast, zero LLM cost)
```sh
wiki context "food noise" --caller cli
wiki context "concepts/long-covid" --caller cli
wiki context "mocs/glp1" --caller cli
```
Walks wikilinks from the matched page to depth 2. Returns assembled markdown without any LLM call. If the result is substantive, you have your answer. Only proceed to Step 3 if context comes up short.

**Step 3 — `wiki query`** (slow, LLM cost, creates a new page)
```sh
wiki query "what mechanisms explain GLP-1's effect on food noise?" --domain glp1
```
Use this only when Steps 1 and 2 confirm the wiki does not already have the answer.

### How Obsidian addresses context window pressure

**Pre-flight check.** Searching Obsidian takes 2 seconds. If the synthesis page exists, you load it as context directly (`wiki context`) rather than running a new synthesis. This avoids creating duplicate synthesis pages and burning tokens re-deriving existing knowledge.

**Session priming via MOCs.** At the start of a Claude Code session touching a domain, run:
```sh
wiki context "mocs/orita-cmo" --caller cli
```
The MOC page links to the 5–10 most important concept and synthesis pages for the domain. `wiki context` follows those links and returns everything in one call. One round-trip instead of many.

**Offline reading.** When you read wiki pages in Obsidian, you are loading domain knowledge into your own memory, not into the context window. Decisions you make informed by Obsidian reading do not consume Claude Code tokens.

**Backlinks as scope reduction.** Before asking Claude Code to find related pages, check the Backlinks panel in Obsidian for the relevant concept page. The list of pages that link to it is already computed — no LLM needed.

---

## 3. Core navigation and retrieval

### Wikilink navigation

Every `[[sources/pdf-abc123]]` in a wiki page is a clickable link. Click through to the source summary, then click the raw source link to read the original document.

```
[[concepts/food-noise]]              # jump to concept page
[[entities/carla-kuon]]              # jump to entity
[[sources/pdf-50a1f07b475f]]         # jump to source summary
[[concepts/food-noise|food noise]]   # display text differs from target
```

Click a link: `Cmd+Click` opens in a new pane. `Click` navigates in place.

### Search

`Cmd+Shift+F` — full-text search across all vault files.

Useful search patterns:
```
# find all pages in a domain
path:wiki/concepts "domains: [\"glp1\"]"

# find synthesis pages mentioning a specific entity
path:wiki/synthesis orita

# find pages with a specific source cited
[[sources/pdf-50a1f07b475f]]

# find draft pages
draft: true

# find pages by filter score range (frontmatter search)
filter.score: 0.9
```

### Backlinks panel

`Cmd+Click` on any page → open Backlinks panel in the right sidebar. Shows every wiki page that links to the current one. This is the citation graph from the other direction — useful for finding which synthesis pages drew from a specific source, or which concepts reference a specific entity.

### Local graph

`Cmd+Shift+G` with a page open → local graph for that page, depth adjustable. More useful than the global graph because it shows the actual neighborhood of a concept. Set depth to 2 to see concepts linked by synthesis pages.

---

## 4. Dataview — zero-LLM inventory queries

Dataview is the most underused capability available here. It lets you write SQL-like queries over the YAML frontmatter of every wiki page, returning live tables that update as the corpus grows. Zero LLM calls, zero API cost.

**Install:** Settings → Community Plugins → Browse → "Dataview" → Install → Enable.

Enable JavaScript queries in Dataview settings (needed for more complex views).

### Inventory queries

Create a note at `docs/dashboards/inventory.md` and paste these blocks:

**All synthesis pages for a domain, most recent first:**
````markdown
```dataview
TABLE title, last_updated
FROM "wiki/synthesis"
WHERE contains(domains, "glp1")
SORT last_updated DESC
```
````

**Concept pages with the most citation links (proxy for importance):**
````markdown
```dataview
TABLE canonical_name, length(file.inlinks) AS citations
FROM "wiki/concepts"
SORT length(file.inlinks) DESC
LIMIT 20
```
````

**Sources not yet cited by any wiki page (orphans):**
````markdown
```dataview
TABLE title, filter.score, ingested_at
FROM "wiki/sources"
WHERE length(file.inlinks) = 0
SORT filter.score DESC
```
````

**Draft pages older than 7 days:**
````markdown
```dataview
TABLE title, created_at
FROM "wiki"
WHERE draft = true AND date(created_at) < date(today) - dur(7 days)
SORT created_at ASC
```
````

**Sources added in the last 30 days by domain:**
````markdown
```dataview
TABLE title, domains, filter.score
FROM "wiki/sources"
WHERE date(ingested_at) > date(today) - dur(30 days)
SORT ingested_at DESC
```
````

**All concept pages in a domain, grouped by whether they have synthesis coverage:**
````markdown
```dataview
TABLE canonical_name, length(file.inlinks) AS inbound_links
FROM "wiki/concepts"
WHERE contains(domains, "orita-cmo")
SORT length(file.inlinks) DESC
```
````

### Pre-query check dashboard

The most important dashboard to build. Before any `wiki query`, open this and see if the answer already exists:

````markdown
```dataview
TABLE title, question, last_updated
FROM "wiki/synthesis"
SORT last_updated DESC
LIMIT 30
```
````

This is the 30 most recent synthesis pages. If the topic you're about to query appears here, read the existing page instead of synthesizing again.

### Domain health dashboard

````markdown
```dataview
TABLE 
  length(rows) AS page_count,
  round(average(rows.filter.score), 2) AS avg_score
FROM "wiki/sources"
FLATTEN domains AS domain
GROUP BY domain
SORT page_count DESC
```
````

---

## 5. Maps of Content (MOCs) as session primers

A MOC is a manually curated index page for a domain. It links to the 5–10 most important concept, synthesis, and entity pages, with a one-line description of each. It is the single most effective tool for reducing context window pressure in Claude Code sessions.

**Location:** `wiki/mocs/<domain>.md`

**Anatomy of a good MOC:**
```markdown
---
schema_version: 1
type: moc
slug: glp1
canonical_name: GLP-1 — Map of Content
domains:
- glp1
created_at: '2026-05-01T00:00:00Z'
last_updated: '2026-05-28T00:00:00Z'
---

# GLP-1 — Map of Content

Core mechanism: [[concepts/glp-1-receptor-agonists]] · [[concepts/food-noise]] · [[concepts/reward-blunting]]

Recovery and long-term use: [[concepts/glp-1-cessation-rebound]] · [[concepts/weight-loss-plateau-glp1]]

Key entities: [[entities/novo-nordisk]] · [[entities/eli-lilly]] · [[entities/ozempic]]

Best synthesis pages:
- [[synthesis/2026-04-12-glp1-food-noise-mechanisms]] — mechanistic review, 12 sources
- [[synthesis/2026-04-28-glp1-cardiovascular-evidence]] — CVOT trial summary
- [[synthesis/2026-05-10-glp1-beyond-weight-loss]] — broader indications
```

**How to use in a Claude Code session:**
```sh
wiki context "mocs/glp1" --caller cli
```
This returns the MOC body plus depth-2 expansion of every linked page — a complete domain primer in one command. Compare this to firing 8 separate `wiki context` calls.

**Rule:** Create a MOC for every domain you actively research. Spend 15 minutes after a major ingest to update the MOC with the best new pages. The time investment pays back on every future session.

---

## 6. Daily notes as a capture surface

Daily notes are Obsidian's built-in journal feature. Each day gets a fresh note at a configured path. The value here is using daily notes as a structured inbox that feeds the knowledge pipeline.

**Enable:** Settings → Core Plugins → Daily Notes → Enable.

Configure:
- **New file location:** `raw/inbox/daily/`
- **Template file location:** `docs/templates/daily-note.md` (see Templater section)
- **Date format:** `YYYY-MM-DD`

**Why `raw/inbox/daily/`:** The inbox watcher (`wiki watch`) monitors `raw/inbox/`. Files dropped there are picked up for ingestion. Daily notes written in Obsidian flow directly into the pipeline.

**What to capture in a daily note:**
- Research questions you want the wiki to answer (become `wiki query` candidates)
- Observations from reading (become source annotations)
- Meeting notes (become note-type sources)
- Links to articles worth ingesting (become `wiki ingest` candidates)

**Basic daily note template** (save at `docs/templates/daily-note.md`):
```markdown
---
type: note
source_app: obsidian-vault
title: "Daily note {{date:YYYY-MM-DD}}"
ingested_at: "{{date:YYYY-MM-DDThh:mm:ssZ}}"
domains: []
---

# {{date:YYYY-MM-DD}}

## Questions for the wiki
<!-- wiki query candidates — prefix with ? -->

## Sources to ingest
<!-- URLs or file paths — prefix with > -->

## Observations
<!-- freeform notes -->
```

After writing, the note poller picks it up:
```sh
wiki poll notes
```

Or watch for automatic pickup if `wiki watch` is running.

---

## 7. Canvas — working memory workspace

Canvas is Obsidian's infinite whiteboard. It lets you pull wiki pages onto a canvas, draw connections, add freeform notes, and build a temporary cross-domain view — without creating permanent wiki pages.

**Open:** `Cmd+N` → "New Canvas" or `File → New Canvas`.

**How to use it:**

Drag wiki pages onto the canvas from the file explorer. Connect them with arrows. Add text cards for annotations. Use it as a scratchpad for:
- **Pre-query planning:** lay out what you know before running a synthesis
- **Research sessions:** map which sources cover which claims
- **Cross-domain views:** pull concepts from different domains together temporarily
- **Meeting prep:** assemble the relevant entities and synthesis pages for a briefing

**Key syntax:**
- Drag a file from the left panel onto the canvas → creates an embedded card showing the page content
- Right-click on canvas → Add card → text → add a freeform annotation
- Click the edge of a card → drag to another card → creates a directed arrow
- Right-click an arrow → Add label → annotates the relationship

**Important:** Canvas files are saved as `.canvas` JSON files. They do not feed into the wiki pipeline. Treat them as ephemeral workspaces. If a relationship you find on canvas is worth preserving, create a synthesis page via `wiki query` or add a link in the relevant MOC.

---

## 8. Templater — structured capture

Templater is a community plugin that adds dynamic templates with date functions, file metadata, and cursor positioning. Use it to produce frontmatter-compliant note files that the pipeline can ingest.

**Install:** Settings → Community Plugins → Browse → "Templater" → Install → Enable.

Configure: Settings → Templater → Template folder → `docs/templates/`.

### Meeting notes template

Save at `docs/templates/meeting-note.md`:
```markdown
---
type: note
source_app: obsidian-vault
title: "<% tp.file.title %>"
ingested_at: "<% tp.date.now("YYYY-MM-DDThh:mm:ssZ") %>"
domains: []
---

# <% tp.file.title %>

**Date:** <% tp.date.now("YYYY-MM-DD") %>
**Attendees:** 

## Key points

## Decisions made

## Follow-up questions
<!-- Mark with ? to flag as wiki query candidates -->

## Sources mentioned
<!-- URLs or documents referenced — mark with > to flag for ingest -->
```

Create a new meeting note: `Cmd+P` → "Templater: Create new note from template" → select `meeting-note`.

### Research question template

Save at `docs/templates/research-question.md`:
```markdown
---
type: note
source_app: obsidian-vault
title: "Research: <% tp.file.title %>"
ingested_at: "<% tp.date.now("YYYY-MM-DDThh:mm:ssZ") %>"
domains: []
---

# Research: <% tp.file.title %>

**Question:** 

**Why it matters:** 

**What I already know:** 

**Related wiki pages:**
<!-- [[concepts/...]] [[synthesis/...]] -->

**Sources to check:**
<!-- URLs or existing raw/ sources -->
```

When ready to synthesize:
```sh
wiki query "your question here" --domain <domain> --draft
```

---

## 9. Callouts and block references

### Callouts

Callouts are styled annotation boxes. Use them in daily notes and capture documents to mark items for downstream processing.

```markdown
> [!note] Standard annotation

> [!important] High-priority item

> [!question] Wiki query candidate
> What is the mechanism by which quercetin stabilises mast cells?

> [!todo] Ingest candidate
> https://www.nature.com/articles/...

> [!warning] Contradicts existing wiki claim
> This source says X but wiki/concepts/food-noise.md says Y

> [!summary] Key takeaway
> GLP-1 effect on alcohol use appears dose-dependent
```

### Block references

Every paragraph in a note can be given a stable ID and referenced from other pages.

**Create a block ID:**
```markdown
This is a specific claim I want to reference. ^claim-id-123
```

**Reference it from another page:**
```markdown
[[daily/2026-05-28#^claim-id-123]]
```

**Embed it inline:**
```markdown
![[daily/2026-05-28#^claim-id-123]]
```

Use block references to link a captured observation in a daily note directly to the wiki concept it relates to, without duplicating the text.

### Heading references

```markdown
[[concepts/long-covid#Key claims]]
```

Links directly to the "Key claims" section of the long-covid concept page.

---

## 10. Graph view — the right use

The global graph (`Cmd+G`) shows the full corpus. It is visually impressive and analytically weak at corpus size. Resist using it as a retrieval tool.

**When the global graph is actually useful:**
- After a major ingest batch — check that new pages have connected into the graph and aren't isolated islands
- Identifying domains — clusters of nodes with no cross-cluster links indicate domain silos
- Finding orphans — nodes with no connections are source pages with no wiki authorship yet

**The local graph is more useful.** `Cmd+Shift+G` with a specific page open → set depth to 2 → shows the actual concept neighborhood. Use this before a `wiki query` to see what the wiki already knows around a topic.

**Graph filters** (left sidebar in graph view):
- Filter by tag: `tag:#health` shows only health-domain pages
- Filter by path: `path:wiki/synthesis` shows only synthesis pages
- Color groups: assign different colours to concepts, entities, synthesis pages

---

## 11. Potential expansion areas

### 11a. Obsidian Publish as a read-only team surface

Obsidian Publish ($10/month) hosts a subset of your vault as a public or password-protected website. Candidate use: publish MOC pages, synthesis pages, and entity pages for a domain to give the CMO team read-only access without any gateway or server work. The published site is static — no write access, no MCP, no ingest. Right for "consume the knowledge" use cases, wrong for "contribute to the knowledge" use cases.

**What to publish:**
```
wiki/mocs/orita-cmo.md
wiki/synthesis/...  (orita-cmo domain only)
wiki/concepts/...   (orita-cmo domain only)
wiki/entities/...   (orita-cmo domain only)
```

Exclude `raw/`, `wiki/sources/`, `docs/`, `.knowledge/`.

### 11b. Omnisearch plugin

Omnisearch is a community plugin that provides full-text semantic search across the vault, including PDF content in sidecars. More powerful than the built-in search for large corpora.

**Install:** Settings → Community Plugins → Browse → "Omnisearch".

At corpus size (1.3 GB raw, 3500+ wiki pages), Omnisearch significantly improves the pre-`wiki query` check step. Search becomes a viable alternative to Dataview for ad-hoc retrieval.

### 11c. Tasks plugin for research workflow management

The Tasks plugin adds structured task tracking with due dates, priorities, and filters. Use it in daily notes to track:
- Sources queued for ingest
- `wiki query` calls queued
- MOC pages due for update
- Synthesis pages due for review

```markdown
- [ ] Ingest HubSpot integration paper 📅 2026-05-30 #orita-cmo
- [ ] wiki query "what are HubSpot's native AI capabilities" #orita-cmo
- [ ] Update mocs/orita-cmo with new synthesis pages 📅 2026-06-01
```

Query all open tasks across the vault:
````markdown
```tasks
not done
tags include #orita-cmo
sort by due
```
````

### 11d. Readwise Reader integration

If Readwise Reader is in the stack, its Obsidian plugin syncs highlights and annotations directly into the vault as structured markdown notes. These become candidate sources for `wiki ingest`. The sync is one-directional (Readwise → Obsidian) and creates files in a configurable folder.

Point the sync folder at `raw/inbox/readwise/` and the watcher picks them up automatically.

### 11e. Periodic notes for longitudinal tracking

The Periodic Notes plugin extends daily notes to weekly, monthly, and quarterly reviews. Useful for:
- Weekly: which domains got the most ingest activity? Which synthesis pages were created?
- Monthly: which MOC pages need updating? Which orphan sources should be discharged?
- Quarterly: domain health review via Dataview

Weekly template query:
````markdown
```dataview
TABLE title, domains
FROM "wiki/synthesis"
WHERE date(created_at) > date(today) - dur(7 days)
SORT created_at DESC
```
````

---

## 12. Plugin stack

Recommended install order. All are community plugins unless noted.

| Plugin | Purpose | Priority |
|---|---|---|
| **Dataview** | Frontmatter query engine | Essential |
| **Templater** | Dynamic capture templates | Essential |
| **Daily Notes** | Capture inbox (core plugin) | Essential |
| **Canvas** | Working memory workspace (core plugin) | High |
| **Omnisearch** | Full-text search at scale | High |
| **Tasks** | Research workflow tracking | Medium |
| **Periodic Notes** | Weekly/monthly reviews | Medium |
| **Obsidian Publish** | Team read-only surface | If needed |
| **Readwise Official** | Highlight sync → ingest pipeline | If Readwise in stack |

**Installing community plugins:**
Settings → Community Plugins → Turn off Restricted Mode → Browse → search plugin name → Install → Enable.

---

## Quick reference

| Task | Tool | Command / Syntax |
|---|---|---|
| Check if wiki has an answer | Obsidian search | `Cmd+Shift+F` |
| Load wiki context into Claude session | CLI | `wiki context "<topic>" --caller cli` |
| See what synthesis exists for a domain | Dataview | `FROM "wiki/synthesis" WHERE contains(domains, "x")` |
| Find orphan sources | Dataview | `WHERE length(file.inlinks) = 0` |
| Orient a Claude session on a domain | CLI | `wiki context "mocs/<domain>" --caller cli` |
| Capture a research question | Templater | `Cmd+P` → Create from template → research-question |
| Create a working memory workspace | Canvas | `File → New Canvas` |
| Check concept neighborhood | Local graph | `Cmd+Shift+G` on concept page |
| Navigate wikilinks | Obsidian | `Cmd+Click` on `[[link]]` |
| Reference a specific paragraph | Block ref | `[[page#^block-id]]` |
| Embed a page section | Embed | `![[page#Heading]]` |
