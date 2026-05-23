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


# --- entry point -----------------------------------------------------------


def run() -> None:
    """Run the MCP server over stdio (FastMCP's default transport)."""
    mcp.run()


if __name__ == "__main__":
    run()
