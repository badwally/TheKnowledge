---
type: concept
slug: transformer-architecture
canonical_name: Transformer Architecture
domains:
  - ai-and-agents
---

# Transformer Architecture

## Summary

A neural sequence transduction architecture introduced by Vaswani et al. (NIPS 2017) that relies entirely on attention mechanisms — dispensing with recurrence and convolutions — and that achieves state-of-the-art translation quality while being significantly more parallelizable and cheaper to train than prior recurrent or convolutional encoder-decoder models [[sources/pdf-ashish-vaswani-2025-attention-is-all]].

## Key claims

- The Transformer is described as a "new simple network architecture ... based solely on attention mechanisms, dispensing with recurrence and convolutions entirely" [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The architecture follows an overall encoder-decoder structure built from stacked self-attention and point-wise fully connected layers for both the encoder and the decoder [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The encoder is composed of a stack of N=6 identical layers, each with two sub-layers: a multi-head self-attention mechanism and a position-wise fully connected feed-forward network, with residual connections around each sub-layer followed by layer normalization [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The decoder is also composed of a stack of N=6 identical layers and inserts a third sub-layer that performs multi-head attention over the encoder stack's output, while modifying the self-attention sub-layer to prevent positions from attending to subsequent positions and thereby preserve the auto-regressive property [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- All sub-layers and embedding layers produce outputs of dimension d_model = 512, and the inner-layer of the position-wise feed-forward network has dimensionality d_ff = 2048 [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The Transformer is, to the authors' knowledge, the first transduction model to rely entirely on self-attention to compute representations of its input and output without using sequence-aligned RNNs or convolution [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The Transformer reduces the number of operations required to relate signals from two arbitrary input or output positions to a constant — versus linear for ConvS2S and logarithmic for ByteNet — at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect counteracted by Multi-Head Attention [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The Transformer achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results — including ensembles — by over 2 BLEU [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- On the WMT 2014 English-to-French translation task, the Transformer establishes a new single-model state-of-the-art BLEU score of 41.0 after training for 3.5 days on eight GPUs, a small fraction of the training cost of prior best models [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The architecture is designed to allow for significantly more parallelization than recurrent models because it eliminates the inherently sequential factorization of computation along symbol positions [[sources/pdf-ashish-vaswani-2025-attention-is-all]].

## Sources

- [[sources/pdf-ashish-vaswani-2025-attention-is-all]]

## Related

- [[concepts/self-attention]]
- [[concepts/multi-head-attention]]
- [[concepts/scaled-dot-product-attention]]
- [[concepts/positional-encoding]]
- [[concepts/encoder-decoder-architecture]]
- [[entities/ashish-vaswani]]
- [[entities/noam-shazeer]]
- [[entities/google-brain]]
