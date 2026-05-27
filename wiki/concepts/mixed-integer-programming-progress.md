---
schema_version: 1
type: concept
slug: mixed-integer-programming-progress
canonical_name: Algorithmic Progress in Mixed Integer Programming
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Algorithmic Progress in Mixed Integer Programming

## Summary

The 21-year track record of solver speedups on Bixby's mixed-integer-programming benchmark, used by Hernandez & Brown as the cleanest non-ML evidence that algorithmic efficiency can compound smoothly and outpace Moore's Law over multi-decade horizons [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].

## Key claims

- A 2x speedup every 13 months was observed on Bixby's benchmark of 1,892 mixed-integer problems (a subset of linear programming), described as real-world problems collected from academic and industry sources over 21 years [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- Cumulatively, the benchmark records a 500,000x speedup in MIP over 21 years (1995–roughly 2015), graphed by release date of CPLEX and Gurobi rather than version number [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- Over the same period Moore's Law yielded approximately 1,500x hardware efficiency improvement, so MIP solver progress substantially outpaced hardware [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- Progress is easy to track in this domain because there were distinct releases of commercial software (CPLEX and Gurobi) that can be compared with hardware held fixed [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- The smoothness of progress is partially explained by the measure aggregating many problems of varying difficulty, which dampens the noise visible in any single instance [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- Caveats include that the benchmark was designed by the CEO of Gurobi, who had an incentive to demonstrate large amounts of progress, and that a 30,000-second maximum search time was applied — making earlier solvers look relatively stronger and making the overall estimate conservative [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].
- The authors note that this is the related domain with the highest amount of measured algorithmic-efficiency progress they are aware of for this period, and use it to argue that an algorithmic Moore's Law is plausible for optimization problems of interest [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]].

## Sources

- [[sources/pdf-danny-hernandez-2025-measuring-the-algorithmic]]

## Related

- [[concepts/algorithmic-efficiency]]
- [[concepts/moores-law]]
