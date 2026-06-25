# tests/test_retrieval_probe_gate.py
"""META-GATE: hybrid recall beats lexical-only on a paraphrased query.

Corpus is a small synthetic fixture (jargon page + noise filler), so this test
is corpus-independent and runs in the full suite. gate.py Step-1 catches any
regression automatically.

Teeth verification (tuned from the brief's original fixture):
- Brief used query "why do people lose pleasure and drive" — "and" is an OR-joined
  FTS prefix token that matches "and" in the body, so BM25 found the page and the
  precondition was inert. Widened the vocabulary gap by switching to
  "inability to feel happiness": zero FTS prefix matches against the body
  ("blunted reward sensitivity and lost motivation"), so lexical-only returns [].
- Hybrid (BM25+dense via stub encoder char-3-gram hashing) ranks "anhedonia"
  first via the dense component, proving the feature adds recall over lexical.
"""
from pathlib import Path

from gateway import paths, search_index, frontmatter as fm
from gateway.ops import retrieve as retr


def _page(slug: str, body: str) -> None:
    d = paths.wiki_dir() / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{slug}.md").write_text(
        fm.serialize(
            {
                "type": "concept",
                "slug": slug,
                "title": slug,
                "domains": ["d"],
                "created_at": "2026-01-01T00:00:00Z",
                "last_updated": "2026-05-01T00:00:00Z",
            },
            body,
        )
    )


def test_hybrid_beats_lexical_on_paraphrase(kb_root: Path) -> None:
    """Hybrid (BM25+dense) surfaces a jargon page that lexical-only misses.

    The jargon page uses clinical vocabulary (anhedonia, blunted reward,
    motivation); the query uses lay vocabulary (inability, happiness).
    BM25 shares zero tokens — no FTS prefix match between
    "inability to feel happiness" and "blunted reward sensitivity and lost
    motivation" — so lexical-only returns nothing. The stub encoder's
    char-3-gram hashing finds similarity and ranks "anhedonia" first in the
    dense component; RRF fusion surfaces it in the hybrid result.
    """
    # Jargon page: clinical vocabulary only. Body excludes ALL query tokens
    # ("inability", "feel", "happiness") so FTS OR-prefix cannot match.
    _page(
        "anhedonia",
        "## Body\n\nblunted reward sensitivity and lost motivation.\n",
    )
    # Noise filler: lexically unrelated pages to exercise RRF and confirm
    # anhedonia must win via dense, not just by default.
    for i in range(4):
        _page(
            f"noise{i}",
            f"## B\n\nunrelated filler about tax filing widget accounting ledger {i}.\n",
        )

    # Build both indexes.
    search_index.refresh(rebuild=True)
    from gateway.retrieval_index import retrieval_index

    retrieval_index().rebuild_from_canonical()

    # Lay query: none of "inability", "to", "feel", "happiness" appear in or
    # prefix-match any token in the anhedonia page body.
    q = "inability to feel happiness"

    _, lex = retr.retrieve(q, domain="d", hybrid=False)
    _, hyb = retr.retrieve(q, domain="d", hybrid=True)

    lex_slugs = [s.slug for s in lex]
    hyb_slugs = [s.slug for s in hyb]

    # Precondition: BM25/FTS must NOT find "anhedonia" — proves the vocabulary
    # gap is real and the test has teeth (not already solved by lexical alone).
    assert "anhedonia" not in lex_slugs, (
        f"precondition failed: lexical-only found 'anhedonia' in {lex_slugs}; "
        "widen the jargon/lay vocabulary gap so BM25 cannot match."
    )

    # Hybrid assertion: dense component must surface "anhedonia" via the
    # stub encoder's char-3-gram similarity.
    assert "anhedonia" in hyb_slugs, (
        f"hybrid must surface 'anhedonia'; got {hyb_slugs}. "
        "Dense index may not be populated or RRF fusion is not lifting it."
    )
