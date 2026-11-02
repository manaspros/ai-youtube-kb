# Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `X1kp-ABIIxQ` · [watch](https://youtu.be/X1kp-ABIIxQ) · **date:** 2026-08-18 · **length:** 19:20 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Dan Farrelly · **orgs:** Inngest
- **topics:** agent-architecture, sandboxing-execution, observability, evals · **tags:** durable-execution, execution-layer, architecture-layers, resumability, background-agents, loops, sandboxes, session-tracing, outcome-scoring, inngest

> Dan Farrelly (Inngest CTO) argues agent architectures decay fast unless the execution layer (durable state, retries, triggers, tracing) is separated from fast-changing context (prompts, models, tools) and compute (sandboxes).

## Summary
Dan Farrelly, CTO of Inngest, argues that agent architectures have a half-life of about six months because teams couple fast-changing parts (prompts, models, frameworks) with slow-changing ones. He proposes three layers: execution (the brain: flow, state, durability, retries), context (models, prompts, tools, memory, which changes most), and compute (the hands: sandboxes, runtimes, browsers). His main claim is that the execution layer is the stable one to invest in, and it should hold durable external state so a failed step can resume without restarting the run. He lists the invocation patterns it must support (crons, events, APIs, human-in-the-loop, sub-agents, sync/async/delayed) and full-session tracing that includes non-LLM failures. He treats sandboxes as ephemeral and says using them for durability is an anti-pattern. He walks through a self-improving loop (cron health check, triage agent, weekly reviewer) and suggests scoring agents with outcome events such as "PR opened" instead of thumbs up/down. The talk is conceptual, with a short product pitch for Inngest at the end.

## Key ideas
- **Split agent systems into three layers: execution, context, and compute** — Execution is the brain (flow, state, durability, retries). Context covers models, prompts, tools and memory, and changes most. Compute is the hands (sandboxes, runtimes, browsers). Keeping them separate lets one layer change without rewriting the others. ([2:21](https://youtu.be/X1kp-ABIIxQ?t=141))
- **Architecture half-life comes from coupling layers** — Prompts last weeks, models months, execution years if built well. When layers are coupled, fast-changing parts drag the stable parts down, and this becomes technical debt under another name. ([3:50](https://youtu.be/X1kp-ABIIxQ?t=230))
- **Durable state must live outside the running work** — A three-hour run cannot keep state in memory or on disk. If step 38 of a run fails, the system should retry from that step rather than restart and lose tokens, cost and time. ([6:22](https://youtu.be/X1kp-ABIIxQ?t=382))
- **The execution layer must support many invocation patterns natively** — Crons, events, APIs, human-in-the-loop, sub-agents, and sync, async or delayed calls. Without these primitives, harness code absorbs queues, workers, polling, backoff and scheduling. ([7:48](https://youtu.be/X1kp-ABIIxQ?t=468))
- **Trace the whole session, not just LLM and tool calls** — Traces should run from the trigger through the full stack, including database errors, permission issues and performance. Without that, debugging and improving the agent is hard. ([8:48](https://youtu.be/X1kp-ABIIxQ?t=528))
- **Sandboxes are ephemeral, so do not use them for durability** — A sandbox is stateless by design. Durability, sequence and context should come from the execution layer, which hands the sandbox what it needs. ([9:50](https://youtu.be/X1kp-ABIIxQ?t=590))
- **Background agents and loops need execution awareness** — Background agents may run for minutes or hours with hundreds of tool calls, and at least one failure is likely. A loop is a system that runs on a schedule, assesses state against goals, and decides what to do next. The example is a 30-minute health-check cron that feeds a triage agent, plus a weekly reviewer that checks whether the triage system is over- or under-reacting. ([11:21](https://youtu.be/X1kp-ABIIxQ?t=681))
- **Use the execution layer as the hub for scoring** — User actions and session results all pass through the execution layer, so it is a natural place to attach scores. Scoring can run after the fact on the full trace, with inputs and outputs. ([15:36](https://youtu.be/X1kp-ABIIxQ?t=936))
- **Outcome events beat thumbs up/down** — Attach real-world events to a session, such as a triage that led to an engineer action, a PR that was opened, or a research report that was saved. These become outcome-based scores. ([17:05](https://youtu.be/X1kp-ABIIxQ?t=1025))

## Techniques
- **Three-layer decomposition (execution / context / compute)** — Treat orchestration and durability as their own layer. Keep prompts, models and tools in a context layer, and sandboxes or browsers in a compute layer, with clean interfaces between them. *When:* When agent code is changing every few months and you need to swap models, frameworks or sandboxes without rewriting orchestration.
- **Externalised durable step state with resume-from-failure** — Persist each step's state outside the agent process. On failure, retry or continue from the failed step instead of restarting the whole run. *When:* For long-running agent tasks (hours, hundreds of tool calls) where restarts waste tokens, cost and time.
- **Cron-triggered health check, triage agent, and reviewer loop** — A scheduled job pulls system metrics and asks an LLM whether things are healthy. If not, it spawns a triage agent that gathers context and investigates. A periodic reviewer reads the history of triage runs and proposes prompt, metric or data changes. *When:* For autonomous monitoring or improvement loops that must be observable and inspectable after the fact.
- **Deferred outcome scoring from downstream events** — After a run, attach downstream events (PR opened, report saved, action taken by a team) to the session trace and score the run from those outcomes. *When:* When you need a success signal for agent runs that is more reliable than user thumbs up/down.
- **Ephemeral sandboxes with state kept in the orchestrator** — Create the sandbox per task and keep sequence, state and durability in the execution layer. Pass only what the sandbox needs. *When:* When sandboxes are used for code execution or browsing and must be disposable.

## Numbers
- Architecture half-life of about six months; prompts last weeks, models months, execution years when built well (speaker's estimate, not measured) ([3:50](https://youtu.be/X1kp-ABIIxQ?t=230))
- Background agent runs can take minutes or hours with around 200 tool calls, and the speaker says at least one failure is nearly guaranteed ([11:21](https://youtu.be/X1kp-ABIIxQ?t=681))
- Example health-check cron runs every 30 minutes; the reviewer loop runs weekly ([12:44](https://youtu.be/X1kp-ABIIxQ?t=764))

## Hot takes
- Most teams couple everything together, so one layer's half-life drags the others down.
- Sandboxes are ephemeral and stateless by design, so using them for durability is an anti-pattern.
- Frameworks from three months ago were not designed for background and loop agents, so you need to design the execution layer yourself.
- Thumbs up/down is weaker than outcome events such as a PR being opened.

## Tools mentioned
Inngest

## Relevance to our work
- **prosharness** (3/3): ProsHarness does checkpoint/resume of long Claude Code runs and loops or schedules. The talk's core requirement is that durable state live outside the running work, with resume from the failed step. This directly tests whether ProsHarness's checkpoint design meets that bar. → *Audit ProsHarness checkpoint/resume: confirm state lives outside the Claude CLI process and sandbox, that resume starts from the failed step rather than the run start, and that scheduled loops are visible in one inspectable trace.*
- **agentos** (2/3): AgentOS's open SkillForge question is what success signal to use. The talk's outcome-event scoring (PR opened, report saved) is a concrete candidate. Its execution-layer framing also maps onto the L1 proxy and L2 pillars, though the talk does not address proxies. → *Prototype SkillForge success scoring by attaching downstream outcome events (for example, a PR merged or a saved artifact) to each agent session trace, and check whether they separate good runs from bad ones.*
