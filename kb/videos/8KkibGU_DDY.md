# Mousepower: agents that can’t be measured, can’t be managed. — Maximillian Piras, Yutori

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `8KkibGU_DDY` · [watch](https://youtu.be/8KkibGU_DDY) · **date:** 2026-09-18 · **length:** 20:38 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Maximillian Piras · **orgs:** Yutori, Ramp, Coinbase, Anthropic
- **topics:** governance-compliance, evals, token-cost-efficiency, product-ux · **tags:** roi-measurement, token-cost, verification, verifier-agent, task-triage, code-review-bottleneck, computer-use, background-agents, outcome-attribution

> Maximillian Piras (Yutori) argues agents have a measurement problem: token spend must trace to verifiable outcomes, and tasks should be triaged by step and acceptance-criteria uncertainty before building an agent.

## Summary
Piras, a founding designer at Yutori (a computer-use model company), describes how he runs background agents in parallel and how the resulting token bills raise the question of whether the spend was worth it. He argues that customers cannot judge agent value because nobody has a clear ROI measure, and that token counts are only an input, so they need to be tied to outcomes such as closed bugs or resolved support requests. He draws an analogy to James Watt inventing horsepower to make steam engines understandable to horse-mill owners, and suggests a similar "mouse power" idea, though he says it is a thought starter rather than a real metric. He points out that code review is now the bottleneck, so verification does not scale with generation, and that code review's shared assumptions need rethinking for agents. His main framework is a two-axis matrix: uncertainty in task steps and uncertainty in acceptance criteria. Low step uncertainty means write a script, high acceptance uncertainty means verification costs as much as execution, and the sweet spot is tasks that are verifiable enough to be checked cheaply, which he says is where you should also build a verifier agent.

## Key ideas
- **Agents have a measurement problem, not only a capability problem** — Token spend is hard to justify because nobody has a clean value measure. Teams burn a year's token budget in a quarter, or they run token leaderboards, and the spend is not tied to results. ([3:47](https://youtu.be/8KkibGU_DDY?t=227))
- **Tokens are an input signal; trace them to outcomes** — Tokens are useful for internal monitoring but are only an output. Spend should be linked to outcomes such as bugs fixed or support tickets closed, and then to the objectives those outcomes serve. ([10:24](https://youtu.be/8KkibGU_DDY?t=624))
- **Code review is the bottleneck, so verification must scale with generation** — Coding agents produce many pull requests, but human review does not speed up at the same rate. Without a way to judge quality at that speed, the ROI of generated code cannot be shown. ([11:46](https://youtu.be/8KkibGU_DDY?t=706))
- **Historical analogy: a communicable metric beats an accurate one** — Watt's horsepower was not scientifically precise, but it let horse-mill owners calibrate the efficiency gain of a steam engine enough to try one. The metric's job was to get people past the first step of adoption. ([7:33](https://youtu.be/8KkibGU_DDY?t=453))
- **Triage tasks on two uncertainty axes before building an agent** — One axis is uncertainty in the steps. Predictable steps mean just write a script. The other axis is uncertainty in the acceptance criteria. If acceptance is unclear, verifying the output costs as much as doing the task, so an agent is wasted spend. The middle is the sweet spot. ([17:54](https://youtu.be/8KkibGU_DDY?t=1074))
- **Tasks that are easier to verify than to execute suit a verifier agent** — When the verification of a task follows a repeatable pattern, build a second agent that checks the first agent's output. The speaker frames this as an NP-style problem, where checking is cheaper than solving. ([19:14](https://youtu.be/8KkibGU_DDY?t=1154))

## Techniques
- **Two-axis task triage** — Score each candidate task on uncertainty in its steps and uncertainty in its acceptance criteria. Script the low-step-uncertainty tasks, skip the high-acceptance-uncertainty tasks, and direct agents at the middle band where verification is cheap. *When:* Before deciding what to hand to an agent or what to parallelize, and when a token budget needs to be justified.
- **Verifier agent alongside worker agent** — For tasks with a repeatable verification pattern, run a second agent whose only job is to check the first agent's work against a fixed rubric. *When:* When human review is the bottleneck and the acceptance criteria can be written down as a clear rubric.
- **Background parallel agents for peripheral work** — Keep one main task in focus and run several agents in the background on side explorations, such as design directions for slides, with shared design-system guidance set up beforehand. *When:* When there is a lot of exploratory work that is not on the critical path, and a deadline makes wall-clock time matter.
- **Outcome-tied token accounting** — Attach token spend to completed units of work (bugs squashed, tickets closed) rather than reporting tokens alone. The speaker cites Coinbase changing model defaults so that frontier models are used only for the hardest tasks, and Ramp's write-up on token maxing. *When:* When reporting agent spend to leadership or customers, or when deciding model routing defaults.

## Numbers
- Speaker has been the founding designer at Yutori for about a year and a half ([2:28](https://youtu.be/8KkibGU_DDY?t=148))
- Talk runs 20:38 in total ([0:00](https://youtu.be/8KkibGU_DDY?t=0))

## Hot takes
- Agents have a measurement problem, and that matters more than the capability gap.
- If you sell an agent, you also owe the customer a rubric for checking its output.
- For some tasks, building the verifier agent is the real product, not the worker agent.
- Teams are in a doom loop of overspending and then underusing, because they lack a value measure.

## Tools mentioned
Claude

## Relevance to our work
- **agentos** (1/3): Govrix budgets and the Merkle audit log could record spend per task, but the talk argues for outcome attribution, which the current design does not do. → *Add an optional task or outcome id to Govrix budget and audit records so token spend can later be joined to a completed task or merged PR.*
- **prosharness** (1/3): ProsHarness runs plan, critique and debate, but it does not check run output against an acceptance rubric before a checkpoint is marked done. The verifier-agent idea fits there. → *Read the talk's two-axis triage again and decide whether ProsHarness steps with a clear rubric should get a separate verifier pass before checkpoint.*
- **general** (1/3): The triage matrix is a cheap check to run before fanning out parallel agents, which the speaker does by habit. → *Before launching a parallel agent batch, label each task by step uncertainty and acceptance-criteria uncertainty, and script the low-uncertainty ones.*
