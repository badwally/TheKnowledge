"""Plan format for agent-driven wiki authorship per BUILD.md M6.

A `Plan` is the agent's structured response to "given this source and the
current wiki state, what pages should change?" The gateway parses the plan,
runs the full validator on every update, and applies all writes atomically.

This is the structural enforcement of the "plan-before-write" rule from
WIKI § 11.6: the agent's only sanctioned path to wiki/ is to return a Plan;
the gateway is the only thing that mutates wiki/ files.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import json
import re

from gateway.llm import CallResult, ClaudeCLIClient, LLMError, model_for
from typing import Protocol


class PlanError(ValueError):
    """Raised when a Plan is missing, malformed, or rejected by validation."""


@dataclass
class WikiUpdate:
    """One file change in a Plan."""

    target_path: str          # e.g. "wiki/entities/semaglutide.md"
    update_kind: str          # "create" | "update"
    content: str              # full canonical markdown text (frontmatter + body)
    rationale: str = ""


@dataclass
class Contradiction:
    """A conflict between a new source's claim and an existing wiki page."""

    existing_page: str
    existing_claim: str
    new_claim: str
    source_id: str
    severity: str = "moderate"  # "minor" | "moderate" | "major"


@dataclass
class Plan:
    """The agent's plan for a single source ingest."""

    source_id: str
    rationale: str = ""
    updates: list[WikiUpdate] = field(default_factory=list)
    contradictions: list[Contradiction] = field(default_factory=list)

    def __bool__(self) -> bool:
        return bool(self.updates) or bool(self.contradictions)


# --- response parsing ------------------------------------------------------


_OBJECT_RE = re.compile(r"\{[\s\S]*\}")


def parse_plan_response(text: str, *, expected_source_id: str | None = None) -> Plan:
    """Pull a Plan out of an agent response.

    Tolerates:
    - leading/trailing prose
    - markdown code fences
    - extra whitespace
    """
    if not text or not text.strip():
        raise PlanError("empty response from plan client")

    cleaned = text.strip()
    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()

    obj = None
    try:
        obj = json.loads(cleaned)
    except json.JSONDecodeError:
        match = _OBJECT_RE.search(cleaned)
        if match:
            try:
                obj = json.loads(match.group(0))
            except json.JSONDecodeError as e:
                raise PlanError(f"could not parse JSON in plan response: {e}") from e

    if not isinstance(obj, dict):
        raise PlanError(f"plan response was not a JSON object: {cleaned[:200]!r}")

    source_id = str(obj.get("source_id", "")).strip()
    if not source_id:
        raise PlanError("plan missing 'source_id'")
    if expected_source_id and source_id != expected_source_id:
        raise PlanError(
            f"plan source_id {source_id!r} does not match expected {expected_source_id!r}"
        )

    raw_updates = obj.get("updates", [])
    if not isinstance(raw_updates, list):
        raise PlanError(f"plan 'updates' must be a list, got {type(raw_updates).__name__}")

    updates: list[WikiUpdate] = []
    for i, item in enumerate(raw_updates):
        if not isinstance(item, dict):
            raise PlanError(f"plan update #{i} is not an object: {item!r}")
        target = str(item.get("target_path", "")).strip()
        kind = str(item.get("update_kind", "")).strip()
        content = item.get("content", "")
        rationale = str(item.get("rationale", "")).strip()

        if not target:
            raise PlanError(f"plan update #{i} missing 'target_path'")
        if kind not in ("create", "update"):
            raise PlanError(
                f"plan update #{i} has invalid update_kind {kind!r}; expected 'create' or 'update'"
            )
        if not isinstance(content, str) or not content.strip():
            raise PlanError(f"plan update #{i} has empty 'content'")
        updates.append(
            WikiUpdate(
                target_path=target,
                update_kind=kind,
                content=content,
                rationale=rationale,
            )
        )

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

    return Plan(
        source_id=source_id,
        rationale=str(obj.get("rationale", "")).strip(),
        updates=updates,
        contradictions=contradictions,
    )


# --- agent client -----------------------------------------------------------


class PlanClient(Protocol):
    """Anything that takes a planning prompt and returns a JSON-shaped response."""

    def call(self, prompt: str) -> str: ...


