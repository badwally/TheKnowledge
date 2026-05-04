---
type: concept
slug: self-attention
canonical_name: Self-Attention
domains:
  - ai-and-agents
---

# Self-Attention

## Summary

An attention mechanism — sometimes called intra-attention — that relates different positions of a single sequence in order to compute a representation of the sequence, and that forms the foundation of the Transformer architecture introduced by Vaswani et al. (NIPS 2017) [[sources/pdf-ashish-vaswani-2025-attention-is-all]].

## Key claims

- Self-attention, sometimes called intra-attention, is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- Prior to the Transformer, self-attention had been used successfully in tasks including reading comprehension, abstractive summarization, textual entailment, and learning task-independent sentence representations [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- In the encoder of the Transformer, all of the keys, values, and queries come from the same place — the output of the previous layer — and each position can attend to all positions in the previous encoder layer [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- Self-attention layers in the decoder allow each position to attend to all positions in the decoder up to and including that position, with leftward information flow blocked by masking out (setting to −∞) all softmax inputs corresponding to illegal connections, which preserves the auto-regressive property [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- A self-attention layer connects all positions with a constant number of sequentially executed operations, whereas a recurrent layer requires O(n) sequential operations [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- In terms of computational complexity, self-attention layers are faster than recurrent layers when the sequence length n is smaller than the representation dimensionality d, which is most often the case with sentence representations used by state-of-the-art translation models [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- Self-attention reduces the maximum path length between any two input and output positions to O(1), making it easier to learn long-range dependencies than recurrent (O(n)) or convolutional (O(log_k(n))) layers [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- Three desiderata motivate the use of self-attention over recurrent and convolutional layers: total computational complexity per layer, the amount of computation that can be parallelized as measured by minimum sequential operations, and the path length between long-range dependencies [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The Transformer is, to the authors' knowledge, the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequence-aligned RNNs or convolution [[sources/pdf-ashish-vaswani-2025-attention-is-all]].

## Sources

- [[sources/pdf-ashish-vaswani-2025-attention-is-all]]

## Related

- [[concepts/transformer-architecture]]
- [[concepts/scaled-dot-product-attention]]
- [[concepts/multi-head-attention]]
- [[concepts/encoder-decoder-architecture]]
