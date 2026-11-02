# Guide: observability

*Synthesized by Sonnet from 97 talks since 2026-05-18.*

Scope: tracing, logging, monitoring and analytics on agent and LLM traffic. In 2026 the topic has merged with evals. Most talks treat the trace as the raw material for everything else.

## State of the art

What practitioners do now, newest first.

- **Trace first, then eval.** Evals are tests whose inputs are traces. Teams read traces by hand, name the failure modes, and only then write evaluators (`SHMCGrNJJGc`, `qZj7sqmidqA`, `obfPzbapMIM`). A trace is a tree of spans: LLM calls, tool calls, agent turns (`BOCjybvJYM4`).
- **Production is the eval set.** Failing traces go into a dataset. A candidate fix is replayed against that dataset and must beat the baseline before it ships (`_zUp6y9bDU8`, `fnuNVFgLjHA`, `TeErpYBUIeM`, `nxokqOq1imY`).
- **Agents now read the traces.** A coding agent with a CLI and a few skills pulls spans, clusters failures, drafts evaluators, and proposes a fix. A human gates the merge (`9HbzAWnKbo4`, `BOCjybvJYM4`, `JJGbw4ggaFs`, `kZsf_Sfm7RU`). Reading millions of traces by hand costs more than running them, so teams sample and automate the first read (`CvRngaQZQ3Y`, `pSto5YaNGUo`).
- **Binary, failure-specific judges.** Yes/no criteria beat 1-10 scores. Judges are validated against human labels like any classifier (`-aM2EDTiaMs`, `hfEczxdNyvU`, `3z2uT5aDx_Y`, `eAXxdtNlK04`, `YXEqC05WEI0`). Deterministic code checks run on everything. LLM judges run on a sample.
- **Three layers of evaluation.** Code checks, rubric LLM judges, and a newer agent-as-judge that reads whole traces and finds unknown failures (`q2JrUKBMf0w`, `fnuNVFgLjHA`). One Databricks talk stacks deterministic, LLM-judge and behavioral checks instead (`ObTPqBGsEbA`).
- **Replay over reproduction.** Agents are not bitwise deterministic. Teams record each step's inputs and outputs and replay with stubs (`Lc8zRh9muoY`, `bZISsg7H7DA`, `0RNNfxpdbQk`). Event logs are the same idea built into the runtime (`UPwGaM2MKHY`, `KHudyx5wW3U`, `vi-2nasppAg`).
- **Cost and safety are first-class signals.** Every LLM call gets cost tags. Token creep and model drift get their own alerts (`rTojoVotlD8`). A gateway or proxy that logs every call is the common place to see traffic (`BM2JX9hqsVQ`, `abw_m-DRi1k`).
- **Agent traces are a new data shape.** They are huge and text-heavy, and people search them by words (`XBaznoTRDFI`, `mUQoVz7THu0`, `_fQ7Z_Wfouk`).
- **OpenTelemetry is the common wire format.** Used for sessions, hooks and voice (`JsCCrBF7F1g`, `32nrHU6zHU8`, `42Bz0TUfeOQ`).

## Consensus patterns

