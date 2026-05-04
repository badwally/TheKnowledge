---
type: concept
slug: encoder-decoder-architecture
canonical_name: Encoder-Decoder Architecture
domains:
  - ai-and-agents
---

# Encoder-Decoder Architecture

## Summary

The dominant framework for neural sequence transduction prior to and including the Transformer: an encoder maps an input sequence of symbol representations to a sequence of continuous representations, and a decoder generates an output sequence one element at a time, auto-regressively consuming previously generated symbols as additional input [[sources/pdf-ashish-vaswani-2025-attention-is-all]].

## Key claims

- Most competitive neural sequence transduction models have an encoder-decoder structure: the encoder maps an input sequence (x_1, ..., x_n) to a sequence of continuous representations z = (z_1, ..., z_n), and given z the decoder then generates an output sequence (y_1, ..., y_m) of symbols one element at a time [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- At each step the model is auto-regressive, consuming the previously generated symbols as additional input when generating the next [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The dominant sequence transduction models prior to the Transformer were based on complex recurrent or convolutional neural networks that include an encoder and a decoder, with the best performing models also connecting the encoder and decoder through an attention mechanism [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The Transformer follows this overall encoder-decoder architecture using stacked self-attention and point-wise fully connected layers for both the encoder and the decoder [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- In the Transformer's "encoder-decoder attention" layers, queries come from the previous decoder layer while memory keys and values come from the output of the encoder, allowing every position in the decoder to attend over all positions in the input sequence — mimicking the typical encoder-decoder attention mechanisms in earlier sequence-to-sequence models [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- Attention mechanisms had become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences, but in all but a few cases such attention was used in conjunction with a recurrent network [[sources/pdf-ashish-vaswani-2025-attention-is-all]].

## Sources

- [[sources/pdf-ashish-vaswani-2025-attention-is-all]]

## Related

- [[concepts/transformer-architecture]]
- [[concepts/self-attention]]
- [[concepts/multi-head-attention]]
