# Chat and citations won't save your vertical AI - Atul Ramachandran, Filed Inc

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `RGiXcVxSD3s` · [watch](https://youtu.be/RGiXcVxSD3s) · **date:** 2026-07-18 · **length:** 15:12 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Atul Ramachandran · **orgs:** Filed
- **topics:** product-ux, agent-architecture, observability, skills-self-improvement · **tags:** vertical-ai, delegation, long-running-agents, background-agents, skills-capture, trace, human-in-the-loop, plan-approval, weekly-active-sessions, tax

> Vertical AI talk by the Filed CTO arguing chat and citations are not enough; products should be built for delegating long-running work to agents, with skills, traces, pause-and-intervene and plan approval.

## Summary
The speaker, CTO of Filed (a US tax-software company), argues that chat and citations alone cannot keep the promise of saving customers time, because chat is synchronous and citations push verification work back onto the user. He frames product history as three bottlenecks: employees, then users, and now agentic delegation, where value depends on the work agents complete rather than on how often users log in. He describes a conveyor-belt model in which users are supervisors and agents are workers, so products should be designed for delegation rather than participation. The four components he names are finding delegable tasks (repeatable work that takes more than a couple of hours), teaching agents through automatically captured skills, monitoring through task lists and per-value traces, and giving users control through pauses and plan approval before irreversible actions. He ends by proposing that teams measure weekly active sessions instead of weekly active users. The talk is mostly a product thesis with a company pitch in it, and it gives few hard benchmarks.

## Key ideas
- **Chat and citations are not enough for vertical AI** — Chat is synchronous, so the user waits on the agent and cannot leave. Citations push verification work back onto the customer. Both reduce hallucinations but do not deliver the promise of agents working while the user sleeps. ([0:01](https://youtu.be/RGiXcVxSD3s?t=1))
- **The bottleneck has moved to delegation** — Value used to be limited by the number of employees, then by the number of users. With agentic delegation, value is limited by how much long-running work users hand off, and users do not need to be online while the agent works. ([3:53](https://youtu.be/RGiXcVxSD3s?t=233))
- **Design for delegation, not participation** — Treat the product as a conveyor belt. The agents are the workers, the user is the supervisor, and the product is the belt plus the infrastructure around it. Ask what the interface looks like when a user hands the task off instead of doing it. ([5:20](https://youtu.be/RGiXcVxSD3s?t=320))
- **Pick tasks that take hours and repeat across users** — The speaker says the tasks worth delegating take more than a couple of hours. He names three tax-workflow tasks that take over an hour each. These tasks should be repeatable, or repeatable with variation per customer, and they form the core long-running background agent. ([6:45](https://youtu.be/RGiXcVxSD3s?t=405))
- **The last 20% is each customer's own way of working** — A generic end-to-end agent gets roughly 80 to 90 percent of the way. The remainder is user conventions, such as a company's coding practices. The speaker says this gap is where the product value sits, so the agent must learn these quirks. ([8:12](https://youtu.be/RGiXcVxSD3s?t=492))
- **Capture skills from product usage automatically** — Instead of a separate skill-authoring interface, the product watches usage and decides when a repeated pattern should become a skill. Wispr Flow is cited as an example of a product that learns skills as the user works. ([9:11](https://youtu.be/RGiXcVxSD3s?t=551))
- **Trace every output value back to its source** — Because long-running agents run many parallel tasks, users need a task list with status and traces that link each value the agent produced back to how it was made. The speaker says this visibility is where trust is built. ([9:11](https://youtu.be/RGiXcVxSD3s?t=551))
- **Pause at the point of assumption and let the user step in** — When the agent hits a judgment call, the system pauses the belt. The user answers in a chat-style thread by tagging the agent, so control feels like taking the wheel, not abandoning the car. ([10:42](https://youtu.be/RGiXcVxSD3s?t=642))
- **Show a plan before irreversible actions and keep the manual UI** — Before the agent overwrites data in tax software, it shows a plan for the user to approve. Level-2 manual features stay in the product so users can always take back control. ([12:12](https://youtu.be/RGiXcVxSD3s?t=732))
- **Measure weekly active sessions, not weekly active users** — A session is a task finished by a human or an agent, including when the user is not in the product. The aim is for sessions to rise while weekly active users fall, though not to zero. ([13:39](https://youtu.be/RGiXcVxSD3s?t=819))

## Techniques
- **Delegation-first task selection** — Find user tasks that take more than a couple of hours, repeat across users, or repeat with variation. Build a long-running background agent for each one, and do not design the feature around the user doing the work in the UI. *When:* Scoping a new agent feature or deciding which workflow to automate first in a vertical product.
- **Implicit skill capture from usage** — Watch how users actually work in the product, detect recurring patterns or corrections, and turn them into skills automatically. No separate skill-authoring UI is needed. The speaker presents this as the way to close the last 20% gap. *When:* A generic agent produces mostly correct output but misses each customer's conventions.
- **Per-value trace-back for trust** — Record how each output value was produced and show it to users in a readable form, next to a task list that shows the status of each running task. *When:* Several long-running agent tasks run in parallel and users must verify outputs they did not watch being made.
- **Pause-and-tag intervention** — When the agent meets a judgment call or an ambiguous assumption, pause that task. Surface the question in a chat-like thread where the user tags the agent with an answer, then resume. *When:* Mid-run ambiguity where a wrong guess would waste hours of agent work.
- **Plan approval gate for irreversible actions** — Before any destructive or hard-to-undo write, such as overwriting existing data, generate an explicit plan and require user approval before execution. *When:* The agent writes to a system of record and mistakes cannot be easily reversed.

## Numbers
- Raised more than $17M; about two years building AI agents for tax professionals ([1:02](https://youtu.be/RGiXcVxSD3s?t=62))
- Last month's revenue exceeded everything earned in the prior full year ([1:02](https://youtu.be/RGiXcVxSD3s?t=62))
- Three tax-workflow tasks each take users more than an hour ([6:45](https://youtu.be/RGiXcVxSD3s?t=405))
- A generic end-to-end agent gets roughly 80 to 90 percent of the way; the rest is user-specific ([8:12](https://youtu.be/RGiXcVxSD3s?t=492))
- Proposed metric shift: weekly active users should fall while weekly active sessions rise. No target values given. ([13:39](https://youtu.be/RGiXcVxSD3s?t=819))

## Hot takes
- Chat and citations alone will not save vertical AI because chat is synchronous and citations shift verification work onto the customer.
- Weekly active users is the wrong success metric for delegation products; weekly active sessions is the better one.
- The most valuable part of a vertical agent is the last 20% of customer-specific behaviour, and it should be learned, not configured by hand.
- Agent products should keep the manual UI as a fallback so users can always take back control.

## Tools mentioned
Wispr Flow

## Relevance to our work
- **agentos** (2/3): The talk's automatic skill capture from product usage maps onto SkillForge's open question about the success signal and skill-worthiness scoring. The talk gives a concrete framing (repeated user corrections on top of an 80 to 90 percent generic output), though no method. → *Prototype a SkillForge step that flags repeated user corrections in agent telemetry as candidate skills, and test whether those flags predict which candidate skills are later reused.*
- **prosharness** (2/3): ProsHarness already has phone-driven approvals and checkpoint/resume. The talk's plan-before-irreversible-action gate and pause-and-tag intervention are concrete patterns for that same loop. → *Add a plan-approval gate in ProsHarness that pauses before any irreversible step (file overwrite or external write) and shows the plan for approval through the existing phone approval flow.*
- **general** (1/3): Useful as a product framing when judging agent features: count completed agent tasks per session, not user logins. → *When reviewing agent features, add a metric for completed agent tasks per session alongside active users.*
