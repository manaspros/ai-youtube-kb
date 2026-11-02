# China Just Open-Sourced 6 Ways to Speed Up Your AI Inference (Tencent AngelSpec)

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `0ixklwdIsuY` · [watch](https://youtu.be/0ixklwdIsuY) · **date:** 2026-09-02 · **length:** 15:54 · **format:** review · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kai (Kai Explains host; not named in transcript) · **orgs:** Tencent, UC San Diego, Peking University, DeepSeek, vLLM, NVIDIA, Alibaba, Hugging Face
- **topics:** inference-serving, token-cost-efficiency, models-research · **tags:** speculative-decoding, drafter, block-diffusion, vllm, angelspec, dcut, eagle-3, mtp, verification-bottleneck, concurrency, h20, hi3

> Kai Explains walks through Tencent's AngelSpec repo: six speculative-decoding drafter methods, why block-diffusion drafters win on acceptance but not under load, and the DCut verification trick that helps at high concurrency.

## Summary
AngelSpec is a training framework for speculative-decoding drafters, not an inference engine; every benchmark in the repo comes from drafters it trained for Tencent's Hi3 model. The repo covers six methods in two families: autoregressive drafters (MTP, EAGLE-3) and block-diffusion drafters (D-Flash, dFlare, dSpark, D-Fly), with D-Fly as Tencent's own contribution. Block-diffusion drafters win clearly on tokens accepted per pass, but later tokens in a parallel block are drafted blind, so acceptance collapses deeper into the block. Pointing the drafters at live concurrent traffic exposed a plateau around 850 tokens/s at 48 to 64 users, because the verifier becomes the bottleneck. DCut addresses this by stopping verification early when a draft looks shaky, which the presenter says gives about 16% more throughput at 64 users for a 2.8% acceptance drop. The video also flags that DCut closely matches a DeepSeek mechanism published weeks earlier and later shipped in vLLM, that plain MTP beats the block drafters on MTBench throughput, that acceptance falls about 31% in thinking mode, and that an open vLLM issue shows dynamic speculation can badly regress latency.

## Key ideas
- **AngelSpec is a training framework for drafters, not an inference engine** — The framework itself serves no tokens. Its benchmark numbers come from drafters it trained for Tencent's Hi3, so headlines calling it a drop-in vLLM replacement are wrong. ([1:17](https://youtu.be/0ixklwdIsuY?t=77))
- **Two drafter families: autoregressive vs block diffusion** — Autoregressive drafters (MTP, EAGLE-3) still write one token at a time. Block-diffusion drafters (D-Flash, dFlare, dSpark, D-Fly) emit a whole block in one forward pass. Four of the six methods are block-diffusion. ([2:35](https://youtu.be/0ixklwdIsuY?t=155))
- **Block drafters win on acceptance but degrade positionally** — Tokens in a parallel block are drafted without seeing each other. vLLM data on DeepSeek V4 shows first-token survival above 70% and seventh-token survival below 10%. D-Fly adds a small sequential head to pass context to later tokens. ([5:05](https://youtu.be/0ixklwdIsuY?t=305))
- **Architecture gained less than training data in the ablation** — Architecture changes raised accepted tokens per pass from 3.77 to 4.60. Adding about 700k code and math prompts to training then gave +0.15 (to 4.75), with almost no engineering cost. ([6:29](https://youtu.be/0ixklwdIsuY?t=389))
- **Offline speedups do not survive concurrent load** — D-Fly at block length 8 was 1.98 to 2.40x faster offline across 4 to 32 users, but under live load it fell to about 1.33x and flatlined near 850 tokens/s from 48 to 64 users. The verifier became the bottleneck, so longer drafts add work without adding throughput. ([7:48](https://youtu.be/0ixklwdIsuY?t=468))
- **DCut: verify only as far as the draft looks confident** — The verifier stops reading a draft as soon as it looks unreliable. At 64 users, D-Fly rose from 848 to 981 tokens/s for a 2.8% drop in acceptance rate. ([9:08](https://youtu.be/0ixklwdIsuY?t=548))
- **Convergent discovery: DCut overlaps with DeepSeek's and vLLM's work** — DeepSeek published the same mechanism as Confident Scheduled Verification on July 6. vLLM shipped it upstream on August 14, crediting DeepSeek and not AngelSpec. ([10:31](https://youtu.be/0ixklwdIsuY?t=631))
- **Plain MTP beats the block drafters on MTBench throughput; thinking mode hurts acceptance** — On MTBench at 64 users, D-Flash reaches 1.89x vs MTP at 2.08x. The drafters were trained on non-thinking output, and acceptance falls from 4.79 to 3.29 in thinking mode, about 31%. ([10:31](https://youtu.be/0ixklwdIsuY?t=631))
- **Choose speculation depth by concurrency, and test dynamic schedules carefully** — Below about 8 concurrent users, use the deepest block drafter. Above about 48, the scheduler matters more than the drafter, and a fixed speculation depth can hurt. An open vLLM issue reports a dynamic schedule dropping throughput from 232 tokens/s to between 24 and 157. ([11:55](https://youtu.be/0ixklwdIsuY?t=715))
- **Benchmarks ran on H20 GPUs, and the licensing is worth reading** — Tencent benchmarked on eight H20s (about 296 TFLOPS vs 1,979 for H100). AngelSpec is under a custom license, not Apache, though Hi3 itself is Apache 2.0. ([13:19](https://youtu.be/0ixklwdIsuY?t=799))

## Techniques
- **Speculative decoding with a cheap drafter and a verifier** — A small drafter proposes k tokens. The target model verifies all k in one pass, and the first mismatch discards the rest. Output is unchanged, and speed depends on tokens accepted per pass. *When:* Serving a large model where decode is memory-bound and the drafter is much cheaper per token.
- **Pick the drafter by concurrency level** — Under about 8 concurrent users, use the deepest block-diffusion drafter (for example D-Fly at block length 8). Above about 48 users, benchmark the scheduler and consider a shallower or adaptive speculation depth instead of the deepest drafter. *When:* Choosing a speculation setup for a specific traffic profile, not for a single-request benchmark.
- **Enable adaptive verification in vLLM (DCut-style)** — Use the vLLM method strings MTP, EAGLE3, DFLASH, or DSPARC. Adaptive verification is exposed as the flag 'Enable Adaptive Verification' and works only with DSPARC. It requires an FP8 KV cache and full varlen CUDA graphs, and vLLM refuses to start with pipeline parallelism, LoRA, or output logprobs. *When:* High-concurrency serving where the verifier is the bottleneck and the config requirements above are acceptable.
- **Use pretrained drafters instead of training** — For Hi3 or Qwen3-8B (transcribed as Quen38B), download the AngelSlim-organization drafters on Hugging Face, including the D-Fly block-length-8 variant and the MTP variant, and point the inference engine at them. *When:* Serving one of the supported target models and not needing custom drafters.
- **Match the drafter to the serving mode** — Drafters trained on non-thinking completions lose a lot of acceptance in thinking mode. Use the thinking-mode drafter variant if the server runs reasoning traces. *When:* Any deployment where thinking or chain-of-thought output is enabled.
- **Load-test the speculation config before production** — Sweep concurrency and compare throughput with and without speculation. Watch for dynamic schedules that regress tail latency, such as the 6-second request that grew to 40 seconds in the reported vLLM issue. *When:* Before enabling any dynamic or adaptive speculation schedule in production.

## Numbers
- Accepted tokens per pass on Hi3 (21B active): MTP about 3, D-Flash 3.69, D-Fly 4.79. D-Fly is about 60% above autoregressive and 30% above the prior block drafter. ([3:50](https://youtu.be/0ixklwdIsuY?t=230))
- Per-position survival in a 7-token block (vLLM, DeepSeek V4): first token above 70%, seventh token below 10%. ([5:05](https://youtu.be/0ixklwdIsuY?t=305))
- Ablation of accepted tokens per pass: 3.77 (D-Flash backbone) to 4.40 (new backbone) to 4.56 (sequential head) to 4.60 (hidden-state correction) to 4.75 (about 700k extra code and math prompts). ([6:29](https://youtu.be/0ixklwdIsuY?t=389))
- Offline D-Fly at block length 8: 1.98x to 2.40x faster than plain decoding across 4 to 32 concurrent users. Under moderate live load it is about 1.33x. ([7:48](https://youtu.be/0ixklwdIsuY?t=468))
- Throughput flatlines with concurrency: 860 tokens/s at 48 users, 858 at 56, 848 at 64. ([7:48](https://youtu.be/0ixklwdIsuY?t=468))
- DCut on D-Fly at 64 users: 848 to 981 tokens/s (+16%) for a 2.8% drop in acceptance rate. ([9:08](https://youtu.be/0ixklwdIsuY?t=548))
- MTBench at 64 users: D-Flash 1.89x base decoding vs MTP 2.08x. ([10:31](https://youtu.be/0ixklwdIsuY?t=631))
- Thinking-mode acceptance drops from 4.79 to 3.29 tokens per pass, about 31%, for drafters trained on non-thinking output. ([10:31](https://youtu.be/0ixklwdIsuY?t=631))
- Concurrency thresholds given: under about 8 users use the deepest block drafter; past about 48 users the scheduler becomes the variable. ([11:55](https://youtu.be/0ixklwdIsuY?t=715))
- Open vLLM issue (July 23): a dynamic speculation schedule dropped throughput from 232 tokens/s to 24 to 157, and a 6-second request took about 40 seconds. ([13:19](https://youtu.be/0ixklwdIsuY?t=799))
- Compute: NVIDIA H20 about 296 TFLOPS vs H100 about 1,979 TFLOPS. Benchmarks ran on eight H20 GPUs. ([13:19](https://youtu.be/0ixklwdIsuY?t=799))

## Hot takes
- The presenter argues the repo's real contribution is the systems finding, not the drafter architectures: the verifier, not the drafter, becomes the bottleneck under load.
- Tencent's benchmark numbers come from its own repo and hardware (H20s), and the video calls them vendor benchmarks to be treated with skepticism. The one Tencent-original method is D-Fly, and DCut overlaps with DeepSeek's prior work.
- Giving away the trainer makes Hi3 the default target that others train drafters against, which the presenter reads as an ecosystem lock-in play.
- Headlines describing AngelSpec as a drop-in vLLM replacement are wrong; it is a training framework.
- The 'convergent discovery' framing gives credit to the vLLM upstream merge, while the video does not name AngelSpec as the originator.

## Tools mentioned
AngelSpec (Tencent training framework for speculative-decoding drafters; custom license), Hi3 (Tencent, 21B active parameters), MTP (multi-token prediction), EAGLE-3, D-Flash (block diffusion, UC San Diego), dFlare (named in the video; Peking University and Tencent), dSpark (DeepSeek serving team), D-Fly (Tencent), DCut (verification early-exit), vLLM, DeepSeek V4, Qwen3-8B, MTBench, NVIDIA H20, NVIDIA H100, AngelSlim drafter models on Hugging Face

## Relevance to our work
- **agentos** (2/3): InferCraft (L2B) already runs vLLM with EAGLE-3 speculative decoding on one RTX 5090. This video gives concurrency-dependent guidance and the vLLM adaptive-verification requirements that bear on that config. → *Add a concurrency sweep (1, 8, 32, 48, 64 users) to the InferCraft Locust runs and compare EAGLE-3 against a block drafter (D-Fly or D-Flash from the AngelSlim HF org) to test whether the throughput plateau appears on the 5090.*
