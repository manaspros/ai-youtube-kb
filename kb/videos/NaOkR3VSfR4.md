# Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `NaOkR3VSfR4` · [watch](https://youtu.be/NaOkR3VSfR4) · **date:** 2026-10-09 · **length:** 16:50 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Viren Baraiya · **orgs:** Orkes, Conductor (open source)
- **topics:** agent-architecture, security-guardrails, multi-agent · **tags:** harness, durable-execution, saga, brains-vs-hands, human-in-the-loop, idempotency, workflow-engine, sre-agent, conductor, background-agents, event-driven-agents

> Viren Baraiya on running production agents: the LLM only plans, a deterministic harness executes side effects, durable state and human gates make it safe, shown with a Conductor SRE remediation demo.

## Summary
Viren Baraiya argues that production agents should be treated as applications built from harnesses, not as a single loop with tools. He splits responsibilities into "brains" (the LLM, which only plans the next steps) and "hands" (a deterministic harness that executes them, including approvals and side effects). He frames harnesses as late-bound sagas: the tool set is fixed and deterministic, but the agent composes the sequence at runtime. Because harnesses can run for seconds or months, durability is presented as the baseline requirement rather than a feature. The demo is an SRE remediation agent that emits a multi-step plan, compiles it into a Conductor workflow, runs it, and replans in a second loop that skips a rollback already completed in the first. The talk is short and mostly conceptual, with a brief closing pitch for the open-source Conductor project.

## Key ideas
- **Agents in production are applications, not chatbots** — Background, scheduled, event-driven, long-running coordinator and multi-agent setups are the real shapes. Each harness should have one goal and single responsibility, like microservices, and several can be composed. ([1:08](https://youtu.be/NaOkR3VSfR4?t=68))
- **A harness mixes non-deterministic and deterministic parts** — The LLM supplies reasoning. Anything that must happen the same way every time (payments, cluster restarts) should be fixed code in the harness, so LLM nondeterminism does not leak into it. ([5:00](https://youtu.be/NaOkR3VSfR4?t=300))
- **Durability is the cost of admission** — Harnesses may run seconds to months, waiting on humans, third parties or events. They must recover from crashes, network partitions and host failures, so durability is assumed rather than sold as a feature. ([6:28](https://youtu.be/NaOkR3VSfR4?t=388))
- **Brains plan, hands execute** — The agent only proposes what should happen next. The harness decides how to do it (for example, how to restart a cluster) using deterministic code. The speaker calls this the single most important takeaway. ([7:34](https://youtu.be/NaOkR3VSfR4?t=454))
- **Approvals and idempotency belong in the harness** — A prod restart should pass through a human gate (for example, a Slack approval) enforced by code, not left to the LLM's judgment. Steps should be idempotent, or their non-idempotency should be recorded so side effects can be handled separately. ([9:03](https://youtu.be/NaOkR3VSfR4?t=543))
- **Harnesses are late-bound sagas** — Classic sagas fix the steps ahead of time. An agent harness has a finite, deterministic set of tools and composes the sequence at runtime, which gives the visibility and control of a workflow while allowing many branch combinations no one could enumerate in advance. ([10:28](https://youtu.be/NaOkR3VSfR4?t=628))
- **Plan, compile, execute, then replan from state** — In the demo the LLM emits several steps at once, a plan-and-compile tool turns them into a runnable Conductor workflow, and the engine runs it. The loop then reads the recorded state and plans again. In the second iteration the agent skipped a rollback already done in the first. ([14:00](https://youtu.be/NaOkR3VSfR4?t=840))

## Techniques
- **Brains/hands split** — The LLM returns only a plan (ordered steps). Deterministic harness code performs every side effect, such as restarts, emails and deploys, and the LLM never calls those directly. *When:* Any agent that changes production systems or external state, where repeatable and auditable execution matters.
- **Plan-compile-execute** — Have the agent emit a multi-step plan, compile it into a fixed workflow graph (the talk uses Conductor), then run that graph on a durable engine. *When:* Multi-step remediation or ops tasks that need visibility, retries and a record of what ran.
- **Code-enforced human approval gate** — Pause the workflow at a defined step, notify a human (for example, via Slack), and continue only on approval, implemented as workflow logic rather than a prompt instruction. *When:* High-impact or irreversible actions such as restarting a production cluster.
- **Idempotent steps or recorded side effects** — Make each tool step idempotent where possible. If not, log that it is non-idempotent and what it did, so retries and cleanup can be handled separately. *When:* Long-running harnesses that may retry or resume after failure.
- **State-driven replanning loop** — Each iteration reads recorded side effects and current system state, then asks the LLM what remains. Completed actions are visible to the planner so it does not repeat them. *When:* Iterative remediation or any loop that spans several cycles over the same system.
- **Single-responsibility harnesses** — Build one harness per business goal, for example an SRE harness that combines logs, Kubernetes, metrics and support dashboards, and avoid one agent owning many responsibilities. *When:* When an agent's scope grows and hallucination risk rises with the number of responsibilities.

## Numbers
- Talk length is 16:50 and the speaker said 15 to 20 minutes was planned. No benchmarks or cost figures are given. ([0:12](https://youtu.be/NaOkR3VSfR4?t=12))
- Audience poll: many hands went up for running agents in production. The speaker said a conference a couple of weeks earlier had about one hand. ([0:12](https://youtu.be/NaOkR3VSfR4?t=12))
- Harness lifetimes range from a few seconds to days, months or longer. ([5:00](https://youtu.be/NaOkR3VSfR4?t=300))
- Demo SRE remediation loop ran for two iterations, and the second skipped a rollback already done in the first. ([15:06](https://youtu.be/NaOkR3VSfR4?t=906))

## Hot takes
- Durability is the cost of admission for a harness, not a feature to sell.
- The LLM should only plan; the harness, not the model, should decide how a restart is done.
- Agent harnesses are late-bound sagas.
- Human approval for production actions should be enforced by code, not left to an LLM's judgment.

## Tools mentioned
Conductor, Kubernetes, Slack, LangChain agents, OpenAI Agents SDK, Google ADK, MCP, APIs

## Relevance to our work
- **prosharness** (2/3): ProsHarness already has checkpoint/resume, loops and phone approvals around Claude Code. The brains/hands split and code-enforced approval gates give a concrete way to check which steps are deterministic side effects. → *Audit ProsHarness so that side-effecting steps (push, deploy, restart, send) run through a fixed executor with an approval gate, and record each step's idempotency in the checkpoint.*
- **agentos** (1/3): Crucible's exec-gate and the budget/guardrail layer overlap with the idea of deterministic execution around the agent. The talk gives no benchmarks or implementation details. → *Consider whether the exec-gate should treat tool calls with side effects as steps that a deterministic executor must run, with idempotency keys recorded.*
