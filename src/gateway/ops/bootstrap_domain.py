"""`wiki bootstrap-domain "<description>" <slug>` — author a starter policy.

Restores the predecessor's top-down green-field workflow: take a
natural-language description of a new domain, have Claude draft a
policy.yaml, validate strictly, and write to the policies directory.

Bug-prevention measures (M39 design):
- Single synthetic reference policy in the prompt (no real-domain leakage).
- Strict validator gates minimum-specificity (≥3 inclusion criteria, etc.).
- Refusal-with-hint on collisions with promoted policies or open proposals.
- Single retry on underspecified response; draft-save on second failure.
- `policy_schema_version` stamped on every output.
"""

from __future__ import annotations

import hashlib
import json
import re
from typing import TYPE_CHECKING

import yaml

from gateway import frontmatter as fm
from gateway import log, paths, wiki_pages
from gateway.core import OperationResult, write_atomic
from gateway.filter.policy import policy_path
from gateway.locking import file_lock
from gateway.ops.policy_validator import (
    POLICY_SCHEMA_VERSION,
    REFERENCE_POLICY_PATH,
    validate_policy,
)

if TYPE_CHECKING:
    from gateway.plan import PlanClient


_LOCK_NAME = "wiki-author"
_SHORT_DESCRIPTION_THRESHOLD = 20  # words
_OBJECT_RE = re.compile(r"\{[\s\S]*\}")


_PROMPT_TEMPLATE = """\
You are authoring an editorial policy for a personal knowledge base. The
policy gates which sources are accepted into a research domain via a
semantic filter. Below is the user's natural-language description of the
new domain, followed by a synthetic reference policy that demonstrates
the schema. Produce a policy YAML for the user's domain — do NOT copy
content from the reference; use it only as a structural template.

## User description

{description}

## Required slug

{slug}

## Reference policy (structural template only — do NOT copy content)

```yaml
{reference}
```

## Requirements

Your output must be a single YAML document (or a JSON object with the
same structure). It must include:

- `version: v1`
- `policy_schema_version: {schema_version}`
- `domain.slug: {slug}` (lowercase, hyphenated; must match exactly)
- `domain.topic`, `domain.field`, `domain.description` (one to three sentences each)
- `filter.threshold_include` (0.0-1.0, suggested 0.65-0.75)
- `filter.threshold_review` (0.0-1.0, lower than threshold_include)
- `inclusion_criteria`: at least 3 specific, concrete criteria. Each
  should describe a recognizable signal — what the source must discuss,
  cover, or report. Avoid vague verbs like "is interesting" or
  "is high-quality". Anchor each criterion in domain-specific terminology.
- `exclusion_criteria`: at least 1 specific exclusion (hard gate).
- `quality_signals`: at least 2 categories (e.g. publication_venue,
  content_depth), each with at least 2 total signals across
  positive_signals and negative_signals.
- If this domain is likely to draw substantially on video or talk sources
  (recorded lectures, conference keynotes and seminars, YouTube explainers,
  podcast or interview transcripts), you MUST also include `channel_authority`
  and `speaker_expertise` as `quality_signals` categories. Video and audio
  metadata (titles, descriptions) systematically under-represent the actual
  content, so the filter has to weight source authority instead. Shape them
  like the other categories: `positive_signals` for recognized institutions,
  established venues and events, and credentialed or well-known speakers;
  `negative_signals` for influencer or growth-marketing channels with no track
  record and content that mainly upsells a product, course, or newsletter. Use
  terminology specific to THIS domain's institutions, venues, and practitioners
  — do not copy generic examples. If the domain is unlikely to use video or
  talk sources (e.g. a pure lab-science, archival-text, or numerical field),
  omit these two categories.

Return ONLY the YAML or JSON. No prose, no markdown fences.
"""


