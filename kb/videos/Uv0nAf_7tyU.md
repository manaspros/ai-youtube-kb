# Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Uv0nAf_7tyU` · [watch](https://youtu.be/Uv0nAf_7tyU) · **date:** 2026-10-12 · **length:** 17:40 · **format:** workshop · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Priyanka, Gabe Semach · **orgs:** Anthropic
- **topics:** agent-architecture, sandboxing-execution, context-engineering, mcp-and-tools · **tags:** claude-managed-agents, harness, sandbox, session-log, event-stream, credential-proxy, custom-tools, workshop, part-1-of-4

> Anthropic engineers explain how they split Claude Managed Agents into a session log, a harness "brain" and swappable sandbox "hands", then start a hands-on workshop building a first agent.

## Summary
Two Anthropic engineers, Priyanka and Gabe Semach, present part 1 of a four-part Claude Managed Agents workshop. They define an agent as a model in a loop with tools, and a harness as the wrapper that fills gaps the model cannot cover. Their first architecture ran the session, harness and sandbox inside one container, which turned each container into a hard-to-debug "pet". They then decoupled it into three parts: an append-only session log, a stateless brain (harness plus Claude), and hands (sandboxes, MCP calls) provisioned on demand. The change made failures recoverable by replay, kept credentials out of the sandbox via an injecting proxy, let compaction strategies vary without losing data, and cut time to first token by about 90%. The second half of the talk is a console-based walkthrough: create an environment, an agent with a model and system prompt, and a session, then exchange user.message and custom tool events. Memory and multi-agent features are deferred to later parts, and the transcript ends before the workshop's coding portion.

## Key ideas
- **An agent is a model running in a loop with tools, and the harness is the layer that runs that loop, manages context and covers what the model cannot do.** — The speaker's example is Sonnet 4.5's context anxiety, which needed a context reset in the harness. Opus 4.5 did not need it. So harness assumptions go stale with each model and must be revisited. ([2:47](https://youtu.be/Uv0nAf_7tyU?t=167))
- **Sandboxes should be isolated per task because model-written code is untrusted.** — The sandbox runs the code the agent writes, which may be buggy. Running each task in its own container limits the blast radius. ([4:04](https://youtu.be/Uv0nAf_7tyU?t=244))
- **Putting session, harness and sandbox in one container made each container a pet, which was hard to debug and investigate.** — A dead container looked like a dropped packet. Customer data lived in the containers, so engineers could not get in to investigate. Reaching an MCP server inside a customer VPC meant peering networks or shipping the harness. ([5:13](https://youtu.be/Uv0nAf_7tyU?t=313))
- **Decouple the brain from the hands. The session is an append-only event log, the harness is a stateless brain, and sandboxes and tools are hands that can be replaced.** — Each part is cattle. If a sandbox dies, the error returns to Claude as an ordinary tool failure, and Claude can respawn it. If the harness dies, a new one resumes by reading the session log. Only the log must be protected. ([7:53](https://youtu.be/Uv0nAf_7tyU?t=473))
- **Credentials never enter the sandbox. Calls that need a token go through a proxy that injects it before the external endpoint or MCP server is reached.** — The model never sees the token, so prompt injection cannot ask it to print or write the token out. ([7:53](https://youtu.be/Uv0nAf_7tyU?t=473))
- **Because nothing is discarded from the event log, the compaction strategy can change freely. It can summarize the full log or keep only the last N events.** — The stored history stays the same while the view put into context changes. ([9:13](https://youtu.be/Uv0nAf_7tyU?t=553))
- **Start inference immediately and provision the sandbox only when a tool needs it.** — This cut time to first token by about 90% compared with waiting for the container to start. ([10:19](https://youtu.be/Uv0nAf_7tyU?t=619))
- **Design interfaces to outlast the model assumptions built into them, so the harness can be replaced without changing the architecture.** — The speaker's takeaway is that harnesses encode assumptions and those assumptions go stale. The interfaces are the durable part. ([11:21](https://youtu.be/Uv0nAf_7tyU?t=681))
- **The workshop's agent is built from three API objects: an environment (networking and packages), an agent (name, model, system prompt, toolset), and a session (agent ID plus environment ID, the unit of work).** — A session stays idle until a user.message event is sent. The agent then emits events such as custom tool use, which the client handles and answers with a custom tool result. session.error, status idle and interrupt are also events. ([14:13](https://youtu.be/Uv0nAf_7tyU?t=853))

## Techniques
- **Brain / hands / session split** — Keep an append-only event log as the only durable state. Run the harness as a stateless loop that reads the log to resume. Provision sandboxes and tool connections on demand and treat them as replaceable. *When:* Long-running agents where any component can crash mid-task and work must resume from the last event without restarting.
- **Credential-injecting egress proxy** — Route any sandbox call that needs auth through a proxy that adds the token before the request leaves. The sandbox and model never hold the secret. *When:* Agents that call authenticated APIs or MCP servers and run untrusted, model-written code that could be prompt-injected.
- **Append-only event log with pluggable context strategy** — Store every event unchanged. Build the model's context from the log with a separate strategy, such as a full summary or the last N events. *When:* When you want to change context management or compaction later without losing or rewriting history.
- **Lazy sandbox provisioning** — Start the first model call straight away and create the container only when the model issues a tool call that needs it. *When:* When time to first token matters and many turns do not touch the sandbox.
- **One container per task** — Give each task its own sandbox and do not share containers across tasks. *When:* Running untrusted or buggy generated code where one task must not affect another.
- **Custom tools as an event round-trip** — Declare the tool on the agent. When the model calls it, the session emits a custom tool use event. The client listens for it, runs its own logic and returns a custom tool result. *When:* When a tool must run in your own system or hold your own data and the managed sandbox cannot host it.

## Numbers
- Time to first token reduced by about 90% after lazy sandbox provisioning. ([10:19](https://youtu.be/Uv0nAf_7tyU?t=619))
- Session is a two-hour slot split into four parts; this talk is part 1 and covers intro, architecture and the start of the console workshop. ([1:26](https://youtu.be/Uv0nAf_7tyU?t=86))

## Hot takes
- Harnesses encode assumptions, and those assumptions go stale with each new model, so the interfaces matter more than the harness.
- The session log is the only thing you must protect. Containers and harness instances should be treated as disposable.

## Tools mentioned
Claude Managed Agents, Claude Platform console (quick start), Claude Code, MCP, Sonnet 4.5, Opus 4.5, Haiku, Sonnet

## Relevance to our work
- **agentos** (2/3): The append-only session log and pluggable compaction map onto AgentOS L2A memory tiers and L2B scheduling, both of which need replayable run state. → *Prototype an append-only per-run event log in AgentOS, with a separate, swappable function that builds context from it, and check that a changed compaction strategy replays old runs without rewriting them.*
- **prosharness** (2/3): ProsHarness does checkpoint and resume for long Claude Code runs. The talk's recovery model, where a new harness resumes by reading the event log, is a direct design option for those checkpoints. → *Compare ProsHarness checkpoints with a replayable event log, and test resuming a killed run from its last logged event.*
- **general** (1/3): The talk gives a concrete per-task container and event-stream model for hosted agents. Its memory and multi-agent content is deferred to parts 2 to 4, which are not in this transcript. → *Read parts 2 to 4 of this series for the memory and multi-agent APIs before designing any orchestration around them.*
