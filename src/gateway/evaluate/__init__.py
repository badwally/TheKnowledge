"""M50 framework — per-domain goldens, LLM-as-judge, regression detection."""

from gateway.evaluate.schema import (
    Golden,
    EvalResult,
    EvalRunSummary,
    SchemaError,
    load_goldens,
    save_goldens,
    scaffold_template,
)

__all__ = [
    "Golden",
    "EvalResult",
    "EvalRunSummary",
    "SchemaError",
    "load_goldens",
    "save_goldens",
    "scaffold_template",
]
