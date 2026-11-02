# The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ow1we5PzK-o` · [watch](https://youtu.be/ow1we5PzK-o) · **date:** 2026-05-18 · **length:** 18:31 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Luke Alvoeiro · **orgs:** Factory, Block, Agentic AI Foundation
- **topics:** multi-agent, agent-architecture, software-factory, testing-verification · **tags:** missions, orchestrator-worker-validator, validation-contract, handoffs, droid, long-running-agents, bitter-lesson, prompt-caching, serial-execution

> Luke Alvoeiro (Factory) on "Missions", a multi-agent system that runs for hours or days by combining delegation, creator/verifier, broadcast and negotiation, with a validation contract written before any code.

## Summary
Factory's Luke Alvoeiro argues the bottleneck in software engineering is human attention, not model intelligence. He sorts multi-agent patterns into five types (delegation, creator-verifier, direct communication, negotiation, broadcast) and says Factory's Missions system combines four of them. Missions uses three roles: an orchestrator that plans and writes a validation contract, workers that implement features with clean context, and validators that check behavior end-to-end. Work runs serially, with parallelism limited to read-only steps, and workers leave structured handoffs. He reports a 16-day longest run, 60% of time and tokens spent on implementation, and about 90% test coverage on a Slack-clone example. He says orchestration logic lives in prompts and skills (about 700 lines) rather than a state machine, so the system should improve with each model release.

