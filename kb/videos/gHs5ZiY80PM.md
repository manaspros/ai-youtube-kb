# You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `gHs5ZiY80PM` · [watch](https://youtu.be/gHs5ZiY80PM) · **date:** 2026-06-18 · **length:** 18:46 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ziv Ilan · **orgs:** NVIDIA
- **topics:** inference-serving, training-finetuning-rl, voice-multimodal · **tags:** diffusion, image-generation, video-generation, quantization, step-caching, TeaCache, step-distillation, FastGen, TensorRT-LLM, Blackwell, real-time, NVFP4, FP4

> NVIDIA's Ziv Ilan on making diffusion image and video models fast enough for real use: quantization, step caching and step distillation, stacked incrementally, with distillation as the biggest win.

## Summary
Ziv Ilan from NVIDIA's AI Labs team argues that diffusion image and video models are hard to use in developer or enterprise settings because they are slow and their serving ecosystem is immature compared with LLMs. Typical models need 20 to 50 denoising steps, so real-time generation is the main goal and latency is the main barrier. He walks through three levers: quantization (post-training, static vs dynamic ranges, pre-quantized checkpoints), caching (TeaCache-style skipping of steps or chunks whose change is small), and step distillation (training a student to match a teacher in far fewer steps). He says distribution-matching distillation is now more common and better quality than trajectory matching, and that distillation is post-training, so it needs data and compute. He presents FastGen, an open-source NVIDIA repo for structuring distillation of 20B to 40B-plus models with sharding, and reports a near real-time demo on one B200 at GTC. His closing advice is that the optimizations are incremental: start with quantization, add multi-GPU or context parallelism and caching, and treat distillation as the most impactful but last step. The talk is high level and light on hard benchmarks, and it is a vendor talk that points to NVIDIA's own tools.

