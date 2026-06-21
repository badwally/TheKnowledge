"""E2E confabulation / grounding guards (E2E-2, E2E-9).

These drive the REAL producers at PRODUCTION-DEFAULT settings — not a
fabricated fixture standing in for the data the gate reads, and not the
thresholds monkeypatched to extremes. The cardinal rule (see
`docs/e2e-challenge-cases.md`): drive the real producer so a green test
cannot lie about whether the shipped configuration actually fires.

E2E-9 — NotebookLM synthesis refuses to confabulate on a sparse corpus.
  The unit coverage in `tests/gateway/test_research_orchestrator.py`
  fabricates `_MaterializedSource(word_count=...)` AND overrides
  `_CORPUS_MIN_MEDIAN`/`_CORPUS_SPARSE_FRAC` to extremes (10000 / 0.0), so
  it proves the gate's arithmetic but NOT that the SHIPPED defaults
  (300 words / 0.60 sparse) block a real-sparse corpus, nor that the real
  word-count producer (`_materialize`) feeds it. These tests close that gap
  and never touch live NLM (spend/quota): the sparse case asserts the run
  blocks before any notebook is created; the rich case is the negative
  control proving the gate is not a tautology that always blocks.

E2E-2 — citation-grounding gate is not bypassable. No path lets an uncited
  claim reach a finalized page: non-draft commit is rejected, `--draft`
  downgrades to a warning, and `wiki finalize` re-runs the strict validator
  and fails until the claim is cited.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

import io

from gateway import frontmatter as fm
from gateway import paths, search_index, validator
from gateway.evaluate import retrieval_eval as rev
from gateway.filter.semantic import FilterResult
from gateway.ops import ingest as ingest_op
from gateway.ops.finalize import finalize
from gateway.research import orchestrator as orch
from gateway.research.adapters import CandidateItem

pytestmark = pytest.mark.e2e


# --- shared temp KNOWLEDGE_ROOT --------------------------------------------


@pytest.fixture
def kb_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """A seeded temp KNOWLEDGE_ROOT — no production-wiki writes."""
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    for sub in (
        "raw",
        "wiki",
        "wiki/sources",
        "wiki/synthesis",
        "nlm",
        ".knowledge",
        ".knowledge/locks",
    ):
        (tmp_path / sub).mkdir(parents=True, exist_ok=True)
    for src_type in paths.SOURCE_TYPES:
        (tmp_path / "raw" / src_type).mkdir(parents=True, exist_ok=True)
    return tmp_path


# ===========================================================================
# E2E-9 — corpus-quality gate at production-default thresholds
# ===========================================================================


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _write_policy(kb_root: Path, slug: str, threshold: float = 0.5) -> None:
    pol_dir = kb_root / ".knowledge" / "policies" / slug
    pol_dir.mkdir(parents=True, exist_ok=True)
    (pol_dir / "policy.yaml").write_text(
        yaml.safe_dump(
            {
                "version": "v1",
                "domain": {"slug": slug, "topic": slug, "field": "test"},
                "filter": {
                    "threshold_include": threshold,
                    "threshold_review": threshold - 0.2,
                    "example_count_in_prompt": 0,
                    "example_strategy": "balanced",
                },
                "inclusion_criteria": ["always"],
                "exclusion_criteria": [],
                "quality_signals": {},
            }
        )
    )


@dataclass
class _StubAdapter:
    name: str
    items: list[CandidateItem] = field(default_factory=list)

    def search(self, query, *, filter_hints=None, max_results=50):
        return list(self.items)


@dataclass
class _BodyConverter:
    """Stub converter emitting a canonical source page whose body has a
    controllable word count — the seam through which we 'seed' the corpus.
    The word count consumed downstream is produced by the REAL
    `_materialize` (`len(body.split())`), not hand-set on the fixture."""

    words: int

    def detect(self, source: str) -> bool:
        return True

    def convert(self, source: str) -> str:
        body = " ".join(f"word{i}" for i in range(self.words)) + ".\n"
        ident = "".join(ch for ch in source.lower() if ch.isalnum())[-12:] or "abcdef123456"
        slug_id = "web-2026-04-29-" + ident
        front = {
            "id": slug_id,
            "type": "web",
            "title": f"Title for {source}",
            "url": source,
            "authors": ["Test"],
            "published_at": "2026-04-29",
            "ingested_at": _now(),
            "content_hash": validator.compute_content_hash(body),
            "domains": ["alpha"],
            "nlm_corpus_ids": [],
            "wiki_pages": [],
            "meta": {},
        }
        return fm.serialize(front, body)


@dataclass
class _MockNlm:
    """Records every notebook touch so we can assert NLM was never engaged."""

    next_persistent: str = "nb-persistent"
    next_session: str = "nb-session"
    creates: list[str] = field(default_factory=list)

    def notebook_create(self, title: str) -> str:
        self.creates.append(title)
        return self.next_session if "session" in title else self.next_persistent

    def source_add_url(self, notebook_id, url):  # pragma: no cover - guard
        raise AssertionError("NLM source_add must not be reached on a blocked corpus")

    def source_add_text(self, notebook_id, content, *, title=None):  # pragma: no cover
        raise AssertionError("NLM source_add must not be reached on a blocked corpus")

    def notebook_query(self, notebook_id, question):  # pragma: no cover
        return {"answer": "", "citations": {}, "sources_used": []}


def _candidate(url: str) -> CandidateItem:
    return CandidateItem(
        item_id=url.rsplit("/", 1)[-1] or "x",
        source_type="web",
        url=url,
        title="Some article",
        description="(short description)",
    )


def _patch_research_harness(
    monkeypatch: pytest.MonkeyPatch, *, adapter: _StubAdapter, converter
) -> None:
    monkeypatch.setattr(orch, "enabled_adapters", lambda *, include_local=None: [adapter])
    monkeypatch.setattr(orch, "_load_examples", lambda domain: [])
    monkeypatch.setattr(orch, "_select_examples", lambda examples, policy: [])
    monkeypatch.setattr(orch.converters, "dispatch", lambda url: converter)

    def _score(front, body, policy, examples=None, client=None, body_head_chars=16000, _prebuilt_system=None):
        return FilterResult(
            score=0.9,
            rationale="stub",
            policy_version=f"{policy.domain_slug}-v1",
            decided_at=_now(),
        )

    monkeypatch.setattr(orch, "filter_score", _score)


def test_e2e9_sparse_corpus_blocks_research_at_default_thresholds(
    monkeypatch: pytest.MonkeyPatch, kb_root: Path
):
    """A real-sparse corpus blocks the run at the SHIPPED defaults
    (`_CORPUS_MIN_MEDIAN`=300, `_CORPUS_SPARSE_FRAC`=0.60) and NLM is never
    created — the confabulation trap stays shut without a fixture override."""
    # Production defaults must be in force for this guard to mean anything.
    assert orch._CORPUS_MIN_MEDIAN == 300
    assert orch._CORPUS_SPARSE_FRAC == 0.60
    # Belt-and-suspenders: never sleep on the index-settle wait (the gate
    # fires earlier, but a default settle wait would block a misordered build).
    monkeypatch.setattr(orch, "_SETTLE_MAX_S", 0.0, raising=False)

    _write_policy(kb_root, "alpha")
    adapter = _StubAdapter(
        name="web",
        items=[_candidate(f"https://sparse.example/{n}") for n in range(3)],
    )
    # ~6-word bodies: real median << 300 and 100% sparse.
    _patch_research_harness(monkeypatch, adapter=adapter, converter=_BodyConverter(words=6))

    nlm = _MockNlm()
    result = orch.research("test prompt", domain="alpha", nlm_client=nlm)

    assert not result.success
    assert any("corpus quality" in e.lower() for e in result.errors)
    assert nlm.creates == []  # NLM never touched — no spend, no confabulation


def test_e2e9_rich_corpus_passes_quality_gate(
    monkeypatch: pytest.MonkeyPatch, kb_root: Path
):
    """Negative control: a genuinely rich corpus (real word counts well above
    the 300-word floor) PASSES the gate at default thresholds — proving the
    gate is not a tautology that always blocks. Drives the real word-count
    producer (`_materialize`) into the real gate; no NLM, no live synthesis."""
    assert orch._CORPUS_MIN_MEDIAN == 300
    monkeypatch.setattr(orch.converters, "dispatch", lambda url: _BodyConverter(words=450))

    accepted = [(_candidate(f"https://rich.example/{n}"), 0.9) for n in range(3)]
    materialized = orch._materialize(accepted, session_id="e2e9-rich")

    # Word counts are produced by `_materialize`, not set on the fixture.
    assert materialized, "materialize produced no sources"
    assert all(ms.word_count >= 300 for ms in materialized)
    assert orch._check_corpus_quality(materialized, "e2e9-rich") is True


# ===========================================================================
# E2E-2 — citation grounding gate is not bypassable
# ===========================================================================


_SYNTH_BODY_UNCITED = """\
# Do GLP-1 agonists differ in efficacy

