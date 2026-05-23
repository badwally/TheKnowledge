"""Tests for the citation-chain rendering fix (M46-followup #2 / Fix D).

Bug: NotebookLM's synthesis prompts ask it to produce inline `[N]`
citations *and* `[^N]: [[sources/<id>]]` footnote definitions. NLM doesn't
know the gateway's real `wiki/sources/<slug>` slugs, so it substitutes
the citation number itself (or the NLM source UUID) — producing broken
`[[sources/1]]`, `[[sources/2]]` etc. wikilinks. The orchestrator's own
`_render_finding_block` then **appends** correctly-resolved
`[^N]: [[sources/<slug>]]` footnotes on top, so the synthesis page ends
up with two parallel footnote blocks — one broken, one correct.

Fix: strip any pre-existing `[^N]: [[sources/...]]` footnote-definition
lines from the answer body before appending the orchestrator's resolved
set. The orchestrator's resolved set is authoritative.
"""

from __future__ import annotations

from gateway.research import orchestrator as orch


def test_render_finding_strips_nlm_emitted_footnote_definitions():
    """When the NotebookLM answer body already contains `[^N]: [[sources/X]]`
    footnote-definition lines (with integer or NLM-id slugs), the renderer
    must strip them before appending the orchestrator's resolved set —
    otherwise the page ends up with two parallel footnote blocks."""
    finding = {
        "answer": (
            "The substrate-first AI stack lets one operator replace a "
            "60-person team [1]. Lovable reached $50M ARR with under 30 "
            "engineers [2].\n\n"
            "[^1]: [[sources/1]]\n"
            "[^2]: [[sources/2]]\n"
        ),
        "citations": {
            1: "nlm-uuid-aaaa",
            2: "nlm-uuid-bbbb",
        },
    }
    source_map = {
        "nlm-uuid-aaaa": "raw/web/web-2026-04-23-e4c",
        "nlm-uuid-bbbb": "raw/web/web-2025-10-04-aae",
    }

    rendered = orch._render_finding_block(finding, source_map)

    # Broken integer-slug footnotes must be gone
    assert "[[sources/1]]" not in rendered
    assert "[[sources/2]]" not in rendered
    # Resolved slug-form footnotes must be present
    assert "[[sources/web-2026-04-23-e4c]]" in rendered
    assert "[[sources/web-2025-10-04-aae]]" in rendered


def test_render_finding_strips_nlm_emitted_nlm_id_footnotes_too():
    """NotebookLM sometimes emits `[^N]: [[sources/<nlm-uuid>]]` (the raw
    NLM source UUID as the slug). Those are also broken — wiki/sources
    uses gateway-side slugs, not NLM UUIDs. Strip these too."""
    finding = {
        "answer": (
            "Mercor's AI labs wedge is the canonical data-flywheel play [1].\n\n"
            "[^1]: [[sources/nlm-uuid-aaaa]]\n"
        ),
        "citations": {1: "nlm-uuid-aaaa"},
    }
    source_map = {"nlm-uuid-aaaa": "raw/web/web-2026-04-23-e4c"}

    rendered = orch._render_finding_block(finding, source_map)

    assert "[[sources/nlm-uuid-aaaa]]" not in rendered
    assert "[[sources/web-2026-04-23-e4c]]" in rendered


def test_render_finding_strips_nlm_footnotes_only_keeps_other_lines():
    """The strip pass must be surgical — only `[^N]: [[sources/...]]` lines
    go. Body prose, bullet lines, and `## Section` headings stay."""
    finding = {
        "answer": (
            "## Specifics\n"
            "\n"
            "Solo operator + many agents replaces small-team org [1].\n"
            "- Decagon charges per-resolution rather than per-seat [2].\n"
            "- Gamma's player-coach model has leaders building [3].\n"
            "\n"
            "[^1]: [[sources/1]]\n"
            "[^2]: [[sources/2]]\n"
            "[^3]: [[sources/3]]\n"
        ),
        "citations": {
            1: "nlm-aaa",
            2: "nlm-bbb",
            3: "nlm-ccc",
        },
    }
    source_map = {
        "nlm-aaa": "raw/web/web-2026-04-23-e4c",
        "nlm-bbb": "raw/web/web-2025-02-14-794",
        "nlm-ccc": "raw/web/web-2026-04-10-562",
    }

    rendered = orch._render_finding_block(finding, source_map)

    # Body prose preserved
    assert "## Specifics" in rendered
    assert "Solo operator + many agents" in rendered
    assert "Decagon charges per-resolution" in rendered
    assert "Gamma's player-coach model" in rendered
    # No broken integer-slug refs
    for n in (1, 2, 3):
        assert f"[[sources/{n}]]" not in rendered
    # Resolved refs present
    assert "[[sources/web-2026-04-23-e4c]]" in rendered
    assert "[[sources/web-2025-02-14-794]]" in rendered
    assert "[[sources/web-2026-04-10-562]]" in rendered


def test_render_finding_preserves_unresolved_nlm_fallback():
    """If a citation has no source-map entry, the orchestrator emits
    `[[nlm:<id>]]` as a deliberate broken wikilink (per source_map docstring).
    That fallback must survive the post-process pass."""
    finding = {
        "answer": "One claim cited [1] in the corpus.\n",
        "citations": {1: "nlm-uuid-no-mapping"},
    }
    source_map = {}  # nothing resolves

    rendered = orch._render_finding_block(finding, source_map)

    assert "[[nlm:nlm-uuid-no-mapping]]" in rendered


def test_render_finding_no_footnotes_in_input_still_appends_resolved():
    """If NLM behaves and doesn't emit any footnote defs, the resolved
    set must still be appended (this is the existing happy path; the
    fix must not break it)."""
    finding = {
        "answer": "A single claim [1].",
        "citations": {1: "nlm-uuid-aaaa"},
    }
    source_map = {"nlm-uuid-aaaa": "raw/web/web-2026-04-23-e4c"}

    rendered = orch._render_finding_block(finding, source_map)

    assert "[[sources/web-2026-04-23-e4c]]" in rendered
