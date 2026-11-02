# Agent Frameworks Considered Harmful — Rémi Louf, .txt

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `KHudyx5wW3U` · [watch](https://youtu.be/KHudyx5wW3U) · **date:** 2026-09-18 · **length:** 20:29 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Rémi Louf · **orgs:** .text, Anthropic, OpenAI
- **topics:** agent-architecture, observability, context-engineering · **tags:** event-driven agents, append-only event log, content-addressed prompts, replay and diff, markdown agent definitions, structured outputs, agent runtime, build vs buy, open-source models, solo-CEO prototyping

> Rémi Louf (CEO of .text) on building a small event-driven agent runtime in two weeks: typed events, an append-only log, and content-addressed prompts for auditable, replayable agents.

## Summary
Rémi Louf, CEO of the 15-person company .text, spent two weeks in January building personal and then company agents after agents got much better around December. He found that frameworks kept the prompts buried in code, so he used markdown agent definitions that can be versioned and reviewed in PRs, plus cron schedules and events. Each failure he hit (duplicate posts, a lost voice note, an unversioned prompt change) led him to build a runtime piece: an append-only event log with causal links. He then stored every prompt part as a content hash and built the prompt as a list of hashes, which makes it possible to trace exactly what the model saw, diff two runs, and replay a request on a different model. He treats agents as processes under a kernel, with markdown as userland, and enforces two typed boundaries (tool calls and events) because structured-output errors were a real problem for him. He reports about 20 agents in use at the company after a month, runs on open-source models, and advises building the infra before buying it.

## Key ideas
- **Agents do not need a graph. Each agent declares the events it accepts and the events it emits, so the system's topology comes from the log.** — Cron covers only a point in time. Event triggers (new voice note, new PR, new CRM entry) start agents, and the speaker says that is all the wiring needed. ([5:20](https://youtu.be/KHudyx5wW3U?t=320))
- **Early failures drove the design. Each one turned into a runtime component.** — Duplicate Slack posts led to a real queue and attempt counting. A vanished voice note led to a log that keeps everything. An unversioned prompt edit that ruined the market brief pushed him toward content addressing. He says none of it is new and calls it the usual distributed-systems checklist. ([7:55](https://youtu.be/KHudyx5wW3U?t=475))
- **The append-only log is the system's memory. Every event links to the event that caused it.** — Causal links make debugging multi-agent chains practical. The speaker says the Codex chat view is misleading, because compaction, quirks, and hidden thinking traces mean the model did not see what the UI shows. ([10:42](https://youtu.be/KHudyx5wW3U?t=642))
- **Build the prompt from hashed parts so the exact model input can be reconstructed.** — System prompt, each skill description, tool descriptions, and user messages are each stored under a hash. A prompt is a list of hashes, and each model response is stored the same way. Compaction and KV-cache handling become graph operations on that list. ([12:08](https://youtu.be/KHudyx5wW3U?t=728))
- **Diffing and replay come almost for free once prompts are content-addressed.** — Diffing two runs shows which components changed, for example only the user message, a skill, or a tool. Replaying a stored request on an open-source model lets the speaker compare outputs when costs rose. ([14:16](https://youtu.be/KHudyx5wW3U?t=856))
- **Think of agents as processes under a kernel. Markdown is userland, and the kernel makes bad actions impossible, not merely unlikely.** — The kernel schedules and isolates agents and journals them to the log. Two typed boundaries are enforced: tool calls must name real tools, and events must match their declared types. The speaker calls the event boundary non-negotiable. About 20% of his events were rejected by structured-output errors with the model he was using then. ([15:21](https://youtu.be/KHudyx5wW3U?t=921))
- **Build before you buy, and make your own team dogfood the framework.** — After a month, about 20 agents were deployed, including some written by non-engineers. The speaker says the infrastructure category is still unsettled, that open-source models are good enough for his uses, and that he no longer uses third-party APIs. ([17:50](https://youtu.be/KHudyx5wW3U?t=1070))

## Techniques
- **Markdown-defined agents in a versioned folder** — Each agent is a markdown file dropped in a folder. The runtime picks it up. Changes are diffed and reviewed in PRs, and the runtime is treated as the kernel while the file is userland. *When:* When non-engineers need to author agents, or when prompt edits must be reviewable and reversible.
- **Event-typed agent contracts** — Each agent declares the event types it accepts and the event types it returns. Output is forced through structured outputs, and a schema violation is rejected at the boundary rather than passed downstream. *When:* When many agents chain together and bad payloads would otherwise cascade silently.
- **Append-only event log with causal ids** — Every event is appended, never updated, and records the id of the event that triggered it. The log is queryable for debugging. *When:* When three or more agents interact and you need to trace which event caused which action.
- **Content-addressed prompt assembly** — Store each prompt component (system prompt, skill descriptions, tool descriptions, user messages, model responses) under its hash. Represent a request as a list of hashes and render text only when needed. *When:* When you must answer exactly what the model saw, diff two runs by component, or do compaction and cache work on structure instead of strings.
- **Replay a stored request against another model** — Rebuild the exact request from the stored hash list, send it to a different model or with a changed component, and compare outputs. *When:* When you want to cut cost by moving to an open-source model and need evidence that output quality holds.
- **Two-boundary enforcement** — Type-check tool calls against the registered tool set, and type-check every inter-agent event against its schema before it is accepted. *When:* When you want invalid actions to be impossible rather than merely unlikely.

## Numbers
- The company is 15 people. The speaker's experiment ran for two weeks in January. ([0:08](https://youtu.be/KHudyx5wW3U?t=8))
- The first version of the system took about one day to write with Codex. ([7:55](https://youtu.be/KHudyx5wW3U?t=475))
- With the structured-output setup used earlier, about 20% of the speaker's events were wrong and got rejected by the system. ([16:34](https://youtu.be/KHudyx5wW3U?t=994))
- After one month of company deployment there are about 20 agents, some written by non-technical staff. ([17:50](https://youtu.be/KHudyx5wW3U?t=1070))
- The speaker's stack no longer uses third-party APIs and runs open-source models, including locally on a laptop. ([17:50](https://youtu.be/KHudyx5wW3U?t=1070))

## Hot takes
- Agent frameworks are considered harmful. They hide the prompt inside code and leave agents inside their abstractions.
- You do not need a graph database for agent topology. An append-only event log plus typed events is enough.
- The Codex or chat transcript is a lie about what the model saw. Compaction and hidden thinking make it so.
- Markdown files for agents beat code for versioning and review, even if engineers hate YAML.
- Build the agent infrastructure before you buy it.

## Tools mentioned
Codex, Slack, Linear, llama.cpp

## Relevance to our work
- **agentos** (2/3): AgentOS already plans a Govrix audit log, an exec gate and SkillForge telemetry. The talk shows an event log with causal ids and content-addressed prompts as a concrete design for the same audit and replay needs, plus typed agent boundaries. → *Prototype a content-addressed prompt store for Govrix Scout requests: hash each prompt component, keep the request as a hash list, and add a run-diff command that shows which component changed between two runs.*
- **prosharness** (2/3): ProsHarness runs checkpoint and resume loops and schedules. The talk argues event triggers beat cron for reacting to state changes, and that an append-only causal log is the way to resume long runs. → *Consider adding event-typed triggers (for example a PR merged or a checkpoint written) alongside the existing cron loops, and record each checkpoint as a causal event so resumes can be traced.*
