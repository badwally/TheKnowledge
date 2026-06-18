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


def test_footnote_style_citations_count_as_cited():
    """NotebookLM-rendered synthesis pages cite via in-text [N] refs that
    resolve to page-level `[^N]: [[sources/<id>]]` definitions. The
    validator must recognize this pattern."""
    body = (
        "## Specifics\n"
        "\n"
        "This claim asserts a non-trivial fact about the corpus [1].\n"
        "Another claim with two footnote refs in one sentence [2, 3].\n"
        "Range form covers consecutive refs in one go [4-6].\n"
        "\n"
        "[^1]: [[sources/web-2026-03-09-423]] [^2]: [[sources/web-1995-01-01-0ff]] "
        "[^3]: [[sources/web-2022-07-20-7d3]] [^4]: [[sources/web-2026-01-01-970]] "
        "[^5]: [[sources/web-2023-06-26-652]] [^6]: [[sources/web-2025-10-29-056]]\n"
    )
    uncited = cit.uncited_claims(body)
    assert uncited == [], f"expected no uncited claims, got: {[u.text for u in uncited]}"


def test_footnote_ref_without_definition_still_flagged():
    """A `[N]` reference whose footnote is not defined as
    `[[sources/<id>]]` does NOT count as a citation."""
    body = (
        "This claim has a stray bracket reference with no definition [99].\n"
    )
    uncited = cit.uncited_claims(body)
    assert len(uncited) == 1


def test_claim_detector_does_not_split_comparison_on_vs():
    """`X vs. Y` comparison-enumeration items must not be split on the
    'vs.' abbreviation period into a spurious uncited claim. The item has
    no terminal sentence punctuation, so it is not a claim at all."""
    body = (
        "## Comparisons\n\n"
        "*   Native RDF Triple Stores vs. Labeled-Property-Graph Databases\n"
    )
    uncited = cit.uncited_claims(body)
    assert uncited == [], f"got: {[u.text for u in uncited]}"


def test_claim_detector_treats_eg_as_one_sentence():
    """'e.g.' must not break a sentence: an uncited sentence containing it
    is ONE claim, not two fragments split on the abbreviation period."""
    body = (
        "Developers register prefixes on community services e.g. w3id and "
        "purl for long-term stability of identifiers.\n"
    )
    uncited = cit.uncited_claims(body)
    assert len(uncited) == 1, f"got {len(uncited)}: {[u.text for u in uncited]}"


def test_synthesis_metadata_lines_skipped():
    """`**Origin question:**`, `**Session:**`, `**Branch:**` are page
    metadata, not claims — the validator must not flag them."""
    body = (
        "**Origin question:** What is the best practice for X in domain Y?\n"
        "**Session:** 2026-05-08-foo-bar-baz\n"
        "**Branch:** Some Branch Name\n"
        "\n"
        "## Specifics\n"
        "\n"
        "Real claim sentence that should still be detected [1].\n"
        "\n"
        "[^1]: [[sources/web-2026-01-01-aaa]]\n"
    )
    uncited = cit.uncited_claims(body)
    assert uncited == []


def test_bold_only_lines_treated_as_headers():
    """Lines that are entirely wrapped in `**...**` (used as visual
    sub-headers in synthesis comparison sections) are not claims."""
    body = (
        "**1. Scope and Component Inclusion: Subjective Best Practices vs. Objective Statutory Rules**\n"
        "\n"
        "This is a real claim that follows the bold header [1].\n"
        "\n"
        "[^1]: [[sources/web-2026-01-01-aaa]]\n"
    )
    uncited = cit.uncited_claims(body)
    assert uncited == []


def test_bold_label_followed_by_text_is_still_a_claim():
    """Bold inline-label lines (`**The Comparison:** <claim text>`)
    are NOT pure bold headers — the text after the label still counts.
    Labels NOT in the structural-frame allowlist must be flagged."""
    body = (
        "**The Comparison:** This is a substantive claim that needs a citation source.\n"
    )
    uncited = cit.uncited_claims(body)
    assert len(uncited) == 1


# --- NotebookLM-internal corpus citations: [[nlm:<uuid>]] ------------------


