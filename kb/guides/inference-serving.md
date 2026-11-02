# Guide: inference-serving

*Synthesized by Sonnet from 79 talks since 2026-05-18.*

Scope: model serving, KV cache, speculative decoding, quantization, GPUs, latency. Notes come from talk summaries. Many speakers are vendors, so numbers are often self-reported.

## State of the art (what practitioners actually do now — most recent talks weigh most)

**The unit of work is now the agent task, not the request.** Agent traffic has long prompts, short outputs and many turns. Sessions run from a few turns to about 3,000. Cache hit rates often pass 90% because system prompts and tool definitions repeat (`YXowceUKYJI`). Teams now measure cost per successful task, including retries and failures (`7c9FSUVcXR0`), and latency per finished task (`Hvb2LfMH58c`).

**The serving stack has a standard shape.**
- Engine: vLLM or SGLang with continuous batching and paged KV cache (`4n08JHb90hI`, `_cRgl3maiT8`).
- Routing above the engine: KV-cache-aware routing. Score each replica on queue depth, KV use and prefix-hit chance. Keep a session on one pod (`YXowceUKYJI`, `cQQbJqvZkpo`, `TRe1u7dHYiA`).
- KV tiers: hot KV in GPU memory, warm in CPU RAM, cold on NVMe or disk (`_naLJOqVOEI`, `cQQbJqvZkpo`).
- Prefill/decode (PD) disaggregation: used, but called a trade-off, not a default (`YXowceUKYJI`, `cQQbJqvZkpo`).

**Prefill is compute-bound and decode is memory-bound.** Almost every talk starts here. It sets the two metrics: time to first token (TTFT) and inter-token latency (`woIYJYd_etI`, `y2W4FNAuPEA`, `ESbWpPT_9-o`). Capacity math starts from KV bytes per token (`y2W4FNAuPEA`, `4n08JHb90hI`).

**Speculative decoding is mainstream but workload-dependent.**
- EAGLE-style drafting is the baseline. DFlash (block drafting by a diffusion model) beat EAGLE-3 in one Baseten measurement (`75ckHC2LU_0`).
- Training the draft on your own live traffic is the most actionable production tip (`75ckHC2LU_0`, `TRe1u7dHYiA`, `13YZ1EB9hjU`).
- It needs spare GPU memory. Acceptance rate depends on the workload, so measure it per workload (`XTpyNrEgJQ4`).

**Quantization: per-layer and verified.**
- Weights go to NVFP4 or similar. Do not quantize every layer the same way (`J4_jCrTxMkk`).
- TurboQuant (4-bit KV) lost on data-center throughput. It may suit memory-bound local setups (`75ckHC2LU_0`).
- Judge a quant by KL divergence against the BF16 model, then test it in the real agent harness (`J4_jCrTxMkk`).

**Routing between models is also routing between engines.** A frontier model plans and a cheaper model executes. The hard parts are noticing when the cheap model is out of depth and keeping caches warm (`QHBjufYK8TA`, `TeGsFFNqRLA`, `KB41dTlX1Uc`).

**Reliability work looks like normal distributed systems.** Control-plane/data-plane split, outlier penalties, utilization-aware retry budgets, load shedding (`sOB3HSiG8vo`, `7c9FSUVcXR0`). Per-route P99 and hedged requests at about P90 (`zrZ1amZBSPw`).

**Local and edge inference is a real track.** Gemma 4 on phones, MLX on iPhone, fine-tuned tiny models for fixed function calls (`a2muGkT4WD4`, `hacEQHHhu2Q`, `-TiET_K-E_g`, `BKWpYIWvAo4`). Memory (DRAM), not compute, is the main constraint (`hacEQHHhu2Q`).

## Consensus patterns (numbered; each cites videos as `video_id`)

