# Every Harness Will Become A Claw — Sam Bhagwat, Mastra

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `8qWIPUia2O8` · [watch](https://youtu.be/8qWIPUia2O8) · **date:** 2026-08-18 · **length:** 15:36 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Sam Bhagwat · **orgs:** Mastra
- **topics:** agent-architecture, sandboxing-execution, skills-self-improvement, product-ux · **tags:** harness, claw, always-on agents, durability, heartbeat, continual learning, shakeout, TypeScript, Mastra, OpenClaw, Hermes Agent, Claude Code, Codex

> Sam Bhagwat (Mastra) argues agent harnesses will keep expanding into always-on "claws" with durability, initiative and learning, then shake out to a few winners. Mostly conceptual, with little hard data.

## Summary
Sam Bhagwat, co-founder and CEO of Mastra (a TypeScript agent framework), frames 2026 as the "harness era." He sorts harnesses into local ones (daily coding tools), cloud ones (hosted or internal agents reachable from Slack), and open-source frameworks. He walks through what separates an agent from a plain LLM call, then lists the qualities that appear when an agent becomes a harness: durability (running for hours or days), always-on operation, initiative, and learning from traces. He calls the trajectory "Steinberger's Law": every harness will keep expanding until it becomes a claw, because users keep asking for more features. He predicts a shakeout like the phone app ecosystem, where each category ends up with only one or two logos people actually keep, based on how economically valuable or how frequently used a product is. His practical advice is to ship the capabilities users need and to re-check the landscape often, since change is fast. The talk is short on implementation detail and includes some vendor positioning for Mastra.

## Key ideas
- **Harnesses come in three kinds: local (daily coding tools), cloud (products or internal agents, often in Slack), and open-source frameworks that supply the primitives.** — The speaker places Mastra in the third group. He says the industry moved from talking about the agent loop and agents vs workflows last year to a harness era. ([1:04](https://youtu.be/8qWIPUia2O8?t=64))
- **Durability is the first quality that separates a harness from an agent. It means running for hours or days, not minutes.** — Examples given: resuming after a dropped connection by persisting the stream, planning mode, parallel subagents, dynamically created agents, background bash tasks, auto-compaction when the context window fills, persisted threads you can resume, and queue, steer and interrupt controls during a turn. He also mentions session-long tool approval. ([3:17](https://youtu.be/8qWIPUia2O8?t=197))
- **The next step is an always-on harness. You reach it from Slack or a phone, it runs in cloud sandboxes, and it ends in a PR.** — Cloud sandboxes allow more parallel subagents than a laptop can run. He calls this a distributed-systems trade-off that needs a different architecture. ([4:20](https://youtu.be/8qWIPUia2O8?t=260))
- **Turning a harness into a claw means adding initiative and learning. Initiative comes from a heartbeat that wakes the agent on a timer and from external feeds. Learning means changing behavior based on traces.** — Persistent memory should live somewhere more accessible than flat files. A gateway handles incoming requests from chat channels. Automatic skill generation from traces is one example of continual learning, but he says the right method is still unsettled. ([6:47](https://youtu.be/8qWIPUia2O8?t=407))
- **Steinberger's Law: every harness expands until it becomes a claw.** — He gives three reasons: the expansion is driven by user demand, the same demand is visible in OpenClaw and Hermes Agent, and users want these features with control, not just a claw on a box. He says this expansion is partly technical, economic and psychological. ([9:04](https://youtu.be/8qWIPUia2O8?t=544))
- **A shakeout is coming, and users have room for only a few claws.** — His analogy is the 2010s phone ecosystem, where each category kept one or two apps. A product survives the shakeout if it is either very valuable or used very often. He expects the shakeout later in the 2020s. ([10:20](https://youtu.be/8qWIPUia2O8?t=620))

## Techniques
- **Durable turn streaming with resume** — Persist the streamed output of a turn so that a lost connection can resume from where it stopped, instead of restarting the whole run. *When:* Long-running agent turns over unreliable connections, such as mobile or remote clients.
- **Queue, steer and interrupt on running threads** — Let the user send new messages into an in-progress thread, redirect it, or stop it. Do not block the user until the LLM call finishes. *When:* Agents that run for minutes or longer and need human direction while they work.
- **Session-scoped tool approval** — Approve a tool or command pattern once for the whole session, not one call at a time. The speaker warns that this can approve dangerous commands too, so the scope has to be chosen with care. *When:* Reducing approval prompts in long autonomous sessions, with the risk understood.
- **Heartbeat wake-ups** — Wake the agent on a fixed interval so it can check external feeds, such as email, and decide whether anything needs action. *When:* Proactive assistants that should act without a user message.
- **Trace-driven continual learning** — Derive improvements from the agent's own run traces, such as auto-generated skills or code changes. The speaker presents this as an open area with no settled method. *When:* Exploring self-improving agents. Treat the outputs as experimental.
- **Cloud sandbox per parallel subagent** — Run each subagent in its own cloud sandbox so more tasks can run in parallel than a local machine allows. Deliver results as PRs. *When:* Fan-out work that exceeds local resources and must end in a reviewable change.

## Numbers
- Teams have seen agents running in production for about the last 18 months. ([0:08](https://youtu.be/8qWIPUia2O8?t=8))
- The always-on, cloud-harness shift has been visible for roughly the last three months. ([4:20](https://youtu.be/8qWIPUia2O8?t=260))
- Compared with 18 to 24 months ago, the speaker says a simple LLM call now sits much higher on the agentic spectrum. ([9:04](https://youtu.be/8qWIPUia2O8?t=544))
- Speaker's estimate: if the rate of change rises 3 to 4x, people need to track developments more often. ([14:02](https://youtu.be/8qWIPUia2O8?t=842))
- In phone app categories, usually only one or two logos survive regular use. The speaker uses this to predict the claw shakeout. ([11:21](https://youtu.be/8qWIPUia2O8?t=681))

## Hot takes
- Every harness will expand until it becomes a claw (Steinberger's Law).
- Most agent products will shake out, and users will keep only a few claws because attention is limited.
- Continual learning from traces is the next frontier, and the right method is not yet known.
- Another shakeout is likely in the later 2020s.

## Tools mentioned
Mastra, Claude Code, Codex, OpenClaw, Hermes Agent, Slack, Telegram, WhatsApp, GitHub

## Relevance to our work
- **agentos** (2/3): SkillForge's open question is how to turn agent telemetry into governed skills. The talk names trace-driven skill generation as a live approach, but says no method has settled. → *Compare automatic skill generation from run traces (6:47 to 8:04) with SkillForge's open questions on the success signal and skill-worthiness scoring.*
- **prosharness** (2/3): Checkpoint and resume, loops and schedules, and phone-driven approvals already exist in ProsHarness. The talk adds stream persistence for resume after a dropped connection, heartbeat wake-ups, and queue and steer during a turn. → *Test whether a checkpointed run can resume after a dropped client connection by persisting its streamed output, then consider a heartbeat-style scheduled wake-up that checks external feeds.*
- **general** (1/3): The talk gives a useful vocabulary for always-on harness features, but offers no concrete implementation details. → *Watch whether always-on harness features such as heartbeat, resume and session approvals settle into shared patterns before building custom versions.*
