# Traces vs Spans Explained (with real examples)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `A-nbuPugjxo` · [watch](https://youtu.be/A-nbuPugjxo) · **date:** 2025-11-02 · **length:** 7:39 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed) · **orgs:** Better Stack, Uber (developer of Jaeger, as stated), OpenTelemetry
- **topics:** observability, dev-tools · **tags:** distributed-tracing, spans, context-propagation, jaeger, opentelemetry, instrumentation, observability-basics

> Beginner primer on distributed tracing: a trace is one request's whole journey, spans are the units of work inside it, and the common mistake is starting new traces instead of child spans.

## Summary
Better Stack explains the difference between traces and spans using a food-delivery analogy: a trace is the whole request journey across services, and spans are the individual operations (HTTP calls, DB queries, processing steps) that make it up. Spans form a parent-child tree, and each one records its parent, duration and errors through propagated context. The video's main point is that developers often add new traces where they should add spans. It demonstrates this in Jaeger, where one payment request showed up as several separate traces with no top-level entry, and then shows the corrected single-trace view with nested spans. It closes with three rules (think journey not stops, connect spans via context, instrument with purpose) and two pitfalls (a new trace per operation, and not propagating context between services). This is an introductory treatment with no benchmarks or production data.

## Key ideas
- **A trace is the complete journey of one request, from entry to response, possibly across several services; spans are the steps inside it.** — Food-delivery analogy: the whole order is the trace, and the restaurant, chef and driver are spans. A span is one unit of work such as an HTTP call, a DB query or a service call. ([0:00](https://youtu.be/A-nbuPugjxo?t=0))
- **Spans form a parent-child tree, and each span knows its parent, duration and errors via context.** — Together the spans form a family tree that shows what happened within one trace. A child cannot start until its parent step has done its work (the chef finishes before the driver leaves). ([1:09](https://youtu.be/A-nbuPugjxo?t=69))
- **The most common error is creating a new trace where a span belongs.** — Developers say they are 'adding traces to this function' when they mean spans. Splitting one request into 20 separate traces instead of one trace with 20 spans makes it hard to reconstruct the flow during debugging. ([1:09](https://youtu.be/A-nbuPugjxo?t=69))
- **Jaeger demo: one request appeared as several unrelated traces with no top-level entry.** — Each service was its own trace (validate payment, check payment auth, get payment config), so there was nothing to click into for the single request. Errors were hard to attribute to the request that caused them. ([2:35](https://youtu.be/A-nbuPugjxo?t=155))
- **With correct structure, the root trace shows what kicked off the request and all its child spans.** — After restructuring, one GET request is one trace with nested spans (validate payment, validate format, validate range). The trace graph shows the request fanning out to the downstream calls, and an error can be traced back to the originating request. ([3:53](https://youtu.be/A-nbuPugjxo?t=233))
- **Three rules: think journey not stops, connect spans explicitly, and instrument with purpose.** — Do not make multiple traces when you need spans in one trace. Propagate span context so no span is disconnected. Trace critical paths, bottlenecks and error-prone code rather than everything, and prefer quality telemetry over volume. ([3:53](https://youtu.be/A-nbuPugjxo?t=233))
- **The two pitfalls are a new trace per operation, and not propagating context into service calls.** — Create spans for operations within the trace, and always pass trace context into outbound service calls. The suggested next step is to audit your tracing setup for disconnected traces that should be spans. ([6:22](https://youtu.be/A-nbuPugjxo?t=382))

## Techniques
- **One trace per inbound request, one span per operation** — Start a trace at the request entry point. Wrap each unit of work (HTTP call, DB query, validation, processing step) in a child span rather than starting a new trace. Use the parent span's context so the child is linked. *When:* Any request that touches multiple steps or services, which is most backend and agent-gateway paths.
- **Propagate trace context into every outbound call** — Pass the current span context into each downstream service call so the callee creates child spans under the same trace ID. Without this, the downstream work appears as a disconnected trace. *When:* Any service-to-service call, including proxies, gateways and tool/API calls made by agents.
- **Instrument selectively** — Put spans on critical paths, known bottlenecks and error-prone operations first. Skip trivial internal functions. *When:* When telemetry volume or cost is a concern and you need signal, not everything.
- **Audit for disconnected traces** — In the tracing UI (Jaeger in the demo), search for the service's traces and check whether one user request shows up as several traces. Each such case should be converted into spans under a single root trace. *When:* When debugging is slow because a request is hard to follow end to end.
- **Read the trace graph and span tree in Jaeger** — Use Find Traces for a service, open one trace, and inspect the spans and their parent-child nesting and durations. The trace graph shows which upstream call triggered each downstream span. *When:* For diagnosing latency or errors on one specific request.

## Numbers
- Illustrative example: a payment-processing debug that could take hours when split into 20 traces instead of one trace with 20 spans (hypothetical, no measured data). ([1:09](https://youtu.be/A-nbuPugjxo?t=69))
- Video length 7:39; no benchmarks, costs, or adoption stats are given. ([0:00](https://youtu.be/A-nbuPugjxo?t=0))

## Hot takes
- Most of the value is correcting a naming habit (trace vs span), and the mental model is correct but elementary for anyone who has used distributed tracing.
- The presenter says teams often add traces where they should add spans, which is a plausible but unquantified claim; the Jaeger demo is a single hand-built example app, not a measured case.

## Tools mentioned
Jaeger, OpenTelemetry (documentation referenced; no version stated)

## Relevance to our work
- **agentos** (2/3):  → *Check that the Govrix Scout proxy opens one OTel trace per inbound request and creates child spans for budget, PII/injection scan, routing and upstream calls, instead of separate traces per stage; verify trace context is propagated to the upstream vLLM/Ray Serve calls.*
- **prosharness** (1/3): ProsHarness wraps long Claude Code runs with checkpoint/resume and plan-critique-debate steps. A run could be modeled as a trace with spans per step, though the video is generic and does not cover agent runs. → *Consider tagging each ProsHarness checkpoint step as a span under one run-level trace so a resumed run can be followed across restarts.*
