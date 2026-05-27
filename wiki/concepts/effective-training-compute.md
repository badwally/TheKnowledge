---
schema_version: 1
type: concept
slug: effective-training-compute
canonical_name: Effective Training Compute
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Effective Training Compute

## Summary

A composite measure of how much capability-equivalent compute is actually available to the largest AI experiments, combining hardware improvements, increases in spending, and algorithmic efficiency gains; Hernandez & Brown estimate this metric grew by a factor of 7.5 million between 2012 and 2018 [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].

## Key claims

- Hernandez & Brown estimate a 7.5 million-times increase in the effective training compute available to the largest AI experiments between 2012 and 2018 [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- The authors emphasize that hardware and algorithmic efficiency gains multiply rather than add, so a complete model of AI progress must integrate measures from both [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- DawnBench results illustrate that training cost in dollars aggregates four distinct effects: algorithmic-progress efficiency gains, Moore's-Law effects on GPUs/TPUs, reduced cloud-computing costs from modernization and competition, and improvements in hardware utilization [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- DawnBench submissions reduced the cost of training a ResNet-50-level ImageNet model from $2,323 to $12.60 — a 184x cost reduction in less than a year [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- More targeted measurements like training efficiency in FLOPs help disentangle which of the four effects is responsible, clarifying takeaways from aggregate dollar-cost benchmarks [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- Bloom et al. (2017), cited in the paper, observe that the number of researchers required today to maintain Moore's Law is more than 18x the number required in the early 1970s — i.e., research productivity is declining and exponential progress is sustained by exponentially rising research effort [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].

## Sources

- [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]]

## Related

- [[concepts/algorithmic-efficiency]]
- [[concepts/training-compute-scaling]]
- [[concepts/moores-law]]
