# MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `s4r6nk5WsZw` · [watch](https://youtu.be/s4r6nk5WsZw) · **date:** 2026-08-18 · **length:** 23:54 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Cornelia Davis · **orgs:** Temporal, Agentic AI Foundation, FastMCP
- **topics:** mcp-and-tools, agent-architecture, infra-cost-scaling · **tags:** MCP Tasks, async tools, long-running, durability, Temporal, workflow, human-in-the-loop, stateless protocol, FastMCP, signals

> Cornelia Davis (Temporal) explains why no MCP clients support MCP Tasks (async long-running tools) in v1, shows live demos of durable purchase-order and invoice workflows, and walks through the v2 changes that make tasks stateless and extension-based.

## Summary
The talk asks why no agents support MCP Tasks, the async mechanism for long-running MCP tools. The speaker grounds it in a purchase-order flow where an invoice-processing MCP tool waits on human approval and an ERP that retries. Tasks return a handle instead of a response, and the spec requires them to be durable, so they must survive client and server crashes and human delays. In v1, the lifecycle (working, input required, completed, canceled, failed) is sound, but task list is a stateful endpoint with no filter, and input-required is tunneled over a long-lived connection that is hard to implement. The speaker built a custom client-side workflow for the v1 reference implementation, which also had FIFO limits on multiple pending input requests. MCP v2, due around July, makes the protocol stateless, moves tasks into an extension, removes task list, and replaces the long-lived input channel with an update endpoint, while the server-side lifecycle mapping stays the same. Scale remains open: polling each task does not scale, so a notifications protocol is the proposed fix. The speaker plans a simpler implementation in FastMCP.

## Key ideas
- **Async MCP tools need durability, not just a handle** — Tasks return a handle instead of a response. The spec requires them to be durable, so they must survive network blips, human approvals that take days, and client or server crashes. ([4:44](https://youtu.be/s4r6nk5WsZw?t=284))
- **Task lifecycle is the core of the v1 spec** — Tasks move through working, input required, back to working, then completed, canceled or failed. Server-side, the speaker maps these lifecycle states onto the app's own domain state machine. ([11:44](https://youtu.be/s4r6nk5WsZw?t=704))
- **v1 has two hard problems: task list and tunneled input** — task list is a stateful endpoint with no filter, so it does not scale to many tasks. Input-required is carried over a long-lived result connection, which is tricky to implement and to recover after a drop. ([13:02](https://youtu.be/s4r6nk5WsZw?t=782))
- **v1 input responses were FIFO in the reference implementation** — With several tasks waiting for input at once, the client could only answer the first one. The speaker worked around this with a custom client-side workflow. ([23:03](https://youtu.be/s4r6nk5WsZw?t=1383))
- **v2 makes the protocol stateless and moves tasks into an extension** — The core protocol is stateless, and tasks become an extension. task list is removed. An update endpoint replaces the long-lived input channel, which works like a signal into the running task. ([16:15](https://youtu.be/s4r6nk5WsZw?t=975))
- **Clients should persist task IDs, and the spec only says so softly** — Without a persisted task ID there is no way to get the task back, and the spec states this as a should, not a must. Client-side durability is therefore the client's responsibility. ([18:48](https://youtu.be/s4r6nk5WsZw?t=1128))
- **Polling per task does not scale to millions of tasks** — A million clients polling a million tasks is not workable. A notifications part of the spec, with one endpoint that reports which tasks changed, is the proposed fix. The speaker says it is still early. ([21:14](https://youtu.be/s4r6nk5WsZw?t=1274))

## Techniques
- **Map task lifecycle onto a domain state machine** — Keep the app's own state machine (for example, invoice steps) on the server and translate its states into MCP task states (working, input required, completed, failed). The MCP layer then stays a thin view over the durable workflow. *When:* Building an MCP tool whose work is multi-step and takes minutes to days, with human approvals in the middle.
- **Signal into a long-running workflow for approvals** — Expose an update endpoint on the task. A human approval or rejection is sent as a signal into the durable workflow, which then resumes. This replaces holding a long-lived response connection open. *When:* Any tool step that needs human input while the process may run for a long time or the client may disconnect.
- **Client-side task tracker workflow** — Run the client's MCP task handling as its own durable workflow. It tracks the task ID, sends elicitation or input responses, and keeps going across client restarts. The speaker used this to handle many pending tasks and avoid FIFO limits. *When:* A client must manage many concurrent async MCP tasks and must survive restarts without losing track of them.
- **Parallel back-office steps beside an async tool call** — Record the receipt and run inventory and notification steps in parallel with the MCP tool call, which runs independently as its own task. *When:* A workflow has an async sub-step that should not block other steps.

## Numbers
- The v1 MCP Tasks spec was published in November and marked experimental. ([0:08](https://youtu.be/s4r6nk5WsZw?t=8))
- A v2 of the MCP Tasks spec is expected around July, and the speaker says it makes the protocol much simpler. ([7:03](https://youtu.be/s4r6nk5WsZw?t=423))
- The speaker submitted about 13 purchase orders in flight in the v1 demo. ([21:14](https://youtu.be/s4r6nk5WsZw?t=1274))
- Task list has no filter, so finding one task among a million requires paging through all of them. ([13:02](https://youtu.be/s4r6nk5WsZw?t=782))

## Hot takes
- Nobody implements MCP Tasks on the client side because the v1 spec is too involved, not because clients are behind.
- Stateful protocols are the worst thing for large distributed systems, so the move to a stateless core in v2 is the right call.
- Task list is a feature you should not use: just because you can list tasks does not mean you should.

## Tools mentioned
MCP Tasks, FastMCP, Temporal

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs long Claude Code jobs with checkpoint and resume, phone-driven approvals and loops. The durable-task, signal-for-approval and persist-the-task-ID patterns map closely onto its checkpoint and approval design. → *Compare ProsHarness approval and resume flow against the signal-into-workflow pattern, and make sure task or run IDs are persisted to disk before a run starts.*
- **general** (2/3): Durable long-running agent work with human approval is a recurring interest, and this talk gives a concrete failure list (network blips, vacations, crashes) plus the state mapping pattern. → *Read the speaker's MCP Dev Summit talk (March) on server-side durability for the server-side design details this talk skips.*
- **agentos** (1/3): AgentOS sits between agents and tools, and long-running async tool calls with approvals are a real gap there, but the talk is about MCP client and server protocol mechanics, not a pillar AgentOS has.
