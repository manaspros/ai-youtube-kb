# Frontier results, on device - RL Nabors, Arize

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `fWXJM-J0ZB8` · [watch](https://youtu.be/fWXJM-J0ZB8) · **date:** 2026-07-18 · **length:** 30:52 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Rachel Lee Neighbors · **orgs:** Arize, Mozilla, W3C, Microsoft, Google, Meta
- **topics:** local-ai, inference-serving, evals, context-engineering · **tags:** small-language-models, on-device-inference, model-right-sizing, golden-dataset, llm-as-judge, prompt-engineering, regression-evals, phoenix, p95-latency, few-shot

> Rachel Lee Neighbors shows how to right-size a model: prototype with a frontier model, build a golden eval set, then pick the smallest local model (Llama 3.2 3B) that meets latency and quality targets, closing the gap with prompt changes and deterministic post-processing.

## Summary
The speaker argues that many LLM calls do not need a frontier model and cites security, latency (4-second believability limit), cost, and offline-availability as reasons to move work to small or on-device models. Her method is "prototype big, deploy small": first prove the task is possible with the largest model, then build a golden dataset of inputs and outputs from that model's answers (14 threads, 28 examples in her case). She scores candidates on JSON validity, reference structural validity, factual consistency, length compliance, and P50/P95 latency, using Phoenix (Arize's open-source tool) for experiments. Among the small models tested, Llama 3.2 3B gave the best accuracy-latency trade-off, while Qwen 2.5 was fastest but least accurate and Gemma 4 E2B was slow (around 8 seconds). A few-shot prompt was the only prompt variant that clearly helped, and explicit negative rules made results worse. The remaining gap was closed in post-processing: truncating summaries and checking that reference counts fit the thread, while the Claude-based judge was seen as too strict. She ends by recommending regression evals in CI so future model or prompt changes do not degrade output.

