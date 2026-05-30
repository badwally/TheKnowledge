# Backlog: MOC Pages for Active Domains

**Category:** Editorial / Knowledge Architecture
**Priority:** High
**Effort:** ~1 hour per domain (no code required)
**Trigger to action:** Any domain that is being actively queried in a Claude Code session and lacks a MOC page

---

## Problem

`wiki context mocs/<domain>` is the most efficient session-primer available — one command returns the entire domain map with key concepts, synthesis pages, and entities resolved to depth 2. But the command is only as useful as the MOC page behind it. Currently MOC pages are thin or absent for most domains, making the pre-session orientation step useless.

Without MOC pages:
- Every Claude Code session on a domain starts cold — requiring multiple `wiki context` round-trips to reconstruct the mental model
- `wiki list-concepts --domain X` lists all concepts but provides no curation signal (which ones matter most?)
- Duplicate `wiki query` calls happen because neither the user nor the agent knows what synthesis already exists

## What a good MOC page looks like

A MOC (Map of Content) for a domain is a curated, human-maintained index linking to the 5–10 most important concept, synthesis, and entity pages, with a one-line description of each. It is **not** auto-generated — curation is the point.

**Anatomy:**

```markdown
---
schema_version: 1
type: moc
slug: <domain>
canonical_name: <Domain> — Map of Content
domains:
- <domain>
created_at: '<ISO timestamp>'
last_updated: '<ISO timestamp>'
---

# <Domain> — Map of Content

## Core mechanisms
- [[concepts/X]] — one-line description of why this concept is central
- [[concepts/Y]] — ...

## Key synthesis
- [[synthesis/YYYY-MM-DD-slug]] — what question it answers, how many sources
- [[synthesis/YYYY-MM-DD-slug]] — ...

## Key entities
- [[entities/X]] — role in domain

## Open questions
<!-- wiki query candidates not yet synthesised -->
```

## Domains requiring MOC pages (priority order)

| Domain | Pages | Status | Notes |
|---|---|---|---|
| `trading-and-markets` | 704 | Missing | Largest domain — highest return on MOC investment |
| `condo-software` | 465 | Missing | |
| `ai-and-agents` | 263 | Missing | Actively referenced from other projects |
| `risksystems` | 289 | Missing | |
| `condo-capital-infra` | 197 | Missing | |
| `edge-ai-agentic` | 143 | Missing | |
| `glp1-reward-modulation` | 107 | Missing | Health domain — personal use |
| `orita-cmo` | 47 | Missing | CMO team use case |
| `cycling-and-fitness` | 72 | Missing | |
| `condo` | 53 | Missing | |

## How to write a MOC

1. Run `wiki list-concepts --domain <slug> --kind all` to see all pages in the domain
2. Open the top synthesis pages in Obsidian and read their summaries
3. Write the MOC page via the gateway:

```sh
wiki concept-add <domain> --body "$(cat /tmp/moc-draft.md)"
```

Or more practically: use `wiki query` with a meta-question to draft it, then hand-edit:

```sh
wiki query "What are the most important concepts, synthesis pages, and open questions in the <domain> domain?" --domain <domain> --draft
```

Then finalize with `wiki finalize` after editing.

4. After writing, verify with:

```sh
wiki context "mocs/<domain>" --caller cli
```

The output should be substantive enough to orient a fresh Claude Code session on the domain.

## Maintenance rule

Update the MOC after any `wiki query` run that produces a synthesis page worth featuring, or after any `wiki batch-ingest` that adds a significant source cluster. Treat the MOC as the domain's table of contents — it should reflect what's worth reading, not everything that exists.
