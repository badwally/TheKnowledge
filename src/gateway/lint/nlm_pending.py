"""NotebookLM-pending check per WIKI § 12.2.

A source belongs in a domain's NotebookLM corpus iff:
- the domain has a notebook registered in nlm/notebooks.yaml,
- the source's filter.score >= the domain's threshold_include,
- the domain is in the source's `domains:` frontmatter,
- the source's `nlm_corpus_ids` does NOT yet include that notebook_id.

This check surfaces sources that pass the bar but haven't been pushed to
NotebookLM yet. Run `wiki nlm-add <domain> <source-id>` for each.
"""

from __future__ import annotations

from gateway import paths
from gateway import nlm_registry
from gateway.filter.policy import policy_exists, load_policy, PolicyError
from gateway.lint import LintFinding, SEVERITY_INFO
from gateway.lint._walk import walk_raw_sources


def run() -> list[LintFinding]:
    findings: list[LintFinding] = []
    registry = nlm_registry.load()
    if not registry:
        return findings

    # Cache policies so we load each one at most once.
    policy_cache: dict[str, float] = {}

    def _threshold_for(domain: str) -> float | None:
        if domain in policy_cache:
            return policy_cache[domain]
        if not policy_exists(domain):
            policy_cache[domain] = 0.7  # fall back to default include threshold
            return policy_cache[domain]
        try:
            p = load_policy(domain)
            policy_cache[domain] = p.threshold_include
        except PolicyError:
            policy_cache[domain] = 0.7
        return policy_cache[domain]

    for source_type, path, front, body in walk_raw_sources():
        domains = list(front.get("domains") or [])
        if not domains:
            continue
        nlm_ids = list(front.get("nlm_corpus_ids") or [])
        score = (front.get("filter") or {}).get("score")
        if score is None:
            continue
        try:
            score = float(score)
        except (TypeError, ValueError):
            continue

        for domain in domains:
            entry = registry.get(domain)
            if entry is None:
                continue
            if entry.notebook_id in nlm_ids:
                continue
            threshold = _threshold_for(domain)
            if threshold is None:
                continue
            if score < threshold:
                continue
            findings.append(
                LintFinding(
                    check="nlm-pending",
                    severity=SEVERITY_INFO,
                    message=(
                        f"{front.get('id', path.stem)} eligible for {domain} corpus "
                        f"(score {score:.2f} ≥ {threshold:.2f}) but not synced to "
                        f"{entry.notebook_id}"
                    ),
                    path=str(path.relative_to(paths.knowledge_root())),
                    metadata={
                        "domain": domain,
                        "source_id": front.get("id", path.stem),
                        "notebook_id": entry.notebook_id,
                        "score": score,
                        "threshold": threshold,
                    },
                )
            )
    return findings
