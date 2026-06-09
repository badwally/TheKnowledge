"""Full-text search over wiki/ and raw/ markdown files (SRCH-1 / WS1).

Backed by the SQLite FTS5 derived index (`gateway.search_index`): BM25
ranking over section-level rows, self-healing against the filesystem on
every call. The public contract is unchanged — `search()` still returns a
`SearchResult` of `SearchHit`s with the SRCH-1 integer tiers (3 title /
2 slug / 1 body) so existing CLI and MCP consumers and their ordering
survive. WS1 added `order="bm25"` for pure lexical ranking.

Search scope:
  "wiki"  — wiki/ subtree only (entities, concepts, synthesis, mocs, sources)
  "raw"   — raw/ subtree only (source documents)
  "all"   — both (default)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

from gateway import paths, search_index


Scope = Literal["wiki", "raw", "all"]

_MAX_SNIPPET = 120
_DEFAULT_LIMIT = 20


@dataclass
class SearchHit:
    path: Path
    slug: str
    title: str
    page_type: str          # source type or wiki page type
    domain: str             # first domain, or ""
    score: int              # 1=body, 2=slug, 3=title
    snippet: str            # surrounding context line(s)


@dataclass
class SearchResult:
    hits: list[SearchHit] = field(default_factory=list)
    query: str = ""
    total: int = 0


def search(
    query: str,
    *,
    scope: Scope = "all",
    domain: str | None = None,
    page_type: str | None = None,
    limit: int = _DEFAULT_LIMIT,
    order: Literal["tiered", "bm25"] = "tiered",
) -> SearchResult:
    """Search wiki/ and/or raw/ for `query` via the FTS5 index.

    Args:
        query: Search string. Tokenized; each token prefix-matched, OR-joined.
        scope: "wiki", "raw", or "all".
        domain: Filter hits to pages tagged with this domain.
        page_type: Filter hits to pages of this type (e.g. "synthesis", "web").
        limit: Maximum number of hits to return (default 20).
        order: "tiered" (SRCH-1 tier then BM25) or "bm25" (relevance only).

    Returns:
        SearchResult with hits sorted per `order`.
    """
    if not query or not query.strip():
        return SearchResult(query=query)

    index_hits = search_index.search_fts(
        query.strip(),
        scope=scope,
        domain=domain,
        page_type=page_type,
        limit=limit,
        order=order,
    )

    root = paths.knowledge_root()
    hits = [
        SearchHit(
            path=root / h.rel_path,
            slug=h.slug,
            title=h.title,
            page_type=h.page_type,
            domain=h.domain,
            score=h.score,
            snippet=_truncate(h.snippet) if h.snippet else _truncate(h.title),
        )
        for h in index_hits
    ]
    return SearchResult(hits=hits, query=query, total=len(hits))


def _truncate(text: str, max_len: int = _MAX_SNIPPET) -> str:
    if len(text) <= max_len:
        return text
    return text[:max_len - 1] + "…"


def format_results(result: SearchResult, *, relative_to: Path | None = None) -> str:
    """Format SearchResult as a human-readable string."""
    if not result.hits:
        return f"No results for {result.query!r}."

    lines = [f"{result.total} result(s) for {result.query!r} (showing {len(result.hits)}):"]
    for hit in result.hits:
        path_str = (
            str(hit.path.relative_to(relative_to))
            if relative_to and hit.path.is_relative_to(relative_to)
            else str(hit.path)
        )
        domain_tag = f"  [{hit.domain}]" if hit.domain else ""
        lines.append(f"  {path_str}{domain_tag}")
        if hit.snippet:
            lines.append(f"    {hit.snippet}")
    return "\n".join(lines)
