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
import subprocess
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
    """Default backend: subprocess to `claude -p`. Reuses Max-plan auth."""

    def __init__(self, executable: str = "claude", timeout_s: float = 300.0):
        self._exe = executable
        self._timeout = timeout_s

    def call(self, prompt: str) -> str:
        try:
            result = subprocess.run(
                [self._exe, "-p", prompt],
                capture_output=True,
                text=True,
                timeout=self._timeout,
                check=False,
            )
        except FileNotFoundError as e:
            raise PlanError(f"`{self._exe}` not found on PATH; install Claude Code or inject a PlanClient") from e
        except subprocess.TimeoutExpired as e:
            raise PlanError(f"`{self._exe} -p` timed out after {self._timeout}s") from e

        if result.returncode != 0:
            raise PlanError(
                f"`{self._exe} -p` exited {result.returncode}: {result.stderr.strip()[:300]}"
            )
        return result.stdout


# --- prompt construction ---------------------------------------------------


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
{{{{
  "source_id": "<exact source_id from the source frontmatter>",
  "rationale": "<one sentence: why these updates>",
  "updates": [
    {{{{
      "target_path": "wiki/entities/<slug>.md",
      "update_kind": "create" | "update",
      "content": "<FULL canonical markdown for the page (frontmatter + body)>",
      "rationale": "<why this page changes>"
    }}}}
  ],
  "contradictions": [
    {{{{
      "existing_page": "wiki/concepts/<slug>.md",
      "existing_claim": "<the existing claim text>",
      "new_claim": "<the conflicting claim from the new source>",
      "source_id": "<source_id of the new source>",
      "severity": "minor" | "moderate" | "major"
    }}}}
  ]
}}}}
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


def build_plan_prompt(source_text: str, existing_pages: dict[str, str]) -> str:
    """Construct the planning prompt.

    `existing_pages` maps relative-path (e.g. "wiki/concepts/food-noise.md")
    to the page's current canonical text. The prompt embeds these so the
    agent can revise rather than overwrite.

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

    return _PLAN_PROMPT_TEMPLATE.format(
        source_text=source_text.replace("\x00", ""),
        existing_pages_section=existing_section,
    )
