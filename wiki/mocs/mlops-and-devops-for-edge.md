---
type: moc
slug: mlops-and-devops-for-edge
domain: edge-ai-agentic
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/mocs/mlops-and-devops-for-edge.md
  legacy_slug: mlops-and-devops-for-edge
---

# MLOps and DevOps for Edge

The operational tooling required to package, deploy, serve, monitor, and scale AI models and autonomous agents across distributed hardware fleets.

## Local Inference Engines

Highly optimized runtime software that loads and executes quantized models on diverse local hardware backends.

**Concept:** [[concepts/local-inference-engines|Local Inference Engines]]

**Methods:**
- [[concepts/llamacpp-using-gguf-format|Llama.cpp (using GGUF format)]]
- [[concepts/vllm|vLLM]]

## Fleet Management and Edge Deployment

Containerization and over-the-air deployment systems that push machine learning updates and dependencies to massive fleets of edge devices securely.

**Concept:** [[concepts/fleet-management-and-edge-deployment|Fleet Management and Edge Deployment]]

**Methods:**
- [[concepts/aws-iot-greengrass|AWS IoT Greengrass]]
- [[concepts/amazon-sagemaker-edge-manager|Amazon SageMaker Edge Manager]]
- [[concepts/chassis-docker-containerization|Chassis/Docker containerization]]

## Dynamic Scheduling and Workload Balancing

Algorithms that optimize hardware utilization by batching requests, migrating KV-caches, and offloading tasks dynamically across edge resources.

**Concept:** [[concepts/dynamic-scheduling-and-workload-balancing|Dynamic Scheduling and Workload Balancing]]

**Methods:**
- [[concepts/halo-batch-query-processing|Halo (Batch Query Processing)]]
- [[concepts/ents-edge-native-task-scheduling|ENTS (Edge-native Task Scheduling)]]
- [[concepts/comdml-workload-balancing|ComDML (Workload Balancing)]]

## Open Problems

**Technical Gaps Limiting Edge+Agentic Deployment Today**

*   **Continuous Monitoring Under Extreme Power Budgets:** While pushing models to edge devices is becoming easier, continuously monitoring those models in the field for concept drift and data drift remains a massive unsolved problem. On battery-powered tinyML or edge devices, the power budget often prohibits continuously sending telemetry or inference logs back to the cloud, making it incredibly difficult to know when a deployed model has degraded due to changing real-world conditions [1-3].
*   **The Containerization Redundancy Penalty:** To solve "dependency hell" (matching specific versions of PyTorch, NumPy, etc., to specific edge chips), platforms like Chassis.ml package models into immutable Docker containers [4-6]. However, running multiple isolated model containers on a single-board computer incurs a massive resource penalty due to redundant framework dependencies loaded into memory for each container [7, 8].
*   **Kubernetes is not "Edge-Native":** While Kubernetes is the cloud standard for orchestration, it neglects the unique features of edge computing, primarily ensuring resource provision while ignoring the latency, throughput, data locality, and fragile networking constraints of edge-native applications [9]. 
*   **Workflow-Blind LLM Execution:** Existing serving engines focus on optimizing individual LLM calls. However, agentic workflows feature massive redundancy from overlapping contexts and parallel exploration. Without system-level performance planning, this results in fragmented CPU-GPU execution and poor hardware utilization, creating a severe bottleneck for edge agents [10].

**Standardization Needs**

*   **"TinyML-as-a-Service" Abstractions:** There is a critical need to decouple edge hardware specifics (compilers, ISAs, memory constraints) from the cloud build environment. The industry requires standardized "Machine Learning as a Service" deployment layers that handle the messy backend compilation for highly fragmented device architectures, allowing data scientists to remain hardware-agnostic [11, 12].
*   **Standardized Device Farms for CI/CD:** Because edge hardware is so fragmented, continuous integration and delivery (CI/CD) pipelines break down. The ecosystem needs standardized, cloud-accessible device farms or advanced functional simulators (like Renode) so developers can rigorously test models across hundreds of physical edge profiles before deployment [13-16].
*   **Standardized Benchmarking:** Tools and metrics (like those pursued by MLPerf) need to be standardized across the industry to accurately evaluate and compare how models serve predictions under different scenarios (streaming, batch, online) across wildly different edge endpoints [1, 17].

