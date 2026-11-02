# Stop Guessing Your vLLM Config: Benchmarking LLMs on Runpod - Chris Vela, Runpod

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `P_0_Th_ZzIg` · [watch](https://youtu.be/P_0_Th_ZzIg) · **date:** 2026-10-28 · **length:** 16:29 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Chris Vela · **orgs:** RunPod
- **topics:** inference-serving, infra-cost-scaling, evals · **tags:** vllm, benchmarking, runpod, gpu-selection, concurrency, inter-token-latency, ttft, cold-start, self-hosting, kimi-k3, cuda-version, kv-cache, watchdog, fastapi

> RunPod's Chris Vela argues for benchmarking vLLM configs on GPU pods across concurrency levels before production, and previews an unreleased BenchPod template. Vendor pitch with some reusable method.

## Summary
Chris Vela, a forward deployed engineer at RunPod, argues that teams pick vLLM versions, GPUs and config knobs by guesswork and should measure instead. He frames the first questions as the task (coding agent versus simple summaries) and the expected concurrency, then says to pick a model and GPU that fit those. He demos a dashboard called BenchPod, an unreleased RunPod template built on vLLM's OpenAI-compatible server with a benchmark harness, live metrics, error scanning, a self-healing watchdog and a FastAPI layer that agents can call. In the demo he runs Kimi K3 at concurrency 1, 8, 64 and 192 and shows that raising the max batched tokens barely moves time-to-first-token but cuts inter-token latency, which speeds long jobs. He closes with a loop of picking a pod, comparing configs, testing with an agent, optimizing on the metric that matters (ITL, TTFT or TPOT), then scaling to multi-node or serverless. Much of the content is product promotion, and the template and its numbers are single-run demos.

## Key ideas
- **Decide the model and GPU from the workload and user count before chasing the frontier model** — The first questions are what the model is for (coding agent, long detailed tasks, or simple summaries) and how many concurrent users there will be. A smaller model on a cheaper machine can be enough, and he says a team may not need the largest model. ([1:21](https://youtu.be/P_0_Th_ZzIg?t=81))
- **Recent model releases often break on the wrong vLLM or CUDA version** — He says people fail on new models because they run an old or mismatched vLLM version, and that a version he cites (0.27) will not work for Kimi K3. For Kimi he says CUDA 12.8 fails and CUDA 13.0 works. Bleeding-edge model support is still unstable early on, so a model released the day before is not production-ready. ([2:21](https://youtu.be/P_0_Th_ZzIg?t=141))
- **Do not put a brand-new model straight into production** — He says the day after a release like Kimi K3 he would not ship it, and expects hallucinations and rough code paths. Wait for the stack to settle. ([3:36](https://youtu.be/P_0_Th_ZzIg?t=216))
- **Cold starts and weight downloads eat the time you need for config iteration** — Changing config means restarting the image and waiting for cold starts, including roughly 30 minutes for Kimi K3 to download and load weights. He reports about nine minutes of cold start on the pod and says a template that bakes in every vLLM version and a model list helps avoid this. ([9:12](https://youtu.be/P_0_Th_ZzIg?t=552))
- **Benchmark several concurrency levels and compare runs against each other** — In the demo the runs are at concurrency 1, 8, 64 and 192, and the runs can be compared side by side. The recipe baseline is the default to beat, not the end point. ([10:33](https://youtu.be/P_0_Th_ZzIg?t=633))
- **Raising max batched tokens lowered inter-token latency but not time-to-first-token** — The only knob changed in the demo was the max batched token count. Time to first token barely changed, but inter-token latency dropped noticeably, so long generations finished faster than with the vLLM recipe config. This is one run on one pod, not a general result. ([10:33](https://youtu.be/P_0_Th_ZzIg?t=633))
- **Ship on the metric you need (ITL, TTFT or TPOT), then scale** — The closing loop is: pick a pod, get a GPU, load the model, compare configs, have an agent test them, optimize on the metric the workload needs, ship the winner, then move to multi-node or serverless once demand scales. ([13:33](https://youtu.be/P_0_Th_ZzIg?t=813))
- **Expose benchmark and health data through an API so agents can read it, not just a dashboard** — BenchPod serves its metrics and error scans through FastAPI endpoints, and a watchdog self-heals the service. He says an internal Kimi instance went down one Sunday and recovered without users noticing, and that four nodes run internally. ([9:12](https://youtu.be/P_0_Th_ZzIg?t=552))

## Techniques
- **Config-sweep benchmarking before production** — Start a GPU pod with the model, then change the vLLM server config (it is a YAML config file) one knob at a time. Run the same benchmark at concurrency 1, 8, 64 and 192 for each config, and compare time-to-first-token, inter-token latency and total job time across runs. Pick the winner on the metric your workload needs and ship that config. *When:* Before deploying a new model or moving from prototype to production, and whenever you expect rising concurrency or long generations.
- **Tune max batched tokens for long generations** — Raise the vLLM max batched tokens setting while watching inter-token latency at high concurrency. In his demo this lowered inter-token latency and left time-to-first-token roughly flat. *When:* Workloads with long outputs (coding agents, long jobs) where per-token speed matters more than first-token latency.
- **Pin vLLM and CUDA to what the model needs** — Before deploying a new model, check the vLLM version it needs (not an older stable release) and the CUDA version. He says Kimi K3 failed on CUDA 12.8 and worked on 13.0. Build this check into your deploy process so mismatches show up before traffic does. *When:* Whenever a new open-weight model is released or a dependency upgrade is planned.
- **Agent-readable benchmark and health API** — Expose benchmark runs, GPU metrics, error scans and service health as HTTP endpoints, so an agent can start a run, read the results and decide on a config without a UI. Keep a watchdog that restarts the model server when it fails. *When:* When an agent is in the loop for tuning or ops, or when you want a single source of metrics for several model instances.
- **Model choice by task size and team size** — Ask what the model is for and how many people will use it before choosing size. He uses DeepSeek on 4 H200s for general work and reserves Kimi K3 for long detailed tasks. He suggests treating the frontier model as optional, not the default. *When:* Before sizing a self-hosted deployment, to avoid paying for a large node that the workload does not need.

## Numbers
- Kimi K3 context of about 1 million tokens; on a B300 you can only use about half of that ([6:08](https://youtu.be/P_0_Th_ZzIg?t=368))
- Concurrency levels in the benchmark: 1, 8, 64 and 192 concurrent users ([10:33](https://youtu.be/P_0_Th_ZzIg?t=633))
- Cold start for Kimi K3 about 9 minutes on the pod, and about 30 minutes to download and load weights ([9:12](https://youtu.be/P_0_Th_ZzIg?t=552))
- A single B300 node on the platform costs about $40k per month (approximate, from the speaker) ([13:33](https://youtu.be/P_0_Th_ZzIg?t=813))
- Internal user base of about 50 people, mostly moving off Claude onto self-hosted models ([12:03](https://youtu.be/P_0_Th_ZzIg?t=723))
- Four nodes running the internal Kimi instance ([4:48](https://youtu.be/P_0_Th_ZzIg?t=288))
- A DeepSeek instance on 4 H200s is described as doing a good job for general work ([15:03](https://youtu.be/P_0_Th_ZzIg?t=903))

## Hot takes
- Vendor pitch: the talk promotes RunPod and an unreleased template (BenchPod, 'probably at the end of the month'), and ends with a QR code for credits and a booth invitation. Quality is capped at 2 for this reason.
- The benchmark is one demo run on one pod with one knob changed. The inter-token latency improvement is not a general result, and no methodology, hardware spec, or variance is shown.
- The claims that Kimi K3 fails on CUDA 12.8 and needs vLLM beyond 0.27 are stated without shown evidence in the talk.
- The core advice is sound and generic: measure configs under realistic concurrency, don't ship a model the day it drops, and right-size the model to the task.

## Tools mentioned
RunPod (GPU pods, serverless, storage volumes, Docker images), vLLM (OpenAI-compatible server, YAML config, nightly builds), BenchPod (unreleased RunPod template built on vLLM, with FastAPI, a watchdog and benchmark metrics), Kimi K3, DeepSeek, GLM, Qwen 3.8 (transcribed as 'Quinn 3.8'), Docker, NVIDIA B300, NVIDIA H200, CUDA 12.8 and 13.0, Claude (mentioned as the service many internal users are moving off)

## Relevance to our work
- **agentos** (2/3): InferCraft runs vLLM on one RTX 5090 with KV-cache strategies and a priority scheduler. This talk's method (sweep concurrency 1/8/64/192, compare TTFT, ITL and TPOT across vLLM configs, track cold start) is the benchmarking approach InferCraft needs to back its claims. → *Build a concurrency-sweep benchmark for InferCraft on the RTX 5090 that records TTFT, inter-token latency and total job time for each max-batched-tokens setting, and use the results to pick defaults instead of the vLLM recipe values.*
