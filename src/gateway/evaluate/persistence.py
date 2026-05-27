"""Per-run YAML + trend CSV persistence for the M50 evaluation framework."""

from __future__ import annotations

import csv
from dataclasses import asdict
from pathlib import Path

import yaml

from gateway import paths
from gateway.evaluate.schema import EvalRunSummary


def eval_dir_for(domain: str) -> Path:
    return paths.knowledge_internal() / "eval" / domain


def runs_dir_for(domain: str) -> Path:
    return eval_dir_for(domain) / "runs"


def trend_path_for(domain: str) -> Path:
    return eval_dir_for(domain) / "trend.csv"


def goldens_path_for(domain: str) -> Path:
    return eval_dir_for(domain) / "goldens.yaml"


def write_run(summary: EvalRunSummary) -> Path:
    """Write the per-run YAML and return its path."""
    run_dir = runs_dir_for(summary.domain)
    run_dir.mkdir(parents=True, exist_ok=True)
    path = run_dir / f"{summary.timestamp}.yaml"
    path.write_text(yaml.safe_dump(asdict(summary), sort_keys=False, allow_unicode=True))
    return path


_TREND_COLUMNS = [
    "timestamp",
    "n_questions",
    "mean_score",
    "total_input_tokens",
    "total_output_tokens",
    "total_cache_read_tokens",
]


def append_to_trend(summary: EvalRunSummary) -> Path:
    """Append one row to `trend.csv`. Creates the file with a header if absent."""
    path = trend_path_for(summary.domain)
    path.parent.mkdir(parents=True, exist_ok=True)
    new_file = not path.exists()
    with path.open("a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=_TREND_COLUMNS)
        if new_file:
            writer.writeheader()
        writer.writerow({
            "timestamp": summary.timestamp,
            "n_questions": summary.n_questions,
            "mean_score": summary.mean_score,
            "total_input_tokens": summary.total_input_tokens,
            "total_output_tokens": summary.total_output_tokens,
            "total_cache_read_tokens": summary.total_cache_read_tokens,
        })
    return path


def read_trend(domain: str) -> list[dict[str, str]]:
    """Read `trend.csv` as a list of dict rows. Returns [] if absent."""
    path = trend_path_for(domain)
    if not path.exists():
        return []
    with path.open() as f:
        return list(csv.DictReader(f))


def domains_with_goldens() -> list[str]:
    """Return sorted list of domain slugs that have a goldens.yaml evaluation file."""
    eval_root = paths.knowledge_internal() / "eval"
    if not eval_root.exists():
        return []
    return sorted(
        d.name
        for d in eval_root.iterdir()
        if d.is_dir() and (d / "goldens.yaml").exists()
    )
