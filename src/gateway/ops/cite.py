"""`wiki cite <page-path> <line:source-id> [...]` — add citation tokens.

Sanctioned gateway path for adding `[[sources/<id>]]` tokens to specific
lines of an existing wiki page. Avoids direct file edits to `wiki/`,
which CLAUDE.md hard rule #1 prohibits.

Refuses if the target source page does not exist (`wiki/sources/<id>.md`
must already be ingested), if the source-id is malformed, or if the
target line already cites that source. Updates bidirectional backlinks
on the cited source's `raw/<type>/<id>.md` frontmatter (`wiki_pages`
list) per WIKI § 11.2.

Idempotency: re-citing the same source on the same line is rejected (duplicate guard); safe to retry after partial failure.
"""

from __future__ import annotations

from pathlib import Path

from gateway import frontmatter as fm
from gateway import log, paths
from gateway.core import OperationResult, write_atomic
from gateway.locking import file_lock
from gateway.validator import validate_source_frontmatter_diff


def cite(page_path: str | Path, additions: list[tuple[int, str]]) -> OperationResult:
    """Append `[[sources/<source_id>]]` to specific lines of a wiki page.

    Each `additions` entry is `(line_number, source_id)`, 1-indexed into
    the on-disk file (frontmatter included). Multiple additions to the
    same line are allowed (each appends one token).
    """
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

    rel_str = str(rel).replace("\\", "/")
    if not rel_str.startswith("wiki/"):
        return OperationResult(
            success=False,
            errors=[f"page is not under wiki/: {rel_str}"],
        )

    if not additions:
        return OperationResult(success=False, errors=["no citations provided"])

    errors: list[str] = []
    for ln, sid in additions:
        if ln < 1:
            errors.append(f"line number must be ≥ 1: {ln}")
        if not sid or "/" in sid or sid.startswith("."):
            errors.append(f"invalid source id: {sid!r}")
            continue
        wiki_src = paths.wiki_source_path(sid)
        if not wiki_src.exists():
            errors.append(f"source page does not exist: wiki/sources/{sid}.md")
    if errors:
        return OperationResult(success=False, errors=errors)

    text = target.read_text()
    try:
        fm.parse(text)  # ensure frontmatter parses before we touch anything
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"frontmatter: {e}"])

    lines = text.splitlines(keepends=True)

    for ln, sid in additions:
        if ln > len(lines):
            errors.append(f"line {ln} out of range (file has {len(lines)} lines)")
            continue
        token = f"[[sources/{sid}]]"
        if token in lines[ln - 1]:
            errors.append(f"line {ln} already cites {sid}")
    if errors:
        return OperationResult(success=False, errors=errors)

    sources_touched: set[str] = set()
    for ln, sid in additions:
        token = f"[[sources/{sid}]]"
        line = lines[ln - 1]
        if line.endswith("\n"):
            stripped = line[:-1].rstrip()
            lines[ln - 1] = f"{stripped} {token}\n"
        else:
            lines[ln - 1] = f"{line.rstrip()} {token}"
        sources_touched.add(sid)

    new_text = "".join(lines)
    try:
        fm.parse(new_text)  # post-write integrity check
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"frontmatter integrity broken: {e}"])

    raw_paths_touched: list[Path] = []
    with file_lock("wiki-author"):
        write_atomic(target, new_text)
        for sid in sources_touched:
            wiki_src = paths.wiki_source_path(sid)
            try:
                src_front, _ = fm.parse(wiki_src.read_text())
            except fm.FrontmatterError:
                continue
            src_type = src_front.get("source_type")
            if not src_type or src_type not in paths.SOURCE_TYPES:
                continue
            raw_path = paths.raw_source_path(src_type, sid)
            if not raw_path.exists():
                continue
            try:
                raw_front, raw_body = fm.parse(raw_path.read_text())
            except fm.FrontmatterError:
                continue
            wiki_pages_list = list(raw_front.get("wiki_pages") or [])
            if rel_str in wiki_pages_list:
                continue
            old_raw_front = dict(raw_front)
            wiki_pages_list.append(rel_str)
            raw_front["wiki_pages"] = wiki_pages_list
            if not validate_source_frontmatter_diff(old_raw_front, raw_front).ok:
                continue
            write_atomic(raw_path, fm.serialize(raw_front, raw_body))
            raw_paths_touched.append(raw_path)

        log.append(
            op="cite",
            fields={
                "page": rel_str,
                "additions": len(additions),
                "sources": len(sources_touched),
            },
            summary=f"added {len(additions)} citation(s) to {rel_str}",
        )

    return OperationResult(
        success=True,
        paths_touched=[target, *raw_paths_touched, paths.log_path()],
        summary=f"added {len(additions)} citation(s) to {rel_str}",
    )
