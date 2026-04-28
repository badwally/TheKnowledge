---
type: moc
slug: on-device-inference-foundations
domain: edge-ai-agentic
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/mocs/on-device-inference-foundations.md
  legacy_slug: on-device-inference-foundations
---

# On-Device Inference Foundations

This branch focuses on techniques to shrink large AI models so they fit within the memory, compute, and power constraints of edge devices without losing reasoning capabilities. It heavily emphasizes numerical precision reduction and structural efficiency.

## Quantization and Low-Bit Precision

Methods to convert floating-point parameters and activations into lower-bit integer or ternary representations to drastically cut memory usage and boost inference speed.

**Concept:** [[concepts/quantization-and-low-bit-precision|Quantization and Low-Bit Precision]]

**Methods:**
- [[concepts/hessian-aware-quantization-haq|Hessian-Aware Quantization (HAQ)]]
- [[concepts/wkvquant-weight-and-key-value-cache-quantization|WKVQuant (Weight and Key/Value cache quantization)]]
- [[concepts/ptqtp-post-training-quantization-to-trit-planes|PTQTP (Post-Training Quantization to Trit-Planes)]]
- [[concepts/amed-automatic-mixed-precision-quantization|AMED (Automatic Mixed-Precision Quantization)]]

## Model Compression and Distillation

Approaches that structurally reduce model size or transfer knowledge from large teacher models to compact student models tailored for edge deployment.

**Concept:** [[concepts/model-compression-and-distillation|Model Compression and Distillation]]

**Methods:**
- [[concepts/knowledge-grafting|Knowledge Grafting]]
- [[concepts/collaborative-compression-for-mixture-of-experts-moe|Collaborative Compression for Mixture of Experts (MoE)]]
- [[concepts/data-centric-compression|Data-Centric Compression]]

## Open Problems

**Technical Gaps Limiting Edge+Agentic Deployment Today**
While running Large Language Models (LLMs) locally has become feasible, several technical hurdles prevent widespread deployment of complex, autonomous agentic workflows on the edge:
*   **The KV Cache Memory Bottleneck:** LLM inference is highly memory-bound. While shrinking model weights via quantization is common, the Key/Value (KV) cache required for long-context auto-regressive generation consumes massive memory. Techniques like *WKVQuant* are emerging to jointly quantize both weights and the KV cache using two-dimensional strategies, but this remains a critical bottleneck for agents that require extensive context history [1].
*   **Quantization Degradation in MLLMs and MoE:** As models scale using Mixture of Experts (MoE) or incorporate vision (Multimodal LLMs), they exhibit extreme activation outliers. Standard quantization causes severe accuracy drops. Emerging solutions require complex methods like Hessian-Aware Quantization (HAQ) to smooth matrices, or Modality-Specific Static Quantization (MSQ) to handle the differing distributions of visual versus textual tokens [2, 3]. 
*   **Lack of Workflow-Level Optimization:** Current inference engines (like vLLM or Llama.cpp) optimize individual LLM calls in isolation. However, agentic workflows generate massive redundancy through repeated prompts, overlapping contexts, and parallel exploration across multiple agents [4, 5]. There is a gap in systems capable of "workflow-aware" serving—such as caching contexts across an entire Directed Acyclic Graph (DAG) of agents to maximize CPU-GPU pipelining and hardware utilization [4, 5].
*   **Hardware Fragmentation:** The edge consists of wildly heterogeneous hardware (MCUs, NPUs, DSPs, and varied GPUs) with distinct instruction set architectures (ISAs) and memory constraints. Compiling, tuning, and reliably executing models across this fragmented landscape remains a massive DevOps challenge [6-9].

