"""`wiki context` — read-side outbound op (M51 INT-11).

Resolves a slug-or-query to a wiki page, walks wikilinks to depth N,
returns the assembled context. Read-only — no wiki/ or raw/ mutation.
"""

from __future__ import annotations

from pathlib import Path
import json
import re

from gateway import frontmatter as fm
from gateway import log, paths, search_index
from gateway.core import OperationResult


class NoMatchError(LookupError):
    """The slug-or-query didn't resolve to any wiki page."""


class AmbiguousQueryError(LookupError):
    """Title-substring matched >1 page; query needs to be more specific."""


_PAGE_KINDS = ("entities", "concepts", "mocs", "synthesis", "sources")
# Wikilinks followed during expansion. nlm:<uuid> excluded (opaque corpus refs).
_FOLLOWABLE_PREFIXES = ("sources/", "entities/", "concepts/", "mocs/", "synthesis/")
_WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def _resolve_target(query: str) -> Path:
    """Resolve `query` to a wiki page path.

    Tries, in order:
    1. As a literal path (with or without `wiki/` prefix and `.md` suffix).
    2. As a `<kind>/<slug>` reference (e.g. "entities/alpha-co").
    3. Title-substring fallback: case-insensitive match against frontmatter
       `title:` across `_PAGE_KINDS`. Multi-match → AmbiguousQueryError
       (listing up to 5 candidates). Zero match → NoMatchError.
    """
    kb_root = paths.knowledge_root()
    q = query.strip()

    # 1. literal path
    for candidate in (
        kb_root / q,
        kb_root / (q + ".md"),
        kb_root / "wiki" / q,
        kb_root / "wiki" / (q + ".md"),
    ):
        if candidate.is_file() and candidate.suffix == ".md":
            return candidate

    # 2. <kind>/<slug>
    if "/" in q and not q.startswith("wiki/"):
        candidate = kb_root / "wiki" / (q + ".md" if not q.endswith(".md") else q)
        if candidate.is_file():
            return candidate

    # 2b. slug-normalised scan: spaces → hyphens, try each page kind.
    #     Handles "long covid" → concepts/long-covid.md without a title scan.
    slug_q = re.sub(r"\s+", "-", q.lower())
    for kind in _PAGE_KINDS:
        candidate = kb_root / "wiki" / kind / (slug_q + ".md")
        if candidate.is_file():
            return candidate

    # 3. title-substring fallback.
    #     Concept and entity pages use `canonical_name`; synthesis pages use
    #     `title`. Check both so neither type is invisible to queries.
    needle = q.lower()
    matches: list[Path] = []
    for kind in _PAGE_KINDS:
        d = kb_root / "wiki" / kind
        if not d.exists():
            continue
        for p in sorted(d.glob("*.md")):
            try:
                front, _ = fm.parse(p.read_text())
            except fm.FrontmatterError:
                continue
            title = str(front.get("title") or front.get("canonical_name") or "").lower()
            if needle in title:
                matches.append(p)
    if len(matches) == 0:
        raise NoMatchError(
            f"no wiki page matched {query!r} (tried path lookup + title-substring)"
        )
    if len(matches) > 1:
        preview = "\n".join(
            f"  - {p.relative_to(kb_root)}"
            for p in matches[:5]
        )
        raise AmbiguousQueryError(
            f"query {query!r} matched {len(matches)} pages; be more specific. "
            f"top candidates:\n{preview}"
        )
    return matches[0]


def _walk_neighbors(start: Path, depth: int) -> list[Path]:
    """BFS over wikilinks starting at `start`, up to `depth` hops.

    Returns a deduplicated list of pages in visit order (root first).
    Missing wikilink targets are silently skipped. Cycles are avoided
    via a visited set.
    """
    kb_root = paths.knowledge_root()
    visited: list[Path] = []
    seen: set[Path] = set()
    frontier: list[tuple[Path, int]] = [(start, 0)]

    while frontier:
        page, d = frontier.pop(0)
        if page in seen:
            continue
        seen.add(page)
        visited.append(page)

        if d >= depth:
            continue
        try:
            _, body = fm.parse(page.read_text())
        except fm.FrontmatterError:
            continue
        for target in _extract_wikilink_targets(body):
            resolved = _resolve_wikilink(kb_root, target)
            if resolved is not None and resolved not in seen:
                frontier.append((resolved, d + 1))
    return visited


def _extract_wikilink_targets(body: str) -> list[str]:
    """Find `[[<target>]]` patterns and return the bare target (no anchor,
    no display text) for those starting with a followable prefix."""
    out: list[str] = []
    for m in _WIKILINK_RE.finditer(body):
        target = m.group(1).strip()
        if any(target.startswith(p) for p in _FOLLOWABLE_PREFIXES):
            out.append(target)
    return out


def _resolve_wikilink(kb_root: Path, target: str) -> Path | None:
    """`<kind>/<slug>` → `wiki/<kind>/<slug>.md` if it exists, else None."""
    if not any(target.startswith(p) for p in _FOLLOWABLE_PREFIXES):
        return None
    candidate = kb_root / "wiki" / f"{target}.md"
    return candidate if candidate.is_file() else None