1. **Split metrics by phase.** Track TTFT (prefill-bound) and inter-token latency (decode-bound) separately. Also log prefix-reuse rate and QPS per replica. (`woIYJYd_etI`, `y2W4FNAuPEA`, `4n08JHb90hI`)
2. **Plan KV capacity before picking hardware.** KV bytes per token = 2 x head_dim x layers x KV heads x bytes. Max users = KV budget / (bytes per token x context). (`y2W4FNAuPEA`, `4n08JHb90hI`)
3. **Route by cache locality, with a load fallback.** Random or round-robin balancing wastes cached prefixes. Keep a task on one replica. (`YXowceUKYJI`, `Hvb2LfMH58c`, `cQQbJqvZkpo`, `TRe1u7dHYiA`, `_naLJOqVOEI`)
4. **Treat KV as a memory hierarchy.** Offload idle sessions to CPU or storage and reload, instead of evicting and paying prefill again. Pin active sessions. (`cQQbJqvZkpo`, `_naLJOqVOEI`, `YXowceUKYJI`)
5. **Disaggregate prefill and decode only when it fits.** It needs a fast fabric (RDMA/RoCE). It suits long context, large models and middle concurrency. (`YXowceUKYJI`, `cQQbJqvZkpo`, `ESbWpPT_9-o`)
6. **Measure speculation per workload.** Compare acceptance rate and tokens/s against a baseline. Use a draft 10 to 50 times smaller with the same tokenizer. Retrain the draft when the target changes. (`XTpyNrEgJQ4`, `75ckHC2LU_0`, `woIYJYd_etI`)
7. **Quantize per layer and check against the unquantized model.** Keep sensitive layers (first/last, QKV, linear-attention projections) at higher precision. Use KL divergence, then harness tests. (`J4_jCrTxMkk`)
8. **Size to the knee and the tail, not the average.** Sweep concurrency, pick the point before throughput flattens and latency jumps. Use P90/P99. (`4n08JHb90hI`, `g4SsanB0gMc`, `YXowceUKYJI`, `zrZ1amZBSPw`)
9. **Validate the benchmark client first.** Report achieved QPS beside requested QPS. Fix temperature and dataset sampling. (`l1-D89bAuOA`)
10. **Protect the fleet from cascades.** Shed load by queue depth. Cap retries with a budget that tightens as utilization rises. Lower an outlier's weight instead of dropping it. (`sOB3HSiG8vo`, `7c9FSUVcXR0`, `zrZ1amZBSPw`)
11. **Keep host work off the GPU critical path.** Capture CUDA graphs, fuse tiny kernels, find host syncs. (`woIYJYd_etI`, `ESbWpPT_9-o`, `c1hGBoWw20A`, `0jeZfjJMfmo`)
12. **Plan with a big model, execute with a fast or cheap one.** Verify every step because verification is cheap at high speed. (`TeGsFFNqRLA`, `QHBjufYK8TA`, `KB41dTlX1Uc`, `SS-A8sE7hkw`)
13. **Rent to learn, own to earn.** Self-host when usage is steady and high, or data rules require it. (`Bck7ABCZRZI`, `4n08JHb90hI`)
14. **Voice and video need first-chunk latency.** Stream audio, measure time to first audio from end of user speech. (`3jGAU2sbAyY`, `vblnYHzBgS4`, `0jeZfjJMfmo`)
15. **For small models, search for the smallest model that passes.** Fine-tune on synthetic data for narrow tasks. (`hacEQHHhu2Q`, `-TiET_K-E_g`, `fWXJM-J0ZB8`)

## Disagreements & open questions

- **Is PD disaggregation worth it?** Red Hat shows strong inter-token gains, but warns it needs RDMA and a middle load range (`YXowceUKYJI`). CoreWeave says it is not cheap enough for every workload and keeps it optional (`cQQbJqvZkpo`). Baseten lists it among future bets (`75ckHC2LU_0`).
- **Router design.** OpenAI replaced a feedback-loop weight controller because it oscillated and hurt cache locality (`sOB3HSiG8vo`). Superlinked argues for a centralized pull queue for many small requests, which they say doubles throughput (`g4SsanB0gMc`). A later Superlinked talk found per-worker batching beat one shared queue in their tests (`Ndp5VaqFrl0`). These two claims conflict and neither has published methodology.
- **KV compression.** TurboQuant halves memory but cut throughput by over half in data-center use (`75ckHC2LU_0`). Learned compaction is promising but early (`75ckHC2LU_0`).
- **Task-type routing for agents.** Panelists call it fragile and want a frontier watcher plus escalation (`QHBjufYK8TA`). Callosum pitches fully automated model and hardware routing (`WRBNDpUhsJQ`).
- **Same weights, different provider.** Vendors claim big speed gaps (`_naLJOqVOEI`, `Hvb2LfMH58c`). All are vendor-sourced single examples. Nobody shows an independent bake-off.
- **Trust in public numbers.** Leaderboards are thin and metrics need validation (`hqHC6Z_lXyo`). Serving benchmarks can blame the server for client faults (`l1-D89bAuOA`). Vendor speedups (`7BcQdtRA3Tc`) are best treated as claims to reproduce.
- **Multi-tenant GPU safety.** Timing probes on a shared H100 can fingerprint a neighbor's model depth. Open question: how much isolation is enough (`SacJfmp33vM`).

