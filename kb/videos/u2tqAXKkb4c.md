# Claude Code + Better Stack: The Only Error Debugging Setup You Need

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `u2tqAXKkb4c` · [watch](https://youtu.be/u2tqAXKkb4c) · **date:** 2026-06-02 · **length:** 4:18 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack, Anthropic
- **topics:** observability, mcp-and-tools, claude-code · **tags:** error-tracking, mcp, debugging, sentry-sdk, session-replay, pr-workflow, deferred-tool-loading, scheduled-routines

> Better Stack demo of triaging a live React frontend error from the terminal: Claude Code pulls error data through the Better Stack MCP server, opens a fix PR, then resolves the issue. Short, vendor-led.

## Summary
The presenter reproduces a real uncaught security error in a React video app, which blocks timeline scrubbing, and shows it captured by Better Stack error tracking via the Sentry React SDK. Instead of pasting errors into an agent by hand, they connect the Better Stack MCP server to Claude Code, which pulls the latest error details for the project. The agent summarizes errors, finds related ones to fix together, and separates unrelated 404s. It identifies a root cause, pushes a fix on a feature branch and opens a PR. The presenter verifies locally, the PR is merged, and the agent confirms the fix in code and resolves the issue and its earlier occurrences in Better Stack. The video ends by suggesting scheduled error-summary routines with notifications or auto-PRs. It is a 4-minute demo with no benchmarks, and the closing claim is that agents will replace visits to the UI.

## Key ideas
- **Copying errors into a coding agent by hand does not scale; an MCP server lets the agent read error data directly from the terminal.** — The motivating problem is opening the browser and pasting each error into the agent, which the presenter calls tedious when there are many errors. The Better Stack MCP server gives Claude Code the error details it needs to fix them in place. ([0:00](https://youtu.be/u2tqAXKkb4c?t=0))
- **The demo bug is a real, intermittent frontend error that is reproduced live.** — An uncaught security error appears when scrubbing the timeline after uploading a video in a React app. It is captured through the Sentry React SDK pointed at a Better Stack-specific DSN. ([0:00](https://youtu.be/u2tqAXKkb4c?t=0))
- **Setup is a copy-paste prompt from the Better Stack UI that the coding agent applies.** — After connecting an application and choosing its type, Better Stack shows a prompt to paste into an AI agent, which handles the SDK setup. Errors then appear in the Better Stack UI with browser info, reproduction steps, an AI explanation option and anonymous session replay. ([1:24](https://youtu.be/u2tqAXKkb4c?t=84))
- **The agent triages from the project directory: it finds the right app, summarizes recent errors, and groups only the related ones.** — A plain request for the app's error details is enough; the agent picks the correct app through MCP. Asking for related errors led the agent to read the codebase in parallel, give a root cause and suggested fix, and keep unrelated 404s separate. ([2:32](https://youtu.be/u2tqAXKkb4c?t=152))
- **The fix was a one-line change, and the agent handled the git flow: feature branch, PR, then a local check before merge.** — The agent created a feature branch and a PR. The presenter reviewed the changed files, tested locally by scrubbing for a few minutes, and could not reproduce the error before merging. ([2:32](https://youtu.be/u2tqAXKkb4c?t=152))
- **The loop closes by resolving issues through the agent after the fix is confirmed.** — After pulling the merged change, the agent checked the fix was in place and then resolved the three related security issues in Better Stack. Earlier occurrences were resolved too, so no UI clicks were needed. ([3:41](https://youtu.be/u2tqAXKkb4c?t=221))
- **The same MCP loop can run unattended as a scheduled routine.** — The presenter suggests a regular routine that emails new errors or pings WhatsApp or Telegram, and even has Claude open PRs for new issues. This is described, not demonstrated. ([2:32](https://youtu.be/u2tqAXKkb4c?t=152))

## Techniques
- **MCP-backed error triage loop** — 1) Add the Better Stack MCP server to Claude Code, either with the command shown in the video or by editing the harness config, then sign in to Better Stack (exact command not shown on screen). 2) From the project directory, prompt for all error details for the app; the agent picks the right app via the MCP tools. 3) Ask whether other errors are related so they can be fixed together. 4) Have the agent fix the root cause on a new feature branch and open a PR. 5) After merge, pull, have the agent confirm the fix is in the code, then resolve the issue and its occurrences via MCP. *When:* Many production or frontend errors to work through from the terminal, instead of the browser UI.
- **Deferred tool loading for MCP servers** — Turn on deferred tool loading in the Claude settings JSON so only the MCP tools the agent needs are loaded into context. The exact key is not shown in the video. *When:* An MCP server exposes many tools and you want to save context window.
- **Frontend error capture with a vendor DSN and an agent setup prompt** — In the Better Stack UI, connect the app and pick its type (here, React). Copy the Better Stack-specific DSN and the setup prompt from the same screen. Paste the prompt into the coding agent, which wires up the Sentry React SDK. *When:* Adding error tracking with session replay to a React app, using an agent to do the setup.
- **Scheduled error-triage routine** — Run the MCP error summary on a schedule. Send new errors by email, WhatsApp or Telegram, or have the agent open fix PRs for new issues. The presenter describes this but does not show the setup. *When:* You want unattended triage of new errors, with a human reviewing the PRs.

## Numbers
- The error the presenter reproduced had triggered about six minutes before it was inspected in the UI. ([1:24](https://youtu.be/u2tqAXKkb4c?t=84))
- The agent resolved three related security issues in Better Stack in one pass, along with earlier occurrences. ([3:41](https://youtu.be/u2tqAXKkb4c?t=221))
- The fix was one line of code. ([2:32](https://youtu.be/u2tqAXKkb4c?t=152))

## Hot takes
- The presenter says agents will increasingly replace visits to the UI: 'We'll be using more agents and less visiting the UI.' (3:41)
- The video is vendor-led: it promotes Better Stack's own MCP server and product and ends with a recommendation to try it. Treat the setup as the vendor's workflow, not an independent comparison.
- The one-line-fix claim rests on a single bug in a single app, so it is anecdotal evidence, not a measured result.

## Tools mentioned
Claude Code, Better Stack (error tracking, session replay, MCP server), Sentry React SDK, Telegram, WhatsApp, email

## Relevance to our work
- **agentos** (1/3): AgentOS observability (L4) could expose its own error and trace data through an MCP surface, which the video shows as a useful pattern for agent triage. The video itself covers frontend error tracking only. → *Prototype a read-only MCP server over AgentOS error and trace data so Claude Code can summarize recent failures and propose fixes.*
- **prosharness** (1/3): The scheduled triage routine with notifications overlaps ProsHarness loops, schedules and phone-driven approvals. The video only describes this and does not show it working. → *Add a scheduled routine that summarizes new errors, then routes any proposed fix through the existing phone approval step before a PR is opened.*