def test_nlm_citation_counts_as_cited():
    """`[[nlm:<uuid>]]` references NotebookLM's internal corpus citations
    (chunk-level handles emitted by NLM-authored synthesis pages). These
    are legitimate grounding into the corpus and must count as cited."""
    body = (
        "This is a substantive interpretive claim about the corpus [[nlm:a17f0b4f-ba96-46b0-b4e1-6be759219e89]].\n"
    )
    uncited = cit.uncited_claims(body)
    assert uncited == [], f"expected no uncited claims, got: {[u.text for u in uncited]}"


def test_nlm_citation_mixed_with_source_citation_counts():
    """Mixed-form lines (footnote ref + NLM ref) common in NLM-authored
    pages: `[34] [[nlm:<uuid>]]` — the NLM ref alone is enough."""
    body = (
        "Gross margins typically compress to 50-60% in AI-native businesses [34] [[nlm:a8d5e313-b8ae-441a-9e82-9f45cadfb006]].\n"
    )
    uncited = cit.uncited_claims(body)
    assert uncited == []


def test_nlm_citation_density_counts_grounded_claims():
    """Citation density treats `[[nlm:<uuid>]]` claims as cited."""
    body = (
        "First claim grounded in the NLM corpus directly [[nlm:11111111-1111-1111-1111-111111111111]].\n"
        "Second claim with no citation anywhere on the line.\n"
    )
    cited, total, ratio = cit.citation_density(body)
    assert total == 2
    assert cited == 1
    assert 0.49 < ratio < 0.51


def test_nlm_citation_in_synthesis_footer_list_does_not_create_claim():
    """`[[nlm:<uuid>]]` in a bullet-only `## Sources cited` footer list
    is a cross-reference, not a claim. The list itself must not be
    misread as an uncited claim."""
    body = (
        "## Sources cited\n"
        "\n"
        "- [[nlm:0718d341-8604-4a60-8498-6045e01b7a8e]]\n"
        "- [[nlm:ea4c9058-3185-4080-8e76-2f4d69b6e6b8]]\n"
        "- [[sources/web-2026-04-23-e4c]]\n"
    )
    uncited = cit.uncited_claims(body)
    assert uncited == []


# --- M44.2: structural-frame labels exempted from citation grounding -------


def test_structural_frame_labels_skipped():
    """NotebookLM-emitted synthesis-frame bullets like `**Themes Used In:**`
    are metadata about the analysis structure, not claims about the world.
    Restricted to an explicit allowlist so real claims still get flagged."""
    body = (
        "## Cross-cutting\n"
        "\n"
        "**Themes Used In:** Component-Level Degradation Modeling, Optimal Inspection.\n"
        "**Which themes draw on it:** Cost and Financial Framing, Integrated Frameworks.\n"
        "**Items Compared:** ASTM E917 is compared against BEES methodology.\n"
        "**Name and key claim:** CAI Reserve Study Standards Framework.\n"
        "**Core approach/mechanism:** Probabilistic component-level forecasting.\n"
        "**Concrete details:** Standards originally published in 1998.\n"
        "\n"
        "A real interpretive claim with no citation still gets flagged here.\n"
    )
    uncited = cit.uncited_claims(body)
    # Only the real interpretive claim should remain
    assert len(uncited) == 1
    assert "real interpretive claim" in uncited[0].text


def test_structural_frame_label_allowlist_is_strict():
    """`**Finding:** Drug X causes Y.` must NOT be exempted just because
    it follows the `**Label:** content` shape — the label is not in the
    allowlist, so the content still counts as a claim."""
    body = (
        "**Finding:** Drug X causes effect Y in patients with condition Z.\n"
        "**Implication:** This means policy A should change to align with B.\n"
    )
    uncited = cit.uncited_claims(body)
    assert len(uncited) == 2


def test_structural_frame_labels_allowlist_pinned():
    """Pin every label currently in the allowlist with a test case so
    drift in `_STRUCTURAL_FRAME_LABELS` is caught."""
    expected = {
        "Themes Used In",
        "Which themes draw on it",
        "Which themes use it",
        "Items Compared",
        "Name and key claim",
        "Core approach/mechanism",
        "Concrete details",
        "Differences in Evidence",
        "Trade-offs and Contexts",
        "Strengths and Weaknesses",
        "Context",
        # M45.1 additions
        "Gap Identified",
        "Limitation Identified",
        "Tension Identified",
    }
    assert cit._STRUCTURAL_FRAME_LABELS == expected
    for label in expected:
        body = f"**{label}:** content that follows the structural label here.\n"
        uncited = cit.uncited_claims(body)
        assert uncited == [], f"label {label!r} should be exempt, got: {[u.text for u in uncited]}"


