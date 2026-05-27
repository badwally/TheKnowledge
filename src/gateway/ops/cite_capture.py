"""AGT-7: capture-to-cite — ingest a URL if needed and add a citation.

cite_capture(quote, url, target_page=None):
  1. Looks up URL in raw/ — if already ingested, reuses the source_id.
  2. If not ingested, calls ingest(url, draft=True) to pull it in.
  3. Ensures wiki/sources/<id>.md exists (backfills if filter excluded it).
  4. Finds target wiki page — explicit slug or auto-picked by token-overlap.
  5. Calls cite_add(target_page, claim_text=quote, source_id=source_id).

Idempotent: re-running on the same quote+url+target is safe (cite_add is
idempotent for already-cited lines).
"""

from __future__ import annotations

import re
from pathlib import Path

from gateway import frontmatter as fm, paths
from gateway.core import OperationResult, write_atomic


# --------------------------------------------------------------------------- #
# URL dedup                                                                    #
# --------------------------------------------------------------------------- #


def _normalize_url(url: str) -> str:
    return url.rstrip("/").lower().split("?")[0]


def _find_source_by_url(url: str) -> tuple[str, str] | None:
    """Return (source_id, source_type) if url is already in raw/, else None."""
    normalized = _normalize_url(url)
    for source_type in paths.SOURCE_TYPES:
        source_dir = paths.raw_dir() / source_type
        if not source_dir.exists():
            continue
        for p in source_dir.glob("*.md"):
            try:
                front, _ = fm.parse(p.read_text())
            except Exception:
                continue
            raw_url = str(front.get("url", ""))
            if raw_url and _normalize_url(raw_url) == normalized:
                return str(front.get("id", p.stem)), source_type
    return None


# --------------------------------------------------------------------------- #
# Wiki/sources page backfill                                                   #
# --------------------------------------------------------------------------- #


def _ensure_source_wiki_page(source_id: str, source_type: str) -> bool:
    """Create wiki/sources/<id>.md if missing. Returns True if it exists after."""
    wiki_path = paths.wiki_source_path(source_id)
    if wiki_path.exists():
        return True
    raw_path = paths.raw_dir() / source_type / f"{source_id}.md"
    if not raw_path.exists():
        return False
    try:
        front, _ = fm.parse(raw_path.read_text())
    except Exception:
        return False
    from gateway.ops.ingest import _make_source_page
    wiki_path.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(wiki_path, _make_source_page(front))
    return True


# --------------------------------------------------------------------------- #
# Auto target-page picker                                                      #
# --------------------------------------------------------------------------- #


_STOP_WORDS = frozenset({
    "the", "and", "that", "this", "with", "from", "have", "been",
    "they", "their", "which", "when", "also", "into", "some", "more",
    "than", "such", "each", "both", "than", "your", "can", "may",
    "are", "was", "its", "has", "for", "not", "but", "all",
})


def _tokenize(text: str) -> set[str]:
    tokens = re.findall(r"[a-z]{4,}", text.lower())
    return {t for t in tokens if t not in _STOP_WORDS}


def _find_target_by_overlap(quote: str) -> str | None:
    """Return the best-matching wiki page path by slug token-overlap with quote."""
    quote_tokens = _tokenize(quote)
    if not quote_tokens:
        return None

    best_score = 0
    best_path: str | None = None

    wiki = paths.wiki_dir()
    for sub in ("entities", "concepts", "synthesis"):
        d = wiki / sub
        if not d.exists():
            continue
        for p in d.glob("*.md"):
            slug_tokens = _tokenize(p.stem.replace("-", " "))
            try:
                front, body = fm.parse(p.read_text())
                title_tokens = _tokenize(str(front.get("title", "")))
            except Exception:
                title_tokens = set()
            page_tokens = slug_tokens | title_tokens
            score = len(quote_tokens & page_tokens)
            if score > best_score:
                best_score = score
                rel = str(p.relative_to(paths.knowledge_root()))
                best_path = rel

    return best_path if best_score > 0 else None


# --------------------------------------------------------------------------- #
# Public API                                                                   #
# --------------------------------------------------------------------------- #


def cite_capture(
    quote: str,
    url: str,
    target_page: str | None = None,
    *,
    filter_client=None,
) -> OperationResult:
    """Ingest url if needed, then cite quote in target_page.

    Args:
        quote:       The claim text to cite. Must be findable in target_page.
        url:         The source URL to ingest (idempotent if already in raw/).
        target_page: Wiki page path (relative to knowledge root) to add the
                     citation to. Auto-picked by token-overlap if omitted.
        filter_client: Optional FilterClient injection (for tests).

    Returns:
        OperationResult. success=True if citation was written.
    """
    if not quote or not quote.strip():
        return OperationResult(success=False, errors=["quote must be non-empty"])
    if not url or not url.strip():
        return OperationResult(success=False, errors=["url must be non-empty"])

    # 1. Dedup — check if URL already ingested
    found = _find_source_by_url(url)
    if found:
        source_id, source_type = found
        ingested_now = False
    else:
        # 2. Ingest the URL
        from gateway.ops.ingest import ingest

        ingest_result = ingest(url, draft=True, filter_client=filter_client)
        if not ingest_result.success:
            return OperationResult(
                success=False,
                errors=[f"ingest failed: {'; '.join(ingest_result.errors)}"],
            )
        # Re-lookup by URL to get source_id reliably
        found = _find_source_by_url(url)
        if found is None:
            return OperationResult(
                success=False,
                errors=["ingest succeeded but source not found in raw/ by URL — check logs"],
            )
        source_id, source_type = found
        ingested_now = True

    # 3. Ensure wiki/sources page exists
    if not _ensure_source_wiki_page(source_id, source_type):
        return OperationResult(
            success=False,
            errors=[f"wiki/sources/{source_id}.md could not be created"],
        )

    # 4. Resolve target page
    if target_page is None:
        target_page = _find_target_by_overlap(quote)
        if target_page is None:
            return OperationResult(
                success=False,
                errors=[
                    "could not auto-pick target wiki page — no slug token-overlap with quote; "
                    "specify target_page explicitly"
                ],
                summary=(
                    f"source {'ingested' if ingested_now else 'already in raw'}: {source_id}; "
                    "citation not added (no target)"
                ),
            )

    # 5. Add citation
    from gateway.ops.cite_add import cite_add

    cite_result = cite_add(target_page, claim_text=quote, source_id=source_id)
    if not cite_result.success:
        return OperationResult(
            success=False,
            errors=cite_result.errors,
            summary=(
                f"source {'ingested' if ingested_now else 'reused'}: {source_id}; "
                f"cite-add failed on {target_page}"
            ),
        )

    return OperationResult(
        success=True,
        paths_touched=cite_result.paths_touched,
        summary=(
            f"{'ingested' if ingested_now else 'reused'} {source_id}; "
            f"cited in {target_page}"
        ),
    )
