---
type: concept
slug: dgm-hyperagents
canonical_name: DGM-Hyperagents (DGM-H)
domains:
  - ai-and-agents
---

# DGM-Hyperagents (DGM-H)

## Summary

The system introduced in Zhang et al. (2026) that extends the Darwin Gödel Machine with hyperagents — keeping the open-ended exploration structure of the DGM (an archive of stepping stones grown by branching, self-modification, and evaluation) but allowing the self-modification procedure itself to be modified, so the system is no longer constrained by an alignment between task-solving and self-modification skills [[sources/pdf-jenny-zhang-2026-hyperagents]].

## Key claims

- DGM-H extends the Darwin Gödel Machine with hyperagents, replacing the DGM's fixed handcrafted instruction-generation step with a self-referential, modifiable improvement procedure [[sources/pdf-jenny-zhang-2026-hyperagents]].
- DGM-H retains the open-ended exploration structure of the DGM: it grows an archive of hyperagents by branching from selected candidates, allowing them to self-modify, evaluating the resulting hyperagents, and adding them back to the archive [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Because a hyperagent can modify its own self-modification process, DGM-H is not constrained by its initial implementation and can potentially self-improve for any computable task [[sources/pdf-jenny-zhang-2026-hyperagents]].
- On the Polyglot coding benchmark (Gauthier, 2024), DGM-H achieves gains comparable to the DGM despite not being handcrafted for coding [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Beyond coding, DGM-H substantially improves performance on paper review (Zhao et al., 2026) and robotics reward design (Genesis, 2024), with gains transferring to held-out test tasks and significantly outperforming prior self-improving algorithms, which struggle outside coding unless customized [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Ablations without self-improvement or without open-ended exploration show little to no progress, highlighting the necessity of each component [[sources/pdf-jenny-zhang-2026-hyperagents]].
- DGM-H learns transferable mechanisms for self-improvement — including persistent memory and performance tracking — that systematically improve its ability to generate better task or meta agents over time [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Meta-level improvements learned by DGM-H transfer across domains: hyperagents optimized in one setting (paper review and robotics tasks) remain significantly effective at generating improved task agents in a different domain (Olympiad-level math grading) [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Self-improvements learned by DGM-H in one setting can compound with continued self-improvement in another, suggesting potential for unbounded open-ended self-improvement over time [[sources/pdf-jenny-zhang-2026-hyperagents]].
- All experiments were conducted with safety precautions, including sandboxing and human oversight [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Code is released at github.com/facebookresearch/Hyperagents [[sources/pdf-jenny-zhang-2026-hyperagents]].

## Sources

- [[sources/pdf-jenny-zhang-2026-hyperagents]]

## Related

- [[concepts/hyperagent]]
- [[concepts/darwin-godel-machine]]
- [[concepts/metacognitive-self-modification]]
- [[concepts/open-ended-self-improvement]]
- [[concepts/recursive-self-improvement]]
- [[entities/fair-at-meta]]