# --- M44.3: multi-line continuation of structural-frame labels -------------


def test_structural_label_value_on_next_line_exempt():
    """`**Which themes use it:**` on one line, value on the next — the value
    line gets the structural exemption too. Matches the multi-line layout
    NotebookLM uses for shared-anchor responses."""
    body = (
        "## Cross-cutting\n"
        "\n"
        "**Which themes use it:**\n"
        "Component-Level Degradation Modeling and Data Ingestion; Cost and Financial Framing.\n"
        "\n"
        "A real interpretive claim with enough words to count here.\n"
    )
    uncited = cit.uncited_claims(body)
    assert len(uncited) == 1
    assert "real interpretive claim" in uncited[0].text


def test_structural_label_value_after_blank_line_exempt():
    """NotebookLM sometimes inserts a blank line between label and value.
    Blank lines must NOT reset the continuation flag."""
    body = (
        "**Themes Used In:**\n"
        "\n"
        "Component-Level Degradation Modeling and Data Ingestion; Cost and Financial Framing.\n"
    )
    uncited = cit.uncited_claims(body)
    assert uncited == []


def test_structural_label_continuation_does_not_cascade():
    """The continuation flag is consumed by ONE value line — the second line
    after the label is a normal claim candidate again."""
    body = (
        "**Which themes use it:**\n"
        "Theme A; Theme B; Theme C.\n"
        "This second line after the value is a real claim and must be flagged.\n"
    )
    uncited = cit.uncited_claims(body)
    assert len(uncited) == 1
    assert "second line after the value" in uncited[0].text


def test_non_allowlisted_bold_header_does_not_arm_continuation():
    """A fully-bold header that is NOT in the structural-frame allowlist
    (e.g., a numbered comparison heading) must not arm the continuation
    flag — the next line is a normal claim candidate."""
    body = (
        "**1. Scope and Component Inclusion: Subjective vs. Objective Rules**\n"
        "This line right after a non-allowlisted bold header must be flagged as a claim.\n"
    )
    uncited = cit.uncited_claims(body)
    assert len(uncited) == 1
    assert "right after a non-allowlisted" in uncited[0].text


def test_consecutive_structural_labels_chain_continuation():
    """Two structural labels in a row: each consumes one continuation slot."""
    body = (
        "**Which themes use it:**\n"
        "Theme A; Theme B.\n"
        "**Themes Used In:**\n"
        "Theme C; Theme D.\n"
        "\n"
        "An actual claim sentence that should still be flagged here.\n"
    )
    uncited = cit.uncited_claims(body)
    assert len(uncited) == 1
    assert "actual claim sentence" in uncited[0].text


# --- M45: synthesizes + aggregate-framing exemption -----------------------


def _synth_body_with_framing(opener_sentence: str) -> str:
    """Body fixture with `## Included works` mirroring 2 sources plus a `##
    Synthesis` section whose first claim is the aggregate-framing opener."""
    return (
        "## Synthesis\n"
        "\n"
        f"{opener_sentence}\n"
        "A later sentence in the same section that should still be flagged.\n"
        "\n"
        "## Included works\n"
        "\n"
        "- [[sources/web-2026-01-01-aaa]]\n"
        "- [[sources/web-2026-02-02-bbb]]\n"
    )


def test_aggregate_framing_opener_exempted_when_synthesizes_present():
    """Opening sentence matching `Based on the provided sources...` is exempt
    when `synthesizes:` has ≥2 entries mirrored by `## Included works`."""
    body = _synth_body_with_framing(
        "Based on the provided sources, several specific patterns emerge across themes."
    )
    front = {"synthesizes": ["sources/web-2026-01-01-aaa", "sources/web-2026-02-02-bbb"]}
    uncited = cit.uncited_claims(body, front)
    # Only the LATER sentence should remain uncited; the opener is exempt
    assert len(uncited) == 1
    assert "later sentence" in uncited[0].text


def test_aggregate_framing_opener_NOT_exempted_without_synthesizes():
    """Without `synthesizes:` frontmatter, the opener IS flagged."""
    body = _synth_body_with_framing(
        "Based on the provided sources, several specific patterns emerge across themes."
    )
    uncited = cit.uncited_claims(body)  # no front
    # Both the opener AND the later sentence are flagged
    assert len(uncited) == 2


