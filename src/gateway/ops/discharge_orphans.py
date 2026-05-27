"""wiki routine discharge-orphans — batch synthesize wiki pages for orphaned sources (M99).

Orphan sources are raw/* files whose `wiki_pages:` list is empty — they
have been ingested but no wiki page cites them yet.  For each orphan in
`domain`, we generate a synthesizing question from the source's title and
call `query()` to produce a draft synthesis page that naturally cites it.

The resulting draft pages are review-ready; they count as wiki coverage so
the source is no longer listed as an orphan after `wiki finalize`.
"""

from __future__ import annotations

from gateway import frontmatter as fm, log, paths
from gateway.core import OperationResult


DEFAULT_LIMIT = 10


def _orphan_sources_for_domain(domain: str, limit: int) -> list[dict]:
    """Return up to `limit` raw sources tagged to `domain` with no wiki coverage."""
    results: list[dict] = []
    for source_type in paths.SOURCE_TYPES:
        if len(results) >= limit:
            break
        source_dir = paths.raw_dir() / source_type
        if not source_dir.exists():
            continue
        for p in sorted(source_dir.glob("*.md")):
            if len(results) >= limit:
                break
            try:
                front, _ = fm.parse(p.read_text())
            except Exception:
                continue
            if front.get("wiki_pages"):
                continue
            source_domains = front.get("domain") or front.get("domains") or []
            if isinstance(source_domains, str):
                source_domains = [source_domains]
            if domain not in source_domains:
                continue
            results.append({
                "id": front.get("id", p.stem),
                "title": str(front.get("title", p.stem)),
                "source_type": source_type,
            })
    return results


def _synthesis_question(source: dict) -> str:
    title = source["title"]
    return f"What does '{title}' contribute to this domain's understanding?"


def discharge_orphans(
    domain: str,
    *,
    limit: int = DEFAULT_LIMIT,
    dry_run: bool = False,
) -> OperationResult:
    """Batch-synthesize draft wiki pages for orphaned raw sources in `domain`."""
    from gateway.ops.query import query

    if not domain:
        return OperationResult(success=False, errors=["domain is required"])

    sources = _orphan_sources_for_domain(domain, limit)
    if not sources:
        return OperationResult(
            success=True,
            summary=f"discharge-orphans: no orphan sources found for domain {domain!r}",
        )

    filed = 0
    skipped = 0
    errors: list[str] = []

    for source in sources:
        question = _synthesis_question(source)
        if dry_run:
            filed += 1
            continue
        result = query(question, domain=domain, draft=True)
        if result.success:
            filed += 1
        else:
            skipped += 1
            errors.append(f"{source['id']}: {'; '.join(result.errors)}")

    if not dry_run:
        log.append(
            op="discharge-orphans",
            fields={
                "domain": domain,
                "filed": filed,
                "skipped": skipped,
                "limit": limit,
                "errors": len(errors),
            },
            summary=f"discharge-orphans: {filed} drafts filed for domain {domain!r}",
        )

    mode = " (dry-run)" if dry_run else ""
    return OperationResult(
        success=len(errors) == 0,
        errors=errors,
        summary=(
            f"discharge-orphans{mode}: {filed} synthesis drafts filed, "
            f"{skipped} skipped — domain {domain!r}, limit {limit}"
        ),
    )
