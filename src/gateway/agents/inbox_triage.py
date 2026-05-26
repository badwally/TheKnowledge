"""AGT-1 — Inbox-triage agent.

Triggered by ingest.complete and poll.complete events. For each newly ingested
source:
1. If domains already set (and not "needs-domain"): run filter.score().
2. If domain absent/empty: infer domain via lightweight keyword overlap against
   all policy descriptions. Confidence ≥ 0.6 for exactly one domain → tag +
   filter. Ambiguous or no match → tag "needs-domain", no filter.
3. If filter score in review band (threshold_review ≤ score < threshold_include):
   write .knowledge/triage/<source_id>.yaml.

NEVER calls filter-correct autonomously.
"""

from __future__ import annotations

import re
import yaml
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING

from gateway import frontmatter as fm, paths
from gateway.filter.policy import load_policy, policy_exists, PolicyError
from gateway.filter.semantic import FilterResult, score as filter_score

if TYPE_CHECKING:
    from gateway.filter.semantic import FilterClient


_DOMAIN_INFERENCE_THRESHOLD = 0.6
_DOMAIN_AMBIGUOUS_THRESHOLD = 0.4
_NEEDS_DOMAIN = "needs-domain"


# ---------------------------------------------------------------------------
# result type
# ---------------------------------------------------------------------------


@dataclass
class TriageResult:
    source_id: str
    domain: str | None = None
    filter_score: float | None = None
    in_review_band: bool = False
    notes: str = ""


# ---------------------------------------------------------------------------
# public API
# ---------------------------------------------------------------------------


def run_triage(
    source_id: str,
    *,
    filter_client: "FilterClient | None" = None,
) -> TriageResult:
    """Triage a single source. Mutates source frontmatter on disk."""
    source_path = _find_raw_source(source_id)
    if source_path is None:
        return TriageResult(source_id=source_id, notes="source not found in raw/")

    text = source_path.read_text()
    try:
        front, body = fm.parse(text)
    except fm.FrontmatterError:
        return TriageResult(source_id=source_id, notes="frontmatter parse error")

    domains: list[str] = list(front.get("domains") or [])
    effective_domain: str | None = None

    if _NEEDS_DOMAIN in domains:
        # Already flagged — skip filter entirely
        return TriageResult(source_id=source_id, domain=_NEEDS_DOMAIN, notes="already needs-domain")

    if domains:
        # Domain(s) present — use the first one that has a policy
        for d in domains:
            if policy_exists(d):
                effective_domain = d
                break
    else:
        # Domain absent — try inference
        effective_domain = _infer_domain(front)
        if effective_domain == _NEEDS_DOMAIN:
            # Tag source with needs-domain and persist
            domains = [_NEEDS_DOMAIN]
            front["domains"] = domains
            source_path.write_text(fm.serialize(front, body))
            return TriageResult(source_id=source_id, domain=_NEEDS_DOMAIN, notes="domain ambiguous or unmatched")
        elif effective_domain:
            # Apply inferred domain
            domains = [effective_domain]
            front["domains"] = domains

    if effective_domain is None or not policy_exists(effective_domain):
        return TriageResult(source_id=source_id, domain=effective_domain, notes="no policy for domain")

    # Run filter score
    try:
        policy = load_policy(effective_domain)
    except PolicyError as e:
        return TriageResult(source_id=source_id, domain=effective_domain, notes=f"policy error: {e}")

    from gateway.filter import load_all, select
    examples = select(load_all(effective_domain), policy)
    result: FilterResult = filter_score(front, body, policy, examples, client=filter_client)

    # Persist filter block and domain into source frontmatter
    front["filter"] = result.to_frontmatter_block()
    if effective_domain not in (front.get("domains") or []):
        front["domains"] = list(front.get("domains") or []) + [effective_domain]
    source_path.write_text(fm.serialize(front, body))

    score_val = result.score
    in_review = policy.threshold_review <= score_val < policy.threshold_include

    triage_result = TriageResult(
        source_id=source_id,
        domain=effective_domain,
        filter_score=score_val,
        in_review_band=in_review,
    )

    if in_review:
        _write_triage_entry(triage_result, front)

    return triage_result


def triage_list() -> list[dict]:
    """Return all entries in the triage queue."""
    d = paths.knowledge_internal() / "triage"
    if not d.is_dir():
        return []
    results = []
    for f in sorted(d.glob("*.yaml")):
        try:
            data = yaml.safe_load(f.read_text()) or {}
            results.append(data)
        except Exception:
            pass
    return results