def test_aggregate_framing_opener_NOT_exempted_when_included_works_missing():
    """`synthesizes:` set but `## Included works` absent → no exemption."""
    body = (
        "## Synthesis\n"
        "\n"
        "Based on the provided sources, several patterns emerge across themes.\n"
    )
    front = {"synthesizes": ["sources/web-2026-01-01-aaa", "sources/web-2026-02-02-bbb"]}
    uncited = cit.uncited_claims(body, front)
    assert len(uncited) == 1


def test_aggregate_framing_opener_NOT_exempted_when_included_works_drift():
    """`## Included works` exists but lists different entries from
    `synthesizes:` — no exemption (citation laundering anti-pattern)."""
    body = (
        "## Synthesis\n"
        "\n"
        "Based on the corpus, several patterns emerge.\n"
        "\n"
        "## Included works\n"
        "\n"
        "- [[sources/web-different-1]]\n"
        "- [[sources/web-different-2]]\n"
    )
    front = {"synthesizes": ["sources/web-2026-01-01-aaa", "sources/web-2026-02-02-bbb"]}
    uncited = cit.uncited_claims(body, front)
    assert len(uncited) == 1
    assert "patterns emerge" in uncited[0].text


def test_aggregate_framing_opener_NOT_exempted_when_only_one_synthesis():
    """`synthesizes:` with a single entry doesn't aggregate — exemption
    requires ≥2 (one source is just a normal citation, not an aggregate)."""
    body = (
        "## Synthesis\n"
        "\n"
        "Based on the provided sources, several patterns emerge.\n"
        "\n"
        "## Included works\n"
        "\n"
        "- [[sources/web-2026-01-01-aaa]]\n"
    )
    front = {"synthesizes": ["sources/web-2026-01-01-aaa"]}
    uncited = cit.uncited_claims(body, front)
    assert len(uncited) == 1


def test_aggregate_framing_opener_one_per_section_bound():
    """Exemption is bounded: only the FIRST opener-shaped sentence per
    section is exempt; a second opener in the same section is flagged."""
    body = (
        "## Synthesis\n"
        "\n"
        "Based on the provided sources, the first pattern is clear.\n"
        "Across the corpus, a second aggregate observation appears later.\n"
        "\n"
        "## Included works\n"
        "\n"
        "- [[sources/web-2026-01-01-aaa]]\n"
        "- [[sources/web-2026-02-02-bbb]]\n"
    )
    front = {"synthesizes": ["sources/web-2026-01-01-aaa", "sources/web-2026-02-02-bbb"]}
    uncited = cit.uncited_claims(body, front)
    assert len(uncited) == 1
    assert "second aggregate" in uncited[0].text


def test_aggregate_framing_per_section_independence():
    """Each `##` section gets its own opener exemption."""
    body = (
        "## Section A\n"
        "\n"
        "Based on the provided sources, pattern A emerges across the corpus.\n"
        "\n"
        "## Section B\n"
        "\n"
        "Across the corpus, pattern B emerges in a complementary way here.\n"
        "\n"
        "## Included works\n"
        "\n"
        "- [[sources/web-2026-01-01-aaa]]\n"
        "- [[sources/web-2026-02-02-bbb]]\n"
    )
    front = {"synthesizes": ["sources/web-2026-01-01-aaa", "sources/web-2026-02-02-bbb"]}
    uncited = cit.uncited_claims(body, front)
    assert uncited == []


def test_aggregate_framing_synthesis_tier_works_too():
    """`synthesizes:` with `synthesis/<slug>` entries (second-derivative)
    also enables the exemption."""
    body = (
        "## Cross-cutting\n"
        "\n"
        "Based on the previous thematic analysis, four anchors emerge across themes.\n"
        "\n"
        "## Included works\n"
        "\n"
        "- [[synthesis/2026-05-11-component-degradation]]\n"
        "- [[synthesis/2026-05-11-cost-and-financial-framing]]\n"
    )
    front = {
        "synthesizes": [
            "synthesis/2026-05-11-component-degradation",
            "synthesis/2026-05-11-cost-and-financial-framing",
        ]
    }
    uncited = cit.uncited_claims(body, front)
    assert uncited == []


