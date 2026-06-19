"""G7 — privileged-intent policy-edit path.

Policy changes govern dedup/trust/contradiction behaviour corpus-wide. They
route through the CommitGate as a typed intent — never a direct file write. This
module handles the enqueue side (principal/allowlist check → validate shape →
submit intent); the CommitGate handles the apply side (eval-compare + merge-map
golden gate → write or dead-letter).

Trust model
-----------
Policy edits are rare, high-impact, human-judgment events (the operator monitors
the §1.4/§1.5 keys). The trust model is:

- **Not an agent tool.** ``policy-edit`` is human-CLI-only (``wiki policy-edit``).
  It is NOT registered on any MCP surface (read or build tier), so an agent
  cannot invoke it through the tool layer. There is no use case for an agent to
  autonomously rewrite corpus-wide policy.
- **Server-sourced principal.** Privilege is bound to a server-side principal
  read from ``GATEWAY_POLICY_PRINCIPAL`` (or ``.knowledge/secrets.env``), NOT to
  caller arguments. A caller cannot pass an identity to gain privilege. An unset
  or empty principal is NOT privileged → reject (fail-closed). The server
  principal is stamped onto the intent for provenance/audit, so the audit
  principal is unspoofable.
- **Change-control gates.** The dual eval + merge-map gate, the monotone version
  bump, and the provenance node enforce change-control on every edit.

This is change-control + an unspoofable audit principal, not a hard boundary
against a process that already has shell access: a build-tier agent with full
Bash can shell out to any ``wiki`` command, so an in-request allowlist was never
a hard boundary against that agent. Confining the op to the CLI and binding
privilege + audit to a server-sourced principal is the property this layer
provides; isolating shell access is a gateway-wide concern, not this module's.

Hardcoded threshold constants (e.g. commit_gate.py's COMMIT_LOCK_ACQUIRE_TIMEOUT,
deposit.py's MAX_BACKLOG) are NOT gated by this runtime path; they require a
code-review and merge. This is documented here and in the lint/policy_provenance
message so the boundary is explicit, not silent.
"""

from __future__ import annotations

import os
import re

from gateway.core import OperationResult
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id

# Strict domain-slug regex (HIGH 2: path-traversal guard). A domain slug is
# computed into a filesystem path (.knowledge/policies/<slug>/policy.yaml); an
# unvalidated slug like "../../etc/x" escapes the policies root. Enforced here at
# the enqueue layer AND at the CommitGate apply layer (defense in depth).
_DOMAIN_SLUG_RE = re.compile(r"[a-z0-9][a-z0-9_-]{0,63}")

# ---------------------------------------------------------------------------
# Build-time allowlist for policy-edit privilege.
# A SERVER-SOURCED principal (agent, role) is privileged iff it appears here.
# Adding an entry requires code-review + merge — there is no runtime extension.
# ---------------------------------------------------------------------------
_ALLOWLIST: frozenset[tuple[str, str]] = frozenset(
    {
        ("librarian-admin", "policy-admin"),
    }
)

# Env var carrying the server-sourced privileged principal, "agent:role".
# Populated from the real environment or from .knowledge/secrets.env (loaded at
# the CLI entrypoint via secrets_env.load_secrets_env). NOT caller-supplied.
_PRINCIPAL_ENV = "GATEWAY_POLICY_PRINCIPAL"

# Default poll-interval hint (seconds) on the async receipt.
_RETRY_AFTER = 2


def _server_principal() -> dict | None:
    """Resolve the server-sourced principal from the environment.

    Returns ``{"agent": ..., "role": ...}`` parsed from ``GATEWAY_POLICY_PRINCIPAL``
    (format ``"agent:role"``), or ``None`` if unset/empty/malformed. The principal
    is NEVER taken from caller arguments — that is the spoofing fix. An unset or
    malformed principal yields None → the caller is not privileged (fail-closed)."""
    raw = (os.environ.get(_PRINCIPAL_ENV) or "").strip()
    if not raw or ":" not in raw:
        return None
    agent, _, role = raw.partition(":")
    agent, role = agent.strip(), role.strip()
    if not agent or not role:
        return None
    return {"agent": agent, "role": role}


def _is_allowlisted(identity: dict) -> bool:
    """Return True iff the principal's (agent, role) is on the build-time allowlist."""
    agent = identity.get("agent", "")
    role = identity.get("role", "")
    return (agent, role) in _ALLOWLIST


def _read_on_disk_version(domain: str) -> int:
    """Return the on-disk policy version for ``domain`` (0 if no policy yet).

    Used by the version-conflict guard: a policy edit must propose a version
    strictly greater than the current on-disk version. A missing or malformed
    version reads as 0 so a first edit (version 1) is accepted.
    """
    import yaml
    from gateway.filter.policy import policy_path

    p = policy_path(domain)
    if not p.exists():
        return 0
    try:
        data = yaml.safe_load(p.read_text()) or {}
        return int(data.get("version", 0))
    except (OSError, ValueError, TypeError, yaml.YAMLError):
        return 0