## Key ideas
- **Frontier models are costly beyond token price** — She frames costs as security exposure of data sent to remote servers, latency above about 4 seconds losing users, unpredictable agentic token spend, and failure when offline. Token prices fall, but total spend rises with agentic and reasoning workloads. ([0:01](https://youtu.be/fWXJM-J0ZB8?t=1))
- **Ask whether the job needs an LLM at all** — Use task-specific models for vision (MobileNet, YOLO, MediaPipe) and audio (Whisper), and small language models for chat, translation or analysis when multimodal breadth and world knowledge are not needed. ([2:13](https://youtu.be/fWXJM-J0ZB8?t=133))
- **Prototype big, deploy small** — Use the largest model first to confirm the task is possible at all, then move the production path to smaller or specialized models. Her framework was built with Google and published on web.dev. ([9:12](https://youtu.be/fWXJM-J0ZB8?t=552))
- **Define success before choosing a model** — Build a golden dataset of inputs and outputs (human-labeled where possible) and decide metrics first. Her metrics: JSON parse validity, reference structural validity, factual consistency, length compliance, and P50/P95 latency. ([10:23](https://youtu.be/fWXJM-J0ZB8?t=623))
- **Pick the smallest acceptable model, not the most popular one** — Qwen 2.5 was fastest but least accurate, Gemma 4 E2B was slow, and Llama 3.2 3B had the best accuracy-latency balance. She warns that the model peers recommend may not fit your task. ([15:07](https://youtu.be/fWXJM-J0ZB8?t=907))
- **Change one variable per prompt variant** — She tested a baseline plus four variants (numbered input, few-shot, strict rules, chain-of-thought). Few-shot won on length and accuracy for about 200 ms extra latency, and explicit negative rules made results worse. ([20:56](https://youtu.be/fWXJM-J0ZB8?t=1256))
- **Close the remaining gap with deterministic post-processing and inspect judges** — Truncating long summaries and checking reference counts against thread size brought JSON and structural validity to 100%. Claude as judge was too strict and favored its own sibling model, so she read the raw outputs herself. ([26:16](https://youtu.be/fWXJM-J0ZB8?t=1576))
- **Keep regression evals running in CI** — Rerun the golden set whenever the model or prompt changes so that summaries do not grow or hallucinate after an upgrade. ([27:33](https://youtu.be/fWXJM-J0ZB8?t=1653))

## Techniques
- **Prototype-big-deploy-small pipeline** — Validate feasibility with a frontier model, record its outputs as a golden set, then test models from smallest to largest and pick the smallest one that passes the bar (the 'SAGE' model). *When:* Starting a new LLM feature or moving a high-volume LLM call to cheaper or on-device inference.
- **Golden dataset with multi-metric eval in Phoenix** — Store curated JSONL input-output pairs. Score JSON parse, reference validity against real thread entries, factual consistency, length, and P50/P95 latency per model in a Phoenix experiment, then open the raw outputs to compare. *When:* Comparing candidate models or prompts for a structured-output summarization task.
- **Latency budget by percentile** — Set a P50 target (about 1 to 1.5 seconds) and a P95 target (about 3.5 seconds), using 4 seconds as the point where users feel disconnected. *When:* Choosing a model for user-facing, interactive AI features.
- **Single-variable prompt ablation** — Keep the baseline prompt and change one thing per variant (input format, few-shot examples, explicit rules, chain-of-thought), then measure each against the golden set. *When:* Improving a small model's output without retraining or shipping a new model.
- **Deterministic post-processing instead of prompt tuning** — Enforce constraints in code: truncate over-long output, validate that reference indices exist in the source, and reject outputs that fail JSON parsing. *When:* A small model misses a structural or length rule that code can check more cheaply than a prompt can enforce.
- **Auditing the LLM judge** — Check whether the judge model is biased toward its own family or too strict. Read the disputed examples to decide whether the metric or the judge is wrong. *When:* Using an LLM-as-judge to score factual consistency across models.
- **Regression evals in CI** — Run the golden set as a test suite on every model swap or prompt change, failing the change if quality or latency drops. *When:* Maintaining an LLM feature that will receive model or prompt updates.

## Numbers
- Research cited: about 4 seconds is the limit of believability for users waiting on an AI response ([1:17](https://youtu.be/fWXJM-J0ZB8?t=77))
- Small models: about 1B parameters fit in roughly 2 GB in FP16, and quantized (8-bit or 4-bit) models need less memory ([4:28](https://youtu.be/fWXJM-J0ZB8?t=268))
- Speaker's energy bar chart: an SLM uses about 25% of the energy an LLM uses for the same task, and a task-specific model about half of that ([5:44](https://youtu.be/fWXJM-J0ZB8?t=344))
- Baseline (Claude Sonnet) on 14 tasks: 2.9 s average latency and about $0.22 per run; she estimates about $1 per day of inference for her app ([14:00](https://youtu.be/fWXJM-J0ZB8?t=840))
- Model sizes and disk footprint: Qwen 2.5 1.5B about 1 GB; Llama 3.2 3B about 2 GB; Gemma 4 E2B 5B parameters at 3.1 GB ([15:07](https://youtu.be/fWXJM-J0ZB8?t=907))
- Model results: Qwen 2.5 about 1 s P50 but low accuracy; Llama 3.2 about 90% accuracy; Gemma 4 about 8 s latency ([16:15](https://youtu.be/fWXJM-J0ZB8?t=975))
- Golden dataset size: 14 threads, each with a short and a referenced summary, giving 28 examples ([11:29](https://youtu.be/fWXJM-J0ZB8?t=689))
- Llama 3.2 baseline prompt: reference accuracy 91.2%, factual correctness 87.1%, latency about 1 s ([23:15](https://youtu.be/fWXJM-J0ZB8?t=1395))
- Few-shot prompt on Llama 3.2 3B: structural validity 91.7%, factual consistency 92.9%; added about 200 ms latency. Chain-of-thought added about 600 ms ([24:18](https://youtu.be/fWXJM-J0ZB8?t=1458))
- Latency targets: P50 about 1 to 1.5 s, P95 about 3.5 s ([20:56](https://youtu.be/fWXJM-J0ZB8?t=1256))
- After post-processing: 100% JSON validity and 100% structural validity; P50 about 1 s; P95 about 3.5 s (transcript partly garbled here) ([27:33](https://youtu.be/fWXJM-J0ZB8?t=1653))
- Savings: about $1 per day in inference cost after moving to Llama 3.2 3B ([27:33](https://youtu.be/fWXJM-J0ZB8?t=1653))

## Hot takes
- Pick the smallest model that is good enough (what she calls the SAGE model) instead of the one engineers recommend most.
- Explicit negative rules made small models worse, while few-shot examples helped.
- A Claude judge scored Llama's outputs too strictly and favored its own family, so raw outputs should be checked by hand.
- Many LLM calls in a product could be handled by small or task-specific models.
- Post-processing in code can close quality gaps that prompt tuning cannot.

## Tools mentioned
Phoenix (Arize), Goose, Gemma 4 E2B, Gemma 3, Llama 3.2 3B, Qwen 2.5 1.5B, Qwen 3 1.7B, Claude Sonnet, Claude Opus, MobileNet, YOLO, MediaPipe, Whisper, Chrome Prompt API / Gemini Nano, Pixel 10 Pro

## Relevance to our work
- **agentos** (2/3): InferCraft runs vLLM on one RTX 5090 and already plans small-model and speculative-decoding work; this talk gives a concrete SAGE-model selection method and percentile latency budgets that could be applied there. → *Build a golden set from frontier-model outputs for one AgentOS summarization or classification task, then run a Phoenix-style capability eval across 3 to 4 small local models with P50/P95 gates before picking the default local model.*
- **general** (2/3): The 'prototype big, deploy small' flow with a golden set and regression evals matches how cheap-model (Haiku) pipelines should be validated before use, including for entity-resolution-style extraction. → *For any Haiku pipeline, record Sonnet or Opus outputs on 30 to 50 labeled cases, pick the cheapest model that passes, and keep that set as a regression suite.*
- **prosharness** (1/3): ProsHarness runs plan, critique and debate loops, and the talk's lesson on judge bias and code-side validation applies to those loops. → *Add deterministic checks (JSON parse, referenced-file existence) before the LLM critique step in the plan loop, and spot-check the critic's outputs for bias toward its own model family.*
