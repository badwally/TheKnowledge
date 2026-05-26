"""QUAL-14: Source-decay re-ingest policy (supersedes / superseded_by).

When a source is revised (arXiv v2, edited blog post), `wiki reingest` creates
a new versioned source (`<base>-v2`, `-v3`, …), preserves both, and links them
via `supersedes` / `superseded_by` in raw frontmatter. Body content of the old
source remains immutable — only the frontmatter `superseded_by` field is updated.

The new source goes through the normal ingest pipeline (converter, filter,
wiki/sources page).  The old source's `superseded_by` field is a pipeline-stage
mutation allowed under WIKI § 11.5 (same category as `retracted`).

QUAL-8 (semantic citation-claim coherence) is deferred — this op returns the
list of wiki pages that cite the old source so the caller can review them.
"""

from __future__ import annotations

import re
from pathlib import Path

from gateway import frontmatter as fm, log, paths
from gateway.core import OperationResult, write_atomic
from gateway.filter.semantic import FilterClient
from gateway.locking import file_lock
from gateway.ops.ingest import ingest


_VERSION_SUFFIX_RE = re.compile(r"-v(\d+)$")


def _version_base(source_id: str) -> tuple[str, int]:
    """Return (base, current_version) for a source_id.

    'web-2026-01-15-abc'    → ('web-2026-01-15-abc', 1)
    'web-2026-01-15-abc-v2' → ('web-2026-01-15-abc', 2)
    """
    m = _VERSION_SUFFIX_RE.search(source_id)
    if m:
        return source_id[: m.start()], int(m.group(1))
    return source_id, 1


def _next_version_id(source_id: str) -> str:
    """Return the next versioned ID: 'foo' → 'foo-v2'; 'foo-v2' → 'foo-v3'."""
    base, ver = _version_base(source_id)
    return f"{base}-v{ver + 1}"


def _find_raw_path(source_id: str) -> Path | None:
    """Locate the raw source file for source_id."""
    for source_type in paths.SOURCE_TYPES:
        p = paths.raw_source_path(source_type, source_id)
        if p.exists():
            return p
    return None


def _affected_wiki_pages(source_id: str) -> list[str]:
    """Find wiki pages that contain [[sources/<source_id>]] citation tokens."""
    pattern = f"[[sources/{source_id}]]"
    affected: list[str] = []
    wiki = paths.wiki_dir()
    for p in wiki.rglob("*.md"):
        try:
            if pattern in p.read_text(encoding="utf-8"):
                affected.append(str(p.relative_to(wiki)))
        except OSError:
            continue
    return sorted(affected)


def reingest(
    source_id: str,
    new_input: str | Path,
    *,
    domain: str | None = None,
    filter_client: FilterClient | None = None,
) -> OperationResult:
    """Re-ingest a revised source.

    Creates `<source_id>-vN` as a new source, links old ↔ new via
    `superseded_by` / `supersedes` frontmatter, and returns the list of wiki
    pages that cite the old source so the caller can review affected claims.
    """
    # 1. Find and parse the old source
    old_raw_path = _find_raw_path(source_id)
    if old_raw_path is None:
        return OperationResult(
            success=False,
            errors=[f"source {source_id!r} not found in raw/"],
        )

    try:
        old_front, old_body = fm.parse(old_raw_path.read_text(encoding="utf-8"))
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"old source frontmatter: {e}"])

    if old_front.get("superseded_by"):
        existing_successor = old_front["superseded_by"]
        return OperationResult(
            success=False,
            errors=[
                f"source {source_id!r} is already superseded by {existing_successor!r}; "
                f"reingest the successor instead"
            ],
        )

    # 2. Determine the new version ID
    new_id = _next_version_id(source_id)
    # Keep incrementing until we find a free slot
    while _find_raw_path(new_id) is not None:
        new_id = _next_version_id(new_id)

    # 3. Ingest the new source via the standard ingest pipeline
    ingest_result = ingest(
        Path(new_input) if isinstance(new_input, str) else new_input,
        domain=domain or (old_front.get("domains") or [None])[0],
        filter_client=filter_client,
    )

    if not ingest_result.success:
        return OperationResult(
            success=False,
            errors=[f"re-ingest conversion failed: {e}" for e in ingest_result.errors],
        )

    # 4. Find the new raw file (it was written by ingest; locate it)
    new_raw_path = _find_from_ingest_result(ingest_result)
    if new_raw_path is None:
        # Fallback: ingest succeeded but the path wasn't in paths_touched
        # (e.g., no-op idempotency). Try locating by new_id.
        new_raw_path_by_id = _find_raw_path(new_id)
        if new_raw_path_by_id is None:
            return OperationResult(
                success=False,
                errors=["could not locate newly ingested raw file"],
            )
        new_raw_path = new_raw_path_by_id

    # 5. Determine the actual new source_id from the ingested file's frontmatter
    try:
        new_front, new_body = fm.parse(new_raw_path.read_text(encoding="utf-8"))
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"new source frontmatter: {e}"])

    actual_new_id = new_front.get("id") or new_id

    # 6. Stamp supersedes on the new source
    with file_lock(f"ingest-{actual_new_id}"):
        new_front["supersedes"] = [source_id]
        write_atomic(new_raw_path, fm.serialize(new_front, new_body))

    # 7. Stamp superseded_by on the old source (frontmatter-only mutation)
    with file_lock(f"ingest-{source_id}"):
        old_front["superseded_by"] = actual_new_id
        write_atomic(old_raw_path, fm.serialize(old_front, old_body))

    # 8. Find affected wiki pages
    affected = _affected_wiki_pages(source_id)

    log.append(
        op="reingest",
        fields={
            "old_id": source_id,
            "new_id": actual_new_id,
            "affected_pages": len(affected),
        },
        summary=f"reingested {source_id!r} → {actual_new_id!r}; {len(affected)} wiki page(s) affected",
    )

    touched = [old_raw_path, new_raw_path, paths.log_path()]
    touched.extend(ingest_result.paths_touched)
    # deduplicate preserving order
    seen: set[str] = set()
    deduped: list[Path] = []
    for p in touched:
        key = str(p)
        if key not in seen:
            seen.add(key)
            deduped.append(p)

    return OperationResult(
        success=True,
        paths_touched=deduped,
        summary=(
            f"reingested: {source_id!r} → {actual_new_id!r}; "
            f"{len(affected)} wiki page(s) cite the old source"
        ),
        data={
            "old_id": source_id,
            "new_id": actual_new_id,
            "affected_pages": affected,
        },
    )


def _find_from_ingest_result(result: OperationResult) -> Path | None:
    """Extract the raw source path from an ingest OperationResult."""
    for p in (result.paths_touched or []):
        if "raw/" in str(p) and str(p).endswith(".md"):
            return p
    return None
