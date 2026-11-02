# Why I’m Switching To Powabase for My AI Apps

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `wC2QpP_A9-Y` · [watch](https://youtu.be/wC2QpP_A9-Y) · **date:** 2026-06-02 · **length:** 7:56 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Andres · **orgs:** Better Stack, PowerBase, Supabase, Internet Archive
- **topics:** rag-retrieval, vibe-coding-app-building, coding-agents · **tags:** backend-as-a-service, pgvector, postgres, rag, agentic-workflows, claude-code, mvp, ocr-text-ingestion, grounded-qa

> Better Stack tests PowerBase, a hosted backend bundling Postgres, pgvector RAG and an agent workflow builder, by having Claude Code build a RAG chatbot over an 80s hardware catalog. One demo, no measurements.

## Summary
Andres from Better Stack evaluates PowerBase, a backend-as-a-service that combines Postgres (built on Supabase), pgvector-based RAG, and a visual agentic workflow builder. He builds a retro-styled product site with an AI chatbot over an OCR text export of an 1980s computer hardware catalog from the Internet Archive. Setup is manual: Claude Code receives the project base URL, a secret key in an env file, and a link to the docs, because the official skill was not yet released. Within a few minutes the agent ingests the catalog, builds the knowledge base and runs a test chat. The chatbot answers product questions from the catalog and, for a Pac-Man query absent from the catalog, says so and offers the closest game it found. The dashboard's Run section logs every chatbot session. The conclusion is that PowerBase removes integration plumbing for MVPs, but the evidence is one seven-minute run with no latency, retrieval-quality, cost or pricing-after-credits measurements.

## Key ideas
- **PowerBase positions itself as one backend: Postgres, a RAG engine and an agentic workflow builder, extending the Supabase open-source base.** — The pitch is that a database, vector store and RAG pipeline are otherwise separate services that must be wired together. Postgres is presented as the single source of truth. ([0:00](https://youtu.be/wC2QpP_A9-Y?t=0))
- **Vectors and relational rows share one Postgres engine, so they share ACID transactions.** — The speaker says a rolled-back database transaction also rolls back the vector update, because pgvector lives in the same engine. This is a vendor claim that the video does not test. ([1:05](https://youtu.be/wC2QpP_A9-Y?t=65))
- **A visual node-based workflow canvas lets you combine deterministic guardrails and business rules with LLM tool calling.** — Execution limits are set on the canvas while the LLM still chooses tools and reasons through tasks. This is described but not demonstrated in the video. ([1:05](https://youtu.be/wC2QpP_A9-Y?t=65))
- **A coding agent can set up the whole backend from docs plus credentials, with no PowerBase skill required.** — The prompt supplied the base URL and secret key in a separate env file, a docs link, and reference design images. The official skill was announced but not yet available at recording time. ([2:24](https://youtu.be/wC2QpP_A9-Y?t=144))
- **The agent ingested the catalog, built the knowledge base and ran its own test chat in a few minutes.** — The source was the Internet Archive's OCR-scraped TXT of the PDF catalog, not the PDF. The run also appeared in the PowerBase dashboard. ([3:45](https://youtu.be/wC2QpP_A9-Y?t=225))
- **The RAG bot stays inside its corpus: for an item absent from the catalog it says so and offers the nearest match.** — The speaker calls this a common RAG trait and a good one. Questions with a clear answer in the catalog (storage for floppy disks, a $500 budget gaming machine) returned prices and recommendations. ([4:56](https://youtu.be/wC2QpP_A9-Y?t=296))
- **The dashboard's Run section logs every chatbot session with its responses, which works as a basic usage review.** — The speaker suggests this as a way to track how real users query the bot. ([6:12](https://youtu.be/wC2QpP_A9-Y?t=372))

## Techniques
- **Agent-driven backend setup from docs and credentials** — Give Claude Code the platform base URL and secret key in a separate env file, add a link to the platform docs, and describe the app and its design references in one prompt. The video does not show the exact env var names, commands or config keys. *When:* Greenfield MVP when the vendor has docs but no agent skill yet. Keep credentials in a file the agent reads, not in the prompt.
- **Single-Postgres RAG with pgvector** — Store embeddings with pgvector in the same database as the app's relational tables, so one transaction can cover a document row and its vector update. *When:* When document rows and their embeddings must stay consistent, and you would rather not run a separate vector store. The video only asserts the ACID property; it does not test it.
- **Ingest an existing OCR text export for RAG** — Download the plain-text OCR export of a scanned document and use that TXT as the RAG source instead of the PDF. The speaker used the Internet Archive's TXT of an 80s product catalog. *When:* Legacy scanned documents that already have OCR text published alongside them.
- **Corpus-bounded answers with a missing-item probe** — Test the chatbot with an item that is not in the corpus (here, a Pac-Man query against a hardware catalog) and check that it says so and offers only in-corpus alternatives. *When:* Product or catalog Q&A where invented items are costly. This is a cheap eval case to keep alongside in-corpus queries.
- **Node-based guardrails around LLM tool use** — Map deterministic steps, hard business rules and execution limits as nodes on a visual canvas, and let the LLM pick tools inside those nodes. The feature is described only. *When:* Agents that must follow fixed business rules and stay within execution budgets while still reasoning freely.
- **Review the session run log** — Use the dashboard's Run section to read each chatbot session and its responses, to see what users actually ask. *When:* After launch, as a lightweight review of real chatbot traffic before building proper analytics.

## Numbers
- New accounts get $20 of PowerBase credits after answering a short questionnaire. ([1:05](https://youtu.be/wC2QpP_A9-Y?t=65))
- The coding agent built the ingestion, knowledge base and a test chat run in 'a few minutes'. No timing is given beyond that. ([3:45](https://youtu.be/wC2QpP_A9-Y?t=225))
- One catalog answer quotes a $500 price for a budget gaming computer (auto-captioned 'Interact Family Computer'). ([4:56](https://youtu.be/wC2QpP_A9-Y?t=296))
- A Pac-Man query returned no match in the catalog, and the bot offered a similar game as the closest alternative. ([4:56](https://youtu.be/wC2QpP_A9-Y?t=296))
- The whole demo runs 7:56. The video reports no latency, token counts, retrieval accuracy or cost figures. ([0:00](https://youtu.be/wC2QpP_A9-Y?t=0))

## Hot takes
- The conclusion, that PowerBase is 'a perfect backend as a service' for MVPs, rests on one seven-minute run judged by how the site looks and a few sample queries.
- Retrieval quality, latency and cost after the free credits are not measured or discussed.
- The grounded refusal on Pac-Man is shown as a positive, but the video never tests recall, precision or misses on in-corpus questions.
- The agent setup worked from manual docs prompting because the official skill was not yet out at recording.
- The transactional claim about pgvector and relational rows is asserted, not demonstrated.
- No sponsorship disclosure appears in the transcript, but the framing ('Why I'm Switching') and praise ('Oh my God, this looks so good') lean toward a vendor showcase.

## Tools mentioned
PowerBase (powerbase.ai), Supabase, PostgreSQL, pgvector, Claude Code

## Relevance to our work
- **agentos** (1/3): PowerBase keeps relational data, pgvector embeddings and RAG in one Postgres. That is a different point in the design space from our MemoryMesh, which spans Postgres/pgvector, Redis, Neo4j and other stores. The video's transactional claim is untested. → *Check whether MemoryMesh writes to pgvector should share a transaction with the source-row writes, and test the claim before adopting or rejecting the single-Postgres design.*
- **prosharness** (1/3): The setup hands a coding agent a base URL and secret key through a separate env file, which is close to ProsHarness's zero-token credential handling. The video shows no mechanism for keeping credentials out of the agent's context. → *Compare how this demo passes secrets to Claude Code (env file plus docs link) with ProsHarness's zero-token credential path, and note where the agent could still read the secret.*
