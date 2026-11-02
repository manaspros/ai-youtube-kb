# Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `3_gYbhABcAE` · [watch](https://youtu.be/3_gYbhABcAE) · **date:** 2026-06-18 · **length:** 10:40 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Philipp Schmid · **orgs:** Google DeepMind, Google
- **topics:** agent-architecture, evals, mcp-and-tools, context-engineering · **tags:** agent-design, non-determinism, error-recovery, pass-rate-evals, tool-design, semantic-interfaces, human-in-the-loop, agent-reliability

> Philipp Schmid (Google DeepMind) lists five habits from deterministic software that break when building agents: text as state, handing control to the LLM, errors as inputs, pass-rate evals, and agent-ready tools.

## Summary
Schmid says building agents is an iterative loop of defining instructions, running, observing, and adjusting prompts and tools, unlike the spec-code-test-deploy path of traditional software. He frames the change as moving from a traffic controller who sets every step to a dispatcher who sets the goal and lets the agent pick the route. He argues that state is now text and context, so approvals can carry free-form edits and preferences cannot be reduced to profile flags. He says control must be handed to the model, since fixed intent-based workflows are hard to maintain. Failures should be fed back to the model as inputs and not trigger full restarts of long runs. Unit tests are replaced by evals that measure how often an agent succeeds, graded by LLM judges or human experts with tracing for debugging. Finally, tools must be self-documenting for agents, which see only schemas and docstrings, and the whole approach needs recovery design, balanced reliability thresholds, and a willingness to rebuild as models improve.

## Key ideas
- **Agent development is an iterative loop, not spec-code-test-deploy** — You define instructions, run the agent, observe what it does, adjust prompts or tools, and run again until it is reliable. ([0:00](https://youtu.be/3_gYbhABcAE?t=0))
- **Shift from traffic controller to dispatcher** — Traditional software controls each step. With agents you define the goal (e.g. get to London) and let the agent choose the steps, even if its route looks odd, as long as the outcome is right. ([1:28](https://youtu.be/3_gYbhABcAE?t=88))
- **Text and context are the new state** — Flags and booleans cannot capture semantic feedback. A user can approve a research plan and also add scope changes such as focusing on the US market and ignoring California. Preferences like Fahrenheit for cooking cannot be modeled as profile fields. ([1:28](https://youtu.be/3_gYbhABcAE?t=88))
- **Hand control to the LLM instead of fixed intent workflows** — A classify-then-branch churn flow is brittle. An agent that understands intent can respond dynamically, for example offering an alternative when a user asks to cancel, and the conversation can change intent midway. ([3:58](https://youtu.be/3_gYbhABcAE?t=238))
- **Treat errors as inputs** — Failures should go back to the model as observations, like user input, so the agent can work around them. Restarting a 5 to 15 minute agent run wastes compute and loses context. ([3:58](https://youtu.be/3_gYbhABcAE?t=238))
- **Replace unit tests with evals on success rate** — Agents are non-deterministic, so the same input may take different steps. A prompt that works one time in ten is not production-ready. Measure pass rate over repeated runs, grade outcomes with an LLM judge or human expert, and trace the steps for debugging. ([5:23](https://youtu.be/3_gYbhABcAE?t=323))
- **Design tools for agents, not for developers who already know the API** — An agent sees only function schemas, docstrings, and tool definitions, not the code or the team's context. Tools need semantic, self-documenting descriptions, including what failures mean. ([8:05](https://youtu.be/3_gYbhABcAE?t=485))
- **Design for recovery, build to delete** — Models and agents are imperfect, especially in longer runs, so recovery must be designed in and reliability thresholds balanced. Software is disposable, so expect to rebuild the same systems as models improve. ([9:35](https://youtu.be/3_gYbhABcAE?t=575))

## Techniques
- **Goal-first dispatcher prompting** — Specify the outcome and constraints, not the exact step sequence, and check results against the outcome rather than the path. *When:* Multi-step tasks where the best route varies per run or per user.
- **Free-text approval with edits** — Instead of accept or deny buttons, let the user reply in natural language to approve a plan with added scope or constraints, and feed that text back into the agent. *When:* Plan checkpoints such as deep research or long multi-step jobs.
- **Preferences as natural language in context** — Keep user preferences and memory as text the agent reads, rather than as fixed profile fields or flags. *When:* Personalization that varies by context, such as unit choices per task.
- **Errors as observations** — Pass tool or step failures back to the model as normal input so it can retry, work around them, or add checks, and keep the flow going. *When:* Long-running agent runs where restarting from scratch is expensive.
- **Repeated-run pass-rate evals with judges** — Run the same task many times, count how often it passes, and score subjective outputs with an LLM-as-judge or human graders. Keep traces for debugging but score the final outcome. *When:* Before shipping any non-deterministic agent, in place of unit and integration tests.
- **Agent-ready tool definitions** — Write tool names, docstrings, and schemas that explain purpose, parameters, and failure behavior, since the model sees nothing else. *When:* Exposing existing product APIs or microservices as agent tools.

## Numbers
- Long agent runs take roughly 5 to 15 minutes, so restarting after a failure repeats a lot of compute and can lose context ([5:23](https://youtu.be/3_gYbhABcAE?t=323))
- An agent that succeeds only one time in ten on the same prompt is too flaky to put in production ([6:44](https://youtu.be/3_gYbhABcAE?t=404))

## Hot takes
- Senior engineers struggle with agents because they apply deterministic habits such as specs, unit tests, and fixed workflows.
- Tools should be written for the model, which sees only schemas and docstrings, not the code or the years of API context.
- Software is disposable; expect to rebuild agent systems many times as models improve.

## Tools mentioned
Gemini API, Gemini

## Relevance to our work
- **prosharness** (2/3): ProsHarness already does checkpoint and resume of long runs. The talk's point that step errors should go back to the model as observations, rather than restarting, fits that design directly. → *When a step fails inside a ProsHarness long run, return the error to the Claude Code session as input and resume from the last checkpoint instead of restarting the run; measure the pass rate across repeated harness runs.*
- **agentos** (1/3): The eval and error-as-input points apply to AgentOS agent flows, but the talk gives no infrastructure or benchmarks for them. → *For any AgentOS agent flow, add a repeated-run pass-rate check (run N times, report the share that pass) alongside single-run tests.*
