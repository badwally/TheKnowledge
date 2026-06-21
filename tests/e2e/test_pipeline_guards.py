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

from gateway import frontmatter as fm
from gateway import paths, validator
from gateway.filter.semantic import FilterResult
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
