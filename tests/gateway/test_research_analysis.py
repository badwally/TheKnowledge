"""Tests for `gateway.research.analysis`.

The unit under test is the three-phase analysis pipeline (taxonomy →
investigate → synthesize). The `NlmClient` is mocked at the
`notebook_query` boundary — no subprocess and no real NotebookLM.
"""

from __future__ import annotations

import pytest

from gateway.research import analysis


# --- fake client ------------------------------------------------------------


class FakeClient:
    """Minimal NlmClient stand-in.

    `notebook_query` returns the first response whose key substring
    appears in `question`. Falsy keys (empty string) are skipped so the
    fallback only fires when nothing else matches. Optional
    `raise_when` substrings let a test simulate per-query failures.
    """

    def __init__(
        self,
        responses_by_prompt: dict[str, dict],
        *,
        raise_when: dict[str, Exception] | None = None,
    ):
        self._responses = responses_by_prompt
        self._raise_when = raise_when or {}
        self.calls: list[tuple[str, str]] = []

    def notebook_query(self, notebook_id: str, question: str) -> dict:
        self.calls.append((notebook_id, question))
        for needle, exc in self._raise_when.items():
            if needle and needle in question:
                raise exc
        # Longest needle wins — protects against shorter substrings (like a
        # research-query token threaded into investigation prompts) shadowing
        # more-specific keys (like a branch-name marker).
        for needle, resp in sorted(
            self._responses.items(), key=lambda kv: len(kv[0]), reverse=True
        ):
            if needle and needle in question:
                return resp
        return {"answer": "", "citations": {}, "sources_used": []}


# --- canned responses -------------------------------------------------------


_TAXONOMY_ANSWER_FIVE_BRANCHES = """
AREA: Branch One
DESCRIPTION: First branch description.
  SUB: Sub A
  DESCRIPTION: First sub of branch one.
    METHOD: Method 1A
AREA: Branch Two
DESCRIPTION: Second branch description.
  SUB: Sub B
  DESCRIPTION: First sub of branch two.
    METHOD: Method 2A
AREA: Branch Three
DESCRIPTION: Third branch description.
  SUB: Sub C
  DESCRIPTION: First sub of branch three.
    METHOD: Method 3A
AREA: Branch Four
DESCRIPTION: Fourth branch description.
  SUB: Sub D
  DESCRIPTION: First sub of branch four.
    METHOD: Method 4A
AREA: Branch Five
DESCRIPTION: Fifth branch description.
  SUB: Sub E
  DESCRIPTION: First sub of branch five.
    METHOD: Method 5A
""".strip()


_TAXONOMY_ANSWER_ONE_BRANCH = """
AREA: Only Branch
DESCRIPTION: A single branch.
  SUB: The Sub
  DESCRIPTION: The only sub.
    METHOD: Single Method
""".strip()


def _taxonomy_response(answer: str = _TAXONOMY_ANSWER_FIVE_BRANCHES) -> dict:
    return {
        "answer": answer,
        "citations": {1: "nlm-src-tax-1", 2: "nlm-src-tax-2"},
        "sources_used": ["nlm-src-tax-1", "nlm-src-tax-2"],
    }


def _branch_response(branch_name: str, query_name: str) -> dict:
    return {
        "answer": f"answer for {branch_name} / {query_name}",
        "citations": {1: f"nlm-{branch_name}-{query_name}-cite"},
        "sources_used": [f"nlm-{branch_name}-{query_name}-cite"],
    }


# --- happy path ------------------------------------------------------------


