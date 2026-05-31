# Smart Authorship: Knowledge Connection + Post-Ingest Feedback

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the authorship agent to detect contradictions with existing wiki claims, prioritize updating existing pages over creating new ones, and emit a structured post-ingest report showing what changed and why.

**Architecture:** Three changes compose into one milestone: (1) expand the `Plan` response schema with a `contradictions` field so the agent can surface claim conflicts, (2) enhance `apply_plan` to build an `AuthorshipReport` summarizing pages created/updated/contradictions found, (3) enhance the prompt to explicitly instruct contradiction detection and existing-page integration. The report flows through `OperationResult` into CLI output and `log.md`.

**Tech Stack:** Python 3.11+, pytest, existing gateway infrastructure (plan.py, apply_plan.py, ingest.py, cli.py, core.py)

---

### Task 1: Add Contradiction dataclass and expand Plan schema

**Files:**
- Modify: `src/gateway/plan.py:25-45` (dataclasses)
- Test: `tests/gateway/test_authorship.py`

- [ ] **Step 1: Write the failing test for Contradiction parsing**

```python
# In tests/gateway/test_authorship.py, after existing parse_plan_response tests (~line 286)

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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py::test_parse_plan_response_parses_contradictions tests/gateway/test_authorship.py::test_parse_plan_response_defaults_empty_contradictions -v`
Expected: FAIL — `Plan` has no `contradictions` attribute

- [ ] **Step 3: Add Contradiction dataclass and update Plan**

In `src/gateway/plan.py`, after the `WikiUpdate` dataclass (line 33):

```python
@dataclass
class Contradiction:
    """A conflict between a new source's claim and an existing wiki page."""

    existing_page: str
    existing_claim: str
    new_claim: str
    source_id: str
    severity: str = "moderate"  # "minor" | "moderate" | "major"
```

Update the `Plan` dataclass (line 36):

```python
@dataclass
class Plan:
    """The agent's plan for a single source ingest."""

    source_id: str
    rationale: str = ""
    updates: list[WikiUpdate] = field(default_factory=list)
    contradictions: list[Contradiction] = field(default_factory=list)

    def __bool__(self) -> bool:
        return bool(self.updates) or bool(self.contradictions)
```

- [ ] **Step 4: Update parse_plan_response to handle contradictions**

In `src/gateway/plan.py`, in `parse_plan_response()`, after the updates loop (after line 123), add:

```python
    raw_contradictions = obj.get("contradictions", [])
    if not isinstance(raw_contradictions, list):
        raw_contradictions = []

    contradictions: list[Contradiction] = []
    for item in raw_contradictions:
        if not isinstance(item, dict):
            continue
        contradictions.append(
            Contradiction(
                existing_page=str(item.get("existing_page", "")).strip(),
                existing_claim=str(item.get("existing_claim", "")).strip(),
                new_claim=str(item.get("new_claim", "")).strip(),
                source_id=str(item.get("source_id", "")).strip(),
                severity=str(item.get("severity", "moderate")).strip(),
            )
        )
```

Update the return statement to include contradictions:

```python
    return Plan(
        source_id=source_id,
        rationale=str(obj.get("rationale", "")).strip(),
        updates=updates,
        contradictions=contradictions,
    )
```

- [ ] **Step 5: Update the Plan import in test file**

In `tests/gateway/test_authorship.py` line 20, update the import:

```python
from gateway.plan import (
    Contradiction,
    Plan,
    PlanError,
    WikiUpdate,
    build_plan_prompt,
    parse_plan_response,
)
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py::test_parse_plan_response_parses_contradictions tests/gateway/test_authorship.py::test_parse_plan_response_defaults_empty_contradictions -v`
Expected: PASS

