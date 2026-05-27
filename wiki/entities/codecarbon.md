---
schema_version: 1
type: entity
slug: codecarbon
canonical_name: CodeCarbon
entity_kind: organization
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# CodeCarbon

## Summary

Open-source Python tool used to measure the energy and carbon footprint of compute workloads; the "Video Killed the Energy Budget" study uses it to log GPU and CPU energy via NVML and pyRAPL, with RAM energy estimated by its default heuristic [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Key facts

- Used by the "Video Killed the Energy Budget" study (Delavande et al., 2025) to measure GPU and CPU energy during inference of open text-to-video models, on a dedicated NVIDIA H100 SXM (80 GB HBM3) paired with an 8-core AMD EPYC 7R13 CPU [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Interfaces with NVIDIA's NVML library for GPU energy and with pyRAPL for CPU energy [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Estimates RAM energy via its default heuristic, documented at mlco2.github.io/codecarbon [[sources/pdf-julien-delavande-2025-video-killed-the]].
- Cited as Courty et al. (2024) in the paper [[sources/pdf-julien-delavande-2025-video-killed-the]].

## Sources

- [[sources/pdf-julien-delavande-2025-video-killed-the]]

## Related

- [[entities/sasha-luccioni]]
- [[concepts/generative-ai-energy-footprint]]