**Market Opportunities for Platform Plays and Ecosystem Consolidation**

*   **Adaptive Data Flywheels (MAPE Control Loops):** A major opportunity lies in building closed-loop systems that automatically fix AI agent failures. For instance, NVIDIA's NVInfo AI system uses a MAPE (Monitor, Analyze, Plan, Execute) loop to capture human-in-the-loop feedback on routing and rephrasal errors. It then automatically funnels those negative samples into fine-tuning pipelines, enabling enterprise agents to act as self-improving systems that shrink in size while growing in accuracy over time [18].
*   **Workflow-Aware Batch Processing Systems:** Platforms that treat multi-agent workloads as structured Directed Acyclic Graphs (DAGs) represent a massive market opportunity. Emerging systems like **Halo** perform plan-level optimization—adaptively batching queries and sharing KV-caches across the entire workflow—which can achieve up to a 3.6x speedup for batch inference without compromising quality [10].
*   **Edge-Native Task Schedulers:** Startups and platforms that can extend or replace Kubernetes specifically for Collaborative Edge Computing (CEC). Systems like **ENTS (Edge-native Task Scheduling)** that jointly schedule computation and network flow routing across geo-distributed nodes can increase job throughput by up to 220% [9].
*   **Purpose-Built Edge MLOps:** Existing big-ML platforms (like SageMaker, TFX, Michelangelo) do not naturally translate to tinyML constraints [19-21]. There is a large gap for specialized MLOps platforms that natively merge embedded systems engineering with machine learning operations [21, 22].

**Strategic Positioning: Google vs. Competitors**

*   **Google (The Ubiquitous Cross-Platform Player):** Google's primary advantage in edge deployment is bypassing native OS monopolies altogether. With the **MediaPipe Web** and **LLM Inference API**, Google allows developers to deploy high-performance, WebGPU-accelerated models natively inside the browser across iOS, Android, Mac, and Windows [23-25]. For enterprise MLOps, Google leverages **Anthos** (Google Distributed Cloud) to seamlessly orchestrate containerized edge workloads using familiar cloud-native Kubernetes tooling [26-28]. However, adapting cloud-native Kubernetes directly to resource-constrained edge hardware remains a technical friction point [9, 21].
*   **AWS (The Industrial Fleet Manager):** Amazon currently dominates the MLOps pipeline for massive, disconnected industrial fleets. **AWS IoT Greengrass** paired with **SageMaker Edge Manager** provides an end-to-end, highly mature ecosystem for cryptographically signing models, pushing them Over-The-Air (OTA) to millions of devices, and running local agents that sample data for cloud retraining [29-32]. 
*   **NVIDIA (The Physical Edge Moat):** NVIDIA holds a massive moat in high-performance physical edge deployment (robotics, smart cities) by coupling their Jetson hardware with the **DeepStream SDK** and **TensorRT**. They lock developers into their ecosystem by providing unmatched, out-of-the-box optimization (like zero-memory-copy pipelines and hardware acceleration) that requires CUDA to function [33, 34]. 
*   **Qualcomm & Microsoft (The Open Deployers):** Qualcomm and Microsoft are aggressively partnering to commoditize the deployment layer. Qualcomm provides the **AI Hub** (allowing developers to remotely test models on physical Snapdragon devices) [35], while integrating deeply with Microsoft's **ONNX Runtime**. This guarantees that developers can build hardware-agnostic models that deploy seamlessly across Windows Copilot+ PCs and Android mobile devices without being locked into Apple or NVIDIA's walled gardens [36, 37].

## Overview

_(needs population from legacy import)_

## Key entities

_(needs population from legacy import)_

## Key concepts

_(needs population from legacy import)_

## Synthesis pages

_(needs population from legacy import)_
