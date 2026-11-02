# Cloudflare Just Made AI Agents WAY Easier (Agents SDK)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `l4tHKJFQvRg` · [watch](https://youtu.be/l4tHKJFQvRg) · **date:** 2025-11-02 · **length:** 7:14 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack, Cloudflare
- **topics:** agent-architecture, infra-cost-scaling, dev-tools · **tags:** cloudflare, agents-sdk, durable-objects, human-in-the-loop, scheduled-tasks, websocket, ai-sdk, react, model-routing, workers-ai

> Better Stack demos Cloudflare's Agents SDK starter: durable-object agents that persist state, sync across browsers, schedule tasks and pause for human approval. Demo-driven, with no benchmarks.

## Summary
The presenter walks through Cloudflare's new Agents SDK starter, which runs each agent as a Durable Object so state persists across refreshes, dev-server restarts and long sleeps. The demo covers a chat agent that schedules a delayed task, keeps two browser windows in sync, and waits for approval before running a weather tool. The code tour covers the React useAgent hook, the server-side AIChatAgent base class, agent.setState backed by a per-instance SQL store, tool definitions with and without an execute function, and the schedule method with its callback and payload. It also mentions model routing through Workers AI on reachability, rate limits and cost budgets, plus a roadmap for email, WebRTC voice/video, a built-in eval framework and self-hosting. It is a single short walkthrough of a starter app with no latency, cost or scale measurements, and most claims about waiting for days or scaling to millions of agents are untested.