- [ ] **Step 7: Run full test suite to check for regressions**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py -v`
Expected: All existing tests still pass

- [ ] **Step 8: Commit**

```bash
git add src/gateway/plan.py tests/gateway/test_authorship.py
git commit -m "feat: add Contradiction to Plan schema for claim conflict detection"
```

---

### Task 2: Add AuthorshipReport to OperationResult

**Files:**
- Modify: `src/gateway/core.py:23-38`
- Test: `tests/gateway/test_authorship.py`

- [ ] **Step 1: Write the failing test for AuthorshipReport**

```python
# In tests/gateway/test_authorship.py, after the Contradiction tests

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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py::test_authorship_report_summary_formatting tests/gateway/test_authorship.py::test_authorship_report_empty -v`
Expected: FAIL — `AuthorshipReport` does not exist

- [ ] **Step 3: Add AuthorshipReport dataclass**

In `src/gateway/core.py`, after the existing imports (line 3), add:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gateway.plan import Contradiction
```

After the `OperationResult` class (after line 38), add:

```python
@dataclass
class AuthorshipReport:
    """Structured summary of what the authorship agent did."""

    pages_created: list[str] = field(default_factory=list)
    pages_updated: list[str] = field(default_factory=list)
    contradictions: list["Contradiction"] = field(default_factory=list)

    def format_summary(self) -> str:
        parts = [
            f"{len(self.pages_created)} created",
            f"{len(self.pages_updated)} updated",
        ]
        if self.contradictions:
            parts.append(f"{len(self.contradictions)} contradiction(s) found")
        return ", ".join(parts)

    def format_detail(self) -> list[str]:
        """Return lines suitable for CLI output."""
        lines: list[str] = []
        for p in self.pages_created:
            lines.append(f"  + {p}")
        for p in self.pages_updated:
            lines.append(f"  ~ {p}")
        for c in self.contradictions:
            lines.append(
                f"  ! CONTRADICTION ({c.severity}) in {c.existing_page}:"
            )
            lines.append(f"    existing: {c.existing_claim[:120]}")
            lines.append(f"    new:      {c.new_claim[:120]}")
        return lines
```

Add `authorship_report` field to `OperationResult`:

```python
@dataclass
class OperationResult:
    """Structured return value from any gateway operation."""

    success: bool
    paths_touched: list[Path] = field(default_factory=list)
    summary: str = ""
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    no_op: bool = False
    authorship_report: AuthorshipReport | None = None

    def __str__(self) -> str:  # pragma: no cover — debug aid
        if self.success:
            tag = "no-op" if self.no_op else "ok"
            return f"[{tag}] {self.summary}"
        return f"[fail] {'; '.join(self.errors) or self.summary}"
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py::test_authorship_report_summary_formatting tests/gateway/test_authorship.py::test_authorship_report_empty -v`
Expected: PASS

- [ ] **Step 5: Run full test suite for regressions**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py -v`
Expected: All tests pass (new field defaults to None, no breakage)

- [ ] **Step 6: Commit**

```bash
git add src/gateway/core.py tests/gateway/test_authorship.py
git commit -m "feat: add AuthorshipReport to OperationResult for structured post-ingest feedback"
```

---

### Task 3: Wire AuthorshipReport into apply_plan

**Files:**
- Modify: `src/gateway/ops/apply_plan.py:24-138`
- Test: `tests/gateway/test_authorship.py`

- [ ] **Step 1: Write the failing test**

```python
# In tests/gateway/test_authorship.py, after existing apply_plan tests

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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py::test_apply_plan_populates_authorship_report tests/gateway/test_authorship.py::test_apply_plan_report_distinguishes_create_and_update -v`
Expected: FAIL — `authorship_report` is None

- [ ] **Step 3: Update apply_plan to build AuthorshipReport**

In `src/gateway/ops/apply_plan.py`, add import at line 9:

```python
from gateway.core import AuthorshipReport, OperationResult, write_atomic
```

(Replace the existing `from gateway.core import OperationResult, write_atomic`)

In `apply_plan()`, after Phase 2 writes (replace the return block at lines 133-138):

```python
    # --- Phase 3: build authorship report ---
    report = AuthorshipReport(
        pages_created=[
            u.target_path for u, pt, f, b in parsed if u.update_kind == "create"
        ],
        pages_updated=[
            u.target_path for u, pt, f, b in parsed if u.update_kind == "update"
        ],
        contradictions=list(plan.contradictions),
    )

    return OperationResult(
        success=True,
        paths_touched=paths_touched + [paths.log_path()],
        summary=f"applied plan for {plan.source_id}: {len(plan.updates)} update(s)",
        warnings=warnings,
        authorship_report=report,
    )
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py::test_apply_plan_populates_authorship_report tests/gateway/test_authorship.py::test_apply_plan_report_distinguishes_create_and_update -v`
Expected: PASS

- [ ] **Step 5: Run full test suite for regressions**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py -v`
Expected: All tests pass

