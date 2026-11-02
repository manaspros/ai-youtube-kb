# Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `YNJvm7t3yq8` · [watch](https://youtu.be/YNJvm7t3yq8) · **date:** 2026-05-18 · **length:** 18:38 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Mike Christensen · **orgs:** Ably
- **topics:** agent-architecture, product-ux, multi-agent · **tags:** durable-sessions, resumable-streams, sse, websockets, pubsub, multi-device, live-control, ably, ai-chat-ux, subagents

> Ably's Mike Christensen argues that AI chat UX breaks under direct HTTP/SSE streaming and proposes durable sessions (a shared, resumable channel between agents and clients) to get resilient streams, multi-device sync, and live steering or cancel.

## Summary
The talk starts from the default chat pattern, where a client holds one SSE or HTTP stream to one agent, and argues that this couples the agent's output to a single client connection. Losing the connection drops the stream, a second tab or phone sees nothing, and no other client can steer or cancel the agent. The speaker names three capabilities that good AI products need: resilient delivery, continuity across devices, and live control. He says SSE is one-way, so resume and cancel conflict; moving to a bidirectional transport such as WebSockets fixes the upstream channel but not the multi-client problem. The proposed fix is a durable session, a persistent shared medium that agents write events into and clients subscribe to, which he says behaves like a pub/sub channel with addressability, persistence and resumability. Multi-agent setups benefit because sub-agents publish their own progress and the orchestrator only needs final results. The last part is a vendor demo of Ably AI Transport, a drop-in SDK on top of Ably channels, shown with multi-tab sync, reconnects, cross-device cancel, and a human agent joining the session. The talk gives architecture reasoning but no latency or cost benchmarks.

