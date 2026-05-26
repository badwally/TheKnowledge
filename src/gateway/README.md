# gateway

The gateway package is the sole authorized write path for the personal knowledge base at `~/code/knowledge/`. It enforces three structural invariants: all writes to `wiki/` and `raw/` go through gateway operations (never direct file writes); every write uses `locking.file_lock(name)` for atomic, exclusive access via `core.write_atomic`; and the validator runs before every write so malformed frontmatter or wikilinks are rejected at the boundary. The return type for every operation is `core.OperationResult`.

See `ARCHITECTURE.md` for the layer diagram and `WIKI.md` for the frontmatter schema and page conventions.

## Top-level modules

| File | Purpose |
|------|---------|
| `__init__.py` | Package version declaration |
| `cli.py` | `wiki` CLI entry point; dispatches subcommands to `ops/` |
| `core.py` | `OperationResult`, `write_atomic`, `claude_cli_env` |
| `validator.py` | Frontmatter schema checks, wikilink validation, immutability guard |
| `frontmatter.py` | YAML frontmatter parse/serialize; `FrontmatterError` |
| `paths.py` | Canonical path constants: `wiki_dir()`, `raw_source_path()`, `SOURCE_TYPES` |
| `locking.py` | `file_lock(name)` context manager — exclusive per-operation locks |
| `log.py` | `log.append(op, fields, summary)` — append-only `log.md` writer |
| `index.py` | `index.update_for()` — maintains `index.md` after every ingest |
| `plan.py` | `Plan`, `PlanClient`, `build_plan_prompt`, `parse_plan_response` |
| `wiki_pages.py` | `PAGE_SCHEMAS` — registered wiki page types and their directories |
| `watcher.py` | Filesystem watcher: picks up new files in `raw/` and calls ingest |
| `scheduler.py` | Cron/launchd shim for `wiki poll` |
| `mcp_server.py` | FastMCP server exposing gateway ops as MCP tools |
| `events.py` | Internal event bus (M56) for cross-op notifications |
| `vlm.py` | Vision-language model helper for image source ingestion |
| `transcription.py` | Audio transcription helper for voice/audiobook converters |
| `nlm_client.py` | `NlmClient` Protocol + concrete implementation for NotebookLM API |
| `nlm_registry.py` | Domain ↔ NotebookLM notebook ID map backed by `nlm/notebooks.yaml` |
| `citations.py` | Citation suggestion utilities |
| `contradictions_log.py` | Append-only log for detected contradictions |
| `slugmap.py` | Slug ↔ path resolution helpers |
| `frontmatter.py` | (see above) |
| `costs.py` | LLM cost tracking helpers |

## Worked example: ingest a URL

```
Input:  "https://arxiv.org/abs/2403.12345"
Call:   ops.ingest.ingest("https://arxiv.org/abs/2403.12345", domain="glp1")

1. ingest() sees an https:// prefix → calls ingest_url()
2. ingest_url() calls converters.dispatch(url) → returns ArxivConverter
3. ArxivConverter.convert(url) fetches abstract, returns canonical markdown string
4. _ingest_canonical_text() calls frontmatter.parse(text) → (front, body)
5. validator.validate_source_frontmatter(front) runs; rejects if id/type/title missing
6. validator.validate_content_hash(front, body) confirms SHA-256 matches
7. file_lock("ingest-arxiv-2403.12345") acquired
8. validator.validate_source_immutability() passes (new source, no existing raw file)
9. write_atomic(raw_target, text) writes raw/arxiv/arxiv-2403.12345.md
10. wiki source page written to wiki/sources/arxiv-2403.12345.md
11. index.update_for(source_id, ...) updates index.md
12. log.append("ingest", ...) appends to log.md
13. Lock released
Output: OperationResult(success=True, paths=["raw/arxiv/arxiv-2403.12345.md", ...])

Failure modes:
- No converter matched       → OperationResult(success=False, errors=["no converter for ..."])
- ConversionError            → OperationResult(success=False, errors=["conversion failed: ..."])
- Validator rejects          → OperationResult(success=False, errors=["missing required field: id"])
- Body modified on re-ingest → OperationResult(success=False, errors=["source body is immutable"])
```
