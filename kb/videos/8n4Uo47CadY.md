# How They Fixed AI's Biggest Local Hardware Problem (with FreeToken)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `8n4Uo47CadY` · [watch](https://youtu.be/8n4Uo47CadY) · **date:** 2026-09-02 · **length:** 9:36 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andres (Better Stack host) · **orgs:** Better Stack, UC Berkeley, University of Texas
- **topics:** local-ai, inference-serving · **tags:** moe, expert-offload, pcie, vram, kv-cache-offload, ollama, llama.cpp, opencode, qwen, deepseek, rtx-5090, double-buffering, live-cache-resize

> Walkthrough of FreeToken, an open-source MoE inference engine that caches hot experts on the GPU, streams misses over PCIe, and splits misses between GPU and CPU; the speaker's 2.3x speedup over Ollama held only when the model overflowed VRAM.

## Summary
Better Stack reviews FreeToken, an open-source inference engine from Berkeley and UT Austin researchers, built for serving mixture-of-experts (MoE) models on consumer GPUs. The core idea is to treat expert placement as a caching problem: the full model stays in system RAM and the GPU keeps the most recently used experts, which works because the router tends to reuse the same experts across tokens. The engine hides prefill transfer costs with double buffering, and on a cache miss it measures PCIe and RAM bandwidth to decide how to split missing experts between GPU transfer and CPU compute. The speaker tested Qwen 3.6 35B at 8-bit (about 38 GB) on an RTX 5090 with 32 GB VRAM, where FreeToken finished an OpenCode test-writing task in 4:40 at 132 tok/s versus Ollama's 14:20 at about 58 tok/s. Shrinking the expert cache showed that cutting it from 58% to 40% of the model cost only about 7% speed, while going below roughly 20% fell off a cliff. When a 4-bit build fit fully in VRAM, Ollama was faster (240 vs 225 tok/s), so the speaker concludes FreeToken only helps once a model exceeds VRAM and only for MoE models. Single-machine, single-task, single-run evidence.

