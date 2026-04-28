"""Contradictions check.

Per WIKI § 12.2: LLM-driven scan for contradictory claims across wiki
pages, scoped per domain. The check extracts claim sentences from
concept/synthesis/MOC bodies, batches them with their owning page slug,
and asks Claude to identify contradictory pairs.

Cost: one Claude call per domain (additional calls if a domain has more
claims than `_MAX_CLAIMS_PER_CALL`). The check is intentionally bounded —
no per-pair cross-product calls.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass

from gateway import citations
from gateway.filter.semantic import ClaudeCLIFilterClient, FilterClient
from gateway.lint import LintFinding, SEVERITY_INFO, SEVERITY_WARNING
from gateway.lint._walk import walk_wiki_pages


_PAGE_TYPES_FOR_PROMPT = ("concept", "entity", "synthesis", "moc")
_MIN_CLAIMS_PER_DOMAIN = 4
_MAX_CLAIMS_PER_CALL = 80
_MAX_CLAIM_CHARS = 280


@dataclass(frozen=True)
class _Claim:
    page_type: str
    page_slug: str
    text: str  # the claim sentence


def _domains_for_page(front: dict) -> list[str]:
    if isinstance(front.get("domains"), list):
        return [d for d in front["domains"] if isinstance(d, str)]
    if isinstance(front.get("domain"), str):
        return [front["domain"]]
    return []


def _slug(front: dict, fallback: str) -> str:
    return str(front.get("slug") or front.get("source_id") or fallback)


def _gather_claims_by_domain() -> dict[str, list[_Claim]]:
    out: dict[str, list[_Claim]] = {}
    for page_type, path, front, body in walk_wiki_pages():
        if page_type not in _PAGE_TYPES_FOR_PROMPT:
            continue
        slug = _slug(front, path.stem)
        for cs in citations.find_claim_sentences(body):
            text = cs.text.strip()
            if len(text) > _MAX_CLAIM_CHARS:
                text = text[: _MAX_CLAIM_CHARS - 1].rsplit(" ", 1)[0] + "…"
            for d in _domains_for_page(front):
                out.setdefault(d, []).append(
                    _Claim(page_type=page_type, page_slug=slug, text=text)
                )
    return out


def _build_prompt(domain: str, claims: list[_Claim]) -> str:
    lines: list[str] = [
        "You are auditing a personal knowledge wiki for contradictory claims.",
        "",
        f"Domain: {domain}",
        "",
        "Numbered claims (each from a single wiki page):",
    ]
    for i, c in enumerate(claims, start=1):
        lines.append(f"  {i}. [{c.page_type}/{c.page_slug}] {c.text}")
    lines.extend([
        "",
        "Task: identify pairs of claims that ASSERT CONTRADICTORY FACTS within this",
        "      domain. A pair must directly conflict on a specific empirical or",
        "      definitional point — not differ in scope, framing, or context.",
        "",
        "Constraints:",
        "- Do not flag pairs that just emphasize different aspects of the same finding.",
        "- Do not flag claims that are precisely qualified ('in mice', 'short-term').",
        "- Be conservative: prefer to return [] than to flag spurious pairs.",
        "",
        "Respond with a single JSON object — no prose, no markdown fences:",
        '{"contradictions": [{"a": <int>, "b": <int>, "rationale": "..."}, ...]}',
        "",
        "Each `a` and `b` must be a claim number from the list above. Return at most",
        "12 pairs. If nothing qualifies, return {\"contradictions\": []}.",
    ])
    return "\n".join(lines)


_JSON_OBJECT_RE = re.compile(r"\{.*\}", re.DOTALL)


def _parse_response(raw: str) -> list[dict]:
    if not raw:
        return []
    match = _JSON_OBJECT_RE.search(raw)
    if not match:
        return []
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return []
    items = data.get("contradictions") if isinstance(data, dict) else None
    if not isinstance(items, list):
        return []
    return [it for it in items if isinstance(it, dict)]


def _findings_for_pairs(
    domain: str, claims: list[_Claim], pairs: list[dict]
) -> list[LintFinding]:
    out: list[LintFinding] = []
    seen: set[tuple[int, int]] = set()
    for p in pairs:
        try:
            a = int(p.get("a"))
            b = int(p.get("b"))
        except (TypeError, ValueError):
            continue
        if a == b:
            continue
        if not (1 <= a <= len(claims) and 1 <= b <= len(claims)):
            continue
        key = (min(a, b), max(a, b))
        if key in seen:
            continue
        seen.add(key)
        ca, cb = claims[a - 1], claims[b - 1]
        rationale = str(p.get("rationale", "")).strip()[:240]
        msg = (
            f"contradiction in '{domain}': "
            f"`{ca.page_type}/{ca.page_slug}` vs `{cb.page_type}/{cb.page_slug}`"
            + (f" — {rationale}" if rationale else "")
        )
        out.append(
            LintFinding(
                check="contradictions",
                severity=SEVERITY_WARNING,
                message=msg,
                metadata={
                    "domain": domain,
                    "a_page": f"{ca.page_type}/{ca.page_slug}",
                    "b_page": f"{cb.page_type}/{cb.page_slug}",
                    "a_text": ca.text,
                    "b_text": cb.text,
                    "rationale": rationale,
                },
            )
        )
    return out


def _chunked(claims: list[_Claim], size: int) -> list[list[_Claim]]:
    if not claims:
        return []
    return [claims[i : i + size] for i in range(0, len(claims), size)]


def run(client: FilterClient | None = None) -> list[LintFinding]:
    """Run contradictions across every domain in the wiki."""
    by_domain = _gather_claims_by_domain()
    if not by_domain:
        return []

    if client is None:
        client = ClaudeCLIFilterClient()

    out: list[LintFinding] = []
    for domain, claims in sorted(by_domain.items()):
        if len(claims) < _MIN_CLAIMS_PER_DOMAIN:
            continue

        for chunk in _chunked(claims, _MAX_CLAIMS_PER_CALL):
            prompt = _build_prompt(domain, chunk)
            try:
                response = client.call(prompt)
            except Exception as e:
                out.append(
                    LintFinding(
                        check="contradictions",
                        severity=SEVERITY_WARNING,
                        message=f"contradictions call failed for '{domain}': {e!r}",
                        metadata={"domain": domain},
                    )
                )
                continue
            pairs = _parse_response(response)
            out.extend(_findings_for_pairs(domain, chunk, pairs))

    return out
