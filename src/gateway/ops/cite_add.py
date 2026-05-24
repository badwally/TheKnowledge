"""`wiki cite-add <page> "<claim>" <source-id> [--fuzzy]` — claim-text-driven
citation insertion (K1 / M48).

Solves the high-friction case the original `wiki cite` doesn't cover:
users (and agents) often know which *claim* needs a source but not the
exact file line number. `cite_add` resolves the claim to a line via an
escalation pipeline, then delegates to `cite()` for the actual write so
all of cite's invariants (bidirectional backlinks, atomic write,
file_lock, log append) are inherited.

Per D5, the escalation pipeline is:

1. **Exact** substring match in the page body.
2. **Normalized** substring match: NFKC unicode-normalize +
   ``casefold`` + collapse internal whitespace + tolerate trailing
   punctuation. Catches the realistic copy-paste failure modes (smart
   quotes, em-dash drift, extra spaces).
3. **Fuzzy** (LLM-judged) — only when ``fuzzy=True`` (off by default).
   Asks an LLM "find the best matching line in this body for this
   claim." The LLM call is one Sonnet/Haiku call; cost is small but
   non-zero, so opt-in only.

At any step:
- 1 hit → resolve to file-line and call ``cite()``
- 2+ hits → ambiguity error with the matching line numbers
- 0 hits at final step → error with 3 nearest-by-edit-distance candidates

The default (deterministic) path covers ~90% of real failures of bare
exact match without an LLM call. The fuzzy escalation is for the
agentic capture-to-cite case (Phase 3 `AGT-7`).
"""

from __future__ import annotations

from dataclasses import dataclass
import re
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable, Protocol

from gateway import frontmatter as fm
from gateway import paths
from gateway.core import OperationResult
from gateway.ops.cite import cite


class FuzzyResolverClient(Protocol):
    """LLM-driven claim resolver. Returns a 1-indexed file line or None."""

    def resolve(self, claim_text: str, body: str) -> int | None: ...


@dataclass
class _Match:
    body_line: int   # 1-indexed within `body` (not file)
    body_text: str


# --- normalization ---------------------------------------------------------


_WHITESPACE_RE = re.compile(r"\s+")
_TRAIL_PUNCT_RE = re.compile(r"[.,;:!?—–\-]+\s*$")


def _normalize(s: str) -> str:
    """NFKC + casefold + collapse whitespace + strip trailing punctuation.

    Robust to: straight-vs-curly quotes, em-dash drift, extra spaces,
    case differences, trailing periods.
    """
    s = unicodedata.normalize("NFKC", s).casefold()
    s = _WHITESPACE_RE.sub(" ", s).strip()
    s = _TRAIL_PUNCT_RE.sub("", s)
    return s


def _find_exact_matches(body: str, claim: str) -> list[_Match]:
    matches: list[_Match] = []
    for i, line in enumerate(body.splitlines(), start=1):
        if claim in line:
            matches.append(_Match(body_line=i, body_text=line))
    return matches


def _find_normalized_matches(body: str, claim: str) -> list[_Match]:
    norm_claim = _normalize(claim)
    if not norm_claim:
        return []
    matches: list[_Match] = []
    for i, line in enumerate(body.splitlines(), start=1):
        if norm_claim in _normalize(line):
            matches.append(_Match(body_line=i, body_text=line))
    return matches


def _nearest_by_similarity(body: str, claim: str, *, top: int = 3) -> list[_Match]:
    """Return top-N lines closest to `claim` by SequenceMatcher ratio."""
    norm_claim = _normalize(claim)
    scored: list[tuple[float, _Match]] = []
    for i, line in enumerate(body.splitlines(), start=1):
        if not line.strip():
            continue
        ratio = SequenceMatcher(None, norm_claim, _normalize(line)).ratio()
        scored.append((ratio, _Match(body_line=i, body_text=line)))
    scored.sort(key=lambda t: t[0], reverse=True)
    return [m for _r, m in scored[:top]]


# --- main op ---------------------------------------------------------------


