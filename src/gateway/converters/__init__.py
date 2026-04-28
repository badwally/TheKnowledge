"""Converter registry and dispatch.

Converters self-register on first use via `_ensure_registered()`. New
converters are added by appending to the import chain in that function.

Real converter implementations land per BUILD.md:
- M2: web
- M8: youtube, arxiv, pubmed
- M10: pdf, voice, audiobook
"""

from gateway.converters.base import ConversionError, Converter


class NoConverterError(LookupError):
    """Raised when no registered converter handles a source."""


_REGISTRY: list[Converter] = []
_initialized: bool = False


def register(converter: Converter) -> None:
    """Add a converter to the registry. Idempotent on (type_name, class)."""
    for existing in _REGISTRY:
        if type(existing) is type(converter):
            return
    _REGISTRY.append(converter)


def _ensure_registered() -> None:
    """Lazy registration of built-in converters.

    Done lazily so `wiki --help` does not pay the import cost of trafilatura
    et al., and so test code can register mock converters before built-ins.
    """
    global _initialized
    if _initialized:
        return
    from gateway.converters.web import WebConverter

    register(WebConverter())
    _initialized = True


def dispatch(source: str) -> Converter:
    """Return the converter that handles `source`, or raise."""
    _ensure_registered()
    for c in _REGISTRY:
        if c.detect(source):
            return c
    raise NoConverterError(
        f"no converter handles {source!r} "
        f"(registered: {[type(c).__name__ for c in _REGISTRY]})"
    )


def reset_registry_for_tests() -> None:
    """Test-only: empty the registry and clear the initialized flag."""
    _REGISTRY.clear()
    global _initialized
    _initialized = False


__all__ = [
    "ConversionError",
    "Converter",
    "NoConverterError",
    "dispatch",
    "register",
    "reset_registry_for_tests",
]
