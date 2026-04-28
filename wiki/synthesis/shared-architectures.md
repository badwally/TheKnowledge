---
type: synthesis
slug: shared-architectures
title: Shared Architectures
domains:
- ai-temporal-video
question: '(legacy synthesis: shared-architectures)'
draft: true
draft_started_at: '2026-04-28T15:21:51Z'
legacy_provenance:
  imported_at: '2026-04-28T15:21:51Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian/synthesis/shared-architectures.md
  legacy_slug: shared-architectures
---

# Shared Architectures

*Cross-cutting analysis across all research branches.*

## Related Branches

- [[mocs/action-recognition-classification|Action Recognition & Classification]]
- [[mocs/temporal-action-detection-localization|Temporal Action Detection & Localization]]
- [[mocs/video-object-tracking-trajectory-prediction|Video Object Tracking & Trajectory Prediction]]
- [[mocs/video-language-understanding-grounding|Video-Language Understanding & Grounding]]
- [[mocs/biologically-inspired-advanced-spatio-temporal-computing|Biologically Inspired & Advanced Spatio-Temporal Computing]]

## Analysis

Several foundational architectures transcend individual research areas in video analysis, being creatively adapted to handle the unique spatial and temporal demands of different sub-fields. Here are the major cross-cutting architectures and how they are adapted for various tasks:

**1. Graph Neural Networks (GNNs) and Graph Convolutions**
Graphs are used across multiple domains to explicitly model relationships, but the definition of the "nodes" and "edges" completely changes based on the task:
*   **Action Recognition (Modeling Anatomy):** In ST-GCN (Spatial Temporal Graph Convolutional Networks), the graph represents physical human topology. The **nodes are human joints** (e.g., elbows, wrists) and the **edges are the bones** connecting them. The GNN passes spatial information between adjacent physical joints to recognize actions [1, 2].
*   **Trajectory Prediction & Tracking (Modeling Social Interaction):** In GraphTCN and TransMOT, the graph models the social or physical environment. The **nodes represent individual pedestrians or tracking candidates**, and the **edges represent relative spatial distances and human-human interactions**. This allows the network to predict collision-free pathways and maintain identities in crowded scenes [3-5].
*   **Temporal Action Detection (Modeling Video Context):** In G-TAD (Sub-Graph Localization), the video itself is the graph. The **nodes are individual video snippets**, and the **edges are the temporal and semantic correlations** between those snippets, helping to localize actions in long, untrimmed videos [6]. In METAL, GCNs are similarly used to output multi-scale similarity scores for video segments [7].

**2. Transformers and Attention Mechanisms**
Transformers, originally built for natural language, are utilized across almost all video tasks to capture long-range dependencies, though their implementations are heavily modified:
*   **Video-Language Understanding & Grounding:** Transformers serve as multi-modal bridges. In TubeDETR, a space-time decoder uses alternating temporal self-attention and cross-attention layers to fuse text queries with video features [8, 9]. Models like TGIF-QA utilize dual attention modules—a spatial attention module to decide *where* in a frame to look, and a temporal attention module to decide *which frame* to look at [10].
*   **Temporal Action Detection:** Standard self-attention struggles here due to "temporal collapse" or "rank loss," where temporal features become too similar to one another [11-13]. To adapt, architectures like Self-Feedback DETR guide self-attention using cross-attention maps [14], while TriDet replaces self-attention entirely with a convolution-based Self-Guided Pooling (SGP) layer to preserve feature discrimination [15].
*   **3D Human Pose Estimation:** Temporal Transformers are used to process sequences of 3D joint positions, capturing the temporal evolution of a person's pose across distant frames [16].

**3. Temporal Convolutional Networks (TCNs) / 1D Convolutions**
TCNs act as a 1D sliding window over time and are frequently used as a faster, more efficient alternative to Recurrent Neural Networks:
*   **Action Recognition:** In ST-GCN, TCNs are layered on top of the graph convolutions. While the GCN handles the spatial layout of the skeleton, the TCN uses a 1D kernel to track the movement of a *single joint* across multiple consecutive frames [17, 18].
*   **Trajectory Prediction:** GraphTCN swaps out LSTMs for modified TCN modules. Because TCNs process local time windows concurrently, they avoid the gradient vanishing problems of RNNs and allow for parallel execution, achieving inference speeds over 5 times faster than peer methods [3, 19].

**4. LSTMs and Recurrent Neural Networks (RNNs)**
LSTMs are classic tools for sequential modeling, but they have been structurally adapted to preserve spatial data or manage complex memory:
*   **Action Recognition:** Standard LSTMs flatten images into 1D vectors, losing spatial structure. **VideoLSTM** adapts the architecture by hardwiring 2D convolutions directly inside the LSTM unit and introducing motion-based attention (via optical flow), allowing it to output 2D spatial attention maps instead of vectorized weights [20-25]. RPAN (Recurrent Pose-Attention Network) similarly feeds human joint attention maps into an LSTM for sequence modeling [26, 27].
*   **Object Tracking:** In RAN (Recurrent Autoregressive Networks), LSTMs are adapted to handle visual occlusions during tracking. The model utilizes the RNN's hidden layer as an "internal memory" but pairs it with an adaptive "external memory" template. If a tracked object is occluded, the network shifts its attention weights away from recent frames and relies on older external memory to predict the trajectory [28, 29].
*   **Video-Language Understanding:** Temporal VM uses a Bidirectional LSTM (Bi-LSTM) to convert fine-grained local clip features into a global semantic representation, looking both forward and backward in time to align video data with a Large Language Model's latent space [30].

**5. 3D Convolutional Neural Networks (3D CNNs)**
3D CNNs expand standard 2D image convolutions by adding a temporal depth dimension, allowing them to extract spatial appearance and temporal dynamics simultaneously:
*   **Action Recognition & Classification:** Models like i3D ResNet utilize 3D spatio-temporal filters. Deep analysis shows they adapt hierarchically: shallow layers act like 1-frame filters to extract static appearance, while deeper layers dynamically enlarge their temporal receptive fields to encode various action speeds [31-35]. ActionFlowNet adapts a 3D ResNet to jointly estimate optical flow and recognize actions directly from raw pixels [36].
*   **Object Tracking:** TubeTK adapts 3D CNNs to directly track multiple objects in one step. Instead of outputting 2D bounding boxes for individual frames, the 3D kernels in its regression head predict comprehensive "bounding tubes" across space and time [37]. Another approach for biological cell tracking uses 3D CNNs to estimate long-term motion maps to prevent identity switches when cells divide or overlap [38].

## Synthesis

_(needs population from legacy import)_

## Sources cited

_(needs population from legacy import)_
