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

    Order matters: more-specific URL converters (youtube, arxiv, pubmed)
    register before the catch-all WebConverter. Local-file converters
    (pdf) are registered after URL ones — their `detect()` only matches
    local paths so order is moot, but keeping URL converters first is a
    natural reading order.
    """
    global _initialized
    if _initialized:
        return
    from gateway.converters.youtube import YouTubeConverter
    from gateway.converters.arxiv import ArxivConverter
    from gateway.converters.pubmed import PubMedConverter
    from gateway.converters.web import WebConverter
    from gateway.converters.pdf import PDFConverter
    from gateway.converters.csv import CSVConverter
    from gateway.converters.docx import DocxConverter
    from gateway.converters.xlsx import XlsxConverter

    register(YouTubeConverter())
    register(ArxivConverter())
    register(PubMedConverter())
    register(WebConverter())
    register(PDFConverter())
    register(CSVConverter())
    register(DocxConverter())
    register(XlsxConverter())

    # Voice / audiobook converters depend on the optional `[whisper]` extra.
    # Register only when the heavy deps are importable so the default install
    # stays light.
    try:
        from gateway.converters.audiobook import AudiobookConverter
        from gateway.converters.voice import VoiceConverter
    except ImportError:
        pass
    else:
        # Audiobook before voice — m4b files match audiobook only; .mp3/.m4a
        # files would match voice first if order were reversed.
        register(AudiobookConverter())
        register(VoiceConverter())
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
