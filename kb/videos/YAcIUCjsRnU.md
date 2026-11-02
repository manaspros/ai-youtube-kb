# Inkling: This Open-Weight Model Wants To Be Fine Tuned

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `YAcIUCjsRnU` · [watch](https://youtu.be/YAcIUCjsRnU) · **date:** 2026-08-02 · **length:** 6:41 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Warren · **orgs:** Thinking Machines, Better Stack, Harvey, Hugging Face
- **topics:** models-research, training-finetuning-rl, voice-multimodal · **tags:** open-weight, fine-tuning, tinker, mixture-of-experts, multimodal, raw-audio, lora, distillation, fine-tune-vs-rag, thinking-effort

> Better Stack walks through Thinking Machines' open-weight "Inkling" model: a MoE that takes raw audio and image patches, positioned as a base for fine-tuning on Tinker rather than a general frontier model.

## Summary
The host introduces Inkling, the first open-weight model from Thinking Machines, released under Apache 2.0 with weights on Hugging Face. The model is explicitly not meant to compete with frontier generalists; its intended use is fine-tuning on the Tinker platform. Benchmarks cited show it ahead on instruction following but well behind on Terminal Bench, which tests agents doing multi-step work. Architecturally it is a mixture-of-experts model (975B total, about 41B active per token) that accepts text, images and raw audio in one token space, rather than routing audio and images through a transcriber or captioner first. The video then gives a rule of thumb for when fine-tuning beats retrieval (behavior, format, distillation of narrow tasks) and when it does not (knowledge gaps, reasoning). A Harvey legal citation-extraction case study and a Tinker demo, where the model fine-tunes itself with LoRA after being told to avoid the letter E, illustrate the workflow. The host's bottom line is that Inkling is worth trying mainly for narrow, high-volume jobs with labeled data and especially when audio input matters.

## Key ideas
- **Inkling is positioned as a fine-tuning base, not a general model** — The host says the lab is upfront that Inkling is weaker than general frontier models, and its real goal is to be fine-tuned on the Tinker platform. Apache 2.0 weights are on Hugging Face. ([0:00](https://youtu.be/YAcIUCjsRnU?t=0))
- **Benchmarks show a clear split between instruction following and agentic work** — Inkling beats GLM 5.2 on instruction following (79.8 vs 73.3) but loses badly on Terminal Bench (63.8 vs 82.7). The host reads this as good at following orders, much weaker at working things out on its own. ([0:52](https://youtu.be/YAcIUCjsRnU?t=52))
- **Mixture-of-experts with sparse activation** — 975B total parameters, 256 unique experts per layer, and each token is routed to 6 experts, so about 41B parameters do work per token. ([0:52](https://youtu.be/YAcIUCjsRnU?t=52))
- **Raw audio and image patches go straight into the language model** — Most multimodal models put a speech model or vision captioner in front of the LLM, which loses information. Inkling feeds audio as a spectrogram (frequency bands in buckets) and images as 40x40 pixel patches, into the same space as text tokens, so nothing is compressed into a text description first. ([2:03](https://youtu.be/YAcIUCjsRnU?t=123))
- **Fine-tune to change how a model answers, use retrieval for what it knows** — Rule of thumb: fine-tuning teaches tone, rigid structured output and narrow behavior, especially where thousands of in-context examples would be impractical in cost or latency. If the model lacks knowledge, don't fine-tune. Fine-tuning can also degrade chain-of-thought, and smaller models suffer most. ([2:54](https://youtu.be/YAcIUCjsRnU?t=174))
- **Narrow-task fine-tuning of a small model can beat a large general model** — Harvey trained a small model to extract citations from legal documents. F1 rose from 0.56 to 0.68. Against GPT-4.0 head to head, the small model won or tied 93% of the time and ran faster. ([3:40](https://youtu.be/YAcIUCjsRnU?t=220))
- **Self-driven fine-tuning via Tinker** — In a demo, Inkling was told to never use the letter E. It then built its own training dataset and ran the fine-tune through Tinker. The result was a model that avoids E while still producing coherent answers. Training uses LoRA, which freezes base weights and trains small low-rank matrices. ([4:15](https://youtu.be/YAcIUCjsRnU?t=255))
- **Two differentiators: raw audio and a continuous thinking-effort slider** — Among Tinker-supported models, Inkling is the only one that takes raw audio; others handle images (Kimi, most Qwen) but not sound. Thinking effort is a 0-to-1 slider where most models offer 2-3 discrete levels (gpt-oss offers low/medium/high). ([5:17](https://youtu.be/YAcIUCjsRnU?t=317))

## Techniques
- **Decide fine-tune vs retrieval by failure type** — If the model lacks facts, add retrieval. If it needs a consistent tone, rigid structured output, or behavior that would take thousands of in-prompt examples, fine-tune. Check whether reasoning degrades after tuning. *When:* Before choosing between RAG and fine-tuning for a narrow, high-volume task with labeled data and a way to grade output.
- **Distill a narrow task from a general model into a small fine-tuned model** — Collect labeled examples for one task, fine-tune a small open model on them, then compare head to head against the large general model on F1 or win rate, with latency as a second metric. *When:* When a general model is too expensive or slow for a repeated narrow job (the Harvey citation-extraction example).
- **Let the model generate its own fine-tuning dataset via Tinker** — Describe the target behavior in natural language (the demo used no letter E); the model builds the training set and runs the full fine-tune on Tinker. The video shows the prompt only, not the exact commands or config. *When:* For quick behavior-shaping experiments where hand-building a dataset is slower than iterating on a description.
- **Feed raw audio directly to the model for tasks needing prosody or delivery** — Pass the audio clip into the multimodal model instead of a transcript so it can classify how something was said (speaking style) and not only what was said. Video cites cookbook recipes for speech recognition, speaking-style classification and dictated medical prescriptions. *When:* When tone, speaking style or pronunciation of domain terms matters and a transcript would drop that information.
- **Tune reasoning depth with the thinking-effort slider** — Set Inkling's thinking effort as a continuous value from 0 to 1 rather than picking one of 2-3 discrete levels. *When:* When you need finer control over the latency-versus-reasoning trade-off than discrete effort levels allow.

## Numbers
- Model size: 975B total parameters, about 41B active per token, 256 experts per layer, 6 experts routed per token ([0:00-0:52](https://youtu.be/YAcIUCjsRnU?t=0))
- Instruction following: Inkling 79.8 vs GLM 5.2 73.3 ([0:52](https://youtu.be/YAcIUCjsRnU?t=52))
- Terminal Bench: Inkling 63.8 vs 82.7 for the comparison model ([0:52](https://youtu.be/YAcIUCjsRnU?t=52))
- Image input uses 40x40 pixel patches ([2:03](https://youtu.be/YAcIUCjsRnU?t=123))
- Harvey citation extraction F1 rose from 0.56 to 0.68 after fine-tuning ([3:40](https://youtu.be/YAcIUCjsRnU?t=220))
- Fine-tuned small model won or tied against GPT-4.0 93% of the time in Harvey's head-to-head, and ran faster ([3:40](https://youtu.be/YAcIUCjsRnU?t=220))
- Thinking effort is a continuous 0-1 slider; gpt-oss offers 3 discrete levels ([5:17](https://youtu.be/YAcIUCjsRnU?t=317))

## Hot takes
- Inkling is not worth using as a general model; the host says the value is fine-tuning and audio input.
- Fine-tuning can make reasoning worse, and smaller models are hit hardest; the host frames this as a reason to be careful with tuning for reasoning tasks.
- Only Inkling among Tinker models takes raw audio, which the host calls a standout feature.
- The Harvey result is a single customer anecdote and is presented as a vendor-style success story, not independent evaluation.
- The video's own benchmark data shows Inkling trailing badly on agentic (Terminal Bench) work, which the host states plainly.

## Tools mentioned
Inkling (Thinking Machines open-weight MoE model), Tinker (fine-tuning platform), LoRA, Hugging Face, GLM 5.2, GPT-OSS, GPT-4.0, Kimi K3, Qwen, DeepSeek, NVIDIA Nemotron

## Relevance to our work
- **general** (2/3): The fine-tune-vs-RAG rule of thumb and the distillation example (small model beating a large one on a narrow task) apply to cheap-model pipelines, which is a recurring interest. → *Read the Harvey case-study claims against the original source before citing them; the video is a secondhand summary.*
- **agentos** (1/3): An open-weight, fine-tunable multimodal base could fit a narrow-task model path, and the fine-tune-vs-retrieval split is a useful lens for MemoryMesh, but the video gives no serving or deployment details relevant to InferCraft. → *Note Inkling as a candidate base for a narrow labeled task. Before adopting, verify its serving stack works with vLLM on one RTX 5090, since the video does not cover it.*