- [ ] **Step 6: Commit**

```bash
git add src/gateway/ops/apply_plan.py tests/gateway/test_authorship.py
git commit -m "feat: apply_plan builds AuthorshipReport with created/updated/contradictions"
```

---

### Task 4: Render AuthorshipReport in CLI output and log.md

**Files:**
- Modify: `src/gateway/cli.py:571-583`
- Modify: `src/gateway/ops/ingest.py:354-375`
- Modify: `src/gateway/ops/apply_plan.py:123-131` (log entry)
- Test: `tests/gateway/test_authorship.py`

- [ ] **Step 1: Write the failing test for enriched log entry**

```python
# In tests/gateway/test_authorship.py

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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py::test_apply_plan_log_includes_contradictions -v`
Expected: FAIL — log entry doesn't contain contradictions

- [ ] **Step 3: Enhance log entry in apply_plan**

In `src/gateway/ops/apply_plan.py`, update the `log.append()` call in Phase 2 (lines 123-131):

```python
        log_fields = {
            "id": plan.source_id,
            "updates": len(plan.updates),
            "created": len(report.pages_created),
            "updated": len(report.pages_updated),
            "contradictions": len(report.contradictions),
            "draft": "yes" if draft else "no",
        }

        log_summary_parts = [plan.rationale or "(no rationale provided)"]
        if report.pages_created:
            log_summary_parts.append(f"created: {', '.join(report.pages_created)}")
        if report.pages_updated:
            log_summary_parts.append(f"updated: {', '.join(report.pages_updated)}")
        for c in report.contradictions:
            log_summary_parts.append(
                f"CONTRADICTION ({c.severity}) in {c.existing_page}: "
                f"was \"{c.existing_claim[:80]}\" vs new \"{c.new_claim[:80]}\""
            )

        log.append(
            op="wiki-author",
            fields=log_fields,
            summary="\n".join(log_summary_parts),
        )
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py::test_apply_plan_log_includes_contradictions -v`
Expected: PASS

- [ ] **Step 5: Enhance _emit_result in cli.py**

In `src/gateway/cli.py`, update `_emit_result` (lines 571-583):

```python
def _emit_result(result, *, no_op_label: str = "no-op", ok_label: str = "ok") -> int:
    if result.success:
        prefix = no_op_label if result.no_op else ok_label
        print(f"{prefix}: {result.summary}")
        for p in result.paths_touched:
            print(f"  touched: {p}")
        if result.authorship_report is not None:
            report = result.authorship_report
            print(f"  authorship: {report.format_summary()}")
            for line in report.format_detail():
                print(line)
        for w in result.warnings:
            print(f"warning: {w}", file=sys.stderr)
        return 0
    print("operation failed:", file=sys.stderr)
    for e in result.errors:
        print(f"  - {e}", file=sys.stderr)
    return 1
```

- [ ] **Step 6: Propagate authorship_report through ingest result**

In `src/gateway/ops/ingest.py`, in the `--with-plan` block (lines 354-374), update the success path:

```python
    if with_plan and wiki_written:
        plan_result = _invoke_plan_and_apply(
            front=front,
            body=body,
            domain=effective_domain,
            plan_client=plan_client,
            draft=draft,
        )
        if plan_result.success:
            result_obj.paths_touched.extend(plan_result.paths_touched)
            result_obj.summary += f"; authorship: {plan_result.summary}"
            result_obj.warnings.extend(plan_result.warnings)
            result_obj.authorship_report = plan_result.authorship_report
        else:
            result_obj.warnings.append(
                "wiki authorship failed (source page still committed): "
                + "; ".join(plan_result.errors)
            )
```

