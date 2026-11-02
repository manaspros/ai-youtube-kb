# Same Model, Different Speed: Why Your Inference Provider Matters — FriendliAI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `_naLJOqVOEI` · [watch](https://youtu.be/_naLJOqVOEI) · **date:** 2026-10-12 · **length:** 13:04 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Yunmo · **orgs:** FriendliAI, OpenRouter
- **topics:** inference-serving, infra-cost-scaling, models-research · **tags:** open-weight models, inference provider choice, KV cache, prefix caching, cache-aware routing, speculative decoding, GLM 5.2, reliability, vendor pitch

> A FriendliAI engineer argues open-weight models now rival frontier ones, so the inference provider's speed, reliability and cost decide the outcome. Covers prefix-cache routing, tiered KV cache and hybrid speculative decoding. Mostly a sales pitch.

## Summary
The speaker, a founding engineer at FriendliAI, says open-weight models such as GLM 5.2 and MiniMax M3 now compete with leading proprietary models on coding, reasoning and agentic benchmarks. In a single-prompt test, GLM 5.2 built a tower-defense game about as well as Opus 4.8 at roughly 5.6 times lower cost. He says the same model can feel very different across providers, because latency, throughput and reliability depend on the whole inference stack. He describes two serving techniques for long agent prompts: cache-aware routing to the replica that already holds the prefix, and a hot/warm/cold KV cache hierarchy. He also covers hybrid speculative decoding, which picks between a draft model and prompt-copy drafting per workload. He argues reliability (5xx errors, rate limits, uptime) is part of speed, since one failed call can break a multi-step agent run. He closes by asking viewers to benchmark providers on their own workload and cites a customer split test that favored FriendliAI.

