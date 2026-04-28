"""Missing-pages check.

Per WIKI § 12.2: identify entities or concepts that appear in 3+ wiki pages
within a domain but lack a dedicated `wiki/concepts/<slug>.md` or
`wiki/entities/<slug>.md` page.

One LLM call per domain. The prompt summarizes the domain's existing
concept/entity inventory and a sampled view of the wiki page bodies, then
asks Claude to enumerate missing entities/concepts. The runner validates
the response and emits one `LintFinding` per suggested term.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Iterable

from gateway.filter.semantic import ClaudeCLIFilterClient, FilterClient
from gateway.lint import LintFinding, SEVERITY_INFO, SEVERITY_WARNING
from gateway.lint._walk import walk_wiki_pages


_PAGE_TYPES_FOR_PROMPT = ("concept", "entity", "synthesis", "moc")
_BODY_EXCERPT_CHARS = 1200
_MAX_PAGES_IN_PROMPT = 60


@dataclass(frozen=True)
class _DomainPage:
    page_type: str
    slug: str
    title: str
    body_excerpt: str


def _domains_for_page(front: dict) -> Iterable[str]:
    """Concepts/synthesis use `domains:` (list); MOCs use `domain:` (scalar)."""
    if isinstance(front.get("domains"), list):
        return [d for d in front["domains"] if isinstance(d, str)]
    if isinstance(front.get("domain"), str):
        return [front["domain"]]
    return ()


def _slug(front: dict, fallback: str) -> str:
    raw = front.get("slug") or front.get("source_id") or fallback
    return str(raw)


def _excerpt(body: str, limit: int = _BODY_EXCERPT_CHARS) -> str:
    body = body.strip()
    if len(body) <= limit:
        return body
    return body[:limit].rsplit(" ", 1)[0] + " …"


def _gather_by_domain() -> dict[str, list[_DomainPage]]:
    out: dict[str, list[_DomainPage]] = {}
    for page_type, path, front, body in walk_wiki_pages():
        if page_type not in _PAGE_TYPES_FOR_PROMPT:
            continue
        for d in _domains_for_page(front):
            slug = _slug(front, path.stem)
            title = str(front.get("canonical_name") or front.get("title") or slug)
            out.setdefault(d, []).append(
                _DomainPage(
                    page_type=page_type,
                    slug=slug,
                    title=title,
                    body_excerpt=_excerpt(body),
                )
            )
    return out


def _existing_named_pages(pages: list[_DomainPage]) -> set[str]:
    return {p.slug for p in pages if p.page_type in ("concept", "entity")}


def _build_prompt(domain: str, pages: list[_DomainPage]) -> str:
    existing = sorted(_existing_named_pages(pages))
    sampled = pages[:_MAX_PAGES_IN_PROMPT]

    lines: list[str] = [
        "You are auditing a personal knowledge wiki for missing entity / concept pages.",
        "",
        f"Domain: {domain}",
        "",
        "Existing dedicated pages (by slug):",
        "  " + (", ".join(existing) if existing else "(none)"),
        "",
        "Sampled wiki pages (page_type | slug | title — body excerpt):",
    ]
    for p in sampled:
        lines.append(f"- {p.page_type} | {p.slug} | {p.title}")
        lines.append(f"    {p.body_excerpt}")
    lines.extend([
        "",
        "Task: identify ENTITIES (people, organizations, drugs, papers, datasets) and",
        "      CONCEPTS (mechanisms, phenomena, techniques) that appear in 3 or more",
        "      sampled pages but do NOT have a dedicated page in the existing list above.",
        "",
        "Constraints:",
        "- Do not propose terms that are already in the existing list.",
        "- Do not propose generic terms (e.g., 'study', 'method', 'data').",
        "- The same entity may go by multiple names — collapse to one canonical name.",
        "- Suggested slug: lowercase, hyphenated, ASCII; <= 60 chars.",
        "",
        "Respond with a single JSON object — no prose, no markdown fences:",
        '{"missing": [{"name": "...", "kind": "entity|concept", "slug": "...",',
        '"occurrences_estimate": <int>, "rationale": "..."}, ...]}',
        "",
        "Return at most 12 suggestions. If nothing qualifies, return {\"missing\": []}.",
    ])
    return "\n".join(lines)


_JSON_OBJECT_RE = re.compile(r"\{.*\}", re.DOTALL)


def _parse_response(raw: str) -> list[dict]:
    """Tolerant parse: handles code fences and surrounding prose."""
    if not raw:
        return []
    match = _JSON_OBJECT_RE.search(raw)
    if not match:
        return []
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return []
    items = data.get("missing") if isinstance(data, dict) else None
    if not isinstance(items, list):
        return []
    return [it for it in items if isinstance(it, dict) and it.get("name")]


def _findings_for_domain(
    domain: str, suggestions: list[dict], existing_slugs: set[str]
) -> list[LintFinding]:
    out: list[LintFinding] = []
    seen: set[str] = set()
    for s in suggestions:
        name = str(s.get("name", "")).strip()
        slug = str(s.get("slug", "")).strip().lower()
        kind = str(s.get("kind", "")).strip().lower() or "concept"
        if not name or not slug:
            continue
        if slug in existing_slugs or slug in seen:
            continue
        seen.add(slug)
        rationale = str(s.get("rationale", "")).strip()[:240]
        occurrences = s.get("occurrences_estimate")
        suffix = f"): {rationale}" if rationale else ")"
        occ = f", ~{occurrences} occurrences" if isinstance(occurrences, int) else ""
        msg = f"missing {kind} page in '{domain}': '{name}' (suggested slug `{slug}`{occ}{suffix}"
        out.append(
            LintFinding(
                check="missing-pages",
                severity=SEVERITY_INFO,
                message=msg,
                metadata={
                    "domain": domain,
                    "kind": kind,
                    "name": name,
                    "slug": slug,
                    "occurrences_estimate": occurrences,
                    "rationale": rationale,
                },
            )
        )
    return out


def run(client: FilterClient | None = None) -> list[LintFinding]:
    """Run missing-pages on every domain present in the wiki.

    `client` is injectable for tests; defaults to the `claude -p` subprocess
    backend used by the semantic filter. The `FilterClient` Protocol is
    generic (`call(prompt: str) -> str`) — naming is historical.
    """
    by_domain = _gather_by_domain()
    if not by_domain:
        return []

    if client is None:
        client = ClaudeCLIFilterClient()

    out: list[LintFinding] = []
    for domain, pages in sorted(by_domain.items()):
        existing_slugs = _existing_named_pages(pages)
        prompt = _build_prompt(domain, pages)
        try:
            response = client.call(prompt)
        except Exception as e:
            out.append(
                LintFinding(
                    check="missing-pages",
                    severity=SEVERITY_WARNING,
                    message=f"missing-pages call failed for domain '{domain}': {e!r}",
                    metadata={"domain": domain},
                )
            )
            continue
        suggestions = _parse_response(response)
        out.extend(_findings_for_domain(domain, suggestions, existing_slugs))
    return out
