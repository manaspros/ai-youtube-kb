# Learned Execution Graphs for Anomaly Detection & Drift in APIs — Ritvik Pandya, JP Morgan Chase

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `u1yaOeEX4e8` · [watch](https://youtu.be/u1yaOeEX4e8) · **date:** 2026-08-18 · **length:** 19:38 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ritvik Pandya · **orgs:** JPMorgan Chase
- **topics:** observability, infra-cost-scaling, data-engineering · **tags:** execution-graph, DAG, anomaly-detection, drift-detection, OpenTelemetry, baselines, payments, latency, kafka, stream-processing, root-cause-analysis, non-LLM

> JPMorgan payments lead on modeling each API request as a short-lived execution DAG, then using per-segment baselines and drift categories to detect anomalies with fewer false alarms.

## Summary
Ritvik Pandya, who leads payments at JPMorgan Chase, argues that a request's path through gateways, auth, orchestration and parallel downstream services should be modeled as a short-lived DAG built from telemetry, not stored in a persistent graph database. With that DAG he builds a baseline, detects deviation, and localizes the slow node before deciding whether to alert or act. He separates anomalies (one-off deviations) from drift (slow change over time) and classifies drift as structural, load-driven, covariate (input mix shift) or same-request behavior change, each needing a different response. Baselines should be per client, per segment and per endpoint, with a cold-start baseline for new endpoints, to cut alert noise. The pipeline runs asynchronously: OpenTelemetry feeds Kafka and stream processing, with a fast hot path and a slower, more accurate reconciliation path, so the payment request path is not slowed. He flags telemetry lag from one node as a false structural-change risk, and suggests rolling automated fixes out to 5-10% of machines before 100%. The talk is conceptual, with few hard numbers, and the statistical methods are named only briefly.

## Key ideas
- **Model each request's processing as a short-lived DAG built from telemetry** — Nodes are services or steps (edge, gateway, auth, orchestration, parallel calls). Ordering and per-node context come from the graph. Retries and loops are tracked as separate nodes. The graph is ephemeral, unlike a persistent property graph in Neo4j. ([1:14](https://youtu.be/u1yaOeEX4e8?t=74))
- **Use a cheap end-to-end check first and only go deeper on a breach** — Like a boarding-pass check at the airport. If the request's end-to-end baseline looks fine, skip the expensive analysis. If latency is off, then check which node changed and whether it is past threshold. ([3:11](https://youtu.be/u1yaOeEX4e8?t=191))
- **Baselines must be per segment, not global** — A request from a local client and one from overseas have different normal latency, so one threshold makes noisy alerts. Baselines should be set per client, per use case (real-time payments vs wire), and per endpoint. ([4:37](https://youtu.be/u1yaOeEX4e8?t=277))
- **Separate anomalies from drift, then classify the drift** — An anomaly is a one-off deviation. Drift is a slow change in pattern over time, such as a commute that grows from 1 hour to 80 minutes. Drift types: structural (node added or removed), load-driven (a service can no longer handle volume), covariate (input mix changes, such as the share of foreign-currency requests), and same-request behavior change. Each type calls for a different response. ([7:44](https://youtu.be/u1yaOeEX4e8?t=464))
- **Use an asynchronous telemetry pipeline with hot and reconciliation paths** — OpenTelemetry data goes to Kafka, then stream processing. The hot path decides fast enough to automate a fix. The reconciliation path is slower but more accurate. Telemetry is never on the request path, so payment latency is not affected. ([14:14](https://youtu.be/u1yaOeEX4e8?t=854))
- **Delayed telemetry from one node can look like a structural change** — If one of seven nodes reports late, the system sees six nodes and may call it a structural change. Window and timing rules must be tuned to avoid false alarms. Tracking start and end per node suggests a tail-based approach. ([15:22](https://youtu.be/u1yaOeEX4e8?t=922))
- **Confirm with a human and roll out fixes in stages** — After detection and classification, a human confirms. Automate the fix only when the risk is known. Roll it out to 5-10% of machines, monitor, then go to 100%. Label data to help learning. Make the system aware of deployments so it knows when to roll back. ([13:12](https://youtu.be/u1yaOeEX4e8?t=792))
- **Cold start and explainability** — A new endpoint gets its own new baseline and is not forced onto a generic one. Alerts should explain their evidence, since a bare score such as 'health score 22' is not actionable. ([16:24](https://youtu.be/u1yaOeEX4e8?t=984))

## Techniques
- **Request-as-DAG from traces** — Build a short-lived graph per request from spans or telemetry. Nodes are steps, edges are call order, retries and loops are their own nodes. Use it to find the order of execution, the context passed at each node, and which node is slow. *When:* Latency or behavior issues in multi-hop API or gateway paths where you need to localize which hop changed.
- **Tiered detection** — Tier one checks end-to-end latency against a baseline. Only on breach, localize the node and run statistical deviation tests and thresholds. Alert or act only if the deviation is past threshold. *When:* High-volume paths where deep analysis on every request is too costly.
- **Segmented baselines** — Compute a separate baseline per client, region, use case or endpoint. Give new endpoints a cold-start baseline and do not reuse a generic one. *When:* Mixed traffic where normal latency differs by segment, so that global thresholds create noise.
- **Drift classification before action** — For each detected drift, decide whether it is structural, load-driven, covariate or behavioral. Then pick the response: update the topology and baseline, scale or make the call async, add a per-segment baseline, or roll back. *When:* After a drift alert, to choose between re-baselining, scaling and rollback instead of treating all drift the same.
- **Async telemetry to hot and recon paths** — Send telemetry asynchronously to a queue such as Kafka. Run a fast stream job for quick decisions and a slower, more accurate job for reconciliation. *When:* Latency-sensitive request paths where the observability pipeline must not add to request time.
- **Staged automated remediation** — Roll out an automated fix to a small share of machines first (5-10%), watch the metrics, then expand to all nodes. *When:* Any automated change to production routing or scaling.
- **Synthetic training data for detectors** — Generate about seven days of traces with a benchmark telemetry dataset, inject known anomalies, then train the detector before it goes live. *When:* Before launching a detector, when production anomalies are rare and labels are scarce.

## Numbers
- Synthetic benchmark: about 7 days of traces, millions of traces injected to train the detector before go-live (benchmark name garbled in captions) ([6:09](https://youtu.be/u1yaOeEX4e8?t=369))
- Example: overall request processing normally takes about 700 ms ([13:12](https://youtu.be/u1yaOeEX4e8?t=792))
- Example traffic mix at the start: about 60% local and 40% foreign requests, later shifting as the product grows ([10:15](https://youtu.be/u1yaOeEX4e8?t=615))
- Staged rollout of automated remediation: 5-10% of machines first, then 100% ([13:12](https://youtu.be/u1yaOeEX4e8?t=792))
- Illustrative drift: a commute that grows from 1 hour to 1 hour 20 minutes over a year ([7:44](https://youtu.be/u1yaOeEX4e8?t=464))
- Mean time to discovery reduced a lot after moving to single-window detection (no figure given) ([16:24](https://youtu.be/u1yaOeEX4e8?t=984))

## Hot takes
- Baselines should be per client and per use case, not one global number for all requests.
- Drift should be classified before any action, because structural, load and covariate drift need different fixes.

## Tools mentioned
OpenTelemetry, Kafka, Neo4j (mentioned as contrast), KL divergence, MMD, EWMA (exponential moving average)

## Relevance to our work
- **agentos** (1/3): L4 observability uses OTel and Prometheus. The talk's drift classes and per-segment baselines could extend L4, but it is about payments APIs, not agents. → *Read the talk's drift taxonomy (structural / load / covariate) and consider adding segment-level latency baselines to the L4 OTel dashboards.*
- **general** (1/3): Shows the same segmented-baseline and drift-classification ideas that apply to monitoring any LLM or agent traffic. → *When designing monitoring for agent or LLM traffic, test whether one global latency or cost baseline hides segment-level drift.*