def bootstrap_domain(
    description: str,
    slug: str,
    *,
    plan_client: "PlanClient | None" = None,
    force: bool = False,
) -> OperationResult:
    """Author a starter policy from a natural-language description."""
    description = (description or "").strip()
    if not description:
        return OperationResult(success=False, errors=["description must be non-empty"])
    if not wiki_pages.is_valid_slug(slug):
        return OperationResult(
            success=False,
            errors=[f"slug {slug!r} is not a valid slug (lowercase, hyphenated)"],
        )

    proposal_path = paths.wiki_dir() / "proposals" / f"{slug}.md"
    if proposal_path.exists():
        try:
            prop_front, _ = fm.parse(proposal_path.read_text())
            if prop_front.get("status") == "draft":
                return OperationResult(
                    success=False,
                    errors=[
                        f"draft proposal exists at {proposal_path.relative_to(paths.knowledge_root())}; "
                        f"run `wiki promote-domain {slug}` to use the proposal's clustered "
                        f"sources, `wiki reject-proposal {slug}` to discard, or pick a "
                        f"different slug"
                    ],
                )
        except fm.FrontmatterError:
            pass

    target = policy_path(slug)
    if target.exists():
        existing_promoted = _is_promoted_policy(target)
        if existing_promoted:
            return OperationResult(
                success=False,
                errors=[
                    f"policy at {target.relative_to(paths.knowledge_root())} was generated "
                    f"from a proposal (auto_generated_from_proposal=true); run "
                    f"`wiki demote-domain {slug}` first to remove the back-tags before "
                    f"bootstrapping a replacement"
                ],
            )
        if not force:
            return OperationResult(
                success=False,
                errors=[
                    f"policy at {target.relative_to(paths.knowledge_root())} already exists; "
                    f"pass --force to overwrite"
                ],
            )

    if plan_client is None:
        from gateway.llm import model_for
        from gateway.plan import ClaudeCLIPlanClient

        # M46-followup Fix E: bootstrap-domain is bounded structural
        # authoring (policy.yaml generation). Sonnet handles it well
        # at lower cost; reserve Opus for multi-page wiki authorship.
        plan_client = ClaudeCLIPlanClient(model=model_for("plan_bootstrap_domain"))

    warnings: list[str] = []
    if len(description.split()) < _SHORT_DESCRIPTION_THRESHOLD:
        warnings.append(
            f"description is short (<{_SHORT_DESCRIPTION_THRESHOLD} words); "
            f"specificity of resulting criteria may suffer"
        )
    if force and target.exists():
        warnings.append(f"--force overwrote existing policy at {target}")

    reference = REFERENCE_POLICY_PATH.read_text()
    prompt = _PROMPT_TEMPLATE.format(
        description=description,
        slug=slug,
        reference=reference,
        schema_version=POLICY_SCHEMA_VERSION,
    )

    # K5 telemetry: bootstrap is rare (per new domain) but expensive (Sonnet
    # for structural generation). Worth recording.
    call_with_usage = getattr(plan_client, "call_with_usage", None)
    last_errors: list[str] = []
    last_data: dict | None = None
    for attempt in range(2):
        current_prompt = prompt if attempt == 0 else _retry_prompt(prompt, last_errors)
        try:
            if callable(call_with_usage):
                from gateway.log import log_llm_call

                result = call_with_usage(current_prompt)
                log_llm_call("plan_bootstrap_domain", result, extra={"attempt": attempt})
                raw = result.text
            else:
                raw = plan_client.call(current_prompt)
        except Exception as e:  # noqa: BLE001
            return OperationResult(
                success=False,
                errors=[f"plan client failed: {e}"],
                warnings=warnings,
            )

        try:
            data = _parse_response(raw)
        except ValueError as e:
            last_errors = [f"parse failed: {e}"]
            last_data = None
            continue

        data.setdefault("version", "v1")
        data["policy_schema_version"] = POLICY_SCHEMA_VERSION
        if isinstance(data.get("domain"), dict):
            data["domain"]["slug"] = slug
        data["bootstrapped_from_description_hash"] = _hash_description(description)

        result = validate_policy(data, mode="strict")
        if result.ok:
            return _commit_policy(slug, data, warnings + [str(w) for w in result.warnings])

        last_errors = [str(e) for e in result.errors]
        last_data = data

    if last_data is not None:
        draft_path = paths.policies_dir() / slug / "policy.draft.yaml"
        draft_path.parent.mkdir(parents=True, exist_ok=True)
        write_atomic(draft_path, _serialize_yaml(last_data))
        return OperationResult(
            success=False,
            errors=last_errors
            + [
                f"saved best-effort draft to {draft_path.relative_to(paths.knowledge_root())}; "
                f"hand-edit and rename to policy.yaml when ready"
            ],
            warnings=warnings,
            paths_touched=[draft_path],
        )

    return OperationResult(success=False, errors=last_errors, warnings=warnings)


def _commit_policy(slug: str, data: dict, warnings: list[str]) -> OperationResult:
    target = policy_path(slug)
    examples_dir = paths.policies_dir() / slug / "examples"
    paths_touched = []
    with file_lock(_LOCK_NAME):
        target.parent.mkdir(parents=True, exist_ok=True)
        examples_dir.mkdir(parents=True, exist_ok=True)
        write_atomic(target, _serialize_yaml(data))
        paths_touched.append(target)
        log.append(
            op="bootstrap-domain",
            fields={
                "slug": slug,
                "inclusion_count": len(data.get("inclusion_criteria") or []),
                "exclusion_count": len(data.get("exclusion_criteria") or []),
            },
            summary=f"authored policy for {slug} from description",
        )
        paths_touched.append(paths.log_path())

    return OperationResult(
        success=True,
        paths_touched=paths_touched,
        summary=f"bootstrapped policy for {slug}",
        warnings=warnings,
    )


def _is_promoted_policy(path) -> bool:
    try:
        data = yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError:
        return False
    return bool(data.get("auto_generated_from_proposal"))


def _parse_response(text: str) -> dict:
    if not text or not text.strip():
        raise ValueError("empty response from plan client")
    cleaned = text.strip()
    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()

    try:
        obj = json.loads(cleaned)
        if isinstance(obj, dict):
            return obj
    except json.JSONDecodeError:
        pass

    try:
        obj = yaml.safe_load(cleaned)
        if isinstance(obj, dict):
            return obj
    except yaml.YAMLError:
        pass

    match = _OBJECT_RE.search(cleaned)
    if match:
        try:
            obj = json.loads(match.group(0))
            if isinstance(obj, dict):
                return obj
        except json.JSONDecodeError as e:
            raise ValueError(f"could not parse response as JSON or YAML: {e}") from e

    raise ValueError(f"could not parse response (preview: {cleaned[:200]!r})")


def _serialize_yaml(data: dict) -> str:
    header = (
        "# Authored by `wiki bootstrap-domain` from a natural-language description.\n"
        "# Edit freely; re-run `wiki refine-domain` to evolve the policy.\n\n"
    )
    return header + yaml.safe_dump(data, sort_keys=False, default_flow_style=False)


def _retry_prompt(original: str, errors: list[str]) -> str:
    err_block = "\n".join(f"- {e}" for e in errors)
    return (
        original
        + "\n\n## Previous attempt failed validation with:\n\n"
        + err_block
        + "\n\nReturn a corrected policy that addresses every error above. "
        + "Be more specific in inclusion_criteria and quality_signals."
    )


def _hash_description(description: str) -> str:
    return hashlib.sha256(description.encode("utf-8")).hexdigest()[:16]
