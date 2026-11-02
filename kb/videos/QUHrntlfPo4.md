# Claude Code is Expensive. This MCP Server Fixes It (Context Mode)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `QUHrntlfPo4` · [watch](https://youtu.be/QUHrntlfPo4) · **date:** 2026-04-02 · **length:** 6:09 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack
- **topics:** token-cost-efficiency, context-engineering, mcp-and-tools · **tags:** claude-code, context-mode, mcp, context-bloat, sqlite, fts5, compaction, session-continuity, token-savings, playwright

> Better Stack demo of Context Mode, a Claude Code MCP plugin that indexes large tool outputs in local SQLite FTS5 and keeps a small snapshot across compaction. Practical, with one small measured example.

## Summary
The video argues that Claude Code MCP tool calls dump full outputs into the 200k context window, so context fills and compacts fast (the speaker cites about 30 minutes in some cases). It presents Context Mode as a virtualization layer: the agent talks to a sandbox, and large outputs are chunked into a local SQLite FTS5 index so the model receives only a confirmation and searches on demand. The headline example is a 56 KB Playwright snapshot reduced to 299 bytes. Context Mode also uses hooks on file edits, git operations and subagent tasks to build a priority-tiered snapshot (usually under 2 KB) that is reinjected after compaction, and it records decisions and errors so failed fixes are not repeated. Installation is a Claude Code marketplace add plus plugin install, or an npm install with a settings config for Gemini CLI and VS Code Copilot. The demo indexes a generated 5,000-line access log with 500 errors, finds the error IPs, and shows about 1,200 tokens (roughly 25%) kept out of context, with the speaker extrapolating to around 100,000 tokens on large repos.

