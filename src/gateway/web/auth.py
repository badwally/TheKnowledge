"""K3 (M48): bearer-token authentication for cloud-exposed endpoints.

Tokens are stored hashed (sha256) in `.knowledge/auth.yaml`. The CLI
(`wiki auth add`) generates a 32-byte token via `secrets.token_urlsafe`,
prints the plaintext **once**, and persists only the hash. Verification
is constant-time (`hmac.compare_digest`).

Per C2 the file is `.gitignore`'d (defense-in-depth — `.knowledge/` is
already covered, but auth.yaml gets an explicit entry).

This module exposes:

- `add_token(name) -> str`: generates a token, stores its hash, returns
  the plaintext (caller must surface it to the user; never logged).
- `list_tokens() -> list[dict]`: read-side, no plaintext disclosure.
- `revoke_token(name) -> bool`: removes the entry.
- `verify_bearer(authorization: str | None) -> str`: FastAPI dependency
  that raises HTTPException(401) on missing/invalid auth and returns
  the token name on success (useful for audit logging).
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import hmac
import secrets
from typing import Any

import yaml
from fastapi import HTTPException, Header

from gateway import paths


_TOKEN_HASH_PREFIX = "sha256:"
_TOKEN_BYTES = 32  # secrets.token_urlsafe(32) → ~43 char base64-url token


def _auth_path():
    return paths.knowledge_internal() / "auth.yaml"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _hash_token(plaintext: str) -> str:
    return _TOKEN_HASH_PREFIX + hashlib.sha256(plaintext.encode("utf-8")).hexdigest()


def _load_auth() -> dict[str, Any]:
    path = _auth_path()
    if not path.exists():
        return {"tokens": []}
    raw = yaml.safe_load(path.read_text()) or {}
    if "tokens" not in raw:
        raw["tokens"] = []
    return raw


def _save_auth(data: dict[str, Any]) -> None:
    path = _auth_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
    # Best-effort chmod 600 — the file holds credentials even hashed
    try:
        path.chmod(0o600)
    except OSError:
        pass


def add_token(name: str) -> str:
    """Generate a new token, store its hash, return the plaintext.

    Refuses to overwrite an existing entry with the same name.
    """
    if not name or not name.strip():
        raise ValueError("token name must be non-empty")
    auth = _load_auth()
    for entry in auth["tokens"]:
        if entry.get("name") == name:
            raise ValueError(f"token {name!r} already exists; revoke first to rotate")
    plaintext = secrets.token_urlsafe(_TOKEN_BYTES)
    auth["tokens"].append(
        {
            "name": name,
            "token_hash": _hash_token(plaintext),
            "created_at": _now_iso(),
            "last_used_at": None,
        }
    )
    _save_auth(auth)
    return plaintext


def list_tokens() -> list[dict[str, Any]]:
    """Return token entries WITHOUT plaintext or hash (audit-friendly)."""
    auth = _load_auth()
    return [
        {
            "name": e.get("name"),
            "created_at": e.get("created_at"),
            "last_used_at": e.get("last_used_at"),
        }
        for e in auth["tokens"]
    ]


def revoke_token(name: str) -> bool:
    """Remove the entry named `name`. Returns True if it existed."""
    auth = _load_auth()
    before = len(auth["tokens"])
    auth["tokens"] = [e for e in auth["tokens"] if e.get("name") != name]
    if len(auth["tokens"]) == before:
        return False
    _save_auth(auth)
    return True


def _check_plaintext(plaintext: str) -> str | None:
    """If `plaintext` matches a stored hash, return the token name; else None.

    Constant-time comparison via hmac.compare_digest on the hex digests.
    Also updates `last_used_at` on the matched entry as a side-effect.
    """
    if not plaintext:
        return None
    candidate = _hash_token(plaintext)
    auth = _load_auth()
    matched_name: str | None = None
    for entry in auth["tokens"]:
        stored = entry.get("token_hash", "")
        if hmac.compare_digest(stored, candidate):
            matched_name = entry.get("name")
            entry["last_used_at"] = _now_iso()
            break
    if matched_name is not None:
        _save_auth(auth)
    return matched_name


def verify_bearer(authorization: str | None = Header(default=None)) -> str:
    """FastAPI dependency: validate the `Authorization: Bearer <token>` header.

    Returns the token's `name` on success (callers can log it). Raises
    HTTPException(401) on missing/invalid auth.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="missing Authorization header")
    parts = authorization.split(" ", 1)
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(
            status_code=401, detail='Authorization must be "Bearer <token>"'
        )
    name = _check_plaintext(parts[1].strip())
    if name is None:
        raise HTTPException(status_code=401, detail="invalid token")
    return name
