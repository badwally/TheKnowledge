---
schema_version: 1
type: concept
slug: positional-encoding
canonical_name: Positional Encoding
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Positional Encoding

## Summary

A technique used in the Transformer to inject information about the relative or absolute position of tokens into a model that contains no recurrence or convolution; Vaswani et al. add fixed sinusoidal functions of different frequencies to the input embeddings, with wavelengths forming a geometric progression from 2π to 10000·2π [[sources/pdf-ashish-vaswani-2025-attention-is-all]].

## Key claims

- Because the Transformer contains no recurrence and no convolution, in order for the model to make use of the order of the sequence it must inject some information about the relative or absolute position of tokens [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- Positional encodings are added to the input embeddings at the bottoms of the encoder and decoder stacks, and have the same dimension d_model as the embeddings so that the two can be summed [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The chosen encoding uses sine and cosine functions of different frequencies: PE_(pos,2i) = sin(pos / 10000^(2i/d_model)) and PE_(pos,2i+1) = cos(pos / 10000^(2i/d_model)) [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- Each dimension of the positional encoding corresponds to a sinusoid, and the wavelengths form a geometric progression from 2π to 10000·2π [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The authors hypothesize that this function would allow the model to easily learn to attend by relative positions, since for any fixed offset k, PE_(pos+k) can be represented as a linear function of PE_pos [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The authors also experimented with learned positional embeddings and found that the two versions produced nearly identical results; they chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than those encountered during training [[sources/pdf-ashish-vaswani-2025-attention-is-all]].
- The contribution footnote credits Noam Shazeer with proposing the parameter-free position representation used in the Transformer [[sources/pdf-ashish-vaswani-2025-attention-is-all]].

## Sources

- [[sources/pdf-ashish-vaswani-2025-attention-is-all]]

## Related

- [[concepts/transformer-architecture]]
- [[concepts/self-attention]]
- [[entities/noam-shazeer]]
