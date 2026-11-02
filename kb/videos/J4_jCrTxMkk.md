# Compression at the Edge — NVIDIA, Unsloth, HuggingFace, Ollama

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `J4_jCrTxMkk` · [watch](https://youtu.be/J4_jCrTxMkk) · **date:** 2026-08-18 · **length:** 46:01 · **format:** panel · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Chris Alexiak, Daniel, Merve, Parth · **orgs:** NVIDIA, Unsloth, Hugging Face, Ollama
- **topics:** local-ai, inference-serving, evals · **tags:** quantization, NVFP4, dynamic-quantization, QAD, KL-divergence, local-models, llama.cpp, Ollama, hybrid-attention, KV-cache, model-routing, edge

> Panel from NVIDIA, Unsloth, Hugging Face and Ollama on how quantization and compression make large open models run on local hardware, how to pick per-layer precision, and how to evaluate the result.

## Summary
Four panelists (NVIDIA model optimizer and Nemotron, Unsloth, Hugging Face, Ollama) discuss compression as the way to run big open models on consumer hardware. The core claim is that naive compression breaks models, but per-layer sensitivity-aware quantization keeps most accuracy, with first/last and sensitive layers kept at higher precision. NVIDIA describes NVFP4 (4-bit values with a shared FP8 scale per 16 elements) and says it targets under 1% benchmark degradation, using gradient-based sensitivity analysis and an LP/knapsack solver to pick precisions. Post-training quantization is described as easy for large models, while small models (roughly under 20B) need quantization-aware distillation, which is fragile if the training data is wrong. The speakers say benchmarks are noisy and gameable, so they favour KL divergence against the BF16 logits on calibration data, plus real harness testing. Their outlook is that hybrid and linear attention make quantization harder because some layers break at low bits, and that KV-cache compression and activation sparsity are the next areas.

## Key ideas
- **Compression makes big models usable locally, but there is no free lunch: you pay in latency or quality.** — Ollama's popularity came from running larger models on small machines via quantization. The panel frames compression as democratizing access, and says the cost always shows up somewhere. ([1:09](https://youtu.be/J4_jCrTxMkk?t=69))
- **Quantizing a giant model to 1-2 bits is survivable if the right layers stay at higher precision.** — Unsloth's dynamic quantization keeps a few important layers at 16-bit and pushes most layers to 1-2 bits. The speaker says this recovers about 76% of accuracy. Random compression of the same size would fail. ([3:21](https://youtu.be/J4_jCrTxMkk?t=201))
- **Layer importance is uneven and must be measured per layer, not applied uniformly.** — First and last layers matter most, middle layers less. Some single weights are critical (the speaker cites a superweights paper, where quantizing one value can badly degrade the model). Per-layer sensitivity analysis is therefore needed, and the search is combinatorial. ([12:32](https://youtu.be/J4_jCrTxMkk?t=752))
- **NVFP4 is a numeric format trick, not just smaller numbers: micro-block scaling.** — Groups of 16 four-bit values share one FP8 scale factor. The speaker credits the idea to bitsandbytes and says NVIDIA's variant gives better results than other 4-bit formats. ([16:05](https://youtu.be/J4_jCrTxMkk?t=965))
- **Sensitivity is architecture-specific, so heuristics per layer type matter.** — NVIDIA finds linear-attention projections and QKV layers sensitive, while MoE layers can stay in FP4 by default. Hybrid and linear-attention architectures make the old per-model heuristics fail. A linear-attention layer can look fine on short benchmarks but produce gibberish on long context. ([15:01](https://youtu.be/J4_jCrTxMkk?t=901))
- **Benchmarks miss behaviour, so test the quantized model inside a real agent harness.** — The speakers say verifiable benchmarks are only a rough signal. A quantized model can pass them yet feel wrong in Claude Code or another harness, so they run real harness checks and vibe checks before shipping. ([18:55](https://youtu.be/J4_jCrTxMkk?t=1135))
- **Most business workloads do not need a frontier model, and compression saves money in other ways too.** — Concurrency gains and distilling mid-sized models into small re-rankers that do not generate text are cited as large cost savers. The speaker says most people do not know this. ([20:16](https://youtu.be/J4_jCrTxMkk?t=1216))
- **A large model quantized to 4-bit can beat a smaller model at 16-bit of the same disk size.** — The speaker cites a paper comparing a 35B model at 16-bit with a roughly 120B model at 4-bit at equal size, where the larger quantized model wins. The panel expects models to keep growing, which makes compression more needed. ([22:51](https://youtu.be/J4_jCrTxMkk?t=1371))
- **Quantization is easy to produce but hard to verify, and KL divergence is preferred to sampled benchmarks.** — Post-training quantization of a huge model takes a couple of hours on Blackwell nodes. The long part is evaluation against the model card. The proposed metric is KL divergence between the BF16 and quantized output logits on calibration data, driven toward zero at a smaller size. ([42:49](https://youtu.be/J4_jCrTxMkk?t=2569))

## Techniques
- **Sensitivity-aware dynamic quantization** — Measure how much each layer hurts accuracy when quantized, then keep the sensitive layers (first/last, QKV, linear-attention projections) at 16-bit and push the rest to 1-2 bit. Auto-quantize uses gradient-based sensitivity with an LP or knapsack solver to choose the per-layer precisions under a size budget. *When:* When you need a very large model to fit a memory budget and cannot afford uniform 4-bit loss.
- **Post-training quantization first, QAD for small models** — For large or mid-size models (roughly 20-30B and up), run PTQ with selective heuristics, which the speakers say usually works out of the box. For smaller models, use quantization-aware distillation to recover accuracy, with training data matched to the original mix. *When:* Choose PTQ by default. Move to QAD only when PTQ output fails evaluation on a small model.
- **KL-divergence evaluation against the unquantized model** — Run the BF16 model and the quantized model on a calibration dataset, compare their output logits with a divergence measure, and treat a lower divergence at a smaller size as better. This avoids the variance of sampled accuracy benchmarks. *When:* When comparing quant candidates or choosing a default quant for a model, and when sampled benchmarks are too noisy to trust.
- **Harness-level vibe testing before shipping a quant** — Run the quantized model inside the real agent harness on real tasks, including long-context ones, and check behaviour directly rather than trusting benchmark scores alone. *When:* Before publishing or defaulting to a quant, especially for agentic or long-horizon workloads.
- **Per-model default quant with precision kept high for tiny models** — Publish one default quantization per model. For very small models, keep a higher precision by default, because aggressive quantization can leave the model unusable. *When:* When shipping a local-model runtime to end users who will not tune quant settings.
- **Big planner, small executor routing** — Use a large model for planning and a compressed or small model for execution steps, which keeps most tokens on the faster model. *When:* When a big model is too slow on your hardware for every step, and planning quality matters more than execution speed.

## Numbers
- GLM 5.2 weights shrink from about 1.5 TB to about 250 GB via quantization, which the speaker describes as 86% smaller. ([1:58](https://youtu.be/J4_jCrTxMkk?t=118))
- Dynamic quantization of 1-2 bit layers with some 16-bit layers recovers about 76% of accuracy, per the speaker. ([3:21](https://youtu.be/J4_jCrTxMkk?t=201))
- A 1.58-bit quantization of DeepSeek R1 was the first Unsloth quant that surprised the team by working well. ([4:36](https://youtu.be/J4_jCrTxMkk?t=276))
- NVIDIA targets under 1% accuracy degradation overall on benchmarks for FP4 checkpoints. ([15:01](https://youtu.be/J4_jCrTxMkk?t=901))
- NVFP4 shares one FP8 scale across each group of 16 four-bit elements. ([16:05](https://youtu.be/J4_jCrTxMkk?t=965))
- The speaker says that quantizing one specific number in a model can make it about 20% worse (superweights paper). ([12:32](https://youtu.be/J4_jCrTxMkk?t=752))
- A large model quantized to 4-bit is said to beat a roughly 35B model at 16-bit at the same disk size (cited paper). ([22:51](https://youtu.be/J4_jCrTxMkk?t=1371))
- A large model on limited GPU power may run at about 5-10 tokens per second, versus about 200 tokens per second for a small model. ([24:09](https://youtu.be/J4_jCrTxMkk?t=1449))
- A quantized checkpoint for a very large (trillion-scale) model is ready in a couple of hours on Blackwell nodes, while evaluation takes much longer. ([29:20](https://youtu.be/J4_jCrTxMkk?t=1760))
- Small VLMs at 256M, 500M and 1.5B parameters were trained; the 500M model runs on an iPhone. ([27:01](https://youtu.be/J4_jCrTxMkk?t=1621))
- Most KV-cache quantization in use is 8-bit; 4-bit holds up well on large models but shows drops on smaller ones. ([40:19](https://youtu.be/J4_jCrTxMkk?t=2419))

## Hot takes
- Compression is an artisanal science right now, not a real science.
- A big model quantized down beats a small model at full precision when the size is the same.
- Public arenas and benchmarks are easy to game, so the vibe has to be checked in a real harness.
- Most jobs do not need a frontier model, and people are unaware how much cost they could cut with compression and distillation.
- Mixing many architectures is good for the open ecosystem, even though it makes quantization harder.

## Tools mentioned
llama.cpp, Ollama, Unsloth, NVIDIA Model Optimizer (ModelOpt), TRL, bitsandbytes, QLoRA, GRPO, NVFP4, MXFP4, OpenClaw, Hermes agent, Claude Code

## Relevance to our work
- **agentos** (2/3): InferCraft runs vLLM with quantization (NVFP4) and KV-cache strategies on one RTX 5090. The talk's per-layer sensitivity and KL-divergence methods apply directly to choosing quant levels for that stack. → *Add a KL-divergence check (quantized vs BF16 logits on a calibration set) to the InferCraft quant selection, and keep linear-attention and QKV layers at higher precision for long-context runs.*
- **prosharness** (1/3): ProsHarness uses Claude Code and has a cheap-model interest. The talk shows local quantized models running in Claude Code, which is relevant if ProsHarness ever needs a cheap local executor. → *Consider a local quantized executor model as a low-cost option for simple ProsHarness steps, and benchmark it inside the harness before trusting it.*
