"""`wiki moc-add <slug>` — author a wiki/mocs/<slug>.md domain map-of-content page.

Sanctioned gateway path for creating or replacing a MOC page. Follows the
same shape as `concept_add`: caller supplies the body, op constructs
frontmatter, validates, writes atomically.

MOC pages are intentionally hand-curated indexes — they link to the most
important concept, entity, and synthesis pages for a domain, not to raw
sources. They are the primary session-primer surface for Claude Code and
for `wiki context mocs/<domain>`.
"""

from __future__ import annotations

from datetime import datetime, timezone

from gateway import frontmatter as fm
from gateway import log, paths, validator, wiki_pages
from gateway.core import OperationResult, write_atomic
from gateway.locking import file_lock


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def moc_add(
    slug: str,
    *,
    domain: str,
    title: str,
    body: str,
    draft: bool = False,
    force: bool = False,
) -> OperationResult:
    """Author wiki/mocs/<slug>.md.

    ``slug``: page slug, conventionally matches the domain slug.
    ``domain``: domain slug this MOC indexes.
    ``title``: display title (e.g. "condo-software — Map of Content").
    ``body``: page body markdown (no frontmatter). Must contain the
    required sections: Overview, Key entities, Key concepts, Synthesis pages.
    ``draft``: if True, sets draft: true and skips citation-grounding errors.
    ``force``: overwrite an existing MOC page.
    """
    if not wiki_pages.is_valid_slug(slug):
        return OperationResult(
            success=False,
            errors=[f"invalid slug {slug!r}: must match [a-z0-9][a-z0-9-]*"],
        )

    target = paths.knowledge_root() / "wiki" / "mocs" / f"{slug}.md"
    if target.exists() and not force:
        return OperationResult(
            success=False,
            errors=[
                f"MOC page already exists at {target.relative_to(paths.knowledge_root())}; "
                "pass force=True to overwrite"
            ],
        )

    _now = _now_iso()
    front: dict = {
        "type": "moc",
        "slug": slug,
        "title": title,
        "domain": domain,
        "created_at": _now,
        "last_updated": _now,
    }
    if draft:
        front["draft"] = True
        front["draft_started_at"] = _now

    val = validator.validate_wiki_page(front, body, "moc", draft=draft)
    if not val.ok:
        return OperationResult(
            success=False,
            errors=[str(e) for e in val.errors],
            warnings=[str(w) for w in val.warnings],
        )

    with file_lock(f"moc-add-{slug}"):
        target.parent.mkdir(parents=True, exist_ok=True)
        write_atomic(target, fm.serialize(front, body))
        log.append(
            op="moc-add",
            fields={"slug": slug, "domain": domain, "draft": "yes" if draft else "no"},
            summary=f"created wiki/mocs/{slug}.md",
        )

    return OperationResult(
        success=True,
        paths_touched=[target, paths.log_path()],
        warnings=[str(w) for w in val.warnings],
        summary=f"created MOC: {slug}",
    )
