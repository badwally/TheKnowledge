"""Citation parsing, resolution, density per WIKI § 5.

Citations look like `[[sources/<id>]]` (optionally with an anchor: `#1820`,
`#p7`, `#para3`). This module extracts them, classifies sentences as claims,
and reports citation density. Used by the validator (M6+) and lint (M9).
"""

from __future__ import annotations

from dataclasses import dataclass
import re


# `[[ target | optional alias ]]` — capture the target.
_WIKILINK_RE = re.compile(r"\[\[([^\]\|]+?)(?:\|[^\]]+)?\]\]")

# Same shape but with the alias as a separate captured group so we can rebuild.
_WIKILINK_REWRITE_RE = re.compile(r"\[\[([^\]\|]+?)(\|[^\]]+)?\]\]")

# Markdown fenced code blocks — used to skip code from citation-grounding rules.
_FENCE_RE = re.compile(r"```")


@dataclass
class Citation:
    target: str             # e.g. "sources/yt-LfRiBJgD7sk" or "concepts/food-noise"
    anchor: str = ""        # e.g. "1820" (after #) or "" if none
    raw: str = ""           # original [[...]] text


def find_wikilinks(text: str) -> list[Citation]:
    """Return all wikilinks in `text` (any kind, not just citations)."""
    out: list[Citation] = []
    for match in _WIKILINK_RE.finditer(text):
        target = match.group(1).strip()
        anchor = ""
        if "#" in target:
            target, _, anchor = target.partition("#")
        out.append(Citation(target=target, anchor=anchor, raw=match.group(0)))
    return out


def find_source_citations(text: str) -> list[Citation]:
    """Wikilinks pointing into `sources/...`."""
    return [c for c in find_wikilinks(text) if c.target.startswith("sources/")]


# --- claim detection ---------------------------------------------------------


# Strip these structural markers when looking for claim sentences.
_HEADER_RE = re.compile(r"^\s*#{1,6}\s+", re.MULTILINE)
_LIST_BULLET_RE = re.compile(r"^\s*[-*+]\s+")
_NUMBERED_RE = re.compile(r"^\s*\d+\.\s+")
_BLANK_RE = re.compile(r"^\s*$")
_CITATION_LINE_RE = re.compile(r"\[\[sources/[^\]]+\]\]")

# Lines that are pure bold-wrapped text (used as visual sub-headers in
# orchestrator-rendered syntheses): "**1. Scope ... vs. Foo**".
_BOLD_HEADER_RE = re.compile(r"^\*\*.+\*\*$")

# Orchestrator-emitted metadata at the top of each synthesis page.
_SYNTHESIS_META_RE = re.compile(
    r"^\*\*(?:Origin question|Session|Branch):\*\*\s"
)

# Markdown footnote definition pointing into sources/: `[^12]: [[sources/<id>]]`.
# Multiple definitions can share a line (NotebookLM-rendered syntheses do this).
_FOOTNOTE_DEF_RE = re.compile(
    r"\[\^(\d+)\]:\s*(\[\[sources/[^\]]+\]\])"
)
# In-text footnote reference: `[12]`, `[1, 2]`, `[3-5]`, `[1, 4-6, 9]`.
# Negative lookbehind/lookahead exclude `[[wikilinks]]` and footnote defs.
_FOOTNOTE_REF_RE = re.compile(r"(?<!\[)\[(\d+(?:\s*[,\-]\s*\d+)*)\](?!:)")

# Heuristics for distinguishing claims from prose:
# A "claim" is a sentence containing at least 5 words that ends in
# `.`, `!`, or `?`, and is NOT inside a code fence, header, or
# list-item that's purely a label/reference.
_MIN_CLAIM_WORDS = 5
_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+")


@dataclass
class ClaimSentence:
    text: str
    line_no: int
    has_citation: bool


def _strip_code_fences(text: str) -> tuple[list[str], list[bool]]:
    """Split `text` into lines and return (lines, in_code_fence_mask)."""
    lines = text.split("\n")
    in_fence = False
    mask: list[bool] = []
    for line in lines:
        if _FENCE_RE.search(line):
            in_fence = not in_fence
            mask.append(True)  # the fence marker line itself is "code"
            continue
        mask.append(in_fence)
    return lines, mask


def _build_footnote_map(body: str) -> dict[int, str]:
    """Return ``{footnote_number: source-wikilink}`` for all
    ``[^N]: [[sources/<id>]]`` definitions found anywhere in `body`.

    Multiple definitions may share a line; each is captured independently.
    """
    out: dict[int, str] = {}
    for m in _FOOTNOTE_DEF_RE.finditer(body):
        try:
            out[int(m.group(1))] = m.group(2)
        except ValueError:
            continue
    return out


def _parse_footnote_ref_numbers(raw: str) -> list[int]:
    """Expand a footnote-ref body like ``1, 4-6, 9`` to ``[1, 4, 5, 6, 9]``."""
    numbers: list[int] = []
    for chunk in raw.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        if "-" in chunk:
            lo_s, _, hi_s = chunk.partition("-")
            try:
                lo, hi = int(lo_s.strip()), int(hi_s.strip())
            except ValueError:
                continue
            if lo <= hi:
                numbers.extend(range(lo, hi + 1))
        else:
            try:
                numbers.append(int(chunk))
            except ValueError:
                continue
    return numbers


