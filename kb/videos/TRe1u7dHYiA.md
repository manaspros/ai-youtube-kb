# What Makes Open Models Fast in Production — Sujee Maniyam, Nebius

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `TRe1u7dHYiA` · [watch](https://youtu.be/TRe1u7dHYiA) · **date:** 2026-10-04 · **length:** 20:32 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Dylan (product marketing, Nebius Token Factory), Sujee Maniyam (developer advocate, Nebius) · **orgs:** Nebius, NVIDIA, Artificial Analysis, Microsoft, Meta
- **topics:** inference-serving, infra-cost-scaling · **tags:** open-models, managed-inference, speculative-decoding, kv-cache, cache-aware-routing, prefill-decode-disaggregation, quantization, vendor-pitch

> Nebius Token Factory explains the serving optimizations behind fast open-model inference: cache-aware routing, speculative decoding, KV-cache offload, and prefill/decode separation. It is mostly a product pitch with few measured results.

## Summary
Two Nebius speakers pitch Token Factory, a managed inference service for open-weight LLMs that runs on Nebius-owned bare-metal GPUs. The first half is positioning: they argue open models are close to proprietary ones, that managed inference sits between closed APIs and self-hosting, and that the platform also covers data logs, post-training and deployment. The technical second half, given by Sujee Maniyam, lists serving optimizations the platform applies automatically: per-model engine selection, cache-aware request routing, speculative decoding with draft models, KV-cache offload to CPU memory, separating prefill and decode onto different GPU pools, and quantization tuned to a quality sweet spot. Only a few numbers are given (5-10x cache speedup, up to 30% from draft models, 60+ hosted models), and none come with a setup or benchmark. The routing and cache ideas are the most reusable parts. Treat the claims as vendor assertions.

## Key ideas
- **Random load balancing fails for LLM traffic because requests vary widely in size and share cached prefixes.** — Workloads moved from short one-line prompts to large codebases sent by coding agents. A router that tracks which GPU holds which KV cache, and sends matching requests there, gives a much higher cache hit rate. ([13:21](https://youtu.be/TRe1u7dHYiA?t=801))
- **Speculative decoding: a small draft model proposes tokens and the large model verifies them in one pass.** — The speaker compares this to a senior engineer checking a junior's work. If the large model rejects a token, it regenerates from that point, which is the worst case. Mixing small and large models gives a net speedup. ([13:21](https://youtu.be/TRe1u7dHYiA?t=801))
- **Draft models trained on your own production traffic outperform generic ones.** — They report up to 30% improvement with generic training data, with more when the draft model is trained on the customer's own data. The platform captures production traffic and trains the draft model, presented as close to one click. ([14:49](https://youtu.be/TRe1u7dHYiA?t=889))
- **KV-cache offload to host RAM and restore on demand is a major cost saving.** — Generated tokens' KV entries are reused rather than recomputed. When GPU memory is full, the cache is moved to regular memory and brought back later, not discarded. The speaker says this is automatic and reports 5-10x speedups. ([16:17](https://youtu.be/TRe1u7dHYiA?t=977))
- **Prefill and decode have different hardware profiles, so they are split across separate GPU sets.** — Prefill (filling the context) is compute-heavy. Decode (generating tokens) is memory-heavy. Running both on one GPU makes them compete. The KV cache is transferred between the two pools. ([17:45](https://youtu.be/TRe1u7dHYiA?t=1065))
- **Engine choice and quantization are tuned per model rather than used as a single default.** — They run a forked open-source engine and choose the best engine for each model. Quantization is set by experiments to find the lowest precision that keeps quality acceptable. ([11:54](https://youtu.be/TRe1u7dHYiA?t=714))

## Techniques
- **Cache-aware request routing** — Keep a map of which replica holds which prompt-prefix KV cache, and route each request to the replica that already has its prefix instead of load-balancing randomly. *When:* Several inference replicas serve long, shared prefixes such as coding agents re-reading the same codebase.
- **Speculative decoding with a self-trained draft model** — Use a small model to propose several tokens and have the large model verify them in one pass. Train the draft model on your own logged completions. *When:* Decode latency of a large model is the bottleneck and you have enough production logs to train a draft model.
- **KV-cache offload to host memory** — When GPU memory fills, move cold KV entries to CPU RAM and restore them on the next hit, instead of evicting and recomputing. *When:* Long-context workloads where prefill recomputation is costly and GPU memory is the limit.
- **Prefill/decode disaggregation** — Assign prefill and decode to separate GPU pools and transfer the KV cache between them. *When:* Mixed traffic with long prompts and long outputs, where the two phases compete for the same GPU.
- **Per-model engine and precision selection** — Benchmark several inference engines and quantization levels per model, then deploy each model on the one that performs best. *When:* Serving a varied model catalogue where no single engine is best for every model.

## Numbers
- Nebius targets 5 GW of NVIDIA systems by end of 2030; NVIDIA invested $2B in Nebius ([1:07](https://youtu.be/TRe1u7dHYiA?t=67))
- Token Factory hosts 60+ open models (for example Kimi, DeepSeek, Qwen) ([3:54](https://youtu.be/TRe1u7dHYiA?t=234))
- Draft-model speculative decoding gives up to 30% improvement with generic training data, more with own data (unbenchmarked) ([14:49](https://youtu.be/TRe1u7dHYiA?t=889))
- KV-cache reuse gives 5-10x speedups (speaker's statement, no setup given) ([16:17](https://youtu.be/TRe1u7dHYiA?t=977))

## Hot takes
- Open-weight models are now close enough to proprietary ones that teams should pick them for cost.
- Random load balancing is wrong for LLM traffic; routing has to be cache-aware.
- Draft models trained on your own production logs beat generic draft models.

## Tools mentioned
Cursor, OpenCode

## Relevance to our work
- **agentos** (2/3): InferCraft (L2B) plans pluggable KV-cache strategies including CPU offload, and speculative decoding is on its roadmap. The talk gives the same tradeoffs at a higher level without measurements. → *Benchmark KV-cache CPU offload versus recompute on long coding-agent prompts on the single RTX 5090, and log the results as an InferCraft strategy comparison. The talk gives no setup to copy.*
- **general** (1/3): Long repeated coding-agent prompts depend on cache hits. Keeping prompt prefixes stable is a cheap way to get the benefit the talk describes. → *When writing agent prompts, keep the stable prefix (system prompt, CLAUDE.md, tool definitions) first and unchanging so cache hits are possible.*
