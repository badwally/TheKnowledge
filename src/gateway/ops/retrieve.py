"""`wiki retrieve` — composite RAG primitive (WS2, 2026-06-09 RAG review).

One call that does what an agent previously had to orchestrate by hand
(search → resolve → read → repeat): BM25 section retrieval over the FTS5
index, then assembly of a single bounded context block of the most relevant
sections. Deterministic and LLM-free — no API cost, no NotebookLM quota.

The block is the unit a downstream model consumes:

    <page path="wiki/concepts/order-block.md" section="Mechanism"
          title="Order Block" domain="trading-and-markets" score="3">
    ...section text, with [[sources/<id>]] citations preserved...
    </page>

`[[sources/<id>]]` links survive verbatim so any synthesis built on the
block inherits provenance. Each section is capped (`max_section_chars`) and
the whole block is capped (`budget_chars`) so a few large sections can't
blow the context window — an operational lesson from M1 (the index will
happily return large sections).
"""

from __future__ import annotations

from dataclasses import dataclass

from gateway import log, paths, search_index
from gateway.core import OperationResult

_DEFAULT_BUDGET_CHARS = 40_000
_DEFAULT_MAX_SECTION_CHARS = 4_000
_DEFAULT_K = 12


@dataclass
class RetrievedSection:
    rel_path: str
    slug: str
    title: str
    page_type: str
    domain: str
    heading: str
    text: str
    score: int
    rank: float


def _xml_attr(value: str) -> str:
    return (
        value.replace("&", "&amp;").replace('"', "&quot;")
        .replace("<", "&lt;").replace(">", "&gt;")
    )


def retrieve(
    query: str,
    *,
    domain: str | None = None,
    k: int = _DEFAULT_K,
    budget_chars: int = _DEFAULT_BUDGET_CHARS,
    max_section_chars: int = _DEFAULT_MAX_SECTION_CHARS,
    scope: str = "wiki",
    include_drafts: bool = False,
) -> tuple[str, list[RetrievedSection]]:
    """Assemble a bounded context block for `query`. Returns (block, sections).

    Pure retrieval — no logging, no LLM. `retrieve_op` wraps this for the
    CLI/MCP surface (logging + OperationResult).
    """
    if not query or not query.strip():
        return "", []

    hits = search_index.search_fts(
        query.strip(),
        scope=scope,
        domain=domain,
        limit=k,
        order="bm25",
        include_drafts=include_drafts,
    )

    sections: list[RetrievedSection] = []
    blocks: list[str] = []
    total = 0
    for h in hits:
        text = search_index.section_text(h.rel_path, h.heading)
        if not text:
            continue
        if len(text) > max_section_chars:
            text = text[:max_section_chars].rstrip() + "\n…[section truncated]"
        attrs = (
            f'path="{_xml_attr(h.rel_path)}" '
            f'section="{_xml_attr(h.heading or "(intro)")}" '
            f'title="{_xml_attr(h.title)}"'
        )
        if h.domain:
            attrs += f' domain="{_xml_attr(h.domain)}"'
        attrs += f' score="{h.score}"'
        block = f"<page {attrs}>\n{text}\n</page>"
        if total + len(block) > budget_chars and blocks:
            break
        blocks.append(block)
        total += len(block)
        sections.append(
            RetrievedSection(
                rel_path=h.rel_path, slug=h.slug, title=h.title,
                page_type=h.page_type, domain=h.domain, heading=h.heading,
                text=text, score=h.score, rank=h.rank,
            )
        )

    return "\n\n".join(blocks), sections


def retrieve_op(
    query: str,
    *,
    domain: str | None = None,
    k: int = _DEFAULT_K,
    budget_chars: int = _DEFAULT_BUDGET_CHARS,
    caller: str | None = None,
) -> OperationResult:
    """CLI/MCP entry point: retrieve + log."""
    if not query or not query.strip():
        return OperationResult(success=False, errors=["query is required"])

    block, sections = retrieve(
        query, domain=domain, k=k, budget_chars=budget_chars
    )
    if not sections:
        return OperationResult(
            success=False,
            summary=f"no results for {query!r}"
            + (f" in domain {domain!r}" if domain else ""),
        )

    log.append(
        op="retrieve",
        fields={
            "caller": caller or "",
            "query": query,
            "domain": domain or "",
            "sections": len(sections),
            "chars": len(block),
        },
        summary=(
            f"retrieve: {query!r} domain={domain or '-'} "
            f"sections={len(sections)} chars={len(block)}"
        ),
    )
    return OperationResult(
        success=True,
        paths_touched=[paths.log_path()],
        summary=block,
        data={
            "query": query,
            "domain": domain,
            "section_count": len(sections),
            "chars": len(block),
            "sources": [
                {"path": s.rel_path, "slug": s.slug, "title": s.title,
                 "section": s.heading, "score": s.score}
                for s in sections
            ],
        },
    )
