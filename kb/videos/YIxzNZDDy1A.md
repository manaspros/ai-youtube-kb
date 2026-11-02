# From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `YIxzNZDDy1A` · [watch](https://youtu.be/YIxzNZDDy1A) · **date:** 2026-10-12 · **length:** 52:30 · **format:** workshop · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Wolfram Ravenwolf · **orgs:** Weights & Biases, CoreWeave, Daytona, OpenRouter, UK AI Security Institute
- **topics:** evals, observability, sandboxing-execution, coding-agents · **tags:** agent benchmarking, terminal-bench, harbor, reproducibility, variance, solve rate, consistency, cost per task, wolfbench, weave traces, thinking effort, overthinking, sandbox per task, openrouter provider pinning, refusals

> Wolfram Ravenwolf's hands-on workshop on building a reproducible agent benchmark (Terminal-Bench via Harbor, WolfBench dashboard), arguing that one averaged score hides variance, cost and configuration choices.

## Summary
Ravenwolf runs a live workshop on evaluating agents with Terminal-Bench 2.0 run through the Harbor framework in per-task cloud sandboxes. His core argument is that a single aggregate score is not enough: he reports solve rate, a consistency floor, best/worst spread and a ceiling across five runs, plus tokens and cost. He stresses that a benchmark result describes a whole configuration (harness version, model and provider, context size, thinking effort, system prompt, timeouts, concurrency, retries, sampling), so any change means a different experiment. He shows how he pins versions, isolates each task in a sandbox, separates infrastructure errors from model failures, and audits runs for inference problems. The workshop uses his WolfBench toolkit to aggregate 443 local runs and publish charts, and he traces surprising results back to agent transcripts. Several concrete findings come from this: a cheap Flash model used so many tokens it cost more than a frontier model, and raising thinking effort on Opus lowered the score because the model overthought. Much of the session is setup walkthrough and vendor promotion (W&B, CoreWeave), so the reusable part is the methodology checklist and the trace-first debugging habit.

