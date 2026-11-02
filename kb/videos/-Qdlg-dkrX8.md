# Claude 4 is HERE and is taking on Cursor... (Claude Code)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `-Qdlg-dkrX8` · [watch](https://youtu.be/-Qdlg-dkrX8) · **date:** 2025-11-02 · **length:** 7:20 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic, Cursor, Replit, GitHub, OpenAI, JetBrains
- **topics:** coding-agents, claude-code, models-research, mcp-and-tools · **tags:** claude-4, claude-opus-4, claude-sonnet-4, claude-code, vs-code, jetbrains, swe-bench, prompt-caching, remote-mcp, claude-code-sdk, github-pr, pricing, tetris-demo

> Better Stack's launch-day recap of Claude 4 (Sonnet 4, Opus 4) with a short Claude Code VS Code demo. It mostly relays Anthropic's benchmark and behavior claims, with light skepticism.

## Summary
This is a launch-day roundup of Anthropic's Claude 4 release, Sonnet 4 and Opus 4, plus Claude Code becoming generally available with VS Code and JetBrains integration. The presenter runs a quick side-by-side Tetris test in the Claude UI, then reads the SWE-bench numbers, where Sonnet 4 (72.7%) edges Opus 4 (72.5%) and parallel test-time compute reaches 80.2%. He notes this sits awkwardly with the "world's best coding model" framing, and says Opus leads on Terminal Bench. Anthropic's behavior claims are repeated without independent testing: fewer shortcuts and loopholes, better steerability, memory-file creation, and multi-hour unattended runs. The hands-on part is a small Next.js to-do app bug fixed by pasting an error into Claude Code inside VS Code, with the diff shown in the editor. He also covers the Claude Code SDK (which he thinks is just non-interactive CLI), GitHub PR tagging, and direct remote MCP connections from the Claude API. Overall it is an announcement recap with one small demo, not an evaluation.

