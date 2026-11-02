# Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `HvMyYLTfvhg` · [watch](https://youtu.be/HvMyYLTfvhg) · **date:** 2026-09-18 · **length:** 13:22 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Jeff Ng · **orgs:** Unblocked, Cloudflare, Vercel, AWS, Linear, Slack
- **topics:** context-engineering, memory, agent-architecture, mcp-and-tools · **tags:** context-engine, background-agents, durable-execution, checkpointing, org-knowledge, mcp-limits, permission-scoped-retrieval, vendor-talk

> Jeff Ng (Unblocked) argues agent infrastructure is now easy to assemble, so the real gap is organizational context. He demos a context engine that feeds agents synthesized, permission-scoped knowledge instead of raw MCP results.

## Summary
Jeff Ng, a founding engineer at Unblocked, says building a production agent used to take a team about a quarter, but primitives from Cloudflare, Vercel, AWS and frameworks like Mastra now cover most of the plumbing. He lists the remaining infrastructure tax: durable checkpointing of long runs, isolated sandboxes for agent-run code, and cross-system observability. His main claim is that agents still fail confidently because they lack organizational context such as Slack discussions and postmortems. In a live demo, a Linear-ticket enrichment agent recommended re-enabling an async dispatch that had caused an outage, because it did not see the postmortem. When a context engine was connected first, the recommendation flipped to avoid the outage. He argues MCP provides access but not understanding, since it returns raw results that flood the context window and can conflict with each other. The talk is short and vendor-led, with one anecdotal demo and no benchmarks.

## Key ideas
- **Agent plumbing is now mostly solved by primitives** — Cloudflare, Vercel, AWS and frameworks such as Mastra handle much of the infrastructure. Defining an agent reduces to a model, instructions, tools, skills, and a sandbox location. ([0:14](https://youtu.be/HvMyYLTfvhg?t=14))
- **Durable checkpointing is needed for long agent runs** — Crashes lose message history, tool-call records and loop position. Restarting wastes tokens and latency, and can repeat side effects. ([1:12](https://youtu.be/HvMyYLTfvhg?t=72))
- **Sandboxes are required for agent-run and third-party code** — Isolation keeps agent code away from environment secrets and unneeded network access, and protects the shared host. ([2:13](https://youtu.be/HvMyYLTfvhg?t=133))
- **Background agents fail on missing organizational context** — The demo agent recommended re-enabling async dispatch, which had caused an outage. It had not seen the Slack thread or the postmortem ticket, so it had a narrow view of the problem. ([5:52](https://youtu.be/HvMyYLTfvhg?t=352))
- **Humans currently act as the context layer in local use** — In-the-loop engineers supply decisions, past incidents and reasons. Without a human, that missing context becomes a silent failure. ([6:54](https://youtu.be/HvMyYLTfvhg?t=414))
- **A context engine returns synthesized, scoped understanding, not documents** — It resolves conflicts across sources, respects the agent's access roles, and delivers task-relevant conclusions the agent can act on directly. ([8:24](https://youtu.be/HvMyYLTfvhg?t=504))
- **MCP gives access, not understanding** — Connecting Slack, Linear and GitHub MCP servers returns raw results that flood the context window, raise token cost, and can disagree with each other. The agent is left to decide what to believe. ([10:25](https://youtu.be/HvMyYLTfvhg?t=625))
- **Use cases beyond ticket enrichment** — The speaker lists hydrating coding-agent plans, code review that reflects team conventions, and answering customer-success and sales questions from institutional knowledge. ([11:40](https://youtu.be/HvMyYLTfvhg?t=700))

## Techniques
- **Durable per-step checkpoints for agent runs** — Persist message history, tool calls and loop position so a crashed session resumes instead of restarting. Keep side effects from firing twice on resume. *When:* Long-lived, stateful agent runs on ephemeral infrastructure.
- **Isolated sandboxes for agent and third-party code** — Run generated or third-party code in an isolated sandbox that cannot read environment secrets or reach the network unless needed, so the shared host is not exposed. *When:* Agents execute code they did not write, on shared infrastructure.
- **Context engine queried before the agent reasons** — Connect docs, code, tickets and chat, build a model of the organization, and have the agent call the engine first. The engine returns reconciled, ranked, permission-scoped summaries. In the demo, the agent was prompted to research the ticket through the engine before recommending a next step. *When:* Background or unattended agents that need institutional knowledge such as postmortems and decisions.
- **Synthesized context over raw tool results** — Have a layer resolve conflicts across sources and return a short conclusion, instead of exposing several raw MCP results that the agent must reconcile itself. *When:* Several sources can disagree, or raw results would fill the context window.

## Numbers
- Six months earlier, building an agent took a team's effort and about a quarter ([0:14](https://youtu.be/HvMyYLTfvhg?t=14))
- The QA pipeline's time to first character had degraded to 3-4 seconds, against a realistic target of hundreds of milliseconds (the scenario behind the demo ticket) ([4:20](https://youtu.be/HvMyYLTfvhg?t=260))

## Hot takes
- Building agents is trivial now; the hard part is context.
- MCP is great at access, but access isn't understanding.
- The gap isn't intelligence. It's context.
- Without a human in the loop, missing organizational context becomes a silent failure.

## Tools mentioned
Cloudflare, Vercel, Mastra, Flu (transcript spelling of the framework), Linear, Slack, GitHub MCP, Claude Code, Codex, Unblocked context engine

## Relevance to our work
- **prosharness** (3/3): ProsHarness checkpoints and resumes long Claude Code runs. The talk's main warning is that resume must preserve messages, tool calls and loop position, and must not repeat side effects. → *Audit ProsHarness checkpoint/resume: confirm each checkpoint records tool-call results and loop position, and that replaying a resumed run cannot re-fire external side effects. Add a test that kills a run mid-tool-call and checks for duplicate effects.*
- **agentos** (2/3): MemoryMesh already has cross-session memory, conflict resolution and provenance. The talk argues that memory should return synthesized, permission-scoped conclusions rather than raw hits. → *Add an eval to MemoryMesh where two sources conflict and the test checks whether the retrieval output is a reconciled answer with provenance, not raw chunks. Compare it with a flood-the-context baseline on tokens used.*
- **general** (1/3): The failure case is an agent that acted on a ticket without the linked incident discussion. This suggests a test type for evals. → *Add eval cases where the correct answer depends on a fact that only appears in another system, such as a postmortem or chat thread, and check whether the agent finds it.*
