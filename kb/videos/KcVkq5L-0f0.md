# Your agents lack context: Here's how to fix "You're absolutely right!" — Brandon Waselnuk, Unblocked

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `KcVkq5L-0f0` · [watch](https://youtu.be/KcVkq5L-0f0) · **date:** 2026-09-18 · **length:** 14:09 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Brandon Waselnuk · **orgs:** Unblocked, LinkedIn, Workday, General Motors, Anthropic
- **topics:** context-engineering, rag-retrieval, mcp-and-tools · **tags:** context-engine, context-engineering, brownfield, mcp, tool-descriptions, satisfaction-of-search, conflict-resolution, permissions, token-efficiency, relational-retrieval, schema-discovery, rules-files, team-graph, github, slack, vendor-pitch

> Brandon Waselnuk (Unblocked) argues AI coding agents fail on missing company context, not intelligence, and outlines context-engine design: avoid curated markdown, separate access from understanding, and use schema discovery for relational questions.

## Summary
The speaker says agents write compilable code that still breaks production because they lack company context such as rollout procedures, ownership and recent decisions. He calls hand-curated markdown context files a trap because they rot and nobody owns them org-wide. He also says MCP tools go unused when their descriptions are weak, and agents accept the first plausible hit (satisfaction-of-search bias). His core claim is that access to information is not understanding, so a context engine must resolve conflicts between sources, enforce permissions and deliver token-efficient context. He describes a relational workflow where the agent discovers a schema and writes deterministic queries, since RAG alone cannot answer questions like "open PRs I touched on auth last week." He reports one internal test: the same task used about 21M tokens without context and about 10.8M with it, with a 50% token reduction claimed in general. The talk closes with a pitch for his company's product and a few free open-source tools, so vendor framing is present throughout.

## Key ideas
- **Agents lack company context, so they produce code that compiles but breaks production** — Each new agent session starts with no knowledge of how the company operates. The gap is missed rollout steps, feature-flag procedures and ownership, not model intelligence. ([1:43](https://youtu.be/KcVkq5L-0f0?t=103))
- **Bad context compounds as agents scale** — Missing context shows up as doom loops of correction, wasted tokens and rework, then as a review tax on AI reviewers and background agents. Fixing context early is cheap, similar to shift-left for defects. ([3:10](https://youtu.be/KcVkq5L-0f0?t=190))
- **Curated markdown context is a trap** — Hand-written context files in a repo go stale, are hard to distribute, and need one person with the taste to curate them for the whole org. ([4:31](https://youtu.be/KcVkq5L-0f0?t=271))
- **MCP plateau: tool descriptions decide whether tools are used, and agents stop at the first hit** — A weak server or tool description means the agent may never call the tool. Satisfaction-of-search bias also makes the agent accept the first plausible answer, even when a later Slack message overrides it. ([4:31](https://youtu.be/KcVkq5L-0f0?t=271))
- **Access to information is not understanding** — A context engine must resolve conflicts between sources (an old architecture diagram vs. a recent CTO Slack thread), respect permissions and deliver token-optimized context at the right moment. ([5:28](https://youtu.be/KcVkq5L-0f0?t=328))
- **Map-then-discover: give the model a map so it can find unknown unknowns** — He cites a remark that models should be given a map and then discover the territory. Broad context lets the model surface relevant facts the user did not know to ask about. Targeted lookups should stay fast, while deep research can run long. ([7:57](https://youtu.be/KcVkq5L-0f0?t=477))
- **Relational questions need schema discovery plus deterministic queries, not RAG alone** — The agent discovers a schema without a fixed one, then writes queries against it. This answers structured questions like open PRs on a topic by a person, which embedding retrieval cannot reliably do. ([11:41](https://youtu.be/KcVkq5L-0f0?t=701))

## Techniques
- **Derive context from systems instead of hand-curated files** — Ingest data from source systems (GitHub, Slack, incident tools) into an engine rather than maintaining markdown in the repo that rots. *When:* Large or brownfield orgs where context is spread across tools and no single person can keep docs current.
- **Deterministic team graph from GitHub** — Build a graph of who commits where, who reviews whose work, and team membership using deterministic code. An optional LLM pass can label teams. *When:* You need ownership and reviewer context to focus an agent's search or route reviews.
- **Rules-file discovery and index** — Find every rules file across the repo, check severities and duplicates, and produce an index that agents can grep and dedupe. *When:* Several CLAUDE.md, AGENTS.md or rules files have accumulated and conflict or repeat each other.
- **Schema-less lookup, then deterministic query** — Let the agent discover the schema at runtime, then write queries against it to answer relational questions. Combine this with RAG for text-heavy questions. *When:* The question involves relationships (authors, reviewers, time ranges, PR state) that similarity search answers poorly.
- **Two retrieval modes: deep research and fast unfurl** — Use long-running retrieval for open-ended research and a quick direct lookup, such as unfurling a shared link, when speed matters. *When:* The same context engine serves both background agents and interactive use in Slack or support tools.
- **Context hydration to avoid repeated discovery searches** — Preload relevant context at the start of a session so the agent does not spend tokens rediscovering the codebase and org each time. *When:* Long tasks where the agent would otherwise repeat broad searches on every session.

## Numbers
- Same task with and without context: about 21M tokens without context vs about 10.8M with it (speaker first said 18M, then corrected to 10.8M) ([9:22](https://youtu.be/KcVkq5L-0f0?t=562))
- Typical outcome cited: about 50% fewer tokens, faster triage and better answer quality with a context engine ([9:22](https://youtu.be/KcVkq5L-0f0?t=562))
- Wall-clock time saving on the same test task, given as a figure around two hours (the transcript is unclear on the exact number) ([7:57](https://youtu.be/KcVkq5L-0f0?t=477))
- Vendor has hundreds of enterprise and mid-market clients ([3:10](https://youtu.be/KcVkq5L-0f0?t=190))

## Hot takes
- The gap is no longer intelligence; it is the context you surround models with.
- Curated markdown context files rot and do not scale to a whole organization.
- A tool that works without context is cheap early and expensive later: bad context compounds across agents and reviews.

## Tools mentioned
MCP, GitHub, Slack, OAuth, SSO, OpenAI API, Anthropic API

## Relevance to our work
- **agentos** (2/3): MemoryMesh already combines BM25 and pgvector retrieval. The talk's schema-discovery-then-query pattern for relational questions is a gap RAG alone leaves open. → *Prototype a MemoryMesh path where the agent introspects a schema and runs deterministic queries for relational questions (e.g. open PRs touching a topic), and compare against BM25 + pgvector on a small set of relational queries.*
- **prosharness** (1/3): The repo-rules agent idea (find, dedupe and index rules files) applies to CLAUDE.md and rules files in ProsHarness workflows, but the talk does not add much beyond that. → *Run a quick scan of CLAUDE.md and any rules files across ProsHarness repos for duplicates and conflicting instructions, then decide whether an index is worth adding.*
- **general** (1/3): The paired with/without-context token comparison is a simple measurement method for context work, though the talk gives no details on the setup. → *Borrow the same-prompt, with-vs-without-context token comparison as a benchmark when evaluating any context or memory change.*
