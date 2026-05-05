"""Corpus-constructive research orchestrator.

`wiki research <prompt>` fans out searches across enabled adapters, runs
the semantic filter, materializes accepted sources through the existing
converter family, pushes them into a NotebookLM session notebook, runs
NotebookLM-driven analysis (taxonomy / per-branch investigation /
cross-cutting synthesis), files the output as wiki pages with resolved
citations, and on success promotes session sources into the persistent
domain notebook.

Public entry point: `gateway.research.orchestrator.research`.
"""
