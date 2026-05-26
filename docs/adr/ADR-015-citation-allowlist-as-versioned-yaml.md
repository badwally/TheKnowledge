# ADR-015: Citation allowlist as versioned YAML (not hardcoded Python)

**Status:** Accepted
**Date:** 2026-05-25

## Context

The citation grounding validator must exempt certain sentence patterns from the "every claim needs a citation" rule: structural frame labels (`**Themes Used In:**`), aggregate framing openers (`Based on the provided sources...`), and NLM-compat phrases that appear in LLM-generated content. This exemption list evolves as new prompt templates are deployed.

## Decision

Exemptions live in `src/gateway/data/citations_allowlist.yaml` (ARCH-10). The file contains two keys: `structural_frame_labels` (exact strings) and `aggregate_framing_openers` (regex fragments). `citations.py` loads the YAML at import time and builds the exemption sets. Updating an exemption requires editing the YAML and committing; the change is tracked in git history.

Hardcoding the exemptions as Python lists was rejected: they would be scattered across `citations.py` and `validator.py` with no clear ownership boundary. Every update would require a code review to confirm no logic changed. Storing exemptions in a database table was rejected as unnecessary infrastructure for a list that changes rarely and needs to be auditable.

## Consequences

The allowlist is a shared global loaded at import time — tests that need different allowlist behavior must monkeypatch the compiled sets rather than the YAML file. The YAML format must remain stable; adding new top-level keys requires updating `citations.py`. Exemptions that are too broad (e.g., a generic phrase that also matches real claim sentences) silently suppress citation errors rather than surfacing them.
