"""MCP server exposing every gateway operation as a native tool.

Run with `wiki mcp-serve`. Configure in any Claude Code project's MCP config
(typically `.claude/mcp_servers.json` or equivalent) so agents in any
`~/code/*` repo get `wiki_*` tools without shelling out to the CLI.

Same backend as the CLI — every tool delegates to `gateway/ops/*.py`. No
logic duplication; the only difference is the calling surface.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

from gateway.core import OperationResult


_INSTRUCTIONS = """\
Tools for the canonical knowledge base at ~/code/knowledge/.

The wiki is a structured personal KB built from filtered sources. All write
operations on raw/ and wiki/ go through these tools — direct file writes
are forbidden by the schema doc. Read operations on the content layer
(raw/, wiki/, index.md, log.md) can be done with normal file reads since
those paths are stable.

Use `wiki_status` first to orient. `wiki_filter` is read-only and useful
for probing how a candidate source would score before committing to ingest.
`wiki_query` synthesizes an answer across the wiki and files it as a
synthesis page. NotebookLM operations are mediated by `wiki_nlm_*`.
"""


mcp = FastMCP(
    "knowledge-gateway",
    instructions=_INSTRUCTIONS,
)


# CLI ops intentionally without MCP wrappers. The parity test in
# `tests/gateway/test_mcp_parity.py` reads this set and asserts every other
# IMPLEMENTED CLI op has a `wiki_*` tool. Add to this set explicitly when an
# op should remain CLI-only.
#
# - watch, mcp-serve, serve: daemons / servers, not request/response ops
# - migrate: one-shot schema/content migration runs (rare, dangerous)
# - demote-domain: destructive cross-state action (per plan C4 — agents
#   should not autonomously demote blessed domains)
CLI_ONLY: frozenset[str] = frozenset(
    {
        "watch",
        "mcp-serve",
        "serve",
        "migrate",
        "demote-domain",
        # `eval-retrieval` (WS4) is a dev/measurement harness over the golden
        # query set. It scores retrieval quality during development; agents
        # have no reason to invoke it at runtime. CLI-only by design.
        "eval-retrieval",
        # `schedule` is multi-action and runs arbitrary shell commands.
        # Exposing add/remove/enable to agents would let an agent grant
        # itself persistent execution. Keep CLI-only (K4 / wave-2). If
        # read-only introspection is needed, add a `wiki_schedule_list`
        # auxiliary later following the wiki_poll_list pattern.
        "schedule",
        # `auth` mints / revokes bearer tokens for the K3 cloud shim.
        # Agents must NOT be able to grant themselves remote-capture
        # credentials. CLI-only by design.
        "auth",
        # `briefing-cron` is a scheduled maintenance job (AGT-6). Agents
        # should not trigger corpus-wide NLM briefing runs; the scheduler
        # owns invocation. CLI-only by design.
        "briefing-cron",
        # `contradiction-drift` is a nightly snapshot job (TOOL-14).
        # Agents should not trigger corpus-wide LLM contradiction scans;
        # the scheduler owns invocation. CLI-only by design.
        "contradiction-drift",
        # One-time migration ops (ONT-4, ONT-6, ONT-11). Safe to run from CLI only;
        # agents must not trigger bulk wiki rewrites unsupervised.
        "backfill-entity-kinds",
        "backfill-timestamps",
        "backfill-synthesizes",
        "backfill-sources-count",
        "fix-wikilinks",
        # `abandon-stale-drafts` is a bulk destructive maintenance op (M98). Agents
        # must not auto-abandon drafts unsupervised; CLI-only by design.
        "abandon-stale-drafts",
        # Log rotation is a bulk maintenance operation. Scheduler owns invocation.
        "rotate-log",
        # `question` is a multi-action umbrella (new/list); the fine-grained
        # wiki_question_new + wiki_question_list MCP tools are registered as
        # auxiliaries (TOOL-16). The umbrella name has no 1:1 MCP counterpart.
        "question",
    }
)


def _serialize(result: OperationResult) -> dict[str, Any]:
    """Convert an OperationResult to a plain JSON-friendly dict."""
    return {
        "success": result.success,
        "no_op": result.no_op,
        "summary": result.summary,
        "paths_touched": [str(p) for p in result.paths_touched],
        "errors": list(result.errors),
        "warnings": list(result.warnings),
    }


def _resolve_input(value: str) -> str | Path:
    """Match CLI behavior: URL strings pass through; everything else is a path."""
    if value.startswith(("http://", "https://")):
        return value
    return Path(value).expanduser().resolve()


# --- ingest / filter / authorship ------------------------------------------


@mcp.tool()
def wiki_ingest(
    input: str,
    domain: str | None = None,
    with_plan: bool = False,
    draft: bool = False,
) -> dict[str, Any]:
    """Ingest a single source into the canonical wiki.

    `input` is a URL (web converter handles HTTP/HTTPS) or a path to a
    canonical markdown file. `domain` selects the policy for filter scoring.
    `with_plan=True` invokes the wiki authorship agent to update entity/
    concept/synthesis pages. `draft=True` allows partial citations on
    agent-generated pages.
    """
    from gateway.ops.ingest import ingest

    return _serialize(
        ingest(
            _resolve_input(input),
            domain=domain,
            with_plan=with_plan,
            draft=draft,
        )
    )


@mcp.tool()
def wiki_filter(input: str, domain: str | None = None) -> dict[str, Any]:
    """Score a candidate source against a domain's policy without writing.

    Read-only. Returns the score and the agent's rationale. Useful for
    probing how a source would land before committing to ingest.
    """
    from gateway.ops.filter_op import filter_source

    return _serialize(filter_source(_resolve_input(input), domain=domain))


@mcp.tool()
def wiki_filter_correct(
    source_id: str,
    decision: str,
    rationale: str,
    domain: str | None = None,
) -> dict[str, Any]:
    """Override a past filter decision; pin as a corrected example.

    `decision` is "include" or "exclude". The corrected example is added to
    the example bank with `pinned_by: user-correction` so future filter calls
    learn from it.
    """
    from gateway.ops.filter_correct import filter_correct

    return _serialize(
        filter_correct(source_id, decision=decision, rationale=rationale, domain=domain)
    )


@mcp.tool()
def wiki_query(question: str, domain: str | None = None) -> dict[str, Any]:
    """Search the wiki for a question and file a synthesis page with the answer.

    Keyword-narrows scope (optionally restricted to one `domain`), passes
    candidates to the planning agent, and applies the synthesis Plan.
    """
    from gateway.ops.query import query

    return _serialize(query(question, domain=domain))


@mcp.tool()
def wiki_finalize(page_path: str, abandon: bool = False) -> dict[str, Any]:
    """Finalize a draft wiki page: re-validate strict, clear draft fields.

    `abandon=True` deletes the draft page and removes its backlinks instead.
    """
    from gateway.ops.finalize import finalize

    return _serialize(finalize(page_path, abandon=abandon))


@mcp.tool()
def wiki_finalize_batch(
    domain: str | None = None,
    limit: int | None = None,
    execute: bool = False,
    suggest: bool = False,
) -> dict[str, Any]:
    """Batch-finalize stale drafts (Cat A: unresolved_claims == 0).

    Dry-run by default. Pass execute=True to actually finalize.
    domain restricts to drafts whose frontmatter domains includes this value.
    limit caps the number of drafts processed.
    suggest is a Phase C/D stub (not yet wired).
    """
    from gateway.ops.finalize_batch import finalize_batch

    return _serialize(finalize_batch(domain=domain, limit=limit, execute=execute, suggest=suggest))


@mcp.tool()
def wiki_evaluate(
    domain: str | None = None,
    limit: int | None = None,
    scaffold: str | None = None,
) -> dict[str, Any]:
    """Run the M50 evaluation for a domain or scaffold a goldens template.

    domain is required unless scaffold is set.
    limit caps the number of goldens scored.
    scaffold writes a template goldens.yaml for the named domain.
    """
    from gateway.ops.evaluate_op import evaluate_op

    return _serialize(evaluate_op(domain=domain, limit=limit, scaffold=scaffold))


@mcp.tool()
def wiki_context(
    query: str,
    depth: int = 1,
    format: str = "markdown",
    caller: str | None = None,
    budget: int | None = None,
) -> dict[str, Any]:
    """Read-only fetch of a wiki page + N-hop wikilink-resolved neighbors.

    query: slug, path, or title substring.
    depth: how many wikilink hops to follow (default 1).
    format: "markdown" or "json".
    caller: free-form caller identifier (logged to log.md). Required.
    budget: optional max characters (markdown only). Over budget, neighbors
            are authority-ranked (inbound links + domain overlap) and
            truncated rather than dropped, so the root and its most important
            neighbors survive. Use for precise neighborhood expansion around a
            known page; use wiki_retrieve for question-driven retrieval.
    """
    from gateway.ops.context_op import context_op

    return _serialize(
        context_op(query, depth=depth, fmt=format, caller=caller, budget=budget)
    )


@mcp.tool()
def wiki_retrieve(
    query: str,
    domain: str | None = None,
    k: int = 12,
    budget_chars: int = 40_000,
    caller: str | None = None,
) -> dict[str, Any]:
    """Retrieve a bounded, ranked context block answering a question (RAG).

    The default first call for grounding an answer in the wiki: BM25 section
    retrieval over the FTS5 index assembled into one context block, each
    section wrapped in <page path=... section=...> with [[sources/<id>]]
    citations preserved. Deterministic and LLM-free (no NotebookLM quota).

    query: natural-language question or topic.
    domain: optional domain scope.
    k: max sections (default 12).
    budget_chars: max characters in the block (default 40000).
    caller: free-form caller identifier (logged).

    Prefer this over wiki_search (which returns snippets, not usable context)
    and over wiki_query (heavy NotebookLM synthesis that files a page).
    """
    from gateway.ops.retrieve import retrieve_op

    return _serialize(
        retrieve_op(query, domain=domain, k=k, budget_chars=budget_chars, caller=caller)
    )


@mcp.tool()
def wiki_related(query: str, limit: int = 10, caller: str | None = None) -> dict[str, Any]:
    """Pages co-citing the same sources as a target page (graph neighbors).

    Cheap, LLM-free expansion from a known page to its conceptual neighbors,
    ranked by shared-citation count then inbound-link authority. `query`
    resolves like wiki_context (path, slug, or title substring).
    """
    from gateway.ops.retrieve import related_op

    return _serialize(related_op(query, limit=limit, caller=caller))


@mcp.tool()
def wiki_concept_add(
    slug: str,
    canonical_name: str,
    body: str,
    domain: str,
    *,
    draft: bool = False,
    cite_sources: list[str] | None = None,
    force: bool = False,
) -> dict[str, Any]:
    """Author a `wiki/concepts/<slug>.md` page from a markdown body.

    `body` is the page body (no frontmatter). Frontmatter is constructed
    from the args. Validates against the concept schema (frontmatter +
    required sections + citation grounding); refuses to overwrite without
    `force=True`. `cite_sources` populates the `synthesizes:` list as
    `["sources/<id>", ...]`; when set, body must include a matching
    `## Included works` section per the M45 § 3.6 invariant.
    """
    from gateway.ops.concept_add import concept_add

    return _serialize(
        concept_add(
            slug,
            canonical_name=canonical_name,
            body=body,
            domain=domain,
            draft=draft,
            cite_sources=cite_sources,
            force=force,
        )
    )


# --- NotebookLM gateway ----------------------------------------------------


@mcp.tool()
def wiki_nlm_add(domain: str, source_id: str) -> dict[str, Any]:
    """Add a raw source (already in raw/) to the domain's NotebookLM corpus.

    Auto-creates the notebook on first use. Idempotent on repeat. Updates
    the source's `nlm_corpus_ids` frontmatter and the registry's
    sources_count.
    """
    from gateway.ops.nlm import nlm_add

    return _serialize(nlm_add(domain, source_id))


@mcp.tool()
def wiki_nlm_sync(
    domain: str,
    *,
    limit: int | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Sync every raw source tagged with `domain` into its persistent
    NotebookLM corpus. Idempotent and resumable: per-source failures are
    collected and the run continues. Use `dry_run=True` to preview the
    candidate list before paying the network cost.
    """
    from gateway.ops.nlm import nlm_sync

    return _serialize(nlm_sync(domain, dry_run=dry_run, limit=limit))


