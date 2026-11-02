# Introducing Open-Source PHIDATA: Your first step towards building your own AI Agents

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `nkh7q8WU7oU` · [watch](https://youtu.be/nkh7q8WU7oU) · **date:** 2024-11-02 · **length:** 11:08 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Ashpreet Bedi · **orgs:** Phidata, OpenAI, Exa, DuckDuckGo, Ollama
- **topics:** agent-architecture, memory · **tags:** phidata, agent-ui, agent-playground, local-agents, session-storage, privacy, demo

> Walkthrough of Phidata's agent playground UI, showing how to serve agents from a local server on port 7777 and chat with them through the hosted app while memory and sessions stay on your machine.

## Summary
AI LABS introduces Phidata, an open-source framework for building AI agents with memory, knowledge and tools, and its agent UI. The first part is a tour of the hosted playground, where demo agents (finance, web search, research, YouTube) run on Phidata's servers. The second part is a clip from a Phidata developer who runs the same kind of agents locally: clone the repo, set up a virtualenv, export API keys, install dependencies, authenticate the Phidata app from the terminal, and start a demo playground server on localhost:7777. The server registers only its endpoint with the hosted UI, and the chat traffic goes to the local agents. Sessions and memory are stored in a local database file, so deleting that file erases history. Session logging is off by default. The video is mostly a UI demo with little on agent design, evals or failure modes, so the reusable content is the local-serve architecture and the session-storage behavior.

## Key ideas
- **Phidata presents agents as having their own memory, knowledge and tools, with the agent UI as the chat front end.** — The intro frames the tool as running agents with local memory, knowledge and tools through a simple UI. The hosted playground demo agents run on Phidata's servers, not locally. ([0:00](https://youtu.be/nkh7q8WU7oU?t=0))
- **The local setup keeps agent execution on your machine and tells the hosted app only the endpoint.** — The speaker says the only thing sent from the local machine to Phidata is the server endpoint. The hosted UI then connects to the local agents and chat happens through it. This is the architecture claim the video makes, not one it verifies. ([2:45](https://youtu.be/nkh7q8WU7oU?t=165))
- **Each agent is defined like a normal data agent, with a description and tools, and a demo file serves several of them at once.** — The demo file defines a web search agent, a finance agent, an image generation agent, a research agent (using Exa) and a YouTube transcript agent. These can be grouped into a team and served from one playground. ([5:29](https://youtu.be/nkh7q8WU7oU?t=329))
- **Sessions and memory are stored in one local database file, so deleting that file erases conversation history.** — The speaker deletes the agents DB file and the earlier sessions disappear, then the database is recreated on the next run. This is the basis for the claim that all session data stays local. ([8:23](https://youtu.be/nkh7q8WU7oU?t=503))
- **Session logging is off by default and turned on with a flag.** — Setting log sessions to true makes the sessions appear in the sessions tab. The speaker says the default is off so the product does not track sessions. ([9:50](https://youtu.be/nkh7q8WU7oU?t=590))
- **The video suggests that local agents could get OS shell access and private data access, but does not demo either.** — The speaker mentions adding shell tools so an agent can control the operating system, and giving it private knowledge that should not leave the machine. These are stated as possibilities only. ([8:23](https://youtu.be/nkh7q8WU7oU?t=503))

## Techniques
- **Serve agents from a local server and attach a hosted chat UI** — Clone the Phidata repo and open the cookbooks/playground README. Create a virtualenv, export the API keys (the demo uses OpenAI and Exa, and Ollama can be swapped in), and install the requirements. Authenticate the Phidata app from the terminal and sign in, which registers the local endpoint. Export the phi debug variable as true to see logs (the captions say 'phi debug', likely PHI_DEBUG). Then run the demo.py playground server. It reports that it is serving on localhost:7777, and the Phidata app connects to that endpoint. *When:* When you want a hosted chat UI for agents that must keep tools, data and sessions on your own machine.
- **Define an agent with a description, tools and a current date** — Each agent is a normal agent definition with a description and a list of tools. The speaker gives the agent today's date and tells it how to format results in the prompt, then asks for a report. Tool calls and memory show up in the UI during the run. *When:* When you build small specialist agents (search, research, finance, transcript summarizing) to test through one playground.
- **Keep session history in a local DB file and reset by deleting it** — Point the agent's storage at a local database file (the speaker calls it an agents DB file). Sessions and memory are written there. Deleting the file and restarting recreates an empty database, which clears history. Leave session logging off unless you want the sessions tab populated. *When:* When you need inspectable, user-controlled session state for local agents and want an easy reset during development.
- **Turn on debug logs with an environment variable** — Export the debug variable (spoken as 'phi debug' as true) before starting the server to see logs. The speaker says you can also set debug mode on individual agents instead. *When:* When you need to see what the agent did behind the scenes during local development.

## Numbers
- Local playground server listens on localhost port 7777. ([5:29](https://youtu.be/nkh7q8WU7oU?t=329))
- Video length is 11:08. About 4 minutes (roughly 4:13 to 9:50) cover the local setup, and the rest is the hosted UI demo. ([4:13](https://youtu.be/nkh7q8WU7oU?t=253))
- Speaker's anecdote: a 30 to 50 minute YouTube video can be condensed into a roughly 10 second summary snippet. This is a personal claim with no measurement. ([6:55](https://youtu.be/nkh7q8WU7oU?t=415))

## Hot takes
- The privacy claim ('no information is sent to Phidata' beyond the endpoint) is the speaker's assertion. The video does not show network traffic to check it.
- Thin substance and product-led framing: most of the 11 minutes is UI praise ('looks absolutely beautiful') and demos of hosted agents, with little on agent design, evals or failure cases.
- The caption rendering of the product name varies ('FiData', 'PyData', 'Phi Data') and the speaker's name ('Ashreet Betty') is auto-caption noise. The product is Phidata.
- Some setup details are only partly visible in the captions (the exact authentication command, the exact debug variable name, and the session-logging flag), so reproduce them from the Phidata repo README rather than from this video.

## Tools mentioned
Phidata, Phidata agent UI / playground, OpenAI, Exa, DuckDuckGo search, Ollama, Python virtualenv

## Relevance to our work
- **agentos** (1/3): A local-first agent dev surface that keeps sessions in one local DB and gives an endpoint-registration model. Only a loose overlap with AgentOS's proxy and memory layers. → *Skim the Phidata cookbooks/playground README to compare its local session storage and endpoint registration with how MemoryMesh stores cross-session memory.*
