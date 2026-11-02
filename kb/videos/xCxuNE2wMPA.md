# Llama 4 Has a 10M Token Context Window... (and its the best)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `xCxuNE2wMPA` · [watch](https://youtu.be/xCxuNE2wMPA) · **date:** 2025-11-02 · **length:** 4:16 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Meta, Hugging Face, OpenRouter, Groq, LM Arena
- **topics:** models-research, local-ai, context-engineering · **tags:** llama-4, open-weights, mixture-of-experts, long-context, multimodal, distillation, model-release, lm-arena

> Better Stack recap of Meta's Llama 4 launch: open-weight Scout and Maverick (MoE, 17B active) with a claimed 10M-token context, plus the unreleased Behemoth teacher model. All benchmark and efficiency claims are Meta's, repeated without independent checks.

## Summary
The video is a four-minute news recap of Meta's Llama 4 release. It covers two downloadable open-weight models, Llama 4 Scout and Llama 4 Maverick, both described as natively multimodal mixture-of-experts models with 17B active parameters. Scout is pitched with a 10M-token context window and a claim that it fits on a single H100. Maverick is pitched on cost-efficiency, citing an experimental LM Arena ELO of 1,417 and a claim that it matches DeepSeek V3 on reasoning and coding with under half the parameters. Llama 4 Behemoth (288B active, nearly 2T total) is previewed but not released, and is described as the teacher for the smaller models through distillation. The speaker also summarises Meta's training scale (30T+ tokens across 200 languages, 32,000 GPUs) and its three-step post-training recipe. Nearly everything is restated from Meta's launch materials; the video shows no independent evaluation or long-context testing.

