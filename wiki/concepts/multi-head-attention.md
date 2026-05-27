---
schema_version: 1
type: concept
slug: multi-head-attention
canonical_name: Multi-Head Attention
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Multi-Head Attention

## Summary

A mechanism used throughout the Transformer that runs h scaled-dot-product attention layers in parallel on linearly projected, lower-dimensional versions of the queries, keys, and values, then concatenates and re-projects the results — allowing the model to jointly attend to information from different representation subspaces at different positions [[sources/pdf-ashish-vaswani-2025-attention-is-all]].

## Key claims

- Instead of performing a single attention function with d_model-dimensional keys, values, and queries, the Transformer linearly projects the queries, keys, and values h times with different learned linear projections to d_k, d_k, and d_v dimensions respectively [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- On each projected version, attention is performed in parallel, yielding d_v-dimensional output values that are concatenated and once again projected to produce the final output [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- Formally: MultiHead(Q,K,V) = Concat(head_1, ..., head_h) W^O, where head_i = Attention(Q W_i^Q, K W_i^K, V W_i^V) [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions; with a single attention head, averaging inhibits this [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The Transformer employs h = 8 parallel attention layers (heads), with d_k = d_v = d_model / h = 64; due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The Transformer uses multi-head attention in three different ways: encoder-decoder attention layers (queries from the previous decoder layer, keys/values from the encoder output), encoder self-attention layers, and decoder self-attention layers (with masking to prevent attending to subsequent positions) [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- Multi-head attention partly counteracts the reduction in effective resolution caused by averaging attention-weighted positions in self-attention [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The contribution footnote credits Noam Shazeer with proposing multi-head attention [[sources/pdf-ashish-vaswani-2025-attention-is-all]].

## Sources

- [[sources/pdf-ashish-vaswani-2025-attention-is-all]]

## Related

- [[concepts/self-attention]]
- [[concepts/scaled-dot-product-attention]]
- [[concepts/transformer-architecture]]
- [[entities/noam-shazeer]]
