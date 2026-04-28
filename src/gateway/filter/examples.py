"""Example bank manager per WIKI.md § 10.2.

Past filter decisions accumulate at
`.knowledge/policies/<domain-slug>/examples/<source-id>.yaml`. The bank is
read at filter-call time; representative examples are folded into the prompt
to give Claude calibration signal.

Three pin reasons:
- "user-correction"   — the user overrode an automated decision (highest signal)
- "high-confidence"   — auto-pinned when the score is far above/below threshold
- "edge-case"         — manually pinned to teach near-threshold judgment
- "legacy-backfill"   — populated by M8 migration from JSON checkpoints
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from gateway.filter.policy import Policy
from gateway import paths


VALID_DECISIONS: set[str] = {"include", "exclude"}
VALID_PIN_REASONS: set[str] = {"user-correction", "high-confidence", "edge-case", "legacy-backfill"}
VALID_STRATEGIES: set[str] = {"balanced", "recent", "corrections-weighted"}


@dataclass
class Example:
    source_id: str
    domain: str
    decision: str
    score: float
    policy_version: str
    rationale: str
    pinned_at: str
    pinned_by: str
    frontmatter_snapshot: dict[str, Any] = field(default_factory=dict)
    content_excerpt: str = ""

    def to_yaml_dict(self) -> dict[str, Any]:
        return {
            "source_id": self.source_id,
            "domain": self.domain,
            "decision": self.decision,
            "score": self.score,
            "policy_version": self.policy_version,
            "rationale": self.rationale,
            "pinned_at": self.pinned_at,
            "pinned_by": self.pinned_by,
            "frontmatter_snapshot": self.frontmatter_snapshot,
            "content_excerpt": self.content_excerpt,
        }


def examples_dir(domain_slug: str) -> Path:
    return paths.policies_dir() / domain_slug / "examples"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def pin(
    *,
    source_id: str,
    domain: str,
    decision: str,
    score: float,
    policy_version: str,
    rationale: str,
    pinned_by: str,
    frontmatter_snapshot: dict[str, Any] | None = None,
    content_excerpt: str = "",
) -> Path:
    """Write or overwrite the example file for `source_id` in `domain`."""
    if decision not in VALID_DECISIONS:
        raise ValueError(f"decision must be one of {VALID_DECISIONS}, got {decision!r}")
    if pinned_by not in VALID_PIN_REASONS:
        raise ValueError(f"pinned_by must be one of {VALID_PIN_REASONS}, got {pinned_by!r}")

    example = Example(
        source_id=source_id,
        domain=domain,
        decision=decision,
        score=float(score),
        policy_version=policy_version,
        rationale=rationale,
        pinned_at=_now_iso(),
        pinned_by=pinned_by,
        frontmatter_snapshot=frontmatter_snapshot or {},
        content_excerpt=content_excerpt[:500],
    )

    target_dir = examples_dir(domain)
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / f"{source_id}.yaml"
    path.write_text(yaml.safe_dump(example.to_yaml_dict(), sort_keys=False, allow_unicode=True))
    return path


def load_all(domain_slug: str) -> list[Example]:
    """Load every example for a domain (no selection)."""
    dir_ = examples_dir(domain_slug)
    if not dir_.exists():
        return []
    out: list[Example] = []
    for path in sorted(dir_.glob("*.yaml")):
        try:
            data = yaml.safe_load(path.read_text()) or {}
        except yaml.YAMLError:
            continue  # skip malformed; lint will catch
        try:
            out.append(Example(
                source_id=data["source_id"],
                domain=data["domain"],
                decision=data["decision"],
                score=float(data["score"]),
                policy_version=data.get("policy_version", "unknown"),
                rationale=data.get("rationale", ""),
                pinned_at=data.get("pinned_at", ""),
                pinned_by=data.get("pinned_by", "unknown"),
                frontmatter_snapshot=data.get("frontmatter_snapshot") or {},
                content_excerpt=data.get("content_excerpt", ""),
            ))
        except (KeyError, TypeError):
            continue
    return out


def select(examples: list[Example], policy: Policy) -> list[Example]:
    """Pick representative examples per the policy's strategy."""
    return _select(examples, policy.example_count_in_prompt, policy.example_strategy)


def _select(examples: list[Example], count: int, strategy: str) -> list[Example]:
    if strategy not in VALID_STRATEGIES:
        raise ValueError(
            f"example_strategy must be one of {VALID_STRATEGIES}, got {strategy!r}"
        )
    if count <= 0 or not examples:
        return []

    if strategy == "recent":
        return sorted(examples, key=lambda e: e.pinned_at, reverse=True)[:count]

    if strategy == "corrections-weighted":
        # Prefer corrections, then high-confidence, then anything
        ordered = sorted(
            examples,
            key=lambda e: (
                0 if e.pinned_by == "user-correction" else 1,
                -_pinned_at_sort_key(e.pinned_at),
            ),
        )
        return ordered[:count]

    # balanced: ~third corrections, third include high-conf, third exclude high-conf
    corrections = [e for e in examples if e.pinned_by == "user-correction"]
    includes = [e for e in examples if e.decision == "include" and e.pinned_by != "user-correction"]
    excludes = [e for e in examples if e.decision == "exclude" and e.pinned_by != "user-correction"]

    per_bucket = max(1, count // 3)

    chosen: list[Example] = []
    for bucket in (corrections, includes, excludes):
        chosen.extend(sorted(bucket, key=lambda e: e.pinned_at, reverse=True)[:per_bucket])

    if len(chosen) < count:
        # Top up from any remaining, recency-ordered
        remaining = [e for e in examples if e not in chosen]
        chosen.extend(sorted(remaining, key=lambda e: e.pinned_at, reverse=True)[: count - len(chosen)])

    return chosen[:count]


def _pinned_at_sort_key(timestamp: str) -> float:
    """Lex sort of ISO-8601 strings is fine for relative ordering; cheap proxy for time."""
    if not timestamp:
        return 0.0
    return float(sum(ord(c) for c in timestamp))
