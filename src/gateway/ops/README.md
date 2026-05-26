# gateway.ops

The ops package contains one module per gateway operation — the authoritative implementations of every `wiki <subcommand>`. Each module's public entry point accepts plain Python arguments, acquires locks where needed, calls the validator, delegates writes to `core.write_atomic`, updates `index.md` and `log.md`, and returns an `OperationResult`. No op module writes directly to `wiki/` or `raw/` except through `write_atomic` or `apply_plan`. This is the enforcement boundary for hard rule #1 in `CLAUDE.md`.

See `ARCHITECTURE.md` for the full nine-step write protocol that every op follows.

## Files

| File | Entry point(s) | Purpose |
|------|---------------|---------|
| `ingest.py` | `ingest()`, `ingest_url()`, `ingest_file()`, `ingest_canonical()` | Single-source ingest pipeline |
| `batch_ingest.py` | `batch_ingest()` | Multi-source batch ingest with parallelism |
| `query.py` | `query()` | Answer a question and file a synthesis page |
| `filter_op.py` | `filter_op()` | Run the semantic filter on a source |
| `filter_correct.py` | `filter_correct()` | Pin a corrected filter decision |
| `finalize.py` | `finalize()` | Promote a draft page to finalized |
| `finalize_batch.py` | `finalize_batch()` | Bulk-finalize drafts matching criteria |
| `cite.py` | `cite()` | Add a citation wikilink to a page |
| `cite_add.py` | `cite_add()` | Low-level citation insertion |
| `cite_suggest.py` | `cite_suggest()` | LLM-assisted citation suggestion |
| `edit_section.py` | `edit_section()` | Replace a named section body in a wiki page |
| `lint.py` | `run_lint()` | Compose all lint checks; write report |
| `status.py` | `status()` | Watcher heartbeat + queue summary |
| `migrate.py` | `migrate()` | Import from legacy Obsidian vaults |
| `nlm.py` | `nlm_slides()`, `nlm_audio()`, `nlm_briefing()`, `nlm_add()`, `nlm_sync()`, `nlm_revise()` | NotebookLM artifact generation (opt-in only) |
| `apply_plan.py` | `apply_plan()` | Write a set of wiki pages from a structured `Plan` |
| `bootstrap_domain.py` | `bootstrap_domain()` | Create a new domain from a natural-language description |
| `discover_domains.py` | `discover_domains()` | Detect candidate domains in unsorted raw sources |
| `promote_domain.py` | `promote_domain()` | Bless a draft proposal as a real domain |
| `demote_domain.py` | `demote_domain()` | Reverse a domain promotion |
| `reject_proposal.py` | `reject_proposal()` | Delete a draft domain proposal |
| `concept_add.py` | `concept_add()` | Create a concept wiki page |
| `contradiction.py` | `contradiction()` | File or resolve a contradiction page |
| `context_op.py` | `context_op()` | Build LLM-safe wiki context for a query |
| `evaluate_op.py` | `evaluate_op()` | Run eval suite for a domain |
| `example_bank.py` | `example_bank()` | Inspect / distill the filter example bank |
| `finetune.py` | `finetune()` | Trigger detection + distilled-prompt extraction |
| `agent_log.py` | `agent_log()` | Read/write the structured agent activity log |
| `policy_validator.py` | Internal — validates domain policy YAML |

## Worked example: `wiki ingest` for a canonical `.md` file

```
Input:  Path("raw/web/my-article.md") — already-canonical markdown written by a converter
Call:   ops.ingest.ingest(Path("raw/web/my-article.md"), domain="glp1")

1. ingest() sees a local .md path → calls ingest_canonical(path)
2. ingest_canonical() reads path.read_text() → calls _ingest_canonical_text(text)
3. frontmatter.parse(text) → (front, body)
4. validator.validate_source_frontmatter(front): checks id, type, title, date, content_hash
5. validator.validate_content_hash(front, body): SHA-256 of body matches front["content_hash"]
6. validator.validate_wikilinks(body): all [[wikilinks]] use valid syntax
7. file_lock("ingest-web-my-article") acquired (blocks concurrent ingests of same id)
8. raw_target = paths.raw_source_path("web", "web-my-article")
9. raw_target.exists() → True; validator.validate_source_immutability() confirms body unchanged
10. front["content_hash"] matches existing → idempotency check: wiki/sources page missing?
    - Yes → write_atomic(wiki_target, _make_source_page(existing_front))
    - No  → no-op
11. index.update_for(source_id, source_type, title, domains) patches index.md
12. log.append("ingest", fields={...}, summary="backfilled wiki/sources/web-my-article.md")
13. Lock released
Output: OperationResult(success=True, paths=["wiki/sources/web-my-article.md"])

Failure modes:
- input_path does not exist          → OperationResult(success=False, errors=["input not found: ..."])
- frontmatter.parse raises           → OperationResult(success=False, errors=["frontmatter: ..."])
- validator rejects                  → OperationResult(success=False, errors=["missing required field: id"])
- body has changed since first ingest → OperationResult(success=False, errors=["source body is immutable: ..."])
```
