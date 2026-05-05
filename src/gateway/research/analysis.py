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

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gateway.nlm_client import NlmClient


# --- prompt templates ------------------------------------------------------


_TAXONOMY_PROMPT = """Analyze all sources in this notebook in the context of the following research question:

"{research_query}"

Identify the major research areas, method categories, and architectural families discussed in the sources that are relevant to that question. Scope the taxonomy to what was actually researched — do not invent areas not present in the corpus.

Organize your response as a structured hierarchy with these levels:
1. Top-level research areas (e.g., "Temporal Action Detection", "Video Object Tracking")
2. For each area, list the sub-categories or method families
3. For each sub-category, name 1-3 specific methods or papers discussed in the sources

Format your response as a structured list using this exact pattern for each area:

AREA: [area name]
DESCRIPTION: [1-2 sentence description]
  SUB: [sub-category name]
  DESCRIPTION: [1 sentence description]
    METHOD: [specific method name]
    METHOD: [specific method name]
  SUB: [sub-category name]
  DESCRIPTION: [1 sentence description]
    METHOD: [specific method name]

Cover ALL major areas relevant to the research question. Be comprehensive."""


_METHODS_TEMPLATE = """In the context of the research question "{research_query}", and for the research area "{branch_name}" ({branch_description}), what specific methods and architectures are discussed in the sources? For each method, describe:
- Its name and key contribution
- The core technical approach
- Any reported benchmark results

Be specific and cite sources."""


_COMPARISONS_TEMPLATE = """In the context of the research question "{research_query}", and for the research area "{branch_name}", how do the different methods compare? Consider:
- Accuracy and performance differences
- Computational efficiency and speed
- Scalability to longer videos or larger datasets
- Strengths and weaknesses of each approach

Be specific about which methods you are comparing and cite sources."""


_OPEN_PROBLEMS_TEMPLATE = """In the context of the research question "{research_query}", and for the research area "{branch_name}", what unsolved problems, limitations, or future research directions are identified in the sources? What gaps remain? What challenges do current methods still face?

Be specific and cite sources."""


_SHARED_ARCHITECTURES_PROMPT = """Looking across ALL research areas in this corpus, what architectures or techniques appear in multiple sub-fields? For example, do transformers appear in both action detection and video captioning? Do graph neural networks appear in both tracking and action recognition?

Identify the cross-cutting architectures and explain how they are adapted for different tasks. Cite sources."""


_COMMON_DATASETS_PROMPT = """What benchmark datasets are referenced across multiple research areas in this corpus? For each dataset, describe:
- What it contains (video types, annotations)
- Which research areas use it
- Why it is considered important

Cite sources."""


_RECURRING_TRADEOFFS_PROMPT = """What fundamental trade-offs recur across different methods and research areas in this corpus? Consider:
- Accuracy vs computational efficiency
- Local temporal modeling vs global temporal modeling
- Supervised vs self-supervised approaches
- Model complexity vs generalization
- Real-time capability vs offline accuracy

For each trade-off, give specific examples from different research areas. Cite sources."""


_DEFAULT_INVESTIGATION_TEMPLATES: dict[str, str] = {
    "methods": _METHODS_TEMPLATE,
    "comparisons": _COMPARISONS_TEMPLATE,
    "open_problems": _OPEN_PROBLEMS_TEMPLATE,
}


_DEFAULT_SYNTHESIS_QUERIES: dict[str, str] = {
    "shared_architectures": _SHARED_ARCHITECTURES_PROMPT,
    "common_datasets": _COMMON_DATASETS_PROMPT,
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


# --- public entry point ----------------------------------------------------


def analyze(
    notebook_id: str,
    *,
    domain: str,
    research_query: str,
    client: "NlmClient",
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

    findings: dict[str, dict] = {}
    for branch in taxonomy.get("branches", []):
        name = branch.get("name", "")
        if not name:
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
    """
    formatted = (
        prompt.format(research_query=research_query)
        if "{research_query}" in prompt
        else prompt
    )
    raw = client.notebook_query(notebook_id, formatted)
    branches = _parse_taxonomy_response(raw.get("answer", ""))
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
    """Parse the structured AREA / SUB / METHOD response into branches.

    Ported verbatim from research-notebook's `_parse_taxonomy_response`.
    Tolerant of trailing markdown emphasis (`*name*`) on AREA / SUB
    headers, which NotebookLM occasionally emits.
    """
    branches: list[dict] = []
    current_branch: dict | None = None
    current_sub: dict | None = None

    for line in answer.split("\n"):
        line = line.strip()
        if not line:
            continue

        if line.startswith("AREA:"):
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
        elif line.startswith("SUB:") and current_branch is not None:
            if current_sub is not None:
                current_branch["sub_branches"].append(current_sub)
            current_sub = {
                "name": line.split(":", 1)[1].strip().strip("*"),
                "description": "",
                "methods": [],
            }
        elif line.startswith("METHOD:") and current_sub is not None:
            current_sub["methods"].append(line.split(":", 1)[1].strip())

    if current_sub is not None and current_branch is not None:
        current_branch["sub_branches"].append(current_sub)
    if current_branch is not None:
        branches.append(current_branch)

    return branches
