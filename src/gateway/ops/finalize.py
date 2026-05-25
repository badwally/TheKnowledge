"""`wiki finalize <page-path>` per WIKI § 5.5.

Re-runs the full validator with the citation-grounding rule restored to
rejection (no draft downgrade). On success, clears `draft: true` and
`draft_started_at` and sets `finalized_at`. On failure, returns the
unresolved rules.

`--abandon` deletes the draft page and removes its backlinks instead.

Idempotency: finalizing an already-finalized page is a no-op (returns success with no writes).
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from gateway import frontmatter as fm
from gateway import log, paths, validator, wiki_pages
from gateway.core import OperationResult, write_atomic
from gateway.locking import file_lock


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def finalize(page_path: str | Path, *, abandon: bool = False) -> OperationResult:
    target = Path(page_path).expanduser()
    if not target.is_absolute():
        target = (paths.knowledge_root() / target).resolve()

    if not target.exists():
        return OperationResult(success=False, errors=[f"page not found: {target}"])

    try:
        rel = target.relative_to(paths.knowledge_root())
    except ValueError:
        return OperationResult(
            success=False,
            errors=[f"page is outside KNOWLEDGE_ROOT: {target}"],
        )

    page_type = wiki_pages.page_type_for_path(rel)
    if page_type is None:
        return OperationResult(
            success=False,
            errors=[f"path does not point at a known wiki page type: {rel}"],
        )

    try:
        page_text = target.read_text()
        front, body = fm.parse(page_text)
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"frontmatter: {e}"])
    # K1/D2: compute file-line offset so validator errors are file-relative
    # (matching `wiki cite`/`wiki cite-add` line numbering).
    body_offset = fm.body_line_offset(page_text)

    if not front.get("draft"):
        return OperationResult(
            success=False,
            errors=[f"page is not a draft (no `draft: true` in frontmatter)"],
        )

    if abandon:
        return _abandon(target, rel, front)

    # Re-validate with the draft flag stripped from a *copy* so the citation
    # rule is restored to rejection. The on-disk file keeps `draft: true`
    # until validation passes.
    strict_front = {k: v for k, v in front.items() if k not in ("draft", "draft_started_at", "draft_unresolved_claims")}
    result = validator.validate_wiki_page(
        strict_front, body, page_type, draft=False, body_line_offset=body_offset
    )
    if not result.ok:
        return OperationResult(
            success=False,
            errors=[
                "cannot finalize — citation grounding still has unresolved claims:",
                *(str(e) for e in result.errors),
            ],
        )

    front.pop("draft", None)
    front.pop("draft_started_at", None)
    front.pop("draft_unresolved_claims", None)
    front["finalized_at"] = _now_iso()

    with file_lock("wiki-author"):
        write_atomic(target, fm.serialize(front, body))
        log.append(
            op="finalize",
            fields={"page": str(rel)},
            summary=f"finalized {rel}",
        )

    return OperationResult(
        success=True,
        paths_touched=[target, paths.log_path()],
        summary=f"finalized: {rel}",
    )


def _abandon(target: Path, rel: Path, front: dict) -> OperationResult:
    """Delete the draft page; remove backlinks from any source pages that
    reference it via `wiki_pages:`."""
    rel_str = str(rel)
    sources_touched = []
    for source_type in paths.SOURCE_TYPES:
        for raw in (paths.raw_dir() / source_type).glob("*.md"):
            try:
                rfront, rbody = fm.parse(raw.read_text())
            except fm.FrontmatterError:
                continue
            wiki_pages_list = list(rfront.get("wiki_pages") or [])
            if rel_str in wiki_pages_list:
                wiki_pages_list.remove(rel_str)
                rfront["wiki_pages"] = wiki_pages_list
                write_atomic(raw, fm.serialize(rfront, rbody))
                sources_touched.append(raw)

    target.unlink(missing_ok=True)
    log.append(
        op="finalize-abandon",
        fields={"page": rel_str, "backlinks_removed": len(sources_touched)},
        summary=f"abandoned draft {rel_str}",
    )

    return OperationResult(
        success=True,
        paths_touched=[target, *sources_touched, paths.log_path()],
        summary=f"abandoned: {rel}",
    )
