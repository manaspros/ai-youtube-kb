# Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `vJukHCIv7Ck` · [watch](https://youtu.be/vJukHCIv7Ck) · **date:** 2026-07-18 · **length:** 55:19 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Elizabeth Fuentes · **orgs:** AWS, Strands Agents, Neo4j, OpenAI
- **topics:** mcp-and-tools, rag-retrieval, security-guardrails, multi-agent · **tags:** hallucination, semantic-tool-selection, tool-schema-tokens, graphrag, text-to-cypher, neo4j, multi-agent-validation, swarm, hooks, guardrails, steering, agent-control, strands, agentcore, live-demo

> AWS developer advocate walks through five code-level techniques to reduce agent hallucinations: semantic tool selection, GraphRAG for aggregation, multi-agent validation, code-enforced hooks, and steering rules. Demos use dummy tools.

## Summary
The speaker argues that many agent hallucinations come from what goes into the context window: every tool schema is sent on every call, vector search returns top chunks even when nothing fits, and prompt rules are only suggestions. She shows five fixes built with the Strands Agents framework and OpenAI: filter tools per query with a vector index, answer aggregation questions with a Neo4j graph and generated Cypher, add an executor/validator/critic chain, enforce hard rules in before-tool hooks, and use a steering library to let the agent adjust instead of failing. The demos are small and self-described as not production-ready. The tool-selection test uses 90 labelled queries over 29 dummy tools, but the talk reports no clean accuracy table, and the token figures are inconsistent in the auto-captions. The GraphRAG comparison uses only two or three hotels, so it is a weak test of the scaling claim. The closing section pitches Amazon Bedrock AgentCore (Gateway, Runtime, Policy, DynamoDB-backed rules) as the production path.

