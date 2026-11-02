# Agentic Search for Context Engineering — Leonie Monigatti, Elastic

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ynJyIKwjonM` · [watch](https://youtu.be/ynJyIKwjonM) · **date:** 2026-05-18 · **length:** 1:03:13 · **format:** workshop · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Leonie Monigatti · **orgs:** Elastic
- **topics:** rag-retrieval, context-engineering, mcp-and-tools, skills-self-improvement · **tags:** agentic-search, agentic-rag, tool-design, tool-descriptions, es-ql, elasticsearch, agent-skills, progressive-disclosure, shell-tool, grep, semantic-grep, langchain, low-floor-high-ceiling, context-window, live-demo

> Leonie Monigatti (Elastic) argues context engineering is mostly agentic search, then walks through live demos of semantic search, ES|QL query tools, skill loading, and grep-style shell search, and when to use each.

## Summary
The speaker argues that context engineering depends mainly on the search tools that decide what enters the context window, and calls that about 80% agentic search. She traces the move from fixed RAG pipelines to agentic RAG, then to many context sources (local files, skills, databases, web, memory) that each need their own search tool. She lists three common failures: the agent skips the tool, picks the wrong tool, or writes bad parameters. Her live demos use LangChain with a semantic search tool (top-k 3), which fails on a loosely related query. A general ES|QL query tool does better, but the agent writes a wildcard the wrong way and gets zero results. Adding a skill that the agent must load first fixes it. She then shows shell and grep search over a folder of session files, notes that agents cheat at semantic search by chaining synonyms, and suggests a semantic grep CLI for fuzzy queries. Her closing advice is to mix specialized tools (low floor) with general tools (high ceiling), start general, and log tool calls, since four or five calls per question signals a tool that is too hard to use.

## Key ideas
- **Context engineering is mostly the search tool choice** — The speaker says the real work is the search tool that decides what moves from context sources into the window, so she calls context engineering about 80% agentic search. ([1:14](https://youtu.be/ynJyIKwjonM?t=74))
- **Fixed RAG pipelines are replaced by agentic RAG** — A fixed pipeline retrieves whether or not context is needed and can confuse the model. Giving the agent a search tool lets it decide if, when, and how often to search, which handles multi-hop questions. ([2:31](https://youtu.be/ynJyIKwjonM?t=151))
- **Context spans many sources, each needing its own search tool** — Local files, skills, databases, web and memory each have different native tools. A shell tool (bash or exec) can also search across them, since the agent can run ls, grep, or curl. ([4:57](https://youtu.be/ynJyIKwjonM?t=297))
- **Three failure modes: no tool call, wrong tool, bad parameters** — The agent may answer from memory without searching, call the web tool instead of the database tool, or generate parameters the tool cannot use. The speaker says these show up in most production agent builds at Elastic. ([9:09](https://youtu.be/ynJyIKwjonM?t=549))
- **Tool descriptions need trigger conditions and ordering, not one sentence** — Start with the core purpose. If the agent still picks the wrong tool, add when to use it, when not to use it, and which tool or skill must come first. Reinforce the same rules in the system prompt. ([10:09](https://youtu.be/ynJyIKwjonM?t=609))
- **Zero results can be a failure, not an answer** — The agent wrote an ES|QL query using the SQL percent wildcard, which matched nothing. The speaker says teams should check whether an empty result is valid or means the query was wrong. ([27:17](https://youtu.be/ynJyIKwjonM?t=1637))
- **Skills with progressive disclosure fix hard query languages** — Only the skill name and description go into the system prompt. The agent loads the full body when needed. The tool description and system prompt then both say to load the skill before calling the query tool, which fixed the wildcard error. ([28:46](https://youtu.be/ynJyIKwjonM?t=1726))
- **Let the query engine do counting and aggregation** — Counting sessions for a date through an ES|QL aggregation avoids pulling a long list into the context window, and the speaker says LLMs are poor at counting. ([32:27](https://youtu.be/ynJyIKwjonM?t=1947))
- **Shell grep fails at semantics, and a semantic grep CLI helps** — Agents chain synonyms like compliance, GDPR and governance to find regulation talks. The speaker suggests a semantic grep CLI for fuzzy queries, with a rule to use plain grep for exact matches. ([39:31](https://youtu.be/ynJyIKwjonM?t=2371))
- **Mix low-floor specialized tools with high-ceiling general tools, then log** — Specialized tools are reliable for common operations. General tools (query or shell) handle unexpected questions. Start general, log behaviour, and build specialized tools when a question takes four or five calls. ([45:19](https://youtu.be/ynJyIKwjonM?t=2719))

## Techniques
- **Layered tool descriptions** — Write the purpose first. Add trigger conditions, a when-not-to-use line, and ordering rules such as 'load this skill before calling this tool'. Repeat the key rules in the system prompt if the agent still ignores them. *When:* Several search tools are available, or the agent keeps calling the wrong one or skipping tools.
- **Errors returned to the agent** — Wrap the query tool in try/except and return the error text as the tool result, so the agent can rewrite the query instead of crashing the run. *When:* The tool takes a complex query language such as SQL or ES|QL, where generated queries often fail.
- **Progressive disclosure for skills** — Put only name and description from each skill's front matter in the system prompt. Load the full body into context when needed. The speaker says the framework also offloads skill bodies after use as context fills. *When:* Query syntax needs more documentation than a one-line tool description can hold, and the context window must stay small.
- **Outsource aggregation to the search engine** — Give the agent an aggregation-capable query tool so filtering and counting run inside the database, and only the result comes back to the model. *When:* The question asks for counts, sums, or filtered lists that would fill the context window.
- **Shell tool with semantic grep** — Give the agent a shell tool and install a semantic grep CLI. Describe in the system prompt when to use exact grep and when to use semantic grep, with an example command. *When:* Local files or a folder of documents hold the context, and fuzzy or synonym-heavy queries are common.
- **Hybrid shell plus database verification** — Describe a pattern from a Vercel blog post the speaker cites: the agent queries the database first, then checks the results with the shell tool. The speaker says this hybrid gave the highest accuracy in that test. *When:* Analytical queries where database answers need a second check against raw files.
- **Log tool calls to find where specialization is needed** — Record the tool calls per question. Four or five calls for a routine question means the tool is too hard to use, so look at the queries the agent is trying to solve and add a specialized tool for them. *When:* A general-purpose tool is deployed and the team does not yet know the real query patterns.
- **Use the file store as memory and offload old results** — Keep tool outputs in a file store and let the agent grep earlier results instead of holding them in the window. Offload skill bodies and compact context as the session grows. *When:* Long agent sessions where accumulated tool results and skills push the context window toward its limit.

## Numbers
- The first semantic search tool returns top-k = 3 results. The speaker says this limit is deliberate foreshadowing of its narrow scope. ([18:12](https://youtu.be/ynJyIKwjonM?t=1092))
- Demo models: GPT-5.4 nano for the semantic search and shell demos. GPT-5.4 mini was chosen for the ES|QL query tool because writing queries was expected to be harder. ([23:30](https://youtu.be/ynJyIKwjonM?t=1410))
- A semantic grep run returned top-k = 10 results, and the correct session came back first. ([42:32](https://youtu.be/ynJyIKwjonM?t=2552))
- An ES|QL aggregation counted 27 sessions on April 8, so the agent did not need to list them all in context. ([32:27](https://youtu.be/ynJyIKwjonM?t=1947))
- Four or five tool calls per question is named as a sign the tool is too hard for the agent. This is the speaker's rule of thumb and is not measured. ([46:45](https://youtu.be/ynJyIKwjonM?t=2805))
- In internal testing at Elastic, a more capable model cut parameter error rates by a 'very big amount'. No figures were given. ([44:01](https://youtu.be/ynJyIKwjonM?t=2641))

## Hot takes
- Context engineering is about 80% agentic search.
- The tool description is the most important part of a search tool, yet teams usually write it as one sentence.
- Doing good search is incredibly difficult, so you need a curated set of search tools, not one silver bullet.
- A zero-result search may be a failure mode, not a valid answer.
- Agents are notoriously bad at counting, so let the query engine count.
- Agents cheat at semantic search with grep by chaining synonyms, which is not the most efficient approach.
- Patching a prompt for each new query error is a band-aid; full documentation belongs in a skill.

## Tools mentioned
LangChain, Elasticsearch, ES|QL, Jina embeddings v5, Jina grep (captioned as Gina grep), OpenAI GPT-5.4 nano and mini, shell / bash tool, Claude Code, OpenClaw (captioned as OpenCloud, exec tool)

## Relevance to our work
- **agentos** (2/3): MemoryMesh already does hybrid retrieval (BM25 and pgvector) and GraphRAG, so the talk's lessons on tool design, zero-result handling, and tool-call logging apply directly to its retrieval tools. → *Add a per-question tool-call counter and a zero-result flag to the MemoryMesh retrieval path, then review any question that takes four or more calls to decide whether a specialized retrieval tool is needed.*
- **prosharness** (1/3): The harness loads skills and runs long agent sessions, so the progressive-disclosure and skill-offloading pattern from the talk may help keep the context window small. → *Check whether ProsHarness puts only skill names and descriptions in the system prompt and unloads skill bodies after use, then test it on a long checkpointed run.*
