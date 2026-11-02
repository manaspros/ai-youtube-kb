# I Tested Every Qwen3.8-27B Quant: Here’s the Best One For Your GPU

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `hg26j0erUSo` · [watch](https://youtu.be/hg26j0erUSo) · **date:** 2026-09-02 · **length:** 14:40 · **format:** review · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kai · **orgs:** Alibaba, Unsloth, Bartowski, Atomic Chat, Quesma
- **topics:** local-ai, inference-serving, evals · **tags:** quantization, gguf, kv-cache, vram, qwen3.8-27b, speculative-decoding, mtp, reasoning-effort, chat-template, benchmarks, greedy-decoding, imatrix, dynamic-quant, consumer-gpu

> Kai's practitioner guide to choosing a quant of Qwen3.8-27B for consumer GPUs: architecture-aware quants, why a Q4 KV cache silently degrades outputs, and VRAM-based file picks.

## Summary
Kai describes running a quantized Qwen3.8-27B that looked healthy (throughput, temps, no errors) while its outputs quietly drifted, which he only caught by diffing against the full-precision model. The model has 64 layers, 48 of them gated delta net linear-attention layers whose running state is fragile under compression, so good quants keep the output, attention-value and down-projection tensors at 5+ bits and squeeze the embeddings and linear-attention layers instead. He cites a Quesma run (about $3,000 of GPU time; GPQA Diamond, IFBench, TerminalBench) where 4-bit matched BF16 on TerminalBench, instruction following held down to 2-bit, and 1-bit fell to chance or below. He warns against a popular launch recipe that sets the KV cache to Q4, citing a drop in greedy-output similarity from 81.6% (Q8 cache) to 8.3% (Q4), though that measurement was on a 7B coder rather than this model. He then gives VRAM-based file picks, names three settings that matter more than the quant (reasoning effort, built-in MTP speculative decoding, chat-template handling), and closes by saying benchmarks go stale because quant files get replaced.

## Key ideas
- **Quantized models can degrade silently: throughput, temperatures and error logs look normal while outputs drift from the full-precision model.** — Kai only noticed after someone asked for a side-by-side comparison with the BF16 output. Symptoms are long answers drifting and earlier context stopping to stick; he first blamed his prompt. ([0:00](https://youtu.be/hg26j0erUSo?t=0))
- **Good quants protect the tensors that matter rather than just hitting a low average bits-per-weight.** — Common pattern: keep output, attention-value and down-projection layers at 5+ bits; let embeddings and the linear-attention (gated delta net) layers absorb the compression. Same file size, more model intact. ([2:46](https://youtu.be/hg26j0erUSo?t=166))
- **The 48 gated delta net layers hold a running state that is fragile under aggressive compression.** — Crushing that state makes a file that loads and generates normally but slowly loses the thread. Different teams reach the same goal differently: one protects the delta-net state and squeezes the FFN layers; Unsloth uses a dynamic approach; Bartowski uses an importance-matrix calibration on a corpus that was 63% tool-calling traffic. ([3:46](https://youtu.be/hg26j0erUSo?t=226))
- **Independent benchmarks put 4-bit at the practical floor, 8-bit as marginal, and 1-bit as unusable.** — Quesma's roughly $3,000 run found 4-bit matched BF16 on TerminalBench, instruction following held to 2-bit, and both 1-bit builds scored near random on reasoning, with the smaller one below random. Kai treats the vendor KL-divergence numbers (Atomic Chat: 96% top-token agreement at 4-bit, 98.9% at 8-bit) as directional only. ([6:01](https://youtu.be/hg26j0erUSo?t=361))
- **A Q4 KV cache is a silent quality regression for a small VRAM saving, and the popular launch recipe sets it.** — Greedy-decoding output similarity to full precision fell from 81.6% at Q8 cache to 8.3% at Q4. Kai states this was measured on a 7B coder, not Qwen3.8-27B, and that Q4 cache saved only about 112 MB at short context. ([8:29](https://youtu.be/hg26j0erUSo?t=509))
- **Pick the file by VRAM headroom, and pin the revision because files get replaced.** — 24 GB: Unsloth UD-Q4_K_XL (17.92 GB, about 7 GB left, 32-64K context with an 8-bit cache). 32 GB: Q6 or Q8. 16 GB: Bartowski IQ4_XS. 12 GB or less: use a smaller model. Unsloth replaced its original builds on August 19, so benchmarks for the old files no longer match. ([9:25](https://youtu.be/hg26j0erUSo?t=565))
- **Reasoning effort, MTP speculative decoding and chat-template handling change daily experience more than Q4 vs Q6.** — The default is the highest reasoning mode: one SVG prompt used 22,276 thinking tokens, and turning reasoning off took one job from 21 minutes to 137 seconds. Built-in MTP draft decoding gives self-reported 31-41 tok/s on a 3090, but no gain on an M4 (5.8 tok/s both ways). The chat template nests thinking blocks in multi-turn history, which can silently truncate context unless the Jinja flag or an equivalent is used. ([10:49](https://youtu.be/hg26j0erUSo?t=649))

## Techniques
- **Diff quantized output against the full-precision model before trusting a quant or cache setting** — Run fixed prompts with greedy decoding on both the BF16 model and the quant, then compare outputs (Kai used text similarity). Also run a task-level benchmark. Throughput and error logs cannot catch degradation. *When:* Before adopting any quant file, KV-cache quantization, or launch-flag change, and after swapping model files.
- **Keep the KV cache at Q8 or full precision** — Do not set the KV cache to Q4 to save VRAM. Kai's example saves about 112 MB at short context, while the quality cost is large. *When:* Any local serving setup where context length is tuned against VRAM.
- **Choose the quant by VRAM budget** — 24 GB: Unsloth UD-Q4_K_XL (17.92 GB) with an 8-bit KV cache for 32-64K context. 32 GB: Q6 or Q8. 16 GB: Bartowski IQ4_XS. 12 GB or less: use a smaller model, not a 2-bit build. *When:* Selecting a GGUF quant of Qwen3.8-27B for a given GPU.
- **Pin the model revision on download** — Record and pin the exact Hugging Face revision of the quant so the file that was benchmarked is the one you run. Kai notes Unsloth replaced its original builds on August 19. *When:* Any time you download a quant whose benchmarks you rely on.
- **Lower reasoning effort for simple tasks** — The model defaults to the highest reasoning mode. Turn reasoning down or off for summarization, quick coding questions and chat. Kai cites 21 min to 137 s on one job. *When:* Latency-sensitive or simple tasks on a reasoning-default model.
- **Enable the built-in MTP draft head for speculative decoding** — The file ships an MTP draft head, so no separate draft model is needed. Kai's flag is spoken as 'spec type draft MTP' (exact CLI spelling not shown on screen). Skip it on Apple Silicon, where he saw no gain. *When:* NVIDIA GPU decoding; not Apple Silicon with this implementation.
- **Make sure the front end renders the chat template correctly** — Use the Jinja flag, or otherwise make sure the server applies the model's chat template, so nested thinking blocks in multi-turn history are handled. Kai says it otherwise truncates history oddly over long conversations. *When:* Multi-turn chat or agent sessions on this model.
- **Load the vision projector as a separate file** — Multimodal input needs the vision projector file downloaded alongside the main weights; it is not in the main GGUF. *When:* When you need image or screenshot input.

## Numbers
- Full BF16 Qwen3.8-27B file is about 55 GB; 64 layers total, 16 standard attention and 48 gated delta net ([1:22](https://youtu.be/hg26j0erUSo?t=82))
- Atomic Chat vendor numbers: 4-bit agrees with full-model top token 96% of the time; 8-bit 98.9%; next step up costs about 2.5 GB more ([6:01](https://youtu.be/hg26j0erUSo?t=361))
- Quesma benchmark cost about $3,000 of rented GPU time over four quants and three benchmarks (GPQA Diamond, IFBench, TerminalBench with 89 tasks) ([6:01](https://youtu.be/hg26j0erUSo?t=361))
- Unsloth card: a 1-bit build retains about 72% top-1 accuracy while being 89% smaller ([7:16](https://youtu.be/hg26j0erUSo?t=436))
- Greedy-output similarity to full precision: 81.6% with Q8 KV cache vs 8.3% with Q4 KV cache (measured on a 7B coder, not this model); Q4 cache saved about 112 MB at short context ([8:29](https://youtu.be/hg26j0erUSo?t=509))
- Unsloth UD-Q4_K_XL is 17.92 GB, leaving about 7 GB on a 24 GB card for 32-64K context at 8-bit cache ([9:25](https://youtu.be/hg26j0erUSo?t=565))
- Bartowski IQ4_XS recommended for 16 GB cards; Unsloth replaced original builds on August 19 ([9:25](https://youtu.be/hg26j0erUSo?t=565))
- One SVG generation prompt used 22,276 thinking tokens at default reasoning; a job went from 21 minutes to 137 seconds with reasoning off ([10:49](https://youtu.be/hg26j0erUSo?t=649))
- Self-reported 31-41 tokens/s on a 3090 with MTP speculative decoding; M4 went from 5.8 to 5.8 tokens/s ([12:04](https://youtu.be/hg26j0erUSo?t=724))
- Unsloth files cleared 2.7 million downloads in the first four days ([13:05](https://youtu.be/hg26j0erUSo?t=785))
- Bartowski's importance-matrix calibration corpus was 63% tool-calling traffic ([4:49](https://youtu.be/hg26j0erUSo?t=289))
- Ridge quant is 11.7 GB ([4:49](https://youtu.be/hg26j0erUSo?t=289))

## Hot takes
- 4-bit is the floor, 8-bit is splitting hairs, and 1-bit is a science experiment rather than a daily driver.
- The GGUF filename size is only roughly the fourth most important thing about a quant, behind what the packer protected, the KV-cache setting, and reasoning length.
- Popular launch recipes that set the KV cache to Q4 are a silent quality regression.
- Vendor benchmarks and KL numbers are marketing with real math; independent benchmarks are the better evidence but go stale quickly when files are replaced.
- Mac users get no MTP speculative-decoding benefit with this implementation yet.

## Tools mentioned
Qwen3.8-27B, Unsloth UD-Q4_K_XL / Q6 / Q8 quants, Bartowski IQ4_XS quant, Ridge quant (name as transcribed; may be a caption error), Atomic Chat KL-divergence benchmark, Quesma benchmark run, GPQA Diamond, IFBench, TerminalBench, Jinja chat-template flag, spec type draft MTP (speculative decoding flag as spoken), RTX 3090, RTX 4090, Apple M4

## Relevance to our work
- **agentos** (2/3): InferCraft (L2B) runs vLLM on one RTX 5090 with quantization (NVFP4) and KV-cache strategies. The talk's core warnings (quant choice protects specific tensors, KV-cache quantization degrades output silently, throughput hides regressions) apply directly, though the consumer-GPU and llama.cpp-style file picks do not map onto vLLM. → *Add a quant/KV-cache regression gate to InferCraft: fixed prompts, greedy decoding, diff against BF16 output plus a task benchmark (e.g. multi-turn and long-context tasks), and block any KV-cache quantization setting that fails before it is used in production.*
