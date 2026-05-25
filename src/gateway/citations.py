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

# ONT-2: CiTO 8-verb typed citation subset (WIKI § 5.6).
# Syntax: [[sources/<id>|<verb>]] — the alias position carries the relation type.
_CITO_VERBS = frozenset({
    "supports",
    "disputes",
    "extends",
    "qualifies",
    "confirms",
    "reviews",
    "usesMethodIn",
    "citesAsAuthority",
})

# Matches aliased source wikilinks: [[sources/<id>|<alias>]] — group 1 is the alias.
_ALIASED_SOURCE_RE = re.compile(r"\[\[sources/[^\]\|]+\|([^\]]+)\]\]")


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

# NotebookLM-internal corpus citation: `[[nlm:<uuid>]]`. Emitted by
# NLM-authored synthesis pages as chunk-level handles into the corpus
# (the page's `nlm_notebook_id`). Treated as valid grounding for the
# citation-grounding rule — the validator does not verify UUID existence
# (that would require live NLM API access; out of scope here).
_NLM_CITATION_LINE_RE = re.compile(r"\[\[nlm:[^\]]+\]\]")

# Lines that are pure bold-wrapped text (used as visual sub-headers in
# orchestrator-rendered syntheses): "**1. Scope ... vs. Foo**".
_BOLD_HEADER_RE = re.compile(r"^\*\*.+\*\*$")

# Orchestrator-emitted metadata at the top of each synthesis page.
_SYNTHESIS_META_RE = re.compile(
    r"^\*\*(?:Origin question|Session|Branch):\*\*\s"
)

# NotebookLM-emitted structural-frame labels in synthesis pages. Lines of the
# form `**<label>:** <content>` where `<label>` is one of these are metadata
# about the synthesis structure (which themes are being compared, what
# foundational sources are shared) — they describe the analysis frame, not
# claims about the world, so they do not need per-line citation.
#
# This is an explicit allowlist (not a heuristic) so a real claim hiding as
# `**Finding:** Drug X causes Y` still gets flagged. Extend the set when
# NotebookLM introduces a new frame label.
_STRUCTURAL_FRAME_LABELS = frozenset({
    "Themes Used In",
    "Which themes draw on it",
    "Which themes use it",
    "Items Compared",
    "Name and key claim",
    "Core approach/mechanism",
    "Concrete details",
    "Differences in Evidence",
    "Trade-offs and Contexts",
    "Strengths and Weaknesses",
    "Context",
    # M45.1 (2026-05-13): observed in the ML-models-for-reserve-studies run.
    # NotebookLM uses these as structural sub-headers under "Gaps" /
    # "Limitations" / "Tensions" sections to call out the specific issue.
    "Gap Identified",
    "Limitation Identified",
    "Tension Identified",
})

_STRUCTURAL_FRAME_LABEL_RE = re.compile(r"^\*\*([^*]+?):\*\*\s")


# M45: aggregate-framing opener allowlist. The first claim sentence of a
# `## ` section is exempt from per-claim citation when the page declares
# `synthesizes:` (with ≥2 entries) and the corresponding `## Included works`
# section mirrors that list. The exemption is bounded — only one opener per
# section — so subsequent claims in the same paragraph still require direct
# citation. Patterns observed empirically on NotebookLM cross-cutting
# branches (2026-05-12, 2026-05-13 runs); extend as new patterns appear.
_AGGREGATE_FRAMING_OPENERS_RE = re.compile(
    r"^(?:"
    r"Based on the (?:provided sources|corpus|previous thematic analysis|conversation history)"
    r"|Across the corpus"
    r"|Across (?:all )?(?:the )?(?:sources|themes)"
    r"|Looking across (?:all )?(?:the )?(?:themes|sources)"
    r"|Aggregating across (?:all )?(?:the )?(?:themes|sources)"
    r"|Across the (?:provided )?sources"
    r")\b",
    re.IGNORECASE,
)


# M45: a synthesizes: list entry like `sources/web-...` or `synthesis/<slug>`.
# Mixed types within one list are forbidden by the validator (one-level
# strict typing; see M45 design § 3.6 invariant 1).
_SYNTHESIZES_ENTRY_RE = re.compile(r"^(sources|synthesis)/[A-Za-z0-9][A-Za-z0-9_-]*$")


