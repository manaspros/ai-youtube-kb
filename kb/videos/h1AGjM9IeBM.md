# Claude Code SDK: Build Real AI Apps with Python & MCP

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `h1AGjM9IeBM` · [watch](https://youtu.be/h1AGjM9IeBM) · **date:** 2025-11-02 · **length:** 8:25 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Cursor, GitHub
- **topics:** claude-code, coding-agents, mcp-and-tools, pr-code-review · **tags:** claude-code-sdk, subprocess, python, query, ClaudeCodeOptions, max_turns, mcp-config, github-actions, issue-to-pr, agentic-coding, doc-ingestion-gap

> A short walkthrough of the Claude Code SDK (Python, with the docs' example script and a GitHub Actions demo) that frames Claude Code as a programmable subprocess. The example broke for the speaker, and the video shows no working SDK run beyond that.

## Summary
The host presents the Claude Code SDK as a way to run Claude Code as a subprocess from scripts or applications, available through the command line, TypeScript and Python. They contrast plain AI coding with agentic coding, where the tool chooses among built-in tools (ls, read, edit and others) to finish a task. They argue that Claude Code's inclusion in the $20 Pro plan makes it cheaper than API-metered modes in Cursor, though no usage numbers are shown. The Python walkthrough copies the docs' example, which asks Claude to write a haiku about foo.py; the speaker says it broke after a Python SDK update and that their workaround only partly works. They explain that query() starts an instance, ClaudeCodeOptions sets max_turns, and results come back as structured message objects that have to be parsed. The main demo is a GitHub Actions workflow in which mentioning Claude on an issue implements a dark-mode feature in a small notes app, with a to-do list and a file-change summary. The closing idea, not built, is wiring Jira and Slack MCP servers to a PR-review and ticket-assignment flow. The video ends with a note that Claude Code lacks Cursor's built-in doc-URL ingestion.

## Key ideas
- **The SDK exposes Claude Code as a callable subprocess, so scripts or full apps can embed a coding agent.** — Available through the CLI, TypeScript and Python. The prompt inside your code can direct the agent to do any task. The speaker presents this as the main shift from using Claude Code interactively to programming it. ([0:00](https://youtu.be/h1AGjM9IeBM?t=0))
- **Agentic coding differs from plain AI coding because the agent chooses and sequences tools.** — For a file edit, the speaker describes Claude Code running ls, then fetching contents, then read, then edit. The speaker says Claude Code has 11 built-in tools (stated on screen, not enumerated in the transcript). ([1:16](https://youtu.be/h1AGjM9IeBM?t=76))
- **The speaker's cost argument is that Claude Code fits a flat $20 Pro subscription, while Cursor's max mode is API-metered.** — This is the speaker's assertion. No token counts, prices or measured spend are given, and the claim is not checked against plan limits. ([2:16](https://youtu.be/h1AGjM9IeBM?t=136))
- **The Python API has three parts: query() to start an instance, ClaudeCodeOptions to configure it, and structured messages to parse.** — The example sets max_turns, which caps how many times the agent builds on its own responses. Output is not plain text, so the caller must extract content from message objects. ([3:21](https://youtu.be/h1AGjM9IeBM?t=201))
- **The official example script broke after a Python SDK update, and the speaker's workaround only partly works.** — The speaker reports that the output is still wrong after the fix and hopes for an upstream update. The video does not show a clean end-to-end SDK run. ([3:21](https://youtu.be/h1AGjM9IeBM?t=201))
- **MCP configuration lets programmatic Claude Code instances use external MCP servers.** — The speaker calls this the most important capability. The config format is not shown, so the video does not show how to set it up. ([4:40](https://youtu.be/h1AGjM9IeBM?t=280))
- **The GitHub Actions demo runs Claude on a PR or issue. Mentioning Claude in a comment triggers it to implement the requested feature.** — The demo turns an issue asking for dark mode into a branch with the change. The run shows a to-do list and a summary of files created or modified. The speaker then checks out the branch and confirms the toggle works. ([4:40](https://youtu.be/h1AGjM9IeBM?t=280))
- **The speaker proposes an unbuilt workflow that chains PR review, Jira ticketing and Slack-triggered assignment through MCP.** — The idea is that a review produces a Jira ticket automatically, and a Slack mention assigns tickets to Claude. Nothing in the video implements or tests this flow. ([6:53](https://youtu.be/h1AGjM9IeBM?t=413))
- **Claude Code has no built-in way to ingest documentation from a URL, unlike Cursor.** — The speaker's workarounds are to download the docs as markdown and reference them, or to add the docs in Cursor. They say the markdown route uses too much context, so they recommend Cursor for doc-heavy work. ([7:40](https://youtu.be/h1AGjM9IeBM?t=460))

## Techniques
- **Run Claude Code as a subprocess from Python** — Create a venv, activate it, and install the SDK with the pip command from the docs prerequisites (the exact package name is shown on screen, not spoken). Copy the docs example into main.py. It imports query, ClaudeCodeOptions and message types, passes the prompt to query() with ClaudeCodeOptions(max_turns=...), and iterates the structured message objects to pull out text. Create foo.py (the speaker uses a Fibonacci script) and run main.py. *When:* When a script or backend needs a coding agent as one step. Pair it with a bounded max_turns and expect to parse messages yourself.
- **Cap agent iterations with max_turns** — Set max_turns in ClaudeCodeOptions. The speaker describes it as the number of times the agent can build on its own response. *When:* When you need a hard stop on an agent run, for cost or loop control in automated jobs.
- **Attach external MCP servers to programmatic Claude Code** — Configure MCP servers for the SDK instance so the agent can call external tools. The speaker does not show the config format, so check the docs before using it. *When:* When an automated agent needs live systems such as Jira, Slack or internal APIs.
- **Mention-triggered issue-to-PR workflow in GitHub Actions** — Install the Claude Code GitHub Actions workflow. Write the feature request as an issue. Mention Claude in a comment to trigger the run. Claude reads the issue and the codebase, works through a to-do list, commits changes to a branch, and posts a summary of files changed. Review and merge the branch like any other PR. The workflow file and setup steps are not shown. *When:* For small, well-specified feature or bug issues in a repo where a human reviews the branch before merging.

## Numbers
- Claude Code has 11 built-in tools (speaker's statement, shown on screen). ([1:16](https://youtu.be/h1AGjM9IeBM?t=76))
- Claude Code is available on the $20 Pro plan, which the speaker compares with API-metered max mode in Cursor. No usage or cost figures are given. ([2:16](https://youtu.be/h1AGjM9IeBM?t=136))
- max_turns sets how many times the agent can build on its own response. No value is given in the video. ([3:21](https://youtu.be/h1AGjM9IeBM?t=201))
- The dark-mode demo was run from an issue on a small notes app. No timing or cost is shown for the run. ([4:40](https://youtu.be/h1AGjM9IeBM?t=280))

## Hot takes
- Thin content: most of the 8 minutes is reading the docs and describing features. The SDK example is never shown working.
- The hype intro ('completely changed', 'the future of software engineering', '10 times more powerful') is not backed by measurements.
- The cost claim (Pro plan beats Cursor max mode) is asserted without numbers.
- The Jira/Slack ticketing flow is a proposal, not a demo.
- The only end-to-end proof is one dark-mode toggle in a toy notes app.
- The speaker's own closing note concedes that Claude Code lacks Cursor's doc-URL ingestion, which is a real gap for SDK builders.

## Tools mentioned
Claude Code, Claude Code SDK (Python, TypeScript, CLI), ClaudeCodeOptions, query(), Cursor, GitHub Actions, Claude Code GitHub Actions workflow, Jira MCP server, Slack MCP server, pip

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI as a harness. This video shows the programmatic subprocess route (query, ClaudeCodeOptions, max_turns, MCP config) that a harness would sit on, and the speaker reports a breaking SDK update. → *Compare ProsHarness's CLI wrapper against the SDK's query()/max_turns/structured-message model, and pin the SDK version to avoid the breakage the speaker hit.*
- **agentos** (1/3): AgentOS proxies agent traffic via a base URL and tracks budgets and audit. The video does not say whether SDK-driven runs can be routed through a proxy, so this is only a loose fit. → *Test whether SDK-driven Claude Code runs can be pointed at the AgentOS proxy and whether MCP-attached tool calls show up in the audit log.*
