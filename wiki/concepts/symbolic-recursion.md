---
schema_version: 1
type: concept
slug: symbolic-recursion
canonical_name: Symbolic Recursion
domains:
- ai-and-agents
created_at: '2026-06-23T16:16:04Z'
last_updated: '2026-06-23T16:16:04Z'
---

# Symbolic Recursion

## Summary

A design property identified by Zhang, Kraska, and Khattab (2026) as the most important distinguishing feature of Recursive Language Models: code running inside a REPL environment must be able to invoke the base LLM on programmatically constructed transformations of the prompt — for example, inside arbitrarily large loops — and store intermediate results symbolically [[sources/pdf-5c2f94fd33cd]].

## Key claims

- Symbolic recursion requires that code running inside the REPL environment E be able to invoke the base model M on programmatically constructed transformations of P, including inside arbitrarily large loops, while storing intermediate results symbolically [[sources/pdf-5c2f94fd33cd]].
- Scaffolds that include both a code-execution action and a separate sub-LLM action without programmatic invocation can only delegate a few explicitly verbalized tasks rather than writing short programs that loop over slices of the prompt [[sources/pdf-5c2f94fd33cd]].
- Symbolic recursion enables on the order of Ω(|P|) or even Ω(|P|^2) processes to understand or transform all parts of the prompt P [[sources/pdf-5c2f94fd33cd]].
- Prior coding agents and retrieval agents treat some designated external data source as an environment for fetching snippets, but can only fill up the underlying LLM's context window with snippets before breaking down [[sources/pdf-5c2f94fd33cd]].
- Prior self-delegation approaches allow LLMs to invoke themselves as sub-agents but are capped by the underlying LLM's limited output lengths because they verbalize sub-calls autoregressively rather than producing them programmatically [[sources/pdf-5c2f94fd33cd]].

## Sources

- [[sources/pdf-5c2f94fd33cd]]

## Related

- [[concepts/recursive-language-model]]
- [[concepts/context-compaction]]
