# Google’s Golden Signals with the OpenTelemetry Demo and Grafana

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `QWmU9Y_zKsw` · [watch](https://youtu.be/QWmU9Y_zKsw) · **date:** 2025-11-02 · **length:** 4:40 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Google, OpenTelemetry, Better Stack
- **topics:** observability, infra-cost-scaling · **tags:** golden-signals, observability, opentelemetry, grafana, promql, prometheus, jaeger, feature-flags, fault-injection, load-testing, locust, sponsored

> A short walkthrough of Google's four golden signals (latency, errors, traffic, saturation) on the OpenTelemetry demo app in Grafana, then a feature-flag fault-injection demo showing how failures ripple across services. Sponsored segment in the middle.

## Summary
The presenter explains Google's four golden signals (latency, errors, traffic, saturation) and what to watch for each, using the OpenTelemetry demo e-commerce app (about 20 microservices, Locust load generator, OTel collector) running on EC2 with Docker. Latency is shown as quantiles (p99, p99.9) rather than an average, errors as a percentage over time that can include threshold-based failures, traffic as requests per second, and saturation as CPU, memory and queue or batch-processor load. A short sponsored segment promotes Better Stack for PromQL dashboards, alerts and status pages. The second half turns on demo feature flags to show that a failing product-catalog call raises error rates in upstream services (front-end, front-end proxy, checkout), and that a disabled payment path drops payment request volume while checkout errors rise. The presenter's pitch is that tracking golden signals helps you locate errors faster. The content is introductory, with little depth on alerting thresholds, SLOs or how to set up the pipeline.

## Key ideas
- **Four golden signals as the first-look checklist: latency, errors, traffic, saturation** — Presenter attributes the set to Google. Latency is time from request to response (network, DB, app processing). Errors are failed responses, including HTTP 500s, 200s with wrong content, and responses breaching a custom threshold such as latency over 500 ms. Traffic is volume, usually requests per second. Saturation is how close the system is to its resource limits. ([0:00](https://youtu.be/QWmU9Y_zKsw?t=0))
- **Measure latency by quantile, not average** — The demo reads p99 (about 1% of users) and p99.9 for the front-end service, and says most users see under 200 ms. The tail is where the bad experience sits. ([0:00](https://youtu.be/QWmU9Y_zKsw?t=0))
- **Error rate is a windowed percentage, and a flat 0% on one series means little when another climbs** — Error rate is shown as a percentage sampled every two minutes over 30 minutes. The presenter compares a series that stays at 0% with one that rises and falls, and says that trajectory should be investigated. ([1:17](https://youtu.be/QWmU9Y_zKsw?t=77))
- **Traffic is best read per endpoint, since aggregate RPS hides slow calls** — Cart and Valkey cache calls are graphed separately. Two calls exceed about a second and two stay under 200 ms, showing that request rate and latency can be read together per operation. ([1:17](https://youtu.be/QWmU9Y_zKsw?t=77))
- **Saturation covers CPU and memory plus queue-like signals such as batch span processors** — Saturation panels include CPU and memory of Python services, a recommendation rate (per two minutes), and a batch span processor that forwards spans to the collector. ([2:29](https://youtu.be/QWmU9Y_zKsw?t=149))
- **Fault injection with feature flags to see the blast radius of a failure** — A flag that breaks one product in the catalog raises error spans in the product-catalog service, then in the front-end and front-end proxy. Disabling checkout to the payment service drops payment request volume to near zero and produces errors in checkout. The presenter says this is how you learn which services depend on each other. ([2:29](https://youtu.be/QWmU9Y_zKsw?t=149))

## Techniques
- **Golden-signal dashboard per service** — For each service, chart latency at p99 and p99.9 (not the mean), error rate as a percentage over a window, request rate per endpoint, and saturation (CPU, memory, queue or batch-processor backlog). The demo does this in Grafana with PromQL, using the pre-built OpenTelemetry demo dashboards. *When:* First look at an unfamiliar system, or when triage is slow and you need one page that covers the basic health of each service.
- **Span-derived RED-style metrics cross-checked against traces** — The demo's span-metrics section builds error and latency metrics from trace spans. When a Grafana error spike appears, the presenter opens the matching traces in Jaeger to confirm the errors line up. *When:* When you have tracing but no per-service metrics yet, or to confirm that a metric spike is a real failure and not a dashboard artifact.
- **Feature-flag fault injection to map dependencies** — Turn on a demo flag that fails one product or one dependency, then check the golden signals of each upstream and downstream service for errors and for request-volume drops. Turn it off and repeat with another flag to map the blast radius. The video runs flags in sequence: product catalog failure first, then payment unreachable. *When:* To validate that alerts and dashboards catch a real failure and to learn which services depend on each other, before an incident does it for you.
- **Load generation to produce realistic traffic before reading signals** — The demo runs a Locust load generator against the app so that all panels have traffic to show, and it runs the demo on EC2 with Docker (or Kubernetes, per the OTel docs). *When:* When a test environment is idle and the dashboards would otherwise show nothing useful.

## Numbers
- Demo app is made of about 20 microservices, with a Locust load generator and an OTel collector collecting telemetry ([0:00](https://youtu.be/QWmU9Y_zKsw?t=0))
- p99 latency for the front-end service can exceed about 365 ms (1% of users) ([0:00](https://youtu.be/QWmU9Y_zKsw?t=0))
- Most users see latency under 200 ms. The p99.9 figure is garbled in the captions ("7 to 4 milliseconds"), so treat the exact value as unknown. ([0:00](https://youtu.be/QWmU9Y_zKsw?t=0))
- Error rate is a percentage sampled every two minutes over a 30-minute window ([1:17](https://youtu.be/QWmU9Y_zKsw?t=77))
- Two cart and cache calls take about a second or more, and two take under 200 ms ([1:17](https://youtu.be/QWmU9Y_zKsw?t=77))
- Product-catalog error rate increase is shown over the last 45 minutes ([2:29](https://youtu.be/QWmU9Y_zKsw?t=149))
- Recommendation rate is sampled every two minutes ([2:29](https://youtu.be/QWmU9Y_zKsw?t=149))

## Hot takes
- Sponsored segment: Better Stack is promoted mid-video (PromQL dashboards, status pages, alerts, a free tier). Quality is capped at 2 because of the sponsor and the thin depth.
- The opening claim that golden signals will stop errors in your code is hyperbole. The presenter partly walks it back, saying they help you find errors faster.
- Attribution of the four signals to Google is the presenter's claim and is not sourced in the video.

## Tools mentioned
OpenTelemetry demo app, OpenTelemetry Collector, Grafana, PromQL, Prometheus, Jaeger, Locust, Valkey (cache), Docker, Kubernetes, EC2, Better Stack

## Relevance to our work
- **agentos** (2/3): AgentOS L4 observability is Prometheus/Grafana, OTel and Locust. The video gives a concrete golden-signal panel set and a flag-driven failure drill that map directly onto that stack, and onto the proxy and vLLM services. → *Build a golden-signals dashboard for the Govrix proxy (:4000) and InferCraft (vLLM/Ray Serve): p99 and p99.9 latency, error rate, requests per second per route, and KV-cache or queue saturation. Add a fault-injection drill that disables one backend and checks the blast radius.*
- **general** (1/3): Reporting quantile latency instead of averages and using fault injection to check dependency blast radius are general SRE habits, and the video demonstrates both briefly. → *Report p99 and p99.9 alongside the mean for any service you measure, and add one flag-driven failure test per critical dependency.*
