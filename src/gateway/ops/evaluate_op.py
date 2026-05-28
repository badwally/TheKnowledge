"""`wiki evaluate` gateway op (M50 Phase F)."""

from __future__ import annotations

from gateway import log, paths
from gateway.core import OperationResult
from gateway.evaluate.persistence import domains_with_goldens, goldens_path_for
from gateway.evaluate.runner import NoGoldensError, run_evaluate
from gateway.evaluate.schema import scaffold_template


def evaluate_op(*,
                domain: str | None = None,
                limit: int | None = None,
                max_chars: int | None = None,
                scaffold: str | None = None,
                all_domains: bool = False) -> OperationResult:
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

    if all_domains:
        return _evaluate_all_domains(limit=limit, max_chars=max_chars)

    if domain is None:
        return OperationResult(
            success=False,
            errors=["--domain is required (or pass --scaffold <domain> to bootstrap, or --all-domains to score all)"],
        )

    try:
        summary = run_evaluate(domain, limit=limit, max_chars=max_chars)
    except NoGoldensError as e:
        return OperationResult(success=False, errors=[str(e)])
    except Exception as e:
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


def _evaluate_all_domains(*, limit: int | None = None,
                          max_chars: int | None = None) -> OperationResult:
    """Run evaluate_op for every domain that has a goldens.yaml and return aggregate results."""
    domains = domains_with_goldens()
    if not domains:
        return OperationResult(
            success=False,
            errors=["no domains with goldens.yaml found — use `wiki evaluate --scaffold <domain>` to create one"],
        )

    lines: list[str] = []
    errors: list[str] = []
    paths_touched: list = []

    for d in domains:
        result = evaluate_op(domain=d, limit=limit, max_chars=max_chars)
        if result.success:
            first_line = result.summary.splitlines()[0] if result.summary else d
            lines.append(f"  {first_line}")
            paths_touched.extend(result.paths_touched or [])
        else:
            errors.append(f"{d}: {'; '.join(result.errors)}")

    scored = len(domains) - len(errors)
    summary = f"evaluate --all-domains: {scored}/{len(domains)} domains scored\n" + "\n".join(lines)
    return OperationResult(
        success=scored > 0,
        errors=errors,
        paths_touched=paths_touched,
        summary=summary,
    )
