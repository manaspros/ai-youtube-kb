# Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `cKhpeEBnT1o` · [watch](https://youtu.be/cKhpeEBnT1o) · **date:** 2026-10-04 · **length:** 12:23 · **format:** talk · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Jakub Hojsan · **orgs:** Exa, Cursor, Cognition, Warp, CodeRabbit, OpenAI, Anthropic, SimilarWeb, Particle, Crunchbase
- **topics:** rag-retrieval, mcp-and-tools, coding-agents · **tags:** web-search, knowledge-cutoff, highlights, code-review-agents, search-api, re-ranking, structured-output, exa, product-pitch

> Exa's forward-deployed engineer explains why coding agents miss recent changes past their model cutoff, and how query-targeted web search snippets, plus explicit search rules, close that gap. Partly a product pitch.

## Summary
Jakub Hojsan (Exa) argues that coding and code-review agents lag about six months behind the model's knowledge cutoff, so they cannot review recent PRs or dependency changes without search. He says adding a web search tool is not enough: the agent also needs rules about when to search, since native search may not know newer model or package versions. Exa's approach returns short, query-specific highlights from pages rather than full pages, using a computational extraction step for raw highlights and an optional LLM distillation step on top. He claims this gives a full search trace for telemetry, lower cost than native search at scale, and a single API that works across model providers. He describes a multi-stage retrieval pipeline (query embedding, keyword filtering, semantic search, re-ranking) over a curated index of tens of billions of documents. The talk closes with a product plug for Exa Agent, MCP access, and natural-language-to-schema structured output. The speaker's claims about latency and quality are not backed by benchmarks in the talk.

## Key ideas
- **Coding and review agents are stuck at the model's knowledge cutoff, which lags release by about six months.** — Repos keep changing after the cutoff (a dependency bump, a vector store PR), so the model cannot review those diffs from its own knowledge. The speaker says the gap is structural, not a bug in any one model. ([0:12](https://youtu.be/cKhpeEBnT1o?t=12))
- **Return small, query-specific snippets from pages instead of whole pages.** — The search returns a few highlights that answer the query. The speaker's example is about 500 characters fed to the model instead of roughly 100,000. An interpretation step can distill the page to what the model needs. ([2:41](https://youtu.be/cKhpeEBnT1o?t=161))
- **Adding a search tool to an agent is not enough; the agent also needs rules for when to search.** — Native search may be missing from the harness, and the model may not know that newer versions exist (his example: it says a Sonnet version does not exist). He suggests a rule such as: when a diff bumps a dependency, check the upstream source and ground the review in it. ([4:12](https://youtu.be/cKhpeEBnT1o?t=252))
- **Native web search is a black box; a third-party search API gives a full trace.** — Native search returns some sources but no content, and can take up to 10 seconds. The speaker says a search API returns the exact queries, sources and highlights passed to the model, which can go into telemetry for debugging. ([4:12](https://youtu.be/cKhpeEBnT1o?t=252))
- **Highlights are picked computationally, without an LLM, so the speaker claims no added latency.** — At runtime the system pulls matching lines from a page. The speaker says this works for any page or query, such as an About page for a bio or a phone number, and for a large repo where you want only the relevant part. ([5:38](https://youtu.be/cKhpeEBnT1o?t=338))
- **A single search API keeps the agent independent of the model provider.** — The speaker says the same fixed API and parameters work whichever model is in use, so switching to a new model does not change the search integration. ([5:38](https://youtu.be/cKhpeEBnT1o?t=338))
- **Search quality comes from a multi-stage pipeline: embedding, filtering, semantic search, re-ranking.** — The query is embedded, then keyword filtering and semantic search run, then re-ranking drops irrelevant results. The index is curated and smaller than Google's, but the speaker says its quality is high. He gives no metrics. ([10:38](https://youtu.be/cKhpeEBnT1o?t=638))

## Techniques
- **Two-part search instructions for agents** — Add the search tool and also write explicit rules in the agent prompt: when to search (e.g. a dependency bump in a diff, or a model or version name the model does not recognise) and what to do with the result (verify against the upstream source before the review claim). *When:* Use when an agent must review or act on facts after the model's training cutoff, or when the native tool set does not include search.
- **Query-targeted highlight extraction** — Fetch the page, pick the lines or passages relevant to the query, and return only those, with no LLM in the loop. Optionally add an interpretation step that distills the snippets into an answer. *When:* Use for large pages or repos where full content is too costly, and where you want to keep latency and token use low.
- **Full retrieval trace logging** — Keep the exact queries, sources returned and the highlights that went into the prompt, and send them to telemetry. *When:* Use when you need to debug why an agent gave a wrong answer based on search results.
- **Natural-language schema for structured output** — Describe the fields you want in plain language to generate a JSON schema (the speaker gives limits of up to 10 fields for deep and up to 100 for agents). Set additional properties to true to allow extra fields. *When:* Use to extract structured records from web results without writing the schema by hand.

## Numbers
- Model knowledge cutoff lags release by about six months (from a graph shown in the talk). ([0:12](https://youtu.be/cKhpeEBnT1o?t=12))
- Native search can take up to 10 seconds and returns sources but no content. ([4:12](https://youtu.be/cKhpeEBnT1o?t=252))
- Speaker's example: about 500 characters of highlights fed to the model instead of about 100,000 characters for the full page. ([2:41](https://youtu.be/cKhpeEBnT1o?t=161))
- Speaker claims zero added latency for computational highlight extraction (no benchmark shown). ([5:38](https://youtu.be/cKhpeEBnT1o?t=338))
- Index holds tens of billions of documents, curated, smaller than Google's index (speaker's claim). ([10:38](https://youtu.be/cKhpeEBnT1o?t=638))
- Structured output schema limits: up to 10 fields on deep, up to 100 on agents. ([10:38](https://youtu.be/cKhpeEBnT1o?t=638))

## Hot takes
- Adding a web search tool to an agent does nothing unless the agent is also told when to search.
- Native web search from model providers is a black box and gets expensive at scale.
- Returning the relevant 500 characters beats feeding the model a 100,000-character page.
- Coding agents are months out of date by default, so review of recent changes needs live search.

## Tools mentioned
Exa search API, Exa Agent, MCP server, Claude Code, CodeRabbit, Cursor

## Relevance to our work
- **agentos** (1/3): The talk's multi-stage retrieval (embedding, keyword filter, semantic search, re-rank) and per-query highlights touch MemoryMesh's hybrid BM25 + pgvector retrieval, but the talk gives no metrics or code. → *Compare MemoryMesh's re-rank stage against the filter-semantic-rerank flow in the talk, and log retrieval traces for each query so the same debugging is possible.*
- **prosharness** (1/3): The 'add the tool and also write rules for when to use it' point applies to a harness around Claude Code, which may need explicit verification rules for model names and dependency versions. → *Add a CLAUDE.md or skill rule that tells the Claude Code run when to verify model names and dependency versions with a search, and what to check before the claim is accepted.*