class ClaudeCLIPlanClient:
    """Default backend: subprocess to `claude -p`. Reuses Max-plan auth.

    M44: delegates to `gateway.llm.ClaudeCLIClient` so plan invocations get
    ``--bare --tools "" --model claude-opus-4-7`` and a clean
    ``--system-prompt`` slot. Exposes both Protocol-compatible ``call(prompt)``
    and the optimized ``call_split(system, user)``. Plan stays on Opus 4.7
    (synthesis-grade reasoning); only filter routes to Haiku.
    """

    def __init__(
        self,
        executable: str = "claude",
        timeout_s: float = 300.0,
        *,
        max_retries: int = 0,
        model: str | None = None,
        cli: ClaudeCLIClient | None = None,
    ):
        self._model = model or model_for("plan")
        self._cli = cli or ClaudeCLIClient(
            executable=executable,
            timeout_s=timeout_s,
            max_retries=max_retries,
        )

    def call(self, prompt: str) -> str:
        """Protocol-compatible single-string entry point."""
        return self._invoke(system_prompt=None, user_prompt=prompt)

    def call_split(self, *, system: str, user: str) -> str:
        """M44 optimized: system prefix via --system-prompt."""
        return self._invoke(system_prompt=system, user_prompt=user)

    def call_with_usage(self, prompt: str) -> CallResult:
        """K5 telemetry variant of ``call(prompt)``."""
        return self._invoke_with_usage(system_prompt=None, user_prompt=prompt)

    def call_split_with_usage(self, *, system: str, user: str) -> CallResult:
        """K5 telemetry variant of ``call_split``."""
        return self._invoke_with_usage(system_prompt=system, user_prompt=user)

    def _invoke(self, *, system_prompt: str | None, user_prompt: str) -> str:
        try:
            return self._cli.call(
                user_prompt=user_prompt,
                system_prompt=system_prompt,
                model=self._model,
                tools="",
            )
        except LLMError as e:
            raise PlanError(str(e)) from e

    def _invoke_with_usage(
        self, *, system_prompt: str | None, user_prompt: str
    ) -> CallResult:
        try:
            return self._cli.call_with_usage(
                user_prompt=user_prompt,
                system_prompt=system_prompt,
                model=self._model,
                tools="",
            )
        except LLMError as e:
            raise PlanError(str(e)) from e


# --- prompt construction ---------------------------------------------------


_PLAN_SYSTEM_PROMPT = """\
You are the wiki authorship agent for a personal knowledge base. Your job is
to produce a structured Plan that updates entity / concept pages based on a
newly-ingested source, and to detect contradictions between the new source and
existing wiki claims.

## Conventions you must follow

- Page types live under `wiki/`:
  - `wiki/entities/<slug>.md` — people, organizations, products, statutes, papers, named artifacts (domain-dependent)
  - `wiki/concepts/<slug>.md` — mechanisms, frameworks, patterns, principles, phenomena (domain-dependent)
  - `wiki/synthesis/<slug>.md` — cross-source narrative analyses
  - `wiki/mocs/<domain>.md` — domain map of content

- Slugs: lowercase, hyphenated, semantic; reflect the entity/concept's canonical short name (e.g., `<topic-name>`, `<framework-name>`, `<statute-id>`).

- Citation grounding is mandatory. The validator's rule is operational, not
  vague: **every claim sentence (5+ words, ending in `.` or `!`) must carry a
  `[[sources/<id>]]` citation ON THE SAME LINE as the claim.** A citation in the
  Sources section does NOT satisfy a claim line elsewhere — cite inline, on each
  claim line. Rhetorical questions and short labels are exempt. The validator
  rejects any page with an uncited claim line.

- Each page has required sections (exact names; the validator rejects a page
  missing any of them):
  - entity:    Summary, Key facts, Sources, Related
  - concept:   Summary, Key claims, Sources, Related
  - synthesis: Synthesis, Sources cited (and optional Open questions)

- Frontmatter shape per type (key fields):
  - entity:    type, slug, canonical_name, entity_kind, domains
  - concept:   type, slug, canonical_name, domains
  - synthesis: type, slug, title, domains, question

- `entity_kind` (entity pages only) MUST be exactly one of this controlled
  vocabulary — any other value is rejected:
  __ENTITY_KIND_ENUM__
  Pick the closest: a company/lab/agency → `organization`; a research paper →
  `paper`; a law or bill → `statute` or `regulation`; a published spec → `standard`;
  a method/architecture/framework/system → `model` or `artifact`; a software tool
  or library → `software`; a named dataset → `dataset`; an evaluation/benchmark →
  `benchmark`; a person → `person`; a commercial product → `product`; a medication
  → `drug`; if nothing fits → `other`.

- Do NOT emit `created_at`, `last_updated`, or `sources_count` — the gateway
  auto-stamps these. Emitting a malformed timestamp will be rejected.

## Your task

The user message contains a newly-ingested source and the existing wiki
pages relevant to it. Produce a Plan that updates or creates entity/concept
pages and reports any contradictions.

### 1. Update or create pages

**Prioritize updating existing pages over creating new ones.** For every
entity or concept mentioned in the source, check the existing pages provided.
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
{
  "source_id": "<exact source_id from the source frontmatter>",
  "rationale": "<one sentence: why these updates>",
  "updates": [
    {
      "target_path": "wiki/entities/<slug>.md",
      "update_kind": "create" | "update",
      "content": "<FULL canonical markdown for the page (frontmatter + body)>",
      "rationale": "<why this page changes>"
    }
  ],
  "contradictions": [
    {
      "existing_page": "wiki/concepts/<slug>.md",
      "existing_claim": "<the existing claim text>",
      "new_claim": "<the conflicting claim from the new source>",
      "source_id": "<source_id of the new source>",
      "severity": "minor" | "moderate" | "major"
    }
  ]
}
```

Touch as many pages as the source genuinely informs (typically 5–15).
For `update`s, the `content` field replaces the page entirely. The full current
body of every page you update is provided to you below — you MUST copy every
existing claim and its `[[sources/<id>]]` citation verbatim into your new
`content` and then integrate the new claims. **The gateway rejects any update
that drops a citation the page already had** — never delete a prior claim or
citation while integrating; only add.

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

## Worked example

A valid `create` for a concept page, showing inline same-line citations and the
exact required sections (frontmatter timestamps omitted — the gateway stamps them):

```
{
  "target_path": "wiki/concepts/hypothesis-tree-search.md",
  "update_kind": "create",
  "content": "---\\ntype: concept\\nslug: hypothesis-tree-search\\ncanonical_name: Hypothesis-Tree Search\\ndomains:\\n- ai-and-agents\\n---\\n\\n# Hypothesis-Tree Search\\n\\n## Summary\\n\\nA search strategy that stores research state as a persistent tree of hypotheses, expanding and pruning branches as evidence accrues [[sources/example-source-id]].\\n\\n## Key claims\\n\\n- A persistent coordinator maintains global state while short-lived executors test one hypothesis each in isolation [[sources/example-source-id]].\\n- The approach reported more than 2.5x the average baseline gain across six research tasks [[sources/example-source-id]].\\n\\n## Sources\\n\\n- [[sources/example-source-id]]\\n\\n## Related\\n\\n- [[concepts/autonomous-research-agent]]\\n",
  "rationale": "New concept introduced by this source"
}
```

Note every claim sentence ends with `[[sources/example-source-id]]` on the same
line, all four required sections are present, and no timestamps are emitted.
"""


