"""NotebookLM-driven analysis layer for the corpus-constructive research op.

Three phases, each implemented as a private helper that calls
`NlmClient.notebook_query` and parses `{answer, citations, sources_used}`:

1. `_extract_taxonomy` — anchors on the original `research_query` and asks
   the corpus for a hierarchical AREA / SUB / METHOD breakdown of what's
   actually present.
2. `_investigate_branch` — runs the METHODS / COMPARISONS / OPEN_PROBLEMS
   templates against each taxonomy branch.
3. `_synthesize_themes` — runs corpus-wide cross-cutting prompts
   (SHARED_ARCHITECTURES, COMMON_DATASETS, RECURRING_TRADEOFFS).

Ported from `~/code/research-notebook/src/research/{taxonomy,investigate,
synthesize,query}.py`. The only material change is the call mechanism:
the legacy code shelled out to `nlm` directly; this module reuses the
gateway's `NlmClient.notebook_query` so we get the Protocol-typed,
test-injectable surface (CLAUDE.md: "no direct calls to `nlm` or
NotebookLM MCP tools — all NotebookLM operations go through the
gateway").

Per-phase error isolation: a single branch or synthesis-query failure is
captured in `AnalysisResult.errors` and the run continues. The
orchestrator owns persistence — this module performs no I/O beyond
`client.notebook_query`.
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

from gateway import paths

if TYPE_CHECKING:
    from gateway.nlm_client import NlmClient


FINDINGS_STALE_HOURS = 24


# --- prompt templates ------------------------------------------------------


_TAXONOMY_PROMPT = """Analyze all sources in this notebook in the context of the following research question:

"{research_query}"

Identify the major themes, sub-themes, and specific points discussed in the sources that are relevant to that question. Scope the taxonomy to what is actually present in the corpus — do not invent themes not supported by the sources.

Organize your response as a structured hierarchy with these levels:
1. Top-level themes (the main conceptual areas the corpus addresses)
2. For each theme, list the sub-themes or sub-areas
3. For each sub-theme, name 1-3 specific points, instances, mechanisms, or findings discussed in the sources

Format your response as a structured list using this exact pattern for each theme:

THEME: [theme name]
DESCRIPTION: [1-2 sentence description]
  SUBTHEME: [sub-theme name]
  DESCRIPTION: [1 sentence description]
    POINT: [specific point, instance, or finding]
    POINT: [specific point, instance, or finding]
  SUBTHEME: [sub-theme name]
  DESCRIPTION: [1 sentence description]
    POINT: [specific point, instance, or finding]

Cover ALL major themes relevant to the research question. Be comprehensive."""


_CITATION_DIRECTIVE = (
    "Citation rules (the validator rejects pages that break them):\n"
    "- Every interpretive sentence — including concluding statements, tensions, "
    "and trade-off summaries — MUST end with an inline footnote reference like "
    "`[1]` (or `[2, 3]`, `[4-6]`).\n"
    "- Every `[N]` reference must resolve to a `[^N]: [[sources/<id>]]` definition "
    "you include at the end of your response.\n"
    "- Structural-frame bullets like `**Themes Used In:**`, `**Items Compared:**`, "
    "or `**Which themes draw on it:**` describe the analysis frame and do not need "
    "per-line citations — but any prose sentence following them does.\n"
    "- A single opening sentence per `##` section MAY aggregate across the corpus "
    "(e.g., \"Based on the provided sources, several patterns emerge…\") without "
    "inline citation; the page's enumerated constituent list grounds it. All "
    "subsequent prose still requires inline `[N]` citations. Never use `[[corpus]]` "
    "or similar hand-wave aggregate tokens — the validator rejects them."
)


_SPECIFICS_TEMPLATE = """In the context of the research question "{research_query}", and for the theme "{branch_name}" ({branch_description}), what specific points, instances, mechanisms, frameworks, or findings does the corpus document? For each one, describe:
- Its name and the key claim or contribution
- The core approach, mechanism, or supporting evidence
- Any concrete details (numbers, examples, named protocols, outcomes) the sources report

Be specific.

{citation_directive}"""


_COMPARISONS_TEMPLATE = """In the context of the research question "{research_query}", and for the theme "{branch_name}", how do the different points, frameworks, or approaches compare? Consider:
- Differences in evidence, outcomes, or stated claims
- Trade-offs or contexts where each applies
- Strengths and weaknesses noted in the sources

Be specific about which items you are comparing.

