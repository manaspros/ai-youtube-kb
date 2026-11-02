# Semantic Conventions - The SECRET to Crystal Clear Telemetry Data

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ckcbPgZb3TU` · [watch](https://youtu.be/ckcbPgZb3TU) · **date:** 2025-11-02 · **length:** 7:34 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack, Elastic, OpenTelemetry
- **topics:** observability, dev-tools · **tags:** opentelemetry, semantic-conventions, ecs, tracing, metrics, logs, vector, better-stack, typescript, hono, nodejs

> Better Stack walkthrough of OpenTelemetry semantic conventions: renaming tracers, spans, metrics and events in a small Node/Hono dice app, and keeping existing logs aligned with ECS via Vector.

## Summary
The video explains semantic conventions as shared rules for naming and structuring telemetry fields, and traces how Elastic's ECS (2018) was merged with OpenTelemetry's conventions in 2023. It then walks through a small TypeScript dice-roll app that uses the OTel Node SDK and Hono middleware, and rewrites its custom tracer, HTTP span, event names and metric to follow the conventions. The key step is using stable, required HTTP server attributes and the standard HTTP server request duration metric instead of ad hoc names. For logs, the advice is to keep existing log formats and rename fields with Vector, and to use the ECS docs as the reference for log fields until OTel's log documentation matures. The video closes with a short plug for Better Stack's hosted dashboards and metrics as a cheaper alternative to self-hosting Prometheus.

## Key ideas
- **Semantic conventions are shared rules for how telemetry fields are named, structured, and which are required or optional; they stop teams from debating names.** — Elastic's ECS (2018) solved this only for Elastic users; in 2023 ECS was merged with the OTel semantic conventions, which the speaker prefers because they are open, vendor-neutral and community-led. ([0:00](https://youtu.be/ckcbPgZb3TU?t=0))
- **OTel conventions apply automatically to OTel SDKs and instrumentation, so they matter most for custom traces, metrics and events.** — The demo is a random dice-roll app (TypeScript, Hono) with OTel Node SDK instrumentation and a custom trace and metric in middleware. Its names (a generic 'kind' value, a query-param attribute called 'key', a metric named after the full path with stringified query params) are called out as non-standard. ([1:16](https://youtu.be/ckcbPgZb3TU?t=76))
- **Tracer names should be the instrumentation scope (library name plus version), not a generic label like 'HTTP server'.** — Span names for HTTP should contain the method and the target. HTTP server spans have four required attributes at stable stability level: request method, server address, server port and full URL, plus one optional attribute. ([2:36](https://youtu.be/ckcbPgZb3TU?t=156))
- **Check each attribute's stability before adopting it: stable (unlikely to change), experimental (may change), or deprecated (changed or removed).** — The four HTTP server attributes shown are stable, so the speaker switched the span to SERVER kind and set those attributes. ([2:36](https://youtu.be/ckcbPgZb3TU?t=156))
- **Event names follow the same rules as attribute names, and metrics need their required semconv metric.** — For HTTP, the HTTP server request duration metric is required. Because it covers the speaker's custom metric, the custom one is replaced; the new one gets a semconv name, a unit and the required attributes. ([3:59](https://youtu.be/ckcbPgZb3TU?t=239))
- **For logs, keep the existing log format and normalize fields with Vector, rather than changing the log producers.** — Nginx, Apache and similar logs stay as they are, and Vector renames their fields. The OTel log documentation focuses on log attributes and its log data model is thinner than ECS's, so the speaker suggests ECS for log fields for now, unless you use the OTel Logs SDK. ([5:22](https://youtu.be/ckcbPgZb3TU?t=322))
- **Ready-made dashboards and hosted metrics can be used instead of self-hosting Prometheus.** — The speaker plugs Better Stack, which provides prebuilt dashboards for OpenTelemetry, Prometheus and Postgres, and says its metrics pricing makes it cheaper than self-hosting. This is a vendor plug with no numbers given. ([5:22](https://youtu.be/ckcbPgZb3TU?t=322))

## Techniques
- **Name tracers after the instrumentation scope** — Use the instrumenting library name plus its version as the tracer name (e.g. the custom middleware's package and version), not a generic label such as 'HTTP server'. *When:* Any custom tracer you create in an app that already has OTel instrumentation.
- **HTTP server span with semconv names** — Name the span '<HTTP method> <target>', set span kind to SERVER (the video changes it from an internal kind to SpanKind.SERVER), and set the four required stable attributes: request method, server address, server port, full URL. Add the one optional attribute if useful. *When:* Custom HTTP middleware or handlers that create their own server spans (the dice app's Hono middleware).
- **Use the standard HTTP duration metric** — Replace a custom request-timing metric with the semconv 'HTTP server request duration' metric. Give it a semconv name, a unit, and its required attributes. Don't keep both if the standard one covers the same measurement. *When:* Latency and request-count metrics for HTTP services, so dashboards and tools can read them without custom mapping.
- **Format event names like attribute names** — Give custom events names that follow the same naming rules as attribute names from the conventions docs. *When:* Custom span events or log-like events emitted by your own code.
- **Check stability before adopting an attribute** — In the semconv docs, read each attribute's requirement level and stability tag (stable, experimental, deprecated) before using it. Only build on stable ones if you want to avoid renames. *When:* Choosing attribute names for long-lived telemetry you can't easily change later.
- **Normalize existing logs with Vector instead of rewriting them** — Keep Nginx/Apache (or other) logs as they are, parse them into structured fields, and use Vector to rename those fields to the chosen convention. The video points to its Vector tutorial for unstructured-to-structured logs. *When:* You have existing unstructured access or application logs and don't want to change the producers.
- **Use ECS as the log field reference for now** — For top-level log fields, use the ECS documentation rather than the OTel log data model docs, which the speaker finds less complete. Use the OTel Logs SDK instead if you emit logs through it, since it may already define these fields. *When:* Designing log schemas today while the OTel and ECS log specs are still merging.

## Numbers
- Elastic introduced the Elastic Common Schema (ECS) in 2018, and it was merged with the OTel semantic conventions in 2023. ([0:00](https://youtu.be/ckcbPgZb3TU?t=0))
- HTTP server spans have four required stable attributes (request method, server address, server port, full URL) plus one optional attribute. ([2:36](https://youtu.be/ckcbPgZb3TU?t=156))
- There are three stability levels for attributes: stable, experimental, and deprecated. ([2:36](https://youtu.be/ckcbPgZb3TU?t=156))
- HTTP server request duration is a required metric in the HTTP semconv; the speaker replaces a custom metric with it. ([3:59](https://youtu.be/ckcbPgZb3TU?t=239))
- Video length is 7:34. ([0:00](https://youtu.be/ckcbPgZb3TU?t=0))

## Hot takes
- The speaker prefers the OTel semantic conventions to ECS because they are open, vendor-neutral, and community-led, even though ECS came first.
- The speaker finds ECS's documentation better than the OTel log data model docs and recommends ECS for log fields until OTel's log spec is more complete.
- Better Stack's hosted metrics are called cheap enough that the speaker thinks they make more sense than self-hosting Prometheus. This is a vendor plug with no pricing shown.
- Semantic conventions are presented as something SDKs already apply; only custom telemetry needs manual naming work.
- Quality is capped by the self-promotion. The Better Stack plug is short and doesn't make the content a sponsored segment, so the tutorial itself is the main content.

## Tools mentioned
OpenTelemetry semantic conventions, OpenTelemetry Node SDK, OpenTelemetry Logs SDK, Hono (TypeScript web framework), TypeScript, Node.js, Elastic Common Schema (ECS), Vector, Better Stack, Prometheus, PostgreSQL, Nginx, Apache HTTP Server, OCSF

## Relevance to our work
- **agentos** (2/3): AgentOS's L4 observability (OTel, Prometheus/Grafana) and its Hono/Node or Rust proxy services would need consistent span, metric and log field names to be queryable across pillars. The video covers the exact HTTP server conventions that apply. → *Audit the OTel spans and metrics in the L4 observability path against the HTTP server semconv (span name, SERVER kind, four required attributes, standard request duration metric) before adding any custom metrics.*
