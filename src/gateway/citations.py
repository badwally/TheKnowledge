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
    whether the same line contains a `[[sources/...]]` citation.
    """
    lines, code_mask = _strip_code_fences(body)
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
            words = sentence.split()
            if len(words) < _MIN_CLAIM_WORDS:
                continue
            has_citation = bool(_CITATION_LINE_RE.search(raw_line))
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
