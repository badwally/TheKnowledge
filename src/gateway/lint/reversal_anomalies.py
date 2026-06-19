"""G2 — reversal-anomalies lint check.

Builds a snapshot from the real resolution-act log + cascade-depth sidecar
and runs the three reversal/anomaly detectors. Emits a LintFinding for each
detector that trips.

Severity: WARNING — the §1.5 Option-B gating signal has crossed its threshold.
The operator should review whether automatic transitive cascade-revert (Option B)
needs to be built.
"""

from __future__ import annotations

from gateway.lint import LintFinding, SEVERITY_WARNING
from gateway.reversal_detectors import build_snapshot, detect


def run() -> list[LintFinding]:
    """Run the three reversal/anomaly detectors over the real act log."""
    snapshot = build_snapshot()
    alarms = detect(snapshot)

    findings: list[LintFinding] = []
    for alarm in alarms:
        if not alarm.tripped:
            continue
        findings.append(
            LintFinding(
                check="reversal-anomalies",
                severity=SEVERITY_WARNING,
                message=(
                    f"§1.5 Option-B gating signal tripped: "
                    f"{alarm.name} = {alarm.value:.3g} > {alarm.threshold} "
                    f"(detail: {alarm.detail})"
                ),
                path="",
                metadata={
                    "detector": alarm.name,
                    "value": alarm.value,
                    "threshold": alarm.threshold,
                    "detail": alarm.detail,
                },
            )
        )
    return findings
