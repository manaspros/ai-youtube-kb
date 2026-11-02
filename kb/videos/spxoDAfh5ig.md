# Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `spxoDAfh5ig` · [watch](https://youtu.be/spxoDAfh5ig) · **date:** 2026-10-11 · **length:** 38:19 · **format:** workshop · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Peter Werry, Brandon · **orgs:** Unblocked
- **topics:** rag-retrieval, data-engineering, security-guardrails, context-engineering · **tags:** text-to-query, nl-to-mongo, schema-discovery, identity-resolution, query-validation, allow-list, retry-loop, structured-retrieval, temporal-queries, hybrid-search, webhooks, tenant-isolation

> Peter Werry (Unblocked) builds a schema-aware natural-language-to-database-query engine from scratch, covering schema sampling, identity mapping, allow-list validation and an error-retry loop, as the structured half of retrieval beyond RAG.

## Summary
The speaker argues that RAG (embedding search) only covers half of retrieval, and that structural and temporal questions such as "PRs I merged last week" need the model to write database queries. The workshop builds this in stages: a UX with a stubbed engine, then dynamic schema discovery by sampling about 300 MongoDB documents and merging them into one tree. Next comes identity resolution, where a user's name is fuzzy-matched to their GitHub login, followed by a forced tool call for name extraction and a date-aware prompt. Safety comes from a deny-by-default allow-list of operators and fields, with tenant fields hidden from the model and injected server-side. The talk ends with a retry loop that feeds validation and execution errors back to the model, plus a note that production systems should use static schemas, with webhook-driven re-ingestion for freshness. The speaker says the error loop is among the most important parts of the design.

