# A Piece of Pi: Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `vAIDdLKB6-w` · [watch](https://youtu.be/vAIDdLKB6-w) · **date:** 2026-05-18 · **length:** 20:42 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Matthias Luebken · **orgs:** Taven AI, OpenClaw, Pi, Anthropic (Claude Cowork), NVIDIA
- **topics:** agent-architecture, coding-agents, enterprise-adoption · **tags:** pi, openclaw, embedding-coding-agents, agent-loop, extensions, hooks, per-customer-agents, agents-md, cli-tools, sandboxing, rfp-workflow, typescript

> Matthias Luebken (Taven AI) shows how the open-source Pi coding agent, the core under OpenClaw, can be embedded in a product: an agent is a tool-calling loop, and a sales-RFP email agent is built on per-customer sessions and CLI tools.

## Summary
The speaker, from a small European agent company called Taven AI, introduces Pi, a minimal open-source coding agent that sits underneath OpenClaw. He argues that an agent is just an LLM running tools in a loop, and that a coding agent is the same loop with a shell and a runtime added, so most of the "magic" comes from the tools it can call. He walks through a small TypeScript CRM demo that uses Pi's agent class, its event stream, and a before-tool-call hook for authorization checks. He then shows Pi's extension API, which can add slash commands and interactive UI selects in the terminal, and notes that the same mechanism could drive a web UI although that path is still being refactored. For a client project, his team dropped the coding-agent framing and built an email-driven sales workflow in which one agent per customer, with its own AGENTS.md and CUSTOMER.md, handles each inbound RFP inside a reused session, using CLIs to reach CRM and ERP systems and producing drafts for a human to edit. He admits that sandboxing is still early for them and points to NVIDIA's OpenShell as something to study.

## Key ideas
- **An agent is just an LLM running tools in a loop, with goals and context (often AGENTS.md). Everything else is use-case shaping.** — The speaker stresses that the core is small, so the best way to understand agents is to open up a minimal SDK like Pi and play with it directly. ([5:01](https://youtu.be/vAIDdLKB6-w?t=301))
- **A coding agent is the same loop plus a shell and runtime, so any capability can be added as a tool call.** — His example: when OpenClaw got a voice message it did not know how to handle, it used a local FFmpeg tool through the shell. From outside this looks like learning, but internally it is one more tool call. ([9:00](https://youtu.be/vAIDdLKB6-w?t=540))
- **Use before-tool-call hooks and session events to steer and gate an agent.** — A hook can block a contact update unless a check passes, which is a place to add role-based access or other enterprise rules. Events let the host see each tool call and its result. ([7:35](https://youtu.be/vAIDdLKB6-w?t=455))
- **Extensions can add commands and interactive UI, not only tools.** — In the terminal, a custom pipeline command loads context and then shows a select or dropdown to the user. The speaker says the same extension mechanism could drive a web UI, though the refactor is still in progress and the framework is still tuned to coding agents. ([10:25](https://youtu.be/vAIDdLKB6-w?t=625))
- **Pi's core packages are reused by OpenClaw, but OpenClaw built its own plugin layer.** — The packages are the coding agent, agent core, a unified LLM abstraction (pi-ai), and a terminal UI. OpenClaw adds multi-channel routing, provider orchestration, sub-agents and gateway support on top. ([13:14](https://youtu.be/vAIDdLKB6-w?t=794))
- **For a product, design a per-customer agent with its own harness file and a session per case, rather than one general agent.** — An RFP email is routed to the agent for that customer. AGENTS.md describes the agent's role, CUSTOMER.md holds customer-specific rules, discounts and access, and a session is reused per case so earlier conversation is kept. ([14:20](https://youtu.be/vAIDdLKB6-w?t=860))
- **Expose backend systems as small CLIs, since agents use CLIs well, and keep a human in the loop by writing drafts.** — CRM and ERP access is wrapped as CLIs behind the team's own sandbox. The output is an email draft the user edits in their inbox, so the user stays in the tool they already use. Sandboxing is acknowledged as not yet solved. ([17:01](https://youtu.be/vAIDdLKB6-w?t=1021))

## Techniques
- **Agent as tool loop with event and hook surface** — Build a thin agent class with a system prompt and tool list, subscribe to events for each tool call and result, and add a before-tool-call hook for authorization or policy checks. *When:* When you need to see and control each step of an agent without adopting a large framework.
- **Extension commands with UI selection** — Register a slash command in an extension that loads context and then calls a UI select or dropdown, so the agent interacts with the user as well as with backend systems. *When:* When a workflow needs human choices mid-run and the agent host is a terminal or a future web UI.
- **Per-customer agent with harness and customer files** — Give each customer its own agent directory with a general AGENTS.md for behavior and a CUSTOMER.md for account-specific rules, then reuse one session per business case. *When:* When many customers have different rules, access and pricing, and each case needs continuity across emails.
- **Backend access as CLIs for the agent** — Wrap CRM, ERP and similar systems as small CLI tools rather than bespoke APIs, and let the agent call them from its shell. *When:* When the agent needs to read or write business systems and you want a simple, inspectable tool surface.
- **Small single-purpose tools packaged as a skill** — Instead of one large integration, combine small CLIs (for example pandas, openpyxl and LibreOffice for Excel) and package them as a skill the agent can use. *When:* When adding a domain capability such as spreadsheet work and you want each piece to do one thing well.
- **Draft-first human-in-the-loop output** — The agent writes a draft into the tool the user already uses (an email draft), and the human edits and sends it. *When:* When the agent output has external impact and a person must approve it.

## Hot takes
- Nobody can write an authoritative book on this yet because there are no settled patterns; the speaker says the field is still at a fuck-around-and-find-out phase.
- Coding agents will be a core building block of software systems, and the speaker is betting on it.
- Make the system easy for the coding agent to use, since agents are good at CLIs and small, single-purpose tools.

## Tools mentioned
Pi, OpenClaw, Claude Cowork, FFmpeg, pandas, openpyxl, LibreOffice, AGENTS.md, NVIDIA OpenShell, TypeScript

## Relevance to our work
- **agentos** (1/3): The per-customer agent harness, session-per-case reuse, and CLI-first tool surface are relevant patterns for AgentOS's gateway and multi-agent layers, but the talk gives no measurements. → *Read the Pi package README and try a per-tenant AGENTS.md plus CUSTOMER.md split in a small AgentOS routing prototype before designing the tenant config format.*
- **prosharness** (1/3): A before-tool-call hook for authorization is a pattern ProsHarness could use for approval gating, though ProsHarness wraps the Claude Code CLI rather than Pi. → *Check whether ProsHarness's approval step can run as a pre-tool-call hook that blocks specific tool calls, and compare it with Claude Code's own hook config.*