1. **Read traces before writing evals.** Do open coding, then group into root causes, then weigh by frequency times severity (`Xfl50508LZM`, `qZj7sqmidqA`, `SHMCGrNJJGc`, `obfPzbapMIM`).
2. **Flywheel: production failure to dataset to fix to monitor.** Cluster production failures, turn each into an eval case, fix, ship, keep monitoring the same dimension (`ZdheJTfLu-s`, `FB-MLPhL9Ms`, `nxokqOq1imY`, `Emo5FGGY-wM`, `XyV6bSMyq-I`, `hd7TOvmyAxU`).
3. **Binary criteria over scores, and calibrate the judge.** Check the judge on contrasting cases before changing the agent. A judge that over-calls is a judge bug (`YXEqC05WEI0`, `3z2uT5aDx_Y`, `hfEczxdNyvU`, `eAXxdtNlK04`).
4. **Give the judge the agent's context.** A correctness judge with stale knowledge failed 0 of 13 traces on a live-research agent. A faithfulness judge with the same sources worked (`Xfl50508LZM`, `qZj7sqmidqA`, `SHMCGrNJJGc`).
5. **Cheap deterministic signals first, expensive LLM work second.** Regex on user messages, small trained classifiers, code classifiers on traces. Then hand flagged items to an agent as a concrete task (`-aM2EDTiaMs`, `jHMiYtjoJfA`).
6. **Ship slices and compare to a control.** Percentage rollout judged by signal rates (`-aM2EDTiaMs`, `vSx5IULvBns` for deploy watching, `Ib5t2RLtxvM` for private simulation benchmarks).
7. **Record at the node boundary and replay.** Checkpoint code version, config and artifacts per step. Change one variable and replay (`Lc8zRh9muoY`, `bZISsg7H7DA`, `0RNNfxpdbQk`).
8. **Trace the whole session, not just LLM calls.** Group turns into sessions. Score at the smallest scope that answers the question: span, trajectory or session (`JsCCrBF7F1g`, `X1kp-ABIIxQ`, `42Bz0TUfeOQ`, `32nrHU6zHU8`).
9. **Agent-run monitors with a fresh-context reviewer and a human gate.** An hourly log-monitor opens PRs, a separate reviewer critiques them, a human merges (`kZsf_Sfm7RU`, `9HbzAWnKbo4`, `JJGbw4ggaFs`, `zMiSRliEzv4`).
10. **Give the agent an outlet.** A neutral "report" or "vent" tool plus one prompt line turns the agent into a failure sensor. Tune for low noise (`-aM2EDTiaMs`, `KA5kPbdkK2E`).
11. **Tag cost at every call.** Feature, user or org, model, endpoint (`rTojoVotlD8`, `GJX19pNhmSw`).
12. **Protect the eval set from the optimizer.** Keep golden data and scorers off-limits, use fit/validate/test splits, and keep the test set hidden (`aHhB3sjGjkI`, `eAXxdtNlK04`).
13. **Mask sensitive data before traces are stored.** Strip PII at ingestion, not at display time (`obfPzbapMIM`, `YXEqC05WEI0`, `xn8EsW0wxyc`).

## Disagreements & open questions

- **Evals vs monitoring.** Raindrop says production monitoring should replace evals as the main safety net (`-aM2EDTiaMs`). Braintrust and Langfuse treat production traces as the eval dataset, one loop across both environments (`mUQoVz7THu0`, `obfPzbapMIM`). Meta calls evaluation a post-deployment loop (`vljxQZfJ9wY`). Raindrop later said big static eval sets break when the model or harness changes (`jHMiYtjoJfA`).
- **How much to build.** Some build their own trace store (`ON5LIT0M4do`). Most vendors say buy, and argue DIY stacks fail on text-heavy analytics (`_fQ7Z_Wfouk`).
- **Clustering.** One speaker says clusters are not issues and prefers code classifiers (`jHMiYtjoJfA`). Others lean on clustering to find failure modes (`nxokqOq1imY`, `fnuNVFgLjHA`).
- **Fixed rubric vs agent judge.** Fixed rubrics miss new failures (`q2JrUKBMf0w`). The agent-judge talks are vendor pitches with little method detail and no measured accuracy.
- **Trust in automation.** HUD says automated runs need much higher trust than interactive use (`JJGbw4ggaFs`). Others still keep a human at the merge point (`TeErpYBUIeM`, `exiwa9QbQXI`). Where the gate moves is open.
- **Do examples help judge prompts?** One workshop says examples can hurt as well as help (`SHMCGrNJJGc`). Others recommend few-shot examples (`hfEczxdNyvU`, `qZj7sqmidqA`).
- **Open:** a good agent-correctness measure when the task has no verifiable answer (`AQv3qRCG6Gw`). Whether deferred downstream outcomes (PR merged, action taken) are a reliable score (`X1kp-ABIIxQ`). How to store 10-20 MB spans cheaply (`XBaznoTRDFI`).

## How thinking changed over time

