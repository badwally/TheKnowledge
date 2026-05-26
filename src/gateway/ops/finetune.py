"""Filter fine-tuning loop per WIKI § 10.4.

Two operations:

1. **trigger_state(domain)** — examples-per-domain accounting against the
   `_TRIGGER_THRESHOLD`. Cheap, deterministic, no LLM. Used by tooling
   (CLI, MCP) to decide whether a domain is ready for distillation.

2. **distill_prompt(domain, client)** — when a domain crosses the threshold,
   feeds the example bank to Claude and asks for a tighter, distilled
   inclusion/exclusion rubric extracted from the patterns observed. The
   distilled output is written to `.knowledge/policies/<d>/policy_versions/
   <timestamp>.yaml` as a CANDIDATE — never overwriting the live
   `policy.yaml`. Reviewing and promoting a candidate is a human step.

Why hybrid (not full fine-tuning): a distilled-prompt extraction is the
practical path while example counts are below the open-weight-model
threshold. The dataclass + writer separation here also makes it easy to
swap the distillation step for a real classifier once the per-domain
example bank crosses ~1000 high-quality decisions.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml

from gateway import paths
from gateway.filter import examples as example_bank
from gateway.filter.policy import load_policy, policy_exists
from gateway.filter.semantic import ClaudeCLIFilterClient, FilterClient
from gateway.ops.calibration import score_calibration


_TRIGGER_THRESHOLD = 500  # per-domain, per WIKI § 10.4
_MAX_EXAMPLES_IN_PROMPT = 80
_MAX_RATIONALE_CHARS = 240


@dataclass(frozen=True)
class TriggerState:
    domain: str
    count: int
    threshold: int
    ready: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "domain": self.domain,
            "count": self.count,
            "threshold": self.threshold,
            "ready": self.ready,
        }


def trigger_state(domain: str, *, threshold: int = _TRIGGER_THRESHOLD) -> TriggerState:
    """Return whether `domain`'s example bank is large enough to distill."""
    count = len(example_bank.load_all(domain))
    return TriggerState(domain=domain, count=count, threshold=threshold, ready=count >= threshold)


def trigger_states_all(*, threshold: int = _TRIGGER_THRESHOLD) -> list[TriggerState]:
    """Return one TriggerState per domain that has any policy.yaml."""
    root = paths.policies_dir()
    if not root.exists():
        return []
    out: list[TriggerState] = []
    for d in sorted(root.iterdir()):
        if not d.is_dir():
            continue
        if (d / "policy.yaml").exists():
            out.append(trigger_state(d.name, threshold=threshold))
    return out


# --- distill ---------------------------------------------------------------


def policy_versions_dir(domain: str) -> Path:
    return paths.policies_dir() / domain / "policy_versions"


def _excerpt(text: str, limit: int) -> str:
    text = (text or "").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rsplit(" ", 1)[0] + "…"


def _build_prompt(domain: str, current_policy: dict[str, Any], examples: list[example_bank.Example]) -> str:
    includes = [e for e in examples if e.decision == "include"]
    excludes = [e for e in examples if e.decision == "exclude"]

    # Cap each side roughly proportional to the prompt budget.
    half = max(1, _MAX_EXAMPLES_IN_PROMPT // 2)
    include_sample = includes[:half]
    exclude_sample = excludes[:half]

    lines: list[str] = [
        f"You are distilling editorial policy for the domain '{domain}'.",
        "",
        "Current policy (live):",
        "  topic: " + str(current_policy.get("domain", {}).get("topic", "")),
        "  inclusion_criteria:",
    ]
    for c in current_policy.get("inclusion_criteria", []) or []:
        lines.append(f"    - {c}")
    lines.append("  exclusion_criteria:")
    for c in current_policy.get("exclusion_criteria", []) or []:
        lines.append(f"    - {c}")
    lines.extend(["", f"INCLUDED examples ({len(include_sample)} of {len(includes)}):"])
    for e in include_sample:
        title = (e.frontmatter_snapshot or {}).get("title") or e.source_id
        lines.append(f"- [{e.source_id}] {title}")
        lines.append(f"    rationale: {_excerpt(e.rationale, _MAX_RATIONALE_CHARS)}")

    lines.extend(["", f"EXCLUDED examples ({len(exclude_sample)} of {len(excludes)}):"])
    for e in exclude_sample:
        title = (e.frontmatter_snapshot or {}).get("title") or e.source_id
        lines.append(f"- [{e.source_id}] {title}")
        lines.append(f"    rationale: {_excerpt(e.rationale, _MAX_RATIONALE_CHARS)}")

    lines.extend([
        "",
        "Task: produce a DISTILLED policy that:",
        "1. Tightens `inclusion_criteria` so it covers the patterns observed in INCLUDES.",
        "2. Tightens `exclusion_criteria` so it explains the EXCLUDES the existing policy",
        "   already filters out.",
        "3. Adds at most 3 NEW criteria on each side that are clearly evidenced by the",
        "   examples but missing from the current policy.",
        "4. Removes criteria that are redundant or never appear to discriminate.",
        "5. Preserves domain.topic, domain.field, domain.description verbatim.",
        "",
        "Be conservative: small, evidence-grounded edits. Keep the same shape.",
        "",
        "Respond with a single JSON object — no prose, no markdown fences:",
        '{"inclusion_criteria": ["...", "..."], "exclusion_criteria": ["...", "..."],',
        ' "summary": "<one paragraph describing the patterns observed>"}',
    ])
    return "\n".join(lines)


_JSON_OBJECT_RE = re.compile(r"\{.*\}", re.DOTALL)


def _parse_response(raw: str) -> dict[str, Any] | None:
    if not raw:
        return None
    match = _JSON_OBJECT_RE.search(raw)
    if not match:
        return None
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict):
        return None
    inc = data.get("inclusion_criteria")
    exc = data.get("exclusion_criteria")
    if not isinstance(inc, list) or not isinstance(exc, list):
        return None
    return {
        "inclusion_criteria": [str(x) for x in inc if isinstance(x, str)],
        "exclusion_criteria": [str(x) for x in exc if isinstance(x, str)],
        "summary": str(data.get("summary", "")).strip(),
    }


