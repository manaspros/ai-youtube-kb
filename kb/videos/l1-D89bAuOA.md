# Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `l1-D89bAuOA` · [watch](https://youtu.be/l1-D89bAuOA) · **date:** 2026-09-20 · **length:** 16:07 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ashok Chandrasekar, Jason Kramberger · **orgs:** Google
- **topics:** evals, inference-serving, observability · **tags:** benchmarking, load-testing, reproducibility, inference-perf, llm-d, production-scale-inference, SLO, workload-catalog, client-side-metrics

> Google engineers argue that LLM serving benchmarks often blame the server when the benchmark client is at fault, and show Inference Perf, a multi-process, reproducible load generator built for production-scale inference.

## Summary
Two Google engineers (Ashok Chandrasekar and Jason Kramberger) argue that LLM performance numbers are often unreliable because the benchmark harness itself distorts results. They describe how simple benchmark tools break at production scale with many replicas, disaggregated prefill/decode, and autoscaling. Their examples include a Python harness that delivered only 38 of 200 requested QPS on a small machine, and client-side latency inflation of up to 58 seconds that looked like a server bottleneck. They also show that hidden settings such as temperature 0 and dataset tokenization can change throughput claims a lot. The second half presents Inference Perf (a CNCF project) with a multi-process load generator, declarative configs, a shared workload catalog, and the Prism results UI from llm-d. The talk ends with four validity principles for benchmarks. Roughly half the talk is project showcase, so treat the product sections as context rather than evidence.

