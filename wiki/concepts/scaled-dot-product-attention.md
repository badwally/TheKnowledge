---
schema_version: 1
type: concept
slug: scaled-dot-product-attention
canonical_name: Scaled Dot-Product Attention
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Scaled Dot-Product Attention

## Summary

The attention function used as a building block of the Transformer, defined as Attention(Q,K,V) = softmax(QK^T / √d_k) V, where the 1/√d_k scaling factor counteracts vanishing gradients in the softmax that would otherwise occur for large key dimensionality [[sources/pdf-ashish-vaswani-2025-attention-is-all]].

## Key claims

- Scaled dot-product attention takes queries and keys of dimension d_k and values of dimension d_v, computes the dot products of the query with all keys, divides each by √d_k, and applies a softmax function to obtain the weights on the values [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- In matrix form, the attention output is computed as Attention(Q,K,V) = softmax(QK^T / √d_k) V, with queries packed into Q and keys and values packed into K and V respectively [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The two most commonly used attention functions prior to the Transformer were additive attention and dot-product (multiplicative) attention; dot-product attention is identical to scaled dot-product attention except for the scaling factor of 1/√d_k [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- Additive attention computes the compatibility function using a feed-forward network with a single hidden layer; while the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice because it can be implemented using highly optimized matrix multiplication code [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- For small values of d_k the two mechanisms perform similarly, but additive attention outperforms unscaled dot-product attention for larger d_k; the authors suspect that for large d_k the dot products grow large in magnitude, pushing the softmax into regions of extremely small gradients [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The 1/√d_k scaling counteracts this gradient-saturation effect; assuming q and k components are independent random variables with mean 0 and variance 1, their dot product has mean 0 and variance d_k, motivating the choice of √d_k [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The contribution footnote credits Noam Shazeer with proposing scaled dot-product attention [[sources/pdf-ashish-vaswani-2025-attention-is-all]].

## Sources

- [[sources/pdf-ashish-vaswani-2025-attention-is-all]]

## Related

- [[concepts/self-attention]]
- [[concepts/multi-head-attention]]
- [[concepts/transformer-architecture]]
- [[entities/noam-shazeer]]