## Key ideas
- **Scout and Maverick are released as open-weight, natively multimodal models, downloadable from Llama.com or Hugging Face and usable through hosted providers.** — Behemoth is only previewed. The speaker presents the open-weight release as the main news. ([0:00](https://youtu.be/xCxuNE2wMPA?t=0))
- **Scout's headline feature is a claimed 10M-token context window (about 5M words) and a claim that it fits on a single H100.** — Use cases the speaker lists are multi-document summarisation, passing large user-activity logs, and reasoning over codebases. The speaker presents these as expectations, not tested results. ([0:00](https://youtu.be/xCxuNE2wMPA?t=0))
- **Maverick is positioned on performance per parameter: 128 experts, about 17B active, and a claim that it matches DeepSeek V3 on reasoning and coding with less than half the parameters.** — The speaker cites an experimental Maverick ELO of 1,417 on LM Arena as evidence of the best performance-to-cost ratio. ([1:09](https://youtu.be/xCxuNE2wMPA?t=69))
- **Behemoth is a teacher model, not a product: 288B active parameters, 16 experts, nearly 2T total. Meta used it to produce the smaller models, and it is previewed but not released.** — The speaker says Behemoth beats GPT-4.5, Claude Sonnet 3.7 and Gemini 2.0 Pro on STEM benchmarks (MATH-500, GPQA Diamond). These numbers cannot be checked because the model is unreleased. ([2:18](https://youtu.be/xCxuNE2wMPA?t=138))
- **Mixture-of-experts is the efficiency mechanism: a large total parameter count, with only a few experts (about 17B parameters for Maverick) active for any token.** — The speaker's analogy is a company of specialists where only the most relevant ones are called on a given task. Maverick has about 400B total parameters. ([2:18](https://youtu.be/xCxuNE2wMPA?t=138))
- **Pretraining scale was over 30T tokens of text, images and video in 200 languages, which the speaker describes as more than twice the data of earlier Llama versions.** — The largest model's training used 32,000 GPUs, each at about 390 trillion operations per second. These are figures from Meta's materials, relayed by the speaker. ([2:18](https://youtu.be/xCxuNE2wMPA?t=138))
- **Post-training ran in three stages: supervised examples, trial-and-error learning, then fine-tuning on quality preferences.** — The speaker does not name the algorithms, so the video offers only the high-level order of the stages. ([2:18](https://youtu.be/xCxuNE2wMPA?t=138))
- **Behemoth's capability is moved into the smaller models by distillation, which the speaker says gives near-teacher performance at much lower inference cost.** — This is the most transferable idea in the video, but the speaker gives no measurements to support the near-teacher claim. ([3:35](https://youtu.be/xCxuNE2wMPA?t=215))

## Techniques
- **Teacher-to-student distillation for deployable models** — Train a very large model (Behemoth) first, then transfer its behaviour into smaller models that are cheaper to serve. The speaker describes this as compressing the teacher's capability into deployment-friendly architectures. *When:* When you need a small, cheap model to inherit capability from a large model you can only run during training or for generating data.
- **Sparse mixture-of-experts for cheaper inference** — Keep a large total parameter count split across many experts, and activate only a few per token (for example, about 17B active out of roughly 400B total for Maverick). Quality comes from total capacity while per-token compute stays low. *When:* When you want a high-capacity open model that is cheaper to serve than a dense model of the same total size, and you can accept the memory cost of holding all the experts.
- **Three-stage post-training recipe** — Apply supervised fine-tuning on curated examples, then trial-and-error learning, then fine-tuning on quality preferences. The speaker gives this order only, without algorithm or data details. *When:* As a high-level reference for how a frontier open-weight model is typically post-trained. It is not enough to reproduce the recipe.

## Numbers
- Scout context window of 10M tokens, roughly 5M words (speaker's figure) ([0:00](https://youtu.be/xCxuNE2wMPA?t=0))
- Scout: 17B active parameters, 16 experts; claimed to fit on a single H100 ([0:00](https://youtu.be/xCxuNE2wMPA?t=0))
- Maverick: 17B active parameters, 128 experts; experimental version ELO 1,417 on LM Arena ([1:09](https://youtu.be/xCxuNE2wMPA?t=69))
- Behemoth: 288B active parameters, 16 experts, nearly 2T total; previewed, not released ([2:18](https://youtu.be/xCxuNE2wMPA?t=138))
- Maverick has about 400B total parameters but uses about 17B at any moment ([2:18](https://youtu.be/xCxuNE2wMPA?t=138))
- Pretraining on over 30 trillion tokens of text, images and video in 200 languages; about twice the knowledge of previous versions (speaker's paraphrase) ([2:18](https://youtu.be/xCxuNE2wMPA?t=138))
- Largest model trained on 32,000 GPUs, each at about 390 trillion calculations per second ([2:18](https://youtu.be/xCxuNE2wMPA?t=138))

## Hot takes
- The title ('and its the best') is hype. The four-minute video mostly restates Meta's launch claims and shows no independent evaluation, long-context test, or third-party benchmark.
- The 10M-token context and the 'best in class' multimodal claims are vendor-reported. Nothing in the video checks whether quality holds at long context lengths.
- Behemoth's benchmark wins over GPT-4.5, Claude Sonnet 3.7 and Gemini 2.0 Pro cannot be verified because the model is not released.
- The 'near teacher-level' claim for distilled models comes with no numbers.
- Transcript auto-captions misspell several names: 'Sonic 3.7' is Sonnet 3.7, 'Gemini 2 Flashlight' is Gemini 2 Flash-Lite, 'DeepSeat' is DeepSeek, 'GPT-40' is GPT-4o, and 'Grok' is probably Groq.

## Tools mentioned
Llama 4 Scout, Llama 4 Maverick, Llama 4 Behemoth, Llama.com, Hugging Face, OpenRouter, Groq (transcript says 'Grok'), LM Arena, GPT-4.5, Claude Sonnet 3.7, Gemini 2.0 Pro, Gemma 3, Gemini 2.0 Flash-Lite, Mistral 3.1, GPT-4o, Gemini 2.0 Flash, DeepSeek V3, H100 GPU, MATH-500, GPQA Diamond

## Relevance to our work
- **agentos** (1/3): Adds two open-weight MoE candidates for the InferCraft model set and a long-context claim relevant to context engineering. The single-GPU claim is worth checking against our one-GPU setup, but the video offers no evidence for it. → *Add Llama 4 Scout and Maverick as candidates in the next InferCraft model comparison. Verify the 10M-token claim with our own long-context retrieval test before relying on it in MemoryMesh or context-window design.*
