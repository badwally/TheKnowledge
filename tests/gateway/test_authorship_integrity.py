"""Tier-2 structural integrity guards for the wiki authorship loop.

These guards make the gateway enforce knowledge integrity regardless of what the
(fallible) LLM authorship agent returns: an update may not silently drop prior
citations or shrink a page, a multi-page plan is all-or-nothing, slugs are unique
across page kinds, and re-applying an unchanged page is a no-op.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops.apply_plan import apply_plan
from gateway.plan import Plan, WikiUpdate


def _seed_source(kb_root, make_source, source_id="yt-integ001A", domain="d-integ"):
    text = make_source(id_=source_id, domains=[domain])
    raw = paths.raw_source_path("youtube", source_id)
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(text)
    return raw


def _concept_body(slug: str, *citations: str, extra_claims: int = 0) -> str:
    cites = list(citations)
    claim_lines = "\n".join(
        f"- Established claim number {n} by the literature [[sources/{cites[n % len(cites)]}]]."
        for n in range(1 + extra_claims)
    )
    src_lines = "\n".join(f"- [[sources/{c}]]" for c in dict.fromkeys(cites))
    return (
        f"# {slug}\n\n"
        f"## Summary\n\nThis concept is grounded in the source [[sources/{cites[0]}]].\n\n"
        f"## Key claims\n\n{claim_lines}\n\n"
        f"## Sources\n\n{src_lines}\n\n"
        f"## Related\n\n- [[concepts/related-thing]]\n"
    )


def _concept_update(slug: str, *citations: str, kind: str = "update", extra_claims: int = 0):
    front = {
        "type": "concept",
        "slug": slug,
        "canonical_name": slug.replace("-", " ").title(),
        "domains": ["d-integ"],
    }
    return WikiUpdate(
        target_path=f"wiki/concepts/{slug}.md",
        update_kind=kind,
        content=fm.serialize(front, _concept_body(slug, *citations, extra_claims=extra_claims)),
    )


def _write_existing_concept(kb_root, slug: str, *citations: str, extra_claims: int = 0) -> Path:
    d = paths.wiki_dir() / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": slug,
        "canonical_name": slug.replace("-", " ").title(),
        "domains": ["d-integ"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, _concept_body(slug, *citations, extra_claims=extra_claims)))
    return p


# --- T2.7: no-citation-loss-on-update ---------------------------------------


def test_update_dropping_a_prior_citation_is_rejected(kb_root, make_source):
    """An update that removes a citation the page already had must fail — the
    gateway makes knowledge monotonic; the agent cannot silently destroy a
    cited claim by rewriting the page from a partial view."""
    _seed_source(kb_root, make_source)
    _write_existing_concept(kb_root, "arbor", "yt-integ001A", "yt-otherSrc9Z")

    # New content keeps only one of the two prior citations.
    update = _concept_update("arbor", "yt-integ001A", kind="update")
    plan = Plan(source_id="yt-integ001A", updates=[update])

    result = apply_plan(plan)

    assert not result.success
    assert any("citation" in e.lower() and "arbor" in e for e in result.errors), result.errors
    # The page on disk is untouched (still has both citations).
    body = (paths.wiki_dir() / "concepts" / "arbor.md").read_text()
    assert "[[sources/yt-otherSrc9Z]]" in body


def test_update_preserving_all_citations_and_adding_succeeds(kb_root, make_source):
    """Negative control: an update that keeps all prior citations and adds the
    new source's must succeed."""
    _seed_source(kb_root, make_source)
    _write_existing_concept(kb_root, "arbor", "yt-otherSrc9Z")

    # Keep the prior citation, add the new source.
    update = _concept_update("arbor", "yt-otherSrc9Z", "yt-integ001A", kind="update", extra_claims=1)
    plan = Plan(source_id="yt-integ001A", updates=[update])

    result = apply_plan(plan)

    assert result.success, result.errors
    body = (paths.wiki_dir() / "concepts" / "arbor.md").read_text()
    assert "[[sources/yt-otherSrc9Z]]" in body
    assert "[[sources/yt-integ001A]]" in body


# --- T2.8: all-or-nothing application ---------------------------------------


def test_midloop_write_failure_rolls_back_earlier_creates(kb_root, make_source, monkeypatch):
    """If page 2's write fails, page 1 (a create) must be rolled back — the
    multi-page plan is all-or-nothing, no half-authored wiki."""
    import gateway.ops.apply_plan as ap

    _seed_source(kb_root, make_source)
    plan = Plan(
        source_id="yt-integ001A",
        updates=[
            _concept_update("page-one", "yt-integ001A", kind="create"),
            _concept_update("page-two", "yt-integ001A", kind="create"),
        ],
    )

    real_write = ap.write_atomic
    calls = {"n": 0}

    def flaky_write(target, content):
        calls["n"] += 1
        if "page-two" in str(target):
            raise OSError("simulated disk failure on page two")
        return real_write(target, content)

    monkeypatch.setattr(ap, "write_atomic", flaky_write)

    result = apply_plan(plan)

    assert not result.success
    # Page one must have been rolled back (it was a create → unlinked).
    assert not (paths.wiki_dir() / "concepts" / "page-one.md").exists(), (
        "page-one was committed despite page-two failing — not atomic"
    )
    assert not (paths.wiki_dir() / "concepts" / "page-two.md").exists()


