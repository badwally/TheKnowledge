# Glossary

Terms used in the gateway codebase, documentation, and operation guides. One definition per term; links go to the canonical source. See also `WIKI.md` for schema definitions and `CLAUDE.md` for operational rules.

---

**Aggregate framing opener.** A documented allowlist of NotebookLM phrasings that wrap claims without per-claim citations (e.g., "Across these sources..."). Citation grounding tolerates them; the allowlist lives in `src/gateway/validator.py` and is considered a NLM-compatibility shim subject to future tightening. See `WIKI.md § 5`.

**AnthropicAPIClient.** Thin wrapper in `src/gateway/llm/api_client.py` around the Anthropic SDK that records per-call token telemetry (`input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`) and logs them to `log.md` via the K5 telemetry path. Shipped M49.

**Authority ranking.** The `order="authority"` mode of `search_index.search_fts` (default for `wiki retrieve`). Blends BM25 relevance with the SRCH-1 title/slug tier, inbound-link authority (`log1p(inbound)`), a page-kind boost, and a draft penalty, so a term's *canonical* page outranks pages that merely mention it. Weights tuned against the retrieval golden set. Shipped M118.

**Choke-point / Discipline Gate.** The invariant that every write to `wiki/` and `raw/` passes through the gateway so validator, citation grounding, log, index, and lock discipline are always applied. Hard rule #1 of the system; enforced socially today, partially structurally via `assert_safe_for_prompt` and `validate_source_frontmatter_diff`.

**Citation grounding.** Every claim in a wiki page must be followed by `[[sources/<id>]]` linking to the source page. The validator rejects pages that violate this rule; draft mode (see below) downgrades the rule to a warning. See `WIKI.md § 5`.

**CiTO.** Citation Typology Ontology (Shotton 2010). 41 typed citation relations (`supports`, `disputes`, `extends`, `qualifies`, etc.). Not yet adopted in this codebase; a recommended subset is documented in the system review at `docs/reviews/2026-05-23-knowledge-system-review.md § ONT-2`.

**Converter.** A subclass of `Converter` in `src/gateway/converters/` that implements `detect()` and `convert()` for a specific source type (web, youtube, arxiv, pubmed, pdf, voice, audiobook, note, csv, docx, xlsx, pptx, image). Converters write canonical markdown to `raw/<type>/<slug>.md`. See `CLAUDE.md § Adding a new source type`.

**Derived retrieval index (FTS5).** SQLite FTS5 database at `.index/wiki.db` (`src/gateway/search_index.py`) over section-level chunks of `wiki/` + `raw/`, with BM25 + authority ranking. Derived state — gitignored, self-healing on read (mtime/size diff; no write-path hook), rebuilt by `wiki index --rebuild`, never canonical (markdown is source of truth). Serves `wiki search`, `wiki retrieve`, `wiki related`, `wiki context --budget`, and `wiki answer`. Shipped M116.

**Domain proposal lifecycle.** `wiki discover-domains` → draft at `wiki/proposals/<slug>.md` → `wiki promote-domain` → blessed domain with `policy.yaml` and example bank. `wiki demote-domain` reverses a promotion; `wiki reject-proposal` discards a draft proposal without promoting.

**Draft mode.** A page with `draft: true` in frontmatter. Citation grounding is a lint warning rather than a validator error. Finalized via `wiki finalize <page-path>`. Drafts older than 7 days are flagged by `wiki lint`. Shipped as the default for research-driven authoring in M45.1.

**Example bank.** Per-domain corpus of `(source, decision, rationale)` triplets used as few-shot examples in the filter LLM call and (eventually) as fine-tune data when the count crosses ~500. Stored under `.knowledge/policies/<domain>/examples/`. Inspected via `wiki finetune --check`.

**Filter.** Per-source classification (`include` / `review` / `exclude`) using a per-domain `policy.yaml` and example bank. LLM-driven (currently Haiku-tier). Implemented in `src/gateway/filter/semantic.py`. Filter scores are written into source frontmatter as `filter: {score: <float>}` at ingest time. See `WIKI.md § 10`.

**Filter band.** Sources scored between `threshold_review` and `threshold_include` — the human-review queue. Operators override decisions in the band via `wiki filter-correct`.

**Gateway.** The Python service at `src/gateway/` that mediates all reads used in LLM prompts and all writes to `wiki/` and `raw/`. The CLI (`wiki`), MCP server (`wiki mcp-serve`), and web app (`wiki serve`) are surfaces over the same gateway ops layer. See `CLAUDE.md`.

**Golden.** A test case in the per-domain eval framework: a `(question, expected_decision, rationale)` triple stored in `.knowledge/eval/<domain>/goldens.yaml`. The eval framework scores filter decisions against goldens and tracks accuracy per domain version. Shipped M50. See `WIKI.md § QUAL-12`.

**Judge.** The LLM-as-judge component in `src/gateway/evaluate/` that scores filter decisions against a golden set. Calls the Anthropic API with `wiki_context` attached (M50.1 cache_control optimization). Returns a structured `EvalResult`. Shipped M50.

**MoC.** Map of Content. One wiki page per domain (`wiki/mocs/<domain>.md`) that indexes entities, concepts, syntheses, and open threads for that domain. Pattern from the Obsidian community / Zettelkasten lineage. Created automatically by `wiki promote-domain`.

