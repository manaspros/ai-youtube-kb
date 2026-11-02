# Why Bigger Context Windows Won't Save Your Agent — Elizabeth Fuentes Leone, AWS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `DrfyORO8RqA` · [watch](https://youtu.be/DrfyORO8RqA) · **date:** 2026-10-08 · **length:** 15:54 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Elizabeth Fuentes Leone · **orgs:** AWS
- **topics:** context-engineering, memory, agent-architecture · **tags:** context window, context engineering, memory pointer, externalize select isolate, Strands Agents, conversation manager, summarization, tool call limits, async tools, MCP, swarm, AWS API Gateway timeout

> AWS speaker on why larger context windows don't fix agents; she covers externalizing big tool output, summarizing and isolating context, loop caps and async tool calls, using Strands Agents.

## Summary
Elizabeth Fuentes Leone (AWS) argues that agents break when tools return large data, because the context window fills, the agent forgets material in the middle, and it starts to hallucinate. She frames the fix as context engineering with three moves: externalize big data to storage, select only what is relevant, and isolate context across agents, plus compressing it when needed. Her first example is conversation management in the Strands Agents framework, which offers sliding-window, summarization and combined strategies. For long-term use she suggests layering short-term history, a vector store and an entity graph. She then shows a memory-pointer pattern, where a tool saves large logs, returns an ID kept in agent state, and a second tool fetches the data only when needed. For multi-agent swarms she shares a pointer through invocation state rather than the full context. She closes with loop guards (per-tool call caps), async start/check tools for slow external APIs, and a list of anti-patterns such as content stuffing and lossy native summarization.

## Key ideas
- **Bigger context windows do not solve agent degradation** — She says that adding tokens was the old fix, but the agent still forgets the middle of a long context (she calls it the attention U-curve). Large tool output also overflows the window and can carry prompt-injection content. ([0:12](https://youtu.be/DrfyORO8RqA?t=12))
- **Three context strategies: externalize, select, isolate (plus compress)** — Externalize moves big data to persistent storage behind a pointer. Select retrieves only what is relevant. Compress summarizes or compacts. Isolate splits context across agents. ([3:07](https://youtu.be/DrfyORO8RqA?t=187))
- **Use a framework's conversation manager as the first step** — In Strands, one line sets up the agent loop. Sliding window keeps only recent messages. Summarization condenses older messages. The combined option summarizes old messages and keeps recent ones. ([4:34](https://youtu.be/DrfyORO8RqA?t=274))
- **Layer memory: short-term history, vector long-term memory, entity graph** — Short-term is the conversation history inside the window. Long-term lives in a vector database and is retrieved in new sessions. Relations between entities can go into a graph memory such as Neo4j. ([5:58](https://youtu.be/DrfyORO8RqA?t=358))
- **Memory pointer for large tool output** — A tool saves big logs to storage and returns an ID, which is kept in agent state. A second tool takes the ID and fetches the logs only when the agent needs them. The ID stays in the window in place of the data. ([8:50](https://youtu.be/DrfyORO8RqA?t=530))
- **Share large data across swarm agents by pointer, not by full context** — Sharing the whole context across agents adds noise. Instead, put the pointer in shared invocation state so each agent retrieves only what it needs. ([10:11](https://youtu.be/DrfyORO8RqA?t=611))
- **Cap tool calls and make tool responses clear to stop loops** — Agents can repeat the same tool forever when the response is unclear. A max-invocation count per tool (her example uses 3) ends the loop, and clear tool answers reduce the retries. ([11:12](https://youtu.be/DrfyORO8RqA?t=672))
- **Use async start/check tools for slow external APIs** — Synchronous MCP or API calls can block the agent and hit gateway timeouts such as AWS API Gateway's. She splits the work into a start-job tool and a check-status tool, and retrieves the result in a later invocation. She says her tests showed a large difference. ([12:36](https://youtu.be/DrfyORO8RqA?t=756))
- **Anti-patterns: content stuffing and lossy native summarization** — Do not put everything into the window. Native summarization can drop details the agent later needs. Context pollution from unneeded data should also be avoided. Pass only what the answer needs. ([14:04](https://youtu.be/DrfyORO8RqA?t=844))

## Techniques
- **Memory pointer for large tool output** — Tool A stores the large result in external storage and returns an ID held in agent state. Tool B takes the ID and fetches the data on demand. Only the ID stays in the context window. *When:* A tool returns logs, database rows or other large payloads that the agent only sometimes needs.
- **Summarizing conversation manager with a ratio and a keep-last-N** — Set a summary ratio (she uses 50%) and preserve the last N messages (she uses 4). Older messages are summarized on each invocation. Sliding window and the combined mode are the alternatives. *When:* Long single sessions where the window fills up but recent turns must stay verbatim.
- **Tiered memory: short-term, vector long-term, entity graph** — Keep recent history in the window. Store durable facts in a vector DB with typed memory prompts and retrieve them in new sessions. Store relationships in a graph and traverse it when needed. *When:* Agents that must remember across sessions and need relational recall.
- **Shared invocation-state pointer for multi-agent swarms** — Store the pointer ID in invocation state shared by the agents of a swarm. Each agent resolves the pointer only when it needs the data. *When:* Several agents need the same large data but not the full conversation.
- **Per-tool invocation cap** — Set a max call count per tool (her example is 3) so the loop ends even if the agent keeps calling the same tool. *When:* Agents that get stuck calling a tool with an unclear or empty result.
- **Async job start/check tool pair** — Expose a start-job tool that returns a job ID and a check-status tool. The agent does other work or ends the turn, then retrieves the result in a later invocation. She implements the tools with FastAPI behind MCP. *When:* External MCP servers or APIs are slow and can exceed gateway timeouts or block the agent.

## Numbers
- Summarization conversation manager example: summary ratio 50%, last 4 messages preserved ([5:58](https://youtu.be/DrfyORO8RqA?t=358))
- Per-tool invocation cap example: each tool may be called at most 3 times ([11:12](https://youtu.be/DrfyORO8RqA?t=672))
- Talk length 15:54; speaker said she had about nine minutes left at the 10:11 mark and cut content to fit ([10:11](https://youtu.be/DrfyORO8RqA?t=611))

## Hot takes
- Adding more tokens to the context window does not fix agent degradation.
- Sharing the full context across multi-agent swarms is like adding garbage to the other agents.
- Native summarization can drop details the agent needs, so it is risky for correctness.
- Synchronous calls to MCP or external APIs can make agents hang; async job tools are the safer default.

## Tools mentioned
Strands Agents, FastAPI, MCP, Neo4j, AWS API Gateway, Amazon Bedrock, Ollama, Gemini, Anthropic, OpenAI

## Relevance to our work
- **agentos** (2/3): MemoryMesh's tiered cross-session memory and tool-output handling match the memory-pointer and long-term-vector-plus-graph layers described here. → *Check whether MemoryMesh or the proxy path stores large tool results by reference with a fetch tool, and add a per-tool call cap to the agent loop.*
- **general** (2/3): The externalize, select, compress and isolate framing is a usable checklist for context engineering with subagents and CLAUDE.md-style context. → *Use externalize, select and isolate as a checklist when designing subagent context, and read the deck the speaker says she will share.*
- **prosharness** (1/3): Checkpoint/resume of long runs overlaps with async job handles, but the talk does not cover Claude Code CLI harnesses directly. → *Consider a per-tool call cap in ProsHarness loops so a repeated tool call cannot run forever.*