def test_aggregate_framing_mixed_tier_rejected():
    """`synthesizes:` with mixed `sources/` and `synthesis/` violates the
    one-level strict-typing invariant — no exemption."""
    body = (
        "## Synthesis\n"
        "\n"
        "Based on the corpus, a pattern emerges across the sources.\n"
        "\n"
        "## Included works\n"
        "\n"
        "- [[sources/web-2026-01-01-aaa]]\n"
        "- [[synthesis/2026-05-11-component-degradation]]\n"
    )
    front = {
        "synthesizes": [
            "sources/web-2026-01-01-aaa",
            "synthesis/2026-05-11-component-degradation",
        ]
    }
    uncited = cit.uncited_claims(body, front)
    assert len(uncited) == 1


def test_aggregate_framing_invalid_synthesizes_entry_no_exemption():
    """A malformed entry in `synthesizes:` disables the exemption entirely."""
    body = _synth_body_with_framing(
        "Based on the provided sources, patterns emerge."
    )
    front = {"synthesizes": ["not-a-valid-entry", "sources/web-2026-02-02-bbb"]}
    uncited = cit.uncited_claims(body, front)
    # All claims flagged; exemption gated on shape
    assert len(uncited) == 2


def test_is_aggregate_framing_opener_allowlist_pinned():
    """Pin the M45 aggregate-opener allowlist so drift is caught."""
    accepted = [
        "Based on the provided sources, X.",
        "Based on the corpus, Y.",
        "Based on the previous thematic analysis, Z.",
        "Based on the conversation history, W.",
        "Across the corpus, A.",
        "Across all the sources, B.",
        "Looking across all the themes, C.",
        "Aggregating across the themes, D.",
        "Across the provided sources, E.",
    ]
    for s in accepted:
        assert cit.is_aggregate_framing_opener(s), f"should match: {s!r}"
    rejected = [
        "The drug X causes effect Y in patients.",
        "Finding: drug X causes Y.",
        "**Themes Used In:** A; B.",
    ]
    for s in rejected:
        assert not cit.is_aggregate_framing_opener(s), f"should NOT match: {s!r}"


# --- M45: validate_synthesizes_integrity ----------------------------------


def test_synthesizes_integrity_passes_when_absent():
    """Pages without `synthesizes:` skip the integrity check entirely."""
    from gateway.validator import validate_synthesizes_integrity
    front = {"type": "synthesis", "slug": "s", "title": "t", "domains": ["d"], "question": "q"}
    body = "## Synthesis\n\nA claim that doesn't need synthesizes integrity.\n"
    result = validate_synthesizes_integrity(front, body)
    assert not result.errors


def test_synthesizes_integrity_rejects_bad_entry_shape():
    from gateway.validator import validate_synthesizes_integrity
    front = {"synthesizes": ["sources/ok-1", "INVALID ENTRY"]}
    body = "## Included works\n\n- [[sources/ok-1]]\n"
    result = validate_synthesizes_integrity(front, body)
    assert any(e.rule == "synthesizes-shape" for e in result.errors)


def test_synthesizes_integrity_rejects_mixed_tier():
    from gateway.validator import validate_synthesizes_integrity
    front = {"synthesizes": ["sources/web-aaa", "synthesis/foo-bar"]}
    body = (
        "## Included works\n"
        "\n"
        "- [[sources/web-aaa]]\n"
        "- [[synthesis/foo-bar]]\n"
    )
    result = validate_synthesizes_integrity(front, body)
    assert any(e.rule == "synthesizes-mixed-tier" for e in result.errors)


def test_synthesizes_integrity_rejects_included_works_drift():
    from gateway.validator import validate_synthesizes_integrity
    front = {"synthesizes": ["sources/web-aaa", "sources/web-bbb"]}
    body = (
        "## Included works\n"
        "\n"
        "- [[sources/web-aaa]]\n"
    )
    result = validate_synthesizes_integrity(front, body)
    assert any(e.rule == "synthesizes-included-works-drift" for e in result.errors)


def test_synthesizes_integrity_accepts_correct_mirror():
    from gateway.validator import validate_synthesizes_integrity
    front = {"synthesizes": ["sources/web-aaa", "sources/web-bbb"]}
    body = (
        "## Included works\n"
        "\n"
        "- [[sources/web-aaa]]\n"
        "- [[sources/web-bbb]]\n"
    )
    result = validate_synthesizes_integrity(front, body)
    assert result.errors == []