def test_analyze_happy_path_runs_all_three_phases():
    responses = {
        # Phase 1 — taxonomy: anchor on the unique research-query string.
        "compare frobnication": _taxonomy_response(_TAXONOMY_ANSWER_ONE_BRANCH),
        # Phase 2 — investigate the single branch (3 templated queries).
        'for the research area "Only Branch"': _branch_response("Only Branch", "methods"),
        # Phase 3 — synthesis (3 default queries).
        "architectures or techniques appear in multiple sub-fields": {
            "answer": "shared architectures answer",
            "citations": {1: "nlm-shared-1"},
            "sources_used": ["nlm-shared-1"],
        },
        "benchmark datasets are referenced": {
            "answer": "common datasets answer",
            "citations": {1: "nlm-data-1"},
            "sources_used": ["nlm-data-1"],
        },
        "fundamental trade-offs": {
            "answer": "tradeoffs answer",
            "citations": {1: "nlm-trade-1"},
            "sources_used": ["nlm-trade-1"],
        },
    }
    client = FakeClient(responses)

    result = analysis.analyze(
        "nb-1",
        domain="d1",
        research_query="compare frobnication",
        client=client,
    )

    assert result.domain == "d1"
    assert result.research_query == "compare frobnication"
    assert result.notebook_id == "nb-1"
    assert result.errors == []

    # Taxonomy parsed correctly.
    assert result.taxonomy["field"] == "compare frobnication"
    assert len(result.taxonomy["branches"]) == 1
    branch = result.taxonomy["branches"][0]
    assert branch["name"] == "Only Branch"
    assert branch["description"] == "A single branch."
    assert branch["sub_branches"][0]["methods"] == ["Single Method"]

    # Findings — one branch with all three sub-queries.
    assert "Only Branch" in result.findings
    findings = result.findings["Only Branch"]
    assert findings["branch"] == "Only Branch"
    for key in ("methods", "comparisons", "open_problems"):
        assert key in findings, f"missing {key}"
        # All three sub-queries hit the same branch fallback above; "error" must NOT be present.
        assert "error" not in findings[key]

    # Synthesis — all three default queries present, none erroring.
    assert set(result.synthesis.keys()) == {"shared_architectures", "common_datasets", "recurring_tradeoffs"}
    for v in result.synthesis.values():
        assert "error" not in v

    # Call accounting: 1 taxonomy + 3 branch queries + 3 synthesis = 7.
    assert len(client.calls) == 1 + 3 + 3


# --- per-branch error isolation --------------------------------------------


def test_analyze_continues_past_branch_failure():
    """Branch 3's investigation raises; branches 1, 2, 4, 5 still complete and
    `errors` records the failure."""
    responses = {
        "branch failure test": _taxonomy_response(),  # 5 branches
    }
    # The failure must trigger inside `_investigate_branch` itself, not on
    # an individual sub-query (those are caught locally and turn into
    # error-keyed findings without aborting the branch). Easiest way: have
    # the branch dict raise when iterated. We instead simulate this by
    # making one query raise *and* asserting that the whole-branch path
    # continues. To force `_investigate_branch` to raise outright, we
    # patch the templates dict to one that triggers a KeyError on .format().
    # Cleaner: make the FakeClient raise a non-Exception subclass to
    # bypass the inner per-query catch — but `except Exception` catches
    # everything. Instead: monkeypatch `_investigate_branch` for one
    # branch.
    client = FakeClient(responses)

    # Replace `_investigate_branch` with a wrapper that raises for branch 3.
    real = analysis._investigate_branch
    branch_3_name = "Branch Three"

    def maybe_raise(notebook_id, c, branch, templates, *, research_query):
        if branch.get("name") == branch_3_name:
            raise RuntimeError("simulated branch 3 failure")
        return real(notebook_id, c, branch, templates, research_query=research_query)

    # Patch via attribute replacement (module-level function).
    analysis._investigate_branch = maybe_raise  # type: ignore[assignment]
    try:
        result = analysis.analyze(
            "nb-2",
            domain="d2",
            research_query="branch failure test",
            client=client,
        )
    finally:
        analysis._investigate_branch = real  # type: ignore[assignment]

    branch_names = [b["name"] for b in result.taxonomy["branches"]]
    assert branch_names == [
        "Branch One",
        "Branch Two",
        "Branch Three",
        "Branch Four",
        "Branch Five",
    ]

    # All five branches show up in findings.
    assert set(result.findings.keys()) == set(branch_names)

    # Branch 3's findings is the error-only payload.
    assert result.findings[branch_3_name] == {
        "branch": branch_3_name,
        "error": "simulated branch 3 failure",
    }

    # Branches 1, 2, 4, 5 ran their three sub-queries normally.
    for ok in ("Branch One", "Branch Two", "Branch Four", "Branch Five"):
        for key in ("methods", "comparisons", "open_problems"):
            assert key in result.findings[ok]

    # One error recorded, naming the failed branch.
    assert any("Branch Three" in e for e in result.errors)
    assert len([e for e in result.errors if "investigate[" in e]) == 1