## Key ideas
- **A single average score hides the distribution** — Performance is a distribution, not a point. Averages from leaderboards do not show lucky runs, hidden trade-offs or why people's numbers differ. A single run is a 'benchmark lottery', so he runs five trials per configuration. ([4:20](https://youtu.be/YIxzNZDDy1A?t=260))
- **Report several metrics, not one** — He looks at the average, the best and worst run, the consistency floor (share of tasks solved in every run), and the ceiling (share solved at least once). A high floor means reliability. A wide best-worst gap means high variance. Tokens and cost are part of the score. ([5:42](https://youtu.be/YIxzNZDDy1A?t=342))
- **You are benchmarking a configuration, not a model** — Dataset version, harness version, model provider endpoint, sandbox backend, and every setting are variables. Changing any one of them makes it a new experiment. Provider-side inference updates can also change results without notice. ([7:03](https://youtu.be/YIxzNZDDy1A?t=423))
- **Isolate each task in its own sandbox and pin versions** — Running agents on your own machine lets runs contaminate each other. He uses a fresh cloud sandbox per task and pins the harness version, and suggests keeping a fork so you can backport fixes without changing versions. ([9:41](https://youtu.be/YIxzNZDDy1A?t=581))
- **Tokens and cost can flip the ranking** — Gemini 3.5 Flash scored close to GPT-5.5 but used about 1.65 billion tokens versus 136 million, so it cost more ($620 vs $497). A cheap per-token model can be the expensive choice. ([37:03](https://youtu.be/YIxzNZDDy1A?t=2223))
- **Surprising scores should be checked in the traces** — Raising thinking effort on Opus lowered its score. Traces showed it overthinking, spending minutes on reasoning before trying commands, while the other model used quick trial and error and got more turns done. He also found a model looking up the published solution, which he treats as a legitimate finding about tool access. ([45:05](https://youtu.be/YIxzNZDDy1A?t=2705))
- **Separate infrastructure failures from model failures** — Retry sandbox or infra crashes, but not crashes the model caused. Scan each run for repeated characters or chat-template tokens leaking into responses, which point to tokenizer or inference-server problems. Newly released models often improve weeks later as inference engines mature. ([23:15](https://youtu.be/YIxzNZDDy1A?t=1395))
- **Concurrency and quotas can silently corrupt results** — High parallelism can hit endpoint rate limits or sandbox resource caps, causing timeouts and missing scores. He recommends choosing concurrency from the provider's limits, and notes that a timeout of about one hour worked better than two hours, where stuck tasks just loop until they fail. ([21:51](https://youtu.be/YIxzNZDDy1A?t=1311))

## Techniques
- **Multi-metric leaderboard per configuration** — Run each configuration at least five times. Compute the mean, best and worst run, the consistency floor (tasks solved in every run), the ceiling (tasks solved at least once), and token use and cost. Plot them together and read the band width as variance. *When:* Comparing models or agents where reliability matters more than a single headline number.
- **Pin the harness and keep a fork** — Install the evaluation harness at a fixed version with a tool installer in an isolated environment. Fork it and backport only the fixes you need, rather than upgrading mid-series. *When:* Any benchmark you plan to compare over time or publish.
- **Sandbox per trial with bounded concurrency** — Give each task a fresh cloud sandbox. Set concurrency based on the endpoint's rate limits and the sandbox resource quota. Watch for timeouts and missing scores at high parallelism. *When:* Parallel agent runs where state must not leak between tasks, and the machine must not be changed by the agent.
- **Smoke-test one task before the full run** — Run a single small task first to check the full pipeline: install, sandbox start, agent run, verifier, result collection. Only then launch the full set. *When:* Before any expensive benchmark run.
- **Explicit retry policy by error class** — Define which errors are infrastructure errors (retry) and which are model behaviour (score as failure). Log each class separately after every run. *When:* Any run where sandboxes or endpoints can fail independently of the model.
- **Set and record every sampling and agent setting** — Record context window size, thinking effort, system prompt, tool access, sandbox CPU and memory, task timeout, temperature, top-p, max tokens and seed. Do not set temperature to zero if the provider recommends a non-zero value. Pin the router provider when using OpenRouter. *When:* Publishing results, or any time someone else must reproduce the number.
- **Trace-first debugging of surprising scores** — Click through from the chart bar to the individual run transcripts. Check the initial prompt, each command, and where the agent looped or overthought. Use an agent to summarise the traces, but verify the links it cites. *When:* A score moves unexpectedly, such as after a settings change or a model swap.
- **Shareable result snapshot** — Export all run results to one JSON file, then generate charts from that snapshot. Publish the snapshot and the trace links so others can inspect the same data. *When:* Sharing benchmark results that others need to audit.

## Numbers
- Terminal-Bench 2.0 has 89 tasks; the speaker runs five trials per configuration ([5:42](https://youtu.be/YIxzNZDDy1A?t=342))
- Speaker says 2.1 fixes only 28 of the 89 tasks, and he stays on 2.0 so results stay comparable ([11:04](https://youtu.be/YIxzNZDDy1A?t=664))
- Default task timeouts range from about 5 minutes to over 3 hours; he moved from a 2-hour timeout to about 1 hour ([20:29](https://youtu.be/YIxzNZDDy1A?t=1229))
- Gemini 3.5 Flash used about 1.65 billion tokens vs 136 million for GPT-5.5 on the same benchmark ([37:03](https://youtu.be/YIxzNZDDy1A?t=2223))
- Estimated cost: Gemini 3.5 Flash $620 vs GPT-5.5 $497 ([42:20](https://youtu.be/YIxzNZDDy1A?t=2540))
- Codex with GPT-5.5 cost almost $1,000 vs $282 for Cursor with the same model ([43:40](https://youtu.be/YIxzNZDDy1A?t=2620))
- Claude Fable produced 13 refusals on the benchmark and was the most expensive run at about $11,000 ([43:40](https://youtu.be/YIxzNZDDy1A?t=2620))
- Speaker has run 430 runs so far (later counted as 443 unique runs after local scan) ([31:47](https://youtu.be/YIxzNZDDy1A?t=1907))
- Total spend displayed for the runs was almost $40K, partly on his own inference ([33:23](https://youtu.be/YIxzNZDDy1A?t=2003))
- Consistency floor example: about 60% of tasks solved in every run for one configuration; best-to-worst range of 79% to 60% indicates high variance ([35:34](https://youtu.be/YIxzNZDDy1A?t=2134))
- Context window served at 256K instead of the advertised 1M for GLM 5.2 on the speaker's inference endpoint ([17:45](https://youtu.be/YIxzNZDDy1A?t=1065))

## Hot takes
- One benchmark score is not enough. Report the spread, the consistency floor and the ceiling as well.
- A cheap-per-token model can cost more than a frontier model if it uses far more tokens.
- Raising thinking effort can make a model worse, because it overthinks and takes fewer useful turns.
- Most published leaderboard numbers are hard to compare because settings like sampling, timeouts and agent version are not reported.
- Model refusals should be scored and reported, not hidden; a refusal can be the biggest cost driver.

## Tools mentioned
Harbor, Terminal-Bench 2.0, Terminus 2, Weights & Biases Weave, WolfBench, Inspect (UK AISI), Marimo, CoreWeave serverless sandboxes, Daytona, OpenRouter, Docker, uv, Codex, Claude Code, Cursor

## Relevance to our work
- **agentos** (2/3): AgentOS already plans RAGAS evals and load tests, and the next-phase thesis is to prove it with benchmarks. The talk's method for multi-run variance, consistency and cost reporting applies directly to how we should report agent-level results. → *Extend the AgentOS eval report so each agent or model config is run at least five times and shows mean, worst, best, solved-every-run and tokens/cost, with the full config (sampling, timeout, concurrency, versions) saved next to each result.*
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI. The talk's findings on thinking effort (Opus scored worse at max effort because of overthinking) and task timeouts (one hour is more useful than two) are directly relevant to long agent runs and retry or timeout policy. → *Before raising thinking effort in long ProsHarness runs, compare two or three effort levels on a small task set, read the traces for overthinking loops, and record the Claude Code version and effort setting in the checkpoint metadata.*
- **agentos** (1/3): Per-task sandbox isolation matches the Crucible sandboxing layer, but the talk is about benchmarking, not the execution layer itself. → *When Crucible runs benchmark-style tasks, consider one sandbox per trial and record sandbox CPU and memory limits, since the talk shows these can change the score.*
