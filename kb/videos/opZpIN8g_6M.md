# Claude Just Solved Their Biggest Problem

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `opZpIN8g_6M` · [watch](https://youtu.be/opZpIN8g_6M) · **date:** 2025-12-02 · **length:** 9:24 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic, Cloudflare
- **topics:** mcp-and-tools, context-engineering, token-cost-efficiency, sandboxing-execution · **tags:** MCP, MCP as code, context window, progressive disclosure, tool definitions, code execution, sandboxing, memory tool, skills, Cloudflare code mode

> Walkthrough of Anthropic's paper on running MCP servers as code files instead of direct tool calls, to cut context bloat; no implementation shown.

## Summary
The speaker explains why MCP tool definitions and tool-call results both consume context window even when unused, using a measurement of three connected MCP servers that took about 10% of the window before any messages. He then summarizes Anthropic's proposed fix: expose each MCP server as a folder of code files (one file per tool, plus an index file) that the agent navigates and loads on demand. The claimed benefits are progressive disclosure, shaping large results in code before they reach the model, control flow in code instead of model-sequenced calls, privacy by returning placeholder values, and file-based state through the memory tool. He notes the trade-off: agent-generated code needs sandboxing, resources and monitoring, so token savings are paid for with infrastructure complexity. He credits Cloudflare's earlier "code mode" as the same idea. The video gives no commands or config, and the last part is an unrelated AI Labs hackathon recap.

## Key ideas
- **MCP tool definitions occupy context even when no task uses them** — Each connected MCP's tools stay exposed to the model from the start. In the speaker's test, three MCPs used about 10% of the window with zero tokens of messages, and he expects it to grow with more servers. ([0:00](https://youtu.be/opZpIN8g_6M?t=0))
- **Tool-call results also stay in context and bloat it** — Results from MCP calls remain in the window after the call, so large outputs add up. The speaker says this can take more space than the user's actual messages. ([0:00](https://youtu.be/opZpIN8g_6M?t=0))
- **Anthropic's proposed fix is to present MCP servers as code files** — Instead of direct tool calls, each MCP server becomes a folder of code files in a servers directory, with one file per tool and an index file listing what is available. The agent reads files on demand rather than carrying every schema. ([1:23](https://youtu.be/opZpIN8g_6M?t=83))
- **Progressive disclosure: the agent loads only the tool files it needs** — The agent uses the file tree and file names to find the right tool, reads index.ts for the catalogue, and loads only the specific tool file. The speaker notes Cloudflare proposed a similar idea earlier, which it called code mode, converting MCP tools to a TypeScript API. ([2:32](https://youtu.be/opZpIN8g_6M?t=152))
- **Shape large tool results in code before the model sees them** — Code can transform or aggregate a large response and return only the needed slice. His example is a 10,000-row spreadsheet read, where only the first five rows go to the model. ([3:39](https://youtu.be/opZpIN8g_6M?t=219))
- **Move control flow out of the model and into code** — Today the model sequences tool calls one by one. With code, conditionals, checks and loops run in the script, which avoids chaining model turns. The speaker claims this also reduces hallucinations, without evidence in the video. ([3:39](https://youtu.be/opZpIN8g_6M?t=219))
- **Privacy: the model only sees what the code logs or returns** — Sensitive data can stay in the execution environment. The code can return generic or placeholder values so the agent can work without the raw database contents. ([5:02](https://youtu.be/opZpIN8g_6M?t=302))
- **State persists as files, similar to Claude skills** — With the memory tool, the agent can save working code and intermediate results to files and resume where it stopped. The speaker compares this to skills, which are also file-based and loaded on demand, though skills hold broader multi-resource bundles. ([5:02](https://youtu.be/opZpIN8g_6M?t=302))
- **The trade-off is token savings versus sandboxing and infrastructure complexity** — Running agent-generated code needs a secure sandbox with resource limits and monitoring. Lower token cost and latency come with this operational burden, which he frames as a choice. ([6:13](https://youtu.be/opZpIN8g_6M?t=373))

## Techniques
- **Filesystem-based MCP tool catalogue with progressive disclosure** — Generate a servers/<mcp-server>/ folder with one code file per tool and an index file that exposes every tool name and definition. The agent reads the index, then loads only the tool file it needs. The video does not show code or config. *When:* Use when several MCP servers are connected and their tool schemas dominate the context window before any work starts.
- **Result shaping inside the execution script** — Have the code call the tool, then filter, aggregate or slice the output (for example, first N rows or a summary) and return only that to the model, so the full payload never enters context. *When:* Use when a tool returns large data such as tables, query results or logs that the model only needs to inspect in part.
- **Code-owned control flow between tool calls** — Write conditionals, loops and checks in the generated code that calls several tools in sequence, so the model is not asked to decide each step. *When:* Use for deterministic multi-step pipelines where the branching logic is known in advance and each model turn is expensive.
- **Placeholder returns for sensitive data** — Make the code log or return only generic or redacted values, so the agent sees the shape of the result but not the underlying records. *When:* Use when the agent works against a database or other source that holds private data it should not read directly.
- **File-based state for resumable runs** — Use the memory tool to save working code and intermediate outputs as files, so the agent can resume a task from the saved state rather than replaying the whole conversation. *When:* Use for long multi-step tasks where a context reset or interruption would otherwise lose progress.

## Numbers
- Three connected MCP servers consumed about 10% of the context window before any user messages (messages were 0%). ([0:00](https://youtu.be/opZpIN8g_6M?t=0))
- Example: a Google Sheets tool call returning 10,000 rows, where the code would pass only the first 5 rows to the model. ([3:39](https://youtu.be/opZpIN8g_6M?t=219))

## Hot takes
- The title, 'Claude Just Solved Their Biggest Problem', overstates it: this is a summary of an Anthropic write-up on an approach, with no benchmark and no implementation.
- The speaker's 10% figure comes from his own setup with three MCPs and is not a general measurement.
- He states that code-based control flow reduces hallucinations, but offers no evidence for that.
- He credits Cloudflare with the same idea earlier, so the 'new' part is mostly the framing.
- The final 2 minutes are an unrelated AI Labs hackathon recap.

## Tools mentioned
MCP (Model Context Protocol), Claude, Claude skills, Memory tool, Cloudflare code mode, TypeScript, index.ts (file convention from the paper)

## Relevance to our work
- **agentos** (2/3): Crucible already plans opt-in sandboxed code execution, which the MCP-as-code approach requires. The Scout proxy is also a natural place to measure per-request context and tool-definition tokens. → *Prototype MCP-as-code for two MCP servers in Crucible's sandbox, then compare tool-definition tokens per request with and without the file-tree approach through the Scout proxy.*
- **prosharness** (1/3): ProsHarness wraps Claude Code and checkpoints long runs. MCP tool definitions and results inflate those checkpoints, but the video gives no implementation details. → *Measure how much context MCP tool definitions take in a long ProsHarness run before checkpointing, and consider deferring servers the run does not use.*
