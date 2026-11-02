# Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `SS-A8sE7hkw` · [watch](https://youtu.be/SS-A8sE7hkw) · **date:** 2026-06-18 · **length:** 20:52 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Gus Martins, Ian Ballantyne · **orgs:** Google DeepMind, OpenRouter, LM Arena
- **topics:** local-ai, models-research, inference-serving, governance-compliance · **tags:** gemma-4, open-weights, on-device, local-inference, sovereignty, licensing, mixture-of-experts, lm-studio, ollama, fine-tuning, function-calling, sub-agents

> Google DeepMind's Gemma team pitches open-weight Gemma 4 models (E2B to 31B) as a way to own, customize and run models locally, with on-device and single-GPU demos.

## Summary
Two Google DeepMind speakers present the Gemma 4 open-weight family as the "ownership" counterpart to the hosted Gemini models, arguing that some workloads need models you run on your own hardware. They describe four sizes: two small "effective" models (E2B, E4B) that run on phones and accept text, image and audio input, and two larger models (26B mixture-of-experts with about 4B active parameters, and a 31B dense model) that fit on one GPU. The talk argues the main reasons to choose open models are sovereignty, data that cannot leave the infrastructure, customization, and token-cost control for agentic workloads. A licensing change to Apache 2.0 for Gemma 4 is framed as the key move for legal adoption by governments and institutions. A live LM Studio demo runs the 26B model on a 48GB M4 Mac, fanning translation subtasks out to parallel sub-agents. The closing advice is to drop the model into existing workflows, build your own eval suite, and count serving and maintenance costs. Much of the content is product promotion, though the decision framework for offloading tasks is practical.