# --- per-synthesis-query error isolation -----------------------------------


def test_analyze_continues_past_synthesis_query_failure():
    """One synthesis query raises; the other two still run."""
    responses = {
        "synth failure test": _taxonomy_response(_TAXONOMY_ANSWER_ONE_BRANCH),
        "benchmark datasets are referenced": {
            "answer": "datasets ok",
            "citations": {1: "nlm-d-1"},
            "sources_used": ["nlm-d-1"],
        },
        "fundamental trade-offs": {
            "answer": "tradeoffs ok",
            "citations": {1: "nlm-t-1"},
            "sources_used": ["nlm-t-1"],
        },
    }
    raise_when = {
        "architectures or techniques appear in multiple sub-fields": RuntimeError(
            "shared_architectures down"
        ),
    }
    client = FakeClient(responses, raise_when=raise_when)

    result = analysis.analyze(
        "nb-3",
        domain="d3",
        research_query="synth failure test",
        client=client,
    )

    assert "shared_architectures" in result.synthesis
    assert result.synthesis["shared_architectures"]["error"] == "shared_architectures down"
    assert result.synthesis["shared_architectures"]["answer"] == ""

    # The other two synthesis queries succeeded.
    assert result.synthesis["common_datasets"]["answer"] == "datasets ok"
    assert result.synthesis["recurring_tradeoffs"]["answer"] == "tradeoffs ok"

    # Recorded in errors.
    assert any("synthesis[shared_architectures]" in e for e in result.errors)


# --- custom prompt injection ------------------------------------------------


def test_custom_synthesis_queries_replace_defaults():
    """Pass `custom_synthesis_queries={'only_one': "..."}` and verify
    the synthesis phase makes exactly one call, using that prompt."""
    sentinel_prompt = "ZZZ-UNIQUE-CUSTOM-SYNTH-PROMPT-ZZZ"
    responses = {
        "custom injection test": _taxonomy_response(_TAXONOMY_ANSWER_ONE_BRANCH),
        sentinel_prompt: {
            "answer": "custom synth answer",
            "citations": {1: "nlm-c-1"},
            "sources_used": ["nlm-c-1"],
        },
    }
    client = FakeClient(responses)

    result = analysis.analyze(
        "nb-4",
        domain="d4",
        research_query="custom injection test",
        client=client,
        custom_synthesis_queries={"only_one": sentinel_prompt},
    )

    # Synthesis phase produced exactly one entry.
    assert list(result.synthesis.keys()) == ["only_one"]
    assert result.synthesis["only_one"]["answer"] == "custom synth answer"

    # And exactly one synthesis call hit the client (verify by counting
    # questions equal to the sentinel prompt).
    synth_calls = [q for _nb, q in client.calls if q == sentinel_prompt]
    assert len(synth_calls) == 1

    # None of the default synthesis prompts were called.
    for default_prompt in (
        analysis._SHARED_ARCHITECTURES_PROMPT,
        analysis._COMMON_DATASETS_PROMPT,
        analysis._RECURRING_TRADEOFFS_PROMPT,
    ):
        assert all(default_prompt != q for _nb, q in client.calls)


def test_custom_taxonomy_prompt_used_verbatim_when_no_placeholder():
    """A custom taxonomy prompt without `{research_query}` is sent as-is."""
    custom = "JUST GIVE ME AREAS — no placeholder here."
    responses = {
        "JUST GIVE ME AREAS": _taxonomy_response(_TAXONOMY_ANSWER_ONE_BRANCH),
    }
    client = FakeClient(responses)

    result = analysis.analyze(
        "nb-5",
        domain="d5",
        research_query="anything",
        client=client,
        custom_taxonomy_prompt=custom,
    )

    # First call (phase 1) used the verbatim custom prompt.
    assert client.calls[0][1] == custom
    assert result.errors == []