- **2026-05-18.** Many talks pitch golden sets, GEPA-style prompt search, and LLM-as-judge (`A48uhxfxbsM`, `Xfl50508LZM`). The counter-view: monitor in production with implicit signals (`-aM2EDTiaMs`). Evals and observability get called one systems problem (`_fQ7Z_Wfouk`).
- **2026-06-18.** The focus moves to what is different about agent observability: quality not uptime, huge traces, domain experts in review (`XBaznoTRDFI`). Coding agents start to consume observability data via skills and CLIs (`vNCY9kXXyDQ`). Lovable and PostHog turn signals into fixes (`KA5kPbdkK2E`, `zMiSRliEzv4`).
- **2026-07-18.** Replay, checkpoints and event logs appear (`Lc8zRh9muoY`, `bZISsg7H7DA`, `UPwGaM2MKHY`). Production telemetry is named the eval dataset (`vljxQZfJ9wY`). Post-launch loops with agents that open PRs appear (`kZsf_Sfm7RU`).
- **2026-08-18.** The agents-reading-traces pattern dominates. HUD, Arize and LangChain show agents mining traces and proposing fixes (`JJGbw4ggaFs`, `9HbzAWnKbo4`, `CvRngaQZQ3Y`). Simulation from traces becomes common (`Ib5t2RLtxvM`, `3z2uT5aDx_Y`, `31GUkCBD-Uc`). 
- **2026-09-18 to 09-27.** Pass@k versus pass^k is proposed for loop agents (`nxokqOq1imY`). Cost attribution per run, not per request, gets its own talk (`GJX19pNhmSw`). Attribution headers are propagated like trace IDs (`wCIYViPd4SU`). W&B shows prod and research agents on one trace format (`XyV6bSMyq-I`, `hd7TOvmyAxU`).
- **2026-10.** Vendors converge on one loop: trace, score online, cluster, fix with a coding agent, replay failing traces, gate in CI (`hfEczxdNyvU`, `fnuNVFgLjHA`, `_zUp6y9bDU8`, `obfPzbapMIM`, `TeErpYBUIeM`). Datadog frames LLM monitoring as a layer on golden signals (`rTojoVotlD8`).

## Numbers worth remembering

