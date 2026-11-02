# Pinecone 2.0 — Edo Liberty, Pinecone

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `IN-rb-9WmiY` · [watch](https://youtu.be/IN-rb-9WmiY) · **date:** 2026-09-18 · **length:** 19:50 · **format:** talk · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Edo Liberty · **orgs:** Pinecone
- **topics:** memory, rag-retrieval, context-engineering · **tags:** knowledge layer, tribal knowledge, manifest, semantic map, runtime code generation, budgeted query, agent memory, Pinecone Nexus, product pitch

> Pinecone's Edo Liberty argues agents need a persistent, domain-owned company knowledge layer (Nexus) that goes beyond RAG, with query-time code generation and budgeted queries. Mostly a product pitch with vendor-reported numbers.

## Summary
Edo Liberty of Pinecone frames the problem as a theory-of-mind mismatch: agents are capable but start each session like a new hire with no knowledge of company tribal knowledge. He sorts knowledge into general (models already have it), private specific (RAG and vector search handle it), and tribal knowledge (not findable by search). He says a knowledge layer should be persistent, specialized and owned by domain experts, and kept current so deprecated facts are overridden quickly. His product Nexus is built from connectors, a manifest-driven "context" (semantic map, markdown, SQL tables, vector index, graph), and tasks (import, curate, search, and a budgeted query language). The most distinctive claim is that Nexus answers queries by generating and executing code, producing reusable programs rather than returning database results. He reports that tool-spec prompts shrink from about 150,000 tokens to under 1,000, and that early-access customers saw 77-90% token reduction and faster, more accurate answers. These results are vendor-reported and not backed by detail, and the talk ends with a launch push.

## Key ideas
- **Agents behave like new hires on day one every session, so they need a persistent company knowledge layer, not just a smarter model or more tools.** — The speaker treats the gap as a theory-of-mind mismatch: the agent does not know company goals, processes, or who owns what, and must re-read documents each time. ([3:51](https://youtu.be/IN-rb-9WmiY?t=231))
- **Knowledge comes in three kinds, and only the first two are solved by existing tools.** — General knowledge is in the model, private documents are handled by RAG and vector search, and tribal knowledge (how the company operates) cannot be retrieved from one document. ([2:27](https://youtu.be/IN-rb-9WmiY?t=147))
- **A knowledge layer must be persistent, specialized per domain with domain experts owning it, and continuously updated so that old facts are deprecated.** — The CEO example: after a change, the new name should become the overriding fact at once, even when thousands of older documents say otherwise. Plain RAG keeps returning the old answer. ([5:09](https://youtu.be/IN-rb-9WmiY?t=309))
- **The context is driven by a manifest: users declare the tasks, entities, and information they care about, and the system builds and maintains its own storage.** — The manifest replaces hand-written skills, plugins, and markdown files. Its contents are a semantic map plus markdown notes, SQL tables, a vector index, and graph entities and indexes, all maintained by the system. ([9:23](https://youtu.be/IN-rb-9WmiY?t=563))
- **Curate is the main write path: a new file or event is assimilated by consulting the manifest and semantic map, then updating tables, graph, and indexes.** — Import brings data in, curate updates the world model, and search wraps internal access so that agents do not need to know the storage layout. ([11:39](https://youtu.be/IN-rb-9WmiY?t=699))
- **Queries specify a budget (tokens or dollars, and time) so the agent can choose between a quick answer and an exhaustive search.** — Results are grounded, structured text for agents, not chat replies. The interface is an agentic tool, not a human chat UI. ([13:08](https://youtu.be/IN-rb-9WmiY?t=788))
- **Nexus answers queries by writing and running code at query time, and the code it produces is saved and can be rerun as a program.** — The speaker calls this a runtime coding agent. It works like a notebook: write code, run it, inspect the result, and rewrite the failing step. Answers come from code rather than a single database query, which he says makes them more flexible. ([15:39](https://youtu.be/IN-rb-9WmiY?t=939))
- **Replacing tool sprawl with a compact interface spec cuts prompt overhead dramatically.** — He reports going from about 150,000 tokens of tooling to under 1,000 tokens of interface specification. He says the agent without the layer is slower, more expensive, and less accurate. ([17:04](https://youtu.be/IN-rb-9WmiY?t=1024))

## Techniques
- **Manifest-declared knowledge base** — Write a manifest that lists the tasks, entities, and information a domain must track. The system then maintains its own semantic map, notes, tables, vector index, and graph from it, so no one hand-writes the storage. *When:* Shared company context used by many agents, where skills or markdown files are getting hard to maintain.
- **Curate-on-ingest** — On each new document or event, use the manifest and semantic map to decide which tables, graph edges, and indexes to update. Mark old facts as deprecated when new ones arrive. *When:* Information changes often and stale answers are costly, such as org charts, policies, or customer facts.
- **Budgeted agent queries** — Pass a token or dollar budget and a time limit with each query, and get back grounded, structured text the agent can parse. *When:* Agents need to trade off speed, cost, and accuracy per call instead of always getting the same depth of search.
- **Query-time code generation over a knowledge layer** — Let the engine write and execute code against the stored data to answer a question, then keep the working program so it can be rerun. *When:* Questions need multi-step logic that a single retrieval or SQL call cannot express, and the answer should be repeatable.
- **Compact interface spec in place of tool sprawl** — Expose only the few interfaces needed to query the knowledge layer, instead of giving the agent a large tool set to learn each time. *When:* The agent's prompt is filling up with tool definitions and it is spending time figuring out where data lives.

## Numbers
- Tooling prompt reduced from about 150,000 tokens to under 1,000 tokens for interface specs (vendor claim) ([17:04](https://youtu.be/IN-rb-9WmiY?t=1024))
- Token reduction of 77% to 90% commonly seen in early-access customers (vendor-reported, no methodology given) ([18:31](https://youtu.be/IN-rb-9WmiY?t=1111))
- Up to 20-30%, sometimes 77%, faster (vendor-reported) ([18:31](https://youtu.be/IN-rb-9WmiY?t=1111))
- Example of a stale-fact problem: 9,000 documents with an outdated fact spanning ten years ([6:32](https://youtu.be/IN-rb-9WmiY?t=392))

## Hot takes
- Agents need a separate persistent knowledge layer, and RAG alone will keep returning old facts after a change.
- Code generated at query time and saved as a rerunnable program beats a database query for flexibility.
- Giving agents many tools is a bigger cost than most people admit; a compact interface is enough.

## Tools mentioned
Pinecone Nexus, vector database, SQL tables, graph database, markdown notes

## Relevance to our work
- **agentos** (2/3): MemoryMesh already has tiered memory, GraphRAG, and conflict resolution with provenance. The manifest idea and budgeted queries map onto its retrieval layer. → *Add an optional token or dollar budget and time limit to the MemoryMesh retrieval call so the agent can choose between fast and exhaustive search, and measure the latency and accuracy trade-off with the existing RAGAS evals.*
- **prosharness** (1/3): Checkpoint and resume of long Claude Code runs could benefit from a declared list of what must persist, but the talk is about enterprise knowledge, not run state. → *Consider whether ProsHarness checkpoints could be built from a short manifest of tracked entities instead of free-form notes; low priority.*
- **general** (1/3): The talk gives a framework for why agents lose company context, which is useful background for context-engineering work. → *Read the transcript sections on manifest and curate if designing shared agent memory; no code change needed yet.*
