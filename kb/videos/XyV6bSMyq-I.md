# How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `XyV6bSMyq-I` · [watch](https://youtu.be/XyV6bSMyq-I) · **date:** 2026-09-27 · **length:** 17:06 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Zubin Aysola · **orgs:** Weights & Biases, CoreWeave
- **topics:** evals, skills-self-improvement, observability, agent-architecture · **tags:** self-improving-agent, eval-flywheel, prod-offline-parity, trace-to-task, llm-as-judge, persona-simulation, weave, yaml-config-variants

> Weights & Biases walks through how its ARIA agent evaluates and improves itself: production traces become offline regression tasks, and the agent runs its own hill-climbing loop.

## Summary
Zubin Aysola of Weights & Biases describes building and evaluating the ARIA agent, which was released to general availability the week before. His core claim is that agents, benchmarks and configurations are covariant, so evaluation has to measure both production and offline behaviour. The team runs the same agent code in production and in an offline research environment, with a sync job to prevent drift. Every production miss or success becomes an eval task, and tasks are defined as YAML start and end states that are simulated by text instructions or persona-driven user LLMs. Scoring uses both pass/fail and relative comparison between variants. A live demo shows ARIA turning a production trace into a regression task, finding a missing weave.log call, and proposing a prompt fix. The talk is useful for its eval-flywheel pattern, though it is partly a product walkthrough for Weave and the speaker's own platform.

## Key ideas
- **Agents, benchmarks and configs are covariant, so measurement has to cover both production and offline environments.** — Changing the agent or its config changes what the benchmark measures. The speaker argues that eval design must account for this and check performance in both places. ([0:50](https://youtu.be/XyV6bSMyq-I?t=50))
- **Production traces and offline sim traces are logged in the same format, which closes a data flywheel.** — Production traces are pulled into the offline environment as tasks, the agent is hill-climbed on them, and fixes ship back to production. ([2:07](https://youtu.be/XyV6bSMyq-I?t=127))
- **Research and production run identical agent code, kept in sync to avoid drift.** — The agent runs byte-identical in both places. A roughly four-hour sync job copies production to the research environment so researchers do not drift when they cut new variants. ([5:45](https://youtu.be/XyV6bSMyq-I?t=345))
- **Every production miss (and success) becomes a task for the agent framework.** — The speaker treats each production trace as a candidate eval task. This is the core of the flywheel. He also says running more experiments beats running fewer. ([6:39](https://youtu.be/XyV6bSMyq-I?t=399))
- **The eval pipeline is a DAG: config, hydrate live data, set up environment, rehydrate runtime values, run agent, score.** — Some runtime settings cannot be encoded in YAML, so they are patched back into the config at runtime. Scoring is where most of the robustness work happens. ([8:02](https://youtu.be/XyV6bSMyq-I?t=482))
- **Score agents two ways: normative pass/fail per task, and relative comparison between variants.** — For example, one variant asks clarifying questions and one does not, and the team compares them on the same tasks. ([9:19](https://youtu.be/XyV6bSMyq-I?t=559))
- **Tasks are YAML start and end states, simulated by text instructions or by a persona-driven user LLM for multi-turn flows.** — The team has 886 tasks, categorised by level, and product teams review whether the tasks reflect what they care about. ([10:34](https://youtu.be/XyV6bSMyq-I?t=634))
- **The agent can turn a production trace into a regression task, run it, and propose a fix itself.** — In the demo, ARIA finds that weave.log was not called correctly in the sandbox, adds a hill-climb target, and compares production with the candidate variant. ([13:01](https://youtu.be/XyV6bSMyq-I?t=781))
- **The winning candidate was a small prompt injected into the system prompt or a skill to fix one specific SDK error.** — The speaker presents this as the pattern to copy: a production failure replicated in simulation, then fixed through a targeted instruction change. ([16:12](https://youtu.be/XyV6bSMyq-I?t=972))

## Techniques
- **Eval flywheel from production traces** — Log production traces in the same format as offline runs. Pull a failing or good production trace into the offline eval set as a task, run candidate and production agents on it, and score both. *When:* When you have a live agent and want offline evals to reflect real user failures rather than synthetic cases.
- **Byte-identical prod and research agent with a sync job** — Keep one agent code path for production and offline. Sync production state to the research environment on a schedule, so variant comparisons are not confounded by code or data drift. *When:* When offline numbers stop predicting production behaviour, or when several researchers cut variants in parallel.
- **YAML-defined config variants** — Describe each agent configuration (compaction, context prep, UI payload assembly, model) as YAML. Generate many mutations and run them in parallel. *When:* When you want to test many prompt, context or model variants cheaply and compare them on the same task set.
- **Three task simulation modes** — Use a single text instruction for simple tasks. Use a persona-prompted LLM to play a user who asks questions in a set order for multi-turn tasks. Define each task as a YAML start condition and end condition. *When:* When you need repeatable multi-turn evals without real users, and want product teams to review task quality.
- **Dual scoring: pass/fail plus pairwise relative scoring** — Score each run as pass or fail against the task end condition. Also compare variants head to head on the same tasks, for example questions asked versus not asked. *When:* When absolute pass rates hide which design change actually helps.
- **Unconstrained sandbox for agent research loops** — Give the agent its own sandbox so it can launch parallel runs of its own research loop, with teammates' runs kept separate through teardown. *When:* When you want the agent to run its own experiments rather than only executing a fixed script.

## Numbers
- 886 simulated tasks, categorised by level and reviewed by product teams. ([10:34](https://youtu.be/XyV6bSMyq-I?t=634))
- About 66% performance on some tasks, from seven weeks of nightly CI traces. ([4:22](https://youtu.be/XyV6bSMyq-I?t=262))
- Production-to-research sync job runs roughly every four hours. ([5:45](https://youtu.be/XyV6bSMyq-I?t=345))
- The speaker says he has not written a line of code in about eight months, because he has Claude write it. ([14:50](https://youtu.be/XyV6bSMyq-I?t=890))

## Hot takes
- Running more experiments beats running fewer.
- Agents, benchmarks and configs are covariant, so offline evals alone cannot be trusted.
- Auto mode is attractive, but humans still need to think about what improvements to make.

## Tools mentioned
Weights & Biases Weave, W&B Reports, ARIA agent, Claude Code, YAML task and config specs

## Relevance to our work
- **agentos** (2/3): The prod-trace-to-regression-task loop and the pass/fail plus pairwise scoring address the open SkillForge question of a success signal for skill-worthiness. → *Prototype a SkillForge scorer that takes a production trace, replays it as a task, and records both pass/fail and a pairwise comparison between the current and candidate skill.*
- **general** (2/3): The eval flywheel and the byte-identical prod and offline agent pattern apply to any agent team. → *Write a short design note on how production failures would enter an offline eval set, and who reviews the tasks.*
- **prosharness** (1/3): Defining runs as YAML variants with start and end conditions could structure ProsHarness plan and checkpoint tests. → *Read the W&B task and config YAML structure and consider it as a format for ProsHarness regression scenarios.*