## Key ideas
- **Human attention, not model intelligence, is now the bottleneck in software engineering.** — Models can handle a 50-task backlog, but humans can only supervise a few tasks a day. The aim is to let agents work for hours or days while the human sets goals and reviews results. ([1:09](https://youtu.be/ow1we5PzK-o?t=69))
- **Multi-agent systems fall into five patterns: delegation, creator-verifier, direct communication, negotiation, and broadcast.** — Delegation (parent spawns child) is the most common starting point. Creator-verifier separates building from checking because the builder has sunk-cost bias. Direct communication lacks a single source of truth. Negotiation works best for net-positive trades. Broadcast keeps long tasks coherent. ([0:38](https://youtu.be/ow1we5PzK-o?t=38))
- **Missions uses three roles: orchestrator, workers, and validators.** — The orchestrator plans with the user and writes features, milestones, and a validation contract. Workers implement one feature each with clean context and commit to git. Validators check the work and never saw the code being written. ([3:36](https://youtu.be/ow1we5PzK-o?t=216))
- **The validation contract is written before any code, so tests do not just confirm what the code already does.** — The speaker argues tests written after implementation are shaped by the code and only confirm decisions. A contract of assertions defines correctness independently, and each feature must cover one or more assertions. ([5:02](https://youtu.be/ow1we5PzK-o?t=302))
- **Validation has two layers: a scrutiny validator for code and a user-testing validator that drives the live app.** — Scrutiny runs tests, type checks, lint, and per-feature code review agents. User testing uses computer use to fill forms and click through flows. It takes most of the wall-clock time because it waits on real execution. ([6:28](https://youtu.be/ow1we5PzK-o?t=388))
- **Structured handoffs and serial execution beat parallel swarms for multi-day work.** — Parallel agents step on each other and make inconsistent architecture choices, so coordination costs eat the gains. Missions runs one writing agent at a time, parallelizes only read-only search and review, and has workers write handoffs with commands and exit codes. ([7:53](https://youtu.be/ow1we5PzK-o?t=473))
- **Put orchestration logic in prompts and skills, not a hard-coded state machine, so it improves with each model release.** — About 700 lines of text decide decomposition and failure handling, and a few sentences can change strategy. Deterministic code only handles bookkeeping, such as blocking progress on unresolved handoff issues. ([14:58](https://youtu.be/ow1we5PzK-o?t=898))

## Techniques
- **Validation contract written at planning time** — Before coding, the planner writes a set of assertions describing correctness. Each feature is mapped to one or more assertions, and the union must cover every assertion. Validators check against these, not against the implementation. *When:* Long agent runs where tests written after implementation would drift and confirm bugs instead of catching them.
- **Fresh-context adversarial validators** — Validators are separate agents that have never seen the implementation. One runs tests, type checks, lint, and per-feature code review. Another drives the running app through computer use and checks end-to-end flows. *When:* Any agent-built feature where code-level checks alone miss behavior bugs. Also suitable when the cost of a live-app check is acceptable.
- **Structured worker handoffs** — A worker ends by writing what it completed, what it left undone, which commands it ran with exit codes, what issues it found, and whether it followed the orchestrator's procedures. The next agent inherits this record and clean code. *When:* Multi-day runs where agents must not rely on memory, and where errors should be caught at milestone boundaries.
- **Serial features with read-only parallelism** — Only one writing agent (worker or validator) runs at a time. Code search, API research, and read-only review are parallelized inside a single step. *When:* Software tasks where concurrent writers conflict on the same code and architecture decisions. Accepts lower raw speed for a lower error rate.
- **Per-role model choice** — Use a slow, careful model for planning, a fast model for implementation, and a precise instruction-following model for validation. Validation may use a different provider so it is not biased by the same training data. *When:* Model-agnostic systems where the weakest model in a chain limits the whole run, or where open-weight models must be used with structured checks.
- **Milestone-based negotiation** — After each milestone the orchestrator reviews the handoff summaries and decides whether to accept, add follow-up features, or re-scope. *When:* Checkpoints in long tasks where corrective work must be scoped and the plan adjusted.
- **Orchestration as prompts and skills** — Keep decomposition and failure handling in short prompt text and per-mission skills. Keep code limited to bookkeeping such as validation runs and progress gates. *When:* Systems that must improve automatically with each model release and avoid a rigid state machine.

## Numbers
- Longest mission ran 16 days; the speaker believes 30 days is achievable. ([9:17](https://youtu.be/ow1we5PzK-o?t=557))
- On the Slack-clone example, 60% of time and 60% of tokens went to implementation. ([12:58](https://youtu.be/ow1we5PzK-o?t=778))
- About 50% of final lines of code are tests, with about 90% coverage. ([12:58](https://youtu.be/ow1we5PzK-o?t=778))
- Estimated capacity: a team of five could run 30 workstreams with Missions, up from 10 without. ([15:26](https://youtu.be/ow1we5PzK-o?t=926))
- Orchestration logic is about 700 lines of text. ([14:58](https://youtu.be/ow1we5PzK-o?t=898))
- Most wall-clock time in a mission is spent in the user-testing validator waiting on live app execution. ([6:28](https://youtu.be/ow1we5PzK-o?t=388))

## Hot takes
- Tests written after implementation do not catch bugs; they only confirm decisions made in the code.
- Parallel coding agents usually lose to serial execution once coordination cost and token burn are counted.
- Model-agnostic architecture is a structural advantage, because a system is only as strong as its weakest model in the chain.

## Tools mentioned
Factory Droid (open source Goose lineage mentioned), AGENTS.md, skills, computer use (for user-testing validator), prompt caching

## Relevance to our work
- **prosharness** (3/3): ProsHarness already checkpoints long Claude Code runs and plans with critique. Missions' validation contract, fresh-context validators, and structured handoffs map directly onto that design. → *Add a validation contract step at plan time, and require handoff records with command exit codes before a checkpoint can advance, then check that the runs stay drift-free.*
- **general** (2/3): Strong practitioner guidance on multi-agent taxonomy, serial vs parallel execution, and per-role model choice. → *Compare the five-pattern taxonomy and the serial-with-read-only-parallel rule against our current subagent setup, and check whether any review step is run by an agent that has not seen the implementation.*
- **agentos** (1/3): Multi-agent and long-running patterns relate to the distributed-system thesis, but the talk is about coding-agent teams, not infra. → *Read the talk's ideas on a validation contract and handoffs as a pattern for supervised long runs of agents on AgentOS work.*