- Frustration rate fell 37% to 9% after one prompt change, found by classifier signals (`-aM2EDTiaMs`). An LLM judge on every output would roughly double AI spend (`-aM2EDTiaMs`).
- Trace sizes: spans of 10-20 MB, traces over 1 GB (`XBaznoTRDFI`). Typical span is a couple of KB (`_fQ7Z_Wfouk`). Traditional heartbeat records are KB-sized (`mUQoVz7THu0`).
- Judge calibration used about 100 hand labels in train/dev/test. An 84% vs 88% gap on 50 traces is too small to call (`3z2uT5aDx_Y`). First offline simulation scored 90%+, which the team judged too good to be true (`3z2uT5aDx_Y`).
- Built-in correctness judge: 0 of 13 and 0 of 16 traces passed due to stale knowledge. Faithfulness judge flagged 7 of 13 and 14 of 16 as unfaithful (`qZj7sqmidqA`, `SHMCGrNJJGc`).
- Sampled LLM judges at 5-10% once a baseline is set (`ZdheJTfLu-s`). Topics pipeline priced at $0.06 per M input and $0.48 per M output tokens; needs 100+ facet matches (`hfEczxdNyvU`).
- Four-level cost tags. Token creep can raise cost up to 8x; Opus-class can be 15x Haiku per request; about 70% of spend sometimes redundant (`rTojoVotlD8`).
- A broker agent turned a $1,000 order into 1,000 shares (about $190,000 exposure) with 200 OK and green dashboards (`Lc8zRh9muoY`).
- Tau-bench: a model passing 60% of the time is self-consistent about a quarter of the time. So one replay is weak evidence (`bZISsg7H7DA`).
- Ceiling test: production agreed with itself about 93%. The cheaper model disagreed 18% before that baseline (`8g1N_a3h9H0`).
- Prompt search: 85-87% simple, 92% hand-written, 96.7% GEPA (`A48uhxfxbsM`). A fit/validate loop got 68% to about 83%, with most gain in iteration one (`eAXxdtNlK04`). Auto-agent raised a toy agent 18% to 83% in about 10 iterations (`aHhB3sjGjkI`).
- Agent traces: reading them costs more than running agents at scale, so sample (`pSto5YaNGUo`). Harness engineering cycle about two minutes (`CvRngaQZQ3Y`).
- Post-launch: PR plus review agents make about 10 times more PRs than three people can review (`kZsf_Sfm7RU`). Ready PR about half an hour after detection (`kZsf_Sfm7RU`).
- Reliability perception: 80% needs monitoring, about 92% lets customers hand over workflows (`Emo5FGGY-wM`, speaker claim).
- Voice agents: about 10% error rate across about 10,000 monitored agents (`qStB9GbppMU`). Arize cites 2.4 s of dead air found only in audio (`42Bz0TUfeOQ`).
- Bench client can be the bottleneck: 38 of 200 requested QPS (`l1-D89bAuOA`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Coverage: every creator video cited in this section is from Better Stack, a hosted logging vendor whose platform is the sink in most demos. None of the cited videos come from Kai Explains or AI LABS, so this section has no evidence from those two channels. Most items are tutorial steps, not measured results. Single-video claims and sponsored segments are flagged.

### Practical playbook

1. Pick log levels by what the app can do next. Unrecoverable failure: critical, then exit. Handled but unexpected: error, with a fallback. Needs future attention: warning. Normal milestones: info. Developer-only detail: debug (`myxlDVC2K74`).
2. Emit one canonical line per request, at the end. Include the user action, identity, outcome, total duration and time spent in the database. Debug from that line before opening detail logs (`I2mWnh66Bkg`).
3. Keep 100% of error and warning logs. Sample success logs, and sample hot endpoints harder. The speaker's example is 20% of identical login events. His claim of an 80%+ log-cost cut is unmeasured (`I2mWnh66Bkg`).
4. Cap Docker json-file logs. In /etc/docker/daemon.json set `log-driver` to json-file, and `log-opts` to max-size 20m, max-file 5, compress true. Restart Docker, then recreate the containers (`Zlj39xXPu2k`).
5. Rotate app logs with logrotate. Keep the default `create` when the app reopens its log file. Add `copytruncate` only for apps that cannot reopen it. Test one config with `sudo logrotate --force <file>`, then check that the live file is zero bytes (`-tM6DsYam0c`).
6. Add a heartbeat to each scheduled job. Ping the heartbeat URL only after the work succeeds. Set the grace period to about 20% above the expected duration. The 20% figure is Better Stack's own guidance (`gMOkw_x9ByY`, `nurgToSGoUM`).
7. Make logs structured. In Python, use python-json-logger: `handler.setFormatter(JsonFormatter())`, and pass per-request fields with `extra=` (`aJCK0LWz8kg`). In Node, Pino emits JSON by default. Set the threshold with its `level` option. Its default values are info=30 and error=50, so a warn threshold hides info (`fluDEkA1h6w`).
8. Keep sink tokens out of code. Read them from an env var or a secret store (`aJCK0LWz8kg`).
9. Redact in the pipeline as well as in app code. Strip or mask card numbers, SSNs and API keys in a Collector processor before storage. In code, log IDs rather than whole objects (`I2mWnh66Bkg`).
10. Move slow log sinks off the request thread. Put the SMTP or network handler behind QueueHandler and QueueListener. Attach email only at CRITICAL. The speaker measured about 2.3 s added to one endpoint response by a direct SMTP handler. Stop the listener on shutdown, or queued records are lost (`_UgXBArTWOA`).
11. Build the Collector config from three parts: receivers, processors and exporters. Add a batch processor (defaults: release after 200 ms or 8192 items). Wire one pipeline per signal. Components defined but not wired into a pipeline are silently ignored. Scrape the Collector's own metrics on port 8888 every 10 s (`4ACQhkJBKyA`).
12. Centralize Linux logs over TCP. On the collector, enable TCP reception on 514 and open the firewall. On each client, add `*.* @@<central-host>:514` to /etc/rsyslog.d/50-default.conf and restart rsyslog. Check with `logger` on the client, then tail the per-host file on the collector (`JocDslKu3j4`).
13. Keep one trace per inbound request. Make each operation a child span, and pass the span context into every outbound call. If one user request shows up as several traces, convert them into child spans under one root (`A-nbuPugjxo`).
14. Measure hidden agent-side model calls. Turn on Claude Code's OpenTelemetry export, group requests by query source, and compare tokens per source. JSONL-based usage tools miss these calls. Single creator video. The speaker measured about 12% of cost in one sleep test and about 8% in a three-agent build. Anthropic's own figure is lower (`F4h3a8HFBSE`).
15. Expect background-agent overhead to grow with wall-clock time. Each working agent triggers a summary call about every 30 seconds. The only workaround the video names is setting the subagent setting to zero, which also removes forked subagents (`F4h3a8HFBSE`).
16. Alert on DNS TXT volume. Flag one host that makes many TXT lookups to odd subdomains of one parent domain. Run an internal resolver so lookups stay visible. The "hundreds" threshold is the speaker's example, not a benchmark (`66EG2a81_rE`).
17. Set retention by log type. Example values: errors about 90 days, debug about 7, security audit about a year, then cold storage (`I2mWnh66Bkg`).

### Tools creators recommend

- Better Stack: hosted logs, metrics, heartbeats and alerts. Default sink in most tutorials. Vendor channel. The sponsored segment in `uRA7qee4Frg` is a plug, not part of the comparison (`uRA7qee4Frg`, `4ACQhkJBKyA`).
- OpenTelemetry Collector: vendor-neutral receive, process and export. The main pitch is switching backends without app changes (`4ACQhkJBKyA`).
- Vector: log transforms with VRL. The review rates it better than the Collector for logs and metrics (`uRA7qee4Frg`, `We7s8KFY7Qg`).
- Fluentd: tail, parse and route, with a pos_file so reads survive restarts (`ephdg9usWyc`).
- rsyslog: central syslog, with one drop-in file per app (`JocDslKu3j4`, `fgdXuqiyUKs`).
- logrotate: rotation and compression for flat log files (`-tM6DsYam0c`).
- Dozzle: web UI over Docker container logs, with the socket mounted read-only (`4ynKW5rwd1E`).
- Jaeger: trace backend that accepts OTLP (`E956jBlMKcA`).
- Language loggers: Pino (`fluDEkA1h6w`), Winston (`YjEqmINAQpI`), Loguru (`gSc1oHcwkE4`), Monolog (`GLbeuxNAcn8`), Go slog (`_mqB7LLgwgs`).
- Claude Code OpenTelemetry export: groups agent calls by query source (`F4h3a8HFBSE`).
- MindWalk: 3D session replay and an LLM judge for Claude Code and Codex logs. Read-only. Single review with no measurements (`Y_7_rbtQXcs`).
- Dograh: self-hosted voice agent with a per-call transcript, trace and recording. Single review, with no cost or latency benchmarks (`xD9JEvfCH9k`).

### Where creators agree or clash with the conference talks

- Agree: cost is a first-class signal. The creator on hidden Claude Code calls (`F4h3a8HFBSE`) matches the conference view of cost tags on every call.
- Agree, with a stricter line: keep a human at the production gate. The SRE podcast says AI should change production only on a constrained, well-defined path, and that letting AI push infrastructure changes without human input is irresponsible (`K7y8ZAHQYGY`). Conference talks (see State of the art, agent-run monitors) let agents open PRs and verify fixes, with a human merge. The podcast's view is opinion and one client case, with no data.
- Clash in focus: creators barely touch model output quality. They stop at structure, delivery and alerting: logs answer what happened, metrics answer whether a service is healthy (`I2mWnh66Bkg`). The conference talks center on judges and evals over traces. Creators leave that gap open for LLM apps.
- Tension on volume: the conference talks say read whole sessions and score at the smallest scope that answers the question. The creators sample successes and keep all errors. My synthesis: sample for cost, but keep every failing trace as eval input.
- Agree on OpenTelemetry as the wire format. The creator verdict is split: the Collector for traces and vendor decoupling, Vector for logs (`uRA7qee4Frg`).

### Watch first

- `F4h3a8HFBSE` — the only creator piece on hidden agent-side model calls. Most relevant to our Claude Code and ProsHarness cost questions. Single video; the subagent-setting name is not clear in the captions, so check the docs.
- `I2mWnh66Bkg` — canonical line, sampling, redaction and retention in one 12-minute pass. Treat the savings numbers as the speaker's claims.
- `4ACQhkJBKyA` — the cleanest walk through Collector pipelines and batch defaults. Use it as the config template.
- `uRA7qee4Frg` — a fair log-versus-trace comparison. Skip the sponsored Better Stack segment.
- `_UgXBArTWOA` — concrete gotchas: logging latency on the request path, and listener shutdown.
- `K7y8ZAHQYGY` — an SRE view on AI-driven change volume and automation limits. Long and opinion-heavy.

## Watch first

- `Lc8zRh9muoY` — short and clear case for replay instead of determinism, with the node-boundary recording design.
- `bZISsg7H7DA` — checkpoint, counterfactual replay and cohort verdicts. Fixes single-replay overconfidence.
- `-aM2EDTiaMs` — implicit signals, regex, self-diagnostic report tool, ship-versus-control. Most reusable cheap tricks.
- `qZj7sqmidqA` — best hands-on guide to error analysis and judge design, with real failing numbers.
- `kZsf_Sfm7RU` — fast loop plus slow loop for post-launch monitoring, with a fresh-context reviewer.
- `XBaznoTRDFI` — why agent traces break ordinary data stacks (size, full text, two read patterns).
- `rTojoVotlD8` — practical tagging and metric list on top of golden signals.

## Implications for our projects

- Agent traces are large, semi-structured and searched by text. Plan hot and cold paths, keep big payloads apart from small telemetry rows, and add full-text search plus SQL access (`XBaznoTRDFI`, `mUQoVz7THu0`).
- Capture heavy detail only above a threshold such as p99 to limit noise (`JJGbw4ggaFs`).
- Detect latency anomalies per segment (client, endpoint), not globally. Check end-to-end first, localize only on breach (`u1yaOeEX4e8`).

**AgentOS L1 Govrix Scout and L4 observability.**
- Proxy-level logging is the right place for full request and response logs, per-identity budgets and per-tool-call hooks (`BM2JX9hqsVQ`, `abw_m-DRi1k`).
- Add four-level cost tags (feature, user, model, endpoint) to every proxied call, plus token-creep and model-drift alerts (`rTojoVotlD8`).
- Move budgets and tags to the run level, not only the request level. Steer first, halt last (`GJX19pNhmSw`).
- Propagate an attribution header like a trace ID (`wCIYViPd4SU`).
- Keep the Merkle audit log as the receipt: trigger, identity, state used, call with idempotency key, external result (`BInpv7lGp1o`).
- Mask PII before traces persist (`obfPzbapMIM`).
- Emit OTel spans that follow one open schema for LLM traffic, so new providers need only a mapping (`42Bz0TUfeOQ`).

**AgentOS MemoryMesh and SkillForge.**
- RAGAS evals sit well with failure-mode evaluators (`BOCjybvJYM4`). Log search queries to find gaps (`vNCY9kXXyDQ`).
- SkillForge success signal: use stuck-to-unstuck transitions and user corrections as evidence (`KA5kPbdkK2E`, `RGiXcVxSD3s`). Test injection with blank holdouts (`KA5kPbdkK2E`).
- Score skills with a few plain-language checks run by an LLM over file and trace state (`vNCY9kXXyDQ`). Use a hidden test set and a fit/validate split so the optimizer cannot overfit (`eAXxdtNlK04`, `aHhB3sjGjkI`).
- Add provenance to every memory (`9_oy4owGtPI`).

**AgentOS InferCraft and benchmarks.**
- Report phase-split metrics: time to first token, inter-token latency, prefix reuse, per-replica QPS (`woIYJYd_etI`).
- Sweep concurrency to find the knee, and change one flag at a time (`4n08JHb90hI`).
- Report multiple metrics and at least five runs per configuration, not one average (`YIxzNZDDy1A`).
- Debug silent wrong output with a logprob oracle against a reference pass (`btxG75rNJC4`).
- Use cost per successful task as the headline KPI (`7c9FSUVcXR0`).

**ProsHarness.**
- Add a fresh-context critic stage that scores each run's PR without planning context. Compare it to the Codex critique (`kZsf_Sfm7RU`, `TeErpYBUIeM`).
- Checkpoint beyond tool I/O: code version, config, environment. Support counterfactual replay and cohort-level diffs (`bZISsg7H7DA`, `Lc8zRh9muoY`).
- Keep an append-only event log as the source of truth. Persist pending approvals as events so a fresh worker shows the same prompt (`UPwGaM2MKHY`).
- Give each run a deadline, a cancel path and a terminal outcome (`BInpv7lGp1o`).
- Phone approvals: store approvals as scoped records bound to actor, run, tool, exact args and expiry (`BInpv7lGp1o`).

**Evals, entity resolution and Haiku pipelines.**
- Use binary, failure-specific judges. Validate against human labels with a held-out split (`SHMCGrNJJGc`).
- Run a ceiling test: run the same model three times to get the noise floor before judging a cheaper model (`8g1N_a3h9H0`).
- Turn each production miss into a task (`XyV6bSMyq-I`). Report pass@k for capability and pass^k for reliability (`nxokqOq1imY`).
- Add negative cases: the agent must not take a harmful action (`xyL2Ltkh-SA`).
