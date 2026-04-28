"""Stale-claims check.

Per WIKI § 12.2: claims whose cited source has been superseded by a newer
same-domain source on the same topic.

Two modes:

1. **Deterministic** (default for `wiki lint`): gather (claim, cited_source,
   candidate_newer_sources) tuples; emit one info finding per domain with
   the count of claims that have at least one same-domain academic source
   published >= `_YEAR_GAP` years later. No LLM calls — cheap signal of
   how much follow-up authoring may be needed.

2. **LLM analysis** (opt-in via `sample_size > 0`): sample candidate claims
   and ask Claude per claim whether any candidate genuinely supersedes the
   cited source for that specific claim. Emits a warning per confirmed
   supersede.

Why hybrid: a full LLM pass is too expensive for the default lint cadence
(O(claims) calls). The deterministic count surfaces the workload; an
explicit `wiki lint --scope stale-claims` invocation can be wired to a
larger sample later.
"""

from __future__ import annotations

import json
import random
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

from gateway import citations, frontmatter as fm, paths
from gateway.filter.semantic import ClaudeCLIFilterClient, FilterClient
from gateway.lint import LintFinding, SEVERITY_INFO, SEVERITY_WARNING
from gateway.lint._walk import walk_raw_sources, walk_wiki_pages


_PAGE_TYPES_FOR_PROMPT = ("concept", "entity", "synthesis", "moc")
_ACADEMIC_TYPES = ("arxiv", "pubmed")
_YEAR_GAP = 3
_MAX_CANDIDATES = 3
_MAX_CLAIM_CHARS = 280
_RANDOM_SEED = 24680


@dataclass(frozen=True)
class _SourceMeta:
    canonical_id: str
    source_type: str
    year: int
    title: str
    body_excerpt: str
    domains: tuple[str, ...]


@dataclass(frozen=True)
class _ClaimRef:
    domain: str
    page_type: str
    page_slug: str
    text: str
    cited_id: str  # canonical source id, no `sources/` prefix


@dataclass(frozen=True)
class _StaleCandidate:
    claim: _ClaimRef
    cited: _SourceMeta
    candidates: tuple[_SourceMeta, ...]


_YEAR_RE = re.compile(r"\b(\d{4})\b")


def _year_of(value: object) -> int | None:
    if value is None:
        return None
    match = _YEAR_RE.search(str(value))
    if not match:
        return None
    yr = int(match.group(1))
    return yr if 1900 <= yr <= 2100 else None


def _sources_index() -> dict[str, _SourceMeta]:
    out: dict[str, _SourceMeta] = {}
    for source_type, path, front, body in walk_raw_sources():
        if source_type not in _ACADEMIC_TYPES:
            continue
        cid = str(front.get("id") or path.stem)
        year = _year_of(front.get("published_at"))
        if year is None:
            continue
        domains = tuple(d for d in (front.get("domains") or []) if isinstance(d, str))
        title = str(front.get("title") or cid)
        excerpt = body.strip()[:600]
        out[cid] = _SourceMeta(
            canonical_id=cid,
            source_type=source_type,
            year=year,
            title=title,
            body_excerpt=excerpt,
            domains=domains,
        )
    return out


def _domains_for_page(front: dict) -> list[str]:
    if isinstance(front.get("domains"), list):
        return [d for d in front["domains"] if isinstance(d, str)]
    if isinstance(front.get("domain"), str):
        return [front["domain"]]
    return []


def _slug(front: dict, fallback: str) -> str:
    return str(front.get("slug") or front.get("source_id") or fallback)


def _gather_claim_refs() -> list[_ClaimRef]:
    """Walk wiki pages, return claims that cite an academic-type canonical
    source. Deduped by (domain, page_slug, claim_text, cited_id) so that a
    page repeating the same claim across sections (e.g., Summary + Key
    claims) is treated once."""
    seen: set[tuple[str, str, str, str]] = set()
    out: list[_ClaimRef] = []
    for page_type, path, front, body in walk_wiki_pages():
        if page_type not in _PAGE_TYPES_FOR_PROMPT:
            continue
        page_slug = _slug(front, path.stem)
        page_domains = _domains_for_page(front)
        body_lines = body.split("\n")

        for cs in citations.find_claim_sentences(body):
            if not cs.has_citation:
                continue
            line = body_lines[cs.line_no - 1] if cs.line_no - 1 < len(body_lines) else ""
            for c in citations.find_source_citations(line):
                cited = c.target.removeprefix("sources/")
                if not (cited.startswith("arxiv-") or cited.startswith("pubmed-")):
                    continue
                text = cs.text.strip()
                if len(text) > _MAX_CLAIM_CHARS:
                    text = text[: _MAX_CLAIM_CHARS - 1].rsplit(" ", 1)[0] + "…"
                for d in page_domains:
                    key = (d, page_slug, text, cited)
                    if key in seen:
                        continue
                    seen.add(key)
                    out.append(
                        _ClaimRef(
                            domain=d,
                            page_type=page_type,
                            page_slug=page_slug,
                            text=text,
                            cited_id=cited,
                        )
                    )
    return out


def _candidates_for(
    claim: _ClaimRef, sources: dict[str, _SourceMeta]
) -> tuple[_SourceMeta, tuple[_SourceMeta, ...]] | None:
    cited = sources.get(claim.cited_id)
    if cited is None:
        return None
    if claim.domain not in cited.domains:
        return None

    candidates = [
        s for s in sources.values()
        if s.canonical_id != cited.canonical_id
        and s.source_type == cited.source_type
        and claim.domain in s.domains
        and s.year >= cited.year + _YEAR_GAP
    ]
    candidates.sort(key=lambda s: -s.year)
    return cited, tuple(candidates[:_MAX_CANDIDATES])


