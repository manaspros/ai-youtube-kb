# Why I’m Switching From Python to Docker Agent for AI Agents

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Mph1H5u3yeA` · [watch](https://youtu.be/Mph1H5u3yeA) · **date:** 2026-10-12 · **length:** 6:24 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andres · **orgs:** Better Stack, Docker, OpenAI, Anthropic, Google, OpenRouter, Kimi (Moonshot)
- **topics:** multi-agent, agent-architecture, mcp-and-tools · **tags:** docker-agent, a2a, yaml-agent-config, oci-registry, sub-agents, mcp, battleship-demo, docker-desktop, homebrew

> Better Stack walks through Docker Agent, an open-source Docker tool that defines agents in YAML, runs them with one command, and serves them over A2A. Demoed with an on-call incident and a Battleship match between two models.

## Summary
The speaker introduces Docker Agent, an open-source Docker tool for building and running AI agents, which he compares to what docker run is for containers. An agent is a YAML file naming a model, instructions and allowed tools, and Docker Agent runs the loop of calling the model, running tools and feeding results back. The model can point at OpenAI, Anthropic, Gemini, OpenRouter or a local model via Docker's model runner, and tools come from built-ins such as file access and shell plus any MCP server. He highlights three properties: agents as reviewable configuration, distribution through Docker Hub or any OCI registry, and running an agent as an HTTP API, MCP server or A2A server. The on-call demo splits a log-analyst agent (read-only file access to the logs folder) from an on-call assistant that has no file access and only knows the analyst's URL. The closing demo runs two player agents and a referee on separate ports, with the referee on a different model. Haiku wins Battleship in 34 shots at 50% accuracy, which the speaker explicitly says is not a benchmark.

## Key ideas
- **An agent is a declarative YAML file (model, instructions, tool sets) and Docker Agent runs the agent loop: call the model, run tools, feed results back, repeat until done.** — The speaker frames it as docker run for agents. Hand-written Python tool-calling loops are contrasted with the YAML version on screen, though the transcript shows no measurement of how much code is saved. ([0:00](https://youtu.be/Mph1H5u3yeA?t=0))
- **Agents become configuration that can be versioned, code-reviewed in pull requests, and swapped between models by changing one line.** — Model choice is a single config line; the speaker presents this as one of three main benefits. ([1:15](https://youtu.be/Mph1H5u3yeA?t=75))
- **Least-privilege multi-agent split: the team that owns the logs agent exposes it over A2A, and other agents query it without ever getting log access.** — The log analyst has a read-only file tool locked to the logs folder. The on-call assistant has no file access and only knows the analyst's URL. The on-call agent receives findings and writes the incident summary. ([3:35](https://youtu.be/Mph1H5u3yeA?t=215))
- **Any agent can be exposed as an HTTP API, an MCP server, or an A2A server with one command, so other agents connect by URL alone.** — The speaker calls this the third benefit and demos it with two terminals: one serving the analyst, one running the on-call assistant. ([2:24](https://youtu.be/Mph1H5u3yeA?t=144))
- **Agents can be distributed like container images: push to Docker Hub or any OCI registry and anyone runs them by image name.** — This is the second benefit. The speaker says it works the way containers are shared. ([1:15](https://youtu.be/Mph1H5u3yeA?t=75))
- **Multi-agent games use a separate referee agent on a different model so no player judges its own game.** — Two player agents (Haiku 5.5 and GPT-6 Luna as spoken) run on ports 8080 and 8081 over A2A. The referee runs on Kimi K3. The board runs on a local server, and each turn a player gets its view of the enemy waters, picks a square and adds trash talk. ([3:35](https://youtu.be/Mph1H5u3yeA?t=215))
- **The Battleship result is an anecdote, not a benchmark: Haiku wins in 34 shots at 50% accuracy, and both models clearly beat random play.** — The speaker explicitly declines to call it a benchmark. Luna had sunk all but one of Haiku's ships when the match ended. ([4:45](https://youtu.be/Mph1H5u3yeA?t=285))

## Techniques
- **Define an agent as a YAML file** — Declare the model (provider or a Docker model runner local model), instructions, and tool sets (built-in file and shell tools, or MCP servers) in one file. Optionally list sub-agents so a coordinator can hand off to specialists. Run the file with a single docker agent run command, which opens a terminal UI. The speaker's exact syntax is partly garbled in the captions, so verify against Docker's docs before copying. *When:* Replacing a hand-written Python tool-calling loop for a simple or medium-complexity agent where the agent should be reviewable as config.
- **Least-privilege agent split behind A2A** — Give the one agent that can read sensitive data (logs) read-only, path-scoped file tools. Give the front-door agent no file tools at all. Connect them by serving the data-owning agent over A2A on a port and giving the other agent only its URL. *When:* A team owns a data source and other teams' agents need answers but must not get direct access to the data.
- **Serve an agent as A2A on a port** — Run the serve subcommand with the A2A protocol, select the agent with the agent flag, and set the port (8080 in the demo). The consuming agent then gets that URL. The caption text for the exact subcommand is garbled, so check the docs. *When:* Exposing one agent to other agents or systems without writing server code.
- **Install Docker Agent** — On Docker Desktop 4.63 or newer it is preinstalled. Otherwise install it with Homebrew, then symlink the binary into the Docker CLI plugins folder so it runs as docker agent. *When:* Setting up a machine to try Docker Agent outside the default Desktop install.
- **Share an agent as an image** — Push the agent definition to Docker Hub or another OCI registry, then anyone runs it by image name with the run command. *When:* Distributing a reusable agent to a team or publicly, the way container images are shared.

## Numbers
- Battleship: Haiku won in 34 shots at 50% accuracy, a single-ship margin. ([4:45](https://youtu.be/Mph1H5u3yeA?t=285))
- Docker Agent is preinstalled on Docker Desktop 4.63 or newer. ([2:24](https://youtu.be/Mph1H5u3yeA?t=144))
- Player agents listen on ports 8080 and 8081, with the referee as a third agent. ([3:35](https://youtu.be/Mph1H5u3yeA?t=215))
- Video length is 6:24 and it is a single-speaker demo, with no benchmark or cost figures given. ([0:00](https://youtu.be/Mph1H5u3yeA?t=0))

## Hot takes
- Docker Agent makes multi-agent systems dramatically simpler than the Python-and-Hugging-Face route. The speaker shows no measurement; this is his impression.
- Agents as versioned, shareable OCI artifacts is the interesting idea, more than the YAML syntax.
- The speaker gives no tradeoffs, limitations or security notes for running agents as network services, and no cost or latency data.

## Tools mentioned
Docker Agent, Docker Desktop (4.63+), Docker model runner, Docker Hub, Homebrew, A2A protocol, MCP, Claude Haiku 5.5, GPT-6 Luna, Kimi K3, OpenAI, Anthropic, Gemini, OpenRouter

## Relevance to our work
- **agentos** (1/3): AgentOS is an opt-in proxy with a manifest; Docker Agent's YAML-config-plus-A2A pattern is adjacent but aimed at a different layer. → *Skim Docker Agent's A2A serving and agent-config format and compare it with AgentOS manifest toggles. Consider whether agents need a portable, versioned config artifact.*
- **prosharness** (1/3): ProsHarness wraps Claude Code CLI with checkpoint/resume and loops; Docker Agent is a separate YAML-defined loop runner, so the overlap is limited to config-as-code and sub-agent handoff. → *Skim how Docker Agent declares sub-agents and tool scoping in YAML, and compare it with ProsHarness's agent definitions.*
