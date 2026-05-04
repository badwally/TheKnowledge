---
type: concept
slug: algorithmic-efficiency
canonical_name: Algorithmic Efficiency in Neural Networks
domains:
  - ai-and-agents
---

# Algorithmic Efficiency in Neural Networks

## Summary

A framework introduced by Hernandez & Brown for measuring algorithmic progress in machine learning by holding capability constant and tracking the reduction over time in the compute (FLOPs) needed to reach that capability — the deep-learning analogue of asymptotic-cost analysis in classical computer science [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].

## Key claims

- Three factors drive the advance of AI: algorithmic innovation, data, and the amount of compute available for training; algorithmic progress has traditionally been more difficult to quantify than compute and data [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- The paper argues that algorithmic progress has an aspect that is both straightforward to measure and interesting: reductions over time in the compute needed to reach past capabilities [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- The number of floating-point operations required to train a classifier to AlexNet-level performance on ImageNet decreased by a factor of 44x between 2012 and 2019 [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- This corresponds to algorithmic efficiency doubling every 16 months over a period of 7 years, outpacing the original Moore's Law rate of improvement in hardware efficiency (11x over the same period) [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- The authors observe that hardware and algorithmic efficiency gains multiply and can be on a similar scale over meaningful horizons, which suggests that a good model of AI progress should integrate measures from both [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- In classic computer-science problems like sorting, algorithmic quality is measured asymptotically (e.g., O(n log n) for quicksort); deep learning resists this analysis because solutions are approximate and problem difficulty is not cleanly defined, motivating the constant-capability approach [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- The authors focused on training efficiency rather than inference efficiency because they were more interested in what systems are possible to produce than in how much it costs to run those systems [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- They measured total floating-point operations used in training rather than parameters or another efficiency proxy, because in their research setting they were typically FLOPs-bound rather than memory- or communication-bound [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- The 44x AlexNet-level efficiency gain is attributed to sparsity, batch normalization, residual connections, architecture search, and appropriate scaling [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- A similar rate of progress was observed for ResNet-50-level classification performance, and faster rates of efficiency improvement were observed in Go, Dota, and machine translation [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- The authors caveat that it is unclear the degree to which the observed efficiency trends generalize to other AI tasks, and that new capabilities are probably a larger portion of progress than observed efficiency gains [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- They speculate there may be an algorithmic Moore's Law for optimization problems of interest, given the smoothness of the trend across multiple domains [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].

## Sources

- [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]]

## Related

- [[concepts/training-compute-scaling]]
- [[concepts/effective-training-compute]]
- [[concepts/moores-law]]
- [[concepts/alexnet-benchmark]]
- [[concepts/scaling-laws]]
- [[concepts/mixed-integer-programming-progress]]
- [[entities/danny-hernandez]]
- [[entities/tom-brown]]
- [[entities/openai]]