def _render_markdown(pages: list[Path]) -> str:
    parts = []
    kb_root = paths.knowledge_root()
    for p in pages:
        rel = p.relative_to(kb_root)
        try:
            front, body = fm.parse(p.read_text())
        except fm.FrontmatterError:
            front, body = {}, p.read_text()
        title = front.get("title") or front.get("slug") or p.stem
        parts.append(f"## {rel} — {title}\n\n{body.rstrip()}")
    return "\n\n---\n\n".join(parts)


def _root_domains(root: Path) -> set[str]:
    try:
        front, _ = fm.parse(root.read_text())
    except fm.FrontmatterError:
        return set()
    doms = front.get("domains") or []
    if not isinstance(doms, list):
        doms = [doms]
    if front.get("domain"):
        doms.append(front["domain"])
    return {str(d) for d in doms if d}


def _render_markdown_budgeted(pages: list[Path], budget: int) -> tuple[str, int]:
    """Render root + neighbors within a character budget (WS3).

    Root is always rendered (full). Neighbors are ranked by authority —
    inbound-link count (from the index) plus a boost for sharing the root's
    domain — and each is truncated to its leading content so a few large
    neighbors can't consume the whole budget. Returns (markdown, pages_kept).
    """
    if not pages:
        return "", 0
    kb_root = paths.knowledge_root()
    root, neighbors = pages[0], pages[1:]
    root_domains = _root_domains(root)

    rels = [str(n.relative_to(kb_root)) for n in neighbors]
    inbound = search_index.inbound_counts(rels)

    def _authority(n: Path) -> tuple[int, int]:
        rel = str(n.relative_to(kb_root))
        overlap = 1 if _root_domains(n) & root_domains else 0
        return (overlap, inbound.get(rel, 0))

    ranked = sorted(neighbors, key=_authority, reverse=True)

    def _block(p: Path, limit: int | None) -> str:
        rel = p.relative_to(kb_root)
        try:
            front, body = fm.parse(p.read_text())
        except fm.FrontmatterError:
            front, body = {}, p.read_text()
        title = front.get("title") or front.get("slug") or p.stem
        body = body.rstrip()
        if limit is not None and len(body) > limit:
            body = body[:limit].rstrip() + "\n…[truncated for budget]"
        return f"## {rel} — {title}\n\n{body}"

    parts = [_block(root, None)]
    total = len(parts[0])
    kept = 1
    sep = "\n\n---\n\n"
    # Per-neighbor cap scales down as more neighbors compete for the budget.
    per_cap = max(800, budget // max(len(ranked), 1))
    for n in ranked:
        remaining = budget - total - len(sep)
        if remaining <= 200:
            break
        block = _block(n, min(per_cap, remaining))
        parts.append(block)
        total += len(sep) + len(block)
        kept += 1
    return sep.join(parts), kept


def _render_json(pages: list[Path]) -> str:
    kb_root = paths.knowledge_root()

    def _page_obj(p: Path) -> dict:
        try:
            front, body = fm.parse(p.read_text())
        except fm.FrontmatterError:
            front, body = {}, p.read_text()
        return {
            "path": str(p.relative_to(kb_root)),
            "slug": str(front.get("slug") or p.stem),
            "title": str(front.get("title") or ""),
            "kind": str(front.get("type") or p.parent.name.rstrip("s")),
            "body": body,
        }

    if not pages:
        return json.dumps({"root": None, "neighbors": []})
    return json.dumps({
        "root": _page_obj(pages[0]),
        "neighbors": [_page_obj(p) for p in pages[1:]],
    }, indent=2)


def context_op(query: str, *,
               depth: int = 1,
               fmt: str = "markdown",
               caller: str | None = None,
               budget: int | None = None) -> OperationResult:
    if not caller:
        return OperationResult(
            success=False,
            errors=["--caller is required (free-form identifier; logged to log.md)"],
        )
    if fmt not in ("markdown", "json"):
        return OperationResult(
            success=False,
            errors=[f"--format must be 'markdown' or 'json', got {fmt!r}"],
        )
    if depth < 0:
        return OperationResult(
            success=False,
            errors=[f"--depth must be >= 0, got {depth}"],
        )
    if budget is not None and budget <= 0:
        return OperationResult(
            success=False,
            errors=[f"--budget must be > 0, got {budget}"],
        )

    try:
        root = _resolve_target(query)
    except (NoMatchError, AmbiguousQueryError) as e:
        return OperationResult(success=False, errors=[str(e)])

    pages = _walk_neighbors(root, depth=depth)

    pages_kept = len(pages)
    if fmt == "json":
        # Budget does not apply to JSON (structured consumers page themselves).
        rendered = _render_json(pages)
    elif budget is not None:
        full = _render_markdown(pages)
        if len(full) <= budget:
            rendered = full
        else:
            rendered, pages_kept = _render_markdown_budgeted(pages, budget)
    else:
        rendered = _render_markdown(pages)

    log.append(
        op="context",
        fields={
            "caller": caller,
            "target": str(root.relative_to(paths.knowledge_root())),
            "depth": depth,
            "format": fmt,
            "budget": budget if budget is not None else "",
            "pages_returned": pages_kept,
            "pages_found": len(pages),
        },
        summary=(
            f"context: caller={caller!r} target={root.relative_to(paths.knowledge_root())} "
            f"depth={depth} pages={pages_kept}/{len(pages)}"
            + (f" budget={budget}" if budget is not None else "")
        ),
    )
    return OperationResult(
        success=True,
        paths_touched=[paths.log_path()],
        summary=rendered,
    )