@mcp.tool()
def wiki_nlm_slides(domain: str, topic: str) -> dict[str, Any]:
    """Generate a slide deck from a domain's NotebookLM corpus and file it
    back as a wiki artifact page with bidirectional links.
    """
    from gateway.ops.nlm import nlm_slides

    return _serialize(nlm_slides(domain, topic))


@mcp.tool()
def wiki_nlm_audio(domain: str, topic: str) -> dict[str, Any]:
    """Generate an audio overview and file as a wiki artifact page."""
    from gateway.ops.nlm import nlm_audio

    return _serialize(nlm_audio(domain, topic))


@mcp.tool()
def wiki_nlm_briefing(domain: str) -> dict[str, Any]:
    """Generate a briefing doc and file as a wiki artifact page."""
    from gateway.ops.nlm import nlm_briefing

    return _serialize(nlm_briefing(domain))


@mcp.tool()
def wiki_nlm_revise(artifact_slug: str, slides: list[str]) -> dict[str, Any]:
    """Revise an existing slide deck.

    `slides` is a list of strings, each formatted as
    `"<slide-num> <instruction>"`. Files the revised deck as a NEW wiki
    artifact page (the original is preserved, per nlm semantics).
    """
    from gateway.ops.nlm import nlm_revise

    return _serialize(nlm_revise(artifact_slug, slides))


