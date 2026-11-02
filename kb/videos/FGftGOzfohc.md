# Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `FGftGOzfohc` · [watch](https://youtu.be/FGftGOzfohc) · **date:** 2026-10-12 · **length:** 35:36 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Gabe (Anthropic, hands-on presenter), Priyanka (Anthropic, opening presenter, referenced) · **orgs:** Anthropic, SEC (EDGAR), AWS
- **topics:** agent-architecture, multi-agent, security-guardrails, memory · **tags:** claude-managed-agents, research-agent, sub-agents, outcomes, rubric-grading, vaults, credential-injection, memory-store, dreaming, map-reduce, sec-edgar, mcp-tunnels, self-hosted-sandbox, workshop

> Anthropic hands-on workshop (Part 2 of 4) building a research agent on Claude Managed Agents: sub-agents, rubric-graded outcomes, vaults, shared memory, dreaming, and a map-reduce harness.

## Summary
This is a 35-minute Anthropic workshop, part 2 of a four-part series, where attendees build a financial research agent on Claude Managed Agents. The presenter starts with a chat UI over the managed session event stream, then adds a skill for pulling SEC EDGAR filings and a sub-agent team. Next comes an async "outcome" where a rubric defines done and a separate grader sub-agent checks the work and triggers retries. The talk then covers vaults, which swap placeholder secrets for real credentials at egress only on allowed domains. It also shows shared memory stores, "dreaming" (consolidating memory from transcripts), and a custom orchestration tool that fans out many sessions. Q&A covers the limits: no per-session token budgets yet, no rewind (forking is on the roadmap), memory only consolidated for memory stores, and private-network access via MCP tunnels or self-hosted sandboxes. Much of the content is product walkthrough, but the outcome-grading, credential-swap, and sub-agent context-isolation details are concrete and reusable.