## Synthesis

Semaglutide reduces appetite through GLP-1 receptor agonism in the hypothalamus. [[sources/web-test-aaa]]

Tirzepatide produces greater average weight loss than semaglutide in head-to-head trials.

## Sources cited

- [[sources/web-test-aaa]]
"""

_SYNTH_BODY_CITED = """\
# Do GLP-1 agonists differ in efficacy

## Synthesis

Semaglutide reduces appetite through GLP-1 receptor agonism in the hypothalamus. [[sources/web-test-aaa]]

Tirzepatide produces greater average weight loss than semaglutide in head-to-head trials. [[sources/web-test-bbb]]

## Sources cited

- [[sources/web-test-aaa]]
- [[sources/web-test-bbb]]
"""


def _synth_front(*, draft: bool) -> dict:
    front = {
        "type": "synthesis",
        "slug": "glp1-efficacy-differences",
        "title": "Do GLP-1 agonists differ in efficacy",
        "domains": ["alpha"],
        "question": "Do GLP-1 agonists differ in efficacy?",
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        "sources_count": 2,
    }
    if draft:
        front["draft"] = True
        front["draft_started_at"] = "2026-01-01T00:00:00Z"
    return front


def test_e2e2_non_draft_with_uncited_claim_is_rejected(kb_root: Path):
    """The strict (non-draft) validator REJECTS a synthesis page carrying an
    uncited claim sentence — the grounding error names the citation rule."""
    result = validator.validate_wiki_page(
        _synth_front(draft=False), _SYNTH_BODY_UNCITED, "synthesis", draft=False
    )
    assert not result.ok
    assert any(e.rule == "citation-grounding" for e in result.errors)
    # The cited claim is not what trips the gate.
    assert any("tirzepatide" in str(e).lower() for e in result.errors)


def test_e2e2_draft_downgrades_uncited_claim_to_warning(kb_root: Path):
    """`--draft` commits the same page: the uncited claim is a WARNING, not an
    error, so partial work is allowed through with `draft: true`."""
    result = validator.validate_wiki_page(
        _synth_front(draft=True), _SYNTH_BODY_UNCITED, "synthesis", draft=True
    )
    assert result.ok  # no errors — draft commits
    assert any(w.rule == "citation-grounding" for w in result.warnings)


def test_e2e2_finalize_fails_until_uncited_claim_is_cited(kb_root: Path):
    """`wiki finalize` re-runs the strict validator: it FAILS on the draft
    while a claim is uncited (page stays `draft: true`), and SUCCEEDS only
    after the claim gains a citation. No path finalizes an uncited claim."""
    page = kb_root / "wiki" / "synthesis" / "glp1-efficacy-differences.md"

    # Draft with an uncited claim → finalize must refuse.
    page.write_text(fm.serialize(_synth_front(draft=True), _SYNTH_BODY_UNCITED))
    blocked = finalize(page)
    assert not blocked.success
    assert any("citation grounding" in e.lower() for e in blocked.errors)
    front_after, _ = fm.parse(page.read_text())
    assert front_after.get("draft") is True  # still a draft — not finalized

    # Same page, claim now cited → finalize succeeds and clears the draft flag.
    page.write_text(fm.serialize(_synth_front(draft=True), _SYNTH_BODY_CITED))
    ok = finalize(page)
    assert ok.success
    front_final, _ = fm.parse(page.read_text())
    assert "draft" not in front_final
    assert "finalized_at" in front_final


# ===========================================================================
# E2E-1 — ingest → filter → convert → wiki page (the spine)
# ===========================================================================
#
# Drives the REAL pdf converter (pdfplumber, offline), the REAL ingest op,
# the REAL validator + source-immutability check, and REAL source-page
# authoring. The two-pass *filter* is the one external LLM dependency, so it
# is stubbed deterministically here (exactly as E2E-9 stubs NLM) — the filter
# decision logic that the stub feeds (threshold compare → wiki-page-or-not) is
# still the real ingest code. The filter's *judgment* (source-type blindness)
# has no faithful offline case; it is exercised by a one-time live hand-run
# against a real corpus, not the gate.
#
# The PDF is generated in-process (a ~800-byte text-bearing PDF, no external
# dependency, no committed binary fixture) so the converter has a real file to
# parse.


def _make_min_pdf(lines: list[str]) -> bytes:
    """Assemble a minimal one-page text-bearing PDF, computing xref offsets so
    pdfminer/pdfplumber can parse it. `lines=[]` yields a no-text PDF."""
    parts = ["BT", "/F1 12 Tf", "72 720 Td", "14 TL"]
    for i, ln in enumerate(lines):
        esc = ln.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
        if i:
            parts.append("T*")
        parts.append(f"({esc}) Tj")
    parts.append("ET")
    content = "\n".join(parts).encode()
    objs = [
        b"<</Type /Catalog /Pages 2 0 R>>",
        b"<</Type /Pages /Kids [3 0 R] /Count 1>>",
        b"<</Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Contents 4 0 R /Resources <</Font <</F1 5 0 R>>>>>>",
        b"<</Length %d>>\nstream\n" % len(content) + content + b"\nendstream",
        b"<</Type /Font /Subtype /Type1 /BaseFont /Helvetica>>",
    ]
    out = io.BytesIO()
    out.write(b"%PDF-1.4\n")
    offsets = []
    for i, o in enumerate(objs, 1):
        offsets.append(out.tell())
        out.write(b"%d 0 obj\n" % i + o + b"\nendobj\n")
    xref = out.tell()
    out.write(b"xref\n0 %d\n" % (len(objs) + 1))
    out.write(b"0000000000 65535 f \n")
    for off in offsets:
        out.write(b"%010d 00000 n \n" % off)
    out.write(
        b"trailer\n<</Size %d /Root 1 0 R>>\nstartxref\n%d\n%%%%EOF\n"
        % (len(objs) + 1, xref)
    )
    return out.getvalue()


_RICH_LINES = [
    f"Self-evolving agents revise their own harness during run number {n} of the study."
    for n in range(20)
]  # ~280 words — comfortably above the stub's 100-word include bar
_SPARSE_LINES = ["A two line stub.", "No technical substance here."]  # ~8 words


def _e2e1_kb(kb_root: Path) -> Path:
    """`kb_root` plus a registered domain `seagents` with a real policy file."""
    pol = kb_root / ".knowledge" / "policies" / "seagents"
    pol.mkdir(parents=True, exist_ok=True)
    (pol / "policy.yaml").write_text(
        yaml.safe_dump(
            {
                "version": "0.1.0",
                "domain": {
                    "slug": "seagents",
                    "topic": "Self-evolving LLM agents",
                    "field": "LLM agents",
                    "description": "Self-evolving / self-improving LLM agents.",
                },
                "filter": {
                    "threshold_include": 0.7,
                    "threshold_review": 0.5,
                    "example_count_in_prompt": 0,
                    "example_strategy": "balanced",
                },
                "inclusion_criteria": ["Studies self-evolving LLM agents"],
                "exclusion_criteria": ["Thin stubs with no substance"],
                "quality_signals": {},
            }
        )
    )
    return kb_root


def _patch_filter_by_length(monkeypatch: pytest.MonkeyPatch) -> None:
    """Stub the filter LLM: a rich body scores include, a thin body scores
    reject. Deterministic; the real ingest threshold logic consumes it."""

    def _score(front, body, policy, examples=None, client=None, **kw):
        wc = len(body.split())
        return FilterResult(
            score=0.95 if wc >= 100 else 0.10,
            rationale=f"stub by length (wc={wc})",
            policy_version=f"{policy.domain_slug}-v1",
            decided_at=_now(),
        )

    monkeypatch.setattr(ingest_op, "filter_score", _score)


def _only_pdf_raw(kb_root: Path) -> Path:
    pdfs = list((kb_root / "raw" / "pdf").glob("*.md"))
    assert len(pdfs) == 1, f"expected one raw pdf page, got {pdfs}"
    return pdfs[0]


def test_e2e1_rich_pdf_lands_with_source_page_and_immutable_body(
    monkeypatch: pytest.MonkeyPatch, kb_root: Path
):
    """A rich PDF ingests through the REAL converter: it lands in raw/pdf/, an
    accepted source page is authored with raw-provenance grounding, and the
    raw body is byte-identical to the converter output after the filter block
    is written to frontmatter (immutable body, mutable frontmatter)."""
    _e2e1_kb(kb_root)
    _patch_filter_by_length(monkeypatch)
    pdf = kb_root / "rich.pdf"
    pdf.write_bytes(_make_min_pdf(_RICH_LINES))

    # Body the converter produces, before ingest persists it.
    _, conv_body = fm.parse(ingest_op.converters.dispatch(str(pdf)).convert(str(pdf)))

    result = ingest_op.ingest(pdf, domain="seagents")
    assert result.success

    raw = _only_pdf_raw(kb_root)
    raw_front, raw_body = fm.parse(raw.read_text())
    # Immutability: frontmatter gained a filter block; the body is untouched.
    assert "filter" in raw_front
    assert raw_body == conv_body

    # Accepted → a source page was authored, grounded to its raw provenance.
    source_page = paths.wiki_source_path(raw_front["id"])
    assert source_page.exists()
    sp_text = source_page.read_text()
    assert f"[[raw/pdf/{raw_front['id']}]]" in sp_text

    # Re-ingest is a no-op and does not mutate the immutable body.
    again = ingest_op.ingest(pdf, domain="seagents")
    assert again.no_op
    _, raw_body_2 = fm.parse(raw.read_text())
    assert raw_body_2 == conv_body


def test_e2e1_sparse_pdf_is_filtered_out_no_source_page(
    monkeypatch: pytest.MonkeyPatch, kb_root: Path
):
    """A thin PDF lands in raw/ (the immutable record) but is filtered out —
    NO wiki/sources page is authored. The rich/sparse pair is the complementary
    control: a tautological 'always author' gate would fail this half."""
    _e2e1_kb(kb_root)
    _patch_filter_by_length(monkeypatch)
    pdf = kb_root / "sparse.pdf"
    pdf.write_bytes(_make_min_pdf(_SPARSE_LINES))

    result = ingest_op.ingest(pdf, domain="seagents")
    assert result.success  # ingest succeeds; the source is recorded

    raw = _only_pdf_raw(kb_root)
    raw_front, _ = fm.parse(raw.read_text())
    assert raw_front["filter"]["score"] < 0.7  # rejected band
    assert not paths.wiki_source_path(raw_front["id"]).exists()


def test_e2e1_unextractable_pdf_fails_not_silent_success(
    monkeypatch: pytest.MonkeyPatch, kb_root: Path
):
    """A PDF with no extractable text must surface a conversion FAILURE, not a
    silent success that writes an empty source — the convert-failure-as-success
    trap. No raw/pdf page is written."""
    _e2e1_kb(kb_root)
    _patch_filter_by_length(monkeypatch)
    pdf = kb_root / "empty.pdf"
    pdf.write_bytes(_make_min_pdf([]))  # valid PDF, zero text

    result = ingest_op.ingest(pdf, domain="seagents")
    assert not result.success
    assert any("conversion failed" in e.lower() for e in result.errors)
    assert list((kb_root / "raw" / "pdf").glob("*.md")) == []


# ===========================================================================
# E2E-4 — retrieval recall floor under content growth
# ===========================================================================
#
# The pre-merge gate already runs `eval-retrieval --compare` against the
# PRODUCTION golden/corpus, so re-asserting a recall number there would just
# duplicate it. These tests instead drive the catches the gate does NOT cover,
# on a seeded temp corpus with its own small golden set:
#   - the derived FTS index, healed incrementally on read, must match a cold
#     rebuild from canonical markdown (derived-state drift from canonical);
#   - a query self-heals the index on an mtime/size diff (no explicit rebuild);
#   - recall@10 stays above the floor and MRR does not regress when 20+ new
#     sources are added across domains (ranking regression hidden by additive
#     content).


def _concept_page(kb_root: Path, slug: str, title: str, body: str, domain: str = "d") -> None:
    d = kb_root / "wiki" / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": slug,
        "title": title,
        "domains": [domain],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-05-01T00:00:00Z",
    }
    (d / f"{slug}.md").write_text(fm.serialize(front, body))


_SIGNAL_PAGES = [
    ("fair-value-gap", "Fair Value Gap",
     "An imbalance gap in candlestick price left by aggressive institutional orders."),
    ("order-block", "Order Block",
     "An institutional order block marks where price action originated before a move."),
    ("liquidity-sweep", "Liquidity Sweep",
     "A liquidity sweep takes out resting stop orders beyond a swing high or low."),
    ("market-structure-shift", "Market Structure Shift",
     "A market structure shift signals a trend change after a confirmed break of structure."),
    ("premium-discount", "Premium and Discount",
     "Premium and discount zones split a dealing range around the equilibrium midpoint."),
]

_SIGNAL_GOLDENS = [
    rev.GoldenQuery(q="imbalance gap left by aggressive orders", expect=["fair-value-gap"], domain="d"),
    rev.GoldenQuery(q="institutional order block where price originated", expect=["order-block"], domain="d"),
    rev.GoldenQuery(q="sweep that takes out resting stop orders beyond a swing", expect=["liquidity-sweep"], domain="d"),
    rev.GoldenQuery(q="trend change after a confirmed break of structure", expect=["market-structure-shift"], domain="d"),
    rev.GoldenQuery(q="zones split a dealing range around the equilibrium midpoint", expect=["premium-discount"], domain="d"),
]


def _seed_signal(kb_root: Path) -> None:
    for slug, title, body in _SIGNAL_PAGES:
        _concept_page(kb_root, slug, title, body)


def _seed_noise(kb_root: Path, n: int, *, start: int = 0) -> None:
    """Unrelated filler pages across two domains — additive content growth."""
    for i in range(start, start + n):
        _concept_page(
            kb_root,
            f"noise-{i:03d}",
            f"Filler {i}",
            f"Unrelated note {i} about garden compost, mulch, rainfall, and soil pH.",
            domain="garden" if i % 2 else "weather",
        )


def test_e2e4_recall_floor_holds_under_additive_growth(kb_root: Path):
    """Recall@10 stays >= the 0.90 floor and MRR does not regress when 24 new
    off-topic sources are added across domains and the index is rebuilt."""
    _seed_signal(kb_root)
    search_index.refresh(rebuild=True)
    base = rev.evaluate("fts", goldens=_SIGNAL_GOLDENS, k=10)
    assert base.recall_at(10) >= 0.90

    _seed_noise(kb_root, 24)  # 20+ additive sources across domains
    search_index.refresh(rebuild=True)
    after = rev.evaluate("fts", goldens=_SIGNAL_GOLDENS, k=10)

    assert after.recall_at(10) >= 0.90                      # floor holds
    assert after.recall_at(10) >= base.recall_at(10)        # not buried by growth
    assert after.mrr >= base.mrr - 1e-9                     # no MRR regression


def test_e2e4_query_self_heals_index_on_new_content(kb_root: Path):
    """A query self-heals the index on an mtime/size diff: content added AFTER
    the last rebuild is retrievable with no explicit `index --rebuild`."""
    _concept_page(kb_root, "alpha-aardvark", "Alpha",
                  "Distinctive aardvark terminology unique to the alpha concept.")
    search_index.refresh(rebuild=True)

    # New page written after the rebuild — never explicitly indexed.
    _concept_page(kb_root, "beta-xylophone", "Beta",
                  "Distinctive xylophone terminology unique to the beta concept.")
    healed = rev.evaluate(
        "fts",
        goldens=[rev.GoldenQuery(q="xylophone terminology unique to the beta concept",
                                 expect=["beta-xylophone"], domain="d")],
        k=10,
    )
    assert healed.recall_at(10) == 1.0  # found via self-heal on read


# Wave-2 near-duplicates that share the golden queries' vocabulary, so they
# actually enter the ranked lists — making the incremental-vs-cold comparison
# non-trivial (a pure-noise wave never changes the signal rankings).
_COMPETITOR_PAGES = [
    ("fvg-echo", "FVG Echo", "A second imbalance gap left by aggressive orders appears in price."),
    ("ob-echo", "OB Echo", "A second institutional order block where price originated forms here."),
    ("sweep-echo", "Sweep Echo", "Another sweep taking out resting stop orders beyond a swing point."),
    ("mss-echo", "MSS Echo", "Another trend change after a confirmed break of structure occurs."),
    ("pd-echo", "PD Echo", "More zones split a dealing range around the equilibrium midpoint here."),
]


def test_e2e4_incremental_self_heal_matches_cold_rebuild(kb_root: Path):
    """The derived index healed incrementally on read must rank IDENTICALLY to
    a cold rebuild from the same canonical markdown — no derived-state drift."""
    _seed_signal(kb_root)
    search_index.refresh(rebuild=True)        # wave 1 indexed cold
    for slug, title, body in _COMPETITOR_PAGES:
        _concept_page(kb_root, slug, title, body)  # wave 2, not yet indexed

    # Incremental: the eval's queries self-heal the index (no rebuild=True).
    incr = rev.evaluate("fts", goldens=_SIGNAL_GOLDENS, k=10)
    incr_ranked = [r.ranked_slugs for r in incr.results]
    # The comparison must be non-trivial: competitors pulled into the rankings.
    assert any(len(r) >= 2 for r in incr_ranked)

    # Cold rebuild from the identical on-disk corpus.
    search_index.refresh(rebuild=True)
    cold = rev.evaluate("fts", goldens=_SIGNAL_GOLDENS, k=10)
    cold_ranked = [r.ranked_slugs for r in cold.results]

    assert incr_ranked == cold_ranked
