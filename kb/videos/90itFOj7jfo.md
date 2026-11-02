# This Open-Source Engine Claims 2x Faster Than llama.cpp

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `90itFOj7jfo` · [watch](https://youtu.be/90itFOj7jfo) · **date:** 2026-10-12 · **length:** 8:01 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Josh · **orgs:** Better Stack, Magnitude, NVIDIA
- **topics:** local-ai, inference-serving, coding-agents · **tags:** magnitude, llama.cpp, mlx, ollama, local inference, kernel autotuning, kv cache compression, prefill vs decode, claude code, apple silicon, benchmarks, open-weight models

> Hands-on test of Magnitude, a new Rust inference engine for Apple Silicon that tunes kernels per machine and targets agent workloads; the "2x llama.cpp" claim holds for one decode config but is mixed in independent tests.

## Summary
Better Stack's Josh tests Magnitude, a new open-source local inference engine (v0.2.5, Rust, on a compiler it calls Seismic) that claims up to 2x llama.cpp decode speed on Mac. Its main idea is per-machine tuning: on first model download it times different kernel configurations on the user's hardware, keeps the fastest, and caches it, which takes about a minute. It also exposes OpenAI- and Anthropic-compatible endpoints on localhost, with a one-click connect to Claude Code, Codex and OpenCode, and adds agent-oriented features: shared prompt caches across sessions, a compressed KV cache by default, and load-on-demand with unload when idle. The headline 2x comes from one benchmark (Qwen 3.6 35B A3B at 4-bit, 64K context, M4 Pro): decode went from 30 to 57 tok/s while prefill was only 9% faster, and llama.cpp ran a full 16-bit KV cache because its compressed path broke in that test. Independent results are mixed: one M5 Max run had Magnitude at 161 tok/s against RapidMLX's 175, and others found llama.cpp 20-30% faster or twice as fast; the founder attributes part of this to Magnitude not yet using the M5's Metal matrix units. The author's verdict is that it is useful for M1-M4 owners running local coding agents, mainly for the connect flow, and should not be used for production until more independent MLX comparisons appear. Caveats: macOS 13+, Intel Macs CPU-only, under 4-bit models not supported, few curated models (about 15), no documented way to load your own GGUF, and models left behind in a hidden folder after uninstall.

## Key ideas
- **Magnitude tunes kernels for the specific machine instead of shipping one precompiled kernel set** — Engines like llama.cpp and Ollama ship precompiled kernels for portability. Magnitude tries different kernel configuration knobs on the user's hardware when a model is downloaded, times them, and caches the fastest setup per device. The tuning takes about a minute. ([0:00](https://youtu.be/90itFOj7jfo?t=0))
- **Decode speed, not prefill, is what a coding agent feels** — Prefill is how fast the prompt is read; decode is generation one token at a time. The speaker says that while watching a coding agent work, decode is the number you actually notice. ([1:05](https://youtu.be/90itFOj7jfo?t=65))
- **Local OpenAI- and Anthropic-compatible endpoints make it a drop-in backend for coding agents** — Magnitude serves both APIs on localhost. A connect button configures Claude Code, Codex, OpenCode and others, after which Claude Code is restarted and talks to the local model. The speaker calls this the strongest reason to install it. ([2:09](https://youtu.be/90itFOj7jfo?t=129))
- **Agent-specific optimizations sit on top of the engine** — Several agent sessions can share prompt caches, memory grows and shrinks as needed, the KV cache is compressed, and models load on demand and unload when idle. The engine is positioned between llama.cpp/Ollama (portable, slower), vLLM/SGLang (data-center batching) and MLX (fast but Apple-only). ([3:33](https://youtu.be/90itFOj7jfo?t=213))
- **The 2x headline is narrow and the comparison was not like-for-like** — On an M4 Pro with 48 GB, Qwen 3.6 35B A3B at 4-bit with 64K context: decode rose from 30 to 57 tok/s, but prefill was only 9% faster. On an NVIDIA DGX Spark decode improved 19%. llama.cpp ran a full 16-bit KV cache because its compressed path broke in that run, while Magnitude compresses by default. ([4:31](https://youtu.be/90itFOj7jfo?t=271))
- **Independent benchmarks contradict the 2x claim on some hardware** — On an M5 Max, RapidMLX reached 175 tok/s versus Magnitude's 161. Other users measured llama.cpp at about 2x Magnitude on an M5 Max and an RTX 5070 Ti, or 20-30% faster. The founder says Magnitude does not yet use the M5's Metal matrix hardware and an official MLX comparison is coming. ([5:34](https://youtu.be/90itFOj7jfo?t=334))
- **The project is very early** — Version 0.2.5, five releases in about four days, and the engine was rewritten in September. The model library has about 15 curated models, nothing below 4-bit, and no documented way to load your own GGUF. ([5:34](https://youtu.be/90itFOj7jfo?t=334))
- **Practical operational caveats** — Requires macOS 13 or newer; Intel Macs run CPU-only. Downloaded models live in a hidden folder in the home directory and survive uninstall. An idle model takes a while to reload on its first response. ([6:34](https://youtu.be/90itFOj7jfo?t=394))

## Techniques
- **Benchmark decode and prefill separately, and match KV-cache precision** — Report prefill tok/s and decode tok/s as separate numbers. Before comparing engines, confirm both use the same KV cache precision (16-bit versus compressed). The speaker's test pasted Moby Dick into context up to 64K tokens and asked the model to repeat the final section. *When:* Any local-engine comparison. A single headline multiplier can hide a small prefill gain and a context-dependent decode gain.
- **Per-device kernel autotuning, cached per machine** — On first model download, run several kernel configurations on the local hardware, time each, keep the fastest, and cache the choice keyed to the device so later loads skip the search. The tuning step takes about one minute. *When:* A fixed fleet or single workstation where the one-time cost is amortized and portable precompiled kernels leave performance on the table.
- **Point Claude Code at a local Anthropic-compatible endpoint** — Run a local engine that exposes an Anthropic-compatible API on localhost, use its connect option (or set Claude Code's API base URL to that localhost endpoint), and restart Claude Code. The video does not show the exact environment variable or config key. *When:* Running coding-agent sessions against a local open-weight model with no cloud spend, or for offline experiments.
- **Agent-serving cache and memory policy** — Let concurrent agent sessions share a prompt cache, compress the KV cache by default, grow and shrink memory on demand, and unload a model after it has been idle. Expect a slow first response after an idle unload. *When:* Long-running or multi-session agent workloads on a single machine, where repeated system prompts and idle-model memory dominate.

## Numbers
- Kernel tuning on first download takes about 1 minute ([1:05](https://youtu.be/90itFOj7jfo?t=65))
- Qwen 3.6 35B A3B 4-bit, 64K context, M4 Pro 48 GB: decode 30 -> 57 tok/s (+92%) vs llama.cpp ([4:31](https://youtu.be/90itFOj7jfo?t=271))
- Same test: prefill only about 9% faster ([4:31](https://youtu.be/90itFOj7jfo?t=271))
- Same test on NVIDIA DGX Spark: decode improvement 19% ([4:31](https://youtu.be/90itFOj7jfo?t=271))
- M5 Max independent run: RapidMLX 175 tok/s vs Magnitude 161 tok/s ([5:34](https://youtu.be/90itFOj7jfo?t=334))
- Another user measured llama.cpp about 20-30% faster; others found llama.cpp about 2x Magnitude on M5 Max and RTX 5070 Ti ([5:34](https://youtu.be/90itFOj7jfo?t=334))
- Magnitude v0.2.5, five releases in about four days, engine rewritten in September, about 15 curated models, nothing below 4-bit ([5:34](https://youtu.be/90itFOj7jfo?t=334))

## Hot takes
- The 2x headline rests on one configuration in which llama.cpp was not using its compressed KV cache, so the comparison is not like-for-like.
- The connect-to-Claude-Code button may be the strongest reason to install Magnitude, more than its raw speed.
- On M5 hardware, stay on MLX for raw tokens per second; wait for independent MLX comparisons before any production use.

## Tools mentioned
Magnitude (v0.2.5), llama.cpp, MLX, Ollama, Qwen 3.5 4B (Q8), Qwen 3.6 35B A3B (4-bit), Seismic (numerical compiler), Claude Code, Codex, OpenCode, RapidMLX, vLLM, SGLang, NVIDIA DGX Spark, RTX 5070 Ti, M5 Max, M4 Pro, GGUF

## Relevance to our work
- **agentos** (1/3): L2B InferCraft plans pluggable KV-cache strategies on a single RTX 5090; this video's compressed-KV-by-default and cross-session prompt-cache sharing are comparison points, and its decode-vs-prefill and cache-precision caveats apply to any benchmark we run. → *When benchmarking InferCraft KV strategies, report prefill and decode separately and pin KV precision in every baseline, as the video's 2x comparison did not.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI; pointing Claude Code at a local Anthropic-compatible endpoint could support offline or zero-token test runs of checkpoint/resume flows. → *Try running a ProsHarness checkpoint/resume test with Claude Code pointed at a local model endpoint, and check the resume path.*
