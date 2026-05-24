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
    {"watch", "mcp-serve", "serve", "migrate", "demote-domain"}
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


# --- entry point -----------------------------------------------------------


def run() -> None:
    """Run the MCP server over stdio (FastMCP's default transport)."""
    mcp.run()


if __name__ == "__main__":
    run()
