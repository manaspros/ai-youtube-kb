# Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ZRM_TfEZcIo` · [watch](https://youtu.be/ZRM_TfEZcIo) · **date:** 2026-07-18 · **length:** 39:32 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Paul Iusztin, Louis-François Bouchard · **orgs:** Decoding AI, Towards AI
- **topics:** memory, rag-retrieval, context-engineering · **tags:** second-brain, obsidian, wiki, index-yaml, deep-research, plain-files, claude-code, codex, para, readwise, notebooklm, file-based-memory, write-back, tiered-retrieval

> Two builders show a file-based personal research system: raw sources, an index.yaml catalog and an LLM-written wiki, queried in tiers and fed by every question. No vector DB needed.

## Summary
Paul Iusztin and Louis-François Bouchard describe a personal "AI research OS" built on their own notes (about 10k items across Obsidian, Readwise, Notion and Drive). The core argument is that the bottleneck is how an agent can reach and reuse past research inside a limited context window, not how much data it can be given. They reject NotebookLM for being closed and browser-bound, and reject vector-DB RAG stacks as too heavy for a personal tool. Their system is plain markdown: an immutable raw/ folder, an index.yaml catalog with per-source summaries, and an LLM-maintained wiki of source summaries, concepts, entities and comparisons. Agents query it top-down (index, then source summary, then derivative pages, then raw file only as a last resort). Each question can write a new note back into the wiki, so the wiki grows through use. The talk traces three versions, from a static research.md to a seeded deep-research loop over their own sources to the wiki layer, and ends with demos and an honest list of weak points (source freshness, memory compaction, linting). It is a workshop-style talk with a course plug at the end.