## Key ideas
- **Each agent is a Durable Object instance, so its state survives page refreshes and a stopped dev server, and it can sleep for minutes, hours or days and resume.** — The scheduled-task demo fires after the browser refresh and after the dev server is shut down. Persistence is the core claim; no limits or pricing are given. ([0:00](https://youtu.be/l4tHKJFQvRg?t=0))
- **Scheduling is a first-class tool pattern: the LLM turns natural language (a specific date, a delay in seconds, or a cron expression) into structured schedule arguments.** — The schedule tool takes a type of scheduled, delayed or cron. The execute function calls the agent's schedule method with the time, a callback method name and a payload. The presenter argues this unstructured-to-structured conversion is the main thing LLMs are good at here. ([5:24](https://youtu.be/l4tHKJFQvRg?t=324))
- **When a scheduled callback fires, it inserts a synthetic user message into the chat history and the normal chat loop answers it.** — The executeTask method on the agent receives the stored description as payload and writes it as if the user had typed it, so the reply path needs no special handling. ([5:24](https://youtu.be/l4tHKJFQvRg?t=324))
- **Human approval is done by leaving the tool's execute function out, so the call waits for the user; the real implementation lives in an executions map keyed by tool.** — The weather tool pauses until approved. The approval state syncs to other open browsers and survives refreshes, and the presenter says it would wait for approval for minutes, hours or days. The local-time tool has an execute function and runs without approval. ([1:23](https://youtu.be/l4tHKJFQvRg?t=83))
- **Agent state is a built-in SQL store per instance, and the recommended write path is agent.setState, which pushes to clients through onStateUpdate; raw agent.sql is the lower-level option.** — On the client, the useAgent hook manages the WebSocket connection. An onStateUpdate handler copies the state into React useState. Multi-window and multi-device sync come from this store, not separate code. ([2:48](https://youtu.be/l4tHKJFQvRg?t=168))
- **Agent identity is the routing key: one shared agent ID (chat) syncs everyone, while a user ID or workflow ID gives each user or workflow its own agent.** — The presenter says this lets an app run very many agents without managing infrastructure. Scale is asserted, not measured. ([1:23](https://youtu.be/l4tHKJFQvRg?t=83))
- **Model routing can be done in the agent code via Workers AI, switching models on unreachability, rate limits or exceeded per-provider cost budgets.** — The presenter describes the trigger conditions and points to docs. No thresholds, fallback order or code are shown. ([4:13](https://youtu.be/l4tHKJFQvRg?t=253))

## Techniques
- **Single shared agent for multi-window sync** — Connect the React client with the useAgent hook using a fixed agent ID (the demo uses chat). Every connected browser then shares one Durable Object and its state. *When:* Shared-state apps such as a team chat or a demo where several windows should stay in sync.
- **Per-user or per-workflow agent routing** — Use the user ID or a workflow ID as the agent ID in the connection, so each user or workflow gets its own agent instance and its own SQL state. *When:* Multi-tenant agents where state must be isolated per user or per run.
- **Chat agent setup** — On the server, define a class that extends AIChatAgent (not the base Agent when chat is not involved) and implement onChatMessage. Models are wired through the AI SDK; any model with an OpenAI-compatible API schema works. *When:* Chat-style agents where message history and streaming are needed. Use the base Agent class for non-chat agents.
- **Persisting UI state** — On the server, call agent.setState(newState) to write. On the client, register onStateUpdate in useAgent and copy the incoming state into React state. Use agent.sql only when setState does not fit. *When:* Counters, form fields, preferences and user history that must survive reloads and sync across devices.
- **Human-in-the-loop tool approval** — Define the AI SDK tool without an execute function, so the call waits for approval. Put the real implementation in the executions object at the bottom of the tools file, keyed by tool name, and it runs only after the user approves. Keep execute on tools that should run automatically. *When:* Side-effecting tools such as sending messages, spending money or calling external APIs where a user should confirm first.
- **Scheduling tasks from chat** — Define a schedule tool whose input is a type (scheduled date, delayed seconds, or cron). In execute, get the agent context and call agent.schedule with the time or cron expression, a callback method name and a payload. Implement that callback method on the agent (executeTask here) to insert the payload as a user message. *When:* Reminders, delayed follow-ups or recurring agent runs that must survive restarts.

## Numbers
- Scheduled task demo: a request made with a 10-second delay ran after the browser refresh and dev-server shutdown. ([0:00](https://youtu.be/l4tHKJFQvRg?t=0))
- Human approval is described as waitable for minutes, hours or days. This is a claim about durable-object sleep; it was not tested in the video. ([1:23](https://youtu.be/l4tHKJFQvRg?t=83))
- Agent-per-user routing is described as scaling to millions of agents. This is an assertion with no load or cost data. ([1:23](https://youtu.be/l4tHKJFQvRg?t=83))
- Model routing triggers: unreachable model, client rate limit, or exceeded per-provider cost budget. No thresholds are given. ([4:13](https://youtu.be/l4tHKJFQvRg?t=253))
- No latency, throughput, pricing or cost-per-agent figures appear anywhere in the video (length 7:14). ([0:00](https://youtu.be/l4tHKJFQvRg?t=0))

## Hot takes
- The presenter calls the SDK 'insane' in ease of use, but the evidence is one starter app running locally, with no production or failure-mode testing.
- The 'millions of agents' and 'wait days for approval' claims are asserted, not demonstrated.
- Roadmap items (email, WebRTC voice/video, built-in evals, self-hosting) are not shipped features in the demo.
- Scheduling via LLM-parsed natural language is presented as the SDK's strongest feature; the parsing step's failure modes are not discussed.
- The model-routing feature is mentioned in passing with no code or thresholds, so it is hard to evaluate from this video.

## Tools mentioned
Cloudflare Agents SDK (starter template), Cloudflare Durable Objects, Cloudflare Workers AI, AI SDK (used for tools and model calls), AIChatAgent (Agents SDK base class for chat), useAgent (React hook from the SDK), React, WebSocket, Hono (official middleware mentioned), OpenAI-compatible API schema (for model choice)

## Relevance to our work
- **agentos** (2/3): Human approval pauses and scheduled callbacks persisted per agent instance match the approval and scheduling ideas in Crucible's exec-gate design and in the L2D skill-mining pipeline. The Cloudflare platform itself is not what AgentOS runs. → *Write down the approval-pending state for Crucible exec-gate as durable server state (survives client refresh and restart) before building its UI, and test it against a restart.*
- **prosharness** (2/3): Phone-driven approvals need pending approvals to survive refresh and sleep. The approval-as-missing-execute pattern and the synced approval state map directly onto that requirement. → *Check that ProsHarness approval requests are stored server-side and resume after a refresh or dropped connection, the way the weather-tool approval does here.*
