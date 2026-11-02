# Why Your Applications NEED Distributed Tracing

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `E956jBlMKcA` · [watch](https://youtu.be/E956jBlMKcA) · **date:** 2025-11-02 · **length:** 9:13 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Google, Twitter, Uber, Stripe
- **topics:** observability, dev-tools · **tags:** distributed-tracing, opentelemetry, otel-collector, jaeger, zipkin, spans, otlp, docker, nodejs, express, microservices

> Intro to distributed tracing: why logs and metrics fall short for microservices, what traces and spans are, and a Node.js demo sending OpenTelemetry data through an OTel Collector to Jaeger.

## Summary
Better Stack explains why distributed tracing exists: in microservice and cloud systems, logs and metrics don't show which services a single request touched, how long each took, or where it failed. A trace is a waterfall of spans sharing one trace ID, with each span carrying its own span ID and a parent ID. The demo is a small Express app instrumented with OpenTelemetry that exports over OTLP to an OpenTelemetry Collector, which forwards traces to Jaeger over a shared Docker network through a batch processor. The walkthrough shows spans with custom attributes, span events, and recorded exceptions, then how Jaeger's search filters (tags, status, time window, minimum duration) find the relevant trace in a busy system. The video is a conceptual primer with a basic setup. It does not cover sampling, context propagation across services, or production sizing, and it skips the exact Docker and collector config commands.

## Key ideas
- **Logs and metrics don't show the path of one request through many services, and containers and multiple teams make root-cause hunting harder. Distributed tracing is meant to answer which services a request hit, what each did, how long it took, and where errors started.** — The speaker's e-commerce example chains catalog, recommendations, payment, order management and shipping, with some parts being SaaS like Stripe. ([0:00](https://youtu.be/E956jBlMKcA?t=0))
- **A trace is the full lifecycle of one operation, shown as a waterfall. Spans are its units: they share one trace ID, each has its own span ID, and a parent ID records the causal link, which forms a tree rooted at the top-level request span.** — Span A is the root for the whole API request, B is a service it calls, and C is called by B. Context passing through the calls is what links the spans. ([2:37](https://youtu.be/E956jBlMKcA?t=157))
- **Early open-source tracing systems that shaped the space were Zipkin (from Twitter) and Jaeger (from Uber), and the concept was popularized by Google's Dapper paper.** — Background only. The video does not compare them in depth. ([1:16](https://youtu.be/E956jBlMKcA?t=76))
- **Pipeline pattern: the app sends traces over OTLP to an OpenTelemetry Collector, and the collector forwards them to the backend. Swapping backends later then means changing the collector config, not the app.** — The collector config has a Jaeger exporter pointed at the Jaeger container by its Docker name on port 4318, and a traces pipeline that receives OTLP, runs the batch processor (called the recommended one), and exports to Jaeger. ([4:17](https://youtu.be/E956jBlMKcA?t=257))
- **Spans carry rich context beyond timing: custom attributes, status, span events, and exception details, plus resource info about the process. That makes it possible to see where and why a failure occurred.** — The demo sets a custom attribute recording four dice rolls, a status error, a span event, and an exception on a child span. The demo errors are deliberate. ([6:43](https://youtu.be/E956jBlMKcA?t=403))
- **The backend's query features are what make tracing practical at scale. At high traffic you filter by tags, status code, error state, time window, or minimum duration (e.g. only traces over 10 seconds) to locate the one trace you need.** — The speaker recommends keeping traces in an observability backend for this reason. ([7:50](https://youtu.be/E956jBlMKcA?t=470))
- **Propagation is the requirement that makes it all work: every service must pass the trace context along, or the parent-child links break and the trace is incomplete.** — The speaker says that if tracing is set up on all services so the context is passed correctly, a single request, like one purchase, can show every layer it touched. ([6:43](https://youtu.be/E956jBlMKcA?t=403))

## Techniques
- **Collector-based OTLP export to Jaeger** — Run Jaeger and the OpenTelemetry Collector as containers on one Docker network so they can reach each other by container name. In the collector config, add a Jaeger exporter whose endpoint is the Jaeger container on port 4318. Add a traces pipeline: receivers (OTLP) -> processors (batch) -> exporters (Jaeger). Point the app's OpenTelemetry exporter at the collector, not at Jaeger. The video does not show the exact docker commands or full YAML. The endpoint and pipeline shape are as described above. *When:* Local or dev setup where you want to switch trace backends later without changing application code.
- **Instrument a Node.js app with an instrumentation file** — Keep OpenTelemetry setup in a separate instrumentation.ts file that configures trace export over OTLP to the collector. The video only refers to earlier OpenTelemetry videos for the full setup. *When:* Adding tracing to an existing Node service without touching business logic.
- **Add custom span attributes, events and exceptions for debugging** — Set a custom attribute on a span (the demo tags a dice-roll function with its roll count), add span events with named messages, and record exceptions so they appear on the span with status error. Then inspect them in the trace detail view. *When:* When you need the failing function's inputs and the error details in the trace, not just timing.
- **Trace search for root-cause isolation** — In the backend UI, filter traces by tag or attribute, status code, error flag, time range (e.g. last hour), and minimum duration (e.g. over 10 seconds) to find slow or failing requests, then open the waterfall to see which child span is slow or errored. *When:* High-volume services where thousands of requests per minute make scanning by hand impossible.

## Numbers
- Jaeger collector receives OTLP via port 4318 (HTTP) in the demo collector config ([4:17](https://youtu.be/E956jBlMKcA?t=257))
- Example search filter: minimum trace duration over 10 seconds ([7:50](https://youtu.be/E956jBlMKcA?t=470))
- Demo app makes four dice rolls, so the trace shows four child spans under the roll-dice call ([5:23](https://youtu.be/E956jBlMKcA?t=323))
- Video length 9:13; no benchmarks, costs or adoption figures are given ([0:00](https://youtu.be/E956jBlMKcA?t=0))

## Hot takes
- Logs and metrics alone are insufficient for microservices, and distributed tracing is the way to answer per-request questions.
- Route telemetry through the OpenTelemetry Collector so the observability backend can be swapped later without touching application code.
- Keeping traces in a backend with real query features matters more than just collecting them, because raw trace volume is unusable without search.

## Tools mentioned
OpenTelemetry, OpenTelemetry Collector, Jaeger, Zipkin, Docker, Node.js, Express, OTLP (OpenTelemetry Protocol)

## Relevance to our work
- **agentos** (2/3): AgentOS L4 already lists OTel and Prometheus/Grafana. Per-request spans across the proxy, budget checks, retrieval and sandbox calls would show where a multi-hop agent request spends its time. → *Add OTel spans with a shared trace ID to the Govrix proxy and one InferCraft request path, export through an OTel Collector to Jaeger, then compare the trace to the Locust load-test latency.*
- **prosharness** (1/3): ProsHarness runs long multi-step Claude Code workflows (plan, Codex critique, debate). Spans per step could show where a run stalls, but the video is an intro to tracing, not agent-specific. → *Optional: propagate one trace ID through the plan, critique and debate steps when instrumenting ProsHarness checkpoints.*
