# The Frontier AI Inference Cloud for Agents — Byung-Gon (Gon) Chun, FriendliAI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Hvb2LfMH58c` · [watch](https://youtu.be/Hvb2LfMH58c) · **date:** 2026-09-20 · **length:** 14:59 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Byung-Gon Chun · **orgs:** FriendlyAI (FriendliAI), Seoul National University, Kilo Code, LG
- **topics:** inference-serving, infra-cost-scaling, agent-architecture · **tags:** agentic-inference, prefix-caching, kv-cache, cache-aware-routing, open-weight-models, end-to-end-task-latency, vendor-pitch, glm-5.2

> FriendliAI's CEO argues agent workloads need task-level (end-to-end) latency optimization, not per-request speed, and pitches prefix caching, KV cache management and cache-aware routing on an open-weight inference cloud.

## Summary
The speaker, the founder and CEO of FriendliAI, argues that agents are a different inference workload from chat: a task is a loop of LLM calls and tool calls with a growing shared context, so the metric that matters is end-to-end task completion time. He says open-weight models now reach a usable quality bar for many agent tasks and cost far less than a frontier closed model on the same job. The core technical content is four pillars for agent inference: prefix caching of KV state, KV cache management across GPU, host memory and disk, cache-aware routing across replicas, and agent-aware scheduling that uses task context. Most of the talk is company positioning, with a demo, customer testimonials and a product overview (serverless API, dedicated endpoints, bring-your-own-GPU). The concrete numbers are from a single vendor-chosen comparison and a client's split test, so they should be treated as unverified claims. The agent-aware optimization pillar is presented as a frontier direction rather than a described implementation.

