"""`wiki retrieve` — composite RAG primitive (WS2, 2026-06-09 RAG review).

One call that does what an agent previously had to orchestrate by hand
(search → resolve → read → repeat): BM25 section retrieval over the FTS5
index, then assembly of a single bounded context block of the most relevant
sections. Deterministic and LLM-free — no API cost, no NotebookLM quota.

The block is the unit a downstream model consumes:

    <page path="wiki/concepts/order-block.md" section="Mechanism"
          title="Order Block" domain="trading-and-markets" score="3">
    ...section text, with [[sources/<id>]] citations preserved...
    </page>

`[[sources/<id>]]` links survive verbatim so any synthesis built on the
block inherits provenance. Each section is capped (`max_section_chars`) and
the whole block is capped (`budget_chars`) so a few large sections can't
blow the context window — an operational lesson from M1 (the index will
happily return large sections).
"""

from __future__ import annotations

import json
import math
import os
import re
from dataclasses import dataclass
from pathlib import Path

from gateway import log, paths, search_index
from gateway.core import OperationResult
from gateway.retrieval_index import dense_section_hits

# --- Hole 1: draft section content-gate --------------------------------------
#
# `retrieve` admits draft pages into the candidate pool (demote-not-exclude, see
# `include_drafts` below) so the ~1,100 legacy-migrated curated concept/entity/
# synthesis pages are reachable. The dominant legacy draft is HYBRID: a real
# lede/Methods plus placeholder sections whose entire body is a lone markdown-
# italic parenthetical — `_(needs population from legacy import)_` and ~1,090
# siblings (`_(summary not yet generated …)_`, `_(claims not yet extracted)_`,
# `_(no cross-references yet)_`, `_(no citations returned)_`). These carry zero
# grounding value, so they are gated out at the SECTION level (the substantive
# sections of the same page still surface). The predicate is structural — a
# section body that, stripped, is solely a single italic parenthetical — so it
# covers the whole marker family without enumerating each string, and cannot
# match a real section that merely contains a parenthetical aside.
#
# Forward pointer: the principled long-term form is an index-time grounding-
# worthiness flag reusable by `wiki search` too — see
# docs/backlog/rag-index-time-grounding-worthiness.md.
_PLACEHOLDER_SECTION_RE = re.compile(r"^_\([^)]*\)_$")


def is_placeholder_section(text: str) -> bool:
    """True iff `text` is solely a lone italic-parenthetical placeholder stub.

    Section-body-scoped: matches an unpopulated legacy/M6 placeholder section
    (whose entire stripped body is `_(...)_`) and nothing else. Empty text is
    handled by the caller's empty-section skip, not here.
    """
    return bool(_PLACEHOLDER_SECTION_RE.fullmatch(text.strip()))

# --- A4 carry-forward suppression -------------------------------------------
#
# Before logging a corpus-miss, check whether the same caller already has an
# outstanding deposit (in submitted/claimed/authored state) whose topic overlaps
# the query.  If so, suppress the miss: log corpus_miss=0 + suppressed_a4=1.
#
# Topic-match rule: any non-trivial word (> 3 chars, lowercased) that appears
# in both the query and the deposit's payload["title"] is sufficient.  Simple
# and defensible — avoids over-engineering a semantic-similarity layer here.
# The match is intentionally loose; false negatives cost an extra A4 log entry,
# false positives merely suppress a log line.  We accept a loose match.
# Future hardening: add a domain-match as a second required signal (caller +
# title-word-overlap + same domain) to reduce over-suppression on common
# cross-domain vocabulary.
#
# Outstanding states per the intent-queue spec: submitted, claimed, authored.
# Terminal states (committed, rejected, dead_lettered, quarantined) are skipped.

_A4_OUTSTANDING_STATES = ("submitted", "claimed", "authored")
_A4_MIN_WORD_LEN = 3


def _a4_suppressed(caller: str | None, query: str) -> bool:
    """Return True if the caller has an outstanding deposit whose title overlaps query."""
    if not caller:
        return False
    intents_dir = paths.intents_dir()
    query_words = {w for w in query.lower().split() if len(w) > _A4_MIN_WORD_LEN}
    if not query_words:
        return False
    for state in _A4_OUTSTANDING_STATES:
        state_dir = intents_dir / state
        if not state_dir.exists():
            continue
        for p in state_dir.glob("*.json"):
            if p.name.startswith("."):
                continue
            try:
                rec = json.loads(p.read_text())
            except (OSError, json.JSONDecodeError):
                continue
            # Caller match: identity["caller"] must equal caller
            identity = rec.get("identity", {})
            if identity.get("caller") != caller:
                continue
            # Topic match: overlap between query words and deposit title words
            title = str(rec.get("payload", {}).get("title", ""))
            title_words = {w for w in title.lower().split() if len(w) > _A4_MIN_WORD_LEN}
            if query_words & title_words:
                return True
    return False