def test_custom_investigation_templates_extend_defaults():
    """Custom investigation templates merge over defaults, not replace
    wholesale — same semantics as research-notebook's `query_templates.update()`."""
    extra = "MY-VERY-UNIQUE-EXTRA-TEMPLATE-MARKER for {branch_name} / {research_query}"
    responses = {
        "ciq": _taxonomy_response(_TAXONOMY_ANSWER_ONE_BRANCH),
        "MY-VERY-UNIQUE-EXTRA-TEMPLATE-MARKER": {
            "answer": "extra answer",
            "citations": {1: "nlm-extra-1"},
            "sources_used": ["nlm-extra-1"],
        },
    }
    client = FakeClient(responses)

    result = analysis.analyze(
        "nb-6",
        domain="d6",
        research_query="ciq",
        client=client,
        custom_investigation_templates={"extra": extra},
    )

    findings = result.findings["Only Branch"]
    # Defaults still ran.
    assert "methods" in findings
    assert "comparisons" in findings
    assert "open_problems" in findings
    # Plus the extra template.
    assert findings["extra"]["answer"] == "extra answer"


# --- citation preservation -------------------------------------------------


def test_citation_dicts_preserved_unchanged():
    """Every NotebookLM response has `citations: dict[int, str]`. The
    analysis layer must not transform them — the orchestrator's
    source-map resolves them later."""
    tax_citations = {1: "nlm-tax-A", 2: "nlm-tax-B", 7: "nlm-tax-C"}
    branch_citations = {3: "nlm-br-X", 4: "nlm-br-Y"}
    synth_shared = {1: "nlm-shared-1"}
    synth_data = {2: "nlm-data-2"}
    synth_trade = {5: "nlm-trade-5"}

    responses = {
        "citation preservation test": {
            "answer": _TAXONOMY_ANSWER_ONE_BRANCH,
            "citations": tax_citations,
            "sources_used": list(tax_citations.values()),
        },
        'for the research area "Only Branch"': {
            "answer": "branch answer",
            "citations": branch_citations,
            "sources_used": list(branch_citations.values()),
        },
        "architectures or techniques appear in multiple sub-fields": {
            "answer": "x",
            "citations": synth_shared,
            "sources_used": list(synth_shared.values()),
        },
        "benchmark datasets are referenced": {
            "answer": "y",
            "citations": synth_data,
            "sources_used": list(synth_data.values()),
        },
        "fundamental trade-offs": {
            "answer": "z",
            "citations": synth_trade,
            "sources_used": list(synth_trade.values()),
        },
    }
    client = FakeClient(responses)

    result = analysis.analyze(
        "nb-7",
        domain="d7",
        research_query="citation preservation test",
        client=client,
    )

    # Taxonomy citations preserved exactly.
    assert result.taxonomy["citations"] == tax_citations
    # Each branch sub-query carries the same branch citations dict
    # (FakeClient returned the same payload for all three templates).
    for key in ("methods", "comparisons", "open_problems"):
        assert result.findings["Only Branch"][key]["citations"] == branch_citations
    # Synthesis citations preserved exactly.
    assert result.synthesis["shared_architectures"]["citations"] == synth_shared
    assert result.synthesis["common_datasets"]["citations"] == synth_data
    assert result.synthesis["recurring_tradeoffs"]["citations"] == synth_trade


# --- prompt anchoring ------------------------------------------------------


def test_default_taxonomy_prompt_includes_research_query():
    """The default taxonomy prompt must mention the research query so
    NotebookLM scopes to what was actually researched."""
    responses = {
        "very-specific-research-query-marker": _taxonomy_response(_TAXONOMY_ANSWER_ONE_BRANCH),
    }
    client = FakeClient(responses)

    analysis.analyze(
        "nb-8",
        domain="d8",
        research_query="very-specific-research-query-marker",
        client=client,
    )

    # The first call is the taxonomy phase.
    _nb, taxonomy_question = client.calls[0]
    assert "very-specific-research-query-marker" in taxonomy_question


def test_default_investigation_templates_include_research_query():
    """Per the spec, investigation templates also reference the research
    query so the model anchors when the corpus has more than the session
    sources."""
    responses = {
        "ANCHOR-TOKEN-INVEST": _taxonomy_response(_TAXONOMY_ANSWER_ONE_BRANCH),
    }
    client = FakeClient(responses)

    analysis.analyze(
        "nb-9",
        domain="d9",
        research_query="ANCHOR-TOKEN-INVEST",
        client=client,
    )

    # Skip the first call (taxonomy). Branch sub-queries (3 of them) come next.
    branch_questions = [q for _nb, q in client.calls[1:4]]
    assert len(branch_questions) == 3
    for q in branch_questions:
        assert "ANCHOR-TOKEN-INVEST" in q