def is_aggregate_framing_opener(sentence: str) -> bool:
    """Return True if `sentence` matches the M45 aggregate-framing opener
    allowlist — patterns that legitimately aggregate across a page's
    `synthesizes:` set without per-source citation.
    """
    return bool(_AGGREGATE_FRAMING_OPENERS_RE.match(sentence.lstrip()))

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
    - NotebookLM structural-frame labels (allowlist in
      `_STRUCTURAL_FRAME_LABELS`) and the continuation line that carries
      their value when NotebookLM splits label/value across two lines

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
    # M44.3: track whether the most recent non-blank line was a bare
    # structural-frame label (e.g., `**Which themes use it:**` on its own
    # line). When True, the next non-blank line is the label's value and
    # also gets the structural exemption. Blank lines do NOT clear the
    # flag — markdown often inserts one between label and value.
    expect_continuation = False
    for idx, raw_line in enumerate(lines):
        if code_mask[idx]:
            continue
        line = raw_line.strip()
        if not line:
            continue
        if _HEADER_RE.match(raw_line):
            expect_continuation = False
            continue

        stripped = _LIST_BULLET_RE.sub("", raw_line, count=1)
        stripped = _NUMBERED_RE.sub("", stripped, count=1).strip()
        if not stripped:
            continue

        # Skip orchestrator-rendered synthesis metadata
        # (`**Origin question:** ...`, `**Session:** ...`, `**Branch:** ...`).
        if _SYNTHESIS_META_RE.match(stripped):
            expect_continuation = False
            continue

        # Multi-line continuation: the previous non-blank line was a bare
        # structural-frame label, so this line is its value — exempt it
        # the same way we exempt the label itself.
        if expect_continuation:
            expect_continuation = False
            continue

        # Skip lines that are fully bold-wrapped (used as visual sub-headers
        # by `_make_branch_synthesis_update`'s comparison sections). When the
        # bold inner text is a structural-frame label with a trailing colon,
        # also expect the next non-blank line to be its value.
        if _BOLD_HEADER_RE.match(stripped):
            inner = stripped[2:-2]
            if inner.endswith(":") and inner[:-1].strip() in _STRUCTURAL_FRAME_LABELS:
                expect_continuation = True
            continue

        # Skip NotebookLM structural-frame labels (e.g.,
        # `**Themes Used In:** Component-Level Degradation Modeling, ...`).
        # These describe the analysis structure, not claims about the world.
        # Restricted to a small allowlist so real claims still get flagged.
        frame_match = _STRUCTURAL_FRAME_LABEL_RE.match(stripped)
        if frame_match and frame_match.group(1).strip() in _STRUCTURAL_FRAME_LABELS:
            expect_continuation = False
            continue

        # Past the structural-frame checks — if we reach here, this line
        # is a claim candidate and should reset the continuation flag.
        expect_continuation = False

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
            has_citation = (
                bool(_CITATION_LINE_RE.search(raw_line))
                or bool(_NLM_CITATION_LINE_RE.search(raw_line))
                or _line_cites_via_footnote(raw_line, footnote_map)
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


def uncited_claims(body: str, front: dict | None = None) -> list[ClaimSentence]:
    """Return only the claim sentences that are missing a source citation.

    M45: when `front` is supplied and contains a valid `synthesizes:` list
    (≥2 entries, mirrored by `## Included works`), the first claim
    sentence of each `## ` section that matches the aggregate-framing
    opener allowlist (`is_aggregate_framing_opener`) is exempt — it's a
    legitimate aggregate observation backed by the enumerated constituent
    set rather than a single source.
    """
    exempt_lines = aggregate_exempt_lines(body, front or {})
    return [
        c for c in find_claim_sentences(body)
        if not c.has_citation and c.line_no not in exempt_lines
    ]


# --- M45: synthesizes / Included works helpers ------------------------------


def aggregate_exempt_lines(body: str, front: dict) -> set[int]:
    """Return the set of 1-indexed line numbers that are exempt from
    citation grounding under the M45 aggregate-framing rule.

    Conditions (all must hold):
    - `front['synthesizes']` is a list with ≥ 2 entries
    - all entries are validly-shaped `(sources|synthesis)/<slug>`
    - all entries are same tier (all `sources/` or all `synthesis/`)
    - `## Included works` section exists and mirrors the list 1:1

    For each `## ` section in the body, the FIRST claim-shaped line that
    matches the aggregate-framing opener allowlist is exempt; later
    claims in the same section are not.
    """
    synth = front.get("synthesizes") if isinstance(front, dict) else None
    if not isinstance(synth, list) or len(synth) < 2:
        return set()
    if not all(
        isinstance(e, str) and _SYNTHESIZES_ENTRY_RE.match(e) for e in synth
    ):
        return set()
    tiers = {e.split("/", 1)[0] for e in synth}
    if len(tiers) != 1:
        return set()
    if not _included_works_mirrors_synthesizes(body, synth):
        return set()

    exempt: set[int] = set()
    lines = body.split("\n")
    seen_opener_in_section = True  # nothing exempted before the first `## ` section
    for idx, raw_line in enumerate(lines):
        if _HEADER_RE.match(raw_line):
            seen_opener_in_section = False
            continue
        if seen_opener_in_section:
            continue
        stripped = _LIST_BULLET_RE.sub("", raw_line, count=1)
        stripped = _NUMBERED_RE.sub("", stripped, count=1).strip()
        if not stripped:
            continue
        # Take the first sentence on this line.
        first_sentence = _SENTENCE_END_RE.split(stripped, 1)[0].strip()
        if first_sentence and is_aggregate_framing_opener(first_sentence):
            exempt.add(idx + 1)
            seen_opener_in_section = True
    return exempt


def _included_works_mirrors_synthesizes(body: str, synthesizes: list[str]) -> bool:
    """Return True if `## Included works` section body has wikilinks that
    exactly match `synthesizes`."""
    section_body = _extract_section_body(body, "Included works")
    if section_body is None:
        return False
    targets: set[str] = set()
    for m in _WIKILINK_RE.finditer(section_body):
        target = m.group(1).strip().split("#", 1)[0]  # drop #anchor
        targets.add(target)
    return targets == set(synthesizes)


def _extract_section_body(body: str, section_name: str) -> str | None:
    """Return the text between `## <section_name>` and the next `## ` header,
    or None if the section is absent."""
    section_header_re = re.compile(
        rf"^\s*##\s+{re.escape(section_name)}\s*$"
    )
    next_section_re = re.compile(r"^\s*##\s+")
    in_section = False
    out: list[str] = []
    for line in body.split("\n"):
        if in_section:
            if next_section_re.match(line):
                break
            out.append(line)
        elif section_header_re.match(line):
            in_section = True
    return "\n".join(out) if in_section else None


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
