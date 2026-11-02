# Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `iOXM3zE-2dk` · [watch](https://youtu.be/iOXM3zE-2dk) · **date:** 2026-05-18 · **length:** 1:20:07 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Amy Boyd, Nitya Narasimhan · **orgs:** Microsoft
- **topics:** observability, evals, security-guardrails, coding-agents · **tags:** microsoft-foundry, opentelemetry, trace-linked-evals, red-teaming, workflow-agents, prompt-optimization, azure-monitor, agent-versioning, human-in-the-loop

> Microsoft Foundry workshop on agent observability: trace-linked evals, stage-wise agent evaluators, OTel tracing, red teaming, and an observe skill that automates the eval-optimize loop with a human stopping regressions.

## Summary
Amy Boyd and Nitya Narasimhan (Microsoft) walk through a compressed version of a Microsoft Foundry workshop on agent observability, using a fictional "Contoso" travel agent with flight, hotel and car specialists. The core argument is that agents are non-deterministic, so quality has to be measured as rates over many runs, and monitored continuously because models, prompts, and environments drift after launch. They show a portal-first path (create project, agent, App Insights tracing, built-in evaluators) and then the SDK path (agent in code, tools, workflow agents in YAML, OTel tracing to console or Azure Monitor, quality/safety/agentic evals). The main idea is trace-linked evaluation: when an eval fails, you jump to the exact trace to shorten the time from detection to diagnosis. They also cover red teaming, where an attacker agent probes risk categories with attack strategies, and close with an "observe" skill driven from a coding agent. That skill generated an eval dataset, ran batch evals, and ran a prompt optimizer, but the optimizer's scores oscillated, so the human had to stop it and pick the best version (v5). The talk is mostly a product walkthrough, but the eval-per-stage method, version-based rollback, and the oscillation warning are practical.