## Key ideas
- **Diffusion serving is behind LLM serving, and latency is the main gap for real-time use.** — Diffusion needs 20 to 50 denoising steps, and real-time video (robotics world models, games, content) is the stated goal. The speaker says the field is borrowing LLM serving ideas and adapting them to diffusion. ([1:08](https://youtu.be/gHs5ZiY80PM?t=68))
- **The three levers are quantization, caching and distillation, and they stack.** — He says a typical order is distillation, then quantization, then caching. He presented them simplest first: quantization, then caching, then distillation. ([2:32](https://youtu.be/gHs5ZiY80PM?t=152))
- **Quantization is the easiest win, but diffusion is harder to quantize than LLMs.** — Diffusion models are attention-heavy, so gains are smaller than for LLMs or VLMs. Still, it is low-hanging fruit on Blackwell. He prefers post-training quantization where it holds quality. Dynamic ranges, computed at run time, can track the real data distribution better than static ranges set up front. ([3:48](https://youtu.be/gHs5ZiY80PM?t=228))
- **KV cache does not carry over to diffusion, so caching works on denoising steps instead.** — Diffusion does not emit tokens one at a time, so KV-cache tricks do not map directly. TeaCache-style caching compares consecutive denoising steps and skips recomputation when the change is small. Newer chunk-based methods recompute only the regions that changed. A threshold controls the trade-off, and bad settings can hurt image quality. ([6:33](https://youtu.be/gHs5ZiY80PM?t=393))
- **Step distillation aims to cut steps, not parameters.** — The student model is trained to match the teacher's output in far fewer steps, for example from 50 down to 4 or 8, or even one. Trajectory-based methods copy the teacher's denoising path. Distribution-based methods only require the student to reach the same final output distribution, and the speaker calls them more common and better quality. Hybrids are also used. ([9:22](https://youtu.be/gHs5ZiY80PM?t=562))
- **Distillation is post-training, so data and evaluation decide the outcome.** — He says that without good data it is garbage in, garbage out. Open-source data works up to a point. For specialized distributions he recommends fine-tuning on your own data and evaluating the difference against a general dataset. Compute needs are lower than pretraining but still real. ([11:42](https://youtu.be/gHs5ZiY80PM?t=702))
- **FastGen is NVIDIA's open-source structure for large-model distillation.** — Models of 20B to 40B parameters need sharding across GPUs, and he expects hundreds of billions. FastGen handles that machinery so the user focuses on the quality recipe. The speaker says a single B200 reached near real-time video at GTC. ([13:05](https://youtu.be/gHs5ZiY80PM?t=785))
- **Optimizations are incremental, and the order is a choice you can revisit.** — Start with quantization. If quality is good enough, stop there. Otherwise add multi-GPU or context parallelism, then caching, and finally distillation, which he calls the most impactful. He also notes the emergence of autoregressive-diffusion hybrids that generate frame after frame. ([14:29](https://youtu.be/gHs5ZiY80PM?t=869))

## Techniques
- **Post-training quantization with dynamic ranges for diffusion** — Quantize the already-trained model without retraining. Prefer dynamic per-run ranges over static ranges when the inference data distribution differs from calibration. Use pre-quantized checkpoints from partners when no fine-tuning is needed. Tooling is in the TensorRT-LLM Visual Gen repo. *When:* Use as the first optimization for a diffusion model on Blackwell-class GPUs, and stop there if quality holds. Check the output quality after each step.
- **Step caching (TeaCache-style and chunk-based)** — Compare the latent or pixel change between consecutive denoising steps. If the change is below a threshold, reuse the previous result instead of recomputing. Chunk-based variants recompute only the regions that changed, such as moving parts of a video. Enabled as a flag in TensorRT-LLM Visual Gen and available in vLLM-Omni and SGLang Diffusion. *When:* Use when much of the frame stays static between steps, and tune the threshold against quality on your own content.
- **Trajectory vs distribution step distillation** — Train a student model with fewer denoising steps. Trajectory methods teach it to follow the teacher's denoising path. Distribution methods only match the final output distribution. Combine them when training is unstable. Use FastGen to manage the sharded training. *When:* Use when you need real-time or far fewer steps, you have compute for post-training, and you can evaluate quality on your own data distribution.
- **Incremental optimization ladder** — Apply the levers in order and measure quality after each one: quantization, then multi-GPU or context parallelism, then caching, then distillation. *When:* Use when the target latency is not met and each lever's quality cost needs to be checked before adding the next.

## Numbers
- Typical diffusion models run 20 to 50 denoising steps. ([1:08](https://youtu.be/gHs5ZiY80PM?t=68))
- Step distillation reduces steps from about 50 to 4 or 8, and in some cases to one. ([9:22](https://youtu.be/gHs5ZiY80PM?t=562))
- The speaker says good distillation can give a 10x to 200x performance improvement. He gives no benchmark for this, so treat it as an unsupported claim. ([10:19](https://youtu.be/gHs5ZiY80PM?t=619))
- Recent video diffusion models are about 20B to 40B parameters, and he expects hundreds of billions. ([13:05](https://youtu.be/gHs5ZiY80PM?t=785))
- A single NVIDIA B200 GPU generated near real-time video in a GTC demo, using two distillation techniques. ([10:19](https://youtu.be/gHs5ZiY80PM?t=619))
- Some small video diffusion models are 2B to 4B parameters, which need much less compute. ([17:13](https://youtu.be/gHs5ZiY80PM?t=1033))

## Hot takes
- Distillation is the most impactful optimization for diffusion, but it should come last in the ladder.
- Diffusion is less responsive to quantization than LLMs because it is more attention-heavy.

## Tools mentioned
TensorRT-LLM Visual Gen, FastGen, vLLM-Omni, SGLang Diffusion, TeaCache, Blackwell GPUs (B200), Hugging Face checkpoints

## Relevance to our work
- **agentos** (1/3): InferCraft serves LLMs with vLLM and KV-cache strategies. The talk covers diffusion, which is outside the current scope, but the step-caching idea is a parallel to KV-cache reuse. → *If a diffusion or video model is ever added to InferCraft, read the TeaCache and FastGen material first. No change for LLM serving.*
- **general** (1/3): The speaker's ordering rule, which is to apply the cheapest lever first and measure quality after each step, is a general inference-tuning habit. → *When tuning any model's latency, log quality after each lever and stop when the target is met.*
