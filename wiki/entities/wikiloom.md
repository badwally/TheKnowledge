---
schema_version: 1
type: entity
slug: wikiloom
canonical_name: WikiLoom
entity_kind: software
domains:
- knowledge-management
draft: true
draft_started_at: '2026-05-05T00:22:48Z'
draft_unresolved_claims: 0
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# WikiLoom

## Summary

WikiLoom is a Python tool that ingests documents (PDFs, markdown files, URLs) and uses an LLM to write structured wiki pages with deterministic linking, structural provenance, and human-edit protection [[sources/web-2026-04-11-879]]. It auto-commits every state-modifying operation to git with a classifying prefix [[sources/web-2026-04-11-879]]. The project is inspired by Andrej Karpathy's LLM wiki gist [[sources/web-2026-04-11-879]].

## Key facts

- Authored by Do-Y-Lee and hosted at github.com/do-y-lee/wikiloom [[sources/web-2026-04-11-879]].
- Installed via `pip install wikiloom` and requires the spaCy `en_core_web_sm` model [[sources/web-2026-04-11-879]].
- Supports Python 3.10–3.13 on Linux, Windows, and Apple Silicon Macs; Python 3.10–3.12 on Intel Macs because `onnxruntime` no longer publishes Intel macOS wheels for 3.13+ [[sources/web-2026-04-11-879]].
- Default LLM provider is Anthropic; OpenAI, Google, and Ollama (zero-cost local) are also supported via the `--provider` flag at `wikiloom init` time [[sources/web-2026-04-11-879]].
- Project layout includes `wikiloom.toml` for config, a `.env` for API keys, and a `.wikiloom/` directory with customizable prompts and a page schema [[sources/web-2026-04-11-879]].
- Exposes 26 CLI commands grouped into ingest, query, lifecycle, hygiene, and observability categories [[sources/web-2026-04-11-879]].
- Default monthly budget is $50, enforced via a pre-flight token-cost check [[sources/web-2026-04-11-879]].
- Default embedding backend is `fastembed` (~66MB), cached in a per-user durable location across macOS, Linux, and Windows [[sources/web-2026-04-11-879]].
- URL ingestion works on static HTML sites but does not handle JavaScript-rendered pages, paywalled content, or sites with bot protection / WAF [[sources/web-2026-04-11-879]].
- Page status lifecycle is `active → dormant (optional) → deprecated → purged (gone)` [[sources/web-2026-04-11-879]].

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
