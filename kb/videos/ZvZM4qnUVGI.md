# New Local AI Inference Engine You Should Be Using in 2027 ? (FreeToken)

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `ZvZM4qnUVGI` · [watch](https://youtu.be/ZvZM4qnUVGI) · **date:** 2026-09-02 · **length:** 16:17 · **format:** review · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kai (channel host, name taken from the channel) · **orgs:** FreeToken, DeepSeek, Ollama, Anthropic
- **topics:** inference-serving, local-ai · **tags:** moe-expert-offload, expert-cache, pcie-bottleneck, llama-cpp, tail-latency, system-ram, nvidia-rtx, open-weight-models

> FreeToken, a five-week-old local inference engine, runs a 433 GB mixture-of-experts model on one 96 GB GPU by caching recently used experts and splitting misses between PCIe transfer and CPU compute; system RAM is the real limit.

## Summary
The host walks through FreeToken, an Apache-licensed local inference engine about five weeks old, which serves DeepSeek V4 Flash (753B parameters, 433 GB of weights) on a desktop with a 96 GB GPU at roughly 15 tokens per second. The core argument is that a mixture-of-experts model activates only a few experts per token, so the cost that matters is the PCIe transfer needed when a missed expert is requested, not the arithmetic. FreeToken makes two changes: a global LRU expert cache with no router predictor, which relies on short-range routing locality, and a split of misses, where some experts are fetched over the bus and others are computed on the CPU where their weights already sit, with a one-time hardware measurement setting the ratio. The paper's replay results show lower miss rates than llama.cpp's static layer split, and its worst single-turn latency stays under 44 seconds where baselines reach 150 to 946 seconds; the host argues that tail latency matters more than average tokens per second for agents with timeouts. The host flags that the launch post benchmarked against Ollama as a soft target, that third-party benchmarks range from about 7 to 100 tokens per second mainly depending on system RAM and bus speed, and that the project has no macOS build, open AMD and Apple Silicon requests, and a reported crash past 48,000 prefill tokens. Practical advice: stay on llama.cpp, Ollama or LM Studio unless you have a recent NVIDIA card and a lot of system RAM, and buy memory before the next GPU.

## Key ideas
- **Mixture-of-experts models only activate a few experts per token, so the weights can live in system RAM and only the active experts need to reach the GPU.** — DeepSeek V4 Flash has 256 experts per layer across 43 layers, with 6 routed per token. About 13B of 284B parameters are active per token. The router can pick a different set each token, so all weights must stay reachable. ([1:11](https://youtu.be/ZvZM4qnUVGI?t=71))
- **The PCIe transfer from system RAM to the GPU, not the compute, sets the decode speed.** — A good desktop bus runs around 50 GB/s, while GPU memory is about 20x faster. Every miss on a non-resident expert pays the transfer cost. ([2:29](https://youtu.be/ZvZM4qnUVGI?t=149))
- **llama.cpp's layer-based CPU split is fast and predictable but blind to routing.** — The split-by-layer count is fixed before the run, so it cannot adapt to which experts the router picks at runtime. ([3:45](https://youtu.be/ZvZM4qnUVGI?t=225))
- **Expert-prediction offloading is well-trodden and still ends every miss as a PCIe transfer, so better prediction does not lift the bus ceiling.** — The host says prior systems differ mainly in how well they predict misses, not in how they serve them. ([4:43](https://youtu.be/ZvZM4qnUVGI?t=283))
- **A global LRU expert cache with no predictor beats the alternatives on the paper's replay traces.** — Routing has short-range locality, so recently used experts are likely to be needed again. The paper's replay numbers are covered in the numbers list. ([4:43](https://youtu.be/ZvZM4qnUVGI?t=283))
- **FreeToken splits misses between bus transfer and CPU compute, and a one-time hardware measurement sets the ratio.** — For a missed expert, the engine either fetches weights to the GPU or runs the expert on the CPU and returns the small output. Both paths overlap. One command times the actual machine and computes the split. ([6:00](https://youtu.be/ZvZM4qnUVGI?t=360))
- **Tail latency, not average throughput, is the metric that decides whether a coding agent finishes.** — Agent frameworks have timeouts, so a turn that exceeds them is killed. The host cites a two-minute idle watchdog in OpenClaw and a roughly 10-minute default request timeout in Claude Code. ([7:27](https://youtu.be/ZvZM4qnUVGI?t=447))
- **Vendor benchmarks against Ollama overstate the gain. The fair comparison is against the strongest baseline.** — The launch post claims 3 to 4x against Ollama. The paper's own claim against the strongest baseline on real workloads is 1.5 to 2.3x. ([8:39](https://youtu.be/ZvZM4qnUVGI?t=519))
- **System RAM capacity, not VRAM, determines whether a model runs well, and the GPU acts as a cache.** — The hardware table pairs each GPU with a RAM size. Only the 96 GB VRAM and 512 GB RAM configuration fits the 433 GB model. Third-party results spread widely, from about 7 to 100 tokens per second, and track RAM size and bus speed. ([9:52](https://youtu.be/ZvZM4qnUVGI?t=592))
- **The project is immature and has real platform limits.** — The repo is five weeks old with one release and 137 open issues. There is no macOS build. AMD and Apple Silicon are open requests. There is a reported crash past 48,000 prefill tokens, while the paper runs sessions up to 65,000. ([11:04](https://youtu.be/ZvZM4qnUVGI?t=664))

## Techniques
- **Global LRU expert cache across all layers, no predictor** — Keep expert weights in GPU memory and evict by least-recent use across every layer, not per layer. Do not model the router. Rely on routing having short-range locality so the experts used in the last few tokens are likely needed next. *When:* MoE models whose total weights exceed VRAM but whose per-token active set is small and repeats across nearby tokens.
- **Split misses between PCIe fetch and CPU compute, overlapped** — On a cache miss, choose per expert between copying weights to the GPU and running the expert on the CPU, then returning its small output. Run both paths concurrently so the bus and CPU stay busy. The ratio is set by measurement, not a constant. *When:* When the bus is the bottleneck and the CPU has enough memory bandwidth and cores to run expert FFNs in place.
- **Calibrate the offload split once per machine** — Run a one-time benchmark that times this machine's PCIe link, memory channels and CPU, then reuse the resulting ratio for every token. The transcript says one command does this but does not name it. *When:* Heterogeneous setups where PCIe generation, memory channels and board type change the optimal split.
- **Replay recorded routing traces to compare cache policies fairly** — Record expert-routing traces once, then replay the identical traces through each placement policy at the same cache size. Only placement changes, so miss rates are directly comparable. Report the miss rate for each policy (for example, 16% vs 41% vs 62% on one model in the paper). *When:* Benchmarking or choosing an expert or KV cache policy where you want to isolate the policy from the workload.
- **Judge offload engines by worst-case turn latency, not mean tokens per second** — Measure the maximum latency of a single agent turn across configurations and compare it to the client's timeout. Treat any turn past the timeout as a failure, not as slow. *When:* Evaluating local inference for coding agents or other clients with fixed request or idle timeouts.
- **Install and build requirements for FreeToken as stated** — Linux on x86 with an NVIDIA GPU, an NVIDIA driver R580 or newer, and CUDA 13 (the caption reads 'Q to 13'). Kernels compile on first run, so expect a slow first start. There is no macOS build. The transcript does not show the install command. *When:* Deciding whether a machine can run FreeToken before attempting an install.

## Numbers
- DeepSeek V4 Flash: 753B parameters, 433 GB weights, about 15 tokens/s on one desktop with a 96 GB GPU. ([0:00](https://youtu.be/ZvZM4qnUVGI?t=0))
- DeepSeek V4 Flash: 256 experts per layer, 43 layers, 6 routed per token; about 13B of 284B parameters active per token (under 5%). ([1:11](https://youtu.be/ZvZM4qnUVGI?t=71))
- PCIe bus about 50 GB/s on a good desktop; GPU memory about 20x faster. ([2:29](https://youtu.be/ZvZM4qnUVGI?t=149))
- Replay miss rates at 50-90% cache: FreeToken recency cache 16% and 39%; placement during pre-fill 41% and 59%; llama.cpp static split 62% and 89% (two models). ([6:00](https://youtu.be/ZvZM4qnUVGI?t=360))
- RTX 5090, DeepSeek V4 Flash: 22-25 tokens/s, 1.5-1.9x the strongest tested engine (paper). ([7:27](https://youtu.be/ZvZM4qnUVGI?t=447))
- 8 GB RTX 4060 laptop, 35B model: 39.3 tokens/s (paper). ([7:27](https://youtu.be/ZvZM4qnUVGI?t=447))
- Worst single turn: FreeToken under 44 s in every config; every baseline exceeds 150 s somewhere; llama.cpp peaks at 232 s; KTransformers at 946 s. ([7:27](https://youtu.be/ZvZM4qnUVGI?t=447))
- Paper's claimed speedup over the strongest baseline on real workloads: 1.5-2.3x. Launch post claims 3-4x against Ollama. ([8:39](https://youtu.be/ZvZM4qnUVGI?t=519))
- Third-party, RTX 3090 with 64 GB RAM, 35B model: 51.4 vs 28.7 tokens/s (llama.cpp); time to first token on a 21,000-token prompt drops from 37 s to 9 s (1.79x). ([9:52](https://youtu.be/ZvZM4qnUVGI?t=592))
- Third-party: RTX 5080 about 100 tokens/s on a model larger than its VRAM. ([9:52](https://youtu.be/ZvZM4qnUVGI?t=592))
- Third-party, 8 GB laptop: 44.5 vs 11.1 tokens/s (llama.cpp) on the same model. ([11:04](https://youtu.be/ZvZM4qnUVGI?t=664))
- Third-party, RTX 5090 in a coding-agent harness: 996 samples over 68 minutes, averaging 9.66 tokens/s. Another run: 7.5 tokens/s cold, 17 after warmup. ([11:04](https://youtu.be/ZvZM4qnUVGI?t=664))
- Repo status: five weeks old, one release, 137 open issues. ([11:04](https://youtu.be/ZvZM4qnUVGI?t=664))
- Reported crash when pre-fill exceeds 48,000 tokens; the paper's benchmarks run sessions up to 65,000 tokens. ([12:27](https://youtu.be/ZvZM4qnUVGI?t=747))
- llama.cpp: 17 hardware backends, quantization from 1.5 to 8 bits, about 3.5 years old. ([12:27](https://youtu.be/ZvZM4qnUVGI?t=747))
- Agent timeouts cited: OpenClaw two-minute idle watchdog; Claude Code default request timeout around 10 minutes. ([8:39](https://youtu.be/ZvZM4qnUVGI?t=519))

## Hot takes
- FreeToken's central idea (a cache plus CPU compute for misses) is not new as a concept. The novelty is the policy and the measured split, and the speaker says prediction-based prior art mostly differs in prediction, not in serving misses.
- The launch post's 3-4x claim against Ollama is a soft target. The paper's own claim against the strongest baseline is 1.5-2.3x.
- For agents, worst-case turn latency against timeouts matters more than average tokens per second.
- Buy system RAM before the next GPU if you run MoE models locally.
- Almost all headline numbers come from the paper's authors. Independent results vary from about 7 to 100 tokens per second.
- Not usable yet on Mac, AMD, older NVIDIA or ordinary laptops. The idea may land in llama.cpp before FreeToken matures.

## Tools mentioned
FreeToken, llama.cpp, Ollama, LM Studio, KTransformers, DeepSeek V4 Flash, vLLM, Apache Spark, Mixtral offloading, MoE-Infinity, Pro-MoE, Expert Flow, Fine-MoE, Fiddler, Claude Code, OpenClaw, RTX 5090, RTX 5080, RTX 4060, RTX 3090, NVIDIA driver R580+, CUDA 13, PCIe

## Relevance to our work
- **agentos** (2/3): InferCraft (vLLM + Ray Serve on one RTX 5090, pluggable KV-cache strategies incl. CPU offload) overlaps with expert and KV offload policy. The replay-trace method and the LRU-vs-static-split comparison are directly reusable for choosing an offload policy. → *Record routing or access traces from an InferCraft run on the 5090 and replay them through an LRU cache vs a static CPU-offload split at fixed cache size. Report miss rate and worst-case latency.*
- **prosharness** (1/3): ProsHarness wraps Claude Code, and the talk cites Claude Code's default request timeout as the limit that kills slow local-model turns. Long checkpointed runs are exposed to this. → *Check ProsHarness's timeout settings for long turns against Claude Code's default request timeout, and add a checkpoint before any turn that may run past it.*
