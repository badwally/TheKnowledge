"""Full-text search over wiki/ and raw/ markdown files (SRCH-1).

Simple grep-based search — no external deps, fast enough for <5k files.
Returns ranked results: title match > slug match > body match.

Search scope:
  "wiki"  — wiki/ subtree only (entities, concepts, synthesis, mocs, sources)
  "raw"   — raw/ subtree only (source documents)
  "all"   — both (default)

Ranking (descending):
  3 — query term found in title frontmatter field
  2 — query term found in file name (slug)
  1 — query term found in body
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

from gateway import frontmatter as fm, paths


Scope = Literal["wiki", "raw", "all"]

_MAX_SNIPPET = 120
_DEFAULT_LIMIT = 20
_DEFAULT_CONTEXT_LINES = 2


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
) -> SearchResult:
    """Search wiki/ and/or raw/ for `query`.

    Args:
        query: Search string. Case-insensitive substring match.
        scope: "wiki", "raw", or "all".
        domain: Filter hits to pages tagged with this domain.
        page_type: Filter hits to pages of this type (e.g. "synthesis", "web").
        limit: Maximum number of hits to return (default 20).

    Returns:
        SearchResult with hits sorted by score descending.
    """
    if not query or not query.strip():
        return SearchResult(query=query)

    pattern = re.compile(re.escape(query.strip()), re.IGNORECASE)
    candidate_dirs: list[Path] = []

    if scope in ("wiki", "all"):
        candidate_dirs.append(paths.wiki_dir())
    if scope in ("raw", "all"):
        candidate_dirs.append(paths.raw_dir())

    hits: list[SearchHit] = []
    for base in candidate_dirs:
        if not base.exists():
            continue
        for md_path in base.rglob("*.md"):
            hit = _score_file(md_path, pattern, domain, page_type)
            if hit is not None:
                hits.append(hit)

    hits.sort(key=lambda h: (-h.score, h.title.lower()))
    top = hits[:limit]
    return SearchResult(hits=top, query=query, total=len(hits))


def _score_file(
    path: Path,
    pattern: re.Pattern,
    domain_filter: str | None,
    type_filter: str | None,
) -> SearchHit | None:
    """Return a SearchHit if the file matches, else None."""
    try:
        text = path.read_text(errors="replace")
    except OSError:
        return None

    try:
        front, body = fm.parse(text)
    except Exception:
        front, body = {}, text

    title = str(front.get("title", ""))
    page_type = str(front.get("type", ""))
    slug = path.stem
    raw_domains: list = front.get("domains", [])
    if not isinstance(raw_domains, list):
        raw_domains = [raw_domains] if raw_domains else []
    page_domain = str(raw_domains[0]) if raw_domains else str(front.get("domain", ""))

    if domain_filter and page_domain != domain_filter:
        return None
    if type_filter and page_type != type_filter:
        return None

    score = 0
    snippet = ""

    if pattern.search(title):
        score = max(score, 3)
        snippet = snippet or _truncate(title)

    if pattern.search(slug):
        score = max(score, 2)
        snippet = snippet or _truncate(slug)

    body_match = pattern.search(body)
    if body_match:
        score = max(score, 1)
        if not snippet:
            snippet = _extract_snippet(body, body_match)

    if score == 0:
        return None

    return SearchHit(
        path=path,
        slug=slug,
        title=title or slug,
        page_type=page_type,
        domain=page_domain,
        score=score,
        snippet=snippet,
    )


def _extract_snippet(body: str, match: re.Match) -> str:
    """Return the line containing the match, trimmed."""
    start = body.rfind("\n", 0, match.start()) + 1
    end = body.find("\n", match.end())
    if end == -1:
        end = len(body)
    line = body[start:end].strip()
    return _truncate(line)


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