## Key ideas
- **MCP tool output is the context-bloat problem** — Each MCP tool call dumps its full output into the 200k window. The speaker cites a 56 KB Playwright snapshot and 59 KB for 20 GitHub issues, and claims planning-phase reads can use about 70% of the window before any code is written. ([0:00](https://youtu.be/QUHrntlfPo4?t=0))
- **Index outputs in a sandbox instead of returning them** — Context Mode puts the agent behind a sandbox. Large outputs are chunked into a local SQLite FTS5 full-text index, and the model gets only a confirmation and runs searches against it. ([1:17](https://youtu.be/QUHrntlfPo4?t=77))
- **Compaction snapshot for session continuity** — Hooks watch file edits, git operations and subagent tasks. On compaction, a priority-tiered snapshot, usually under 2 KB, is reinjected. The speaker presents this as a save checkpoint and claims it could stretch sessions from about 30 minutes to around 3 hours (not measured in the video). ([1:17](https://youtu.be/QUHrntlfPo4?t=77))
- **Error and decision memory across resets** — The tool tracks decisions and errors, so an approach that failed 20 minutes earlier is not retried after the context resets. ([2:30](https://youtu.be/QUHrntlfPo4?t=150))
- **Install paths differ by host** — On Claude Code: add the Context Mode marketplace, then run the plugin install command, and the MCP server, hooks and routing instructions are configured automatically. On Gemini CLI or VS Code Copilot: npm install context-mode and add the config to settings. ([2:30](https://youtu.be/QUHrntlfPo4?t=150))
- **Measured saving on a small file is modest** — The demo indexes a 5,000-line access log (every 100th line a 500). Claude receives only the indexing confirmation. Stats show about 20 KB of raw data would have entered the conversation, roughly 5 KB stays in the sandbox, about 1,200 tokens are spared, and the overall reduction is about 25%. ([3:29](https://youtu.be/QUHrntlfPo4?t=209))
- **Savings compound because raw data is resent every turn** — Data left in the conversation is resent with every message. Keeping it in the sandbox extends session life, and the speaker extrapolates that large repo or log analyses could save around 100,000 tokens. ([4:54](https://youtu.be/QUHrntlfPo4?t=294))

## Techniques
- **Index large tool output into a local FTS5 store** — Route big tool results (page snapshots, CSVs, logs, issue lists) into a local SQLite database with FTS5 full-text indexing. Return only a confirmation or a summary to the model, then answer questions with targeted searches over the index. *When:* Any MCP or shell call whose output is much larger than the answer it needs, such as log analysis, browser snapshots, or bulk issue reads.
- **Priority-tiered snapshot injected on compaction** — Capture session events with hooks (file edits, git operations, subagent tasks, decisions, errors). When the conversation compacts, reinject a small priority-ordered snapshot (about 2 KB in the video) so the agent keeps track of recent work. *When:* Long coding sessions where compaction causes the agent to forget files, tasks, or decisions made earlier.
- **Remember failed attempts across resets** — Log errors and failed fixes into the persistent session store, and have the snapshot carry them so the agent does not repeat an approach that already failed. *When:* Debugging loops in long sessions where the agent retries the same broken fix after compaction.
- **Install Context Mode in Claude Code** — Add the Context Mode plugin marketplace with the command shown in the video (exact command not legible in the captions), then run the plugin install command. The plugin configures the MCP server, hooks and routing instructions itself. *When:* Claude Code users who want the indexing and snapshot behavior without manual config.
- **Install Context Mode in Gemini CLI or VS Code Copilot** — Run npm install for the context-mode package and add its config block to the editor or CLI settings file. Config keys are not shown in the video. *When:* Using Gemini CLI or VS Code Copilot instead of Claude Code.
- **Measure the savings with the stats command** — Run the Context Mode stats command in the session to see how many bytes and tokens were kept in the sandbox instead of entering the context window. The command name is garbled in the auto-captions. *When:* Checking whether the tool actually saves tokens for a given workload before relying on it.
- **Demo prompt for indexed log analysis** — Generate a dummy access log (a Python script writes 5,000 API request lines, every 100th a 500 error). Prompt Claude: use context mode to index access.log, then find all 500 error patterns and summarize the associated IP addresses. *When:* Reproducing the demo or testing the index-and-search flow on a log file.

## Numbers
- Claude Code context window of 200k tokens, which MCP output fills ([0:00](https://youtu.be/QUHrntlfPo4?t=0))
- A single Playwright page snapshot is about 56 KB ([0:00](https://youtu.be/QUHrntlfPo4?t=0))
- Reading 20 GitHub issues is about 59 KB ([0:00](https://youtu.be/QUHrntlfPo4?t=0))
- Speaker says planning-phase reads can consume about 70% of the window before any code is written; in some scenarios context compacts after about 30 minutes ([0:00](https://youtu.be/QUHrntlfPo4?t=0))
- Playwright snapshot reduced from 56 KB to 299 bytes (99% reduction) ([1:17](https://youtu.be/QUHrntlfPo4?t=77))
- Analytics CSV reduced to 222 bytes (near 100% reduction) ([1:17](https://youtu.be/QUHrntlfPo4?t=77))
- Compaction snapshot usually under 2 KB ([1:17](https://youtu.be/QUHrntlfPo4?t=77))
- Claimed session extension from about 30 minutes to about 3 hours (not measured in the video) ([1:17](https://youtu.be/QUHrntlfPo4?t=77))
- Demo access.log has 5,000 lines with every 100th line a 500 error ([2:30](https://youtu.be/QUHrntlfPo4?t=150))
- Demo: about 20 KB raw would have entered the conversation; about 5 KB kept in sandbox; about 1,200 tokens spared; about 25% reduction on this small test ([3:29](https://youtu.be/QUHrntlfPo4?t=209))
- Speaker extrapolates savings on larger repo or log analyses to about 100,000 tokens (not measured) ([4:54](https://youtu.be/QUHrntlfPo4?t=294))

## Hot takes
- The 99% reduction is one cherry-picked Playwright snapshot. The only measured result in the demo is about 25% on a 20 KB file.
- The 30-minute to 3-hour session extension and the 100,000-token figure are extrapolations, not benchmarks.
- The framing ('Claude Code is expensive') is a product pitch. The video shows no comparison against baseline sessions, no latency cost, and no accuracy check on whether searching the index loses information.

## Tools mentioned
Claude Code, Context Mode, SQLite, FTS5, Playwright, GitHub, Gemini CLI, VS Code Copilot, npm, Python

## Relevance to our work
- **prosharness** (2/3): ProsHarness does checkpoint/resume of long Claude Code runs. Context Mode's hook-driven, under-2 KB snapshot reinjected after compaction is a direct comparison point for what state a resume should carry. → *Read Context Mode's compaction snapshot design (which events it captures, how it tiers them, the size budget) and compare it with ProsHarness's checkpoint format to see what a resume needs beyond the transcript.*
- **agentos** (1/3): Indexing tool output with BM25/FTS5 instead of returning it is the same idea as MemoryMesh's hybrid retrieval, applied to tool results rather than knowledge buckets. → *Benchmark whether MemoryMesh's BM25 leg could serve as the store for oversized tool outputs, measuring bytes kept out of context and retrieval hit rate.*
