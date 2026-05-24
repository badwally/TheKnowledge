"""Apply a Plan: validate every update, write atomically, log.

This is the structural enforcement of the "plan-before-write" rule. The
gateway is the only thing that mutates wiki/ files for entity / concept /
synthesis / MOC pages. Sources still go through `wiki ingest`; artifacts
through `wiki nlm-*`.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from gateway import contradictions_log
from gateway import frontmatter as fm
from gateway import log, paths, validator, wiki_pages
from gateway.core import AuthorshipReport, OperationResult, write_atomic
from gateway.locking import file_lock
from gateway.plan import Plan, WikiUpdate


_LOCK_NAME = "wiki-author"


def apply_plan(
    plan: Plan,
    *,
    draft: bool = False,
    force_new_slug: bool = False,
) -> OperationResult:
    """Validate every update in `plan`, then commit them atomically."""
    if not plan.updates:
        return OperationResult(
            success=True,
            no_op=True,
            summary=f"plan for {plan.source_id} contains no updates",
        )

    errors: list[str] = []
    warnings: list[str] = []
    parsed: list[tuple[WikiUpdate, str, dict, str]] = []  # (update, page_type, front, body)

    # --- Phase 1: validate every update before any write ---
    for i, update in enumerate(plan.updates):
        target_rel = update.target_path
        page_type = wiki_pages.page_type_for_path(target_rel)
        if page_type is None:
            errors.append(
                f"update[{i}]: target_path {target_rel!r} is not under a known wiki page-type directory"
            )
            continue
        if page_type in ("source", "artifact"):
            errors.append(
                f"update[{i}]: page type {page_type!r} is managed by the gateway directly, "
                f"not via plans (target {target_rel!r})"
            )
            continue

        try:
            front, body = fm.parse(update.content)
        except fm.FrontmatterError as e:
            errors.append(f"update[{i}] ({target_rel}): frontmatter: {e}")
            continue

        # K1/D2: file-line offset so validator surfaces file-relative lines.
        body_offset = fm.body_line_offset(update.content)

        existing_slugs = _existing_slugs_for_type(page_type)

        # If the update targets an existing page, exclude its current slug
        # from the duplicate check (we're rewriting that exact slug).
        if update.update_kind == "update":
            existing = _try_read_page(target_rel)
            if existing is not None:
                existing_front, _ = existing
                current_slug = existing_front.get("slug")
                if current_slug and current_slug in existing_slugs:
                    existing_slugs = [s for s in existing_slugs if s != current_slug]

        is_draft = bool(front.get("draft")) or draft
        result = validator.validate_wiki_page(
            front,
            body,
            page_type,
            draft=is_draft,
            existing_slugs=existing_slugs,
            force_new_slug=force_new_slug,
            body_line_offset=body_offset,
        )
        if not result.ok:
            for err in result.errors:
                errors.append(f"update[{i}] ({target_rel}): {err}")
        for warn in result.warnings:
            warnings.append(f"update[{i}] ({target_rel}): {warn}")

        if is_draft:
            front.setdefault("draft", True)
            front.setdefault("draft_started_at", _now_iso())
            uncited_count = len(_uncited_claims(body))
            front["draft_unresolved_claims"] = uncited_count
            update_content = fm.serialize(front, body)
        else:
            update_content = update.content

        parsed.append((update, page_type, front, body))
        # Stash potentially-mutated content (for draft frontmatter additions)
        update.content = update_content

    if errors:
        return OperationResult(
            success=False,
            errors=errors,
            warnings=warnings,
        )

    # --- Phase 2: apply atomically ---
    paths_touched: list[Path] = []
    with file_lock(_LOCK_NAME):
        for update, page_type, front, body in parsed:
            target = paths.knowledge_root() / update.target_path
            target.parent.mkdir(parents=True, exist_ok=True)
            write_atomic(target, update.content)
            paths_touched.append(target)

        # Update the source's `wiki_pages:` so backlinks are tracked.
        _record_backlinks(plan.source_id, [u.target_path for u in plan.updates])

        # M42: persist contradictions to JSONL log for the Review console.
        if plan.contradictions:
            contradictions_log.append_contradictions(plan.contradictions)

        log.append(
            op="wiki-author",
            fields={
                "id": plan.source_id,
                "updates": len(plan.updates),
                "created": sum(1 for u, _, _, _ in parsed if u.update_kind == "create"),
                "updated": sum(1 for u, _, _, _ in parsed if u.update_kind == "update"),
                "contradictions": len(plan.contradictions),
                "draft": "yes" if draft else "no",
            },
            summary=plan.rationale or "(no rationale provided)",
        )

    # --- Phase 3: build authorship report ---
    report = AuthorshipReport(
        pages_created=[
            u.target_path for u, pt, f, b in parsed if u.update_kind == "create"
        ],
        pages_updated=[
            u.target_path for u, pt, f, b in parsed if u.update_kind == "update"
        ],
        contradictions=list(plan.contradictions),
    )

    return OperationResult(
        success=True,
        paths_touched=paths_touched + [paths.log_path()],
        summary=f"applied plan for {plan.source_id}: {len(plan.updates)} update(s)",
        warnings=warnings,
        authorship_report=report,
    )


# --- helpers ---------------------------------------------------------------


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _existing_slugs_for_type(page_type: str) -> list[str]:
    schema = wiki_pages.schema_for_type(page_type)
    if schema is None:
        return []
    dir_ = paths.knowledge_root() / schema.directory
    if not dir_.exists():
        return []
    out: list[str] = []
    for path in dir_.glob("*.md"):
        try:
            front, _ = fm.parse(path.read_text())
        except fm.FrontmatterError:
            continue
        slug = front.get("slug")
        if slug:
            out.append(str(slug))
    return out


def _try_read_page(rel_path: str) -> tuple[dict, str] | None:
    target = paths.knowledge_root() / rel_path
    if not target.exists():
        return None
    try:
        return fm.parse(target.read_text())
    except fm.FrontmatterError:
        return None


def _uncited_claims(body: str):
    from gateway import citations as _citations

    return _citations.uncited_claims(body)


def _record_backlinks(source_id: str, wiki_page_paths: list[str]) -> None:
    """Update the source's `wiki_pages:` frontmatter to include the targets."""
    found = _find_source(source_id)
    if found is None:
        return
    _, raw_path = found
    try:
        front, body = fm.parse(raw_path.read_text())
    except fm.FrontmatterError:
        return
    existing = list(front.get("wiki_pages") or [])
    changed = False
    for p in wiki_page_paths:
        if p not in existing:
            existing.append(p)
            changed = True
    if changed:
        front["wiki_pages"] = existing
        write_atomic(raw_path, fm.serialize(front, body))


def _find_source(source_id: str):
    for source_type in paths.SOURCE_TYPES:
        candidate = paths.raw_source_path(source_type, source_id)
        if candidate.exists():
            return source_type, candidate
    return None
