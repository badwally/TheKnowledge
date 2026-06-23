"""Apply a Plan: validate every update, write atomically, log.

This is the structural enforcement of the "plan-before-write" rule. The
gateway is the only thing that mutates wiki/ files for entity / concept /
synthesis / MOC pages. Sources still go through `wiki ingest`; artifacts
through `wiki nlm-*`.

Idempotency: applying the same plan twice produces the same files; backlink updates skip entries already present.
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
_TIMESTAMP_PAGE_TYPES = frozenset({"entity", "concept", "synthesis"})

# T2.7b: an "update" whose new body is smaller than this fraction of the prior
# body is rejected as a suspicious rewrite that likely drops claims. A floor, not
# a target — re-authoring should add, not gut. (No override today; a deliberate
# >50% condensation is unsupported via the authorship loop — see validate_plan.)
_BODY_SHRINK_FLOOR = 0.5


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _count_source_links(body: str) -> int:
    """Count distinct [[sources/<id>]] links in a body (for sources_count)."""
    return len(_source_citation_set(body))


def _source_citation_set(body: str) -> set[str]:
    """Return the set of distinct [[sources/<id>]] link strings in a body."""
    import re
    return set(re.findall(r"\[\[sources/[^\]]+\]\]", body))


def _stamp_timestamps(
    front: dict,
    page_type: str,
    update_kind: str,
    existing_front: dict | None,
    body: str = "",
) -> None:
    """ONT-6: Ensure created_at, last_updated (and sources_count for synthesis) are set."""
    if page_type not in _TIMESTAMP_PAGE_TYPES:
        return
    now = _now_iso()
    if update_kind == "create" or existing_front is None:
        front.setdefault("created_at", now)
        front.setdefault("last_updated", now)
    else:
        # Preserve existing created_at on updates; always advance last_updated.
        if existing_front.get("created_at"):
            front.setdefault("created_at", existing_front["created_at"])
        else:
            front.setdefault("created_at", now)
        front["last_updated"] = now
    if page_type == "synthesis":
        front.setdefault("sources_count", _count_source_links(body))


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

    # --- Phase 1: validate every update before any write (shared with dry-run) ---
    errors, warnings, parsed = validate_plan(
        plan, draft=draft, force_new_slug=force_new_slug
    )

    if errors:
        return OperationResult(
            success=False,
            errors=errors,
            warnings=warnings,
        )

    if not parsed:
        # M7: every update was a convergent no-op (body byte-identical to disk).
        # Nothing to write — short-circuit so we don't thrash backlinks / the log.
        return OperationResult(
            success=True,
            no_op=True,
            warnings=warnings,
            summary=(
                f"plan for {plan.source_id}: no changes "
                f"(all {len(plan.updates)} update(s) already current)"
            ),
        )

    # --- Phase 2: apply atomically (all-or-nothing across pages) ---
    # write_atomic is per-file atomic, but a multi-page plan must not half-apply:
    # if page N's write fails, pages 1..N-1 are rolled back to their prior state
    # (restored for updates, unlinked for creates). T2.8.
    paths_touched: list[Path] = []
    with file_lock(_LOCK_NAME):
        snapshots: list[tuple[Path, str | None]] = []
        for update, page_type, front, body in parsed:
            target = paths.knowledge_root() / update.target_path
            prior = target.read_text(encoding="utf-8") if target.exists() else None
            snapshots.append((target, prior))

        try:
            for update, page_type, front, body in parsed:
                target = paths.knowledge_root() / update.target_path
                target.parent.mkdir(parents=True, exist_ok=True)
                write_atomic(target, update.content)
                paths_touched.append(target)
        except Exception as e:  # noqa: BLE001 — any write failure triggers rollback
            for target, prior in snapshots:
                try:
                    if prior is None:
                        if target.exists():
                            target.unlink()
                    else:
                        write_atomic(target, prior)
                except OSError:
                    pass  # best-effort restore; report the original failure
            return OperationResult(
                success=False,
                errors=[
                    f"atomic apply failed on {len(parsed)}-page plan; rolled back: {e}"
                ],
            )

        # Pages committed. The following are post-commit bookkeeping (each is
        # individually defensive and does not raise on the common paths).
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


# --- validation (Phase 1) — shared by apply_plan and dry-run ----------------


def validate_plan(
    plan: Plan,
    *,
    draft: bool = False,
    force_new_slug: bool = False,
) -> tuple[list[str], list[str], list[tuple[WikiUpdate, str, dict, str]]]:
    """Validate every update in `plan` without writing. Returns
    (errors, warnings, parsed) where `parsed` is the list of writable
    (update, page_type, front, body) tuples — convergent no-ops are dropped.

    This is the single source of truth for what a plan would do; `apply_plan`
    runs it then writes, and `_dry_run_plan` runs it then reports."""
    errors: list[str] = []
    warnings: list[str] = []
    parsed: list[tuple[WikiUpdate, str, dict, str]] = []

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
        existing_front_for_update: dict | None = None
        existing_body_for_update: str | None = None
        if update.update_kind == "update":
            existing = _try_read_page(target_rel)
            if existing is not None:
                existing_front_for_update, existing_body_for_update = existing
                current_slug = existing_front_for_update.get("slug")
                if current_slug and current_slug in existing_slugs:
                    existing_slugs = [s for s in existing_slugs if s != current_slug]

        # T2.7: no-citation-loss guard. An update rewrites the page wholesale; if
        # the new body drops a `[[sources/...]]` citation the page already had,
        # that is silent knowledge destruction (the agent rebuilt the page from a
        # partial view). Knowledge is monotonic-by-default — reject the drop.
        # NOTE: there is currently no override; deliberate retraction is not
        # supported via the authorship loop (use a dedicated edit path).
        if existing_body_for_update is not None:
            dropped = _source_citation_set(existing_body_for_update) - _source_citation_set(body)
            if dropped:
                errors.append(
                    f"update[{i}] ({target_rel}): citation-loss — drops prior "
                    f"citation(s) {sorted(dropped)}; an update must preserve every "
                    f"existing [[sources/...]] citation and only add"
                )
                continue
        # T2.7b: body-shrink tripwire. Even when citations are shared, a body
        # that shrinks past half its prior size on an "update" signals dropped
        # claims. Reject as suspicious — re-authoring should add, not gut.
        # (Known limitation: this also blocks a legitimate >50% condensation;
        # no override exists today.)
        if existing_body_for_update is not None and body.strip():
            if len(body) < _BODY_SHRINK_FLOOR * len(existing_body_for_update):
                errors.append(
                    f"update[{i}] ({target_rel}): body-shrink — update body is "
                    f"{len(body)} chars vs existing {len(existing_body_for_update)} "
                    f"(>50% smaller); refusing a suspicious rewrite that likely drops claims"
                )
                continue

        # T2.10: convergent no-op. If an update's body is byte-identical to
        # what's already on disk, re-authoring it would only thrash
        # last_updated and the file mtime. Skip it entirely so re-runs converge
        # instead of churn (matches the idempotent-and-convergent op contract).
        if (
            update.update_kind == "update"
            and existing_body_for_update is not None
            and body == existing_body_for_update
        ):
            continue

        # T2.9: cross-kind slug collision. A slug must be unique across page
        # kinds — if `food-noise` already exists as a concept, an entity page of
        # the same slug splits citations across two canonical pages and makes
        # `[[food-noise]]` ambiguous. Reject a target whose slug already lives
        # under a different kind's directory.
        slug = front.get("slug")
        if slug:
            conflict_kind = _cross_kind_slug_conflict(str(slug), page_type)
            if conflict_kind is not None:
                errors.append(
                    f"update[{i}] ({target_rel}): slug-cross-kind-collision — slug "
                    f"{slug!r} already exists as a {conflict_kind} page; slugs must be "
                    f"unique across page kinds"
                )
                continue

        # ONT-6: auto-stamp created_at / last_updated / sources_count on
        # entity, concept, and synthesis pages so the validator's required-
        # field check always passes, even for callers that don't include them.
        _stamp_timestamps(front, page_type, update.update_kind, existing_front_for_update, body)

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
            update_content = fm.serialize(front, body)

        parsed.append((update, page_type, front, body))
        # Stash potentially-mutated content (for draft frontmatter additions)
        update.content = update_content

    return errors, warnings, parsed


# --- helpers ---------------------------------------------------------------


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


def _cross_kind_slug_conflict(slug: str, target_page_type: str) -> str | None:
    """Return the page_type that already owns `slug` under a DIFFERENT kind's
    directory, or None. Used to forbid `food-noise` existing as both a concept
    and an entity (split citations / ambiguous wikilink resolution)."""
    for pt in ("entity", "concept", "synthesis", "moc"):
        if pt == target_page_type:
            continue
        schema = wiki_pages.schema_for_type(pt)
        if schema is None:
            continue
        if (paths.knowledge_root() / schema.directory / f"{slug}.md").exists():
            return pt
    return None


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
        old_front = dict(front)
        front["wiki_pages"] = existing
        if not validator.validate_source_frontmatter_diff(old_front, front).ok:
            return
        write_atomic(raw_path, fm.serialize(front, body))


def _find_source(source_id: str):
    for source_type in paths.SOURCE_TYPES:
        candidate = paths.raw_source_path(source_type, source_id)
        if candidate.exists():
            return source_type, candidate
    return None
