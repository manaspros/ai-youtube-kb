# Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `CvRngaQZQ3Y` · [watch](https://youtu.be/CvRngaQZQ3Y) · **date:** 2026-08-18 · **length:** 20:02 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Vivek Trivedy · **orgs:** LangChain, Harvey
- **topics:** observability, evals, training-finetuning-rl, memory · **tags:** trace-mining, continual-learning, harness-engineering, distillation, open-models, dense-feedback, auto-research, LangSmith, Deep Agents, Terminal Bench

> LangChain's Vivek Trivedy argues agent improvement is a data-mining loop: ship, collect traces, mine them, then run data-driven experiments on prompts, tools and models.

## Summary
Vivek Trivedy (LangChain applied research) frames improving agents as a data-mining problem. The recipe is to ship the agent, collect traces of its tool calls and outputs, mine those traces for failures and successes, then test each change (prompt, tool, orchestration, loop) against the traces. He ties observability to continual learning, since agents learn from environment feedback only if their traces are kept. He argues that prompt changes are hard for humans to reason about, so trace reading has to be automated, with agents reading other agents' traces. Scale is the main problem: reading millions of tokens per trace is expensive and long traces do not fit in context, so traces should be queried as an external store. The talk then covers a model-downgrade path (start on a frontier model, then harness-engineer and fine-tune cheaper open models on the traced task), plus generating evals and summaries for human reviewers. The closing advice is to alternate harness engineering with fine-tuning and to make feedback denser than pass/fail. The talk is partly a pitch for LangSmith Engine and LangChain's open-model service.

## Key ideas
- **Improving agents is a loop: ship, collect traces, mine them, then run data-driven experiments on prompts, tools, orchestration and loops.** — Agents generate tool calls, outputs and API/CLI activity on every run. Store all of it, mine it, and only accept a change if it improves results on the traced behaviour. ([0:08](https://youtu.be/CvRngaQZQ3Y?t=8))
- **Observability and continual learning are tightly coupled.** — Continual learning means an agent uses feedback from its environment to update its own knowledge. Without traces there is no feedback to learn from. ([2:21](https://youtu.be/CvRngaQZQ3Y?t=141))
- **Humans cannot reason about agent behaviour from the code alone, so trace reading must be automated.** — Agent behaviour comes from prompts, tools, skills, hooks and middleware, and it varies by domain. The speaker's team uses agents to read other agents' traces to find good and bad interactions and to answer questions such as whether quality drops after compaction. ([3:31](https://youtu.be/CvRngaQZQ3Y?t=211))
- **Reading traces at scale is an input-token cost problem and a context-size problem.** — Cost is roughly traces times average trace size. Very long coding-agent traces do not fit in one context, so the trace should be treated as an external object that is queried, not pasted in. ([6:42](https://youtu.be/CvRngaQZQ3Y?t=402))
- **Use a frontier model first to prove feasibility, then move down to a cheaper open model using traces.** — Work out the minimum intelligence the task needs. Then harness-engineer an open model, guided by how the frontier model reasons in its traces, until it matches the frontier judge at a much lower cost. ([8:01](https://youtu.be/CvRngaQZQ3Y?t=481))
- **When prompt tuning saturates, fine-tune on a narrow vertical task; at high volume, hardware can beat token pricing.** — Vertical fine-tuning of base models can reach and exceed frontier performance on the narrow task a customer cares about. At high inference volume a dedicated cluster can be cheaper than per-token costs. ([9:23](https://youtu.be/CvRngaQZQ3Y?t=563))
- **Use dense feedback signals and alternate harness work with fine-tuning.** — A pass/fail output gives little guidance. Richer per-step signals from traces let agents propose and test fixes. The suggested order is harness engineering (about two minutes per feedback cycle), then fine-tuning to break its ceiling, then harness engineering again. ([15:20](https://youtu.be/CvRngaQZQ3Y?t=920))

## Techniques
- **Agent-driven trace mining** — Put all agent traces in one tracing project and have an agent search them for good and bad interactions, failure patterns and behaviour over long sessions, rather than reading them by hand. *When:* You have many traces, or single traces too long to read or fit in context.
- **Frontier-to-open-model downgrade via trace judging** — Run the task on a frontier model. Use its traces as the reference judge, then harness-engineer a cheaper open model to match that judging, cutting cost by one to two orders of magnitude. *When:* A task is proven feasible and you want to cut the cost of a repeated judge or agent step.
- **Distillation from good traces** — Select the good runs from a strong model, build a dataset from them, and supervised fine-tune a small model (around 9B to 13B) to imitate that behaviour. *When:* A stronger model performs well on a task with stable, repeated behaviour and you want to lower cost.
- **Evals generated from traces** — Turn observed behaviour and failure modes from traces into eval sets, then update the agent until those evals pass. *When:* You need test coverage for behaviour you only found in production.
- **Score-driven auto-research loop** — Given a metric that can be pushed up, let an agent run experiments, read the results and traces, and make an update. Check it for cheating. *When:* You have a numeric score or eval to climb and enough compute for many iterations.
- **Harness, then fine-tune, then harness sandwich** — Iterate on prompts and harness first for fast feedback. Once that saturates, fine-tune. Then return to harness work on the tuned model. *When:* Harness changes stop improving results and you need to break through the ceiling.
- **Human review summaries** — Have agents condense the traces into digests that humans can review, since humans cannot read every trace. *When:* High-trust domains such as legal or medical, where a person must check agent output.

## Numbers
- Open models can match Opus-level trace judging at roughly one to two orders of magnitude lower cost (Harvey legal benchmark work). ([8:01](https://youtu.be/CvRngaQZQ3Y?t=481))
- Agents now run for millions of tokens per task, so reading traces is costly. ([4:43](https://youtu.be/CvRngaQZQ3Y?t=283))
- Harness engineering gives feedback in about two minutes per cycle. ([16:31](https://youtu.be/CvRngaQZQ3Y?t=991))

## Hot takes
- Showing someone an agent's eval suite tells you how the agent will behave, because agents are tuned until the evals pass.
- If you have traces you can do continual learning; the speaker calls observability and continual learning tightly coupled.
- Agent memory cannot be an append-only log; it needs updating over time, like sleep-time compute and dreaming.
- Pass/fail benchmarks like Terminal Bench give too little signal to improve an agent.

## Tools mentioned
LangSmith, LangSmith Engine, Deep Agents, Claude Code, Codex, Terminal Bench, scikit-learn

## Relevance to our work
- **agentos** (2/3): SkillForge's open question is the success signal for mining telemetry into skills. This talk's trace-mining loop and dense-feedback argument speak directly to it. → *Prototype a SkillForge success signal built from per-step trace feedback (not just pass/fail) and test whether it ranks skill-worthy runs better on a set of recorded AgentOS traces.*
- **general** (2/3): The frontier-to-open-model downgrade, validated against traces, is a direct recipe for the cheap Haiku pipelines the user cares about. → *For one existing Haiku judge or classifier step, run a frontier-model reference on a trace sample, then test whether a cheaper model matches it before switching.*
- **prosharness** (1/3): Harness engineering from traces and the harness-then-fine-tune loop map onto ProsHarness's checkpoint and run-review work. → *Read the talk's harness-iteration loop and check whether ProsHarness run traces can be mined for where Claude Code runs lose context after compaction.*