## Key ideas
- **The bottleneck is context management, not data volume** — The speakers argue that feeding an agent more links and PDFs does not help. What matters is a persistent memory the agent can navigate, because the context window holds everything and is lost when a session ends. ([9:20](https://youtu.be/ZRM_TfEZcIo?t=560))
- **Skip vector DBs and knowledge graphs for a personal wiki** — Their view is that a personal tool should be file-based and easy to inspect by hand. Vector DBs and similar infrastructure add complexity they do not need at this scale. NotebookLM is also rejected because it is not owned, not agent-native and weak for coding. ([6:31](https://youtu.be/ZRM_TfEZcIo?t=391))
- **Three layers: immutable raw sources, index.yaml catalog, LLM-written wiki** — Raw files are never edited. index.yaml holds one entry per source with its link, metadata and summary, and acts as the agent's entry point. The wiki holds LLM-derived pages such as source summaries, concepts, entities, comparisons and open questions. ([20:20](https://youtu.be/ZRM_TfEZcIo?t=1220))
- **Tiered query path that reads the raw file only as a last resort** — The agent reads index.yaml first, then the source wiki page, then linked derivative pages (concepts, entities, comparisons). It opens the full raw source only if those layers do not answer the question. The speakers say this keeps token use low. ([23:06](https://youtu.be/ZRM_TfEZcIo?t=1386))
- **Every question writes back into the wiki** — Each question can create a new concept, note or comparison file, and every question is logged. The wiki therefore evolves through use and not only when new data is ingested. ([23:06](https://youtu.be/ZRM_TfEZcIo?t=1386))
- **Evolution from static research.md to seeded deep research over own sources** — V1 scraped manually chosen golden links and produced one flat research.md. V2 pointed the same multi-round loop at the user's own second brain. V3 stores each source as its own file and builds the index and wiki on top. ([12:05](https://youtu.be/ZRM_TfEZcIo?t=725))
- **Scope a global immutable second brain down to each project** — The global notes stay untouched. For each project, deep research runs over the second brain and the results are scoped to that project, with the project as the work and the second brain as the research. They use PARA (projects, areas, resources, archive) to organise the notes. ([24:29](https://youtu.be/ZRM_TfEZcIo?t=1469))

## Techniques
- **Tiered index-first retrieval** — Keep an index.yaml with one entry per source (link, title, metadata, summary). Ask the agent to read the index, then per-source summary pages, then linked derivative pages, and open the raw file only if still needed. *When:* When a personal or team knowledge base is too big to load into context and must stay token-cheap to query without a vector store.
- **Immutable raw layer with LLM-owned derivatives** — Store original sources in a raw/ folder that the LLM never edits. Put all LLM-generated synthesis (summaries, concepts, entities, comparisons, open questions) in a separate wiki/ folder that can be rebuilt. *When:* When you want to trust the source of truth and still let the agent build reusable summaries on top of it.
- **Query write-back with a log** — After each answer, let the agent write any new concept, note or comparison it produced into the wiki, and append the question to a log file. *When:* When you want the knowledge base to compound from daily questions, not only from ingestion runs.
- **Seeded multi-round deep research** — First scrape known seed sources to frame the questions. An orchestrator makes queries per round. Each sub-agent returns links and short summaries, and the orchestrator aggregates them to keep the context small. Rank the links against the topic, fully scrape only the top-k, and keep summaries for the rest. *When:* When a research run must cover many sources but the context window cannot hold all the raw text.
- **Depth knob for research runs** — Expose a light/fast/deep setting that sets the number of rounds and queries per round. The speakers used light (1 round x 3 queries) for a demo and fast (2 rounds x 3 queries) as the usual default. *When:* When deep research burns many tokens and you want to pay for depth only when a question needs it.
- **Repo ingestion into per-repo and cross-repo notes** — Clone a set of repos, have the agent write one note per repo on each topic (architecture, sub-agents, memory, permission flow), then write comparison and aggregate notes across the repos. *When:* When you want to learn how a family of tools is built, for example agent harnesses, directly from their code.

## Numbers
- About 5,000 notes in Obsidian plus about 5,000 in Readwise, with more in Notion and Google Drive; growth about 250 files per month ([0:00](https://youtu.be/ZRM_TfEZcIo?t=0))
- V1 deep research ran 3 rounds of 6 queries and returned about 40-50 links, which were ranked and only the top-k fully scraped ([13:27](https://youtu.be/ZRM_TfEZcIo?t=807))
- V1 pipeline generated 35 course lessons from its static research.md output ([14:56](https://youtu.be/ZRM_TfEZcIo?t=896))
- Light depth = 1 round of 3 queries; fast depth = 2 rounds of 3 queries ([27:17](https://youtu.be/ZRM_TfEZcIo?t=1637))
- A research run over the second brain takes about 10-20 minutes ([29:56](https://youtu.be/ZRM_TfEZcIo?t=1796))
- Example index.yaml in the demo lists 10 sources and 38 derivative wiki pages ([20:20](https://youtu.be/ZRM_TfEZcIo?t=1220))
- The Agent Engineering course is estimated at about 60 hours, with a multi-agent final project ([38:27](https://youtu.be/ZRM_TfEZcIo?t=2307))

## Hot takes
- NotebookLM is not agent-native, is weak for coding tasks, and you do not own it.
- A personal second brain does not need a vector DB, knowledge graph or semantic search; plain files and an index are enough.
- Adding more context to an agent is not the answer; the bottleneck is memory and context management.
- A wiki should evolve through use, with every question writing back into it, not only when data is ingested.

## Tools mentioned
Obsidian, Readwise, NotebookLM, Notion, Google Drive, Granola, Claude Code, Codex, Gemini Deep Research, Gemini (grounded Google search), Bright Data, YAML, PARA

## Relevance to our work
- **agentos** (2/3): MemoryMesh already plans tiered cross-session memory and hybrid BM25+pgvector retrieval. This talk offers an index-first, file-based alternative and a query write-back loop that could be compared against it. → *Prototype an index.yaml-style catalog tier in MemoryMesh and compare its token cost and answer quality against the current hybrid retrieval on the RAGAS eval set.*
- **prosharness** (1/3): Long agent runs need checkpointed memory. The query write-back loop and the immutable-raw / LLM-derivative split may suit how ProsHarness stores its run artifacts. → *Read the talk's wiki and write-back section and decide whether run checkpoints should keep raw logs separate from LLM-written summaries.*
- **general** (1/3): A practitioner example of file-based memory and tiered retrieval for personal research, useful as background for context-engineering work. → *Read the talk's wiki and index section before the next context-engineering design pass.*
