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

WikiLoom is a Python tool that ingests documents (PDFs, markdown files, URLs) and uses an LLM to write structured wiki pages with deterministic linking, structural provenance, and human-edit protection . It auto-commits every state-modifying operation to git with a classifying prefix . The project is inspired by Andrej Karpathy's LLM wiki gist .

## Key facts

- Authored by Do-Y-Lee and hosted at github.com/do-y-lee/wikiloom .
- Installed via `pip install wikiloom` and requires the spaCy `en_core_web_sm` model .
- Supports Python 3.10–3.13 on Linux, Windows, and Apple Silicon Macs; Python 3.10–3.12 on Intel Macs because `onnxruntime` no longer publishes Intel macOS wheels for 3.13+ .
- Default LLM provider is Anthropic; OpenAI, Google, and Ollama (zero-cost local) are also supported via the `--provider` flag at `wikiloom init` time .
- Project layout includes `wikiloom.toml` for config, a `.env` for API keys, and a `.wikiloom/` directory with customizable prompts and a page schema .
- Exposes 26 CLI commands grouped into ingest, query, lifecycle, hygiene, and observability categories .
- Default monthly budget is $50, enforced via a pre-flight token-cost check .
- Default embedding backend is `fastembed` (~66MB), cached in a per-user durable location across macOS, Linux, and Windows .
- URL ingestion works on static HTML sites but does not handle JavaScript-rendered pages, paywalled content, or sites with bot protection / WAF .
- Page status lifecycle is `active → dormant (optional) → deprecated → purged (gone)` .

## Sources

- — WikiLoom GitHub README

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
