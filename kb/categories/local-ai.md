# local-ai — 216 videos

*running models on your own hardware — GPUs, VRAM, Macs, llama.cpp / Ollama / LM Studio, open-weight model picks, local speedups*

By channel: AI Engineer 27 · Kai Explains 107 · AI LABS 4 · Better Stack 78

**Synthesized guide:** [guides/local-ai.md](../guides/local-ai.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [You Don't Need an Expensive GPU Anymore (Strata 100 tok/s)](../videos/mED-boddeWI.md)
`mED-boddeWI` · Kai Explains · 2026-11-01 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency

Kai tests Strata, an MIT-licensed local inference engine that runs DeepSeek V4.1 Flash (763B MoE) on a 12GB GPU by tiering experts across GPU, RAM and SSD. Conclusion: it works, but RAM is now the real cost, and the viral 100+ tok/s figure was prefill, not decode.

- Techniques: Three-tier expert placement by access frequency; Report prefill and decode separately, with context length, quantization and cache state; Per-tier cost math for a hardware decision; Quantization and KV-cache choices for large local models; Reduced-memory mode and specialized builds; Pre-purchase hardware checklist
- Tools: Strata (local inference engine, MIT license, GitHub, Windows/Linux/Mac desktop app), llama.cpp (mentioned as a comparison), Ollama (mentioned as a comparison), Qwen 3.8 Flash Next (125B, Q2 build), Qwen smaller sibling (transcribed as 'Quen 3.635B', measured at 59.7 tok/s on RTX 3060), DeepSeek V4.1 Flash (763B MoE, MIT license, 1M context; transcribed as 'DeepSeq V4.1 Flash'), DeepSeek API (off-peak and peak output pricing), Betel Juice (community fork, transcribed as 'betel juice'), NVIDIA RTX 3060, RTX 5070, RTX 5070 Ti, RTX 5090, RTX 4090 (price reference), AMD MI50 (2018 data-center GPU, about $700 used), PCIe 4 NVMe SSD (2TB, about $253)

## [Avalon Just Beat Strata by 47% on AMD (9x Faster)](../videos/0F63pTS8Gt0.md)
`0F63pTS8Gt0` · Kai Explains · 2026-11-01 · q4 · practitioner · review · also: inference-serving, evals

Breakdown of the "Avalon beats Strata by 47% on AMD" claim: a llama.cpp fork tuned for one 7900 XT box, and why the number only holds on that machine and that model file.

- Techniques: Benchmark provenance checklist; Bandwidth-ceiling estimate for MoE decode; Expert cache from spare VRAM with CPU fallback; Cheap draft head that shares the expert cache for MoE speculative decoding; Perplexity as a fast quant-quality screen, with a caveat; mmap for models larger than VRAM plus RAM; Diagnose multi-GPU slowdowns as a bottleneck shift
- Tools: Avalon (llama.cpp fork, MIT, repo live Oct 9 2026, Qwen 3.8B Flash Next only, Linux only, RDNA3 required by installer), Strata (AMD-focused inference engine for MoE models; 0.1.43 in the table, 0.2.8 current), llama.cpp (stock, with an open draft PR from Piotr Wilkin), Boon llama.cpp fork (source of the first expert cache version in Avalon), ik_llama.cpp (source of Avalon's compression types), Unsloth IQ4 quantization (perplexity reference), Strata ISTA quantization format, Claude Opus (the video says version 5.5; the README credits it with writing the GPU and CPU kernels), ROCm (AMD software stack, cited as the lagging part), Vulkan (Avalon has no Vulkan backend, so it does not run on Windows), Qwen 3.8B Flash Next (MoE: 125B active, 51B lookup table, 48 layers, 512 experts per layer, top-10 routing)

## [When Running Your Own AI Models Beats Paying for APIs - Steven Latré, imec](../videos/9-Y_oS9OBLc.md)
`9-Y_oS9OBLc` · AI Engineer · 2026-10-31 · q4 · practitioner · talk · also: infra-cost-scaling, inference-serving, token-cost-efficiency

imec's AI lead benchmarks coding agents on open-weight models vs. APIs and finds that concurrency, GPU utilization and harness choice, not just accuracy, decide when self-hosting pays off.

- Techniques: GPU-utilization break-even check for API vs self-host; Concurrency ramp test on a single inference box; Task-level benchmark grid across harness, model and hardware; Measure harness token output and wall time on a paid GPU; Map model choice to hardware tiers
- Tools: Codex, Pi (transcribed as 'Py'), Claude Code, SWE-Bench Pro, Qwen, DeepSeek, GLM, Kimi K3, Claude Opus (mentioned as a reference point), NVIDIA B200-class GPU (transcribed as 'A times B 200')

## [I Hid a Raspberry Pi in a Pumpkin to Fix Smart Speakers](../videos/t9Jro9BAIMw.md)
`t9Jro9BAIMw` · Better Stack · 2026-10-30 · q3 · intro · tutorial · also: voice-multimodal, dev-tools

Better Stack builds a Raspberry Pi voice assistant inside a pumpkin: local wake word and speech-to-text, a fast remote LLM for replies, and remote TTS. Practical on latency and soldering, light on reproducible detail.

- Techniques: Wake word -> local STT -> remote fast LLM -> TTS voice loop; Pick the LLM on measured reply speed first, then check quality; Keep TTS remote when local voice quality or speed falls short; Solder to a separate hat, then mate it to the Pi header; Check clearance between solder joints and the cooler before power-up; Insulate the pumpkin's internals with cling film
- Tools: Raspberry Pi, Perma-Proto hat (Adafruit board, as named in captions), sherpa-onnx, Parakeet (speech-to-text model), Python, DeepSeek Flash, Gemini Flash, Haiku, ElevenLabs Flash, multimeter, active cooler (Raspberry Pi)

## [Every Way to Get 256 GB of VRAM for Local AI at Full Context](../videos/JPHT9AvoPSA.md)
`JPHT9AvoPSA` · Kai Explains · 2026-10-30 · q4 · practitioner · review · also: token-cost-efficiency, inference-serving

A price-and-speed tour of every route to 256GB of memory for running DeepSeek V4.1 Flash locally; the real metric is bits per weight, and a cheap DDR4 plus RTX 3090 MoE-offload build is the surprise pick.

- Techniques: Size the box from bits per weight, not gigabytes; Measure quantization fidelity as next-token agreement; Keep the hot parts of a sparse MoE on GPU and the rest in system RAM; Put a large, sparsely read lookup table on SSD; Raise the macOS GPU memory limit and persist it; Enable the model's draft head for speculative decoding; Break-even against the API before buying hardware; Budget prefill time for long first prompts
- Tools: DeepSeek V4.1 Flash, DeepSeek API, Unsloth quantized builds, Dwarfstar inference engine (transcribed 'Antiresis Dwarfstar'), MLX (Mac inference route), vLLM 0.20, CUDA 13, ROCm, Qwen 3.8 (incl. a Flash Next variant), Mac Studio M5 Ultra 256GB / 512GB, Mac Studio M3 Ultra, NVIDIA DGX Spark

## [Your GPU Is Nerfed for Local AI (NVIDIA's Hidden Limit)](../videos/VIm73gaY_hM.md)
`VIm73gaY_hM` · Kai Explains · 2026-10-28 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency

Explains why the viral RTX GPU "unlock" doubles only one FP16 microbenchmark: real gains land on 16-bit serving, long-context prefill and image/video work, not token decode or GGUF, and power caps can cost more than the unlock gains.

- Techniques: Identify the data path before expecting a GPU gain; Check and raise the GPU power limit before anything else; Benchmark prefill and decode separately; Treat unsigned firmware or kernel modules as high-trust code
- Tools: NVIDIA RTX 4090, NVIDIA RTX 3090, NVIDIA RTX 3090 Ti, NVIDIA RTX 3060, NVIDIA RTX 4070 Ti Super, NVIDIA RTX 5090, NVIDIA RTX A6000, NVIDIA Titan RTX, NVIDIA RTX 2080 Ti, vLLM, llama.cpp, Ollama

## [Your PS5 Can Now Run Open Models (And It's Surprisingly Fast)](../videos/TgmC_VZEKTE.md)
`TgmC_VZEKTE` · Kai Explains · 2026-10-27 · q4 · practitioner · review · also: inference-serving, claude-code

A viral claim that a PS5 runs a 27B open model at 20 tokens/s, checked against a 613-second Claude Code first prompt. The lesson: prefill (reading) speed, driver limits and OS sandboxing decide agent usefulness more than writing speed.

- Techniques: Split latency into prefill and decode; Estimate decode ceiling from bandwidth; Use a smaller model for agent/harness work; Chunk long prompts to avoid GPU watchdog timeouts; Multi-token prediction for decode speedup; Serve a household local API
- Tools: PS5LM (llama.cpp port for PS5; started by Mert Kobanov Oct 1; fork PS5LM+ by ABI245E; the two later merged), llama.cpp, llama.cpp Vulkan build (RedStapler, Linux), RADV (Mesa Vulkan driver, ported to PS5), Unsloth UD-IQ2 2-bit quant (6.8 GB; 9.2 GB sibling), Qwen 27B dense model (Apache 2.0, released Aug by Alibaba; caption reads 'Quen 3.827B'), Qwen 9B (4-bit on PS5 Slim, 55 tokens/s; caption reads 'Quen 3.59b'), Qwen 8B Flash Next (caption reads 'Quen 3.8 Flash Next'; the host says 180B parameters, split across PC and PS5), Gemma 4B (61 tokens/s, reads images; caption reads 'Gemma 44B'), Llama 3.2 3B (124 tokens/s), Claude Code, Relapse (PS5 jailbreak, firmware 7.00-13.60, public Sep 29)

## [Is Flint the Killer of Qwen 3.8 27B? (First RSI Model)](../videos/RmE4G6MhOVU.md)
`RmE4G6MhOVU` · Kai Explains · 2026-10-26 · q4 · practitioner · review · also: inference-serving, models-research, evals

Kai Explains tests Recursive's Flint MoE coding model: the 131 tok/s headline is real, but always-on reasoning, long-context slowdown and agent loops mean task completion time is what matters.

- Techniques: Bandwidth-bound decode estimate; Time-to-task-completion benchmark; Token-budget cap test; Split prefill from decode timing; Hybrid planner and implementer; Fair engine comparison; Hardware fallbacks reported by users
- Tools: Flint (Recursive, 39.8B MoE, 2.5B active, 256 experts, 262,144-token text-only context, Apache license), Recursive REC inference engine (Mac-only, proprietary), Apple MLX, llama.cpp (Vulkan build on AMD), Ollama (23 GB model file), Unsloth 4-bit and NVFP4 weights (25 GB 4-bit file, 11.9 GB smallest quant), vLLM (NVFP4 run on RTX Pro 6000), Qwen dense 27B and Qwen MoE 35B (as named in transcript), OpenCode (agent, 5-minute silence timeout, free tier), Pi (Recursive's own agent, ~17k-token system prompt), OpenRouter (free Flint access), Terminal Bench 2.1

## [These 2 Tiny AI Models Run on Your Phone, Not the Cloud](../videos/7oWM2UEH2mg.md)
`7oWM2UEH2mg` · Better Stack · 2026-10-25 · q3 · practitioner · review · also: voice-multimodal

Better Stack tests two beta on-device models from Desert Ant Labs: WHO (speaker diarization) and I (photo tagging, duplicates, aesthetic score). Fast local demos, but benchmarks are vendor-sourced and the license has a monthly check.

- Techniques: Diarize then merge with ASR by timestamp; Two-threshold tagging policy; Browser-side batch triage with WebGPU fallback; One-call multi-signal triage for photo cleanup
- Tools: Desert Ant Labs SDK 4.0 (beta), WHO (speaker diarization model, Desert Ant Labs), I (image classification and tagging model, Desert Ant Labs), PyAnnote (open-source diarization library, comparison baseline), Apple built-in speech transcriber (macOS), LiteRT.js (Google's web runtime for models), WebGPU, WebAssembly, Chrome, Node, Apple Neural Engine, Who Said What Where (the presenter's Mac app; GitHub link in the description)

## [This Tiny Qwen 27B Model Runs on a 12GB GPU](../videos/XKejQWnispc.md)
`XKejQWnispc` · Better Stack · 2026-10-24 · q3 · practitioner · review · also: inference-serving, mcp-and-tools, evals

Better Stack reviews Saluki 27B, a ~7.9GB quantization of a 27B Qwen-family model tuned to keep tool calling intact at the cost of math, and tests it on local llama.cpp and a DGX Spark.

- Techniques: Serve a GGUF quant locally with llama.cpp; Two-part tool-calling smoke test; Tool-call reliability count; Recommended settings for tool calls; Report strict and lenient parser scores separately; Measure agent throughput, not just file size; Pick by workload
- Tools: Saluki 27B (model name as captioned; the transcript attributes it to Underdog), Qwen 27B base model (captioned as 'QEN 3.827B'), Qwen 3.8 Flash (captioned as 'Quen 3.8 Flash next'; used as a comparison model at 4-bit), llama.cpp (llama-server, stock build), Ollama, Unsloth quants (4-bit, IQ2_XXS, IQ2_S), ISTA-DAS Lab 2-bit quant (RCO quantization search), Ternary Bonsai 2 (PrismML custom llama.cpp fork), MLX (an unfinished port was mentioned), BFCL (Berkeley function-calling benchmark, single-turn), AIME 2025, SWE-bench Verified (50-task subset)

## [llama.cpp Just Made 125B MoE Models 4× Faster!](../videos/shl8FFSoANE.md)
`shl8FFSoANE` · Kai Explains · 2026-10-23 · q4 · practitioner · review · also: inference-serving

A llama.cpp PR caches individual MoE experts in spare VRAM for a claimed 4x decode speedup; the real gain over a tuned baseline is about 1.5-2.2x and depends on hit rate, PCIe link and workload.

- Techniques: Per-expert LRU cache in VRAM instead of whole-layer offload; Go/no-go on hit rate from llama.cpp logs; 15-minute self-benchmark protocol; Check the PCIe link before enabling expert offload; Benchmark the actual workflow, not just decode speed; Disable the cache first when a model starts looping; Sizing rule of thumb
- Tools: llama.cpp (release 0.7 / B11480 or newer; PR 29887; PR 30449), Qwen Flash Next (125B MoE, 4-bit build; transcript spells it 'Quen 3.8 Flashnext'), Strata (model-family-specific runtime, 3-bit build), nvidia-smi, Multi-token prediction (MTP), Speculative decoding, --n-cpu-moe (spoken as NCPU MOE), RTX 5090, RTX 5070, RTX 4090, RTX 4070 Super, RTX 4060 laptop

## [I Tested Every Best Local AI For GPU (8GB TO 24GB VRAM)](../videos/ugKAkCVBcz0.md)
`ugKAkCVBcz0` · Kai Explains · 2026-10-22 · q4 · practitioner · review · also: inference-serving, models-research

Local model picks for 8 to 24 GB VRAM. The GGUF file (quant method and uploader) matters more than the model name, MoE models survive RAM spill while dense ones collapse, and thinking tokens often dominate wall time.

- Techniques: Back-of-envelope decode ceiling; Fit check with desktop headroom; MoE expert offload to system RAM; Pick the quant by builder, then bit width; Quantize the KV cache for Qwen, not Gemma; Time-to-answer measurement; Power-cap for sustained speed on a 3090 Founders Edition; Side-by-side local vs frontier check
- Tools: llama.cpp (named as 'Lama CPP'), Qwen 3.6 27B dense (captioned 'Quen 3.827B'), Qwen 3.6 35B-A3B MoE (captioned 'Quen 3.635BA3B'), Gemma 12B (captioned 'Gemma 412B', Q3 file 5.69 GB), ISTA quantized builds (GSQ build, 2-bit, 3-bit, 3.5-bit), Liquid AI LFM 2.5 24B (captioned 'LFM 2.524B'), NVIDIA Nemotron 3.5 Bolt (captioned as 'Bolt'; 74B total, 9B active, 2-bit with vision module), Speculative decoding head (named, not specified), Hugging Face (default download source), Artificial Analysis (intelligence index scoring), Chat LLM by Abacus AI (sponsor, $10/month, bundles GPT-6 Astra, Claude Fable 5.1, Gemini 4, Opus 5.5, DeepSig V4.1 and Kimi K3 as captioned), Windows (desktop VRAM overhead)

## [Your Local AI Is Not as Private as You Think](../videos/3mx84MRj8lY.md)
`3mx84MRj8lY` · Kai Explains · 2026-10-22 · q4 · practitioner · talk · also: security-guardrails, sandboxing-execution

Local AI is private, but a stranger's model file can still act on your machine through chat templates, runner bugs, exposed ports and poisoned fine-tunes; the fix is to limit what the model can reach.

- Techniques: Keep the model server on loopback; reach it remotely through an encrypted tunnel or an authenticated proxy; Patch the runner before anything else; Use official or established-quantizer weights for any model with tool access; Inspect the GGUF chat template before serving a model; Keep secrets out of the agent's working directory; Split command execution from network access and log the boundary; Do not rely on hash checks or allowlists alone
- Tools: Ollama (version 0.30.6 cited mid-October 2026; the talk also says 0.240.6 at 22:33, which conflicts), LM Studio, llama.cpp / llama.cpp server, llama-cpp-python, SGLang, vLLM, Hugging Face, GGUF, Jinja, SafeTensors, pickle scan / model-scan, Tailscale

## [NCM Is this the End of LLMs?](../videos/vLqswKyHS64.md)
`vLqswKyHS64` · Kai Explains · 2026-10-20 · q4 · practitioner · review · also: models-research, inference-serving, token-cost-efficiency

Kai Explains walks through the Stanford NCM paper (levels-based parallel text generation), separates its real single-stream gains from the hype, and argues memory bandwidth vs compute is the spec to watch for local AI.

- Techniques: Bandwidth-bound decode estimate; Minimum Bayes risk (MBR) decoding; Check speed claims at batch size 1 and at serving batch sizes; Coarse-to-fine residual code generation
- Tools: NCM (Next Concept Modeling, Stanford; GitHub repo with evaluation code and released models), Multi-scale residual VQ-VAE (compression network in NCM), Diffusion Gemma (Google DeepMind, June 10, 2026, Apache 2.0), Gemma (comparison word-by-word model, transcript reads 'Gemma 426B', likely a ~26B Gemma 4), Aurora LM (diffusion baseline in NCM paper), LADA 2.1 Mini (diffusion model with batch-size-1 benchmarks), Mercury (Inception diffusion LM), Meta Large Concept Models (Dec 2024, a different 'concept'), Hugging Face (model hosting), RTX 5090 (1792 GB/s), H100 (benchmark GPU for the 31x result), CUDA (required for NCM code)

## [Why Your Mac Is Slow at Local AI (And It's Not the Chip)](../videos/x_qmqqp6d7s.md)
`x_qmqqp6d7s` · Kai Explains · 2026-10-19 · q4 · practitioner · tutorial · also: inference-serving, token-cost-efficiency, claude-code

Kai Explains on why local AI on a Mac feels slow: prompt prefill and prefix-cache misses, not memory bandwidth, dominate agent turns, and a settings checklist finds the cache-breaking causes.

- Techniques: Split prefill from decode when measuring; Audit cache-token counts per turn; Raise server log verbosity to find cache misses; Check Ollama's context window; Pin the Claude Code version and attribution header; Keep thinking tokens in history; Lower reasoning effort on Qwen models; Test frontends against the same server before committing
- Tools: Claude Code, Ollama, LM Studio, llama.cpp, Qwen 27B (dense model; spoken as 'Quen 27B'), Qwen 3.8 27B as spoken ('Quen 3.827B'; name likely garbled by captions, unverified), OpenClaw (agent frontend), Hermes (agent frontend), Xcode (passing example app), Apple M5 Max, M5 Pro, M5 chip, M4 Max, M1 Max (hardware), Mac Mini 'M6' (as spoken at 1:26; likely a caption or naming error, unverified)

## [Can 9 year old GPU beats today's latest GPUs?](../videos/eckOsa0kBkY.md)
`eckOsa0kBkY` · Kai Explains · 2026-10-19 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency, infra-cost-scaling

Kai Explains tests whether four 2017 Tesla V100s can beat 2025 DGX Sparks and RTX Pro 6000 boxes on local LLM inference; the answer is yes for decode speed, but the software and power economics are the real constraints.

- Techniques: Split inference cost into prefill and decode; Check interconnect before adding GPUs; Break-even math for owned GPUs versus hosted tokens; Pick a fork that still targets your hardware generation
- Tools: NVIDIA Tesla V100 (SXM2, Volta), NVIDIA DGX Spark (GB10, Blackwell, NVFP4), NVIDIA RTX 5090, NVIDIA RTX 5060, NVIDIA GTX 1080 Ti, NVIDIA RTX Pro 6000 Blackwell Server Edition, Qwen 3.8 Flash (model; the speaker gives it as a 125B model and also uses other names), vLLM, OneCat vLLM fork (v1.50, v1.5.1), V100 Skinny (community project built on OneCat), llama.cpp, NVFP4

## [Speech Recognition Without the Internet Now Fits on a $10 Chip (Whistle)](../videos/bavO_V80ohM.md)
`bavO_V80ohM` · Better Stack · 2026-10-19 · q3 · practitioner · tutorial · also: voice-multimodal, inference-serving

Andres from Better Stack runs Cactus's 16.9 MB Whistle speech-to-text model fully offline on a $10 ESP32-S3, trimming decoder layers and quantizing math to fit and speed it up.

- Techniques: Decoder layer trimming for flash-constrained devices; Keyword biasing on a constrained command vocabulary; Confidence-gated retry in another language; Use short phrases, not single words, as voice commands; Microcontroller inference speedups; Push-to-talk with local feedback
- Tools: Whistle (Cactus Compute speech-to-text model, Apache 2.0, on Hugging Face), Needle / Needle 2 / Needle 3 (Cactus models, referenced from earlier videos), Cactus Compute inference engine, ESP32-S3 microcontroller (16 MB flash, 8 MB RAM, 240 MHz), INMP441 digital MEMS microphone, OpenAI WhisperBase (comparison model, 145 MB), LibriSpeech (benchmark test set), A terminal UI app that shows transcript, LED state and per-step timing (unnamed)

## [Local AI Hardware Just Got Way More Expensive Than You Think](../videos/Y226-wwfCSw.md)
`Y226-wwfCSw` · Kai Explains · 2026-10-19 · q4 · practitioner · review · also: token-cost-efficiency, inference-serving

Kai argues local AI hardware got about 74% pricier in a year (DGX Spark, GPUs) through a memory shortage, while hosted open-weight tokens got cheaper, so buying to save on tokens rarely pays off now.

- Techniques: Token break-even calculation for a local box; Use the cheapest provider's price as the ceiling for open weights; Split work by model architecture: MoE hosted, dense local; Offload weights to system RAM with Strata; Sell-or-keep check for idle GPUs
- Tools: NVIDIA DGX Spark (GB10, 128 GB unified memory, 273 GB/s), NVIDIA RTX 5090, NVIDIA RTX 3090, NVIDIA RTX 3080, Framework desktop (128 GB), NVIDIA H100 (cited via SemiAnalysis benchmark), gpt-oss-120b, DeepSeek v4 Flash, DeepSeek v4.1 Flash, Qwen dense ~27B model (caption reads 'Quen 3.827B'), Strata, OpenRouter

## [Don't Buy a GPU Instead Build This 32GB Free AI Server Instead](../videos/IMVjEsKX5UQ.md)
`IMVjEsKX5UQ` · Kai Explains · 2026-10-19 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency

Kai tests the viral "free 32GB AI server" on Kaggle's two T4s and finds layer-split speed and slow prefill make it a lab, not a daily coder; the TPU VM option is the better free route.

- Techniques: Check whether a model fits per card before adding GPUs; Measure prefill (time-to-first-token) separately from tokens/s; Check proxy and tunnel timeouts against TTFT; Convert a free compute quota into tokens and dollars; Run a 27B model at full precision on Kaggle TPU VM; Audit launcher code and model provenance before giving tokens; Never rely on a URL as the secret for an Ollama endpoint; Expect URL churn on idle-killed notebook sessions
- Tools: Kaggle (notebooks, GPU and TPU accelerators), Nvidia Tesla T4, Google TPU VM (8 chips), Ollama, Cloudflare Quick Tunnel, Qwen3-27B (4-bit and full 16-bit), vLLM (TPU backend, 0.28.0), Kaggle TPU lab (GitHub project, MIT), Claude Code, Hermes (coding agent), OpenRouter, Cerebras

## [Qwen 3.8 27B Just Hit 200 Token/s on Mac M5 (Lithos Metal)](../videos/L7noXCBSObc.md)
`L7noXCBSObc` · Kai Explains · 2026-10-19 · q4 · practitioner · review · also: inference-serving, evals

Dissects Lithos Metal's "200 tok/s" Qwen 27B claim on Apple M5 Max: a projection, with ~80 tok/s measured end-to-end. Speculative decoding helps on code, hurts on English, and agent sessions are prefill-bound.

- Techniques: Estimate decode ceiling from memory bandwidth; Speculative decoding with a small drafter; Measure acceptance rate alongside tok/s; Estimate whole-session time from prefill and decode rates; Time the whole task instead of quoting tok/s; Lower thinking-mode effort for local Qwen; Read the benchmark repo before the blog post
- Tools: Lithos Metal (engine, v0 Zero 1.2 mentioned), Qwen 3.8 27B (model, 4-bit), dSpark (speculative-decoding drafter, 1.1 GB), DeepSeek speculative decoding paper (July), MLX, MLX D-SPARK, Ollama, OMLX, D-Flash 2 (Z-Lab and Inco), Splash (Inco), MLTF (as transcribed), AgentPerfLocal (benchmark that replays agent sessions)

## [Every Way to Get 512GB of VRAM for Local AI (at Full Context)](../videos/6tihP50zlcE.md)
`6tihP50zlcE` · Kai Explains · 2026-10-19 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency

Compares hardware routes to 512GB for local LLMs, arguing KV-cache bytes per token, not file size, decides whether full context fits, with cost, speed and API break-even math.

- Techniques: Memory budget formula for local serving; Keep a lookup-table component on SSD (Engram-style); Leave allocation headroom on unified-memory nodes; Raise the Mac GPU memory limit, and re-check after reboots; Break-even check: owned hardware vs API; Rent before buying
- Tools: Muse Spark Open (Meta, 816B parameters), DeepSeek V4.1 Flash, DeepSeek API, GLM 5.3 (4-bit build), GLM 5.2, Kimi K3 (1.56TB download), DwarfStar (inference engine, originally by antirez), Apple Mac Studio M5 Ultra, Apple Mac Studio M3 Ultra, NVIDIA DGX Spark (GB10, 128GB), NVIDIA DGX Spark 64GB unit, NVIDIA RTX Pro 6000 Blackwell Max-Q (96GB)

## [This 164MB Speech Model Might Replace Whisper...](../videos/eskgvQYchd0.md)
`eskgvQYchd0` · Better Stack · 2026-10-19 · q4 · practitioner · review · also: voice-multimodal, models-research

Review of "Phonon 2," a 164 MB local speech-to-text model from Fermion Research. It is fast and includes an OpenAI-compatible server, but the speed and accuracy claims rest mostly on the vendor's own benchmarks.

- Techniques: Local transcription setup; Live captions and hot words; Drop-in OpenAI-compatible speech server; Checking speed claims for the runtime, not just the model
- Tools: Phonon 2 (Fermion Research speech model), phonon CLI (transcribe, listen, serve), NVIDIA Parakeet (original 2.5 GB model), Parakeet Redux (178 MB, 1.58-bit weights, Moondream), Whisper Large V3 Turbo, whisper.cpp (Metal), MLX, Core ML, Fluid Audio (third-party Core ML port), OpenASR leaderboard, Python 3.10+, Fermion's Mac dictation app (named Detta in captions)

## [2 Million TV Boxes Are Already Infected. AI Is Next.](../videos/OfNajAPiGsM.md)
`OfNajAPiGsM` · Better Stack · 2026-10-19 · q3 · intro · news · also: security-guardrails, models-research, inference-serving

Better Stack walks through Anthropic's research on whether a small model could self-replicate across cheap IoT devices like TV boxes, and why the capability requirements don't yet overlap.

- Techniques: Pipeline-split a model across many weak devices; Separate the requirements of a dangerous capability and test each one; Give every model the same stand-in task for a fair comparison; Keep a remote brain, local hands
- Tools: Anthropic research (AI worm / self-replication study), Gemma 4 26B (Google open model), Qwen 3.5 9B, Llama 3.1 8B, GLM 5.2 (about 753B parameters), ADB (Android Debug Bridge), Google Cloud (8 Android test machines), Jetson Nano, NVIDIA RTX 4090, NVIDIA H100, Kimwolf botnet (transcribed as Kinwolf)

## [How I Got Frontier Performance on 16GB VRAM (Qwen 3.8 27B)](../videos/h_KqS4GtU3I.md)
`h_KqS4GtU3I` · Kai Explains · 2026-10-19 · q4 · deep · review · also: inference-serving, token-cost-efficiency, models-research

Why a local Qwen 3.8 27B on a 16GB card often underperforms its leaderboard scores: the reasoning-effort setting, context window, and overthinking. Keep effort at xhigh, size the context to fit, and use the efficiency-tuned Swift 1.5 build.

- Techniques: Set reasoning effort on purpose, not to medium by default; Estimate the wall-clock cost of a reasoning run before starting; Work out the context budget before loading the model; Free GPU memory before loading the model; Turn on multi-token prediction; Use an efficiency-tuned build to cut thinking tokens; Check which setting a benchmark or guide actually used; Use hosted inference for long, parallel, or always-xhigh work
- Tools: Qwen 3.8 27B (transcribed 'Quen 3.827B'), Swift 1.5 (UQ AI retrain of Qwen 3.8 27B, IQ3 with MTP), llama.cpp, Hugging Face, Artificial Analysis Intelligence Index, GPQA Diamond, LiveCodeBench, SWE-Bench Pro, Terminal Bench 2.1, VulcanBench, ARC Prize, RTX 5060 Ti 16GB

## [Nokia Just Released a Free Jev Alternative (AnyJev)](../videos/hJz7zi17mXA.md)
`hJz7zi17mXA` · Better Stack · 2026-10-19 · q3 · practitioner · review · also: evals, models-research

Better Stack tests Nokia's AnyJEV, a training-free library that turns open models into probability-based classifiers; it fixes order bias but trails hosted JEV on accuracy and calibration.

- Techniques: Decision-model setup (AnyJEV flow); Order-swap flip test; L0 debiasing without labels; Confidence reliability check; Local throughput budgeting for debiased runs
- Tools: AnyJEV (Nokia applied research, Python, Apache 2.0), JEV decision model (hosted API via TypeSafe, v1.13), Qwen3 8B (run locally via llama.cpp on an M2 Max MacBook Pro), Hugging Face Transformers, vLLM, SGLang, llama.cpp, Kaggle News Headlines Dataset for Sarcasm Detection (28,619 headlines), Small demo app published by the host on GitHub

## [This Open-Source Engine Claims 2x Faster Than llama.cpp](../videos/90itFOj7jfo.md)
`90itFOj7jfo` · Better Stack · 2026-10-12 · q3 · practitioner · review · also: inference-serving, coding-agents

Hands-on test of Magnitude, a new Rust inference engine for Apple Silicon that tunes kernels per machine and targets agent workloads; the "2x llama.cpp" claim holds for one decode config but is mixed in independent tests.

- Techniques: Benchmark decode and prefill separately, and match KV-cache precision; Per-device kernel autotuning, cached per machine; Point Claude Code at a local Anthropic-compatible endpoint; Agent-serving cache and memory policy
- Tools: Magnitude (v0.2.5), llama.cpp, MLX, Ollama, Qwen 3.5 4B (Q8), Qwen 3.6 35B A3B (4-bit), Seismic (numerical compiler), Claude Code, Codex, OpenCode, RapidMLX, vLLM

## [Don't Buy a RTX Spark Laptop For Local AI Until You See This](../videos/aQKGejbv-Rs.md)
`aQKGejbv-Rs` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: inference-serving, coding-agents

Pre-review critique of the RTX Spark / Surface Laptop Ultra for local AI: the cold-prefill wait on long prompts (about 170 s at 128K) matters more for agent work than decode speed, and the wattage is still unpublished.

- Techniques: Cold prefill benchmark at real context length; Split throughput into prefill and decode; Sustained and battery soak test; Memory budget with OS and tooling headroom; Speculative decoding for decode speed; Keep the prompt cache warm in long sessions
- Tools: Microsoft Surface Laptop Ultra, NVIDIA RTX Spark N1X, NVIDIA DGX Spark, Surface RTX Spark Dev Box, MAI Code 1.1 Flash (Microsoft coding model, 137B total / 6.8B active MoE, about 53 GB compressed), llama.cpp (Windows on ARM build with CUDA; transcribed as 'Lama CPP'), DFlash 2 speculative decoding (transcribed as 'DF Flash 2'), GitHub Copilot, Windows 11, NVIDIA Linux (DGX Spark), AMD Ryzen AI Max Plus 395, ASUS ROG Flow Z13

## [This 125B AI Model Runs 5x Faster on My PC Than in the Cloud (Using Strata)](../videos/vrVaGp_YmQY.md)
`vrVaGp_YmQY` · Better Stack · 2026-10-12 · q3 · practitioner · review · also: inference-serving, token-cost-efficiency

Tests Strata, an open-source runner that spreads a 125B Qwen MoE across RTX 5090 VRAM, system RAM and SSD, against the cloud-hosted model; local is 3-5x faster on short tasks, with caveats.

- Techniques: Tiered expert placement for MoE models larger than VRAM; Per-layer GPU/CPU handoff through shared memory; Speculative decoding with the model's own small helper; Local install and first run (as shown); Fair side-by-side latency comparison of local vs cloud
- Tools: Strata (free, open-source local MoE runner; the paper is referenced but not named), Qwen 3.8 Flash (Next), 125B-parameter MoE; transcript spells it 'Quen', OpenRouter (hosted Qwen 3.8 Flash endpoint used for the cloud comparison), NVIDIA RTX 5090 (32 GB VRAM, test machine), NVIDIA RTX 5070 (12 GB, referenced from the Strata README only), Intel Core Ultra 9 285K (test machine CPU), Speaker's own side-by-side comparison app (speed, time and cost tracking; not named), Python (language for the palindrome test prompt)

## [Every Ways to Get 128GB VRAM for Local AI at Full Context](../videos/NA9D49kQFuU.md)
`NA9D49kQFuU` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency

Kai's buyer's guide to reaching 128GB of memory for local AI: prices every route, shows that expert offloading and the inference engine matter more than raw pool size, and ends with per-budget recommendations.

- Techniques: Expert / lookup-table offloading for large sparse models; Benchmark prefill and decode separately at real context length; Raise the GPU-addressable memory limit before loading; Quantization ladder by available memory; Draft-ahead decoding for speed on DGX Spark-class hardware; Rent-vs-buy break-even check
- Tools: Qwen Flash Next (as transcribed; 4-bit, 3-bit, 2-bit builds), Qwen 3.8 27B (as transcribed), Strata (inference engine, offload-capable), Gufo (community fork of an inference engine), Halogen (closed-source inference engine), MLX serve (Mac inference engine), llama.cpp, vLLM (implied by the RTX 5090 setup context only if mentioned; not named in transcript), CUDA, Linux kernel flags (mentioned, not specified), AMD Ryzen AI Max Plus 395 (Strix Halo), AMD Ryzen AI Max Pro 495 (192GB)

## [Turning My Obsidian Vault Into a Local AI Engineer — Filip Makraduli, Superlinked](../videos/Ndp5VaqFrl0.md)
`Ndp5VaqFrl0` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: mcp-and-tools, inference-serving, security-guardrails

Filip Makraduli (Superlinked) shows a privacy-first setup: a self-hosted MCP tool server runs OCR, redaction and extraction on sensitive documents in your own cloud, so a Claude Code agent only sees the cleaned output.

- Techniques: MCP tool server in front of private inference; Per-worker batching instead of a shared queue; Multi-model hot-swapping on one GPU; Stateless tools-only MCP server over streamable HTTP; Check thinking-token settings per model in tool pipelines; Warm-model-aware routing (roadmap)
- Tools: MCP, Claude Code, Obsidian, Superlinked, Terraform, Helm, Kubernetes, Docker, Claude Co-work

## [The Tiny TTS Everyone Loved Isn't Tiny Anymore (KittenTTS 2)](../videos/9YzLI8-uF4s.md)
`9YzLI8-uF4s` · Better Stack · 2026-10-12 · q3 · practitioner · review · also: voice-multimodal, governance-compliance

Hands-on review of KittenTTS 2: it has grown to 1.7B parameters, runs slower than real time on a Mac CPU, and ships source-available weights under a revocable, revenue-gated license, unlike the tiny Apache-2.0 original.

- Techniques: Clone a voice from a short reference clip; Check that the GPU is actually used; Turn off text normalization for non-English text; License gate before shipping model weights
- Tools: KittenTTS 2 (Kitten TTS v2), Kitten TTS (original, Apache 2.0), S3 Gen vocoder (Resemble AI, Chatterbox Turbo), Whisper (reference-clip transcription), PyTorch (torch), transformers, diffusers, Activity Monitor, ElevenLabs, VoxCPM2, libtorch (C++ port), Hugging Face

## [The End of AI Hallucinations? Meta's New Fix (CLM's)](../videos/9-iiHFQyzuM.md)
`9-iiHFQyzuM` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: context-engineering, agent-architecture, token-cost-efficiency

Meta/UW's Context Language Model lets the model prune its own context through a bash-edited file instead of harness summaries. Gains are mostly compute; KV-cache costs hurt local use.

- Techniques: Notes-file handoff for long agent runs; Context-as-file self-editing (CLM pattern); Keep edits rare and context small; Suffix Cache Reuse (paper's serving fix)
- Tools: Meta CLM paper (Context Language Model, Meta and University of Washington), Qwen 27B, Qwen 9B, Claude Sonnet, Claude Opus 5.5, GPT, bash, Python, SGLang, vLLM, llama.cpp, Ollama

## [Is 16GB All You Need for Serious Local LLM?](../videos/i9mRnbdDYxk.md)
`i9mRnbdDYxk` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency

Kai Explains argues a 16GB GPU fits a 27B model but can't finish real agentic coding sessions: the KV cache, bandwidth, prefill and multi-token prediction decide usable speed and context, not whether the weights load.

- Techniques: VRAM budget before loading a model; Reclaim memory from defaults; Turn multi-token prediction off past a context threshold; Size the model to the conversation; Measure prefill and decode separately; Local-vs-hosted break-even; Tensor split for two cards
- Tools: llama.cpp (called 'Lama CPP' in captions; the speaker calls it the most common local AI runtime), Qwen 27B-class model (captioned 'Quen 3.827B'; Q4 at 17.44 GB, a DASLab GSQ build at 11.8 GB), GSQ quantization (DASLab, IST Austria), Devstral Small 2 (captioned 'DevStraw Small 2'; 160 KB KV per token), Claude Code (captioned 'CloudCode'), OpenRouter (hosted price benchmark), Nvidia RTX 5060 Ti 16GB, Nvidia RTX 5070 Ti, Nvidia RTX 5090, AMD RX 9060 XT 16GB, AMD RX 9070 XT, Apple Mac mini (chip name garbled in captions)

## [Agents That Own Their Inference — Du'an Lightfoot & Khaja Omer, Akamai Technologies](../videos/4n08JHb90hI.md)
`4n08JHb90hI` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: inference-serving, infra-cost-scaling, evals

Akamai hands-on workshop on self-hosting LLM agents on a single GPU with vLLM: memory budgets, prefill vs decode, FP8 quantization, speculative decoding, and finding the concurrency knee.

- Techniques: Memory budget math; Concurrency sweep to find the knee; One-flag-at-a-time tuning; Quantize with your own eval set; Validate speculative decoding by acceptance rate; Prefix caching for repeated context; Own-vs-rent break-even
- Tools: vLLM, Kubernetes, LKE (Akamai Linode Kubernetes Engine), KServe, SGLang, TensorRT-LLM, llama.cpp, Ollama, Prometheus, Grafana, Langfuse, LLM Compressor

## [Every Ways to Get 32GB VRAM for Local AI at Full Context](../videos/uavLRbbfM94.md)
`uavLRbbfM94` · Kai Explains · 2026-10-05 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency

A buying guide for getting 32GB VRAM for local AI at full context: why 27B dense at 6-bit plus 128K context needs about 28.5GB, which cards and engines actually deliver, and when renting beats owning.

- Techniques: VRAM sizing before buying; Check the engine's startup log for usable memory; Two-card tensor split; Multi-token prediction; Speculative decoding on a patched vLLM build; Rent-vs-own break-even; Full-cost comparison for a GPU purchase
- Tools: Qwen 27B-class dense model (captioned as Quen 3.827B), 6-bit quantization, llama.cpp (default engine, with layer and tensor split modes and multi-token prediction), LM Studio (beginner frontend), vLLM and community forks: vLLM Radiance, a Ninfer/Eninfer V100 fork, OneCat VLLM (captioned names), ROCm (AMD) and CUDA 12 / CUDA 13 (Nvidia), GGUF model files, macOS unified memory on Mac mini, RunPod (rented RTX 5090), OpenRouter (hosted Qwen pricing), Vast.ai (rental pricing listing), Digital Spaceport GPU price tracker, RepoChat GPU comparison

## [I Gave a Robot Duck a 15MB AI Brain (Needle 3)](../videos/KQcQ7P78eTI.md)
`KQcQ7P78eTI` · Better Stack · 2026-10-05 · q3 · practitioner · review · also: training-finetuning-rl, mcp-and-tools, evals

Walkthrough of Cactus Compute's Needle 3 on-device tool-calling model: a size-adjustable layer ladder, local fine-tuning on a robot-duck task, and a 49-prompt held-out eval (27% base, 84% fine-tuned 20-layer).

- Techniques: Closed-set tool dispatcher; Layer-truncatable model (intelligence ladder); Rule-categorised synthetic training data; Hand-written held-out scoreboard; Split controller from the LLM decision layer; Local fine-tune over LAN to a GPU box
- Tools: Needle 3, Needle 2, Cactus Compute fine-tuning platform, OpenDuck Mini, MuJoCo, DeepSeek V4 Flash, NVIDIA RTX 5090, ESP32, Pebble Index Ring, BDX droids (Disney)

## [Deepseek & Huawei Made Local AI Run Without NVIDIA's CUDA (And Why it's Hard)](../videos/uJcPjrEgppk.md)
`uJcPjrEgppk` · Kai Explains · 2026-10-05 · q4 · practitioner · news · also: inference-serving, models-research

DeepSeek's Ascend kernel release looks like a CUDA challenger, but its 99.8% figure measures efficiency against Huawei's low ceiling; the stack still depends on Huawei's runtime and the hardware is not yet available.

- Techniques: Read utilization numbers against their denominator; Drop-in kernel swap via identical package/import names; Check hardware provenance and license footnotes before depending on a release; Pin runtime versions to the vendor stack the kernels require
- Tools: DeepGEMM, FlashMLA, DeepEP, TileKernels, TileLang, Apache TVM, CANN 9.2.0, vLLM, llama.cpp, NVCC, CUDA, Ascend 950DT

## [This Speech Model Went From 1.2GB to 178MB (Parakeet Redux)](../videos/sr550syhwL0.md)
`sr550syhwL0` · Better Stack · 2026-10-05 · q3 · practitioner · review · also: voice-multimodal, models-research

Moondream's Parakeet Redux compresses NVIDIA's Parakeet speech model from 1.2GB to 178MB using ternary weights, with near-equal English accuracy. The inference engine is closed, and noisy audio degrades more.

- Techniques: Quantized local speech-to-text on CPU; Word-level timestamps for subtitles; Transcribe a slice of a long recording; Live microphone streaming with replace-not-append handling; Language-agnostic input; Benchmark on your own hardware before trusting speed claims; Keep the original Parakeet for noisy audio
- Tools: Parakeet Redux (Moondream), NVIDIA Parakeet 0.6B v3, Parakeet.cpp, Whisper large-v3-turbo, whisper.cpp, PyTorch, Photon (Moondream inference engine, not open source), Kestrel kernels (proprietary license), Deepgram Nova 3, OpenAI mini-transcribe, Parakeet variant the speaker calls 'parakeet mix' (Apache-licensed; exact name unclear in captions)

## [The New Way to Run 125B Models 6× Faster Than llama.cpp (Strata)](../videos/m0VHx73SAG0.md)
`m0VHx73SAG0` · Kai Explains · 2026-10-05 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency

Review of Strata, a new engine that runs a 125B-parameter MoE model on a 12 GB GPU plus 64 GB RAM. The headline "6x" is inflated; the honest gain is about 2 to 2.5x, with a quality trade-off and a real RAM cost.

- Techniques: Hot-expert GPU cache with CPU cold path; Use multi-token prediction with a trained draft head; Keep big embedding tables on SSD and read only the rows needed; Choose quantization by workload; Tune the host before blaming the engine; Benchmark speed claims fairly; Point a coding agent at a local Anthropic-compatible endpoint
- Tools: Strata (v0.1, GitHub, launched Sept 24; one-click Windows installer or Linux script), llama.cpp (including the multi-token-prediction merge on Oct 1 and the expert-cache draft PR open since Aug 28), Qwen 3.8 Flash Next (125B total, ~6B active; 2-bit Q2, 3-bit IQ3 and full-precision builds), Qwen 3.8 27B (comparison model), Qwen4 (mentioned as the next architecture, not tested), Claude Code (pointed at the local endpoint), LiveCodeBench (benchmark), SWE-Bench Pro (benchmark), NVIDIA RTX 5070 (12 GB), RTX 5090 (32 GB), RTX 3090, DDR5-6000 / DDR4 system RAM, Tom's Hardware price index, LocalLLaMA forum

## [Stop Renting Your AI's Memory — Dylan Couzon, Qdrant](../videos/apyrzaWj0Z4.md)
`apyrzaWj0Z4` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: memory, rag-retrieval

Dylan Couzon (Qdrant) argues agent memory should be owned locally: models are rented, but a private, retrieval-based memory store compounds and stays portable. Includes a live offline drone-vision memory demo.

- Techniques: Write-retrieve-forget memory loop; Embedded in-process vector store with per-app folder; Quantized vectors for small footprint; Pin the embedding model for portability; Detector labels then embeddings for perception memory; Opt-in sync of local memory to a shared store
- Tools: Qdrant, YOLO

## [Is Frontier Class Local AI Finally Possible?](../videos/1--PzaHafAU.md)
`1--PzaHafAU` · Kai Explains · 2026-10-02 · q4 · practitioner · news · also: inference-serving, models-research, token-cost-efficiency

Frontier-class open-weight models can now run on consumer hardware by moving a lookup table to SSD, but prefill speed and rising hardware prices limit local use to batch work rather than interactive agents.

- Techniques: Split latency into prefill and decode when judging local hardware; Budget SSD-offloaded parameters by bytes-touched-per-token; Batch local, interactive hosted; Verify a quantized build against the official weights; Check the prefill number and the memory floor before buying
- Tools: Qwen (Flash Next, Qwen 4 architecture preview), DeepSeek V4 Pro, DeepSeek V4 Flash, Kimi K3, Unsloth (1-bit quantized builds), llama.cpp (SSD offload support, per community report), Claude Code (system prompt size cited), NVIDIA RTX 3060, NVIDIA RTX Pro 6000 Blackwell, NVIDIA H100, NVIDIA 4xH200 (hosted comparison), NVIDIA DGX Spark

## [This AI Startup Is Making Powerful AI Models (Desert Ant Labs)](../videos/P_7HwwUsOfA.md)
`P_7HwwUsOfA` · Better Stack · 2026-10-02 · q3 · intro · review · also: voice-multimodal, security-guardrails

Better Stack hands-on tour of 12 tiny on-device models from Desert Ant Labs (speech, redaction, language ID, emoji). Several are fast and useful, some are weak, and the vendor benchmarks are mostly unverified.

- Techniques: Small specialist model as a background layer; Smoke-test a vendor micro-model on your own data inside a thin wrapper app; Read the confidence score before trusting a language-ID result
- Tools: Desert Ant Labs (vendor, 12 shipped models plus 5 beta), Hugging Face (model hosting), GitHub (SDK), Vaus (on-device speech recognition, claims 10 min audio in ~2 s on iPhone), Clear (speech enhancement), Clips (highlight extraction from long recordings), Clipper (desktop app built on Clips), Title (short factual title and description from text), Redact (on-device PII stripping as you type, 27 languages), Um (filler-word removal), Emo (emoji suggestion, ~5 MB), Gist (topic and tag prediction from titles, claims 101 languages)

## [Xiaomi & DeepSeek Just Solved the Biggest Bottleneck in Your Local AI](../videos/RlRC_6hbBHc.md)
`RlRC_6hbBHc` · Kai Explains · 2026-10-02 · q4 · practitioner · news · also: inference-serving, token-cost-efficiency, models-research

Explainer on DeepSeek V4.1 Flash and Xiaomi HiSparse 2, two independent designs that split a model so the bottom half reads the prompt once; the real gain is cheaper reading (prefill), not memory, and recall is not yet proven.

- Techniques: Cross-layer KV sharing (YOCO-style split); Split input-token cost into cache-hit and cache-miss; Benchmark prefill tok/s and time-to-first-token at 100k and 1M; Run a recall test before trusting long context; Trim large tool output before it enters context (inferred, not stated in video)
- Tools: DeepSeek V4.1 Flash, HiSparse 2 (Xiaomi), MIMO v3 (Xiaomi's next model, per Luo Fuli), YOCO (You Only Cache Once, Microsoft Research and Tsinghua, May 2024), Grouped query attention (referenced), Qwen (smaller model grafted by a LocalLLaMA user), Apple M3 Ultra (512 GB, local benchmark), KV cache

## [DeepSeek Just Shrunk the KV Cache 437×](../videos/n-_e9bROGHo.md)
`n-_e9bROGHo` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency, models-research

Kai rebuilds DeepSeek's "437x smaller KV cache" ratio from config files, shows the denominator compares a 2023 dense model to a 2026 MoE, and explains how sparse layers and 4-bit storage cut per-token cache cost.

- Techniques: Compute KV bytes per token from the model config; Normalise cache comparisons to the same generation and to the same max context; Size node concurrency as free HBM divided by per-session cache; Separate the single-user and multi-user cost models; Check the failure modes of sparse selection and replay; Track output tokens separately from input tokens
- Tools: DeepSeek V1 (dense, grouped-query attention, 4,096 context per speaker), DeepSeek V4.1 Flash (sparse MoE, 40 layers, 1M context, 4-bit experts), DeepSeek V4 Flash (predecessor to V4.1 Flash), DeepSeek V4 Pro (flagship; reversed retirement per speaker), DeepSeek V3 (671 GB at 8-bit, 163,840-token limit), Hugging Face (config files), NVIDIA H200 SXM (141 GB HBM3E per card, 8-card node), Apple M5 Ultra Mac Studio (512 GB), Mac mini (16 GB, SSD weight streaming in developer test), Artificial Analysis (benchmark for output tokens per second)

## [This Tiny Coding Model Shouldn’t Be This Good (MiniCPM5)](../videos/Wik_JQ-enUA.md)
`Wik_JQ-enUA` · Better Stack · 2026-10-02 · q4 · practitioner · review · also: inference-serving, evals, models-research

Review of OpenBMB's 2B MiniCPM5: strong on agent and tool benchmarks against Qwen 3.5 4B, but quantized GGUF runs loop under the documented llama.cpp defaults until min_p and repeat penalty are changed.

- Techniques: Run a small model on a Mac with MLX in a virtualenv; Tool-calling smoke test against a local OpenAI-compatible server; Fix the quantized sampler before judging a small model; Count runaway generations, not just pass rate; Load a GGUF into Ollama or LM Studio without a library entry
- Tools: MiniCPM5 2B (text-only, OpenBMB), MiniCPM5 1B, MLX / mlx-lm, llama.cpp (server), GGUF, OpenAI-compatible client, WebLLM, Ollama, LM Studio, Hugging Face, Qwen 3.5 (2B and 4B), Gemma 4 E2B

## [What It Actually Costs to Run Xiaomi MiMo V2.6 Pro & Flash Locally?](../videos/3hMEcJCGne0.md)
`3hMEcJCGne0` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency, models-research

Why running Xiaomi MiMo V2.6 Pro/Flash locally rarely beats the API on cost: weights already 4-bit, bandwidth caps speed, electricity alone outprices hosted tokens. Only privacy or speed justify it.

- Techniques: Check whether a release is already quantized before quantizing; Estimate the decode speed ceiling from memory bandwidth; Compare local vs API on electricity and break-even before buying hardware; Raise the output cap for reasoning models and turn sampling back on; Measure prefill and decode separately for long contexts
- Tools: Xiaomi MiMo V2.6 Pro, Xiaomi MiMo V2.6 Flash, Xiaomi MiMo V2.6 Distilled (9B), DeepSeek V4.1 Flash, MLX (Apple), llama-bench (llama.cpp), NVIDIA DGX Spark, AMD Ryzen AI Max (Framework desktop), Apple Mac Studio M5 Ultra / M3 Ultra, AMD EPYC (12-channel DDR5 server), NVIDIA RTX Pro 6000, NVIDIA RTX 3060 (12 GB)

## [Don't Buy a Local AI Hardware Until You See This](../videos/L4UV6b2Xc64.md)
`L4UV6b2Xc64` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: token-cost-efficiency, inference-serving

Argues local AI hardware is mispriced: resale value, bandwidth per dollar, prefill latency, idle power and break-even against hosted tokens all matter more than list price or capacity.

- Techniques: Bandwidth per dollar and capacity per dollar as separate metrics; Break-even against hosted tokens; Measure prefill separately from decode; Resale liquidity check; Idle power cost
- Tools: NVIDIA DGX Spark, Framework desktop (Ryzen AI Max, unified memory), Apple Mac Studio M3 Ultra (512GB), NVIDIA RTX 3090, NVIDIA RTX 3080, NVIDIA RTX 3070, NVIDIA RTX 4090, NVIDIA RTX 4070, NVIDIA RTX 5090, NVIDIA RTX 5080, NVIDIA RTX 5060, NVIDIA RTX 3060

## [Is 8GB VRAM enough for 27B models? Tested](../videos/P1K36q76Uzk.md)
`P1K36q76Uzk` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: models-research, inference-serving, token-cost-efficiency

Kai reviews Prism ML's Bonsai 2 (a 27B model compressed to about 1.75 bits per weight, 5.95 GB). The memory win is real, but the vendor's headline numbers hide reasoning-time, agentic and loader problems.

- Techniques: Blockwise Hadamard rotation before ternary rounding; Compare compressed models against the baseline you actually run; Measure long-context generation speed, not TG128; Verify local model loads before trusting output; Keep reasoning effort at default for routine prompts; Supported install path (as stated; repo name not given)
- Tools: Bonsai 2 (Prism ML 27B ternary model, 'Bonsai 227B' in auto-captions), Qwen 3.8 27B (base model, Apache 2.0), llama.cpp (named as 'StockLama CPP' in captions), Ollama (GGUF parser; unofficial Bonsai upload on registry), MLX loaders, Prism ML fork (build B10658 or newer, as transcribed), Q4 / UDQ4 GGUF builds (about 17.6 GB), IQ2 2-bit 27B build, Terminal Bench 2.1, SWE-bench Verified, AIME26 (AIME-style math), IFBench

## [Can a Mac Mini Replace your $200 AI Subscription?](../videos/3R7yba577uA.md)
`3R7yba577uA` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: token-cost-efficiency, inference-serving

Kai argues a $1,299 Mac Mini cannot replace a $200 coding-agent subscription: it only matches the model, not the hosted reading speed or usage allowance, and at per-token prices its output is worth about $19 to $190 a month.

- Techniques: Decode throughput ceiling check; Prefill budget for agent prompts; Prefix caching accounting; Monthly break-even formula; Hybrid orchestrator with cheap hosted subtasks; Usage audit before plan change; Speculative decoding (conceptual); Memory sizing with OS headroom
- Tools: Qwen 3.8 27B (captioned 'Quen 3.827B'; Apache 2.0, about 16.05 GB compressed build), Qwen 3.6 35B-class model (captioned 'Quen 3.635B'; the speaker says it is an older small model), Opus 5.0, Opus 5.5, Fable 5.1, GPT-6, GPT 5.6 Sol, Claude Code, Claude sessions (Anthropic cloud, launched with a $250 introductory credit on Macs per speaker), Codex, OpenClaw, Hermes (agent setups named as the driver of Mac Mini demand)

## [The Real Reason Behind NVIDIA Buying Hugging Face](../videos/s7dKx9Pl2j0.md)
`s7dKx9Pl2j0` · Kai Explains · 2026-10-02 · q3 · intro · news · also: security-guardrails, models-research, sandboxing-execution

Kai Explains argues NVIDIA's $12.9B Hugging Face deal is about the open-weights policy fight, prompted by an AI agent's sandbox escape and breach of Hugging Face, not just distribution.

- Techniques: Treat an egress proxy as an attack surface, not a containment guarantee; Use a locally run open-weight model for incident forensics when closed APIs refuse or data cannot leave; Triage agent-driven intrusion logs for machine-like signatures; Prefer non-executable weight formats, and still audit the loading pipeline
- Tools: Hugging Face Hub, OpenAI Exploit Gym (benchmark), GPT 5.6 Sol (named in the video), GLM 5.2 (open-weight model), safetensors, PyTorch Foundation, NVIDIA Base Command Manager, Bright Computing, Slurm (SchedMD), CUDA, NVIDIA open agent framework

## [Is it Possible to Run Any LLM in Jev Mode Using llama.cpp?](../videos/Oi4JPj58lUA.md)
`Oi4JPj58lUA` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: inference-serving, evals, data-engineering

Breakdown of "Jeff mode": llama.cpp constrained choice scoring is fast, but its confidence score comes from masking and renormalizing, needs calibration on your own data, and its speed depends on model architecture.

- Techniques: Forced-choice classification via cached-prompt branch scoring; Single-field logprob check on the stock server first; Calibrated confidence gate with escalation; Temperature scaling for post-hoc calibration; Group requests by schema to keep the prompt cache warm; Benchmark hygiene for local inference; Keep dependent fields in plain generation
- Tools: Jeff (TypeSafe structured-classification product, as captioned; the title spells it 'Jev mode'), llama.cpp, llama.cpp fork by Kodakus (parallel constrained decoding, two commits), llama.cpp stock server (n_probs / logprobs parameters), NotJeff (project reproducing the approach with stock llama.cpp, Qwen3-8B reported), Qwen 1.5B (plain attention, 28 layers), Qwen3-8B (captioned 'Quen38b'), Qwen 3.6 35B-A3B (captioned 'Quen 3.635BA3B', MoE), Gemma 4 12B (captioned 'Gemma 412b', sliding-window), Insider LLM 27B model (described as dense; config shows hybrid), Banking77 (public bank-intent dataset), Temperature scaling (calibration method)

## [The End of VRAM-Bottlenecked LLMs: Qwen3.8-Flash-Next](../videos/MPrQA-M4Zn4.md)
`MPrQA-M4Zn4` · Kai Explains · 2026-10-02 · q4 · deep · news · also: inference-serving, models-research

Qwen's Flash-Next model stores a 51B n-gram embedding table that can sit in system RAM and be prefetched, so local model fit depends on host RAM vs table size, not VRAM alone.

- Techniques: Deterministic lookup-table offload to host RAM with asynchronous prefetch; Host-RAM-first sizing check for a local model; Context-sweep benchmark for offload tax; KV-cache budget from bytes per token; Support-status checklist before adopting a fork
- Tools: Qwen 3.8 Flash Next (Qwen model; config self-identifies as Qwen4 experimental), DeepSeek Conditional Memory via Scalable Lookup (paper, January), vLLM (official recipe, opt-in host offload env var), llama.cpp (PR 27742, fork only), MLX (external table storage, unreleased PR), Unsloth (one-bit dynamic build), NVIDIA DGX Spark, RTX 4090, RTX 5090 (ruled out by the official vLLM recipe), NVFP4, Muon optimizer (vs AdamW), Gated delta net (hybrid attention)

## [I Tested Every Local AI Model So You Don't Have To](../videos/C9M6iUFtVB4.md)
`C9M6iUFtVB4` · Kai Explains · 2026-10-02 · q3 · practitioner · review · also: inference-serving, token-cost-efficiency

Local-model buying guide by GPU tier: context budget (KV cache) and read speed matter more than which model you pick. Covers quantization pitfalls, two free speed settings, and when renting beats owning.

- Techniques: Budget the KV cache per context length, not just model size; Set the context window explicitly; Cut harness overhead before the first prompt; Enable multi-token prediction; Use medium reasoning effort instead of the max default; Vet quantized builds on your own tasks; Run a mixture-of-experts model with experts offloaded to RAM on 8 GB cards; Split planning from execution across frontier and local models; Track prefill (read) speed separately from generation speed
- Tools: MCP, Mistral 24B (unnamed variant), Apple Silicon, Mac Studio, Reddit

## [This Open-Weights TTS Beat ElevenLabs... Then I Read the License](../videos/kJppefEh2ZA.md)
`kJppefEh2ZA` · Better Stack · 2026-10-02 · q4 · practitioner · review · also: voice-multimodal, evals

Josh from Better Stack tests Breeze TTS 2, an open-weights voice model that tops a benchmark, then shows why its non-commercial weights license blocks most real use.

- Techniques: Local voice-design install on macOS; Lower CFG scale to make voice descriptions stick; Inline vocal-event markup; License check before adopting open weights; Read leaderboards for vote count and prompt control
- Tools: Breeze TTS 2 (Breeze Blue), MLX audio (mlx-audio, pip install), Qwen 3, Qwen3-TTS, T5Gemma 2, Mimi audio codec, ElevenLabs Conversational, Cartesia Sonic 3.6, Artificial Analysis speech arena, Kokoro, Chatterbox, VoxCPM2

## [Don't Buy a Mac Mini For Local AI (Do This)](../videos/IRyiP_U7RuA.md)
`IRyiP_U7RuA` · Kai Explains · 2026-10-02 · q3 · practitioner · review · also: inference-serving, models-research

Kai Explains argues that buying a Mac Mini for local AI is a poor first move: size memory for the model you actually run, switch inference servers and measure time-to-first-token, and rent the model for a month before buying.

- Techniques: Measure end-to-end latency (time to first token + generation), not just tokens/s; Swap the default local inference server before buying hardware; Prefer sparse MoE models for local inference; Size memory for the model you run today, plus KV cache headroom; Rent the model for a month before buying hardware
- Tools: Apple Mac Mini (M6, M5 Pro), Apple Mac Studio (M5 Max, M5 Ultra), Framework Desktop (Ryzen AI Max), NVIDIA DGX Spark, NVIDIA RTX 5090, gpt-oss-120b, Mixture-of-experts 35B model (unnamed), Dense 27B model (unnamed), Apple machine learning research post (cited for bandwidth-bound token generation)

## [How AI Got Smaller And Still Became Smarter](../videos/LqAxNIalgOw.md)
`LqAxNIalgOw` · Kai Explains · 2026-10-02 · q4 · practitioner · news · also: inference-serving, token-cost-efficiency, models-research

Walks through why "smaller" AI models are not cheaper to run locally: active parameters cut compute but not memory, KV cache grows per token, and reasoning-effort defaults inflate cost; benchmarks also mix setups.

- Techniques: Estimate KV cache memory from config before loading a long-context model; Lower the reasoning-effort preset to cut thinking tokens; Read benchmark footnotes for harness and settings before comparing; Separate active and total parameters when sizing MoE models
- Tools: Qwen3.6-27B (Alibaba, 27B dense-active MoE claim, 262K context), Qwen Flash Next (180B total, 6B active), DeepSeek (budget model, 284B to 552B backbone), Claude Opus, GPT-5.5 Codex, Terminal Bench 2.1, SWE-Bench Pro, GPQA Diamond

## [Mac Studio vs AMD AI PC: Don't Buy Before Watching This](../videos/dlyic4oco4s.md)
`dlyic4oco4s` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: inference-serving, infra-cost-scaling

Mac Studio M5 vs Ryzen AI Max+ 395 for local AI: prefill, not tokens/sec, dominates wait time, MoE models shrink Apple's lead, and cheap AMD mini PCs can be misconfigured traps.

- Techniques: Measure prefill and decode separately, at your real context length; Pick hardware by model architecture; Check that the GPU math library is actually in use; Tune the AMD unified-memory box (documented steps as described); Run a constellation of small resident models under an orchestrator; Vet mini-PC SKUs before buying; Use newer open-source attention kernels on the AMD iGPU
- Tools: Mac Studio M5, Apple M5 Ultra, Apple M5 Max, Apple M4 Max, Apple M1 Max, AMD Ryzen AI Max Plus 395, Framework Desktop, Minis Forum MS-S1 Max, Gemma 4 (12B, dense), gpt-oss-120b (~116B total, ~5.1B active), Qwen 3.6 (35B-class MoE, about 3B active), a 122B model (name not given)

## [Apple Won the AI Race](../videos/Ba3xunEk8Y8.md)
`Ba3xunEk8Y8` · Better Stack · 2026-10-02 · q2 · intro · news · also: models-research, product-ux

Better Stack argues Apple can win the AI race through distribution, device data and an on-device model that is good enough, not frontier model quality. Mostly speculative commentary with few verifiable facts.

- Techniques: Distill a frontier model into smaller deployable models; Run large MoE models locally by streaming experts from SSD and caching hot experts in RAM
- Tools: Apple Intelligence, Siri, Apple Foundation Models (AFM3 variants, names partly garbled in captions: AFM3 Core, AFM3 Core Advanced, AFM3 Cloud Pro, and one cloud variant), Private Cloud Compute, Google Gemini, Anthropic Fable (described as the public version of Mythos), Mythos (described as too dangerous for public release), OpenAI Sol Ultra (as captioned), Grok 4.6 (xAI), DeepSeek, Kimi, MiniMax

## [Qwen 3.8 27B Just Got 2× Faster on Mac Same Hardware](../videos/qZTmBhKz7b0.md)
`qZTmBhKz7b0` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: inference-serving, evals

A debunk of the "Qwen 3.8 27B 2x faster on Mac" headline: the 2x comes from speculative decoding with a 1.2 GB draft model, not the Splash engine, and the built-in multi-token-prediction head gives smaller gains for free. Measure effective tokens/s with warm and cold cache, not decode speed.

- Techniques: Measure effective tokens per second, cold and warm; Enable the model's built-in multi-token-prediction head as a draft; Bandwidth ceiling sanity check; Isolate the variable in a benchmark; Fail fast on memory; Point coding agents at a local OpenAI or Anthropic-compatible endpoint
- Tools: Splash (Inco AI inference engine for Apple Silicon, Apache 2.0, Qwen 3.8 27B and 35B only), Inco AI, D-Flash 2 (Splash's 1.2 GB draft model), Qwen 3.8 27B and 35B (built-in multi-token-prediction head), OMLX (inference engine used as baseline), LM Studio (shipped Splash as a selectable backend), MLX, GGUF, llama.cpp, Ollama, SpeedBench (coding benchmark with reasoning mode), Claude Code

## [Apple Just Made the Best Local AI Hardware. Do Not Buy It Yet.](../videos/12lxN9NHuHc.md)
`12lxN9NHuHc` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: inference-serving

Apple's M5 Ultra puts neural accelerators in every GPU core, but LM Studio's bundled runtime switches them off; prefill-vs-decode math and rising memory prices decide whether to buy now or wait.

- Techniques: Benchmark prefill and decode separately; Benchmark at long context (32K tokens and up); Check the runtime startup log for the accelerator path before trusting any numbers; Use the MLX build or upstream llama.cpp instead of the bundled LM Studio runtime for M5 Macs; Buy-or-wait decision rule; Compare memory upgrades by price per gigabyte
- Tools: Apple M5 Ultra, Apple M5 Max, Apple M5 Pro, Apple M3 Ultra, Apple M4 Max, MacBook Pro 14-inch (M5 Max, 128 GB), Mac Studio, LM Studio, llama.cpp (bundled runtime and upstream build), Metal 4 Tensor API, MLX, BaseRT (third-party runtime, paper July 21)

## [I Ran a 35B Param Model On My iPhone (Local AI)](../videos/hM_mEE8BXfU.md)
`hM_mEE8BXfU` · Better Stack · 2026-10-02 · q3 · practitioner · tutorial · also: inference-serving

Better Stack walkthrough of running Qwen 3.5 35B-A3B (a mixture-of-experts model) on an iPhone 17 at about 11 tokens/s by streaming experts from SSD, relying on the OS page cache, and tiered 4-bit/2-bit quantization, with the Flash MoE / Flash iOS setup steps.

- Techniques: Stream MoE experts from SSD and leave caching to the OS page cache; Tiered quantization by expert hotness; Validate expert reads against per-expert sizes; Build and sideload Flash iOS onto an iPhone (tutorial steps); Thinking-loop diagnosis for on-device MoE
- Tools: Flash MoE (Dan Woods; originally written for a MacBook), Flash iOS (iPhone port wrapping the Flash MoE engine), Qwen 3.5 35B-A3B (mixture-of-experts model, 35B total, about 3B active), Xcode, iPhone 17, metalinfer.m (file in the Flash MoE repo), Apple developer account

## [How Fast Is Local AI on Your Mac? (Every Chip, M1 to M6)](../videos/WoGwVXFmWzU.md)
`WoGwVXFmWzU` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: inference-serving

Kai Explains compares Apple Silicon Macs (M1 to M6) for local LLM use and argues that memory size, then memory bandwidth, then the exact chip variant predict real speed better than the chip generation, and that software and speculative decoding can matter more than hardware.

- Techniques: Decode throughput ceiling estimate; Memory-fit check before speed; Like-for-like benchmark protocol; Speculative decoding for memory-bound decode; Try a faster inference engine before buying hardware; Prompt-to-answer ratio rule for hardware choice; Cache-aware agent latency accounting
- Tools: Apple Silicon M1 through M6 (Mac Mini, Mac Studio, MacBook Pro and Air), llama.cpp (called 'Lama CPP' in the auto-captions), MLX (Apple's ML framework), Multi-token prediction (MLX variant), Splash (inference engine, as captioned; 52 tok/s on a short prompt), Speculative decoding with a small draft model, Qwen 27B (auto-caption 'QEN327B'), 4-bit, Apple Neural Accelerator (in M5 GPU cores)

## [Apple Hasn’t Put an LLM on Your Watch. So I Did.](../videos/IGQZuZkwVLI.md)
`IGQZuZkwVLI` · Better Stack · 2026-10-02 · q3 · intro · demo · also: inference-serving, dev-tools

Better Stack runs a 90M-parameter hybrid LLM offline on a 2020 Apple Watch Series 6 via llama.cpp built for watchOS, and explains the ARM64_32 and Core ML limits that shape the port.

- Techniques: Build llama.cpp for watchOS (ARM64_32); Check the 32-bit address ceiling before picking a model; Prefer small hybrid SSM models for memory-bounded edge devices; Register tools by renaming a samples file; Voice as the input channel on a wearable
- Tools: Falcon H1 (90M, hybrid attention + Mamba-2), small M2 135M model (caption-garbled name), llama.cpp, Core ML, Xcode, watchOS / ARM64_32, Mamba 2, GGUF model format, Wikipedia tool call (sample), weather tool call (sample)

## [Open Source AI is dying (and I know why)](../videos/zxnXemN98d0.md)
`zxnXemN98d0` · Kai Explains · 2026-10-02 · q4 · practitioner · talk · also: inference-serving, token-cost-efficiency, governance-compliance

Kai argues open-weight AI died at the size where models no longer fit on hardware you own. Below that line the freedom holds, and frontier open weights now work mainly as a price ceiling on hosted APIs.

- Techniques: Break-even check for self-hosting vs API; Local memory budget before choosing a model; Pin the provider, not just the model name; Detect silent compaction and context caps; Pre-adoption license and file audit
- Tools: Kimi K3, DeepSeek V4 Flash, DeepSeek V4 Pro, DeepSeek V3, Llama 3.3 70B, Llama 2, Gemma 4, Qwen 3.6, Alibaba Qwen, Ollama, OpenRouter, Lambda Labs

## [Mac Studio vs DGX Spark: Which Is Better for Local AI?](../videos/_NZeV2uOVnk.md)
`_NZeV2uOVnk` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: inference-serving, infra-cost-scaling

Kai Explains compares a Mac Studio (M3 Ultra, with M5 Ultra prices and specs) and an NVIDIA DGX Spark for local LLM inference, and argues the answer depends on whether the workload is decode-bound, prefill-bound, or CUDA-shaped.

- Techniques: Benchmark prefill and decode separately; Estimate decode ceiling from bandwidth; Size memory as usable, not nominal; Test concurrency, not just one stream; Disaggregated prefill and decode across two machines; Rent before buying
- Tools: Mac Studio (M3 Ultra, 819 GB/s; M5 Ultra for specs and pricing, 1.2 TB/s), NVIDIA DGX Spark (GB10, 128 GB LPDDR5X, 273 GB/s), llama.cpp, MXFP4, Ollama, vLLM, TensorRT-LLM, SGLang, CUDA, cuDNN, NCCL, Triton

## [This Tiny AI Never Stops Learning (mini-AGI)](../videos/L-6O7R71CCg.md)
`L-6O7R71CCg` · Better Stack · 2026-10-02 · q2 · intro · review · also: training-finetuning-rl, models-research

Better Stack walkthrough of "Mini-AGI," a toy mixture-of-experts model trained from zero on a MacBook to keep learning continuously; the author's retention and forgetting claims are single-run anecdotes.

- Techniques: Ordered streaming training with a small step per chunk; Expert-per-file paging for models larger than VRAM; Two-speed learning rates to limit forgetting; Held-out script as a memorization detector; Fixed probe prompt during training; Pause and resume across sessions
- Tools: Mini-AGI (toy continual-learning mixture-of-experts model; repo tested only on Nvidia GPUs; weights not yet released, per the speaker), TinyStories dataset (short children's stories), Screenplay corpus: Pulp Fiction, Jackie Brown, Inglourious Bastards, Django Unchained, Four Rooms, Kill Bill, Reservoir Dogs (held out), Apple M2 Max MacBook Pro, 32 GB RAM, Author's custom screenplay chat web app (not named)

## [What It Actually Costs to Run DeepSeek V4.1 Flash Locally?](../videos/04ePeOyRN0k.md)
`04ePeOyRN0k` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency, models-research

Kai works through what DeepSeek V4.1 Flash really costs to self-host: 510 GB of resident weights, 23 s/token on a 16 GB Mac, a $18.8k four-Spark cluster, and a roughly four-year break-even against cheap API pricing.

- Techniques: Size local MoE hardware by resident bytes, not active params; Break-even test for self-hosting versus API; Measure decode tok/s by output type, separately from time to first token; Compress the Engram table, not the experts, when the model is already FP4
- Tools: DeepSeek V4.1 Flash (open weights, MIT license), DeepSeek V4 Flash, DeepSeek V4 Pro (retired), DeepSWE V1.1 (benchmark, name as captioned), Claude Opus 5, GPT 5.6 Sol, NVIDIA DGX Spark (GB10 Grace Blackwell, 128 GB unified memory), vLLM (tensor parallel 4), Mac mini (16 GB RAM), Hugging Face, GGUF, RTX 3060

## [Large clusters for small models — Daniel Svonava, Superlinked](../videos/g4SsanB0gMc.md)
`g4SsanB0gMc` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · also: inference-serving, infra-cost-scaling, training-finetuning-rl

Daniel Svonava (Superlinked) on serving fleets of small open models on your own GPUs: why top-down routers fail for many small requests, and how a centralized pull-based queue, a thin Rust gateway and a runtime sidecar fix it.

- Techniques: Centralized pull-based batching queue; Thin gateway with annotation, not full parsing; Runtime sidecar behind a socket; Knee-based benchmarking; Pin plus lazy-load model placement; Per-task model selection with evals, then cheap adaptation; Autoresearch loop for serving tuning
- Tools: vLLM, SGLang, PyTorch, Candle, NATS JetStream, MessagePack, Rust, AWS Bedrock, LoRA, Hugging Face

## [Qwen 3.8 27B is 3X Faster With MTP](../videos/hHdJpiPxhco.md)
`hHdJpiPxhco` · Kai Explains · 2026-09-02 · q4 · practitioner · tutorial · also: inference-serving

Qwen 3.8 27B ships an MTP draft head inside its weights; enabling it can roughly double or triple local decode speed with the same output, but only on a current runtime build, with a tuned draft depth and temperature, and only if the model fits in VRAM.

- Techniques: Enable MTP in llama.cpp; Enable MTP in vLLM; Enable MTP in SGLang; Enable MTP in Ollama with a tag; Sweep draft depth and find your peak; Tune sampler temperature for draft acceptance; Benchmark by task type, not one number; Check the memory path before enabling
- Tools: Qwen 3.8 27B (dense, 27B parameters), MTP (multi-token prediction) draft head, llama.cpp (build after May 13, 2026), Ollama (MTP-tagged model tags), vLLM (speculative decoding config), SGLang (speculative algorithm parameter), NVFP4 (4-bit format, Blackwell only), EAGLE-3 (not mentioned in this video), NVIDIA RTX 3090, 4090, 5090, AMD Radeon (Vulkan and ROCm backends), Apple Silicon with Metal kernels

## [Running a 80B AI Model on a 8GB GPU, FAST (oLLM Guide)](../videos/5E3qTmQPmP8.md)
`5E3qTmQPmP8` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: inference-serving

Kai walks through oLLM, a Python library that streams Qwen3-Next 80B layers off SSD on an 8GB GPU, and argues it is only worth using for long-context offline passes, not interactive or agent work.

- Techniques: Layer-streaming offload from SSD; Disk-backed full-precision KV cache; Chunked projections plus flash attention to cap peak VRAM; Expert-selective streaming for MoE models; Predict throughput from storage bandwidth before running; Pick the runtime by job shape (speaker's decision rule)
- Tools: oLLM (OLM), Qwen3-Next 80B, llama.cpp, Hugging Face transformers, PyTorch, MLX, flash attention

## [Did This Open Source Model Just Fix AI Reasoning? (ThinkingCap)](../videos/byfjZvrYRH0.md)
`byfjZvrYRH0` · Better Stack · 2026-09-02 · q2 · intro · review · also: token-cost-efficiency, training-finetuning-rl

Better Stack tests ThinkingCap, a Qwen3.6-27B fine-tune trained to reason less: about 46% fewer thinking tokens with flat accuracy by vendor numbers, backed by one RTX 5090 demo.

- Techniques: Efficiency-aware reward during fine-tuning; Separate reasoning and answer token counts; Single-answer A/B probe on fixed hardware
- Tools: Qwen3.6-27B (27B parameters, quantized, base for ThinkingCap), ThinkingCap (fine-tune of Qwen3.6-27B), Step 3.5 Flash (reasoning model used as the overthinking example), GPT-3, GPT-3.5, GPT-4, OpenAI thinking model (Sept 2024, unnamed in transcript), DeepSeek R1, NVIDIA RTX 5090 (64 GB RAM test machine), GSM8K benchmark, Hugging Face (model distribution, Apache 2.0)

## [What Would it Cost to Run Claude Opus 5 Locally?](../videos/yJCHNdQ8sLs.md)
`yJCHNdQ8sLs` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency

Kai Explains works through what it would take to run an Opus-class model locally, using open-weight Kimi K3 as a stand-in; the bottleneck is memory bandwidth and the electricity bill, not the hardware price.

- Techniques: Size the local rig from the smallest usable quant plus KV cache, not from headline parameter count; Estimate decode speed from memory bandwidth, and compare hardware on bandwidth, not capacity; Diagnose a slow local run by checking VRAM occupancy and GPU utilization; Benchmark with a short generation and extrapolate to a target reply length; Compute breakeven against the specific API price you would replace, including utilization and price decline; Watch interconnect bandwidth when splitting a model across machines
- Tools: Claude Opus 5, Kimi K3 (Moonshot AI), Unsloth quantized builds, Kimi K3 REAP 512GB (pruned build), NVIDIA RTX Pro 6000 Blackwell, NVIDIA DGX B300, NVIDIA DGX Spark, NVIDIA RTX 5090, NVIDIA H100, NVIDIA B200, NVIDIA A100, RTX 3090

## [I Tested Every Qwen3.8-27B Quant: Here’s the Best One For Your GPU](../videos/hg26j0erUSo.md)
`hg26j0erUSo` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: inference-serving, evals

Kai's practitioner guide to choosing a quant of Qwen3.8-27B for consumer GPUs: architecture-aware quants, why a Q4 KV cache silently degrades outputs, and VRAM-based file picks.

- Techniques: Diff quantized output against the full-precision model before trusting a quant or cache setting; Keep the KV cache at Q8 or full precision; Choose the quant by VRAM budget; Pin the model revision on download; Lower reasoning effort for simple tasks; Enable the built-in MTP draft head for speculative decoding; Make sure the front end renders the chat template correctly; Load the vision projector as a separate file
- Tools: Qwen3.8-27B, Unsloth UD-Q4_K_XL / Q6 / Q8 quants, Bartowski IQ4_XS quant, Ridge quant (name as transcribed; may be a caption error), Atomic Chat KL-divergence benchmark, Quesma benchmark run, GPQA Diamond, IFBench, TerminalBench, Jinja chat-template flag, spec type draft MTP (speculative decoding flag as spoken), RTX 3090

## [What Would It Cost to Run GLM 5.3 Locally?](../videos/ZR3E9-fCFf8.md)
`ZR3E9-fCFf8` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: inference-serving, token-cost-efficiency

Kai works through the memory and dollar math for running GLM 5.3 locally: MoE active params don't reduce memory, quantization sets the footprint, and renting or the API beats buying hardware for most teams.

- Techniques: Resident-memory estimate for MoE models; GPU count from footprint with headroom; Rent-before-buy evaluation with cost break-even; Hybrid local-plus-API routing
- Tools: GLM 5.3 (Z.ai), GLM 5.2 (Z.ai), GLM 5.1 (Z.ai), GLM coding plan (Z.ai), Terminal Bench 3 (benchmark, cited by speaker), CyberGym (benchmark, cited by speaker), ExploitBench (benchmark, cited by speaker), Unsloth dynamic 2-bit quantization, GGUF (2-bit file format, mentioned), Hugging Face (weight hosting), Apple Mac Studio M4 Ultra (512 GB), Apple Silicon unified memory

## [This Tool Finds the Perfect AI Model for Your Hardware (llmfit)](../videos/zf8jpD77sKY.md)
`zf8jpD77sKY` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: inference-serving, dev-tools

Better Stack walks through llmfit, a terminal tool that detects your CPU, RAM and GPU, scores local models for fit and speed, and tests its estimates on machines from a 2012 Raspberry Pi to an RTX 5090.

- Techniques: Pre-download hardware fit check; Back-of-envelope decode speed check; Calibrate the tool against a real run; Use-case-weighted ranking
- Tools: llmfit (spoken as LLM Fit; no version stated), Hugging Face, DeepSeek R1, Qwen 3.6 12B (transcribed as Quen 3.6), Qwen 3.x models (transcribed as Quen 3.8 on the RTX 5090), Gemma 4 12B, Kimi K2.7 Flash variant (transcribed as Kimi K 2.7 D flash), Falcon H1 Mini, Llama 3 (mentioned, not tested), MLX, CUDA, Metal

## [You Don't Need Frontier Models Anymore (Qwen 3.8 27B + DeepSeek Harness)](../videos/3DVRznjCIS8.md)
`3DVRznjCIS8` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: agent-architecture, evals, context-engineering

Same local Qwen model, same weights and prompt: the outcome changed with the harness around it (feedback loop, tools, session log, context), so the software matters as much as the model.

- Techniques: Attribute failures to the harness before blaming the model; Close the feedback loop so the agent can verify its own output; Persistent session log as source of truth for long runs; Sweep reasoning effort on a fixed prompt rather than assuming max is best; Size the local model by capacity and bandwidth, then pick quantization; Hybrid local-then-frontier handoff
- Tools: Qwen 3.8 27B (transcript: 'Quen 3.8'), Qwen 3.6, Qwen 3.7 Plus, DeepSeek Harness (transcript: 'DeepSeq Harness'; MIT licensed, plugin components, developer preview), DeepSeek v4 (2-bit quant, transcript: 'DeepSeq v4'), Claude Code (Qwen's benchmark harness for four agentic evals), Opus API (cost comparison), VS Code Copilot (failed reproduction run), Unsloth Q6 build of Qwen 3.8, Simon Willison's test prompt (reasoning-effort test), DeepSWE 1.1 (benchmark), OSWorld (computer-use benchmark)

## [I Can't Believe This AI Model Fits in 14 Megabytes (Needle 2)](../videos/M24yg6ZM7-I.md)
`M24yg6ZM7-I` · Better Stack · 2026-09-02 · q3 · intro · review · also: models-research, inference-serving

Hands-on demo of Needle 2, a 45M-parameter, 14 MB tool-call dispatcher from Cactus Compute running offline on an ESP32-S3 microcontroller; it maps natural language to predefined device actions, not general chat.

- Techniques: Closed-action-set tool dispatch on a small model; Gate actions on the dispatcher's confidence score; Native low-bit training instead of post-training quantization; Reuse the demo engine by swapping commands
- Tools: Needle 2 (Cactus Compute, Apache 2.0), ESP32-S3, Raspberry Pi 5, LFM 2.5 (comparison model in Cactus benchmarks, as spoken), Custom inference engine and TUI (speaker's own, GitHub link in description)

## [I Tested Meta Muse Glimmer 30B For 48 Hours: Here’s What Happened](../videos/v-xnHMwLgAw.md)
`v-xnHMwLgAw` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: evals, models-research

Kai Explains puts Meta's unannounced Muse Glimmer 30B through 48 hours of agent work on dual RTX 3090s: fast at 50-60 tok/s, but it fails instruction following, context depth and synthesis.

- Techniques: Constant-harness model A/B test; Three-question model vetting probe; Compaction threshold relative to window size; Local llama.cpp serving recipe (as described, not as flags); Long-command detachment rule
- Tools: Meta Muse Glimmer 30B, Unsloth Q8_0 GGUF, llama.cpp, DFlash drafter (speculative decoding), DeepSeek V4 Flash, Qwen 3.6 27B, Qwen 3.5 35B MoE, tmux, ComfyUI

## [Can a Local LLM Actually Replace Claude or Codex for Coding?](../videos/uefMWJ1GBWg.md)
`uefMWJ1GBWg` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: coding-agents, token-cost-efficiency, infra-cost-scaling

Kai Explains on whether a local open-weight model can replace Claude Code or Codex for coding. Verdict: memory and tool-calling decide it, the hybrid and free-tier route wins on cost for most people, and local is a daily driver only for bounded work.

- Techniques: Test the harness on a trivial task before a big job; Size hardware as weights plus context; Prefer higher quantization on a smaller model for tool use; Rewire a cloud CLI to a local endpoint; Hybrid routing: frontier plans, local executes; Sandbox any local agent that can run shell commands; Break-even math for local versus cloud; Price agent API usage on cached input
- Tools: Claude Code, Codex, ChatGPT, Ollama, llama.cpp, MLX, LM Studio, Aider, OpenCode, Cline (transcribed as Klein), Qwen Code (transcribed as QuenCode; model not named), OpenRouter

## [Xiaomi AI Cube vs DGX Spark! The prototype that can change local AI](../videos/SeQ8qou_i-E.md)
`SeQ8qou_i-E` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: inference-serving, infra-cost-scaling

Xiaomi AI Cube vs DGX Spark: headline specs measure different things. Batch size, concurrency, serving config and the network decide real throughput; the Cube is still unshipped.

- Techniques: Normalize vendor throughput claims before comparing; Benchmark a box at several concurrency levels; Check the serving stack's defaults before judging hardware; Test network sensitivity before scaling out; Fit check and payback arithmetic for a purchase
- Tools: Xiaomi AI Cube (D100 chip, prototype, unannounced), NVIDIA DGX Spark, Xiaomi MIMO (3B model at the batch-one lab result), MIMO 2.5 (Xiaomi flagship, over 300B parameters), llama.cpp, vLLM, X-ring backend (name as spoken in the transcript, unverified), HBM4 (memory in data-center GPUs), NVIDIA H200 (comparison reference), Xiaomi phone processor (113 GB/s memory bandwidth, not the Cube chip)

## [I Made Qwen 3.8 and Claude Opus 5 Build the Same Game](../videos/m8HFQ8cZlTU.md)
`m8HFQ8cZlTU` · Better Stack · 2026-09-02 · q2 · intro · review · also: models-research, coding-agents, token-cost-efficiency

Better Stack runs the same one-prompt 3D endless-runner build on Qwen 3.8 (2.4T open-weight) and Claude Opus 5, then argues cost, speed, verbosity and weight access matter more than the 58-vs-63 benchmark gap.

- Techniques: Same-prompt, play-the-output model comparison; Score by behavior, not by code volume; Route by three axes: speed, verbosity, access; Hosted open-weight via an OpenAI-compatible endpoint
- Tools: Qwen 3.8 (2.4T total, ~95B active, open-weight), Qwen 3.8 Max (hosted production variant), Qwen 3.8 27B (mentioned as the locally-runnable size), Claude Opus 5 (Max), three.js (CDN, used by the game test), Artificial Analysis (benchmark index), OpenRouter, DeepInfra, Fireworks

## [10 Best Local Coding Models Right Now 2026](../videos/z605KVofJAY.md)
`z605KVofJAY` · Kai Explains · 2026-09-02 · q3 · intro · review · also: models-research, coding-agents, inference-serving

Kai Explains lists 10 open coding models split by hardware tier and task type, and argues that picking a model for your own hardware and job matters more than leaderboard rank.

- Techniques: Hardware-first model sizing; Route models by job, not one model for everything; Local tab completion with Continue.dev and a FIM model; Running Qwen3.6 27B on one 24 GB card; Pick for tool-call reliability; Filter by license before commercial use; Cheap hosted model for bulk processing
- Tools: GLM 5.3, Kimi K2.7, Kimi K3, DeepSeek V4 Pro, DeepSeek V4 Flash, Qwen3-Coder (480B), Qwen3-Coder-Next, Qwen 3.6 27B, Qwen 2.5 Coder 14B, Devstral Small 2, GPT-OSS-20B, Codestral 2

## [oMLX Best Way to Run Local AI on A MAC](../videos/j557WxWtdZk.md)
`j557WxWtdZk` · Kai Explains · 2026-09-02 · q3 · practitioner · tutorial · also: inference-serving, coding-agents, token-cost-efficiency

Kai Explains walks through OMLX, an open-source local inference server for Apple Silicon Macs that keeps a two-tier (RAM + SSD) KV cache so near-identical prefixes in long coding-agent sessions are reused instead of recomputed, mainly cutting time-to-first-token.

- Techniques: Diagnose slow agent turns as a prefix-cache miss; Install OMLX via the signed DMG; Point Claude Code at OMLX; Point Cursor at a local OpenAI-compatible server; One-command agent configuration with OMLX's CLI launcher; Browse and reuse Hugging Face and LM Studio model caches
- Tools: OMLX (Apache 2.0, about 18.6k GitHub stars, by one developer), Apple MLX / MLX server, Claude Code, Cursor, OpenCode, Codex, PyAgent, Pi, Hugging Face cache, LM Studio, safetensors, Qwen3 Coder Next (8-bit, benchmark model)

## [9 Open Source AI Tools That Will Kill Your Monthly Subscriptions](../videos/DOC9mbZOMW0.md)
`DOC9mbZOMW0` · Kai Explains · 2026-09-02 · q2 · intro · review · also: token-cost-efficiency, dev-tools

Nine self-hostable open-source tools (Karakeep, Steno, Audio.cpp, Harper, Open Notebook, LibreChat, Open WebUI) pitched as replacements for about $150/month of AI subscriptions. Listicle, light on technical detail.

- Techniques: Multi-provider chat front end on one self-hosted UI; Self-hosted bookmark archive with local LLM tagging; On-device meeting transcription with live speaker labels; Editor-native local grammar checking
- Tools: Karakeep (formerly Hoarder), Pocket, Readwise Reader, Ollama, Meilisearch (transcribed as 'Mail-A-Search'), Steno, whisper.cpp, Whisper, Parakeet, llama.cpp, GGML, GGUF

## [I Tried Both New 30B Models... One Of Them Is a DISASTER! (Muse Glimmer & Lightning 3.5)](../videos/mzQC9UK9n84.md)
`mzQC9UK9n84` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: evals, mcp-and-tools, models-research

Hands-on test of Meta's Muse Glimmer and NVIDIA's Nemotron Lightning 3.5 (both ~30B, local via Ollama) on three agentic tasks; Glimmer passes two of three, Lightning fails all three.

- Techniques: Same-prompt, multi-round correction test; Serve two local models and drive them from an agent CLI; Expose a desktop editor to models through a custom UXP plugin; Check numbers against the source document; Treat tool-error fallback as a test case
- Tools: Muse Glimmer (Meta), Muse Spark (Meta), Nemotron Lightning 3.5 (NVIDIA), NeMo Switchyard (NVIDIA routing), D-Flash speculative decoding, Ollama, OpenCode, Opus 5 (reference model), Adobe Premiere Pro, Adobe Bridge, UXP plugin (custom), Epidemic Sound MCP server

## [Everything That Actually Matters for Local AI](../videos/Y_34JZmZElg.md)
`Y_34JZmZElg` · Kai Explains · 2026-09-02 · q4 · practitioner · talk · also: inference-serving, token-cost-efficiency

A numbers-driven guide to local AI hardware: memory bandwidth sets decode speed, active (not total) parameters set speed for MoE models, the model file is not the whole memory bill, and KV cache at long context can outweigh the weights.

- Techniques: Back-of-envelope decode speed; Split the hardware decision by workload; Full memory budget (not just the file size); Asymmetric KV cache quantization; Avoid partial GPU offload for the last layers; Prefer 4-bit or higher with QAT checkpoints; avoid 3-bit and lower for reasoning work; Evaluate on your own task before choosing hardware or quantization; Local versus API break-even check; Cap local agent runs at tool-call budgets
- Tools: llama.cpp, Ollama, LM Studio, vLLM, Apple MLX, Qwen3 (32B dense, 30B MoE, 35B-A3B), Gemma (26B-A3.8B sparse, 27B), DeepSeek (cache compression, cheap API), Kimi K3 (2.8T parameters), NVIDIA RTX 5090, NVIDIA RTX 3090, NVIDIA H200

## [Best Hardware for Running Local LLMs in 2026: Mac vs NVIDIA vs Cloud](../videos/gQ7iJuciMg0.md)
`gQ7iJuciMg0` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency, infra-cost-scaling

Compares Mac Mini M5 Pro, DGX Spark, RTX 5090 and rented GPUs for local LLMs at current prices, arguing that prefill and decode need different hardware and that renting usually wins on cost.

- Techniques: Evaluate hardware separately for prefill (TTFT) and decode (tokens/sec); Split prefill and decode across machines; Budget memory headroom, not just model fit; Measure real memory bandwidth, not spec sheet bandwidth; Rent-vs-buy break-even calculation; Size for the model you run this week; Route by workload
- Tools: Mac Mini M5 / M5 Pro (Apple), Mac Mini M4 Pro (Apple, prior generation), Mac Studio, M3 Ultra (Apple), M5 Ultra (Apple), NVIDIA DGX Spark, NVIDIA RTX 5090, NVIDIA H100 (rental), Strix Halo (AMD, 128GB box), vLLM, DeepSeek V4 Flash (304B parameters), speculative decoding (on the 5090 owner's 27B setup)

## [New Local AI Inference Engine You Should Be Using in 2027 ? (FreeToken)](../videos/ZvZM4qnUVGI.md)
`ZvZM4qnUVGI` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: inference-serving

FreeToken, a five-week-old local inference engine, runs a 433 GB mixture-of-experts model on one 96 GB GPU by caching recently used experts and splitting misses between PCIe transfer and CPU compute; system RAM is the real limit.

- Techniques: Global LRU expert cache across all layers, no predictor; Split misses between PCIe fetch and CPU compute, overlapped; Calibrate the offload split once per machine; Replay recorded routing traces to compare cache policies fairly; Judge offload engines by worst-case turn latency, not mean tokens per second; Install and build requirements for FreeToken as stated
- Tools: FreeToken, llama.cpp, Ollama, LM Studio, KTransformers, DeepSeek V4 Flash, vLLM, Apache Spark, Mixtral offloading, MoE-Infinity, Pro-MoE, Expert Flow

## [The Study NVIDIA Doesn't Want You to See](../videos/5TFzJ38ae1s.md)
`5TFzJ38ae1s` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: inference-serving, infra-cost-scaling, token-cost-efficiency

Kai Explains reads the "Dumpster Cluster" paper (128 used V100s serving Llama models) past its viral 35x tokens-per-dollar claim. Capex-only, 8B-only numbers flip at 70B once electricity, failures and software support are counted.

- Techniques: Lifetime cost-per-token accounting; Operational failure budgeting for used GPU fleets; Track software support as a separate lifecycle
- Tools: Dumpster Cluster paper (128x V100 SXM2 cluster study), NVIDIA V100, NVIDIA A100, NVIDIA H100, NVIDIA B200, vLLM (0.17 for B200 runs, 0.6 for H100/A100 runs, per the video), PyTorch 2.11 (dropped Volta from CUDA 12.8/12.9 pre-built binaries), CUDA (compute capability 7.0 = Volta), CoreWeave Vera Rubin (vendor tokens-per-MW claim)

## [This 2B Model Cloned My Voice Locally (VoxCPM)](../videos/O4TMwZlUJvQ.md)
`O4TMwZlUJvQ` · Better Stack · 2026-09-02 · q3 · practitioner · tutorial · also: voice-multimodal, inference-serving

Tutorial on running OpenBMB's 2B VoxCPM2 TTS locally for speech generation, voice design from text, and voice cloning, with a clear list of where it falls short versus hosted APIs.

- Techniques: Prototype the voice in a hosted demo before any infra work; Local install and minimal generation script; Turn the model into a service behind the OpenAI speech API; Voice design from a persona description; Voice cloning from a short reference, with transcript; Set the output language explicitly for multilingual speech
- Tools: VoxCPM / VoxCPM2 (OpenBMB, Apache 2.0, ~2B params), PyTorch, torchaudio, Python, vLLM, Hugging Face (demo and checkpoint), macOS afplay, ComfyUI, GGUF, MLX (community paths mentioned), Chatterbox (TTS comparison), Qwen3-TTS (TTS comparison), ElevenLabs (hosted TTS comparison)

## [This Makes Claude Code Free Forever](../videos/vxrZWbZ2fZA.md)
`vxrZWbZ2fZA` · Better Stack · 2026-09-02 · q3 · intro · review · also: claude-code, token-cost-efficiency, coding-agents

Free Claude Code, an open-source local proxy that keeps Claude Code's interface but sends its requests to a free, cheaper, or local model. Useful for routing easy tasks off premium models; the speaker says it is not a replacement for Claude.

- Techniques: Proxy-based model swap behind an unchanged coding client; Tiered per-task model routing; Bounded refactor as a smoke test for a new model route; Reliability-first fallback to premium model
- Tools: Free Claude Code (FCC), Claude Code, Codex, Pi, NVIDIA NIM, OpenRouter, Opus 5 (model name shown in Claude Code UI)

## [The Open Model That Popped the AI Bubble](../videos/0y9B_sDLxjQ.md)
`0y9B_sDLxjQ` · Kai Explains · 2026-09-02 · q3 · practitioner · news · also: models-research, software-factory, token-cost-efficiency

News-and-analysis video on Alibaba's open-weight Qwen 3.8 Max: vendor benchmarks, self-run agent demos, weak coding scores, preview pricing, and China-hosted data-handling risk.

- Techniques: Unattended issue-driven build loop; Paper-to-code reproduction with ideation rounds; Base-URL swap to drive existing coding harnesses; Choose a deployment tier by hardware; Checklist before trusting a new open-model claim; Data-sensitivity triage for hosted models
- Tools: Qwen 3.8 Max, Qwen 3.8 27B checkpoint (transcribed as '3.827B'), Qwen 3.7+ and 3.7 Max (comparison models), Claude Opus 4.8, Claude Fable 5, GPT 5.6 Sol, Kimi K3, OhMyCly (repo name as transcribed), Tianchi competition platform, Recreation Bench, Ecommerce Bench, Terminal Bench 2.1

## [Qwen 3.8 27B + DFlash2: 140 Token/Sec?](../videos/H2oWD4WT7Os.md)
`H2oWD4WT7Os` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: inference-serving, models-research

A critical look at the DFlash2 speculative-decoding claims for Qwen 3.8 27B: the 3x headline uses a no-speculation baseline, against the built-in MTP it is about 23%, and it pays off mainly for single-user retrieval and edit-application workloads.

- Techniques: Check MTP is enabled before benchmarking any draft method; Benchmark speculative decoding across a concurrency sweep; Target speculative decoding at context-reproduction workloads; Choose a coherent candidate path instead of independent per-position argmax; Add depthwise convolutions around sublayers in a shallow drafter; Check the concurrency and block-size settings on Apple Silicon
- Tools: Qwen 3.8 27B, DFlash2 (DFLASH2 / D-Flash 2), DFlash1, dSpark, MTP (multi-token prediction), EAGLE-3 (only in the sense of prior art, not stated in video), vLLM, llama.cpp (PR 27342), Ollama (issue 17865), SGLang, MTBench, GGUF quants (mentioned as local model quants)

## [Someone Built Ollama for Audio… and It Runs Locally](../videos/CvZuuKkT3Sw.md)
`CvZuuKkT3Sw` · Better Stack · 2026-09-02 · q3 · intro · review · also: voice-multimodal, inference-serving

Walkthrough of Audio CPP, a month-old GGML single-binary runtime for about 30 local audio model families (TTS, STT, voice cloning, music); early and crash-prone, with speed claims measured only on NVIDIA.

- Techniques: Single-binary local audio runtime; OpenAI-compatible local audio server; Voice cloning from a short reference clip; Validate speed on your own hardware
- Tools: Audio CPP, GGML, llama.cpp, whisper.cpp, Ollama, Kokoro, Piper, FFmpeg, PyTorch, MLX, CUDA, Vulkan

## [How They Fixed AI's Biggest Local Hardware Problem (with FreeToken)](../videos/8n4Uo47CadY.md)
`8n4Uo47CadY` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: inference-serving

Walkthrough of FreeToken, an open-source MoE inference engine that caches hot experts on the GPU, streams misses over PCIe, and splits misses between GPU and CPU; the speaker's 2.3x speedup over Ollama held only when the model overflowed VRAM.

- Techniques: Expert-cache over RAM-resident weights; Double-buffered expert streaming during prefill; Bandwidth-measured split of cache misses between GPU transfer and CPU compute; Load weights directly into runtime memory layout; Find the cache knee by shrinking the cache live; Test setup in OpenCode (as the speaker did)
- Tools: FreeToken (open-source MoE inference engine, CLI and desktop app; Windows/Linux desktop only), Ollama, llama.cpp, OpenCode, DeepSeek V4 Flash (284B total / 13B active, as stated), Qwen 3.6 35B (8-bit and 4-bit builds tested), NVIDIA RTX 5090 (32 GB VRAM), PCIe, DDR5 system RAM (64 GB)

## [Best Local AI Models For Every VRAM Tier](../videos/mn7CD0JjVpw.md)
`mn7CD0JjVpw` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: inference-serving, token-cost-efficiency

Tier-by-tier guide to local LLMs by GPU VRAM (4GB to 24GB+). Pick the biggest quantized model that fits with context headroom, and set the context length explicitly to avoid KV-cache crashes.

- Techniques: Pick the biggest model that fits with context headroom; Prefer a smaller model at higher precision; Set the context length explicitly at model load; Split chat and autocomplete models; Use an MoE model on large-memory machines
- Tools: Ollama, LM Studio, llama.cpp (spoken as 'llama'; context-length crash anecdote), Phi-4-mini, Gemma 4 E2B (Gemma 4 family, ~April 2026 per the host), Qwen 2.5 7B, Qwen 3.5 9B, Qwen 3.6 27B, Qwen3-Coder-Next (80B MoE, ~3B active), Mistral 7B, Mistral Small, Llama 8B (captions read 'Llama 3.38b')

## [OpenSource AI Tools That Feel ILLEGAL To Get Free](../videos/VghawjhiGkw.md)
`VghawjhiGkw` · Kai Explains · 2026-09-02 · q3 · intro · review · also: coding-agents, token-cost-efficiency, agent-architecture

Kai Explains reviews five open-source AI tools (Goose, Jan, Money Printer Turbo, a DeepSeek harness) as subscription replacements, stressing that the software is free but inference, API keys and hardware still cost money.

- Techniques: Point an OpenAI-SDK client at a local endpoint; Run the DeepSeek harness as a local web app; Semantic-mismatch test for generated video; Read a README past the marketing lines
- Tools: Goose, Jan, Hugging Face, Llama, Gemma, Qwen (transcribed as 'Quen'), Money Printer Turbo, FFmpeg, Pexels, Pixabay, Coverr (transcribed as 'Caver'), Edge TTS

## [Best Hardware for Running Local LLMs in 2026: Mac vs NVIDIA vs Cloud](../videos/sR8sJ2mybQU.md)
`sR8sJ2mybQU` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: inference-serving, token-cost-efficiency, infra-cost-scaling

Kai Explains on picking local-LLM hardware in 2026 (Mac Studio vs RTX vs rented cloud GPUs), with measured vLLM vs llama.cpp and multi-GPU scaling results and a budget-based buying guide.

- Techniques: Pick the serving framework by VRAM headroom; Estimate decode speed from memory bandwidth, then confirm with your own benchmark; Pair MoE models with bandwidth-limited hardware; Cap consumer multi-GPU at two cards, or run one server per GPU; Breakeven check before renting or buying; Split work between local and frontier models
- Tools: Qwen3 Coder Next (80B MoE, Q4 about 46 GB, 70.6 SWE-bench as stated), Qwen 3.6 27B dense (16 GB, 77.2 SWE-bench as stated; transcript spells it 'Quen 3.627B'), Claude Sonnet 4.6, Claude Opus, GPT-4 (mentioned only as an example of a frontier API), vLLM, llama.cpp, Apple MLX, CUDA graphs, NVLink, PCIe, Mac Studio M4 Max 128 GB

## [If You Understand These 5 AI Terms, You’re Ahead of 90% of People](../videos/04rRN1oqO2A.md)
`04rRN1oqO2A` · Kai Explains · 2026-09-02 · q2 · intro · review · also: context-engineering, rag-retrieval

Kai Explains walks through five foundational AI terms (tokens, context window, temperature, hallucination, RAG) for non-engineers, using plain analogies and personal anecdotes.

- Techniques: Verify-before-trust workflow for AI output; Restate critical context in long sessions; Adjust temperature for the task; Mental model of RAG for debugging products
- Tools: Claude, ChatGPT, Gemini

## [China Is Coming for Your Local AI Box (XIAOMI AI Cube)](../videos/tjFNIQBFKMs.md)
`tjFNIQBFKMs` · Kai Explains · 2026-09-02 · q4 · practitioner · news · also: inference-serving, models-research

Kai Explains on why local AI boxes are judged by memory bandwidth, not headline TFLOPS or tok/s, and how to read this week's Xiaomi, Alibaba and Apple announcements. Verdict: buy only for a specific model you need now.

- Techniques: Bandwidth-first sizing for local decode; Split prefill and decode benchmarks; Buying checklist for local AI hardware; Read claims by their conditions; Split generation and prefill across heterogeneous nodes
- Tools: DGX Spark (NVIDIA), RTX 5090, AMD Strix Halo, Mac Mini, Apple Mac Studio, Xiaomi AI Cube, Xiaomi O100 accelerator, Xiaomi D100 chip, CUDA, DeepSeek coding harness, Qwen, Kimi

## [Qwen 3.6 vs Nemotron 3.5 vs Muse Glimmer: The Real Test](../videos/GweZqgLxcCo.md)
`GweZqgLxcCo` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: evals, inference-serving

Practitioner head-to-head of Qwen 3.6, Nemotron 3.5 Lightning and Meta's Muse Glimmer on the host's own daily-digest workload: trick questions saturate, premise and pushback tests separate models, Nemotron wins long context, Qwen stays daily driver.

- Techniques: Premise-override trap; Sustained-pushback (spine) test; Needle-in-log long-context test; Benchmark hygiene checks; Agentic task with traps and side-effect checks; Measure total wall time, not per-step latency, for tool loops; Route models by workload
- Tools: Qwen 3.6 (27B), Nemotron 3.5 Lightning (NVIDIA; hybrid Mamba MoE, 32.9B parameters, 1M-token context), Muse Glimmer (Meta; 27.9B parameters, about 18 GB on disk), Q4 quantization, GPU inference (runtime not named), Host's custom benchmark harness (synthetic log, executable tool tasks, trick-question set)

## [I Replaced Every AI Subscription I Pay For](../videos/MgHQncHjDhs.md)
`MgHQncHjDhs` · Kai Explains · 2026-09-02 · q2 · intro · review · also: token-cost-efficiency

Kai Explains argues that a $120/month stack of AI subscriptions can be replaced with self-hosted open-source tools (Ollama, Open WebUI, Perplexica, ComfyUI) running on an old laptop or Raspberry Pi. Mostly motivation; the technical detail is thin.

- Techniques: Ollama engine with Open WebUI front end on a home machine; Small-model fallback for weak hardware; Self-hosted AI search with cited sources; Local image generation with ComfyUI; Local model as backend for editor and browser writing tools
- Tools: Ollama, Open WebUI, Perplexica, SearXNG, ComfyUI, Stable Diffusion, FLUX, Mistral, Qwen, Llama 3.1 8B, Mistral 7B, Raspberry Pi

## [This 600M Model Fixes What Whisper Leaves Behind](../videos/jp0PGmAwK3w.md)
`jp0PGmAwK3w` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: data-engineering, coding-agents

Super Whisper's open 600M-parameter S1 Mini cleans raw speech-to-text output (fillers, self-corrections, spoken numbers, emails) locally via GGUF and Ollama. English only, early software.

- Techniques: Post-ASR cleanup layer; Local GGUF serving with Ollama; Keep the cleanup model narrow and use a general LLM for everything else; Fully local dictation pipeline
- Tools: S1 Mini (Super Whisper, open 600M model), S1 Voice (Super Whisper, cloud ASR, not covered), S1 Language (Super Whisper, cloud, not covered), Whisper, Whisper.cpp, Parakeet, MLX Whisper, Ollama, llama.cpp, LM Studio, Hugging Face, GGUF

## [Why Large? Tiny LMs & Agents on Edge/Robotics — Cormac Brick, Google](../videos/hacEQHHhu2Q.md)
`hacEQHHhu2Q` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: inference-serving, training-finetuning-rl

Google's Cormac Brick on running tiny (50M to 500M) and small (1 to 4B) models on phones, browsers and robots, and why fine-tuning on synthetic data beats bigger models for narrow tasks.

- Techniques: Synthetic-data fine-tuning of a tiny model for one task; Voice-to-function-calling pipeline; Two-stage on-device dictation pipeline; Memory budgeting for on-device LLMs; Multi-token prediction (MTP) for decode speed; Frame budgeting for NPU vision; Side-task tiny model
- Tools: LiteRT-LM, LiteRT / MediaPipe, Gemma 3, Gemma E2B, FunctionGemma, Gemma 4, AI Edge Gallery app, Apple FastVLM, Hugging Face (Mobile Actions dataset), Raspberry Pi, Jetson Nano, Qualcomm IoT boards (NPU)

## [Stop Renting Your Cognitive Infrastructure - Thiyagarajan Maruthavanan, Kalmantic Labs](../videos/Bck7ABCZRZI.md)
`Bck7ABCZRZI` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: token-cost-efficiency, infra-cost-scaling, governance-compliance

Thiyagarajan Maruthavanan (Kalmantic Labs) argues teams should rent inference to learn and own it to earn, using his own runaway-cost incident and enterprise objections to self-hosting as evidence.

- Techniques: Per-key spend monitoring with a cutoff; Input compression and context management in agent loops; Rent-to-own decision gate; Small local inference box for personal agents
- Tools: DGX Spark, Headroom, JustTokenMax, JustInfo, Suno, NemoClaw

## [Compression at the Edge — NVIDIA, Unsloth, HuggingFace, Ollama](../videos/J4_jCrTxMkk.md)
`J4_jCrTxMkk` · AI Engineer · 2026-08-18 · q4 · practitioner · panel · also: inference-serving, evals

Panel from NVIDIA, Unsloth, Hugging Face and Ollama on how quantization and compression make large open models run on local hardware, how to pick per-layer precision, and how to evaluate the result.

- Techniques: Sensitivity-aware dynamic quantization; Post-training quantization first, QAD for small models; KL-divergence evaluation against the unquantized model; Harness-level vibe testing before shipping a quant; Per-model default quant with precision kept high for tiny models; Big planner, small executor routing
- Tools: llama.cpp, Ollama, Unsloth, NVIDIA Model Optimizer (ModelOpt), TRL, bitsandbytes, QLoRA, GRPO, NVFP4, MXFP4, OpenClaw, Hermes agent

## [The Desktop Frontier — Ahmad Osman, Osmantic](../videos/XV2oYi7kojc.md)
`XV2oYi7kojc` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: models-research, inference-serving

Ahmad Osman argues that open-weight models are shrinking in hardware footprint fast enough that a GLM 5.2-class model should run on one RTX 5090 by late 2027, and urges people to own their hardware.

- Techniques: Footprint-over-time tracking; Dense small model for parallel local agents
- Tools: Claude Code, Telegram

## [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../videos/R3-anFK1YM8.md)
`R3-anFK1YM8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, context-engineering, evals

Sakana AI researcher on memory harnesses for long-horizon research agents running on local models; a ranked decision-ledger recall policy beat both no memory and plain vector RAG, at lower cost.

- Techniques: Write-manage-read memory loop; Ranked decision-ledger recall; Recall-mode ladder with an oracle; Ablate with wrong and recent memory; Local, controlled eval pipeline
- Tools: DeepSeek V4 Flash, Qwen (4-bit quantised), XBench, vector RAG, Spyder V2 benchmark

## [Local Models: Trust, Control, Optimization — Carter Abdallah, NVIDIA](../videos/FWMJQDH3iK0.md)
`FWMJQDH3iK0` · AI Engineer · 2026-08-18 · q3 · practitioner · panel · also: training-finetuning-rl, models-research, governance-compliance

A panel from NVIDIA, Prime Intellect and Arcee argues open-weight models give trust, cost control and data ownership, and that post-training them on your own harness and traces beats generalist frontier APIs for narrow work.

- Techniques: Harness-specific post-training of an open base model; RL environment, then deploy, then train on production traces; Trace capture as a fine-tuning dataset; Specialize a small model to one or two tasks; Verify open weights and inference code before trusting them
- Tools: vLLM, SGLang, PrimeRL, NeMo RL, NeMo Gym (captioned as 'Nemo Jim'), verifiers, Hugging Face, Nemotron, Trinity (Arcee model), Hermes (harness), Pi (harness), OpenMDW license

## [Local Agentic Theory For Mobile Games — Shafik Quoraishee & Joanne Song, The New York Times](../videos/418t26CVz-w.md)
`418t26CVz-w` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: agent-architecture, product-ux, inference-serving

NYT engineers on running small agents on-device inside mobile games, under per-frame time, memory and battery budgets, with live accessibility tuning through graded dials instead of fixed menus.

- Techniques: Per-frame perceive-predict-decide-act agent loop; Constraint graph over space, time and energy; Constraint satisfaction with backtracking; Graded accessibility dials driven by live signals; Live focus-path monitoring and layout auditing
- Tools: Efficient Zero V2 (sample-efficient RL, mentioned as state of the art up to 2024), WCAG 2.2 and WCAG 3.0 draft, Gaze estimation CNN, Google SIMA (transcript reads 'SEMA'; generalist agent framework mentioned briefly)

## [Laguna S 2.1: The Best Local Model? Beats GLM 5.2](../videos/YRlM9V_3mR8.md)
`YRlM9V_3mR8` · Kai Explains · 2026-08-02 · q4 · practitioner · review · also: models-research, inference-serving, token-cost-efficiency

Kai reviews Poolside's Laguna S 2.1, an open-weight 118B MoE model with 8B active that runs on one desktop-class box; it beats GLM 5.2 on some coding benchmarks but not all, and the launch numbers are unverified.

- Techniques: Run a MoE model that exceeds VRAM by offloading expert layers to system RAM (llama.cpp); Single-box 4-bit serving on unified memory; Enable max thinking only for hard agentic tasks; Test an open model on your own repo before adopting it
- Tools: Laguna S 2.1 (Poolside, open weights, OpenMDW license), Laguna XS (tinier sibling; captioned 'XS5'), GLM 5.2 (Chinese open model, about 740B), DeepSeek (largest model cited, about 1.6T), Qwen and Kimi (named as Chinese open-model families), Claude (Anthropic, closed frontier comparison), NVIDIA DGX Spark (128 GB unified memory desktop), llama.cpp (GGUF, IQ4_XS quant, expert-layer offload), Ollama (captioned 'Alama'), vLLM, SGLang, OpenRouter (hosted)

## [This Tiny Engine Runs Impossibly Big AI Models Locally! (colibrì)](../videos/3OqZHYNKc9A.md)
`3OqZHYNKc9A` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: inference-serving

Better Stack tests colibrì, a pure-C engine that streams a 744B MoE model (GLM 5.2) from SSD, on a MacBook and a RTX 5090 workstation. Result: it works, but speed is bounded by RAM, not the GPU.

- Techniques: Expert streaming with a RAM-resident dense core; Routing-frequency pinning; Compute-versus-wait profiling per turn; Token-exact validation of a streamed or quantized path; Speculative decoding via the native MTP head
- Tools: colibrì (transcribed as Calibri), pure-C local inference engine by Vincenzo Fornaro, zero external dependencies, GLM 5.2 (744B-parameter MoE language model, about 357 GB on disk, about 40B active per token), MLA (multi-head latent attention) compressed KV cache, Multi-token prediction head (speculative decoding), Apple MacBook M2 Max, 32 GB RAM, NVIDIA RTX 5090, 64 GB RAM workstation, Samsung portable SSD over USB (about 1 GB/s)

## [Qwen 3.6 + DFlash Is INSANE (Beats Claude + 6x Faster + OpenSource)](../videos/JmPS3eLTejY.md)
`JmPS3eLTejY` · Kai Explains · 2026-08-02 · q2 · intro · news · also: inference-serving, models-research, token-cost-efficiency

Kai Explains on Alibaba's open-weight Qwen 3.6 coding model and Z Lab's DFlash speculative-decoding drafter; claims near-Opus benchmark scores and up to 6x speedup, with few independent checks.

- Techniques: Parallel block drafter for speculative decoding (DFlash-style); Confidence-gated verification; Load-adaptive draft length; Validate the drafter before trusting a speedup; Swap the model behind an agent harness via base URL
- Tools: Qwen 3.6 (Alibaba Qwen Lab), DFlash (Z Lab; transcribed 'D-Flash'), Claude Opus 4.8, GPT 5.5, Claude Code, vLLM, Hugging Face, NVIDIA recipe (transcribed 'NAMO', name uncertain), DeepSeek (baseline reference), Apache 2.0 license, Frontier SWE (benchmark), SWE-Bench Pro (benchmark; transcribed 'WeBench Pro')

## [Model Distillation: How to Steal a Billion-Dollar AI](../videos/gacMZf5rqYA.md)
`gacMZf5rqYA` · Kai Explains · 2026-08-02 · q3 · practitioner · other · also: training-finetuning-rl, models-research, security-guardrails

Explainer on model distillation: how small students copy frontier models via API outputs, the DeepSeek R1 and budget-reasoning examples, the capability gaps that remain, and reported extraction campaigns.

- Techniques: White-box soft-label distillation; Black-box distillation via API sampling; Reasoning-trace fine-tuning of an open base; Small curated dataset recipe (S1-style); Append 'Wait' to extend reasoning at inference; Paraphrase robustness check for memorization; Size the local student to the GPU
- Tools: DeepSeek-R1, Qwen (32B, 14B, 7B distilled variants), OpenAI o1-mini, OpenAI o1-preview, OpenAI ChatGPT, Google Gemini, Sky-T1 (Berkeley), S1 (Stanford / University of Washington), Alma (local model runner, as named), OpenRouter, Hugging Face model cards, AIME 2024 benchmark

## [LLM Wiki + OKF Every Local AI Now Shares ONE Memory](../videos/9ciGYHHOLyU.md)
`9ciGYHHOLyU` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: memory, mcp-and-tools, context-engineering

A solo builder turns Karpathy's LLM-wiki idea and Google's OKF spec into a deterministic, local MCP memory layer, then documents the failures that showed up with a local model.

- Techniques: Librarian agent over a deterministic markdown store; Seed memory in MCP instructions and tool descriptions; Enrich-before-create and bidirectional linking rules for memory writes; Deterministic graph lint for orphans and broken links; Contradiction handling by rewrite, not append; Give the memory a model that makes write decisions well
- Tools: Karpathy LLM wiki (concept), Google OKF spec, MCP, llama.cpp server, llamaswap2, Qwen3 30B-A3B, Gemma 12B, Claude Opus (cited as the level of model needed for spec-following), Author's own memory tool, with web UI and graph visualizer (open source, link in description, not named)

## [Gemini 3.6 Flash, 3.5 Flash-Lite, & 3.5 Flash Cyber, Fugu Cyber, Qwen Audio, Audex & More AI News](../videos/pJcCPsa5IbY.md)
`pJcCPsa5IbY` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, voice-multimodal, security-guardrails

Weekly AI news (Aug 2026): Gemini 3.6 Flash and 3.5 Flash-Lite, Poolside's open 118B Laguna S2.1 with published trajectories, Microsoft's 4B MageFlow, plus audio, cyber and humanoid launches. Mostly vendor claims; Poolside's transparency stands out.

- Techniques: Wrap a frozen policy in a planner with memory (Harness VLA); Publish every trial's trajectory for benchmark claims (Poolside); Thinking on/off ablation on the same benchmark; Agent optimizes its own harness in an automated research loop; Fit check before running an image model locally
- Tools: Gemini 3.6 Flash, Gemini 3.5 Flash-Lite, Gemini 3.5 Flash Cyber, Gemini 3.5 Pro (partner testing), Gemini 4 (pre-training), Google AI Studio, Gemini API, Gemini app, Laguna S2.1 (Poolside, 118B total / 8B active MoE), Hugging Face, OpenMDW 1.1 license, GGUF

## [Grok 4.5 beats Claude and GPT, Seedream 5.0, Reve 2.1,Muse image and Video by Meta | AI News](../videos/FUCNOKb33qs.md)
`FUCNOKb33qs` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, token-cost-efficiency, voice-multimodal

Weekly AI news roundup (Aug 2026) covering Meta Muse Image, Grok 4.5, LingBot VLA 2.0, NVIDIA AudX 2B, MOSS Transcribe Diarize, WanStreamer 0.2, Seedream 5.0 Pro, Reve 2.1 and Alaya World, mostly with vendor-reported numbers.

- Techniques: Dual-memory consistency for interactive world models; Thinker/performer pipeline split for latency-neutral resolution upgrades; Layout-first image generation for targeted edits; Single-pass joint ASR and diarization; Unified multi-task audio model that preserves text ability; Test-time compute scaling with tool calls and self-refinement
- Tools: Muse Image, Muse Video, Meta AI, Instagram, WhatsApp, Grok 4.5, Grok Build, Cursor, XAI API, Opus 4.8, Fable Max (as transcribed), GPT 5.5 (as transcribed 'Xi')

## [Best Local Coding Model Right Now in 2026 (My Top 3 Picks)](../videos/ozyazf9xKP4.md)
`ozyazf9xKP4` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: token-cost-efficiency, models-research

Kai ranks three open-weight coding models a 24GB-VRAM owner can actually run, argues for VRAM math and tokens/sec over leaderboard scores, and recommends routing cheap local work and hard tasks to cloud models.

- Techniques: VRAM budget check before choosing a local model; Judge MoE models by active parameters for speed; Split routing between local and cloud models; Select local models by tokens per second, not leaderboard score; Layer offload to system RAM when a model barely overflows VRAM
- Tools: Qwen3 Coder Next (Alibaba, 80B MoE, about 3B active), Qwen 3.6 27B dense (transcribed as 'Quen 3.627B'; released April 22 per speaker), Qwen2.5 Coder 7B (transcribed as 'coder 7B'), DeepSeek V3.2 (transcribed as 'DeepSeq v3.2'), GLM 5 and GLM 5.2 (Zhipu, transcribed as 'GLM, from Jippu'), Kimi K2.7 (transcribed as 'Kimi-K 2.7'), Devstral Small 24B (Mistral, transcribed as 'Devstrol Small 24B'), gpt-oss-20B (transcribed as 'GPTOS 20B'), SWE-bench Verified, SWE-bench Pro, LiveCodeBench, Claude, GPT-5, Gemini (named as frontier cloud examples)

## [Best Local AI Models For Your Every GPU 2026](../videos/mtk8p8czzDU.md)
`mtk8p8czzDU` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: inference-serving, models-research

Kai Explains picks one local model per GPU memory tier (4-8, 8-24, 24-96, 96-192, 192-384 GB): NanBeige 4.2, Bonsai, Qwen 3.6 27B with Thinking Cap, Laguna S2.1 and Motif 3.

- Techniques: Tier-based model selection by VRAM or unified memory; Looped transformer for small models; Ternary retraining instead of post-training quantization; Fine-tune for shorter reasoning traces (Thinking Cap); Serving sparse MoE models locally; Local quickstart with Ollama or LM Studio
- Tools: Ollama, LM Studio, MLX, CUDA, vLLM, SGLang, llama (speaker says 'point a llama at it'; runtime not named precisely), OpenClaw, Hugging Face, Artificial Analysis, Terminal Bench, SWE-bench Verified (captioned as 'CWBench verified')

## [How This Tiny $8 Chip Runs an LLM With Almost No RAM](../videos/0qXVMt3pIjU.md)
`0qXVMt3pIjU` · Better Stack · 2026-08-02 · q3 · practitioner · tutorial · also: inference-serving, models-research

Better Stack walks through running a 28.9M-parameter TinyStories language model on an ~$8 ESP32-S3 microcontroller by keeping the big embedding table in flash and only streaming the rows each token needs.

- Techniques: Keep the embedding table in flash, stream rows on demand; Plain-C inference in llama2.c style on bare metal; Train a tiny model on a narrow dataset; Single-script build pipeline for embedded ML; Pick the board by flash size first
- Tools: ESP32-S3 (N16R8 variant: 16 MB flash, 8 MB PSRAM), Gemma (source of the per-layer embedding idea), TinyStories dataset (Microsoft research), llama2.c (Karpathy), Plain C toolchain for ESP32, MacBook (used for training, about 13 minutes)

## [Run Claude Code with Ollama for 99% Cheaper AI](../videos/LPDWUWP9SCk.md)
`LPDWUWP9SCk` · Better Stack · 2026-08-02 · q2 · intro · tutorial · also: claude-code, token-cost-efficiency

Better Stack setup walkthrough for pointing Claude Code and OpenCode at a local Ollama server to run open models such as Gemma 4 and Qwen 3.6. Setup only: the "99% cheaper" claim is never measured.

- Techniques: Redirect Claude Code to a local Ollama server; Launch a harness through the Ollama CLI; Pull and run a model from the CLI; Match the model to VRAM when choosing context length; Run Ollama in Docker and call its API
- Tools: Ollama, Claude Code, OpenCode, Codex, OpenClaw, Gemma 4, Qwen 3.6, MiniMax, DeepSeek, GLM, vLLM, LM Studio

## [DFlash Just Made AI 6x Faster : DFlash, DeepSpec Explained](../videos/x9MuyVOtX78.md)
`x9MuyVOtX78` · Kai Explains · 2026-08-02 · q4 · practitioner · review · also: inference-serving

Walkthrough of DFlash, a diffusion-drafter speculative decoding method merged into llama.cpp for Qwen 3.6, with local deployment steps and a self-run benchmark that checks whether the "lossless" claim holds.

- Techniques: Lossless-check benchmark protocol for speculative decoding; Deploy DFlash locally with llama.cpp server in Docker; Side-by-side leaderboard of baseline, MTP and DFlash; Tune drafter quantization and draft-token count; Decide by whether the GPU is idle at your concurrency
- Tools: DFlash, llama.cpp (llama CPP), Docker, EAGLE-3, MTP (multi-token prediction), Qwen 3.6 family (Qwen 3.8B build as transcribed), AIPerf, MATH-500, RTX 6000 Pro, vLLM, SGLang, DeepSpec (named in the video title; not explained in the transcript)

## [Granola, But Open Source and Local (Meetily)](../videos/LCoF8dCVkIw.md)
`LCoF8dCVkIw` · Better Stack · 2026-08-02 · q3 · intro · review · also: dev-tools

Short walkthrough of Meetily, an open-source, local-first meeting transcriber that captures system audio without joining calls. Speech-to-text runs on-device; summaries can use a local model or a cloud API key.

- Techniques: Bot-free system-audio capture; Split local-audio / optional-cloud-summary pipeline; Setup on a Mac (Apple Silicon); Offline-verification test
- Tools: Meetily, Granola, Otter, Fireflies, OpenAI Whisper, NVIDIA Parakeet, Ollama (likely; transcript says 'llama'/'Alamo'), Claude (cloud API key), Grok (cloud API key), Zoom, Google Meet, Microsoft Teams

## [Google Shrunk 31GB of AI Memory Down to 4GB (TurboQuant)](../videos/dfMeOTLSar8.md)
`dfMeOTLSar8` · Kai Explains · 2026-08-02 · q3 · practitioner · news · also: rag-retrieval, inference-serving, token-cost-efficiency

Explains TurboQuant, Google's training-free vector compression (31GB to about 4GB for 10M vectors), the independent TurboVec build, and KV-cache gains. Google published math only, not a supported product.

- Techniques: Data-oblivious rotate-and-round quantization; 1-bit residual sign correction (QJL); Filtered search inside the distance kernel; Same rotation applied to the KV cache; Adoption rule of thumb
- Tools: TurboQuant (Google research, published as a paper; no official product), TurboVec (Rust library with Python bindings, by Ryan Kodry; version not stated), FAISS FastScan (Meta; named in the transcript as 'face fast scan'), Qdrant (vector database; now ships the rotation trick, per the speaker), LangChain, LlamaIndex, Lloyd-Max quantizer, QJL (1-bit residual method), Product quantization (background concept, not used)

## [No API Key. No Cloud. Just Mac AI (Apfel)](../videos/wiQo9gayiqU.md)
`wiQo9gayiqU` · Better Stack · 2026-08-02 · q3 · intro · review · also: token-cost-efficiency, dev-tools

Better Stack demos Apfel, an MIT-licensed macOS CLI that exposes Apple's built-in ~3B on-device model through a terminal prompt, shell workflows and an OpenAI-compatible localhost server, and is candid about its limits.

- Techniques: Install and one-shot streaming prompt; Generate code straight into a file; Feed an existing file for feedback; Drop-in OpenAI SDK replacement for local dev; Tiered routing for cheap tasks
- Tools: Apfel (transcribed as Appful; MIT-licensed CLI and local server), Apple Foundation Models framework, Apple Intelligence (on-device ~3B model), Homebrew (brew), OpenAI SDK (Python, used unchanged), Ollama (transcribed as Olama; comparison only), MLX (comparison only), Llama and Qwen (open-weight models named in comparison)

## [Kimi K3 + DSpark Is INSANE (Beats Claude + 3x Faster + OpenSource)](../videos/cGhT8G408lA.md)
`cGhT8G408lA` · Kai Explains · 2026-08-02 · q3 · practitioner · news · also: inference-serving, models-research, token-cost-efficiency

Open-weight Kimi K3 is pitched as near-frontier for coding, and a dSpark speculative-decoding drafter claims 3.14x faster output with identical tokens. The talk includes useful caveats on acceptance rate, hardware and hallucinations.

- Techniques: Speculative decoding with a block-diffusion drafter and confidence-gated verification; Train the drafter on hidden states from the serving engine; Match the drafter's attention design to the target's to share KV layout; Track cost per completed task instead of per-token price; Swap the model behind an existing agent harness via base URL
- Tools: Kimi K3 (Moonshot AI), Kimi K2.6, Kimi Delta Attention, dSpark (Infraact drafter), vLLM, Claude Code, Cursor, Cline, Claude Opus 4.8, Claude Fable 5, GPT 5.6 Sol, DeepSeek V4 Pro

## [Can a Local LLM (Kimi K3) Actually Replace Claude or Codex for Coding?](../videos/wu_I6FWeJl4.md)
`wu_I6FWeJl4` · Kai Explains · 2026-08-02 · q3 · practitioner · news · also: models-research, token-cost-efficiency

Kai Explains argues Kimi K3 is a cheaper, frontier-adjacent API model worth testing for coding, but its "open" weights and launch benchmarks are less impressive than headlines suggest, and it is not a local model.

- Techniques: Week-long hard-ticket bake-off before switching models; Design agent workloads around cache-hit input pricing; Cross-check vendor benchmark claims against independent leaderboards; Three-question filter for model launch claims
- Tools: Kimi K3, Claude Opus 4.8, Claude Fable 5, GPT 5.6, Claude, Codex, Code Arena, Artificial Analysis Intelligence Index, DeepSWE

## [Qwen 3.6 + Ollama is INSANE: Better than Claude Code (FREE + Local + open Source)](../videos/qS5ZUEaKwNw.md)
`qS5ZUEaKwNw` · Kai Explains · 2026-08-02 · q3 · intro · review · also: coding-agents, token-cost-efficiency

Kai runs Alibaba's open Qwen 3.6 locally through Ollama and Qwen Code against Claude Code on three same-prompt builds; local wins on privacy, cost and offline use, but loses on finish and wiring.

- Techniques: Point Qwen Code at a local Ollama model; Raise the Ollama context window before running an agent; Smoke-test the agent loop before real work; Compare agents on the same prompts, judged by behavior; Route by lane: local for private, offline or cheap work; cloud for complex repos
- Tools: Qwen 3.6 (Alibaba open-weights model; sizes from 2B to 122B per transcript), Qwen Code (Alibaba's open-source agentic coding harness), Ollama (local model server, default context 4,096), Claude Code (Anthropic, cloud comparison, $200/month Max plan), Qwen 3.5 (earlier model, mentioned), Three.js (used in the aquarium task)

## [Google Just Made TensorFlow.js Obsolete (LiteRT.js)](../videos/8c68vFpT9Tk.md)
`8c68vFpT9Tk` · Better Stack · 2026-08-02 · q3 · intro · review · also: inference-serving, dev-tools

Better Stack walks through LiteRT.js, Google's WebAssembly on-device inference runtime for browsers, and builds a client-side webcam pose-capture app to test its CPU and WebGPU speed against TensorFlow.js.

- Techniques: Select a backend per device tier; A/B the backends on your own hardware before trusting vendor numbers; Port existing models instead of rewriting them; Client-side webcam pose pipeline; Export pose recordings for retargeting
- Tools: LiteRT.js, LiteRT, TensorFlow.js, WebAssembly, XNNPack, ML Drift, WebGPU, WebNN, LiteRT Torch, AI Edge Quantizer, LiteRT-LM.js (announced, not shipped), BlazePose

## [OpenCV 5 Is Here - The Biggest Update Since 2018 (We Tested It)](../videos/piHpZWcgQyc.md)
`piHpZWcgQyc` · Better Stack · 2026-08-02 · q3 · intro · review · also: inference-serving, dev-tools

Better Stack tests OpenCV 5's rewritten CPU-only DNN engine (ONNX operator coverage 22% to 80%) on colorization, detection, diffusion inpainting and VLM captioning; only detection looks practical.

- Techniques: Choose the DNN engine by backend need; Benchmark a vendor speed claim on your own model before switching; Tune diffusion inpainting steps to trade artifacts for latency
- Tools: OpenCV 5, OpenCV 4 (classic DNN engine), ONNX Runtime, PyTorch, YOLOv8, OWLv2, PaliGemma, Gemma 4 (12B, run locally), CUDA, OpenVINO, C++17

## [The Best Local AI Hardware (APPLE M5 MAX vs NVIDIA DGX SPARK)](../videos/4kuS_1y-nqc.md)
`4kuS_1y-nqc` · Kai Explains · 2026-08-02 · q3 · intro · review · also: inference-serving

Compares Apple Mac Studio, NVIDIA RTX 5090 and DGX Spark for local LLMs through memory capacity, bandwidth and compute. Main takeaway: decode speed follows memory bandwidth, so size the model first, then pick hardware.

- Techniques: Fit-first sizing before hardware choice; Bandwidth-bound decode estimate (derived); Local hardware decision tree; Hybrid local and cloud split
- Tools: NVIDIA GeForce RTX 5090, NVIDIA GeForce RTX 4090, NVIDIA DGX Spark, Apple Mac Studio, Apple M3 Ultra, CUDA

## [Local AI On Apple Silicon uses 7X Less RAM](../videos/vHhephsP6vU.md)
`vHhephsP6vU` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: inference-serving

Better Stack walks through Turbo Fieldfare, a Swift/Metal Mac app that runs a 26B Gemma 4 mixture-of-experts model in about 2 GB of RAM by streaming expert weights from SSD on demand.

- Techniques: Resident/streamed weight split for MoE models; Zero-copy SSD-to-GPU loading on unified memory; Store weights in the kernel's native quantized layout; Overlap I/O with always-resident compute; Per-layer LFU expert cache; Turbo Fieldfare setup steps shown (no exact commands)
- Tools: Turbo Fieldfare (Swift/Metal Mac app, repo linked in video description; no version stated), Gemma 4 (26B-parameter mixture-of-experts model), Swift, Metal (Apple GPU API), Apple Silicon (M3 Max used for the benchmark)

## [Run KIMI K3 on Your Laptop Locally (No GPU Needed)](../videos/tjdCBCr4qhQ.md)
`tjdCBCr4qhQ` · Kai Explains · 2026-08-02 · q4 · practitioner · news · also: models-research, inference-serving

Kimi K3's 2.8T-parameter open weights run on a 2021 M1 Max via the DeltaFin project, which streams routed experts from disk at 14.6 s/token. Covers MXFP4 quantization-aware training, hybrid attention, quant trade-offs, and the serving-hardware gap.

- Techniques: Expert streaming from disk with a resident spine; Selective mixed-precision quantization for MoE; Quantization-aware training instead of post-hoc quantization; Measure a quant ladder by next-token agreement; Fused dequantize-and-matvec kernel; Deterministic decoding with lossless n-gram speculation; Architecture-level KV cache reduction with hybrid attention
- Tools: Kimi K3 (Moonshot AI), DeltaFin (MIT-licensed local inference project, 274 stars at recording), Unsloth quants (UD-IQ1_S, 1-bit M, 2-bit XXS, 2-bit XL, 4-bit, 8-bit), MXFP4 (4-bit block floating point), Kimi Delta Attention, Apple M1 Max (64 GB), Apple Silicon NEON, x86 AVX2, NVIDIA DGX Spark, NVIDIA B300 (8-way node), CUDA, Hugging Face

## [What Would It Cost to Run Claude Fable 5 Locally?](../videos/fXWFSTSvnVM.md)
`fXWFSTSvnVM` · Kai Explains · 2026-08-02 · q3 · intro · other · also: inference-serving, infra-cost-scaling

Back-of-envelope memory and concurrency math on what it would take to self-host a frontier-scale open model (Kimi K3 as a stand-in for Claude Fable 5): a Mac Studio or 4xH100 cannot hold it, and serving 100 people is a data-center sizing problem.

- Techniques: Weight memory floor estimate; Concurrency sizing from arrival rate and service time; Hybrid local and cloud routing; Rent-before-buy pilot
- Tools: Claude Fable 5 (Anthropic model; weights not public, used only as the question), Kimi K3 (open-weight model, 2.8T parameters, MXFP4 weights as stated; used as the sizing example), NVIDIA DGX B200 (8x B200 GPUs, 1.44 TB GPU memory), NVIDIA DGX B300 (8x B300 GPUs, about 2.3 TB GPU memory), NVIDIA H100 (80 GB each, 4 units discussed), Apple Mac Studio (up to 512 GB unified memory), MXFP4 (4-bit weight format, called MXFFP4 in the auto-captions)

## [Kimi K3 Is INSANE with Claude Code (FREE + Local + open Source)](../videos/M48WuCSjmHs.md)
`M48WuCSjmHs` · Kai Explains · 2026-08-02 · q3 · intro · review · also: claude-code, token-cost-efficiency, models-research

Kimi K3 can drive Claude Code through an Anthropic-style endpoint at about a third of frontier price, but 'local' is unrealistic: the full weights need ~1.4 TB.

- Techniques: Swap the backend model under Claude Code via environment variables; Route through OpenRouter for a one-line switch; Acceptance test on a real repo bug before switching; Tiered model routing for cost; Lean on cached input pricing for repeated context; Self-host only with real GPU capacity, for privacy or compliance
- Tools: Claude Code, Kimi K3, Kimi K3 Swarm, Claude Fable 5, Claude Opus 4.8, GPT 5.5, OpenRouter, Artificial Analysis intelligence index, GDPval (transcribed as 'GDP Vol'), Mac Studio, Nvidia H100, Nvidia B200

## [What Would It Cost to Run Kimi K3 Locally?](../videos/ni5P3gT8OXo.md)
`ni5P3gT8OXo` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: inference-serving, infra-cost-scaling

Napkin math for running Kimi K3 locally: ~1.5 TB of 4-bit weights rules out Mac Studio and 4xH100, 8xB200 is barely enough, and serving 100 users is a data-center project.

- Techniques: Weight memory estimate for a quantized model; Headroom budget for a serving node; Concurrency sizing instead of user counting; Peak-moment plus prompt-length sizing; Hybrid routing: local for routine, cloud for hard; Rent before you buy
- Tools: Kimi K3, Hugging Face, Mac Studio, NVIDIA H100, NVIDIA B200, NVIDIA B300, NVIDIA DGX B200, NVIDIA DGX B300, MXFP4 (4-bit format, as named in transcript), Claude, GPT

## [PewDiePie is a software engineer now...](../videos/gQUQZxrM5Ts.md)
`gQUQZxrM5Ts` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: security-guardrails, dev-tools

Walkthrough of Odysseus, a viral self-hosted AI workspace with a local model cookbook, deep research and cross-session memory. The host calls it a fun local playground but not a production dependency, citing code quality and an agent threat model that needs a locked-down host.

- Techniques: Setup on macOS via Docker script; Hardware-aware local model selection; Blinded side-by-side model comparison; Zero-API local deep research loop; Persistent memory via vector store; Keep Mac GPU inference outside Docker
- Tools: Odysseus, Docker, llama.cpp (transcript: 'Llama CPP'), Metal, SearXNG (transcript: 'Sear XNG'), ChromaDB, FastAPI (transcript: 'fast API'), ntfy (transcript: 'Nifty', for push notifications), IMAP, OpenCode, LLM Fit, Alibaba Deep Research

## [This Could Change Local AI Forever](../videos/W_rROyZKEYY.md)
`W_rROyZKEYY` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: inference-serving, models-research

Prism ML's Bonsai 27B compresses a 27B model to 5.9 GB (ternary) or 3.9 GB (1-bit); the speaker says the 1-bit build is a headline and the ternary build is the usable one, with agentic quality falling notably.

- Techniques: Group-scaled low-bit weight quantization; On-device memory budgeting beyond file size; Capability-split regression check before swapping a local model; Local-first routing with cloud escalation; Validate speed in your own runtime
- Tools: Bonsai 27B (PrismML), Qwen 3.6 27B (base model), GGUF runtimes, Q4 / Q5 / Q8 quantizations, speculative decoding, RTX 5090, Apple M5 Max, iPhone (12 GB RAM reference device)

## [Mojo + Vulkan is INSANE: Run Local AI on ANY GPU (Goodbye CUDA)](../videos/CbNrKGMDM7g.md)
`CbNrKGMDM7g` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: inference-serving, dev-tools

Kai Explains argues Vulkan (llama.cpp) and Mojo are weakening the CUDA lock-in, so local AI runs on AMD, Intel, Apple and iGPU hardware, with CUDA still fastest at the top end.

- Techniques: Run local models on a non-NVIDIA GPU via llama.cpp Vulkan backend; Benchmark Vulkan against the vendor stack on the same hardware; Write a GPU kernel once in Mojo and compile per vendor; Compare a rewritten kernel to a vendor-tuned kernel on the same chip
- Tools: CUDA, Vulkan, llama.cpp, ROCm, Metal, SYCL, MoltenVK, Mojo, Modular, PyTorch, TensorFlow, JAX

## [SeFI image, Leanstral Beats Every Math AI, Hy3 Challenges GPT, Agents A1 & Bytedance AI News](../videos/rVwK1fuzKJU.md)
`rVwK1fuzKJU` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, training-finetuning-rl, inference-serving

Weekly Kai Explains roundup of late-July 2026 open-model releases: Mistral Leanstral 1.5 (Lean 4 prover), Tencent HY3, InternScience Agents A1, CeFi Image, ByteDance Depth Anything 3 and GenRecon. Mostly release-announcement content with a few concrete numbers.

- Techniques: Test-time compute scaling for formal provers; Property-generation plus formal proof as a bug finder; Semantic-first two-stream diffusion
- Tools: Leanstral 1.5, Lean 4, Lean language server, CISPO, Mistral Vibe, Hugging Face, Tencent HY3, Hunyuan 3, CodeBuddy, WorkBuddy, Tencent Cloud, OpenRouter

## [Open-Source Dictation Is Here… Goodbye Subscriptions](../videos/mIL4sZa8M0E.md)
`mIL4sZa8M0E` · Better Stack · 2026-08-02 · q2 · intro · review · also: dev-tools

Better Stack demos Fluid Voice, a free open-source Mac dictation app that runs speech-to-text and LLM cleanup fully on-device. Its main pitch is no subscription and no cloud; it is Mac-only and needs a ~3.5 GB model.

- Techniques: Local two-stage dictation with LLM cleanup; Install and permission setup for macOS dictation tools
- Tools: Fluid Voice, Parakeet, Fluid Intelligence, Wispr Flow, SuperWhisper, Cursor, Claude, Slack, Homebrew (brew install mentioned, command not spoken)

## [Bonsai runs on iPhone, Claude Browser ,Muse Spark, ARDY by Nvidia, 1X Robot Hand & More AI News](../videos/4TlbzLB3IgE.md)
`4TlbzLB3IgE` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, claude-code, voice-multimodal

Weekly roundup (Aug 2026): Meta Muse Spark 1.1, a built-in browser in Claude Code, Bonsai 27B running in 1-bit on a phone, several open vision and edge models, NVIDIA's ARTI motion model, and 1X NEO's tendon-driven hands.

- Techniques: Open the Claude Code built-in browser; Expect a domain prompt and per-write classifier on external browsing; Run Bonsai 27B locally on Apple or NVIDIA hardware; Interleaved token stream plus silence token for live video; Output format as the task selector for a unified vision model; Mid-generation constraints with a look-ahead window for motion
- Tools: Muse Spark 1.1 (Meta Superintelligence Labs), Meta Model API (public preview), Meta AI app (thinking mode on meta.ai), Claude Code (desktop Code tab built-in browser), Claude Desktop, Bonsai 27B (PrismML), MLX, CUDA, Hugging Face, GitHub, MoSVL Realtime (name as captioned; 11B), X-RopeE positional encoding (as captioned)

## [Build Your Own Fully Private Local AI Stack (Chat, RAG, Coding Agent & Automation)](../videos/np8booSU7Og.md)
`np8booSU7Og` · Kai Explains · 2026-08-02 · q3 · practitioner · tutorial · also: rag-retrieval, coding-agents, agent-architecture

Kai Explains walkthrough of a fully local AI stack: llama.cpp behind one OpenAI-compatible endpoint, with AnythingLLM for chat and RAG, Pi as a local coding agent, and n8n for email automation.

- Techniques: Single OpenAI-compatible endpoint as the integration bus; llama-server router preset mode, with LlamaSwap as fallback; Headless AnythingLLM in Docker, configured from the UI; Local RAG with AnythingLLM defaults; Pi as a local coding agent; n8n email triage with a local model; Always-on home lab hardening
- Tools: llama.cpp, llama-server, LlamaSwap, AnythingLLM, Open WebUI, LanceDB, Pi (coding agent, npm), OpenCode, n8n, Docker, Docker Compose, Portainer

## [Best Local Agent Harness Right Now (My Top 3)](../videos/YgyyWDGeQWM.md)
`YgyyWDGeQWM` · Kai Explains · 2026-08-02 · q3 · intro · review · also: coding-agents, agent-architecture, context-engineering

A survey of local/open coding-agent harnesses (OpenCode, Aider, Pi, plus OpenHands, Cline, Goose) arguing the harness now matters more than the model, with local-model pairing advice and a warning that the list goes stale fast.

- Techniques: Git-native atomic AI commits (Aider); Mid-session model downgrade for cost; Lazy-loaded skill blocks to keep the base prompt small (Pi); Custom subagents with per-agent model and permissions (OpenCode); Parallel agents on one GPU via vLLM; Local model sizing by memory footprint; Pre-standardization vetting checklist
- Tools: OpenCode (172k+ GitHub stars per speaker; 1.68M weekly npm installs as of June 2026), Aider, Pi (by Armin Ronacher), OpenClaw, OpenHands (spoken as 'Open hands'), Cline (spoken as 'Klein'), Goose, Roo Code (archived May 2026), Gemini CLI, Claude Code, Claude Opus 4.8, GPT-5.5

## [Kimi K3 Fable 5 & GPT 5.6 Sol Killer, Inkling, Xiaomi Robotics U0, MobileWan, Needle & More AI News](../videos/sUamCGBjWkM.md)
`sUamCGBjWkM` · Kai Explains · 2026-08-02 · q3 · practitioner · news · also: models-research, mcp-and-tools, data-engineering

Weekly AI news roundup (Aug 2026): Kimi K3 and Inkling open-weight releases, ACT2 and Xiaomi robot world models, on-phone 5B video diffusion, a 0.8B end-to-end OCR model, and a 26M function-calling model.

- Techniques: Self-driven fine-tuning loop for a behavioral constraint; Failure-driven single-example post-training loop; Chunk-wise recurrent attention for constant-memory long generation; Attention-only tiny router for tool selection; Long-horizon kernel-optimization evaluation
- Tools: Kimi K3 (Moonshot AI), Kimi Delta Attention, Kimi Code, Kimi Work, Kimi API, Claude Fable 5, GPT 5.6 Sol, Opus 4.8, GPT 5.5, Inkling, InklingSmall, OpenCode

## [Local AI Just Hit the Tipping Point (Colibri)](../videos/_2knU_H8XwU.md)
`_2knU_H8XwU` · Kai Explains · 2026-08-02 · q4 · practitioner · review · also: inference-serving, models-research

Walkthrough of Colibri, a one-person C engine that runs the 744B-parameter MIT-licensed GLM 5.2 on a 25GB laptop by streaming MoE experts from disk; honest speed is about 0.05 to 0.1 tokens/s.

- Techniques: Stream MoE experts from disk through a per-layer LRU cache; Learned hot-expert pinning across sessions; Quantize the MTP head to int8 for speculative decoding; Shard-by-shard FP8 to int4 conversion with resumable progress; Colibri reproduction steps (from the video)
- Tools: Colibri (single-file C inference engine for GLM 5.2; .coli model format), GLM 5.2 (ZAI, MIT license, 744B-parameter MoE, FP8 checkpoint about 756GB), GCC, OpenMP, AVX2, Unsloth 2-bit quantization (about 240GB), Ollama (its glm 5.2 cloud tag routes to ZAI's cloud API, not local inference), llama.cpp (runs GLM 5.2 with a dense attention fallback; DSA sparse attention not in mainline), DS4 (disk-streaming approach by the Redis creator, referenced as independent work), WSL2 with VHDX, Hugging Face (pre-built int4 checkpoint), Mac Studio (256GB, Unsloth 2-bit reference)

## [I Haven't Typed in a Week (Thanks to This App)](../videos/ZRsDQp9CrXc.md)
`ZRsDQp9CrXc` · Better Stack · 2026-08-02 · q3 · intro · review · also: voice-multimodal, dev-tools

Better Stack host tours Handy, an open-source, MIT-licensed, fully offline dictation app with user-chosen models, and compares its output against Google Docs voice typing and Wispr Flow on one passage.

- Techniques: Handy push-to-talk or toggle dictation setup; Choosing a model by speed/accuracy trade-off; Adding a custom fine-tuned Whisper model; Side-by-side dictation accuracy check
- Tools: Handy (open-source offline dictation app, MIT, built by CJ Pace), Tauri (transcribed as "talk"; the Rust-plus-web-UI shell is implied by the description), React, TypeScript, Transcribe CPP (runtime for Whisper-family GGML/GGUF models), transcribe-rs (runs Parakeet), Parakeet Unified 0.6B (CPU-only speech model), Whisper (GGML models, including custom fine-tunes), Silero VAD (transcribed as "Cilero VAD"), cpal (cross-platform audio input), rdev (global keyboard shortcuts), rubato (real-time resampling)

## [How to Run Qwen's 36B Model Locally on Laptop](../videos/C4tQLOqYsXw.md)
`C4tQLOqYsXw` · Kai Explains · 2026-08-02 · q3 · practitioner · tutorial · also: inference-serving, models-research

Kai walks through running Qwen's 35B-total / 3B-active MoE coding model locally via Ollama, with hardware tiers, context-length and tool-calling gotchas, and an honest caveat on the SWE-bench headline.

- Techniques: Serve a local coding model with Ollama behind an OpenAI-compatible endpoint; Raise Ollama's context length before agentic use; Pass the Jinja flag when running llama.cpp directly; Choose the model variant by VRAM and workload; Budget KV cache against context length
- Tools: Qwen 3.6 35B-A3B (MoE, 35B total / 3B active, Apache 2.0), Qwen 3.6-plus (proprietary cloud model, not locally runnable), Qwen dense 27B, Gemma 4 (dense 31B and a local model cited at 52% SWE-bench), Claude Sonnet 4.5 (comparison, 77.2% on public harness), Ollama, LM Studio, MLX, llama.cpp (Jinja flag), Unsloth GGUF builds, Hugging Face, Cline (captioned 'Klein')

## [OpenClaw in Your Hand: Building a Physical AI Terminal - Lech Kalinowski, Callstack](../videos/akk6KRlcwW4.md)
`akk6KRlcwW4` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: inference-serving, product-ux

Callstack engineer Lech Kalinowski builds a handheld text-terminal for OpenClaw and local LLMs on an ESP32, with a thin-client design backed by a 120B model on a DGX Spark. Mostly a hardware showcase with useful field notes.

- Techniques: Thin-client MCU with a heavy backend; Pre-allocated one-bit page buffers; Dual-display split by job; OpenAI-style proxy in front of open models; Graceful degradation across hardware parts
- Tools: OpenClaw, ESP32, NVIDIA DGX Spark, NVIDIA serving stack (auto-caption: 'Tensor Earth'), OLED display, e-paper display

## [State of the Union: Why Local, Why Now — NVIDIA, Osmantic, Roboflow, EXO Labs, @matthew_berman](../videos/KB41dTlX1Uc.md)
`KB41dTlX1Uc` · AI Engineer · 2026-07-18 · q3 · intro · panel · also: inference-serving, training-finetuning-rl, models-research

Panel on why local AI is now practical: multi-model setups, frontier-plans/local-executes splits, distilling big-model consensus into small specialized models, and the remaining UX and openness gaps.

- Techniques: Plan with frontier, execute with local; Consensus distillation; Drop open-vocabulary machinery when classes are fixed; Trace-driven model routing; Retune existing configs for small hardware; Hardware-aware model selection; Frontier bootstrap then open model
- Tools: vLLM, SGLang, Local.ai, ODS (open-source deployment system), DGX Spark, DGX Station, Brev, Segment Anything 3 (SAM3), Cursor, Codex, Llama, Qwen 3.5 / 3.6

## [Frontier results, on device - RL Nabors, Arize](../videos/fWXJM-J0ZB8.md)
`fWXJM-J0ZB8` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: inference-serving, evals, context-engineering

Rachel Lee Neighbors shows how to right-size a model: prototype with a frontier model, build a golden eval set, then pick the smallest local model (Llama 3.2 3B) that meets latency and quality targets, closing the gap with prompt changes and deterministic post-processing.

- Techniques: Prototype-big-deploy-small pipeline; Golden dataset with multi-metric eval in Phoenix; Latency budget by percentile; Single-variable prompt ablation; Deterministic post-processing instead of prompt tuning; Auditing the LLM judge; Regression evals in CI
- Tools: Phoenix (Arize), Goose, Gemma 4 E2B, Gemma 3, Llama 3.2 3B, Qwen 2.5 1.5B, Qwen 3 1.7B, Claude Sonnet, Claude Opus, MobileNet, YOLO, MediaPipe

## [Google's New AI Architecture Changes Everything (Gemma 4 12B)](../videos/WLtCHXdHTF0.md)
`WLtCHXdHTF0` · Better Stack · 2026-07-02 · q2 · practitioner · review · also: models-research, voice-multimodal

Better Stack explains Google's encoder-free Gemma 4 12B, which replaces vision and speech encoders with linear projections, then runs an offline image test on a 24GB M2 Mac. The architecture detail is useful, but the claims are unbenchmarked.

- Techniques: Patch-and-project image input for an encoder-free multimodal LLM; Audio frames projected as tokens; Offline real-time image sanity check for a local model; Native multi-token prediction drafters
- Tools: Gemma 4 12B, Gemma 4 26B (sibling model, comparison only), OMLX (local inference framework for Apple Silicon), Google AI Edge Gallery (mobile app, buggy on image input in the host's test), M2 MacBook Pro (24GB, host's test machine)

## [1,000+ Tokens/Sec: Google Just Shattered the AI Speed Limit (DiffusionGemma)](../videos/Dxn3BcSgsMY.md)
`Dxn3BcSgsMY` · Better Stack · 2026-07-02 · q3 · intro · review · also: models-research, inference-serving, coding-agents

Better Stack walks through Google DeepMind's DiffusionGemma, a diffusion-style text model that refines a 256-token canvas in parallel, and tests its speed on an H100 via RunPod and OpenCode.

- Techniques: Parallel canvas refinement (non-autoregressive decoding); Uniform-state corruption for text diffusion; Encoder/denoiser mode split with bidirectional denoising; Run DiffusionGemma on RunPod and read the endpoint; Point OpenCode at the remote DiffusionGemma server; Local serving with vLLM in Docker; Read throughput from the server logs
- Tools: DiffusionGemma, Gemma 4 (26B base), OpenCode, vLLM, Docker, RunPod, NVIDIA H100, NVIDIA RTX 5090, Hugging Face

## [Ideogram 4.0 image model, ByteDance Ditches Nvidia GPU, Google's 16GB Multimodal Beast AI News](../videos/12_TXXeI4uE.md)
`12_TXXeI4uE` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, voice-multimodal, training-finetuning-rl

Roundup of late-June/early-July 2026 open-model releases: Ideogram 4.0 (open-weight, describe-to-structure training), Reve 2.0, Joy AI Echo long-video generation, Gemma 4 12B unified multimodal model, Magenta RealTime 2, ByteDance CUDA Agent, LFM 2.5 VL 450M, Molmo 2, MDA depth, Nemotron ASR, NVIDIA Artifixer.

- Techniques: Describe-to-structure-to-recreate training; Mixture-density depth output; Agentic kernel optimization loop; Unified decoder-only multimodal input without encoders
- Tools: Ideogram 4.0, Reve 2.0, Joy AI Echo, Gemma 4 (12B), Magenta RealTime 2 (MRT2), CUDA Agent, CUDA Agent Ops 6K, torch.compile, KernelBench, LFM 2.5 VL 450M, Molmo 2, MDA (Modeling Depth Ambiguity)

## [Microsoft MAI Models, Live AI Characters, 3D from One Image & More AI News](../videos/WVC03w3AG6k.md)
`WVC03w3AG6k` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, voice-multimodal

Kai Explains weekly AI news: Microsoft's seven-model MAI family from Build 2026, StreamChar live audio-video characters, Pager 360-panorama geometry, and JetBrains' open Mellum 2 coding model.

- Techniques: Reproject non-native inputs into the distribution a model was trained on (Pager); Split a streaming avatar into an LLM planner and a joint audio-video diffusion generator (StreamChar); Try Mellum 2 Thinking as a low-active-parameter coding model
- Tools: MAI-Thinking-1 (captioned MyThinkingOne), MAI Image 2.5, MAI Transcribe 1.5, MAI Voice 2, MAI Voice 1, MAI Code 1 Flash, GitHub Copilot, VS Code, Azure AI Foundry, Arena text-to-image leaderboard, StreamChar, Pager

## [Midjourney full body scanner, VibeThinker, Qwen-Robots, Happy Oyster & More | AI News](../videos/aGseXhwqiLg.md)
`aGseXhwqiLg` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, agent-architecture, voice-multimodal

Weekly AI news roundup (2026-07-02): a 3B reasoning model with contested benchmarks, Midjourney's ultrasonic full-body scanner, Qwen robot models, world models, TTS, a multi-agent deep research system, and a camera-control model.

- Techniques: Orchestrator, parallel sub-agents, and a global verifier; Progressive training for interactive world models; World memory via retrieval of prior generations; Camera grid as a control signal; Two decoders for trajectory prediction; Unified state-action space for cross-embodiment control; Inline control tokens in TTS input
- Tools: VibeThinker (Weibo AI, 3B reasoning model, MIT license), Midjourney Medical (ultrasonic CT body scanner, unreleased), Qwen Robot Nav, Qwen Robot Manip, Qwen Robot World (Alibaba; Nav built on Qwen3-VL), DreamX World (5B interactive world model), Higgs Audio V3 (Boson AI TTS, research license), Molmo Motion and PointMotionBench (Allen AI), Apodex One (deep research agent, up to 150 sub-agents), Happy Oyster (Alibaba hosted world engine; formerly Happy Horse 1.0), OmniDirector (Kling team camera-control model), Hugging Face (weights), GitHub (code), arXiv (papers)

## [Humanoid GPT, GitHub for Robotics, Sana Real-Time AI Video Editing and D4rt 4D Scene Model AI News](../videos/EenYAIfx2ME.md)
`EenYAIfx2ME` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, voice-multimodal, evals

Weekly AI news roundup (2026-07-02) covering NVIDIA SANA streaming, Holo 3.1, Dots.TTS, D4RT, Tanker, MAMA, QJudger, VibeVoice and Humanoid GPT; nearly all claims are repeated from project pages, not tested.

- Techniques: Hybrid softmax/linear attention diffusion transformer for streaming video; Cycle reverse regularization for temporal consistency; Codebook-free autoregressive TTS with a flow-matching head; Ultra-low frame-rate continuous speech tokenizers for long-form dialogue; Multi-dimension structured LLM-as-judge with human-agreement validation; Contact-aware optimization for close multi-person pose; DAgger distillation from motion experts into a GPT-style controller; Compare quantized formats on your own hardware before choosing one
- Tools: SANA streaming, SANA video, SANA (NVIDIA), Holo 3.1, HoloTab harness, Android World benchmark, DGX Spark, NVIDIA RTX 5090, NVFP4, FP8, GGUF Q4, BF16

## [How To Actually Learn ComfyUI In 2026](../videos/p-MnjztaBT4.md)
`p-MnjztaBT4` · Kai Explains · 2026-07-02 · q2 · intro · tutorial · also: —

Kai Explains pitches a "Graph Framework" for learning ComfyUI: find your why, pick one of six domains, track daily habits, avoid pre-built mega workflows. A motivational intro that teases a future video series.

- Techniques: Wonder, Save, Yield plus Venn diagram for setting a learning why; Pick one ComfyUI domain before learning; Daily-activity goals tracked as a game in Habitica; Learn from scratch rather than from mega workflows; Side quests once tutorial copying stops teaching
- Tools: ComfyUI, Midjourney, Habitica, ControlNet, LoRA

## [Character swap live streaming, 3D mesh generator,  Google's DiffusionGemma & More AI News](../videos/73iY1aGFSYI.md)
`73iY1aGFSYI` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, inference-serving, coding-agents

Weekly open-source AI news roundup: Meta's MeshFlow mesh generator, Google's DiffusionGemma block-diffusion LM, Cohere's North Minicode coding model, plus robotics and webcam mocap releases.

- Techniques: Block-wise denoising decoding with confidence-based re-noising; Generate structured geometry as a continuous latent with a parallel diffusion transformer; Self-supervised quality scoring via pairwise majority voting; Shared keypoint conditioning across embodiments
- Tools: MeshFlow, Gradio, Hugging Face, Blender, Maya, DiffusionGemma, Gemma 4, GGUF, Kaggle, Vertex AI, North Minicode, open code

## [Finally… A NotebookLM Alternative With an API](../videos/DnMtDdkSIi0.md)
`DnMtDdkSIi0` · Better Stack · 2026-07-02 · q2 · intro · review · also: rag-retrieval, dev-tools

Walkthrough of Open Notebook, a self-hosted NotebookLM alternative with a REST API, swappable model providers including local Ollama, and podcast generation. Privacy and API access are the main draw; the Docker-first setup is a barrier.

- Techniques: Self-host via Docker Compose, then open the web UI; One notebook per project as a scoped research workspace; Structural codebase questions over an ingested repo; Custom podcast from dense documents; Pick the model provider per notebook based on sensitivity and cost
- Tools: Open Notebook, NotebookLM, AnythingLLM, Ollama, Docker / Docker Compose, SurrealDB, Gemini (named as the default-style provider the tool is not locked to)

## [Grok Imagine Video 1.5, Qwen-VLA, NVIDIA Cosmos3-Nano, MiniMax M3, Bernini AI, Stax & More AI News](../videos/kQh9Hhr_eK0.md)
`kQh9Hhr_eK0` · Kai Explains · 2026-07-02 · q2 · intro · news · also: models-research, token-cost-efficiency, evals

Weekly AI news roundup (Jul 2026): Grok Imagine Video 1.5, MiniMax M3 open-weight 1M-context model, NVIDIA Cosmos 3 Nano, Qwen VLA, ByteDance Bernini, plus OCR, diarization, TTS and Google Stacks eval toolkit.

- Techniques: Plan-then-render for unified video generation/editing; Custom eval datasets with custom evaluators (Google Stacks workflow); Tiered upgrade path for diarization
- Tools: MiniMax M3, MiniMax Sparse Attention (MSA), NVIDIA Cosmos 3 Nano, Cosmos 3 Super, Qwen VLA, Grok Imagine Video 1.5 Preview, ByteDance Bernini, TripoSplat, Quai KeyVL2 (30B sparse MoE, 3B active), PaddleOCR 1.6 (ERNIE 4.5 backbone), pyannote Speaker Diarization 3.1, pyannote Community-1

## [OpenAI GPT 5.6 launch, Realtime Video avatar, HappyHorse 1.1, Nvidia & More AI News](../videos/odlkEMloedA.md)
`odlkEMloedA` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, training-finetuning-rl, voice-multimodal

Weekly AI news roundup: GPT-5.6 Sol/Terra/Luna and its gated release, Happy Horse 1.1 video, Ornith 1.0 open coding models, WanStreamer, NVIDIA's video inference engine, Fine VLA and SURF. Mostly vendor-reported claims.

- Techniques: Self-scaffolding RL training (Ornith 1.0); Tiered model family routing; Automatic per-model acceleration stack selection; Single-transformer streaming for conversational avatars; Fine-grained instruction relabeling for robot data
- Tools: GPT-5.6 (Sol, Terra, Luna), OpenAI Preparedness Framework, Terminal Bench 2.1, GeneBench V1, ExploitBench, ExploitGym, Happy Horse 1.1, Happy Horse 1.0, Arena AI Video Arena, Ornith 1.0 (9B dense, 31B dense, 35B MoE, 397B MoE), Claude Opus 4.7, MiniMax M3

## [I Tried the Open Source ElevenLabs Alternative (Voicebox)](../videos/RL_PDX_BVxw.md)
`RL_PDX_BVxw` · Better Stack · 2026-07-02 · q3 · intro · review · also: voice-multimodal, mcp-and-tools

Better Stack walkthrough of Voicebox, a free open-source local voice studio for cloning, TTS, system-wide dictation and agent speech. Works well on Apple Silicon, but the tool is early and the agent integration was not tested.

- Techniques: Desktop install instead of Docker; Clone a voice from a short sample; System-wide dictation via global hotkey; Restart to clear app-level glitches; Pick the model for emotion control
- Tools: Voicebox, ElevenLabs, Ollama, Docker, Piper, Whisper, Claude Code, Cursor, Chatterbox TTS Turbo, MCP

## [Real-time Voice cloning, Kimi K2.7 CODE, GLM 5.2 and 3D reconstruction | AI News](../videos/DX4kW1vdTXc.md)
`DX4kW1vdTXc` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, voice-multimodal, coding-agents

Weekly open-model news roundup (2026-07-02): Zonos 2 voice cloning, MiniMax M3, Kimi K2.7 Code, GLM 5.2, NVIDIA Motion Bricks, Microsoft Fara-7B, plus robotics and 3D items. Mostly vendor-reported claims.

- Techniques: Shared fixed-size latent for variable-view 3D reconstruction (Surflow); Reusable motion primitives with zero-shot composition (Motion Bricks); Report steps and cost per task next to success rate for computer-use agents (Fara-7B); Canonical body topology as a pivot between body models (SOMA); Haptic torque feedback in teleoperation for robot data collection (UME); Where to get each release (as stated in the video)
- Tools: Zonos 2, Zyphra Cloud, MiniMax M3, MSA (Minimax Sparse Attention), Minimax Code, Kimi K2.7 Code, Kimi K2.6, KimiCode, Kimi Code Bench V2, Program Bench, MLS Bench Lite, MCP Atlas

## [Run Frontier AI at Home — Alex Cheema, EXO Labs](../videos/ESbWpPT_9-o.md)
`ESbWpPT_9-o` · AI Engineer · 2026-06-18 · q3 · deep · talk · also: inference-serving, infra-cost-scaling

EXO Labs' Alex Cheema argues decode is memory-bound, so local frontier inference is a memory, bandwidth and energy problem. He demos Mac clusters over Thunderbolt RDMA and a Mac plus DGX Spark prefill/decode split.

- Techniques: Kernel fusion of redundant launches; Cache-stable prompt prefix in the harness; Prefill/decode disaggregation across devices; Tensor parallelism over RDMA; Full-replica weights with append-only event logs for cluster state; Expose each node over HTTP and reach it through a mesh VPN; Budget-based Pareto benchmarking; Hypothesis-driven auto-research
- Tools: EXO, Claude Code, OpenCode, OpenClaw, Tailscale, MLX, llama.cpp, Thunderbolt 5 RDMA, 10GbE

## [Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind](../videos/SS-A8sE7hkw.md)
`SS-A8sE7hkw` · AI Engineer · 2026-06-18 · q2 · intro · talk · also: models-research, inference-serving, governance-compliance

Google DeepMind's Gemma team pitches open-weight Gemma 4 models (E2B to 31B) as a way to own, customize and run models locally, with on-device and single-GPU demos.

- Techniques: Drop-in local endpoint swap; Local sub-agent fan-out for batch work; Threshold-based task routing; Latency-class scheduling for on-device tasks; Own-eval-first model adoption
- Tools: Gemma 4, Gemini, Google AI Edge Gallery, LM Studio, Ollama, MedGemma, OpenRouter, LM Arena

## [From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google](../videos/-TiET_K-E_g.md)
`-TiET_K-E_g` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: training-finetuning-rl, inference-serving, skills-self-improvement

Google's Cormac Brick on on-device agents: a prompt-based skill harness on Gemma 4, and fine-tuning FunctionGemma on synthetic data to lift function-calling success from about 46% to 90%+ on most functions.

- Techniques: Progressive skill disclosure; In-app JavaScript rendering from a skill; Coding agent writes the skills; Synthetic-data fine-tune for fixed function calling; Export and deploy pipeline for small models; Chained tiny models for a pipeline
- Tools: LiteRT-LM, LiteRT, MediaPipe, Gemma 4, FunctionGemma, Gemma 3, Gemini Nano, Android AICore, Gemini CLI, Gemini Flash, litert-torch, transformers

## [Gemini Nano on device — Florina Muntenescu & Oli Gaymond, Google DeepMind](../videos/owH1f0N-keY.md)
`owH1f0N-keY` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: inference-serving, product-ux

Google DeepMind's Android team on using Gemini Nano on-device via ML Kit GenAI and Firebase hybrid fallback, with Q&A on battery, shared-model scheduling and device reach.

- Techniques: Runtime hybrid routing with cloud fallback; Use the ML Kit GenAI Prompt API for on-device structured tasks; Offload non-urgent batch work to background, charging-time windows; Prompt-stuffed retrieval as a stopgap RAG; Device testing and profiling for custom models
- Tools: Gemini Nano, AICore, ML Kit GenAI APIs, Prompt API, Firebase AI Logic, LiteRT-LM, AI Edge Gallery, Gemma 4

## [Nvidia's Huge releases | Claude Opus 4.8, Liquid AI, Microsoft Lens & More AI News](../videos/_Nh-wDT6Odc.md)
`_Nh-wDT6Odc` · Kai Explains · 2026-06-02 · q3 · intro · news · also: models-research, inference-serving, data-engineering

Weekly Kai Explains roundup (June 2026) of open-model and tool releases: NVIDIA Locate Anything 3B and PID decoder, Sapient HRM-Text-1B, Step 3.7 Flash, NuExtract 3, Microsoft Lens, Claude Opus 4.8, and Perplexity's Rust tokenizer.

- Techniques: Parallel box decoding for detection and grounding; Trace inversion for distilling reasoning into a small model; Template-driven document extraction with a reasoning toggle; Dense re-captioning of training data; Tokenizer hot-path optimization; Local runs of open-weight models; Choosing Opus 4.8 effort per task
- Tools: NVIDIA Locate Anything 3B, Qwen2.5-3B, MoonViT, Qwen3-VL, Rex Omni, HRM-Text-1B (Sapient Intelligence), LFM (Liquid AI, transcript reads 'LFM 2.58'), Quopus 3.6, Qwen3.6-27B, NVIDIA PID (Pixel Diffusion Decoder), SeedVR2, Flux.1-Dev

## [I Ran a Local LLM on 12-Year-Old Raspberry Pi (It Actually Worked!)](../videos/u8XQsL38WjQ.md)
`u8XQsL38WjQ` · Better Stack · 2026-06-02 · q3 · practitioner · tutorial · also: inference-serving

Better Stack runs the 90M-parameter Falcon H1 Tiny on a 2014 Raspberry Pi 1 by cross-compiling llama.cpp for ARMv6 and testing 2/4/8-bit quants; it works, but is far too slow and thin on knowledge to be useful.

- Techniques: Pick the OS image for a low-RAM board; Cross-compile llama.cpp for ARMv6 on a laptop; Minimal-footprint inference invocation; Stepwise quantization sweep with graded probes
- Tools: llama.cpp, Falcon H1 Tiny (90M, Technology Innovation Institute), Raspberry Pi OS Lite 32-bit, Raspberry Pi Imager, cross-compiler toolchain (spoken as DocCross), ssh / scp, Mamba, IBM Granite 4 (mentioned)

## [AI avatar beats HeyGen, 1-min 720p video, video timestamps AI, lip sync model: AI NEWS](../videos/MYzITZG4c4M.md)
`MYzITZG4c4M` · Kai Explains · 2026-06-02 · q3 · intro · news · also: models-research, inference-serving, voice-multimodal

Kai Explains weekly AI news (June 2, 2026): a roundup of new open-weight releases across robotics sim, small translation and video models, avatars, humanoids, TTS and segmentation.

- Techniques: Simulation as an evaluation signal; Prompt-level control of a small translation model; Ternary (1.58-bit) weights for memory savings; Rolling multi-segment inference for identity-stable long video; Few-step distillation (DMD) for video diffusion
- Tools: Genesis World 1.0, Nix (renderer), Quadrants (Python-to-GPU compiler), IsaacSim, MuJoCo, HiMT2 (Tencent translation models, captioned as 'HiMT2'), BitCPM-CANN, MiniCPM4, Huawei Ascend 910B / NPU, Marlin 2B, LongCat Video Avatar 1.5, Whisper Large V3

## [Llama-Swap: This Fixes The Most Annoying Local LLM Problem](../videos/GtTzO5ZOQr4.md)
`GtTzO5ZOQr4` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: infra-cost-scaling

Better Stack walkthrough of llama-swap, a single Go proxy that exposes one OpenAI/Anthropic-compatible endpoint and starts, swaps and TTL-unloads local model backends based on the request's model field.

- Techniques: Single front-door proxy for multiple local model servers; TTL-based idle unloading; Per-model backend control
- Tools: llama-swap, llama.cpp (llama-server), Ollama, LM Studio, vLLM, TabbyAPI, Open WebUI, Cursor, Continue, Qwen coder (transcript: 'quen-coder'), small-lm2 (name as spoken in the config example)

## [Developers Might Finally Have a Local TTS Model That Doesn’t Suck](../videos/pbsTTxKTuts.md)
`pbsTTxKTuts` · Better Stack · 2026-06-02 · q3 · intro · review · also: voice-multimodal

Hands-on test of Supertonic 3, a 99M-parameter local TTS model: fast and easy to deploy, but it mangles prices, dates and expression tags, so test your own app text first.

- Techniques: Stress-test TTS with production-shaped strings; Side-by-side demo harness for a TTS model; Point an OpenAI-style speech client at a local server
- Tools: Supertonic / Supertonic 3 (Supertone, on-device TTS, 99M parameters, 31 languages), supertonic (pip package: Python SDK, CLI, local HTTP server), ONNX Runtime (CPU inference), Python, OpenAI audio speech API (compatible local endpoint; cloud comparison), ElevenLabs ("11 Labs" in the transcript; cloud comparison), Java, C++, C# and browser example clients

## [This Is The Best Local Model Runner For Apple Silicon (oMLX)](../videos/EsLwzxTz-A4.md)
`EsLwzxTz-A4` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: inference-serving, token-cost-efficiency

Hands-on review of oMLX, an MLX-based local inference server for Apple Silicon with SSD-paged KV cache; one Qwen 3.6 35B coding run beats LM Studio on speed, with 400 errors at context overflow as the trade-off.

- Techniques: Serve a local model through an OpenAI-compatible endpoint and point a coding CLI at it; Same-model, same-context head-to-head benchmark for local runtimes; Keep the stable prefix on disk and reuse it after a session clear; Pick a lean harness when the context window is small
- Tools: oMLX, Apple MLX, Qwen 3.6 35B (4-bit), Codex CLI, Claude Code, LM Studio, Apple Silicon (M2 MacBook Pro)

## [This New Engine Runs Local AI Using 10x Less RAM! (Cactus)](../videos/nVhdDgYf_rI.md)
`nVhdDgYf_rI` · Better Stack · 2026-06-02 · q2 · intro · review · also: inference-serving, token-cost-efficiency

Better Stack demos Cactus, an edge inference engine with NPU-first execution, zero-copy weight mapping and a local-to-cloud hybrid router; the only measured result is about 260 ms local transcription on an iPhone 12 Pro, and the 10x RAM claim in the title is never measured.

- Techniques: Confidence-based local-to-cloud fallback; Streaming on-device transcription benchmark; Choose NPU-optimized model variants for the target device
- Tools: Cactus (inference engine, .cact model format, Swift package, dashboard with NPU-optimized models), GGUF (format the engine moves away from; not used), Parakeet (speech model, run locally; spelled Paracat in the auto-captions), Gemini 2.5 Flash (cloud fallback model), Swift (demo app language), iPhone 12 Pro (test device), Apple, Qualcomm and MediaTek NPUs (hardware targets)

## [Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face](../videos/OV56RddyFuU.md)
`OV56RddyFuU` · AI Engineer · 2026-05-18 · q2 · practitioner · demo · also: training-finetuning-rl, mcp-and-tools, coding-agents

Hugging Face's Merve Noyan demos open-model agent workflows: picking and serving open models, Hermes Agent, pushing agent traces to the Hub, HF MCP server and skills that let coding agents launch fine-tuning and batch OCR jobs.

- Techniques: Hub-ID local serving for coding agents; GGUF hardware-fit check before download; Agent-driven fine-tuning via skills; Session traces pushed to a Hub dataset; Corpus OCR via prompted batch job; HF MCP server for catalog access
- Tools: Hugging Face Hub, Hugging Face MCP server, Hugging Face skills (hub CLI, LLM trainer, Gradio, dataset), Inference Providers, Hermes Agent, Pi, llama.cpp, vLLM, MLX, LM Studio, Claude Code, Codex

## [Why MLX — Prince Canuma, Neywa Labs](../videos/zTLJNHj0DeQ.md)
`zTLJNHj0DeQ` · AI Engineer · 2026-05-18 · q3 · intro · talk · also: inference-serving, voice-multimodal

Prince Canuma argues for running agents, voice, and vision models fully on Apple Silicon with MLX to cut cloud subscription costs and work offline. Demos are mixed, and the talk ends with a TurboQuant KV-cache claim.

- Techniques: Modular speech pipeline; Chained short-clip video generation; Grounded visual reasoning on video; Storage-backed model loading on phones; TurboQuant-style KV-cache quantization; Live GPU monitoring during inference
- Tools: MLX, MLX-VLM, MLX-Audio, Marvis TTS, RF-DETR, Gemma 4, Qwen3-Omni, Core ML, Gradio, MacTop, Reachy Mini, LM Studio

## [Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind](../videos/_gVFUEdhCyI.md)
`_gVFUEdhCyI` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: models-research, inference-serving

Google DeepMind's Omar Sanseviero introduces Gemma 4, a family of open models from 2B to 32B parameters, and argues that small open models can now do multimodal and agentic work on-device.

- Techniques: Offload per-layer embeddings to CPU or disk; Parallel local generation on one machine; Pick the model by tokenizer for low-resource language fine-tuning; Stay on the framework the team already uses
- Tools: Gemma 4, llama.cpp, MLX, Ollama, Hugging Face Transformers, vLLM, SGLang, Keras, Android Studio, ShieldGemma, MedGemma, LM Arena

## [Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind](../videos/Lm8BLHkxiAo.md)
`Lm8BLHkxiAo` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: inference-serving, models-research

Google DeepMind's pitch for running Gemma 4 E2B/E4B agents on-device through LiteRT, with the conversion, quantization, device-benchmarking and NPU path laid out and vendor speed claims.

- Techniques: Hybrid local-plus-remote inference via function calling; Use native structured JSON output instead of prompt-only formatting; Packaging capabilities as user-authored skills; Bring-your-own-model conversion with graph inspection; Fleet-benchmark before shipping; Small local model as a gate in a split architecture
- Tools: LiteRT, TensorFlow Lite, LiteRT-LM, Gemma 4, Gemma 3, Model Explorer, AI Edge Portal, Google AI Edge Gallery app, Hugging Face, Core ML, Raspberry Pi, Qualcomm NPU

## [Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX — Adrien Grondin, Locally AI](../videos/a2muGkT4WD4.md)
`a2muGkT4WD4` · AI Engineer · 2026-05-18 · q2 · intro · demo · also: inference-serving

Adrien Grondin (Locally AI) shows how to run quantized Gemma 4 on iPhone with Apple's MLX, covering the mlx-swift-lm package, picking quantized weights, and speed on phones.

- Techniques: Load quantized models by Hub ID in an on-device Swift app; Choose quantization between 4-bit and 8-bit; Stream tokens to the UI; Small local model for automation steps; Compare inference engines via a local server
- Tools: MLX, mlx-swift-lm, mlx-lm, mlx-vlm, mlx-audio, Hugging Face, mlx-community, LM Studio, llama.cpp, Apple Shortcuts, Gemma 4, Qwen

## [Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind](../videos/_A367W_qvc8.md)
`_A367W_qvc8` · AI Engineer · 2026-05-18 · q4 · deep · talk · also: models-research, inference-serving

Google DeepMind researcher walks through Gemma 4's architecture: interleaved local/global attention, asymmetric GQA, per-layer embeddings in flash memory, a shared-expert MoE, and flexible image token budgets.

- Techniques: Interleaved local/global attention with sliding windows; Asymmetric GQA by layer type; Per-layer embedding tables offloaded to flash; Developer-selected image token budget; Shared-plus-routed MoE
- Tools: Gemma 4, Hugging Face, Kaggle, Ollama, Google AI Studio, Vertex AI

## [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google](../videos/BKWpYIWvAo4.md)
`BKWpYIWvAo4` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: inference-serving, skills-self-improvement, training-finetuning-rl

Google AI Edge on running small Gemma models on-device via LiteRT-LM, the on-device agent-skills pattern (progressive disclosure, constrained tool calls), and fine-tuning tiny models with synthetic data.

- Techniques: Progressive disclosure for skills; Three-primitive orchestrator; Constrained decoding scoped to tool calls; Synthetic data then fine-tune then quantize; Modular pipeline of small models; LoRA hot-swap on one base model; Skill testing loop with a coding agent and a device; Build-once, deploy-everywhere model file with AOT for NPU
- Tools: LiteRT-LM, LiteRT (formerly TensorFlow Lite), LiteRT-Torch, Google AI Edge Gallery, MediaPipe, Gemma 4 (E2B, E4B), Function Gemma (270M), Gemma 3 270M, EmbeddingGemma (300M), FastVLM (500M, Apple), Qwen 0.6B, Gemini CLI

## [Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI](../videos/fLUtUkqYHnQ.md)
`fLUtUkqYHnQ` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: training-finetuning-rl, inference-serving, models-research

Liquid AI's Maxime Labonne on training 350M to 24B edge models: small models have their own constraints, narrow targeting and doom-loop fixes via DPO and RL.

- Techniques: On-policy DPO pairs for doom-loop suppression; Repetition penalty inside RLVR; Fix training stage by diagnosis; Profile architecture on target hardware; Tool and environment offload for small models
- Tools: Hugging Face, Python

## [The 2.3B AI Model that "Thinks" like a 70B (Gemma 4)](../videos/ZxQ2DuejRhU.md)
`ZxQ2DuejRhU` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: models-research, evals

Better Stack runs informal local and on-phone tests of Google's Apache 2.0 Gemma 4 E2B and E4B models: fast on iPhone, weak at coding and vision, with Google's benchmark claims left unverified.

- Techniques: Offline local test harness with LM Studio and Cline; Fixed-prompt regression comparison across models; Check model output artifacts for leakage and phantom files; Quick capability probes; Try on a phone with the vendor's app
- Tools: Gemma 4 (E2B, E4B, Google, Apache 2.0), Qwen 3.5 (compared in the speaker's earlier video), LM Studio, Cline (transcribed as 'Klein'), Google AI Edge Gallery app, LiteRT-LM (Google's inference framework), MLX / Swift MLX (no Gemma 4 bindings yet), swift-lm (community project working on unofficial native bindings, as transcribed)

## [This Tiny 82M Model Just Beat Most TTS APIs (Runs Locally)](../videos/bdf6BxyxCnQ.md)
`bdf6BxyxCnQ` · Better Stack · 2026-05-02 · q3 · intro · review · also: voice-multimodal, infra-cost-scaling

Better Stack tries Kokoro 82M, a small open TTS model, on a Mac M4 Pro and weighs its speed, privacy and cost against its missing voice cloning and emotion control.

- Techniques: Run a small local TTS model as a drop-in for cloud TTS; Pick a small TTS model when time-to-first-audio matters; Evaluate TTS by listening to your own text per language and voice
- Tools: Kokoro 82M (TTS model, Apache 2.0), StyleTTS2 (architecture the model is based on), Misaki (text processing library named by the host), XTTS, CosyVoice, F5-TTS, ElevenLabs (cloud TTS), OpenAI TTS (cloud TTS), Python, pip, conda, Mac M4 Pro (test hardware)

## [Qwen 3.5 Small Models Are INCREDIBLE! (Testing 0.8B & 2B On Edge Devices)](../videos/hQoF_dv2UQ4.md)
`hQoF_dv2UQ4` · Better Stack · 2026-04-02 · q3 · intro · review · also: models-research, coding-agents

Hands-on offline tests of Qwen 3.5 0.8B and 2B on a laptop and iPhone: fast and surprisingly multimodal, but repetition loops and hallucinations rule out serious coding.

- Techniques: Local OpenAI-style server in LM Studio, wired into Cline; Constrain the stack so offline output has no external dependencies; On-device iPhone inference with MLX Swift; Five-prompt probe battery for tiny multimodal models
- Tools: Qwen 3.5 (0.8B and 2B, GGUF builds), LM Studio, Cline (VS Code extension; transcribed as 'Klein' and 'Climb'), MLX / MLX Swift, Swift / Xcode-style iOS app, Metal GPU, IBM Granite 4.0 nano (mentioned), Llama 2 7B (mentioned as a comparison point), Unsplash (image URLs the model hard-coded), OCRBench (benchmark named), MMLU (benchmark named)

## [The FASTEST Vision Model for Your Laptop (Liquid AI LFM 2.5)](../videos/ZeMuQh9j3dE.md)
`ZeMuQh9j3dE` · Better Stack · 2026-04-02 · q2 · intro · review · also: models-research, voice-multimodal

Better Stack demos Liquid AI's LFM vision-language model running in the browser via WebGPU and ONNX Runtime; real-time webcam captioning works offline once cached, but no benchmarks are measured.

- Techniques: Run a vision-language model in the browser; Native resolution with tiling for large images; Offline verification by disabling the network
- Tools: Liquid AI LFM (Liquid Foundation Model), vision-language variant, 1.6B parameters (title says LFM 2.5), WebGPU (browser GPU API), ONNX Runtime (transcribed as 'onyx runtime', running in the browser), Hugging Face Spaces (demo host)

## [This Open-Source Tool Replaces Ollama + LangChain + Your UI](../videos/pSYEcJTt4t4.md)
`pSYEcJTt4t4` · Better Stack · 2026-04-02 · q3 · intro · review · also: rag-retrieval, dev-tools

Better Stack walkthrough of AnythingLLM, a self-hosted open-source AI workspace that bundles local LLM chat, drag-and-drop RAG, no-code agents and a REST API into one desktop app, with an honest pros/cons take.

- Techniques: Single-app local RAG setup; Citation-grounded codebase Q&A; Visual agent with tool embedding; Swap providers mid-chat; Embed private RAG in other products
- Tools: AnythingLLM, Ollama, LanceDB, pgvector, Qdrant, LangChain, Open WebUI, PrivateGPT, Flowise, Langflow, SERP API, MCP servers

## [The Open-Source Copilot Alternative Devs Are Switching To (Tabby)](../videos/eZ3J45K7gXU.md)
`eZ3J45K7gXU` · Better Stack · 2026-04-02 · q2 · intro · review · also: coding-agents, dev-tools

Walkthrough of Tabby, a self-hosted AI coding server run via Docker and used from a VS Code extension, giving Copilot-style completions and repo-aware chat with code kept on your own machine. Short promotional demo with little exact setup detail.

- Techniques: Run a self-hosted completion and chat server, then point the IDE at it; Use selected-code actions for refactor, perf and tests; Match the model to hardware before judging quality
- Tools: Tabby (self-hosted AI coding server, Docker), VS Code (Tabby extension), Docker, GitHub Copilot, Cursor, Continue (transcribed as 'Continued Dev'), Tab9 (transcript name; likely Tabnine), Mac M4 Pro (hardware used for the demo)

## [Qwen TTS Just Changed Open-Source Voice](../videos/Lw7mrsG58KY.md)
`Lw7mrsG58KY` · Better Stack · 2026-03-02 · q2 · intro · review · also: voice-multimodal

Hands-on test of Qwen3 TTS, an Apache 2.0 open-source voice model that is steered by plain-language emotion and persona instructions and runs fully local; compares it with ElevenLabs, Chatterbox and Vibe Voice.

- Techniques: Voice cloning in the Qwen3 TTS web UI; Emotion and delivery via the instruct box; Persona voice design; Local setup
- Tools: Qwen3 TTS (Alibaba open-source TTS; 1.7B variant and a lighter model, size not stated), Chatterbox (open-source TTS with emotion slider), Vibe Voice (Microsoft, voice cloning), ElevenLabs (commercial TTS)

## [An Open-Source Audio Model From Microsoft That Does Too Much…](../videos/AyHSSslWeHE.md)
`AyHSSslWeHE` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: voice-multimodal, models-research

Hands-on review of Microsoft's open-source VibeVoice speech stack: strong on long-form multi-speaker audio and offline use, weaker on emotion, languages and polish; worth it for local devs, not production.

- Techniques: Long-form multi-speaker generation in one pass; Voice cloning via the Gradio UI; Using structured ASR output (diarization plus timestamps); Incremental streaming for voice agents
- Tools: VibeVoice (Microsoft), Gradio, Hugging Face (demo and model hosting), Chatterbox, ElevenLabs, Whisper, CosyVoice (called Cozy Voice in transcript), Qwen TTS models, macOS Voice Memos

## [Google’s Latest Genie 3 AI Hype Deserves a Closer Look](../videos/mOku8YCtoOc.md)
`mOku8YCtoOc` · Better Stack · 2026-03-02 · q2 · intro · review · also: models-research, inference-serving

Better Stack tests Google's Genie 3 and the open-source LingBot World model, finds them GPU-hungry and gated, and argues infinite world models are not yet practical on consumer hardware.

- Techniques: Lower sample count to cut memory on world-model runs; Single-GPU-per-node launch on one cloud GPU; Use a 4-bit quantized community build to fit one GPU; Feed a generated still image as the scene seed
- Tools: Genie 3 (Google, infinite world model, US-only with Ultra membership), LingBot World (open-source 14B base model, Robbyant/Ant Group, video generation with camera-pose conditioning), LingBot Fast (announced, not released), NVIDIA RTX 5090, NVIDIA H200, RunPod, ComfyUI, Kalen Humphreys 4-bit quantized LingBot World (community build), Sora (cited only as an example of video generators, not used)

## [Qwen 3.5 The FREE AI Model That Claims to Beat Sonnet 4.5](../videos/y8JWZQpWbxQ.md)
`y8JWZQpWbxQ` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: models-research, coding-agents, evals

Better Stack runs three coding tasks (todo app, Three.js solar system, tweet-screenshot feature) comparing Qwen 3.5 35B on OpenRouter against Claude Sonnet 4.5, and finds Sonnet ahead on all three; the takeaway is to run your own evals, not trust benchmarks.

- Techniques: Three-tier hands-on model bake-off; Pin the harness before comparing models; Check the project layout, not only whether the app runs; Check whether a fix targets the root cause; Code-structure review of generated components
- Tools: Qwen 3.5 (medium series, 35B; 400B max-thinking variant mentioned), Claude Sonnet 4.5, Claude Opus 4.5 (benchmark comparison only), Claude Code, Claude Cowork (mentioned), OpenCode, OpenCode Go (model list, mentioned), OpenRouter, superpowers skill (OpenCode), React, Vite, Three.js

## [How Is This Almost as Good as Opus?](../videos/B6P0Fn6xYfo.md)
`B6P0Fn6xYfo` · Better Stack · 2026-03-02 · q2 · intro · review · also: models-research, token-cost-efficiency, coding-agents

A one-prompt Kanban build comparison of open-weight MiniMax M2.5 against Claude Opus 4.6: near-equal results at roughly a tenth of the price, with UI gaps and one missed feature.

- Techniques: Single-prompt head-to-head build eval; Cost-per-task estimate instead of per-token price; Open-weight model as a drop-in cheap tier
- Tools: MiniMax M2.5, Claude Opus 4.6, Cursor, Ollama, Hugging Face, SWE-Bench Verified, Multi-SWE-Bench, Droid benchmark (as named in the video), GPT-5 (comparison only), Gemini 3 Pro (comparison only), MiniMax M2.1 (predecessor, comparison only)

## [How Big Models Fit on Small GPUs (DeepSpeed)](../videos/OM-DJuwweE0.md)
`OM-DJuwweE0` · Better Stack · 2026-02-02 · q3 · intro · tutorial · also: training-finetuning-rl

Better Stack's short tutorial on using Microsoft's DeepSpeed ZeRO stages to fit training workloads into limited GPU memory, run on Colab from a Mac.

- Techniques: Run the DeepSpeed environment check before training; Begin with a ZeRO stage 2 config.json copied from the official docs; Change one config knob per run; Escalate ZeRO stage only when memory still fails; Use a hosted GPU runtime when the local machine has no NVIDIA GPU; Scale to multiple GPUs through Accelerate
- Tools: DeepSpeed, PyTorch, Hugging Face (transformers), Accelerate, Google Colab, CUDA, DSReport (DeepSpeed environment check), ZeRO / ZeRO-Infinity (DeepSpeed features)

## [This Free Whisper App Runs Fully Offline (No Cloud, No API)](../videos/-Z-Clxo-v-g.md)
`-Z-Clxo-v-g` · Better Stack · 2026-02-02 · q2 · intro · review · also: dev-tools

Quick walkthrough of Buzz, a free open-source desktop and CLI app that runs Whisper transcription and translation fully offline, with an honest list of its drawbacks.

- Techniques: Fully offline transcription with Buzz; Word-level timestamps from JSON output; Foreign-language audio to English from the CLI; Scripted batch of transcription scenarios
- Tools: Buzz, OpenAI Whisper, Python, GitHub

## [Olmo3 Is What ‘Open Weights’ Was Supposed to Mean](../videos/iC7dKRe4hCg.md)
`iC7dKRe4hCg` · Better Stack · 2026-01-02 · q2 · intro · review · also: models-research

Short overview of AI2's fully open Olmo 3 and 3.1 models: sizes, the released data and training scripts, OlmoTrace output attribution, and the gaps versus closed models.

- Techniques: Output provenance check with OlmoTrace; Ad hoc two-prompt check of a reasoning variant; Inspect the full training recipe before fine-tuning
- Tools: Olmo 3, Olmo 3.1, Olmo 3 Base, Olmo 3 Think, Olmo 3 Instruct, OlmoTrace, Dolma 3, AI2 Playground, Molmo 2, Qwen3 (transcribed as QEM3/QEN3), Claude Sonnet, OpenAI o1

## [An Open-Source Alternative to ElevenLabs](../videos/chH2tlh_Vvk.md)
`chH2tlh_Vvk` · Better Stack · 2026-01-02 · q3 · intro · review · also: voice-multimodal

Quick hands-on look at Resemble AI's open-source, MIT-licensed Chatterbox Turbo TTS: runs locally, fast enough for agents, with honest drawbacks around overacting and tail artifacts.

- Techniques: Local offline TTS setup; Zero-shot voice cloning from short reference audio; Tune expressiveness with exaggeration, CFG weight and inline tags; Post-process generations to remove tail artifacts; Benchmark on your own hardware before committing
- Tools: Chatterbox Turbo, Chatterbox Multilingual, Chatterbox (original), Python, Torch, conda, Gradio, Hugging Face, MLX audio, Spark TTS, ElevenLabs, Perth watermarking

## [Goodbye AI Cloud Bills... Exo Runs AI on Your Own Devices](../videos/L8468vMTX2s.md)
`L8468vMTX2s` · Better Stack · 2026-01-02 · q2 · intro · review · also: inference-serving, infra-cost-scaling

Short Better Stack overview of EXO, an open-source tool that auto-discovers devices on a LAN and shards one model across them; the demo runs on a single Mac, so the multi-device claims are unverified.

- Techniques: Zero-config LAN cluster for local inference; Shard the model by measured node capacity; Thunderbolt 5 RDMA between Macs
- Tools: EXO (open-source peer-to-peer inference cluster, ExoLabs), Apple MLX, OpenAI-style chat endpoint (served by EXO), Thunderbolt 5 RDMA, DeepSeek V3 671B (cited community run), Qwen3 235B (cited community run), MacBook Pro M4 Pro (demo machine), Mac Studio M3 Ultra (cited benchmark), Mac mini M4 (cited ExoLabs run), Raspberry Pi (CPU node)

## [Tiny AI Is About to Change Everything (IBM Granite 4.0)](../videos/31r6yxbmrFo.md)
`31r6yxbmrFo` · Better Stack · 2025-12-02 · q3 · practitioner · review · also: models-research, inference-serving

Better Stack walkthrough of IBM Granite 4.0 small models (hybrid Mamba-transformer, tiny browser-runnable variants), ending with an offline in-browser code-completion proof of concept.

- Techniques: Browser-only offline completion loop with transformers.js; Completion prompt and generation settings; Debounced suggestion UI with keyboard accept; Raise the token budget in your own agent
- Tools: IBM Granite 4.0, Granite 4 small, Granite 4 1B, Granite Nano 350M, transformers.js, Hugging Face, Mamba, React, MCP-UI, M2 MacBook (hardware used for the demo)

## [Before You Pay for Manus AI, See What This Free Tool Can Do](../videos/S3Q7CCV_PzE.md)
`S3Q7CCV_PzE` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: multi-agent, agent-architecture

Walkthrough of installing and running Agentic Seek, an open-source Manus-style multi-agent tool that runs locally or through a cloud API, with the speaker's hardware and cost caveats.

- Techniques: Install from the README; Switch config.ini from local to API mode; Headless browser and voice options; Start order; Planner plus specialized agents
- Tools: Agentic Seek (version not stated), Manus AI, Docker, Python 3.10, Ollama, Qwen, DeepSeek, GPT-4o, GPT-4o mini, Cursor (editor used for config)

## [Get 400K+ Al Apps on this site...](../videos/jEYHsyiTwso.md)
`jEYHsyiTwso` · AI LABS · 2025-11-02 · q2 · intro · review · also: models-research

A five-minute tour of Hugging Face Spaces: a public directory of 400K+ community AI apps and hosted open models, shown through logo placement, image-to-3D, image extension and comic generation demos.

- Techniques: Discover demo apps via the Spaces directory; Try an open model through its hosted demo before running it locally; Publish a project as a Space to share a demo
- Tools: Hugging Face Spaces, Flux (Flux Dev), Trellis, Janus Pro 7B, Qwen 2.5 Max, Midjourney, o3 mini (attributed to ChatGPT), AI Comic Factory, Neural Jam, Blender (mentioned as the target for GLB export), GLB (3D file format)

## [OpenAI FINALLY Goes Open... 2 NEW models (they're good?)](../videos/hIgQ_0VMj_4.md)
`hIgQ_0VMj_4` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: models-research, coding-agents

Hands-on test of OpenAI's open-weight gpt-oss-120b and gpt-oss-20b: the 20B runs locally on a MacBook, the 120B runs via OpenRouter, and coding results are mixed against OpenAI's self-reported benchmarks.

- Techniques: Run gpt-oss-20b locally for offline use; Route the 120B model through OpenRouter inside OpenCode; Scope the prompt to what the model can finish; Use a fixed single-file stress prompt for quick model comparisons
- Tools: gpt-oss-120b, gpt-oss-20b, Ollama (auto-caption 'Alarma'), OpenRouter, OpenCode, Next.js, tRPC, Tailwind CSS, Claude Code, Claude Sonnet 4 (auto-caption 'Claude Sonic 4'), o3, o3-mini

## [NEW Qwen 2.5 Coder (32B): Insane Coding Power Tested! Is This the Best Free LLM?](../videos/4shPVb4RqGQ.md)
`4shPVb4RqGQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: models-research, evals

Informal hands-on test of Qwen 2.5 Coder (32B) against five coding prompts via the hosted demo; it passed three and failed two, and the presenter says to test it yourself before switching from Claude.

- Techniques: Fixed pass/fail prompt set for a quick coder-model smoke test; Trying an open coder model locally with Ollama; Testing in a hosted artifacts sandbox
- Tools: Qwen 2.5 Coder (32B and 7B), Qwen 2.5, Claude 3.5 Sonnet, GPT-4 Omni (GPT-4o), Cursor, Open WebUI, Ollama, Hugging Face (demo space and artifacts), Notion (test list)

## [Build an AI Video Generator Like Sora (with ComfyUI)](../videos/DxvC2B0eVkc.md)
`DxvC2B0eVkc` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: voice-multimodal, dev-tools

Step-by-step tutorial for running ComfyUI on a rented DigitalOcean GPU droplet, chaining an OmniGen2 text-to-image workflow into a WAN video workflow, and serving the export through ViewComfy over SSH tunnels.

- Techniques: Remote GPU with SSH-tunneled ComfyUI; Downloading models into the path the workflow expects; Chain text-to-image into image-to-video; Shared prompt node across two text encoders; Export ComfyUI workflow as API JSON and run it in ViewComfy; Cost control for rented GPU droplets
- Tools: ComfyUI, comfy-cli, DigitalOcean GPU Droplets, NVIDIA RTX 4000 Ada, WAN video generation model (speaker says 2.25B parameters, auto-caption), OmniGen2, ViewComfy, Next.js, pip3, SSH

## [This Tiny 1-Bit Model Could Change AI Forever](../videos/DmBBQh5UPwQ.md)
`DmBBQh5UPwQ` · Better Stack · 2025-11-02 · q2 · intro · review · also: inference-serving, models-research

Better Stack hands-on test of Microsoft's BitNet, a 1.58-bit ternary-weight LLM, on a laptop CPU: passes simple logic prompts, fails a coding task badly.

- Techniques: Run BitNet via the Hugging Face model card (transformers) instead of bitnet.cpp; Small-set logic benchmark for a local model; Iterative coding stress test with fix-up prompts
- Tools: BitNet (Microsoft 1-bit LLM), bitnet.cpp, Hugging Face transformers, Hugging Face model card and demo page, Nemotron (NVIDIA; prior video comparison), MacBook Pro M2, LLM logic test spreadsheet (public)

## [NVIDIA Quietly Dropped This POWERFUL AI Model (Nemotron v2)](../videos/8M5IHvDSZXs.md)
`8M5IHvDSZXs` · Better Stack · 2025-11-02 · q2 · intro · review · also: inference-serving, models-research

Better Stack's hands-on look at NVIDIA's 9B Nemotron Nano v2: a hybrid Mamba-2/attention model, a reasoning-budget cap, mixed logic and coding results, and a RunPod + vLLM deployment.

- Techniques: Serve a Hugging Face model on a RunPod vLLM pod; Chat UI on top of a vLLM endpoint; Cap thinking with a reasoning budget client; Quick logic regression prompts
- Tools: NVIDIA Nemotron Nano v2 (9B), Mamba-2, vLLM, RunPod, Hugging Face, Ollama, Next.js vLLM UI, NVIDIA chatbot (free web demo), Llama 3, Qwen 3, Claude Code (mentioned for comparison only), Docker

## [Take Back Your PRIVACY and Run DeepSeek on EC2 in 5 Minutes!](../videos/DCWtyd9AW4w.md)
`DCWtyd9AW4w` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: infra-cost-scaling, dev-tools

Step-by-step tutorial for running distilled DeepSeek (Qwen-based) models on a CPU-only AWS EC2 instance using Ollama, Open WebUI in Docker, and an Nginx reverse proxy, framed around keeping prompts private.

- Techniques: Run Ollama in Docker with a persistent volume and a published port; Open WebUI as a front end for a Docker-hosted Ollama; Nginx reverse proxy from port 80 to a local app port; Pick a quantization level by tradeoff
- Tools: AWS EC2, Amazon Linux, Docker, Ollama, Open WebUI, Nginx, Caddy (mentioned, not used), DeepSeek (distilled models, Qwen-based per the speaker), Qwen (distilled base for the 1.5B and 7B models), vim / nano

## [Why WebGPU + Transformers.js is a Game Changer](../videos/NLQ_gVcjHHA.md)
`NLQ_gVcjHHA` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: inference-serving

Short Better Stack tutorial on running small LLMs fully in the browser with Transformers.js and WebGPU, with a Hugging Face model, quantized weights, offline caching, and worker/streaming fixes for UI freezes.

- Techniques: Pick a small quantized model from the Hugging Face Hub for in-browser inference; Set quantization and generation limits on the Transformers.js pipeline; Keep the UI responsive by running generation in a Web Worker; Serve and iterate on the browser demo with Bun; Inspect where the model is cached
- Tools: Transformers.js, WebGPU, ONNX Runtime Web (spoken as 'Onyx Web Runtime'), Hugging Face Hub, Bun, Node.js, Llama 3.2, SmolLM2 (spoken as 'small lm2', probably), DINOv3 (spoken as 'Dino version 3', unverified), StarCoder, Claude Sonnet, Ollama

## [Phi-4: The Smallest Open Source AI Model](../videos/yzSYIndCWD8.md)
`yzSYIndCWD8` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, vibe-coding-app-building

Single-run hands-on test of Phi-4 (14B, MIT license) through Ollama, bolt.diy and Cline. It runs locally, but it failed to integrate a React component, which the speaker blames on the context window.

- Techniques: Local model via Ollama; OpenRouter key as a hosted fallback; bolt.diy from source; Point Cline at local Ollama; Frontier model writes, local model integrates; Shrink the task when the agent stalls
- Tools: Phi-4 (Microsoft, 14B open weights, MIT license; captioned as "5.4"), Ollama, OpenRouter, bolt.diy (captioned "BoltDIY" and "bold.diy"), Cline (captioned "Klein"; formerly Claude Dev), Claude (used to write the card component), VS Code, pnpm, Next.js 14, React, TypeScript, Tailwind CSS

## [Gemma3n - The Most OVERHYPED AI Model of 2025 (For Coding)](../videos/FCl6ZR8l_EM.md)
`FCl6ZR8l_EM` · Better Stack · 2025-11-02 · q2 · intro · review · also: models-research, coding-agents

Better Stack gives Gemma 3n, Llama 4 and DeepSeek R1 three browser coding prompts. Gemma 3n finishes last, and the speaker concludes open models aren't ready for complex coding.

- Techniques: Feed errors back for a fix; Switch language when a generated graphic does not render; Give the model the CDN link for a 3D library; Same-prompt, multi-attempt model bake-off
- Tools: Gemma 3n, Llama 4, DeepSeek R1, DeepSeek, Ollama, Three.js, Python, JavaScript, Claude 3.7 (comparison reference)

## [Can AI Agents Finally Automate the Web? (BrowserOS Review)](../videos/rIZ8OBHL7Zo.md)
`rIZ8OBHL7Zo` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: voice-multimodal, dev-tools

Better Stack reviews BrowserOS, an open-source Chromium-based agentic browser; the built-in agent works on Gemini, but local Ollama models mostly failed the Amazon cart task.

- Techniques: Run BrowserOS's agent on a local Ollama model; Evaluate candidate models on a browser-agent task before relying on them; Customize an agent's instructions by rebuilding from source
- Tools: BrowserOS, Chromium, Chrome, Perplexity Comet, Opera Neon, Fellow AI, OpenAI Operator, Brave, Arc, Dia, Ollama, Gemini 2.5

## [DeepSeek Releases ANOTHER Model - Janus Pro (image gen + multi-modal)](../videos/UkruXt_ZOkE.md)
`UkruXt_ZOkE` · Better Stack · 2025-11-02 · q3 · intro · review · also: models-research

Hands-on tour of DeepSeek's open Janus Pro multimodal model (image understanding and text-to-image), with its benchmark claims, training cost, and the 384px input limit that caps its OCR.

- Techniques: Round-trip check for image-to-code output; Quick multimodal smoke test set; Check the input resolution before relying on OCR
- Tools: Janus Pro (7B; 1.3B/1.5B variants mentioned), DeepSeek, Hugging Face (model download and hosted demo), DALL-E 3 (comparison), Stable Diffusion XL (benchmark comparison), Flux (quality comparison)

## [Google I/O in 6 Minutes (Developer Focused)](../videos/Da275bLi_-4.md)
`Da275bLi_-4` · Better Stack · 2025-11-02 · q2 · intro · news · also: coding-agents, models-research, mcp-and-tools

A 6-minute developer-focused roundup of Google I/O 2025 announcements: Jules, Gemini Code Assist, Stitch, Colab, Gemini Diffusion, 2.5 Pro/Flash API features, Gemma 3N, Chrome AI APIs and Android agents.

- Techniques: Async function calling for long-running tools; URL context instead of search for known pages; Thinking budgets for cost control on 2.5 Pro; Sketch or wireframe to UI to code loop (Stitch)
- Tools: Jules, Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, Gemini Code Assist, VS Code, JetBrains IDEs, Stitch, Figma, Google Colab, Gemini Diffusion, DeepThink

## [Llama 4 Has a 10M Token Context Window... (and its the best)](../videos/xCxuNE2wMPA.md)
`xCxuNE2wMPA` · Better Stack · 2025-11-02 · q2 · intro · news · also: models-research, context-engineering

Better Stack recap of Meta's Llama 4 launch: open-weight Scout and Maverick (MoE, 17B active) with a claimed 10M-token context, plus the unreleased Behemoth teacher model. All benchmark and efficiency claims are Meta's, repeated without independent checks.

- Techniques: Teacher-to-student distillation for deployable models; Sparse mixture-of-experts for cheaper inference; Three-stage post-training recipe
- Tools: Llama 4 Scout, Llama 4 Maverick, Llama 4 Behemoth, Llama.com, Hugging Face, OpenRouter, Groq (transcript says 'Grok'), LM Arena, GPT-4.5, Claude Sonnet 3.7, Gemini 2.0 Pro, Gemma 3

## [Your Own Mini AWS in Under 30 Minutes (Incus Tutorial)](../videos/zaAtYkM24hU.md)
`zaAtYkM24hU` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools, sandboxing-execution

Better Stack walkthrough of installing Incus (a community fork of LXD) on Ubuntu to run system containers and VMs, host Ollama in a container, and set up per-customer projects with quotas.

- Techniques: Install Incus from the signed apt repo; Initialize Incus and launch a container; Launch a VM with the same command; Add a bridge network so containers can reach the internet; Run Ollama as a service in a container; Create per-tenant projects with resource limits
- Tools: Incus (version not stated), LXD (upstream fork origin), LXC (container layer), QEMU (VM layer), Ubuntu (server image and host OS), Ollama, orca-mini (small test LLM), Zabbly apt repo (Incus package source), apt, gpg, curl

