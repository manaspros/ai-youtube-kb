# Why Large? Tiny LMs & Agents on Edge/Robotics — Cormac Brick, Google

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `hacEQHHhu2Q` · [watch](https://youtu.be/hacEQHHhu2Q) · **date:** 2026-08-18 · **length:** 21:45 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Cormac Brick · **orgs:** Google, Google DeepMind
- **topics:** local-ai, inference-serving, training-finetuning-rl · **tags:** edge-ai, tiny-models, on-device, quantization, synthetic-data, fine-tuning, function-calling, gemma, functiongemma, litert, npu, raspberry-pi, robotics

> Google's Cormac Brick on running tiny (50M to 500M) and small (1 to 4B) models on phones, browsers and robots, and why fine-tuning on synthetic data beats bigger models for narrow tasks.

## Summary
Cormac Brick, a tech lead on Google's AI Edge team, argues that putting AI into many cheap devices needs tiny models. He lists the case for on-device inference (latency, privacy, offline use, cost at scale) and the main constraint now, DRAM cost, which pushes the team toward quantization and the smallest model that can do the job. Small models of 1 to 4B parameters, such as Gemma E2B, work with zero-shot prompting but need 4 to 8 GB of RAM, which excludes low-end devices. For tiny models (roughly 50M to 500M parameters) he recommends first trying off-the-shelf fixed-task models for ASR, vision and embeddings, then fine-tuning on synthetic data when needed. He shows FunctionGemma-based voice-to-function calling at over 86% reliability across 10 functions, a fully on-device dictation app built from two fine-tuned tiny Gemma models, and Chrome built-in summarization and proofreading delivered by tiny models. The numbers are device-specific (Raspberry Pi, Jetson, Qualcomm NPU) and the talk leans on Google's own runtime and models.

## Key ideas
- **Edge AI is driven by latency, privacy, offline use and cost at scale; cloud tokens look cheap but add up across a large user base.** — The speaker lists four reasons to run on device instead of calling a cloud model, and says per-token cost matters most when multiplied across many app users. ([2:05](https://youtu.be/hacEQHHhu2Q?t=125))
- **DRAM cost is the main new constraint on edge AI, and it forces quantization and a search for the smallest model that works.** — He says some phone makers put less DRAM in devices this year, and a Raspberry Pi 3 16 GB has risen about 2.5x in price since launch. ([3:28](https://youtu.be/hacEQHHhu2Q?t=208))
- **Small 1 to 4B models need about 4 to 8 GB of DRAM, which puts them out of reach for many devices, so the team goes smaller.** — Small models ship in Android AI Core and Apple Intelligence, but the speaker says they limit use to laptops, phones and high-end hardware. ([4:50](https://youtu.be/hacEQHHhu2Q?t=290))
- **A 2B model can be squeezed with mixed 2/4/8-bit quantization and per-layer embeddings, but the KV cache and runtime still push RAM needs to about 2 GB plus OS overhead.** — Gemma E2B text weights come to about 841 MB at about 2.9 bits per weight. He gives a rule of thumb of 4 GB or more for a device. ([6:17](https://youtu.be/hacEQHHhu2Q?t=377))
- **Tiny models in the 50M to 500M range are the answer when a small model is too big or too slow, and they are often a background helper, not the main feature.** — Examples are system-health checks that run alongside the main app. Off-the-shelf ASR, vision and embedding models are the first option. Fine-tuning is the next step. ([11:21](https://youtu.be/hacEQHHhu2Q?t=681))
- **For a narrow task, a fine-tuned tiny model on synthetic data can match a 2 to 4B model, and it runs faster because it reads fewer weights from memory.** — FunctionGemma-based mobile actions reach over 86% reliability across 10 output functions. Decode speed rises to about 45 tokens/s from mid-single digits on a Raspberry Pi, which he attributes to less memory reading per token. ([14:56](https://youtu.be/hacEQHHhu2Q?t=896))
- **The playbook is: pick a base model, check quality and memory, then generate 10k to 10M synthetic samples and fine-tune.** — He says this approach has worked for summarization and proofreading, and that the same quality can come from a much smaller model. The Mobile Actions dataset is on Hugging Face. ([16:18](https://youtu.be/hacEQHHhu2Q?t=978))

## Techniques
- **Synthetic-data fine-tuning of a tiny model for one task** — Pick a base model, measure quality and memory. If zero-shot is not enough, generate 10k to 10M synthetic examples for the task and fine-tune. The speaker says this gives high reliability at very wide device scale. He suggests an agent could generate the data. *When:* A single narrow task (function calling, summarization, proofreading) where a 2 to 4B model is reliable but too big or slow for the target devices.
- **Voice-to-function-calling pipeline** — Put a small ASR model in front of a fine-tuned function-calling model that maps free text to one of about 10 device functions. *When:* Devices with complex settings menus where users should state an outcome by speaking.
- **Two-stage on-device dictation pipeline** — Run an ASR model, then a separate text policy model that removes filler words and biases output toward personal names and terms. Both are fine-tuned tiny Gemma models. *When:* A feature that would otherwise need a cloud subscription, and must work offline with good quality.
- **Memory budgeting for on-device LLMs** — Add up weights, KV cache, runtime and OS overhead. Use mixed low-bit quantization and per-layer embeddings to shrink the weights first. *When:* Deciding whether a model fits a device with limited DRAM.
- **Multi-token prediction (MTP) for decode speed** — Enable MTP in the runtime. The speaker reports about 2x faster decoding, depending on the task. *When:* Decode speed is the bottleneck on a small device and the model supports MTP.
- **Frame budgeting for NPU vision** — Estimate tokens per image (about 500 for medium resolution, 1120 for high) and check the NPU prefill rate to see how many frames per second can be processed. *When:* Near-real-time vision on an IoT or robotics NPU.
- **Side-task tiny model** — Run a very small model alongside the main model for a background job such as system health, instead of sharing the large model. *When:* The LLM is one minor feature among many in an app or device.

## Numbers
- Raspberry Pi 3 16 GB price is up about 2.5x since launch. ([3:28](https://youtu.be/hacEQHHhu2Q?t=208))
- Small (1 to 4B) models need about 4 to 8 GB DRAM; the speaker's rule of thumb for deploying Gemma E2B on a device is 4 GB or more. ([4:50](https://youtu.be/hacEQHHhu2Q?t=290))
- Gemma E2B text-only weights are about 841 MB, at about 2.9 bits per weight with mixed 2/4/8-bit quantization. Active RAM is about 2 GB with KV cache and runtime. ([6:17](https://youtu.be/hacEQHHhu2Q?t=377))
- E2B reasoning is on par with a Gemma 3 model about twice its size from 12 months earlier (speaker's comparison, size not stated precisely). ([6:17](https://youtu.be/hacEQHHhu2Q?t=377))
- Gemma E2B decode on Raspberry Pi is about 7.6 tokens/s without MTP; MTP is about 2x faster depending on task. ([7:43](https://youtu.be/hacEQHHhu2Q?t=463))
- Jetson or Nano board decode is up to about 24 tokens/s with the team's toolchain. ([7:43](https://youtu.be/hacEQHHhu2Q?t=463))
- Qualcomm IoT board NPU: about 4,000 tokens/s prefill and 31 tokens/s decode. ([7:43](https://youtu.be/hacEQHHhu2Q?t=463))
- A medium-resolution image is about 500 tokens and a high-resolution image about 1,120 tokens. The speaker says about 3 high-res frames per second is feasible on the NPU. ([7:43](https://youtu.be/hacEQHHhu2Q?t=463))
- Tiny models range from about 50M to 500M parameters and need under about 2 GB RAM. ([12:43](https://youtu.be/hacEQHHhu2Q?t=763))
- FunctionGemma-based mobile actions model: about 45 tokens/s decode on the reference device (vs mid-single digits on Raspberry Pi for the 2B model), 10 output functions, over 86% call reliability. ([14:56](https://youtu.be/hacEQHHhu2Q?t=896))
- Synthetic fine-tuning data needed: about 10,000 to 10 million samples to reach high reliability in a small model. ([16:18](https://youtu.be/hacEQHHhu2Q?t=978))

## Hot takes
- For a narrow task, a fine-tuned sub-500M model on synthetic data can match or beat a 2 to 4B model on that task while being faster and running on more devices.
- DRAM cost, not compute, is now the main constraint for edge AI, and it outweighs the research focus on large MoE models.
- Voice-to-function-calling on device is now robust enough to ship, given a large enough synthetic dataset.

## Tools mentioned
LiteRT-LM, LiteRT / MediaPipe, Gemma 3, Gemma E2B, FunctionGemma, Gemma 4, AI Edge Gallery app, Apple FastVLM, Hugging Face (Mobile Actions dataset), Raspberry Pi, Jetson Nano, Qualcomm IoT boards (NPU), Chrome built-in summarization and proofreading APIs

## Relevance to our work
- **agentos** (1/3): InfraCraft already covers quantization, speculative decoding and a single-GPU scheduler. The talk's point that a fine-tuned tiny model can handle a narrow job could apply to a cheap classifier in the Govrix Scout scan path, but the talk targets phones and robots, not a server. → *Benchmark a small synthetic-data fine-tuned classifier against the current PII or prompt-injection scanner on latency and accuracy, to see whether the scanner path can run on a cheaper model.*
- **general** (1/3): Recurring interest in cheap-model (Haiku) pipelines. The talk gives a concrete playbook for when to fine-tune a small model on synthetic data and when to use off-the-shelf models instead. → *Read the Mobile Actions dataset and the synthetic-data fine-tuning method, and compare it with using a Haiku call for a narrow structured-extraction step.*
