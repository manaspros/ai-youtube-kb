# Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ILdE7FaAjVA` · [watch](https://youtu.be/ILdE7FaAjVA) · **date:** 2026-06-18 · **length:** 13:26 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Audry Hsu · **orgs:** RunPod
- **topics:** inference-serving, infra-cost-scaling · **tags:** serverless GPU, cold start, vLLM, autoscaling, Hugging Face, model deployment, RunPod Hub, endpoint

> RunPod's intro walkthrough of deploying an open LLM (Qwen via vLLM) as a serverless GPU endpoint from its Hub in under five minutes; mostly a product pitch, with a useful look at cold starts and autoscaling settings.

## Summary
Audry Hsu of RunPod introduces the company as a GPU cloud and walks through the product lines: pods, serverless, clusters and the Hub. She focuses on serverless, which autoscales workers, bills per second only while a worker handles a request, and can keep some workers warm. The live demo deploys a Qwen model from a Hub listing, raising the max context length through a vLLM flag, then sends queued requests. The first request waited about 41 seconds in the queue, mostly cold start (container creation and model download), and execution took about 1.5 seconds. The talk is a short product intro, with a second session promised on the Python SDK. Company figures are self-reported and the talk gives no independent benchmarks.

## Key ideas
- **Serverless GPU endpoints suit bursty or real-time inference because workers scale to zero and you pay only while a request is being handled.** — Idle workers spin down, so no cost accrues when idle. Max-worker caps and spending caps limit scale-up. Active (always-on) workers avoid cold starts at a standing cost. ([5:08](https://youtu.be/ILdE7FaAjVA?t=308))
- **Cold start dominates first-request latency for a freshly deployed model.** — The first request waited about 41 seconds in the queue while containers were created and the model downloaded, versus about 1.5 seconds of actual execution. Later requests were much faster. ([11:21](https://youtu.be/ILdE7FaAjVA?t=681))
- **Hub listings are pre-vetted, ready-to-deploy repos with a Dockerfile and defaults, and the speaker presents them as the fastest way to start.** — Each listing is a GitHub repo with a Dockerfile and environment-variable configuration. Deploying one from the Hub is the quick path shown in the demo. ([7:21](https://youtu.be/ILdE7FaAjVA?t=441))
- **Deployment config options are passed straight through as vLLM serve flags.** — The speaker raised the max model length (context window) in the advanced options, and says the other settings such as max LoRA values map to vLLM flags too. ([8:28](https://youtu.be/ILdE7FaAjVA?t=508))
- **The default GPU pool is H100s with A100s as fallback, and pricing is a fraction of a cent per second.** — Billing covers only the time a worker is running and handling requests. Max workers can scale to a set number (15 in the demo). ([9:40](https://youtu.be/ILdE7FaAjVA?t=580))
- **Endpoints are plain HTTP APIs with built-in per-endpoint telemetry.** — The console shows request count, execution time and delay time per endpoint. Requests queue while workers initialize. ([11:21](https://youtu.be/ILdE7FaAjVA?t=681))

## Techniques
- **Serverless GPU autoscaling with warm workers** — Set a max-worker cap and spending cap, and keep a small number of active workers so the model stays loaded and responds without a cold start. *When:* Production inference APIs with spiky traffic where the cold-start penalty is unacceptable for some requests.
- **Deploy a model from a pre-vetted Hub listing** — Fork or deploy a community or RunPod-maintained repo that already has a Dockerfile, then override env vars or vLLM flags such as max model length in the advanced options. *When:* Standing up an open-source model quickly without writing a serving stack.
- **Cold-start awareness in latency budgets** — Measure queue delay and execution time separately in endpoint telemetry. Treat the first request after scale-from-zero as an outlier when judging p95 latency. *When:* Any scale-to-zero deployment where latency SLOs are being measured.

## Numbers
- Over 500,000 developers on the platform ([2:26](https://youtu.be/ILdE7FaAjVA?t=146))
- 30+ data centers worldwide ([2:26](https://youtu.be/ILdE7FaAjVA?t=146))
- 120 million USD annual recurring revenue (company claim) ([2:26](https://youtu.be/ILdE7FaAjVA?t=146))
- Under five minutes from Hub listing to a working serverless endpoint (speaker's demo) ([11:21](https://youtu.be/ILdE7FaAjVA?t=681))
- First request queued about 41 seconds, mostly cold start ([11:21](https://youtu.be/ILdE7FaAjVA?t=681))
- Execution time about 1.5 seconds once warm ([11:21](https://youtu.be/ILdE7FaAjVA?t=681))
- Default GPUs H100 with A100 backup; billing is a fraction of a cent per second ([9:40](https://youtu.be/ILdE7FaAjVA?t=580))
- Max workers example: scale up to 15 ([9:40](https://youtu.be/ILdE7FaAjVA?t=580))

## Hot takes
- GPU shortages are like COVID toilet-paper hoarding, and the market will recover as buyers better estimate compute needs.

## Tools mentioned
RunPod, vLLM, Hugging Face, Docker

## Relevance to our work
- **agentos** (1/3): AgentOS L2B InferCraft runs vLLM on a single local GPU. This talk shows a managed serverless vLLM option with cold-start behavior, which is a useful comparison point but not a change to the build. → *Compare the cold-start and queue-delay numbers here against InferCraft's serving latency when designing the scale-to-zero story, and decide whether the project needs a cold-start metric.*
- **general** (1/3): Practical reference for serverless GPU deploys of open models with vLLM. Useful background for cheap-model pipelines, but the talk is a product intro.
