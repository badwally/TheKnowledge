# YouTube-Aware Filter Restoration — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore the YouTube-awareness the research filter lost in the general-purpose port, so authoritative talks (university lectures, conference keynotes, named-lab seminars) survive the candidate filter instead of being rejected on thin descriptions.

**Architecture:** Three independent changes. (1) Add a static source-type guidance section to the filter system prompt telling the model that video descriptions under-represent content and to weight channel/speaker/venue authority. (2) Add `channel_authority`/`speaker_expertise` quality signals to the `agentic-data-layer` policy — these reach the prompt for free because `build_system_prompt` dumps the whole policy. (3) Flip the planner's YouTube query register from vendor/tutorial to lecture/talk/institution to fix recall. The NLM ingestion path is unchanged — it already ships the URL and lets NotebookLM fetch the transcript for any source that passes the filter; the gap was entirely the filter.

**Tech Stack:** Python 3.11, pytest. Gateway package under `src/gateway/`. Run tests with `.venv/bin/python -m pytest`.

## Global Constraints

- Use `.venv/bin/python -m pytest` — never system `python` (it lacks the gateway package).
- No new dependencies.
- Source-type *guidance* is domain-agnostic and lives in code (`semantic.py`). Channel-authority *signals* are domain-specific and live in the policy YAML.
- Policy files under `.knowledge/policies/` are config and may be edited directly (the bootstrapped policy header says "Edit freely"). This is distinct from the hard rule forbidding direct writes to `wiki/` and `raw/`.
- Prompt-engineering changes are tested at the prompt-construction layer (assert the rendered prompt carries the right instructions/signals). The LLM's scoring response itself is not unit-testable.
- Each task commits `src/` + `tests/` (Task 2 also commits the policy YAML). Isolated from the parallel project's uncommitted `wiki/`/`raw/` files — never `git add -A` or `git add -u`.

---

### Task 1: Source-type guidance in the filter system prompt

**Files:**
- Modify: `src/gateway/filter/semantic.py` (add `_SOURCE_TYPE_GUIDANCE`, insert into `_SYSTEM_PROMPT_TEMPLATE`)
- Test: `tests/gateway/test_filter.py`

**Interfaces:**
- Consumes: `gateway.filter.semantic.build_system_prompt(policy: Policy, examples: list[Example]) -> str` (existing).
- Produces: no signature change. `build_system_prompt` output now contains a "Source-type guidance" section.

- [ ] **Step 1: Write the failing test**

In `tests/gateway/test_filter.py`, add:

```python
def test_system_prompt_includes_youtube_source_type_guidance():
    """Regression: the port dropped per-source-type guidance, so video
    candidates were scored on thin descriptions against paper criteria."""
    from gateway.filter import semantic

    policy = Policy(domain_slug="d", raw={"domain": {"slug": "d"}})
    prompt = semantic.build_system_prompt(policy, [])

    assert "Source-type guidance" in prompt
    assert "youtube" in prompt.lower()
    # The specific regression we are guarding against:
    assert "do not penalize" in prompt.lower()
    assert "channel authority" in prompt.lower()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter.py::test_system_prompt_includes_youtube_source_type_guidance -v`
Expected: FAIL — `assert "Source-type guidance" in prompt` is False.

- [ ] **Step 3: Add the guidance constant**

In `src/gateway/filter/semantic.py`, immediately before `_SYSTEM_PROMPT_TEMPLATE` (around line 154), add:

```python
_SOURCE_TYPE_GUIDANCE = """\
## Source-type guidance

Apply the guidance matching the source's `type` field in the user message:

- **youtube / video**: The `description` is often promotional or truncated and
  does NOT represent the talk's actual depth (the transcript, fetched later by
  NotebookLM, does). Do not penalize a video for a thin or marketing-style
  description. Weight channel authority, speaker and institutional credentials,
  and venue: university courses and named research labs, recognized conferences,
  keynotes, and seminars, and established domain practitioners are high-authority
  even when the blurb is short. Score on source authority plus topical relevance
  to the inclusion criteria — not on whether the metadata itself demonstrates
  technical depth. An on-topic lecture or conference talk from an authoritative
  channel should clear the inclusion bar.
- **arxiv / pubmed**: The abstract represents the work; score it directly against
  the inclusion and methodology criteria.
- **web / pdf**: Judge the fetched body text against the criteria.
"""
```

- [ ] **Step 4: Insert the guidance into the system prompt template**

In `src/gateway/filter/semantic.py`, change `_SYSTEM_PROMPT_TEMPLATE` (lines 154–181) so the guidance appears after the policy block and before `## Instructions`. Replace:

```python
## Past decisions for calibration

{examples_section}

## Instructions
```

with:

```python
## Past decisions for calibration

{examples_section}

{source_type_guidance}

## Instructions
```

Then update `build_system_prompt` (lines 191–200) to fill the new field:

```python
def build_system_prompt(policy: Policy, examples: list[Example]) -> str:
    """Static prefix: policy + examples + scoring instructions.

    Identical across all candidates in a single research run.
    """
    policy_yaml = yaml.safe_dump(policy.raw, sort_keys=False, default_flow_style=False, allow_unicode=True).rstrip()
    return _SYSTEM_PROMPT_TEMPLATE.format(
        policy_yaml=policy_yaml,
        examples_section=_format_examples(examples),
        source_type_guidance=_SOURCE_TYPE_GUIDANCE.rstrip(),
    )
```

- [ ] **Step 5: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter.py::test_system_prompt_includes_youtube_source_type_guidance -v`
Expected: PASS.

- [ ] **Step 6: Run the full filter test module to check nothing else broke**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter.py -q`
Expected: all pass (the `_prebuilt_system` test at line 504 still holds — the signature is unchanged).

- [ ] **Step 7: Commit**

```bash
git add src/gateway/filter/semantic.py tests/gateway/test_filter.py
git commit -m "feat(filter): restore per-source-type guidance in system prompt

Video descriptions under-represent content; instruct the filter to weight
channel/speaker/venue authority and not penalize authoritative talks for thin
descriptions. Regression from the general-purpose port.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 2: Channel-authority quality signals in the agentic-data-layer policy

**Files:**
- Modify: `.knowledge/policies/agentic-data-layer/policy.yaml` (add `channel_authority` + `speaker_expertise` under `quality_signals`)
- Test: `tests/gateway/test_filter.py`

**Interfaces:**
- Consumes: `build_system_prompt` dumps `policy.raw` wholesale, so any `quality_signals` entry appears verbatim in the prompt.
- Produces: no signature change. Guards the mechanism that quality signals reach the prompt.

- [ ] **Step 1: Write the failing test (mechanism guard)**

In `tests/gateway/test_filter.py`, add:

```python
def test_system_prompt_surfaces_channel_authority_quality_signals():
    """Channel-authority signals must reach the prompt so video sources can
    clear the bar on authority. build_system_prompt dumps the whole policy."""
    from gateway.filter import semantic

    raw = {
        "domain": {"slug": "d"},
        "quality_signals": {
            "channel_authority": {
                "positive_signals": ["University course or named research lab"]
            }
        },
    }
    policy = Policy(domain_slug="d", quality_signals=raw["quality_signals"], raw=raw)
    prompt = semantic.build_system_prompt(policy, [])

    assert "channel_authority" in prompt
    assert "University course or named research lab" in prompt
```

- [ ] **Step 2: Run test to verify it passes immediately, OR fails**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter.py::test_system_prompt_surfaces_channel_authority_quality_signals -v`
Expected: PASS (the mechanism already works — `build_system_prompt` dumps `policy.raw`). This test is a *regression guard*, not a RED→GREEN driver: it locks in that a future change to `build_system_prompt` (e.g. dumping only criteria) cannot silently drop quality signals. If it fails, the dump path was already broken — fix `build_system_prompt` to serialize `policy.raw` before proceeding.

- [ ] **Step 3: Add the signals to the policy**

Edit `.knowledge/policies/agentic-data-layer/policy.yaml`. Under the existing `quality_signals:` block (after `publication_venue:`), add:

```yaml
  channel_authority:
    positive_signals:
    - University course lectures or named research-lab talks (e.g. Stanford, MIT,
      Berkeley, DeepMind, Anthropic, FAIR)
    - Recognized conference or workshop sessions (NeurIPS, ICML, ICLR, ISWC, KGC,
      VLDB, or established industry summits)
    - Speaker is a published researcher, framework author, or named practitioner
      in agent systems or knowledge engineering
    negative_signals:
    - Influencer or growth-marketing channel with no technical track record
    - Content primarily promoting a paid course, newsletter, or product upsell
  speaker_expertise:
    positive_signals:
    - Discusses architecture, retrieval, or validation mechanisms with precision
    - References specific systems, papers, or benchmarks by name
    negative_signals:
    - Surface-level overview or hype with no mechanism or implementation detail
```

- [ ] **Step 4: Verify the policy still loads and lints clean**

Run: `.venv/bin/python -c "from gateway.filter.policy import load_policy; p = load_policy('agentic-data-layer'); print(sorted(p.quality_signals))"`
Expected: prints a list including `'channel_authority'`, `'content_depth'`, `'methodology_rigor'`, `'publication_venue'`, `'speaker_expertise'`.

- [ ] **Step 5: Run the filter test module**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter.py -q`
Expected: all pass.

- [ ] **Step 6: Commit**

```bash
git add .knowledge/policies/agentic-data-layer/policy.yaml tests/gateway/test_filter.py
git commit -m "feat(agentic-data-layer): add channel_authority + speaker_expertise signals