## Key ideas
- **The unit of agent inference is a task, not a request, so latency should be measured per task completion** — A user cares when the whole task finishes, not how fast one LLM call returns. Agent tasks alternate LLM calls with tool calls, and the number of calls depends on the input, so a fixed request-rate plan does not fit. ([6:19](https://youtu.be/Hvb2LfMH58c?t=379))
- **Open-weight models have crossed a usable quality bar for many agent workflows and are much cheaper** — One demo task (building a tower defense game) was run on an open-weight model and a frontier closed model. The speaker claims both were usable and the open model cost about 5.6x less ($0.27 vs about $1.50). This is a single example from a vendor. ([1:42](https://youtu.be/Hvb2LfMH58c?t=102))
- **Consecutive agent steps share a large prefix, so recomputing it on every step wastes most of the compute** — Context grows each step because observations are appended. Prompt lengths are much longer than in chat, and the shared prefix is the biggest optimization target. Prefix KV can be cached and only the new suffix processed. ([5:17](https://youtu.be/Hvb2LfMH58c?t=317))
- **Four-pillar stack: prefix caching, KV cache management, cache-aware routing, and agent-aware optimization** — Model-level work such as sparse attention for long contexts sits underneath. Only the four pillars are covered in the talk. The first three are described as shipped; agent-aware optimization is described as the next frontier. ([7:20](https://youtu.be/Hvb2LfMH58c?t=440))
- **Cache-aware routing must trade off locality against load balancing across a global cluster** — A naive load balancer spreads requests evenly and destroys cache locality. A cache-aware router sends a request to a pod that already holds the prefix, but it still balances load so one pod does not become a hotspot. Requests from the same task are routed to the same pod. ([9:25](https://youtu.be/Hvb2LfMH58c?t=565))
- **Scheduler-level knowledge of the agent program could enable preemption, speculative prefill and better eviction** — Most systems schedule each LLM call independently. If the optimizer knows which agent program a call belongs to, it could preempt the right work, speculatively prefill context for the likely next step, or evict cache entries based on agent context. The speaker frames this as future work. ([9:25](https://youtu.be/Hvb2LfMH58c?t=565))
- **KV cache capacity is handled by tiering and sharing, not just by one GPU** — Packing more active context per GPU, KV quantization, hierarchical caching across GPU memory, host memory and disk, and distributed cache sharing across replicas are presented as the tools for keeping prefixes resident. ([8:21](https://youtu.be/Hvb2LfMH58c?t=501))

## Techniques
- **Prefix KV caching for agent steps** — Compute KV for the shared prefix once, store it, and on later steps reuse it and only prefill the new suffix. The speaker says this lowers time to first token and per-step compute. *When:* Multi-step agent loops where the context grows by appending tool observations and each step shares most of the prior prompt.
- **Tiered KV cache with quantization and cross-replica sharing** — Pack more active context per GPU, quantize KV to reduce memory, spill KV across GPU memory, host memory and disk, and share a prefix across replicas instead of keeping it in one instance. *When:* Long agent contexts exceed one GPU's memory, or many replicas serve the same agent prefixes.
- **Cache-aware routing with load-aware fallback** — Route each request to a replica that already holds its prefix in cache, while still balancing load so no replica becomes a hotspot. Keep requests from one task on the same replica. *When:* Multi-replica or multi-region inference where a naive round-robin balancer would repeatedly miss the cache.
- **Optimize end-to-end task latency as the target metric** — Define success as time to finish the whole task across all its LLM and tool calls, not the latency of each call, and tune scheduling and caching against that number. *When:* Designing or benchmarking an agent serving stack, where per-call p95 can look good while the task still runs slowly.
- **Agent-aware scheduling (described as future work)** — Give the scheduler knowledge of which agent program a call belongs to, to decide what to preempt, what to prefill speculatively for the likely next step, and what to evict. *When:* When a serving layer is shared across many concurrent agent sessions with different priorities.

## Numbers
- Opus 4.8 costs about $1.50 vs $0.27 for GLM 5.2 on the same demo task (stated as 5.6x cheaper), on the speaker's own platform, single example ([2:46](https://youtu.be/Hvb2LfMH58c?t=166))
- A client (Kilo Code) split test reported FriendliAI consistently about 7x faster than other third-party providers and direct model-lab use, with a significantly lower error rate; vendor-sourced testimonial, no raw data shown ([13:05](https://youtu.be/Hvb2LfMH58c?t=785))
- Agent tasks can run tens or hundreds of inference steps, sometimes over minutes or hours, in a deep-research style run of explaining vLLM speculative decoding ([5:17](https://youtu.be/Hvb2LfMH58c?t=317))
- Agent prompt and completion lengths are much longer than chat and grow across a task; the speaker shows a distribution chart of internal coding agent runs without giving numeric values in the transcript ([4:15](https://youtu.be/Hvb2LfMH58c?t=255))
- Friendly AI demo of a mobile game task on GLM 5.2 showed the platform completing the task end to end faster than another well-known provider; no numbers given in the transcript ([11:00](https://youtu.be/Hvb2LfMH58c?t=660))

## Hot takes
- Per-request latency is the wrong metric for agents; end-to-end task completion time is what users feel.
- Open-weight models have crossed the quality bar for many agentic workflows, so cost is the main reason to switch from closed frontier models.
- Recomputing the shared prefix on every agent step is one of the largest wastes in agent inference.
- Agent-aware scheduling (knowing which program a call belongs to) is the next frontier, beyond per-request serving.

## Tools mentioned
vLLM, GLM 5.2, Kilo Code, Claude Opus 4.8, MiniMax, Kimi

## Relevance to our work
- **agentos** (2/3): InferCraft is vLLM-based with pluggable KV-cache strategies and a priority scheduler on one RTX 5090. The talk's prefix-caching, tiered KV and cache-aware routing ideas map onto those components, and its task-level latency framing applies to any multi-step agent benchmark. → *Add a task-level benchmark to InferCraft that replays a multi-step agent session (growing shared prefix, interleaved tool calls) and reports end-to-end task time and prefix-cache hit rate, not only per-request TTFT.*
- **prosharness** (1/3): ProsHarness runs long Claude Code agent loops with checkpoint/resume. The talk's point that a long task is many small steps with a growing shared context is relevant to checkpoint design, but it is about serving, not the harness. → *Record per-step wall-clock and context size in the ProsHarness checkpoint log, so long-run slowdowns can be traced to growing context or to tool waits.*
