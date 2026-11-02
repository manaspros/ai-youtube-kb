# RAG Needs a Map: Using GraphRAG to Retrieve Connected Context — Nyah Macklin, Neo4j

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `LJ2a9nX3vlo` · [watch](https://youtu.be/LJ2a9nX3vlo) · **date:** 2026-10-11 · **length:** 52:59 · **format:** workshop · **quality:** 2/5 · **depth:** intro
- **speakers:** Nyah Macklin, Jeremy Adams-Castanias, Ryan Knight, Zach · **orgs:** Neo4j
- **topics:** rag-retrieval, data-engineering, context-engineering · **tags:** graphrag, neo4j, knowledge-graph, text-to-cypher, vector-search, hybrid-retrieval, aura-agents, entity-extraction, schema-design, graphacademy

> Neo4j workshop on GraphRAG: when vector RAG falls short (3+ hops, cross-document aggregation), how an LLM can build a knowledge graph, and how to pair vector search with Cypher in a Neo4j Aura agent.

## Summary
The talk is a hands-on GraphRAG 101 workshop from Neo4j, run with GraphAcademy course material. The speaker argues that vector-only RAG is enough for search-style questions, but that questions needing 3 or more hops, or aggregation across documents, benefit from a knowledge graph in the retrieval path. The recommended setup uses both graph and vector retrieval, not graph alone. The pipeline is: gather text, chunk it, embed the chunks, have an LLM extract entities and relationships as JSON, then load them into a graph. The speaker suggests using an LLM to propose a schema and then constraining extraction to it. The workshop then builds a Neo4j Aura agent with a vector-search tool (top 5 chunks, returning connected graph data) and a text-to-Cypher tool. A counting question exposed duplicate nodes left by re-running the builder, which the speaker fixed by checking counts directly in Cypher. Much of the runtime is setup and logistics, and the talk is promotional for Neo4j's free courses.

## Key ideas
- **GraphRAG is standard RAG where the retrieval path also goes through a knowledge graph.** — Plain RAG chunks documents, embeds them, retrieves top-K and passes them to an LLM. GraphRAG adds a graph store to that same retrieval path. ([11:45](https://youtu.be/LJ2a9nX3vlo?t=705))
- **Use vector RAG for search-style questions. Use a graph when the question needs 3+ hops or joins facts across documents.** — Examples the speaker gives for graph need: source-code analysis, supply-chain questions, and anything needing aggregation or concatenation across documents. He says the goal is both graph and vector together, not a replacement. ([12:44](https://youtu.be/LJ2a9nX3vlo?t=764))
- **Explainability is the main reason to use a graph: you can trace the hops the agent took.** — Nodes and relationships make it possible to show how an answer was reached. The speaker ties this to regulated domains such as finance, medicine and law, where agent decisions must be auditable. ([10:58](https://youtu.be/LJ2a9nX3vlo?t=658))
- **Knowledge graphs are both human-readable and machine-readable.** — A graph of an apple can say it comes from a tree, is round, is red, and is a fruit. The speaker presents this as a fix for the black-box problem of embeddings, which are not readable by people. ([7:15](https://youtu.be/LJ2a9nX3vlo?t=435))
- **Graph construction is an LLM extraction pipeline: chunk, embed, extract JSON, load.** — Gather text, split it into chunks, embed the chunks, prompt an LLM to return entities and relationships as JSON, parse the output, and write it to the graph. The speaker says the LLM is faster than manual extraction. ([19:56](https://youtu.be/LJ2a9nX3vlo?t=1196))
- **Derive the schema first, then pin it in extraction so the LLM does not invent node or relationship types.** — For a new document set, the speaker suggests asking an LLM to propose node and relationship types, then passing that schema into the builder's prompt so extraction stays on it. ([49:28](https://youtu.be/LJ2a9nX3vlo?t=2968))
- **A graph-backed agent can answer counting questions that vector RAG usually gets wrong, but only if the graph is clean.** — The agent could count lessons, but after the builder was re-run without clearing data, it returned 30 instead of 15. A direct Cypher query gave the correct count. The speaker presents this as a deduplication pitfall. ([45:26](https://youtu.be/LJ2a9nX3vlo?t=2726))

## Techniques
- **Hybrid vector-plus-Cypher retrieval tool** — Create a vector index on chunk embeddings. The tool runs a similarity search (top 5 in the demo) and then a Cypher query that walks from the matched chunks to connected nodes, returning nodes and similarity scores together. *When:* When the answer needs both semantic match on text and the connected context around it, such as related entities, prior events or historical links.
- **Text-to-Cypher tool beside the search tool** — Give the agent a natural-language-to-Cypher tool as a second tool, so it can write its own graph queries for structured questions. *When:* For aggregation, counting, or list questions that similarity search answers poorly.
- **Schema-pinned LLM entity extraction** — Ask an LLM to propose node and relationship types from sample documents. Then put that schema in the extraction prompt, so output is limited to those types and output is parsed as JSON before loading. *When:* When building a graph from a new document corpus and you need consistent types across many chunks.
- **Chunk, embed, extract, load pipeline** — Use a fixed-size splitter (the demo uses a chunk size of 500 with some overlap) with a simple KG pipeline class from the GraphRAG for Python package. Each chunk goes through the embedder and the LLM extractor, then the driver writes nodes and relationships. *When:* As a baseline builder for a document-to-graph pipeline, before tuning chunking or the schema.
- **Direct Cypher audit after each rebuild** — After re-running a graph builder, run a count query (for example, counting lesson nodes) in Cypher and check it against the source. Use MATCH p=() -- () to visually inspect what was ingested. *When:* Whenever a graph builder is re-run or appends to an existing database, to catch duplicated nodes before the agent reports them.
- **Grounding instruction to restrict the agent to graph content** — Write an agent instruction that tells it to answer only from knowledge graph content, and enable the internal tool option so no external source is used. *When:* When the agent should answer from a specific corpus and not from the model's general knowledge.

## Numbers
- Multi-hop threshold: graph RAG becomes needed when a question takes at least three hops. ([12:44](https://youtu.be/LJ2a9nX3vlo?t=764))
- Retrieval setup in the demo: top 5 results, text-embedding-3-small embeddings with 1536 dimensions, vector index on chunk embeddings. ([41:19](https://youtu.be/LJ2a9nX3vlo?t=2479))
- Chunking in the builder: fixed-size splitter with chunk size 500 and a chunk overlap, values not given in the talk. ([48:25](https://youtu.be/LJ2a9nX3vlo?t=2905))
- Lesson count from the agent: 30 after re-running the builder without clearing, versus the correct 15 from a direct Cypher count. ([46:16](https://youtu.be/LJ2a9nX3vlo?t=2776))

## Hot takes
- Vector-only RAG is sufficient for search-engine-style questions, and graph RAG becomes necessary at about three hops or cross-document aggregation.
- Graph RAG should be added alongside a vector layer, not used to replace it.
- Graph-based agent memory and graph traces are the main answer to explainability in regulated domains such as finance, medicine and law.
- Much of the workshop is setup and sign-up for a vendor's free courses, so it is more promotional than technical.

## Tools mentioned
Neo4j, Neo4j Aura (free instance), Aura Agents, GraphAcademy, GraphRAG for Python (neo4j-graphrag), OpenAI (LLM and text-embedding-3-small), Cypher, GitHub Codespaces, VS Code

## Relevance to our work
- **agentos** (2/3): AgentOS MemoryMesh already plans GraphRAG and hybrid retrieval (BM25 + pgvector). This talk gives a concrete hop threshold and a vector-plus-Cypher tool pattern that can be compared against that design. It also shows the duplicate-node problem that appears after rebuilds. → *Benchmark MemoryMesh on one 3+ hop question and one counting question against vector-only retrieval. Add a count check after every graph rebuild to catch duplicate entities.*
