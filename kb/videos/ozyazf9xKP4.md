# Best Local Coding Model Right Now in 2026 (My Top 3 Picks)

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `ozyazf9xKP4` · [watch](https://youtu.be/ozyazf9xKP4) · **date:** 2026-08-02 · **length:** 8:17 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Host (Kai Explains channel, unnamed in transcript) · **orgs:** Alibaba, DeepSeek, Mistral AI, Zhipu (GLM), OpenAI
- **topics:** local-ai, token-cost-efficiency, models-research · **tags:** local-coding-models, vram-sizing, quantization, mixture-of-experts, model-routing, hardware-tiers, swe-bench, tokens-per-second

> Kai ranks three open-weight coding models a 24GB-VRAM owner can actually run, argues for VRAM math and tokens/sec over leaderboard scores, and recommends routing cheap local work and hard tasks to cloud models.

## Summary
The host argues that open-weight coding leaderboards are misleading because the top models (Kimi K2.7, GLM 5.2) need hundreds of GB or roughly 750B parameters, far beyond consumer hardware. The core sizing rule is about 2 GB of VRAM per billion parameters at full precision, dropping to about 0.5 GB per billion at 4-bit quantization. Using that rule, he picks Qwen3 Coder Next as the default for most people, with the dense Qwen 3.6 27B as a tighter-card option and DeepSeek V3.2 as a reasoning-heavy but offload-bound choice. He reports vendor-stated SWE-bench Verified numbers and says to treat them as marketing until you run the model yourself. He says tokens per second matters more day to day than benchmark score, and recommends a split setup: a small local model for bulk boilerplate and a frontier cloud model for subtle bugs and architecture. He closes with a VRAM tier checklist (24 GB, 12-16 GB, 8 GB, and Macs with unified memory). The video is opinion-led, with no benchmarks of its own and a subscribe call-to-action at the end.

## Key ideas
- **Open-weight coding leaderboards can mislead for local use: the top-ranked models are not runnable on consumer GPUs.** — Kimi K2.7 is cited as needing about 304 GB even at the smallest working 1-bit quant, against a 24 GB card. GLM 5.2 (about 750B parameters) is called a fantasy for anyone without a server rack. ([0:00](https://youtu.be/ozyazf9xKP4?t=0))
- **VRAM is the sizing constraint, and a simple rule of thumb picks the hardware tier.** — About 2 GB of VRAM per billion parameters at full quality; good 4-bit quantization brings that to about 0.5 GB per billion, so a 30B model fits on one good card with room left for context. ([1:26](https://youtu.be/ozyazf9xKP4?t=86))
- **Qwen3 Coder Next is the speaker's default pick for most people.** — An 80B mixture-of-experts model with about 3B active parameters, around 35-40 GB at 4-bit (a 24 GB card with offload, or a 64 GB Mac), 256k context extendable toward 1M, Apache 2.0 license. ([2:33](https://youtu.be/ozyazf9xKP4?t=153))
- **Dense Qwen 3.6 27B is the option for tighter cards, with vendor claims treated cautiously.** — Fits in about 22 GB. The speaker repeats Alibaba's claim of flagship-level agentic coding, but says independent early results look like a real step up. He says to treat the vendor number as marketing until you run it yourself. ([2:33](https://youtu.be/ozyazf9xKP4?t=153))
- **DeepSeek V3.2 suits reasoning and competitive-programming style work but needs offloading on a single 24 GB card.** — 37B active parameters. Fitting it on 24 GB means offloading layers to system RAM, which slows long runs. The speaker says it is powerful but not a laptop model. ([3:54](https://youtu.be/ozyazf9xKP4?t=234))
- **Tokens per second matters more than benchmark score for daily use.** — A model that benchmarks slightly higher but generates slowly will frustrate a developer working interactively. Leaderboards rarely print generation speed. ([5:18](https://youtu.be/ozyazf9xKP4?t=318))
- **The best local setup routes work between a small local model and a frontier cloud model.** — Cheap local model (for example a quantized Qwen or Devstral Small 24B, which he says is built for tool calling) handles boilerplate, renames, and first drafts. A frontier model is reserved for subtle bugs and architecture decisions. He frames it as cheap local for volume, expensive cloud for judgment. ([5:18](https://youtu.be/ozyazf9xKP4?t=318))
- **Pick the model by the GPU tier you actually own.** — 24 GB: quantized Qwen3 Coder Next or dense Qwen 3.6 27B. 12-16 GB: gpt-oss-20B, or a smaller Qwen for autocomplete-level help. 8 GB: 7-8B class such as Qwen2.5 Coder 7B. Macs with large unified memory are a strong value. ([6:46](https://youtu.be/ozyazf9xKP4?t=406))

## Techniques
- **VRAM budget check before choosing a local model** — Estimate memory as about 2 GB per billion parameters at full precision, or about 0.5 GB per billion at 4-bit, then leave headroom for context and your own work. Map the result to a hardware tier before downloading anything. *When:* Choosing a local coding model for a given GPU or Mac, before comparing benchmark scores.
- **Judge MoE models by active parameters for speed** — For mixture-of-experts models, look at active parameters (for example about 3B active for Qwen3 Coder Next) as a speed hint, while total parameters still set the memory footprint. *When:* Comparing large MoE models that must fit a consumer GPU with offload.
- **Split routing between local and cloud models** — Send high-volume, low-judgment work (boilerplate, bulk renames, first drafts) to a small quantized local model. Escalate subtle bugs and architecture decisions to a frontier cloud model, keeping one cloud key for the hard tail. *When:* You have a private or cost-sensitive codebase but still need top-end reasoning for some tasks.
- **Select local models by tokens per second, not leaderboard score** — Measure how fast a candidate generates on your own hardware, and accept a slightly lower benchmark if interactive speed is much better. *When:* Evaluating which local model to keep as your daily driver.
- **Layer offload to system RAM when a model barely overflows VRAM** — Keep as many layers as possible on the GPU and offload the rest to system RAM. Expect slowdown on long runs. *When:* A model is just over your VRAM and you accept slower generation in exchange for running it at all.

## Numbers
- Kimi K2.7 smallest working 1-bit quant needs about 304 GB of memory; a typical high-end consumer GPU has 24 GB. ([0:00](https://youtu.be/ozyazf9xKP4?t=0))
- Rule of thumb: about 2 GB VRAM per billion parameters at full quality; 4-bit quantization drops this to about 0.5 GB per billion. ([1:26](https://youtu.be/ozyazf9xKP4?t=86))
- GLM 5.2 at roughly 753B parameters implies about 1.5 TB of VRAM at full quality by the same rule. ([1:26](https://youtu.be/ozyazf9xKP4?t=86))
- Qwen3 Coder Next: 80B total, about 3B active, about 35-40 GB at 4-bit, about 58.7% on SWE-bench Verified (vendor figure as stated), 256k context extendable toward 1M. ([2:33](https://youtu.be/ozyazf9xKP4?t=153))
- Qwen 3.6 27B dense fits in about 22 GB (as stated). ([2:33](https://youtu.be/ozyazf9xKP4?t=153))
- DeepSeek V3.2: 37B active parameters, about 70% on SWE-bench Verified (as stated). ([3:54](https://youtu.be/ozyazf9xKP4?t=234))
- GLM 5: about 72.8% on SWE-bench Verified (as stated); GLM 5.2 reported at the top of SWE-bench Pro. ([3:54](https://youtu.be/ozyazf9xKP4?t=234))
- Hardware tiers: 24 GB for quantized Qwen3 Coder Next or dense Qwen 3.6 27B; 12-16 GB for gpt-oss-20B; 8 GB for a 7-8B model class. ([6:46](https://youtu.be/ozyazf9xKP4?t=406))

## Hot takes
- Open weight is not the same as runnable: the models that top coding charts are out of reach for home hardware.
- Tokens per second is the metric that decides daily usefulness, and leaderboards omit it.
- The best local coding model is the one that fits your GPU, not the biggest one.
- Vendor benchmark numbers should be treated as marketing until you run the model yourself.
- The video presents no benchmarks of its own; rankings are qualitative opinion, and the ending is a subscribe call-to-action.

## Tools mentioned
Qwen3 Coder Next (Alibaba, 80B MoE, about 3B active), Qwen 3.6 27B dense (transcribed as 'Quen 3.627B'; released April 22 per speaker), Qwen2.5 Coder 7B (transcribed as 'coder 7B'), DeepSeek V3.2 (transcribed as 'DeepSeq v3.2'), GLM 5 and GLM 5.2 (Zhipu, transcribed as 'GLM, from Jippu'), Kimi K2.7 (transcribed as 'Kimi-K 2.7'), Devstral Small 24B (Mistral, transcribed as 'Devstrol Small 24B'), gpt-oss-20B (transcribed as 'GPTOS 20B'), SWE-bench Verified, SWE-bench Pro, LiveCodeBench, Claude, GPT-5, Gemini (named as frontier cloud examples)

## Relevance to our work
- **agentos** (2/3): InferCraft runs vLLM on a single RTX 5090 (24 GB class), and the VRAM sizing rule and quant tiers apply directly to choosing its model lineup. The small-local versus frontier-cloud split is also relevant to Govrix Scout routing. → *Size candidate local models with the 2 GB-per-billion and 0.5 GB-per-billion (4-bit) rule before adding them to InferCraft, then benchmark each on tokens/sec and agent-style SWE-bench tasks on the RTX 5090.*
- **prosharness** (1/3): ProsHarness loops could push boilerplate subtasks to a small local model and keep frontier calls for critique and debate steps. This is a cost idea, not something the talk tests. → *Consider tagging ProsHarness subtasks as bulk or judgment work and routing bulk steps to a local model, keeping plan critique on a frontier model.*