def _gather_stale_candidates() -> dict[str, list[_StaleCandidate]]:
    sources = _sources_index()
    if not sources:
        return {}

    by_domain: dict[str, list[_StaleCandidate]] = {}
    for claim in _gather_claim_refs():
        result = _candidates_for(claim, sources)
        if result is None:
            continue
        cited, candidates = result
        if not candidates:
            continue
        by_domain.setdefault(claim.domain, []).append(
            _StaleCandidate(claim=claim, cited=cited, candidates=candidates)
        )
    return by_domain


def _build_prompt(stale: _StaleCandidate) -> str:
    cited = stale.cited
    lines: list[str] = [
        "You are auditing a wiki claim against potentially-superseding sources.",
        "",
        f"Domain: {stale.claim.domain}",
        f"Wiki page: {stale.claim.page_type}/{stale.claim.page_slug}",
        "",
        "Claim:",
        f"  \"{stale.claim.text}\"",
        "",
        f"Cited source ({cited.canonical_id}, {cited.year}):",
        f"  title: {cited.title}",
        f"  excerpt: {cited.body_excerpt}",
        "",
        "Candidate newer sources (same domain, same source type):",
    ]
    for cand in stale.candidates:
        lines.extend([
            f"- id: {cand.canonical_id} ({cand.year})",
            f"  title: {cand.title}",
            f"  excerpt: {cand.body_excerpt[:300]}",
        ])
    lines.extend([
        "",
        "Task: does any candidate genuinely supersede the cited source for THIS",
        "      specific claim? Supersede means: the candidate covers the same",
        "      research question with a stronger, larger, or more recent design",
        "      that updates the conclusion the claim is making.",
        "",
        "Constraints:",
        "- A candidate that merely cites or references the cited source is NOT",
        "  superseding.",
        "- Tangentially-related newer work is NOT superseding.",
        "- Be conservative; prefer to return null than flag spuriously.",
        "",
        "Respond with a single JSON object — no prose, no markdown fences:",
        '{"superseded_by": "<candidate_id>" | null, "rationale": "..."}',
    ])
    return "\n".join(lines)


_JSON_OBJECT_RE = re.compile(r"\{.*\}", re.DOTALL)


def _parse_response(raw: str) -> tuple[str | None, str]:
    if not raw:
        return None, ""
    match = _JSON_OBJECT_RE.search(raw)
    if not match:
        return None, ""
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None, ""
    if not isinstance(data, dict):
        return None, ""
    sb = data.get("superseded_by")
    rationale = str(data.get("rationale", "")).strip()[:240]
    return (str(sb) if isinstance(sb, str) and sb else None), rationale


def _info_finding_for_domain(domain: str, count: int) -> LintFinding:
    return LintFinding(
        check="stale-claims",
        severity=SEVERITY_INFO,
        message=(
            f"stale-claims: '{domain}' has {count} claim(s) citing an academic "
            f"source with a same-domain candidate published ≥ {_YEAR_GAP} years later "
            f"(invoke programmatically with `sample_size>0` to LLM-verify)"
        ),
        metadata={"domain": domain, "candidate_count": count},
    )


def run(
    *,
    client: FilterClient | None = None,
    sample_size: int = 0,
) -> list[LintFinding]:
    """Default (sample_size=0) is deterministic-only: counts of claims with
    candidate supersedes per domain. Pass `sample_size > 0` to enable
    Claude-driven verification on a sample.
    """
    by_domain = _gather_stale_candidates()
    if not by_domain:
        return []

    out: list[LintFinding] = []

    if sample_size <= 0:
        for domain, items in sorted(by_domain.items()):
            out.append(_info_finding_for_domain(domain, len(items)))
        return out

    if client is None:
        client = ClaudeCLIFilterClient()

    for domain, items in sorted(by_domain.items()):
        out.append(_info_finding_for_domain(domain, len(items)))
        rng = random.Random(_RANDOM_SEED + hash(domain) % 100_000)
        sampled = items if sample_size >= len(items) else rng.sample(items, sample_size)
        for stale in sampled:
            try:
                response = client.call(_build_prompt(stale))
            except Exception as e:
                out.append(
                    LintFinding(
                        check="stale-claims",
                        severity=SEVERITY_WARNING,
                        message=(
                            f"stale-claims call failed for "
                            f"{stale.claim.page_type}/{stale.claim.page_slug} "
                            f"-> {stale.cited.canonical_id}: {e!r}"
                        ),
                        metadata={"domain": domain},
                    )
                )
                continue
            superseded_by, rationale = _parse_response(response)
            if not superseded_by:
                continue
            valid_ids = {c.canonical_id for c in stale.candidates}
            if superseded_by not in valid_ids:
                continue
            out.append(
                LintFinding(
                    check="stale-claims",
                    severity=SEVERITY_WARNING,
                    message=(
                        f"stale claim in '{domain}' "
                        f"`{stale.claim.page_type}/{stale.claim.page_slug}`: "
                        f"cited `{stale.cited.canonical_id}` ({stale.cited.year}) "
                        f"may be superseded by `{superseded_by}`"
                        + (f" — {rationale}" if rationale else "")
                    ),
                    metadata={
                        "domain": domain,
                        "page": f"{stale.claim.page_type}/{stale.claim.page_slug}",
                        "claim_text": stale.claim.text,
                        "cited_id": stale.cited.canonical_id,
                        "superseded_by": superseded_by,
                        "rationale": rationale,
                    },
                )
            )
    return out