def _now_path_token() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass(frozen=True)
class DistillResult:
    domain: str
    candidate_path: Path
    examples_used: int
    summary: str
    calibration_f1: float | None = None


class DistillError(RuntimeError):
    """Raised when distillation cannot proceed (no policy, no examples, parse failure)."""


def distill_prompt(
    domain: str,
    *,
    client: FilterClient | None = None,
    threshold: int = _TRIGGER_THRESHOLD,
    enforce_threshold: bool = True,
) -> DistillResult:
    """Run distillation for `domain`. Writes a candidate policy version
    under `.knowledge/policies/<domain>/policy_versions/<timestamp>.yaml`
    — the live `policy.yaml` is never overwritten.

    `enforce_threshold=False` skips the trigger check (useful for ops that
    want to distill early under a tighter sample).
    """
    if not policy_exists(domain):
        raise DistillError(f"no policy.yaml for domain {domain!r}")

    examples = example_bank.load_all(domain)
    state = trigger_state(domain, threshold=threshold)
    if enforce_threshold and not state.ready:
        raise DistillError(
            f"domain {domain!r} below distillation threshold: "
            f"{state.count}/{state.threshold} examples"
        )
    if not examples:
        raise DistillError(f"domain {domain!r} has no examples to distill")

    policy = load_policy(domain)
    prompt = _build_prompt(domain, policy.raw, examples)
    client = client or ClaudeCLIFilterClient()

    response = client.call(prompt)
    parsed = _parse_response(response)
    if parsed is None:
        raise DistillError(
            f"distillation response unparseable for {domain!r}: "
            f"{response[:200] if response else '(empty)'}"
        )

    candidate = dict(policy.raw)
    candidate["version"] = _next_version(policy.version)
    candidate["distilled"] = {
        "from_examples": len(examples),
        "from_policy_version": policy.version,
        "distilled_at": _now_iso(),
        "summary": parsed["summary"],
    }
    candidate["inclusion_criteria"] = parsed["inclusion_criteria"]
    candidate["exclusion_criteria"] = parsed["exclusion_criteria"]

    # QUAL-10: score against held-out calibration set if one exists
    calibration_f1: float | None = None
    cal_metrics = score_calibration(
        domain,
        parsed["inclusion_criteria"],
        parsed["exclusion_criteria"],
        client=client,
    )
    if cal_metrics is not None:
        calibration_f1 = cal_metrics.f1
        candidate["calibration_metrics"] = {
            **cal_metrics.to_dict(),
            "scored_at": _now_iso(),
        }

    target_dir = policy_versions_dir(domain)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"{_now_path_token()}.yaml"
    target.write_text(yaml.safe_dump(candidate, sort_keys=False, allow_unicode=True))

    return DistillResult(
        domain=domain,
        candidate_path=target,
        examples_used=len(examples),
        summary=parsed["summary"],
        calibration_f1=calibration_f1,
    )


_VERSION_NUM_RE = re.compile(r"^v(\d+)$")


def _next_version(current: str) -> str:
    match = _VERSION_NUM_RE.match(current)
    if not match:
        return f"{current}-distilled"
    return f"v{int(match.group(1)) + 1}"
