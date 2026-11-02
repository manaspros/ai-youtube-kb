# Google A2A Protocol Explained: Tutorial, Demo, & How It Works with MCP & AI Agents

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `GUozMSpnmcc` · [watch](https://youtu.be/GUozMSpnmcc) · **date:** 2025-11-02 · **length:** 8:20 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Google
- **topics:** mcp-and-tools, multi-agent · **tags:** a2a, agent-to-agent, agent-card, mcp, agent-interop, agent-discovery, crewai, gemini

> Explainer of Google's A2A (agent-to-agent) protocol: agent cards for discovery, how it complements MCP, a hiring demo, and a CrewAI sample repo to clone.

## Summary
The speaker introduces Google's A2A protocol as an HTTP-based way for agents built on any framework (LangChain, CrewAI, Google ADK, custom code) to talk to each other. Each agent publishes an agent card describing its name, version, skills, inputs and auth, and a remote agent reads those cards to decide which agent to hand a task to, forming multi-agent chains. The main walkthrough is Google's demo of hiring a software engineer, where a sourcing agent found five candidates and a later agent ran background checks, all over one protocol. The talk argues A2A complements MCP rather than replacing it: MCP gives an agent its tools and data, and A2A lets agents communicate, with agent cards even exposed as MCP resources. It ends with a pointer to a CrewAI image-generation sample in Google's GitHub repo, which runs client to A2A server to CrewAI agent to Gemini API and back. Most of the content paraphrases Google's docs and demo video; no code is shown on screen.

## Key ideas
- **A2A is an open, HTTP-based protocol for agent-to-agent communication that is framework-agnostic: agents built with LangChain, CrewAI, Google ADK or custom code can talk to each other.** — The speaker frames it as the counterpart to MCP for agent-to-agent traffic, and expects adoption to grow as MCP's did. ([0:00](https://youtu.be/GUozMSpnmcc?t=0))
- **A2A complements MCP rather than replacing it.** — Speaker's analogy: MCP is a repairman with tools and knowledge; A2A is how he talks to clients or borrows parts from other agents. Google's docs are said to expect future agentic apps to use both. Separate MCP servers can themselves act as agents. ([2:37](https://youtu.be/GUozMSpnmcc?t=157))
- **The agent card is the discovery and capability contract.** — Each agent publishes a card describing what it can do. A remote agent reads the cards of other agents and picks the best-suited one, which can pass the task on again, creating a chain. ([1:16](https://youtu.be/GUozMSpnmcc?t=76))
- **Google's demo is a multi-step hiring workflow across agents.** — A remote agent given a job description uses agent cards in a tool registry to find a sourcing agent with extra constraints. The sourcing agent returned five candidates. Two weeks later, after interviews, another agent was called for updates and a background check on one candidate. ([1:16](https://youtu.be/GUozMSpnmcc?t=76))
- **Agent cards can be served through MCP, so the LLM can route to remote agents.** — Cards are listed as MCP resources. The LLM fetches them and passes them to sub-agents, which read the cards and decide which external agent to call. The speaker calls this a clever integration. ([4:08](https://youtu.be/GUozMSpnmcc?t=248))
- **Card accuracy is critical because clients decide on it alone.** — The card includes name, version, description, intended use, skills, default content types, accepted input parameters and any authentication requirements. An LLM or agent reads the card first to decide whether and how to use the agent. ([4:08](https://youtu.be/GUozMSpnmcc?t=248))
- **The protocol examples are simple JSON-style task requests and text responses.** — Google's docs show a sample card for a Google Maps agent, with URL, provider and auth type, and a task-send call whose example is asking for a joke, returning text. Other documented methods are mentioned without detail. ([5:35](https://youtu.be/GUozMSpnmcc?t=335))

## Techniques
- **Select a remote agent by its card before delegating** — Fetch the agent cards of candidate agents, match the task to the listed skills, check the expected input parameters and auth requirements, then send the task to the chosen agent. The speaker says the orchestrating LLM or agent decides from the card alone. *When:* An orchestrator has several candidate agents and must choose one for a task, as in the sourcing example.
- **Expose agent cards as MCP resources** — List each agent's card as an MCP resource on an MCP server. The LLM fetches the cards through MCP and passes the relevant card to the sub-agent that will call the remote agent. *When:* You already run MCP servers and want a single discovery path for remote agents alongside tools.
- **Generate A2A client and server code from the docs** — Add the A2A documentation to an AI coding tool, the speaker names Cursor's @docs feature, and let it generate code instead of memorizing the syntax. *When:* Starting an A2A integration with an unfamiliar protocol.
- **Quickstart with the sample agent repo** — Clone the full Google A2A GitHub repo, because the sample commands depend on its directory structure. Run the setup commands, which open a CLI for the sample A2A agent. The sample is a CrewAI image-generation agent that calls the Gemini API. The exact commands are not shown in the transcript. *When:* You want a working reference implementation of an A2A server and agent before writing your own.

## Numbers
- Sourcing agent identified five candidates for the software-engineer role. ([2:37](https://youtu.be/GUozMSpnmcc?t=157))
- Background check run on one candidate about two weeks after the initial sourcing, following interviews. ([2:37](https://youtu.be/GUozMSpnmcc?t=157))
- Sample task in the docs: a single-line 'tell a joke' request returning text. No latency, cost or adoption figures are given. ([5:35](https://youtu.be/GUozMSpnmcc?t=335))

## Hot takes
- The intro and title oversell the material ('mind-blowing', 'wild'). The content is mostly a paraphrase of Google's docs and demo video, with no code shown on screen.
- The 'tutorial' is a pointer to a repo and to Cursor's @docs feature. The setup commands are not shown, so it is not reproducible from the video alone.
- The claim that A2A will follow MCP's adoption curve is a prediction. The speaker also says the sample 'is not widely used just yet'.
- The speaker says Google confirmed A2A works with MCP. This is not checked against the cited docs in the video.

## Tools mentioned
A2A protocol (Google), MCP (Model Context Protocol), Google Agentspace (spoken as 'agent space'), Google Agent Development Kit (ADK), LangChain, CrewAI, Gemini API, Cursor (@docs feature), Google A2A GitHub repo (sample agents; name not stated)

## Relevance to our work
- **agentos** (1/3): AgentOS is a proxy in front of agents; A2A traffic between agents is a possible future route through the proxy, but the talk does not touch budgets, PII scanning, audit or routing. → *Read the A2A agent-card and task-send sections of Google's spec. Decide whether AgentOS should parse agent cards as a route or policy input before adding any A2A support.*
- **prosharness** (1/3): ProsHarness orchestrates agents (plan, Codex critique, debate). A2A could in principle turn the critique step into a remote agent described by a card, but that is not a current need. → *No change now. Note A2A as an option if the Codex critique step ever needs to run as a separate networked agent.*
- **general** (1/3): Agent-to-agent interoperability is a general multi-agent topic, but the talk stays at protocol level with no measurements. → *Skim Google's A2A spec for the task lifecycle and auth model if we design any multi-agent handoff, since the speaker only covers discovery and the sample task.*