# --- inspection ------------------------------------------------------------


@mcp.tool()
def wiki_status() -> dict[str, Any]:
    """Show watcher state, inbox queue, and recent activity from log.md."""
    from gateway.ops.status import status

    return _serialize(status())


@mcp.tool()
def wiki_moc_add(
    slug: str,
    domain: str,
    title: str,
    body: str,
    draft: bool = False,
    force: bool = False,
) -> dict[str, Any]:
    """Author a wiki/mocs/<slug>.md domain map-of-content page.

    ``slug``: page slug, conventionally matches the domain slug.
    ``domain``: domain slug this MOC indexes.
    ``title``: display title (e.g. "condo-software — Map of Content").
    ``body``: page body markdown, no frontmatter. Must contain sections:
    Overview, Key entities, Key concepts, Synthesis pages.
    ``draft``: write as draft (relaxes citation grounding).
    ``force``: overwrite an existing MOC page.
    """
    from gateway.ops.moc_add import moc_add

    return _serialize(moc_add(slug, domain=domain, title=title, body=body,
                               draft=draft, force=force))


@mcp.tool()
def wiki_list_domains(fmt: str = "text") -> dict[str, Any]:
    """List all blessed domains with slug, title, and wiki page count.

    Use this before wiki_query or wiki_context to discover available domain
    slugs without needing to memorise them.  ``fmt``: "text" (aligned table)
    or "json" (array of {slug, title, wiki_pages}).
    """
    from gateway.ops.list_domains import list_domains

    return _serialize(list_domains(fmt=fmt))


@mcp.tool()
def wiki_list_concepts(
    domain: str | None = None,
    kind: str = "concepts",
    fmt: str = "text",
) -> dict[str, Any]:
    """List concept, entity, synthesis, or MOC pages — optionally filtered to one domain.

    Output is tab-separated slug<TAB>name per line (text) or a JSON array.
    Use to check what the wiki already contains before running wiki_query.

    ``kind``: concepts | entities | synthesis | mocs | all.
    ``domain``: domain slug filter; omit for all domains.
    ``fmt``: "text" (TSV) or "json".
    """
    from gateway.ops.list_concepts import list_concepts

    return _serialize(list_concepts(domain=domain, kind=kind, fmt=fmt))