def cite_add(
    page_path: str | Path,
    *,
    claim_text: str,
    source_id: str,
    fuzzy: bool = False,
    fuzzy_client: FuzzyResolverClient | None = None,
) -> OperationResult:
    """Resolve `claim_text` to a line of `page_path` and add `[[sources/<id>]]`.

    Args:
        page_path: Path to a wiki page (under wiki/).
        claim_text: The claim sentence to find. Resolution is deterministic
            (exact → normalized substring) by default; pass ``fuzzy=True``
            to enable an LLM fallback when both deterministic stages miss.
        source_id: The source id to cite (must already exist as
            ``raw/<type>/<id>.md`` and ``wiki/sources/<id>.md``).
        fuzzy: If True, fall back to an LLM resolver when normalized
            substring matching misses. The LLM call is gated on this
            flag so deterministic calls stay free.
        fuzzy_client: Optional injection of the fuzzy resolver. Defaults
            to a Claude-CLI-backed implementation (not built here; agents
            and the default CLI flow can wire one in for production
            captures). Tests inject stubs.

    Returns:
        OperationResult from the underlying ``cite()`` call, or an error
        result describing the resolution failure (ambiguous claim,
        not-found, etc.).
    """
    target = Path(page_path).expanduser()
    if not target.is_absolute():
        target = (paths.knowledge_root() / target).resolve()

    if not target.exists():
        return OperationResult(success=False, errors=[f"page not found: {target}"])

    if not claim_text or not claim_text.strip():
        return OperationResult(
            success=False, errors=["claim_text must be non-empty"]
        )

    try:
        page_text = target.read_text()
        _, body = fm.parse(page_text)
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"frontmatter: {e}"])

    body_offset = fm.body_line_offset(page_text)

    # Idempotency short-circuit: if the page already cites this source on
    # any line that contains the claim text (exact OR normalized), treat
    # this as a no-op.
    citation_token = f"[[sources/{source_id}]]"
    for line in body.splitlines():
        if citation_token in line:
            if claim_text in line or _normalize(claim_text) in _normalize(line):
                return OperationResult(
                    success=True,
                    no_op=True,
                    summary=f"already cited: claim already references {source_id}",
                )

    # Stage 1: exact substring
    exact = _find_exact_matches(body, claim_text)
    if len(exact) == 1:
        return _delegate_cite(target, body_offset, exact[0], source_id)
    if len(exact) > 1:
        return _ambiguous(exact, body_offset, stage="exact")

    # Stage 2: normalized substring
    normalized = _find_normalized_matches(body, claim_text)
    if len(normalized) == 1:
        return _delegate_cite(target, body_offset, normalized[0], source_id)
    if len(normalized) > 1:
        return _ambiguous(normalized, body_offset, stage="normalized")

    # Stage 3: fuzzy (opt-in)
    if fuzzy:
        if fuzzy_client is None:
            return OperationResult(
                success=False,
                errors=[
                    "fuzzy=True requires a fuzzy_client (no default wired). "
                    "Inject a FuzzyResolverClient or use a CLI flow that "
                    "supplies one."
                ],
            )
        try:
            file_line = fuzzy_client.resolve(claim_text, body)
        except Exception as e:  # noqa: BLE001
            return OperationResult(
                success=False,
                errors=[f"fuzzy resolver failed: {e}"],
            )
        if file_line is None:
            return _not_found(body, claim_text, fuzzy_tried=True)
        # The LLM returns a *file-line* (we asked for file-relative lines so
        # downstream cite() can consume directly).
        return cite(target, [(file_line, source_id)])

    return _not_found(body, claim_text, fuzzy_tried=False)


def _delegate_cite(
    target: Path,
    body_offset: int,
    match: _Match,
    source_id: str,
) -> OperationResult:
    file_line = match.body_line + body_offset
    return cite(target, [(file_line, source_id)])


def _ambiguous(
    matches: list[_Match],
    body_offset: int,
    *,
    stage: str,
) -> OperationResult:
    file_lines = [m.body_line + body_offset for m in matches]
    lines_csv = ", ".join(str(n) for n in file_lines)
    return OperationResult(
        success=False,
        errors=[
            f"ambiguous claim — matches {len(matches)} lines ({stage} match): "
            f"file-lines {lines_csv}. Re-run with `wiki cite <page> "
            f"<line>:<source>` to disambiguate by exact line number."
        ],
    )


def _not_found(body: str, claim_text: str, *, fuzzy_tried: bool) -> OperationResult:
    nearest = _nearest_by_similarity(body, claim_text, top=3)
    if not nearest:
        suggestion_text = "(page body is empty or has no candidate lines)"
    else:
        suggestion_lines = [
            f"  line {m.body_line} (body-relative): {m.body_text.strip()[:120]}"
            for m in nearest
        ]
        suggestion_text = "Nearest matches by edit distance:\n" + "\n".join(suggestion_lines)
    suffix = "" if fuzzy_tried else " — try --fuzzy if the claim was paraphrased"
    return OperationResult(
        success=False,
        errors=[
            f"claim not found in page{suffix}.\n{suggestion_text}"
        ],
    )
