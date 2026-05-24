"""Model selection per LLM stage.

M44: filter routes to Haiku 4.5 (binary triage); plan and VLM stay on Opus 4.7.
M46-followup Fix E (2026-05-23): the single `plan` tier was too coarse —
authorship needs Opus, but bootstrap-domain and query-planner are bounded
structural-generation tasks where Sonnet 4.6 delivers equivalent quality
at ~5x lower cost / faster turnaround. Split into per-purpose stages
(`plan_authorship`, `plan_bootstrap_domain`, `plan_query_planner`); keep
`plan` as a back-compat alias for the authorship default.

Per-domain overrides may be added via `.knowledge/policies/<domain>/model.yaml`
in a follow-up — the resolver is in place but currently returns defaults.
"""

from __future__ import annotations

from typing import Literal


Stage = Literal[
    "filter",
    "plan",                    # back-compat alias → plan_authorship
    "plan_authorship",         # wiki ingest --with-plan (multi-page authorship)
    "plan_bootstrap_domain",   # wiki bootstrap-domain (policy.yaml generation)
    "plan_query_planner",      # wiki research planner (per-adapter query expansion)
    "vlm",
    "cite_suggest",            # M49 wiki cite --suggest (attribution matching)
    "evaluate_judge",          # M50 wiki evaluate (LLM-as-judge over wiki context)
]


DEFAULT_FILTER_MODEL = "claude-haiku-4-5-20251001"
DEFAULT_PLAN_AUTHORSHIP_MODEL = "claude-opus-4-7"
DEFAULT_PLAN_BOOTSTRAP_DOMAIN_MODEL = "claude-sonnet-4-6"
DEFAULT_PLAN_QUERY_PLANNER_MODEL = "claude-sonnet-4-6"
DEFAULT_VLM_MODEL = "claude-opus-4-7"
DEFAULT_CITE_SUGGEST_MODEL = "claude-sonnet-4-6"
DEFAULT_EVALUATE_JUDGE_MODEL = "claude-sonnet-4-6"

# Back-compat aliases for callers that still import these names.
DEFAULT_PLAN_MODEL = DEFAULT_PLAN_AUTHORSHIP_MODEL


def model_for(stage: Stage, domain: str | None = None) -> str:
    """Return the model ID to use for a given stage.

    `domain` is reserved for future per-domain overrides (e.g., a domain
    whose policy needs Opus-level reasoning for filter). Returns the
    default for the stage today.

    Stage values:
      - "filter" → Haiku 4.5 (high-volume binary triage)
      - "plan" → Opus 4.7 (back-compat alias for plan_authorship)
      - "plan_authorship" → Opus 4.7 (`wiki ingest --with-plan`)
      - "plan_bootstrap_domain" → Sonnet 4.6 (`wiki bootstrap-domain`)
      - "plan_query_planner" → Sonnet 4.6 (`wiki research` query expansion)
      - "vlm" → Opus 4.7 (image conversion)
      - "cite_suggest" → Sonnet 4.6 (M49 `wiki cite --suggest`: attribution matching)
      - "evaluate_judge" → Sonnet 4.6 (M50 `wiki evaluate`: LLM-as-judge over wiki context)
    """
    if stage == "filter":
        return DEFAULT_FILTER_MODEL
    if stage == "plan" or stage == "plan_authorship":
        return DEFAULT_PLAN_AUTHORSHIP_MODEL
    if stage == "plan_bootstrap_domain":
        return DEFAULT_PLAN_BOOTSTRAP_DOMAIN_MODEL
    if stage == "plan_query_planner":
        return DEFAULT_PLAN_QUERY_PLANNER_MODEL
    if stage == "vlm":
        return DEFAULT_VLM_MODEL
    if stage == "cite_suggest":
        return DEFAULT_CITE_SUGGEST_MODEL
    if stage == "evaluate_judge":
        return DEFAULT_EVALUATE_JUDGE_MODEL
    raise ValueError(f"unknown LLM stage: {stage!r}")
