# Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `VGN22pPpb-8` · [watch](https://youtu.be/VGN22pPpb-8) · **date:** 2026-08-18 · **length:** 11:06 · **format:** keynote · **quality:** 2/5 · **depth:** intro
- **speakers:** Emil Eifrem · **orgs:** Neo4j, Palantir, Latent Space
- **topics:** data-engineering, memory, multi-agent · **tags:** ontology, semantic-layer, knowledge-graph, neo4j, thin-agents, execution-traces, data-sources, process-guided-agent, markdown-vs-graph

> Neo4j keynote arguing that agents should be thin and share an ontology-based semantic layer over enterprise data, with execution traces that teach source selection over time.

## Summary
Emil Eifrem (Neo4j) argues that enterprise agents break down when each team rewires its own data sources, since the wiring is duplicated, drifts when things change, and does not improve over time. He proposes a shared "ontology-based semantic layer" with three pillars: a business ontology written in terms people in the company use (customer, account, first name), a technical ontology describing where data lives (databases, schemas, Snowflake, S3), and a mapping between the two. A third pillar is execution traces from agent runs, which record context, what was tried, and whether it worked, and roll up into scores. Using a bank account-opening agent as the example, he shows a compliance step that can resolve a government ID through two sources (DMV records or passport verification), with trace scores guiding which one the agent picks next time. He says Markdown files and skills are part of the answer but not the whole answer. The talk is a keynote pitch for Neo4j, with no benchmarks or measured results, and points to a booth, a web page, and a startup program.

## Key ideas
- **Thick agents with hand-wired data sources do not scale across an enterprise.** — Each team re-discovers where its data sits, checks duplicates and trust by hand, and rewires everything when a source changes. The agent also does not get smarter with use, and nothing carries over between agents. ([1:08](https://youtu.be/VGN22pPpb-8?t=68))
- **Markdown files and skills are part of the fix, not all of it.** — The speaker says many teams tried to solve this with Markdown alone and it falls short. He quotes swyx (Latent Space) as saying you cannot vibe-code with Markdown files only. The proposed pattern is thin agents on a smarter shared substrate. ([3:31](https://youtu.be/VGN22pPpb-8?t=211))
- **Three pillars: business ontology, technical ontology, and runtime traces.** — The business ontology uses concepts people recognise (customer has a first name). The technical ontology holds metadata about every data source. A mapping links the two, so a business concept points to the column that stores it, such as an Oracle column called F_NAME. Execution traces then record what each agent step tried, the context, and the result. ([4:56](https://youtu.be/VGN22pPpb-8?t=296))
- **The business process itself is encoded in the graph, and the agent follows it.** — In the bank example, a process-guided agent walks a business-process graph. At a compliance node it finds it needs a government-issued ID, then looks up which sources can supply one in this organisation (DMV records or passport verification). ([6:09](https://youtu.be/VGN22pPpb-8?t=369))
- **Trust in a data source comes from two places: admin curation and observed outcomes.** — Top-down, an administrator labels sources as trusted. Bottom-up, scores from past traces show which source worked in which context. The next invocation then prefers a source that did well in a similar context. ([7:28](https://youtu.be/VGN22pPpb-8?t=448))
- **Shared governed mapping makes changes cascade and lets learning carry across agents.** — One mapping from business intent to data sources means a change is made once and reaches all agents (the DRY argument). Trace scores come from all agents, so one agent's experience improves the others. ([8:28](https://youtu.be/VGN22pPpb-8?t=508))

## Techniques
- **Business-to-technical ontology mapping** — Write the domain as business concepts and relations (customer, account, transaction). Separately catalogue each physical source's schema and location. Store a mapping edge from each business property to the column or field that holds it. *When:* Several agents or teams need the same data across many databases, and the schemas use internal names that do not match business language.
- **Process graph for process-guided agents** — Model the business process as a graph of steps. At each step, the agent asks the graph which data sources can satisfy that step's requirement, instead of hard-coding the source. *When:* The agent must follow a fixed business process (such as account opening or compliance checks) and the data needed at each step varies by organisation.
- **Trace-derived source scores** — After each agent step, log the context, the source tried, and whether the step succeeded. Roll the logs up into a score per source per context. Use the score when choosing a source next time, alongside any admin-set trust label. *When:* Several sources can answer the same question and the best one depends on context, and you want the choice to improve from use rather than being fixed by hand.
- **Thin agents over a shared substrate** — Keep agent code to planning and acting. Move data discovery, trust, and source choice into one shared layer that all agents query. *When:* You run many agents that look structurally alike and keep re-implementing the same data wiring.

## Numbers
- The pattern emerged over roughly the last 6 to 9 months, according to the speaker. ([0:08](https://youtu.be/VGN22pPpb-8?t=8))
- Enterprises have many data stores: a speaker example of 'a hundred databases' plus Snowflake, Databricks and S3 buckets. This is illustrative, not a measured count. ([2:22](https://youtu.be/VGN22pPpb-8?t=142))
- Illustrative count of 14 Oracle databases and 15 Neo4j databases in one organisation. Used as an example, not a measured result. ([4:56](https://youtu.be/VGN22pPpb-8?t=296))
- Named customers: a Fortune 20 global bank, a large Bay Area tech platform, and a leading fintech company. No outcomes or metrics were given. ([3:31](https://youtu.be/VGN22pPpb-8?t=211))
- No benchmarks, latency figures, accuracy numbers, or cost data are given in the talk. ([8:28](https://youtu.be/VGN22pPpb-8?t=508))

## Hot takes
- Markdown files and skills are part of the solution but not the solution for enterprise agents.
- You cannot vibe-code agents with only Markdown files; you have to learn your databases.
- Agents should be thin, sitting on a smarter shared semantic layer rather than carrying their own data wiring.
- Agents' trace data should feed back into how they pick data sources, so a single agent gets smarter over time and so do the others.

## Tools mentioned
Neo4j

## Relevance to our work
- **agentos** (1/3): L2A MemoryMesh already covers cross-session memory and GraphRAG. The talk's idea of storing per-source success scores from traces to bias the next choice is a concrete variant of this, but the talk gives no method for it. → *Consider adding a per-source success score, keyed by context and fed from run traces, to MemoryMesh retrieval routing. Test it on one bucket before building more.*
- **prosharness** (1/3): ProsHarness checkpoints long runs, so it already records state per step. The talk's point that traces should feed later choices applies, but only as an idea. → *Record outcome and context for each tool or skill call in ProsHarness checkpoints, so a later plan step can see which tool worked in similar situations.*
- **general** (1/3): Context engineering: the talk says Markdown and skills do not produce cross-agent learning on their own. That is a useful boundary for deciding what belongs in CLAUDE.md or AGENTS.md versus a queryable store. → *Note the boundary: keep stable rules in CLAUDE.md, and move per-source or per-tool outcome history into a queryable store. No code to build from this talk.*
- **general** (1/3): Entity resolution and data quality: mapping a business term (first name) to the physical column it lives in is a schema-matching problem. The talk does not describe a method for it. → *Read-only. Keep the business-term-to-column mapping in mind as a possible schema-matching baseline, but do not act on it from this talk alone.*
