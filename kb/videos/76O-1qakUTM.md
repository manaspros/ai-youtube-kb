# OpenTelemetry Makes Istio's Telemetry AMAZING!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `76O-1qakUTM` · [watch](https://youtu.be/76O-1qakUTM) · **date:** 2025-11-02 · **length:** 5:16 · **format:** tutorial · **quality:** 2/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack
- **topics:** observability, dev-tools · **tags:** opentelemetry, otel-collector, istio, service-mesh, kubernetes, jaeger, prometheus, tracing, metrics, sidecar, nodejs, auto-instrumentation, otlp

> Walkthrough of putting an OpenTelemetry Collector between Istio sidecars and backends (Jaeger, Prometheus, console), then adding Node.js OTel auto-instrumentation to the app; short tutorial with the config described rather than shown.

## Summary
The speaker argues that a service mesh such as Istio already emits logs, metrics and traces from its sidecar proxies without application code changes, but exporting that data to several backends means configuring each signal separately. An OpenTelemetry Collector in the middle makes fan-out to multiple destinations a pipeline change. He demonstrates on a local Kubernetes cluster with a Node.js frontend, Node.js backend and MongoDB, with Istio injection enabled on the default namespace. He recommends not copying Istio's sample collector config, which uses the deprecated logging exporter (now debug), and instead writing a collector that receives OTLP, runs a batch processor, and exports to the console, Prometheus and Jaeger. The collector, Jaeger and Prometheus go into a separate observability namespace so they are not injected with sidecars. Finally, both services are instrumented with OpenTelemetry Node.js auto-instrumentation to add application-level traces and metrics such as HTTP client duration, and the closing segment suggests exporting onward to third-party backends including Better Stack.

## Key ideas
- **A service mesh's sidecar proxies collect logs, metrics and traces with no application code changes, but sending that telemetry to several backends means configuring each signal separately.** — Istio sidecars intercept pod traffic and emit telemetry. Routing it to Azure, AWS or GCP per signal is the friction the speaker wants to remove. ([0:00](https://youtu.be/76O-1qakUTM?t=0))
- **An OpenTelemetry Collector pipeline makes multi-destination export a configuration change, since adding an exporter does not touch the services.** — Mesh telemetry and app telemetry can both flow into one collector, which then fans out to exporters. ([0:00](https://youtu.be/76O-1qakUTM?t=0))
- **Do not copy Istio's sample OpenTelemetry config as-is. It uses the logging exporter, which has been replaced by debug, so the speaker wrote his own collector config.** — The sample was updated the year before recording. The speaker links his version in the video description, which the transcript does not show. ([1:27](https://youtu.be/76O-1qakUTM?t=87))
- **Run the collector, Jaeger and Prometheus in a separate observability namespace.** — The default namespace carries the Istio injection label, so any pod placed there gets a sidecar. Each injected pod shows two containers instead of one. ([1:27](https://youtu.be/76O-1qakUTM?t=87))
- **The collector receives OTLP, runs a batch processor, and exports logs, traces and metrics to the console, and traces and metrics to Jaeger and Prometheus.** — Separate pipelines per signal. Jaeger and Prometheus both need OTLP receiving enabled so the collector can push to them. Prometheus is enabled through a startup argument and Jaeger through an environment variable. ([2:52](https://youtu.be/76O-1qakUTM?t=172))
- **Application-level OpenTelemetry instrumentation adds telemetry the mesh cannot see, such as app traces and custom metrics.** — Frontend and backend both run Node.js, so the same auto-instrumentation setup applies to each. The speaker reports extra Prometheus metrics, including HTTP client duration and client request metrics. ([4:19](https://youtu.be/76O-1qakUTM?t=259))
- **The closing segment pitches exporting the collector's output to third-party backends, naming Better Stack.** — This is a vendor mention at the end of a short tutorial, not a benchmark or a comparison. ([4:19](https://youtu.be/76O-1qakUTM?t=259))

## Techniques
- **Mesh-first telemetry baseline** — Label the app namespace for Istio injection so each pod gets a sidecar proxy. Install Istio's bundled Jaeger and Prometheus for a first look. The sidecars emit logs, metrics and traces with no app code change. Delete the bundled Jaeger and Prometheus deployments once a collector is in place. *When:* You want baseline service-to-service telemetry on a Kubernetes cluster that already runs a service mesh, before adding anything else.
- **Separate observability namespace** — Create an observability namespace (the speaker names it observability) and deploy the OTel Collector, Jaeger and Prometheus there. Keep it out of the namespace labelled for Istio injection so those pods do not get sidecars. Apply the manifests with kubectl in that namespace. *When:* Your application namespace has automatic sidecar injection and you want the telemetry backends outside the mesh.
- **Hand-written collector config instead of the Istio sample** — Use an OTLP receiver. Add a batch processor. Define exporters: debug for console output, prometheus for Prometheus, and otlp pointing at Jaeger. Wire a separate pipeline for each signal (logs, traces, metrics). Use debug where the sample has logging. The speaker's full file is in his description and is not shown in the transcript. *When:* The vendor sample is out of date, or you need to send the same telemetry to several destinations.
- **Enable OTLP ingest on the backends** — Turn on the OTLP receiver in Prometheus with a startup argument. Enable OTLP in Jaeger through an environment variable. Expose both to the collector in the observability namespace. The speaker does not name the exact flag or variable on screen. *When:* The collector must push traces and metrics into Jaeger and Prometheus over OTLP instead of scraping them.
- **Verify the pipeline with kubectl** — Check pods are Running and list services in the observability namespace. Run kubectl port-forward to Jaeger and Prometheus, then open their UIs to look for trace and metric data. Read the collector pod's console output, where the debug exporter prints traces, metrics and logs. *When:* After applying the manifests, to confirm the collector is receiving and exporting data before you add application instrumentation.
- **Node.js auto-instrumentation in each service** — Add the OpenTelemetry Node.js auto-instrumentation to the frontend and backend, configured to send OTLP to the collector Service in the observability namespace. Add custom spans or metrics in code if needed. The speaker shows no code, but says the same setup works in both services. *When:* You want application-level traces and metrics, such as HTTP client duration, on top of the mesh's sidecar telemetry.

## Numbers
- Each injected pod runs two containers (the app container plus the Istio sidecar proxy) instead of one. ([1:27](https://youtu.be/76O-1qakUTM?t=87))
- Video length is 5:16. ([0:00](https://youtu.be/76O-1qakUTM?t=0))

## Hot takes
- The title says the OpenTelemetry setup is AMAZING, but the video is a short walkthrough. The collector config and manifests are not shown in the transcript and are linked from the description.
- Near the end the video pitches Better Stack as a place to send the telemetry, which is vendor promotion.
- The claim that mesh telemetry needs no code is accurate only for mesh-level signals. Application traces and custom metrics need the Node.js instrumentation the speaker adds later.
- Quality is capped at 2 for hype title, thin substance (no config shown on screen) and the closing vendor pitch.

## Tools mentioned
Kubernetes, Istio, istiod, Istio Ingress Gateway, OpenTelemetry Collector, OpenTelemetry Node.js auto-instrumentation, Jaeger, Prometheus, MongoDB, kubectl, Node.js, Azure, AWS, GCP, Better Stack

## Relevance to our work
- **agentos** (1/3): AgentOS already lists Prometheus/Grafana and OTel under L4 observability. The video shows a collector with one receiver feeding several exporters and a batch processor, which fits the stack. → *Consider routing AgentOS service telemetry through an OTel Collector pipeline with a batch processor and per-signal exporters, so backends are changed in config rather than in each service.*
