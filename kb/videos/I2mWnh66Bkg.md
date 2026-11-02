# 12 Logging BEST Practices in 12 minutes

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `I2mWnh66Bkg` · [watch](https://youtu.be/I2mWnh66Bkg) · **date:** 2025-11-02 · **length:** 12:00 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Twitter, GitHub
- **topics:** observability, dev-tools, infra-cost-scaling, security-guardrails · **tags:** logging, structured-logging, log-sampling, canonical-log-lines, log-retention, log-redaction, opentelemetry, go-slog, centralized-logging, metrics-vs-logs

> A generic logging best-practices list: plan what to log, use levels and structured fields, sample high-volume logs, emit one canonical line per request, centralize, set retention, redact secrets, and watch logging overhead.

## Summary
A short Better Stack tutorial giving twelve logging practices for production debugging. It starts with planning logs around goals and KPIs and overlogging early, then covers the four log levels (info, warn, error, fatal) with a runtime verbosity switch. The speaker argues for structured logs with per-field data and lists what each entry should carry: request IDs, user IDs, system state and full error context. Sampling is presented as the main cost lever, with error logs kept in full and success logs sampled. The talk recommends canonical log lines (one wide event per request), then centralization and correlation across services, with distributed tracing offered as a better option. It closes with retention tiers, encryption and access control, redaction of secrets, a benchmark of logging overhead in Go, and the point that logs explain problems while metrics signal them. Nothing is sponsored, but the content is generic and the speaker's numbers are mostly unsourced.

## Key ideas
- **Plan logging around goals before writing statements; overlog first, then trim the noise.** — Ask what the app's main goals, critical operations and KPIs are. Overlogging and pruning later is easier than adding missing context during a production incident. Periodically review what is noise. ([0:00](https://youtu.be/I2mWnh66Bkg?t=0))
- **Use the four levels (info, warn, error, fatal) and keep a way to raise verbosity on demand.** — Production usually runs at info. Verbosity should be raised temporarily during bug hunts, so the app needs a runtime control for it. ([1:13](https://youtu.be/I2mWnh66Bkg?t=73))
- **Structured logs with one field per datum are far more useful than free text.** — Fields can be filtered and aggregated (for example, counting timeouts per day). Logging frameworks help, and a tool such as Vector can convert unstructured output to JSON. The speaker's line: unstructured logs are expensive text files. ([2:30](https://youtu.be/I2mWnh66Bkg?t=150))
- **Every entry should answer who, what, where and why.** — Include request IDs for tracing across services, user IDs for session context, system state such as database or cache status, and full error context such as stack traces where relevant. The speaker frames logs as a black-box recorder that should allow replaying a scenario. ([3:47](https://youtu.be/I2mWnh66Bkg?t=227))
- **Sample high-volume logs and be selective about what gets sampled.** — Store a representative sample, for example 20% of identical login events. Keep all error logs during an error spike while sampling success logs, sample hot endpoints harder, and keep full logs for critical paths. The speaker claims this can cut log costs by 80% or more. He advises adding sampling early. ([3:47](https://youtu.be/I2mWnh66Bkg?t=227))
- **Emit a canonical log line at the end of each request.** — One wide event per request captures the user action, who the user was, what failed, duration and time spent in the database. The speaker calls it a TLDR per request. He says distributed tracing with OpenTelemetry is a better way to link a request's journey across services. ([5:12](https://youtu.be/I2mWnh66Bkg?t=312))
- **Centralize logs early, and set retention by log type.** — Centralization allows cross-service search and correlation (a slow payment service causing a cart timeout that shows as a frontend error). Example retention: errors 90 days, debug 7 days, security audit logs about a year, with older logs moved to cold storage. ([6:09](https://youtu.be/I2mWnh66Bkg?t=369))
- **Protect logs: encrypt in transit and at rest, apply access controls, and never log secrets.** — Logs often hold user IDs, IPs, queries and internal error details. Junior developers may see basic logs, senior engineers more, and security more again. The speaker cites Twitter's 2018 plaintext-password incident as a warning. A Go slog pattern is shown where logging a whole user object emits only the ID. Redaction filters belong in the pipeline (he recommends the OpenTelemetry Collector) before storage. ([8:45](https://youtu.be/I2mWnh66Bkg?t=525))
- **Logging has a CPU and memory cost, so measure it.** — The speaker's Go benchmark: about 192,000 requests per second with no logging, a roughly 20% drop with Logrus (transcribed as Logris), and about 3% with slog. Practices: efficient library, sampling on hot paths, a separate disk partition for logs, and load tests to find logging bottlenecks. ([10:05](https://youtu.be/I2mWnh66Bkg?t=605))
- **Use logs to debug and metrics to alert.** — Logs answer what happened. Metrics answer how often and show trends. Answering whether a service is healthy right now is tedious with grep, so metrics and alerts should drive detection. ([10:05](https://youtu.be/I2mWnh66Bkg?t=605))

## Techniques
- **Canonical log line per request** — At the end of each request, emit one structured entry with the user action, user identity, outcome, total duration, and time spent in dependencies such as the database. Investigate from that single entry before opening detail logs. *When:* Request-driven services where debugging means stitching together many log lines.
- **Selective sampling** — Keep 100% of error and warning logs. Sample success and high-traffic endpoint logs (the speaker's example is 20% of identical login events). Sample hot paths more aggressively and keep full logs on critical paths. Apply it early, through the logging framework or OpenTelemetry. *When:* Log volume reaches hundreds of GB or TB per day, or log cost starts to spike.
- **Redaction in the pipeline** — Run a filter in the collector (the speaker recommends the OpenTelemetry Collector) to strip or mask card numbers, SSNs and API keys before storage. In code, log IDs rather than whole objects; the speaker shows a Go slog approach for this. *When:* Any service whose logs could carry PII or credentials.
- **Tiered retention policy** — Set retention per log type, for example errors about 90 days, debug about 7 days, security audit about 1 year. Move older logs to cold storage, then delete. *When:* Before the first large log storage bill.
- **Load test logging overhead** — Benchmark the service with no logging, then with the chosen logger and with sampling. Pick an efficient library, sample hot paths, write logs to a separate disk partition, and run load tests before shipping. *When:* High-throughput services where logging could cut throughput.

## Numbers
- Baseline Go web server with no logging handles about 192,000 requests per second ([10:05](https://youtu.be/I2mWnh66Bkg?t=605))
- Adding Logrus logging drops throughput about 20% (speaker's benchmark) ([10:05](https://youtu.be/I2mWnh66Bkg?t=605))
- Using Go's slog drops throughput about 3% ([10:05](https://youtu.be/I2mWnh66Bkg?t=605))
- Log sampling at 20% stores 2 of 10 identical login events; speaker says it can cut log costs 80% or more ([3:47](https://youtu.be/I2mWnh66Bkg?t=227))
- High-traffic systems can generate hundreds of GB to terabytes of logs per day ([3:47](https://youtu.be/I2mWnh66Bkg?t=227))
- Example retention: error logs 90 days, debug logs 7 days, security audit logs about 1 year ([7:17](https://youtu.be/I2mWnh66Bkg?t=437))
- Twitter forced a password reset for all users in 2018 after logging passwords in plain text (speaker's claim, not verified here) ([8:45](https://youtu.be/I2mWnh66Bkg?t=525))

## Hot takes
- Unstructured logs are just expensive text files.
- Overlog during development and trim later, since removing noise is easier than adding missing context in production.
- Use metrics, not logs, to decide whether a service is healthy; logs are for debugging.
- Canonical log lines or distributed tracing are a better model than a stream of per-step log entries.

## Tools mentioned
OpenTelemetry, OpenTelemetry Collector, Vector, Go slog (log/slog), Logrus (transcribed as Logris), Go

## Relevance to our work
- **agentos** (2/3): AgentOS has a Merkle audit log and PII/prompt-injection scanning in Govrix Scout, and L4 observability. Its agent request logs could follow the canonical-line, sampling and redaction-in-collector patterns. → *Emit one canonical log line per proxied agent request (user, tenant, route, budget decision, PII-scan verdict, latency, DB time), and test whether redaction runs in the OTel Collector before storage.*
- **prosharness** (1/3): Checkpoint/resume of long Claude Code runs would benefit from structured per-step logs, but the talk does not cover agent runs or checkpointing. → *Consider structured, per-run JSON logs with a run ID for each checkpoint and resume event.*
