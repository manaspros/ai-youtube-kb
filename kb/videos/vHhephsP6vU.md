# Local AI On Apple Silicon uses 7X Less RAM

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `vHhephsP6vU` · [watch](https://youtu.be/vHhephsP6vU) · **date:** 2026-08-02 · **length:** 6:56 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack
- **topics:** local-ai, inference-serving · **tags:** apple-silicon, metal, mixture-of-experts, ssd-offloading, expert-caching, unified-memory, gemma-4, memory-footprint, swift

> Better Stack walks through Turbo Fieldfare, a Swift/Metal Mac app that runs a 26B Gemma 4 mixture-of-experts model in about 2 GB of RAM by streaming expert weights from SSD on demand.

## Summary
The video presents Turbo Fieldfare, a recently created Mac app written in Swift and Metal that runs Gemma 4 (a 26B-parameter mixture-of-experts model) with about 2.15 GB of resident memory instead of the roughly 14 GB the full model needs. The presenter reports 23.4 tokens/s on an M3 Max. The core idea is that each token activates only 8 of 128 experts per layer, so about 3.9B of the 26B parameters do work per token. The app keeps the always-used weights (attention, router, embeddings, one shared expert, about 1.35 GB) memory-mapped in RAM and leaves the experts (about 12.9 GB) on SSD, pulling them in as the router requests them. On Apple Silicon's unified memory, the CPU can read from SSD straight into a Metal buffer the GPU uses, and the on-disk layout matches the kernel's 4-bit format so no conversion is needed. Each layer caches 16 of its 128 experts with least-frequently-used eviction, which the presenter argues suits skewed routing better than LRU. The design depends on routing being predictable; the video does not show benchmarks beyond the single machine and single run, nor the exact install commands.

## Key ideas
- **A 26B MoE model can run in about 2 GB of RAM because only the always-used weights stay resident while experts stream from SSD.** — Turbo Fieldfare claims ~23 tok/s and a 2.15 GB footprint on an M3 Max, versus ~14 GB for the full Gemma 4 model. The presenter frames the headline as roughly 7x less RAM. ([0:00](https://youtu.be/vHhephsP6vU?t=0))
- **Gemma 4 activates only a small slice of its weights per token.** — Each layer has 128 small experts plus a router that picks the top 8 per token. About 3.9B of 26B parameters do work per token, so roughly 85% of the file is idle at any moment. ([0:54](https://youtu.be/vHhephsP6vU?t=54))
- **Weights are split into a resident pile and a streamed pile at install time.** — Resident: attention, router, embeddings and one shared expert, about 1.35 GB, memory-mapped and always loaded. Streamed: 30 layers x 128 experts at about 3.36 MB each (~12.9 GB), never fully loaded. ([2:08](https://youtu.be/vHhephsP6vU?t=128))
- **Expert prefetching is impossible because the router decides mid-layer, so the CPU stalls on disk about 30 times per token.** — The router's choice depends on attention output for the current token, and it is only known a fraction of a millisecond before the weights are needed. ([3:18](https://youtu.be/vHhephsP6vU?t=198))
- **Apple's unified memory removes the copy hop that would make this slow on a discrete GPU.** — On a PC, weights go SSD to system RAM to PCIe to VRAM. On Apple Silicon the CPU reads from SSD into a Metal buffer that the GPU can also see. ([4:22](https://youtu.be/vHhephsP6vU?t=262))
- **The on-disk format matches the Metal kernel's 4-bit layout, so loading needs no decode step.** — The installer rearranges the data without re-encoding it. Reading the file is effectively loading the weights. ([4:22](https://youtu.be/vHhephsP6vU?t=262))
- **Disk reads overlap with the shared expert's compute, and per-layer expert caches use LFU eviction.** — The shared expert runs for every token, so the GPU works on it while the SSD fetch is in flight. Each layer keeps 16 of 128 experts in memory. LFU suits this because some experts are picked far more often than others. The design depends on routing being predictable. ([5:15](https://youtu.be/vHhephsP6vU?t=315))

## Techniques
- **Resident/streamed weight split for MoE models** — Classify tensors into always-used (attention, router, embeddings, shared expert) and routed experts at install time. Memory-map the always-used set so it stays resident. Leave routed experts on SSD and read each one into memory only when the router selects it. *When:* MoE models where active parameters are a small fraction of total parameters and RAM is the bottleneck. Works best when routing is skewed toward a few popular experts.
- **Zero-copy SSD-to-GPU loading on unified memory** — Read expert bytes straight from SSD into a Metal buffer that the GPU kernel consumes directly, avoiding a separate system-RAM-to-VRAM copy. *When:* Apple Silicon or other unified-memory hardware, where CPU and GPU share physical RAM.
- **Store weights in the kernel's native quantized layout** — Rearrange the 4-bit quantized weights at install time into the exact layout the Metal kernel reads, without re-encoding, so loading is a plain read with no conversion. *When:* Local inference engines that load large quantized weights on every token and need to minimize per-load work.
- **Overlap I/O with always-resident compute** — Start the SSD fetch for routed experts, then run the shared expert, which needs no fetch, on the GPU while the read completes. *When:* Any offloaded design where some compute does not depend on the data being streamed.
- **Per-layer LFU expert cache** — Keep a fixed number of experts per layer in memory (the video uses 16 of 128). On a miss, load from SSD and evict the least frequently used expert, not the least recently used. *When:* When expert or token-to-expert routing is skewed, so usage counts predict reuse better than recency. Measure hit rate on real routing traces to confirm skew.
- **Turbo Fieldfare setup steps shown (no exact commands)** — The video says to clone the GitHub repo and run a series of commands, then download the model, load it, and send a first message. It also says the app can be launched as a Mac app. The exact commands, repo name and model file are not shown on screen or in the transcript; check the repo README. *When:* Trying the app on an Apple Silicon Mac with enough SSD space for the model.

## Numbers
- Full Gemma 4 model is about 14 GB (14.3 GB later); Turbo Fieldfare footprint is 2.15 GB, roughly 6.6x less by arithmetic, which the title rounds to 7x ([0:00 / 0:54](https://youtu.be/vHhephsP6vU?t=0))
- 23 tokens/s on an M3 Max, footprint 2.15 GB ([0:54](https://youtu.be/vHhephsP6vU?t=54))
- Gemma 4: 26B total parameters, about 3.9B active per token, 128 experts per layer, top-8 routing ([0:54](https://youtu.be/vHhephsP6vU?t=54))
- Resident set about 1.35 GB (attention, router, embeddings, one shared expert) ([2:08](https://youtu.be/vHhephsP6vU?t=128))
- Expert pile: 30 layers x 128 experts, about 3.36 MB each, roughly 12.9 GB total, streamed from SSD ([2:08](https://youtu.be/vHhephsP6vU?t=128))
- About 30 SSD fetch stalls per token (one per layer) ([3:18](https://youtu.be/vHhephsP6vU?t=198))
- 16 of 128 experts cached per layer with LFU eviction ([5:15](https://youtu.be/vHhephsP6vU?t=315))

## Hot takes
- The 2.15 GB figure counts resident memory only. Experts are read from SSD on each cache miss, so speed depends on SSD bandwidth and the cache hit rate. The video does not report hit rates or throughput across prompts.
- The benchmark is one run on one machine (M3 Max) with no comparison to llama.cpp or other offload tools. The 23 tok/s figure is a single data point.
- The presenter's own caveat applies: the design is a bet on predictable routing. If routing is near-random, cache misses would dominate, and the video does not test that case.
- The title's '7X less RAM' is a rounded claim (about 6.6x from the stated 14.3 GB to 2.15 GB).

## Tools mentioned
Turbo Fieldfare (Swift/Metal Mac app, repo linked in video description; no version stated), Gemma 4 (26B-parameter mixture-of-experts model), Swift, Metal (Apple GPU API), Apple Silicon (M3 Max used for the benchmark)

## Relevance to our work
- **agentos** (1/3): Expert streaming with a per-layer usage-based cache is a local-inference memory technique in the same space as InferCraft's KV-cache offload, but it targets a single Mac, not the RTX 5090 vLLM stack. → *Read the Turbo Fieldfare repo and compare its LFU expert cache with InferCraft's KV-cache offload strategies; log cache hit rates on real routing traces before proposing any change to InferCraft.*
- **general** (1/3): The LFU-over-LRU argument for skewed access patterns is a reusable cache-design point, not a specific technique for our projects. → *Keep in mind for any cache we add where access is skewed (for example, skill or tool lookups): test LFU against LRU on a recorded access log.*
