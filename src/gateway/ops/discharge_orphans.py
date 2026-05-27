"""wiki routine discharge-orphans — batch synthesize wiki pages for orphaned sources (M99).

Orphan sources are raw/* files whose `wiki_pages:` list is empty — they
have been ingested but no wiki page cites them yet.  For each orphan in
`domain`, we generate a synthesizing question from the source's title and
call `query()` to produce a draft synthesis page that naturally cites it.

The resulting draft pages are review-ready; they count as wiki coverage so
the source is no longer listed as an orphan after `wiki finalize`.
"""

from __future__ import annotations

import re

from gateway import frontmatter as fm, log, paths
from gateway.core import OperationResult
from gateway.filter.policy import PolicyError, load_policy, policy_exists
from gateway import nlm_registry


DEFAULT_LIMIT = 10
_PREVIEW_MAX = 300
_SRC_LINK_RE = re.compile(r'\[\[sources/([^\]]+)\]\]')


def _source_preview(front: dict, body: str) -> str:
    """Extract a short content preview from frontmatter fields or body fallback."""
    meta = front.get("meta") or {}
    preview = (
        str(meta.get("abstract", "")).strip()
        or str(meta.get("excerpt", "")).strip()
        or str(front.get("description", "")).strip()
        or body.strip()[:_PREVIEW_MAX]
    )
    return preview[:_PREVIEW_MAX]


def _cited_source_ids() -> frozenset[str]:
    """Return IDs of sources already cited in any existing synthesis page."""
    synthesis_dir = paths.knowledge_root() / "wiki" / "synthesis"
    cited: set[str] = set()
    if not synthesis_dir.exists():
        return frozenset()
    for p in synthesis_dir.glob("*.md"):
        try:
            cited.update(_SRC_LINK_RE.findall(p.read_text()))
        except Exception:
            continue
    return frozenset(cited)


def _orphan_sources_for_domain(domain: str, limit: int) -> list[dict]:
    """Return up to `limit` raw sources tagged to `domain` with no wiki coverage.

    A source is skipped if `wiki_pages` is set (finalized coverage) OR if its ID
    already appears as `[[sources/<id>]]` in any existing synthesis page (draft
    coverage pending finalization).
    """
    already_cited = _cited_source_ids()
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
                front, body = fm.parse(p.read_text())
            except Exception:
                continue
            if front.get("wiki_pages"):
                continue
            source_id = front.get("id", p.stem)
            if source_id in already_cited or f"{source_type}/{source_id}" in already_cited:
                continue
            source_domains = front.get("domain") or front.get("domains") or []
            if isinstance(source_domains, str):
                source_domains = [source_domains]
            if domain not in source_domains:
                continue
            results.append({
                "id": source_id,
                "title": str(front.get("title", p.stem)),
                "source_type": source_type,
                "preview": _source_preview(front, body),
            })
    return results


def _synthesis_question(source: dict, domain_topic: str = "") -> str:
    """Build a synthesis question grounded in source preview and domain context."""
    title = source["title"]
    preview = source.get("preview", "")
    context = f" in the context of {domain_topic}" if domain_topic else ""
    if preview:
        return (
            f"What are the key insights from \"{title}\"{context}? "
            f"The source describes: {preview}"
        )
    return f"What does \"{title}\" contribute to this domain's understanding{context}?"


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

    # Pre-flight: verify a persistent notebook exists for this domain.
    # Catches "no notebook for domain" before counting/querying any sources.
    # NLM auth validity cannot be pre-checked without a live call; the summary
    # note below reminds callers that dry-run does not validate auth.
    if nlm_registry.get_persistent(domain) is None:
        return OperationResult(
            success=False,
            errors=[
                f"no notebook for domain {domain!r}; "
                "run `wiki research` first to build one"
            ],
        )

    domain_topic = ""
    if policy_exists(domain):
        try:
            domain_topic = load_policy(domain).domain_topic
        except PolicyError:
            pass

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
        question = _synthesis_question(source, domain_topic)
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
    dry_run_note = " [NLM auth not validated]" if dry_run else ""
    return OperationResult(
        success=len(errors) == 0,
        errors=errors,
        summary=(
            f"discharge-orphans{mode}: {filed} synthesis drafts filed, "
            f"{skipped} skipped — domain {domain!r}, limit {limit}{dry_run_note}"
        ),
    )
