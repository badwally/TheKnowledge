"""`wiki concept-add <slug>` — author a wiki/concepts/<slug>.md page.

Sanctioned gateway path for creating a concept page. Surfaced as a gap
during the 2026-05-23 ai-native-business build, where the definitional
substrate-vs-feature-vs-product concept got filed at `wiki/synthesis/`
because `wiki query` only produces synthesis pages and direct writes to
`wiki/` are blocked by hard rule #1.

The op accepts a body (caller-provided markdown), constructs the right
frontmatter, validates against the concept page schema (frontmatter +
sections + citation grounding), and writes atomically. Refuses to
overwrite an existing page unless `force=True`. Slug uniqueness is
enforced via the existing-page check; broader cross-page slug-similarity
warnings remain the validator's job.
"""

from __future__ import annotations

from datetime import datetime, timezone

from gateway import frontmatter as fm
from gateway import log, paths, validator, wiki_pages
from gateway.core import OperationResult, write_atomic
from gateway.locking import file_lock


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def concept_add(
    slug: str,
    *,
    canonical_name: str,
    body: str,
    domain: str,
    draft: bool = False,
    cite_sources: list[str] | None = None,
    force: bool = False,
) -> OperationResult:
    """Author wiki/concepts/<slug>.md.

    `body` is the page body (no frontmatter). The op prepends the
    constructed frontmatter and writes atomically. Validation runs
    against the concept schema (frontmatter + sections + citation
    grounding). `draft=True` downgrades citation grounding to a warning
    (per the project's draft convention) and sets `draft:` /
    `draft_started_at:` so `wiki finalize` can close the page later.

    `cite_sources` is an optional list of source IDs (e.g.
    `["web-2024-02-07-3a2"]`) used to populate the `synthesizes:`
    frontmatter list as `["sources/web-2024-02-07-3a2", ...]`. The
    validator's `synthesizes` integrity check will verify each one points
    at an existing wiki/sources/ page.
    """
    if not wiki_pages.is_valid_slug(slug):
        return OperationResult(
            success=False,
            errors=[
                f"invalid slug {slug!r}: must match [a-z0-9][a-z0-9-]*"
            ],
        )

    target = paths.knowledge_root() / "wiki" / "concepts" / f"{slug}.md"
    if target.exists() and not force:
        return OperationResult(
            success=False,
            errors=[
                f"concept page already exists at {target.relative_to(paths.knowledge_root())}; "
                "pass force=True to overwrite"
            ],
        )

    _now = _now_iso()
    front: dict = {
        "type": "concept",
        "slug": slug,
        "canonical_name": canonical_name,
        "domains": [domain],
        "created_at": _now,
        "last_updated": _now,
    }
    if cite_sources:
        front["synthesizes"] = [f"sources/{sid}" for sid in cite_sources]
    if draft:
        front["draft"] = True
        front["draft_started_at"] = front["created_at"]

    # Validate before writing. Use existing_slugs=None (no cross-page slug
    # uniqueness — that's a broader pass best done by `wiki lint`).
    val = validator.validate_wiki_page(
        front, body, "concept", draft=draft
    )
    if not val.ok:
        return OperationResult(
            success=False,
            errors=[str(e) for e in val.errors],
            warnings=[str(w) for w in val.warnings],
        )

    with file_lock(f"concept-add-{slug}"):
        target.parent.mkdir(parents=True, exist_ok=True)
        write_atomic(target, fm.serialize(front, body))
        log.append(
            op="concept-add",
            fields={
                "slug": slug,
                "domain": domain,
                "draft": "yes" if draft else "no",
                "cite_sources": ",".join(cite_sources or []) or "(none)",
            },
            summary=f"created wiki/concepts/{slug}.md",
        )

    return OperationResult(
        success=True,
        paths_touched=[target, paths.log_path()],
        warnings=[str(w) for w in val.warnings],
        summary=f"created concept: {slug}",
    )
