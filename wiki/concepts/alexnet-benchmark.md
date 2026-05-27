---
schema_version: 1
type: concept
slug: alexnet-benchmark
canonical_name: AlexNet-Level ImageNet Performance as Efficiency Anchor
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# AlexNet-Level ImageNet Performance as Efficiency Anchor

## Summary

A fixed capability target — 79.1% top-5 accuracy on ImageNet, the level achieved by AlexNet (Krizhevsky et al., 2012) — used by Hernandez & Brown as the constant-performance anchor against which the compute cost of reaching that capability can be tracked over time [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].

## Key claims

- The authors operationalize AlexNet-level performance as 79.1% top-5 accuracy on ImageNet [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- AlexNet kicked off the wave of interest in neural networks, and ImageNet remains a benchmark of wide interest, so this measure provides a long-running trend to analyze [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- Holding this performance level constant, the FLOPs needed to train a classifier to that target fell 44x between 2012 and 2019 [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- A parallel ResNet-50-level target (92.9% top-5 ImageNet accuracy) shows a similar rate of progress, with a 10x reduction in training FLOPs and, on DawnBench, a 184x reduction in training cost in dollars from $2,323 to $12.60 [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- It is impractical to perform Big-O-style analysis for deep learning because solutions are approximate and there is no clean measure of problem difficulty; in machine learning, progress is therefore typically reported in terms of new states-of-the-art rather than cost — the AlexNet-level anchor provides a way to recover the cost dimension [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- Holding capability constant addresses four problems that make raw SOTA reporting hard to interpret: incommensurable performance metrics across tasks, non-comparable problem difficulty, conflation of efficiency gains with extra compute, and benchmarks being solved more rapidly than they used to be (e.g., 15 years to human-level on MNIST, 7 on ImageNet, 9 months on GLUE) [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].

## Sources

- [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]]

## Related

- [[concepts/algorithmic-efficiency]]
- [[concepts/moores-law]]