- [ ] **Step 7: Write integration test for ingest with report**

```python
# In tests/gateway/test_authorship.py

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
```

- [ ] **Step 8: Run all new and existing tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py -v`
Expected: All tests pass

- [ ] **Step 9: Commit**

```bash
git add src/gateway/cli.py src/gateway/ops/ingest.py src/gateway/ops/apply_plan.py tests/gateway/test_authorship.py
git commit -m "feat: render AuthorshipReport in CLI output and log.md"
```

---

### Task 5: Enhance authorship prompt for contradiction detection and knowledge integration

**Files:**
- Modify: `src/gateway/plan.py:172-250` (prompt template)
- Test: `tests/gateway/test_authorship.py`

- [ ] **Step 1: Write test that prompt includes contradiction instructions**

```python
# In tests/gateway/test_authorship.py

def test_build_plan_prompt_includes_contradiction_instructions():
    prompt = build_plan_prompt("source body", {"wiki/concepts/x.md": "existing"})
    assert "contradictions" in prompt.lower()
    assert "existing_page" in prompt
    assert "existing_claim" in prompt
    assert "new_claim" in prompt
    assert "severity" in prompt


def test_build_plan_prompt_includes_update_priority():
    prompt = build_plan_prompt("source body", {"wiki/concepts/x.md": "existing"})
    assert "update" in prompt.lower()
    assert "prefer" in prompt.lower() or "prioritize" in prompt.lower() or "existing page" in prompt.lower()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py::test_build_plan_prompt_includes_contradiction_instructions tests/gateway/test_authorship.py::test_build_plan_prompt_includes_update_priority -v`
Expected: FAIL — prompt doesn't contain these terms

- [ ] **Step 3: Rewrite the prompt template**

In `src/gateway/plan.py`, replace `_PLAN_PROMPT_TEMPLATE` (lines 172-250) with:

```python
_PLAN_PROMPT_TEMPLATE = """\
You are the wiki authorship agent for a personal knowledge base. Your job is
to produce a structured Plan that updates entity / concept pages based on a
newly-ingested source, and to detect contradictions between the new source and
existing wiki claims.

## Conventions you must follow

- Page types live under `wiki/`:
  - `wiki/entities/<slug>.md` — drugs, people, papers, organizations
  - `wiki/concepts/<slug>.md` — mechanisms, phenomena, frameworks
  - `wiki/synthesis/<slug>.md` — cross-source narrative analyses
  - `wiki/mocs/<domain>.md` — domain map of content

- Slugs: lowercase, hyphenated, semantic (e.g., `food-noise`, `nucleus-accumbens`).

- Citation grounding is mandatory. Every factual claim in entity / concept /
  synthesis pages must be followed by `[[sources/<id>]]` linking to the
  source page. The validator rejects pages without proper citation.

- Each page has required sections (full schemas in WIKI.md):
  - entity:    Summary, Key facts, Sources, Related
  - concept:   Summary, Key claims, Sources, Related
  - synthesis: Synthesis, Sources cited (and optional Open questions)

- Frontmatter shape per type (key fields):
  - entity:    type, slug, canonical_name, entity_kind, domains
  - concept:   type, slug, canonical_name, domains
  - synthesis: type, slug, title, domains, question

## Source under evaluation

```
{source_text}
```

## Existing wiki pages relevant to this source

{existing_pages_section}

## Your task

### 1. Update or create pages

**Prioritize updating existing pages over creating new ones.** For every
entity or concept mentioned in the source, check the existing pages above.
If a matching page exists, produce an `"update"` that integrates the new
claims (preserving all existing claims and citations). Only create a new
page when no existing page covers the entity or concept.

When updating, merge carefully:
- Keep all existing claims and their citations intact.
- Add new claims from this source with `[[sources/<id>]]` citations.
- Update the Sources section to include the new source.
- Update the Related section if new cross-references are warranted.

### 2. Detect contradictions

Compare claims in the new source against claims in the existing pages.
A contradiction is when the new source asserts something that conflicts
with an existing claim. Report ALL contradictions you find — do not
silently resolve them.

Severity levels:
- `"minor"` — difference in emphasis, framing, or degree
- `"moderate"` — conflicting factual claims that could both be correct in different contexts
- `"major"` — direct factual contradiction where one claim must be wrong

### 3. Return JSON

Return ONLY a JSON object:

```
{{
  "source_id": "<exact source_id from the source frontmatter>",
  "rationale": "<one sentence: why these updates>",
  "updates": [
    {{
      "target_path": "wiki/entities/<slug>.md",
      "update_kind": "create" | "update",
      "content": "<FULL canonical markdown for the page (frontmatter + body)>",
      "rationale": "<why this page changes>"
    }}
  ],
  "contradictions": [
    {{
      "existing_page": "wiki/concepts/<slug>.md",
      "existing_claim": "<the existing claim text>",
      "new_claim": "<the conflicting claim from the new source>",
      "source_id": "<source_id of the new source>",
      "severity": "minor" | "moderate" | "major"
    }}
  ]
}}
```

Touch as many pages as the source genuinely informs (typically 5–15).
For `update`s, the `content` field replaces the page entirely — preserve
existing claims and citations and integrate the new ones.

If no contradictions are found, return an empty `"contradictions": []`.

**Per-source plans must ONLY produce entity (`wiki/entities/`) and concept
(`wiki/concepts/`) pages.** Do NOT generate:

- `wiki/sources/<id>.md` — managed by the gateway.
- `wiki/synthesis/...` — synthesis is by definition cross-source. Generate
  via `wiki query`, not from a single source's ingest plan.
- `wiki/mocs/<domain>.md` — MOCs are domain-scoped, edited by separate
  curation operations.

If the source genuinely warrants a new entity/concept, create it. Otherwise
update the existing one. Concept and entity pages must have every claim
followed by `[[sources/<id>]]` linking to a source already on disk.
"""
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py::test_build_plan_prompt_includes_contradiction_instructions tests/gateway/test_authorship.py::test_build_plan_prompt_includes_update_priority -v`
Expected: PASS

- [ ] **Step 5: Run full test suite**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py -v`
Expected: All tests pass

