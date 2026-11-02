# A Practitioner's Guide to Graphs - Tim Ainge, Good Collective

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `3ySF0I5iE_0` · [watch](https://youtu.be/3ySF0I5iE_0) · **date:** 2026-08-18 · **length:** 14:18 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Tim Ainge · **orgs:** Good Collective
- **topics:** rag-retrieval, data-engineering, context-engineering · **tags:** knowledge-graph, graph-rag, personalized-pagerank, subgraph-matching, shortest-path, schema-extraction, entity-resolution, ontology, code-search, cypher

> Tim Ainge (Good Collective) on when graphs help AI apps: schema-first graph extraction, entity matching, and graph-native retrieval (personalized PageRank, shortest paths, subgraph pattern matching) for cheaper, more reliable results.

## Summary
The speaker argues that graphs often disappoint when teams rush into GraphRAG or a graph database, and that the payoff depends on building the graph carefully. He starts with the basics of nodes, edges, labels and direction. He then recommends extracting graphs from text against an explicit schema (recipe, ingredients, steps, techniques) rather than generic subject-predicate-object triples, and adds ontology rules such as normalised names and metric units. Entity matching is best done with embeddings before new nodes are created, so that duplicates collapse without needing every entity known in advance. On the query side, he covers multi-hop traversal (simpler than deep SQL joins), personalized PageRank for ranking nodes near a seed (citing Pinterest's PixieRank and HippoRAG), and shortest-path variants for explaining how two known nodes relate. He closes with subgraph pattern matching, which finds code or legal structures by shape without knowing names. The main evidence is a 40% cut in tool calls for code search on the eShop .NET codebase. The talk deliberately skips GraphRAG and agent memory graphs.

## Key ideas
- **Graphs are often the wrong tool, and many projects stall after an early letdown.** — The speaker opens by saying a graph is not always the right answer, and that teams who rush into GraphRAG or a graph DB often see no quick payoff. He frames getting past that as the real challenge. ([0:00](https://youtu.be/3ySF0I5iE_0?t=0))
- **Give the extractor a schema, not generic triples.** — Generic subject-predicate-object triples produce messy, hard-to-query graphs. Defining typed nodes and edges (recipe -> ingredients -> steps -> techniques) and using structured outputs makes relationships consistent and queryable. ([2:33](https://youtu.be/3ySF0I5iE_0?t=153))
- **Ontology rules matter as much as the schema.** — Extra instructions such as lowercase ingredient names and metric units standardise values so that matching and conversion work later. He says these rules are as important as the schema itself. ([4:40](https://youtu.be/3ySF0I5iE_0?t=280))
- **Resolve entities with embeddings before creating new nodes.** — Retrospective string-based dedup needs all entities known in advance. Embedding-based matching handles variants such as garlic cloves vs minced garlic without a fixed list, and he calls this a hybrid of graph and AI techniques. ([6:12](https://youtu.be/3ySF0I5iE_0?t=372))
- **Multi-hop traversal is where graph queries beat SQL.** — Finding recipes with garlic is a simple query, but the SQL equivalent grows quickly as you traverse 5, 10 or 20 edges. Graph query languages make deep traversal easier to write and run. ([7:10](https://youtu.be/3ySF0I5iE_0?t=430))
- **Personalized PageRank surfaces nodes near a seed.** — A random walker with teleports back to the start node marks nodes as it goes. Nodes with the most marks are the ones most strongly related to the starting point. It is most useful in dense clusters where importance is not obvious. ([8:14](https://youtu.be/3ySF0I5iE_0?t=494))
- **Shortest-path variants explain how two known nodes relate.** — When both endpoints are known but the link is not, k-shortest, through-a-node, or weighted cheapest paths return the intermediate nodes. Those nodes can then go to the agent as a subgraph of context, which vector search would not have found. ([9:46](https://youtu.be/3ySF0I5iE_0?t=586))
- **Subgraph pattern matching finds code by its shape.** — Querying for a structure, such as a class that wraps another class and both implement the same interface (a decorator), finds matches without knowing any names. He calls this an enabling capability rather than an optimisation, useful for anti-patterns, security issues or legal argument patterns. ([10:42](https://youtu.be/3ySF0I5iE_0?t=642))

## Techniques
- **Schema-constrained graph extraction** — Define typed node and edge classes (for example recipe, ingredient with quantity, step, technique) and use the LLM's structured-output mode to fill them, rather than free-form triples. *When:* Any time unstructured text must become a graph that will later be queried or traversed.
- **Ontology normalisation instructions** — Add explicit extraction rules next to the schema, such as lowercase names and a single unit system, so values match across documents. *When:* When the same entity or unit appears in many surface forms and you need clean joins.
- **Embedding-based entity resolution before node creation** — For each newly extracted entity, embed it and match against existing nodes above a similarity threshold. Only create a new node when nothing matches. *When:* When the full entity list is unknown up front and duplicates would weaken relationship signal.
- **Personalized PageRank from a seed node** — Run a random walk from the query's starting node with periodic teleport back to it, then rank nodes by visit count to get a relevance-ordered context set. *When:* Dense graphs where you need the nodes most related to a starting entity, for example multi-hop retrieval or recommendation.
- **Subgraph context retrieval via path queries** — Given two known nodes, pull k-shortest or constrained paths between them and return the intermediate nodes, symbols or summaries as agent context. *When:* Explaining a failure or relationship between two known entities, such as tracing from a changed constructor to a broken test.
- **Subgraph pattern matching on code graphs** — Express the structure you want (for example an interface shared by a wrapper and its target) as a graph pattern and match it against the codebase graph. *When:* Finding design patterns, anti-patterns or security shapes when you do not know the names of the symbols involved.

## Numbers
- 40% reduction in tool calls for code search on a .NET codebase when using path/subgraph context retrieval to find the context needed for the agent ([10:42](https://youtu.be/3ySF0I5iE_0?t=642))
- Subgraph matching found a decorator-style wrapper pair (catalog view model service and its cached version) in the eShop codebase in one query ([11:50](https://youtu.be/3ySF0I5iE_0?t=710))
- Citation graph example: Miranda v. Arizona was found through citation relationships even though the Canvas v. Sheba case does not cite it directly ([9:12](https://youtu.be/3ySF0I5iE_0?t=552))

## Hot takes
- Graph RAG and graph databases often give no quick payoff, and many teams abandon them in the valley of disillusionment.
- Subgraph matching is less an optimisation and more an enabling algorithm for questions that other tools cannot easily answer.
- Schema and ontology design for extraction are as important as the prompt or the model choice.

## Tools mentioned
Cypher (graph query language, ASR-garbled as 'cipher'), SQL (used as the comparison baseline), HippoRAG, Pinterest PixieRank (cited as the PPR reference), Embedding models, Structured outputs from an LLM, eShop (.NET reference codebase)

## Relevance to our work
- **agentos** (1/3): MemoryMesh already lists GraphRAG and Neo4j in its plan, and the talk gives a concrete ranking method (personalized PageRank) for multi-hop retrieval. The talk explicitly skips GraphRAG and memory graphs, so the fit is partial. → *Prototype PPR seeded from query entities over the existing Neo4j graph as a re-ranker next to the BM25 and pgvector retrieval, and compare recall and context size on a small multi-hop question set.*
- **general** (1/3): The 40% fewer tool calls result for code-context retrieval from graph paths and subgraphs is relevant to context engineering for coding agents, although the evidence is a single speaker-reported run. → *Read the eShop code-graph example in the presentation pack and compare it with how current coding-agent sessions gather context for one task.*
