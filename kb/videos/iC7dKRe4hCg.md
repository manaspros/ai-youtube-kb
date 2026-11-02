# Olmo3 Is What ‘Open Weights’ Was Supposed to Mean

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `iC7dKRe4hCg` · [watch](https://youtu.be/iC7dKRe4hCg) · **date:** 2026-01-02 · **length:** 5:23 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** AI2, Meta, Mistral, OpenAI, Anthropic
- **topics:** models-research, local-ai · **tags:** olmo-3, olmo-3.1, open-weights, olmotrace, dolma-3, reasoning-models, molmo-2, ai2, local-models, data-provenance

> Short overview of AI2's fully open Olmo 3 and 3.1 models: sizes, the released data and training scripts, OlmoTrace output attribution, and the gaps versus closed models.

## Summary
The video introduces Olmo 3 and Olmo 3.1 from AI2, a non-profit, in three variants (Base, Think, Instruct) at 7B and 32B sizes. The speaker's main claim is that AI2 releases far more than weights: the Dolma 3 dataset (about 9T tokens), full training and RL scripts, and intermediate checkpoints. OlmoTrace is shown tracing a model's output back to matching training documents with source URLs, under Apache 2.0 with no usage restrictions. The speaker runs the Think variant in the AI2 Playground on a Rust Fibonacci-with-memoization prompt and a travel-time word problem, and reports benchmark figures (about 96% math, about 91% HumanEval+, and roughly +5 on AIME for 3.1) with a caveat not to over-trust them. The reality check is that Olmo 3 lags closed models on general chat and broad knowledge, accepts text only, is English-focused, and hallucinates more than closed models. Molmo 2, a multimodal follow-up with video, was mentioned as recently released. The video is short and mostly a demo with unsourced numbers.

## Key ideas
- **Olmo 3 comes in Base, Think (reasoning with chain-of-thought traces) and Instruct (chat and tool use) variants.** — Speaker positions Base as purely pre-trained, Think as reasoning-optimized, and Instruct as chat and tool-use ready. ([0:00](https://youtu.be/iC7dKRe4hCg?t=0))
- **Sizes split by hardware: 7B runs on a laptop, 32B needs a high-end GPU.** — The speaker demos both sizes and says the 32B is heavy. No VRAM figure is given. ([0:59](https://youtu.be/iC7dKRe4hCg?t=59))
- **The openness is the differentiator: data, training and RL scripts, and intermediate checkpoints are all released.** — Contrasted with labs that drop weights only. The speaker frames it as enabling auditing, fine-tuning, adding your own data and fixing biases. ([0:59](https://youtu.be/iC7dKRe4hCg?t=59))
- **OlmoTrace links generated text back to the training documents that match it.** — Shows highlighted spans and source URLs next to the output, so the reader can judge source trustworthiness. The speaker frames this as transparency closed models do not offer. ([1:51](https://youtu.be/iC7dKRe4hCg?t=111))
- **Licensing is permissive: Apache 2.0, local use, no usage restrictions.** — Stated by the speaker alongside the OlmoTrace demo. ([1:51](https://youtu.be/iC7dKRe4hCg?t=111))
- **Benchmark claims are favorable but come with a caveat, and the 3.1 update adds gains.** — Speaker cites Think 32B at about 96% math and about 91% HumanEval+, calls it the strongest fully open reasoning model, and says 3.1 adds about +5 on AIME with gains on instruction following. He asks viewers to take this with a grain of salt. ([3:12](https://youtu.be/iC7dKRe4hCg?t=192))
- **Honest limits: lags on general chat and broad knowledge, text-only, English-focused, more hallucination than closed models.** — Speaker says it does not top Claude Sonnet or o1 on many tasks and closed labs still win on versatility. Molmo 2 is flagged as the multimodal, video-capable follow-up. ([4:20](https://youtu.be/iC7dKRe4hCg?t=260))

## Techniques
- **Output provenance check with OlmoTrace** — Run a prompt in the AI2 Playground on an Olmo 3 model. Read the output next to the matched training-data spans and their source URLs, then judge whether the cited sources are trustworthy. No CLI or config is shown. *When:* When you need to audit whether an answer closely echoes specific training text, or to judge sources behind a claim.
- **Ad hoc two-prompt check of a reasoning variant** — Run the Think variant on (1) a coding prompt: implement Fibonacci in Rust with recursion plus memoization, with test cases at larger inputs; and (2) a multi-step word problem: total travel time. Judge the reasoning by reading the output. The speaker does not use a scoring harness. *When:* As a quick qualitative sanity check before testing a model for agent or reasoning work. Use a real eval for anything you need to trust.
- **Inspect the full training recipe before fine-tuning** — Use the released Dolma 3 dataset, training and RL scripts, and intermediate checkpoints to see how a stage was produced. The speaker proposes this for fine-tuning on your own data and bias fixing, but shows no steps. *When:* When you need data-level or stage-level inspection rather than just weights, for example for auditing or custom post-training.

## Numbers
- Olmo 3 reportedly rivals Qwen3 with about six times fewer training tokens (speaker's claim, not sourced). ([0:00](https://youtu.be/iC7dKRe4hCg?t=0))
- Dolma 3 dataset is about 9 trillion tokens total. ([0:59](https://youtu.be/iC7dKRe4hCg?t=59))
- Two sizes: 7B (laptop-capable) and 32B (needs a higher-end GPU). ([0:59](https://youtu.be/iC7dKRe4hCg?t=59))
- Think 32B scores about 96% on math and about 91% on HumanEval+ (speaker's reported figures). ([3:12](https://youtu.be/iC7dKRe4hCg?t=192))
- Olmo 3.1 gains about +5 on AIME over Olmo 3, plus gains on instruction following and hard reasoning benchmarks. ([3:12](https://youtu.be/iC7dKRe4hCg?t=192))
- Olmo 3 is trained on far less data than Qwen3 but is described as neck and neck on reasoning and code. ([3:12](https://youtu.be/iC7dKRe4hCg?t=192))

## Hot takes
- Speaker calls Olmo 3 the strongest fully open reasoning model, which is a comparative claim with no independent benchmark source in the video.
- The 'six times fewer training tokens' comparison is unsourced.
- Speaker says closed models will still beat Olmo 3 on many tasks and that closed labs keep winning on versatility.
- Speaker calls AI2 a non-profit counterweight, contrasting it with OpenAI and Anthropic, who he says are after revenue.
- Title framing ('what open weights was supposed to mean') is more hype than the content, which is a brief demo with few details.

## Tools mentioned
Olmo 3, Olmo 3.1, Olmo 3 Base, Olmo 3 Think, Olmo 3 Instruct, OlmoTrace, Dolma 3, AI2 Playground, Molmo 2, Qwen3 (transcribed as QEM3/QEN3), Claude Sonnet, OpenAI o1, Rust

## Relevance to our work
- **agentos** (1/3): Open, self-hostable 7B and 32B models with released data could be candidates for the InferCraft serving tier. The video gives no VRAM or throughput numbers for the RTX 5090, and OlmoTrace-style provenance is only loosely relevant to evals. → *Benchmark Olmo 3 32B Think served under vLLM on the RTX 5090 against the current InferCraft default, recording VRAM and tokens per second, since the video gives neither.*
