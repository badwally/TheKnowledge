---
schema_version: 1
type: synthesis
slug: on-device-llm-inference-quantization-gguf
title: 'On-Device LLM Inference: Quantization, NPU/Apple Silicon Acceleration, Runtimes,
  and Quality vs Latency'
domains:
- edge-ai-agentic
question: 'On-device LLM inference: quantization (GGUF, AWQ, GPTQ), NPU and Apple
  Silicon acceleration, runtime engines, and quality versus latency tradeoffs'
draft: true
draft_started_at: '2026-04-28T00:00:00Z'
draft_unresolved_claims: 11
created_at: '2026-04-28T17:26:18Z'
last_updated: '2026-04-28T17:26:18Z'
sources_count: 14
---

# On-Device LLM Inference: Quantization, NPU/Apple Silicon Acceleration, Runtimes, and Quality vs Latency

*Cross-cutting synthesis across the edge-ai-agentic corpus.*

## Related branches

- [[mocs/on-device-inference-foundations|On-Device Inference Foundations]]
- [[mocs/edge-hardware-platforms|Edge Hardware Platforms]]
- [[mocs/mlops-and-devops-for-edge|MLOps and DevOps for Edge]]
- [[mocs/competitive-landscape-and-ecosystem-dynamics|Competitive Landscape and Ecosystem Dynamics]]
- [[mocs/googles-edge-ai-stack|Google's Edge AI Stack]]

## Synthesis

On-device LLM inference today is a co-design problem across four layers: a numerical-precision layer (quantization), a hardware-acceleration layer (NPUs, Apple Silicon, mobile SoCs, edge GPUs), a runtime/engine layer (llama.cpp, MediaPipe/LiteRT, Core ML/MLX, vLLM, Qualcomm AI Stack), and a deployment-strategy layer that ultimately decides quality-vs-latency tradeoffs.

### 1. Quantization formats: GGUF, AWQ, GPTQ, and the research frontier

The practical edge ecosystem has converged on a small set of post-training quantization (PTQ) formats packaged as portable file types:

- **GGUF** is the dominant interchange format for CPU-first and heterogeneous local inference. It is the native format of the llama.cpp engine and is what most consumer-grade local LLM stacks (Ollama, LM Studio, llamafile) load [[sources/yt-P8m5eHAyrFM]]. GGUF bundles weights, tokenizer, and metadata in a single mmap-friendly file and supports a ladder of quantization levels (Q2_K through Q8_0, plus k-quants and i-quants) so the same model can be re-packed for different memory budgets [[sources/yt-P8m5eHAyrFM]], [[sources/yt-oaV_8ZSFblg]].
- **AWQ (Activation-aware Weight Quantization)** and **GPTQ** are weight-only PTQ schemes more common in GPU-served stacks (e.g., vLLM, TensorRT-LLM). They preserve a small number of salient channels at higher precision based on activation statistics, which generally beats naive round-to-nearest at 4-bit. The candidate corpus references vLLM as a local inference engine alongside llama.cpp [[sources/yt-pwP1YcHtF8s]] but does not contain a dedicated source page extracting AWQ vs GPTQ claims — this is a gap to fill on next ingest.
- **Sub-4-bit and ternary research.** The frontier is pushing well below 4-bit. PTQTP performs post-training quantization to trit-planes (effectively ternary with a sub-2-bit footprint) and can quantize a model in roughly an hour while rivaling 1.58-bit accuracy [[sources/arxiv-2508.07329]]. Hessian-Aware Quantization (HAQ) uses second-order curvature information to smooth weight matrices, which is necessary because activation outliers (especially in MoE and multimodal models) crater naive low-bit PTQ accuracy [[sources/arxiv-2508.07329]], [[sources/arxiv-2502.00425]].
- **Multimodal-specific quantization.** Standard PTQ degrades multimodal LLMs because text and vision activations have very different distributions. MQuant introduces Modality-Specific Static Quantization (MSQ) plus rotation-based outlier handling so the entire MLLM (vision encoder + LLM) can be served fully statically quantized rather than falling back to dynamic quantization on the hot path [[sources/arxiv-2502.00425]].
- **Joint quantization + low-rank compression.** UniQL unifies quantization with low-rank weight compression so that the same checkpoint can be re-targeted to different edge memory budgets without retraining a separate model per device class [[sources/arxiv-2512.03383]].
- **KV-cache quantization is the next bottleneck.** Once weights are at 4 bits, the KV cache becomes the dominant memory cost for long-context auto-regressive generation. WKVQuant jointly quantizes weights and the KV cache in a 2D scheme and is treated by the corpus as the canonical answer to this bottleneck [[mocs/on-device-inference-foundations]].

### 2. NPU and Apple Silicon acceleration

The acceleration layer is fragmented along vendor lines, and the quantization format you pick is largely a function of which accelerator you target:

- **Apple Silicon (A-series / M-series).** Apple's bet is unified memory plus neural accelerators integrated into the GPU cores, so weights, activations, and KV cache live in a single pool addressable by CPU, GPU, and Neural Engine — eliminating the host↔device copies that dominate latency on PCIe-attached accelerators [[sources/yt-FviaHPrFhTg]], [[sources/yt-wgJX1HndGl0]]. The M5 generation explicitly adds neural accelerators inside the GPU rather than only in the ANE, which matters for LLM workloads because the GPU path is what MLX and Core ML actually dispatch to for transformer matmuls [[sources/yt-wgJX1HndGl0]]. Apple's deployment story (Core ML compilation + on-device fine-tuning hooks) is consolidated in the WWDC24 Core ML guidance [[sources/yt-aawk4l9W9YU]].
- **Mobile NPUs (Qualcomm Hexagon, Apple Neural Engine, etc.).** NPUs win on tokens-per-watt but constrain quantization choice: the Hexagon NPU is fundamentally an integer DSP, so practical deployment requires INT4/INT8 weights and INT8/INT16 activations rather than the FP16/BF16 paths that run cleanly on GPUs [[sources/yt-Sc3zyAzSRP0]]. The Qualcomm AI Stack abstracts this by routing ops to the most efficient backend (CPU, Adreno GPU, or Hexagon NPU) per kernel, so the same model can run with different precision on different blocks [[sources/yt-Sc3zyAzSRP0]].
- **AI PCs and discrete NPUs.** The "Copilot+" / AI mini-PC class (Intel/AMD/Qualcomm laptops with 40+ TOPS NPUs) is the consumer x86 analog of mobile NPUs — same INT-first constraint, same need for vendor-specific runtime [[sources/yt-ZNPkUoPBU84]].
- **Browser as the cross-vendor escape hatch.** Where native NPU access is gated by OS vendors, WebGPU + WebAssembly (MediaPipe LLM Inference API) becomes a portable acceleration layer that hits the GPU directly across Windows, macOS, iOS, and Android — at the cost of giving up NPU access [[sources/yt-G8vzGedNnro]], [[sources/yt-hQQ8KuhXcwU]].

### 3. Runtime engines

The runtime is what actually decides whether a given quantization format can use a given accelerator. The corpus covers four practical families:

- **llama.cpp + GGUF.** A C/C++ engine with hand-written kernels per backend (AVX/AVX-512, Metal, CUDA, ROCm, Vulkan, SYCL). It is the lingua franca of local inference because it runs the same GGUF file on a Raspberry Pi, an M-series Mac, and a 4090, with mmap-based weight loading that lets quantized models exceed RAM [[sources/yt-P8m5eHAyrFM]]. WasmEdge / Second State extend this to a portable WASM-hosted variant for edge-cloud deployment [[sources/yt-pwP1YcHtF8s]].
- **MediaPipe LLM Inference API / LiteRT.** Google's portable runtime targeting WebGPU and Android, demonstrated running 27B-parameter models in-browser at hundreds of prefill tokens/sec via streaming weight loading and mixed-precision transitions [[sources/yt-G8vzGedNnro]], [[sources/yt-hQQ8KuhXcwU]].
- **Core ML / MLX.** Apple's two-tier story: Core ML for compiled, ANE-aware deployment with quantized weights [[sources/yt-aawk4l9W9YU]]; MLX for a NumPy/PyTorch-feeling Python API that targets the GPU via Metal and exploits unified memory for KV-cache-heavy LLM workloads [[sources/yt-wgJX1HndGl0]].
- **Qualcomm AI Stack.** A heterogeneous-execution runtime that accepts ONNX/PyTorch and dispatches per-op across CPU, GPU, and Hexagon NPU [[sources/yt-Sc3zyAzSRP0]].
- **Server-grade engines on the edge cloud.** vLLM (paged-attention, continuous batching) is referenced as the high-throughput counterpart to llama.cpp when the "edge" is actually a colocated edge box rather than a phone [[mocs/mlops-and-devops-for-edge]].

### 4. Quality vs latency tradeoffs

The corpus is consistent on the shape of the tradeoff curve, even where individual numbers vary:

- **4-bit weight-only is the current sweet spot.** Q4_K_M-class GGUF quantization and AWQ-int4 lose roughly perplexity-equivalent quality compared to FP16 on text tasks while cutting weight memory by ~4× and decoding-stage latency by a similar factor — which is why 4-bit is the default level shipped by Ollama/LM Studio/llamafile [[sources/yt-P8m5eHAyrFM]], [[sources/yt-oaV_8ZSFblg]].
- **Below 4 bits, the tradeoff becomes regime-dependent.** Naive 2–3-bit PTQ degrades sharply, but outlier-aware methods (HAQ, PTQTP, MQuant) recover most of the quality at the cost of more compute at quantization time and tighter coupling to a calibration distribution [[sources/arxiv-2508.07329]], [[sources/arxiv-2502.00425]].
- **KV-cache quantization moves the Pareto frontier for long-context.** Once you push to 8k–128k context, the latency story is dominated by KV-cache memory bandwidth, not weight reads — so KV-cache quantization (e.g., WKVQuant, FP8/INT8 KV) often buys more wall-clock latency than another bit off the weights [[mocs/on-device-inference-foundations]].
- **Hardware path matters as much as bit-width.** On Apple Silicon, going through MLX/Metal with FP16 weights and unified memory can beat a 4-bit GGUF that bounces through CPU, because the data-movement savings dominate [[sources/yt-wgJX1HndGl0]], [[sources/yt-FviaHPrFhTg]]. On a Hexagon NPU the opposite is true: anything that isn't INT-quantized falls off the NPU and onto the GPU/CPU, paying a much larger latency penalty [[sources/yt-Sc3zyAzSRP0]].
- **Deployment strategy is a hidden axis.** Empirical work on black-box edge deployment (containerized vs. native vs. edge-runtime) shows that the deployment wrapper itself can dominate latency and even shift accuracy due to op fallbacks, independent of the quantization choice [[sources/arxiv-2403.17154]].
- **Throughput milestones.** The corpus' high-water mark for fully open-source on-device decoding is ~600 tok/s, achieved by combining int4 weights, KV-cache optimizations, and a tight runtime [[sources/yt-hQQ8KuhXcwU]] — useful as a sanity ceiling when evaluating new quantization/runtime combinations.

### 5. Gaps in the current corpus

The candidate source pages above are legacy migrations whose key-claims sections have not yet been extracted (`_(claims not yet extracted from legacy)_`). Quantitative numbers in this synthesis that are not directly footnoted to an arXiv paper or a content-bearing MOC should be re-grounded once those source pages are filled in. Specific gaps:

- No dedicated source page yet extracts **AWQ** or **GPTQ** algorithmic detail — the corpus references them only via the vLLM/llama.cpp ecosystem mentions. A targeted ingest of the AWQ (Lin et al., 2023) and GPTQ (Frantar et al., 2022) papers would close this.
- No source page yet covers **MLX** internals or **Core ML int4 palletization** in claim-extracted form; Apple coverage is currently only via WWDC and the M5/A19 talk [[sources/yt-aawk4l9W9YU]], [[sources/yt-wgJX1HndGl0]], [[sources/yt-FviaHPrFhTg]].
- KV-cache quantization is referenced via the on-device-inference-foundations MOC but not by a dedicated WKVQuant source page.

## Sources cited

- [[sources/yt-P8m5eHAyrFM]] — llama.cpp / GGUF as the local-inference lingua franca
- [[sources/yt-pwP1YcHtF8s]] — Portable LLM inference on the edge cloud (WasmEdge / Second State, vLLM context)
- [[sources/yt-hQQ8KuhXcwU]] — 600 tok/s open-source on-device decoding
- [[sources/yt-G8vzGedNnro]] — MediaPipe LLM Inference API on WebGPU
- [[sources/yt-aawk4l9W9YU]] — WWDC24 Core ML on-device deployment
- [[sources/yt-wgJX1HndGl0]] — M5 / A19 GPUs with neural accelerators
- [[sources/yt-FviaHPrFhTg]] — Apple iPhone chips and on-device AI (unified memory)
- [[sources/yt-Sc3zyAzSRP0]] — Qualcomm AI Stack and Hexagon NPU heterogeneous dispatch
- [[sources/yt-ZNPkUoPBU84]] — AI mini-PCs / consumer NPUs
- [[sources/yt-oaV_8ZSFblg]] — Local LLM hardware/system requirements
- [[sources/arxiv-2508.07329]] — Hessian-Aware Quantization for edge LLMs with CPU-GPU collaboration
- [[sources/arxiv-2502.00425]] — MQuant: full static quantization for multimodal LLMs (MSQ, outlier handling)
- [[sources/arxiv-2512.03383]] — UniQL: unified quantization + low-rank compression for adaptive edge LLMs
- [[sources/arxiv-2403.17154]] — Black-box deployment strategies for edge AI: latency and accuracy impact