## Key ideas
- **RAG is only half of retrieval** — Vector search handles content questions. Structural and temporal questions (author, state, merged last week) need the model to write a database query. The model writes the query and does not answer directly. ([6:02](https://youtu.be/spxoDAfh5ig?t=362))
- **A query-writing model needs four things** — It must know the schema, map natural-language names to real identifiers, produce queries that are safe to run, and self-correct after errors. Missing any one of these produces wrong or unsafe answers. ([7:03](https://youtu.be/spxoDAfh5ig?t=423))
- **Infer the schema from samples when none exists** — For schemaless stores such as Mongo, sample about 300 documents, merge them into one tree, skip nulls because they cannot constrain type, and detect enums procedurally. The speaker prefers deterministic code over LLM extraction, which he calls non-deterministic. ([10:02](https://youtu.be/spxoDAfh5ig?t=602))
- **Identity mapping is a separate step** — A user's name is often not their login (for example 'Peter' versus a GitHub handle). Simple fuzzy matching such as Levenshtein distance is enough to map them. An LLM could synthesise the mapping, but the speaker's version is hard-coded. ([12:45](https://youtu.be/spxoDAfh5ig?t=765))
- **Deny by default, and keep internal fields from the model** — Use an allow-list of operators and, where possible, of fields. Mongo's function operator can run JavaScript on the server, so it is a prompt-injection risk. Tenant IDs should be hidden from the model, then validated on output and injected server-side. The speaker advises separate collections per tenant rather than a tenant field. ([16:40](https://youtu.be/spxoDAfh5ig?t=1000))
- **The retry loop is the most important part** — Validation errors and execution errors both go back to the model with a request to fix the query, up to a maximum number of attempts. Loosening restrictions without adding a matching index can push the model into a weaker query, as happened when exact match replaced full-text search. ([19:59](https://youtu.be/spxoDAfh5ig?t=1199))
- **Add an index before relaxing a rule** — After the model fell back to exact match because regex and full-text search were blocked, the fix was to add a full-text index and combine it with author and state filters in the same match stage. ([21:27](https://youtu.be/spxoDAfh5ig?t=1287))
- **Freshness comes from webhooks, and schema choice comes from production needs** — Webhook events trigger re-ingest and re-embed on each change. In production the speaker's company uses a static, code-controlled schema for correctness. Dynamic discovery suits exploration and wiring up arbitrary databases. ([26:53](https://youtu.be/spxoDAfh5ig?t=1613))

## Techniques
- **Dynamic schema discovery by document sampling** — Sample N documents (about 300 in the demo), merge them into a single tree, skip nulls, and infer types and enums with procedural code. Pass the resulting schema, marked down, to the LLM when it writes the query. The talk also mentions a heuristic that checks string length (2 to 8 characters) when pulling type tokens from the data. *When:* The store is schemaless, or the ingestion runs in another service and the schema is unknown.
- **Deny-by-default query validation** — Allow-list operators and fields, hide internal and tenant fields from the LLM, validate the model's output for those fields, and inject tenant filters server-side. Keep this validation layer as ordinary procedural code. *When:* Model-generated queries run against a shared database or touch multi-tenant data.
- **Error-feedback retry loop** — Send validation or execution errors back to the model with a request to correct its query. Stop after a set number of attempts. The speaker's example took about three attempts for a single query. *When:* Any LLM-generated query, command or plan that can be checked by a validator or by running it.
- **Forced tool call for entity extraction, with a fallback** — Force the model to call a name-extraction tool before query synthesis. A validator checks whether the call happened, and if it did not, inserts a user message telling the model to call it. An alternative is to make the query tool accept a username argument and fail on malformed input. *When:* The query depends on mapping a natural-language name or identifier to a stored one.
- **Fuzzy identity mapping** — Match natural-language names to stored logins with simple string distance such as Levenshtein, and map them before query synthesis. The speaker notes this couples the code to the schema, and that the mapping could be synthesised by the LLM instead. *When:* User names or handles in a question differ from the stored identifiers.
- **Date-aware prompting for temporal queries** — Put the current date and time in the prompt. The speaker says LLMs are good at generating temporal filters when they have it. *When:* Questions refer to relative times such as 'last week' or 'this quarter'.
- **Two-stage schema selection** — Give the LLM short summaries and descriptions of each collection, let it choose the relevant ones, and load only those schemas into the query prompt. *When:* Many collections or tables would overflow the context window if all schemas were included.
- **Hybrid entry point, then structured queries** — Use vector search for a semantic starting point, then give the agent query tools to fetch precise, filtered data. The speaker says full-text search still matters for keywords. *When:* The user knows the topic but not the exact record they want.
- **Webhook-driven ingest and re-embed** — Handle source events such as PR changes with webhooks, so each change triggers re-ingestion and re-embedding. *When:* The data must stay fresh and polling is too slow or too costly.

## Numbers
- Schema discovery samples 300 documents to build one merged tree. ([10:02](https://youtu.be/spxoDAfh5ig?t=602))
- The workshop is a series of six stacked pull requests, cut from a two-hour session to one hour. ([1:42](https://youtu.be/spxoDAfh5ig?t=102))
- A type heuristic checks that a token is 2 to 8 characters long. The speaker describes this as hacky. ([31:43](https://youtu.be/spxoDAfh5ig?t=1903))
- The sample size was chosen empirically, by gathering customer reports of missed documents. ([34:35](https://youtu.be/spxoDAfh5ig?t=2075))
- A query with forbidden regex and full-text operators needed several attempts; the third attempt fell back to exact match. ([19:59](https://youtu.be/spxoDAfh5ig?t=1199))

## Hot takes
- RAG is only half of retrieval. Structured queries are the other half, and the model should write the database query rather than answer.
- Use procedural code, not an LLM, for extraction and validation, because LLM extraction is non-deterministic.
- Do not rely on an LLM for tenant isolation. Separate collections per tenant are better.
- Production systems should use static schemas. Dynamic discovery suits exploration only.

## Tools mentioned
MongoDB, Postgres (mentioned as a comparison with table definitions), GitHub, Linear, Jira, Slack, MCP, Levenshtein distance

## Relevance to our work
- **agentos** (2/3): MemoryMesh already has hybrid retrieval and GraphRAG. A text-to-query tier with schema sampling, allow-lists and retries would add the structured half that RAG cannot answer. → *Prototype a MemoryMesh text-to-query tool: sample the stored documents to infer the schema, allow-list operators and fields, and retry on validator or execution errors. Measure correctness on temporal and author-filtered questions against vector-only retrieval.*
- **general** (2/3): Two-stage schema selection (summaries first, then full schema) is a direct context-engineering pattern for large tool or schema surfaces, which the speaker says LLMs now handle well. → *Apply the summary-then-expand pattern to agent prompts that carry many tool or schema definitions. Load full definitions only for the tools the first pass selects.*
- **prosharness** (1/3): The forced tool call with a validator fallback could check whether a Claude Code run produced a required structured field, such as a checkpoint or plan id. → *Consider a forced-tool-call check in the plan stage: if the required structured tool call is missing, insert a reminder and retry, instead of accepting free text.*
