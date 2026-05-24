"""M50 framework — per-domain goldens, LLM-as-judge, regression detection."""

from gateway.evaluate.schema import (
    Golden,
    EvalResult,
    EvalRunSummary,
    SchemaError,
    load_goldens,
    save_goldens,
    scaffold_template,
    validate_rubric_weights,
)
from gateway.evaluate.judge import Judge
from gateway.evaluate.persistence import (
    write_run,
    append_to_trend,
    read_trend,
    goldens_path_for,
    trend_path_for,
    runs_dir_for,
    eval_dir_for,
)
from gateway.evaluate.runner import run_evaluate, NoGoldensError

__all__ = [
    "Golden",
    "EvalResult",
    "EvalRunSummary",
    "SchemaError",
    "load_goldens",
    "save_goldens",
    "scaffold_template",
    "validate_rubric_weights",
    "Judge",
    "write_run",
    "append_to_trend",
    "read_trend",
    "goldens_path_for",
    "trend_path_for",
    "runs_dir_for",
    "eval_dir_for",
    "run_evaluate",
    "NoGoldensError",
]
