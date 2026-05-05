---
type: concept
slug: intelligent-ai-delegation
canonical_name: Intelligent AI Delegation
domains:
  - ai-and-agents
---

# Intelligent AI Delegation

## Summary

A framework, proposed by Tomašev, Franklin, and Osindero (Google DeepMind, 2026), that defines AI delegation as a sequence of decisions involving task allocation together with transfer of authority, responsibility, accountability, clear specifications of roles and boundaries, clarity of intent, and mechanisms for establishing trust between two or more parties — applicable to both human and AI delegators and delegatees in complex delegation networks [[sources/pdf-nenad-toma-2026-intelligent-ai-delegation]].

## Key claims

- Existing task decomposition and delegation methods rely on simple heuristics and cannot dynamically adapt to environmental changes or robustly handle unexpected failures, limiting AI deployments in high-stakes environments [[sources/pdf-nenad-toma-2026-intelligent-ai-delegation]].
- Delegation goes beyond task decomposition: it additionally requires assignment of responsibility and authority, implicating accountability for outcomes, and involves risk assessment moderated by trust (Castelfranchi and Falcone, 1998; Griffiths, 2005) [[sources/pdf-nenad-toma-2026-intelligent-ai-delegation]].
- The framework enumerates several axes used to contextualize delegation cases: delegator (human or AI), delegatee (human or AI), task characteristics, granularity, autonomy, monitoring, and reciprocity [[sources/pdf-nenad-toma-2026-intelligent-ai-delegation]].
- The task-characteristics axis decomposes further into eleven sub-properties: complexity, criticality, uncertainty, duration, cost, resource requirements, constraints, verifiability, reversibility, contextuality, and subjectivity [[sources/pdf-nenad-toma-2026-intelligent-ai-delegation]].
- High-verifiability tasks (e.g., formal code verification, mathematical proofs) allow "trustless" delegation or automated checking, while low-verifiability tasks (e.g., open-ended research) require high-trust delegatees or expensive labor-intensive oversight [[sources/pdf-nenad-toma-2026-intelligent-ai-delegation]].
- Irreversible tasks with real-world side effects (e.g., executing a financial trade, deleting a database, sending an external email) require stricter liability firebreaks and steeper authority gradients than reversible tasks (e.g., drafting an email, flagging a database entry) [[sources/pdf-nenad-toma-2026-intelligent-ai-delegation]].
- High-context tasks introduce larger privacy surface areas, whereas context-free tasks can more easily be compartmentalized and outsourced to lower-trust nodes [[sources/pdf-nenad-toma-2026-intelligent-ai-delegation]].
- Highly subjective tasks (e.g., "design a compelling logo") typically require "Human-as-Value-Specifier" intervention and iterative feedback loops, whereas objective tasks can be governed by stricter, binary contracts [[sources/pdf-nenad-toma-2026-intelligent-ai-delegation]].
- Three core delegator-delegatee scenarios are: (1) human delegates to AI agent, (2) AI agent delegates to AI agent, and (3) AI agent delegates to a human; agent-agent and AI-to-human delegation are expected to grow with the emergence of virtual agentic markets and economies [[sources/pdf-nenad-toma-2026-intelligent-ai-delegation]].
- Delegation between agents may be hierarchical (e.g., orchestrator agent delegating to a sub-agent) or non-hierarchical (peer agents with equal standing); an advanced AI agent may also delegate to a specialist ML model with no notable agency [[sources/pdf-nenad-toma-2026-intelligent-ai-delegation]].
- Davidson and Hadshar (2025), cited in the paper, predict a coming increase in "AI-directed human labour" that may significantly increase economic productivity, while present-day algorithmic-management deployments in ride-hailing and logistics often degrade rather than enhance worker welfare (Beverungen 2021; Lee et al. 2015; Rosenblat and Stark 2016) [[sources/pdf-nenad-toma-2026-intelligent-ai-delegation]].

## Sources

- [[sources/pdf-nenad-toma-2026-intelligent-ai-delegation]] — Intelligent AI Delegation (Tomašev, Franklin, Osindero, 2026)

## Related

- [[entities/nenad-tomasev]]
- [[entities/matija-franklin]]
- [[entities/simon-osindero]]
- [[entities/google-deepmind]]
- [[concepts/principal-agent-problem]]
- [[concepts/span-of-control]]
- [[concepts/authority-gradient]]
- [[concepts/reward-misspecification]]
- [[concepts/deceptive-alignment]]