## How thinking changed over time (dated)

- **2026-05-18.** Edge and small-model focus. Gemma 4, LiteRT, MLX. Questions are about memory fit and quantization level (4 to 8 bit) (`Lm8BLHkxiAo`, `a2muGkT4WD4`, `_A367W_qvc8`). Superlinked argues small models need their own shared-GPU layer (`qdh_x-uRs9g`).
- **2026-06-18.** Speed becomes the topic. Fast coding models change developer habits (`TeGsFFNqRLA`). Decode is framed as memory-bound with kernel-launch waste (`ESbWpPT_9-o`). Diffusion serving borrows ideas: quantize, cache steps, distill (`gHs5ZiY80PM`). Serverless GPU cold starts show up in p95 (`ILdE7FaAjVA`).
- **2026-08-18.** Open-weight models treated as production-ready. Focus shifts to compression recipes (`J4_jCrTxMkk`), day-zero kernel work with the model maker (`AVMr9PMINyo`), and routing across models (`QHBjufYK8TA`). Cost and ownership arguments grow (`Bck7ABCZRZI`, `FWMJQDH3iK0`).
- **2026-09-18 to 09-20.** Peak of "inference is distributed systems." KV-aware routing, PD disaggregation, control planes, retry budgets, and cost per task (`YXowceUKYJI`, `sOB3HSiG8vo`, `7c9FSUVcXR0`, `zrZ1amZBSPw`). Benchmark validity gets its own talk (`l1-D89bAuOA`). Speculation moves to learned drafts and block drafting (`75ckHC2LU_0`).
- **2026-10-04 to 10-14.** Engine internals and hands-on tuning. What an engine is (`woIYJYd_etI`), when speculation pays (`XTpyNrEgJQ4`), self-hosting on one GPU (`4n08JHb90hI`). Same provider claims repeat across vendors (`TRe1u7dHYiA`, `_naLJOqVOEI`). Security of shared GPUs appears (`SacJfmp33vM`).

## Numbers worth remembering (with `video_id`)