def test_midloop_write_failure_restores_prior_update_content(kb_root, make_source, monkeypatch):
    """If a later page fails, an earlier UPDATE must be restored to its prior
    on-disk content, not left half-rewritten."""
    import gateway.ops.apply_plan as ap

    _seed_source(kb_root, make_source)
    _write_existing_concept(kb_root, "page-one", "yt-integ001A")
    prior = (paths.wiki_dir() / "concepts" / "page-one.md").read_text()

    plan = Plan(
        source_id="yt-integ001A",
        updates=[
            _concept_update("page-one", "yt-integ001A", kind="update", extra_claims=2),
            _concept_update("page-two", "yt-integ001A", kind="create"),
        ],
    )

    real_write = ap.write_atomic

    def flaky_write(target, content):
        if "page-two" in str(target):
            raise OSError("boom")
        return real_write(target, content)

    monkeypatch.setattr(ap, "write_atomic", flaky_write)

    result = apply_plan(plan)

    assert not result.success
    assert (paths.wiki_dir() / "concepts" / "page-one.md").read_text() == prior, (
        "page-one was not restored to its prior content after rollback"
    )


# --- T2.9: cross-kind slug collision ----------------------------------------


def test_create_colliding_with_other_kind_slug_is_rejected(kb_root, make_source):
    """Creating wiki/entities/<slug>.md when wiki/concepts/<slug>.md already
    exists must fail — a slug must be unique across page kinds, or [[<slug>]]
    resolution is ambiguous and citations split across two canonical pages."""
    _seed_source(kb_root, make_source)
    _write_existing_concept(kb_root, "food-noise", "yt-integ001A")

    front = {
        "type": "entity",
        "entity_kind": "other",
        "slug": "food-noise",
        "canonical_name": "Food Noise",
        "domains": ["d-integ"],
    }
    body = (
        "# Food Noise\n\n## Summary\n\nAn entity grounded in the source [[sources/yt-integ001A]].\n\n"
        "## Key facts\n\n- A fact established by the source [[sources/yt-integ001A]].\n\n"
        "## Sources\n\n- [[sources/yt-integ001A]]\n\n## Related\n\n- [[concepts/related-thing]]\n"
    )
    plan = Plan(
        source_id="yt-integ001A",
        updates=[WikiUpdate(target_path="wiki/entities/food-noise.md", update_kind="create", content=fm.serialize(front, body))],
    )

    result = apply_plan(plan)

    assert not result.success
    assert any("cross-kind" in e.lower() or "collision" in e.lower() for e in result.errors), result.errors
    assert not (paths.wiki_dir() / "entities" / "food-noise.md").exists()


def test_same_kind_update_to_existing_slug_is_fine(kb_root, make_source):
    """Negative control: updating the same-kind page with the same slug is the
    normal case and must not trip the cross-kind guard."""
    _seed_source(kb_root, make_source)
    _write_existing_concept(kb_root, "food-noise", "yt-integ001A")

    update = _concept_update("food-noise", "yt-integ001A", kind="update", extra_claims=1)
    result = apply_plan(Plan(source_id="yt-integ001A", updates=[update]))

    assert result.success, result.errors


# --- T2.10: convergence on re-run -------------------------------------------


def test_reapplying_identical_body_does_not_thrash_last_updated(kb_root, make_source):
    """Re-authoring a page whose body is unchanged must be a no-op: no rewrite,
    no last_updated bump. Otherwise a re-run (LLM nondeterminism aside) erodes/
    churns the corpus instead of converging."""
    _seed_source(kb_root, make_source)
    existing = _write_existing_concept(kb_root, "arbor", "yt-integ001A", extra_claims=1)
    front_before, body_before = fm.parse(existing.read_text())
    lu_before = front_before["last_updated"]

    # An update whose body is byte-identical to what's on disk.
    update = WikiUpdate(
        target_path="wiki/concepts/arbor.md",
        update_kind="update",
        content=fm.serialize(
            {"type": "concept", "slug": "arbor", "canonical_name": "Arbor", "domains": ["d-integ"]},
            body_before,
        ),
    )
    result = apply_plan(Plan(source_id="yt-integ001A", updates=[update]))

    assert result.success, result.errors
    front_after, _ = fm.parse(existing.read_text())
    assert front_after["last_updated"] == lu_before, (
        "last_updated thrashed on an identical-body re-apply (not convergent)"
    )