# --- K2 (M47): parity wrappers ---------------------------------------------


@mcp.tool()
def wiki_research(
    prompt: str,
    domain: str | None = None,
    include_local: list[str] | None = None,
    trust_local: bool = False,
    max_results_per_adapter: int = 50,
    draft: bool = False,
    dry_run: bool = False,
    review: bool = False,
    execute_session: str | None = None,
    external_plan_path: str | None = None,
) -> dict[str, Any]:
    """Corpus-constructive research: plan-and-execute multi-adapter search,
    fan out filter, build a NotebookLM session, file syntheses.

    Mirrors all CLI flags per D3. Mutual-exclusivity: `dry_run`, `review`,
    `execute_session`, `external_plan_path` are advisory modes; the
    underlying `research()` op resolves their interaction. Use `dry_run=True`
    first to see the plan before paying network cost.
    """
    from gateway.research.orchestrator import research

    return _serialize(
        research(
            prompt,
            domain=domain,
            include_local=include_local,
            trust_local=trust_local,
            max_results_per_adapter=max_results_per_adapter,
            draft=draft,
            dry_run=dry_run,
            review=review,
            execute_session=execute_session,
            external_plan_path=external_plan_path,
        )
    )


@mcp.tool()
def wiki_lint(scope: str | None = None) -> dict[str, Any]:
    """Run health checks across the wiki.

    Read-only. `scope` narrows to a specific check (e.g., `orphans`,
    `stale_drafts`, `contradictions`, `citation_density`). Omit for the
    full lint pass.
    """
    from gateway.ops.lint import lint

    return _serialize(lint(scope=scope))


