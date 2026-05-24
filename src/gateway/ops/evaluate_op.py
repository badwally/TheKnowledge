"""`wiki evaluate` gateway op (M50 Phase F)."""

from __future__ import annotations

from gateway import log, paths
from gateway.core import OperationResult
from gateway.evaluate.persistence import goldens_path_for
from gateway.evaluate.runner import NoGoldensError, run_evaluate
from gateway.evaluate.schema import scaffold_template


def evaluate_op(*,
                domain: str | None = None,
                limit: int | None = None,
                scaffold: str | None = None) -> OperationResult:
    """Run the M50 evaluation or scaffold a new domain's goldens template."""
    if scaffold is not None:
        path = goldens_path_for(scaffold)
        try:
            scaffold_template(path, domain=scaffold)
        except FileExistsError as e:
            return OperationResult(success=False, errors=[str(e)])
        return OperationResult(
            success=True,
            paths_touched=[path],
            summary=f"scaffolded goldens template at {path}",
        )

    if domain is None:
        return OperationResult(
            success=False,
            errors=["--domain is required (or pass --scaffold <domain> to bootstrap)"],
        )

    try:
        summary = run_evaluate(domain, limit=limit)
    except NoGoldensError as e:
        return OperationResult(success=False, errors=[str(e)])

    log.append(
        op="evaluate",
        fields={
            "domain": domain,
            "n_questions": summary.n_questions,
            "mean_score": round(summary.mean_score, 3),
            "input_tokens": summary.total_input_tokens,
            "cache_read_tokens": summary.total_cache_read_tokens,
        },
        summary=(
            f"evaluate {domain}: {summary.n_questions} Q, "
            f"mean={summary.mean_score:.3f}"
        ),
    )
    run_yaml_path = paths.knowledge_internal() / "eval" / domain / "runs" / f"{summary.timestamp}.yaml"
    trend_path = paths.knowledge_internal() / "eval" / domain / "trend.csv"
    return OperationResult(
        success=True,
        paths_touched=[run_yaml_path, trend_path, paths.log_path()],
        summary=(
            f"evaluate {domain}: {summary.n_questions} Q, mean={summary.mean_score:.3f}\n"
            + "\n".join(
                f"  [{r.score:.2f}] {r.golden_id}: {r.question[:80]}"
                for r in summary.results
            )
        ),
    )