{citation_directive}"""


_GAPS_TEMPLATE = """In the context of the research question "{research_query}", and for the theme "{branch_name}", what unresolved questions, limitations, gaps in coverage, or unanswered tensions are identified in the sources? What does the corpus NOT address that a careful reader would want answered?

Be specific.

{citation_directive}"""


_RECURRING_PATTERNS_PROMPT = """Looking across ALL themes in this corpus, what frameworks, patterns, principles, or approaches appear in multiple sub-areas? For each cross-cutting element, identify which themes use it and explain how it is adapted or applied across those themes.

{citation_directive}"""


_SHARED_ANCHORS_PROMPT = """What authoritative sources, standards, primary references, datasets, or foundational works are cited across multiple themes in this corpus? For each shared anchor, describe:
- What it is and what it contains
- Which themes draw on it
- Why it is treated as foundational or load-bearing for those themes

{citation_directive}"""


_RECURRING_TRADEOFFS_PROMPT = """What recurring trade-offs or tensions surface across different themes and approaches in this corpus? Consider:
- Competing objectives (e.g., precision vs. flexibility, cost vs. coverage, formality vs. agility)
- Context-dependent choices where the right answer changes
- Trade-offs noted explicitly in the sources

For each trade-off, give specific examples from different themes.

{citation_directive}"""


_DEFAULT_INVESTIGATION_TEMPLATES: dict[str, str] = {
    "specifics": _SPECIFICS_TEMPLATE,
    "comparisons": _COMPARISONS_TEMPLATE,
    "gaps": _GAPS_TEMPLATE,
}


_DEFAULT_SYNTHESIS_QUERIES: dict[str, str] = {
    "recurring_patterns": _RECURRING_PATTERNS_PROMPT,
    "shared_anchors": _SHARED_ANCHORS_PROMPT,
    "recurring_tradeoffs": _RECURRING_TRADEOFFS_PROMPT,
}


# --- result dataclass ------------------------------------------------------


@dataclass
class AnalysisResult:
    """Outcome of a full taxonomy → investigate → synthesize run.

    `taxonomy` is a dict shaped like::

        {
          "field": <research_query>,
          "branches": [
            {"name": ..., "description": ..., "sub_branches": [
              {"name": ..., "description": ..., "methods": [...]},
            ]},
          ],
          "citations": {1: "<nlm_source_id>", ...},
          "sources_used": [...],
        }

    `findings` maps `branch_name -> {methods, comparisons, open_problems}`,
    where each inner value is a `{answer, citations, sources_used}` dict
    (or a dict with an `error` key if that branch query failed).

    `synthesis` maps `query_name -> {answer, citations, sources_used}` —
    same shape as `findings`, just keyed by synthesis query name.

    `errors` is a flat list of human-readable error strings — one per
    failed phase / branch / query. The orchestrator surfaces this in the
    final report; it is not a hard failure.
    """

    domain: str
    research_query: str
    notebook_id: str
    taxonomy: dict
    findings: dict[str, dict]
    synthesis: dict[str, dict]
    errors: list[str] = field(default_factory=list)


# --- salvage helpers --------------------------------------------------------


def _slugify_branch(name: str) -> str:
    """Return a filesystem-safe slug for a branch name, collision-safe via hash."""
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:40]
    # 8-char hash suffix makes same-prefix names unique
    h = format(hash(name) & 0xFFFFFFFF, "08x")
    return f"{slug}-{h}"


def _findings_dir(session_id: str) -> Path:
    return paths.nlm_dir() / "findings" / session_id


def _write_branch_finding(session_id: str, branch_name: str, data: dict) -> None:
    d = _findings_dir(session_id)
    d.mkdir(parents=True, exist_ok=True)
    slug = _slugify_branch(branch_name)
    (d / f"{slug}.json").write_text(json.dumps(data))


def load_branch_findings(session_id: str) -> dict[str, dict] | None:
    """Load per-branch findings from disk.

    Returns None if the findings directory is absent or any file is stale
    (older than FINDINGS_STALE_HOURS). Returns a dict mapping branch_name →
    finding dict when all files are fresh.
    """
    d = _findings_dir(session_id)
    if not d.is_dir():
        return None
    files = [f for f in d.glob("*.json") if not f.name.startswith("_")]
    if not files:
        return None
    cutoff = time.time() - FINDINGS_STALE_HOURS * 3600
    result: dict[str, dict] = {}
    for f in files:
        if f.stat().st_mtime < cutoff:
            return None
        data = json.loads(f.read_text())
        branch = data.get("branch")
        if branch:
            result[branch] = data
    return result or None


# --- public entry point ----------------------------------------------------


def analyze(
    notebook_id: str,
    *,
    domain: str,
    research_query: str,
    client: "NlmClient",
    session_id: str | None = None,
    prefetched_findings: dict[str, dict] | None = None,
    custom_taxonomy_prompt: str | None = None,
    custom_investigation_templates: dict[str, str] | None = None,
    custom_synthesis_queries: dict[str, str] | None = None,
) -> AnalysisResult:
    """Run taxonomy → per-branch investigation → cross-cutting synthesis.

    Each phase calls `client.notebook_query(notebook_id, prompt)` and
    parses `{answer, citations, sources_used}`. Errors in one branch /
    one query don't abort the run — they're logged into the result with
    an `error` key on the failed entry and a human-readable line in
    `AnalysisResult.errors`.

    `session_id`: when set, per-branch findings are written to
    `nlm/findings/<session_id>/<slug>.json` after each branch completes.
    `prefetched_findings`: branch_name → finding dict loaded from a prior
    run; matching branches skip NLM calls entirely.
    `custom_*` kwargs override per-domain templates. Unset means use the
    ported defaults from research-notebook.
    """
    errors: list[str] = []

    # Phase 1 — taxonomy. If the taxonomy itself fails, we can't drive
    # phase 2; record the error and continue with an empty taxonomy so
    # phase 3 still runs.
    taxonomy_prompt = custom_taxonomy_prompt or _TAXONOMY_PROMPT
    try:
        taxonomy = _extract_taxonomy(
            notebook_id,
            client,
            prompt=taxonomy_prompt,
            research_query=research_query,
        )
    except Exception as e:  # noqa: BLE001 — mirror per-phase isolation policy
        errors.append(f"taxonomy: {e}")
        taxonomy = {
            "field": research_query,
            "branches": [],
            "citations": {},
            "sources_used": [],
        }

    # Phase 2 — investigate each branch. One branch failure is logged
    # and skipped; the rest still run.
    investigation_templates = dict(_DEFAULT_INVESTIGATION_TEMPLATES)
    if custom_investigation_templates:
        investigation_templates.update(custom_investigation_templates)

    prefetched = prefetched_findings or {}
    findings: dict[str, dict] = {}
    for branch in taxonomy.get("branches", []):
        name = branch.get("name", "")
        if not name:
            continue
        if name in prefetched:
            findings[name] = prefetched[name]
            continue
        try:
            findings[name] = _investigate_branch(
                notebook_id,
                client,
                branch,
                investigation_templates,
                research_query=research_query,
            )
        except Exception as e:  # noqa: BLE001
            errors.append(f"investigate[{name}]: {e}")
            findings[name] = {"branch": name, "error": str(e)}
        if session_id:
            _write_branch_finding(session_id, name, findings[name])

    # Phase 3 — cross-cutting synthesis.
    synthesis_queries = custom_synthesis_queries or _DEFAULT_SYNTHESIS_QUERIES
    synthesis = _synthesize_themes(
        notebook_id,
        client,
        synthesis_queries,
        errors=errors,
    )

    return AnalysisResult(
        domain=domain,
        research_query=research_query,
        notebook_id=notebook_id,
        taxonomy=taxonomy,
        findings=findings,
        synthesis=synthesis,
        errors=errors,
    )


# --- phase helpers (private) ------------------------------------------------


def _try_parse_taxonomy_json(answer: str) -> list[dict] | None:
    """Try to parse a JSON-formatted taxonomy answer; return None if not JSON."""
    stripped = answer.strip()
    if not stripped.startswith("{"):
        return None
    try:
        data = json.loads(stripped)
        branches = data.get("branches")
        if isinstance(branches, list):
            return branches
    except (json.JSONDecodeError, AttributeError):
        pass
    return None


def _extract_taxonomy(
    notebook_id: str,
    client: "NlmClient",
    *,
    prompt: str,
    research_query: str,
) -> dict:
    """Phase 1 — query the corpus for a hierarchical taxonomy.

    The default prompt is anchored on `research_query` so the taxonomy
    is scoped to what was actually researched. A caller-supplied custom
    prompt may or may not contain `{research_query}`; we substitute only
    when the placeholder is present (so domain-specific prompts that
    don't need anchoring still work).

    The answer may be either THEME/SUBTHEME text format or a JSON object
    with a "branches" key (the latter accepted so tests can inject
    structured branches without the text parser).
    """
    formatted = (
        prompt.format(research_query=research_query)
        if "{research_query}" in prompt
        else prompt
    )
    raw = client.notebook_query(notebook_id, formatted)
    answer = raw.get("answer", "")
    # Try JSON first (test injection path and future structured responses)
    branches = _try_parse_taxonomy_json(answer) or _parse_taxonomy_response(answer)
    return {
        "field": research_query,
        "branches": branches,
        "citations": raw.get("citations", {}),
        "sources_used": raw.get("sources_used", []),
    }


def _investigate_branch(
    notebook_id: str,
    client: "NlmClient",
    branch: dict,
    templates: dict[str, str],
    *,
    research_query: str,
) -> dict:
    """Phase 2 — run METHODS / COMPARISONS / OPEN_PROBLEMS for one branch.

    Per-query failures are caught here so a single failing template
    doesn't sink the rest of the branch; the entry gets an `error` key
    and an empty answer. A truly unrecoverable error (e.g. malformed
    branch dict) propagates up to `analyze`, where it's recorded against
    the whole branch.
    """
    name = branch["name"]
    desc = branch.get("description") or name

    findings: dict[str, dict] = {"branch": name}
    for query_name, template in templates.items():
        prompt = template.format(
            branch_name=name,
            branch_description=desc,
            research_query=research_query,
            citation_directive=_CITATION_DIRECTIVE,
        )
        try:
            findings[query_name] = client.notebook_query(notebook_id, prompt)
        except Exception as e:  # noqa: BLE001
            findings[query_name] = {
                "answer": "",
                "citations": {},
                "sources_used": [],
                "error": str(e),
            }
    return findings


def _synthesize_themes(
    notebook_id: str,
    client: "NlmClient",
    queries: dict[str, str],
    *,
    errors: list[str] | None = None,
) -> dict[str, dict]:
    """Phase 3 — run corpus-wide cross-cutting queries.

    Each query is independent: a failing query is caught, recorded with
    an `error` key, and the next one runs. If `errors` is supplied,
    failures are also appended to that list (so they surface in
    `AnalysisResult.errors`).
    """
    synthesis: dict[str, dict] = {}
    for query_name, prompt in queries.items():
        # `{citation_directive}` is the only placeholder in default queries;
        # custom queries that don't use it still work via the conditional.
        if "{citation_directive}" in prompt:
            prompt = prompt.format(citation_directive=_CITATION_DIRECTIVE)
        try:
            synthesis[query_name] = client.notebook_query(notebook_id, prompt)
        except Exception as e:  # noqa: BLE001
            synthesis[query_name] = {
                "answer": "",
                "citations": {},
                "sources_used": [],
                "error": str(e),
            }
            if errors is not None:
                errors.append(f"synthesis[{query_name}]: {e}")
    return synthesis


# --- taxonomy parsing -------------------------------------------------------


def _parse_taxonomy_response(answer: str) -> list[dict]:
    """Parse the structured THEME / SUBTHEME / POINT response into branches.

    Accepts the legacy AREA / SUB / METHOD labels too (used by older
    prompts and any stale fixtures) so the parser is resilient to label
    drift in either direction. Tolerant of trailing markdown emphasis
    (`*name*`) on theme / sub-theme headers.

    Internal dict keys remain stable: each branch has
    `{name, description, sub_branches: [{name, description, points: [...]}]}`.
    """
    branches: list[dict] = []
    current_branch: dict | None = None
    current_sub: dict | None = None

    for line in answer.split("\n"):
        line = line.strip()
        if not line:
            continue

        if line.startswith("THEME:") or line.startswith("AREA:"):
            if current_branch is not None:
                if current_sub is not None:
                    current_branch["sub_branches"].append(current_sub)
                    current_sub = None
                branches.append(current_branch)
            current_branch = {
                "name": line.split(":", 1)[1].strip().strip("*"),
                "description": "",
                "sub_branches": [],
            }
        elif line.startswith("DESCRIPTION:") and current_branch is not None:
            desc = line.split(":", 1)[1].strip()
            if current_sub is not None:
                current_sub["description"] = desc
            else:
                current_branch["description"] = desc
        elif (line.startswith("SUBTHEME:") or line.startswith("SUB:")) and current_branch is not None:
            if current_sub is not None:
                current_branch["sub_branches"].append(current_sub)
            current_sub = {
                "name": line.split(":", 1)[1].strip().strip("*"),
                "description": "",
                "points": [],
            }
        elif (line.startswith("POINT:") or line.startswith("METHOD:")) and current_sub is not None:
            current_sub["points"].append(line.split(":", 1)[1].strip())

    if current_sub is not None and current_branch is not None:
        current_branch["sub_branches"].append(current_sub)
    if current_branch is not None:
        branches.append(current_branch)

    return branches
