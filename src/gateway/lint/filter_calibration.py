"""Filter-calibration check.

Per WIKI § 12.2: re-score a random sample of past filter decisions against
the current policy version; report mean delta and per-source outliers
(|delta| > `_OUTLIER_THRESHOLD`).

Cost: `sample_size` × |domains_with_policy| Claude calls. Default sample_size
is small (5) because each call is 5–30s. The check is opt-in for a full
sample by passing a larger value to `run()`.

When a domain lacks `.knowledge/policies/<domain>/policy.yaml`, the check
emits a single info finding noting the gap and continues. (No samples can
be re-scored without a policy; populating policies is upstream work — see
WIKI § 10 and the M19 example-bank backfill milestone.)
"""

from __future__ import annotations

import random
from dataclasses import dataclass

from gateway.filter import (
    Example,
    FilterClient,
    Policy,
    PolicyError,
    load_policy,
    policy_exists,
    score,
)
from gateway.filter.semantic import ClaudeCLIFilterClient
from gateway.lint import LintFinding, SEVERITY_INFO, SEVERITY_WARNING
from gateway.lint._walk import walk_raw_sources


_OUTLIER_THRESHOLD = 0.20  # |delta| above this surfaces a per-source warning
_DEFAULT_SAMPLE_SIZE = 5
_RANDOM_SEED = 12345


@dataclass(frozen=True)
class _ScoredSample:
    source_id: str
    domain: str
    stored_score: float
    new_score: float
    rationale: str
    policy_version: str


def _candidates_by_domain() -> dict[str, list[tuple[str, dict, str]]]:
    """Yield {domain: [(canonical_id, frontmatter, body), ...]} for every raw
    source carrying a `filter.score`."""
    out: dict[str, list[tuple[str, dict, str]]] = {}
    for _, path, front, body in walk_raw_sources():
        filt = front.get("filter") or {}
        if filt.get("score") is None:
            continue
        for d in front.get("domains") or []:
            if not isinstance(d, str):
                continue
            out.setdefault(d, []).append((path.stem, front, body))
    return out


def _sample(items: list, k: int, *, seed: int) -> list:
    if k >= len(items):
        return list(items)
    rng = random.Random(seed)
    return rng.sample(items, k)


def _score_sample(
    front: dict,
    body: str,
    policy: Policy,
    examples: list[Example],
    client: FilterClient,
) -> tuple[float, str, str]:
    result = score(front, body, policy, examples=examples, client=client)
    return result.score, result.rationale, result.policy_version


def _findings_for_domain(domain: str, scored: list[_ScoredSample]) -> list[LintFinding]:
    if not scored:
        return []

    deltas = [s.new_score - s.stored_score for s in scored]
    mean_delta = sum(deltas) / len(deltas)
    abs_deltas = [abs(d) for d in deltas]
    mean_abs = sum(abs_deltas) / len(abs_deltas)

    findings: list[LintFinding] = [
        LintFinding(
            check="filter-calibration",
            severity=SEVERITY_INFO,
            message=(
                f"filter calibration on '{domain}' "
                f"({len(scored)} sampled): mean delta={mean_delta:+.3f}, "
                f"mean |delta|={mean_abs:.3f}"
            ),
            metadata={
                "domain": domain,
                "sample_size": len(scored),
                "mean_delta": round(mean_delta, 3),
                "mean_abs_delta": round(mean_abs, 3),
                "policy_version": scored[0].policy_version,
            },
        )
    ]

    for s in scored:
        delta = s.new_score - s.stored_score
        if abs(delta) <= _OUTLIER_THRESHOLD:
            continue
        findings.append(
            LintFinding(
                check="filter-calibration",
                severity=SEVERITY_WARNING,
                message=(
                    f"filter outlier in '{domain}': source `{s.source_id}` "
                    f"stored={s.stored_score:.2f} new={s.new_score:.2f} "
                    f"delta={delta:+.2f} ({s.rationale[:120]})"
                ),
                metadata={
                    "domain": domain,
                    "source_id": s.source_id,
                    "stored_score": s.stored_score,
                    "new_score": s.new_score,
                    "delta": round(delta, 3),
                    "rationale": s.rationale,
                },
            )
        )
    return findings


def run(
    *,
    sample_size: int = _DEFAULT_SAMPLE_SIZE,
    client: FilterClient | None = None,
) -> list[LintFinding]:
    """Sample-based filter calibration.

    Tests inject a stub `client`; production uses the `claude -p` subprocess.
    """
    by_domain = _candidates_by_domain()
    if not by_domain:
        return []

    if client is None:
        client = ClaudeCLIFilterClient()

    out: list[LintFinding] = []
    for domain, items in sorted(by_domain.items()):
        if not policy_exists(domain):
            out.append(
                LintFinding(
                    check="filter-calibration",
                    severity=SEVERITY_INFO,
                    message=(
                        f"domain '{domain}' has no policy.yaml; calibration skipped "
                        f"(populate `.knowledge/policies/{domain}/policy.yaml` to enable)"
                    ),
                    metadata={"domain": domain, "skipped": "no_policy"},
                )
            )
            continue

        try:
            policy = load_policy(domain)
        except PolicyError as e:
            out.append(
                LintFinding(
                    check="filter-calibration",
                    severity=SEVERITY_WARNING,
                    message=f"policy load failed for '{domain}': {e}",
                    metadata={"domain": domain},
                )
            )
            continue

        sampled = _sample(items, sample_size, seed=_RANDOM_SEED + hash(domain) % 100_000)
        scored: list[_ScoredSample] = []
        for source_id, front, body in sampled:
            try:
                new_score, rationale, policy_version = _score_sample(
                    front, body, policy, examples=[], client=client
                )
            except Exception as e:
                out.append(
                    LintFinding(
                        check="filter-calibration",
                        severity=SEVERITY_WARNING,
                        message=f"score failed for '{domain}/{source_id}': {e!r}",
                        metadata={"domain": domain, "source_id": source_id},
                    )
                )
                continue
            stored = float(front["filter"]["score"])
            scored.append(
                _ScoredSample(
                    source_id=source_id,
                    domain=domain,
                    stored_score=stored,
                    new_score=new_score,
                    rationale=rationale,
                    policy_version=policy_version,
                )
            )
        out.extend(_findings_for_domain(domain, scored))
    return out
