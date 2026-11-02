# How Inference Keeps Up with Our Insatiable Need for Tokens — Cerebras & Gimlet Labs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `_cRgl3maiT8` · [watch](https://youtu.be/_cRgl3maiT8) · **date:** 2026-10-12 · **length:** 22:47 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Daniel (Cerebras, works on AI agents), Michelle (co-founder, Gimlet Labs) · **orgs:** Cerebras, Gimlet Labs, AWS, Google, AMD, NVIDIA, Anthropic
- **topics:** inference-serving, infra-cost-scaling · **tags:** kv-cache, paged-attention, chunked-prefill, prefill-decode-disaggregation, speculative-decoding, continuous-batching, prompt-caching, heterogeneous-hardware, kernel-generation, cerebras, gimlet, coding-agents-load

> Cerebras and Gimlet Labs walk through LLM inference optimizations, from paged KV cache and chunked prefill to prefill/decode and attention/FFN disaggregation across mixed hardware, plus agent-generated GPU kernels.

## Summary
The speakers open with spend and token-volume figures, then explain why decode is memory-bound: each new token rereads the weights, so compute sits idle for much of the time. They walk through the optimization history: tensor parallelism (with its all-reduce tax), continuous batching, paged KV cache, prompt caching, and chunked prefill to stop long coding-agent prompts from clogging the pipeline. Next they cover disaggregation, splitting prefill and decode into separate pools, and then splitting by model (speculative decoding) and by layer (attention on memory-heavy hardware, FFN on matmul-heavy hardware). Gimlet's pitch is a multi-silicon inference cloud that maps each piece of a workload to the best available chip, with claimed 3-10x gains over homogeneous systems at the same power. The talk ends with Gimlet's Kforge agent, which brute-force searches for faster kernels and reportedly sped up GPT-OSS 120B on AMD by 33% end-to-end in under a week. Much of the closing is product positioning, so the technical sections carry most of the value.