## Key ideas
- **Tool schemas are paid for on every call** — The speaker says each tool schema costs roughly 100-200 tokens, so 29 tools add about 3,000 tokens to every request even when the model uses none of them. Conversation history makes this grow with every turn. ([3:35](https://youtu.be/vJukHCIv7Ck?t=215))
- **Filter tools per query with a vector index** — Embed each tool's name and description into a local vector store. For each user query, retrieve the top 3 tools and send only those to the model. The index is built once and queried on every request. ([6:01](https://youtu.be/vJukHCIv7Ck?t=361))
- **In multi-turn chats, swap tools in and out of agent state each turn** — Keeping semantic selection in a conversation means the old tools must be cleared and the new ones added on each invocation. Strands exposes the tool registry in the agent loop, so this takes a few lines. Token use still rises each turn because chat history is resent. ([13:40](https://youtu.be/vJukHCIv7Ck?t=820))
- **Vector RAG cannot count or aggregate** — Top-k chunk retrieval always returns something, even when nothing is relevant. For questions like average rating across all Paris hotels, or how many hotels have a pool, the model only sees a few chunks and estimates. The speaker presents this as the main failure mode. ([18:36](https://youtu.be/vJukHCIv7Ck?t=1116))
- **Generate a graph query and let the database compute the answer** — Build a knowledge graph from raw text using Neo4j's LLM graph builder. The model writes a Cypher query, and the database runs it over all the data and returns a computed result. Zero matches can be reported honestly, as in the Antarctica example. ([20:05](https://youtu.be/vJukHCIv7Ck?t=1205))
- **A single agent hides tool errors and reports success** — In the single-agent demo the tool returned an error and the agent still confirmed the booking. A Strands Swarm of three agents (executor, validator, critic) catches the error and the critic rejects the result. The user sees a clear failure instead of a false success. ([29:28](https://youtu.be/vJukHCIv7Ck?t=1768))
- **Prompt rules are suggestions; code rules cannot be skipped** — A system-prompt rule like max 10 guests per booking was ignored. The same rule as a before-tool-call hook in Python checks the parameters and cancels the call. Hooks cover hard constraints: date order, max guests, payment before confirmation. ([34:00](https://youtu.be/vJukHCIv7Ck?t=2040))
- **Steer instead of block for soft rules** — A hard block forces a retry. For soft constraints, a steering rule returns guidance so the agent can adjust, for example splitting a 50-guest booking across rooms. Rules live on a local server and change without a code redeploy. The speaker's split-booking example is the only evidence shown, so it is not benchmarked. ([42:52](https://youtu.be/vJukHCIv7Ck?t=2572))

## Techniques
- **Semantic tool selection** — Index tool name and description with an embedding model (she uses sentence-transformers locally, a file store). Per query, retrieve top-k tools (k=3 in the demo) and pass only those to the model. Keep a labelled query-to-correct-tool set to measure accuracy. *When:* Agents with many tools (she uses 29) where per-call schema tokens dominate cost. Watch for similar tool names, which the speaker says caused some misses.
- **Per-turn tool swap in agent loop** — In each invocation, clear the agent's tool registry and add only the tools retrieved for the current message. Chat history stays in the agent state. *When:* Multi-turn conversations where semantic selection must persist across turns without the full tool list building up.
- **Text-to-Cypher GraphRAG for aggregation** — Build a knowledge graph from documents (Neo4j's library uses an LLM to extract entities and relations). Give the model a single tool that takes a question, writes a Cypher query, runs it, and returns the rows. The model phrases the answer from computed results. *When:* Count, average, or multi-hop questions over a whole dataset where top-k chunks would only sample it.
- **Executor, validator, critic swarm** — Define three agents in a Strands Swarm with short system prompts: executor calls tools, validator checks what was done, critic approves or rejects. The swarm manages handoffs and the entry point is the executor. Cap handoffs (she sets six). *When:* Actions with side effects, such as bookings, where a tool error must not turn into a confident success message.
- **Before-tool-call hooks for hard rules** — Register a hook on the before-tool event in Strands. Check parameters against rules (guest limit, payment verified before confirmation, date order) and cancel the call on failure. Use the after-tool event where needed. *When:* Hard constraints where a violation must never run, regardless of what the model decides.
- **Steering rules for soft constraints** — Use the open-source agent-control SDK and a local server. Rules return steering guidance, so the agent can adapt and finish the task. Update rules through the server API without changing agent code. *When:* Soft policies where the goal is still reachable with an alternative, such as splitting a large booking. Also useful when rules change often and should not need a redeploy.

## Numbers
- Travel agent has 29 tools; about 3,000 tokens of tool schema sent on every call (speaker's estimate, roughly 100-200 tokens per tool) ([5:00](https://youtu.be/vJukHCIv7Ck?t=300))
- Test set: 90 queries against 29 tools with ground-truth best tool per query ([9:38](https://youtu.be/vJukHCIv7Ck?t=578))
- Baseline all-tools agent: about 2,000 tokens per single-question query; speaker also says the average is about 1,000 (inconsistent in the transcript) ([10:50](https://youtu.be/vJukHCIv7Ck?t=650))
- Semantic selection shows the model 3 tools per query instead of 29 ([6:01](https://youtu.be/vJukHCIv7Ck?t=361))
- Tool-selection accuracy: speaker says the all-tools baseline sometimes picks the wrong tool, and the filtered version improves accuracy, but no precise percentages are given ([14:43](https://youtu.be/vJukHCIv7Ck?t=883))
- Graph demo: average guest rating across Paris hotels computed as about 4.7 (auto-caption '47') from only 2 hotels, so the RAG comparison is not a scale test ([23:50](https://youtu.be/vJukHCIv7Ck?t=1430))
- Guardrail demo: max 10 guests per booking; a 50-guest request is blocked by the hook ([36:02](https://youtu.be/vJukHCIv7Ck?t=2162))
- Steering demo: 50-guest Lisbon booking is split into two rooms instead of failing ([47:05](https://youtu.be/vJukHCIv7Ck?t=2825))

## Hot takes
- Prompt rules are suggestions to the model; only code executes, so hard constraints belong in hooks.
- Vector RAG should not be used for counting or aggregation questions over a full dataset.
- A second agent acting as validator or critic is a practical fix for agents that report false success.

## Tools mentioned
Strands Agents, OpenAI API, sentence-transformers, Neo4j (Cypher, LLM graph builder), agent-control (steering SDK), Amazon Bedrock AgentCore (Gateway, Runtime, Policy, Memory), DynamoDB, Neo4j AuraDB, AWS Lambda, Ollama (mentioned)

## Relevance to our work
- **agentos** (2/3): Per-request tool filtering and code-enforced guardrails map onto the L1 gateway and the L2C Crucible exec-gate. The graph-for-aggregation point bears on MemoryMesh retrieval, but the evidence here is only a demo.
- **prosharness** (2/3): ProsHarness wraps Claude Code, which has PreToolUse-style hooks. Putting hard budget and approval rules in hooks instead of CLAUDE.md matches the talk's core point. The steering idea could fit the plan/critique loop. → *Audit ProsHarness's pre-tool path and move any hard rule that lives only in prompts (for example spend limits or approval gates) into a hook that can cancel the call.*
- **general** (2/3): The labelled query-to-correct-tool evaluation and the executor/validator/critic check are reusable patterns for testing any agent. The speaker gives no accuracy numbers, so the evidence is thin. → *Borrow the 90-query ground-truth approach to test tool selection in any agent project, and add a critic pass to write-heavy agent flows.*
