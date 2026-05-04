"""Tests for M6: wiki-page validation, plan format, apply_plan, finalize, query."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from gateway import citations as cit
from gateway import frontmatter as fm
from gateway import paths
from gateway import validator as v
from gateway import wiki_pages
from gateway.ops.apply_plan import apply_plan
from gateway.ops.finalize import finalize
from gateway.ops.ingest import ingest
from gateway.ops.query import query
from gateway.plan import (
    Contradiction,
    Plan,
    PlanError,
    WikiUpdate,
    build_plan_prompt,
    parse_plan_response,
)


# --- citations.py ----------------------------------------------------------


def test_find_wikilinks_extracts_targets_and_anchors():
    text = "See [[sources/yt-abc#1820]] and also [[concepts/food-noise]] plus [[sources/pubmed-123|alias]]."
    wikilinks = cit.find_wikilinks(text)
    assert len(wikilinks) == 3
    targets = [(w.target, w.anchor) for w in wikilinks]
    assert ("sources/yt-abc", "1820") in targets
    assert ("concepts/food-noise", "") in targets
    assert ("sources/pubmed-123", "") in targets


def test_find_source_citations_filters():
    text = "[[sources/yt-1]] and [[concepts/x]]"
    src = cit.find_source_citations(text)
    assert len(src) == 1
    assert src[0].target == "sources/yt-1"


def test_claim_sentences_skip_headers_and_lists():
    body = "## A header\n\n- Bullet item\n\nThis is a real claim sentence with enough words to count.\n"
    claims = cit.find_claim_sentences(body)
    assert any("real claim sentence" in c.text for c in claims)
    # The header line should not be a claim
    assert not any("A header" in c.text for c in claims)


def test_claim_sentences_skip_code_fences():
    body = "Real claim sentence with enough words here today.\n```\nthis claim is in code so should be skipped.\n```\n"
    claims = cit.find_claim_sentences(body)
    assert len(claims) == 1
    assert "Real claim sentence" in claims[0].text


def test_citation_density_counts_cited_vs_uncited():
    body = (
        "First claim sentence with enough words [[sources/yt-1]].\n"
        "Second claim sentence with enough words and no citation.\n"
    )
    cited, total, ratio = cit.citation_density(body)
    assert total == 2
    assert cited == 1
    assert 0.49 < ratio < 0.51


# --- wiki_pages.py ---------------------------------------------------------


def test_levenshtein_basic():
    assert wiki_pages.levenshtein("food-noise", "food-noise") == 0
    assert wiki_pages.levenshtein("food-noise", "food_noise") == 1
    assert wiki_pages.levenshtein("food-noise", "foodnoise") == 1


def test_page_type_for_path():
    assert wiki_pages.page_type_for_path("wiki/entities/semaglutide.md") == "entity"
    assert wiki_pages.page_type_for_path("wiki/concepts/food-noise.md") == "concept"
    assert wiki_pages.page_type_for_path("wiki/sources/yt-abc.md") == "source"
    assert wiki_pages.page_type_for_path("wiki/proposals/health.md") == "domain-proposal"
    assert wiki_pages.page_type_for_path("raw/youtube/yt-abc.md") is None


def test_domain_proposal_schema_registered():
    schema = wiki_pages.schema_for_type("domain-proposal")
    assert schema is not None
    assert schema.directory == "wiki/proposals"
    assert "proposed_domain" in schema.required_fields
    assert "status" in schema.required_fields
    assert "member_sources" in schema.required_fields
    assert "Rationale" in schema.required_sections
    assert "Member sources" in schema.required_sections
    assert schema.citation_grounded is False


def test_missing_sections_for_concept_template():
    body = "## Summary\nx\n## Key claims\nx\n"
    missing = wiki_pages.missing_sections(body, ("Summary", "Key claims", "Sources", "Related"))
    assert sorted(missing) == ["Related", "Sources"]


# --- validator wiki-page rules --------------------------------------------


def _good_concept_page() -> tuple[dict, str]:
    front = {
        "type": "concept",
        "slug": "food-noise",
        "canonical_name": "Food noise",
        "domains": ["glp1-reward-modulation"],
    }
    body = (
        "# Food noise\n\n"
        "## Summary\n\n"
        "Food noise is the persistent intrusive thoughts about food [[sources/yt-abc]].\n\n"
        "## Key claims\n\n"
        "- It is reduced by GLP-1 receptor agonists [[sources/pubmed-123]].\n\n"
        "## Sources\n\n"
        "- [[sources/yt-abc]]\n\n"
        "## Related\n\n"
        "- [[concepts/reward-blunting]]\n"
    )
    return front, body


def test_validate_wiki_page_happy_path():
    front, body = _good_concept_page()
    result = v.validate_wiki_page(front, body, "concept")
    assert result.ok, [str(e) for e in result.errors]


def test_validate_wiki_page_missing_required_field():
    front, body = _good_concept_page()
    del front["domains"]
    result = v.validate_wiki_page(front, body, "concept")
    assert not result.ok
    assert any("required-field" in e.rule for e in result.errors)


def test_validate_wiki_page_type_mismatch():
    front, body = _good_concept_page()
    front["type"] = "entity"
    result = v.validate_wiki_page(front, body, "concept")
    assert any("type-mismatch" in e.rule for e in result.errors)


def test_validate_wiki_page_missing_section():
    front, body = _good_concept_page()
    body_no_related = body.replace("## Related\n\n- [[concepts/reward-blunting]]\n", "")
    result = v.validate_wiki_page(front, body_no_related, "concept")
    assert any("section-missing" in e.rule for e in result.errors)


def _good_domain_proposal_page() -> tuple[dict, str]:
    front = {
        "type": "domain-proposal",
        "slug": "proposal-investing-letters",
        "title": "Investing letters and macro commentary",
        "proposed_domain": "investing-letters",
        "status": "draft",
        "member_sources": ["pdf-abc", "pdf-def", "pdf-ghi"],
        "rationale": "Hedge fund letters and macro commentary recur across the Apple Notes corpus.",
    }
    body = (
        "# Investing letters and macro commentary\n\n"
        "## Rationale\n\n"
        "Cluster of investor letters and macro commentary, distinct from "
        "trading-mechanics material in scope and tone.\n\n"
        "## Member sources\n\n"
        "- [[sources/pdf-abc]]: Ambrus Capital Q3 letter\n"
        "- [[sources/pdf-def]]: Druckenmiller speech\n"
        "- [[sources/pdf-ghi]]: BII Global Outlook\n"
    )
    return front, body


def test_validate_domain_proposal_happy_path():
    front, body = _good_domain_proposal_page()
    result = v.validate_wiki_page(front, body, "domain-proposal")
    assert result.ok, [str(e) for e in result.errors]


def test_validate_domain_proposal_missing_member_sources():
    front, body = _good_domain_proposal_page()
    del front["member_sources"]
    result = v.validate_wiki_page(front, body, "domain-proposal")
    assert not result.ok
    assert any("required-field" in e.rule and e.field_name == "member_sources" for e in result.errors)


def test_citation_grounding_rejects_uncited_claim():
    front = {
        "type": "concept",
        "slug": "food-noise",
        "canonical_name": "Food noise",
        "domains": ["d"],
    }
    body = (
        "# Food noise\n\n"
        "## Summary\n\nThis is a long claim sentence with no citation at all anywhere.\n\n"
        "## Key claims\n\n- [[sources/yt-abc]]\n\n"
        "## Sources\n\n- [[sources/yt-abc]]\n\n"
        "## Related\n\n- [[concepts/x]]\n"
    )
    result = v.validate_wiki_page(front, body, "concept")
    assert any("citation-grounding" in e.rule for e in result.errors)


def test_citation_grounding_warning_in_draft_mode():
    front = {
        "type": "concept",
        "slug": "food-noise",
        "canonical_name": "Food noise",
        "domains": ["d"],
        "draft": True,
    }
    body = (
        "# Food noise\n\n"
        "## Summary\n\nThis is a long claim sentence with no citation at all anywhere.\n\n"
        "## Key claims\n\n- [[sources/yt-abc]]\n\n"
        "## Sources\n\n- [[sources/yt-abc]]\n\n"
        "## Related\n\n- [[concepts/x]]\n"
    )
    result = v.validate_wiki_page(front, body, "concept")
    assert result.ok, [str(e) for e in result.errors]
    assert any("citation-grounding" in w.rule for w in result.warnings)


def test_slug_uniqueness_rejects_duplicate():
    result = v.validate_slug_uniqueness("food-noise", ["food-noise", "reward"])
    assert any("slug-duplicate" in e.rule for e in result.errors)


def test_slug_similarity_warns_near_duplicates():
    result = v.validate_slug_uniqueness("food_noise", ["food-noise"])
    assert result.ok  # warning, not error
    assert any("slug-similar" in w.rule for w in result.warnings)


def test_slug_similarity_force_new_overrides_warning():
    result = v.validate_slug_uniqueness("food_noise", ["food-noise"], force_new=True)
    assert result.ok
    assert not result.warnings


# --- plan.py ---------------------------------------------------------------


def test_parse_plan_response_plain_json():
    raw = '{"source_id": "yt-1", "rationale": "r", "updates": [{"target_path": "wiki/entities/x.md", "update_kind": "create", "content": "---\\nx: y\\n---\\nbody"}]}'
    plan = parse_plan_response(raw)
    assert plan.source_id == "yt-1"
    assert len(plan.updates) == 1
    assert plan.updates[0].target_path == "wiki/entities/x.md"


def test_parse_plan_response_strips_code_fences():
    raw = '```json\n{"source_id": "yt-1", "rationale": "r", "updates": []}\n```'
    plan = parse_plan_response(raw)
    assert plan.source_id == "yt-1"
    assert plan.updates == []


def test_parse_plan_response_rejects_missing_source_id():
    with pytest.raises(PlanError):
        parse_plan_response('{"updates": []}')


def test_parse_plan_response_expects_specific_source_id():
    raw = '{"source_id": "yt-1", "rationale": "r", "updates": []}'
    with pytest.raises(PlanError):
        parse_plan_response(raw, expected_source_id="yt-2")


def test_parse_plan_response_rejects_bad_update_kind():
    raw = '{"source_id": "yt-1", "rationale": "r", "updates": [{"target_path": "wiki/entities/x.md", "update_kind": "patch", "content": "x"}]}'
    with pytest.raises(PlanError):
        parse_plan_response(raw)


def test_parse_plan_response_parses_contradictions():
    import json as _json
    raw = _json.dumps({
        "source_id": "yt-1",
        "rationale": "r",
        "updates": [],
        "contradictions": [
            {
                "existing_page": "wiki/concepts/food-noise.md",
                "existing_claim": "Food noise is universally reduced by GLP-1 RAs",
                "new_claim": "Food noise reduction varies by receptor subtype",
                "source_id": "yt-1",
                "severity": "moderate",
            }
        ],
    })
    plan = parse_plan_response(raw)
    assert len(plan.contradictions) == 1
    c = plan.contradictions[0]
    assert c.existing_page == "wiki/concepts/food-noise.md"
    assert c.severity == "moderate"


def test_parse_plan_response_defaults_empty_contradictions():
    raw = '{"source_id": "yt-1", "rationale": "r", "updates": []}'
    plan = parse_plan_response(raw)
    assert plan.contradictions == []


def test_build_plan_prompt_includes_source_and_existing():
    prompt = build_plan_prompt("source body", {"wiki/concepts/x.md": "existing content"})
    assert "source body" in prompt
    assert "existing content" in prompt
    assert "wiki/concepts/x.md" in prompt


# --- AuthorshipReport ------------------------------------------------------


def test_authorship_report_summary_formatting():
    from gateway.core import AuthorshipReport
    from gateway.plan import Contradiction

    report = AuthorshipReport(
        pages_created=["wiki/entities/semaglutide.md", "wiki/concepts/food-noise.md"],
        pages_updated=["wiki/concepts/reward-blunting.md"],
        contradictions=[
            Contradiction(
                existing_page="wiki/concepts/reward-blunting.md",
                existing_claim="Reward blunting is permanent",
                new_claim="Reward blunting reverses after discontinuation",
                source_id="pubmed-123",
                severity="major",
            )
        ],
    )
    summary = report.format_summary()
    assert "2 created" in summary
    assert "1 updated" in summary
    assert "1 contradiction" in summary


def test_authorship_report_empty():
    from gateway.core import AuthorshipReport

    report = AuthorshipReport()
    summary = report.format_summary()
    assert "0 created" in summary


def test_authorship_report_detail_formatting():
    from gateway.core import AuthorshipReport
    from gateway.plan import Contradiction

    report = AuthorshipReport(
        pages_created=["wiki/entities/drug-x.md"],
        pages_updated=["wiki/concepts/mechanism-y.md"],
        contradictions=[
            Contradiction(
                existing_page="wiki/concepts/mechanism-y.md",
                existing_claim="Effect is permanent",
                new_claim="Effect reverses in 12 weeks",
                source_id="pubmed-456",
                severity="major",
            )
        ],
    )
    lines = report.format_detail()
    assert any("+ wiki/entities/drug-x.md" in l for l in lines)
    assert any("~ wiki/concepts/mechanism-y.md" in l for l in lines)
    assert any("CONTRADICTION" in l and "major" in l for l in lines)


# --- apply_plan ------------------------------------------------------------


def _seed_source(kb_root, make_source, source_id="yt-applyTest1A", domain="d-apply"):
    text = make_source(id_=source_id, domains=[domain])
    raw = paths.raw_source_path("youtube", source_id)
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(text)
    return raw


def _make_concept_update(slug: str, source_id: str, *, kind: str = "create"):
    front = {
        "type": "concept",
        "slug": slug,
        "canonical_name": slug.replace("-", " ").title(),
        "domains": ["d-apply"],
    }
    body = (
        f"# {slug}\n\n"
        f"## Summary\n\nThis concept arose from the new source [[sources/{source_id}]].\n\n"
        f"## Key claims\n\n- Established by primary literature [[sources/{source_id}]].\n\n"
        f"## Sources\n\n- [[sources/{source_id}]]\n\n"
        f"## Related\n\n- [[concepts/related-thing]]\n"
    )
    return WikiUpdate(target_path=f"wiki/concepts/{slug}.md", update_kind=kind, content=fm.serialize(front, body))


def test_apply_plan_writes_pages_and_updates_backlinks(kb_root, make_source):
    raw_path = _seed_source(kb_root, make_source)
    plan = Plan(
        source_id="yt-applyTest1A",
        rationale="seed test",
        updates=[_make_concept_update("food-noise", "yt-applyTest1A")],
    )
    result = apply_plan(plan)
    assert result.success, result.errors

    page = paths.wiki_dir() / "concepts" / "food-noise.md"
    assert page.exists()

    front, body = fm.parse(page.read_text())
    assert front["type"] == "concept"
    assert "## Summary" in body

    # Source backlinks updated
    raw_front, _ = fm.parse(raw_path.read_text())
    assert "wiki/concepts/food-noise.md" in raw_front["wiki_pages"]


def test_apply_plan_atomic_rejects_when_one_update_fails(kb_root, make_source):
    _seed_source(kb_root, make_source)
    bad_update = _make_concept_update("malformed", "yt-applyTest1A")
    bad_update.content = "no frontmatter at all"

    plan = Plan(
        source_id="yt-applyTest1A",
        updates=[
            _make_concept_update("food-noise", "yt-applyTest1A"),
            bad_update,
        ],
    )
    result = apply_plan(plan)
    assert not result.success
    # Neither page committed
    assert not (paths.wiki_dir() / "concepts" / "food-noise.md").exists()
    assert not (paths.wiki_dir() / "concepts" / "malformed.md").exists()


def test_apply_plan_rejects_uncited_claim_outside_draft(kb_root, make_source):
    _seed_source(kb_root, make_source)
    front = {
        "type": "concept",
        "slug": "uncited-test",
        "canonical_name": "Uncited",
        "domains": ["d-apply"],
    }
    body = (
        "# Uncited\n\n"
        "## Summary\n\nThis is a long uncited claim that has no citation anywhere on the page.\n\n"
        "## Key claims\n\n- [[sources/x]]\n\n"
        "## Sources\n\n- [[sources/x]]\n\n"
        "## Related\n\n- [[concepts/y]]\n"
    )
    plan = Plan(
        source_id="yt-applyTest1A",
        updates=[
            WikiUpdate(
                target_path="wiki/concepts/uncited-test.md",
                update_kind="create",
                content=fm.serialize(front, body),
            )
        ],
    )
    result = apply_plan(plan)
    assert not result.success
    assert any("citation-grounding" in e for e in result.errors)


def test_apply_plan_accepts_uncited_in_draft(kb_root, make_source):
    _seed_source(kb_root, make_source)
    front = {
        "type": "concept",
        "slug": "draft-test",
        "canonical_name": "Draft",
        "domains": ["d-apply"],
    }
    body = (
        "# Draft\n\n"
        "## Summary\n\nThis is a long uncited claim that will be filled in later.\n\n"
        "## Key claims\n\n- [[sources/yt-applyTest1A]]\n\n"
        "## Sources\n\n- [[sources/yt-applyTest1A]]\n\n"
        "## Related\n\n- [[concepts/y]]\n"
    )
    plan = Plan(
        source_id="yt-applyTest1A",
        updates=[
            WikiUpdate(
                target_path="wiki/concepts/draft-test.md",
                update_kind="create",
                content=fm.serialize(front, body),
            )
        ],
    )
    result = apply_plan(plan, draft=True)
    assert result.success, result.errors

    page = paths.wiki_dir() / "concepts" / "draft-test.md"
    assert page.exists()
    page_front, _ = fm.parse(page.read_text())
    assert page_front.get("draft") is True
    assert "draft_started_at" in page_front
    assert page_front.get("draft_unresolved_claims", 0) > 0


def test_apply_plan_rejects_source_page_target(kb_root, make_source):
    _seed_source(kb_root, make_source)
    plan = Plan(
        source_id="yt-applyTest1A",
        updates=[
            WikiUpdate(
                target_path="wiki/sources/yt-applyTest1A.md",
                update_kind="update",
                content="anything",
            )
        ],
    )
    result = apply_plan(plan)
    assert not result.success
    assert any("managed by the gateway directly" in e for e in result.errors)


def test_apply_plan_rejects_path_outside_wiki(kb_root, make_source):
    _seed_source(kb_root, make_source)
    plan = Plan(
        source_id="yt-applyTest1A",
        updates=[
            WikiUpdate(
                target_path="raw/youtube/yt-x.md",
                update_kind="create",
                content="anything",
            )
        ],
    )
    result = apply_plan(plan)
    assert not result.success
    assert any("not under a known wiki page-type directory" in e for e in result.errors)


def test_apply_plan_populates_authorship_report(kb_root, make_source):
    _seed_source(kb_root, make_source)
    plan = Plan(
        source_id="yt-applyTest1A",
        rationale="test report",
        updates=[
            _make_concept_update("report-concept-a", "yt-applyTest1A", kind="create"),
        ],
        contradictions=[
            Contradiction(
                existing_page="wiki/concepts/old-thing.md",
                existing_claim="Old claim here",
                new_claim="New conflicting claim",
                source_id="yt-applyTest1A",
                severity="major",
            ),
        ],
    )
    result = apply_plan(plan)
    assert result.success, result.errors
    assert result.authorship_report is not None
    assert "wiki/concepts/report-concept-a.md" in result.authorship_report.pages_created
    assert len(result.authorship_report.contradictions) == 1
    assert result.authorship_report.contradictions[0].severity == "major"


def test_apply_plan_report_distinguishes_create_and_update(kb_root, make_source):
    _seed_source(kb_root, make_source)
    # First, create the page
    plan1 = Plan(
        source_id="yt-applyTest1A",
        updates=[_make_concept_update("evolving-concept", "yt-applyTest1A", kind="create")],
    )
    result1 = apply_plan(plan1)
    assert result1.success

    # Now update it
    plan2 = Plan(
        source_id="yt-applyTest1A",
        updates=[_make_concept_update("evolving-concept", "yt-applyTest1A", kind="update")],
    )
    result2 = apply_plan(plan2)
    assert result2.success
    assert result2.authorship_report is not None
    assert "wiki/concepts/evolving-concept.md" in result2.authorship_report.pages_updated
    assert result2.authorship_report.pages_created == []


# --- finalize --------------------------------------------------------------


def test_finalize_promotes_draft_when_citations_resolve(kb_root, make_source):
    _seed_source(kb_root, make_source)
    front = {
        "type": "concept",
        "slug": "fin-1",
        "canonical_name": "Fin",
        "domains": ["d-apply"],
        "draft": True,
        "draft_started_at": "2026-04-28T00:00:00Z",
    }
    body_uncited = (
        "# Fin\n\n"
        "## Summary\n\nA long uncited claim without any source link inline yet.\n\n"
        "## Key claims\n\n- [[sources/yt-applyTest1A]]\n\n"
        "## Sources\n\n- [[sources/yt-applyTest1A]]\n\n"
        "## Related\n\n- [[concepts/y]]\n"
    )
    page_path = paths.wiki_dir() / "concepts" / "fin-1.md"
    page_path.parent.mkdir(parents=True, exist_ok=True)
    page_path.write_text(fm.serialize(front, body_uncited))

    # Finalize should fail while citation is missing
    result = finalize(page_path)
    assert not result.success
    assert any("citation grounding" in e for e in result.errors)

    # Add the citation, retry
    body_cited = body_uncited.replace(
        "A long uncited claim without any source link inline yet.",
        "A long claim with a proper citation now [[sources/yt-applyTest1A]].",
    )
    page_path.write_text(fm.serialize(front, body_cited))

    result = finalize(page_path)
    assert result.success, result.errors

    final_front, _ = fm.parse(page_path.read_text())
    assert "draft" not in final_front
    assert "draft_started_at" not in final_front
    assert "finalized_at" in final_front


def test_finalize_abandon_deletes_and_clears_backlinks(kb_root, make_source):
    raw_path = _seed_source(kb_root, make_source)
    raw_front, raw_body = fm.parse(raw_path.read_text())
    raw_front["wiki_pages"] = ["wiki/concepts/abandon-me.md"]
    raw_path.write_text(fm.serialize(raw_front, raw_body))

    page_path = paths.wiki_dir() / "concepts" / "abandon-me.md"
    page_path.parent.mkdir(parents=True, exist_ok=True)
    page_path.write_text(fm.serialize({"type": "concept", "draft": True}, "stub"))

    result = finalize(page_path, abandon=True)
    assert result.success
    assert not page_path.exists()

    # Backlink cleared from source
    raw_front, _ = fm.parse(raw_path.read_text())
    assert "wiki/concepts/abandon-me.md" not in (raw_front.get("wiki_pages") or [])


def test_finalize_rejects_non_draft_page(kb_root):
    page_path = paths.wiki_dir() / "concepts" / "non-draft.md"
    page_path.parent.mkdir(parents=True, exist_ok=True)
    page_path.write_text(fm.serialize({"type": "concept"}, "## Summary\n\nx\n"))
    result = finalize(page_path)
    assert not result.success
    assert any("not a draft" in e for e in result.errors)


# --- query (with mock plan client) -----------------------------------------


class StubPlanClient:
    def __init__(self, response: str):
        self.response = response
        self.last_prompt: str | None = None

    def call(self, prompt: str) -> str:
        self.last_prompt = prompt
        return self.response


def _seed_concept_page(slug: str, *, domain: str, claim_keyword: str = "dose"):
    front = {
        "type": "concept",
        "slug": slug,
        "canonical_name": slug.replace("-", " "),
        "domains": [domain],
    }
    body = (
        f"# {slug}\n\n"
        f"## Summary\n\nThis page describes {claim_keyword} response in detail [[sources/yt-x]].\n\n"
        f"## Key claims\n\n- {claim_keyword}-related effect [[sources/yt-x]].\n\n"
        f"## Sources\n\n- [[sources/yt-x]]\n\n"
        f"## Related\n\n- [[concepts/related]]\n"
    )
    page = paths.wiki_dir() / "concepts" / f"{slug}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(fm.serialize(front, body))


def test_query_files_synthesis_via_notebooklm(kb_root, make_source):
    # The rebuilt query op asks the persistent NotebookLM corpus and
    # files the answer; the old plan-client-driven path is gone.
    from gateway import nlm_registry
    raw = paths.raw_source_path("youtube", "yt-x")
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(make_source(id_="yt-x", domains=["d-q"]))

    nlm_registry.register("d-q", "nb-test-1")

    # Seed source-map cache so [[sources/yt-x]] resolves.
    cache_dir = paths.knowledge_root() / "nlm" / "source_maps"
    cache_dir.mkdir(parents=True, exist_ok=True)
    import json as _json
    (cache_dir / "nb-test-1.json").write_text(
        _json.dumps({"nlm-1": "raw/youtube/yt-x"})
    )

    class _Stub:
        def notebook_query(self, notebook_id, question):
            return {
                "answer": "Dose response is a documented effect [1].",
                "citations": {1: "nlm-1"},
                "sources_used": ["nlm-1"],
            }

    result = query(
        "What is the dose response?", domain="d-q", nlm_client=_Stub()
    )
    assert result.success, result.errors
    pages = list((paths.wiki_dir() / "synthesis").glob("*-what-is-the-dose-response.md"))
    assert pages, "expected a synthesis page"


def test_query_without_notebook_errors(kb_root):
    # No persistent notebook for 'undefined' → error pointing at `wiki research`.
    result = query("anything", domain="undefined")
    assert not result.success
    joined = " ".join(result.errors)
    assert "no notebook" in joined
    assert "wiki research" in joined


# --- ingest --with-plan integration ----------------------------------------


def test_ingest_with_plan_invokes_client_and_applies(kb_root, make_source, tmp_path):
    # No domain → filter skipped, wiki written (low-stakes path), plan runs.
    text = make_source(id_="yt-ingPlanXYZ_AB", domains=[])
    src = tmp_path / "in.md"
    src.write_text(text)

    update_content = fm.serialize(
        {
            "type": "concept",
            "slug": "new-from-plan",
            "canonical_name": "New from plan",
            "domains": ["any-domain"],
        },
        (
            "# New from plan\n\n"
            "## Summary\n\nA freshly minted concept from the plan call [[sources/yt-ingPlanXYZ_AB]].\n\n"
            "## Key claims\n\n- Distinct mechanism [[sources/yt-ingPlanXYZ_AB]].\n\n"
            "## Sources\n\n- [[sources/yt-ingPlanXYZ_AB]]\n\n"
            "## Related\n\n- [[concepts/related]]\n"
        ),
    )

    import json as _json
    plan_response = _json.dumps({
        "source_id": "yt-ingPlanXYZ_AB",
        "rationale": "stub",
        "updates": [{
            "target_path": "wiki/concepts/new-from-plan.md",
            "update_kind": "create",
            "content": update_content,
        }],
    })

    client = StubPlanClient(response=plan_response)
    result = ingest(src, with_plan=True, plan_client=client)
    assert result.success, result.errors
    # Authorship summary appended
    assert "authorship" in result.summary.lower()

    page = paths.wiki_dir() / "concepts" / "new-from-plan.md"
    assert page.exists()


def test_ingest_with_plan_failure_still_commits_source(kb_root, make_source, tmp_path):
    text = make_source(id_="yt-ingPlanFailX_AB", domains=[])
    src = tmp_path / "in.md"
    src.write_text(text)

    client = StubPlanClient(response="not even json")
    result = ingest(src, with_plan=True, plan_client=client)
    assert result.success
    # source page committed despite plan failure
    assert paths.wiki_source_path("yt-ingPlanFailX_AB").exists()
    assert any("authorship failed" in w for w in result.warnings)
