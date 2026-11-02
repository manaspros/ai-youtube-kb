# Don't Buy a Mac Mini For Local AI (Do This)

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `IRyiP_U7RuA` · [watch](https://youtu.be/IRyiP_U7RuA) · **date:** 2026-10-02 · **length:** 16:11 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Kai (Kai Explains) · **orgs:** Apple, OpenAI, NVIDIA, SK Hynix
- **topics:** local-ai, inference-serving, models-research · **tags:** mac-mini, apple-silicon, memory-bandwidth, prefill, time-to-first-token, time-to-first-token, moe, sparse-models, kv-cache, gpt-oss-120b, dram-prices, hardware-buying-guide, rent-before-buy

> Kai Explains argues that buying a Mac Mini for local AI is a poor first move: size memory for the model you actually run, switch inference servers and measure time-to-first-token, and rent the model for a month before buying.

## Summary
The speaker, who nearly bought a 64GB M5 Pro Mac Mini, walks through why Apple's memory pricing (a flat $25/GB across the lineup) and the 2025-26 DRAM price spike make local AI hardware expensive. He argues that headline tokens-per-second numbers hide prefill latency, which an inference server swap can fix at zero cost. He makes a case for sparse mixture-of-experts models, which run faster than dense models of similar quality on the same hardware. His recommendation is to buy the M6 with 32GB for most people, the M5 Pro 64GB only for users who know their model needs 50 to 60GB, and to rent the model for a month before committing. The video is a practitioner opinion backed by a few anecdotal benchmarks, with no independent test harness.

## Key ideas
- **Headline Mac Mini prices hide the real cost of local AI because Apple charges a flat $25/GB for memory, which is soldered and not upgradable.** — Memory is the hard constraint: models that don't fit don't run at all. The base 16GB model is excluded, and the 64GB M5 Pro is about $2,699. The speaker says every Apple config he checked prices out at exactly $25/GB. ([1:03](https://youtu.be/IRyiP_U7RuA?t=63))
- **Naming is confusing: there is no M5 Mac Mini. The current Mac Mini lineup is the M6 (base chip, 153 GB/s) and the M5 Pro (307 GB/s, up to 64GB).** — The more expensive M5 Pro chip is an older generation than the cheaper M6, and its memory bandwidth is about twice as high. Token generation is bandwidth-bound, so the M5 Pro is the better machine for LLMs. ([3:23](https://youtu.be/IRyiP_U7RuA?t=203))
- **Context (KV cache) costs memory on top of model weights, and a 64GB machine is already near its limit with a large open model.** — gpt-oss-120b needs about 66GB in 4-bit, and 128GB machines show about 64-65GB resident. For a 70B model, the KV cache is about 10GB at 32K tokens and about 40GB at 128K. ([5:58](https://youtu.be/IRyiP_U7RuA?t=358))
- **Tokens-per-second benchmarks usually measure only generation, while prefill (time to first token) can dominate the real wait. Switching inference servers can cut prefill dramatically at zero cost.** — One user measured 57 tok/s in his interface, but end-to-end throughput was 3 tok/s at 8K context because prefill took 94% of response time. A server swap cut prefill from 49s to 1.7s with generation unchanged. Another user saw prefill drop from a minute or two to under 10 seconds on an older Ultra. ([9:30](https://youtu.be/IRyiP_U7RuA?t=570))
- **Sparse mixture-of-experts models are much faster than dense models of similar size on the same hardware, because only the active parameters are read per token.** — On an M4 Pro, a 35B MoE with about 3B active parameters ran at 78.8 tok/s, while a dense 27B ran at 14.7 tok/s. The 4-bit MoE model is about 17GB, so it fits on a 24GB machine. ([10:43](https://youtu.be/IRyiP_U7RuA?t=643))
- **Buying advice depends on the model you run: 64GB M5 Pro for models needing 50-60GB, 32GB M6 for most people, and rent a model for one month before buying.** — The 24GB base chip has about 19GB usable after macOS, and the 32GB M6 costs $1,299. The 24GB base chip with a 32GB upgrade is preferred over the 16GB upgraded to 32GB because it has 170 GB/s bandwidth versus 153 GB/s at the same price. Renting a model for a month costs about as much as a Thunderbolt cable. ([13:14](https://youtu.be/IRyiP_U7RuA?t=794))
- **Local AI is also justified by power draw or data-residency rules, not only by token cost. A Mac Mini idles at about 2.6W, while a dual-GPU rig pulls about 870W under load.** — Regulated records or NDA client code can make local the only option, regardless of token price. ([13:14](https://youtu.be/IRyiP_U7RuA?t=794))

## Techniques
- **Measure end-to-end latency (time to first token + generation), not just tokens/s** — Time from request sent to first token displayed, and the total end-to-end time at a realistic context length (for example 8K tokens). Compare this with the stated tok/s from the interface. *When:* Before buying hardware or judging a local setup, since prefill can dominate perceived latency.
- **Swap the default local inference server before buying hardware** — Keep the same machine, model and quantization, change the inference server (the video does not name the replacement, and the speaker says it is free to download), then compare prefill time at long context. *When:* When local responses feel slow and the default server may be the bottleneck.
- **Prefer sparse MoE models for local inference** — Choose a mixture-of-experts model with few active parameters (for example 35B total with about 3B active) over a dense model of similar quality, and check that the 4-bit file fits in memory with room for context. *When:* On memory-bandwidth-limited hardware such as Apple Silicon, where generation speed is set by bytes read per token.
- **Size memory for the model you run today, plus KV cache headroom** — Budget for weights (about 17GB for a 4-bit 35B MoE, about 66GB for gpt-oss-120b), usable RAM after macOS (about 19GB of 24GB), and KV cache (about 10GB at 32K and 40GB at 128K for a 70B model). *When:* Before choosing a memory tier, to avoid buying for a hypothetical future model.
- **Rent the model for a month before buying hardware** — Use a hosted version of the target model for one month and judge the real usage (heat, speed, quality) before buying. *When:* When deciding whether local AI is worth the hardware spend for your workflow.

## Numbers
- Apple memory price is a flat $25/GB across all Mac Mini and Mac Studio configs; base Mac Mini is $899 and the 64GB M5 Pro is $2,699 ([2:20](https://youtu.be/IRyiP_U7RuA?t=140))
- M6 base chip: 12 CPU cores, 12 GPU cores, 153 GB/s bandwidth. M5 Pro: up to 18 CPU cores, 20 GPU cores, 307 GB/s bandwidth ([3:23](https://youtu.be/IRyiP_U7RuA?t=203))
- gpt-oss-120b needs about 66GB in 4-bit; 128GB machines show about 64-65GB resident ([5:58](https://youtu.be/IRyiP_U7RuA?t=358))
- KV cache for a 70B model: about 10GB at 32K tokens, about 40GB at 128K tokens ([5:58](https://youtu.be/IRyiP_U7RuA?t=358))
- Mac Studio M5 Max starts at $5,099 with 128GB ([5:58](https://youtu.be/IRyiP_U7RuA?t=358))
- DRAM spot prices rose about 700% year over year; data centers consume about 70% of high-end production; SK Hynix expects the squeeze to last past 2030 ([7:03](https://youtu.be/IRyiP_U7RuA?t=423))
- Base Mac Mini: $599 at launch in late 2024, $899 now (+50%) ([8:11](https://youtu.be/IRyiP_U7RuA?t=491))
- Framework Desktop (Ryzen AI Max) went from $1,999 to $3,449 in 19 months; DGX Spark $4,699; RTX 5090 $1,999 MSRP with street price above $4,000 for 32GB ([8:11](https://youtu.be/IRyiP_U7RuA?t=491))
- Prefill benchmark: 57 tok/s reported in interface vs 3 tok/s end-to-end at 8K context; prefill was 94% of response time ([9:30](https://youtu.be/IRyiP_U7RuA?t=570))
- Prefill after a server swap: 49s down to 1.7s at the same context length; older Ultra went from 1-2 minutes down to under 10s ([9:30](https://youtu.be/IRyiP_U7RuA?t=570))
- Sparse 35B MoE (about 3B active): 78.8 tok/s vs dense 27B: 14.7 tok/s on an M4 Pro (about 5x) ([10:43](https://youtu.be/IRyiP_U7RuA?t=643))
- 35B MoE at 4-bit is about 17GB; dense 27B at 4-bit is about 9GB ([11:55](https://youtu.be/IRyiP_U7RuA?t=715))
- 24GB Mac has about 19GB usable after macOS; M6 32GB costs $1,299 (a $400 step up from the $899 base) ([13:14](https://youtu.be/IRyiP_U7RuA?t=794))
- Bandwidth: 16GB upgraded to 32GB runs at 153 GB/s; 24GB base runs at 170 GB/s, same price ([13:14](https://youtu.be/IRyiP_U7RuA?t=794))
- Mac Mini idles at about 2.6W; a dual-GPU rig pulls about 870W under load ([13:14](https://youtu.be/IRyiP_U7RuA?t=794))

## Hot takes
- Buying a Mac Mini for local AI at the headline price is a mistake; the real cost is the memory tier, which is priced at a flat $25/GB.
- The tokens-per-second number in most benchmark videos is generation-only and hides the prefill wait; switching the inference server is the cheapest fix.
- Sparse MoE models give a better experience than dense models of the same memory footprint, so the bigger model can be the faster one.
- Most buyers should get the 32GB M6 ($1,299) rather than the 64GB M5 Pro, unless they already know their model needs 50-60GB.
- Rent the model for a month before buying hardware.

## Tools mentioned
Apple Mac Mini (M6, M5 Pro), Apple Mac Studio (M5 Max, M5 Ultra), Framework Desktop (Ryzen AI Max), NVIDIA DGX Spark, NVIDIA RTX 5090, gpt-oss-120b, Mixture-of-experts 35B model (unnamed), Dense 27B model (unnamed), Apple machine learning research post (cited for bandwidth-bound token generation)

## Relevance to our work
- **agentos** (2/3): AgentOS's InferCraft layer runs vLLM on a single RTX 5090 and already plans for prefill and KV-cache trade-offs, so the video's point about measuring time-to-first-token and sizing KV cache at long context applies directly to its benchmarks. → *Add time-to-first-token and end-to-end latency at 8K and 32K context to the InferCraft benchmark harness, separate from generation tok/s, and log KV-cache footprint for each context length.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, which uses hosted models, so local-model memory sizing and prefill trade-offs matter only if it adds a local-model backend. → *If ProsHarness ever routes work to a local model, measure time to first token separately from tok/s before choosing a default backend.*
