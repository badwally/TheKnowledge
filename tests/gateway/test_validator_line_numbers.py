"""K1 (M48): validator line-number convention per D2.

Validator error messages must report **file-relative** line numbers
(including frontmatter) so users can copy them directly into `wiki cite`
without manual offset calculation.

Pre-fix behavior: validator reported body-relative line numbers; `wiki
cite` expected file-relative. Documented as M46 followup #6 and resolved
in K1 by adding a `body_line_offset` parameter that callers compute
from the source text via `frontmatter.body_line_offset`.
"""

from __future__ import annotations

import pytest

from gateway import frontmatter as fm
from gateway import validator


def _build_synthesis_page(body_claims: list[str], front_kvs: int = 8) -> str:
    """Construct a synthesis page with a known frontmatter line count.

    `front_kvs` controls the number of frontmatter key:value lines (so
    the body offset is predictable).
    """
    front_lines = ["---", "type: synthesis", "slug: test-synth",
                   "canonical_name: Test", "domains:", "- testdom"]
    while len(front_lines) - 1 < front_kvs:
        front_lines.append(f"extra_field_{len(front_lines)}: value")
    front_lines.append("---")
    front_lines.append("")  # blank separator
    body_lines = ["# Test Synthesis", "", "## Summary", ""] + body_claims
    return "\n".join(front_lines + body_lines)


# --- body_line_offset helper ------------------------------------------------


def test_body_line_offset_basic_frontmatter():
    text = "---\nkey: val\n---\nbody line 1\nbody line 2\n"
    # lines: ['---', 'key: val', '---', 'body line 1', ...]
    # closing --- at index 2; body starts at index 3 → offset 3
    assert fm.body_line_offset(text) == 3


def test_body_line_offset_no_frontmatter():
    text = "plain text\nno frontmatter\n"
    assert fm.body_line_offset(text) == 0


def test_body_line_offset_multi_line_frontmatter():
    text = "---\na: 1\nb: 2\nc: 3\nd: 4\n---\nbody\n"
    # closing --- at index 5; offset = 6
    assert fm.body_line_offset(text) == 6


def test_body_line_offset_empty_text():
    assert fm.body_line_offset("") == 0


# --- validate_citation_grounding with offset --------------------------------


def test_validate_citation_grounding_default_offset_preserves_body_line():
    """Default `body_line_offset=0` preserves pre-K1 behavior for old callers."""
    body = "# Title\n\n## Summary\n\nAn uncited claim sentence with substance.\n"
    result = validator.validate_citation_grounding(body, "synthesis", draft=False)
    assert result.errors, "expected at least one citation-grounding error"
    # With offset=0, line numbers are body-relative
    assert any("line 5" in str(e) or "line 4" in str(e) or "line 6" in str(e)
               for e in result.errors), (
        f"expected body-line error, got: {[str(e) for e in result.errors]}"
    )


def test_validate_citation_grounding_offset_shifts_line_number():
    """Non-zero body_line_offset shifts line numbers to file-relative."""
    body = "# Title\n\n## Summary\n\nAn uncited claim sentence with substance.\n"
    # Pretend the frontmatter occupies 10 file lines.
    result = validator.validate_citation_grounding(
        body, "synthesis", draft=False, body_line_offset=10
    )
    assert result.errors
    # Each reported line should be original + 10
    # body claim is at body-line ~5; with offset 10 → file-line ~15
    msgs = " ".join(str(e) for e in result.errors)
    # Look for any double-digit (15-ish) line reference
    import re
    nums = [int(m) for m in re.findall(r"line (\d+):", msgs)]
    assert nums, f"no 'line N:' pattern in errors: {msgs}"
    # All reported lines must be >= 10 (since offset is 10 and minimum body-line is 1)
    assert all(n >= 10 for n in nums), f"lines {nums} did not all shift by offset 10"


# --- validate_wiki_page propagation -----------------------------------------


def test_validate_wiki_page_accepts_and_propagates_body_line_offset():
    """When validate_wiki_page receives `body_line_offset`, citation errors
    surface file-relative line numbers."""
    text = _build_synthesis_page(["This is a substantive bald claim sentence that lacks any source citation at all.\n"])
    front, body = fm.parse(text)
    offset = fm.body_line_offset(text)

    result = validator.validate_wiki_page(
        front, body, "synthesis", body_line_offset=offset
    )
    citation_errs = [e for e in result.errors if e.rule == "citation-grounding"]
    assert citation_errs, f"expected citation-grounding error; got {result.errors}"

    import re
    nums = [int(m) for s in (str(e) for e in citation_errs)
            for m in re.findall(r"line (\d+):", s)]
    # The claim is at body-line ~5; offset accounts for frontmatter (~9 lines).
    # File-line should be > offset (i.e., > 9 in this fixture).
    assert all(n > offset for n in nums), (
        f"expected file-relative lines > offset {offset}; got {nums}"
    )


def test_validate_wiki_page_default_offset_zero_back_compat():
    """Callers that don't pass body_line_offset (existing tests, lint) keep
    their pre-K1 behavior."""
    text = _build_synthesis_page(["This is a substantive uncited claim sentence that should trip the heuristic.\n"])
    front, body = fm.parse(text)

    result = validator.validate_wiki_page(front, body, "synthesis")
    citation_errs = [e for e in result.errors if e.rule == "citation-grounding"]
    assert citation_errs
    # Without offset, line numbers should be small (body-relative ~5)
    import re
    nums = [int(m) for s in (str(e) for e in citation_errs)
            for m in re.findall(r"line (\d+):", s)]
    assert all(n < 10 for n in nums), (
        f"expected body-relative lines < 10 (without offset); got {nums}"
    )
