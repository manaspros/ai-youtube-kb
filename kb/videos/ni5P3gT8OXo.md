# What Would It Cost to Run Kimi K3 Locally?

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `ni5P3gT8OXo` · [watch](https://youtu.be/ni5P3gT8OXo) · **date:** 2026-08-02 · **length:** 7:47 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Kai Explains host (not named in transcript) · **orgs:** Kimi, NVIDIA, Hugging Face
- **topics:** local-ai, inference-serving, infra-cost-scaling · **tags:** kimi-k3, mixture-of-experts, memory-sizing, quantization, gpu-hardware, dgx-b300, dgx-b200, mac-studio, concurrency, self-hosting, cost-estimation, hybrid-local-cloud

> Napkin math for running Kimi K3 locally: ~1.5 TB of 4-bit weights rules out Mac Studio and 4xH100, 8xB200 is barely enough, and serving 100 users is a data-center project.

## Summary
The host works through hardware sizing for Kimi K3, an open-weight mixture-of-experts model with about 2.8 trillion parameters, using only memory arithmetic and public specs. Storing the weights at 4 bits needs roughly 1.5 TB before runtime, KV/context, or serving overhead. A 512 GB Mac Studio cannot hold it, and 4xH100 (320 GB) is even smaller. An 8xB200 DGX (1.44 TB) reaches the weight floor with about 40 GB left, which he calls impractical. A DGX B300 node (about 2.3 TB) leaves roughly 900 GB of headroom, but he says real benchmarks are still needed. He relays Kimi's recommendation of 64+ accelerators for efficient inference, which implies at least eight servers. For 100 users, he argues the number that matters is concurrent active requests, not headcount, and then covers power (about 116 kW for eight B300s before cooling) and rental cost. He closes with a pattern from community threads: local models for private or routine work, cloud models for the hardest tasks, and renting hardware for a few weeks before buying.

## Key ideas
- **Raw 4-bit weight size sets the first hardware filter** — 2.8T parameters at 4 bits (half a byte each) is about 1.5 TB of weights, excluding quantization metadata, inference software, active conversations, and safety margin. ([1:18](https://youtu.be/ni5P3gT8OXo?t=78))
- **MoE sparsity cuts compute, not memory** — Only 16 of 896 experts are active per token, but all experts must stay resident for fast serving because routing can pick different experts for each next token. ([1:18](https://youtu.be/ni5P3gT8OXo?t=78))
- **Mac Studio is ruled out even at 2-bit** — The largest Mac Studio has 512 GB of unified memory. A hypothetical 2-bit version would still need about 700 GB for weights. ([1:18](https://youtu.be/ni5P3gT8OXo?t=78))
- **8xB200 hits the weight floor with almost no room** — 8 B200s give 1.44 TB, leaving about 40 GB after weights. The host does not consider that a practical fast setup. ([2:43](https://youtu.be/ni5P3gT8OXo?t=163))
- **DGX B300 is the first believable single-node option** — 8 B300s give about 2.3 TB, leaving roughly 900 GB beyond the raw weights. The host still says real weights and benchmarks are needed before claiming speed. ([2:43](https://youtu.be/ni5P3gT8OXo?t=163))
- **Kimi's own guidance implies a multi-server deployment** — Kimi recommends a supernode with 64 or more accelerators for efficient inference, which the host reads as at least eight GPU servers. ([4:02](https://youtu.be/ni5P3gT8OXo?t=242))
- **Users are not concurrency** — 100 employees each sending one request every 10 minutes, with 30-second answers, average about 5 active requests. Agents running several jobs each can multiply that quickly. ([4:02](https://youtu.be/ni5P3gT8OXo?t=242))
- **Physical infrastructure is a large hidden cost** — A DGX B300 takes 10 rack units and draws a listed 14.5 kW, so eight add up to about 116 kW before cooling, networking, storage, and operations staff. ([5:22](https://youtu.be/ni5P3gT8OXo?t=322))
- **Rental compute cost is in the hundreds of thousands per month** — Scaling public 8xB200 node prices to eight nodes gives roughly $313,000 to $577,000 per month for compute alone, which the host calls rough scale math. ([5:22](https://youtu.be/ni5P3gT8OXo?t=322))
- **Common practical pattern is hybrid local and cloud** — Community reports describe local models for private or repetitive work and cloud models for the hardest tasks. Commenters suggest renting hardware for a couple of weeks and testing with real users. ([6:48](https://youtu.be/ni5P3gT8OXo?t=408))

## Techniques
- **Weight memory estimate for a quantized model** — Weights in GB ≈ parameters (billions) × bits per parameter / 8. Count all experts for an MoE model, not just the active ones. The host uses 2.8T × 4 bits ≈ 1.5 TB, and he adds that the estimate excludes quantization metadata and runtime costs. *When:* As a first pass before reading any benchmark, to rule hardware in or out.
- **Headroom budget for a serving node** — Available memory minus raw weights minus KV cache, runtime, context, and serving software overhead. Treat anything under a comfortable margin as impractical even if the weights technically fit. The host's example is 8xB200 (1.44 TB) minus about 1.4 TB of weights, leaving about 40 GB. *When:* Deciding whether a GPU or unified-memory box can serve a model at useful speed and context length.
- **Concurrency sizing instead of user counting** — Average active requests ≈ users × requests per user per second × seconds per answer (Little's law). The host's example is 100 users × (1 request per 600 s) × 30 s ≈ 5 concurrent requests. Then size for the busiest moment, and multiply for agents that run several jobs at once. *When:* Sizing shared inference capacity or setting latency targets for a multi-user deployment.
- **Peak-moment plus prompt-length sizing** — Size against the peak number of active requests, the typical and maximum prompt length, and the required answer latency together. Long context needs more runtime memory and compute per request, so a 1M-token maximum is not a planning target. *When:* Choosing hardware for a long-context model shared by many users.
- **Hybrid routing: local for routine, cloud for hard** — Route private or repetitive work (document search, extraction, classification, routine coding) to a smaller local model, and send the hardest tasks to a frontier cloud model. *When:* Cutting cost or keeping data local without giving up quality on hard tasks.
- **Rent before you buy** — Rent a comparable GPU node for a couple of weeks and put real users on real work. Measure whether results are good enough, whether speed is acceptable, and how much operator effort it takes. *When:* Before committing to expensive on-prem hardware for a large open-weight model.

## Numbers
- Kimi K3 is about 2.8T parameters, with 896 experts and 16 active per token, and a 1M-token maximum context. ([1:18](https://youtu.be/ni5P3gT8OXo?t=78))
- 4-bit raw weights are about 1.5 TB (the host's rounding; 2.8T × 0.5 bytes is 1.4 TB). ([1:18](https://youtu.be/ni5P3gT8OXo?t=78))
- The largest Mac Studio has 512 GB of unified memory. A 2-bit version would still need about 700 GB. ([1:18](https://youtu.be/ni5P3gT8OXo?t=78))
- 4 × H100 at 80 GB each gives 320 GB. ([2:43](https://youtu.be/ni5P3gT8OXo?t=163))
- 8 × B200 gives 1.44 TB of GPU memory, leaving about 40 GB after weights. ([2:43](https://youtu.be/ni5P3gT8OXo?t=163))
- 8 × B300 gives about 2.3 TB, leaving roughly 900 GB beyond raw 4-bit weights. ([2:43](https://youtu.be/ni5P3gT8OXo?t=163))
- Kimi recommends a supernode with 64+ accelerators for efficient inference. ([4:02](https://youtu.be/ni5P3gT8OXo?t=242))
- 100 users × one request per 10 minutes × 30-second answers ≈ 5 concurrent requests on average. ([4:02](https://youtu.be/ni5P3gT8OXo?t=242))
- A DGX B300 takes 10 rack units and has a listed power draw of 14.5 kW. Eight units total about 116 kW before cooling. ([5:22](https://youtu.be/ni5P3gT8OXo?t=322))
- Scaling public 8 × B200 node prices to 8 nodes gives about $313,000 to $577,000 per month for compute alone (rough estimate). ([5:22](https://youtu.be/ni5P3gT8OXo?t=322))

## Hot takes
- The memory math is useful, but it is an estimate only. The host says real weights and benchmarks are still needed before any speed claim.
- Internal inconsistency: 8 × B200 gives 1.44 TB, and the host subtracts about 1.5 TB of weights. That would be negative. The stated 40 GB headroom only works with about 1.4 TB of weights (2.8T × 0.5 bytes), so the 1.5 TB figure is a rounding issue, not a clean estimate.
- The 64-accelerator recommendation is relayed secondhand from Kimi's launch blog and is not verified in the transcript.
- Reddit quotes (for example, the Airbus A380 noise comparison and 'models good enough that scale beat supermodels') are anecdotes and not benchmarks, as the host notes.
- Rental and power figures are rough public-price scaling, not quotes. No throughput, latency, or tokens-per-second measurements are shown.
- Not sponsored. The closing 'subscribe' line is a channel plug, not a product pitch. Quality is capped at 3 because there are no measured results.

## Tools mentioned
Kimi K3, Hugging Face, Mac Studio, NVIDIA H100, NVIDIA B200, NVIDIA B300, NVIDIA DGX B200, NVIDIA DGX B300, MXFP4 (4-bit format, as named in transcript), Claude, GPT

## Relevance to our work
- **agentos** (2/3): InferCraft runs vLLM on a single RTX 5090 and needs capacity planning. The weight-size filter, KV/runtime headroom budget, and Little's-law concurrency estimate are directly reusable, though the video is about much larger deployments. → *Add a capacity-planning section to InferCraft docs: weight GB = params × bits/8, plus KV-cache and runtime headroom, and average concurrent requests = users × req rate × latency. Use it to pick which model sizes fit the RTX 5090 before adding larger-model targets.*
- **prosharness** (1/3): ProsHarness wraps Claude Code, and the hybrid pattern of local models for routine work and cloud models for hard tasks is a routing policy question. → *Consider a routing policy for ProsHarness steps: routine or private steps to a local model, hardest steps to Claude. Measure quality on real tasks before switching.*
