# inference-serving — 208 videos

*model serving, KV cache, speculative decoding, quantization, GPUs, latency*

By channel: AI Engineer 83 · Kai Explains 90 · AI LABS 1 · Better Stack 34

**Synthesized guide:** [guides/inference-serving.md](../guides/inference-serving.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [You Don't Need an Expensive GPU Anymore (Strata 100 tok/s)](../videos/mED-boddeWI.md)
`mED-boddeWI` · Kai Explains · 2026-11-01 · q4 · practitioner · review · also: local-ai, token-cost-efficiency

Kai tests Strata, an MIT-licensed local inference engine that runs DeepSeek V4.1 Flash (763B MoE) on a 12GB GPU by tiering experts across GPU, RAM and SSD. Conclusion: it works, but RAM is now the real cost, and the viral 100+ tok/s figure was prefill, not decode.

- Techniques: Three-tier expert placement by access frequency; Report prefill and decode separately, with context length, quantization and cache state; Per-tier cost math for a hardware decision; Quantization and KV-cache choices for large local models; Reduced-memory mode and specialized builds; Pre-purchase hardware checklist
- Tools: Strata (local inference engine, MIT license, GitHub, Windows/Linux/Mac desktop app), llama.cpp (mentioned as a comparison), Ollama (mentioned as a comparison), Qwen 3.8 Flash Next (125B, Q2 build), Qwen smaller sibling (transcribed as 'Quen 3.635B', measured at 59.7 tok/s on RTX 3060), DeepSeek V4.1 Flash (763B MoE, MIT license, 1M context; transcribed as 'DeepSeq V4.1 Flash'), DeepSeek API (off-peak and peak output pricing), Betel Juice (community fork, transcribed as 'betel juice'), NVIDIA RTX 3060, RTX 5070, RTX 5070 Ti, RTX 5090, RTX 4090 (price reference), AMD MI50 (2018 data-center GPU, about $700 used), PCIe 4 NVMe SSD (2TB, about $253)

## [Avalon Just Beat Strata by 47% on AMD (9x Faster)](../videos/0F63pTS8Gt0.md)
`0F63pTS8Gt0` · Kai Explains · 2026-11-01 · q4 · practitioner · review · also: local-ai, evals

Breakdown of the "Avalon beats Strata by 47% on AMD" claim: a llama.cpp fork tuned for one 7900 XT box, and why the number only holds on that machine and that model file.

- Techniques: Benchmark provenance checklist; Bandwidth-ceiling estimate for MoE decode; Expert cache from spare VRAM with CPU fallback; Cheap draft head that shares the expert cache for MoE speculative decoding; Perplexity as a fast quant-quality screen, with a caveat; mmap for models larger than VRAM plus RAM; Diagnose multi-GPU slowdowns as a bottleneck shift
- Tools: Avalon (llama.cpp fork, MIT, repo live Oct 9 2026, Qwen 3.8B Flash Next only, Linux only, RDNA3 required by installer), Strata (AMD-focused inference engine for MoE models; 0.1.43 in the table, 0.2.8 current), llama.cpp (stock, with an open draft PR from Piotr Wilkin), Boon llama.cpp fork (source of the first expert cache version in Avalon), ik_llama.cpp (source of Avalon's compression types), Unsloth IQ4 quantization (perplexity reference), Strata ISTA quantization format, Claude Opus (the video says version 5.5; the README credits it with writing the GPU and CPU kernels), ROCm (AMD software stack, cited as the lagging part), Vulkan (Avalon has no Vulkan backend, so it does not run on Windows), Qwen 3.8B Flash Next (MoE: 125B active, 51B lookup table, 48 layers, 512 experts per layer, top-10 routing)

## [Bytes Is This The End of Token?](../videos/PfR4S3Zzdoo.md)
`PfR4S3Zzdoo` · Kai Explains · 2026-10-31 · q4 · deep · review · also: token-cost-efficiency, models-research

Kai Explains on why tokenizer-free byte models are real progress but still pay per generation step; reads two papers (Breaking the Token Ceiling, H-Net) and gives a cost-per-megabyte audit.

- Techniques: Cost-per-megabyte audit across model upgrades; Measure tokenizer ratio per prompt type before upgrading; Count forward passes, not tokens, when estimating throughput; Filter tokenizer-free model headlines by bytes per expensive step; Convert context window to real text capacity per tokenizer; Entropy-based patching (BLT pattern); Learned hierarchical chunking (H-Net pattern)
- Tools: Llama 3 (8B teacher; 128,256-entry tokenizer), SmolLM3 (3B open-source token model; transcript says 'small LM3'), Gemma 2B (Google token model), Breaking the Token Ceiling (paper: byte students with end-of-token marker), Byte Latent Transformer (BLT, paper), H-Net (Cartesia, hierarchical byte-level network), Mamba (architecture; cited as background), Bolmo (AI2 7B byte model, Olmo architecture, Apache 2.0, on Hugging Face), Olmo (AI2 architecture), Claude Opus 4.7 (Anthropic; new tokenizer), Aleph Alpha model (tokenizer ~15% fewer tokens than GPT-5), GPT-5 (comparison tokenizer)

## [When Running Your Own AI Models Beats Paying for APIs - Steven Latré, imec](../videos/9-Y_oS9OBLc.md)
`9-Y_oS9OBLc` · AI Engineer · 2026-10-31 · q4 · practitioner · talk · also: infra-cost-scaling, token-cost-efficiency, local-ai

imec's AI lead benchmarks coding agents on open-weight models vs. APIs and finds that concurrency, GPU utilization and harness choice, not just accuracy, decide when self-hosting pays off.

- Techniques: GPU-utilization break-even check for API vs self-host; Concurrency ramp test on a single inference box; Task-level benchmark grid across harness, model and hardware; Measure harness token output and wall time on a paid GPU; Map model choice to hardware tiers
- Tools: Codex, Pi (transcribed as 'Py'), Claude Code, SWE-Bench Pro, Qwen, DeepSeek, GLM, Kimi K3, Claude Opus (mentioned as a reference point), NVIDIA B200-class GPU (transcribed as 'A times B 200')

## [Every Way to Get 256 GB of VRAM for Local AI at Full Context](../videos/JPHT9AvoPSA.md)
`JPHT9AvoPSA` · Kai Explains · 2026-10-30 · q4 · practitioner · review · also: local-ai, token-cost-efficiency

A price-and-speed tour of every route to 256GB of memory for running DeepSeek V4.1 Flash locally; the real metric is bits per weight, and a cheap DDR4 plus RTX 3090 MoE-offload build is the surprise pick.

- Techniques: Size the box from bits per weight, not gigabytes; Measure quantization fidelity as next-token agreement; Keep the hot parts of a sparse MoE on GPU and the rest in system RAM; Put a large, sparsely read lookup table on SSD; Raise the macOS GPU memory limit and persist it; Enable the model's draft head for speculative decoding; Break-even against the API before buying hardware; Budget prefill time for long first prompts
- Tools: DeepSeek V4.1 Flash, DeepSeek API, Unsloth quantized builds, Dwarfstar inference engine (transcribed 'Antiresis Dwarfstar'), MLX (Mac inference route), vLLM 0.20, CUDA 13, ROCm, Qwen 3.8 (incl. a Flash Next variant), Mac Studio M5 Ultra 256GB / 512GB, Mac Studio M3 Ultra, NVIDIA DGX Spark

## [How Revolut Cut AI Coding Costs 90% With Self-Hosted Open Models - David Abitbol, Revolut](../videos/Ok6QdZHCcI8.md)
`Ok6QdZHCcI8` · AI Engineer · 2026-10-29 · q4 · practitioner · talk · also: token-cost-efficiency, sandboxing-execution, governance-compliance

Revolut's AI ops lead explains how self-hosting GLM on dedicated GPUs cut its coding-AI invoice to about a tenth, and which serving metrics and tuning levers mattered.

- Techniques: Lead-time-first AI adoption metric; Latency-led GPU capacity planning; Serving parameter sweep; Local router for multimodal fallback; Harness-agnostic OpenAI-compatible endpoint; Sandbox with per-command allow/deny rules; Compliance and telemetry baseline
- Tools: GLM (GLM 5.1 and a later GLM 5.x model; caption reads 'GLM 5.3'), GLM-5 Flash (caption reads 'Glam5G Flash'), Gemini, Claude Code, Codex, Codex app, OpenCode (caption reads 'OpenCodex'), Anthropic API, OpenAI API, OpenAI Responses API (compatible endpoints), NVIDIA B200 GPUs, Blackwell GPUs

## [Your GPU Is Nerfed for Local AI (NVIDIA's Hidden Limit)](../videos/VIm73gaY_hM.md)
`VIm73gaY_hM` · Kai Explains · 2026-10-28 · q4 · practitioner · review · also: local-ai, token-cost-efficiency

Explains why the viral RTX GPU "unlock" doubles only one FP16 microbenchmark: real gains land on 16-bit serving, long-context prefill and image/video work, not token decode or GGUF, and power caps can cost more than the unlock gains.

- Techniques: Identify the data path before expecting a GPU gain; Check and raise the GPU power limit before anything else; Benchmark prefill and decode separately; Treat unsigned firmware or kernel modules as high-trust code
- Tools: NVIDIA RTX 4090, NVIDIA RTX 3090, NVIDIA RTX 3090 Ti, NVIDIA RTX 3060, NVIDIA RTX 4070 Ti Super, NVIDIA RTX 5090, NVIDIA RTX A6000, NVIDIA Titan RTX, NVIDIA RTX 2080 Ti, vLLM, llama.cpp, Ollama

## [Stop Guessing Your vLLM Config: Benchmarking LLMs on Runpod - Chris Vela, Runpod](../videos/P_0_Th_ZzIg.md)
`P_0_Th_ZzIg` · AI Engineer · 2026-10-28 · q2 · practitioner · review · also: infra-cost-scaling, evals

RunPod's Chris Vela argues for benchmarking vLLM configs on GPU pods across concurrency levels before production, and previews an unreleased BenchPod template. Vendor pitch with some reusable method.

- Techniques: Config-sweep benchmarking before production; Tune max batched tokens for long generations; Pin vLLM and CUDA to what the model needs; Agent-readable benchmark and health API; Model choice by task size and team size
- Tools: RunPod (GPU pods, serverless, storage volumes, Docker images), vLLM (OpenAI-compatible server, YAML config, nightly builds), BenchPod (unreleased RunPod template built on vLLM, with FastAPI, a watchdog and benchmark metrics), Kimi K3, DeepSeek, GLM, Qwen 3.8 (transcribed as 'Quinn 3.8'), Docker, NVIDIA B300, NVIDIA H200, CUDA 12.8 and 13.0, Claude (mentioned as the service many internal users are moving off)

## [Your PS5 Can Now Run Open Models (And It's Surprisingly Fast)](../videos/TgmC_VZEKTE.md)
`TgmC_VZEKTE` · Kai Explains · 2026-10-27 · q4 · practitioner · review · also: local-ai, claude-code

A viral claim that a PS5 runs a 27B open model at 20 tokens/s, checked against a 613-second Claude Code first prompt. The lesson: prefill (reading) speed, driver limits and OS sandboxing decide agent usefulness more than writing speed.

- Techniques: Split latency into prefill and decode; Estimate decode ceiling from bandwidth; Use a smaller model for agent/harness work; Chunk long prompts to avoid GPU watchdog timeouts; Multi-token prediction for decode speedup; Serve a household local API
- Tools: PS5LM (llama.cpp port for PS5; started by Mert Kobanov Oct 1; fork PS5LM+ by ABI245E; the two later merged), llama.cpp, llama.cpp Vulkan build (RedStapler, Linux), RADV (Mesa Vulkan driver, ported to PS5), Unsloth UD-IQ2 2-bit quant (6.8 GB; 9.2 GB sibling), Qwen 27B dense model (Apache 2.0, released Aug by Alibaba; caption reads 'Quen 3.827B'), Qwen 9B (4-bit on PS5 Slim, 55 tokens/s; caption reads 'Quen 3.59b'), Qwen 8B Flash Next (caption reads 'Quen 3.8 Flash Next'; the host says 180B parameters, split across PC and PS5), Gemma 4B (61 tokens/s, reads images; caption reads 'Gemma 44B'), Llama 3.2 3B (124 tokens/s), Claude Code, Relapse (PS5 jailbreak, firmware 7.00-13.60, public Sep 29)

## [Is Flint the Killer of Qwen 3.8 27B? (First RSI Model)](../videos/RmE4G6MhOVU.md)
`RmE4G6MhOVU` · Kai Explains · 2026-10-26 · q4 · practitioner · review · also: local-ai, models-research, evals

Kai Explains tests Recursive's Flint MoE coding model: the 131 tok/s headline is real, but always-on reasoning, long-context slowdown and agent loops mean task completion time is what matters.

- Techniques: Bandwidth-bound decode estimate; Time-to-task-completion benchmark; Token-budget cap test; Split prefill from decode timing; Hybrid planner and implementer; Fair engine comparison; Hardware fallbacks reported by users
- Tools: Flint (Recursive, 39.8B MoE, 2.5B active, 256 experts, 262,144-token text-only context, Apache license), Recursive REC inference engine (Mac-only, proprietary), Apple MLX, llama.cpp (Vulkan build on AMD), Ollama (23 GB model file), Unsloth 4-bit and NVFP4 weights (25 GB 4-bit file, 11.9 GB smallest quant), vLLM (NVFP4 run on RTX Pro 6000), Qwen dense 27B and Qwen MoE 35B (as named in transcript), OpenCode (agent, 5-minute silence timeout, free tier), Pi (Recursive's own agent, ~17k-token system prompt), OpenRouter (free Flint access), Terminal Bench 2.1

## [How to Build Voice Agents That Don't Fall Apart When You Interrupt - Jesse Hall, LiveKit](../videos/OmyqelTwpOo.md)
`OmyqelTwpOo` · AI Engineer · 2026-10-26 · q4 · practitioner · talk · also: voice-multimodal, evals

LiveKit's Jesse Hall argues voice agents must be evaluated as whole conversations: measure time-to-first-audio and time-to-first-sentence, use non-blocking tool calls, use audio-aware turn detection, and benchmark full stacks with simulated callers.

- Techniques: Time-to-first-audio and time-to-first-sentence instrumentation; Non-blocking (async) tool calls in a voice agent; Audio-aware turn detection; Full-stack scenario simulation with identical replay; Regression scenarios from production failures; Financial voice-agent guardrail checklist
- Tools: LiveKit (open-source real-time agent framework and infrastructure), LiveKit turn detector (audio + transcript end-of-turn model), LiveKit inference (model serving tuned for voice; speaker says it is model agnostic), Gemma 4 31B (auto-caption reads 'Gemma 431B'; top LLM on the hotel agent benchmark), ChatGPT advanced voice mode (cited as using LiveKit)

## [DeepSeek Is Free Now but What’s the Catch?](../videos/zIWxzkO1nak.md)
`zIWxzkO1nak` · Kai Explains · 2026-10-25 · q4 · practitioner · news · also: token-cost-efficiency, models-research

Kai Explains argues the viral DeepSeek margin math misses the point: DeepSeek's economics come from KV-cache hit rates, not raw GPU throughput, and the cache layer is the part left closed.

- Techniques: Effective input cost from hit rate; Keep a stable prompt prefix across turns; Sticky routing for replica-local caches; Provider checklist for caching; Back-of-envelope check on vendor throughput claims
- Tools: DeepSeek V4.1 Flash (1017 update), DeepInfer (inference engine, Apache 2.0), DeepSeekRecipe (Rust API-to-token library), 3FS (distributed file system), DeepSeek search API, DeepSeek KV cache technical report 'Pushing the Limits of KV Cache Compression', vLLM, Fireworks, DeepInfra, OpenRouter, Nebius, Parasail

## [This Tiny Qwen 27B Model Runs on a 12GB GPU](../videos/XKejQWnispc.md)
`XKejQWnispc` · Better Stack · 2026-10-24 · q3 · practitioner · review · also: local-ai, mcp-and-tools, evals

Better Stack reviews Saluki 27B, a ~7.9GB quantization of a 27B Qwen-family model tuned to keep tool calling intact at the cost of math, and tests it on local llama.cpp and a DGX Spark.

- Techniques: Serve a GGUF quant locally with llama.cpp; Two-part tool-calling smoke test; Tool-call reliability count; Recommended settings for tool calls; Report strict and lenient parser scores separately; Measure agent throughput, not just file size; Pick by workload
- Tools: Saluki 27B (model name as captioned; the transcript attributes it to Underdog), Qwen 27B base model (captioned as 'QEN 3.827B'), Qwen 3.8 Flash (captioned as 'Quen 3.8 Flash next'; used as a comparison model at 4-bit), llama.cpp (llama-server, stock build), Ollama, Unsloth quants (4-bit, IQ2_XXS, IQ2_S), ISTA-DAS Lab 2-bit quant (RCO quantization search), Ternary Bonsai 2 (PrismML custom llama.cpp fork), MLX (an unfinished port was mentioned), BFCL (Berkeley function-calling benchmark, single-turn), AIME 2025, SWE-bench Verified (50-task subset)

## [llama.cpp Just Made 125B MoE Models 4× Faster!](../videos/shl8FFSoANE.md)
`shl8FFSoANE` · Kai Explains · 2026-10-23 · q4 · practitioner · review · also: local-ai

A llama.cpp PR caches individual MoE experts in spare VRAM for a claimed 4x decode speedup; the real gain over a tuned baseline is about 1.5-2.2x and depends on hit rate, PCIe link and workload.

- Techniques: Per-expert LRU cache in VRAM instead of whole-layer offload; Go/no-go on hit rate from llama.cpp logs; 15-minute self-benchmark protocol; Check the PCIe link before enabling expert offload; Benchmark the actual workflow, not just decode speed; Disable the cache first when a model starts looping; Sizing rule of thumb
- Tools: llama.cpp (release 0.7 / B11480 or newer; PR 29887; PR 30449), Qwen Flash Next (125B MoE, 4-bit build; transcript spells it 'Quen 3.8 Flashnext'), Strata (model-family-specific runtime, 3-bit build), nvidia-smi, Multi-token prediction (MTP), Speculative decoding, --n-cpu-moe (spoken as NCPU MOE), RTX 5090, RTX 5070, RTX 4090, RTX 4070 Super, RTX 4060 laptop

## [I Tested Every Best Local AI For GPU (8GB TO 24GB VRAM)](../videos/ugKAkCVBcz0.md)
`ugKAkCVBcz0` · Kai Explains · 2026-10-22 · q4 · practitioner · review · also: local-ai, models-research

Local model picks for 8 to 24 GB VRAM. The GGUF file (quant method and uploader) matters more than the model name, MoE models survive RAM spill while dense ones collapse, and thinking tokens often dominate wall time.

- Techniques: Back-of-envelope decode ceiling; Fit check with desktop headroom; MoE expert offload to system RAM; Pick the quant by builder, then bit width; Quantize the KV cache for Qwen, not Gemma; Time-to-answer measurement; Power-cap for sustained speed on a 3090 Founders Edition; Side-by-side local vs frontier check
- Tools: llama.cpp (named as 'Lama CPP'), Qwen 3.6 27B dense (captioned 'Quen 3.827B'), Qwen 3.6 35B-A3B MoE (captioned 'Quen 3.635BA3B'), Gemma 12B (captioned 'Gemma 412B', Q3 file 5.69 GB), ISTA quantized builds (GSQ build, 2-bit, 3-bit, 3.5-bit), Liquid AI LFM 2.5 24B (captioned 'LFM 2.524B'), NVIDIA Nemotron 3.5 Bolt (captioned as 'Bolt'; 74B total, 9B active, 2-bit with vision module), Speculative decoding head (named, not specified), Hugging Face (default download source), Artificial Analysis (intelligence index scoring), Chat LLM by Abacus AI (sponsor, $10/month, bundles GPT-6 Astra, Claude Fable 5.1, Gemini 4, Opus 5.5, DeepSig V4.1 and Kimi K3 as captioned), Windows (desktop VRAM overhead)

## [Same GPU, 50% More Output: Why the Operator Matters — Oliver Kennon, SemiAnalysis](../videos/3axY1wz2OvA.md)
`3axY1wz2OvA` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · also: infra-cost-scaling, token-cost-efficiency, governance-compliance

Oliver Kennan (SemiAnalysis) argues GPU cost per useful token depends on the operator's serving software and ops discipline, not just the chip, and that cost positions are relative to competitors, which matters for compute futures and rental price hedges.

- Techniques: Cost per acceptable token; Compare on the same chip at a fixed interactivity target; Assess the operator, not just the hardware; Safe update and rollback process for serving
- Tools: SemiAnalysis inference calculator (public), ClusterMax 3.0 (SemiAnalysis operator rating; a 4.0 is mentioned as upcoming), NVIDIA B200 GPU

## [Is a Faster Model Actually Faster? Test the Whole Job — Morgan Suo, MiniMax](../videos/YvQ4BVTWfHI.md)
`YvQ4BVTWfHI` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · also: evals, token-cost-efficiency, models-research

MiniMax's Morgan Suo argues a faster model must be judged on a whole research job (sources, numbers, cost, latency, retries), not on tokens/sec or averages, and walks through M3.1 Flash's sparse attention, KV-cache and expert quantization, speculative decoding, and reasoning-effort trade-offs.

- Techniques: Whole-job acceptance eval; Planted-fact position sweep for long-context retrieval; Per-subscore regression check instead of averages; Concurrency sweep with P95 time-to-first-token; Reasoning-effort budget comparison with a recorded setting; Reproducibility record and staged rollout
- Tools: MiniMax M3.1 Flash (LLM, long context, MoE, sparse attention, KV-cache quantization, reasoning effort control), MiniMax A3 (video generation model, shown in opening and closing segments), speculative decoding (serving method), KV cache (serving-side internal memory of keys and values), MoE experts (routed experts with 4-bit weights and activations, shared expert unchanged)

## [NCM Is this the End of LLMs?](../videos/vLqswKyHS64.md)
`vLqswKyHS64` · Kai Explains · 2026-10-20 · q4 · practitioner · review · also: models-research, local-ai, token-cost-efficiency

Kai Explains walks through the Stanford NCM paper (levels-based parallel text generation), separates its real single-stream gains from the hype, and argues memory bandwidth vs compute is the spec to watch for local AI.

- Techniques: Bandwidth-bound decode estimate; Minimum Bayes risk (MBR) decoding; Check speed claims at batch size 1 and at serving batch sizes; Coarse-to-fine residual code generation
- Tools: NCM (Next Concept Modeling, Stanford; GitHub repo with evaluation code and released models), Multi-scale residual VQ-VAE (compression network in NCM), Diffusion Gemma (Google DeepMind, June 10, 2026, Apache 2.0), Gemma (comparison word-by-word model, transcript reads 'Gemma 426B', likely a ~26B Gemma 4), Aurora LM (diffusion baseline in NCM paper), LADA 2.1 Mini (diffusion model with batch-size-1 benchmarks), Mercury (Inception diffusion LM), Meta Large Concept Models (Dec 2024, a different 'concept'), Hugging Face (model hosting), RTX 5090 (1792 GB/s), H100 (benchmark GPU for the 31x result), CUDA (required for NCM code)

## [Why Your Mac Is Slow at Local AI (And It's Not the Chip)](../videos/x_qmqqp6d7s.md)
`x_qmqqp6d7s` · Kai Explains · 2026-10-19 · q4 · practitioner · tutorial · also: local-ai, token-cost-efficiency, claude-code

Kai Explains on why local AI on a Mac feels slow: prompt prefill and prefix-cache misses, not memory bandwidth, dominate agent turns, and a settings checklist finds the cache-breaking causes.

- Techniques: Split prefill from decode when measuring; Audit cache-token counts per turn; Raise server log verbosity to find cache misses; Check Ollama's context window; Pin the Claude Code version and attribution header; Keep thinking tokens in history; Lower reasoning effort on Qwen models; Test frontends against the same server before committing
- Tools: Claude Code, Ollama, LM Studio, llama.cpp, Qwen 27B (dense model; spoken as 'Quen 27B'), Qwen 3.8 27B as spoken ('Quen 3.827B'; name likely garbled by captions, unverified), OpenClaw (agent frontend), Hermes (agent frontend), Xcode (passing example app), Apple M5 Max, M5 Pro, M5 chip, M4 Max, M1 Max (hardware), Mac Mini 'M6' (as spoken at 1:26; likely a caption or naming error, unverified)

## [Can 9 year old GPU beats today's latest GPUs?](../videos/eckOsa0kBkY.md)
`eckOsa0kBkY` · Kai Explains · 2026-10-19 · q4 · practitioner · review · also: local-ai, token-cost-efficiency, infra-cost-scaling

Kai Explains tests whether four 2017 Tesla V100s can beat 2025 DGX Sparks and RTX Pro 6000 boxes on local LLM inference; the answer is yes for decode speed, but the software and power economics are the real constraints.

- Techniques: Split inference cost into prefill and decode; Check interconnect before adding GPUs; Break-even math for owned GPUs versus hosted tokens; Pick a fork that still targets your hardware generation
- Tools: NVIDIA Tesla V100 (SXM2, Volta), NVIDIA DGX Spark (GB10, Blackwell, NVFP4), NVIDIA RTX 5090, NVIDIA RTX 5060, NVIDIA GTX 1080 Ti, NVIDIA RTX Pro 6000 Blackwell Server Edition, Qwen 3.8 Flash (model; the speaker gives it as a 125B model and also uses other names), vLLM, OneCat vLLM fork (v1.50, v1.5.1), V100 Skinny (community project built on OneCat), llama.cpp, NVFP4

## [Speech Recognition Without the Internet Now Fits on a $10 Chip (Whistle)](../videos/bavO_V80ohM.md)
`bavO_V80ohM` · Better Stack · 2026-10-19 · q3 · practitioner · tutorial · also: local-ai, voice-multimodal

Andres from Better Stack runs Cactus's 16.9 MB Whistle speech-to-text model fully offline on a $10 ESP32-S3, trimming decoder layers and quantizing math to fit and speed it up.

- Techniques: Decoder layer trimming for flash-constrained devices; Keyword biasing on a constrained command vocabulary; Confidence-gated retry in another language; Use short phrases, not single words, as voice commands; Microcontroller inference speedups; Push-to-talk with local feedback
- Tools: Whistle (Cactus Compute speech-to-text model, Apache 2.0, on Hugging Face), Needle / Needle 2 / Needle 3 (Cactus models, referenced from earlier videos), Cactus Compute inference engine, ESP32-S3 microcontroller (16 MB flash, 8 MB RAM, 240 MHz), INMP441 digital MEMS microphone, OpenAI WhisperBase (comparison model, 145 MB), LibriSpeech (benchmark test set), A terminal UI app that shows transcript, LED state and per-step timing (unnamed)

## [Local AI Hardware Just Got Way More Expensive Than You Think](../videos/Y226-wwfCSw.md)
`Y226-wwfCSw` · Kai Explains · 2026-10-19 · q4 · practitioner · review · also: local-ai, token-cost-efficiency

Kai argues local AI hardware got about 74% pricier in a year (DGX Spark, GPUs) through a memory shortage, while hosted open-weight tokens got cheaper, so buying to save on tokens rarely pays off now.

- Techniques: Token break-even calculation for a local box; Use the cheapest provider's price as the ceiling for open weights; Split work by model architecture: MoE hosted, dense local; Offload weights to system RAM with Strata; Sell-or-keep check for idle GPUs
- Tools: NVIDIA DGX Spark (GB10, 128 GB unified memory, 273 GB/s), NVIDIA RTX 5090, NVIDIA RTX 3090, NVIDIA RTX 3080, Framework desktop (128 GB), NVIDIA H100 (cited via SemiAnalysis benchmark), gpt-oss-120b, DeepSeek v4 Flash, DeepSeek v4.1 Flash, Qwen dense ~27B model (caption reads 'Quen 3.827B'), Strata, OpenRouter

## [Don't Buy a GPU Instead Build This 32GB Free AI Server Instead](../videos/IMVjEsKX5UQ.md)
`IMVjEsKX5UQ` · Kai Explains · 2026-10-19 · q4 · practitioner · review · also: local-ai, token-cost-efficiency

Kai tests the viral "free 32GB AI server" on Kaggle's two T4s and finds layer-split speed and slow prefill make it a lab, not a daily coder; the TPU VM option is the better free route.

- Techniques: Check whether a model fits per card before adding GPUs; Measure prefill (time-to-first-token) separately from tokens/s; Check proxy and tunnel timeouts against TTFT; Convert a free compute quota into tokens and dollars; Run a 27B model at full precision on Kaggle TPU VM; Audit launcher code and model provenance before giving tokens; Never rely on a URL as the secret for an Ollama endpoint; Expect URL churn on idle-killed notebook sessions
- Tools: Kaggle (notebooks, GPU and TPU accelerators), Nvidia Tesla T4, Google TPU VM (8 chips), Ollama, Cloudflare Quick Tunnel, Qwen3-27B (4-bit and full 16-bit), vLLM (TPU backend, 0.28.0), Kaggle TPU lab (GitHub project, MIT), Claude Code, Hermes (coding agent), OpenRouter, Cerebras

## [Qwen 3.8 27B Just Hit 200 Token/s on Mac M5 (Lithos Metal)](../videos/L7noXCBSObc.md)
`L7noXCBSObc` · Kai Explains · 2026-10-19 · q4 · practitioner · review · also: local-ai, evals

Dissects Lithos Metal's "200 tok/s" Qwen 27B claim on Apple M5 Max: a projection, with ~80 tok/s measured end-to-end. Speculative decoding helps on code, hurts on English, and agent sessions are prefill-bound.

- Techniques: Estimate decode ceiling from memory bandwidth; Speculative decoding with a small drafter; Measure acceptance rate alongside tok/s; Estimate whole-session time from prefill and decode rates; Time the whole task instead of quoting tok/s; Lower thinking-mode effort for local Qwen; Read the benchmark repo before the blog post
- Tools: Lithos Metal (engine, v0 Zero 1.2 mentioned), Qwen 3.8 27B (model, 4-bit), dSpark (speculative-decoding drafter, 1.1 GB), DeepSeek speculative decoding paper (July), MLX, MLX D-SPARK, Ollama, OMLX, D-Flash 2 (Z-Lab and Inco), Splash (Inco), MLTF (as transcribed), AgentPerfLocal (benchmark that replays agent sessions)

## [Every Way to Get 512GB of VRAM for Local AI (at Full Context)](../videos/6tihP50zlcE.md)
`6tihP50zlcE` · Kai Explains · 2026-10-19 · q4 · practitioner · review · also: local-ai, token-cost-efficiency

Compares hardware routes to 512GB for local LLMs, arguing KV-cache bytes per token, not file size, decides whether full context fits, with cost, speed and API break-even math.

- Techniques: Memory budget formula for local serving; Keep a lookup-table component on SSD (Engram-style); Leave allocation headroom on unified-memory nodes; Raise the Mac GPU memory limit, and re-check after reboots; Break-even check: owned hardware vs API; Rent before buying
- Tools: Muse Spark Open (Meta, 816B parameters), DeepSeek V4.1 Flash, DeepSeek API, GLM 5.3 (4-bit build), GLM 5.2, Kimi K3 (1.56TB download), DwarfStar (inference engine, originally by antirez), Apple Mac Studio M5 Ultra, Apple Mac Studio M3 Ultra, NVIDIA DGX Spark (GB10, 128GB), NVIDIA DGX Spark 64GB unit, NVIDIA RTX Pro 6000 Blackwell Max-Q (96GB)

## [2 Million TV Boxes Are Already Infected. AI Is Next.](../videos/OfNajAPiGsM.md)
`OfNajAPiGsM` · Better Stack · 2026-10-19 · q3 · intro · news · also: security-guardrails, models-research, local-ai

Better Stack walks through Anthropic's research on whether a small model could self-replicate across cheap IoT devices like TV boxes, and why the capability requirements don't yet overlap.

- Techniques: Pipeline-split a model across many weak devices; Separate the requirements of a dangerous capability and test each one; Give every model the same stand-in task for a fair comparison; Keep a remote brain, local hands
- Tools: Anthropic research (AI worm / self-replication study), Gemma 4 26B (Google open model), Qwen 3.5 9B, Llama 3.1 8B, GLM 5.2 (about 753B parameters), ADB (Android Debug Bridge), Google Cloud (8 Android test machines), Jetson Nano, NVIDIA RTX 4090, NVIDIA H100, Kimwolf botnet (transcribed as Kinwolf)

## [How I Got Frontier Performance on 16GB VRAM (Qwen 3.8 27B)](../videos/h_KqS4GtU3I.md)
`h_KqS4GtU3I` · Kai Explains · 2026-10-19 · q4 · deep · review · also: local-ai, token-cost-efficiency, models-research

Why a local Qwen 3.8 27B on a 16GB card often underperforms its leaderboard scores: the reasoning-effort setting, context window, and overthinking. Keep effort at xhigh, size the context to fit, and use the efficiency-tuned Swift 1.5 build.

- Techniques: Set reasoning effort on purpose, not to medium by default; Estimate the wall-clock cost of a reasoning run before starting; Work out the context budget before loading the model; Free GPU memory before loading the model; Turn on multi-token prediction; Use an efficiency-tuned build to cut thinking tokens; Check which setting a benchmark or guide actually used; Use hosted inference for long, parallel, or always-xhigh work
- Tools: Qwen 3.8 27B (transcribed 'Quen 3.827B'), Swift 1.5 (UQ AI retrain of Qwen 3.8 27B, IQ3 with MTP), llama.cpp, Hugging Face, Artificial Analysis Intelligence Index, GPQA Diamond, LiveCodeBench, SWE-Bench Pro, Terminal Bench 2.1, VulcanBench, ARC Prize, RTX 5060 Ti 16GB

## [Judge a Transaction by the Company It Keeps — Somya Rai & MD Sharique, EXL](../videos/SHvwutPSeZg.md)
`SHvwutPSeZg` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · also: models-research, governance-compliance

EXL engineers show a graph neural network feeding XGBoost for card fraud, lifting true-positive capture 27-33% at a fixed alert rate and serving it in about 3 ms P99.

- Techniques: Soft-target sampling that keeps graph connectivity; Disjoint time-window graphs for leakage control; Order-invariant multi-statistic neighbor aggregation; GNN embeddings as features for an existing gradient-boosted model; Entity-behavior deviation features; Layer-wise full-graph precomputation with a cached serving path; Edge-level prediction with entity-only embedding cache; Subgraph attribution for analyst-facing explanations; Latency hygiene for Python model serving
- Tools: XGBoost

## [Your GPU Neighbor Can Hear Your Model — Branislav Brzak, Stealthium](../videos/SacJfmp33vM.md)
`SacJfmp33vM` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: security-guardrails, sandboxing-execution

Timing alone on shared H100s leaks a neighbor's LLM: model depth, token speed and workload type, via MIG or NVLink. Mitigate with careful placement, host-side kernel monitoring, and no MIG co-location with untrusted tenants.

- Techniques: Timing probe on own memory; Frequency analysis of latency traces for model fingerprinting; Keep sensitive models off MIG slices shared with untrusted tenants; Host-side kernel-launch monitoring
- Tools: NVIDIA MIG, NVLink, NVSwitch, vLLM, speculative decoding, Qwen 8B, Llama 3 8B, DeepSeek R1 distill, GPT-OSS 20B, GLM 4.9B

## [Stop Renting Intelligence: The Train-to-Deploy Loop for Specialized AI — Fireworks AI](../videos/13YZ1EB9hjU.md)
`13YZ1EB9hjU` · AI Engineer · 2026-10-12 · q2 · intro · demo · also: training-finetuning-rl, product-ux

Fireworks AI talk on the train-to-deploy loop: moving from closed models to open-source models by fine-tuning (SFT, RFT, DPO) on the same platform used for hosting, with hot-loading and a training agent. Mostly a product pitch, with a few usable workflow ideas.

- Techniques: Continuous train-deploy-monitor-retrain loop; RFT with a vendor-built evaluator function; Training agent with plan approval gate; Draft model training for speculative decoding; Clone-and-compare training runs
- Tools: Fireworks AI platform, FireAttention, Weights & Biases, Qwen3 8B

## [This Open-Source Engine Claims 2x Faster Than llama.cpp](../videos/90itFOj7jfo.md)
`90itFOj7jfo` · Better Stack · 2026-10-12 · q3 · practitioner · review · also: local-ai, coding-agents

Hands-on test of Magnitude, a new Rust inference engine for Apple Silicon that tunes kernels per machine and targets agent workloads; the "2x llama.cpp" claim holds for one decode config but is mixed in independent tests.

- Techniques: Benchmark decode and prefill separately, and match KV-cache precision; Per-device kernel autotuning, cached per machine; Point Claude Code at a local Anthropic-compatible endpoint; Agent-serving cache and memory policy
- Tools: Magnitude (v0.2.5), llama.cpp, MLX, Ollama, Qwen 3.5 4B (Q8), Qwen 3.6 35B A3B (4-bit), Seismic (numerical compiler), Claude Code, Codex, OpenCode, RapidMLX, vLLM

## [Don't Buy a RTX Spark Laptop For Local AI Until You See This](../videos/aQKGejbv-Rs.md)
`aQKGejbv-Rs` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: local-ai, coding-agents

Pre-review critique of the RTX Spark / Surface Laptop Ultra for local AI: the cold-prefill wait on long prompts (about 170 s at 128K) matters more for agent work than decode speed, and the wattage is still unpublished.

- Techniques: Cold prefill benchmark at real context length; Split throughput into prefill and decode; Sustained and battery soak test; Memory budget with OS and tooling headroom; Speculative decoding for decode speed; Keep the prompt cache warm in long sessions
- Tools: Microsoft Surface Laptop Ultra, NVIDIA RTX Spark N1X, NVIDIA DGX Spark, Surface RTX Spark Dev Box, MAI Code 1.1 Flash (Microsoft coding model, 137B total / 6.8B active MoE, about 53 GB compressed), llama.cpp (Windows on ARM build with CUDA; transcribed as 'Lama CPP'), DFlash 2 speculative decoding (transcribed as 'DF Flash 2'), GitHub Copilot, Windows 11, NVIDIA Linux (DGX Spark), AMD Ryzen AI Max Plus 395, ASUS ROG Flow Z13

## [This 125B AI Model Runs 5x Faster on My PC Than in the Cloud (Using Strata)](../videos/vrVaGp_YmQY.md)
`vrVaGp_YmQY` · Better Stack · 2026-10-12 · q3 · practitioner · review · also: local-ai, token-cost-efficiency

Tests Strata, an open-source runner that spreads a 125B Qwen MoE across RTX 5090 VRAM, system RAM and SSD, against the cloud-hosted model; local is 3-5x faster on short tasks, with caveats.

- Techniques: Tiered expert placement for MoE models larger than VRAM; Per-layer GPU/CPU handoff through shared memory; Speculative decoding with the model's own small helper; Local install and first run (as shown); Fair side-by-side latency comparison of local vs cloud
- Tools: Strata (free, open-source local MoE runner; the paper is referenced but not named), Qwen 3.8 Flash (Next), 125B-parameter MoE; transcript spells it 'Quen', OpenRouter (hosted Qwen 3.8 Flash endpoint used for the cloud comparison), NVIDIA RTX 5090 (32 GB VRAM, test machine), NVIDIA RTX 5070 (12 GB, referenced from the Strata README only), Intel Core Ultra 9 285K (test machine CPU), Speaker's own side-by-side comparison app (speed, time and cost tracking; not named), Python (language for the palindrome test prompt)

## [Every Ways to Get 128GB VRAM for Local AI at Full Context](../videos/NA9D49kQFuU.md)
`NA9D49kQFuU` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: local-ai, token-cost-efficiency

Kai's buyer's guide to reaching 128GB of memory for local AI: prices every route, shows that expert offloading and the inference engine matter more than raw pool size, and ends with per-budget recommendations.

- Techniques: Expert / lookup-table offloading for large sparse models; Benchmark prefill and decode separately at real context length; Raise the GPU-addressable memory limit before loading; Quantization ladder by available memory; Draft-ahead decoding for speed on DGX Spark-class hardware; Rent-vs-buy break-even check
- Tools: Qwen Flash Next (as transcribed; 4-bit, 3-bit, 2-bit builds), Qwen 3.8 27B (as transcribed), Strata (inference engine, offload-capable), Gufo (community fork of an inference engine), Halogen (closed-source inference engine), MLX serve (Mac inference engine), llama.cpp, vLLM (implied by the RTX 5090 setup context only if mentioned; not named in transcript), CUDA, Linux kernel flags (mentioned, not specified), AMD Ryzen AI Max Plus 395 (Strix Halo), AMD Ryzen AI Max Pro 495 (192GB)

## [Same Model, Different Speed: Why Your Inference Provider Matters — FriendliAI](../videos/_naLJOqVOEI.md)
`_naLJOqVOEI` · AI Engineer · 2026-10-12 · q2 · intro · talk · also: infra-cost-scaling, models-research

A FriendliAI engineer argues open-weight models now rival frontier ones, so the inference provider's speed, reliability and cost decide the outcome. Covers prefix-cache routing, tiered KV cache and hybrid speculative decoding. Mostly a sales pitch.

- Techniques: Cache-aware request routing; Tiered KV cache offload; Hybrid speculative decoding; Provider bake-off on your own workload
- Tools: OpenRouter (provider stats snapshot), Code Arena leaderboard

## [Taming the AI Hardware Cambrian Explosion — Abdul Dakkak, Modular](../videos/7BcQdtRA3Tc.md)
`7BcQdtRA3Tc` · AI Engineer · 2026-10-12 · q2 · intro · talk · also: infra-cost-scaling

Modular's pitch for a single portable stack (Mojo language, MAX inference engine, Modular Cloud) across NVIDIA, AMD and other accelerators, backed by vendor-run speed and cost benchmarks.

- Techniques: Heterogeneous prefill/decode split; Price-normalized hardware comparison; Portable kernel development with an open benchmark; AI-assisted porting of kernels; Tuning serving parameters on a Pareto frontier
- Tools: Mojo, MAX, Modular Cloud, vLLM, SGLang, TensorRT-LLM, llama.cpp, PyTorch, Triton, CUDA, ROCm, OpenCL

## [Turning My Obsidian Vault Into a Local AI Engineer — Filip Makraduli, Superlinked](../videos/Ndp5VaqFrl0.md)
`Ndp5VaqFrl0` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: local-ai, mcp-and-tools, security-guardrails

Filip Makraduli (Superlinked) shows a privacy-first setup: a self-hosted MCP tool server runs OCR, redaction and extraction on sensitive documents in your own cloud, so a Claude Code agent only sees the cleaned output.

- Techniques: MCP tool server in front of private inference; Per-worker batching instead of a shared queue; Multi-model hot-swapping on one GPU; Stateless tools-only MCP server over streamable HTTP; Check thinking-token settings per model in tool pipelines; Warm-model-aware routing (roadmap)
- Tools: MCP, Claude Code, Obsidian, Superlinked, Terraform, Helm, Kubernetes, Docker, Claude Co-work

## [AI Apps in a Flash: Ship to GPUs Without Docker — Dean Quiñanola, Runpod](../videos/XczFLWEntiE.md)
`XczFLWEntiE` · AI Engineer · 2026-10-12 · q2 · intro · demo · also: infra-cost-scaling, dev-tools

RunPod's Dean Quiñanola demos RunPod Flash, a Python-first way to run and deploy GPU functions on serverless endpoints without writing a Docker image; the main takeaway is that the Docker build-push loop is the bottleneck for AI app iteration.

- Techniques: Docker-free function iteration with a local dev server; Dependencies installed at worker start-up instead of baked into an image; Endpoint-to-endpoint function calls; Network volumes for warm caches across scale-ups; Teardown of dev endpoints on cancel; Spreadsheet-driven experiment fan-out
- Tools: RunPod Flash, RunPod serverless endpoints, Docker, Docker Hub, FastAPI, PyTorch, Hugging Face, Python, GitHub

## [OpenRouter is Quietly Giving Nerfed AI Model (STOP Using Wrong Endpoint)](../videos/ZsnFX5mEJ4s.md)
`ZsnFX5mEJ4s` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: infra-cost-scaling, token-cost-efficiency

Kai argues that OpenRouter "nerfed model" complaints are mostly not quantization. The real causes are price-sorted provider routing, silent context and output caps, tool-call failures and cache pricing. Fix them by pinning providers and logging which endpoint served each request.

- Techniques: Pin trusted providers with provider.order; Require supported parameters and set max_tokens explicitly; Set a precision floor with quantizations; Leave tool-call requests on default AutoExacto; Audit the served provider per request; Check endpoint caps before choosing a provider; Rank providers by effective cost, not listed price
- Tools: OpenRouter, DeepSeek V4 Pro, DeepSeek V4.1 Flash, Kimi K3, GLM 5.2, GLM 5.3, GLM-5, GPT-OSS-120B, Llama 3.3 70B, Novita, DeepInfra, Together

## [Is 16GB All You Need for Serious Local LLM?](../videos/i9mRnbdDYxk.md)
`i9mRnbdDYxk` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: local-ai, token-cost-efficiency

Kai Explains argues a 16GB GPU fits a 27B model but can't finish real agentic coding sessions: the KV cache, bandwidth, prefill and multi-token prediction decide usable speed and context, not whether the weights load.

- Techniques: VRAM budget before loading a model; Reclaim memory from defaults; Turn multi-token prediction off past a context threshold; Size the model to the conversation; Measure prefill and decode separately; Local-vs-hosted break-even; Tensor split for two cards
- Tools: llama.cpp (called 'Lama CPP' in captions; the speaker calls it the most common local AI runtime), Qwen 27B-class model (captioned 'Quen 3.827B'; Q4 at 17.44 GB, a DASLab GSQ build at 11.8 GB), GSQ quantization (DASLab, IST Austria), Devstral Small 2 (captioned 'DevStraw Small 2'; 160 KB KV per token), Claude Code (captioned 'CloudCode'), OpenRouter (hosted price benchmark), Nvidia RTX 5060 Ti 16GB, Nvidia RTX 5070 Ti, Nvidia RTX 5090, AMD RX 9060 XT 16GB, AMD RX 9070 XT, Apple Mac mini (chip name garbled in captions)

## [Agents That Own Their Inference — Du'an Lightfoot & Khaja Omer, Akamai Technologies](../videos/4n08JHb90hI.md)
`4n08JHb90hI` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: local-ai, infra-cost-scaling, evals

Akamai hands-on workshop on self-hosting LLM agents on a single GPU with vLLM: memory budgets, prefill vs decode, FP8 quantization, speculative decoding, and finding the concurrency knee.

- Techniques: Memory budget math; Concurrency sweep to find the knee; One-flag-at-a-time tuning; Quantize with your own eval set; Validate speculative decoding by acceptance rate; Prefix caching for repeated context; Own-vs-rent break-even
- Tools: vLLM, Kubernetes, LKE (Akamai Linode Kubernetes Engine), KServe, SGLang, TensorRT-LLM, llama.cpp, Ollama, Prometheus, Grafana, Langfuse, LLM Compressor

## [How Inference Keeps Up with Our Insatiable Need for Tokens — Cerebras & Gimlet Labs](../videos/_cRgl3maiT8.md)
`_cRgl3maiT8` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: infra-cost-scaling

Cerebras and Gimlet Labs walk through LLM inference optimizations, from paged KV cache and chunked prefill to prefill/decode and attention/FFN disaggregation across mixed hardware, plus agent-generated GPU kernels.

- Techniques: Paged KV cache; Prefix / prompt caching; Chunked prefill; Prefill/decode disaggregation; Speculative decoding; Attention/FFN disaggregation; Agent-driven kernel search
- Tools: Cerebras CS3, AWS Trainium, AWS EFA, NVIDIA H100, AMD GPUs, Kforge (Gimlet agent for kernel generation)

## [How MiniMax M3 Was Built: Sparse Attention and Native Multimodality — Olive Song](../videos/htod7Nv1cBc.md)
`htod7Nv1cBc` · AI Engineer · 2026-10-11 · q4 · practitioner · talk · also: models-research, voice-multimodal

MiniMax's Olive Song explains how M3 adapts DeepSeek-style sparse attention to GQA with per-KV-head block selection, and why it was trained on vision and text from step zero.

- Techniques: Index-branch sparse attention; Per-KV-head selection under GQA; Block-level retrieval instead of token-level top-k; Native multimodal pretraining from step zero; Attention-map check for modality fusion; 3D attention in the ViT with a frame cap
- Tools: MiniMax M3, MSA (MiniMax Sparse Attention), DeepSeek DSA

## [Is Speculative Decoding Worth It? Profiling vLLM on NVIDIA Blackwell — Akamai](../videos/XTpyNrEgJQ4.md)
`XTpyNrEgJQ4` · AI Engineer · 2026-10-07 · q3 · practitioner · demo · also: infra-cost-scaling

Akamai's Sheila explains when speculative decoding pays off on vLLM: spare GPU memory and structured, low-temperature workloads, measured by acceptance rate and tokens/s on a single Blackwell GPU.

- Techniques: Draft-model speculative decoding; Acceptance-rate-first benchmarking; Draft model selection checklist; Side-by-side A/B on one GPU; Workload triage before enabling
- Tools: vLLM, Llama 70B, NVIDIA Blackwell GPU, EAGLE, Medusa, n-gram speculative decoding

## [What Is an Inference Engine, Anyway? — Charles Frye, Modal](../videos/woIYJYd_etI.md)
`woIYJYd_etI` · AI Engineer · 2026-10-06 · q4 · deep · workshop · also: observability, infra-cost-scaling

Charles Frye (Modal) explains what runs inside an LLM inference engine: workloads, prefill vs decode, process layout, scheduler bottlenecks, KV cache, CUDA graphs, speculative decoding, and production debugging.

- Techniques: Phase-split serving metrics; Keep host work off the GPU critical path; Speculative decoding with exact-output verification; Prefix and radix KV-cache reuse; Treat queueing and cache thrash as alerts; Correctness logging and post-deploy evals; Profile for per-GPU or per-host anomalies
- Tools: SGLang, vLLM, TensorRT-LLM, PyTorch, Hugging Face transformers, FlashAttention, FlashInfer, CUTLASS, Triton, DeepGEMM, DeepEP, Marlin

## [Every Ways to Get 32GB VRAM for Local AI at Full Context](../videos/uavLRbbfM94.md)
`uavLRbbfM94` · Kai Explains · 2026-10-05 · q4 · practitioner · review · also: local-ai, token-cost-efficiency

A buying guide for getting 32GB VRAM for local AI at full context: why 27B dense at 6-bit plus 128K context needs about 28.5GB, which cards and engines actually deliver, and when renting beats owning.

- Techniques: VRAM sizing before buying; Check the engine's startup log for usable memory; Two-card tensor split; Multi-token prediction; Speculative decoding on a patched vLLM build; Rent-vs-own break-even; Full-cost comparison for a GPU purchase
- Tools: Qwen 27B-class dense model (captioned as Quen 3.827B), 6-bit quantization, llama.cpp (default engine, with layer and tensor split modes and multi-token prediction), LM Studio (beginner frontend), vLLM and community forks: vLLM Radiance, a Ninfer/Eninfer V100 fork, OneCat VLLM (captioned names), ROCm (AMD) and CUDA 12 / CUDA 13 (Nvidia), GGUF model files, macOS unified memory on Mac mini, RunPod (rented RTX 5090), OpenRouter (hosted Qwen pricing), Vast.ai (rental pricing listing), Digital Spaceport GPU price tracker, RepoChat GPU comparison

## [Deepseek & Huawei Made Local AI Run Without NVIDIA's CUDA (And Why it's Hard)](../videos/uJcPjrEgppk.md)
`uJcPjrEgppk` · Kai Explains · 2026-10-05 · q4 · practitioner · news · also: models-research, local-ai

DeepSeek's Ascend kernel release looks like a CUDA challenger, but its 99.8% figure measures efficiency against Huawei's low ceiling; the stack still depends on Huawei's runtime and the hardware is not yet available.

- Techniques: Read utilization numbers against their denominator; Drop-in kernel swap via identical package/import names; Check hardware provenance and license footnotes before depending on a release; Pin runtime versions to the vendor stack the kernels require
- Tools: DeepGEMM, FlashMLA, DeepEP, TileKernels, TileLang, Apache TVM, CANN 9.2.0, vLLM, llama.cpp, NVCC, CUDA, Ascend 950DT

## [The New Way to Run 125B Models 6× Faster Than llama.cpp (Strata)](../videos/m0VHx73SAG0.md)
`m0VHx73SAG0` · Kai Explains · 2026-10-05 · q4 · practitioner · review · also: local-ai, token-cost-efficiency

Review of Strata, a new engine that runs a 125B-parameter MoE model on a 12 GB GPU plus 64 GB RAM. The headline "6x" is inflated; the honest gain is about 2 to 2.5x, with a quality trade-off and a real RAM cost.

- Techniques: Hot-expert GPU cache with CPU cold path; Use multi-token prediction with a trained draft head; Keep big embedding tables on SSD and read only the rows needed; Choose quantization by workload; Tune the host before blaming the engine; Benchmark speed claims fairly; Point a coding agent at a local Anthropic-compatible endpoint
- Tools: Strata (v0.1, GitHub, launched Sept 24; one-click Windows installer or Linux script), llama.cpp (including the multi-token-prediction merge on Oct 1 and the expert-cache draft PR open since Aug 28), Qwen 3.8 Flash Next (125B total, ~6B active; 2-bit Q2, 3-bit IQ3 and full-precision builds), Qwen 3.8 27B (comparison model), Qwen4 (mentioned as the next architecture, not tested), Claude Code (pointed at the local endpoint), LiveCodeBench (benchmark), SWE-Bench Pro (benchmark), NVIDIA RTX 5070 (12 GB), RTX 5090 (32 GB), RTX 3090, DDR5-6000 / DDR4 system RAM, Tom's Hardware price index, LocalLLaMA forum

## [Lessons from Generating 12 Trillion Synthetic Tokens — Bogdan Gaza, DatologyAI](../videos/FQwTqUmcbRg.md)
`FQwTqUmcbRg` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: data-engineering, training-finetuning-rl, infra-cost-scaling

Datology's CTO on running trillion-token synthetic pretraining data jobs: rephrase seeded documents, batch S3 metadata calls, checkpoint for GPU failures, schedule CPU and GPU pools atomically, and sweep vLLM flags.

- Techniques: Seed-based document rephrasing for synthetic pretraining data; Batched S3 metadata listing at maximum page size; Right-sized partitions with checkpointing and idempotent retries; Atomic CPU and GPU scheduling with dedicated pools; Grid search over vLLM and SGLang serving parameters for batch inference; One workflow for research and product in the same infrastructure
- Tools: Ray, KubeRay, vLLM, SGLang, Apache Spark, Kubernetes, Amazon EKS on HyperPod, Slurm, Amazon S3, Parquet, Beyond Web (DatologyAI synthetic data recipe), Nemotron Synth

## [GPU Died. Training Didn't: Self-Healing Training at Scale — Crusoe](../videos/bRGyYaE0lxI.md)
`bRGyYaE0lxI` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: infra-cost-scaling, training-finetuning-rl

Crusoe engineers explain how they run Slurm on Kubernetes so failed GPU nodes are cordoned, replaced and the training job resumes from checkpoint with no user action, with a live demo.

- Techniques: Automated GPU failure remediation loop; Opt-out label check before node replacement; Checkpoint on SIGTERM grace window; Slurm operator on Kubernetes (Slinky pattern); Shared GPU pool across training and inference
- Tools: Slurm, Kubernetes, Slinky (SchedMD), sbatch, srun, PyTorch, Crusoe Managed Kubernetes (CMK), Crusoe AutoClusters, Crusoe Slurm operator

## [What Makes Open Models Fast in Production — Sujee Maniyam, Nebius](../videos/TRe1u7dHYiA.md)
`TRe1u7dHYiA` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: infra-cost-scaling

Nebius Token Factory explains the serving optimizations behind fast open-model inference: cache-aware routing, speculative decoding, KV-cache offload, and prefill/decode separation. It is mostly a product pitch with few measured results.

- Techniques: Cache-aware request routing; Speculative decoding with a self-trained draft model; KV-cache offload to host memory; Prefill/decode disaggregation; Per-model engine and precision selection
- Tools: Cursor, OpenCode

## [Is Frontier Class Local AI Finally Possible?](../videos/1--PzaHafAU.md)
`1--PzaHafAU` · Kai Explains · 2026-10-02 · q4 · practitioner · news · also: local-ai, models-research, token-cost-efficiency

Frontier-class open-weight models can now run on consumer hardware by moving a lookup table to SSD, but prefill speed and rising hardware prices limit local use to batch work rather than interactive agents.

- Techniques: Split latency into prefill and decode when judging local hardware; Budget SSD-offloaded parameters by bytes-touched-per-token; Batch local, interactive hosted; Verify a quantized build against the official weights; Check the prefill number and the memory floor before buying
- Tools: Qwen (Flash Next, Qwen 4 architecture preview), DeepSeek V4 Pro, DeepSeek V4 Flash, Kimi K3, Unsloth (1-bit quantized builds), llama.cpp (SSD offload support, per community report), Claude Code (system prompt size cited), NVIDIA RTX 3060, NVIDIA RTX Pro 6000 Blackwell, NVIDIA H100, NVIDIA 4xH200 (hosted comparison), NVIDIA DGX Spark

## [Xiaomi & DeepSeek Just Solved the Biggest Bottleneck in Your Local AI](../videos/RlRC_6hbBHc.md)
`RlRC_6hbBHc` · Kai Explains · 2026-10-02 · q4 · practitioner · news · also: token-cost-efficiency, local-ai, models-research

Explainer on DeepSeek V4.1 Flash and Xiaomi HiSparse 2, two independent designs that split a model so the bottom half reads the prompt once; the real gain is cheaper reading (prefill), not memory, and recall is not yet proven.

- Techniques: Cross-layer KV sharing (YOCO-style split); Split input-token cost into cache-hit and cache-miss; Benchmark prefill tok/s and time-to-first-token at 100k and 1M; Run a recall test before trusting long context; Trim large tool output before it enters context (inferred, not stated in video)
- Tools: DeepSeek V4.1 Flash, HiSparse 2 (Xiaomi), MIMO v3 (Xiaomi's next model, per Luo Fuli), YOCO (You Only Cache Once, Microsoft Research and Tsinghua, May 2024), Grouped query attention (referenced), Qwen (smaller model grafted by a LocalLLaMA user), Apple M3 Ultra (512 GB, local benchmark), KV cache

## [Why DeepSeek Ditched Its Own Flagship (And Then Didn't)](../videos/u00vNoI2iQc.md)
`u00vNoI2iQc` · Kai Explains · 2026-10-02 · q3 · practitioner · news · also: token-cost-efficiency, models-research, infra-cost-scaling

Kai Explains on DeepSeek briefly retiring V4 Pro for V4.1 Flash, reversing within a day, and why agent teams should cost-model and test their own prompts before switching models.

- Techniques: Cost agent turns by cache-hit vs cache-miss input; Pin model identifiers and track vendor changelogs; Run candidate models on your own traffic before switching; Route by task type across model tiers; Use concurrency limits as a capacity signal in model choice; Rank models by cost per solved task
- Tools: DeepSeek V4 Pro, DeepSeek V4.1 Flash, DeepSeek V4.1 Pro (named as roadmap, not released), Claude Opus 5, GPT 5.6 Sol, DeepSWE benchmark (as captioned), Humanity's Last Exam, ProgramBench, Terminal Bench (hardest version), Cybergym, GitHub issues (developer feedback channel)

## [DeepSeek Just Shrunk the KV Cache 437×](../videos/n-_e9bROGHo.md)
`n-_e9bROGHo` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: token-cost-efficiency, local-ai, models-research

Kai rebuilds DeepSeek's "437x smaller KV cache" ratio from config files, shows the denominator compares a 2023 dense model to a 2026 MoE, and explains how sparse layers and 4-bit storage cut per-token cache cost.

- Techniques: Compute KV bytes per token from the model config; Normalise cache comparisons to the same generation and to the same max context; Size node concurrency as free HBM divided by per-session cache; Separate the single-user and multi-user cost models; Check the failure modes of sparse selection and replay; Track output tokens separately from input tokens
- Tools: DeepSeek V1 (dense, grouped-query attention, 4,096 context per speaker), DeepSeek V4.1 Flash (sparse MoE, 40 layers, 1M context, 4-bit experts), DeepSeek V4 Flash (predecessor to V4.1 Flash), DeepSeek V4 Pro (flagship; reversed retirement per speaker), DeepSeek V3 (671 GB at 8-bit, 163,840-token limit), Hugging Face (config files), NVIDIA H200 SXM (141 GB HBM3E per card, 8-card node), Apple M5 Ultra Mac Studio (512 GB), Mac mini (16 GB, SSD weight streaming in developer test), Artificial Analysis (benchmark for output tokens per second)

## [This Tiny Coding Model Shouldn’t Be This Good (MiniCPM5)](../videos/Wik_JQ-enUA.md)
`Wik_JQ-enUA` · Better Stack · 2026-10-02 · q4 · practitioner · review · also: local-ai, evals, models-research

Review of OpenBMB's 2B MiniCPM5: strong on agent and tool benchmarks against Qwen 3.5 4B, but quantized GGUF runs loop under the documented llama.cpp defaults until min_p and repeat penalty are changed.

- Techniques: Run a small model on a Mac with MLX in a virtualenv; Tool-calling smoke test against a local OpenAI-compatible server; Fix the quantized sampler before judging a small model; Count runaway generations, not just pass rate; Load a GGUF into Ollama or LM Studio without a library entry
- Tools: MiniCPM5 2B (text-only, OpenBMB), MiniCPM5 1B, MLX / mlx-lm, llama.cpp (server), GGUF, OpenAI-compatible client, WebLLM, Ollama, LM Studio, Hugging Face, Qwen 3.5 (2B and 4B), Gemma 4 E2B

## [What It Actually Costs to Run Xiaomi MiMo V2.6 Pro & Flash Locally?](../videos/3hMEcJCGne0.md)
`3hMEcJCGne0` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai, token-cost-efficiency, models-research

Why running Xiaomi MiMo V2.6 Pro/Flash locally rarely beats the API on cost: weights already 4-bit, bandwidth caps speed, electricity alone outprices hosted tokens. Only privacy or speed justify it.

- Techniques: Check whether a release is already quantized before quantizing; Estimate the decode speed ceiling from memory bandwidth; Compare local vs API on electricity and break-even before buying hardware; Raise the output cap for reasoning models and turn sampling back on; Measure prefill and decode separately for long contexts
- Tools: Xiaomi MiMo V2.6 Pro, Xiaomi MiMo V2.6 Flash, Xiaomi MiMo V2.6 Distilled (9B), DeepSeek V4.1 Flash, MLX (Apple), llama-bench (llama.cpp), NVIDIA DGX Spark, AMD Ryzen AI Max (Framework desktop), Apple Mac Studio M5 Ultra / M3 Ultra, AMD EPYC (12-channel DDR5 server), NVIDIA RTX Pro 6000, NVIDIA RTX 3060 (12 GB)

## [Don't Buy a Local AI Hardware Until You See This](../videos/L4UV6b2Xc64.md)
`L4UV6b2Xc64` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai, token-cost-efficiency

Argues local AI hardware is mispriced: resale value, bandwidth per dollar, prefill latency, idle power and break-even against hosted tokens all matter more than list price or capacity.

- Techniques: Bandwidth per dollar and capacity per dollar as separate metrics; Break-even against hosted tokens; Measure prefill separately from decode; Resale liquidity check; Idle power cost
- Tools: NVIDIA DGX Spark, Framework desktop (Ryzen AI Max, unified memory), Apple Mac Studio M3 Ultra (512GB), NVIDIA RTX 3090, NVIDIA RTX 3080, NVIDIA RTX 3070, NVIDIA RTX 4090, NVIDIA RTX 4070, NVIDIA RTX 5090, NVIDIA RTX 5080, NVIDIA RTX 5060, NVIDIA RTX 3060

## [Is 8GB VRAM enough for 27B models? Tested](../videos/P1K36q76Uzk.md)
`P1K36q76Uzk` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai, models-research, token-cost-efficiency

Kai reviews Prism ML's Bonsai 2 (a 27B model compressed to about 1.75 bits per weight, 5.95 GB). The memory win is real, but the vendor's headline numbers hide reasoning-time, agentic and loader problems.

- Techniques: Blockwise Hadamard rotation before ternary rounding; Compare compressed models against the baseline you actually run; Measure long-context generation speed, not TG128; Verify local model loads before trusting output; Keep reasoning effort at default for routine prompts; Supported install path (as stated; repo name not given)
- Tools: Bonsai 2 (Prism ML 27B ternary model, 'Bonsai 227B' in auto-captions), Qwen 3.8 27B (base model, Apache 2.0), llama.cpp (named as 'StockLama CPP' in captions), Ollama (GGUF parser; unofficial Bonsai upload on registry), MLX loaders, Prism ML fork (build B10658 or newer, as transcribed), Q4 / UDQ4 GGUF builds (about 17.6 GB), IQ2 2-bit 27B build, Terminal Bench 2.1, SWE-bench Verified, AIME26 (AIME-style math), IFBench

## [Can a Mac Mini Replace your $200 AI Subscription?](../videos/3R7yba577uA.md)
`3R7yba577uA` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai, token-cost-efficiency

Kai argues a $1,299 Mac Mini cannot replace a $200 coding-agent subscription: it only matches the model, not the hosted reading speed or usage allowance, and at per-token prices its output is worth about $19 to $190 a month.

- Techniques: Decode throughput ceiling check; Prefill budget for agent prompts; Prefix caching accounting; Monthly break-even formula; Hybrid orchestrator with cheap hosted subtasks; Usage audit before plan change; Speculative decoding (conceptual); Memory sizing with OS headroom
- Tools: Qwen 3.8 27B (captioned 'Quen 3.827B'; Apache 2.0, about 16.05 GB compressed build), Qwen 3.6 35B-class model (captioned 'Quen 3.635B'; the speaker says it is an older small model), Opus 5.0, Opus 5.5, Fable 5.1, GPT-6, GPT 5.6 Sol, Claude Code, Claude sessions (Anthropic cloud, launched with a $250 introductory credit on Macs per speaker), Codex, OpenClaw, Hermes (agent setups named as the driver of Mac Mini demand)

## [Is it Possible to Run Any LLM in Jev Mode Using llama.cpp?](../videos/Oi4JPj58lUA.md)
`Oi4JPj58lUA` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai, evals, data-engineering

Breakdown of "Jeff mode": llama.cpp constrained choice scoring is fast, but its confidence score comes from masking and renormalizing, needs calibration on your own data, and its speed depends on model architecture.

- Techniques: Forced-choice classification via cached-prompt branch scoring; Single-field logprob check on the stock server first; Calibrated confidence gate with escalation; Temperature scaling for post-hoc calibration; Group requests by schema to keep the prompt cache warm; Benchmark hygiene for local inference; Keep dependent fields in plain generation
- Tools: Jeff (TypeSafe structured-classification product, as captioned; the title spells it 'Jev mode'), llama.cpp, llama.cpp fork by Kodakus (parallel constrained decoding, two commits), llama.cpp stock server (n_probs / logprobs parameters), NotJeff (project reproducing the approach with stock llama.cpp, Qwen3-8B reported), Qwen 1.5B (plain attention, 28 layers), Qwen3-8B (captioned 'Quen38b'), Qwen 3.6 35B-A3B (captioned 'Quen 3.635BA3B', MoE), Gemma 4 12B (captioned 'Gemma 412b', sliding-window), Insider LLM 27B model (described as dense; config shows hybrid), Banking77 (public bank-intent dataset), Temperature scaling (calibration method)

## [The End of VRAM-Bottlenecked LLMs: Qwen3.8-Flash-Next](../videos/MPrQA-M4Zn4.md)
`MPrQA-M4Zn4` · Kai Explains · 2026-10-02 · q4 · deep · news · also: local-ai, models-research

Qwen's Flash-Next model stores a 51B n-gram embedding table that can sit in system RAM and be prefetched, so local model fit depends on host RAM vs table size, not VRAM alone.

- Techniques: Deterministic lookup-table offload to host RAM with asynchronous prefetch; Host-RAM-first sizing check for a local model; Context-sweep benchmark for offload tax; KV-cache budget from bytes per token; Support-status checklist before adopting a fork
- Tools: Qwen 3.8 Flash Next (Qwen model; config self-identifies as Qwen4 experimental), DeepSeek Conditional Memory via Scalable Lookup (paper, January), vLLM (official recipe, opt-in host offload env var), llama.cpp (PR 27742, fork only), MLX (external table storage, unreleased PR), Unsloth (one-bit dynamic build), NVIDIA DGX Spark, RTX 4090, RTX 5090 (ruled out by the official vLLM recipe), NVFP4, Muon optimizer (vs AdamW), Gated delta net (hybrid attention)

## [I Tested Every Local AI Model So You Don't Have To](../videos/C9M6iUFtVB4.md)
`C9M6iUFtVB4` · Kai Explains · 2026-10-02 · q3 · practitioner · review · also: local-ai, token-cost-efficiency

Local-model buying guide by GPU tier: context budget (KV cache) and read speed matter more than which model you pick. Covers quantization pitfalls, two free speed settings, and when renting beats owning.

- Techniques: Budget the KV cache per context length, not just model size; Set the context window explicitly; Cut harness overhead before the first prompt; Enable multi-token prediction; Use medium reasoning effort instead of the max default; Vet quantized builds on your own tasks; Run a mixture-of-experts model with experts offloaded to RAM on 8 GB cards; Split planning from execution across frontier and local models; Track prefill (read) speed separately from generation speed
- Tools: MCP, Mistral 24B (unnamed variant), Apple Silicon, Mac Studio, Reddit

## [Don't Buy a Mac Mini For Local AI (Do This)](../videos/IRyiP_U7RuA.md)
`IRyiP_U7RuA` · Kai Explains · 2026-10-02 · q3 · practitioner · review · also: local-ai, models-research

Kai Explains argues that buying a Mac Mini for local AI is a poor first move: size memory for the model you actually run, switch inference servers and measure time-to-first-token, and rent the model for a month before buying.

- Techniques: Measure end-to-end latency (time to first token + generation), not just tokens/s; Swap the default local inference server before buying hardware; Prefer sparse MoE models for local inference; Size memory for the model you run today, plus KV cache headroom; Rent the model for a month before buying hardware
- Tools: Apple Mac Mini (M6, M5 Pro), Apple Mac Studio (M5 Max, M5 Ultra), Framework Desktop (Ryzen AI Max), NVIDIA DGX Spark, NVIDIA RTX 5090, gpt-oss-120b, Mixture-of-experts 35B model (unnamed), Dense 27B model (unnamed), Apple machine learning research post (cited for bandwidth-bound token generation)

## [How AI Got Smaller And Still Became Smarter](../videos/LqAxNIalgOw.md)
`LqAxNIalgOw` · Kai Explains · 2026-10-02 · q4 · practitioner · news · also: local-ai, token-cost-efficiency, models-research

Walks through why "smaller" AI models are not cheaper to run locally: active parameters cut compute but not memory, KV cache grows per token, and reasoning-effort defaults inflate cost; benchmarks also mix setups.

- Techniques: Estimate KV cache memory from config before loading a long-context model; Lower the reasoning-effort preset to cut thinking tokens; Read benchmark footnotes for harness and settings before comparing; Separate active and total parameters when sizing MoE models
- Tools: Qwen3.6-27B (Alibaba, 27B dense-active MoE claim, 262K context), Qwen Flash Next (180B total, 6B active), DeepSeek (budget model, 284B to 552B backbone), Claude Opus, GPT-5.5 Codex, Terminal Bench 2.1, SWE-Bench Pro, GPQA Diamond

## [Mac Studio vs AMD AI PC: Don't Buy Before Watching This](../videos/dlyic4oco4s.md)
`dlyic4oco4s` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai, infra-cost-scaling

Mac Studio M5 vs Ryzen AI Max+ 395 for local AI: prefill, not tokens/sec, dominates wait time, MoE models shrink Apple's lead, and cheap AMD mini PCs can be misconfigured traps.

- Techniques: Measure prefill and decode separately, at your real context length; Pick hardware by model architecture; Check that the GPU math library is actually in use; Tune the AMD unified-memory box (documented steps as described); Run a constellation of small resident models under an orchestrator; Vet mini-PC SKUs before buying; Use newer open-source attention kernels on the AMD iGPU
- Tools: Mac Studio M5, Apple M5 Ultra, Apple M5 Max, Apple M4 Max, Apple M1 Max, AMD Ryzen AI Max Plus 395, Framework Desktop, Minis Forum MS-S1 Max, Gemma 4 (12B, dense), gpt-oss-120b (~116B total, ~5.1B active), Qwen 3.6 (35B-class MoE, about 3B active), a 122B model (name not given)

## [Qwen 3.8 27B Just Got 2× Faster on Mac Same Hardware](../videos/qZTmBhKz7b0.md)
`qZTmBhKz7b0` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai, evals

A debunk of the "Qwen 3.8 27B 2x faster on Mac" headline: the 2x comes from speculative decoding with a 1.2 GB draft model, not the Splash engine, and the built-in multi-token-prediction head gives smaller gains for free. Measure effective tokens/s with warm and cold cache, not decode speed.

- Techniques: Measure effective tokens per second, cold and warm; Enable the model's built-in multi-token-prediction head as a draft; Bandwidth ceiling sanity check; Isolate the variable in a benchmark; Fail fast on memory; Point coding agents at a local OpenAI or Anthropic-compatible endpoint
- Tools: Splash (Inco AI inference engine for Apple Silicon, Apache 2.0, Qwen 3.8 27B and 35B only), Inco AI, D-Flash 2 (Splash's 1.2 GB draft model), Qwen 3.8 27B and 35B (built-in multi-token-prediction head), OMLX (inference engine used as baseline), LM Studio (shipped Splash as a selectable backend), MLX, GGUF, llama.cpp, Ollama, SpeedBench (coding benchmark with reasoning mode), Claude Code

## [Apple Just Made the Best Local AI Hardware. Do Not Buy It Yet.](../videos/12lxN9NHuHc.md)
`12lxN9NHuHc` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai

Apple's M5 Ultra puts neural accelerators in every GPU core, but LM Studio's bundled runtime switches them off; prefill-vs-decode math and rising memory prices decide whether to buy now or wait.

- Techniques: Benchmark prefill and decode separately; Benchmark at long context (32K tokens and up); Check the runtime startup log for the accelerator path before trusting any numbers; Use the MLX build or upstream llama.cpp instead of the bundled LM Studio runtime for M5 Macs; Buy-or-wait decision rule; Compare memory upgrades by price per gigabyte
- Tools: Apple M5 Ultra, Apple M5 Max, Apple M5 Pro, Apple M3 Ultra, Apple M4 Max, MacBook Pro 14-inch (M5 Max, 128 GB), Mac Studio, LM Studio, llama.cpp (bundled runtime and upstream build), Metal 4 Tensor API, MLX, BaseRT (third-party runtime, paper July 21)

## [I Ran a 35B Param Model On My iPhone (Local AI)](../videos/hM_mEE8BXfU.md)
`hM_mEE8BXfU` · Better Stack · 2026-10-02 · q3 · practitioner · tutorial · also: local-ai

Better Stack walkthrough of running Qwen 3.5 35B-A3B (a mixture-of-experts model) on an iPhone 17 at about 11 tokens/s by streaming experts from SSD, relying on the OS page cache, and tiered 4-bit/2-bit quantization, with the Flash MoE / Flash iOS setup steps.

- Techniques: Stream MoE experts from SSD and leave caching to the OS page cache; Tiered quantization by expert hotness; Validate expert reads against per-expert sizes; Build and sideload Flash iOS onto an iPhone (tutorial steps); Thinking-loop diagnosis for on-device MoE
- Tools: Flash MoE (Dan Woods; originally written for a MacBook), Flash iOS (iPhone port wrapping the Flash MoE engine), Qwen 3.5 35B-A3B (mixture-of-experts model, 35B total, about 3B active), Xcode, iPhone 17, metalinfer.m (file in the Flash MoE repo), Apple developer account

## [How Fast Is Local AI on Your Mac? (Every Chip, M1 to M6)](../videos/WoGwVXFmWzU.md)
`WoGwVXFmWzU` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai

Kai Explains compares Apple Silicon Macs (M1 to M6) for local LLM use and argues that memory size, then memory bandwidth, then the exact chip variant predict real speed better than the chip generation, and that software and speculative decoding can matter more than hardware.

- Techniques: Decode throughput ceiling estimate; Memory-fit check before speed; Like-for-like benchmark protocol; Speculative decoding for memory-bound decode; Try a faster inference engine before buying hardware; Prompt-to-answer ratio rule for hardware choice; Cache-aware agent latency accounting
- Tools: Apple Silicon M1 through M6 (Mac Mini, Mac Studio, MacBook Pro and Air), llama.cpp (called 'Lama CPP' in the auto-captions), MLX (Apple's ML framework), Multi-token prediction (MLX variant), Splash (inference engine, as captioned; 52 tok/s on a short prompt), Speculative decoding with a small draft model, Qwen 27B (auto-caption 'QEN327B'), 4-bit, Apple Neural Accelerator (in M5 GPU cores)

## [Mojo Is Finally Open Source... So I Tested It](../videos/uIqjWeO91p4.md)
`uIqjWeO91p4` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: dev-tools

Better Stack tests Mojo 1.0 and its newly open-sourced compiler: a real same-file GPU kernel on a laptop, but inflated benchmarks, unstable APIs and a Qualcomm acquisition cloud the picture.

- Techniques: Benchmark against the right baseline; One-file prototype-to-kernel path; Check the stability promise against the release notes
- Tools: Mojo 1.0 (Modular), Python, NumPy, C++, CUDA, Metal, Swift, Triton, LLVM, Clang, Modular MAX (kernels), Rust

## [Apple Hasn’t Put an LLM on Your Watch. So I Did.](../videos/IGQZuZkwVLI.md)
`IGQZuZkwVLI` · Better Stack · 2026-10-02 · q3 · intro · demo · also: local-ai, dev-tools

Better Stack runs a 90M-parameter hybrid LLM offline on a 2020 Apple Watch Series 6 via llama.cpp built for watchOS, and explains the ARM64_32 and Core ML limits that shape the port.

- Techniques: Build llama.cpp for watchOS (ARM64_32); Check the 32-bit address ceiling before picking a model; Prefer small hybrid SSM models for memory-bounded edge devices; Register tools by renaming a samples file; Voice as the input channel on a wearable
- Tools: Falcon H1 (90M, hybrid attention + Mamba-2), small M2 135M model (caption-garbled name), llama.cpp, Core ML, Xcode, watchOS / ARM64_32, Mamba 2, GGUF model format, Wikipedia tool call (sample), weather tool call (sample)

## [Meet Jev: The Schema-Safe AI Built to Make Decisions](../videos/BGDd26FiOm4.md)
`BGDd26FiOm4` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: token-cost-efficiency, evals, models-research

Critical walkthrough of JEV (TypeSafe AI), a model that returns only probabilities for typed decision questions instead of text; fast and cheap, but accuracy and calibration caveats are the real story.

- Techniques: Probability gate instead of a generated yes/no; Choice query with full distribution for routing; Tool selection without a language model in the loop; Per-tool-call relevance filter for Claude Code; Adversarial state test before trusting the output; Evaluate against a solver or known-correct baseline; Local logit read of an open model for a single decision; Price a decision workload before adopting
- Tools: JEV (TypeSafe AI model, version 1.13 per the vendor page), TypeSafe AI, GPT 5.6 Terra (reference model as transcribed), GPT 5.6 Sol (reference model as transcribed), GPT-6 Astra (reference model as transcribed), Claude Fable 5.1 (reference model as transcribed), Qwen 3.5 4B (captioned as 'Quen 3.54b'; open-model reimplementation), Qwen 3.6 35B (captioned as '3.635B'; open-model reimplementation in the MMLU-Pro comparison), Claude Code (JEV plugin scoring tool calls), RLCD (Reinforcement Learning for Calibrated Decisions, the vendor's training method), MMLU-Pro (benchmark), Vercel

## [Open Source AI is dying (and I know why)](../videos/zxnXemN98d0.md)
`zxnXemN98d0` · Kai Explains · 2026-10-02 · q4 · practitioner · talk · also: local-ai, token-cost-efficiency, governance-compliance

Kai argues open-weight AI died at the size where models no longer fit on hardware you own. Below that line the freedom holds, and frontier open weights now work mainly as a price ceiling on hosted APIs.

- Techniques: Break-even check for self-hosting vs API; Local memory budget before choosing a model; Pin the provider, not just the model name; Detect silent compaction and context caps; Pre-adoption license and file audit
- Tools: Kimi K3, DeepSeek V4 Flash, DeepSeek V4 Pro, DeepSeek V3, Llama 3.3 70B, Llama 2, Gemma 4, Qwen 3.6, Alibaba Qwen, Ollama, OpenRouter, Lambda Labs

## [Mac Studio vs DGX Spark: Which Is Better for Local AI?](../videos/_NZeV2uOVnk.md)
`_NZeV2uOVnk` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai, infra-cost-scaling

Kai Explains compares a Mac Studio (M3 Ultra, with M5 Ultra prices and specs) and an NVIDIA DGX Spark for local LLM inference, and argues the answer depends on whether the workload is decode-bound, prefill-bound, or CUDA-shaped.

- Techniques: Benchmark prefill and decode separately; Estimate decode ceiling from bandwidth; Size memory as usable, not nominal; Test concurrency, not just one stream; Disaggregated prefill and decode across two machines; Rent before buying
- Tools: Mac Studio (M3 Ultra, 819 GB/s; M5 Ultra for specs and pricing, 1.2 TB/s), NVIDIA DGX Spark (GB10, 128 GB LPDDR5X, 273 GB/s), llama.cpp, MXFP4, Ollama, vLLM, TensorRT-LLM, SGLang, CUDA, cuDNN, NCCL, Triton

## [What It Actually Costs to Run DeepSeek V4.1 Flash Locally?](../videos/04ePeOyRN0k.md)
`04ePeOyRN0k` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai, token-cost-efficiency, models-research

Kai works through what DeepSeek V4.1 Flash really costs to self-host: 510 GB of resident weights, 23 s/token on a 16 GB Mac, a $18.8k four-Spark cluster, and a roughly four-year break-even against cheap API pricing.

- Techniques: Size local MoE hardware by resident bytes, not active params; Break-even test for self-hosting versus API; Measure decode tok/s by output type, separately from time to first token; Compress the Engram table, not the experts, when the model is already FP4
- Tools: DeepSeek V4.1 Flash (open weights, MIT license), DeepSeek V4 Flash, DeepSeek V4 Pro (retired), DeepSWE V1.1 (benchmark, name as captioned), Claude Opus 5, GPT 5.6 Sol, NVIDIA DGX Spark (GB10 Grace Blackwell, 128 GB unified memory), vLLM (tensor parallel 4), Mac mini (16 GB RAM), Hugging Face, GGUF, RTX 3060

## [Autoresearch Made Our Models 3x Faster — Tejas Bhakta, Morph](../videos/vrDvatGtIxs.md)
`vrDvatGtIxs` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: testing-verification, agent-architecture

Morph's Tejas Bhakta shows a propose-benchmark-keep-or-revert loop (autoresearch) tuning GPU kernels for about 3x speedup, with human-supplied ideas and explicit guards against reward hacking.

- Techniques: Keep-or-revert benchmark loop; Split the work: human ideas, loop parameters; Profile before tasking the agent; Hardware and model context files in the harness; Explicit anti-cheat rules in the benchmark; Stack kernels and keep fallbacks; Switch models when one fails at the DSL
- Tools: Nsight Systems (NSYS), CUDA, CUDA graphs, CuTe DSL, CUTLASS, FlashInfer, NVFP4, Autoresearch (Karpathy)

## [The Frontier AI Inference Cloud for Agents — Byung-Gon (Gon) Chun, FriendliAI](../videos/Hvb2LfMH58c.md)
`Hvb2LfMH58c` · AI Engineer · 2026-09-20 · q2 · intro · talk · also: infra-cost-scaling, agent-architecture

FriendliAI's CEO argues agent workloads need task-level (end-to-end) latency optimization, not per-request speed, and pitches prefix caching, KV cache management and cache-aware routing on an open-weight inference cloud.

- Techniques: Prefix KV caching for agent steps; Tiered KV cache with quantization and cross-replica sharing; Cache-aware routing with load-aware fallback; Optimize end-to-end task latency as the target metric; Agent-aware scheduling (described as future work)
- Tools: vLLM, GLM 5.2, Kilo Code, Claude Opus 4.8, MiniMax, Kimi

## [Routing LLM Inference in Production: From Engine Signals to Policy — Qianru Lao & Lu Zhang, OpenAI](../videos/sOB3HSiG8vo.md)
`sOB3HSiG8vo` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · also: infra-cost-scaling

OpenAI's inference team explains how its inference load balancer moved from a feedback-loop weight controller to a control-plane/data-plane design that optimizes end-to-end latency, plus retry budgets, outlier penalties and load shedding for production stability.

- Techniques: Control-plane / data-plane routing split; Latency-minimizing routing weights; Outlier penalty by weight reduction; Utilization-dependent retry budget; Proactive load shedding

## [Weight Folding, CUDA Streams, and the Bug That Made My Model Speak Backwards — Filip Makraduli](../videos/c1hGBoWw20A.md)
`c1hGBoWw20A` · AI Engineer · 2026-09-20 · q4 · deep · talk · also: models-research

Filip Makraduli on "flash norm": algebraic rewrites of RMSNorm (weight folding, deferred division) that speed up transformer decoding, plus a CUDA stream race that corrupted long generations.

- Techniques: Weight folding of norm gain into the next linear layer; Deferred scalar division for overlap; Explicit CUDA stream join with event markers; Long-generation regression check for kernel changes; Deploy custom Hugging Face checkpoints on a self-hosted cluster
- Tools: Hugging Face, CUDA streams, torch.compile, transformer-tricks repo

## [Vertical Mobility: Inference from MVP to Trillion-Parameter Workloads — Sitanshu Gupta, CoreWeave](../videos/cQQbJqvZkpo.md)
`cQQbJqvZkpo` · AI Engineer · 2026-09-20 · q3 · practitioner · talk · also: infra-cost-scaling

CoreWeave's inference platform talk: how serverless, dedicated and batch consumption models share one stack, with KV-cache-aware routing, cache offload and quantization/speculative decoding as the main performance levers.

- Techniques: KV-cache-aware request routing; KV-cache offload to high-bandwidth storage; Provisioned throughput on a shared serverless tier; Time-scheduled reuse of reserved GPUs for batch; Async speculator training on customer data; Metering without retaining content
- Tools: vLLM, SGLang, TensorRT-LLM, LMCache, Mooncake, NVFP4, Artificial Analysis, OpenRouter

## [Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer](../videos/btxG75rNJC4.md)
`btxG75rNJC4` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · also: observability, training-finetuning-rl

Two AI21 engineers walk through two silent vLLM bugs for hybrid Mamba models, one a scheduler ordering error and one a 32-bit index overflow, and the debugging method that found them.

- Techniques: Logprob comparison against a reference forward pass; Reproduce under pressure with determinism; Thread identity through the forward context; Bisect by forcing one code path; Check whether a fix is causal and watch for overflow
- Tools: vLLM, Hugging Face Transformers, NVIDIA compute-sanitizer, FSDP, Jamba (hybrid Mamba plus attention model)

## [Operating Distributed Inference Systems at Scale — Nishant Gupta & Naman Ahuja, Meta](../videos/7c9FSUVcXR0.md)
`7c9FSUVcXR0` · AI Engineer · 2026-09-20 · q3 · practitioner · talk · also: infra-cost-scaling, agent-architecture

Two Meta infra engineers argue LLM inference is now a distributed-systems and orchestration problem, so teams should optimize cost per successful task and build a control plane, not just faster tokens.

- Techniques: Four-quadrant optimization check; Workflow-aware scheduling and retries; Cascade breakers: queue-depth shedding, circuit breakers and retry budgets; Cost per successful task as the KPI; Telemetry-driven control loop; Latency, cost and throughput trade-off triangle
- Tools: vLLM, SGLang, TensorRT, Triton, Kubernetes, Mesos

## [What's New in Inference Engineering — Philip Kiely, Baseten](../videos/75ckHC2LU_0.md)
`75ckHC2LU_0` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · also: training-finetuning-rl, models-research

Philip Kiely (Baseten) updates his inference book with post-February 2026 developments: why TurboQuant lost on data-center throughput, learned KV compaction, DFlash diffusion-style drafting, and continuous speculator retraining.

- Techniques: Continuous speculator retraining; DFlash block drafting; Learned KV compaction (Still); Stay on NVFP4 weight quantization for production; Local-first versus data-center-first sequencing
- Tools: vLLM, NVIDIA Dynamo, NIXL (transcribed as 'Nickel'), EAGLE-3, DFlash, DSpark, Medusa, TurboQuant, NVFP4, Still (Base10 KV compaction), attention matching, cartridges

## [Large clusters for small models — Daniel Svonava, Superlinked](../videos/g4SsanB0gMc.md)
`g4SsanB0gMc` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · also: local-ai, infra-cost-scaling, training-finetuning-rl

Daniel Svonava (Superlinked) on serving fleets of small open models on your own GPUs: why top-down routers fail for many small requests, and how a centralized pull-based queue, a thin Rust gateway and a runtime sidecar fix it.

- Techniques: Centralized pull-based batching queue; Thin gateway with annotation, not full parsing; Runtime sidecar behind a socket; Knee-based benchmarking; Pin plus lazy-load model placement; Per-task model selection with evals, then cheap adaptation; Autoresearch loop for serving tuning
- Tools: vLLM, SGLang, PyTorch, Candle, NATS JetStream, MessagePack, Rust, AWS Bedrock, LoRA, Hugging Face

## [Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google](../videos/l1-D89bAuOA.md)
`l1-D89bAuOA` · AI Engineer · 2026-09-20 · q3 · practitioner · talk · also: evals, observability

Google engineers argue that LLM serving benchmarks often blame the server when the benchmark client is at fault, and show Inference Perf, a multi-process, reproducible load generator built for production-scale inference.

- Techniques: Scheduled multi-process load generation; Client-side health check on every run; Declarative benchmark configs with distributions; Sweep the load to find saturation; Match sampling and dataset preprocessing to production; Shared workload definitions
- Tools: Inference Perf, llm-d, Prism, vLLM, SGLang, Kubernetes, k6, Locust, MLPerf, ShareGPT

## [Your Agreements Are a Database You Can't Query — Hiral Shah, Docusign & Sean Sodha, NVIDIA](../videos/_gvamfT8H-w.md)
`_gvamfT8H-w` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: data-engineering, enterprise-adoption

DocuSign and NVIDIA on turning enterprise agreement PDFs into queryable data, using a small layout-aware table extraction VLM (Nemotron Parse) inside a hybrid OCR pipeline.

- Techniques: Purpose-built small table-extraction VLM; Hybrid two-route document pipeline; Offline-heavy vs online-light compute split; Structured export and API over extracted data; Benchmark on table extraction and track accuracy vs speed
- Tools: Nemotron Parse, Nemotron Retriever, NVIDIA NIM, vLLM, C-RADIO, NVFP4, FP8, Coupa

## [Realtime Voice Agents with Frontier Intelligence — Bohan Li, EliseAI](../videos/MBHOH1NmDqc.md)
`MBHOH1NmDqc` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: voice-multimodal, agent-architecture

EliseAI's Bo Li explains a cascaded voice-agent harness (streaming transcription, background tool calls, prefix-cached TTS) that keeps frontier-model intelligence at real-time speed.

- Techniques: Streaming speculative transcription (two-tier ASR); Early generation with background tool calls and cancellation; Word-sequence prefix cache for TTS; Playback deduplication after speculative TTS
- Tools: Flux (fast streaming transcriber), Scribe V2 (accurate batch transcriber), Cartesia (TTS with WebSocket support)

## [Generative Video at the Speed of Light — Keegan McCallum, uRun](../videos/Xln-On3syJk.md)
`Xln-On3syJk` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: voice-multimodal, infra-cost-scaling

Keegan McCallum (uRun) argues generative video is improving on efficiency and long-horizon generation as well as quality, and describes the infra needed for real-time interactive video apps.

- Techniques: Distill a large video model for real-time serving; Real-time steering instead of prompt-and-reroll; Multi-model streaming pipeline with per-frame control sync; Wrap real-time video as a React component plus Python runtime; Agent-facing access via CLI and MCP server
- Tools: Helios, Wan 2.1 14B, WebRTC, ICE, TURN, React, Python async runtime, MCP, CLI, Sora, Sora 2, Seedance

## [Homa: The End of TCP for AI Clusters — John Ousterhout, Stanford](../videos/eZ8WWZzoaR0.md)
`eZ8WWZzoaR0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: infra-cost-scaling

Ousterhout argues AI inference and agentic workloads now send many small latency-sensitive messages, which TCP and RDMA handle badly, and presents Homa, a receiver-driven transport with about 13x lower short-message P99 in his benchmark.

- Techniques: Message-framed transport (RPC unit); Receiver-driven grant scheduling; Unscheduled first-RTT send; SRPT via switch priority queues; Percentile sweep by message size
- Tools: Homa (Linux kernel module), TCP, RDMA over Converged Ethernet (RoCE), ECN marking

## [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../videos/YXowceUKYJI.md)
`YXowceUKYJI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: infra-cost-scaling, agent-architecture

Red Hat engineers explain why agentic multi-turn traffic breaks classic LLM serving, and how llm-d uses KV-cache-aware routing and prefill/decode disaggregation on Kubernetes, with benchmark data and a GLM 5.2 case study.

- Techniques: KV-cache-aware pod routing; Prefill/decode disaggregation with KV transfer; Tiered KV offload with session pinning; Distribution-based capacity planning and trace replay; Decision matrix before choosing PD
- Tools: llm-d, vLLM, Kubernetes, NIXL, DeepEP, Mooncake, inference-perf, LeaderWorkerSet, RDMA/RoCE

## [Why AI Agents Need Million-Token Context — Thomas Wolf & Olive Song, MiniMax](../videos/5Cxe5dv2Xlw.md)
`5Cxe5dv2Xlw` · AI Engineer · 2026-09-18 · q3 · practitioner · interview · also: models-research, context-engineering

MiniMax's Olive Song and Hugging Face's Thomas Wolf on how M3 reaches 1M-token context with sparse attention and native multimodal pretraining, and why agents need that context for multi-round tool use.

- Techniques: Index-then-sparse attention over context blocks; Train vision from the first pretraining step with interleaved data; Open project intake for research; Research harness for automating model-lab workflows
- Tools: MiniMax Sparse Attention (MSA), Hugging Face model card

## [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../videos/pOvWgX7IJsc.md)
`pOvWgX7IJsc` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, models-research

Simran Arora (Together AI) on why multi-GPU communication is now the kernel bottleneck, the transfer and overlap trade-offs behind her Parallel Kittens primitives, and a benchmark showing frontier models still struggle to write fast multi-GPU kernels.

- Techniques: Copy-engine vs device-initiated transfer choice; Intra-SM vs inter-SM communication overlap; Thin primitive layer over a single-GPU kernel; Benchmark built from a parallelism taxonomy plus real-workload problems; Report correctness (pass@k) and speed-gated correctness (fast_1@k) separately; Agent harness: multi-turn bash agent for kernel tasks
- Tools: CUDA, PyTorch, torch.distributed, NCCL, RCCL, Triton, Triton Distributed, TileLink, ThunderKittens, Parallel Kittens, Parallel Kernel Bench, mini-SWE-agent

## [Deep dive on LLM Inference at Scale — Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher](../videos/y2W4FNAuPEA.md)
`y2W4FNAuPEA` · AI Engineer · 2026-09-18 · q3 · practitioner · workshop · also: infra-cost-scaling, agent-architecture

Two-hour LLM inference workshop covering KV-cache memory math, prefill vs decode, attention variants, quantization, vLLM/SGLang serving optimizations, and benchmark caveats.

- Techniques: KV-cache capacity planning; Fix one dimension, then solve the rest for cost; Weight quantization for KV headroom; Attention variant selection; Radix-tree prefix caching for agent loops; Speculative decoding variants; Engine benchmarking loop
- Tools: vLLM, SGLang, TensorRT-LLM, NVIDIA Dynamo, Hugging Face Transformers, FlashAttention, EAGLE, Medusa, Molab, Google Colab, Mistral 7B, GPT-OSS-120B

## [Agentic Sites: Building Hyper Personalized Websites — Carlos Sanchez, Adobe](../videos/jebp4V0vh30.md)
`jebp4V0vh30` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, rag-retrieval, product-ux

Adobe's Carlos Sanchez demos "agentic sites" that personalize page blocks in real time from browsing intent, grounded on the existing site, with provider choice driven by latency and accuracy evals.

- Techniques: Multi-provider eval matrix for accuracy and latency; Grounded block-level generation; Signal bucketing into personas or intents; Pre-generate and prefetch; Fast inference provider for the hot path
- Tools: Adobe Experience Manager, Edge Delivery Services, Cerebras, Gemma 4, Promptfoo, AWS Bedrock, Cloudflare, Google Cloud

## [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](../videos/u6q-byPWUuo.md)
`u6q-byPWUuo` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, training-finetuning-rl, enterprise-adoption

Abridge's engineering lead on running clinical AI at scale: clinician-written rubrics feed LLM judges, staged rollouts, and small post-trained models gated by cheap triggers to balance quality, latency and cost.

- Techniques: Multi-reviewer rubric construction for LLM judges; Staged rollout with online feedback for AI features; Task decomposition into small specialised models; Gate cascade for real-time event triggers

## [Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai](../videos/byn9PURoBNY.md)
`byn9PURoBNY` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: infra-cost-scaling, training-finetuning-rl

Krea's infra engineer on training the from-scratch Krea 2 diffusion transformer at scale: which metrics matter, why to let crashing runs restart, frequent checkpoints, and bursting training and inference across clusters and rented GPUs.

- Techniques: Let crashing jobs restart instead of debugging each crash; Hard GPU health gate on temperature; Checkpoint every 20 to 30 minutes to a high-throughput file system; Two-tier priority queue in front of Kubernetes; Overflow to external GPUs with a virtual node
- Tools: Kubernetes, Virtual Kubelet, Kubernetes descheduler, Kubernetes taints and tolerations, Queue system (captioned as 'Q') for gang scheduling, Prometheus, NVIDIA DCGM, Weka (parallel file system), Ceph, InfiniBand, NVLink, Hugging Face

## [5 Voice Agent Failure Modes You'll Hit in Week One — Venky B, Plivo](../videos/vblnYHzBgS4.md)
`vblnYHzBgS4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: voice-multimodal, data-engineering, evals

Venky B of Plivo lists five voice-agent failure modes seen in production (latency, transcription, data collection, TTS output, barge-in) and the fixes his team uses. Main takeaway: treat voice as a structured pipeline problem, not a prompt problem.

- Techniques: Per-stage latency budget with time-to-first-audio as the metric; Self-hosted small or MoE open model for the conversational LLM; Dynamic keyword boosting per call phase; LLM post-processing of STT output with domain context; Typed field schema with validation and confirmation for data collection; Field-level unit-test evals for voice agents; Normalization layer between LLM and TTS; Pronunciation smoke tests with known hard names
- Tools: LiveKit, Pipecat, Pydantic, Zod, Qwen 3.5, Gemma 4, Cerebras, Groq

## [The Next Medium: Why Real-Time Interactive Video Changes Everything — Ahmed Ahres, Reactor](../videos/5dCAmSDOAjI.md)
`5dCAmSDOAjI` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: voice-multimodal, product-ux, infra-cost-scaling

Ahmed Ahres (Reactor) argues real-time interactive video and world models will change how content is made and consumed, then describes the infra gaps: streaming, session memory, and sub-100 ms global latency. Mostly a company pitch.

- Techniques: Stream frames over a live session instead of returning a file; Regional GPU routing for a latency budget; Session memory to keep generated worlds consistent; Multi-GPU serving plus quantization for cost and speed; Human-in-the-loop evaluation for real-time output
- Tools: Reactor API (real-time world model platform, roughly 10 lines to integrate per the speaker), Helios (ByteDance, interactive video model), LingBot (Alibaba, world model), LongLive 2 (NVIDIA, multi-shot film model), StreamDiffusion (NVIDIA, video-to-video; transcript reads 'SoundCloud Streaming', likely a caption error), Veo, Sora, Genie 3 (mentioned as comparisons)

## [200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI](../videos/AN65uc645mE.md)
`AN65uc645mE` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: voice-multimodal, evals, multi-agent

Hippocratic AI's engineering lead explains how their clinical voice agent (200M+ patient conversations) hits safety, latency and accuracy at once: a vertically built stack, 31 parallel specialist models, context-fed ASR, and lossless inference tricks.

- Techniques: Parallel specialist models with self-gating; Context-conditioned ASR; Second-pass rescoring for ambiguous short utterances; Async and offline verifiers for tool calls; Human plus synthetic eval mix with sample-size planning; Severity-graded harm rubric; Lossless inference stack
- Tools: Whisper (large-turbo, fine-tuned), speculative decoding, 4-bit quantization, KV cache

## [Voice agents with Realtime Video — Sidney Primas, LemonSlice](../videos/z1dqv74SpUs.md)
`z1dqv74SpUs` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: voice-multimodal, agent-architecture

Lemon Slice's CTO explains how they build real-time, photorealistic video avatars from a causal video model, covering past-only attention, one-step denoising, long error-free runs, and a GPU/CPU harness that keeps streams stutter-free.

- Techniques: Causal (past-only) attention mask for streaming video; Collapse denoising steps for real-time output; Expressive audio encoders over default ones; Real-time model harness (GPU/CPU orchestration); Two-layer EQ/IQ split

## [China Just Open-Sourced 6 Ways to Speed Up Your AI Inference (Tencent AngelSpec)](../videos/0ixklwdIsuY.md)
`0ixklwdIsuY` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: token-cost-efficiency, models-research

Kai Explains walks through Tencent's AngelSpec repo: six speculative-decoding drafter methods, why block-diffusion drafters win on acceptance but not under load, and the DCut verification trick that helps at high concurrency.

- Techniques: Speculative decoding with a cheap drafter and a verifier; Pick the drafter by concurrency level; Enable adaptive verification in vLLM (DCut-style); Use pretrained drafters instead of training; Match the drafter to the serving mode; Load-test the speculation config before production
- Tools: AngelSpec (Tencent training framework for speculative-decoding drafters; custom license), Hi3 (Tencent, 21B active parameters), MTP (multi-token prediction), EAGLE-3, D-Flash (block diffusion, UC San Diego), dFlare (named in the video; Peking University and Tencent), dSpark (DeepSeek serving team), D-Fly (Tencent), DCut (verification early-exit), vLLM, DeepSeek V4, Qwen3-8B

## [Qwen 3.8 27B is 3X Faster With MTP](../videos/hHdJpiPxhco.md)
`hHdJpiPxhco` · Kai Explains · 2026-09-02 · q4 · practitioner · tutorial · also: local-ai

Qwen 3.8 27B ships an MTP draft head inside its weights; enabling it can roughly double or triple local decode speed with the same output, but only on a current runtime build, with a tuned draft depth and temperature, and only if the model fits in VRAM.

- Techniques: Enable MTP in llama.cpp; Enable MTP in vLLM; Enable MTP in SGLang; Enable MTP in Ollama with a tag; Sweep draft depth and find your peak; Tune sampler temperature for draft acceptance; Benchmark by task type, not one number; Check the memory path before enabling
- Tools: Qwen 3.8 27B (dense, 27B parameters), MTP (multi-token prediction) draft head, llama.cpp (build after May 13, 2026), Ollama (MTP-tagged model tags), vLLM (speculative decoding config), SGLang (speculative algorithm parameter), NVFP4 (4-bit format, Blackwell only), EAGLE-3 (not mentioned in this video), NVIDIA RTX 3090, 4090, 5090, AMD Radeon (Vulkan and ROCm backends), Apple Silicon with Metal kernels

## [Running a 80B AI Model on a 8GB GPU, FAST (oLLM Guide)](../videos/5E3qTmQPmP8.md)
`5E3qTmQPmP8` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai

Kai walks through oLLM, a Python library that streams Qwen3-Next 80B layers off SSD on an 8GB GPU, and argues it is only worth using for long-context offline passes, not interactive or agent work.

- Techniques: Layer-streaming offload from SSD; Disk-backed full-precision KV cache; Chunked projections plus flash attention to cap peak VRAM; Expert-selective streaming for MoE models; Predict throughput from storage bandwidth before running; Pick the runtime by job shape (speaker's decision rule)
- Tools: oLLM (OLM), Qwen3-Next 80B, llama.cpp, Hugging Face transformers, PyTorch, MLX, flash attention

## [What Would it Cost to Run Claude Opus 5 Locally?](../videos/yJCHNdQ8sLs.md)
`yJCHNdQ8sLs` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, token-cost-efficiency

Kai Explains works through what it would take to run an Opus-class model locally, using open-weight Kimi K3 as a stand-in; the bottleneck is memory bandwidth and the electricity bill, not the hardware price.

- Techniques: Size the local rig from the smallest usable quant plus KV cache, not from headline parameter count; Estimate decode speed from memory bandwidth, and compare hardware on bandwidth, not capacity; Diagnose a slow local run by checking VRAM occupancy and GPU utilization; Benchmark with a short generation and extrapolate to a target reply length; Compute breakeven against the specific API price you would replace, including utilization and price decline; Watch interconnect bandwidth when splitting a model across machines
- Tools: Claude Opus 5, Kimi K3 (Moonshot AI), Unsloth quantized builds, Kimi K3 REAP 512GB (pruned build), NVIDIA RTX Pro 6000 Blackwell, NVIDIA DGX B300, NVIDIA DGX Spark, NVIDIA RTX 5090, NVIDIA H100, NVIDIA B200, NVIDIA A100, RTX 3090

## [I Tested Every Qwen3.8-27B Quant: Here’s the Best One For Your GPU](../videos/hg26j0erUSo.md)
`hg26j0erUSo` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, evals

Kai's practitioner guide to choosing a quant of Qwen3.8-27B for consumer GPUs: architecture-aware quants, why a Q4 KV cache silently degrades outputs, and VRAM-based file picks.

- Techniques: Diff quantized output against the full-precision model before trusting a quant or cache setting; Keep the KV cache at Q8 or full precision; Choose the quant by VRAM budget; Pin the model revision on download; Lower reasoning effort for simple tasks; Enable the built-in MTP draft head for speculative decoding; Make sure the front end renders the chat template correctly; Load the vision projector as a separate file
- Tools: Qwen3.8-27B, Unsloth UD-Q4_K_XL / Q6 / Q8 quants, Bartowski IQ4_XS quant, Ridge quant (name as transcribed; may be a caption error), Atomic Chat KL-divergence benchmark, Quesma benchmark run, GPQA Diamond, IFBench, TerminalBench, Jinja chat-template flag, spec type draft MTP (speculative decoding flag as spoken), RTX 3090

## [What Would It Cost to Run GLM 5.3 Locally?](../videos/ZR3E9-fCFf8.md)
`ZR3E9-fCFf8` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: local-ai, token-cost-efficiency

Kai works through the memory and dollar math for running GLM 5.3 locally: MoE active params don't reduce memory, quantization sets the footprint, and renting or the API beats buying hardware for most teams.

- Techniques: Resident-memory estimate for MoE models; GPU count from footprint with headroom; Rent-before-buy evaluation with cost break-even; Hybrid local-plus-API routing
- Tools: GLM 5.3 (Z.ai), GLM 5.2 (Z.ai), GLM 5.1 (Z.ai), GLM coding plan (Z.ai), Terminal Bench 3 (benchmark, cited by speaker), CyberGym (benchmark, cited by speaker), ExploitBench (benchmark, cited by speaker), Unsloth dynamic 2-bit quantization, GGUF (2-bit file format, mentioned), Hugging Face (weight hosting), Apple Mac Studio M4 Ultra (512 GB), Apple Silicon unified memory

## [This Tool Finds the Perfect AI Model for Your Hardware (llmfit)](../videos/zf8jpD77sKY.md)
`zf8jpD77sKY` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: local-ai, dev-tools

Better Stack walks through llmfit, a terminal tool that detects your CPU, RAM and GPU, scores local models for fit and speed, and tests its estimates on machines from a 2012 Raspberry Pi to an RTX 5090.

- Techniques: Pre-download hardware fit check; Back-of-envelope decode speed check; Calibrate the tool against a real run; Use-case-weighted ranking
- Tools: llmfit (spoken as LLM Fit; no version stated), Hugging Face, DeepSeek R1, Qwen 3.6 12B (transcribed as Quen 3.6), Qwen 3.x models (transcribed as Quen 3.8 on the RTX 5090), Gemma 4 12B, Kimi K2.7 Flash variant (transcribed as Kimi K 2.7 D flash), Falcon H1 Mini, Llama 3 (mentioned, not tested), MLX, CUDA, Metal

## [DeepSeek Did What Other Labs Won’t Even Try](../videos/7C0DDDec3A8.md)
`7C0DDDec3A8` · Kai Explains · 2026-09-02 · q4 · practitioner · news · also: models-research, token-cost-efficiency, training-finetuning-rl

Explainer on DeepSeek V4: how two new compressed attention mechanisms (CSA and HCA) cut long-context KV cache and compute, why that makes $0.435 per million input tokens possible, and what the 58-page report implies for other labs.

- Techniques: Learned KV compression over fixed token blocks (CSA); Heavy block compression with dense attention for global context (HCA); Three-timescale memory layout; Specialist post-training then distillation; FP4 quantization-aware training on MoE experts; Spend thinking tokens as a default when inference is cheap
- Tools: DeepSeek V4 Pro (1.6T total / 49B active), DeepSeek V4 Flash (284B total / 13B active), DeepSeek V3.2, Kimi K3 (2.8T, July 2026), Kimi K2.6, GLM 5.1, Claude Opus 5, GPT 5.4, GPT 5.2, Gemini 3.1 Pro, Gemini 3.0 Pro, Muon optimizer

## [I Can't Believe This AI Model Fits in 14 Megabytes (Needle 2)](../videos/M24yg6ZM7-I.md)
`M24yg6ZM7-I` · Better Stack · 2026-09-02 · q3 · intro · review · also: local-ai, models-research

Hands-on demo of Needle 2, a 45M-parameter, 14 MB tool-call dispatcher from Cactus Compute running offline on an ESP32-S3 microcontroller; it maps natural language to predefined device actions, not general chat.

- Techniques: Closed-action-set tool dispatch on a small model; Gate actions on the dispatcher's confidence score; Native low-bit training instead of post-training quantization; Reuse the demo engine by swapping commands
- Tools: Needle 2 (Cactus Compute, Apache 2.0), ESP32-S3, Raspberry Pi 5, LFM 2.5 (comparison model in Cactus benchmarks, as spoken), Custom inference engine and TUI (speaker's own, GitHub link in description)

## [Xiaomi AI Cube vs DGX Spark! The prototype that can change local AI](../videos/SeQ8qou_i-E.md)
`SeQ8qou_i-E` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, infra-cost-scaling

Xiaomi AI Cube vs DGX Spark: headline specs measure different things. Batch size, concurrency, serving config and the network decide real throughput; the Cube is still unshipped.

- Techniques: Normalize vendor throughput claims before comparing; Benchmark a box at several concurrency levels; Check the serving stack's defaults before judging hardware; Test network sensitivity before scaling out; Fit check and payback arithmetic for a purchase
- Tools: Xiaomi AI Cube (D100 chip, prototype, unannounced), NVIDIA DGX Spark, Xiaomi MIMO (3B model at the batch-one lab result), MIMO 2.5 (Xiaomi flagship, over 300B parameters), llama.cpp, vLLM, X-ring backend (name as spoken in the transcript, unverified), HBM4 (memory in data-center GPUs), NVIDIA H200 (comparison reference), Xiaomi phone processor (113 GB/s memory bandwidth, not the Cube chip)

## [10 Best Local Coding Models Right Now 2026](../videos/z605KVofJAY.md)
`z605KVofJAY` · Kai Explains · 2026-09-02 · q3 · intro · review · also: local-ai, models-research, coding-agents

Kai Explains lists 10 open coding models split by hardware tier and task type, and argues that picking a model for your own hardware and job matters more than leaderboard rank.

- Techniques: Hardware-first model sizing; Route models by job, not one model for everything; Local tab completion with Continue.dev and a FIM model; Running Qwen3.6 27B on one 24 GB card; Pick for tool-call reliability; Filter by license before commercial use; Cheap hosted model for bulk processing
- Tools: GLM 5.3, Kimi K2.7, Kimi K3, DeepSeek V4 Pro, DeepSeek V4 Flash, Qwen3-Coder (480B), Qwen3-Coder-Next, Qwen 3.6 27B, Qwen 2.5 Coder 14B, Devstral Small 2, GPT-OSS-20B, Codestral 2

## [oMLX Best Way to Run Local AI on A MAC](../videos/j557WxWtdZk.md)
`j557WxWtdZk` · Kai Explains · 2026-09-02 · q3 · practitioner · tutorial · also: local-ai, coding-agents, token-cost-efficiency

Kai Explains walks through OMLX, an open-source local inference server for Apple Silicon Macs that keeps a two-tier (RAM + SSD) KV cache so near-identical prefixes in long coding-agent sessions are reused instead of recomputed, mainly cutting time-to-first-token.

- Techniques: Diagnose slow agent turns as a prefix-cache miss; Install OMLX via the signed DMG; Point Claude Code at OMLX; Point Cursor at a local OpenAI-compatible server; One-command agent configuration with OMLX's CLI launcher; Browse and reuse Hugging Face and LM Studio model caches
- Tools: OMLX (Apache 2.0, about 18.6k GitHub stars, by one developer), Apple MLX / MLX server, Claude Code, Cursor, OpenCode, Codex, PyAgent, Pi, Hugging Face cache, LM Studio, safetensors, Qwen3 Coder Next (8-bit, benchmark model)

## [Everything That Actually Matters for Local AI](../videos/Y_34JZmZElg.md)
`Y_34JZmZElg` · Kai Explains · 2026-09-02 · q4 · practitioner · talk · also: local-ai, token-cost-efficiency

A numbers-driven guide to local AI hardware: memory bandwidth sets decode speed, active (not total) parameters set speed for MoE models, the model file is not the whole memory bill, and KV cache at long context can outweigh the weights.

- Techniques: Back-of-envelope decode speed; Split the hardware decision by workload; Full memory budget (not just the file size); Asymmetric KV cache quantization; Avoid partial GPU offload for the last layers; Prefer 4-bit or higher with QAT checkpoints; avoid 3-bit and lower for reasoning work; Evaluate on your own task before choosing hardware or quantization; Local versus API break-even check; Cap local agent runs at tool-call budgets
- Tools: llama.cpp, Ollama, LM Studio, vLLM, Apple MLX, Qwen3 (32B dense, 30B MoE, 35B-A3B), Gemma (26B-A3.8B sparse, 27B), DeepSeek (cache compression, cheap API), Kimi K3 (2.8T parameters), NVIDIA RTX 5090, NVIDIA RTX 3090, NVIDIA H200

## [Best Hardware for Running Local LLMs in 2026: Mac vs NVIDIA vs Cloud](../videos/gQ7iJuciMg0.md)
`gQ7iJuciMg0` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, token-cost-efficiency, infra-cost-scaling

Compares Mac Mini M5 Pro, DGX Spark, RTX 5090 and rented GPUs for local LLMs at current prices, arguing that prefill and decode need different hardware and that renting usually wins on cost.

- Techniques: Evaluate hardware separately for prefill (TTFT) and decode (tokens/sec); Split prefill and decode across machines; Budget memory headroom, not just model fit; Measure real memory bandwidth, not spec sheet bandwidth; Rent-vs-buy break-even calculation; Size for the model you run this week; Route by workload
- Tools: Mac Mini M5 / M5 Pro (Apple), Mac Mini M4 Pro (Apple, prior generation), Mac Studio, M3 Ultra (Apple), M5 Ultra (Apple), NVIDIA DGX Spark, NVIDIA RTX 5090, NVIDIA H100 (rental), Strix Halo (AMD, 128GB box), vLLM, DeepSeek V4 Flash (304B parameters), speculative decoding (on the 5090 owner's 27B setup)

## [New Local AI Inference Engine You Should Be Using in 2027 ? (FreeToken)](../videos/ZvZM4qnUVGI.md)
`ZvZM4qnUVGI` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai

FreeToken, a five-week-old local inference engine, runs a 433 GB mixture-of-experts model on one 96 GB GPU by caching recently used experts and splitting misses between PCIe transfer and CPU compute; system RAM is the real limit.

- Techniques: Global LRU expert cache across all layers, no predictor; Split misses between PCIe fetch and CPU compute, overlapped; Calibrate the offload split once per machine; Replay recorded routing traces to compare cache policies fairly; Judge offload engines by worst-case turn latency, not mean tokens per second; Install and build requirements for FreeToken as stated
- Tools: FreeToken, llama.cpp, Ollama, LM Studio, KTransformers, DeepSeek V4 Flash, vLLM, Apache Spark, Mixtral offloading, MoE-Infinity, Pro-MoE, Expert Flow

## [The Study NVIDIA Doesn't Want You to See](../videos/5TFzJ38ae1s.md)
`5TFzJ38ae1s` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, infra-cost-scaling, token-cost-efficiency

Kai Explains reads the "Dumpster Cluster" paper (128 used V100s serving Llama models) past its viral 35x tokens-per-dollar claim. Capex-only, 8B-only numbers flip at 70B once electricity, failures and software support are counted.

- Techniques: Lifetime cost-per-token accounting; Operational failure budgeting for used GPU fleets; Track software support as a separate lifecycle
- Tools: Dumpster Cluster paper (128x V100 SXM2 cluster study), NVIDIA V100, NVIDIA A100, NVIDIA H100, NVIDIA B200, vLLM (0.17 for B200 runs, 0.6 for H100/A100 runs, per the video), PyTorch 2.11 (dropped Volta from CUDA 12.8/12.9 pre-built binaries), CUDA (compute capability 7.0 = Volta), CoreWeave Vera Rubin (vendor tokens-per-MW claim)

## [This 2B Model Cloned My Voice Locally (VoxCPM)](../videos/O4TMwZlUJvQ.md)
`O4TMwZlUJvQ` · Better Stack · 2026-09-02 · q3 · practitioner · tutorial · also: voice-multimodal, local-ai

Tutorial on running OpenBMB's 2B VoxCPM2 TTS locally for speech generation, voice design from text, and voice cloning, with a clear list of where it falls short versus hosted APIs.

- Techniques: Prototype the voice in a hosted demo before any infra work; Local install and minimal generation script; Turn the model into a service behind the OpenAI speech API; Voice design from a persona description; Voice cloning from a short reference, with transcript; Set the output language explicitly for multilingual speech
- Tools: VoxCPM / VoxCPM2 (OpenBMB, Apache 2.0, ~2B params), PyTorch, torchaudio, Python, vLLM, Hugging Face (demo and checkpoint), macOS afplay, ComfyUI, GGUF, MLX (community paths mentioned), Chatterbox (TTS comparison), Qwen3-TTS (TTS comparison), ElevenLabs (hosted TTS comparison)

## [How China Is Running AI Coding Costs Into the Ground](../videos/Tl3QJk5G8pI.md)
`Tl3QJk5G8pI` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: models-research, token-cost-efficiency

Explainer on how DeepSeek V4Flash cuts long-context attention cost with sparse attention (summaries plus a cheap indexer), the reported economics, and the accuracy caveats.

- Techniques: Two-stage sparse attention with a cheap indexer; Multi-resolution context layout; Train with sparsity from the start, not prune afterward; Stable prompt prefix for cache hits; Speculative decoding with a small draft model
- Tools: DeepSeek V4Flash (284B total parameters, about 13B active per token, 4-bit weights), DeepSeek V4 paper (April, per the video), Native Sparse Attention (paper, Feb 2025), Lightning Indexer (DeepSeek sparse-selection component), OpenRouter (usage ranking), Gemini 3.1 Pro (pricing comparison), GPT-5 (pricing comparison), Claude Opus (retrieval test comparison), OpenAI API (80% price cut, per the video)

## [Qwen 3.8 27B + DFlash2: 140 Token/Sec?](../videos/H2oWD4WT7Os.md)
`H2oWD4WT7Os` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, models-research

A critical look at the DFlash2 speculative-decoding claims for Qwen 3.8 27B: the 3x headline uses a no-speculation baseline, against the built-in MTP it is about 23%, and it pays off mainly for single-user retrieval and edit-application workloads.

- Techniques: Check MTP is enabled before benchmarking any draft method; Benchmark speculative decoding across a concurrency sweep; Target speculative decoding at context-reproduction workloads; Choose a coherent candidate path instead of independent per-position argmax; Add depthwise convolutions around sublayers in a shallow drafter; Check the concurrency and block-size settings on Apple Silicon
- Tools: Qwen 3.8 27B, DFlash2 (DFLASH2 / D-Flash 2), DFlash1, dSpark, MTP (multi-token prediction), EAGLE-3 (only in the sense of prior art, not stated in video), vLLM, llama.cpp (PR 27342), Ollama (issue 17865), SGLang, MTBench, GGUF quants (mentioned as local model quants)

## [Claude Now Watermarks Its Text. How is it Possible?](../videos/cX0xI5FpH3U.md)
`cX0xI5FpH3U` · Kai Explains · 2026-09-02 · q4 · practitioner · news · also: security-guardrails, governance-compliance, models-research

Kai Explains on how Anthropic's text watermark works (sampler-side, keyed tournament sampling, no added characters), why detection and spoofing numbers are unpublished, and what engineers should actually do about it.

- Techniques: Tournament sampling for keyed watermarks; Keyed detection by re-deriving scores; Provenance by drafts and version history; Control the mark by running an open-weight model locally; Check provider support for provenance metadata before relying on it; Avoid invisible-character and character-swap tricks
- Tools: Claude (Anthropic API), Claude 4.7 (sampling parameter restriction mentioned), SynthID-Text (Google DeepMind; transcribed as 'Synth ID text'), Gemini (DeepMind watermark user study), GPTZero (transcribed as 'GPT-0'), Pangram, Turnitin, Amazon Bedrock, Google Cloud, Microsoft Foundry, C2PA-style signed provenance metadata (transcribed as 'C2 Pascal'), Digits of pi (Anthropic's Monopoly analogy)

## [Someone Built Ollama for Audio… and It Runs Locally](../videos/CvZuuKkT3Sw.md)
`CvZuuKkT3Sw` · Better Stack · 2026-09-02 · q3 · intro · review · also: local-ai, voice-multimodal

Walkthrough of Audio CPP, a month-old GGML single-binary runtime for about 30 local audio model families (TTS, STT, voice cloning, music); early and crash-prone, with speed claims measured only on NVIDIA.

- Techniques: Single-binary local audio runtime; OpenAI-compatible local audio server; Voice cloning from a short reference clip; Validate speed on your own hardware
- Tools: Audio CPP, GGML, llama.cpp, whisper.cpp, Ollama, Kokoro, Piper, FFmpeg, PyTorch, MLX, CUDA, Vulkan

## [How They Fixed AI's Biggest Local Hardware Problem (with FreeToken)](../videos/8n4Uo47CadY.md)
`8n4Uo47CadY` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: local-ai

Walkthrough of FreeToken, an open-source MoE inference engine that caches hot experts on the GPU, streams misses over PCIe, and splits misses between GPU and CPU; the speaker's 2.3x speedup over Ollama held only when the model overflowed VRAM.

- Techniques: Expert-cache over RAM-resident weights; Double-buffered expert streaming during prefill; Bandwidth-measured split of cache misses between GPU transfer and CPU compute; Load weights directly into runtime memory layout; Find the cache knee by shrinking the cache live; Test setup in OpenCode (as the speaker did)
- Tools: FreeToken (open-source MoE inference engine, CLI and desktop app; Windows/Linux desktop only), Ollama, llama.cpp, OpenCode, DeepSeek V4 Flash (284B total / 13B active, as stated), Qwen 3.6 35B (8-bit and 4-bit builds tested), NVIDIA RTX 5090 (32 GB VRAM), PCIe, DDR5 system RAM (64 GB)

## [Best Local AI Models For Every VRAM Tier](../videos/mn7CD0JjVpw.md)
`mn7CD0JjVpw` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: local-ai, token-cost-efficiency

Tier-by-tier guide to local LLMs by GPU VRAM (4GB to 24GB+). Pick the biggest quantized model that fits with context headroom, and set the context length explicitly to avoid KV-cache crashes.

- Techniques: Pick the biggest model that fits with context headroom; Prefer a smaller model at higher precision; Set the context length explicitly at model load; Split chat and autocomplete models; Use an MoE model on large-memory machines
- Tools: Ollama, LM Studio, llama.cpp (spoken as 'llama'; context-length crash anecdote), Phi-4-mini, Gemma 4 E2B (Gemma 4 family, ~April 2026 per the host), Qwen 2.5 7B, Qwen 3.5 9B, Qwen 3.6 27B, Qwen3-Coder-Next (80B MoE, ~3B active), Mistral 7B, Mistral Small, Llama 8B (captions read 'Llama 3.38b')

## [Best Hardware for Running Local LLMs in 2026: Mac vs NVIDIA vs Cloud](../videos/sR8sJ2mybQU.md)
`sR8sJ2mybQU` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, token-cost-efficiency, infra-cost-scaling

Kai Explains on picking local-LLM hardware in 2026 (Mac Studio vs RTX vs rented cloud GPUs), with measured vLLM vs llama.cpp and multi-GPU scaling results and a budget-based buying guide.

- Techniques: Pick the serving framework by VRAM headroom; Estimate decode speed from memory bandwidth, then confirm with your own benchmark; Pair MoE models with bandwidth-limited hardware; Cap consumer multi-GPU at two cards, or run one server per GPU; Breakeven check before renting or buying; Split work between local and frontier models
- Tools: Qwen3 Coder Next (80B MoE, Q4 about 46 GB, 70.6 SWE-bench as stated), Qwen 3.6 27B dense (16 GB, 77.2 SWE-bench as stated; transcript spells it 'Quen 3.627B'), Claude Sonnet 4.6, Claude Opus, GPT-4 (mentioned only as an example of a frontier API), vLLM, llama.cpp, Apple MLX, CUDA graphs, NVLink, PCIe, Mac Studio M4 Max 128 GB

## [China Is Coming for Your Local AI Box (XIAOMI AI Cube)](../videos/tjFNIQBFKMs.md)
`tjFNIQBFKMs` · Kai Explains · 2026-09-02 · q4 · practitioner · news · also: local-ai, models-research

Kai Explains on why local AI boxes are judged by memory bandwidth, not headline TFLOPS or tok/s, and how to read this week's Xiaomi, Alibaba and Apple announcements. Verdict: buy only for a specific model you need now.

- Techniques: Bandwidth-first sizing for local decode; Split prefill and decode benchmarks; Buying checklist for local AI hardware; Read claims by their conditions; Split generation and prefill across heterogeneous nodes
- Tools: DGX Spark (NVIDIA), RTX 5090, AMD Strix Halo, Mac Mini, Apple Mac Studio, Xiaomi AI Cube, Xiaomi O100 accelerator, Xiaomi D100 chip, CUDA, DeepSeek coding harness, Qwen, Kimi

## [Qwen 3.6 vs Nemotron 3.5 vs Muse Glimmer: The Real Test](../videos/GweZqgLxcCo.md)
`GweZqgLxcCo` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, evals

Practitioner head-to-head of Qwen 3.6, Nemotron 3.5 Lightning and Meta's Muse Glimmer on the host's own daily-digest workload: trick questions saturate, premise and pushback tests separate models, Nemotron wins long context, Qwen stays daily driver.

- Techniques: Premise-override trap; Sustained-pushback (spine) test; Needle-in-log long-context test; Benchmark hygiene checks; Agentic task with traps and side-effect checks; Measure total wall time, not per-step latency, for tool loops; Route models by workload
- Tools: Qwen 3.6 (27B), Nemotron 3.5 Lightning (NVIDIA; hybrid Mamba MoE, 32.9B parameters, 1M-token context), Muse Glimmer (Meta; 27.9B parameters, about 18 GB on disk), Q4 quantization, GPU inference (runtime not named), Host's custom benchmark harness (synthetic log, executable tool tasks, trick-question set)

## [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../videos/maRzp4kImJ4.md)
`maRzp4kImJ4` · AI Engineer · 2026-08-18 · q4 · deep · talk · also: training-finetuning-rl, infra-cost-scaling

Nan Jiang (Modal) argues RL rollouts can run on scattered, elastic GPUs across regions if the trainer syncs only a bit-exact sparse diff of serving-precision weights instead of full checkpoints.

- Techniques: Decoupled rollout islands; Bit-exact sparse weight diff; Versioned request contract; Sidecar version gate; Floor-based update-visibility check
- Tools: Modal, SGLang, vLLM, Adam, BF16, FP8, NVFP4, RDMA, Stitch

## [Why Large? Tiny LMs & Agents on Edge/Robotics — Cormac Brick, Google](../videos/hacEQHHhu2Q.md)
`hacEQHHhu2Q` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: local-ai, training-finetuning-rl

Google's Cormac Brick on running tiny (50M to 500M) and small (1 to 4B) models on phones, browsers and robots, and why fine-tuning on synthetic data beats bigger models for narrow tasks.

- Techniques: Synthetic-data fine-tuning of a tiny model for one task; Voice-to-function-calling pipeline; Two-stage on-device dictation pipeline; Memory budgeting for on-device LLMs; Multi-token prediction (MTP) for decode speed; Frame budgeting for NPU vision; Side-task tiny model
- Tools: LiteRT-LM, LiteRT / MediaPipe, Gemma 3, Gemma E2B, FunctionGemma, Gemma 4, AI Edge Gallery app, Apple FastVLM, Hugging Face (Mobile Actions dataset), Raspberry Pi, Jetson Nano, Qualcomm IoT boards (NPU)

## [Compression at the Edge — NVIDIA, Unsloth, HuggingFace, Ollama](../videos/J4_jCrTxMkk.md)
`J4_jCrTxMkk` · AI Engineer · 2026-08-18 · q4 · practitioner · panel · also: local-ai, evals

Panel from NVIDIA, Unsloth, Hugging Face and Ollama on how quantization and compression make large open models run on local hardware, how to pick per-layer precision, and how to evaluate the result.

- Techniques: Sensitivity-aware dynamic quantization; Post-training quantization first, QAD for small models; KL-divergence evaluation against the unquantized model; Harness-level vibe testing before shipping a quant; Per-model default quant with precision kept high for tiny models; Big planner, small executor routing
- Tools: llama.cpp, Ollama, Unsloth, NVIDIA Model Optimizer (ModelOpt), TRL, bitsandbytes, QLoRA, GRPO, NVFP4, MXFP4, OpenClaw, Hermes agent

## [The Desktop Frontier — Ahmad Osman, Osmantic](../videos/XV2oYi7kojc.md)
`XV2oYi7kojc` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: local-ai, models-research

Ahmad Osman argues that open-weight models are shrinking in hardware footprint fast enough that a GLM 5.2-class model should run on one RTX 5090 by late 2027, and urges people to own their hardware.

- Techniques: Footprint-over-time tracking; Dense small model for parallel local agents
- Tools: Claude Code, Telegram

## [The State of Model Routing — NVIDIA, Cognition, OpenRouter](../videos/QHBjufYK8TA.md)
`QHBjufYK8TA` · AI Engineer · 2026-08-18 · q3 · practitioner · panel · also: token-cost-efficiency, multi-agent, infra-cost-scaling

Panel from Cognition, NVIDIA and OpenRouter on model routing: frontier models plan and delegate to cheaper models, and the hard parts are detecting when a small model is out of depth and keeping cache costs low.

- Techniques: Frontier-planner, cheap-executor split; Frontier watcher with escalation; Persistent sidekick sub-agent; Reference-based handoff; Piggyback checks on cache refresh; Hidden-state probes for lost-ness; Routing from production signals; Ask the model why, then regression-test the prompt; Privacy-aware local/cloud split
- Tools: Devin, Cognition Fusion, OpenRouter Fusion, OpenRouter Pareto Code, NVIDIA Nemotron, NVIDIA Dynamo, NVIDIA DGX Spark, OpenClaw, TerminalBench, LMArena

## [Local Agentic Theory For Mobile Games — Shafik Quoraishee & Joanne Song, The New York Times](../videos/418t26CVz-w.md)
`418t26CVz-w` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: local-ai, agent-architecture, product-ux

NYT engineers on running small agents on-device inside mobile games, under per-frame time, memory and battery budgets, with live accessibility tuning through graded dials instead of fixed menus.

- Techniques: Per-frame perceive-predict-decide-act agent loop; Constraint graph over space, time and energy; Constraint satisfaction with backtracking; Graded accessibility dials driven by live signals; Live focus-path monitoring and layout auditing
- Tools: Efficient Zero V2 (sample-efficient RL, mentioned as state of the art up to 2024), WCAG 2.2 and WCAG 3.0 draft, Gaze estimation CNN, Google SIMA (transcript reads 'SEMA'; generalist agent framework mentioned briefly)

## [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It — Dan Fu and Olive Song](../videos/AVMr9PMINyo.md)
`AVMr9PMINyo` · AI Engineer · 2026-08-18 · q3 · practitioner · panel · also: models-research, training-finetuning-rl, evals

A MiniMax and Together AI panel on how an open-weight model like MiniMax M3 gets trained, then served at scale, with day-zero kernel work, agentic KV-cache demands and long-horizon RL evals.

- Techniques: Day-zero kernel plus post-launch optimization queue; Benchmark unsolved kernel problems as RL environments; Multi-submission long-horizon evals with held-out validation; Multimodal training from step zero; KV cache as a distributed store; Cross-model optimization transfer
- Tools: KernelBench, Parallel KernelBench, OSWorld, SVG bench, MiniMax sparse attention

## [Laguna S 2.1: The Best Local Model? Beats GLM 5.2](../videos/YRlM9V_3mR8.md)
`YRlM9V_3mR8` · Kai Explains · 2026-08-02 · q4 · practitioner · review · also: local-ai, models-research, token-cost-efficiency

Kai reviews Poolside's Laguna S 2.1, an open-weight 118B MoE model with 8B active that runs on one desktop-class box; it beats GLM 5.2 on some coding benchmarks but not all, and the launch numbers are unverified.

- Techniques: Run a MoE model that exceeds VRAM by offloading expert layers to system RAM (llama.cpp); Single-box 4-bit serving on unified memory; Enable max thinking only for hard agentic tasks; Test an open model on your own repo before adopting it
- Tools: Laguna S 2.1 (Poolside, open weights, OpenMDW license), Laguna XS (tinier sibling; captioned 'XS5'), GLM 5.2 (Chinese open model, about 740B), DeepSeek (largest model cited, about 1.6T), Qwen and Kimi (named as Chinese open-model families), Claude (Anthropic, closed frontier comparison), NVIDIA DGX Spark (128 GB unified memory desktop), llama.cpp (GGUF, IQ4_XS quant, expert-layer offload), Ollama (captioned 'Alama'), vLLM, SGLang, OpenRouter (hosted)

## [This Tiny Engine Runs Impossibly Big AI Models Locally! (colibrì)](../videos/3OqZHYNKc9A.md)
`3OqZHYNKc9A` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: local-ai

Better Stack tests colibrì, a pure-C engine that streams a 744B MoE model (GLM 5.2) from SSD, on a MacBook and a RTX 5090 workstation. Result: it works, but speed is bounded by RAM, not the GPU.

- Techniques: Expert streaming with a RAM-resident dense core; Routing-frequency pinning; Compute-versus-wait profiling per turn; Token-exact validation of a streamed or quantized path; Speculative decoding via the native MTP head
- Tools: colibrì (transcribed as Calibri), pure-C local inference engine by Vincenzo Fornaro, zero external dependencies, GLM 5.2 (744B-parameter MoE language model, about 357 GB on disk, about 40B active per token), MLA (multi-head latent attention) compressed KV cache, Multi-token prediction head (speculative decoding), Apple MacBook M2 Max, 32 GB RAM, NVIDIA RTX 5090, 64 GB RAM workstation, Samsung portable SSD over USB (about 1 GB/s)

## [Qwen 3.6 + DFlash Is INSANE (Beats Claude + 6x Faster + OpenSource)](../videos/JmPS3eLTejY.md)
`JmPS3eLTejY` · Kai Explains · 2026-08-02 · q2 · intro · news · also: local-ai, models-research, token-cost-efficiency

Kai Explains on Alibaba's open-weight Qwen 3.6 coding model and Z Lab's DFlash speculative-decoding drafter; claims near-Opus benchmark scores and up to 6x speedup, with few independent checks.

- Techniques: Parallel block drafter for speculative decoding (DFlash-style); Confidence-gated verification; Load-adaptive draft length; Validate the drafter before trusting a speedup; Swap the model behind an agent harness via base URL
- Tools: Qwen 3.6 (Alibaba Qwen Lab), DFlash (Z Lab; transcribed 'D-Flash'), Claude Opus 4.8, GPT 5.5, Claude Code, vLLM, Hugging Face, NVIDIA recipe (transcribed 'NAMO', name uncertain), DeepSeek (baseline reference), Apache 2.0 license, Frontier SWE (benchmark), SWE-Bench Pro (benchmark; transcribed 'WeBench Pro')

## [Best Local AI Models For Your Every GPU 2026](../videos/mtk8p8czzDU.md)
`mtk8p8czzDU` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: local-ai, models-research

Kai Explains picks one local model per GPU memory tier (4-8, 8-24, 24-96, 96-192, 192-384 GB): NanBeige 4.2, Bonsai, Qwen 3.6 27B with Thinking Cap, Laguna S2.1 and Motif 3.

- Techniques: Tier-based model selection by VRAM or unified memory; Looped transformer for small models; Ternary retraining instead of post-training quantization; Fine-tune for shorter reasoning traces (Thinking Cap); Serving sparse MoE models locally; Local quickstart with Ollama or LM Studio
- Tools: Ollama, LM Studio, MLX, CUDA, vLLM, SGLang, llama (speaker says 'point a llama at it'; runtime not named precisely), OpenClaw, Hugging Face, Artificial Analysis, Terminal Bench, SWE-bench Verified (captioned as 'CWBench verified')

## [How This Tiny $8 Chip Runs an LLM With Almost No RAM](../videos/0qXVMt3pIjU.md)
`0qXVMt3pIjU` · Better Stack · 2026-08-02 · q3 · practitioner · tutorial · also: local-ai, models-research

Better Stack walks through running a 28.9M-parameter TinyStories language model on an ~$8 ESP32-S3 microcontroller by keeping the big embedding table in flash and only streaming the rows each token needs.

- Techniques: Keep the embedding table in flash, stream rows on demand; Plain-C inference in llama2.c style on bare metal; Train a tiny model on a narrow dataset; Single-script build pipeline for embedded ML; Pick the board by flash size first
- Tools: ESP32-S3 (N16R8 variant: 16 MB flash, 8 MB PSRAM), Gemma (source of the per-layer embedding idea), TinyStories dataset (Microsoft research), llama2.c (Karpathy), Plain C toolchain for ESP32, MacBook (used for training, about 13 minutes)

## [Is MOJO actually better than NVIDIA's CUDA?](../videos/KL7pMJ2nkAk.md)
`KL7pMJ2nkAk` · Kai Explains · 2026-08-02 · q3 · intro · review · also: dev-tools, models-research

Analysis of Qualcomm's $3.9B all-stock acquisition of Modular and whether the Mojo language can dent NVIDIA's CUDA moat; the verdict is that Mojo is not faster than CUDA today but wins on portability.

- Techniques: Benchmark vendor speedup claims against an optimized baseline; Score hardware-software stacks on separate axes; Assess neutrality risk after an acquisition
- Tools: Mojo, Modular MAX, CUDA, NumPy, LLVM, Clang, Swift, MLIR, TensorFlow Lite, XLA, ROCm, Triton

## [DFlash Just Made AI 6x Faster : DFlash, DeepSpec Explained](../videos/x9MuyVOtX78.md)
`x9MuyVOtX78` · Kai Explains · 2026-08-02 · q4 · practitioner · review · also: local-ai

Walkthrough of DFlash, a diffusion-drafter speculative decoding method merged into llama.cpp for Qwen 3.6, with local deployment steps and a self-run benchmark that checks whether the "lossless" claim holds.

- Techniques: Lossless-check benchmark protocol for speculative decoding; Deploy DFlash locally with llama.cpp server in Docker; Side-by-side leaderboard of baseline, MTP and DFlash; Tune drafter quantization and draft-token count; Decide by whether the GPU is idle at your concurrency
- Tools: DFlash, llama.cpp (llama CPP), Docker, EAGLE-3, MTP (multi-token prediction), Qwen 3.6 family (Qwen 3.8B build as transcribed), AIPerf, MATH-500, RTX 6000 Pro, vLLM, SGLang, DeepSpec (named in the video title; not explained in the transcript)

## [Google Shrunk 31GB of AI Memory Down to 4GB (TurboQuant)](../videos/dfMeOTLSar8.md)
`dfMeOTLSar8` · Kai Explains · 2026-08-02 · q3 · practitioner · news · also: rag-retrieval, token-cost-efficiency, local-ai

Explains TurboQuant, Google's training-free vector compression (31GB to about 4GB for 10M vectors), the independent TurboVec build, and KV-cache gains. Google published math only, not a supported product.

- Techniques: Data-oblivious rotate-and-round quantization; 1-bit residual sign correction (QJL); Filtered search inside the distance kernel; Same rotation applied to the KV cache; Adoption rule of thumb
- Tools: TurboQuant (Google research, published as a paper; no official product), TurboVec (Rust library with Python bindings, by Ryan Kodry; version not stated), FAISS FastScan (Meta; named in the transcript as 'face fast scan'), Qdrant (vector database; now ships the rotation trick, per the speaker), LangChain, LlamaIndex, Lloyd-Max quantizer, QJL (1-bit residual method), Product quantization (background concept, not used)

## [Kimi K3 + DSpark Is INSANE (Beats Claude + 3x Faster + OpenSource)](../videos/cGhT8G408lA.md)
`cGhT8G408lA` · Kai Explains · 2026-08-02 · q3 · practitioner · news · also: models-research, local-ai, token-cost-efficiency

Open-weight Kimi K3 is pitched as near-frontier for coding, and a dSpark speculative-decoding drafter claims 3.14x faster output with identical tokens. The talk includes useful caveats on acceptance rate, hardware and hallucinations.

- Techniques: Speculative decoding with a block-diffusion drafter and confidence-gated verification; Train the drafter on hidden states from the serving engine; Match the drafter's attention design to the target's to share KV layout; Track cost per completed task instead of per-token price; Swap the model behind an existing agent harness via base URL
- Tools: Kimi K3 (Moonshot AI), Kimi K2.6, Kimi Delta Attention, dSpark (Infraact drafter), vLLM, Claude Code, Cursor, Cline, Claude Opus 4.8, Claude Fable 5, GPT 5.6 Sol, DeepSeek V4 Pro

## [Google Just Made TensorFlow.js Obsolete (LiteRT.js)](../videos/8c68vFpT9Tk.md)
`8c68vFpT9Tk` · Better Stack · 2026-08-02 · q3 · intro · review · also: local-ai, dev-tools

Better Stack walks through LiteRT.js, Google's WebAssembly on-device inference runtime for browsers, and builds a client-side webcam pose-capture app to test its CPU and WebGPU speed against TensorFlow.js.

- Techniques: Select a backend per device tier; A/B the backends on your own hardware before trusting vendor numbers; Port existing models instead of rewriting them; Client-side webcam pose pipeline; Export pose recordings for retargeting
- Tools: LiteRT.js, LiteRT, TensorFlow.js, WebAssembly, XNNPack, ML Drift, WebGPU, WebNN, LiteRT Torch, AI Edge Quantizer, LiteRT-LM.js (announced, not shipped), BlazePose

## [OpenCV 5 Is Here - The Biggest Update Since 2018 (We Tested It)](../videos/piHpZWcgQyc.md)
`piHpZWcgQyc` · Better Stack · 2026-08-02 · q3 · intro · review · also: local-ai, dev-tools

Better Stack tests OpenCV 5's rewritten CPU-only DNN engine (ONNX operator coverage 22% to 80%) on colorization, detection, diffusion inpainting and VLM captioning; only detection looks practical.

- Techniques: Choose the DNN engine by backend need; Benchmark a vendor speed claim on your own model before switching; Tune diffusion inpainting steps to trade artifacts for latency
- Tools: OpenCV 5, OpenCV 4 (classic DNN engine), ONNX Runtime, PyTorch, YOLOv8, OWLv2, PaliGemma, Gemma 4 (12B, run locally), CUDA, OpenVINO, C++17

## [The Best Local AI Hardware (APPLE M5 MAX vs NVIDIA DGX SPARK)](../videos/4kuS_1y-nqc.md)
`4kuS_1y-nqc` · Kai Explains · 2026-08-02 · q3 · intro · review · also: local-ai

Compares Apple Mac Studio, NVIDIA RTX 5090 and DGX Spark for local LLMs through memory capacity, bandwidth and compute. Main takeaway: decode speed follows memory bandwidth, so size the model first, then pick hardware.

- Techniques: Fit-first sizing before hardware choice; Bandwidth-bound decode estimate (derived); Local hardware decision tree; Hybrid local and cloud split
- Tools: NVIDIA GeForce RTX 5090, NVIDIA GeForce RTX 4090, NVIDIA DGX Spark, Apple Mac Studio, Apple M3 Ultra, CUDA

## [Local AI On Apple Silicon uses 7X Less RAM](../videos/vHhephsP6vU.md)
`vHhephsP6vU` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: local-ai

Better Stack walks through Turbo Fieldfare, a Swift/Metal Mac app that runs a 26B Gemma 4 mixture-of-experts model in about 2 GB of RAM by streaming expert weights from SSD on demand.

- Techniques: Resident/streamed weight split for MoE models; Zero-copy SSD-to-GPU loading on unified memory; Store weights in the kernel's native quantized layout; Overlap I/O with always-resident compute; Per-layer LFU expert cache; Turbo Fieldfare setup steps shown (no exact commands)
- Tools: Turbo Fieldfare (Swift/Metal Mac app, repo linked in video description; no version stated), Gemma 4 (26B-parameter mixture-of-experts model), Swift, Metal (Apple GPU API), Apple Silicon (M3 Max used for the benchmark)

## [Run KIMI K3 on Your Laptop Locally (No GPU Needed)](../videos/tjdCBCr4qhQ.md)
`tjdCBCr4qhQ` · Kai Explains · 2026-08-02 · q4 · practitioner · news · also: models-research, local-ai

Kimi K3's 2.8T-parameter open weights run on a 2021 M1 Max via the DeltaFin project, which streams routed experts from disk at 14.6 s/token. Covers MXFP4 quantization-aware training, hybrid attention, quant trade-offs, and the serving-hardware gap.

- Techniques: Expert streaming from disk with a resident spine; Selective mixed-precision quantization for MoE; Quantization-aware training instead of post-hoc quantization; Measure a quant ladder by next-token agreement; Fused dequantize-and-matvec kernel; Deterministic decoding with lossless n-gram speculation; Architecture-level KV cache reduction with hybrid attention
- Tools: Kimi K3 (Moonshot AI), DeltaFin (MIT-licensed local inference project, 274 stars at recording), Unsloth quants (UD-IQ1_S, 1-bit M, 2-bit XXS, 2-bit XL, 4-bit, 8-bit), MXFP4 (4-bit block floating point), Kimi Delta Attention, Apple M1 Max (64 GB), Apple Silicon NEON, x86 AVX2, NVIDIA DGX Spark, NVIDIA B300 (8-way node), CUDA, Hugging Face

## [What Would It Cost to Run Claude Fable 5 Locally?](../videos/fXWFSTSvnVM.md)
`fXWFSTSvnVM` · Kai Explains · 2026-08-02 · q3 · intro · other · also: local-ai, infra-cost-scaling

Back-of-envelope memory and concurrency math on what it would take to self-host a frontier-scale open model (Kimi K3 as a stand-in for Claude Fable 5): a Mac Studio or 4xH100 cannot hold it, and serving 100 people is a data-center sizing problem.

- Techniques: Weight memory floor estimate; Concurrency sizing from arrival rate and service time; Hybrid local and cloud routing; Rent-before-buy pilot
- Tools: Claude Fable 5 (Anthropic model; weights not public, used only as the question), Kimi K3 (open-weight model, 2.8T parameters, MXFP4 weights as stated; used as the sizing example), NVIDIA DGX B200 (8x B200 GPUs, 1.44 TB GPU memory), NVIDIA DGX B300 (8x B300 GPUs, about 2.3 TB GPU memory), NVIDIA H100 (80 GB each, 4 units discussed), Apple Mac Studio (up to 512 GB unified memory), MXFP4 (4-bit weight format, called MXFFP4 in the auto-captions)

## [Mojo is Quietly Replacing Python in AI](../videos/zuDmoLI1dZc.md)
`zuDmoLI1dZc` · Kai Explains · 2026-08-02 · q2 · practitioner · news · also: dev-tools, models-research

Kai Explains argues Qualcomm's reported $3.9B Modular deal makes Mojo a threat to the Python-plus-CUDA ML stack, while flagging vendor-only benchmarks, a closed compiler and missing MoE support.

- Techniques: Triage performance claims by evidence type; Check model-architecture coverage before reading benchmarks; Incremental migration via Python interop
- Tools: Mojo (1.0 Beta 1, shipped May 7 per 4:03; the intro says about three weeks before June 24), Modular Platform 26.2, Modular (company, acquired by Qualcomm per the video), MLIR (captioned as MLR), LLVM / LLVM IR, Clang, Swift, CUDA, CPython, PyTorch, NumPy, Python

## [What Would It Cost to Run Kimi K3 Locally?](../videos/ni5P3gT8OXo.md)
`ni5P3gT8OXo` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: local-ai, infra-cost-scaling

Napkin math for running Kimi K3 locally: ~1.5 TB of 4-bit weights rules out Mac Studio and 4xH100, 8xB200 is barely enough, and serving 100 users is a data-center project.

- Techniques: Weight memory estimate for a quantized model; Headroom budget for a serving node; Concurrency sizing instead of user counting; Peak-moment plus prompt-length sizing; Hybrid routing: local for routine, cloud for hard; Rent before you buy
- Tools: Kimi K3, Hugging Face, Mac Studio, NVIDIA H100, NVIDIA B200, NVIDIA B300, NVIDIA DGX B200, NVIDIA DGX B300, MXFP4 (4-bit format, as named in transcript), Claude, GPT

## [This Could Change Local AI Forever](../videos/W_rROyZKEYY.md)
`W_rROyZKEYY` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: local-ai, models-research

Prism ML's Bonsai 27B compresses a 27B model to 5.9 GB (ternary) or 3.9 GB (1-bit); the speaker says the 1-bit build is a headline and the ternary build is the usable one, with agentic quality falling notably.

- Techniques: Group-scaled low-bit weight quantization; On-device memory budgeting beyond file size; Capability-split regression check before swapping a local model; Local-first routing with cloud escalation; Validate speed in your own runtime
- Tools: Bonsai 27B (PrismML), Qwen 3.6 27B (base model), GGUF runtimes, Q4 / Q5 / Q8 quantizations, speculative decoding, RTX 5090, Apple M5 Max, iPhone (12 GB RAM reference device)

## [Mojo + Vulkan is INSANE: Run Local AI on ANY GPU (Goodbye CUDA)](../videos/CbNrKGMDM7g.md)
`CbNrKGMDM7g` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: local-ai, dev-tools

Kai Explains argues Vulkan (llama.cpp) and Mojo are weakening the CUDA lock-in, so local AI runs on AMD, Intel, Apple and iGPU hardware, with CUDA still fastest at the top end.

- Techniques: Run local models on a non-NVIDIA GPU via llama.cpp Vulkan backend; Benchmark Vulkan against the vendor stack on the same hardware; Write a GPU kernel once in Mojo and compile per vendor; Compare a rewritten kernel to a vendor-tuned kernel on the same chip
- Tools: CUDA, Vulkan, llama.cpp, ROCm, Metal, SYCL, MoltenVK, Mojo, Modular, PyTorch, TensorFlow, JAX

## [SeFI image, Leanstral Beats Every Math AI, Hy3 Challenges GPT, Agents A1 & Bytedance AI News](../videos/rVwK1fuzKJU.md)
`rVwK1fuzKJU` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, training-finetuning-rl, local-ai

Weekly Kai Explains roundup of late-July 2026 open-model releases: Mistral Leanstral 1.5 (Lean 4 prover), Tencent HY3, InternScience Agents A1, CeFi Image, ByteDance Depth Anything 3 and GenRecon. Mostly release-announcement content with a few concrete numbers.

- Techniques: Test-time compute scaling for formal provers; Property-generation plus formal proof as a bug finder; Semantic-first two-stream diffusion
- Tools: Leanstral 1.5, Lean 4, Lean language server, CISPO, Mistral Vibe, Hugging Face, Tencent HY3, Hunyuan 3, CodeBuddy, WorkBuddy, Tencent Cloud, OpenRouter

## [China Drops LongCat, Anthropic Fires Sonnet 5, Google Omni Flash & Robots Learn to Vibe Code AI News](../videos/RgREa6QEsgA.md)
`RgREa6QEsgA` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, token-cost-efficiency, mcp-and-tools

Weekly AI news roundup (Aug 2026): Meituan's LongCat 2.0, Claude Sonnet 5, Google's Nano Banana 2 Lite and Gemini Omni Flash, Booster Studio for robots, Claude Science, and ComfyUI's Claude MCP.

- Techniques: Comfy Cloud MCP setup for Claude Code and Claude Desktop; Two-stage cheap-then-expensive media pipeline; Dedicated reviewer agent for research outputs; Use anonymous or stealth router listings as an adoption signal
- Tools: LongCat 2.0 (Meituan, 1.6T MoE, MIT license), GPT 5.5 (comparison baseline), Claude Sonnet 5 (model string as spoken: Claude-Sonnet-5), Claude Opus 4.8 (comparison baseline), Claude Sonnet 4.6 (comparison baseline), Claude Code, Claude Desktop, ComfyUI / Comfy Cloud MCP, ComfySkills Marketplace, ComfyCloud plugin, Nano Banana 2 Lite, Nano Banana (original)

## [Local AI Just Hit the Tipping Point (Colibri)](../videos/_2knU_H8XwU.md)
`_2knU_H8XwU` · Kai Explains · 2026-08-02 · q4 · practitioner · review · also: local-ai, models-research

Walkthrough of Colibri, a one-person C engine that runs the 744B-parameter MIT-licensed GLM 5.2 on a 25GB laptop by streaming MoE experts from disk; honest speed is about 0.05 to 0.1 tokens/s.

- Techniques: Stream MoE experts from disk through a per-layer LRU cache; Learned hot-expert pinning across sessions; Quantize the MTP head to int8 for speculative decoding; Shard-by-shard FP8 to int4 conversion with resumable progress; Colibri reproduction steps (from the video)
- Tools: Colibri (single-file C inference engine for GLM 5.2; .coli model format), GLM 5.2 (ZAI, MIT license, 744B-parameter MoE, FP8 checkpoint about 756GB), GCC, OpenMP, AVX2, Unsloth 2-bit quantization (about 240GB), Ollama (its glm 5.2 cloud tag routes to ZAI's cloud API, not local inference), llama.cpp (runs GLM 5.2 with a dense attention fallback; DSA sparse attention not in mainline), DS4 (disk-streaming approach by the Redis creator, referenced as independent work), WSL2 with VHDX, Hugging Face (pre-built int4 checkpoint), Mac Studio (256GB, Unsloth 2-bit reference)

## [MAX + Mojo Are Quietly Replacing Python in AI](../videos/fOj8TgAdDGE.md)
`fOj8TgAdDGE` · Kai Explains · 2026-08-02 · q3 · intro · news · also: dev-tools

Kai Explains argues Mojo, Modular's Python-syntax compiled language, could remove the research-to-kernel handoff, with the Qualcomm acquisition as context and caveats on MoE support and vendor benchmarks.

- Techniques: Check architecture coverage before trusting a portable-kernel benchmark; Separate vendor claims from independent evidence
- Tools: Mojo (1.0 Beta 1), Modular Platform (26.2), MAX (named in the video title), MLIR (captioned as MLR), LLVM, Clang, Swift, CUDA, PyTorch, NumPy, CPython, llama.cpp

## [How to Run Qwen's 36B Model Locally on Laptop](../videos/C4tQLOqYsXw.md)
`C4tQLOqYsXw` · Kai Explains · 2026-08-02 · q3 · practitioner · tutorial · also: local-ai, models-research

Kai walks through running Qwen's 35B-total / 3B-active MoE coding model locally via Ollama, with hardware tiers, context-length and tool-calling gotchas, and an honest caveat on the SWE-bench headline.

- Techniques: Serve a local coding model with Ollama behind an OpenAI-compatible endpoint; Raise Ollama's context length before agentic use; Pass the Jinja flag when running llama.cpp directly; Choose the model variant by VRAM and workload; Budget KV cache against context length
- Tools: Qwen 3.6 35B-A3B (MoE, 35B total / 3B active, Apache 2.0), Qwen 3.6-plus (proprietary cloud model, not locally runnable), Qwen dense 27B, Gemma 4 (dense 31B and a local model cited at 52% SWE-bench), Claude Sonnet 4.5 (comparison, 77.2% on public harness), Ollama, LM Studio, MLX, llama.cpp (Jinja flag), Unsloth GGUF builds, Hugging Face, Cline (captioned 'Klein')

## [OpenClaw in Your Hand: Building a Physical AI Terminal - Lech Kalinowski, Callstack](../videos/akk6KRlcwW4.md)
`akk6KRlcwW4` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: local-ai, product-ux

Callstack engineer Lech Kalinowski builds a handheld text-terminal for OpenClaw and local LLMs on an ESP32, with a thin-client design backed by a 120B model on a DGX Spark. Mostly a hardware showcase with useful field notes.

- Techniques: Thin-client MCU with a heavy backend; Pre-allocated one-bit page buffers; Dual-display split by job; OpenAI-style proxy in front of open models; Graceful degradation across hardware parts
- Tools: OpenClaw, ESP32, NVIDIA DGX Spark, NVIDIA serving stack (auto-caption: 'Tensor Earth'), OLED display, e-paper display

## [State of the Union: Why Local, Why Now — NVIDIA, Osmantic, Roboflow, EXO Labs, @matthew_berman](../videos/KB41dTlX1Uc.md)
`KB41dTlX1Uc` · AI Engineer · 2026-07-18 · q3 · intro · panel · also: local-ai, training-finetuning-rl, models-research

Panel on why local AI is now practical: multi-model setups, frontier-plans/local-executes splits, distilling big-model consensus into small specialized models, and the remaining UX and openness gaps.

- Techniques: Plan with frontier, execute with local; Consensus distillation; Drop open-vocabulary machinery when classes are fixed; Trace-driven model routing; Retune existing configs for small hardware; Hardware-aware model selection; Frontier bootstrap then open model
- Tools: vLLM, SGLang, Local.ai, ODS (open-source deployment system), DGX Spark, DGX Station, Brev, Segment Anything 3 (SAM3), Cursor, Codex, Llama, Qwen 3.5 / 3.6

## [Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth](../videos/uIiA6DquRiE.md)
`uIiA6DquRiE` · AI Engineer · 2026-07-18 · q4 · practitioner · workshop · also: evals, training-finetuning-rl, models-research

Daniel Han (Unsloth) workshop on benchmark reliability, harness and inference-provider accuracy drift, dynamic quantization, torch.compile over handwritten kernels, and reward hacking in RL and coding agents.

- Techniques: Repeated sampling with reliability math; Rolling-average regression canary for a hosted agent; Benchmarks with unbounded instance space and programmatic verifiers; Single controlled harness for model comparisons; Calibration-based dynamic quantization; Per-provider accuracy check before adopting an inference endpoint; Open-weight baseline on llama.cpp or llama-server; torch.compile-first performance tuning with randomized bisection over flags; Audit RL and agent runs for reward hacking
- Tools: Unsloth, Hugging Face, Math-Verify (Hugging Face), llama.cpp / llama-server, PyTorch, torch.compile, Triton, CUDA, FlashAttention (FA2, FA3, FA4 mentioned), Claude Code, OpenAI Codex, Gemini CLI

## [Frontier results, on device - RL Nabors, Arize](../videos/fWXJM-J0ZB8.md)
`fWXJM-J0ZB8` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: local-ai, evals, context-engineering

Rachel Lee Neighbors shows how to right-size a model: prototype with a frontier model, build a golden eval set, then pick the smallest local model (Llama 3.2 3B) that meets latency and quality targets, closing the gap with prompt changes and deterministic post-processing.

- Techniques: Prototype-big-deploy-small pipeline; Golden dataset with multi-metric eval in Phoenix; Latency budget by percentile; Single-variable prompt ablation; Deterministic post-processing instead of prompt tuning; Auditing the LLM judge; Regression evals in CI
- Tools: Phoenix (Arize), Goose, Gemma 4 E2B, Gemma 3, Llama 3.2 3B, Qwen 2.5 1.5B, Qwen 3 1.7B, Claude Sonnet, Claude Opus, MobileNet, YOLO, MediaPipe

## [1,000+ Tokens/Sec: Google Just Shattered the AI Speed Limit (DiffusionGemma)](../videos/Dxn3BcSgsMY.md)
`Dxn3BcSgsMY` · Better Stack · 2026-07-02 · q3 · intro · review · also: models-research, local-ai, coding-agents

Better Stack walks through Google DeepMind's DiffusionGemma, a diffusion-style text model that refines a 256-token canvas in parallel, and tests its speed on an H100 via RunPod and OpenCode.

- Techniques: Parallel canvas refinement (non-autoregressive decoding); Uniform-state corruption for text diffusion; Encoder/denoiser mode split with bidirectional denoising; Run DiffusionGemma on RunPod and read the endpoint; Point OpenCode at the remote DiffusionGemma server; Local serving with vLLM in Docker; Read throughput from the server logs
- Tools: DiffusionGemma, Gemma 4 (26B base), OpenCode, vLLM, Docker, RunPod, NVIDIA H100, NVIDIA RTX 5090, Hugging Face

## [Character swap live streaming, 3D mesh generator,  Google's DiffusionGemma & More AI News](../videos/73iY1aGFSYI.md)
`73iY1aGFSYI` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, local-ai, coding-agents

Weekly open-source AI news roundup: Meta's MeshFlow mesh generator, Google's DiffusionGemma block-diffusion LM, Cohere's North Minicode coding model, plus robotics and webcam mocap releases.

- Techniques: Block-wise denoising decoding with confidence-based re-noising; Generate structured geometry as a continuous latent with a parallel diffusion transformer; Self-supervised quality scoring via pairwise majority voting; Shared keypoint conditioning across embodiments
- Tools: MeshFlow, Gradio, Hugging Face, Blender, Maya, DiffusionGemma, Gemma 4, GGUF, Kaggle, Vertex AI, North Minicode, open code

## [3,000+ Tokens Per Second? Let's Stress Test Xiaomi's New Model: MiMo V2.5 Pro UltraSpeed](../videos/HfRVXadseCo.md)
`HfRVXadseCo` · Better Stack · 2026-07-02 · q3 · intro · review · also: models-research, vibe-coding-app-building

Better Stack stress-tests Xiaomi's MiMo V2.5 Pro UltraSpeed, claimed at 1000+ tok/s on a 1T MoE from one 8-GPU server; peaks near 3451 tok/s, with broken or frozen app outputs.

- Techniques: Precision exceptions with quantization-aware training for large MoE weights; Block-parallel drafting for speculative decoding (DFlash); Persistent kernel with warp specialization; Fixed-prompt generation speed and output sweep
- Tools: MiMo V2.5 Pro UltraSpeed (Xiaomi model; the speaker says 'Ultra Speed'), TileRT (systems partner, persistent-kernel engine), MXFP4 (4-bit weight format), QAT (quantization-aware training), DFlash (block-parallel speculative drafting), Three.js (used for the Subway Surfers clone), LeetCode (source of the hard algorithm test), GPT 5.5 (comparison only), Claude 4 Opus (comparison only), Diffusion Gemma (earlier Better Stack video referenced, not used)

## [Claude Fable 5, Grok imagine 1.5, Gemini Live Translate, HumanEgo Robot, Mirage World Model AI News](../videos/ibGW_YqQmLg.md)
`ibGW_YqQmLg` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, voice-multimodal, training-finetuning-rl

Kai Explains weekly AI news roundup (2026-07-02): Claude Fable 5 and Mythos 5, Grok Imagine 1.5, N2 Pro, Quasar, LeVar, vLLM-Omni, HumanEgo, SCAIL 2, Gemini 3.5 Live Translate, Mirage. Mostly vendor and paper claims relayed without testing.

- Techniques: Adaptive thinking gate; Sensitive-category model routing; Persistent file-based memory for long agent runs; Latent-space scene memory (Mirage); Interaction-centric tokens for cross-embodiment policies (HumanEgo); Skeleton-free motion transfer (SCAIL 2); Geometry from a 4D reconstruction model as a video-diffusion condition (LeVar)
- Tools: Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, Claude Mythos Preview, Project Glasswing, Grok Imagine 1.5, xAI API, N2 Pro (SII), N2 Mini, Qwen 3.5, OpenRouter

## [Reachy Mini: the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face](../videos/0jeZfjJMfmo.md)
`0jeZfjJMfmo` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: voice-multimodal, infra-cost-scaling

Hugging Face's Andres Marafioti on the open-source $300-450 Reachy Mini robot, its voice pipeline, and how a streaming TTS model was made fast enough for real-time voice agents.

- Techniques: Stream TTS audio instead of generating full utterances; Static KV cache plus graph capture for autoregressive audio models; Partial STT every 150 ms; Separate scaling of LLM inference from stateful conversation nodes; Measure the whole latency path, not just the model; Codex-driven hardware app development
- Tools: Reachy Mini, Raspberry Pi, Codex, Parakeet, Qwen3-TTS, Qwen 3.5 27B, Kokoro, Voxtral, Hugging Face Inference Endpoints, speech-to-speech pipeline, GPT Realtime

## [Text Diffusion — Brendan O’Donoghue, Google DeepMind](../videos/r305-aQTaU0.md)
`r305-aQTaU0` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: models-research, token-cost-efficiency

Google DeepMind researcher explains text diffusion as a low-latency, non-autoregressive alternative to next-token LLMs, covering why it is fast, self-correcting, and adaptive, plus its throughput cost.

- Techniques: Discrete corruption and denoising training; Latency-first serving by block; Test-time compute via denoising steps; Self-correction through reason-then-revise; In-place infilling and editing
- Tools: Gemini Diffusion, Gemini 2.0 Flash-Lite, Gemini 2.5 Flash, GPT-4o, Gemini (autoregressive baseline, unnamed version), Nano Banana (named as a later image model), Juno (named as the image model at the time; caption may be garbled), GPQA Diamond (eval), MBPP (eval)

## [20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna](../videos/hqHC6Z_lXyo.md)
`hqHC6Z_lXyo` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: evals, models-research

Public leaderboards and manual or metric-based checks mislead model choice; the speaker argues for task-specific, many-sample evals plus Pareto fronts of quality vs latency and cost, where smaller fast models often win.

- Techniques: Pareto front selection; Consensus across leaderboards and per-task boards; Large-sample, condition-matched human evaluation; Metric validation before use; Compression for latency (quantization, pruning, step reduction)
- Tools: Design Arena, LM Arena (now Arena), Artificial Analysis, CLIP score, Pruna open-source compression package

## [Fast Models Need Slow Developers — Sarah Chieng, Cerebras](../videos/TeGsFFNqRLA.md)
`TeGsFFNqRLA` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: coding-agents, testing-verification, context-engineering

Cerebras's Sarah Chieng argues that fast coding models (Codex Spark, ~1,200 tok/s) demand new habits: plan with a large model, execute with a fast one, verify every step, and keep context in bounded goals.

- Techniques: Planner-executor model split; Session-to-skill distillation; Per-step automatic verification; Parallel variant generation with cherry-picking; Scoped steering constraints; Automatic refactor pass after each task; Bounded goals with a context budget; Four-file external memory (AGENTS/PLAN/PROGRESS/VERIFY)
- Tools: Codex Spark, Codex, GPT-5.4, GPT-5.3 Codex, Sonnet, Opus, REAP (router-weighted expert activation pruning)

## [Run Frontier AI at Home — Alex Cheema, EXO Labs](../videos/ESbWpPT_9-o.md)
`ESbWpPT_9-o` · AI Engineer · 2026-06-18 · q3 · deep · talk · also: local-ai, infra-cost-scaling

EXO Labs' Alex Cheema argues decode is memory-bound, so local frontier inference is a memory, bandwidth and energy problem. He demos Mac clusters over Thunderbolt RDMA and a Mac plus DGX Spark prefill/decode split.

- Techniques: Kernel fusion of redundant launches; Cache-stable prompt prefix in the harness; Prefill/decode disaggregation across devices; Tensor parallelism over RDMA; Full-replica weights with append-only event logs for cluster state; Expose each node over HTTP and reach it through a mesh VPN; Budget-based Pareto benchmarking; Hypothesis-driven auto-research
- Tools: EXO, Claude Code, OpenCode, OpenClaw, Tailscale, MLX, llama.cpp, Thunderbolt 5 RDMA, 10GbE

## [Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind](../videos/SS-A8sE7hkw.md)
`SS-A8sE7hkw` · AI Engineer · 2026-06-18 · q2 · intro · talk · also: local-ai, models-research, governance-compliance

Google DeepMind's Gemma team pitches open-weight Gemma 4 models (E2B to 31B) as a way to own, customize and run models locally, with on-device and single-GPU demos.

- Techniques: Drop-in local endpoint swap; Local sub-agent fan-out for batch work; Threshold-based task routing; Latency-class scheduling for on-device tasks; Own-eval-first model adoption
- Tools: Gemma 4, Gemini, Google AI Edge Gallery, LM Studio, Ollama, MedGemma, OpenRouter, LM Arena

## [GPU Cloud Deployment Without Leaving Your IDE — Audry Hsu, RunPod](../videos/zDGHt0LB-dA.md)
`zDGHt0LB-dA` · AI Engineer · 2026-06-18 · q2 · intro · demo · also: infra-cost-scaling

RunPod's Audrey Hsu demos Flash, a Python SDK that runs a decorated async function on a cloud GPU with hot reload from the local dev loop, plus a multi-model image pipeline and a pods-vs-serverless cost note.

- Techniques: Decorator-based remote GPU execution with hot reload; LLM prompt expansion before image generation; Chained model pipeline with separate endpoints per stage; Start small, then scale: pods for experiments, serverless for fan-out
- Tools: RunPod Flash (Python SDK), RunPod Serverless, RunPod Pods, RunPod Clusters, RunPod Hub, Stable Diffusion XL Turbo, DreamShaper, Qwen3, Google image composition model (Nano Banana 2), PyTorch, FastAPI, Docker

## [From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google](../videos/-TiET_K-E_g.md)
`-TiET_K-E_g` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: training-finetuning-rl, local-ai, skills-self-improvement

Google's Cormac Brick on on-device agents: a prompt-based skill harness on Gemma 4, and fine-tuning FunctionGemma on synthetic data to lift function-calling success from about 46% to 90%+ on most functions.

- Techniques: Progressive skill disclosure; In-app JavaScript rendering from a skill; Coding agent writes the skills; Synthetic-data fine-tune for fixed function calling; Export and deploy pipeline for small models; Chained tiny models for a pipeline
- Tools: LiteRT-LM, LiteRT, MediaPipe, Gemma 4, FunctionGemma, Gemma 3, Gemini Nano, Android AICore, Gemini CLI, Gemini Flash, litert-torch, transformers

## [Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod](../videos/ILdE7FaAjVA.md)
`ILdE7FaAjVA` · AI Engineer · 2026-06-18 · q2 · intro · demo · also: infra-cost-scaling

RunPod's intro walkthrough of deploying an open LLM (Qwen via vLLM) as a serverless GPU endpoint from its Hub in under five minutes; mostly a product pitch, with a useful look at cold starts and autoscaling settings.

- Techniques: Serverless GPU autoscaling with warm workers; Deploy a model from a pre-vetted Hub listing; Cold-start awareness in latency budgets
- Tools: RunPod, vLLM, Hugging Face, Docker

## [Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum](../videos/WRBNDpUhsJQ.md)
`WRBNDpUhsJQ` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: multi-agent, token-cost-efficiency

Adrian Bertagnoli (Callosum) argues AI is moving from homogeneous scaling to heterogeneous multi-agent systems mixing models, workflows and chips, and shows a recursive-LM variant that routes sub-contexts to different models and hardware for big cost and speed gains.

- Techniques: Heterogeneous recursion; Subtask offloading to small models; Automated model and hardware routing; Hardware-matched inference for sub-calls
- Tools: Python REPL, Cerebras, Kimi K2.5, GPT-5.2, Gemini 2.5, Qwen3-VL-8B-Instruct, Stamanova

## [You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia](../videos/gHs5ZiY80PM.md)
`gHs5ZiY80PM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: training-finetuning-rl, voice-multimodal

NVIDIA's Ziv Ilan on making diffusion image and video models fast enough for real use: quantization, step caching and step distillation, stacked incrementally, with distillation as the biggest win.

- Techniques: Post-training quantization with dynamic ranges for diffusion; Step caching (TeaCache-style and chunk-based); Trajectory vs distribution step distillation; Incremental optimization ladder
- Tools: TensorRT-LLM Visual Gen, FastGen, vLLM-Omni, SGLang Diffusion, TeaCache, Blackwell GPUs (B200), Hugging Face checkpoints

## [What Lies Beneath the API — Benjamin Cowen, Modal](../videos/HvZXAOZ3iv8.md)
`HvZXAOZ3iv8` · AI Engineer · 2026-06-18 · q2 · intro · talk · also: training-finetuning-rl, infra-cost-scaling

Modal forward-deployed engineer argues that once a product is differentiated, fine-tuning becomes worth it, and that serverless compute and open-source libraries now make it accessible without a cluster team. Sales-leaning, with a few concrete signals and code-size claims.

- Techniques: Signal-based fine-tuning decision; Harness outcomes as RL training data; Parallel hyperparameter sweep with early kill; Sandbox-fanned RL rollouts; Autoscaled serving of custom models
- Tools: Modal, vLLM, SGLang, Triton Inference Server, Python

## [Gemini Nano on device — Florina Muntenescu & Oli Gaymond, Google DeepMind](../videos/owH1f0N-keY.md)
`owH1f0N-keY` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: local-ai, product-ux

Google DeepMind's Android team on using Gemini Nano on-device via ML Kit GenAI and Firebase hybrid fallback, with Q&A on battery, shared-model scheduling and device reach.

- Techniques: Runtime hybrid routing with cloud fallback; Use the ML Kit GenAI Prompt API for on-device structured tasks; Offload non-urgent batch work to background, charging-time windows; Prompt-stuffed retrieval as a stopgap RAG; Device testing and profiling for custom models
- Tools: Gemini Nano, AICore, ML Kit GenAI APIs, Prompt API, Firebase AI Logic, LiteRT-LM, AI Edge Gallery, Gemma 4

## [Nvidia's Huge releases | Claude Opus 4.8, Liquid AI, Microsoft Lens & More AI News](../videos/_Nh-wDT6Odc.md)
`_Nh-wDT6Odc` · Kai Explains · 2026-06-02 · q3 · intro · news · also: models-research, local-ai, data-engineering

Weekly Kai Explains roundup (June 2026) of open-model and tool releases: NVIDIA Locate Anything 3B and PID decoder, Sapient HRM-Text-1B, Step 3.7 Flash, NuExtract 3, Microsoft Lens, Claude Opus 4.8, and Perplexity's Rust tokenizer.

- Techniques: Parallel box decoding for detection and grounding; Trace inversion for distilling reasoning into a small model; Template-driven document extraction with a reasoning toggle; Dense re-captioning of training data; Tokenizer hot-path optimization; Local runs of open-weight models; Choosing Opus 4.8 effort per task
- Tools: NVIDIA Locate Anything 3B, Qwen2.5-3B, MoonViT, Qwen3-VL, Rex Omni, HRM-Text-1B (Sapient Intelligence), LFM (Liquid AI, transcript reads 'LFM 2.58'), Quopus 3.6, Qwen3.6-27B, NVIDIA PID (Pixel Diffusion Decoder), SeedVR2, Flux.1-Dev

## [I Ran a Local LLM on 12-Year-Old Raspberry Pi (It Actually Worked!)](../videos/u8XQsL38WjQ.md)
`u8XQsL38WjQ` · Better Stack · 2026-06-02 · q3 · practitioner · tutorial · also: local-ai

Better Stack runs the 90M-parameter Falcon H1 Tiny on a 2014 Raspberry Pi 1 by cross-compiling llama.cpp for ARMv6 and testing 2/4/8-bit quants; it works, but is far too slow and thin on knowledge to be useful.

- Techniques: Pick the OS image for a low-RAM board; Cross-compile llama.cpp for ARMv6 on a laptop; Minimal-footprint inference invocation; Stepwise quantization sweep with graded probes
- Tools: llama.cpp, Falcon H1 Tiny (90M, Technology Innovation Institute), Raspberry Pi OS Lite 32-bit, Raspberry Pi Imager, cross-compiler toolchain (spoken as DocCross), ssh / scp, Mamba, IBM Granite 4 (mentioned)

## [AI avatar beats HeyGen, 1-min 720p video, video timestamps AI, lip sync model: AI NEWS](../videos/MYzITZG4c4M.md)
`MYzITZG4c4M` · Kai Explains · 2026-06-02 · q3 · intro · news · also: models-research, local-ai, voice-multimodal

Kai Explains weekly AI news (June 2, 2026): a roundup of new open-weight releases across robotics sim, small translation and video models, avatars, humanoids, TTS and segmentation.

- Techniques: Simulation as an evaluation signal; Prompt-level control of a small translation model; Ternary (1.58-bit) weights for memory savings; Rolling multi-segment inference for identity-stable long video; Few-step distillation (DMD) for video diffusion
- Tools: Genesis World 1.0, Nix (renderer), Quadrants (Python-to-GPU compiler), IsaacSim, MuJoCo, HiMT2 (Tencent translation models, captioned as 'HiMT2'), BitCPM-CANN, MiniCPM4, Huawei Ascend 910B / NPU, Marlin 2B, LongCat Video Avatar 1.5, Whisper Large V3

## [This Is The Best Local Model Runner For Apple Silicon (oMLX)](../videos/EsLwzxTz-A4.md)
`EsLwzxTz-A4` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: local-ai, token-cost-efficiency

Hands-on review of oMLX, an MLX-based local inference server for Apple Silicon with SSD-paged KV cache; one Qwen 3.6 35B coding run beats LM Studio on speed, with 400 errors at context overflow as the trade-off.

- Techniques: Serve a local model through an OpenAI-compatible endpoint and point a coding CLI at it; Same-model, same-context head-to-head benchmark for local runtimes; Keep the stable prefix on disk and reuse it after a session clear; Pick a lean harness when the context window is small
- Tools: oMLX, Apple MLX, Qwen 3.6 35B (4-bit), Codex CLI, Claude Code, LM Studio, Apple Silicon (M2 MacBook Pro)

## [This New Engine Runs Local AI Using 10x Less RAM! (Cactus)](../videos/nVhdDgYf_rI.md)
`nVhdDgYf_rI` · Better Stack · 2026-06-02 · q2 · intro · review · also: local-ai, token-cost-efficiency

Better Stack demos Cactus, an edge inference engine with NPU-first execution, zero-copy weight mapping and a local-to-cloud hybrid router; the only measured result is about 260 ms local transcription on an iPhone 12 Pro, and the 10x RAM claim in the title is never measured.

- Techniques: Confidence-based local-to-cloud fallback; Streaming on-device transcription benchmark; Choose NPU-optimized model variants for the target device
- Tools: Cactus (inference engine, .cact model format, Swift package, dashboard with NPU-optimized models), GGUF (format the engine moves away from; not used), Parakeet (speech model, run locally; spelled Paracat in the auto-captions), Gemini 2.5 Flash (cloud fallback model), Swift (demo app language), iPhone 12 Pro (test device), Apple, Qualcomm and MediaTek NPUs (hardware targets)

## [Why MLX — Prince Canuma, Neywa Labs](../videos/zTLJNHj0DeQ.md)
`zTLJNHj0DeQ` · AI Engineer · 2026-05-18 · q3 · intro · talk · also: local-ai, voice-multimodal

Prince Canuma argues for running agents, voice, and vision models fully on Apple Silicon with MLX to cut cloud subscription costs and work offline. Demos are mixed, and the talk ends with a TurboQuant KV-cache claim.

- Techniques: Modular speech pipeline; Chained short-clip video generation; Grounded visual reasoning on video; Storage-backed model loading on phones; TurboQuant-style KV-cache quantization; Live GPU monitoring during inference
- Tools: MLX, MLX-VLM, MLX-Audio, Marvis TTS, RF-DETR, Gemma 4, Qwen3-Omni, Core ML, Gradio, MacTop, Reachy Mini, LM Studio

## [Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind](../videos/_gVFUEdhCyI.md)
`_gVFUEdhCyI` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: models-research, local-ai

Google DeepMind's Omar Sanseviero introduces Gemma 4, a family of open models from 2B to 32B parameters, and argues that small open models can now do multimodal and agentic work on-device.

- Techniques: Offload per-layer embeddings to CPU or disk; Parallel local generation on one machine; Pick the model by tokenizer for low-resource language fine-tuning; Stay on the framework the team already uses
- Tools: Gemma 4, llama.cpp, MLX, Ollama, Hugging Face Transformers, vLLM, SGLang, Keras, Android Studio, ShieldGemma, MedGemma, LM Arena

## [How Transformers Finally Ate Vision – Isaac Robinson, Roboflow](../videos/VhfAVA3BG2I.md)
`VhfAVA3BG2I` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: models-research, training-finetuning-rl

Isaac Robinson (Roboflow) traces how plain ViTs beat CNN and hybrid backbones, crediting massive ViT-specific pretraining, borrowed LLM speedups, and NAS over one foundation model for deployable vision.

- Techniques: Benchmark attention variants against a FlashAttention baseline; Masked-patch pretraining to instill inductive bias; Linear-probe check for frozen features; NAS over a pretrained foundation model; Transfer benchmark for foundation models
- Tools: SAM, SAM2, SAM3, MobileSAM, TinyViT, Hiera, ConvNeXt, Swin Transformer, ViT, MAE, DINOv2, DINOv3

## [Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral](../videos/3jGAU2sbAyY.md)
`3jGAU2sbAyY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: voice-multimodal, models-research

Mistral's Samuel Humeau explains why modern text-to-speech uses autoregressive audio-token LLM-style backbones, frame-level codecs and streamed output for voice agents.

- Techniques: Stream the first audio chunks; Two-level frame decoding; Codec with a bottleneck and text-aware token losses; Flow-matching token head per frame; Full-context conditioning with a short voice prompt; Fast small LLM for the text, TTS for the audio

## [Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind](../videos/Lm8BLHkxiAo.md)
`Lm8BLHkxiAo` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: local-ai, models-research

Google DeepMind's pitch for running Gemma 4 E2B/E4B agents on-device through LiteRT, with the conversion, quantization, device-benchmarking and NPU path laid out and vendor speed claims.

- Techniques: Hybrid local-plus-remote inference via function calling; Use native structured JSON output instead of prompt-only formatting; Packaging capabilities as user-authored skills; Bring-your-own-model conversion with graph inspection; Fleet-benchmark before shipping; Small local model as a gate in a split architecture
- Tools: LiteRT, TensorFlow Lite, LiteRT-LM, Gemma 4, Gemma 3, Model Explorer, AI Edge Portal, Google AI Edge Gallery app, Hugging Face, Core ML, Raspberry Pi, Qualcomm NPU

## [Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX — Adrien Grondin, Locally AI](../videos/a2muGkT4WD4.md)
`a2muGkT4WD4` · AI Engineer · 2026-05-18 · q2 · intro · demo · also: local-ai

Adrien Grondin (Locally AI) shows how to run quantized Gemma 4 on iPhone with Apple's MLX, covering the mlx-swift-lm package, picking quantized weights, and speed on phones.

- Techniques: Load quantized models by Hub ID in an on-device Swift app; Choose quantization between 4-bit and 8-bit; Stream tokens to the UI; Small local model for automation steps; Compare inference engines via a local server
- Tools: MLX, mlx-swift-lm, mlx-lm, mlx-vlm, mlx-audio, Hugging Face, mlx-community, LM Studio, llama.cpp, Apple Shortcuts, Gemma 4, Qwen

## [The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked](../videos/qdh_x-uRs9g.md)
`qdh_x-uRs9g` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: rag-retrieval, infra-cost-scaling

Superlinked's Filip Makraduli on why small models (embeddings, rerankers, NER) need their own inference layer, and the open-source SIE engine built to serve them on shared GPUs.

- Techniques: Hot-swap many small models on one GPU with LRU eviction; Re-implement the forward pass per model family; Small-model preprocessing in front of the agent; Models as config, cluster as code
- Tools: vLLM, Prometheus, Grafana, Terraform, Helm, Docker, Hugging Face, FlashAttention, Chroma, Qdrant, Weaviate (transcribed as VV8), LanceDB (transcribed as LensDB)

## [Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind](../videos/_A367W_qvc8.md)
`_A367W_qvc8` · AI Engineer · 2026-05-18 · q4 · deep · talk · also: models-research, local-ai

Google DeepMind researcher walks through Gemma 4's architecture: interleaved local/global attention, asymmetric GQA, per-layer embeddings in flash memory, a shared-expert MoE, and flexible image token budgets.

- Techniques: Interleaved local/global attention with sliding windows; Asymmetric GQA by layer type; Per-layer embedding tables offloaded to flash; Developer-selected image token budget; Shared-plus-routed MoE
- Tools: Gemma 4, Hugging Face, Kaggle, Ollama, Google AI Studio, Vertex AI

## [FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs](../videos/x8Yb4RidLgM.md)
`x8Yb4RidLgM` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: models-research, voice-multimodal

Black Forest Labs' developer relations engineer walks through FLUX model history, a new self-supervised training method (Self-Flow) that drops external encoders, and sub-second Klein editing.

- Techniques: Dual-noise self-supervised representation learning (Self-Flow); External-encoder representation alignment; Multi-reference conditioning for consistency; Chaining edited frames as video keyframes
- Tools: FLUX.1, FLUX Context, FLUX.2, FLUX.2 Klein, Self-Flow, DINOv2, DINOv3, Qwen

## [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google](../videos/BKWpYIWvAo4.md)
`BKWpYIWvAo4` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: local-ai, skills-self-improvement, training-finetuning-rl

Google AI Edge on running small Gemma models on-device via LiteRT-LM, the on-device agent-skills pattern (progressive disclosure, constrained tool calls), and fine-tuning tiny models with synthetic data.

- Techniques: Progressive disclosure for skills; Three-primitive orchestrator; Constrained decoding scoped to tool calls; Synthetic data then fine-tune then quantize; Modular pipeline of small models; LoRA hot-swap on one base model; Skill testing loop with a coding agent and a device; Build-once, deploy-everywhere model file with AOT for NPU
- Tools: LiteRT-LM, LiteRT (formerly TensorFlow Lite), LiteRT-Torch, Google AI Edge Gallery, MediaPipe, Gemma 4 (E2B, E4B), Function Gemma (270M), Gemma 3 270M, EmbeddingGemma (300M), FastVLM (500M, Apple), Qwen 0.6B, Gemini CLI

## [Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML](../videos/X6NShR2ccOg.md)
`X6NShR2ccOg` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: training-finetuning-rl, evals, enterprise-adoption

Adaptive ML's CCO argues RL, not prompting or SFT, is the systematic way to take enterprise LLMs and agents from MVP to production, using environments, rewards, and LLM judges. Mostly a product pitch for their platform.

- Techniques: Mock environment with mock tools and an LLM-played user; Rejection-sampling bootstrap from reward-scored trajectories; Business KPI as the RL reward; LLM judge with human-written rubric, graduated to a reward model; Prefer a smaller RL-trained model for high-volume or latency-bound features
- Tools: Adaptive Engine, PPO, GSPO, Gemma, Mistral, Qwen

## [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../videos/xOP1PM8fwnk.md)
`xOP1PM8fwnk` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: models-research, training-finetuning-rl, voice-multimodal

Google DeepMind's Sander Dieleman walks through training image and video diffusion models at scale: learned latents, how denoising works, guidance, step-count distillation, and control signals added in post-training.

- Techniques: Two-stage latent diffusion with a learned autoencoder; Guidance by amplifying the conditional-minus-unconditional difference; Deterministic sampling as a distillation teacher; Consistency distillation restricted to sampling intervals; Injecting conditioning via extra tokens or broadcast; Data-parallel first, then model-parallel sharding with JAX pjit
- Tools: JAX, pjit, TPU, Stable Diffusion, GLIDE, EQVAE, Veo, Genie

## [Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI](../videos/fLUtUkqYHnQ.md)
`fLUtUkqYHnQ` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: training-finetuning-rl, models-research, local-ai

Liquid AI's Maxime Labonne on training 350M to 24B edge models: small models have their own constraints, narrow targeting and doom-loop fixes via DPO and RL.

- Techniques: On-policy DPO pairs for doom-loop suppression; Repetition penalty inside RLVR; Fix training stage by diagnosis; Profile architecture on target hardware; Tool and environment offload for small models
- Tools: Hugging Face, Python

## [Google’s Latest Genie 3 AI Hype Deserves a Closer Look](../videos/mOku8YCtoOc.md)
`mOku8YCtoOc` · Better Stack · 2026-03-02 · q2 · intro · review · also: models-research, local-ai

Better Stack tests Google's Genie 3 and the open-source LingBot World model, finds them GPU-hungry and gated, and argues infinite world models are not yet practical on consumer hardware.

- Techniques: Lower sample count to cut memory on world-model runs; Single-GPU-per-node launch on one cloud GPU; Use a 4-bit quantized community build to fit one GPU; Feed a generated still image as the scene seed
- Tools: Genie 3 (Google, infinite world model, US-only with Ultra membership), LingBot World (open-source 14B base model, Robbyant/Ant Group, video generation with camera-pose conditioning), LingBot Fast (announced, not released), NVIDIA RTX 5090, NVIDIA H200, RunPod, ComfyUI, Kalen Humphreys 4-bit quantized LingBot World (community build), Sora (cited only as an example of video generators, not used)

## [NVIDIA’s New Voice AI is Absolutely WILD! (PersonaPlex)](../videos/n_m0fqp8xwQ.md)
`n_m0fqp8xwQ` · Better Stack · 2026-02-02 · q3 · intro · review · also: voice-multimodal, models-research

Hands-on look at NVIDIA's open PersonaPlex full-duplex voice model: deploy on a rented RunPod A40, run the Moshi server, and test role prompts, which work for scripted flows but drift under confusing input.

- Techniques: Deploy PersonaPlex on a rented GPU pod; Role prompt presets and custom persona prompts in the web UI; Stress-test a voice model with adversarial and off-script user turns
- Tools: PersonaPlex (NVIDIA open voice model, full-duplex), Moshi (Kyutai speech-to-speech architecture and server), Mimi (neural audio codec), Opus (audio codec, installed on the server), RunPod (GPU container hosting, A40 used), PyTorch Ubuntu template (RunPod), Hugging Face (model download, token required), ChatGPT voice mode (comparison only)

## [I Stress-Tested Meta’s SAM 3D on Real Photos And The Results Were Shocking!](../videos/vKWDiHZGPs4.md)
`vKWDiHZGPs4` · Better Stack · 2026-01-02 · q3 · intro · tutorial · also: voice-multimodal

Better Stack tutorial that walks through Meta's SAM 2 and SAM 3D Objects models and builds an Expo mobile app that turns a photo into a 3D model, with the models hosted on a rented RunPod A40 GPU.

- Techniques: Provision a RunPod GPU pod for vision models; Hugging Face gated-model access setup; One-command setup script, then launch the API; Point the Expo client at the pod; Iterative point-based segmentation before 3D generation; Export and inspect generated assets
- Tools: SAM 2, SAM 3, SAM 3D Objects, SAM 3D Body, Expo, RunPod (A40 GPU pod), RTX 5090 (mentioned as a faster alternative), Hugging Face CLI, uvicorn, npm, Blender, GLB file format

## [Why Apple's New AI Model is TOO GOOD to Be True](../videos/mwwuvgi1Qmg.md)
`mwwuvgi1Qmg` · Better Stack · 2026-01-02 · q3 · intro · review · also: models-research

Better Stack walkthrough of Apple's open-source STARFlow image/video model (autoregressive normalizing flow), with a single-H200 test run; the image checkpoint works, but there is no video checkpoint and no on-device path.

- Techniques: Reproduce STARFlow image generation on a rented GPU; Check the claimed speedup against your own timing; Edit by inverting the flow and changing part of the latent
- Tools: STARFlow (Apple open-source repo), PyTorch, Hugging Face (checkpoint hosting), DigitalOcean GPU droplet, NVIDIA H200, Python, Nano Banana Pro (comparison), Midjourney (comparison)

## [Goodbye AI Cloud Bills... Exo Runs AI on Your Own Devices](../videos/L8468vMTX2s.md)
`L8468vMTX2s` · Better Stack · 2026-01-02 · q2 · intro · review · also: local-ai, infra-cost-scaling

Short Better Stack overview of EXO, an open-source tool that auto-discovers devices on a LAN and shards one model across them; the demo runs on a single Mac, so the multi-device claims are unverified.

- Techniques: Zero-config LAN cluster for local inference; Shard the model by measured node capacity; Thunderbolt 5 RDMA between Macs
- Tools: EXO (open-source peer-to-peer inference cluster, ExoLabs), Apple MLX, OpenAI-style chat endpoint (served by EXO), Thunderbolt 5 RDMA, DeepSeek V3 671B (cited community run), Qwen3 235B (cited community run), MacBook Pro M4 Pro (demo machine), Mac Studio M3 Ultra (cited benchmark), Mac mini M4 (cited ExoLabs run), Raspberry Pi (CPU node)

## [Tiny AI Is About to Change Everything (IBM Granite 4.0)](../videos/31r6yxbmrFo.md)
`31r6yxbmrFo` · Better Stack · 2025-12-02 · q3 · practitioner · review · also: local-ai, models-research

Better Stack walkthrough of IBM Granite 4.0 small models (hybrid Mamba-transformer, tiny browser-runnable variants), ending with an offline in-browser code-completion proof of concept.

- Techniques: Browser-only offline completion loop with transformers.js; Completion prompt and generation settings; Debounced suggestion UI with keyboard accept; Raise the token budget in your own agent
- Tools: IBM Granite 4.0, Granite 4 small, Granite 4 1B, Granite Nano 350M, transformers.js, Hugging Face, Mamba, React, MCP-UI, M2 MacBook (hardware used for the demo)

## [How does an LLM ACTUALLY Work? (Visual Breakdown)](../videos/tNXVYVMME1I.md)
`tNXVYVMME1I` · Better Stack · 2025-11-02 · q3 · intro · other · also: models-research

A visual, conceptual walkthrough of transformer internals (embeddings, layer norm, self-attention, MLP, stacking, softmax and temperature), using Brandon Bycroft's mini-LLM visualization. No code or steps; useful as grounding, not as new practice.

- Techniques: Causal (left-to-right) attention masking; Temperature as a sampling dial; Residual connections around attention and MLP sublayers
- Tools: GPT-4 (named as a model), GPT-3 (named in passing, ~100x smaller than current models per the speaker), Claude (named as a model), DeepSeek (named as a model), GELU (activation function), SwiGLU (transcribed as 'Swigloo'), FlashAttention, Mixture of Experts, Rotary Embeddings, Brandon Bycroft's mini-LLM visualization (external project credited in the video)

## [AI Tool Converts Your Sketch into Code Instantly!](../videos/p5hEVQIisgc.md)
`p5hEVQIisgc` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, product-ux

Demo and local-install walkthrough of Groq App Gen, an open-source web app that generates and iterates on small web apps from a sketch plus text prompts on Groq inference; speed is asserted, not measured.

- Techniques: Local install of Groq App Gen; Sketch then prompt; One change per prompt, verify each; Generate the edit list with a second LLM
- Tools: Groq App Gen (open-source web app, GitHub repo), Groq API / Groq inference, Llama 3.3 70B (spoken as 'Lama 3.37 70 billion' in captions), Next.js, TypeScript, npm, Python, VS Code, Windsurf, Cursor, ChatGPT

## [This Tiny 1-Bit Model Could Change AI Forever](../videos/DmBBQh5UPwQ.md)
`DmBBQh5UPwQ` · Better Stack · 2025-11-02 · q2 · intro · review · also: local-ai, models-research

Better Stack hands-on test of Microsoft's BitNet, a 1.58-bit ternary-weight LLM, on a laptop CPU: passes simple logic prompts, fails a coding task badly.

- Techniques: Run BitNet via the Hugging Face model card (transformers) instead of bitnet.cpp; Small-set logic benchmark for a local model; Iterative coding stress test with fix-up prompts
- Tools: BitNet (Microsoft 1-bit LLM), bitnet.cpp, Hugging Face transformers, Hugging Face model card and demo page, Nemotron (NVIDIA; prior video comparison), MacBook Pro M2, LLM logic test spreadsheet (public)

## [NVIDIA Quietly Dropped This POWERFUL AI Model (Nemotron v2)](../videos/8M5IHvDSZXs.md)
`8M5IHvDSZXs` · Better Stack · 2025-11-02 · q2 · intro · review · also: local-ai, models-research

Better Stack's hands-on look at NVIDIA's 9B Nemotron Nano v2: a hybrid Mamba-2/attention model, a reasoning-budget cap, mixed logic and coding results, and a RunPod + vLLM deployment.

- Techniques: Serve a Hugging Face model on a RunPod vLLM pod; Chat UI on top of a vLLM endpoint; Cap thinking with a reasoning budget client; Quick logic regression prompts
- Tools: NVIDIA Nemotron Nano v2 (9B), Mamba-2, vLLM, RunPod, Hugging Face, Ollama, Next.js vLLM UI, NVIDIA chatbot (free web demo), Llama 3, Qwen 3, Claude Code (mentioned for comparison only), Docker

## [Why WebGPU + Transformers.js is a Game Changer](../videos/NLQ_gVcjHHA.md)
`NLQ_gVcjHHA` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: local-ai

Short Better Stack tutorial on running small LLMs fully in the browser with Transformers.js and WebGPU, with a Hugging Face model, quantized weights, offline caching, and worker/streaming fixes for UI freezes.

- Techniques: Pick a small quantized model from the Hugging Face Hub for in-browser inference; Set quantization and generation limits on the Transformers.js pipeline; Keep the UI responsive by running generation in a Web Worker; Serve and iterate on the browser demo with Bun; Inspect where the model is cached
- Tools: Transformers.js, WebGPU, ONNX Runtime Web (spoken as 'Onyx Web Runtime'), Hugging Face Hub, Bun, Node.js, Llama 3.2, SmolLM2 (spoken as 'small lm2', probably), DINOv3 (spoken as 'Dino version 3', unverified), StarCoder, Claude Sonnet, Ollama

