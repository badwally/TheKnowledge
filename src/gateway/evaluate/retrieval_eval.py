"""Retrieval eval harness (WS4, 2026-06-09 RAG review).

Scores the retrieval layer against a golden query set: recall@k and MRR.
This is the measurement that disciplines every later retrieval workstream
(WS2/WS3/WS5) and is the *only* legitimate trigger for adding vector search
(WS7) — if recall stays high on paraphrase queries, BM25 is sufficient.

Two retrievers are compared:
  - "fts"  — the live `search_index` BM25 backend (current default).
  - "grep" — a substring-scan baseline reproducing the pre-WS1 behavior,
             kept ONLY for the WS1 before/after measurement.

The harness reads goldens from `.knowledge/eval/retrieval/goldens.yaml`
(or an explicit path) and never mutates the index.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from gateway import frontmatter as fm, paths, search_index


@dataclass
class GoldenQuery:
    q: str
    expect: list[str]
    domain: str | None = None


@dataclass
class QueryResult:
    query: str
    expected: list[str]
    ranked_slugs: list[str]
    best_rank: int | None  # 1-based rank of first expected slug, or None

    def hit_at(self, k: int) -> bool:
        return self.best_rank is not None and self.best_rank <= k

    @property
    def reciprocal_rank(self) -> float:
        return 1.0 / self.best_rank if self.best_rank else 0.0


@dataclass
class EvalReport:
    retriever: str
    results: list[QueryResult] = field(default_factory=list)

    @property
    def n(self) -> int:
        return len(self.results)

    def recall_at(self, k: int) -> float:
        if not self.results:
            return 0.0
        return sum(r.hit_at(k) for r in self.results) / len(self.results)

    @property
    def mrr(self) -> float:
        if not self.results:
            return 0.0
        return sum(r.reciprocal_rank for r in self.results) / len(self.results)

    def misses_at(self, k: int) -> list[QueryResult]:
        return [r for r in self.results if not r.hit_at(k)]


def load_goldens(path: Path | None = None) -> list[GoldenQuery]:
    p = path or (paths.knowledge_internal() / "eval" / "retrieval" / "goldens.yaml")
    data = yaml.safe_load(p.read_text()) or {}
    out: list[GoldenQuery] = []
    for entry in data.get("queries", []):
        expect = entry["expect"]
        if isinstance(expect, str):
            expect = [expect]
        out.append(GoldenQuery(q=entry["q"], expect=expect, domain=entry.get("domain")))
    return out


def _fts_ranked_slugs(g: GoldenQuery, limit: int) -> list[str]:
    # Measure the ranking the `retrieve` primitive actually serves (WS5).
    hits = search_index.search_fts(
        g.q, scope="wiki", domain=g.domain, limit=limit, order="authority"
    )
    return [h.slug for h in hits]


_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")


def _grep_ranked_slugs(g: GoldenQuery, limit: int) -> list[str]:
    """Pre-WS1 baseline: substring scan, tier 3/2/1 by title/slug/body.

    Reproduces the old ops.search behavior for an apples-to-apples WS1
    before/after. Scans the live wiki tree; slow but only run in eval.
    """
    pattern = re.compile(re.escape(g.q.strip()), re.IGNORECASE)
    scored: list[tuple[int, str, str]] = []
    for path in paths.wiki_dir().rglob("*.md"):
        try:
            front, body = fm.parse(path.read_text(errors="replace"))
        except Exception:
            continue
        domains = front.get("domains") or []
        if not isinstance(domains, list):
            domains = [domains]
        if g.domain and g.domain not in domains and front.get("domain") != g.domain:
            continue
        title = str(front.get("title", ""))
        slug = path.stem
        score = 0
        if pattern.search(title):
            score = 3
        elif pattern.search(slug):
            score = 2
        elif pattern.search(body):
            score = 1
        if score:
            scored.append((score, title.lower(), slug))
    scored.sort(key=lambda t: (-t[0], t[1]))
    return [slug for _, _, slug in scored[:limit]]


def evaluate(
    retriever: str = "fts",
    *,
    goldens: list[GoldenQuery] | None = None,
    k: int = 10,
) -> EvalReport:
    """Run the golden set through `retriever` ("fts" or "grep")."""
    goldens = goldens if goldens is not None else load_goldens()
    rank_fn = _fts_ranked_slugs if retriever == "fts" else _grep_ranked_slugs

    report = EvalReport(retriever=retriever)
    for g in goldens:
        ranked = rank_fn(g, k)
        best: int | None = None
        for i, slug in enumerate(ranked, start=1):
            if slug in g.expect:
                best = i
                break
        report.results.append(
            QueryResult(query=g.q, expected=g.expect, ranked_slugs=ranked, best_rank=best)
        )
    return report


def format_report(report: EvalReport, *, show_misses: bool = True) -> str:
    lines = [
        f"Retriever: {report.retriever}  (n={report.n})",
        f"  recall@5  = {report.recall_at(5):.3f}",
        f"  recall@10 = {report.recall_at(10):.3f}",
        f"  MRR       = {report.mrr:.3f}",
    ]
    if show_misses:
        misses = report.misses_at(10)
        if misses:
            lines.append(f"  misses@10 ({len(misses)}):")
            for m in misses:
                lines.append(f"    - {m.query!r} → expected {m.expected}")
    return "\n".join(lines)