def _line_cites_via_footnote(raw_line: str, footnote_map: dict[int, str]) -> bool:
    """Return True if `raw_line` references any footnote that resolves to a
    ``[[sources/...]]`` definition in `footnote_map`."""
    if not footnote_map:
        return False
    # Remove footnote definitions on this line so they don't self-match as refs.
    stripped = _FOOTNOTE_DEF_RE.sub("", raw_line)
    for m in _FOOTNOTE_REF_RE.finditer(stripped):
        for n in _parse_footnote_ref_numbers(m.group(1)):
            if n in footnote_map:
                return True
    return False


def find_claim_sentences(body: str) -> list[ClaimSentence]:
    """Locate sentences in `body` that look like factual claims.

    Skips:
    - lines inside ``` code fences ``` ``
    - markdown headers (## Foo)
    - bullet items that are just `[[wikilinks]]` cross-reference lists
    - blank lines
    - frontmatter-style key: value lines

    The remaining sentences (split on `.!?`) are evaluated; sentences with
    ≥ MIN_CLAIM_WORDS are returned with line numbers and a flag indicating
    whether the source is cited — either by a direct `[[sources/...]]` on
    the same line, or by an in-text footnote reference (`[N]`, `[N, M]`,
    `[N-M]`) that resolves to a `[^N]: [[sources/<id>]]` definition
    elsewhere in the page.
    """
    lines, code_mask = _strip_code_fences(body)
    footnote_map = _build_footnote_map(body)
    out: list[ClaimSentence] = []
    for idx, raw_line in enumerate(lines):
        if code_mask[idx]:
            continue
        line = raw_line.strip()
        if not line:
            continue
        if _HEADER_RE.match(raw_line):
            continue

        stripped = _LIST_BULLET_RE.sub("", raw_line, count=1)
        stripped = _NUMBERED_RE.sub("", stripped, count=1).strip()
        if not stripped:
            continue

        # Skip orchestrator-rendered synthesis metadata
        # (`**Origin question:** ...`, `**Session:** ...`, `**Branch:** ...`).
        if _SYNTHESIS_META_RE.match(stripped):
            continue

        # Skip lines that are fully bold-wrapped (used as visual sub-headers
        # by `_make_branch_synthesis_update`'s comparison sections).
        if _BOLD_HEADER_RE.match(stripped):
            continue

        # Skip lines that are only wikilinks (cross-reference lists).
        bare = _WIKILINK_RE.sub("", stripped).strip(" ·:-,;")
        if len(bare) < 3:
            continue

        # Split into sentences and qualify each.
        for sentence in _SENTENCE_END_RE.split(stripped):
            sentence = sentence.strip()
            if not sentence:
                continue
            if not sentence.endswith((".", "!", "?")):
                continue
            # Rhetorical questions (which NotebookLM uses as framing devices
            # like "How do planners decide ... ?") are not factual claims.
            if sentence.endswith("?"):
                continue
            words = sentence.split()
            if len(words) < _MIN_CLAIM_WORDS:
                continue
            has_citation = bool(_CITATION_LINE_RE.search(raw_line)) or (
                _line_cites_via_footnote(raw_line, footnote_map)
            )
            out.append(ClaimSentence(text=sentence, line_no=idx + 1, has_citation=has_citation))
    return out


def citation_density(body: str) -> tuple[int, int, float]:
    """Return (cited_claims, total_claims, ratio).

    A claim is "cited" when its source line contains any `[[sources/...]]`.
    Ratio is 1.0 when total_claims == 0 (vacuously satisfied).
    """
    claims = find_claim_sentences(body)
    total = len(claims)
    if total == 0:
        return 0, 0, 1.0
    cited = sum(1 for c in claims if c.has_citation)
    return cited, total, cited / total


def uncited_claims(body: str) -> list[ClaimSentence]:
    """Return only the claim sentences that are missing a source citation."""
    return [c for c in find_claim_sentences(body) if not c.has_citation]


# --- bulk rewrite (used by migration) --------------------------------------


def rewrite_wikilinks(text: str, mapping: dict[str, str]) -> str:
    """Rewrite `[[old-target]]` (and `[[old-target|alias]]`, `[[old-target#anchor]]`)
    to `[[new-target]]` using a {old: new} mapping.

    Targets not in the mapping are left untouched. Aliases and anchors are
    preserved verbatim.
    """
    if not mapping:
        return text

    def _replace(match: re.Match) -> str:
        target = match.group(1).strip()
        alias = match.group(2) or ""

        anchor = ""
        bare_target = target
        if "#" in target:
            bare_target, _, anchor = target.partition("#")
            anchor = f"#{anchor}"

        new_target = mapping.get(bare_target, bare_target)
        return f"[[{new_target}{anchor}{alias}]]"

    return _WIKILINK_REWRITE_RE.sub(_replace, text)