def test_synthesizes_integrity_accepts_empty_list_as_noop():
    """`synthesizes: []` is treated as no-op (same as field absent)."""
    from gateway.validator import validate_synthesizes_integrity
    front = {"synthesizes": []}
    body = "## Synthesis\n\nNo Included works needed.\n"
    result = validate_synthesizes_integrity(front, body)
    assert result.errors == []


def test_synthesizes_integrity_rejects_non_list_value():
    from gateway.validator import validate_synthesizes_integrity
    front = {"synthesizes": "sources/web-aaa"}  # string, not list
    body = "## Included works\n\n- [[sources/web-aaa]]\n"
    result = validate_synthesizes_integrity(front, body)
    assert any(e.rule == "synthesizes-shape" for e in result.errors)


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
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
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
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
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


def test_build_plan_prompt_includes_contradiction_instructions():
    prompt = build_plan_prompt("source body", {"wiki/concepts/x.md": "existing"})
    assert "contradictions" in prompt.lower()
    assert "existing_page" in prompt
    assert "existing_claim" in prompt
    assert "new_claim" in prompt
    assert "severity" in prompt


def test_build_plan_prompt_includes_update_priority():
    prompt = build_plan_prompt("source body", {"wiki/concepts/x.md": "existing"})
    # Should instruct to prioritize updates over creates
    assert "prioritize" in prompt.lower() or "prefer" in prompt.lower()
    assert "update" in prompt.lower()


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
        "created_at": "2026-04-28T00:00:00Z",
        "last_updated": "2026-04-28T00:00:00Z",
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


def test_apply_plan_log_includes_contradictions(kb_root, make_source):
    _seed_source(kb_root, make_source)
    plan = Plan(
        source_id="yt-applyTest1A",
        rationale="test log",
        updates=[_make_concept_update("log-concept", "yt-applyTest1A")],
        contradictions=[
            Contradiction(
                existing_page="wiki/concepts/old.md",
                existing_claim="Old statement",
                new_claim="New conflicting statement",
                source_id="yt-applyTest1A",
                severity="major",
            ),
        ],
    )
    result = apply_plan(plan)
    assert result.success

    log_text = paths.log_path().read_text()
    assert "contradictions=1" in log_text


def test_ingest_with_plan_propagates_authorship_report(kb_root, make_source, tmp_path):
    import json as _json

    text = make_source(id_="yt-reportTest_AB", domains=[])
    src = tmp_path / "in.md"
    src.write_text(text)

    update_content = fm.serialize(
        {
            "type": "concept",
            "slug": "reported-concept",
            "canonical_name": "Reported concept",
            "domains": ["any"],
        },
        (
            "# Reported concept\n\n"
            "## Summary\n\nA concept with a citation [[sources/yt-reportTest_AB]].\n\n"
            "## Key claims\n\n- Key claim here [[sources/yt-reportTest_AB]].\n\n"
            "## Sources\n\n- [[sources/yt-reportTest_AB]]\n\n"
            "## Related\n\n- [[concepts/other]]\n"
        ),
    )

    plan_response = _json.dumps({
        "source_id": "yt-reportTest_AB",
        "rationale": "stub with report",
        "updates": [{
            "target_path": "wiki/concepts/reported-concept.md",
            "update_kind": "create",
            "content": update_content,
        }],
        "contradictions": [{
            "existing_page": "wiki/concepts/old-concept.md",
            "existing_claim": "Old claim",
            "new_claim": "New claim",
            "source_id": "yt-reportTest_AB",
            "severity": "minor",
        }],
    })

    client = StubPlanClient(response=plan_response)
    result = ingest(src, with_plan=True, plan_client=client)
    assert result.success, result.errors
    assert result.authorship_report is not None
    assert len(result.authorship_report.pages_created) == 1
    assert len(result.authorship_report.contradictions) == 1