## Key ideas
- **Open models complement hosted frontier models** — The speakers say Gemini is the strongest model, but some situations need to own the model: run on your own hardware, customize it, or keep proprietary data inside your infrastructure. Gemma is positioned for those cases. ([1:08](https://youtu.be/SS-A8sE7hkw?t=68))
- **Effective-parameter small models are sized by accelerator memory** — E2B and E4B are described as about 5B raw parameters, but the per-layer embedding part can sit in other memory, so GPU memory needs only the roughly 2B or 4B active part. This is why they run on phones. Both take text, image and audio input and output text. ([2:27](https://youtu.be/SS-A8sE7hkw?t=147))
- **Mixture-of-experts gives capacity without full compute** — The 26B model has about 4B active parameters per step, so it needs roughly the memory and compute of a 4B model while keeping the capacity of a larger one. The 31B dense model is presented as the strongest. ([3:41](https://youtu.be/SS-A8sE7hkw?t=221))
- **Licensing is a sovereignty and adoption issue, not just a legal detail** — Custom licenses force legal review that can take many months, so the team moved Gemma 4 to Apache 2.0. The speakers present this as what lets sovereign institutions adopt the models. Examples mentioned are a Bulgarian fine-tune and a Brazilian Portuguese fine-tune. ([7:46](https://youtu.be/SS-A8sE7hkw?t=466))
- **Language fine-tuning gains are shrinking** — Because the base model is already strong in many languages, fine-tuning for one language may yield only small gains. The speaker says this may not be the best use of time, though multilingual quality is strong out of the box. ([9:09](https://youtu.be/SS-A8sE7hkw?t=549))
- **Agentic token costs make local compute more valuable** — Programming is one of the largest token-consuming categories in the OpenRouter report cited. As agents consume more tokens, owning or leasing GPU time for suitable tasks becomes more worthwhile. Frontier models are still kept for architecture-level work. ([10:33](https://youtu.be/SS-A8sE7hkw?t=633))
- **Decide what to offload using a threshold checklist** — Four criteria are proposed: whether the model is capable enough for the task, whether it fits the hardware, whether latency suits the use (seconds for interactive, relaxed for batch), and the cost, including sunk hardware versus leased GPUs. Scope is best for bounded tasks like refactoring, analysis and small code generation. ([11:38](https://youtu.be/SS-A8sE7hkw?t=698))
- **Local function calling works on a phone** — A demo app runs a model on a phone with a set of skills, such as calendar and maps actions, and the model picks and calls the right function. The speaker says Gemma 4 handles this more reliably than the previous generation. ([12:38](https://youtu.be/SS-A8sE7hkw?t=758))
- **Scheduling depends on execution location** — On device or self-hosted hardware, the question shifts from per-token cost to utilization: interactive tasks like a photo query need an immediate answer, while others can run in the background, such as when the phone is charging overnight. ([17:00](https://youtu.be/SS-A8sE7hkw?t=1020))
- **Drop-in OpenAI-compatible swap, then test on your own tasks** — The only code change needed is the base URL and model name when pointing an OpenAI-compatible client at a local server such as Ollama or LM Studio. The speakers advise checking where the model works and fails in your own workflow, because public benchmarks do not show task-specific quality. ([20:11](https://youtu.be/SS-A8sE7hkw?t=1211))

## Techniques
- **Drop-in local endpoint swap** — Keep the OpenAI-compatible client code and change only the base URL and model name to point at a local server such as Ollama or LM Studio. *When:* Trying an open model against existing agent or pipeline code with minimal change.
- **Local sub-agent fan-out for batch work** — An orchestrator splits one job (for example translating a document into many languages) into independent subtasks, each run as a sub-agent against a local model, then collects the outputs and assembles a final artifact. *When:* Bulk, offline, or private-data processing where per-token API cost would be high.
- **Threshold-based task routing** — For each task, check whether the model is capable enough, fits the available hardware, meets the latency need, and is cheap enough given sunk or leased compute. Send bounded tasks such as refactoring, analysis or small code modules to the local model and keep architecture-level work on frontier models. *When:* Deciding which parts of an agent workload to self-host versus call a hosted frontier model.
- **Latency-class scheduling for on-device tasks** — Classify work as interactive (answer in seconds) or background (run when the device is idle or charging) and schedule the local model accordingly. *When:* Designing on-device or self-hosted agent features with limited hardware.
- **Own-eval-first model adoption** — Build or extend your own evaluation suite on your real tasks, and judge the model on that rather than on general leaderboards. Include serving and maintenance cost in the decision. *When:* Before committing to moving a workload to an open model.

## Numbers
- E2B and E4B: about 5B raw parameters, but only about 2B and 4B need accelerator memory because the per-layer embedding part can live elsewhere ([2:27](https://youtu.be/SS-A8sE7hkw?t=147))
- 26B MoE model has about 4B active parameters; 26B model used about 26 GB RAM including context on a 48 GB M4 Mac ([3:41](https://youtu.be/SS-A8sE7hkw?t=221))
- Gemma 26B and 31B rank about 4th and 7th among open models on LM Arena ELO; several top-20 to top-30 models are described as 2 to 3 times larger, sometimes 20 times ([3:41](https://youtu.be/SS-A8sE7hkw?t=221))
- 31B model runs on one GPU, where competitors are said to need about 200 GB memory, roughly four or five GPUs ([5:03](https://youtu.be/SS-A8sE7hkw?t=303))
- A 300B-plus model may need multiple GPUs, whereas the 31B model fits on a single H100, A100, or even L4 ([15:04](https://youtu.be/SS-A8sE7hkw?t=904))

## Hot takes
- Most everyday tasks such as summarizing email do not need the most intelligent model in the world, so cheaper, smaller models are enough.
- Fine-tuning a strong model for one language may yield only about 1% gains, which may not be worth the effort.
- The thresholds for using a model change on-device: energy and idle utilization matter more than per-token price.

## Tools mentioned
Gemma 4, Gemini, Google AI Edge Gallery, LM Studio, Ollama, MedGemma, OpenRouter, LM Arena

## Relevance to our work
- **agentos** (1/3): AgentOS InferCraft runs local models on one RTX 5090 and already uses an OpenAI-compatible base URL, so Gemma 4 is a new candidate model for that stack, but the talk does not change the architecture. → *Add Gemma 4 26B-A4B (MoE) and 31B to InferCraft's model shortlist and benchmark tokens/s, KV-cache memory and task accuracy on the 5090 against the current baseline, using AgentOS's own task evals.*
- **general** (1/3): The threshold checklist (capability, hardware fit, latency, cost) is a reusable way to decide which steps of a cheap-model pipeline should run locally versus on a hosted model. → *When designing a cheap-model pipeline, write down per-step capability, latency and cost thresholds for local versus hosted execution before picking the model.*
