# Observability vs Monitoring - Whats the difference?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ytx6jr2TyxI` · [watch](https://youtu.be/ytx6jr2TyxI) · **date:** 2025-11-02 · **length:** 4:07 · **format:** other · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Coinbase, Better Stack
- **topics:** observability, infra-cost-scaling · **tags:** monitoring, observability, structured-logs, metrics, distributed-tracing, alerting, debugging

> Beginner explainer distinguishing monitoring (known thresholds, the "what and when") from observability (logs, metrics and traces for the "how and why"), with a plug for Better Stack at the end.

## Summary
The speaker defines monitoring as continuously comparing key metrics such as CPU and response time against predefined thresholds, which catches only problems someone anticipated. Observability is presented as the response to complex microservice and container systems: structured logs, metrics and distributed tracing together let you answer questions about states you did not predict. He argues the data collected must be balanced against storage cost, since recording everything is impractical. The worked example is a slow application: monitoring flags high memory, while observability traces which services and requests are affected and which functions consume memory. The closing advice is to start with solid monitoring, then build out observability based on real debugging needs, with a brief promotion of Better Stack. The content is conceptual, with no benchmarks, code, or configuration shown.

## Key ideas
- **Monitoring tracks known health metrics against predefined thresholds and alerts when they are crossed.** — Example: alert when server CPU exceeds 80%. Its limit is that it only catches problems anticipated in advance and does not explain why the metric moved. ([0:00](https://youtu.be/ytx6jr2TyxI?t=0))
- **Observability exists because modern systems (microservices, cloud infrastructure, containers) have countless failure modes.** — It is meant to let you understand system states you never anticipated, not just the ones you set thresholds for. ([0:00](https://youtu.be/ytx6jr2TyxI?t=0))
- **Observability rests on three tools: structured logs, metrics, and distributed tracing.** — The speaker says the value comes from using them together, so you know why, how, where and when something happened. ([1:19](https://youtu.be/ytx6jr2TyxI?t=79))
- **Collecting everything is impractical, so observability requires balancing which data to collect and how much detail to capture.** — He says any data point could be the missing clue, but storing everything is expensive to scale. Coinbase is cited as spending $65 million on this, with no source or context given. ([1:19](https://youtu.be/ytx6jr2TyxI?t=79))
- **Worked example: monitoring says memory is high, while observability shows which services, requests and functions are responsible.** — Observability lets you reconstruct the sequence of events that led to the alert that monitoring raised. ([1:19](https://youtu.be/ytx6jr2TyxI?t=79))
- **Monitoring answers what and when; observability answers how and why.** — Analogy: a car dashboard (monitoring) versus a diagnostic tool (observability) that finds the specific engine fault after the check-engine light comes on. ([2:41](https://youtu.be/ytx6jr2TyxI?t=161))
- **The practical advice is to start with solid monitoring and then build observability from real debugging needs, not to choose one over the other.** — Monitoring is the first line of defense for known issues; observability traces the path of errors through many microservices to find root causes. The challenge is collecting enough data to debug while controlling cost. ([2:41](https://youtu.be/ytx6jr2TyxI?t=161))

## Techniques
- **Layered monitoring then observability** — Begin with threshold-based alerts on infrastructure metrics (CPU, memory) and application metrics (response time). Add structured logs, metrics and distributed tracing as real debugging needs appear, so you collect detail where you have actually needed it. *When:* Early on, or when building out alerting and debugging for a system of many services. The video recommends it as the default path.
- **Tiered data collection for cost control** — Decide deliberately which events, metrics and trace detail to capture, rather than recording everything. Pick detail levels against the debugging questions you expect to ask. *When:* When log, metric or trace volume threatens storage cost at scale.

## Numbers
- Example monitoring threshold: alert when server CPU usage crosses 80%. ([0:00](https://youtu.be/ytx6jr2TyxI?t=0))
- Coinbase is said to want to spend $65 million on observability; the figure is stated without a source or context. ([1:19](https://youtu.be/ytx6jr2TyxI?t=79))
- Video length is 4:07, and the content has no benchmarks, latencies or measured costs. ([0:00](https://youtu.be/ytx6jr2TyxI?t=0))

## Hot takes
- Monitoring is not enough for modern microservice systems, because it only catches anticipated problems. Observability is needed to find root causes.
- Observability should be built incrementally from real debugging needs, not adopted all at once.
- Sponsored plug: the video closes by pointing viewers to Better Stack, and the Coinbase $65M figure is unsourced, so quality is capped at 2.

## Tools mentioned
Better Stack

## Relevance to our work
- **agentos** (1/3): L4 observability (Prometheus/Grafana, OTel) is on the roadmap. The video gives only a conceptual split between alerts for known failures and traces/logs for root cause, with no implementation detail. → *Check that the L4 stack has both threshold alerts for known failure modes and per-request tracing for root-cause work, and decide what trace detail to keep to control cost.*
