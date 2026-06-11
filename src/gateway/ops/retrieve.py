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

import math
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


def _merge_domains(
    query: str, domains: list[str], k: int, *, order: str, include_drafts: bool, scope: str,
) -> list:
    """Per-domain quota + round-robin interleave, de-duped by rel_path.

    Runs one search per named domain at quota ceil(k/N), then interleaves by
    per-domain rank so byte-budget truncation downstream preserves balance
    rather than collapsing toward the lexically-dominant domain.
    """
    n = len(domains)
    quota = math.ceil(k / n)
    per_domain = [
        search_index.search_fts(
            query, scope=scope, domain=d, limit=quota,
            order=order, include_drafts=include_drafts,
        )
        for d in domains
    ]
    merged: list = []
    seen: set[str] = set()
    for rank in range(quota):
        for hits in per_domain:
            if rank < len(hits) and hits[rank].rel_path not in seen:
                seen.add(hits[rank].rel_path)
                merged.append(hits[rank])
    return merged[:k]


def retrieve(
    query: str,
    *,
    domain: str | None = None,
    domains: list[str] | None = None,
    k: int = _DEFAULT_K,
    budget_chars: int = _DEFAULT_BUDGET_CHARS,
    max_section_chars: int = _DEFAULT_MAX_SECTION_CHARS,
    scope: str = "wiki",
    include_drafts: bool = False,
) -> tuple[str, list[RetrievedSection]]:
    """Assemble a bounded context block for `query`. Returns (block, sections).

    Pure retrieval — no logging, no LLM. `retrieve_op` wraps this for the
    CLI/MCP surface (logging + OperationResult). When `domains` names ≥2
    domains, the block is balanced by a per-domain quota merge (ceil(k/N) each,
    round-robin-interleaved) instead of a single global k-window that collapses
    toward the lexically-dominant domain. `domains` takes precedence over the
    single `domain`.
    """
    if not query or not query.strip():
        return "", []

    multi = [d for d in (domains or []) if d and d.strip()]
    if len(multi) >= 2:
        hits = _merge_domains(
            query.strip(), multi, k,
            order="authority", include_drafts=include_drafts, scope=scope,
        )
    else:
        single = multi[0] if multi else domain
        hits = search_index.search_fts(
            query.strip(),
            scope=scope,
            domain=single,
            limit=k,
            order="authority",  # WS5: lift canonical pages over mere mentions
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


def related_op(query: str, *, limit: int = 10, caller: str | None = None) -> OperationResult:
    """Find pages co-citing the same sources as a target page (WS5).

    `query` resolves to a page the same way `wiki context` does (path, slug,
    or title substring). Returns a ranked co-citation list — useful for an
    agent to expand from a known page to its conceptual neighbors without an
    LLM call.
    """
    from gateway.ops.context_op import _resolve_target, NoMatchError, AmbiguousQueryError

    try:
        target = _resolve_target(query)
    except (NoMatchError, AmbiguousQueryError) as e:
        return OperationResult(success=False, errors=[str(e)])

    rel = str(target.relative_to(paths.knowledge_root()))
    related = search_index.related_pages(rel, limit=limit)
    if not related:
        return OperationResult(
            success=True,
            summary=f"no co-citation neighbors for {rel}",
            data={"target": rel, "related": []},
        )

    lines = [f"Related to {rel} (by shared citations):"]
    for r in related:
        lines.append(
            f"  [{r.shared} shared, {r.inbound_count} inbound] "
            f"{r.rel_path} — {r.title}"
        )
    return OperationResult(
        success=True,
        summary="\n".join(lines),
        data={
            "target": rel,
            "related": [
                {"path": r.rel_path, "slug": r.slug, "title": r.title,
                 "type": r.page_type, "shared": r.shared, "inbound": r.inbound_count}
                for r in related
            ],
        },
    )


def retrieve_op(
    query: str,
    *,
    domain: str | None = None,
    domains: list[str] | None = None,
    k: int = _DEFAULT_K,
    budget_chars: int = _DEFAULT_BUDGET_CHARS,
    caller: str | None = None,
) -> OperationResult:
    """CLI/MCP entry point: retrieve + log."""
    if not query or not query.strip():
        return OperationResult(success=False, errors=["query is required"])

    domain_label = ",".join(domains) if domains else (domain or "")
    block, sections = retrieve(
        query, domain=domain, domains=domains, k=k, budget_chars=budget_chars
    )
    if not sections:
        return OperationResult(
            success=False,
            summary=f"no results for {query!r}"
            + (f" in domain {domain_label!r}" if domain_label else ""),
        )

    log.append(
        op="retrieve",
        fields={
            "caller": caller or "",
            "query": query,
            "domain": domain_label,
            "sections": len(sections),
            "chars": len(block),
        },
        summary=(
            f"retrieve: {query!r} domain={domain_label or '-'} "
            f"sections={len(sections)} chars={len(block)}"
        ),
    )
    return OperationResult(
        success=True,
        paths_touched=[paths.log_path()],
        summary=block,
        data={
            "query": query,
            "domain": domain_label or None,
            "section_count": len(sections),
            "chars": len(block),
            "sources": [
                {"path": s.rel_path, "slug": s.slug, "title": s.title,
                 "section": s.heading, "score": s.score}
                for s in sections
            ],
        },
    )