## Key ideas
- **Direct HTTP/SSE streaming ties the agent's output to one client connection** — The default chat pattern is one point-to-point stream from one client to one agent. If that connection drops, the stream is gone, and no other tab or device can see or reach the in-progress response. The speaker treats this as a design limit, not a model problem. ([0:00](https://youtu.be/YNJvm7t3yq8?t=0))
- **Three capabilities separate a fragile demo from a good AI product** — He names resilient delivery (reconnect and pick up where you left off), continuity across surfaces (same session on every tab or device), and live control (talk to the agent while it works, such as steer, follow up, or stop). ([2:49](https://youtu.be/YNJvm7t3yq8?t=169))
- **Durable session: a shared, persistent layer between agent and clients** — The agent writes events into the session without caring whether the client is connected. Clients connect to the session, replay, and resume from it. The agent does not need per-client replay logic. ([5:31](https://youtu.be/YNJvm7t3yq8?t=331))
- **SSE cannot offer resume and cancel together** — SSE is one-way, so a stop button can only close the connection. The agent then has to guess: buffer for a reconnect, or treat the close as cancel and stop paying for tokens. He says the AI SDK docs call abort incompatible with resume. He proposes a bidirectional transport such as WebSockets. ([7:55](https://youtu.be/YNJvm7t3yq8?t=475))
- **Multi-device needs a shared stream, not a private pipe** — A second tab or phone needs both visibility into the live response and an upstream route to the agent. A persistent connection to the session gives both, so any client can send a follow-up or cancel from any device. ([9:23](https://youtu.be/YNJvm7t3yq8?t=563))
- **Sub-agents should publish progress directly to the session** — In a multi-agent setup the orchestrator should only delegate and collect final results. Sub-agents write their granular progress to the shared session, and clients subscribe once to see all of it, without the orchestrator proxying every update. ([11:21](https://youtu.be/YNJvm7t3yq8?t=681))
- **A durable session is essentially a pub/sub channel with three properties** — Channels must be independently addressable (any client or agent joins by name), persistent (messages outlive any one connection or agent), and resumable (a dropped client rejoins at its last position). He presents Ably channels as meeting these properties. ([12:48](https://youtu.be/YNJvm7t3yq8?t=768))

## Techniques
- **Durable session as a shared channel** — Put the agent's event stream on a named, persistent channel. Agents publish events and clients subscribe. Clients resume from their last position after a drop, so the agent never handles reconnect or replay. *When:* Any streaming agent UI where users reconnect often (mobile, refresh, navigating away) or open the same conversation on several devices.
- **Hand-rolled resumable stream (the baseline he contrasts with)** — Store each streamed event with a sequence number in a fast store such as Redis. On reconnect, a resume handler works out which events the client missed and replays them in order. The speaker says this works but makes the agent own per-client replay plumbing. *When:* Only when you cannot use a shared session layer. It is the cost you pay for direct HTTP streaming.
- **Bidirectional transport to separate cancel from disconnect** — Replace SSE with a bidirectional transport such as WebSockets so the client can send an explicit cancel upstream. A dropped connection then means resume, and a cancel message means stop the LLM generation. *When:* When the UI needs a stop or steer button and the agent should stop burning tokens on cancel without losing the stream on a network drop.
- **Multi-agent writes straight to the shared session** — Each sub-agent publishes its own progress events to the session. The orchestrator publishes only the delegation and final result. Clients subscribe to the session, not to each agent. *When:* Orchestrator-plus-sub-agent systems where the user needs visibility into each sub-agent's progress and the orchestrator should stay simple.
- **Any-client control through the session** — Treat cancel, steer and follow-up messages as events sent to the session. The agent listens on the session, so any tab or device can send them. Cancelling one sub-agent from another tab is the example. *When:* Multi-device products where a phone or second tab should be able to interrupt or redirect a running agent.
- **Human handoff as another session participant** — Add a human support agent to the same session. They see the full history, then send messages as another participant, so the customer's conversation carries over without re-entering context. *When:* Support or copilot flows where an AI agent sometimes escalates to a person.

## Numbers
- Ably handles traffic for more than 2 billion devices per month (vendor self-report) ([1:21](https://youtu.be/YNJvm7t3yq8?t=81))
- Ably handles more than 30 billion monthly connections (vendor self-report) ([1:21](https://youtu.be/YNJvm7t3yq8?t=81))
- Ably processes more than 2 trillion API operations (vendor self-report) ([1:21](https://youtu.be/YNJvm7t3yq8?t=81))
- Speaker's team has talked to engineering teams at more than 40 companies across 10 industries about shipping AI agents and copilots ([1:21](https://youtu.be/YNJvm7t3yq8?t=81))

## Hot takes
- Resume and cancel are mutually exclusive over SSE, so direct HTTP streaming cannot support a proper stop button and reconnect together.
- The orchestrator agent should not relay sub-agent progress; sub-agents should write to a shared session directly.
- Agent code should not own per-client replay; that belongs in the transport or session layer.
- A durable session is basically pub/sub with addressability, persistence and resumability.

## Tools mentioned
Ably channels, Ably AI Transport, Server-Sent Events (SSE), WebSockets, Redis, Vercel AI SDK, TanStack AI

## Relevance to our work
- **prosharness** (2/3): ProsHarness does checkpoint/resume of long runs, phone-driven approvals and interactive control. The durable-session pattern fits these directly: events on a shared log, replay on reconnect, and approve, steer or cancel from any device. → *Prototype a sequence-numbered, append-only run-event log for ProsHarness so a phone or a second terminal can attach, replay from the last seen event, and send approve, steer or cancel messages.*
- **agentos** (1/3): AgentOS is a proxy in front of agents. A resumable, sequence-numbered event stream is relevant to its streaming path, but the talk is about client-agent UX, not proxy internals. → *Check whether the Govrix Scout proxy streaming path survives a client disconnect and whether it can replay missed chunks from a sequence number.*
- **general** (1/3): Useful background for any streaming agent UI, but there is no benchmark or code. → *Read the durable-sessions section before building any streaming agent chat UI that must survive refresh or multi-device use.*
