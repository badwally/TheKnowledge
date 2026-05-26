---
name: wiki-ingest-triage
description: Triage a URL, PDF, or file for ingestion into the knowledge wiki — assess fit, pick domain, run ingest
triggers: [wiki-ingest-triage, wiki ingest-triage]
---

## What This Does

Evaluates whether a source belongs in the wiki, picks the right domain, and
runs `wiki ingest`. Covers the full triage loop: fit check → domain selection →
ingest → confirm frontmatter.

Reference conventions: WIKI.md § 3 (source types), § 9 (hard rules), § 10 (filter policy).

## Usage

```
/wiki-ingest-triage <url-or-path>          # Triage a single source
/wiki-ingest-triage <url> --domain glp1   # Skip domain selection, use glp1
```

## Execution Steps

1. **Identify source type**: Determine type from URL/path extension per WIKI.md § 3.1.
   Supported: `web`, `youtube`, `arxiv`, `pubmed`, `pdf`, `voice`, `note`, `image`, etc.

2. **Assess fit**: Ask one question — does this source contribute novel, citable
   evidence to any existing domain? If no, say so and stop.

3. **Select domain**: Run `wiki status` to see active domains. Match source topic
   to the best-fit domain slug. If ambiguous, ask the user.

4. **Plan before ingest** (hard rule — WIKI.md § 9): State which pages will be
   created before running any command.

5. **Run ingest**:
   ```
   .venv/bin/wiki ingest <path-or-url> --domain <slug>
   ```
   Add `--draft` if the source needs citation review before finalization.

6. **Confirm**: Read the created raw page and wiki/sources page. Verify frontmatter
   has `domains:`, `content_hash:`, `ingested_at:`. Report the source ID.

## Key constraints

- Never write directly to `wiki/` or `raw/`. All writes go through the gateway (WIKI.md § 9).
- Large batches (50+ sources) belong in `wiki batch-ingest`, not this skill.
- If the source type is unsupported, report the gap — don't attempt a manual write.