def _validate(domain: str, policy_data: dict, reason: str) -> list[str]:
    """Return a list of validation errors for the policy-edit shape (empty = ok)."""
    errors: list[str] = []
    if not domain or not isinstance(domain, str):
        errors.append("domain must be a non-empty string")
    elif not _DOMAIN_SLUG_RE.fullmatch(domain):
        # HIGH 2: reject path-traversal / non-slug domains before they reach the gate.
        errors.append(
            f"invalid domain slug {domain!r} (must match [a-z0-9][a-z0-9_-]{{0,63}}) "
            f"— possible path traversal"
        )
    if not policy_data or not isinstance(policy_data, dict):
        errors.append("policy_data must be a non-empty dict")
    if not reason or not isinstance(reason, str) or not reason.strip():
        errors.append("reason must be a non-empty string documenting the change motivation")
    return errors


def policy_edit(
    domain: str,
    policy_data: dict,
    *,
    reason: str,
    queue: IntentQueue | None = None,
) -> OperationResult:
    """Validate and enqueue a policy-edit CommitGate intent under a server principal.

    Privilege is bound to the SERVER-SOURCED principal (``GATEWAY_POLICY_PRINCIPAL``),
    never to caller arguments — this function takes no ``identity``/``agent``/``role``
    parameter, so a caller cannot pass an identity to gain privilege. An unset,
    empty, or non-allowlisted principal is rejected (fail-closed). The resolved
    principal is stamped onto the intent for provenance/audit.

    Parameters
    ----------
    domain:
        The domain slug whose policy.yaml will be updated.
    policy_data:
        The full new policy mapping (must be a non-empty dict).
    reason:
        Human-readable motivation for the change (required; the CommitGate
        records it in the provenance node).
    queue:
        Optional IntentQueue override (defaults to the live queue).

    Returns
    -------
    OperationResult
        ``disposition="queued"`` on success.
        ``disposition="rejected"`` if the server principal is unset/non-allowlisted
        or validation fails.
    """
    q = queue or IntentQueue()

    # --- Server-sourced principal check (must be first — fail closed) ---
    # Privilege comes from the server-side principal, NOT from caller args. An
    # unset/empty/malformed principal is not privileged → reject.
    principal = _server_principal()
    if principal is None:
        return OperationResult(
            success=False,
            disposition="rejected",
            errors=[
                f"no server policy-edit principal configured ({_PRINCIPAL_ENV} unset "
                "or malformed) — this privileged operation is rejected (fail-closed). "
                "Set the principal in the server environment or .knowledge/secrets.env"
            ],
            summary="policy-edit rejected: no server principal (fail-closed)",
        )
    if not _is_allowlisted(principal):
        return OperationResult(
            success=False,
            disposition="rejected",
            errors=[
                f"server principal ({principal['agent']!r}, {principal['role']!r}) is not "
                "on the policy-edit allowlist; this is a privileged operation — add the "
                "(agent, role) pair to the build-time allowlist in ops/policy_edit.py "
                "via code-review"
            ],
            summary=f"policy-edit rejected: {principal['agent']!r} not allowlisted",
        )
    identity = principal

    # --- Shape validation ---
    errors = _validate(domain, policy_data, reason)
    if errors:
        return OperationResult(
            success=False,
            disposition="rejected",
            errors=errors,
            summary=f"policy-edit validation failed: {errors[0]}",
        )

    # --- Version-conflict guard + monotone bump («policy-version provenance») ---
    # Read the on-disk version; the proposed version MUST be strictly greater so
    # a stale edit (built against an older policy) cannot silently overwrite a
    # newer one. If the proposed policy omits a version, auto-bump to on-disk + 1.
    on_disk_version = _read_on_disk_version(domain)
    proposed_version = policy_data.get("version")
    if proposed_version is None:
        policy_version = on_disk_version + 1
        policy_data = {**policy_data, "version": policy_version}
    else:
        try:
            policy_version = int(proposed_version)
        except (TypeError, ValueError):
            return OperationResult(
                success=False,
                disposition="rejected",
                errors=[f"policy version must be an integer, got {proposed_version!r}"],
                summary="policy-edit rejected: non-integer version",
            )
        if policy_version <= on_disk_version:
            return OperationResult(
                success=False,
                disposition="rejected",
                errors=[
                    f"policy version conflict: proposed version {policy_version} is not "
                    f"greater than on-disk version {on_disk_version} for domain {domain!r} "
                    f"— rebase the edit on the current policy and bump the version"
                ],
                summary=f"policy-edit rejected: version {policy_version} <= {on_disk_version}",
            )

    # --- Enqueue the typed CommitGate intent ---
    payload: dict = {
        "op": "policy-edit",
        "domain": domain,
        "policy_data": policy_data,
        "reason": reason,
        "policy_version": policy_version,
    }
    iid = compute_intent_id(payload, identity, semantics=f"policy-edit:{domain}")
    intent = Intent(
        intent_id=iid,
        payload=payload,
        identity=identity,
        head_oid="HEAD",
    )
    q.submit(intent)

    return OperationResult(
        success=True,
        intent_id=iid,
        disposition="queued",
        retry_after=_RETRY_AFTER,
        summary=f"policy-edit enqueued for domain {domain!r} ({reason!r})",
    )
