# Connecting the Dots with Context Graphs — Stephen Chin, Neo4j

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `eW_vxrjvERk` · [watch](https://youtu.be/eW_vxrjvERk) · **date:** 2026-05-18 · **length:** 17:39 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Stephen Chin · **orgs:** Neo4j, Gartner, Foundation Capital
- **topics:** memory, rag-retrieval, mcp-and-tools · **tags:** context graph, knowledge graph, Neo4j, Cypher, GraphRAG, decision traces, reasoning memory, explainability, audit, MCP, vector search, FastRP, Leiden

> Neo4j DevRel lead argues agents need a knowledge graph that stores short-term, long-term and reasoning memory together, so decisions can be explained and reused. Mostly a product pitch with one finance demo.

## Summary
Stephen Chin of Neo4j frames the problem as enterprise knowledge being scattered across Slack, tickets, CRMs and other silos, so agents make decisions without the context behind them. He proposes a "context graph" that holds three kinds of memory in one structure: short-term state of the current pipeline, long-term entity and process history, and reasoning traces that record why a decision was made. He contrasts a plain LLM answer, a vector-RAG answer and a graph-grounded answer on a healthcare example, where the graph version recovers patient history that similarity search dropped. The main demo is a financial-services loan approval agent that pulls from a support system, a CRM and an internal system through about 10 MCP tools, writes entities and decisions into Neo4j, and shows the Cypher queries it ran as an audit trail. The talk is mostly a vendor pitch for Neo4j's open-source agent memory package and free Aura and Graph Academy resources. It gives no benchmarks, so the value is the architecture pattern rather than measured results.

## Key ideas
- **Plain audit logs record what happened but not why; a context graph captures decision traces as entities and relationships.** — The speaker says an audit log misses the reasoning, while a graph stores the policies applied, risk factors, previous decisions and approvals, so later agents can look them up. Presented as the core difference between context graphs and logs. ([11:41](https://youtu.be/eW_vxrjvERk?t=701))
- **Split agent memory into three stores that live in one graph: short-term state, long-term history, and reasoning traces.** — Short-term memory is the current pipeline state. Long-term memory needs a domain model of entities and processes so it stays organized across tasks and customers. Reasoning memory keeps decision provenance that can be reused and used for compliance and debugging. ([6:33](https://youtu.be/eW_vxrjvERk?t=393))
- **Vector similarity search alone drops background facts that matter for the answer.** — In the healthcare example, the vector-RAG answer gave generic breathing and coughing advice. The graph-grounded answer added smoking-cessation counselling and pulmonary rehab based on the patient's history and prior operation. The speaker presents this as the reason to add graph retrieval. ([5:15](https://youtu.be/eW_vxrjvERk?t=315))
- **Use vector lookup only to find an entry node, then traverse the graph for multi-hop context.** — The speaker describes FastRP graph embeddings and vector lookups as the way into the graph, followed by traversal and Leiden community detection. He says this gives explainable results and handles multi-hop questions better than joining tables. ([8:58](https://youtu.be/eW_vxrjvERk?t=538))
- **Write each agent decision back into the graph so later queries can read it.** — The loop is: retrieve through graph, vector and data-science tools, run the agent, then store the output and its reasoning as new graph data that later queries draw on. This makes the graph grow with use. ([11:41](https://youtu.be/eW_vxrjvERk?t=701))
- **Expose the Cypher queries and traversed subgraph to the user to make the agent's answer auditable.** — In the loan demo, the UI shows the Cypher the model generated and the graph it walked, including a previous rejection and fraud-pattern hits. The speaker argues this lets a human justify the decision to the organization. ([14:27](https://youtu.be/eW_vxrjvERk?t=867))

## Techniques
- **Three-tier memory in one graph** — Store short-term pipeline state, long-term entity and process history, and reasoning traces as connected nodes and relationships in one graph store, with a domain model for entities. *When:* Agents need to recall prior sessions and explain why earlier decisions were made, not just what was retrieved.
- **Vector entry point then graph traversal** — Embed nodes, use vector lookup to find a starting node, then traverse relationships with graph algorithms such as FastRP embeddings and Leiden community grouping. *When:* Similarity search returns relevant chunks but misses linked background facts, such as patient history or account relationships.
- **Decision write-back to the graph** — After each agent run, store the recommendation, its reasoning and its sources as new nodes linked to the entities involved, so later queries retrieve them as precedent. *When:* Decisions repeat across cases and the organization needs decision precedent, provenance or compliance trails.
- **LLM-generated Cypher with visible query trace** — Let the model write Cypher against the graph and show the generated queries and traversed subgraph in the UI next to the answer. *When:* A human must sign off on an agent's recommendation and needs to see the evidence used.
- **Multi-source ingestion through MCP tools into a graph** — Expose each source system (support tickets, CRM, internal business data) as MCP tools, then use an LLM to extract entities and create OpenAI embeddings that populate the graph. *When:* Context lives in several enterprise systems and needs to be joined into one queryable structure.

## Numbers
- The loan demo agent uses 10 MCP tools to reach the support ticket system, CRM and internal business data system. ([16:00](https://youtu.be/eW_vxrjvERk?t=960))
- Foundation Capital's post, cited by the speaker, calls context graphs a $3 trillion startup opportunity. This is a third-party claim the speaker repeats, not verified here. ([2:33](https://youtu.be/eW_vxrjvERk?t=153))
- Gartner has added context graphs to the AI hype cycle, according to the speaker. No figures given. ([2:33](https://youtu.be/eW_vxrjvERk?t=153))
- The talk gives no benchmark, latency, cost or accuracy figures for the graph-grounded approach. The healthcare comparison is qualitative. ([5:15](https://youtu.be/eW_vxrjvERk?t=315))

## Hot takes
- An audit log is not enough for agents: it records outcomes but not the why, and the why is what the graph should keep.
- Vector-only RAG loses background facts that a graph would keep, so agents built on similarity search alone give generic answers.
- Enterprise context is stuck in Slack threads, tickets and siloed systems, and agents cannot make good business decisions until it is joined into one structure.

## Tools mentioned
Neo4j, Neo4j Agent Memory package (open source), Cypher, OpenAI embeddings, FastRP, Leiden algorithm, MCP, Next.js, Neo4j Aura (free tier), Graph Academy

## Relevance to our work
- **agentos** (2/3): MemoryMesh already has tiered cross-session memory, provenance and GraphRAG, and Neo4j is already in the L3 storage plan. The talk's idea of storing reasoning traces as graph nodes maps onto MemoryMesh's provenance layer. → *Prototype one MemoryMesh path that stores each agent decision and its cited sources as linked nodes, then benchmark multi-hop precedent lookup against the current BM25 plus pgvector retrieval on a small decision set.*
- **prosharness** (1/3): The plan, critique and debate steps create decision records that a later checkpointed run could reuse. The talk's reasoning-trace idea applies, but only as a storage pattern. → *Consider saving plan, critique and debate outcomes as structured records with links to the checkpoint they came from, so resumed runs can query earlier decisions.*
- **general** (1/3): The three-tier memory split (short-term, long-term, reasoning traces) is a clear framing for agent memory design. The talk gives no measurements to support it. → *Read the Neo4j agent memory package README to see how it separates short-term, long-term and reasoning memory, and compare it with our current memory design.*
