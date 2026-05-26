# gateway.research

The research package implements the `wiki research` pipeline: a corpus-constructive loop that searches multiple adapters, filters candidates against a domain policy, converts accepted sources, runs analysis via a temporary NotebookLM session, and files results back to the wiki through `ops.apply_plan`. The orchestrator in `orchestrator.py` wires all stages together; the other modules are factored sub-concerns (query planning, session lifecycle, source deduplication, analysis). No module in this package writes directly to `wiki/` or `raw/` — sources flow through `core.write_atomic` and wiki pages flow through `apply_plan`, preserving hard rule #1.

See `ARCHITECTURE.md` for the full pipeline stages and `WIKI.md § 11` for the research operation contract.

## Files

| File | Purpose |
|------|---------|
| `__init__.py` | Package exports |
| `orchestrator.py` | `research()` — top-level pipeline: search → filter → convert → NLM → analyze → file |
| `session.py` | `make_session_id()`, `promote()`, `abandon()` — NotebookLM session lifecycle |
| `query_planner.py` | Generates per-adapter query sets from a natural-language research prompt |
| `query_plan_store.py` | Persists query plans to `nlm/query_plans/` for review and re-execution |
| `source_map.py` | Builds and resolves the NLM-title → source-id map at `nlm/source_maps/` |
| `analysis.py` | Taxonomy construction, per-branch synthesis, cross-cutting analysis |
| `adapters/` | Search adapter implementations (web, arXiv, PubMed, local-files, etc.) |

## Worked example: `wiki research "GLP-1 receptor agonist mechanisms" --domain glp1`

```
Input:  prompt="GLP-1 receptor agonist mechanisms", domain="glp1"
Call:   research.orchestrator.research(prompt, domain="glp1", ...)

1. _infer_domain() confirms "glp1" is a registered domain slug
2. query_planner generates per-adapter query sets:
   {"web": ["GLP-1 receptor agonist mechanism site:nih.gov", ...],
    "arxiv": ["GLP1 receptor agonist neural mechanism"], ...}
3. query_plan_store.save() persists plan to nlm/query_plans/<session_id>.yaml
4. _fan_out_search() runs all enabled adapters in a ThreadPoolExecutor:
   - Each adapter.search(query) returns list[CandidateItem]
   - Results merged; URL-keyed dedup applied
5. _run_filter() scores each candidate against domain policy via FilterClient
   - Accepted: score >= policy.threshold
   - Parallel filter workers (WIKI_FILTER_MAX_WORKERS, default 8)
6. _materialize() converts accepted candidates:
   - converters.dispatch(item.url) → converter
   - converter.convert(url) → canonical markdown
   - write_atomic(raw_path, text) writes to raw/
7. NlmClient creates ephemeral NotebookLM session (session.make_session_id())
8. Materialized sources added to NLM session via nlm_client
9. analysis.run() builds taxonomy, per-branch synthesis, cross-cutting themes
10. Plan built from analysis output (plan.Plan with WikiUpdate entries)
11. apply_plan(plan) writes synthesis pages to wiki/ (hard rule #1 preserved)
12. session.promote() rolls session sources into persistent domain notebook
13. log.append("research", ...) records full run by session_id
Output: OperationResult(success=True, data={"session_id": "...", "pages_filed": 4, ...})

Failure modes (steps 1-7):
- No adapters enabled → OperationResult(success=False, errors=["no search adapters enabled"])
- All candidates filtered out → OperationResult(success=False, errors=["0 sources passed filter"])
- ConversionError on all sources → OperationResult(success=False, errors=["no sources materialized"])

Failure modes (steps 8-13):
- NLM or analysis fails → session.abandon() called; session state preserved for forensics
  → OperationResult(success=False, errors=["analysis failed: ..."])
- apply_plan fails → same abandon path
```