**NotebookLM corpus / notebook.** A persistent Google NotebookLM notebook per domain, populated by `wiki nlm-sync`, used by `wiki query` and `wiki nlm-*` artifact generation ops. Registry at `nlm/notebooks.yaml`. All interactions go through the gateway (hard rule #2).

**OperationResult.** Structured return type from gateway ops (`src/gateway/ops/`): `{"status": "ok" | "error", "message": str, ...}`. Ensures CLI and MCP callers get consistent structured responses. Pattern established in M47.

**Policy.yaml.** Per-domain editorial policy file at `.knowledge/policies/<domain>/policy.yaml`. Contains include/exclude criteria, score thresholds, key entities, and a MoC pointer. Required for `wiki filter` and `wiki research`. Created by `wiki promote-domain` or `wiki bootstrap-domain`.

**Poller.** Subclass of `Poller` in `src/gateway/pollers/` that runs on a schedule (or via `wiki poll <name>`) to pull from API-only sources (Apple Notes, Notion, Slack, Gmail) and write canonical markdown to `raw/<type>/`. Apple Notes shipped M34. See `CLAUDE.md § Adding a new source type`.

**PromptGuardError.** Exception raised by `gateway.paths.assert_safe_for_prompt(path)` when a caller attempts to load `log.md` or `index.md` wholesale into an LLM prompt. Both files are unbounded in size. Shipped M53 (TOK-7). See `CLAUDE.md § Session-state discipline`.

**PROV-O.** W3C Provenance Ontology. `wasDerivedFrom`, `wasGeneratedBy`, `wasAttributedTo`. Vocabulary inspiration for the `synthesizes:` frontmatter field on synthesis pages.

**Query plan.** YAML describing a multi-adapter research run (NotebookLM + web + arXiv + S2 + PubMed). Persisted at `nlm/query_plans/<date>-<slug>.yaml`. Reviewed via `wiki research --review <id>`, executed via `wiki research --execute <id>`.

**Retrieval ladder.** The preferred order for grounding an answer in the wiki, fast to heavy: `wiki retrieve` (ranked, bounded, cited context block; default) → `wiki context` (known page + neighbors) → `wiki answer` (one local grounded LLM call) → `wiki query` (NotebookLM corpus synthesis). Documented in `CLAUDE.md`. Shipped Phase 14 (M116–M121).

**Retrieval golden set.** Paraphrase-style `(query, expected slugs)` pairs at `.knowledge/eval/retrieval/goldens.yaml`, scored by `wiki eval-retrieval` (recall@k, MRR) to govern ranking changes — distinct from the per-domain filter **Golden** above. Shipped M116.

**Scheduler.** Cron-driven job substrate in `src/gateway/scheduler/` and `src/gateway/ops/schedule.py`. Manages polling intervals for pollers and other recurring gateway tasks. Managed via `wiki schedule list/add/remove/enable/disable/run`. Shipped M48.

**Session state.** The file `docs/session-state.md` in this repo. Load-bearing record of open contracts, in-flight edits, session decisions, and the next atomic step across context compactions and session boundaries. The PreCompact hook instructs the agent to write it before context is compressed; the SessionStart hook instructs re-anchor on resume. See `CLAUDE.md § Session-state discipline`.

**Source map.** Translation from NotebookLM's per-query citation numbering back to `raw/<id>` identifiers. Persisted at `nlm/source_maps/<session>.json`. Used by the citation-render step of `wiki research` to generate `[[sources/<id>]]` links in synthesis pages.

**Surface-anchor leakage.** When porting code from a specific-purpose tool to a general-purpose successor, structural decisions tend to get rethought while surface conventions (variable names, prompt templates, schema labels, example content, section headers) are copied forward and silently encode the original domain's assumptions. Documented in `~/.claude/CLAUDE.md § Anti-Pattern Guards`.

**`synthesizes:`** Frontmatter list on synthesis pages (`wiki/synthesis/`) enumerating the source corpus that produced the synthesis, as `[[sources/<id>]]` links. PROV-O-aligned `wasDerivedFrom` semantics. Validator warns when a synthesis page is missing this field.

**TranscriptionResult.** Dataclass in `src/gateway/transcription.py` holding the output of an mlx-whisper transcription run: `text`, `language`, `duration_s`, `model`, `diarized`, `segments`. Cached to `raw/<type>/_transcripts/<sha256hex>.json` after first transcription. Shipped M53 (TOK-6).

**Validator.** `src/gateway/validator.py`. Checks page frontmatter and body against the schema defined in `WIKI.md §§ 3–5`. Called by every gateway write op. Returns a `ValidationResult` with per-finding severity (`ERROR`, `WARNING`, `INFO`). Callers bail on `ERROR`; `WARNING` is logged.

**Watcher.** launchd-managed daemon (`wiki watch`) that monitors `raw/inbox/` for dropped files and routes them through the ingest pipeline. Also surfaces watcher heartbeat and pending-queue counts in `wiki status`.

**Wiki context.** Read-side op (`wiki context <query>`) that returns a wiki page and its N-hop wikilink-resolved neighbors, assembled as a structured context block for LLM prompts. Result includes `cache_control: {type: "ephemeral"}` for prompt caching. Shipped M51 (INT-11). See `WIKI.md § Gateway operations`.