**Standardization Needs**
To move beyond fragmented, custom-built solutions, the industry is coalescing around several standardization efforts:
*   **Inter-Agent Communication (A2A):** As multi-agent systems grow, agents built on different frameworks (e.g., LangChain, CrewAI) need a standard way to discover each other, negotiate, and delegate tasks. Google's open-source Agent-to-Agent (A2A) protocol addresses this by using standardized "agent cards" (JSON-RPC documents) published at well-known paths, allowing agents to advertise their capabilities and interact over HTTP [10-14].
*   **Context and Tool Integration (MCP):** Anthropic’s Model Context Protocol (MCP) is rapidly becoming the "USB-C for AI," standardizing how AI models connect to external tools (APIs, web searches) and resources (databases, local files) [15-18]. This replaces bespoke REST API glue-code with a uniform interface [19].
*   **Model Formats and Runtimes:** The open-source community relies heavily on the GGUF format (used by Llama.cpp) to package weights, metadata, and quantization structures into a single file for local CPU/GPU execution [20, 21]. Concurrently, enterprise frameworks like Microsoft’s ONNX Runtime and Meta’s ExecuTorch aim to provide standardized runtimes that can automatically delegate operations to the best available local hardware (e.g., an NPU vs. a GPU) [22-24].

**Market Opportunities for Platform Plays & Ecosystem Consolidation**
*   **Edge MLOps and Fleet Management:** Deploying a model is only the first step; models in the real world suffer from data drift as user behaviors change [25, 26]. There is a massive market opportunity for platforms that manage the lifecycle of edge AI—facilitating Over-The-Air (OTA) containerized updates, monitoring hardware telemetry, and automating the retraining pipeline across distributed fleets of thousands of edge devices [27-29].
*   **Data-Centric Compression:** A strategic shift is occurring from model-centric compression to data-centric compression. Because the primary computational bottleneck for modern LLMs is the quadratic cost of self-attention over ultra-long contexts, future platforms will focus on compressing the input data itself (text, high-res images, video) before or during inference to improve efficiency [30].
*   **Federated Agentic Coalitions:** There is a burgeoning opportunity for "Internet of Agentic AI" platforms. These frameworks allow decentralized edge devices to securely collaborate, train, and execute workflows without centralizing private data. Using Confidential Computing (Secure Enclaves/TEEs) and Federated Learning, these platforms can create secure, auditable, and economically viable multi-agent systems across untrusted environments [31-34].

**Strategic Positioning: Google vs. Competitors**
*   **Google (The Ubiquitous Cross-Platform Play):** Google is exceptionally well-positioned to democratize edge AI across the web and mobile ecosystem. Through the MediaPipe LLM Inference API and WebGPU, Google enables developers to run models like Gemma directly inside browsers and across iOS/Android without backend server costs [35-37]. Additionally, by embedding AICore into Android, Google makes on-device AI a system-level service, reducing app bloat [38]. However, their reliance on heterogeneous hardware makes achieving peak performance across all devices challenging.
*   **Apple (The Vertical Integration Advantage):** Apple holds a distinct hardware advantage due to its Unified Memory Architecture, where the CPU, GPU, and Neural Engine share the same pool of high-speed RAM [39, 40]. This inherently solves the memory bottlenecks that plague LLM inference, allowing Macs and iPhones to run massive models incredibly efficiently [41]. Through Core ML and the MLX framework, Apple offers unmatched out-of-the-box optimization, but firmly locks developers into its proprietary ecosystem [42, 43].
*   **NVIDIA (The High-Performance Industrial Moat):** NVIDIA dominates the physical and industrial edge (robotics, smart cities, autonomous vehicles) with its Jetson Orin/Thor platforms and DGX Spark [44, 45]. They secure their dominance through the CUDA software ecosystem and TensorRT, which offers staggering inference speedups (via kernel fusion and dynamic tensor memory) but strictly binds developers to NVIDIA silicon [46-48].
*   **Qualcomm, Meta, and Microsoft (The Open Alliance):** To combat Apple and NVIDIA's hardware lock-in, these companies are consolidating an open software/hardware stack. Qualcomm’s AI Stack pairs with Microsoft’s ONNX Runtime and Meta’s ExecuTorch to ensure open-source models (like Llama) can run optimally on any hardware, specifically targeting Snapdragon NPUs for extreme power efficiency [22-24, 49]. This alliance aims to commoditize the software layer and standardize edge deployments across Windows and Android.

## Overview

_(needs population from legacy import)_

## Key entities

_(needs population from legacy import)_

## Key concepts

_(needs population from legacy import)_

## Synthesis pages

_(needs population from legacy import)_
