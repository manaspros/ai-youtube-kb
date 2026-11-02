# How MiniMax M3 Was Built: Sparse Attention and Native Multimodality — Olive Song

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `htod7Nv1cBc` · [watch](https://youtu.be/htod7Nv1cBc) · **date:** 2026-10-11 · **length:** 15:03 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Olive Song · **orgs:** MiniMax, DeepSeek
- **topics:** models-research, inference-serving, voice-multimodal · **tags:** sparse-attention, GQA, block-level-retrieval, native-multimodal, 1M-context, open-weight, MiniMax-M3, MSA, DSA, 3D-attention, ViT

> MiniMax's Olive Song explains how M3 adapts DeepSeek-style sparse attention to GQA with per-KV-head block selection, and why it was trained on vision and text from step zero.

## Summary
Olive Song from MiniMax presents the open-weight M3 model, which she says combines frontier coding and agentic ability, a 1M-token context window, and native multimodality. The core is MSA (MiniMax Sparse Attention), built by adapting DeepSeek's DSA design to GQA rather than copying it. A lightweight index branch scores attention and picks blocks for the main branch to attend to. Two changes make this work under GQA: each KV head keeps its own selection, and selection moves from token level to block level for better memory access and cheaper top-k. The second half covers multimodal training. She compares three strategies (adding vision after pretraining decay, mixing it in before decay, and training natively from scratch) and reports that native training almost does not hurt text ability at the same token budget. Attention maps are used to argue the modalities fuse more fully in the native setup. The talk ends with ViT design, including 3D attention across video frames capped at four frames. Only high-level design is given: kernels are skipped and no benchmark tables are shown.

## Key ideas
- **Sparse attention must be co-designed with infrastructure, not just borrowed.** — DSA was tuned for MQA with a large head count. Porting it straight to GQA causes algorithmic and memory-access problems, so the team redesigned it under GQA and system constraints. ([4:13](https://youtu.be/htod7Nv1cBc?t=253))
- **Sharing one token selection across all GQA KV heads cancels the diversity GQA is meant to give.** — If every KV head attends to the same selected tokens, the heads add little. Letting each KV head keep its own selection preserves that diversity. ([5:16](https://youtu.be/htod7Nv1cBc?t=316))
- **Token-level top-k is a bottleneck on GPUs.** — Top-k has data dependencies that resist parallel execution, and token-level candidates add merge overhead. Block-level retrieval shrinks the candidate set and improves memory access. ([6:44](https://youtu.be/htod7Nv1cBc?t=404))
- **Adding multimodal data after pretraining decay degrades text ability.** — The model has largely converged by then, so the new data interferes with text learning. Mixing it in before decay is sensitive to data mix and learning rate, and those knobs cannot be tuned freely at pretraining scale. ([9:38](https://youtu.be/htod7Nv1cBc?t=578))
- **Native multimodal training from scratch almost does not hurt text under the same token budget.** — Attention maps from CPT-style models show text tokens barely attending to visual tokens. Native training shows a more integrated map with no clear separation between text and vision tokens. ([10:40](https://youtu.be/htod7Nv1cBc?t=640))
- **3D attention inside the ViT helps video understanding and transfers to some image benchmarks.** — Standard ViT attention is per frame. Attending across frames improves temporal modelling, but the frame count must be capped for system and load-balancing reasons. The team found four frames the best trade-off. ([13:09](https://youtu.be/htod7Nv1cBc?t=789))

## Techniques
- **Index-branch sparse attention** — A lightweight attention branch (4 query heads, 1 key head) is trained with a KL loss to match the main branch's attention scores. It picks the highest-scoring blocks, and the main branch attends only to those keys and values. *When:* Long-context attention (1M tokens) where full attention is too slow in prefill and decode.
- **Per-KV-head selection under GQA** — Do not merge index-branch outputs into one shared token set. Each KV head keeps its own selection, so heads see different tokens. *When:* Adapting a sparse attention design built for MQA to a GQA architecture.
- **Block-level retrieval instead of token-level top-k** — Select contiguous blocks rather than individual tokens, which cuts candidates and merge cost and keeps memory reads contiguous. *When:* GPU kernels where top-k and scattered KV reads are the bottleneck.
- **Native multimodal pretraining from step zero** — Mix vision data into pretraining from the start, rather than adding it as CPT after decay or mixing it in just before decay. *When:* You want strong text ability and vision in one model and can afford full pretraining runs.
- **Attention-map check for modality fusion** — Plot text-to-visual attention maps to see whether text tokens actually attend to visual tokens, which tells you if modalities are integrated or walled off. *When:* Comparing multimodal training recipes, as a diagnostic beyond benchmark scores.
- **3D attention in the ViT with a frame cap** — Let patches attend across frames inside the vision encoder, and limit the frame count (four was the best trade-off) to control cost and load balance. *When:* Video understanding where temporal relations matter and the frame budget is bounded.

## Numbers
- Prefill is about 9x faster and decode about 15x faster than full attention, with a 1M-token context window. ([1:34](https://youtu.be/htod7Nv1cBc?t=94))
- Index branch uses 4 query heads and 1 key head. ([2:59](https://youtu.be/htod7Nv1cBc?t=179))
- Four frames gave the best performance/efficiency trade-off for 3D attention in the ViT. ([13:09](https://youtu.be/htod7Nv1cBc?t=789))

## Hot takes
- A simpler architecture can always lead to better scaling properties (stated core design principle).
- Multimodal added after pretraining is the wrong default; native from-scratch training avoids the text regression.
- Claimed but not shown: M3 can drop in for 90% of current coding work.

## Tools mentioned
MiniMax M3, MSA (MiniMax Sparse Attention), DeepSeek DSA

## Relevance to our work
- **agentos** (1/3): InferCraft runs vLLM with pluggable KV-cache strategies (H2O, CPU offload, LMCache). Block-level sparse attention is a model-side alternative to those, and the talk gives no local-GPU numbers. → *Read the MSA block-selection design as a candidate entry for InferCraft's pluggable KV-cache strategies, and check whether a vLLM-compatible open-weight build exists for the single RTX 5090.*