## Key ideas
- **Managed agents turn a session into an event stream** — Apps start a session, send user-message events, and listen to an SSE stream of agent events. Anthropic runs hosting, harness, sandbox, scaling, and the event log. Chat is just one client of this stream. ([2:57](https://youtu.be/FGftGOzfohc?t=177))
- **Long-running work is the point, not chat** — The presenter frames the product around async tasks that run for hours, days, or even months. The chat UI is shown as a stopping point, not the destination. ([13:07](https://youtu.be/FGftGOzfohc?t=787))
- **Outcomes provide self-supervision with a rubric** — A user-defined outcome carries the task, a rubric, and max iterations. When the main agent thinks it is done, a sub-agent grades the artifacts against the rubric. If the check fails, the agent retries. ([18:09](https://youtu.be/FGftGOzfohc?t=1089))
- **Sub-agents run as threads and report back to the main agent** — The demo spawned an extractor and a risk evaluator. Each sub-agent works in its own thread and returns results to the parent, which then writes the deliverables and updates memory. ([20:27](https://youtu.be/FGftGOzfohc?t=1227))
- **Self-reference sub-agents copy definitions, not transcripts** — An agent can declare itself as a sub-agent type. A spawned copy gets the prompt, tool descriptions, and schemas, but not the parent's transcript. ([15:24](https://youtu.be/FGftGOzfohc?t=924))
- **Vaults keep real secrets out of the sandbox** — The agent's environment holds a placeholder. At egress the platform swaps in the real value, but only for the domains the secret is allowed to reach. Calls to other domains get no swap. ([24:25](https://youtu.be/FGftGOzfohc?t=1465))
- **Skills are live artifacts that new sessions pick up** — Updating a skill's content (here, adding a new SEC form) means any new session that references it gets the change. Old sessions are not affected. ([22:41](https://youtu.be/FGftGOzfohc?t=1361))
- **Dreaming consolidates memory across sessions, but only for memory stores today** — The consolidation pass reads transcripts and memories from many sessions and updates the memory store so future agents find better notes. The presenter says it could extend to skills, prompts, and agent definitions later. ([29:59](https://youtu.be/FGftGOzfohc?t=1799))
- **Steering is by queued messages, not rewind** — A user can send new message events mid-run, and they queue up. There is no rewind or roll-forward yet; session forking is a requested feature on the roadmap. ([28:18](https://youtu.be/FGftGOzfohc?t=1698))
- **Environment dependencies are installed at creation and cached** — Packages are set when the environment is created and reused across sandbox restarts. Only packages reachable through npm, cargo, or pip work directly; other files or GitHub repos can be uploaded into a session. ([67:00](https://youtu.be/FGftGOzfohc?t=4020))

## Techniques
- **Rubric-gated outcome with a grader sub-agent** — Define the task, a rubric, and max iterations in one outcome event. A separate grader sub-agent checks the produced artifacts against the rubric before the run is marked complete. Failing runs retry up to the cap. *When:* Async tasks with checkable deliverables, such as a scorecard file plus a memory note, where you need a completion check that does not rely on the worker agent's own claim.
- **Placeholder secrets with domain-scoped egress swap** — Store the real credential in a vault. The sandbox only sees a placeholder env var. The egress layer replaces it with the real value only when the request goes to an allowed host. *When:* Any agent that calls authenticated APIs or MCP servers, so the model and sandbox never hold the raw key and the key cannot leak to other domains.
- **Context isolation via self-referencing sub-agents** — Declare the main agent as a sub-agent type. Spawned copies inherit its prompt and tool schemas, not its conversation, so each worker starts with a small, fresh context. *When:* When the parent does not know in advance which sub-tasks will come up, but wants to fan out copies of its own behavior.
- **Check shared memory before redoing work** — Agents first query a memory store for prior analysis of the same entity (for example, a company ticker), and only do new research for what is missing. They write back notes at the end. *When:* Repeated research or analysis over the same entities, where cost and duplicate work matter.
- **Map-reduce orchestration via a custom dispatch tool** — Give the main agent a custom tool that calls the platform API to start one session per item (such as per ticker). Aggregate the results at the end. *When:* Batch work across many items where each item needs its own long-running, isolated session.
- **Transcript-driven memory consolidation (dreaming)** — Run a scheduled pass over transcripts and memories from many sessions. Merge and correct the memory store so future agents pull better notes. *When:* Multi-session agent fleets where edge-case lessons should accumulate across users.

## Numbers
- Ticker analysis session takes about 10 minutes, with a pre-recorded run shown ([19:17](https://youtu.be/FGftGOzfohc?t=1157))
- Demo spawned 2 sub-agents (financial extractor and risk evaluator) for one ticker analysis ([20:27](https://youtu.be/FGftGOzfohc?t=1227))
- Credits said to appear within about 5 minutes, although the form says 1 to 2 days ([23:50](https://youtu.be/FGftGOzfohc?t=1430))
- Workshop structured as six acts ([7:25](https://youtu.be/FGftGOzfohc?t=445))
- Video length 35:36 in a four-part series ([0:00](https://youtu.be/FGftGOzfohc?t=0))

## Hot takes
- "I don't think anybody's writing code by hand, so I'm not going to do that either." (6:19)
- Everything is an API call, so you can take your memory and data anywhere; no lock-in. (31:06)
- Budget controls such as max money or tokens per session are not offered today, but are being explored. (27:43)

## Tools mentioned
Claude Managed Agents API, Claude Code (used to drive the workshop), SEC EDGAR Python package, MCP, Bun, npm, Agent SDK (compared)

## Relevance to our work
- **agentos** (2/3): The vault placeholder-plus-egress-swap maps onto the L1 proxy's role as the single choke point for agent traffic. Domain-scoped secret injection is a governance/security feature the proxy could own. → *Prototype placeholder secrets in the Govrix proxy: agents see a placeholder, and the proxy swaps the real key only for allowed hosts, with each swap logged to the Merkle audit log.*
- **agentos** (2/3): Dreaming (transcript-driven memory consolidation) is a concrete pattern for the conflict-resolution and provenance parts of MemoryMesh, which the talk does not address in depth. → *Read the dreaming design and compare its consolidation step with MemoryMesh's conflict resolution, using RAGAS to measure whether consolidated memories help later sessions.*
- **prosharness** (2/3): A rubric-gated completion check with a separate grader sub-agent and a retry cap fits ProsHarness's plan, critique, and debate loop, and checks that a run is really done. → *Add an outcome-style gate to ProsHarness runs: a rubric file, a separate grader sub-agent (Codex or Claude) that checks the artifacts, and a max-iterations cap before a checkpoint is marked complete.*
- **general** (2/3): A concrete, practical comparison of managed-agent primitives (outcomes, vaults, memory stores, sub-agents, dreaming) for anyone designing long-running agents, plus the explicit gaps (no budgets, no rewind, memory-only dreaming). → *Read the Managed Agents docs for outcomes and vaults and write a short comparison against our own agent harness design.*
- **agentos** (1/3): Live-updated, versioned skills picked up by new sessions is close to SkillForge's governed skill library. The talk gives no governance detail. → *Compare the live-skill update model with SkillForge's governed skill registry to decide how a new skill version is rolled out to new sessions only.*
- **agentos** (1/3): The platform has no built-in per-session token or money budgets, which is a gap AgentOS's L1 budget pillar could fill. → *Note this gap in the AgentOS budget design: enforce per-session token caps in the proxy, not in the agent harness.*
- **prosharness** (1/3): Queued steering messages mid-run are a lightweight alternative to rewind. ProsHarness already has checkpoint/resume, so the relevant part is the mid-run steering UX. → *Check whether ProsHarness can queue user steering messages to a running session, instead of only approving or killing it.*
