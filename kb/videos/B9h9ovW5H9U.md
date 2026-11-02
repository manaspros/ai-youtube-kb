# Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `B9h9ovW5H9U` · [watch](https://youtu.be/B9h9ovW5H9U) · **date:** 2026-06-18 · **length:** 20:12 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Zach Blumenfeld · **orgs:** Neo4j, Foundation Capital
- **topics:** memory, rag-retrieval, context-engineering, data-engineering · **tags:** context-graph, decision-traces, neo4j, knowledge-graph, graph-embeddings, hybrid-search, precedents, cypher, mcp, entity-extraction, gliner, spacy, pydantic-ai, agent-memory

> Neo4j's Zach Blumenfeld on context graphs: why agents need stored decision traces and precedents, not just documents, plus a one-line scaffold (create-context-graph) and the Neo4j agent memory pipeline.

## Summary
Zach Blumenfeld (Neo4j) argues that accurate agents need a context graph, a layer that holds entities, events (decisions, transactions, approvals) and the reasoning behind past decisions, on top of a plain knowledge base. He demos a financial-analyst style agent that uses hybrid search over decision traces, combining vector similarity on text with graph embeddings (GDS) of how past decisions were structured, to find precedents and recommend accept or reject with reasons. He introduces a uvx "create context graph" scaffold that generates a full-stack app (backend, frontend, Cypher retrieval, MCP server) from a chosen domain (22 built-in, including healthcare and FinServ) and agent framework, and it is open source but early. The underlying Neo4j agent memory package separates short-term (conversation), long-term (resolved entities) and reasoning (decision traces) memory, and extracts entities from raw text through a spaCy, then GLiNER, then LLM-fallback pipeline with merge and dedup. In Q&A he admits writing new decision traces back into the graph is still unsolved and that the approach is still rough.

## Key ideas
- **A knowledge base answers questions, but a context graph also records decisions and why they were made.** — Agents that only retrieve facts can say what the data is. Agents that decide need decision traces, precedents, causal chains and expected outcomes stored alongside entities and events. ([2:00](https://youtu.be/B9h9ovW5H9U?t=120))
- **Model the context graph as three node kinds: entities, events, and context.** — Entities are things that exist. Events are decisions, transactions and approvals. Context is the reasoning and memory, recorded by AI and by the humans who made past decisions. ([3:34](https://youtu.be/B9h9ovW5H9U?t=214))
- **Precedent search should combine semantic similarity with structural similarity in the graph.** — A vector index finds decision text similar to a query. Graph embeddings of how each decision connects to others let the system find past decisions with a similar causal shape, which plain document search would miss. ([7:04](https://youtu.be/B9h9ovW5H9U?t=424))
- **Graph embeddings work the same way as text embeddings.** — Node neighbourhoods are embedded into vectors (computed with GDS), so similar decision traces can be found by vector lookup, just as text chunks are. ([7:04](https://youtu.be/B9h9ovW5H9U?t=424))
- **Long-term memory comes from short-term conversation by extracting and resolving entities.** — Conversation history is short-term memory. Entities that recur are resolved into long-term memory. Reasoning traces are a third store, and all three are needed for a context graph. ([13:26](https://youtu.be/B9h9ovW5H9U?t=806))
- **Raw text is turned into graph entities with a staged pipeline.** — The package runs spaCy first, then GLiNER, then an LLM fallback for harder cases, followed by merging, deduplication and enrichment. Structured data can instead be mapped to Cypher directly. ([13:26](https://youtu.be/B9h9ovW5H9U?t=806))
- **Recording new decision traces is still an open problem.** — In the demo the agent only stores decisions when prompted. Writing traces back automatically, and scoring their quality, is unsolved. He suggests sentiment or quality scores. ([18:02](https://youtu.be/B9h9ovW5H9U?t=1082))

## Techniques
- **Hybrid precedent retrieval over decision traces** — Run vector search on decision text together with graph-embedding similarity over the structure of each decision's causal chain, then give the agent the matched precedents to base its accept or reject reasoning on. *When:* When an agent must justify a decision by pointing to how similar past cases were decided.
- **Scaffold a context-graph app from a domain** — Run one uvx command that names the app, domain (e.g. healthcare, FinServ, or custom), and agent framework. It generates a backend, frontend, Cypher retrieval, decision traces, an MCP server and multi-turn chat from demo fixtures. *When:* To get a working graph-backed agent prototype quickly, or to inspect how a domain ontology is turned into a schema.
- **Staged entity extraction from text into a graph** — Chain a fast NER (spaCy), then a stronger model (GLiNER), then an LLM fallback, and finish with merge, dedup and enrichment, so the cheap steps handle most text. *When:* When unstructured conversation or documents must become resolvable long-term entities at lower cost than LLM extraction alone.
- **Ontology-first graph schema generation** — Describe the domain and data to get a generated ontology, then use it to guide entity and relationship extraction. Pre-built domains come with predefined entity and relationship types. *When:* When starting a new domain and you want a schema before extraction.
- **Separate memory stores by kind** — Keep conversation history (short-term), resolved entities (long-term) and decision traces (reasoning) as distinct parts of one graph, linked to each other. *When:* When designing agent memory that must support both recall and reasoning about past decisions.

## Numbers
- 22 built-in domains in the scaffold (healthcare and FinServ shown) ([12:09](https://youtu.be/B9h9ovW5H9U?t=729))
- Scaffold works with many agent frameworks, including OpenAI, LangGraph, CrewAI, Strands and Google ADK ([12:09](https://youtu.be/B9h9ovW5H9U?t=729))
- The scaffold was released about a month before the talk ([8:04](https://youtu.be/B9h9ovW5H9U?t=484))
- About half the room had heard of context graphs; about half had coded with a graph database ([0:57](https://youtu.be/B9h9ovW5H9U?t=57))

## Hot takes
- Document search alone cannot capture the precedents that good decisions depend on; decision traces need to be first-class graph data.
- Graph embeddings of decision structure can find precedents that text similarity misses.

## Tools mentioned
Neo4j, Neo4j agent memory package, Graph Data Science (GDS), Cypher, uvx create-context-graph, Pydantic AI, Claude, OpenAI embeddings, Next.js, spaCy, GLiNER, MCP

## Relevance to our work
- **agentos** (2/3): MemoryMesh already plans hybrid retrieval and tiered cross-session memory; this talk's split of short-term, long-term and reasoning memory with a staged extraction pipeline maps directly onto that design. → *Read the Neo4j agent memory package code and compare its spaCy/GLiNER/LLM extraction staging and merge/dedup step with MemoryMesh's planned conflict-resolution and provenance layer.*
- **general** (2/3): The context-graph framing (decision traces plus precedent retrieval) and the open problem of writing traces back are a clear next reading topic for agent memory design. → *Read the Neo4j context-graph blog and the create-context-graph repo to see how traces are modelled and how the open write-back question is handled.*
- **prosharness** (1/3): Decision traces and precedents could record why a plan or critique was accepted across checkpointed runs, but the talk does not address coding agents.