_DEFAULT_BUDGET_CHARS = 40_000
_DEFAULT_MAX_SECTION_CHARS = 4_000
_DEFAULT_K = 12


def _record_demand_gap(query: str, caller: str | None) -> None:
    """Record a genuine corpus miss as a DemandLedger gap (decision 11 producer).

    Best-effort telemetry: a failure here must never break the read op, so any
    exception is swallowed (the miss is already logged to log.md regardless).
    """
    try:
        from gateway.demand_ledger import DemandLedger

        DemandLedger().record_gap(query, caller=caller)
    except Exception:
        pass


@dataclass
class RetrievedSection:
    rel_path: str
    slug: str
    title: str
    page_type: str
    domain: str
    heading: str
    text: str
    score: int
    rank: float


def _xml_attr(value: str) -> str:
    return (
        value.replace("&", "&amp;").replace('"', "&quot;")
        .replace("<", "&lt;").replace(">", "&gt;")
    )


def _merge_domains(
    query: str, domains: list[str], k: int, *, order: str, include_drafts: bool, scope: str,
) -> list:
    """Per-domain quota + round-robin interleave, de-duped by rel_path.

    Runs one search per named domain at quota ceil(k/N), then interleaves by
    per-domain rank so byte-budget truncation downstream preserves balance
    rather than collapsing toward the lexically-dominant domain.
    """
    n = len(domains)
    quota = math.ceil(k / n)
    per_domain = [
        search_index.search_fts(
            query, scope=scope, domain=d, limit=quota,
            order=order, include_drafts=include_drafts,
        )
        for d in domains
    ]
    merged: list = []
    seen: set[str] = set()
    for rank in range(quota):
        for hits in per_domain:
            if rank < len(hits) and hits[rank].rel_path not in seen:
                seen.add(hits[rank].rel_path)
                merged.append(hits[rank])
    return merged[:k]


# Dense-weighted RRF. The dense bi-encoder's top-10 is far stronger than BM25 on
# paraphrase queries (4B bake-off: dense-only R@10 0.905 vs equal-weight hybrid 0.667),
# so the dense list earns a higher fusion weight; BM25 stays at 1.0 to keep
# lexically-exact queries reachable. w=2.0 is the robust knee of the 4B sweep
# (probe R@10 0.667→0.857; easy goldens un-regressed); higher w approaches dense-only.
# Tunable via WIKI_RRF_DENSE_WEIGHT to re-sweep without a rebuild.
_DENSE_RRF_WEIGHT = 2.0


def _dense_rrf_weight() -> float:
    """Read at call time so the bake-off sweep can vary it within one process."""
    return float(os.environ.get("WIKI_RRF_DENSE_WEIGHT", _DENSE_RRF_WEIGHT))


def _rrf_fuse(ranked_lists: list[list[str]], k_rrf: int = 60,
              weights: list[float] | None = None) -> list[str]:
    """Weighted Reciprocal Rank Fusion. score(id) = Σ wₗ/(k_rrf + rank) over each list
    l the id appears in (rank is 0-based; wₗ defaults to 1.0). Returns ids by descending
    fused score; ties broken by first-seen order for determinism."""
    weights = weights if weights is not None else [1.0] * len(ranked_lists)
    scores: dict[str, float] = {}
    first_seen: dict[str, int] = {}
    seq = 0
    for w, lst in zip(weights, ranked_lists):
        for rank, ident in enumerate(lst):
            scores[ident] = scores.get(ident, 0.0) + w / (k_rrf + rank)
            if ident not in first_seen:
                first_seen[ident] = seq; seq += 1
    return sorted(scores, key=lambda i: (-scores[i], first_seen[i]))