def triage_depth() -> int:
    """Return the number of sources currently in the triage queue."""
    d = paths.knowledge_internal() / "triage"
    if not d.is_dir():
        return 0
    return len(list(d.glob("*.yaml")))


@dataclass
class BatchTriageResult:
    processed: int = 0
    skipped: int = 0
    failed: int = 0
    results: list[TriageResult] = field(default_factory=list)


def run_inbox_triage_batch(*, filter_client=None) -> BatchTriageResult:
    """Scan all raw sources without a filter score and run triage on each.

    Skips sources that already have a ``filter`` block in frontmatter.
    Used by the scheduled fallback sweep (every 15 min via AGT-1 cron entry).
    """
    raw = paths.raw_dir()
    if not raw.exists():
        return BatchTriageResult()

    result = BatchTriageResult()
    for type_dir in sorted(raw.iterdir()):
        if not type_dir.is_dir():
            continue
        for source_file in sorted(type_dir.glob("*.md")):
            try:
                front, _ = fm.parse(source_file.read_text())
            except Exception:
                result.failed += 1
                continue
            if front.get("filter"):
                result.skipped += 1
                continue
            source_id = front.get("id") or source_file.stem
            try:
                tr = run_triage(source_id, source_path=source_file, filter_client=filter_client)
                result.processed += 1
                result.results.append(tr)
            except Exception:
                result.failed += 1

    return result


# ---------------------------------------------------------------------------
# private helpers
# ---------------------------------------------------------------------------


def _find_raw_source(source_id: str) -> Path | None:
    """Find the raw source file for any supported type."""
    for source_type in paths.SOURCE_TYPES:
        p = paths.raw_dir() / source_type / f"{source_id}.md"
        if p.exists():
            return p
    return None


def _tokenize(text: str) -> set[str]:
    """Split text into lowercase word tokens, filter short/stopwords."""
    _STOP = frozenset({"the", "and", "for", "are", "with", "has", "have",
                       "this", "that", "from", "its", "not", "but", "can",
                       "was", "were", "been", "will", "also", "any", "all"})
    words = re.findall(r"[a-z]+", text.lower())
    return {w for w in words if len(w) > 2 and w not in _STOP}


def _infer_domain(front: dict) -> str | None:
    """Keyword-overlap domain inference. Returns slug, 'needs-domain', or None."""
    policies_root = paths.policies_dir()
    if not policies_root.is_dir():
        return _NEEDS_DOMAIN

    title = front.get("title") or ""
    tags = front.get("tags") or []
    source_tokens = _tokenize(title + " " + " ".join(tags))
    if not source_tokens:
        return _NEEDS_DOMAIN

    scores: dict[str, float] = {}
    for policy_dir in policies_root.iterdir():
        if not policy_dir.is_dir():
            continue
        policy_file = policy_dir / "policy.yaml"
        if not policy_file.exists():
            continue
        try:
            data = yaml.safe_load(policy_file.read_text()) or {}
        except Exception:
            continue
        desc = " ".join([
            str(data.get("domain_description") or ""),
            str(data.get("domain_topic") or ""),
            " ".join(str(c) for c in (data.get("inclusion_criteria") or [])),
        ])
        policy_tokens = _tokenize(desc)
        if not policy_tokens:
            continue
        overlap = len(source_tokens & policy_tokens)
        conf = overlap / len(source_tokens)
        if conf > 0:
            scores[policy_dir.name] = conf

    above_threshold = [(s, c) for s, c in scores.items() if c >= _DOMAIN_INFERENCE_THRESHOLD]
    above_ambiguous = [(s, c) for s, c in scores.items() if c >= _DOMAIN_AMBIGUOUS_THRESHOLD]

    if len(above_threshold) == 1:
        return above_threshold[0][0]
    if len(above_ambiguous) >= 2:
        return _NEEDS_DOMAIN
    if not scores:
        return _NEEDS_DOMAIN
    return _NEEDS_DOMAIN


def _write_triage_entry(result: TriageResult, front: dict) -> None:
    triage_dir = paths.knowledge_internal() / "triage"
    triage_dir.mkdir(parents=True, exist_ok=True)
    entry = {
        "source_id": result.source_id,
        "title": front.get("title") or "",
        "domain": result.domain,
        "filter_score": round(result.filter_score, 3) if result.filter_score is not None else None,
        "scored_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    (triage_dir / f"{result.source_id}.yaml").write_text(yaml.dump(entry))