## Key ideas
- **Benchmark tools fall into four groups: model-server built-in scripts, competitive-analysis suites (MLPerf and similar), generic web load tools (Locust, k6), and production-stack LLM benchmarks. The talk targets the last group, which is the gap.** — The speaker says the production-stack group is the one that matters for finding bottlenecks in a real serving setup, and the other three do not cover it. ([1:11](https://youtu.be/l1-D89bAuOA?t=71))
- **A simple benchmark harness fails at production scale, where there are many servers, prefill/decode disaggregation, and autoscaling. The benchmark needs high load, realistic workloads, and metric fidelity.** — Metric fidelity means the reported numbers are accurate and tell you how the run actually went, not just that it finished. ([2:37](https://youtu.be/l1-D89bAuOA?t=157))
- **The benchmark client can be the bottleneck. A single Python process (GIL-bound) delivered 38 of 200 requested QPS on a small shared-core machine, and the tool still reported the run as normal.** — Requested rate and achieved rate can differ silently. You need to check that the load you asked for is the load that was sent. ([4:59](https://youtu.be/l1-D89bAuOA?t=299))
- **Client-side thrashing inflates measured latency. The speaker saw delays up to 58 seconds, which looked like server saturation. A scaled-out harness at about 1,000 QPS showed very little latency against a simulated server.** — Diagnose the harness first when latency looks bad. Otherwise you will tune a server that is not the problem. ([6:00](https://youtu.be/l1-D89bAuOA?t=360))
- **Sampling and dataset settings change results. Temperature 0 makes outputs deterministic and raised a shared throughput claim by about 20%, compared with typical temperature near 0.7. The same ShareGPT dataset gave different input token counts in two harnesses because of different sampling and truncation.** — Other open questions the speaker lists: forcing generation to end-of-sequence, prefix-cache hit rates, and how to replay multi-turn conversations. ([7:28](https://youtu.be/l1-D89bAuOA?t=448))
- **Inference Perf is a CNCF project that began in the Kubernetes serving working group. It uses a declarative config for reproducible runs and reports client metrics next to server metrics.** — The goal is that when a run looks wrong, you can tell whether the load tool or the system under test is responsible. ([8:59](https://youtu.be/l1-D89bAuOA?t=539))
- **The load generator queues requests at their planned send times in a main process. Worker processes pull from that queue and record how far each request's actual execution lagged its plan.** — This lag measurement is what lets the tool report whether it kept up. The speaker says it kept up at 5,000 QPS in a comparison with HTTP tools such as k6. ([10:02](https://youtu.be/l1-D89bAuOA?t=602))
- **A shared workload catalog defines each scenario in plain language and in config (for example multi-turn chat, tree-of-thought agentic generation, and batch summarization). The aim is to share definitions across tools.** — Results are displayed in the Prism UI, which is part of llm-d. The example shown is an agentic code-generation workload on TPUs with 8 replicas. ([11:07](https://youtu.be/l1-D89bAuOA?t=667))
- **Four validity principles: run at production client concurrency, observe the client, make stochastic settings match real demand, and use datasets close to the target workload.** — The speaker's summary is that if a result looks like a server problem, the benchmark may be the cause. ([13:39](https://youtu.be/l1-D89bAuOA?t=819))

## Techniques
- **Scheduled multi-process load generation** — The main process queues each request at its planned send time. Several worker processes pull from the queue, so the work is not limited by one Python GIL. Record the gap between planned and actual execution for each request. *When:* When you need high QPS from a Python-based harness, or need proof that a load test actually delivered its target rate.
- **Client-side health check on every run** — Report achieved QPS next to requested QPS and track client-side latency and lag alongside server metrics. Treat a shortfall or client lag as a failed run to fix before reading the server numbers. *When:* Before trusting any latency or throughput result, especially when the server looks slower than expected.
- **Declarative benchmark configs with distributions** — Describe input and output length distributions, arrival process (constant rate, Poisson, or fixed concurrency), and conversation replay in a versioned config file, so the same run can be repeated. *When:* When you need a run someone else can reproduce, or want to compare two configurations fairly.
- **Sweep the load to find saturation** — Measure at a range of request rates instead of one QPS. Find the point where the server saturates and check the P90 time-to-first-token SLO at each level. *When:* For capacity planning, choosing the right serving configuration, or checking whether an SLO holds.
- **Match sampling and dataset preprocessing to production** — Use realistic temperature (about 0.7, not 0). Check token counts after tokenization and truncation when comparing harnesses on the same dataset. Decide explicitly whether to force end-of-sequence. *When:* Any time you compare throughput or latency between harnesses, or quote a throughput improvement.
- **Shared workload definitions** — Write each workload as a natural-language scenario with an attached config (for example multi-turn chat or agentic generation), and publish it so other tools can run the same definition. *When:* When results need to be compared across teams or tools, or you want a fixed set of realistic scenarios to regression-test against.

## Numbers
- Requested 200 QPS but achieved only 38 QPS on a small shared-core machine with a single-process Python harness. ([4:59](https://youtu.be/l1-D89bAuOA?t=299))
- A single-process harness capped at about 170 QPS on a larger machine. ([4:59](https://youtu.be/l1-D89bAuOA?t=299))
- Client-side latency inflation reached up to 58 seconds, which looked like server bottlenecking. ([6:00](https://youtu.be/l1-D89bAuOA?t=360))
- A scaled-out harness at about 1,000 QPS showed very little latency against a simulated server. ([6:00](https://youtu.be/l1-D89bAuOA?t=360))
- A shared benchmark reported about 20% higher throughput. The speaker traced it to temperature 0 versus a realistic temperature near 0.7. ([7:28](https://youtu.be/l1-D89bAuOA?t=448))
- Inference Perf kept up at 5,000 QPS in the speaker's comparison with HTTP load tools such as k6. ([10:02](https://youtu.be/l1-D89bAuOA?t=602))
- Production-scale Prism example with 8 replicas: combined optimizations reached almost hundreds of thousands of tokens per second on TPUs, versus a plain Kubernetes-service baseline. ([12:34](https://youtu.be/l1-D89bAuOA?t=754))

## Hot takes
- If a tool says it ran at 200 QPS, that does not mean it delivered 200 QPS. Check the achieved rate.
- A slow server result is often the benchmark client's fault, not the serving stack's.
- Temperature 0 can make throughput look about 20% better than a realistic workload would show.

## Tools mentioned
Inference Perf, llm-d, Prism, vLLM, SGLang, Kubernetes, k6, Locust, MLPerf, ShareGPT

## Relevance to our work
- **agentos** (2/3): AgentOS L2B InferCraft runs vLLM on one RTX 5090 and claims the next phase is proof through benchmarks. The talk shows the load client can distort those numbers, so the benchmark harness needs checking. → *Before publishing any AgentOS latency or throughput number, add a check that achieved QPS matches requested QPS and that client-side lag stays low. Pin temperature (about 0.7) and log input token counts after tokenization.*
- **general** (1/3): The reproducibility lessons (record sampling settings, check the dataset after preprocessing, and check the harness before the system) also apply to agent eval runs. → *Record temperature, dataset preprocessing, and achieved-vs-requested load for each eval run, so results from two runs can be compared fairly.*