def _hybrid_hits(query: str, *, domain: str | None, k: int, scope: str,
                 include_drafts: bool) -> list:
    """Fuse BM25 (authority order) with dense section NN via dense-weighted RRF;
    best-per-page, ≤k. `include_drafts` is honored on the lexical leg (carried from
    the caller, not hard-coded) so the hybrid path obeys the same draft gate as the
    FTS-only path; dense hits are content-gated downstream in `retrieve`."""
    lexical = search_index.search_fts(
        query, scope=scope, domain=domain, limit=k * 2,
        order="authority", include_drafts=include_drafts,
    )
    lex_ids = [f"{h.rel_path}#{h.heading}" for h in lexical]
    dense = dense_section_hits(query, k=k * 2)  # (rel, heading, dist)
    dense_ids = [f"{rel}#{heading}" for rel, heading, _d in dense]
    dense_meta = search_index.hits_for_sections([(r, h) for r, h, _ in dense])

    by_id = {f"{h.rel_path}#{h.heading}": h for h in lexical}
    for (rel, heading), hit in dense_meta.items():
        by_id.setdefault(f"{rel}#{heading}", hit)

    fused_ids = _rrf_fuse([lex_ids, dense_ids], weights=[1.0, _dense_rrf_weight()])
    out, seen_pages = [], set()
    for ident in fused_ids:
        hit = by_id.get(ident)
        if hit is None or hit.rel_path in seen_pages:   # best-section-per-page
            continue
        seen_pages.add(hit.rel_path)
        out.append(hit)
        if len(out) >= k:
            break
    return out


def retrieve(
    query: str,
    *,
    domain: str | None = None,
    domains: list[str] | None = None,
    k: int = _DEFAULT_K,
    budget_chars: int = _DEFAULT_BUDGET_CHARS,
    max_section_chars: int = _DEFAULT_MAX_SECTION_CHARS,
    scope: str = "wiki",
    include_drafts: bool = True,
    hybrid: bool = True,
) -> tuple[str, list[RetrievedSection]]:
    """Assemble a bounded context block for `query`. Returns (block, sections).

    Pure retrieval — no logging, no LLM. `retrieve_op` wraps this for the
    CLI/MCP surface (logging + OperationResult). When `domains` names ≥2
    domains, the block is balanced by a per-domain quota merge (ceil(k/N) each,
    round-robin-interleaved) instead of a single global k-window that collapses
    toward the lexically-dominant domain. `domains` takes precedence over the
    single `domain`.

    Drafts are admitted by default (`include_drafts=True`, Hole 1): the legacy
    migration committed the curated layer as `draft: true`, so excluding drafts
    hid ~1,100 pages from the default grounding path. Drafts compete in the pool
    demoted by `_DRAFT_PENALTY`; placeholder-stub sections are content-gated out
    (`is_placeholder_section`); surfaced drafts are tagged `draft="true"`.

    `hybrid=True` is the default single-domain path (Hole 2): BM25 is fused with
    dense section NN via dense-weighted RRF (`_DENSE_RRF_WEIGHT`) so paraphrase
    queries reach pages BM25 alone misses. With no built/loaded dense index the
    dense leg returns nothing and the path degrades to lexical-only. The neural
    encoder is ENV-selected (`WIKI_RETRIEVAL_ENCODER`); CI/tests use the stub.
    """
    if not query or not query.strip():
        return "", []

    multi = [d for d in (domains or []) if d and d.strip()]
    if len(multi) >= 2:
        hits = _merge_domains(
            query.strip(), multi, k,
            order="authority", include_drafts=include_drafts, scope=scope,
        )
    else:
        single = multi[0] if multi else domain
        if hybrid:
            hits = _hybrid_hits(query.strip(), domain=single, k=k, scope=scope,
                                include_drafts=include_drafts)
        else:
            hits = search_index.search_fts(
                query.strip(),
                scope=scope,
                domain=single,
                limit=k,
                order="authority",  # WS5: lift canonical pages over mere mentions
                include_drafts=include_drafts,
            )

    sections: list[RetrievedSection] = []
    blocks: list[str] = []
    total = 0
    for h in hits:
        text = search_index.section_text(h.rel_path, h.heading)
        if not text:
            continue
        # Hole 1 content-gate: drop unpopulated placeholder-stub sections so an
        # admitted draft never floats `_(needs population…)_` into the block.
        if is_placeholder_section(text):
            continue
        if len(text) > max_section_chars:
            text = text[:max_section_chars].rstrip() + "\n…[section truncated]"
        attrs = (
            f'path="{_xml_attr(h.rel_path)}" '
            f'section="{_xml_attr(h.heading or "(intro)")}" '
            f'title="{_xml_attr(h.title)}"'
        )
        if h.domain:
            attrs += f' domain="{_xml_attr(h.domain)}"'
        attrs += f' score="{h.score}"'
        # Q2: mark unfinalized provenance so a consumer (incl. `wiki answer`'s
        # LLM) knows this page's citation grounding is a downgraded lint warning.
        if h.draft:
            attrs += ' draft="true"'
        block = f"<page {attrs}>\n{text}\n</page>"
        if total + len(block) > budget_chars and blocks:
            break
        blocks.append(block)
        total += len(block)
        sections.append(
            RetrievedSection(
                rel_path=h.rel_path, slug=h.slug, title=h.title,
                page_type=h.page_type, domain=h.domain, heading=h.heading,
                text=text, score=h.score, rank=h.rank,
            )
        )

    return "\n\n".join(blocks), sections