## Key ideas
- **Claude 4 launch: Sonnet 4 is pitched as the balance of performance and efficiency, and Opus 4 as the top coding model. Claude Code is now generally available and integrated into VS Code and JetBrains.** — Presenter frames the release as a major version bump. The Claude UI also gained code execution (e.g. running Python on uploaded files). ([0:00](https://youtu.be/-Qdlg-dkrX8?t=0))
- **SWE-bench is essentially a tie between the two models, which undercuts the 'best coding model' claim for Opus.** — Opus 4 scores 72.5% and Sonnet 4 scores 72.7%, both slightly above Codex 1 and OpenAI o3. The presenter says Opus wins on Terminal Bench by a larger margin. Sonnet 4 reaches 80.2% with parallel test-time compute. ([0:58](https://youtu.be/-Qdlg-dkrX8?t=58))
- **Opus 4 is claimed to keep useful memory files when given local file access. A Pokemon demo shows it writing a navigation guide for itself.** — Anthropic positions this as better long-term task awareness and coherence for agent tasks. This is a vendor demo, not independently tested in the video. ([2:14](https://youtu.be/-Qdlg-dkrX8?t=134))
- **Behavior fixes: Sonnet 4 is more steerable, and both models use fewer shortcuts and loopholes.** — Anthropic says 3.7 Sonnet was over-eager and did unrequested work, and claims a 65% reduction in shortcut behavior versus 3.7 Sonnet. Thinking summaries come from a smaller model and only kick in about 5% of the time. ([2:14](https://youtu.be/-Qdlg-dkrX8?t=134))
- **Anthropic says the models can run unattended for hours, which the presenter reads as agent-friendly.** — Customers reportedly left the model running without stepping in, so it does not stop to ask questions or make mistakes that force a rerun. The video offers no measurement behind this. ([3:24](https://youtu.be/-Qdlg-dkrX8?t=204))
- **Pricing stays flat, and a 1-hour prompt cache option is added alongside the default 5-minute cache.** — Opus 4 costs $15 per million input and $75 per million output tokens. Sonnet 4 costs $3 and $15, the same as 3.7 Sonnet. The longer cache option is presented as the cost mitigation. ([3:24](https://youtu.be/-Qdlg-dkrX8?t=204))
- **Claude Code in VS Code is a bug-fix demo. The agent reads the pasted error, searches files, and changes one value, which the user accepts through an in-editor diff.** — The fix changed a select item's empty-string value to none. The user chose 'yes, don't ask again for this session' on the edit prompt. The presenter says the integration is the CLI inside the IDE, with diffs shown in the editor. ([4:43](https://youtu.be/-Qdlg-dkrX8?t=283))
- **On-stage claims: a 90-minute uninterrupted Claude Code run that added a table feature to the Excalidraw repo, and tagging Claude Code in GitHub PRs to handle review feedback.** — These are vendor-reported and were not reproduced in the video. ([5:58](https://youtu.be/-Qdlg-dkrX8?t=358))
- **The Claude Code SDK looks like non-interactive Claude Code, so you would still shell out to a CLI from your own backend.** — The presenter doubts the SDK is a real SDK for that reason, which is a useful caveat for anyone planning to embed it. ([5:58](https://youtu.be/-Qdlg-dkrX8?t=358))
- **The Claude API can connect to remote MCP servers directly, so the client does not need its own MCP connection code.** — You pass the MCP server you want in the API request, and Anthropic's side handles the connection. The video does not show the exact request field. ([6:58](https://youtu.be/-Qdlg-dkrX8?t=418))

## Techniques
- **Claude Code inside VS Code or JetBrains via the CLI** — Install the latest Claude Code CLI on the machine. Open VS Code's integrated terminal and run `claude`. The video says the extension is then detected from the terminal, rather than installed from the marketplace. Use Cmd+Esc (the video says 'command escape', so this is macOS) to launch Claude Code from inside the IDE. Diffs open in VS Code for review. *When:* You want the CLI's agent behavior with editor diff review, for example for a bug fix in an existing project.
- **Paste-the-error bug fix** — Copy the runtime error from the app's UI. In Claude Code, type 'fix this bug' and paste the error. Review the diff opened in the editor. Accept the edit, optionally choosing 'don't ask again for this session' to avoid repeated prompts. *When:* Small, well-scoped bugs where the error text points at the cause. The demo's fix was a one-line change.
- **Agent-maintained memory file** — Give the model access to local files so it can create and update a notes file that persists across steps, such as a navigation guide or key facts. The video shows this only in the Pokemon example and offers no file name or prompt. *When:* Long-running agent tasks that need to keep state across many steps and context resets.
- **Remote MCP servers through the Claude API** — Pass the MCP server endpoint you want to use in the API request, and let Anthropic connect to it server-side, instead of running your own MCP client. The exact request field is not shown in the video; check the API docs. *When:* You want to use a remote MCP server from an app that calls the Claude API directly and do not want to build or run an MCP client.
- **One-hour prompt cache TTL** — Use the new option that extends the prompt cache lifetime from the default 5 minutes to 1 hour. The video does not show the parameter name, so check the API docs for how to set it. *When:* Agent loops or workflows where calls to the same long prefix are spaced more than 5 minutes apart but still reuse the same context.
- **Tagging Claude Code in GitHub PRs** — Tag Claude Code in a pull request comment. It responds to reviewer feedback, fixes errors, and edits the code. The video shows no trigger syntax or setup. *When:* Addressing review comments on agent-written or human PRs without switching to a local session.

## Numbers
- SWE-bench: Opus 4 72.5%, Sonnet 4 72.7% ([0:58](https://youtu.be/-Qdlg-dkrX8?t=58))
- Sonnet 4 with parallel test-time compute: 80.2% on SWE-bench ([0:58](https://youtu.be/-Qdlg-dkrX8?t=58))
- 65% reduction in shortcut and loophole behavior versus 3.7 Sonnet (Anthropic claim) ([2:14](https://youtu.be/-Qdlg-dkrX8?t=134))
- Thinking summaries use a smaller model and are needed about 5% of the time ([2:14](https://youtu.be/-Qdlg-dkrX8?t=134))
- Opus 4 pricing: $15 per million input tokens, $75 per million output tokens ([3:24](https://youtu.be/-Qdlg-dkrX8?t=204))
- Sonnet 4 pricing: $3 per million input tokens, $15 per million output tokens (same as 3.7 Sonnet) ([3:24](https://youtu.be/-Qdlg-dkrX8?t=204))
- Prompt cache TTL can be extended from 5 minutes to 1 hour ([3:24](https://youtu.be/-Qdlg-dkrX8?t=204))
- On-stage claim: Claude Code ran uninterrupted for 90 minutes on a table feature in the Excalidraw repo (vendor claim, not verified in video) ([5:58](https://youtu.be/-Qdlg-dkrX8?t=358))

## Hot takes
- The 'world's best coding model' claim for Opus 4 is undercut by its SWE-bench score being slightly below Sonnet 4 (presenter's own read).
- The Claude Code SDK is just Claude Code in non-interactive mode, so it may not be the SDK it is advertised as (presenter's doubt).
- Customer quotes, Replit and Cursor praise, the Pokemon memory demo, the 90-minute run and the 65% figure are all vendor-reported and not tested in the video.
- Hype-style launch coverage: the title and framing run ahead of the substance, which is mostly a relay of Anthropic's announcement, plus one small app demo.

## Tools mentioned
Claude Opus 4, Claude Sonnet 4, Claude 3.7 Sonnet, Claude Code, Claude Code SDK, Claude API (remote MCP connector), VS Code, JetBrains IDEs, Next.js, Excalidraw, GitHub Copilot agent, Codex 1, OpenAI o3, Terminal Bench, SWE-bench, Python (Claude UI code execution), MCP

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI. The video covers VS Code integration, unattended long runs, and the non-interactive mode behind the SDK, all of which bear on how the harness invokes Claude Code. → *Compare ProsHarness's CLI invocation against Claude Code's non-interactive mode and the SDK the presenter describes, and verify the unattended-run claims before relying on them for checkpoint and resume design.*
- **agentos** (1/3): The 1-hour prompt-cache option is a cost lever for long agent loops, which the budget and routing layer would need to model. → *Model the 5-minute vs 1-hour prompt-cache TTL as a cost option in the Govrix budget and routing layer, after confirming the current pricing in the Anthropic docs.*
