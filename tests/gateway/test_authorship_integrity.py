"""Tier-2 structural integrity guards for the wiki authorship loop.

These guards make the gateway enforce knowledge integrity regardless of what the
(fallible) LLM authorship agent returns: an update may not silently drop prior
citations or shrink a page, a multi-page plan is all-or-nothing, slugs are unique
across page kinds, and re-applying an unchanged page is a no-op.
"""

from __future__ import annotations

from pathlib import Path

import pytest

import json

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops.apply_plan import apply_plan
from gateway.ops.ingest import _invoke_plan_and_apply
from gateway.plan import Plan, WikiUpdate


class _QueuedPlanClient:
    """Stub plan client returning queued responses; counts calls (for the
    repair loop). Implements `call_split` (the dispatch's preferred stub path)."""

    def __init__(self, responses):
        self._responses = list(responses)
        self.calls = 0

    def call_split(self, *, system: str, user: str) -> str:
        self.calls += 1
        return self._responses.pop(0)


def _entity_plan_json(entity_kind: str, source_id: str = "yt-integ001A") -> str:
    front = {
        "type": "entity",
        "slug": "arbor-system",
        "canonical_name": "Arbor",
        "entity_kind": entity_kind,
        "domains": ["d-integ"],
    }
    body = (
        f"# Arbor\n\n## Summary\n\nArbor is grounded in the source [[sources/{source_id}]].\n\n"
        f"## Key facts\n\n- A fact established by the source [[sources/{source_id}]].\n\n"
        f"## Sources\n\n- [[sources/{source_id}]]\n\n## Related\n\n- [[concepts/related-thing]]\n"
    )
    return json.dumps(
        {
            "source_id": source_id,
            "updates": [
                {
                    "target_path": "wiki/entities/arbor-system.md",
                    "update_kind": "create",
                    "content": fm.serialize(front, body),
                }
            ],
        }
    )


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


# --- T3: validate-then-repair loop ------------------------------------------

_FRONT = {"id": "yt-integ001A", "type": "youtube", "title": "Arbor", "domains": ["d-integ"]}


def test_authorship_repairs_after_validator_rejection(kb_root, make_source):
    """First plan uses entity_kind 'system' (rejected); the gateway feeds the
    validator error back and the agent's corrected plan ('software') applies."""
    _seed_source(kb_root, make_source)
    client = _QueuedPlanClient([_entity_plan_json("system"), _entity_plan_json("software")])

    result = _invoke_plan_and_apply(
        front=_FRONT, body="source body", domain="d-integ", plan_client=client, draft=False
    )

    assert result.success, result.errors
    assert client.calls == 2, "should have made one repair attempt"
    pf, _ = fm.parse((paths.wiki_dir() / "entities" / "arbor-system.md").read_text())
    assert pf["entity_kind"] == "software"


def test_authorship_gives_up_after_max_repair(kb_root, make_source):
    """If both the original and the repair are invalid, fail cleanly after the
    bounded number of attempts (no infinite loop)."""
    _seed_source(kb_root, make_source)
    client = _QueuedPlanClient([_entity_plan_json("system"), _entity_plan_json("alsobad")])

    result = _invoke_plan_and_apply(
        front=_FRONT, body="source body", domain="d-integ", plan_client=client, draft=False
    )

    assert not result.success
    assert client.calls == 2
    assert not (paths.wiki_dir() / "entities" / "arbor-system.md").exists()


# --- T4.12: dry-run -----------------------------------------------------------


def test_dry_run_reports_plan_without_writing(kb_root, make_source):
    """--dry-run validates the plan and reports created/updated, writing nothing."""
    _seed_source(kb_root, make_source)
    client = _QueuedPlanClient([_entity_plan_json("software")])

    result = _invoke_plan_and_apply(
        front=_FRONT, body="b", domain="d-integ", plan_client=client, draft=False, dry_run=True
    )

    assert result.success
    assert "[dry-run]" in result.summary
    assert result.authorship_report.pages_created == ["wiki/entities/arbor-system.md"]
    assert not (paths.wiki_dir() / "entities" / "arbor-system.md").exists(), "dry-run wrote a file"


