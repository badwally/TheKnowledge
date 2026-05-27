"""ONT-7: per-claim confidence distribution and propagation.

Two checks:
1. confidence-distribution — per domain, counts established/tentative/speculative/none
   for entity/concept/synthesis pages; surfaces as INFO finding per domain.
2. confidence-propagation — synthesis pages that synthesize from sources whose
   wiki page carries confidence: tentative or speculative but whose own
   confidence is not downgraded (propagation rule: synthesis <= most-uncertain
   source).

Both checks are read-only. The confidence: field is optional; absence means
the page inherits the domain default (treated as 'established' for scoring).
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from gateway import frontmatter as fm, paths
from gateway.lint import LintFinding, SEVERITY_WARNING
from gateway.lint._walk import walk_wiki_pages


CONFIDENCE_TIERS = ("established", "tentative", "speculative")
_TIER_RANK = {"established": 0, "tentative": 1, "speculative": 2}
SEVERITY_INFO = "INFO"


# --------------------------------------------------------------------------- #
# Distribution check                                                           #
# --------------------------------------------------------------------------- #


def _domain_confidence_distribution() -> dict[str, dict[str, int]]:
    """Return {domain: {tier: count}} for entity/concept/synthesis pages."""
    dist: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for type_name, path, front, body in walk_wiki_pages():
        if type_name not in ("entity", "concept", "synthesis"):
            continue
        confidence = str(front.get("confidence", "none")).lower()
        tier = confidence if confidence in CONFIDENCE_TIERS else "none"
        domains = front.get("domains") or front.get("domain") or []
        if isinstance(domains, str):
            domains = [domains]
        for domain in domains:
            dist[domain][tier] += 1
        if not domains:
            dist["(untagged)"][tier] += 1
    return {d: dict(counts) for d, counts in dist.items()}


def run_distribution() -> list[LintFinding]:
    """Surface per-domain confidence distribution as INFO findings."""
    dist = _domain_confidence_distribution()
    findings: list[LintFinding] = []
    for domain, counts in sorted(dist.items()):
        total = sum(counts.values())
        if total == 0:
            continue
        summary_parts = []
        for tier in (*CONFIDENCE_TIERS, "none"):
            n = counts.get(tier, 0)
            if n:
                summary_parts.append(f"{tier}={n}")
        pct_annotated = int(
            100 * (counts.get("established", 0) + counts.get("tentative", 0) + counts.get("speculative", 0)) / total
        )
        findings.append(
            LintFinding(
                check="confidence-distribution",
                severity=SEVERITY_INFO,
                message=(
                    f"domain '{domain}': {total} pages, {pct_annotated}% annotated "
                    f"({', '.join(summary_parts)})"
                ),
                path=f".knowledge/policies/{domain}/policy.yaml",
                metadata={
                    "domain": domain,
                    "total": total,
                    "pct_annotated": pct_annotated,
                    **counts,
                },
            )
        )
    return findings


# --------------------------------------------------------------------------- #
# Propagation check                                                            #
# --------------------------------------------------------------------------- #


def _confidence_of_source_wiki_page(source_id: str) -> str | None:
    """Return confidence: of wiki/sources/<id>.md, or None if absent/missing."""
    p = paths.wiki_source_path(source_id)
    if not p.exists():
        return None
    try:
        front, _ = fm.parse(p.read_text())
    except Exception:
        return None
    val = str(front.get("confidence", "")).lower()
    return val if val in CONFIDENCE_TIERS else None


def run_propagation() -> list[LintFinding]:
    """Flag synthesis pages whose confidence is higher than their source evidence warrants."""
    findings: list[LintFinding] = []
    for type_name, path, front, body in walk_wiki_pages():
        if type_name != "synthesis":
            continue
        synth_confidence = str(front.get("confidence", "established")).lower()
        if synth_confidence not in _TIER_RANK:
            synth_confidence = "established"
        synth_rank = _TIER_RANK[synth_confidence]

        synthesizes = front.get("synthesizes", []) or []
        max_source_rank = 0
        weakest_source: str | None = None
        for ref in synthesizes:
            # ref is "sources/<id>" — strip prefix to get source_id
            source_id = str(ref).removeprefix("sources/")
            source_conf = _confidence_of_source_wiki_page(source_id)
            if source_conf is None:
                continue
            rank = _TIER_RANK.get(source_conf, 0)
            if rank > max_source_rank:
                max_source_rank = rank
                weakest_source = source_id

        if weakest_source and synth_rank < max_source_rank:
            weakest_tier = CONFIDENCE_TIERS[max_source_rank]
            findings.append(
                LintFinding(
                    check="confidence-propagation",
                    severity=SEVERITY_WARNING,
                    message=(
                        f"synthesis confidence '{synth_confidence}' is stronger than source evidence warrants; "
                        f"weakest cited source is '{weakest_source}' ({weakest_tier}); "
                        f"consider setting confidence: {weakest_tier}"
                    ),
                    path=str(path.relative_to(paths.knowledge_root())),
                    metadata={
                        "synthesis_confidence": synth_confidence,
                        "weakest_source": weakest_source,
                        "weakest_tier": weakest_tier,
                    },
                )
            )
    return findings


# --------------------------------------------------------------------------- #
# Combined entry point                                                         #
# --------------------------------------------------------------------------- #


def run() -> list[LintFinding]:
    return run_distribution() + run_propagation()
