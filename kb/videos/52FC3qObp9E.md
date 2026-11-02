# This Free Tool Makes Cursor 10x Smarter

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `52FC3qObp9E` · [watch](https://youtu.be/52FC3qObp9E) · **date:** 2025-11-02 · **length:** 4:39 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack, Upstash, Cursor
- **topics:** coding-agents, mcp-and-tools, context-engineering · **tags:** cursor, context7, mcp, documentation-retrieval, nextjs, stale-model-knowledge

> Better Stack demo: Cursor's built-in docs indexing misses newer APIs, so adding "use context7" to a prompt fetches current library docs through an MCP server. Install is a single npx entry.

## Summary
The presenter says Cursor's built-in documentation indexing is unreliable and that models lag behind fast-changing JavaScript libraries. A prompt asking for a Next.js 15.3 onNavigate handler, with the Next.js docs tagged in Cursor, still produced code using the older onClick pattern. Adding "use context7" to the same prompt made the model call the Context7 MCP tool, first resolving the library and then fetching docs for onNavigate, and the generated code followed the documented example. The server is an npx command that is added as a global MCP server in Cursor's settings. Context7 can also be used directly on its website: search a library, copy a snippet, and set a token limit. The presenter closes by saying documentation versioning is the feature they are most looking forward to. The whole evidence base is one Next.js API example.

## Key ideas
- **Cursor's built-in docs indexing is weak, and models lag behind fast-moving JS libraries, so generated code uses outdated APIs.** — The presenter says the indexing requires explicit prompting each time and that the models in use lack knowledge of recent library releases. ([0:00](https://youtu.be/52FC3qObp9E?t=0))
- **Tagging the official docs in Cursor did not steer the output. The code used the old onClick pattern instead of the Next.js 15.3 onNavigate handler the prompt asked for.** — Specificity in the prompt did not fix it. The presenter notes the docs for onNavigate had been published for about two weeks or more. ([0:59](https://youtu.be/52FC3qObp9E?t=59))
- **Adding 'use context7' to the prompt makes the model call the Context7 MCP tool: it resolves the library name first, then queries docs for the specific API.** — The fix is retrieval at generation time, not a different model. The presenter discards the first output and re-runs the prompt with the tool available. ([0:59](https://youtu.be/52FC3qObp9E?t=59))
- **The first retrieved result was a source-based example of onNavigate, and the generated code matched it closely.** — The presenter credits the result to Context7 returning concise, code-first snippets with no filler. The result is one example, not a measured comparison. ([2:06](https://youtu.be/52FC3qObp9E?t=126))
- **Setup is a single npx MCP entry added to Cursor's global MCP settings. Context7 indexes over 850 libraries, and users can request more.** — The presenter says the same tool can be used without MCP by searching the library on context7.com and copying the snippet. ([2:06](https://youtu.be/52FC3qObp9E?t=126))
- **Documentation versioning is the presenter's most anticipated feature. It would let developers request a specific doc version for legacy code.** — The presenter presents this as a future capability ('the one I'm looking forward to'), so it is not shown working in the video. ([3:18](https://youtu.be/52FC3qObp9E?t=198))

## Techniques
- **Install Context7 as a global MCP server in Cursor** — Open the Context7 GitHub README and copy the MCP config block, which launches the server with npx. In Cursor settings go to MCP, choose 'Add new global MCP server', and paste the block. The presenter notes the same block works in any MCP client. *When:* When an agent must write code against a library newer than the model's training data, or when the built-in docs index keeps producing old APIs.
- **Trigger doc retrieval with 'use context7' in the prompt** — End the prompt with 'use context7'. The model first resolves the library name through the MCP tool, then queries docs for the named API (here, onNavigate) before writing code. *When:* For prompts that name a specific new API, where the model would otherwise write from older memory. Discard the previous output and re-run the prompt instead of patching it.
- **Manual doc snippet pull without MCP** — On context7.com, open the library (Next.js in the demo), search for the API name ('onNavigate'), set the token count limit, and copy the returned snippet into the prompt. *When:* In a client without MCP support, or for a one-off lookup. The presenter warns that a higher token limit tends to bring back less relevant material, so tune the limit.

## Numbers
- Context7 indexes over 850 libraries, and the count is growing as users request new ones. ([2:06](https://youtu.be/52FC3qObp9E?t=126))
- The test API, Next.js onNavigate, is from Next.js 15.3, which Claude 3.5 Sonnet does not know about. ([0:00](https://youtu.be/52FC3qObp9E?t=0))
- The tagged Next.js docs had been published for about two weeks or longer before the test. ([0:59](https://youtu.be/52FC3qObp9E?t=59))
- Video length is 4:39, and the demo is a single prompt-and-result comparison with no timing or accuracy measurements. ([0:00](https://youtu.be/52FC3qObp9E?t=0))

## Hot takes
- The title's '10x Smarter' is not measured. The evidence is one Next.js API example, shown once with and without the tool.
- The framing is promotional: the tool is called 'completely free', and the video closes with a subscribe call. The transcript shows no sponsor disclosure, but it reads as a tool promo rather than an evaluation.
- The fix is retrieval, not a better model. Quality still depends on the library's docs being indexed correctly and on the model choosing to call the tool, which the presenter does not test.
- Documentation versioning is described as a future wish, not a shipped feature, so the legacy-code use case is not demonstrated.

## Tools mentioned
Cursor, Context7 (MCP server, run via npx; maintained by Upstash), Next.js 15.3 (onNavigate handler), Claude 3.5 Sonnet (model used in Cursor), MCP (Model Context Protocol), npx

## Relevance to our work
- **agentos** (1/3): Context7 is a retrieval service that returns version-specific code snippets to an agent on demand. This is adjacent to MemoryMesh's knowledge-bucket retrieval, but it is not a memory or RAG technique the talk explains. → *Read the Context7 README and check whether a library-scoped, token-capped snippet lookup is a useful pattern for MemoryMesh's knowledge-bucket API.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, and the talk shows a docs MCP server that works from an MCP client's config. A docs server could reduce outdated-API output in long unattended runs. → *Try adding a docs MCP server (Context7 is the one shown) to the Claude Code config used by ProsHarness runs, then measure how often generated code uses outdated APIs on a library released after the model's cutoff.*
