"""AGT-8: Monthly filter calibrator routine.

Checks every domain's example-bank count against the distillation threshold.
For each domain that has crossed the threshold, emits a log event recommending
`wiki finetune --distill --domain <domain>`. Never executes distillation itself —
that is a user decision.

Designed to run monthly from the scheduler (`wiki routine filter-calibrator`).
"""

from __future__ import annotations

from datetime import datetime, timezone

from gateway import log, paths
from gateway.core import OperationResult
from gateway.ops.finetune import trigger_states_all


_ALREADY_LOGGED_PATH_NAME = "filter_calibrator_logged.yaml"


def _already_logged_path():
    return paths.knowledge_internal() / _ALREADY_LOGGED_PATH_NAME


def _load_already_logged() -> set[str]:
    import yaml

    p = _already_logged_path()
    if not p.exists():
        return set()
    try:
        data = yaml.safe_load(p.read_text()) or {}
        return set(data.get("logged_domains", []))
    except Exception:
        return set()


def _save_already_logged(domains: set[str]) -> None:
    import yaml

    p = _already_logged_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(yaml.safe_dump({"logged_domains": sorted(domains)}))


def run_filter_calibrator() -> OperationResult:
    """Check calibration readiness; emit log events for threshold-crossing domains."""
    states = trigger_states_all()
    if not states:
        return OperationResult(
            success=True,
            summary="filter-calibrator: no domains with policies registered",
        )

    already_logged = _load_already_logged()
    newly_ready: list[str] = []
    lines: list[str] = []

    for ts in states:
        pct = int(min(100, ts.count / ts.threshold * 100))
        readiness = "ready" if ts.ready else f"{pct}% ({ts.count}/{ts.threshold})"
        lines.append(f"  {ts.domain}: {readiness}")

        if ts.ready and ts.domain not in already_logged:
            log.append(
                "calibration-distill-ready",
                fields={
                    "domain": ts.domain,
                    "count": ts.count,
                    "threshold": ts.threshold,
                    "command": f"wiki finetune --distill --domain {ts.domain}",
                    "as_of": datetime.now(timezone.utc).isoformat(),
                },
                summary=(
                    f"{ts.domain} crossed distillation threshold "
                    f"({ts.count}/{ts.threshold}) — run: "
                    f"wiki finetune --distill --domain {ts.domain}"
                ),
            )
            newly_ready.append(ts.domain)

    if newly_ready:
        _save_already_logged(already_logged | set(newly_ready))

    header = "filter-calibrator:"
    if newly_ready:
        header += f" {len(newly_ready)} domain(s) newly ready for distillation"
    body = "\n".join([header] + lines)
    return OperationResult(success=True, summary=body)
