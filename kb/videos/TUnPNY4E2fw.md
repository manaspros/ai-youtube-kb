# Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `TUnPNY4E2fw` · [watch](https://youtu.be/TUnPNY4E2fw) · **date:** 2026-06-18 · **length:** 15:50 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Max Ryabinin · **orgs:** Together AI, Microsoft, Hugging Face, Unsloth
- **topics:** training-finetuning-rl, infra-cost-scaling · **tags:** long-context, context-parallelism, deepspeed-ulysses, activation-checkpointing, cpu-offload, sequence-tiling, upipe, fsdp, flash-attention, memory-optimization, training-infrastructure

> Together AI's Max Ryabinin walks through stacking memory optimizations (Ulysses context parallelism, checkpointing, CPU offload, tiling, and the UPipe head-chunking method) to train with multi-million-token context.

## Summary
Max Ryabinin of Together AI presents a research project on training long-context transformers, aiming for a 5M-token sequence length. He says long context matters for agents and for video models that must track many frames over time. The core problem he names is that attention compute grows quadratically with sequence length and activation memory grows linearly. He walks through a memory ladder on an 8-GPU H100 node: parameters alone do not fit, FSDP fixes parameter memory but not attention activations, and Ulysses-style context parallelism, activation checkpointing, CPU offload of block inputs, and sequence tiling each add a step. His main contribution, which he calls UPipe (the transcript garbles it as "untitled Ulysses"), processes groups of attention heads in chunks and reuses one smaller buffer across chunks. He reports that this matches the most memory-optimized transformer training implementations at 8B and 32B scale while reaching 5M tokens, with chunk size trading memory for throughput. He closes by saying bottlenecks show up where you least expect them, so profile with the PyTorch profiler first.

## Key ideas
- **Long-context training has two walls: attention compute grows quadratically with sequence length, and activation memory grows linearly.** — Speaker frames the problem as pairwise attention cost plus linearly growing memory, and says even modest context extensions make memory accounting worth doing. ([3:24](https://youtu.be/TUnPNY4E2fw?t=204))
- **Work through a memory ladder, one fix at a time, instead of guessing.** — On an 8-GPU H100 node with a Llama-3-style 8B-class model (transcript says 'LAMO3B') aimed at 3M tokens, the model does not fit even before activations. FSDP fixes parameter memory but attention activations still overflow. ([4:48](https://youtu.be/TUnPNY4E2fw?t=288))
- **Ulysses-style context parallelism splits attention by heads, not by sequence.** — Each GPU handles a subset of heads but attends over the full sequence, which lets standard fused attention kernels be used. Speaker says utilization drops by roughly 8x with this approach. ([6:08](https://youtu.be/TUnPNY4E2fw?t=368))
- **Activation checkpointing and CPU offload cut the activation footprint further.** — Checkpointing trades recompute for memory and gives about a further 8x drop in activation usage, per the speaker. Block inputs go to CPU and are prefetched during backward. Element-wise ops like loss and MLP can be tiled along the sequence to avoid huge buffers. ([7:36](https://youtu.be/TUnPNY4E2fw?t=456))
- **Tiling and CPU offload together make 3M tokens feasible, but not 5M.** — Offloading roughly 37 GB of activations to CPU and tiling element-wise computations gets the run to 3M. Going further needs the main contribution. ([9:01](https://youtu.be/TUnPNY4E2fw?t=541))
- **UPipe: one head group saturates the GPU, so process head groups in chunks and reuse one buffer.** — Computing attention for a single group of heads already fills the GPU, so heads are split into chunks processed in sequence. Each stage writes its partial result and the next stage reuses the same allocated buffers, which is smaller than the one-shot buffer. ([10:13](https://youtu.be/TUnPNY4E2fw?t=613))
- **Chunk size is a memory-throughput dial, and the method holds up at 8B and 32B scale.** — Larger chunks use more memory but run faster. Speaker says results match the most memory-optimized transformer training implementations at 8B and 32B while scaling to about 5M tokens, and sometimes run faster at shorter lengths. ([11:34](https://youtu.be/TUnPNY4E2fw?t=694))
- **Profile before optimizing; the bottleneck is often somewhere unexpected.** — Speaker's takeaway is that large-context training bottlenecks surprise people, and tools like the PyTorch profiler help locate them. Full results are in the paper, which he says is public. ([12:57](https://youtu.be/TUnPNY4E2fw?t=777))

## Techniques
- **Staged memory accounting** — Measure peak memory after each change in a fixed order (parameters, then FSDP, then attention activations, then checkpointing, offload, and tiling) so each optimization's effect is visible. *When:* Before scaling any training run to a context length that does not fit on the current hardware.
- **Head-based context parallelism (DeepSpeed Ulysses)** — Shard attention heads across GPUs while each GPU still attends over the full sequence, communicating activations as needed. This keeps a standard fused attention kernel usable. *When:* When sequence length, not parameter count, is what exhausts GPU memory during training.
- **Activation checkpointing plus CPU offload of block inputs** — Recompute activations in the backward pass instead of storing them, and move per-block inputs to CPU, prefetching them back when the backward pass reaches each layer. *When:* When activation memory is the limit and the extra recompute and transfer cost is acceptable.
- **Sequence tiling of element-wise ops** — Split loss computation and MLP layers into chunks along the sequence dimension so no full-length intermediate buffer is created. *When:* When full-length intermediate tensors in loss or MLP layers dominate peak memory.
- **UPipe head chunking with buffer reuse** — Split a GPU's attention heads into chunks, process them in order, store each partial result, and reuse the same buffers across chunks. Tune chunk size to trade memory for throughput. *When:* When you need the last large memory savings in attention while keeping throughput close to the best implementations.
- **Profile with PyTorch profiler first** — Run the profiler on the training step to find where time and memory go, rather than assuming the bottleneck. *When:* Whenever a long-context training run is slower or larger than expected.

## Numbers
- Target run: a standard Llama-3-style 8B-class model (transcript says 'LAMO3B') at 3M-token sequence length on one 8x H100 node; parameters alone do not fit before sharding. ([4:48](https://youtu.be/TUnPNY4E2fw?t=288))
- Ulysses context parallelism reduces utilization by about 8x, per speaker. ([6:08](https://youtu.be/TUnPNY4E2fw?t=368))
- Activation checkpointing gives about a further 8x drop in activation usage, per speaker. ([7:36](https://youtu.be/TUnPNY4E2fw?t=456))
- About 37 GB of activations offloaded to CPU as part of reaching 3M tokens. ([9:01](https://youtu.be/TUnPNY4E2fw?t=541))
- UPipe results match the most memory-optimized transformer training implementations at 8B and 32B scale while scaling to about 5M tokens. ([11:34](https://youtu.be/TUnPNY4E2fw?t=694))

## Hot takes
- Activation memory, not parameter count, is the real wall for multi-million-token training.
- Head-chunked attention with reused buffers can be as memory-efficient as the best existing implementations while scaling further.

## Tools mentioned
PyTorch profiler, FSDP, DeepSpeed Ulysses, FlashAttention

## Relevance to our work
- **agentos** (1/3): InferCraft (L2B) is serving-side, and this talk covers training memory. The step-by-step memory accounting method is reusable if AgentOS benchmarks long-context behavior. → *When benchmarking long-context behaviour for InferCraft, use the same staged memory accounting (measure peak after each change, in a fixed order) and read the paper for the chunked-attention method.*
