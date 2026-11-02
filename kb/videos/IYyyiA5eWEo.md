# Stack Overflow for your LLMs (and you!)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `IYyyiA5eWEo` · [watch](https://youtu.be/IYyyiA5eWEo) · **date:** 2025-11-02 · **length:** 4:48 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, GitHub, Anthropic, Cursor
- **topics:** coding-agents, mcp-and-tools, rag-retrieval · **tags:** grep.app, code search, MCP, Claude Code, Cursor, hallucinated APIs, up-to-date library usage, regex, secret scanning

> A short Better Stack tool walkthrough of grep.app, a fast regex code search over GitHub, and its MCP server, which lets Claude Code or Cursor pull real library usage into context instead of hallucinating APIs.

## Summary
The presenter pitches grep.app as a Stack Overflow replacement for niche, new, or poorly documented libraries, where LLMs tend to invent code. He demos literal and regex search over millions of GitHub repositories that returns results as he types, with filters for repo, path, and language. He shows a regex used to find hardcoded OpenAI keys in public repos, and notes security researchers use the same approach to find packages with known vulnerabilities. He also uses it to find current usage of packages newer than an LLM's training data, such as React Router v7. The grep.app MCP server lets an agent search GitHub on its own; the tool description tells the model when to call it, and the user can approve it once with "don't ask again". In the demo, Claude Code searched for the Lexical convert-from-markdown function, looked at real projects, and then wrote working code in Cursor. The video is short and mostly a demo with no benchmarks.

## Key ideas
- **Use real code search as a stand-in for Stack Overflow when docs are thin, since LLMs hallucinate niche or new APIs.** — The speaker's core claim: grep.app over GitHub gives real usage examples to load into the model's context, so the agent writes correct code for the Lexical convert-from-markdown function. ([0:00](https://youtu.be/IYyyiA5eWEo?t=0))
- **Search is literal and very fast, with filters for repo, path, and language.** — Results update on every keystroke across millions of repos. Filtering by repo narrows to official examples (e.g. the Lexical repo) and by path (e.g. app/ for Next.js app router) narrows to a project structure. ([0:00](https://youtu.be/IYyyiA5eWEo?t=0))
- **Regex search finds hardcoded secrets, and security researchers use it to find vulnerable dependencies.** — A regex for OpenAI API keys returned several public-repo hits, including test fixtures. The speaker says researchers also search for outdated, vulnerable package versions; he does not recommend that unless the vulnerability is reported. ([1:13](https://youtu.be/IYyyiA5eWEo?t=73))
- **Search for version-specific usage when the model's training data is out of date.** — Google and LLMs gave poor results for React Router v6 and the newer v7. Searching for the new version surfaces projects already on it, showing how they structure the code. ([2:11](https://youtu.be/IYyyiA5eWEo?t=131))
- **Expose the search as an MCP server so the agent calls it without being asked.** — The grep.app MCP tool description says it searches literal code patterns and when to use it (unfamiliar APIs, unsure of syntax). The agent picked it up automatically and sent the search with the user's project languages (TypeScript, JavaScript). ([2:11](https://youtu.be/IYyyiA5eWEo?t=131))
- **Agent output after the search is grounded in the retrieved repos.** — After a one-time approval, the agent found Payload CMS, Facebook Lexical and other projects, explained how to call the function, and then implemented it in Cursor. The speaker presents this as the reason LLMs stop inventing niche APIs. ([3:20](https://youtu.be/IYyyiA5eWEo?t=200))

## Techniques
- **Add grep.app as an MCP server in Cursor or Claude Code** — Cursor: add the server entry to mcp.json. Claude Code: run an add command from the CLI. The exact JSON and CLI command are not shown on screen; check the grep.app docs. Approve the search tool once with 'don't ask again'. *When:* When the coding agent needs real usage of an unfamiliar or fresh library and you don't want to paste examples by hand.
- **Literal and regex code search with filters** — Type the function name (e.g. convert from markdown) to see results as you type. Filter by repo (e.g. the official Lexical repo), path (e.g. app/ for Next.js app router) and language (e.g. JSON). Turn on match case, match whole words, or regex. *When:* Finding how a specific function, config key or file layout is used in real projects before writing code.
- **Version-specific search for new packages** — Search for the new major version string or API (the demo used 'react router v7') and read the projects already on it, instead of relying on web search or model memory. *When:* A package has shipped breaking changes after the model's training cutoff.
- **Regex to detect committed secrets (defensive use)** — Paste a provider key regex (the demo used an OpenAI key pattern) into the regex search to see public repos with leaked keys. The speaker blurred the results and did not share the regex itself. *When:* Auditing your own org's public repos for leaked credentials, or security research tied to responsible disclosure.

## Numbers
- Searches millions of GitHub repositories with results updating on every keystroke (speaker's description, not measured). ([0:00](https://youtu.be/IYyyiA5eWEo?t=0))
- Regex search for an OpenAI API key format returned several public GitHub hits; some were test fixtures. ([1:13](https://youtu.be/IYyyiA5eWEo?t=73))

## Hot takes
- 'Stack Overflow is dead' and 'the perfect replacement for Stack Overflow' oversell what is really a code search engine. It finds usage examples; it does not answer questions.
- Hype framing ('honestly insane', 'blows my mind') with no latency or accuracy measurements. Speed is shown only as a live demo.
- Mentions security researchers scanning for vulnerable package versions, and says he would not do it unless reporting the issue.

## Tools mentioned
grep.app, GitHub, Claude Code, Cursor, MCP, Lexical, Next.js, React Router, Payload CMS

## Relevance to our work
- **agentos** (1/3): Code search over public repos is a retrieval source for coding agents. It is a different layer from MemoryMesh's hybrid retrieval over knowledge buckets. → *Compare a grep.app-style code-search MCP against MemoryMesh's BM25 + pgvector retrieval on niche-library questions, and note whether results beat the model's own knowledge.*
- **prosharness** (1/3): ProsHarness runs the Claude Code CLI, and adding an MCP code-search server to those runs would help with unfamiliar-library tasks. → *Test adding a grep.app-style MCP server to the Claude Code config ProsHarness launches, then check whether it reduces hallucinated APIs on a sample task.*