- [ ] **Step 6: Commit**

```bash
git add src/gateway/plan.py tests/gateway/test_authorship.py
git commit -m "feat: enhance authorship prompt for contradiction detection and update prioritization"
```

---

### Task 6: End-to-end integration test

**Files:**
- Test: `tests/gateway/test_authorship.py`

This task verifies the full flow: ingest with plan → contradictions detected → report rendered → log entry written.

- [ ] **Step 1: Write the end-to-end test**

```python
# In tests/gateway/test_authorship.py

def test_end_to_end_smart_authorship(kb_root, make_source, tmp_path):
    """Full flow: ingest → plan with create + update + contradiction → report + log."""
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

    # Ingest a new source
    text = make_source(id_="yt-newSource_AB", domains=["d-e2e"])
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
    result = ingest(src, domain="d-e2e", with_plan=True, plan_client=client)
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
```

- [ ] **Step 2: Run the e2e test**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py::test_end_to_end_smart_authorship -v`
Expected: PASS (all prior tasks should make this work)

- [ ] **Step 3: Run the complete test suite**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/ -v`
Expected: All tests pass

- [ ] **Step 4: Commit**

```bash
git add tests/gateway/test_authorship.py
git commit -m "test: end-to-end smart authorship with contradictions and report"
```

---

### Task 7: Update BUILD.md with delivery record

**Files:**
- Modify: `BUILD.md`

- [ ] **Step 1: Append milestone entry to BUILD.md**

Add a new section to the delivery record in BUILD.md documenting this milestone. Include:
- What was built (smart authorship: contradiction detection, update prioritization, structured feedback)
- Which files were modified
- Test coverage summary
- Commit hashes

- [ ] **Step 2: Commit**

```bash
git add BUILD.md
git commit -m "docs: BUILD.md delivery record for smart authorship milestone"
```