- Cached tokens are about 10x cheaper than uncached (cited from API pricing). Agent cache hit rates often exceed 90%. (`YXowceUKYJI`)
- Prefix routing cut TTFT from about 3 s to about 1 s on cache hits. In one GPT-OSS 120B multi-turn test, P99 inter-token latency was about 100 ms with PD versus about 900 ms aggregated. (`YXowceUKYJI`)
- Agentic inputs are 80 to 90% shared across requests. (`cQQbJqvZkpo`) Another source says 50 to 90%. (`_naLJOqVOEI`)
- Calls per task: 1 for chatbots, 10 to 20 for copilots, about 50 for research agents. Request sizes run from about 50 to 100,000 tokens. (`7c9FSUVcXR0`)
- A benchmark client asked for 200 QPS and delivered 38. Client-side lag looked like 58 s of server latency. Temperature 0 raised a throughput claim by about 20%. (`l1-D89bAuOA`)
- Router and reasoning request latency for one prompt ranged from about 2 s to 60 s. Embeddings and classification are under 1 s, chat about 3 s. (`zrZ1amZBSPw`)
- Small-request fleets with vLLM/SGLang routers sat at 20 to 30% GPU utilization. A central pull queue roughly doubled throughput. (`g4SsanB0gMc`)
- TurboQuant: KV memory halved, tokens/s cut by more than half. DFlash: over 3x versus EAGLE on one B200 with an 8B-class model (speaker's own measure). Retrained speculators gave 20% to 2x acceptance gains. (`75ckHC2LU_0`)
- Draft-model speculation: 3 to 5 tokens per cycle, draft 10 to 50x smaller, demo 16 GB target and 2.5 GB draft. (`XTpyNrEgJQ4`)
- Single RTX 4000 Ada, Qwen3 4B BF16: TTFT about 37 ms, decode 40 to 45 tok/s, KV pool about 37,000 tokens. (`4n08JHb90hI`)
- Unsloth dynamic 1 to 2 bit quant recovers about 76% of accuracy. GLM 5.2 shrinks from about 1.5 TB to about 250 GB. (`J4_jCrTxMkk`)
- Qwen 3.5 on Apple Silicon ran 50% below theoretical speed. Fusing kernels gave about 30% faster. 150 tok/s means under 10 ms per token. (`ESbWpPT_9-o`)
- H100: about 1 petaflop/s compute but about 3 TB/s memory bandwidth. (`JomVvNDjGb8`)
- Hardware and memory movement are 50 to 80% of inference latency (speaker figure). Codex Spark about 1,200 tok/s versus 40 to 60 for Sonnet/Opus. (`TeGsFFNqRLA`)
- Voice: target time-to-first-audio under about 550 ms, real deployments 750 ms to 1.2 s, users hang up above 1.2 s. Frontier P50 TTFT is 450 to 500 ms but P95 passes 1.2 s. (`vblnYHzBgS4`)
- Short-message P99 round trip: TCP above 1 ms versus Homa under 100 microseconds. (`eZ8WWZzoaR0`)
- MiniMax M3 sparse attention: prefill about 9x and decode about 15x faster than full attention at 1M context. (`htod7Nv1cBc`)
- Diffusion step distillation: about 50 steps to 4 or 8. The 10x to 200x claim has no benchmark. (`gHs5ZiY80PM`)
- Autoresearch on kernels: about 3x speedup, about 80% of attempts are bad, bare metal gave about 25% over virtualized cloud. (`vrDvatGtIxs`)
- Node failure remediation: about 5 min to a healthy node, under 15 min end to end. (`bRGyYaE0lxI`)
- Edge: Gemma E2B text weights about 841 MB at about 2.9 bits per weight, about 2 GB active RAM. (`hacEQHHhu2Q`) Gemma 4 4-bit at about 40 tok/s on a current iPhone. (`a2muGkT4WD4`)

## From creator channels (Kai Explains, AI LABS, Better Stack)

Evidence base: 42 creator videos in this category's notes (41 Kai Explains, 1 Better Stack). No AI LABS video is in this category. Most creator claims come from one video, focus on consumer hardware (Macs, 16 GB GPUs, free tiers) and are self-measured or secondhand. Treat their numbers as illustrative.

### Practical playbook

1. **Time enter-to-first-token apart from the tokens/s counter.** The counter shows only decode. One M1 Max test showed a 57 tok/s counter but about 3 tok/s to the first word with 8,500 tokens of context. Measure prefill as prompt tokens divided by prefill tok/s. (`x_qmqqp6d7s`, `i9mRnbdDYxk`)
2. **Audit cache-token counts on every turn.** Zero cached tokens deep into a session means every turn is a full miss. Keep volatile values out of the top of the system prompt, and do not rewrite or strip earlier history. (`x_qmqqp6d7s`, single video)
3. **Find cache misses in the server log.** Raise llama.cpp or LM Studio log verbosity to level 4 (default 3), run a session, and search for the full prompt reprocessing line. If it appears every turn, the cache misses every turn. (`x_qmqqp6d7s`, single video)
4. **Check Ollama's context window.** Run `ollama ps` and read the context column. The speaker says a 48 GB Mac gets a 32k default, and Claude Code's first request (about 33k tokens) fills it. The config key is not shown, so check Ollama's docs. (`x_qmqqp6d7s`)
5. **Budget VRAM before loading a model.** Usable VRAM, minus about 1 GB runtime margin, minus weights, MTP head and vision projector, divided by KV bytes per token (about 64 KB for Qwen 27B, 160 KB for Devstral Small 2). On a 16 GB card with an 11.8 GB model this leaves about 47k tokens at 16-bit cache, or about 110k with vision off and an 8-bit cache. (`i9mRnbdDYxk`)
6. **Turn multi-token prediction off past a context threshold.** One user's MTP test went from 27.4 to 45.6 tok/s. The draft needs cache room, so the speaker switches MTP off at about 32k on a 16 GB card. (`i9mRnbdDYxk`)
7. **Gate expert caching on hit rate.** Read the expert-cache hit rate at log level 4. Keep the cache only above about 90%. Under 85% it costs speed. The rule of thumb is about a quarter of expert weight size in VRAM. (`shl8FFSoANE`)
8. **Check the PCIe link before any offload benchmark.** Run `nvidia-smi` and read the current link width and speed. A chipset-wired x4 slot caps the cache path. Benchmark against the best tuned whole-layer split, not against no offload. (`shl8FFSoANE`)
9. **Set reasoning effort per request, and do not cap thinking.** Use high effort for hard multi-step work and low or medium for simple tasks. A 512-token reasoning budget cut thinking to about 3% of what a GPQA question needed. (`h_KqS4GtU3I`)
10. **Estimate wall time before a reasoning run.** Divide expected thinking tokens by measured tok/s at your real context size. The example is about 15k thinking tokens at 45.6 tok/s, roughly 5.5 minutes per question. (`h_KqS4GtU3I`)
11. **Pin hosted providers, and log the one that served each request.** Use a provider block with an order list of verified providers, require-parameters set to true, and an explicit max_tokens. Keep the default routing for requests with tools. Check the key names against OpenRouter's docs. When output is bad, read the activity log for the serving provider and its context and output caps. (`ZsnFX5mEJ4s`)
12. **Sanitize small GGUF models before judging them.** A community test with the default sampler (llama.cpp min_p 0.05) saw heavy repetition loops. Set min_p to 0 and use the vendor's repeat penalty. Report the runaway rate next to pass rate. (`Wik_JQ-enUA`, single video)
13. **Compare time to first token with every proxy timeout.** The speaker estimates a 30k-token prompt takes about 92 s at roughly 325 tok/s, near a 100 s Cloudflare Quick Tunnel limit that returns 524. The 325 figure is his extrapolation. (`IMVjEsKX5UQ`, single video)
14. **Benchmark speculation cold and warm, with acceptance rate.** Send one large-context prompt to a cold cache, then again warm. Report output tokens over total wall time, not the UI decode rate. Log accepted drafts per round by prompt type, because code and English behave differently. (`qZTmBhKz7b0`, `L7noXCBSObc`)
15. **Check any tok/s claim against bandwidth.** The decode ceiling is memory bandwidth divided by bytes read per token. A 15.1 GB 4-bit model on a 307 GB/s chip caps near 20 tok/s. Reported speeds far above that imply speculation or batching. (`qZTmBhKz7b0`)
16. **On macOS, check and raise the GPU memory cap.** The default GPU share is about two-thirds of RAM by one account and about three-quarters by others. The override resets on reboot, and the command is not named in these videos, so verify it before using it. (`uavLRbbfM94`, `6tihP50zlcE`)

### Tools creators recommend (tool — what for — `video_id`)

- llama.cpp — local OpenAI-compatible server, log levels, expert-cache flag, tensor split for two cards — `shl8FFSoANE`, `i9mRnbdDYxk`, `Wik_JQ-enUA`
- Ollama — quick local serving, `ollama ps` for context size; no default auth, so do not expose it bare — `x_qmqqp6d7s`, `IMVjEsKX5UQ`
- LM Studio — GUI runtime; one test found its bundled llama.cpp had the accelerators off, so check the startup log — `12lxN9NHuHc`
- MLX / mlx-lm — Apple-silicon runtime; use a version that respects the model's end-of-sequence tokens — `Wik_JQ-enUA`, `12lxN9NHuHc`
- Strata — tiered MoE engine (GPU, RAM, SSD). Reviews cut the headline gain to about 2 to 2.5x like-for-like, and RAM is the real cost — `m0VHx73SAG0`, `mED-boddeWI`
- OpenRouter provider routing — pin providers, read the activity log — `ZsnFX5mEJ4s`
- Built-in MTP heads and small drafters (dSpark) — drafting for decode, gains depend on the prompt type — `L7noXCBSObc`, `qZTmBhKz7b0`
- `nvidia-smi` — read PCIe link width and speed before offload tests — `shl8FFSoANE`
- Cloudflare Quick Tunnel — exposing a local endpoint; 100 s timeout and no uptime guarantee, so it is not a local setup — `IMVjEsKX5UQ`
- Kaggle TPU VM with vLLM's TPU backend — free time quota, full 16-bit 27B model; vendor-reported speed — `IMVjEsKX5UQ`
- Swift 1.5 (Qwen 3.8 27B retrained to overthink less) — fewer thinking tokens at similar GPQA accuracy in one creator's run — `h_KqS4GtU3I`, single video

### Where creators agree or clash with the conference talks

- **Agree: split prefill and decode metrics** (guide consensus 1). Creators go further and say the tok/s counter misleads agent users. (`x_qmqqp6d7s`, `i9mRnbdDYxk`, `IMVjEsKX5UQ`)
- **Agree: keep prefixes stable and route for cache hits** (guide consensus 3 and 4). A changing token at the top of one system prompt turned every turn into a miss. Cache-hit pricing is a large part of cost: one hosted endpoint reported about 94.5% hits, against 51 to 69% for most third parties. (`x_qmqqp6d7s`, `ZsnFX5mEJ4s`)
- **Agree: measure speculation per workload** (guide consensus 6). Code speeds up more than English, and a per-expert cache can make drafting slower. (`L7noXCBSObc`, `shl8FFSoANE`)
- **Clash: cache locality vs cheapest-first routing.** The conference view covers self-run fleets. The creator view covers a third-party router that picks the cheapest provider by default. Both want sticky, cached routing, but the creators show the default is the problem. (`ZsnFX5mEJ4s`)
- **Clash: offload.** The guide says to move idle KV to CPU or storage. Creators say expert offload to RAM only pays with a high hit rate and a fast PCIe link. A 0.5 GB cache on an 80B model was 24% slower than none. (`shl8FFSoANE`)
- **Clash: buy or rent.** The guide says rent to learn, own to earn. Creators say the 2026 memory price rise changes the math: one reports a DGX Spark box up 74% on identical hardware while open-weight hosted tokens got cheaper. (`Y226-wwfCSw`, `3hMEcJCGne0`). Another shows a 16 GB card paying back in about 97 days against a $2.95/M model run around the clock, but taking years against a $0.16/M model. Break-even depends on the hosted price of the same model. (`i9mRnbdDYxk`)
- **Clash between creators: reasoning effort.** One says drop Qwen to medium so the cache and context stay stable. Another says keep high effort for hard work, because lower settings cost accuracy. The conference guide does not cover this. Decide per task and measure. (`x_qmqqp6d7s`, `h_KqS4GtU3I`)
- **Agree, with sharper numbers: vendor claims.** The guide says public numbers need reproduction. Creators name the gap: a 6x headline measured as about 2 to 2.5x like-for-like (`m0VHx73SAG0`), a 4x headline measured as 1.5 to 2.2x over a tuned baseline (`shl8FFSoANE`), and a 2x speculative gain that was really speculation on versus off (`qZTmBhKz7b0`).
- **Agree, with a baseline rule: quantization.** The guide says check a quant by KL divergence, then in the harness. A creator adds that the baseline should be the build you actually run, not FP16, and that agentic retention can fall to about 75% even when headline retention is 98%. (`P1K36q76Uzk`)

### Watch first (5 `video_id` — why)

- `x_qmqqp6d7s` — why prefill and cache misses dominate local agent turns, with a checklist you can run in an afternoon.
- `shl8FFSoANE` — hit-rate go/no-go and a benchmark protocol for expert offload, with the baseline rule.
- `i9mRnbdDYxk` — VRAM budget, KV-per-token math and buy-vs-rent break-even on a 16 GB card.
- `P1K36q76Uzk` — how to read compression headlines: baseline, reasoning setting, and context length.
- `ZsnFX5mEJ4s` — provider pinning and per-request endpoint logging, relevant to hosted routing in AgentOS.

## Watch first (5-8 best videos: `video_id` — why)

- `woIYJYd_etI` — best single tour of an engine: scheduler, KV cache, CUDA graphs, speculation, and how to read a dashboard.
- `YXowceUKYJI` — KV-aware routing and PD disaggregation with data on agentic traffic, and honest limits.
- `sOB3HSiG8vo` — OpenAI on why a feedback-loop router oscillated, and the control-plane/data-plane fix with retry budgets.
- `7c9FSUVcXR0` — Meta's framing: cost per successful task, avoid/share/move/delay, cascade breakers.
- `75ckHC2LU_0` — what changed in speculation, KV compression and quantization since February.
- `4n08JHb90hI` — hands-on single-GPU workshop: memory math, concurrency knee, one flag at a time.
- `l1-D89bAuOA` — shows why your benchmark may be wrong before you tune anything.
- `J4_jCrTxMkk` — practical quantization: per-layer sensitivity, KL divergence, harness testing.

## Implications for our projects (use the profile; concrete, cite `video_id`)

**AgentOS L2B InferCraft (vLLM + Ray Serve, KV strategies, EAGLE-3, NVFP4, priority scheduler, one RTX 5090).**
- Use the KV capacity formula to set context limits and batch size on the 5090 before testing strategies (`y2W4FNAuPEA`, `4n08JHb90hI`).
- Benchmark each KV strategy (H2O, CPU offload, LMCache) at several concurrencies and report the knee, not one number (`4n08JHb90hI`, `g4SsanB0gMc`). Add the metric split TTFT versus inter-token latency to every run (`woIYJYd_etI`).
- Keep NVFP4 for weights. Skip TurboQuant-style KV quantization on the throughput path, since it cost over half the tokens/s (`75ckHC2LU_0`). Use KL divergence against BF16 plus a harness test as the quant gate (`J4_jCrTxMkk`).
- Speculative decoding: run baseline versus EAGLE-3 on each workload type, and log acceptance rate. It needs spare VRAM, so check it against the KV pool (`XTpyNrEgJQ4`). Consider retraining the draft on AgentOS's own logged traffic (`75ckHC2LU_0`, `TRe1u7dHYiA`).
- Priority scheduler with preemption: Krea runs a queue with explicit priority where training pods preempt inference pods (`byn9PURoBNY`). Meta describes workflow-aware admission using step index, spend and tenant priority (`7c9FSUVcXR0`). Feed task context into the 4-class scheduler.
- Pin sessions and tier KV (GPU to CPU to disk) for multi-turn agents (`YXowceUKYJI`, `cQQbJqvZkpo`).
- Prove it as a distributed system: use `l1-D89bAuOA` for the load-test method (achieved versus requested QPS, declarative configs). The Locust tests must pass that client-health check, or numbers are suspect. Reproduce a vendor claim before citing it (`7BcQdtRA3Tc`).
- Debug method for silent wrong output: compare engine logprobs to a plain reference forward pass (`btxG75rNJC4`). After any kernel or stream change, test long generations (`c1hGBoWw20A`).

**AgentOS L1 Govrix Scout (proxy, budgets, strategy routing).**
- Add per-key spend tracking with early alerts and a cutoff (`Bck7ABCZRZI`).
- Borrow gateway patterns: per-request fallback with a normalization layer, cool-down for failing providers, per-route P99 and timeouts, hedging near P90 of the budget, fail-open/closed choice per guardrail (`zrZ1amZBSPw`). Make retries budgeted and shed load by queue depth (`7c9FSUVcXR0`, `sOB3HSiG8vo`).
- Strategy routing: use the planner-executor split with an escalation watcher and a persistent sidekick to keep caches warm (`QHBjufYK8TA`). Route per use case from logged traces and feedback (`KB41dTlX1Uc`).
- Keep the system prompt and tool definitions byte-identical across turns so upstream caches hit (`ESbWpPT_9-o`). Report cached versus uncached tokens separately in budgets (`YXowceUKYJI`).

- Look at the same fixes: shed by queue depth, retry budgets that tighten under load, per-route P99, hedged reads, circuit breakers in the routing layer (`7c9FSUVcXR0`, `zrZ1amZBSPw`, `sOB3HSiG8vo`).
- Separate queue delay from execution time, and treat cold starts as outliers when reading p95 (`ILdE7FaAjVA`).
- Cheap global-state design: a control plane publishes snapshots and selectors decide locally with no synchronous call (`sOB3HSiG8vo`).

**ProsHarness.**
- Plan-then-execute with a fast model: per-step verification, session-to-skill replay, parallel variants (`TeGsFFNqRLA`). Checkpoint-resume is the same pattern as SIGTERM grace plus requeue (`bRGyYaE0lxI`).
- Cache-stable prompt prefixes make long runs cheaper (`ESbWpPT_9-o`, `YXowceUKYJI`).
- Keep-or-revert benchmark loops with human-chosen direction and reward-hack guards fit loops and schedules (`vrDvatGtIxs`).

**Haiku pipelines and entity resolution.**
- Use the smallest model that passes a golden set, with P50/P95 targets (`fWXJM-J0ZB8`). Gate expensive calls behind cheap classifiers (`u6q-byPWUuo`). Split work into narrow small-model steps (`g4SsanB0gMc`, `qdh_x-uRs9g`).
- If we ever self-host a small matcher, hot-swap several small models on one GPU with LRU eviction (`qdh_x-uRs9g`).

**Gaps worth a follow-up.** No talk gives independent evidence for PD disaggregation on a single consumer GPU. Treat PD as a multi-node tool and skip it on the 5090 until measured (`YXowceUKYJI`, `cQQbJqvZkpo`).
