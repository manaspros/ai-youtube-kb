# Agno AI Agent Tutorial: Build & Run AI Agents with Agent UI + MCP + CrewAI (Best Tutorial)

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `RWQv6JV7rKw` · [watch](https://youtu.be/RWQv6JV7rKw) · **date:** 2025-11-02 · **length:** 8:24 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS presenter (unnamed) · **orgs:** Agno, OpenAI, AI LABS
- **topics:** multi-agent, mcp-and-tools, agent-architecture · **tags:** agent-ui, agno, agno-playground, a2a, fastapi, nextjs, chat-ui, agent-routing, openai-sdk, langchain, mcp

> A short tutorial on Agent UI, an open-source Next.js chat front-end for agents. It shows swapping Agno's playground for a FastAPI backend and routing between specialist agents over A2A.

## Summary
The presenter introduces Agent UI, an open-source Next.js chat interface for AI agents, as a replacement for terminal-based agent use. He tours the default Agno Playground setup, which acts as a middle layer between agents and the UI and provides session memory. He recommends the automatic npx install from the docs and notes that the Agno Playground must be running first. For a non-Agno backend, he says you edit the Playground TypeScript file in Agent UI's API directory to point at your own endpoints. His demo replaces the Agno Playground with a FastAPI service hosting a main router agent and two specialist agents (plants and animals) on separate endpoints, communicating over A2A, with agents built on the OpenAI SDK. The video is mostly a UI tour and a verbal walkthrough; it omits the exact install command, config keys and code, and reports no measurements.

## Key ideas
- **Agent UI is an open-source chat front-end for agents, meant to be reused and rebranded, so you do not have to build chat UI from scratch.** — Pitched as an alternative to running agents in the terminal. The presenter says it is production-oriented and can be restyled for a product. ([0:00](https://youtu.be/RWQv6JV7rKw?t=0))
- **The Agno Playground sits between the agents and the UI and must be running in the background.** — It hosts multiple agents, shows which model each uses, and includes a memory layer that stores session data across interactions. The default demo has two agents: a web agent and another. ([1:00](https://youtu.be/RWQv6JV7rKw?t=60))
- **Install Agent UI with the automatic npx method from the docs, not the manual one.** — The template is built on Next.js. The Agno Playground must be running before Agent UI is used. The exact command is not spoken in the video. ([2:27](https://youtu.be/RWQv6JV7rKw?t=147))
- **To use a non-Agno backend, change the Playground TypeScript file in Agent UI's API directory to call your own agent endpoints.** — The presenter's version uses a FastAPI backend that exposes agent endpoints. He says the integration touched only about three or four files and a few core functions. ([3:52](https://youtu.be/RWQv6JV7rKw?t=232))
- **A main agent can route each query to a specialist agent on its own endpoint, with a fallback for general messages.** — The main agent forwards plant questions and animal questions to separate agents. Messages it does not classify are labelled other and answered by the main agent directly. ([5:56](https://youtu.be/RWQv6JV7rKw?t=356))
- **The agents talk to each other over A2A (agent-to-agent protocol), so agents built on different frameworks can interoperate.** — The presenter's agents are built with the OpenAI SDK. He refers viewers to a separate video for A2A detail. ([5:10](https://youtu.be/RWQv6JV7rKw?t=310))
- **The routing is verified with a few sample queries, one per route, to see the correct specialist answer.** — Tests: a general greeting, a plant question, and 'where do lions live?'. The presenter reports each was classified and handled by the expected agent, but gives no accuracy numbers. ([7:09](https://youtu.be/RWQv6JV7rKw?t=429))
- **Keep specialist replies short by putting the length rule in the system prompt of a small model.** — The presenter runs the agents on gpt-4o-mini and says he set short, focused replies through the system prompt. ([7:09](https://youtu.be/RWQv6JV7rKw?t=429))

## Techniques
- **Install Agent UI via the docs' npx template** — Copy the npx command from the Agent UI docs and run it in the directory where you want the project. The result is a Next.js project. Start the Agno Playground in the background first (the docs have a background example). The video does not show the exact command. *When:* Starting a browser front-end for your agents without building chat UI from scratch.
- **Swap the Agno Playground for your own backend** — Keep Agent UI as the front-end. Build a FastAPI service that exposes one endpoint per agent. Edit the Playground TypeScript file in Agent UI's API directory so it calls your endpoints instead of the Agno playground. The presenter says this took about three or four files plus a few core functions. *When:* Your agents use LangChain, the OpenAI SDK or another framework, not Agno.
- **Main-agent router over specialist endpoints** — Put a router agent in front. It reads each incoming message, picks the specialist (plant, animal), and forwards the message to that agent's own endpoint. Messages that match neither are handled by the main agent with a fallback label (other). Specialists talk over A2A. *When:* Several domain-specific agents sit behind one chat entry point, and each should run on its own endpoint.
- **Cap reply length with the system prompt** — Put a brevity instruction in the system prompt of the model (the presenter used gpt-4o-mini). *When:* Chat-style agents where long answers hurt the UI experience and cost.

## Numbers
- The video is 8:24 long and shows a 3-agent setup: one main router agent and two specialist agents (plants and animals). ([5:56](https://youtu.be/RWQv6JV7rKw?t=356))
- Replacing the Agno Playground with FastAPI took about three or four files plus a few core functions. ([5:56](https://youtu.be/RWQv6JV7rKw?t=356))
- The default Agno Playground demo has two agents running. ([1:00](https://youtu.be/RWQv6JV7rKw?t=60))
- Specialist agents run on gpt-4o-mini, configured with a short-reply system prompt. ([7:09](https://youtu.be/RWQv6JV7rKw?t=429))

## Hot takes
- Thin on substance for a tutorial: the exact npx command, config keys, code and A2A wiring are not shown, so the reader must check the docs or the repo.
- Roughly two of eight minutes are a UI tour with no technical content, and the praise for the UI is not backed by any evaluation.
- The routing demo is three hand-picked queries. Nothing shows how the router decides, its failure modes, or latency.

## Tools mentioned
Agent UI, Agno, Agno Playground, Next.js, npx, FastAPI, OpenAI SDK, A2A (agent-to-agent protocol), Cursor, LangChain, gpt-4o-mini, Gemini 2.5 Pro (mentioned in the demo answer, not used by the presenter's own setup)

## Relevance to our work
- **agentos** (1/3): AgentOS is an OpenAI-compatible proxy for any agent. This video shows a router agent that forwards queries to specialist agents over A2A, which is a small multi-agent routing pattern. → *Skim the A2A protocol docs before deciding whether AgentOS should route between separately deployed agents.*