Lets authoritative video sources (university lectures, conference talks, named
labs) clear the filter on source authority. Mechanism-guard test pins that
quality_signals reach the system prompt.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 3: Flip the planner's YouTube query register to lecture/talk

**Files:**
- Modify: `src/gateway/research/query_planner.py` (`_ADAPTER_GUIDANCE["youtube"]`)
- Test: `tests/gateway/test_research_query_planner.py`

**Interfaces:**
- Consumes: `query_planner._ADAPTER_GUIDANCE` (dict), `query_planner.plan_per_adapter_queries(...)` (existing), `_MockClient` capturing `last_prompt` (existing test helper).
- Produces: no signature change. The rendered planner prompt now steers YouTube queries toward lecture/talk/institution register.

- [ ] **Step 1: Write the failing tests**

In `tests/gateway/test_research_query_planner.py`, add:

```python
def test_youtube_adapter_guidance_targets_lecture_register() -> None:
    g = qp._ADAPTER_GUIDANCE["youtube"].lower()
    assert "lecture" in g
    assert "keynote" in g or "seminar" in g
    # the old vendor/tutorial bias should be gone
    assert "tutorial" not in g or "avoid" in g


def test_rendered_plan_prompt_carries_youtube_lecture_register() -> None:
    client = _MockClient('{"youtube": [], "arxiv": [], "web": [], "pubmed": []}')
    qp.plan_per_adapter_queries(
        "agents that query semantic data",
        domain="d",
        policy=_policy(),
        adapter_names=["youtube", "arxiv", "web", "pubmed"],
        plan_client=client,
    )
    assert client.last_prompt is not None
    assert "lecture" in client.last_prompt.lower()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/gateway/test_research_query_planner.py -k "lecture_register or carries_youtube" -v`
Expected: FAIL — current guidance has no "lecture"/"keynote".

- [ ] **Step 3: Rewrite the YouTube adapter guidance**

In `src/gateway/research/query_planner.py`, replace the `"youtube"` entry in `_ADAPTER_GUIDANCE` (lines 49–53):

```python
    "youtube": (
        "short keyword phrases (3-7 words). target authoritative talks: "
        "university lectures and course series, conference keynotes and "
        "seminars, named research labs, and recognized practitioners. anchor "
        "on institutions, events, and speaker names (e.g. Stanford, MIT, "
        "NeurIPS, a named lab or researcher) and named frameworks. avoid "
        "tutorial and vendor-demo phrasing and full sentences."
    ),
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/gateway/test_research_query_planner.py -k "lecture_register or carries_youtube" -v`
Expected: PASS.

- [ ] **Step 5: Run the full planner test module**

Run: `.venv/bin/python -m pytest tests/gateway/test_research_query_planner.py -q`
Expected: all pass.

- [ ] **Step 6: Commit**

```bash
git add src/gateway/research/query_planner.py tests/gateway/test_research_query_planner.py
git commit -m "feat(planner): steer YouTube queries to lecture/talk register

Old guidance biased toward product/vendor/tutorial phrasing, so authoritative
lectures and conference talks never surfaced as candidates. Anchor on
institutions, events, and speaker names instead.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 4: Full-suite regression check

**Files:** none (verification only).

- [ ] **Step 1: Run the gateway filter + research suites**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter.py tests/gateway/test_research_query_planner.py -q`
Expected: all pass.

- [ ] **Step 2: Run the broader research test set to catch incidental breakage**

Run: `.venv/bin/python -m pytest tests/gateway -q -k "filter or research or planner"`
Expected: all pass. If anything fails, it indicates a prompt-format assertion elsewhere coupled to the old template — fix that test's expectation, do not revert the guidance.

## Out of scope (follow-ups)

- **Bootstrap generates channel-authority signals automatically.** `wiki bootstrap-domain`'s policy-gen prompt should emit `channel_authority`/`speaker_expertise` when a domain is likely to draw on video sources. Larger change to the bootstrap LLM prompt; defer.
- **Local-RAG transcript capture.** The wiki's `raw/` copy and `wiki retrieve` see only what the YouTube *converter* writes, not NLM's fetched transcript. Verify the converter captures the full transcript so local retrieval quality matches the NLM corpus. Independent of this fix.
- **Re-run to validate.** After landing, re-run a YouTube-heavy query plan in `agentic-data-layer` (when the shared S2 key is idle) and confirm authoritative talks now appear in `accepted`. This is empirical validation, not a code task.

## Self-Review

- **Spec coverage:** (a) per-source-type guidance → Task 1; (b) channel-authority signals → Task 2; (c) query-register fix → Task 3; full-suite guard → Task 4. All three agreed changes covered.
- **Placeholder scan:** none — every step carries exact code/commands.
- **Type consistency:** no signature changes in any task; `build_system_prompt` adds a `.format` field only; `_ADAPTER_GUIDANCE` and `_SOURCE_TYPE_GUIDANCE` are module-level constants referenced exactly as named.
