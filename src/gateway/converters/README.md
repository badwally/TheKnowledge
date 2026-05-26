# gateway.converters

Converters translate external sources — URLs, file paths, bare identifiers — into canonical markdown (frontmatter + body) matching the schema in `WIKI.md § 3`. The output is a string, not a file write; `ops/ingest.py` owns writing to `raw/`. Some converters write binary sidecars to `raw/<type>/<id>.<ext>` as a side effect (e.g., PDFConverter writes the `.pdf` alongside the `.md`). The dispatch registry in `__init__.py` selects the right converter via `detect()` in priority order; more-specific converters (YouTube, arXiv, PubMed) register before the catch-all WebConverter.

See `ARCHITECTURE.md` for where converters sit in the pipeline.

## Files

| File | Converter / Purpose |
|------|---------------------|
| `__init__.py` | Registry: `dispatch()`, `register()`, `_ensure_registered()`, `NoConverterError` |
| `base.py` | `Converter` ABC: `detect()`, `convert()`; `ConversionError` |
| `web.py` | `WebConverter` — catch-all HTTP/HTTPS via Trafilatura |
| `arxiv.py` | `ArxivConverter` — arXiv abstract + optional PDF full text |
| `pubmed.py` | `PubMedConverter` — PubMed abstract via E-utilities |
| `youtube.py` | `YouTubeConverter` — transcript + metadata via yt-dlp |
| `pdf.py` | `PDFConverter` — local PDF via pdfminer |
| `csv.py` | `CSVConverter` — local CSV, produces a tabular source page |
| `docx.py` | `DocxConverter` — local .docx via python-docx |
| `xlsx.py` | `XlsxConverter` — local .xlsx via openpyxl |
| `pptx.py` | `PptxConverter` — local .pptx via python-pptx |
| `image.py` | `ImageConverter` — local image via VLM (`gateway.vlm`) |
| `_search/` | Internal helpers shared by search-oriented adapters (not a public API) |

## Adding a new converter (6-step contract)

1. Add the type string to `paths.SOURCE_TYPES` in `gateway/paths.py`.
2. Add it to `validator.ALLOWED_SOURCE_TYPES` in `gateway/validator.py` and define an `ID_PATTERNS` regex entry for the new type's canonical ID format.
3. Implement the converter as a `Converter` subclass with `detect(source: str) -> bool` and `convert(source: str) -> str`. Set `type_name` to match the string added in step 1.
4. Register it in `gateway.converters.__init__._ensure_registered` — import the class and call `register(MyConverter())`. More-specific converters should appear before WebConverter.
5. Update `WIKI.md § 3.1` (type enum), `§ 3.2` (meta block example), and `§ 6.1` (ID format table) to document the new type.
6. Write tests at `tests/gateway/test_converters_<type>.py`, mirroring an existing converter's test structure (detect, happy path, ConversionError propagation, canonical frontmatter fields).

### You're done when:

- [ ] `pytest tests/gateway/test_converters_<type>.py` passes
- [ ] `wiki lint` reports no new errors
- [ ] `pytest tests/gateway/test_mcp_parity.py` green (MCP surface exposes the type)

## Worked example: dispatching a YouTube URL

```
Input:  "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
Call:   converters.dispatch("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

1. _ensure_registered() runs if not already done; fills _REGISTRY in order:
   YouTubeConverter, ArxivConverter, PubMedConverter, WebConverter, ...
2. dispatch() iterates _REGISTRY, calls converter.detect(source) for each
3. YouTubeConverter.detect() matches "youtube.com" in the URL → returns True
4. dispatch() returns YouTubeConverter instance
5. Caller: YouTubeConverter.convert(url) → fetches transcript + metadata
6. Returns canonical markdown string starting with "---\nid: youtube-dQw4w9WgXcQ\n..."

Failure modes:
- No converter matches → NoConverterError("no converter for ...")
- Fetch fails          → ConversionError("yt-dlp error: ...")
- Caller catches both; ops/ingest.py maps them to OperationResult(success=False)
```
