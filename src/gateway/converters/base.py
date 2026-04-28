"""Converter ABC.

A converter takes a source identifier (URL or path) and produces canonical
markdown text — frontmatter + body matching the schema in WIKI.md § 3.

Some converters may write binary sidecars to `raw/<type>/<id>.<ext>` as a side
effect (PDF → keep the .pdf alongside; voice → keep the .m4a). M2 handles
the simplest case (web) which has no sidecars.
"""

from abc import ABC, abstractmethod


class ConversionError(RuntimeError):
    """Raised when a converter cannot fetch, parse, or extract content."""


class Converter(ABC):
    """Base class for all source-type converters.

    Subclasses register themselves via gateway.converters (the package's
    dispatch registry) and are selected by URL pattern, file extension,
    or explicit `--type` override.
    """

    #: Short label for the source type produced by this converter
    #: (matches the values in `paths.SOURCE_TYPES`).
    type_name: str = ""

    @abstractmethod
    def detect(self, source: str) -> bool:
        """Return True if this converter handles `source`.

        Called by the dispatcher to pick the right converter for a given
        input. May inspect URL scheme, file extension, MIME, etc.
        """

    @abstractmethod
    def convert(self, source: str) -> str:
        """Fetch / read `source` and return canonical markdown text.

        The returned string is `frontmatter + body` ready to be parsed by
        `gateway.frontmatter.parse(...)`. Implementations may also write
        binary sidecars to `raw/<type>/<id>.<ext>` for non-textual content.

        Raises:
            ConversionError: if fetching or extraction fails.
        """
