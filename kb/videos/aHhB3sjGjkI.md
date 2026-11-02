# Agents Building Agents - Alfonso Graziano, Nearform

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `aHhB3sjGjkI` · [watch](https://youtu.be/aHhB3sjGjkI) · **date:** 2026-07-18 · **length:** 30:14 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Alfonso Graziano · **orgs:** Nearform
- **topics:** evals, skills-self-improvement, observability, coding-agents · **tags:** auto-research, auto-agent, golden-dataset, eval-driven-development, trace-clustering, branch-per-hypothesis, rollback, harness-engineering, live-feedback, Mastra, Claude Code

> Alfonso Graziano (Nearform) shows coding agents improving other agents: an eval-driven loop lifts a toy agent from 18% to 83% and a production agent from 67% to 86%, and a trace-clustering loop turns live user feedback into fixes.

## Summary
The speaker frames an AI agent as an LLM in an agentic loop with tools and retrieved context, and says the main failure classes are poor eval scores and poor live-data performance. He builds a golden dataset with subject matter experts and pairs it with scorers that act as a non-deterministic test suite. A naive hello-world agent (built with Mastra) starts at an 18% pass rate, and failures come from missing tools, weak system prompts, and poor context retrieval. He adapts Karpathy's auto-research idea into "auto agent", a loop where a coding agent (Claude Code is named) edits prompts, tools and code, reruns evals, and keeps or rolls back each change on a branch per hypothesis. A shared memory file and a per-iteration report let later iterations learn from earlier ones, and humans can read and steer rejected hypotheses. For live data, thumbs up/down feedback and SME annotations are exported as traces (114 in the example), clustered into failure modes, checked by an adversarial review and root-cause analysis, triaged into fix, defer or discard, and then added to the golden set as regression tests. He credits this to harness engineering: specs per failure mode, quality gates, context engineering and observability.

## Key ideas
- **An agent is an LLM in an agentic loop with tools and retrieved context, so the fixes are usually prompts, tools and retrieval, not model changes** — The speaker lists missing tools, weak system prompts and context retrieval gaps as the usual causes of low eval scores. ([1:09](https://youtu.be/aHhB3sjGjkI?t=69))
- **A golden dataset is the test suite for a non-deterministic agent** — It holds inputs and expected outputs written with subject matter experts. The expected output can be a text answer, a number, a specific tool call, or a tool chain. Scorers run the whole set to give an accuracy baseline for detecting regressions. ([3:53](https://youtu.be/aHhB3sjGjkI?t=233))
- **Auto-research can be applied to agents, not just ML models** — Karpathy's auto-research loop tweaks ML code and hyperparameters. The speaker's auto agent runs evals, then edits the agent's code, system prompt and tools, reruns evals, and checks again, with no human in each step. ([8:07](https://youtu.be/aHhB3sjGjkI?t=487))
- **The optimizer must not be allowed to change the eval set** — Editing the golden dataset or scorers just to make evals pass is treated as cheating, so the instructions to the coding agent explicitly forbid it. ([12:23](https://youtu.be/aHhB3sjGjkI?t=743))
- **Each hypothesis gets a branch, and the loop keeps only real improvements** — Each iteration tests one failure class on a new branch, reruns evals, and writes a report. Improvements are kept and regressions are rolled back to the last good branch. A global memory file across runs lets later hypotheses build on earlier results. ([13:49](https://youtu.be/aHhB3sjGjkI?t=829))
- **Live feedback becomes regression tests through clustering and triage** — Thumbs feedback and SME annotations are exported as traces and clustered into failure modes, mostly from negative feedback. An adversarial review and root-cause analysis follow, then triage into fix now, fix later or discard, and every accepted failure mode is added to the golden set. ([20:31](https://youtu.be/aHhB3sjGjkI?t=1231))
- **Harness engineering is what makes the loops work** — Each failure mode becomes a spec, and quality gates (linting, unit tests, evals, LLM code review), context engineering and observability give the coding agent a feedback loop it can check its own changes against. ([26:04](https://youtu.be/aHhB3sjGjkI?t=1564))

## Techniques
- **Golden dataset plus scorers as the agent test suite** — Write input and expected-output pairs with SMEs. Expected output can be text, a value, or a required tool call or chain. Attach scorers, run the full set, and record the accuracy as the baseline. *When:* Before optimizing any agent, so every change can be checked for regressions against a fixed number.
- **Baseline report before the optimization loop** — Run the evals once and write a report with the cases, a pass/fail summary and what works or fails. Give it to the coding agent as its starting picture. *When:* At the start of any automated improvement job.
- **Branch-per-hypothesis improvement loop with rollback** — Each iteration: new branch, one hypothesis about one failure class, edit the agent, run evals, write a reports.md, update a global memory file. Keep the branch if the metric improves. Roll back to the last improving branch on regression or no gain. *When:* When an agent has a clear metric and the changes can be tested automatically.
- **Protected eval set in the optimizer instructions** — Put the objective, target repo, metrics and off-limits files (golden dataset and scorers) in a markdown job file that the coding agent reads at the start. *When:* Whenever a coding agent edits the system it is also being scored on.
- **Reading the agent's full traces, including thinking traces, for root cause** — Let the coding agent read the target agent's traces to find where the reasoning or tool use went wrong, then propose a change. *When:* When the eval score drops but the failure reason is unclear from the output alone.
- **Trace clustering from live feedback** — Export traces with thumbs feedback and SME annotations as JSON, cluster the negative ones into failure modes, run an adversarial review and root-cause analysis, and produce a markdown report with an executive summary. *When:* When real users or SMEs give feedback on production traces.
- **Packaging the analysis as a reusable skill** — Write the clustering, review and root-cause steps as a skill the coding agent loads, so each report run follows the same procedure. *When:* When the same analysis will run repeatedly, for example once per sprint.
- **Failure mode to spec to golden-set entry** — Turn each accepted failure mode into a spec of expected behavior, add it to the golden dataset and scorers, and fix it through the normal quality gates. *When:* After triage, so the same failure is caught if it comes back.

## Numbers
- Naive hello-world agent pass rate on the golden dataset with a string-contains evaluator (about 18% of questions answerable without tools) ([5:11](https://youtu.be/aHhB3sjGjkI?t=311))
- Auto-agent raised the naive agent from 18% to 83% in about 10 iterations ([9:33](https://youtu.be/aHhB3sjGjkI?t=573))
- Plus 10% on internal benchmarks for a production agent that had already been tuned by hand ([10:58](https://youtu.be/aHhB3sjGjkI?t=658))
- Example iteration results: first change regressed (rolled back), then +5%, then 0%, then +12% ([13:49](https://youtu.be/aHhB3sjGjkI?t=829))
- Production agent accuracy rose from 67% to 86% in about 10 iterations, found by the loop without cheating on evals ([18:08](https://youtu.be/aHhB3sjGjkI?t=1088))
- Trace export used for clustering in the example: 114 traces ([23:12](https://youtu.be/aHhB3sjGjkI?t=1392))
- Suggested cadence for the live-data report: about once per sprint, more often with much higher trace volume (for example 10,000 traces) ([26:04](https://youtu.be/aHhB3sjGjkI?t=1564))

## Hot takes
- Agents building agents: a coding agent with an eval loop can find fixes that human prompt engineers missed on an already-tuned production agent.
- The eval set and scorers must be off-limits to the optimizer; otherwise the loop just games its own metric.
- Every production failure mode should become a golden-set entry, so it is caught the next time it appears.

## Tools mentioned
Claude Code, Mastra, auto-agent (the speaker's own internal tool, not public)

## Relevance to our work
- **agentos** (2/3): MemoryMesh and the observability layer need an eval-driven improvement path; the branch-per-hypothesis loop with rollback and protected scorers is a concrete pattern for that. → *Pick one AgentOS agent path, write a small golden set with scorers, and prototype a branch-per-hypothesis loop that rolls back regressions and writes a reports.md per iteration.*
- **prosharness** (2/3): The harness already runs loops with checkpoints and quality gates; the rollback-on-regression loop, per-iteration reports and rule against editing the eval set fit that design. → *Add to ProsHarness loops a rule that the optimizer cannot edit eval or scorer files, a per-iteration report, and rollback to the last improving checkpoint.*
- **general** (2/3): Matches the autoresearch layered harness for entity resolution: a fixed gold set with scorers, plus the warning that the optimizer must not change gold labels or scoring. → *Check the ER testing harness to confirm the optimizer cannot change gold labels or scorers, and that each hypothesis writes its own report with a rollback path.*
