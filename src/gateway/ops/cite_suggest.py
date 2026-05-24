"""LLM-driven citation suggestion for `wiki cite --suggest` (M49 AGT-2).

Reads a wiki draft + its declared sources, asks Sonnet 4.6 (via
``AnthropicAPIClient`` with prompt caching) to propose
``{line, source_id, evidence_quote}`` triples for unresolved claims,
then verifies each triple's evidence quote is a substring of the
proposed source's raw body. Unverified or multi-candidate suggestions
are flagged for escalation rather than auto-applied.

The Aggressive caller (``finalize-batch --suggest --execute``) applies
only suggestions with ``unambiguous=True`` and ``evidence_verified=True``.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import logging
import re

from gateway import frontmatter as fm
from gateway import paths
from gateway.llm.api_client import AnthropicAPIClient
from gateway.llm.config import model_for

_log = logging.getLogger(__name__)


@dataclass(frozen=True)
class CiteSuggestion:
    line: int
    source_id: str
    evidence_quote: str
    unambiguous: bool
    evidence_verified: bool
    skip_reason: str = ""

    @property
    def auto_appliable(self) -> bool:
        return self.unambiguous and self.evidence_verified


_SYSTEM_PROMPT = (
    "You are a citation assistant for a knowledge wiki. The user will "
    "give you a draft wiki page (with line numbers) and the raw bodies of "
    "the sources (each wrapped in <source id=\"...\"> tags) the draft was "
    "authored from. Your job: for each line "
    "containing a substantive claim that lacks any citation (neither "
    "inline `[[sources/<id>]]` nor footnote-style `[N]` with a matching "
    "footnote definition), identify which single source supports the "
    "claim and emit a JSON object of the form:\n\n"
    '{"suggestions": [{"line": <int>, "source_id": "<id>", '
    '"evidence_quote": "<verbatim substring from that source>"}]}\n\n'
    "Rules:\n"
    "- Only emit a suggestion when exactly one source supports the claim. "
    "If more than one source could support it, OMIT the line entirely.\n"
    "- `source_id` is the BARE id (e.g. `web-2024-02-07-3a2` or "
    "`yt-abc123`), WITHOUT the `sources/` prefix.\n"
    "- The `evidence_quote` must be a verbatim substring of the named "
    "source's body (preserving capitalization, punctuation, and spaces "
    "as much as possible).\n"
    "- Use 1-indexed line numbers matching the file shown to you.\n"
    "- Output strictly the JSON object — no prose, no markdown."
)


def _normalize_whitespace(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _strip_sources_prefix(source_id: str) -> str:
    """`synthesizes:` and `sources:` frontmatter entries are stored with a
    `sources/` prefix matching the inline `[[sources/<id>]]` citation form
    (e.g. `sources/web-2024-02-07-3a2`). Raw files live at
    `raw/<type>/<id>.md` with the bare id. Strip the prefix here."""
    if source_id.startswith("sources/"):
        return source_id[len("sources/"):]
    return source_id


def _read_source_body(kb_root: Path, source_id: str) -> str | None:
    """Find the raw source file for ``source_id`` and return its body
    (frontmatter stripped). Returns None if not found / unparseable."""
    sid = _strip_sources_prefix(source_id)
    for st in paths.SOURCE_TYPES:
        candidate = kb_root / "raw" / st / f"{sid}.md"
        if candidate.exists():
            try:
                _, body = fm.parse(candidate.read_text())
                return body
            except fm.FrontmatterError:
                return None
    return None


def _verify_quote(quote: str, source_body: str) -> bool:
    return _normalize_whitespace(quote) in _normalize_whitespace(source_body)


def suggest_cites(page_path: str | Path, *,
                  client: AnthropicAPIClient | None = None) -> list[CiteSuggestion]:
    """Run cite-suggest on one draft. Returns a list of suggestions —
    callers (the Aggressive batch driver) decide which to auto-apply.

    `client` is injectable for testing. If omitted, instantiates a fresh
    ``AnthropicAPIClient`` reading ``ANTHROPIC_API_KEY_RESEARCH``.
    """
    kb_root = paths.knowledge_root()
    target = Path(page_path)
    if not target.is_absolute():
        target = (kb_root / target).resolve()

    text = target.read_text()
    front, _body = fm.parse(text)
    source_ids = list(front.get("sources") or []) + list(front.get("synthesizes") or [])

    source_bodies: dict[str, str] = {}
    for sid in source_ids:
        body = _read_source_body(kb_root, sid)
        if body is not None:
            # Key by the bare id (without "sources/" prefix) so the dict
            # matches whatever form the LLM emits in `source_id`.
            source_bodies[_strip_sources_prefix(sid)] = body

    user_prompt = _build_user_prompt(text, source_bodies)

    if client is None:
        client = AnthropicAPIClient()
    result = client.call_with_usage(
        user_prompt=user_prompt,
        system_prompt=_SYSTEM_PROMPT,
        model=model_for("cite_suggest"),
        max_tokens=2048,
    )

    return _parse_and_verify(result.text, source_bodies)


def _build_user_prompt(file_text: str, source_bodies: dict[str, str]) -> str:
    numbered = "\n".join(
        f"{i + 1:4}: {line}"
        for i, line in enumerate(file_text.splitlines())
    )
    sources_block = "\n\n".join(
        f"<source id={sid!r}>\n{body}\n</source>"
        for sid, body in source_bodies.items()
    )
    return (
        "DRAFT WIKI PAGE (line-numbered):\n\n"
        f"{numbered}\n\n"
        "SOURCES:\n\n"
        f"{sources_block}\n\n"
        "Emit the JSON object now."
    )


def _parse_and_verify(raw_text: str,
                      source_bodies: dict[str, str]) -> list[CiteSuggestion]:
    raw_text = raw_text.strip()
    if raw_text.startswith("```"):
        raw_text = re.sub(r"^```(?:json)?\s*", "", raw_text)
        raw_text = re.sub(r"\s*```\s*$", "", raw_text)

    try:
        payload = json.loads(raw_text)
    except json.JSONDecodeError as e:
        _log.warning(
            "cite_suggest: LLM response was not valid JSON (%s); first 200 chars: %r",
            e, raw_text[:200],
        )
        return []

    raw_suggestions = payload.get("suggestions") or []
    line_counts: dict[int, int] = {}
    for s in raw_suggestions:
        ln = int(s.get("line", 0))
        if ln <= 0:
            continue
        line_counts[ln] = line_counts.get(ln, 0) + 1

    out: list[CiteSuggestion] = []
    for s in raw_suggestions:
        try:
            line = int(s["line"])
            source_id = str(s["source_id"])
            quote = str(s["evidence_quote"])
        except (KeyError, TypeError, ValueError):
            continue

        # LLM may emit the id with or without the `sources/` prefix
        # depending on what it sees in the page text. Normalize for lookup
        # AND store the bare form on the CiteSuggestion (which is what
        # `wiki cite` and bidirectional backlinks expect).
        source_id = _strip_sources_prefix(source_id)

        unambiguous = line_counts.get(line, 0) == 1
        body = source_bodies.get(source_id, "")
        verified = bool(body) and _verify_quote(quote, body)

        skip_reason = ""
        if not unambiguous:
            skip_reason = "multi-candidate line"
        elif not verified:
            skip_reason = "evidence quote not found in source body"

        out.append(CiteSuggestion(
            line=line,
            source_id=source_id,
            evidence_quote=quote,
            unambiguous=unambiguous,
            evidence_verified=verified,
            skip_reason=skip_reason,
        ))

    return out
