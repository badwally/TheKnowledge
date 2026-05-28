---
schema_version: 1
type: entity
slug: wikiloom
canonical_name: WikiLoom
entity_kind: product
domains:
- knowledge-systems
created_at: '2026-05-28T20:23:59Z'
last_updated: '2026-05-28T20:23:59Z'
---

# WikiLoom

## Summary

WikiLoom is an LLM-driven tool that turns raw documents (PDFs, markdown files, URLs) into a persistent, compounding knowledge base of structured wiki pages with deterministic linking, structural provenance, and human-edit protection [[sources/web-2026-04-11-879]]. It is explicitly inspired by Andrej Karpathy's LLM wiki gist [[sources/web-2026-04-11-879]].

## Key facts

- WikiLoom is distributed as a Python package installable via `pip install wikiloom` and requires the spaCy `en_core_web_sm` model for its linking engine [[sources/web-2026-04-11-879]].
- It supports Python 3.10–3.13 on Linux, Windows, and Apple Silicon Macs; Intel Macs are limited to 3.10–3.12 because `onnxruntime` (a transitive embedding dependency) no longer publishes Intel macOS wheels for Python 3.13+ [[sources/web-2026-04-11-879]].
- Python 3.14 is not yet supported on any platform because spaCy has no 3.14 wheel [[sources/web-2026-04-11-879]].
- Provider presets include Anthropic (default), OpenAI, Google, and Ollama; the Ollama backend enables zero-cost local operation [[sources/web-2026-04-11-879]].
- The architecture splits responsibilities: the LLM handles judgment (reading sources, extracting claims, assessing confidence), while linking, backlink graph maintenance, index regeneration, and git commits are deterministic [[sources/web-2026-04-11-879]].
- Every command that modifies state auto-commits with a classifying prefix such as `ingest:`, `lint:`, `merge:`, or `human-edit:` [[sources/web-2026-04-11-879]].
- WikiLoom exposes 26 commands grouped into init/save/rebuild, ingest, query and inspection, page lifecycle (merge, deprecate, purge, dormant), maintenance (lint, relink, review, reindex, protect), and observability (status, log, edits, cost) [[sources/web-2026-04-11-879]].
- A pre-flight budget check refuses ingest runs that would exceed `monthly_budget_usd` in `wikiloom.toml` (default $50/month) [[sources/web-2026-04-11-879]].
- The default embedding backend is `fastembed`, downloading a ~66MB model once into a durable per-user cache (e.g. `~/Library/Caches/wikiloom/fastembed` on macOS) [[sources/web-2026-04-11-879]].
- Recommended ingest formats are `.md`, `.txt`, `.rst`, text-based PDFs, and URLs (`http://`/`https://`); `.docx`, `.pptx`, code files, and config/IaC files are supported with caveats; scanned PDFs, Excel, large CSVs, images, and standalone HTML are not supported [[sources/web-2026-04-11-879]].
- URL ingestion works for static HTML sites but not for JavaScript-rendered apps, paywalled content, or sites with bot protection — users are told to download such pages as PDF and ingest the PDF instead [[sources/web-2026-04-11-879]].
- WikiLoom is authored by Do-Y-Lee and hosted at github.com/do-y-lee/wikiloom [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/do-y-lee]]
- [[entities/karpathy-llm-wiki-gist]]
- [[concepts/llm-wiki-pattern]]
- [[concepts/deterministic-linking]]
- [[concepts/structural-provenance]]
- [[concepts/human-edit-protection]]
- [[concepts/page-lifecycle]]
- [[concepts/per-chunk-page-context]]
- [[concepts/pre-flight-budget-check]]
- [[concepts/auto-commit-pattern]]
