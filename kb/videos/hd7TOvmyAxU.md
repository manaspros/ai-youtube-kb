# An AI Research Agent That Runs Your Experiments — Tim Sweeney, Weights & Biases

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `hd7TOvmyAxU` · [watch](https://youtu.be/hd7TOvmyAxU) · **date:** 2026-09-27 · **length:** 21:16 · **format:** demo · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Tim Sweeney · **orgs:** Weights & Biases, CoreWeave
- **topics:** evals, observability, agent-architecture, training-finetuning-rl · **tags:** autoresearch, llm-as-judge, agent-tracing, nightly-evals, long-running-jobs, weave, launch, behavioral-bugs, eval-gated-promotion

> Live demo of W&B's ARIA research agent running autoresearch experiments, plus its trace-to-eval loop: production traces, LLM judges, nightly YAML task suites, and promotion gated on eval scores.

## Summary
Tim Sweeney (Weights & Biases / CoreWeave) demos ARIA, an agent inside the W&B UI that runs autoresearch-style training experiments. It edits code and hyperparameters, submits GPU jobs to a W&B Launch queue on a Kubernetes cluster, and polls until they finish. The talk then shows the architecture behind ARIA: a client, API server, turn database and worker harness, plus a sandbox, an LLM provider, a long-running compute path and an observability layer. Production traces go into Weave, where LLM judges flag behavior such as user frustration, and the team turns those traces into YAML tasks. Each task mixes LLM judges with rule-based checks, about 200 tasks run as a nightly eval suite, and the candidate is promoted only if its scores beat the production model. The closing advice is to log behavioral signals, treat evals as CI, keep humans reviewing traces, and add domain context before adding harness complexity. Much of the talk is product promotion, but the eval and tracing loop is concrete.

## Key ideas
- **Long-running compute is pushed out of the agent loop** — The agent turn does not hold the GPU job. It submits work to a launch queue on a compute cluster, then polls for results. This lets training run for days while the agent keeps working. ([4:30](https://youtu.be/hd7TOvmyAxU?t=270))
- **Reference architecture for a production agent** — Client, API server, turn database and worker harness, with the worker connected to a sandbox for arbitrary shell and Python, an LLM provider, a launch path for long jobs, and an observability layer that logs sessions, turns, tool calls and errors. ([10:49](https://youtu.be/hd7TOvmyAxU?t=649))
- **Behavioral bugs are a separate class from exceptions** — The speaker says agents need observability to catch bugs that do not raise errors and do not show up as performance problems, such as a bad answer or a wrong approach. Logging sessions, turns, tool calls and user feedback is how these get found. ([18:48](https://youtu.be/hd7TOvmyAxU?t=1128))
- **Production traces become YAML unit tests** — Each task is a YAML file with a prompt and a few judges. One judge checks correctness, another checks whether the insight is interesting, and a rule-based judge checks whether the result came within six tool calls. About 200 tasks are clustered into a nightly eval suite. ([16:07](https://youtu.be/hd7TOvmyAxU?t=967))
- **Live LLM judges on production traffic find clusters of failure** — Judges such as user frustration, low-quality response and ask-user run against live traffic and store their reasoning. The team uses the flags to pick clusters of behavior to fix in the next iteration. ([14:48](https://youtu.be/hd7TOvmyAxU?t=888))
- **Promotion is a go/no-go decision on eval scores** — The nightly eval results for a candidate model are compared with the production model on one dashboard. The example is 73% for the candidate against 72% for prod, which the team takes as the basis for the Friday push. ([17:22](https://youtu.be/hd7TOvmyAxU?t=1042))
- **Humans stay in the loop and add value through context before harness complexity** — The speaker says LLMs miss behavioral nuance, so the team reviews the best and worst traces by hand each week. He also says most low-hanging gains come from giving the agent business context, primitives and data, not from memory or harness tricks. ([18:48](https://youtu.be/hd7TOvmyAxU?t=1128))

## Techniques
- **Eval suite as YAML unit tests** — Write each task as a YAML file with a prompt and a mix of LLM judges (correctness, insight quality) and rule-based checks (for example, a tool-call budget). Cluster the tasks into a suite and run it nightly, tracking results in an observability tool. *When:* When you want regression tests for agent behavior that cannot be fully checked by exact-match assertions, and want them to grow from real production failures.
- **Production traces to tasks loop** — Log 100% of production sessions, turns and tool calls. Review them as humans and with LLM help, pull out behavioral patterns, turn each pattern into a task, implement a candidate, and rerun the suite. *When:* When an agent is live and you need to find and fix behavior problems that users hit but tests miss.
- **Live LLM judges as signal detectors** — Run judges such as user frustration, low-quality response and ask-user against live traffic. Keep the judge's reasoning next to each flag so reviewers can see why it fired. *When:* When you have too many traces to review by hand and need clusters of likely problems to inspect.
- **Eval-gated promotion** — Score the candidate and the production model on the same nightly suite, put both on one dashboard, and promote the candidate only when it clearly beats prod. Store model versions in a registry. *When:* When model or prompt changes need a shared go/no-go decision across the team.
- **Async job dispatch from an agent** — The agent submits long-running work to a launch queue on a cluster, then polls for status. Results come back as data the agent reads on the next turn. *When:* When a task, such as GPU training, runs much longer than an agent turn.
- **Agent analyzes its own traces** — Add a summarize action in the UI that starts a new chat seeded with the current trace or conversation, so the agent can explain and critique its own runs. *When:* When reviewers need quick analysis of individual traces and want to triage faster.

## Numbers
- Project had over 200 training jobs (experiments) run through the autoresearch loop ([2:07](https://youtu.be/hd7TOvmyAxU?t=127))
- Nightly eval suite of about 200 YAML tasks ([16:07](https://youtu.be/hd7TOvmyAxU?t=967))
- Rule-based task check: result must come within six tool calls ([16:07](https://youtu.be/hd7TOvmyAxU?t=967))
- Candidate scored 73% on the eval suite vs 72% for the production model (two nights before the talk) ([17:22](https://youtu.be/hd7TOvmyAxU?t=1042))
- One live experiment batch ran 12 experiments; loss 5.833 vs previous 5.831, just short of a new best ([20:00](https://youtu.be/hd7TOvmyAxU?t=1200))
- Weave logs 100% of agent traces ([10:49](https://youtu.be/hd7TOvmyAxU?t=649))

## Hot takes
- Tasks and evals are the new CI, and researchers should sit on the same scrum team as engineers.
- Behavioral bugs (not exceptions or performance problems) are the new class agent teams must catch, and LLM judges alone will miss some of them.
- Most low-hanging fruit comes from giving the agent domain context and primitives, not from over-engineering memory or the harness.
- The tool is not meant to replace RL researchers; it takes over the mechanics so researchers can focus on ideas.

## Tools mentioned
Weights & Biases Weave, W&B Launch, W&B Inference, W&B Artifacts, W&B Reports, CoreWeave sandbox, Kubernetes, iOS app

## Relevance to our work
- **agentos** (2/3): AgentOS has L4 observability and RAGAS evals. The talk's pattern of live LLM judges on traffic plus nightly YAML task suites with rule-based checks maps onto that layer. → *Prototype a nightly YAML task suite for AgentOS that mixes an LLM judge with a rule-based check (such as a tool-call budget), and gate promotion on the candidate-vs-baseline score.*
- **prosharness** (2/3): ProsHarness does checkpoint and resume for long runs. This talk shows a different approach: the agent submits long jobs to a queue and polls for them, which keeps the agent loop short. → *Compare ProsHarness checkpoint/resume with a submit-and-poll pattern for long training or batch jobs, and decide which fits loops that run for days.*
- **general** (1/3): The eval-as-CI pattern and the rule that behavioral bugs need human trace review apply to any agent team. → *Read the W&B Weave docs on judges and tasks to compare with our eval setup; the talk gives no benchmark figures beyond the 73% vs 72% comparison.*