def test_dry_run_validates_and_surfaces_errors(kb_root, make_source):
    """I1: dry-run must VALIDATE (no-loss/schema/entity-kind), not just echo the
    plan. An invalid plan (and an invalid repair) must report failure and write
    nothing — dry-run that reports green on a rejectable plan is a footgun."""
    _seed_source(kb_root, make_source)
    client = _QueuedPlanClient([_entity_plan_json("boguskind1"), _entity_plan_json("boguskind2")])

    result = _invoke_plan_and_apply(
        front=_FRONT, body="b", domain="d-integ", plan_client=client, draft=False, dry_run=True
    )

    assert not result.success, "dry-run must surface the validation failure"
    assert any("entity" in e.lower() and "kind" in e.lower() for e in result.errors), result.errors
    assert not (paths.wiki_dir() / "entities" / "arbor-system.md").exists()


def test_dry_run_repairs_then_reports_valid_plan(kb_root, make_source):
    """Dry-run engages the repair loop too: a fixable first plan is repaired and
    the report reflects the VALID plan — still writing nothing."""
    _seed_source(kb_root, make_source)
    client = _QueuedPlanClient([_entity_plan_json("badkind"), _entity_plan_json("software")])

    result = _invoke_plan_and_apply(
        front=_FRONT, body="b", domain="d-integ", plan_client=client, draft=False, dry_run=True
    )

    assert result.success, result.errors
    assert client.calls == 2  # repaired in dry-run
    assert result.authorship_report.pages_created == ["wiki/entities/arbor-system.md"]
    assert not (paths.wiki_dir() / "entities" / "arbor-system.md").exists()


def test_repair_handles_unparseable_first_response(kb_root, make_source):
    """M6: the repair loop also recovers from a malformed-JSON first response,
    not just validation errors."""
    _seed_source(kb_root, make_source)
    client = _QueuedPlanClient(["this is not json at all", _entity_plan_json("software")])

    result = _invoke_plan_and_apply(
        front=_FRONT, body="b", domain="d-integ", plan_client=client, draft=False
    )

    assert result.success, result.errors
    assert client.calls == 2
    assert (paths.wiki_dir() / "entities" / "arbor-system.md").exists()


def test_cross_kind_guard_covers_moc(kb_root, make_source):
    """M5: a concept create colliding with an existing MOC slug is rejected
    (the cross-kind scan includes mocs)."""
    _seed_source(kb_root, make_source)
    d = paths.wiki_dir() / "mocs"
    d.mkdir(parents=True, exist_ok=True)
    (d / "ai-and-agents.md").write_text(
        fm.serialize({"type": "moc", "slug": "ai-and-agents", "domain": "d-integ"}, "# MOC\n")
    )

    update = _concept_update("ai-and-agents", "yt-integ001A", kind="create")
    result = apply_plan(Plan(source_id="yt-integ001A", updates=[update]))

    assert not result.success
    assert any("cross-kind" in e.lower() for e in result.errors), result.errors


# --- T2.7b: body-shrink tripwire (was shipped untested — review §1 High) -----


def test_update_shrinking_body_past_floor_is_rejected(kb_root, make_source):
    """An update that PRESERVES all citations but cuts the body past the shrink
    floor is rejected as a suspicious rewrite that likely drops claims. Isolates
    the shrink guard from the citation-loss guard (same single citation kept)."""
    _seed_source(kb_root, make_source)
    _write_existing_concept(kb_root, "big", "yt-integ001A", extra_claims=30)

    # Same citation preserved, but a tiny body (well under 50% of the original).
    update = _concept_update("big", "yt-integ001A", kind="update", extra_claims=0)
    result = apply_plan(Plan(source_id="yt-integ001A", updates=[update]))

    assert not result.success
    assert any("body-shrink" in e for e in result.errors), result.errors
    # On-disk page untouched (still large).
    assert "claim number 30" in (paths.wiki_dir() / "concepts" / "big.md").read_text()


def test_update_growing_body_is_not_shrink_rejected(kb_root, make_source):
    """Negative control: an update that GROWS the page (citations preserved) must
    not trip the shrink guard."""
    _seed_source(kb_root, make_source)
    _write_existing_concept(kb_root, "big", "yt-integ001A", extra_claims=2)

    update = _concept_update("big", "yt-integ001A", kind="update", extra_claims=12)
    result = apply_plan(Plan(source_id="yt-integ001A", updates=[update]))

    assert result.success, result.errors
