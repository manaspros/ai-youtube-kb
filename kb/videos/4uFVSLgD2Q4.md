# Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `4uFVSLgD2Q4` · [watch](https://youtu.be/4uFVSLgD2Q4) · **date:** 2026-07-18 · **length:** 18:30 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Gabe De Mesa · **orgs:** OpenGov
- **topics:** agent-architecture, enterprise-adoption, evals, sandboxing-execution · **tags:** OG Assist, Effect, Effect AI, A2A protocol, agent loop, human-in-the-loop, sandbox, rolling summary, generative UI, thumbs up/down feedback, CI evals, OpenTelemetry-style tracing, LangGraph, Claude, Cursor, TypeScript

> OpenGov's Gabe De Mesa on how they built and scaled OG Assist, an in-product agent: an in-house Effect-native agent loop, A2A contracts, approval gates, ephemeral sandboxes, and rolling-summary context.

## Summary
Gabe De Mesa, an engineer on OpenGov's AI agents team, describes OG Assist, a chat agent behind a nav-bar button in OpenGov's ERP products (budgeting, procurement, asset management, permitting). The team moved from LangGraph to its own agent loop built on the Effect TypeScript library, which gives tracing, logging, and dependency injection for swapping models. They use the A2A protocol as a rigid contract between front end and back end. Quality comes from thumbs up/down signals plus CI evals that run against real completions and check tool calls. Mutating tool calls deterministically pause for human Accept/Reject. Code execution and file creation run in on-demand sandboxes that are torn down afterward. For long conversations they use a rolling summary with recall over it, not stuffing the latest messages. The talk ends with internal use of Claude, Cursor, and cloud agents for development. It is a practitioner walkthrough of one production system, with no benchmarks.

## Key ideas
- **Own the agent loop instead of using a framework** — They moved off LangGraph because the team and use cases outgrew it. A custom loop gives full control of the agent, and Effect propagates tracing, structured concurrency, and logging through the whole loop. ([5:11](https://youtu.be/4uFVSLgD2Q4?t=311))
- **Effect is the foundation bet** — Effect is a TypeScript library with schemas, error handling, logging, and tracing built in. The team says it helped design the loop and services. Its dependency injection lets them swap the language model without changing loop code. ([3:47](https://youtu.be/4uFVSLgD2Q4?t=227))
- **A2A protocol as a front-end/back-end contract** — Google's Agent-to-Agent protocol is used to define agent routes, models, and schemas. The agent card (name, description, etc.) is the spec both sides build to, which kept development aligned. A2A has extensions, such as A2UI. ([7:32](https://youtu.be/4uFVSLgD2Q4?t=452))
- **Feedback signal plus CI evals on real completions** — Thumbs up/down from users is one signal. CI also runs evals against real completions, checking whether the right tools were hit and the expected actions happened. The team says these two loops together let them iterate on tools, skills, and the harness fast. The talk's line is that shipping is the start, not the finish. ([8:53](https://youtu.be/4uFVSLgD2Q4?t=533))
- **Deterministic human approval for mutating actions** — When a tool call needs approval, the loop is interrupted in code, not by prompting the model. The user sees an Accept or Reject UI before the action runs. This is used for write operations to keep humans in control. ([9:58](https://youtu.be/4uFVSLgD2Q4?t=598))
- **Ephemeral per-task sandboxes for agent code and files** — Code execution and file creation happen in sandboxes spun up on demand and torn down at the end. This isolates the agent from production systems. Example: the agent builds a PDF inside the sandbox that the user downloads. ([11:22](https://youtu.be/4uFVSLgD2Q4?t=682))
- **Rolling summary beats stuffing the latest messages** — Past a point, legacy token limits and long threads overload context. They keep a running summary updated every n messages, keep only the most recent messages verbatim, and let the agent recall details from the summary. This lets users refer back to material from far earlier in the conversation. ([12:33](https://youtu.be/4uFVSLgD2Q4?t=753))
- **Tools, then skills, built from Effect primitives** — A tool is defined, put into a toolkit (a collection of tools), and the toolkit is registered with the language model. Skills were built on the same blocks. The team says tools and skills are all you need. Generative UI works the same way: the agent registers a form primitive and renders it at runtime. ([16:13](https://youtu.be/4uFVSLgD2Q4?t=973))

## Techniques
- **Effect-native agent loop with injected language model** — Use the Effect AI package: a chat and a language model are both dependencies. Stream text through the chat, and pass the model in through dependency injection so it can be swapped. *When:* When you need full control over the agent loop and want to change models without rewriting loop logic.
- **A2A agent card as the API contract** — Model agent routes, the model, and the schema on the A2A spec (agent card with name and description). Build the front end and back end against that spec. *When:* When front-end and back-end teams build one agent surface and need a rigid, shared contract.
- **Deterministic approval interrupt** — Stop the loop in code when a mutating tool call is requested, show Accept or Reject, and resume only after the human answers. *When:* For any agent action that writes data or has side effects and needs human sign-off.
- **Automated tool-call evals in CI** — Run prompts against real model completions in CI and assert the expected tools were called and expected behavior happened. Pair with user thumbs up/down data. *When:* To catch regressions in tools, skills, and prompts on every change.
- **Ephemeral sandbox per agent task** — Create an isolated sandbox on demand for code execution and file creation, let the agent work there, return the artifact, and tear the sandbox down. *When:* When an agent must run code or produce files and must not touch production systems.
- **Rolling summary with recent-window and recall** — After every n messages, update a running summary. Keep only the last few messages in full (for example n-5 or n-10). Let the agent recall earlier topics from the summary. *When:* For long-running chat threads that exceed context limits but still need access to earlier turns.
- **Runtime generative UI via registered primitives** — Register a UI primitive (for example, a form) with the agent. The agent builds and renders an instance at runtime, with options drawn from the conversation. *When:* When the answer is best given as an interactive control, such as choosing among options, rather than as text.
- **Tools to toolkits to model registration** — Define each tool with a schema, group tools into a toolkit, and register the toolkit with the language model. *When:* When building a set of capabilities the model should call, and skills need to be composed from tools.

## Hot takes
- Tools and skills are really all you need.
- Shipping is the start, not the finish.
- Recommends trying the Effect AI package and building your own tools and skills.

## Tools mentioned
Effect, Effect AI, LangGraph, A2A protocol, A2UI, Claude, Cursor, Claude Cloud Agents

## Relevance to our work
- **agentos** (2/3): Crucible needs sandboxed code execution with teardown, and this talk gives a production example. The deterministic approval interrupt also maps to the exec-gate guardrail idea. The rolling-summary pattern is relevant to MemoryMesh's tiered cross-session memory. → *Specify Crucible's celld lifecycle as create-on-demand, return artifact, tear down, and add a test that confirms no sandbox state survives a task.*
- **prosharness** (2/3): ProsHarness uses phone-driven approvals. The talk's point is that the loop enforces approval in code for mutating tool calls, and that pattern fits a checkpoint-and-approve harness. → *Check that ProsHarness's phone approval blocks the mutating step in the loop itself, not only in the UI, and add a test for a rejected action.*
- **general** (1/3): Rolling summary with a recent-window and recall over the summary is a concrete context-engineering approach for long chats. The talk gives no measurements, though. → *Read the talk's rolling-summary section (12:33) and compare it to the current context compaction approach before choosing one.*