def related_op(query: str, *, limit: int = 10, caller: str | None = None) -> OperationResult:
    """Find pages co-citing the same sources as a target page (WS5).

    `query` resolves to a page the same way `wiki context` does (path, slug,
    or title substring). Returns a ranked co-citation list — useful for an
    agent to expand from a known page to its conceptual neighbors without an
    LLM call.
    """
    from gateway.ops.context_op import _resolve_target, NoMatchError, AmbiguousQueryError

    try:
        target = _resolve_target(query)
    except (NoMatchError, AmbiguousQueryError) as e:
        return OperationResult(success=False, errors=[str(e)])

    rel = str(target.relative_to(paths.knowledge_root()))
    related = search_index.related_pages(rel, limit=limit)
    if not related:
        return OperationResult(
            success=True,
            summary=f"no co-citation neighbors for {rel}",
            data={"target": rel, "related": []},
        )

    lines = [f"Related to {rel} (by shared citations):"]
    for r in related:
        lines.append(
            f"  [{r.shared} shared, {r.inbound_count} inbound] "
            f"{r.rel_path} — {r.title}"
        )
    return OperationResult(
        success=True,
        summary="\n".join(lines),
        data={
            "target": rel,
            "related": [
                {"path": r.rel_path, "slug": r.slug, "title": r.title,
                 "type": r.page_type, "shared": r.shared, "inbound": r.inbound_count}
                for r in related
            ],
        },
    )


def retrieve_op(
    query: str,
    *,
    domain: str | None = None,
    domains: list[str] | None = None,
    k: int = _DEFAULT_K,
    budget_chars: int = _DEFAULT_BUDGET_CHARS,
    caller: str | None = None,
) -> OperationResult:
    """CLI/MCP entry point: retrieve + log."""
    if not query or not query.strip():
        return OperationResult(success=False, errors=["query is required"])

    domain_label = ",".join(domains) if domains else (domain or "")
    block, sections = retrieve(
        query, domain=domain, domains=domains, k=k, budget_chars=budget_chars
    )
    if not sections:
        # Corpus-miss telemetry (decision 10).  A4 suppression: if the same caller
        # has an outstanding deposit whose topic overlaps this query, do not count
        # this as a gap — the agent already has work in flight covering the topic.
        suppressed = _a4_suppressed(caller, query)
        miss_fields: dict = {
            "caller": caller or "",
            "query": query,
            "domain": domain_label,
            "corpus_miss": 0 if suppressed else 1,
        }
        if suppressed:
            miss_fields["suppressed_a4"] = 1
        log.append(
            op="retrieve",
            fields=miss_fields,
            summary=(
                f"retrieve: {query!r} domain={domain_label or '-'} "
                f"corpus_miss={'suppressed' if suppressed else '1'}"
            ),
        )
        # Demand-loop producer (decision 11): a genuine, non-suppressed corpus miss
        # is an open demand signal — record the raw query as a gap in the DemandLedger.
        # Recording to gitignored .knowledge/demand/ is read-tier-consistent (same
        # class as the log.md append above — telemetry, not corpus mutation).
        if not suppressed:
            _record_demand_gap(query, caller)
        return OperationResult(
            success=False,
            paths_touched=[paths.log_path()],
            summary=f"no results for {query!r}"
            + (f" in domain {domain_label!r}" if domain_label else ""),
        )

    log.append(
        op="retrieve",
        fields={
            "caller": caller or "",
            "query": query,
            "domain": domain_label,
            "sections": len(sections),
            "chars": len(block),
            "corpus_miss": 0,
        },
        summary=(
            f"retrieve: {query!r} domain={domain_label or '-'} "
            f"sections={len(sections)} chars={len(block)}"
        ),
    )
    return OperationResult(
        success=True,
        paths_touched=[paths.log_path()],
        summary=block,
        data={
            "query": query,
            "domain": domain_label or None,
            "section_count": len(sections),
            "chars": len(block),
            "sources": [
                {"path": s.rel_path, "slug": s.slug, "title": s.title,
                 "section": s.heading, "score": s.score}
                for s in sections
            ],
        },
    )