## Key ideas
- **Treat MoE expert placement as a caching problem, not a fixed layer-placement problem.** — llama.cpp-style tools pin layers to GPU or CPU at load time, but the experts used change every token, so a fixed layout misses most traffic. FreeToken keeps the full model in RAM as the source of truth and lets the GPU hold recently used experts. The speaker argues routers reuse experts heavily, so most requests hit the cache. ([0:58](https://youtu.be/8n4Uo47CadY?t=58))
- **Prefill is the worst case for expert streaming, and double buffering hides most of it.** — A long prompt touches nearly every expert, so sparsity disappears and nearly the whole model must stream from RAM. FreeToken computes the current layer while streaming the next layer's experts over PCIe, so transfer and compute overlap. ([2:20](https://youtu.be/8n4Uo47CadY?t=140))
- **On a cache miss, the engine chooses between a PCIe transfer and CPU compute, based on measured hardware.** — The 'QSTAR' policy splits each batch of missing experts between sending them to the GPU and computing them on the CPU. FreeToken measures PCIe and RAM bandwidth on the machine, so a narrow-PCIe laptop and a fast-RAM desktop get different splits without manual config. ([3:34](https://youtu.be/8n4Uo47CadY?t=214))
- **Weights are loaded from disk directly into the engine's runtime memory layout.** — A custom format the speaker calls 'FTW' (transcript wording) skips the repackaging step most tools run at startup, which the speaker credits for fast load times of very large models. ([3:34](https://youtu.be/8n4Uo47CadY?t=214))
- **Ollama's layer split sends every token through a slow CPU detour once the model overflows VRAM.** — For the 8-bit Qwen model (~38 GB on a 32 GB card), Ollama keeps roughly 70% of layers on GPU and 30% on CPU, so every token crosses the CPU layers. FreeToken keeps the math on the GPU and streams only the missing experts. ([4:35](https://youtu.be/8n4Uo47CadY?t=275))
- **Benchmark result: about 2.3x faster on one overflow case, not the 3x in the title.** — On the 8-bit Qwen 3.6 35B OpenCode task, FreeToken took 4:40 at 132 tok/s versus Ollama's 14:20 at about 58 tok/s. The speaker's own numbers support roughly 2.3x on one run. ([5:37](https://youtu.be/8n4Uo47CadY?t=337))
- **Expert cache size can be resized live, and a small hot set does most of the work.** — The cache can be resized on a running server in about a second without restart. Dropping from 58% to 40% of the model cached cost about 7% speed; going below roughly 20% degraded sharply as the PCIe link saturated. ([6:56](https://youtu.be/8n4Uo47CadY?t=416))
- **When the model fits in VRAM, FreeToken is slower than Ollama.** — With a 4-bit build that fits in 32 GB, Ollama loads it fully on GPU at 240 tok/s versus FreeToken's 225 tok/s, since streaming has nothing to stream and only adds overhead. ([6:56](https://youtu.be/8n4Uo47CadY?t=416))

## Techniques
- **Expert-cache over RAM-resident weights** — Keep all MoE weights in system RAM as the authoritative copy; allocate a fixed GPU budget for experts; on routing, serve hits from GPU and fetch misses over PCIe. Recently used experts are retained in the cache. *When:* MoE models whose total weights exceed VRAM but whose per-token active set is small, with routing locality across tokens.
- **Double-buffered expert streaming during prefill** — While the GPU computes layer N, asynchronously transfer layer N+1's required experts over PCIe so transfer and compute overlap instead of running serially. *When:* Long prompts where routing touches nearly all experts and the engine would otherwise stall on bulk transfer.
- **Bandwidth-measured split of cache misses between GPU transfer and CPU compute** — Measure PCIe and host RAM bandwidth at startup. For each batch of missing experts, choose the fraction to transfer to the GPU and the fraction to compute on the CPU so both finish at about the same time. *When:* Hardware with an uneven balance of PCIe and RAM bandwidth (e.g., narrow PCIe link vs fast DDR5), where neither pure strategy is always better.
- **Load weights directly into runtime memory layout** — Store the model in an engine-native on-disk format so loading maps the bytes straight into the layout the engine uses, with no repack pass on startup. The speaker names the format 'FTW' (transcript wording). *When:* Very large model files where startup repackaging dominates load time.
- **Find the cache knee by shrinking the cache live** — On a running server, resize the GPU expert cache in steps (the speaker reports about 1 s per resize, no restart) and record tok/s at each size. The knee where speed falls off marks the working-set size of hot experts. *When:* Sizing the GPU expert budget for a given model, quant and workload, or checking how much VRAM a model's hot set really needs.
- **Test setup in OpenCode (as the speaker did)** — Point OpenCode at the local OpenAI-compatible endpoint for each engine (the speaker configured both Ollama and FreeToken there), then run the same coding task on each and compare run statistics. Config keys and commands were not shown in the video. *When:* A quick head-to-head of local inference engines on a real agent coding task rather than a synthetic benchmark.

## Numbers
- DeepSeek V4 Flash: 284B total parameters, 13B active per token (speaker's example). ([0:58](https://youtu.be/8n4Uo47CadY?t=58))
- Qwen 3.6 35B at 8-bit is about 38 GB, roughly 6 GB over the RTX 5090's 32 GB VRAM. ([4:35](https://youtu.be/8n4Uo47CadY?t=275))
- Ollama splits this model roughly 70% GPU / 30% CPU by layer. ([4:35](https://youtu.be/8n4Uo47CadY?t=275))
- OpenCode test-writing task, 8-bit Qwen 3.6 35B: Ollama 14 min 20 s at about 58 tok/s; FreeToken 4 min 40 s at 132 tok/s (about 2.3x, not the 3x in the title). ([5:37](https://youtu.be/8n4Uo47CadY?t=337))
- Shrinking the expert cache from 58% to 40% of the model cost about 7% speed; below about 20% speed fell off sharply. ([6:56](https://youtu.be/8n4Uo47CadY?t=416))
- 4-bit Qwen 3.6 35B (fits in 32 GB): Ollama 240 tok/s vs FreeToken 225 tok/s. ([6:56](https://youtu.be/8n4Uo47CadY?t=416))
- Live GPU expert cache resize on a running server takes about 1 second without restart. ([6:20](https://youtu.be/8n4Uo47CadY?t=380))

## Hot takes
- The title's 'three times faster than Ollama' is not what the on-camera test showed: about 2.3x on one overflow case, and Ollama was faster when the model fits in VRAM.
- Evidence is one machine, one model, one OpenCode task, and one run per engine, with no variance or repeats reported.
- The speaker frames the tool as adaptive hardware profiling, and the 'FTW' weight-format and 'QSTAR' policy details are unverified claims from the research paper, not shown in the video.
- Desktop app is limited (Windows/Linux only, could not modify files in the test), so the usable path is the CLI.

## Tools mentioned
FreeToken (open-source MoE inference engine, CLI and desktop app; Windows/Linux desktop only), Ollama, llama.cpp, OpenCode, DeepSeek V4 Flash (284B total / 13B active, as stated), Qwen 3.6 35B (8-bit and 4-bit builds tested), NVIDIA RTX 5090 (32 GB VRAM), PCIe, DDR5 system RAM (64 GB)

## Relevance to our work
- **agentos** (2/3): InferCraft runs vLLM on one RTX 5090 with pluggable KV-cache offload strategies (H2O, CPU offload, LMCache); FreeToken's GPU expert cache over RAM with PCIe-vs-CPU miss routing is a directly comparable offload design for MoE models on the same class of hardware. → *Benchmark MoE serving in InferCraft on the 5090 with an expert-offload setup (or vLLM CPU offload) at a few GPU cache sizes, recording tok/s at each to find the knee, the way the video does.*
