---
type: concept
slug: statistical-relational-learning
canonical_name: Statistical Relational Learning
domains:
  - ai-and-agents
---

# Statistical Relational Learning

## Summary

A research field that aims to unify logical and probabilistic frameworks by controlling expressiveness — for example, via finite-domain relational extensions to Bayesian networks; described by Belle and Marcus (AAAI-26) as a foundational antecedent of neuro-symbolic AI and the basis for one well-defined view of neuro-symbolic AI as the neural extension of weighted model counting [[sources/pdf-vaishak-belle-2026-the-future-is]].

## Key claims

- Statistical relational learning (SRL) aimed to unify logical and probabilistic frameworks by controlling the expressiveness of representations (Raedt et al. 2016), for example via finite-domain relational extensions to Bayesian networks (Koller and Pfeffer 1997; Getoor et al. 2001) [[sources/pdf-vaishak-belle-2026-the-future-is]].
- SRL built on the success of Bayesian and later causal networks (Pearl 1998), which offered a reasonable compromise between expert knowledge and probabilistic/statistical information and were amenable to certain types of learning from data (Koller and Friedman 2009) [[sources/pdf-vaishak-belle-2026-the-future-is]].
- Earlier probabilistic logics (Bacchus 1990; Halpern 2003) inherited the expressive power of (often first-order) logic and extended it for probabilistic knowledge, but suffered from scalability issues and largely glossed over the question of where probabilities came from (Valiant 1999) [[sources/pdf-vaishak-belle-2026-the-future-is]].
- A purely expert-driven SRL paradigm for high-dimensional data is unlikely to succeed unless data-heavy computation is outsourced to neural networks — a foundational motivation for neuro-symbolic AI [[sources/pdf-vaishak-belle-2026-the-future-is]].
- One important branch of neuro-symbolic AI builds directly on SRL by combining probabilistic logical models with neural training (De Raedt et al. 2020), giving a well-defined and scoped view of neuro-symbolic AI as the neural extension of weighted model counting (Belle 2017; Chavira and Darwiche 2008; Sang, Beame, and Kautz 2005; Van den Broeck, Meert, and Darwiche 2014) [[sources/pdf-vaishak-belle-2026-the-future-is]].

## Sources

- [[sources/pdf-vaishak-belle-2026-the-future-is]]

## Related

- [[concepts/neuro-symbolic-ai]]
- [[entities/deepproblog]]
- [[entities/vaishak-belle]]
