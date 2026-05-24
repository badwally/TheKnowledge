"""`wiki edit <page> --section <name> --body-file <path>` — constrained
section-replace (K1 / M48).

Per C1, the edit surface is intentionally minimal: replace the body of
one named ``## Section``, leaving frontmatter and every other section
untouched. After the replacement the full validator runs; if validation
fails (e.g., the new body would invalidate a required-section contract,
or introduce a citation-grounding error in non-draft mode), the edit is
rejected and the file is not written.

This is the sanctioned path for non-citation amendments to wiki pages
that don't require re-running the authorship plan. Examples: rewriting
a stale Summary, swapping out an obsolete Key-facts bullet list,
revising a Cross-references list. The op acquires the same
``wiki-author`` lock that ``cite`` uses so two writers can't interleave.
"""

from __future__ import annotations

import re
from pathlib import Path

from gateway import frontmatter as fm
from gateway import log, paths, validator, wiki_pages
from gateway.core import OperationResult, write_atomic
from gateway.locking import file_lock


_HEADER_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


def edit_section(
    page_path: str | Path,
    *,
    section: str,
    new_body: str,
) -> OperationResult:
    """Replace the body of one named `## Section` in `page_path`.

    Args:
        page_path: Path to a wiki page (must be under `wiki/`).
        section: Section name to replace. Matched case-insensitively
            against `## <name>` headers. The header itself is preserved;
            only the body content between this header and the next
            same-or-higher-level header is replaced.
        new_body: Replacement markdown for the section body. May be the
            empty string (the header stays; the body becomes empty).
            Newlines are honored; a trailing newline is added if missing
            so downstream parsers see consistent block boundaries.
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
            success=False, errors=[f"page is outside KNOWLEDGE_ROOT: {target}"]
        )
    rel_str = str(rel).replace("\\", "/")
    if not rel_str.startswith("wiki/"):
        return OperationResult(
            success=False, errors=[f"page is not under wiki/: {rel_str}"]
        )

    if not section or not section.strip():
        return OperationResult(success=False, errors=["section name must be non-empty"])

    try:
        page_text = target.read_text()
        front, body = fm.parse(page_text)
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"frontmatter: {e}"])

    page_type = wiki_pages.page_type_for_path(rel_str)
    if page_type is None:
        return OperationResult(
            success=False, errors=[f"path is not a known wiki page type: {rel_str}"]
        )

    new_body_block = _build_replacement(new_body)
    try:
        new_full_body = _replace_section_body(body, section, new_body_block)
    except _SectionNotFound as e:
        return OperationResult(success=False, errors=[str(e)])

    new_full_text = fm.serialize(front, new_full_body)

    # Re-run the full validator on the result. Honor frontmatter `draft: true`.
    body_offset = fm.body_line_offset(new_full_text)
    val = validator.validate_wiki_page(
        front, new_full_body, page_type, body_line_offset=body_offset
    )
    if not val.ok:
        return OperationResult(
            success=False,
            errors=[
                "edit rejected by validator (page would no longer satisfy schema or citations):",
                *(str(e) for e in val.errors),
            ],
            warnings=[str(w) for w in val.warnings],
        )

    with file_lock("wiki-author"):
        write_atomic(target, new_full_text)
        log.append(
            op="edit-section",
            fields={"page": rel_str, "section": section},
            summary=f"edited section '{section}' in {rel_str}",
        )

    return OperationResult(
        success=True,
        paths_touched=[target, paths.log_path()],
        summary=f"edited section '{section}' in {rel_str}",
        warnings=[str(w) for w in val.warnings],
    )


class _SectionNotFound(LookupError):
    pass


def _build_replacement(new_body: str) -> str:
    """Normalize the replacement so it starts with one blank line and ends
    with one newline. The opening blank gives the prior `## Section`
    header a visual separator; the trailing newline ensures the next
    section's `## ` heading is on its own line."""
    body = new_body.rstrip("\n")
    if not body:
        return "\n"  # empty section body = single blank line under the heading
    return "\n" + body + "\n"


def _replace_section_body(body: str, section: str, replacement: str) -> str:
    """Locate `## <section>` (case-insensitive) and replace its body
    contents up to the next ``## `` (or higher-level) header.

    Returns the new body. Raises `_SectionNotFound` if the section
    header isn't present.
    """
    target_section = section.strip().casefold()

    # Scan for headers; record (start_offset, end_of_header_line, level, name)
    headers: list[tuple[int, int, int, str]] = []
    for m in _HEADER_RE.finditer(body):
        level = len(m.group(1))
        name = m.group(2).casefold()
        headers.append((m.start(), m.end(), level, name))

    target_idx: int | None = None
    target_level: int | None = None
    for i, (_start, _end, level, name) in enumerate(headers):
        if level == 2 and name == target_section:
            target_idx = i
            target_level = level
            break
    if target_idx is None:
        raise _SectionNotFound(
            f"section '## {section}' not found in page"
        )

    # End of the section: the next header at level <= target_level, or EOF.
    section_start_offset = headers[target_idx][1]  # end of `## <section>` line
    section_end_offset = len(body)
    for _start, _end, level, _name in headers[target_idx + 1 :]:
        if level <= target_level:
            section_end_offset = _start
            break

    return body[:section_start_offset] + replacement + body[section_end_offset:]
