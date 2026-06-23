---
schema_version: 1
type: concept
slug: recursive-language-model
canonical_name: Recursive Language Model (RLM)
domains:
- ai-and-agents
created_at: '2026-06-23T16:16:03Z'
last_updated: '2026-06-23T16:16:03Z'
---

# Recursive Language Model (RLM)

## Summary

A general inference paradigm proposed by Zhang, Kraska, and Khattab (2026) that treats long prompts as part of an external environment and allows the LLM to programmatically examine, decompose, and recursively call itself over snippets of the prompt [[sources/pdf-5c2f94fd33cd]].

## Key claims

- An RLM is an inference-time scaffold around a base language model M that treats the user prompt as part of the environment without giving up the ability to densely process its content through different calls to M [[sources/pdf-5c2f94fd33cd]].
- Given a prompt P, the RLM initializes a Read-Eval-Print Loop (REPL) programming environment in which P is set as the value of a variable [[sources/pdf-5c2f94fd33cd]].
- The RLM offers the LLM general context about the REPL environment, such as the length of the string P, and permits it to write code that peeks into and decomposes P, iteratively observing any side effects from execution [[sources/pdf-5c2f94fd33cd]].
- The key insight is that arbitrarily long user prompts should not be fed into the neural network directly but should instead be treated as part of the environment that the LLM is tasked to symbolically and recursively interact with [[sources/pdf-5c2f94fd33cd]].
- RLMs encourage the LLM to understand, transform, and execute the input prompt by writing symbolic programs that invoke the LLM itself on as many slices of the input as necessary [[sources/pdf-5c2f94fd33cd]].
- The same external interface as an LLM or reasoning model is preserved: an RLM accepts a string prompt of arbitrary structure and produces a string response [[sources/pdf-5c2f94fd33cd]].
- RLMs make three design choices missing from existing scaffolds: a symbolic handle to the user prompt, programmatically generated outputs rather than autoregressive verbalization, and symbolic recursion that lets code invoke M on programmatically constructed transformations of P [[sources/pdf-5c2f94fd33cd]].
- Only constant-size metadata about the input prompt and about stdout, like a short prefix and length, is appended to the model's history per iteration, forcing the model to rely on variables and sub-calls to manage long strings rather than polluting its window [[sources/pdf-5c2f94fd33cd]].
- Iteration stops once the RLM sets the variable Final inside the REPL, at which point the value in Final is returned as the response [[sources/pdf-5c2f94fd33cd]].
- RLMs can successfully process inputs up to two orders of magnitude beyond model context windows [[sources/pdf-5c2f94fd33cd]].
- Even for shorter prompts, RLMs dramatically outperform the quality of vanilla frontier LLMs and common long-context scaffolds across four diverse long-context tasks while having comparable cost [[sources/pdf-5c2f94fd33cd]].
- The authors evaluate RLMs using a frontier closed model (GPT-5) and a frontier open model (Qwen3-Coder-480B-A35B) across deep research, information aggregation, code repository understanding, and a synthetic pairwise reasoning task where even frontier models fail catastrophically [[sources/pdf-5c2f94fd33cd]].
- RLMs demonstrate extremely strong performance even at the 10M+ token scale and substantially outperform direct LLM calls, context compaction, retrieval tool-use agents, and code-generation agents, in many cases by double-digit percentage gains [[sources/pdf-5c2f94fd33cd]].
- At small scale, the authors post-train RLM-Qwen3-8B as the first natively recursive language model, outperforming the underlying Qwen3-8B by a median of 28.3% across four long-context evaluation tasks [[sources/pdf-5c2f94fd33cd]].
- Code is released at https://github.com/alexzhang13/rlm [[sources/pdf-5c2f94fd33cd]].

## Sources

- [[sources/pdf-5c2f94fd33cd]]

## Related

- [[concepts/context-rot]]
- [[concepts/context-compaction]]
- [[concepts/symbolic-recursion]]
- [[concepts/long-context-llm-evaluation]]
- [[entities/alex-l-zhang]]
- [[entities/omar-khattab]]
- [[entities/tim-kraska]]
- [[entities/mit-csail]]
- [[entities/rlm-qwen3-8b]]