## Key ideas
- **Agents are non-deterministic, so evaluation has to report percentages over many runs, and monitoring must continue after launch as requirements, users and environment change.** — The speakers frame the gap between platform requirements and what the agent actually does as the thing to close, through evals, guardrails, and continuous monitoring. ([5:28](https://youtu.be/iOXM3zE-2dk?t=328))
- **Evaluate each stage of the agent workflow, not only the final answer.** — Stages are intent resolution (did it understand the request), tool-call correctness (was the expected tool called), and task adherence/completion at the whole-agent level. Custom evaluators can be added when built-ins do not fit. ([9:16](https://youtu.be/iOXM3zE-2dk?t=556))
- **Trace-linked evaluations shorten the time from detecting a problem to diagnosing it.** — If eval results are linked to the trace that produced them, a failed metric leads straight to the spans that caused it. After a model swap, you can compare the trace of the new version with the old one to see, for example, a tool that stopped being called. ([33:39](https://youtu.be/iOXM3zE-2dk?t=2019))
- **Workflow agents split one monolithic agent into specialist agents (flight, hotel, car) with an orchestrator defined in YAML.** — Per-agent traces then show which specialist is underperforming and what each one costs in tokens, so only the weak part needs optimizing. ([45:27](https://youtu.be/iOXM3zE-2dk?t=2727))
- **Deployed agent versions act as rollback points, and an endpoint is enough for tracing and evaluation.** — Deploying an older version by name restores it. The speakers argue tracing and evals do not care how the agent was built, as long as it exposes an endpoint that emits OTel traces. ([49:40](https://youtu.be/iOXM3zE-2dk?t=2980))
- **Red teaming uses one AI agent to attack another, with risk categories and attack strategies.** — Simple encoding tricks such as leetspeak can slip past guardrails. Multi-turn escalation (Crescendo) is slower but finds more vulnerabilities. For agents, a prohibited-actions taxonomy defines actions the agent must never take, and attacks try to get around it. ([58:58](https://youtu.be/iOXM3zE-2dk?t=3538))
- **An automated optimize loop needs a human to stop it, because prompt optimizers oscillate.** — The observe skill generated the eval dataset, ran batch evals, and rewrote the prompt across about 10 versions. Scores went up and down (for example 7 to 5 to 8), so the human picked the best version (v5) and stopped the loop. ([1:08:45](https://youtu.be/iOXM3zE-2dk?t=4125))

## Techniques
- **Trace-linked evaluation** — Attach evaluator results to the trace or span that produced them, so a failing metric opens the exact trace for diagnosis. *When:* After any model, prompt, or tool change, when you need to know why a metric dropped.
- **Stage-wise agent evaluators** — Score intent resolution, tool-call correctness, and task adherence separately, each as a percentage over many runs; write custom evaluators where built-ins do not fit. *When:* When a single end-to-end pass/fail score hides which part of the agent broke.
- **Bootstrapped eval dataset from instructions** — Have a coding agent read the agent's instructions and generate test prompts, then run a batch eval to get a baseline. *When:* When the agent is new and there is no existing eval data.
- **Version-compare regression diff** — Give each agent change a version number, rerun the same evaluators on each version, compare traces across versions, and deploy the best-scoring version by name. *When:* When a change may have regressed another metric and you need a safe rollback.
- **Bounded auto-optimization with human stop** — Let a prompt optimizer iterate, track the score of every version, and have a person choose the best version when scores start oscillating. *When:* When automated prompt tuning is useful but can regress as well as improve.
- **Adversarial red teaming with an attacker agent** — Pick risk categories, attack strategies (encodings, multi-turn escalation like Crescendo), and for agents a prohibited-actions taxonomy; run the scan and read the report of failing cases. *When:* Before exposing an agent to users, and as a complement to normal safety evaluators.
- **OTel GenAI tracing with custom attributes** — Set the environment flags that enable GenAI tracing and message-content capture, add custom attributes to spans, and export to the local console during development and to Azure Monitor in production. *When:* When you need to debug agent runs locally and in a shared backend with the same telemetry.
- **Eval gate on model swap** — Switch to a cheaper model, then run the eval suite immediately to check whether cost fell without an accuracy regression. *When:* When cost or latency pressure tempts a model downgrade.

## Numbers
- Hugging Face hosts over 2 million models. ([15:32](https://youtu.be/iOXM3zE-2dk?t=932))
- The Azure model catalog has over 11,000 models. ([15:32](https://youtu.be/iOXM3zE-2dk?t=932))
- The speaker reports about $10 of Azure cost for two days of running the workshop repo. ([18:27](https://youtu.be/iOXM3zE-2dk?t=1107))
- The optimize loop ran through about 10 agent versions; the best was version 5, and the first optimization fixed one of the failing evaluator cases. ([1:08:45](https://youtu.be/iOXM3zE-2dk?t=4125))
- The talk is a compressed version of a workshop the speaker describes as almost four hours long. ([14:36](https://youtu.be/iOXM3zE-2dk?t=876))
- The talk runs 1:20:07 in length. ([0:00](https://youtu.be/iOXM3zE-2dk?t=0))

## Hot takes
- Evaluating the agent workflow end-to-end is more useful than evaluating the LLM alone.
- Automated prompt optimizers oscillate, so a human should choose the best version and stop the loop.
- Guardrails tested only on normal input miss simple encoding attacks; adversarial red teaming should be routine.
- Start in the portal to learn the built-in evaluators before writing code.

## Tools mentioned
Microsoft Foundry, Azure Monitor, Application Insights, OpenTelemetry, GitHub Codespaces, dev containers, GitHub Copilot Chat, Foundry MCP server, Azure AI Toolkit (VS Code extension), LangGraph, KQL, PyRIT (auto-caption reads it as 'pirate'), Jupyter notebooks, Bing web search tool

## Relevance to our work
- **agentos** (2/3): AgentOS L4 covers observability and L2D/EvolveCraft covers self-improving loops; the talk's trace-linked evals and version rollback map directly onto both. → *Emit OTel spans that carry the agent version and eval score for each run, so a regression can be diffed trace-to-trace, and add a rollback-to-best-version rule to the self-improving loop.*
- **prosharness** (2/3): ProsHarness runs loops and checkpoint/resume; an optimizer that oscillates needs the same best-checkpoint stop rule the talk shows. → *Track a score per checkpoint in ProsHarness loops, stop after N non-improving iterations, and resume from the best checkpoint rather than the latest.*
