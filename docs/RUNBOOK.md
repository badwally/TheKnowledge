# Operational Runbook

Day-to-day operations and symptom → remedy mapping. For architecture see `ARCHITECTURE.md`; for usage see `TUTORIAL.md`; for schema see `WIKI.md`.

---

## Common operations

### Start the watcher daemon
```bash
wiki watch   # foreground; launchd manages it in production
```

### Ingest a batch of sources
```bash
wiki batch-ingest <dir> --domain <slug>
wiki batch-ingest <legacy-vault> --legacy-import --domain <slug>
```

### Run health checks
```bash
wiki lint                    # all checks
wiki lint --scope orphans    # targeted check
```

### Rotate the log
```bash
wiki rotate-log                  # archive entries older than 90 days
wiki rotate-log --keep-days 30   # more aggressive
wiki rotate-log --dry-run        # preview only
```

### Rebuild the content index
```bash
wiki index --rebuild
```

### Emit domain skill files
```bash
wiki skill-emit <domain>   # writes .claude/skills/wiki-<domain>/SKILL.md
```

---

## Troubleshooting

### Ingest failures

| Symptom | Cause | Fix |
|---------|-------|-----|
| `no converter handles <input>` | URL scheme or extension not in `SOURCE_TYPES` | Check `WIKI.md § 3.1`; add a converter if needed |
| `source already ingested` | Content hash matches existing raw source | Idempotent; inspect the existing raw file |
| `ingest: filter score below threshold` | Score < `threshold_include` in `policy.yaml` | Review the source; use `wiki filter-correct` to override |
| `TranscriptionError: HF_TOKEN` | Diarization needs Hugging Face auth | `hf auth login` + accept pyannote model terms |
| PDF parse error | Malformed or password-protected PDF | Extract text manually; ingest as a `note` source |

### Authorship / query failures

| Symptom | Cause | Fix |
|---------|-------|-----|
| `wiki query` returns "no wiki pages matched" | Keyword mismatch or empty wiki | Add `--domain`; run more ingests first |
| Plan validation fails with citation errors | Agent wrote claims without `[[sources/<id>]]` | Use `--draft` to allow partial citations; run `wiki finalize` later |
| `synthesizes: requires ## Included works` | Synthesis page missing `## Included works` section | Add section manually or via `wiki edit` |
| `wiki edit` rejects the new body | Validator rule violated (citation density, schema) | Check the error message; fix the body before re-editing |

### NotebookLM

| Symptom | Cause | Fix |
|---------|-------|-----|
| `nlm-*` errors on auth | NotebookLM session expired | `nlm login` |
| `wiki nlm-add` fails for local sources | Source has no `url:` in frontmatter | Use `wiki nlm-add`'s `source_add_text` fallback; add `url:` to frontmatter if available |
| Corpus query returns nothing | Corpus empty or source not synced | `wiki nlm-sync <domain> --dry-run` to check; then `wiki nlm-sync <domain>` |

### MCP

| Symptom | Cause | Fix |
|---------|-------|-----|
| `wiki_*` tools missing in a Claude Code session | MCP server not configured or not running | Restart Claude Code; verify `.mcp.json` points to `wiki mcp-serve` |
| MCP tool returns `success: false` | Op failed; inspect `errors` field | Same diagnosis as CLI; `wiki status` to orient |
| CLI-only op called via MCP | Op is in `CLI_ONLY` frozenset | Use the CLI: `! wiki <op>` in the session prompt |

### Watcher

| Symptom | Cause | Fix |
|---------|-------|-----|
| Files in `raw/inbox/` not being processed | Watcher not running | `wiki watch` foreground or check launchd |
| File moved to `raw/inbox/_failed/` | Conversion or validation error | Read the sidecar `.error` file; fix the source and re-drop |
| Watcher stalls on a large file | Converter timeout | Increase timeout in `ops/ingest.py`; or ingest manually |

### Lint findings

| Check | Severity | Meaning | Remedy |
|-------|----------|---------|--------|
| `orphans` | warning | Source has no inbound wiki citation | Run `wiki query` synthesis loops |
| `stale-drafts` | warning | Draft page > 7 days old | `wiki finalize` or `wiki finalize --abandon` |
| `synthesizes_coverage` | error | Synthesis page missing `synthesizes:` field | `wiki backfill-synthesizes` |
| `broken-wikilinks` | error | `[[link]]` points to nothing | Fix slug or create the target page |
| `retracted-citations` | error | Wiki page cites a retracted source | Update or remove the claim |
| `domain-purity` | warning | Source tagged to multiple blessed domains | Review; use `wiki demote-domain` if promotion was wrong |
| `stale-verified` | error | `statute`/`standard` entity missing `last_verified_at` | Add field via `wiki edit` |

### Pre-commit hook failures

| Message | Fix |
|---------|-----|
| `nlm ` raw invocation detected | Replace with `wiki nlm-*` gateway command |
| Validator errors on staged files | Fix frontmatter; re-stage |

### Lock files

If a `wiki` command crashes, it may leave a lock file at `.knowledge/locks/<name>.lock`. Locks are PID-checked on acquire — if the holding process is dead, the lock is automatically broken. If the lock persists with a live PID that isn't `wiki`, investigate before deleting.

---

## Scheduled jobs

Jobs registered in `.knowledge/schedule.yaml`, run via `wiki schedule run <name>`:

| Job | Schedule | What it does |
|-----|----------|--------------|
| `rotate-log` | `0 3 * * 0` (Sun 03:00 UTC) | Archive `log.md` entries older than 90 days |
| `briefing-cron` | (domain-specific) | Per-domain NLM briefing for all blessed domains |
| `contradiction-sweep` | (weekly) | LLM scan for contradictions → draft synthesis pages |
| `contradiction-drift` | `0 5 * * *` (nightly) | Snapshot + diff contradiction log |

---

## Emergency procedures

### Revert a mistaken `wiki promote-domain`
```bash
wiki demote-domain <domain-slug>   # reverses back-tags; deletes auto-generated policy
```

### Revert a mistaken ingest
```bash
# Source body is immutable — you cannot un-ingest.
# To suppress a source: set filter.user_correction = "exclude" in the raw frontmatter.
wiki filter-correct <source-id>   # interactive correction
```

### Recover from a broken wiki/ write
All wiki writes go through `write_atomic` (temp-then-rename). A crash mid-write leaves the old file intact. If a committed page is broken, use `wiki edit` to fix the body section, or `git revert` the offending commit.

### Reset to last good git state
```bash
git status                          # see what changed
git stash                           # save working changes
git log --oneline -10               # find the good commit
git checkout <sha> -- wiki/<path>   # restore one file
```