@mcp.tool()
def wiki_batch_ingest(
    vault: str,
    legacy_import: bool = False,
    domain: str | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Bulk-ingest a vault directory. Today only `--legacy-import` is wired;
    canonical batch ingest is `wiki ingest <file>` per source.
    """
    from gateway.ops.batch_ingest import batch_ingest

    return _serialize(
        batch_ingest(
            vault,
            legacy_import=legacy_import,
            domain=domain,
            dry_run=dry_run,
        )
    )


@mcp.tool()
def wiki_bootstrap_domain(
    description: str,
    slug: str,
    force: bool = False,
) -> dict[str, Any]:
    """Author a starter policy.yaml + example bank from a natural-language
    description of the domain. Idempotent: re-running with the same
    description hash is a no-op; `force=True` overrides.
    """
    from gateway.ops.bootstrap_domain import bootstrap_domain

    return _serialize(bootstrap_domain(description, slug, force=force))


@mcp.tool()
def wiki_discover_domains(
    scope: str | None = None,
    since: str | None = None,
    untagged: bool = False,
    timeout_s: float | None = None,
) -> dict[str, Any]:
    """Cluster source pages into draft domain proposals (M36).

    Filters combined as AND: `scope` (glob), `since` (ISO-8601 prefix),
    `untagged` (sources without `domains:`).
    """
    from gateway.ops.discover_domains import discover_domains

    return _serialize(
        discover_domains(
            scope=scope,
            since=since,
            untagged=untagged,
            timeout_s=timeout_s,
        )
    )


@mcp.tool()
def wiki_promote_domain(proposal_slug: str) -> dict[str, Any]:
    """Bless a draft domain proposal: write the policy.yaml, back-tag
    member sources with the new domain. Idempotent on re-run."""
    from gateway.ops.promote_domain import promote_domain

    return _serialize(promote_domain(proposal_slug))


@mcp.tool()
def wiki_reject_proposal(proposal_slug: str) -> dict[str, Any]:
    """Delete a draft domain proposal page. Drafts only — `wiki_demote_domain`
    is CLI-only per C4."""
    from gateway.ops.reject_proposal import reject_proposal

    return _serialize(reject_proposal(proposal_slug))


@mcp.tool()
def wiki_cite(
    page_path: str,
    additions: list[dict[str, Any]],
) -> dict[str, Any]:
    """Add `[[sources/<id>]]` citation tokens to specific lines of a wiki page.

    `additions` is a list of objects shaped ``{"line": <int>, "source_id":
    <str>}``. Per C6 — typed object list (not strings) so the JSON-RPC
    surface is unambiguous. Line numbers are file-relative (including
    frontmatter) per D2.
    """
    from gateway.ops.cite import cite

    # Convert from typed dicts to the (line, source_id) tuples that cite() expects.
    pairs: list[tuple[int, str]] = []
    for item in additions:
        try:
            line = int(item["line"])
            source_id = str(item["source_id"])
        except (KeyError, TypeError, ValueError) as e:
            return _serialize(
                OperationResult(
                    success=False,
                    errors=[
                        f"each `additions` entry needs 'line' (int) and 'source_id' (str): {e}"
                    ],
                )
            )
        pairs.append((line, source_id))
    return _serialize(cite(page_path, pairs))


@mcp.tool()
def wiki_backfill_examples(
    domain: str,
    legacy_config: str | None = None,
    json_paths: list[str] | None = None,
    policy_version: str | None = None,
) -> dict[str, Any]:
    """Backfill policy.yaml + example bank for a domain from legacy
    research-notebook artifacts.

    At least one of `legacy_config` (path to the legacy yaml) or
    `json_paths` (list of legacy staged JSONs) must be set.
    """
    from gateway.ops.example_bank import backfill

    if legacy_config is None and not json_paths:
        return _serialize(
            OperationResult(
                success=False,
                errors=["needs at least one of legacy_config or json_paths"],
            )
        )
    legacy_path = Path(legacy_config).expanduser().resolve() if legacy_config else None
    json_path_objs = (
        [Path(p).expanduser().resolve() for p in (json_paths or [])]
    )
    summary = backfill(
        domain_slug=domain,
        legacy_config_path=legacy_path,
        json_paths=json_path_objs,
        policy_version=policy_version,
    )
    # `backfill()` returns a dict, not OperationResult — wrap it for parity.
    return _serialize(
        OperationResult(
            success=not summary.get("errors"),
            summary=f"backfill {domain}: {summary}",
            errors=summary.get("errors", []),
        )
    )


@mcp.tool()
def wiki_finetune(
    domain: str | None = None,
    check: bool = False,
    distill: bool = False,
    threshold: int = 500,
    force: bool = False,
) -> dict[str, Any]:
    """Inspect or distill the per-domain example bank.

    Modes (mutually exclusive):
    - default / `check=True`: report trigger-state across domains (or one
      domain if `domain` set). Read-only.
    - `distill=True`: build a candidate policy version from the example
      bank. Requires `domain`. `force=True` bypasses the threshold check.
    """
    from gateway.ops.finetune import (
        DistillError,
        distill_prompt,
        trigger_state,
        trigger_states_all,
    )

    if distill:
        if not domain:
            return _serialize(
                OperationResult(
                    success=False,
                    errors=["distill mode requires a domain"],
                )
            )
        try:
            result = distill_prompt(
                domain,
                threshold=threshold,
                enforce_threshold=not force,
            )
        except DistillError as e:
            return _serialize(
                OperationResult(success=False, errors=[f"distill failed: {e}"])
            )
        return _serialize(
            OperationResult(
                success=True,
                summary=(
                    f"distilled candidate for {result.domain}: "
                    f"{result.candidate_path} (examples_used={result.examples_used})"
                ),
                paths_touched=[result.candidate_path],
            )
        )

    # check / default: report trigger states
    if domain:
        state = trigger_state(domain, threshold=threshold)
        summary = (
            f"{state.domain}: {state.count}/{state.threshold} "
            f"(ready={state.ready})"
        )
    else:
        states = trigger_states_all(threshold=threshold)
        lines = [
            f"  {s.domain}: {s.count}/{s.threshold} (ready={s.ready})"
            for s in states
        ]
        summary = "fine-tune readiness:\n" + "\n".join(lines)
    return _serialize(OperationResult(success=True, summary=summary))


@mcp.tool()
def wiki_poll(name: str) -> dict[str, Any]:
    """Run a registered poller (e.g., `apple-notes`) to fetch new items.

    See `wiki_poll_list` for available poller names.
    """
    from gateway import pollers

    try:
        poller = pollers.get_poller(name)
    except pollers.UnknownPollerError as e:
        return _serialize(OperationResult(success=False, errors=[str(e)]))

    result = poller.run()
    return _serialize(
        OperationResult(
            success=result.success,
            summary=(
                result.summary
                or f"{name}: fetched={result.fetched} skipped={result.skipped}"
            ),
            errors=list(result.errors or []),
        )
    )


@mcp.tool()
def wiki_cite_add(
    page_path: str,
    claim_text: str,
    source_id: str,
    fuzzy: bool = False,
) -> dict[str, Any]:
    """Add a citation by claim text (K1).

    Resolves `claim_text` to a line via deterministic escalation
    (exact → normalized substring), then delegates to `wiki cite` for
    the actual write. Set `fuzzy=True` to enable LLM-judged fallback
    when deterministic resolution misses (one extra Sonnet/Haiku call;
    off by default).

    Returns ambiguity error when the claim matches multiple lines —
    re-issue with the explicit line number via `wiki_cite`.
    """
    from gateway.ops.cite_add import cite_add

    return _serialize(
        cite_add(
            page_path,
            claim_text=claim_text,
            source_id=source_id,
            fuzzy=fuzzy,
        )
    )


@mcp.tool()
def wiki_edit(
    page_path: str,
    section: str,
    new_body: str,
) -> dict[str, Any]:
    """Replace the body of one named `## Section` in a wiki page (K1).

    Constrained surface: only the body of the named section is replaced;
    frontmatter, the section heading, and every other section stay
    untouched. After the replacement the full validator runs; if it
    rejects, the edit is not written.

    `section` matches case-insensitively against `## <name>` headers.
    `new_body` is markdown for the section body (may be empty).
    """
    from gateway.ops.edit_section import edit_section

    return _serialize(
        edit_section(page_path, section=section, new_body=new_body)
    )


@mcp.tool()
def wiki_poll_list() -> dict[str, Any]:
    """Return the names of all registered pollers. Read-only auxiliary
    tool (no CLI counterpart — `wiki poll --list` covers the CLI side)."""
    from gateway import pollers

    names = pollers.list_pollers()
    return _serialize(
        OperationResult(
            success=True,
            summary="registered pollers:\n" + "\n".join(f"  {n}" for n in names) if names else "no pollers registered",
        )
    )


# --- AGT-14 / QUAL-3 -------------------------------------------------------


@mcp.tool()
def wiki_agent_log(since: str = "24h") -> dict[str, Any]:
    """Show per-agent event counts and top-5 payloads for the given window.

    `since` accepts '24h', '48h', or '7d'.
    """
    from gateway.ops.agent_log import aggregate

    window_map = {"24h": 24, "48h": 48, "7d": 168}
    since_hours = window_map.get(since, 24)
    data = aggregate(since_hours=since_hours)
    lines: list[str] = []
    for agent, stats in sorted(data.items()):
        lines.append(f"{agent}: {stats['count']} event(s)")
        for payload in stats["top_payloads"]:
            if payload:
                lines.append(f"  - {payload}")
    summary = "\n".join(lines) if lines else f"No agent events in the last {since}."
    return _serialize(OperationResult(success=True, summary=summary))


@mcp.tool()
def wiki_contradiction(
    action: str,
    slug: str | None = None,
    severity: str | None = None,
    status: str = "open",
    note: str = "",
) -> dict[str, Any]:
    """List or resolve structured contradiction pages.

    `action`: 'list' or 'resolve'.
    For 'list': `severity` filters by major/minor/methodological; `status`
    filters by open/investigating/resolved/wontfix (default 'open').
    For 'resolve': `slug` is required; `status` must be 'resolved' or
    'wontfix'; `note` is the resolution explanation.
    """
    from gateway.ops.contradiction import list_contradictions, resolve_contradiction

    if action == "list":
        return _serialize(list_contradictions(severity=severity, status=status))
    if action == "resolve":
        if not slug:
            return _serialize(OperationResult(success=False, summary="slug is required for resolve", errors=["missing slug"]))
        return _serialize(resolve_contradiction(slug, status=status, note=note))
    return _serialize(OperationResult(success=False, summary=f"unknown action {action!r}", errors=[f"expected list or resolve"]))


@mcp.tool()
def wiki_publish_notion(
    domain: str,
    include_sources: bool = False,
    include_artifacts: bool = False,
) -> dict[str, Any]:
    """Mirror wiki pages for a domain to a Notion database (INT-12).

    Upserts entities, concepts, synthesis, and MoC pages to a per-domain
    Notion database. Idempotent: re-running converges to current state.
    Archives Notion rows for wiki pages that no longer exist.

    Requires NOTION_TOKEN and NOTION_PARENT_PAGE_ID environment variables.

    `domain`: domain slug to mirror.
    `include_sources`: also sync wiki/sources pages (default False).
    `include_artifacts`: also sync wiki/artifacts pages (default False).
    """
    from gateway.ops.publish_notion import publish_notion

    return _serialize(
        publish_notion(
            domain,
            include_sources=include_sources,
            include_artifacts=include_artifacts,
        )
    )


@mcp.tool()
def wiki_contradiction_sweep(
    domain: str = "",
    week: str = "",
) -> dict[str, Any]:
    """Run a contradiction sweep for a domain (or all blessed domains).

    Detects same-domain opposite-polarity claim pairs and writes a draft
    wiki/synthesis/contradictions-<domain>-<week>.md page. Idempotent:
    skips if the page already exists for this domain+week.

    `domain`: domain slug to sweep (default: all blessed domains).
    `week`: ISO week override e.g. '2026-W22' (default: current week).
    """
    from gateway.ops.contradiction_sweeper import run_contradiction_sweep

    return _serialize(
        run_contradiction_sweep(
            domain=domain or None,
            week=week or None,
        )
    )


@mcp.tool()
def wiki_draft_close(action: str = "run") -> dict[str, Any]:
    """Run the draft-closer agent (AGT-2).

    `action`: 'run' — process all stale drafts: easy wins (≤1 citation per claim) are
    finalized; hard cases (multi-citation lines) are escalated to log.md.
    Returns counts of finalized/escalated/skipped pages.
    """
    from gateway.agents.draft_closer import run_draft_closer

    if action == "run":
        result = run_draft_closer()
        summary = (
            f"draft-closer complete: finalized={result.pages_finalized} "
            f"escalated={result.pages_escalated} skipped={result.pages_skipped}"
        )
        return _serialize(OperationResult(success=True, summary=summary))
    return _serialize(OperationResult(success=False, summary=f"unknown action {action!r}", errors=[f"expected run"]))


@mcp.tool()
def wiki_triage(action: str = "list") -> dict[str, Any]:
    """Manage the inbox-triage review queue (AGT-1).

    `action`: 'list' — return sources in the review-band triage queue.
    Each entry includes source_id, title, domain, filter_score, scored_at.
    """
    from gateway.agents.inbox_triage import triage_list

    if action == "list":
        items = triage_list()
        if not items:
            return _serialize(OperationResult(success=True, summary="triage queue is empty"))
        lines = [f"{i['source_id']}: {i.get('domain','')} score={i.get('filter_score','')} — {i.get('title','')}" for i in items]
        summary = f"{len(items)} source(s) in triage queue:\n" + "\n".join(lines)
        return _serialize(OperationResult(success=True, summary=summary))
    return _serialize(OperationResult(success=False, summary=f"unknown action {action!r}", errors=[f"expected list"]))


@mcp.tool()
def wiki_agents(agent_name: str, action: str = "run") -> dict[str, Any]:
    """Run a named gateway agent on demand (A1 — AGT-1/AGT-2/AGT-14 unified surface).

    `agent_name`: one of 'inbox-triage', 'draft-closer', 'agent-digest'.
    `action`: 'run' (only valid action).

    - inbox-triage: scans raw/ sources lacking a filter score and triages each.
    - draft-closer: auto-finalizes easy-win stale drafts; escalates hard cases to log.md.
    - agent-digest: aggregates 24h agent events and writes a draft synthesis page.
    """
    if action != "run":
        return _serialize(OperationResult(success=False, summary=f"unknown action {action!r}", errors=["expected run"]))

    if agent_name == "inbox-triage":
        from gateway.agents.inbox_triage import run_inbox_triage_batch
        result = run_inbox_triage_batch()
        summary = (
            f"inbox-triage: processed={result.processed} "
            f"skipped={result.skipped} failed={result.failed}"
        )
        return _serialize(OperationResult(success=result.failed == 0, summary=summary))

    if agent_name == "draft-closer":
        from gateway.agents.draft_closer import run_draft_closer
        result = run_draft_closer()
        summary = (
            f"draft-closer: finalized={result.pages_finalized} "
            f"escalated={result.pages_escalated} skipped={result.pages_skipped}"
        )
        return _serialize(OperationResult(success=True, summary=summary))

    if agent_name == "agent-digest":
        from gateway.ops.agent_log import aggregate, build_digest_page
        from datetime import datetime, timezone
        data = aggregate(since_hours=24)
        if not data:
            return _serialize(OperationResult(success=True, summary="agent-digest: no agent events in last 24h"))
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        content = build_digest_page(date_str=date_str)
        from gateway.plan import Plan, WikiUpdate
        from gateway.ops.apply_plan import apply_plan
        slug = f"agent-digest-{date_str}"
        plan = Plan(
            source_id="agent-digest",
            rationale=f"Daily agent-activity digest for {date_str} (AGT-14)",
            updates=[WikiUpdate(
                target_path=f"wiki/synthesis/{slug}.md",
                update_kind="create",
                content=content,
            )],
        )
        op_result = apply_plan(plan, draft=True)
        return _serialize(op_result)

    return _serialize(OperationResult(success=False, summary=f"unknown agent {agent_name!r}", errors=[f"expected inbox-triage, draft-closer, or agent-digest"]))


@mcp.tool()
def wiki_digest(hours: float = 24.0, stale_days: int = 7) -> dict[str, Any]:
    """Daily content brief: new sources, new synthesis, stale drafts, triage queue (INT-14).

    `hours`: look-back window for new sources/synthesis (default 24).
    `stale_days`: draft staleness threshold in days (default 7).

    Returns the markdown digest as a string in `summary`. Never sends anything.
    """
    from gateway.ops.wiki_digest import build_wiki_digest
    content = build_wiki_digest(hours=hours, stale_days=stale_days)
    return _serialize(OperationResult(success=True, summary=content))


@mcp.tool()
def wiki_agenda(
    date: str = "",
    events: list[dict[str, Any]] | None = None,
    write: bool = True,
) -> dict[str, Any]:
    """Calendar-aware meeting-prep briefing (INT-13).

    Assembles a markdown briefing for meetings with ≥2 attendees by looking up
    attendee entity pages and event-topic concept pages in the wiki.

    Typical agent workflow:
      1. Call `mcp__claude_ai_Google_Calendar__list_events` for the target date.
      2. Pass the resulting event list to this tool as `events`.

    `date`: ISO date string (YYYY-MM-DD). Defaults to today.
    `events`: Calendar event dicts in Google Calendar API format.
    `write`: If True (default), write output to wiki/agenda/<date>.md.
    """
    import json as _json
    from datetime import date as _date
    from gateway.ops.wiki_agenda import build_agenda, write_agenda

    date_str = date or _date.today().isoformat()
    ev = events or []
    # events may arrive as JSON string from some MCP clients
    if isinstance(ev, str):
        ev = _json.loads(ev)

    if write:
        out_path = write_agenda(date_str, ev)
        agenda_md = out_path.read_text()
        result = _serialize(OperationResult(
            success=True,
            summary=f"Agenda written to {out_path}",
            paths_touched=[out_path],
        ))
        result["agenda"] = agenda_md
        return result

    content = build_agenda(date_str, ev)
    return _serialize(OperationResult(success=True, summary=content))


def wiki_skill_emit(domain: str) -> dict[str, Any]:
    """Generate `.claude/skills/wiki-<domain>/SKILL.md` for a domain (AGT-13).

    Reads policy.yaml + MOC + recent synthesis titles; writes a deterministic
    skill file with inclusion criteria, key entities/concepts, and open threads.
    Safe to regenerate at any time — idempotent, deterministic, <300 lines.

    `domain`: domain slug (e.g. 'glp1-reward-modulation').
    """
    from gateway.ops.skill_emit import skill_emit

    return _serialize(skill_emit(domain))


@mcp.tool()
def wiki_reingest(source_id: str, new_input: str, domain: str | None = None) -> dict[str, Any]:
    """Re-ingest a revised source, creating a versioned successor linked via supersedes/superseded_by.

    Creates `<source_id>-v2` (or next free version), writes the new source via
    the standard ingest pipeline, and links old ↔ new. Returns the list of wiki
    pages that cite the old source so affected claims can be reviewed.

    `source_id`: ID of the existing source to supersede.
    `new_input`: URL or path to the revised source.
    `domain`: optional domain override for filter scoring.
    """
    from gateway.ops.reingest import reingest

    return _serialize(reingest(source_id, new_input, domain=domain))


@mcp.tool()
def wiki_index(dry_run: bool = False) -> dict[str, Any]:
    """Regenerate index.md with current wiki + raw state.

    Produces a domain-grouped catalog (WIKI.md § 7) with source counts,
    entity/concept/synthesis links per domain, cross-domain pages, and
    a health summary (orphans, inbox).

    `dry_run`: if True, compute and return the result without writing index.md.
    """
    from gateway.ops.index_rebuild import rebuild

    return _serialize(rebuild(dry_run=dry_run))


@mcp.tool()
def wiki_search(
    query: str,
    scope: str = "all",
    domain: str | None = None,
    page_type: str | None = None,
    limit: int = 20,
) -> dict[str, Any]:
    """Full-text search over wiki pages and/or raw sources.

    `query`: Case-insensitive search string.
    `scope`: "wiki", "raw", or "all" (default "all").
    `domain`: Optional domain filter (e.g. "glp1-reward-modulation").
    `page_type`: Optional type filter (e.g. "synthesis", "concept", "web").
    `limit`: Maximum results to return (default 20).

    Returns a dict with `hits` (list of {path, slug, title, page_type, domain,
    score, snippet}), `query`, and `total`.
    """
    from gateway.ops.search import search

    if scope not in ("wiki", "raw", "all"):
        scope = "all"
    result = search(query, scope=scope, domain=domain, page_type=page_type, limit=limit)
    return {
        "query": result.query,
        "total": result.total,
        "hits": [
            {
                "path": str(h.path),
                "slug": h.slug,
                "title": h.title,
                "page_type": h.page_type,
                "domain": h.domain,
                "score": h.score,
                "snippet": h.snippet,
            }
            for h in result.hits
        ],
    }


@mcp.tool()
def wiki_routine(
    routine: str,
    domain: str | None = None,
    date: str | None = None,
    lookback_hours: int = 24,
) -> dict[str, Any]:
    """Run a named orchestration routine.

    `routine`: Name of the routine. Currently supported:
      - "daily-domain-digest": summarize sources ingested in the last lookback_hours
        for one or all blessed domains; write a draft synthesis page per domain.
    `domain`: Optional domain slug. If omitted, runs for all blessed domains.
    `date`: Optional date override YYYY-MM-DD (default: today UTC).
    `lookback_hours`: How many hours back to scan for new sources (default 24).
    """
    if routine == "daily-domain-digest":
        from gateway.ops.daily_digest import run_all_domains, run_daily_domain_digest
        if domain:
            result = run_daily_domain_digest(domain, date_str=date, lookback_hours=lookback_hours)
        else:
            result = run_all_domains(date_str=date, lookback_hours=lookback_hours)
        return _serialize(result)
    return {"success": False, "summary": f"unknown routine: {routine}"}


@mcp.tool()
def wiki_cite_capture(
    quote: str,
    url: str,
    target_page: str = "",
) -> dict[str, Any]:
    """Ingest a URL if needed and add a citation to a wiki page.

    `quote`: The claim text to cite (must appear in target_page).
    `url`:   Source URL. Idempotent — re-runs on an already-ingested URL reuse it.
    `target_page`: Relative path to the wiki page to cite in (e.g.
      ``wiki/concepts/food-noise.md``). Auto-picked by token-overlap if empty.
    """
    from gateway.ops.cite_capture import cite_capture

    return _serialize(cite_capture(quote, url, target_page or None))


@mcp.tool()
def wiki_daily(
    lookback_hours: float = 24.0,
    stale_days: int = 7,
    orphan_limit: int = 30,
) -> dict[str, Any]:
    """Morning triage list: stale drafts, orphan sources, inbox count, recently ingested.

    `lookback_hours`: Look-back window for recently ingested sources (default 24).
    `stale_days`: Draft staleness threshold in days (default 7).
    `orphan_limit`: Max orphan sources to include (default 30).
    """
    import dataclasses
    from gateway.ops.daily_review import run_daily_review

    result = run_daily_review(
        lookback_hours=lookback_hours,
        stale_days=stale_days,
        orphan_limit=orphan_limit,
    )
    return dataclasses.asdict(result)


@mcp.tool()
def wiki_ask_corpus(domain: str, question: str, draft: bool = True) -> dict[str, Any]:
    """Ask the domain's NLM corpus a question and file the answer as a draft synthesis (TOOL-15).

    Simpler interface than wiki_query: domain comes first, defaults to draft=True.
    """
    from gateway.ops.query import query

    return _serialize(query(question, domain=domain, draft=draft))


@mcp.tool()
def wiki_question_new(slug: str, title: str, domain: str, status: str = "open") -> dict[str, Any]:
    """Create a new wiki question page at wiki/questions/<slug>.md (TOOL-16)."""
    from gateway.ops.question import question_new

    return _serialize(question_new(slug, title, domain, status=status))


@mcp.tool()
def wiki_question_list(domain: str | None = None, status: str | None = None) -> list[dict[str, Any]]:
    """List wiki question pages, optionally filtered by domain or status (TOOL-16)."""
    from gateway.ops.question import question_list

    return question_list(domain=domain, status=status)


# --- entry point -----------------------------------------------------------


def run() -> None:
    """Run the MCP server over stdio (FastMCP's default transport)."""
    mcp.run()


if __name__ == "__main__":
    run()
