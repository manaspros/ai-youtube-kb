# CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Q0VkgCyNVUg` · [watch](https://youtu.be/Q0VkgCyNVUg) · **date:** 2026-08-18 · **length:** 20:42 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Stephen Chin · **orgs:** Neo4j, Cognee, Agentic AI Foundation
- **topics:** memory, rag-retrieval, context-engineering · **tags:** graph-memory, knowledge-graph, neo4j, cypher, vector-vs-graph, graphrag, digital-twin, home-lab-demo, markdown-memory, openclaw, goose, hermes-agent, cognee, agent-memory

> Neo4j's Stephen Chin argues agent memory stored as markdown or vector lookups fails on multi-hop questions, and shows a live home-lab demo where a vector-seeded graph traversal beats a vector-only store.

## Summary
Stephen Chin (Neo4j developer relations) opens with a personal-assistant agent that forgets between days because its memory lives in markdown files. He says those files waste tokens: his average agents load about 100K tokens per round, much of it repetitive. Moving memory into an MCP server (Goose) or a vector database does not fix the core problem, because similarity search returns look-alike facts rather than the actual relationships. He proposes a hybrid: vector search finds seed nodes, then a graph traversal pulls neighbors and ranks them by relatedness, which makes answers explainable and auditable. In a live demo on an isolated home-lab digital twin, built from the same markdown source for both backends, the graph store gave precise answers to security questions where the vector store was vague, and it followed a router node to every exposed service. He notes that Claude can write the Cypher queries and entity extractors needed to start. The talk is partly a promotion for a Neo4j-backed memory product and a book, so the evidence is one small, hand-picked demo rather than a benchmark.

## Key ideas
- **Markdown memory files are easy to read and compact, but loading them into context is token-heavy and repetitive; the speaker's average agents load about 100K tokens per round.** — The fix he wants is retrieving only what the task needs, instead of loading everything in case it is useful. ([2:33](https://youtu.be/Q0VkgCyNVUg?t=153))
- **Moving memory behind an MCP server (Goose) is still plain files on disk; a forget command exposed as a tool is one wrong call from wiping memory.** — Pluggable memory does not solve picking the right memory or protecting it. ([5:58](https://youtu.be/Q0VkgCyNVUg?t=358))
- **Vector similarity is not the same as relationships. Vector-only lookup gives related-but-wrong facts and cannot handle multi-hop reasoning chains.** — He uses the 'wrong shell' analogy: look-alike results are the failure mode, and it gets worse with complex, domain-specific questions. ([7:25](https://youtu.be/Q0VkgCyNVUg?t=445))
- **Hybrid retrieval: vector search finds seed nodes, then graph traversal expands neighbors and ranks them by how related they are.** — The retrieved subgraph can be shown to a human, which makes the answer explainable and auditable. ([10:02](https://youtu.be/Q0VkgCyNVUg?t=602))
- **A graph is debuggable. When an answer is wrong you can inspect which nodes entered context, change extraction, and merge duplicate nodes.** — He says this lets you converge on a good answer quickly, which is hard to do with a similarity index. ([11:29](https://youtu.be/Q0VkgCyNVUg?t=689))
- **Non-experts can start: give Claude a basic data model and it can write Cypher and entity extractors.** — He built the digital twin over a week or two, with the agent writing each action into the graph as it worked. ([11:29](https://youtu.be/Q0VkgCyNVUg?t=689))
- **Demo design: one set of markdown source files feeds both a vector store (A) and a graph store (B), on an isolated VLAN so answers come only from memory and not live lookups.** — The comparison is same data, different store, five queued questions. ([12:54](https://youtu.be/Q0VkgCyNVUg?t=774))
- **In the demo, the graph store found the EOL OS on an exposed Minecraft server that the vector store missed, and it traversed from the pfSense router node to the exposed HAProxy and OpenVPN services.** — This is a single live run on the speaker's own lab, not a benchmark. ([16:21](https://youtu.be/Q0VkgCyNVUg?t=981))

## Techniques
- **Vector-seeded graph traversal** — Embed nodes and run a vector search to get seed nodes. Expand one hop (later multi-hop) with Cypher, rank neighbors by relatedness, and cap what enters context. *When:* Multi-hop questions where similarity search returns look-alikes that are not the actual related entities.
- **Graph as the agent's write target** — Have the agent write each action or fact into the graph while it works. Later answer by traversing the graph, not by rereading markdown. A fresh session queries the graph. *When:* Long-running personal or ops agents that need recall across sessions without loading whole memory files.
- **Inspect-and-fix retrieval loop** — Look at the subgraph that actually entered context (highlighted nodes), find the node responsible for a wrong answer, fix extraction, merge duplicate nodes, and rerun. *When:* Answers are wrong and you need to know which stored fact caused it.
- **Let the coding agent write the graph layer** — Give the agent the graph data model; let it write the Cypher queries and entity extractors. *When:* Starting with graph memory without graph expertise.
- **Same-source backend A/B test** — Build two memory stores from identical source files, ask the same fixed questions, and compare the answers side by side. *When:* Choosing between memory backends such as a vector store and a graph store.
- **Keep destructive memory tools away from the agent** — Do not expose forget or delete memory operations as tools the agent can call directly. *When:* Any agent with memory exposed through MCP tools.

## Numbers
- Average agents of the speaker load about 100K tokens of context per round, much of it repetitive. ([3:32](https://youtu.be/Q0VkgCyNVUg?t=212))
- Demo compares two stores built from the same source, with five queued questions; the lab is a three or four node home lab. ([12:54](https://youtu.be/Q0VkgCyNVUg?t=774))
- The digital twin was built over one to two weeks. ([11:29](https://youtu.be/Q0VkgCyNVUg?t=689))
- Speaker cites the one million token context window of modern models as the scale where markdown memory breaks down. ([17:30](https://youtu.be/Q0VkgCyNVUg?t=1050))

## Hot takes
- Storing agent memory as markdown files does not scale past small agents.
- Vector similarity alone produces hallucinations and related-but-wrong facts, so graph relationships are needed.
- Graph-based memory is more explainable and auditable than vector retrieval.
- A forget or delete memory tool exposed to the agent is dangerous.

## Tools mentioned
Neo4j, Cypher, Cognee, OpenClaw, Goose, Hermes Agent, pgvector, LanceDB, Claude, Proxmox, pfSense, HAProxy, OpenVPN, MCP

## Relevance to our work
- **agentos** (2/3): MemoryMesh already has hybrid BM25 plus pgvector retrieval and GraphRAG; the talk gives a concrete seed-then-traverse pattern and an auditability angle that fits the L2A design and its Neo4j storage. → *Prototype a one-hop Neo4j expansion after pgvector seeding in MemoryMesh retrieval, and log which nodes entered the context window so each answer can be audited. Compare it to vector-only on a small set of multi-hop questions.*
- **prosharness** (1/3): Checkpointed runs carry state across sessions, and the talk's point about per-round token cost from markdown memory is relevant to how ProsHarness restores context. → *Before adding cross-session memory to checkpoint/resume, measure how many tokens a resumed round loads from existing state files, to check whether the talk's token-cost concern applies.*
