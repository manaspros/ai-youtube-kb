# I Built a Personal AI Agent on a Raspberry Pi — Jeremy Adams, Neo4j

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `oUZEt4EiPbk` · [watch](https://youtu.be/oUZEt4EiPbk) · **date:** 2026-10-04 · **length:** 20:10 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Jeremy Adams · **orgs:** Neo4j, Anthropic
- **topics:** memory, agent-architecture, mcp-and-tools, sandboxing-execution · **tags:** raspberry-pi, edge-agent, personal-agent, nanoclaw, whatsapp-channel, neo4j, graph-memory, pole-plus-o, mcp, offline-first, docker-isolation, cypher, conference-demo

> Neo4j's Jeremy Adams builds a personal agent on a Raspberry Pi 4B: NanoClaw in Docker, WhatsApp as the channel, cloud LLMs, and graph memory, with a live demo and an offline capture mode for conference Wi-Fi.

## Summary
The speaker built a personal agent on a Raspberry Pi 4B. He chose NanoClaw over OpenClaw because it is small (about 15 source files) and runs each agent process in a Docker container. The Pi does no LLM inference; it receives WhatsApp messages and calls Claude-based cloud services. He connected a cloud Neo4j database to the agent through an MCP server, so chat questions such as which movies an actor appeared in are answered by running graph queries. For memory he used the POLE+O entity schema (person, object, location, event, organization), written as an agent skill on a persistent mount. For a conference booth-mapping task he added an offline mode: a local Neo4j on the Pi, plus regex parsing of voice-transcribed booth numbers into Cypher inserts, synced to the cloud later. He then loaded his full WhatsApp history into Neo4j's agent memory service, which distilled it into memories that the agent reaches over MCP. The talk is mostly a live hardware demo with a Neo4j product plug at the end, so the reusable material is the architecture pattern rather than measured results.

## Key ideas
- **Keep the personal agent small, cheap and hackable rather than feature-rich** — The speaker is a conservative sysadmin/DevOps person. He preferred a cheap, open, understandable box to a laptop-resident agent, and noted the Mac mini price he cited has since risen. ([6:07](https://youtu.be/oUZEt4EiPbk?t=367))
- **Pick a compact agent framework that isolates each agent process in a container** — He chose NanoClaw over OpenClaw because it has about 15 source files and uses Docker containers so agent processes cannot run arbitrary commands on the host. It is built on the Claude Agent SDK and is meant to be modified with Claude Code. ([7:29](https://youtu.be/oUZEt4EiPbk?t=449))
- **Split the device from the brain: the Pi only handles I/O and orchestration** — WhatsApp messages reach the Pi, which runs the agent. All LLM inference runs in the cloud, so the small board needs no model capacity. The speaker calls this a big brain reached over a wire. ([8:27](https://youtu.be/oUZEt4EiPbk?t=507))
- **Expose the graph database to the agent as a tool through MCP** — A chat question such as which movies Tom Hanks acted in goes through an MCP server to Neo4j, and the results are sent back through the messaging channel. He also had to fix auth before it worked. ([9:38](https://youtu.be/oUZEt4EiPbk?t=578))
- **Use a typed entity schema for memory and write it as an agent skill** — He used POLE+O (person, object, location, event, organization), a schema from policing graph work, and asked the agent to build the memory system as a skill on a mount that survives reboots. Memory nodes record places, events and people, linked into one graph. ([11:03](https://youtu.be/oUZEt4EiPbk?t=663))
- **Capture offline and sync later, with a deterministic parser at the edge** — For conference Wi-Fi he ran a local Neo4j on the Pi. Voice-to-text output is parsed with regexes for booth numbers and turned into Cypher inserts. Raw notes are later uploaded and enriched in the cloud database. ([13:32](https://youtu.be/oUZEt4EiPbk?t=812))
- **Graph structure can show themes that were not stored explicitly** — Linking exhibitors to shared theme nodes surfaced clusters such as evaluation and observability. The speaker presents this as knowledge that may be new, though it is an informal observation with no measurement. ([17:00](https://youtu.be/oUZEt4EiPbk?t=1020))
- **Distill long chat histories into memories and expose them over MCP** — He loaded his full WhatsApp history into Neo4j's agent memory service. It produced memories about conversations, people, locations and concepts, which the agent can browse through MCP. ([18:25](https://youtu.be/oUZEt4EiPbk?t=1105))

## Techniques
- **Edge orchestrator, cloud brain** — Run the agent runtime and message channel on a small device and send every model call to a hosted API. The device holds no model weights or GPU. *When:* Low-power hardware or a personal agent where local inference is unnecessary.
- **Container per agent process** — Run each agent process inside a Docker container so it cannot execute commands on the host, and use a compact framework that is easy to read and change. *When:* Running an agent on personal or shared hardware where you want containment without a large framework.
- **Messaging app as the agent front end** — Use WhatsApp or Telegram as the chat channel and route messages to the agent on the device. *When:* You want to reach the agent from a phone with no custom UI.
- **Graph database as an MCP tool** — Wrap a graph database in an MCP server so the agent can run queries as tool calls, then return the results in chat. *When:* The answer lives in connected data, such as entities and relationships.
- **Offline-first capture with deterministic parsing and later sync** — Keep a local database on the device. Use regexes to parse speech-to-text output into structured inserts when there is no network. Upload and enrich the records when the connection returns. *When:* Unreliable network, such as a conference venue, where data is captured on the spot.
- **Typed entity memory schema written as a skill** — Define memory nodes by entity type (person, object, location, event, organization) and let the agent create its own memory layer as a skill stored on a persistent mount. *When:* Personal or cross-session memory where entities and their links matter more than free text.
- **Batch distillation of chat history** — Load an archive of past conversations into a memory service that extracts memories, then expose the result to the agent through MCP. *When:* You have a long conversation history and want searchable, distilled memories rather than raw logs.

## Numbers
- NanoClaw is about 15 source files, which the speaker cites as the reason he chose it over OpenClaw ([7:29](https://youtu.be/oUZEt4EiPbk?t=449))
- Hardware is a Raspberry Pi 4B, first run on a 32-bit OS and later moved to 64-bit ARM ([4:43](https://youtu.be/oUZEt4EiPbk?t=283))
- The Mac mini price the speaker cited was about $600 before recent price increases, which he said no longer holds ([6:07](https://youtu.be/oUZEt4EiPbk?t=367))
- Talk length is 20:10 ([0:00](https://youtu.be/oUZEt4EiPbk?t=0))

## Hot takes
- A personal agent on a laptop is too much exposure for someone who wants to understand what it does; a cheap, hackable box is the better start.
- The Pi should hold no model: keep all inference in the cloud and use the device only for channels and orchestration.
- Conference Wi-Fi is bad enough that an offline capture mode is worth building.

## Tools mentioned
Raspberry Pi 4B, NanoClaw, OpenClaw, Claude Agent SDK, WhatsApp, Telegram, Docker, Neo4j, Neo4j Aura, Cypher, MCP, Neo4j agent memory service, POLE+O schema, Obsidian, USB microphone

## Relevance to our work
- **agentos** (1/3): The talk's POLE+O entity schema and graph memory overlap with MemoryMesh's graph layer, but it is a personal demo with no measured retrieval results. → *Try one entity-typed preset (person, location, event, organization) for MemoryMesh's graph layer and compare entity-based recall against the current BM25 plus pgvector retrieval on a small personal chat history.*
- **prosharness** (1/3): A chat app as the control channel for a containerized agent matches ProsHarness's phone-driven approvals. The talk shows no approval flow or credential handling. → *Compare the per-process container isolation and messaging-channel control described in the talk against ProsHarness's phone approval path, and check whether it can cover the zero-token credential handling.*
- **general** (1/3): Offline-first capture with a regex parser and later sync is a small reusable pattern, but nothing is measured. → *Read the NanoClaw source (about 15 files) to see how the container and channel setup is structured before copying any of it.*