## Key ideas
- **Open-weight models are now good enough for many production workloads** — The speaker points to coding, reasoning and agentic benchmarks and a Code Arena leaderboard where GLM 5.2 ranks above Opus 4.8. He says the open question has shifted from quality to how fast and reliably they can run. ([1:13](https://youtu.be/_naLJOqVOEI?t=73))
- **Same weights, different provider, different experience** — In a tower-defense test, GLM 5.2 was about 5.6x cheaper than Opus 4.8 with similar quality. In a second test on the same model, one provider took about 2 minutes and another over 3 minutes. He argues this comes from the full stack: architecture, cache, routing, scheduler, quantization and GPU choice. ([2:38](https://youtu.be/_naLJOqVOEI?t=158))
- **Agent prompts are long and mostly repeated, so prefill is the cost** — Agent inputs often exceed 10K tokens, and 50 to 90 percent of tokens can be identical across requests. Recomputing the shared prefix wastes latency and GPU time. Reusing its KV tensors cuts TTFT. ([5:29](https://youtu.be/_naLJOqVOEI?t=329))
- **Reuse only works if the router knows where the cache lives** — KV cache sits on individual replicas rather than in one central store. The router must send each request to a replica that already holds its prefix, or the reuse benefit is lost. ([5:29](https://youtu.be/_naLJOqVOEI?t=329))
- **Treat KV cache as a memory hierarchy** — KV cache can exceed model weight size for long contexts. Hot blocks stay in GPU memory, warm blocks in CPU RAM, and cold blocks go to NVMe or disk. Less-used blocks are offloaded and fetched back when needed. ([6:55](https://youtu.be/_naLJOqVOEI?t=415))
- **Speculative decoding trades per-request speed against batch overhead** — Draft tokens are verified in one forward pass, so accepted tokens are effectively free and output quality is unchanged. Model-based drafting accepts more tokens but costs compute. Model-free drafting from the prompt or prior output is cheap but only helps when output resembles the context. The best choice depends on the workload. ([8:21](https://youtu.be/_naLJOqVOEI?t=501))
- **Reliability is part of speed for agent chains** — An agent may make many model calls for one task, so a single timeout, 5xx or 429 can invalidate the whole run. He says the provider should be judged on error rate and uptime, not only average latency. He cites a provider-stats snapshot showing over 99.9 percent uptime for GLM 5.1 Pro. ([9:45](https://youtu.be/_naLJOqVOEI?t=585))
- **Vendor benchmarks are conditional; benchmark your own workload** — He says many providers are fast only under certain benchmarks and conditions. His advice is to test prompts, token lengths, traffic patterns and latency targets on your own workload, across speed, reliability, cost and quality. ([11:07](https://youtu.be/_naLJOqVOEI?t=667))

## Techniques
- **Cache-aware request routing** — Track which replica holds which prompt prefix and route each request to the replica with the longest matching cached prefix, rather than round-robin. *When:* Multi-replica serving where agent requests share long system prompts or context prefixes.
- **Tiered KV cache offload** — Keep hot KV blocks in GPU memory, move less-used blocks to CPU RAM, and push cold blocks to NVMe or disk. Fetch them back on demand. *When:* Long-context workloads where KV cache is larger than the model weights and GPU VRAM is the limit.
- **Hybrid speculative decoding** — Choose per request between a small draft model (higher acceptance, more compute) and model-free n-gram-style drafting from prompt or prior output (low overhead). Let a speculator adapt to live traffic. *When:* Serving mixed workloads where output sometimes copies the context (edits, code) and sometimes does not.
- **Provider bake-off on your own workload** — Replay your real prompts, token lengths and traffic through several providers. Compare TTFT, throughput, error rate, uptime, cost per finished task and output quality. *When:* Choosing or switching inference providers for an open-weight model, especially for multi-step agents where cost compounds.

## Numbers
- GLM 5.2 was more than 5.6x cheaper than Opus 4.8 on the single-prompt tower-defense game task, with similar quality ([2:38](https://youtu.be/_naLJOqVOEI?t=158))
- Candy-crush-style game generation with the same model: FriendliAI about 2 minutes, another provider over 3 minutes ([4:02](https://youtu.be/_naLJOqVOEI?t=242))
- Agent inputs often exceed 10K tokens; 50 to 90 percent of tokens can be identical across requests ([5:29](https://youtu.be/_naLJOqVOEI?t=329))
- Customer split test for GLM models: FriendliAI over 7x faster than many other providers, with significantly lower error rate (customer is a coding-agent platform processing several trillion tokens per week) ([11:07](https://youtu.be/_naLJOqVOEI?t=667))
- Provider-stats snapshot shows over 99.9 percent uptime for GLM 5.1 Pro on FriendliAI ([9:45](https://youtu.be/_naLJOqVOEI?t=585))

## Hot takes
- Model quality is no longer the main question; what you can afford to run at scale is.
- The inference provider can matter as much as the model choice, even with identical weights.
- Speed claims from providers hold only under specific benchmarks; your own workload is the only benchmark that matters.
- Reliability is part of speed for agents, since one failed call can invalidate a whole multi-step run.

## Tools mentioned
OpenRouter (provider stats snapshot), Code Arena leaderboard

## Relevance to our work
- **agentos** (2/3): The talk's KV-cache reuse via cache-aware routing, tiered offload (GPU, CPU, NVMe) and hybrid speculative decoding overlap with InferCraft's KV-cache strategies and EAGLE-3 speculation on one RTX 5090. → *Read the cache-aware routing and tiered-offload sections, then compare TTFT on a shared-prefix agent workload between InferCraft's current KV strategy and a plain prefill baseline. Expected payoff: a number for the shared-prefix claim (50 to 90 percent identical tokens) on our own traffic.*
- **general** (1/3): The talk gives a clear framing for choosing an inference provider: bake off on your own workload and measure cost per finished agent task, not per token. → *When picking a provider or model for the entity-resolution LLM steps, run a short bake-off on real prompts and log latency, errors and cost per task.*