_PLAN_USER_TEMPLATE = """\
## Source under evaluation

```
{source_text}
```

## Existing wiki pages relevant to this source

{existing_pages_section}
"""


def build_plan_system_prompt() -> str:
    """Conventions + task instructions + JSON schema.

    Injects the live `entity_kind` controlled vocabulary so the agent picks from
    the closed set the validator enforces (rather than free-forming a rejected
    value). Deterministic for a given validator enum.
    """
    from gateway.validator import ENTITY_KIND_ENUM

    enum_line = ", ".join(f"`{k}`" for k in sorted(ENTITY_KIND_ENUM))
    return _PLAN_SYSTEM_PROMPT.replace("__ENTITY_KIND_ENUM__", enum_line)


def build_plan_user_prompt(source_text: str, existing_pages: dict[str, str]) -> str:
    """Per-item payload: the source and the relevant existing wiki pages.

    Strips embedded null bytes from `source_text` before embedding —
    pdfplumber occasionally extracts NUL characters from malformed PDFs
    and `subprocess.run` rejects them with `embedded null byte`.
    """
    if not existing_pages:
        existing_section = "_(no existing wiki pages yet for this domain)_"
    else:
        blocks = []
        for path in sorted(existing_pages.keys()):
            blocks.append(f"### {path}\n\n```\n{existing_pages[path]}\n```")
        existing_section = "\n\n".join(blocks)

    return _PLAN_USER_TEMPLATE.format(
        source_text=source_text.replace("\x00", ""),
        existing_pages_section=existing_section,
    )


_PLAN_REPAIR_TEMPLATE = """\
Your previous plan was REJECTED by the gateway validator. Fix ONLY the listed
errors and return a corrected JSON plan in the exact same schema. Preserve every
other update unchanged, and do not introduce new errors. In particular: keep all
existing `[[sources/<id>]]` citations (dropping one is rejected), use only the
allowed `entity_kind` values, give every claim sentence an inline same-line
citation, and include all required sections.

## Validator errors to fix

{errors}

## Your previous (rejected) response

```
{prior_response}
```

## Source under evaluation (unchanged)

```
{source_text}
```

## Existing wiki pages (unchanged)

{existing_pages_section}
"""


def build_plan_repair_prompt(
    source_text: str,
    existing_pages: dict[str, str],
    *,
    prior_response: str,
    errors: list[str],
) -> str:
    """Per-attempt repair payload: the validator errors + the rejected response,
    asking the agent to fix only those errors. Reuses the static system prompt."""
    if not existing_pages:
        existing_section = "_(no existing wiki pages yet for this domain)_"
    else:
        blocks = [
            f"### {path}\n\n```\n{existing_pages[path]}\n```"
            for path in sorted(existing_pages.keys())
        ]
        existing_section = "\n\n".join(blocks)
    error_lines = "\n".join(f"- {e}" for e in errors) or "- (no detail provided)"
    return _PLAN_REPAIR_TEMPLATE.format(
        errors=error_lines,
        prior_response=prior_response.replace("\x00", "")[:20000],
        source_text=source_text.replace("\x00", ""),
        existing_pages_section=existing_section,
    )


def build_plan_prompt(source_text: str, existing_pages: dict[str, str]) -> str:
    """Backwards-compatible: concatenated system + user prompt.

    Callers that pre-date M44 still get one big string. The ingest path
    uses `build_plan_system_prompt()` + `build_plan_user_prompt()` via
    `call_split` for the agent-harness savings.
    """
    return (
        build_plan_system_prompt()
        + "\n"
        + build_plan_user_prompt(source_text, existing_pages)
    )