## Key ideas
- **Decode is memory-bound, not compute-bound** — Each generated token requires reading all model weights from memory, so compute often sits idle, with the speakers claiming up to 90% of time spent waiting on memory loads. ([1:28](https://youtu.be/_cRgl3maiT8?t=88))
- **Tensor-parallel splitting has a communication tax** — Splitting a model across GPUs needs all-reduce before attention and FFN in every layer, so adding GPUs gives well under linear speedup and costs more energy per token. This creates a throughput vs. speed Pareto frontier. ([2:59](https://youtu.be/_cRgl3maiT8?t=179))
- **Continuous batching fills idle slots, but the KV cache becomes the limit** — Batching reuses one weight read across many requests, and continuous batching slots new requests into freed slots. Each request's KV cache grows with context, so memory runs out quickly under long contexts. ([4:08](https://youtu.be/_cRgl3maiT8?t=248))
- **Paged KV cache removes reserved-but-unused memory** — Allocating KV cache in virtual-memory-style pages, instead of reserving a full contiguous block per request, reduces waste and lets the server handle roughly 3x more requests. ([5:34](https://youtu.be/_cRgl3maiT8?t=334))
- **Prompt caching skips repeated prefill** — When a long system prompt is shared, the KV cache from an earlier request can be reused, so the server skips the expensive prefill phase and picks up where it left off. ([6:39](https://youtu.be/_cRgl3maiT8?t=399))
- **Long agent prompts block short requests unless prefill is chunked** — A single very long prefill (200K to 1M context coding agents) blocks other prefill and decode work. Splitting prefill into chunks lets short chat requests interleave. ([8:06](https://youtu.be/_cRgl3maiT8?t=486))
- **Disaggregate by phase, then by layer, based on the workload** — Prefill is compute-bound and decode is memory-bound, so separate pools can scale independently. The speakers extend this to splitting attention (memory-heavy) from FFN (matmul-heavy) across different machines, and say no single best disaggregation or hardware exists. ([10:42](https://youtu.be/_cRgl3maiT8?t=642))
- **Match each workload piece to the hardware it fits** — The speakers argue that the right chip depends on the piece: Cerebras SRAM-based memory is much faster for decode, and AWS Trainium handles prefill in their proposed split. Gimlet's cloud routes each piece to the best of many chip types. ([12:43](https://youtu.be/_cRgl3maiT8?t=763))
- **Speculative decoding uses a small draft model to cut full-model passes** — A small draft model proposes candidate tokens and the full model verifies them in one pass. In their example, 9 tokens took 3 full-model passes instead of 9. ([14:02](https://youtu.be/_cRgl3maiT8?t=842))
- **Agents are now being used to write GPU kernels** — Gimlet's Kforge agent takes hardware and workload profiles and searches for faster kernels by brute force. The speakers say it sped up GPT-OSS 120B on AMD by 33% end-to-end within about a week. They also propose agents for compilers, incident response, and chip design. ([19:19](https://youtu.be/_cRgl3maiT8?t=1159))

## Techniques
- **Paged KV cache** — Allocate KV cache in fixed-size virtual pages mapped to free physical memory, rather than reserving a contiguous block for each request's maximum length. *When:* When serving many concurrent requests with variable context lengths and memory is the bottleneck.
- **Prefix / prompt caching** — Keep the KV cache for a shared long prefix, such as a system prompt, and reuse it for later requests so prefill is skipped. *When:* When many requests share a long system prompt or document prefix, like coding agents or chat apps.
- **Chunked prefill** — Split a very long prompt's prefill into smaller chunks and interleave them with decode steps and other requests' prefill. *When:* When long-context requests (agents, big documents) are causing latency spikes for short interactive requests.
- **Prefill/decode disaggregation** — Run prefill and decode on separate worker pools, scaling each pool by its own load, and transfer KV cache between them. *When:* When the prompt-to-output token ratio varies widely and compute and memory needs diverge.
- **Speculative decoding** — Run a small draft model to propose several tokens, then verify them with one forward pass of the full model. *When:* When decode latency per token matters more than raw throughput, and a well-matched draft model is available.
- **Attention/FFN disaggregation** — Map attention layers (KV-cache-heavy, memory-bound) and FFN layers (dense matmul) to different hardware, passing activations between them. *When:* For very large models where a single layer is resource-heavy and hardware with different bandwidth/compute profiles is available.
- **Agent-driven kernel search** — Give an LLM agent hardware profiles, workload profiles, and a baseline kernel, then have it search and benchmark candidate optimized kernels. *When:* When kernels must be tuned across many hardware targets and model/workload shapes, and hand-tuning does not scale.

## Numbers
- Projected AI compute spend of $765B this year, rising to up to $1.6T in 2031 (speaker figures) ([0:08](https://youtu.be/_cRgl3maiT8?t=8))
- Google's serving volume went from 480T tokens/month (I/O last year) to 3.2 quadrillion tokens/month (last month), per the speaker ([0:08](https://youtu.be/_cRgl3maiT8?t=8))
- Llama 3.3 70B is 25% cheaper and 3.6x faster than at its first release ([1:28](https://youtu.be/_cRgl3maiT8?t=88))
- Up to 90% of time spent with compute idle waiting on memory during decode ([1:28](https://youtu.be/_cRgl3maiT8?t=88))
- Splitting a model across 4 GPUs gives roughly 2x speedup in practice, not 4x, because of all-reduce overhead ([2:59](https://youtu.be/_cRgl3maiT8?t=179))
- A 128K-context coding agent request needs about 42 GB of KV cache ([5:34](https://youtu.be/_cRgl3maiT8?t=334))
- Rule of thumb for a 70B model: about 1 GB of KV cache per 3,000 tokens per request ([5:34](https://youtu.be/_cRgl3maiT8?t=334))
- Paged KV cache lets the server handle about 3x more requests than contiguous reservation ([6:39](https://youtu.be/_cRgl3maiT8?t=399))
- H100 memory bandwidth is 3.35 TB/s; the speaker claims Cerebras has about 7,000x that bandwidth (21,000 TB/s) ([12:43](https://youtu.be/_cRgl3maiT8?t=763))
- Decode throughput: about 3,000 tokens/s on Cerebras vs about 600 tokens/s on H100 (speaker figures) ([12:43](https://youtu.be/_cRgl3maiT8?t=763))
- Partnership with AWS Trainium prefill plus Cerebras decode claimed to give 5x high-speed token capacity in the same footprint ([12:43](https://youtu.be/_cRgl3maiT8?t=763))
- Gimlet's heterogeneous mapping claimed to give 3-10x faster inference vs homogeneous systems at the same power budget ([14:02](https://youtu.be/_cRgl3maiT8?t=842))
- Speculative decoding example: 9 tokens needed 3 full-model passes instead of 9 ([15:30](https://youtu.be/_cRgl3maiT8?t=930))
- Speculative decoding plus fast-hardware draft models claimed to give about 10x interactivity at the same throughput vs homogeneous machines ([16:49](https://youtu.be/_cRgl3maiT8?t=1009))
- Kforge sped up GPT-OSS 120B on AMD hardware by 33% end-to-end in under a week ([19:19](https://youtu.be/_cRgl3maiT8?t=1159))
- Claude Code fast mode described as using about 6x the tokens for about 2x speed (speaker says 'I think', so unverified) ([4:08](https://youtu.be/_cRgl3maiT8?t=248))

## Hot takes
- There is no best form of disaggregation and no best hardware; the right choice depends on model, workload, and latency vs. throughput targets.
- Agents will help build the next generation of custom silicon, creating a recursive loop between AI and chip design.
- Inference providers face a fundamental throughput vs. speed trade-off, and fast modes are sold by moving to the speed end of the Pareto frontier.

## Tools mentioned
Cerebras CS3, AWS Trainium, AWS EFA, NVIDIA H100, AMD GPUs, Kforge (Gimlet agent for kernel generation)

## Relevance to our work
- **agentos** (2/3): InferCraft (vLLM, one RTX 5090, 4-class priority scheduler, KV-cache strategies) overlaps directly with paged KV, chunked prefill, prompt caching, and speculative decoding covered here. → *In InferCraft's priority scheduler, test chunked prefill so long coding-agent prompts don't stall short interactive requests on the single 5090; benchmark TTFT for the short-request class before and after.*
- **general** (1/3): Useful background on why long-context coding agents load inference systems, and on prompt-prefix reuse as a cost lever for cheap-model pipelines. → *When designing Haiku pipelines with long shared system prompts, keep the prefix stable so provider prompt caching can skip prefill.*