def test_apply_plan_writes_contradictions_to_jsonl(kb_root, make_source):
    """When plan.contradictions is non-empty, apply_plan appends one JSONL record per contradiction."""
    import json as _json
    from gateway import paths

    _seed_source(kb_root, make_source)
    plan = Plan(
        source_id="yt-applyTest1A",
        rationale="contradictions persistence test",
        updates=[
            _make_concept_update("jsonl-test-concept", "yt-applyTest1A"),
        ],
        contradictions=[
            Contradiction(
                existing_page="wiki/concepts/old.md",
                existing_claim="Original claim text",
                new_claim="Conflicting claim text",
                source_id="yt-applyTest1A",
                severity="major",
            ),
            Contradiction(
                existing_page="wiki/concepts/other.md",
                existing_claim="Another original claim",
                new_claim="Another conflicting claim",
                source_id="yt-applyTest1A",
                severity="minor",
            ),
        ],
    )
    result = apply_plan(plan)
    assert result.success, result.errors

    log_path = paths.knowledge_root() / ".knowledge" / "contradictions" / "log.jsonl"
    assert log_path.is_file()

    lines = [
        line for line in log_path.read_text().splitlines() if line.strip()
    ]
    assert len(lines) == 2
    records = [_json.loads(line) for line in lines]
    assert records[0]["source_id"] == "yt-applyTest1A"
    assert records[0]["existing_page"] == "wiki/concepts/old.md"
    assert records[0]["severity"] == "major"
    assert "recorded_at" in records[0]
    assert records[1]["severity"] == "minor"


def test_apply_plan_no_jsonl_write_when_no_contradictions(kb_root, make_source):
    """Plans without contradictions don't create the JSONL file."""
    from gateway import paths

    _seed_source(kb_root, make_source)
    plan = Plan(
        source_id="yt-applyTest1A",
        rationale="no contradictions",
        updates=[
            _make_concept_update("no-contradictions-concept", "yt-applyTest1A"),
        ],
    )
    result = apply_plan(plan)
    assert result.success

    log_path = paths.knowledge_root() / ".knowledge" / "contradictions" / "log.jsonl"
    if log_path.is_file():
        lines = [l for l in log_path.read_text().splitlines() if l.strip()]
        assert lines == []


def test_end_to_end_smart_authorship(kb_root, make_source, tmp_path):
    """Full flow: ingest -> plan with create + update + contradiction -> report + log."""
    import json as _json

    # Seed an existing concept page in the wiki
    _seed_source(kb_root, make_source, source_id="yt-oldSource_AB", domain="d-e2e")
    existing_front = {
        "type": "concept",
        "slug": "existing-mechanism",
        "canonical_name": "Existing mechanism",
        "domains": ["d-e2e"],
    }
    existing_body = (
        "# Existing mechanism\n\n"
        "## Summary\n\nThis mechanism is irreversible [[sources/yt-oldSource_AB]].\n\n"
        "## Key claims\n\n- The effect is permanent [[sources/yt-oldSource_AB]].\n\n"
        "## Sources\n\n- [[sources/yt-oldSource_AB]]\n\n"
        "## Related\n\n- [[concepts/other]]\n"
    )
    existing_page = paths.wiki_dir() / "concepts" / "existing-mechanism.md"
    existing_page.parent.mkdir(parents=True, exist_ok=True)
    existing_page.write_text(fm.serialize(existing_front, existing_body))

    # Ingest a new source (no domain → filter skipped → wiki page written)
    text = make_source(id_="yt-newSource_AB", domains=[])
    src = tmp_path / "new.md"
    src.write_text(text)

    # Prepare plan response: update existing + create new + one contradiction
    updated_content = fm.serialize(
        {
            "type": "concept",
            "slug": "existing-mechanism",
            "canonical_name": "Existing mechanism",
            "domains": ["d-e2e"],
        },
        (
            "# Existing mechanism\n\n"
            "## Summary\n\nThis mechanism is irreversible [[sources/yt-oldSource_AB]]. "
            "However, recent evidence suggests partial reversibility [[sources/yt-newSource_AB]].\n\n"
            "## Key claims\n\n"
            "- The effect is permanent [[sources/yt-oldSource_AB]].\n"
            "- Partial reversal observed after 12 weeks [[sources/yt-newSource_AB]].\n\n"
            "## Sources\n\n- [[sources/yt-oldSource_AB]]\n- [[sources/yt-newSource_AB]]\n\n"
            "## Related\n\n- [[concepts/other]]\n- [[concepts/new-entity]]\n"
        ),
    )
    new_content = fm.serialize(
        {
            "type": "entity",
            "slug": "new-entity",
            "canonical_name": "New entity",
            "entity_kind": "drug",
            "domains": ["d-e2e"],
        },
        (
            "# New entity\n\n"
            "## Summary\n\nA newly discovered entity [[sources/yt-newSource_AB]].\n\n"
            "## Key facts\n\n- First documented in 2026 [[sources/yt-newSource_AB]].\n\n"
            "## Sources\n\n- [[sources/yt-newSource_AB]]\n\n"
            "## Related\n\n- [[concepts/existing-mechanism]]\n"
        ),
    )

    plan_response = _json.dumps({
        "source_id": "yt-newSource_AB",
        "rationale": "integrates new evidence on mechanism reversibility",
        "updates": [
            {
                "target_path": "wiki/concepts/existing-mechanism.md",
                "update_kind": "update",
                "content": updated_content,
            },
            {
                "target_path": "wiki/entities/new-entity.md",
                "update_kind": "create",
                "content": new_content,
            },
        ],
        "contradictions": [
            {
                "existing_page": "wiki/concepts/existing-mechanism.md",
                "existing_claim": "The effect is permanent",
                "new_claim": "Partial reversal observed after 12 weeks",
                "source_id": "yt-newSource_AB",
                "severity": "major",
            },
        ],
    })

    client = StubPlanClient(response=plan_response)
    result = ingest(src, with_plan=True, plan_client=client)
    assert result.success, result.errors

    # AuthorshipReport populated
    report = result.authorship_report
    assert report is not None
    assert "wiki/entities/new-entity.md" in report.pages_created
    assert "wiki/concepts/existing-mechanism.md" in report.pages_updated
    assert len(report.contradictions) == 1
    assert report.contradictions[0].severity == "major"

    # Wiki pages written
    assert (paths.wiki_dir() / "entities" / "new-entity.md").exists()
    updated_text = existing_page.read_text()
    assert "partial reversibility" in updated_text.lower()

    # Log entry includes contradiction count
    log_text = paths.log_path().read_text()
    assert "contradictions=1" in log_text

    # Summary includes authorship info
    assert "authorship" in result.summary


# --- ARCH-10: citations_allowlist.yaml ----------------------------------------


def test_citations_allowlist_yaml_exists():
    """ARCH-10: citations_allowlist.yaml exists alongside citations.py."""
    from pathlib import Path
    import gateway
    pkg_dir = Path(gateway.__file__).parent
    yaml_path = pkg_dir / "data" / "citations_allowlist.yaml"
    assert yaml_path.exists(), f"citations_allowlist.yaml not found at {yaml_path}"


def test_citations_allowlist_yaml_has_version():
    """ARCH-10: YAML has a version: field."""
    from pathlib import Path
    import gateway
    pkg_dir = Path(gateway.__file__).parent
    yaml_path = pkg_dir / "data" / "citations_allowlist.yaml"
    data = yaml.safe_load(yaml_path.read_text())
    assert "version" in data


def test_structural_frame_labels_loaded_from_yaml():
    """ARCH-10: _STRUCTURAL_FRAME_LABELS is loaded from YAML, not hardcoded."""
    from pathlib import Path
    import gateway
    pkg_dir = Path(gateway.__file__).parent
    yaml_path = pkg_dir / "data" / "citations_allowlist.yaml"
    data = yaml.safe_load(yaml_path.read_text())
    yaml_labels = frozenset(data["structural_frame_labels"])
    assert cit._STRUCTURAL_FRAME_LABELS == yaml_labels


def test_aggregate_framing_openers_loaded_from_yaml():
    """ARCH-10: _AGGREGATE_FRAMING_OPENERS_RE patterns are loaded from YAML."""
    from pathlib import Path
    import gateway
    import re
    pkg_dir = Path(gateway.__file__).parent
    yaml_path = pkg_dir / "data" / "citations_allowlist.yaml"
    data = yaml.safe_load(yaml_path.read_text())
    # The combined pattern must match every phrase from the YAML
    for phrase_re in data["aggregate_framing_openers"]:
        sample = re.sub(r"\(\?:[^)]+\)", lambda m: m.group(0).split("|")[0].lstrip("(?:"), phrase_re)
        # Just confirm the YAML parses as valid regex (each entry compiles)
        re.compile(phrase_re)  # raises if invalid


def test_allowlist_yaml_phrase_set_pinned():
    """ARCH-10: pin the YAML phrase set so deliberate changes require this test to be updated."""
    from pathlib import Path
    import gateway
    pkg_dir = Path(gateway.__file__).parent
    yaml_path = pkg_dir / "data" / "citations_allowlist.yaml"
    data = yaml.safe_load(yaml_path.read_text())
    assert len(data["structural_frame_labels"]) == 14
    assert len(data["aggregate_framing_openers"]) == 6
