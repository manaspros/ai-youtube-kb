# Google won't STOP... They Just Upped the Gemini CLI Again

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `A3AOeX1s7yw` · [watch](https://youtu.be/A3AOeX1s7yw) · **date:** 2025-11-02 · **length:** 9:34 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Google, Skywork
- **topics:** coding-agents, mcp-and-tools, context-engineering · **tags:** gemini-cli, ide-integration, slash-commands, mcp, extensions, yolo-mode, request-quotas, shadcn, vs-code, sponsored

> A walkthrough of Gemini CLI's recent updates: free-tier quotas, MCP setup via settings.json, slash commands, VS Code inline diffs, and "extensions" as shareable bundles of context, MCP servers and commands.

## Summary
The speaker builds a to-do list front end with Gemini CLI (Gemini 2.5 Pro) and the ShadCN MCP server, using two custom slash commands, `add` and `page`. He describes the free tier as 60 requests per minute and 1000 per day, and reports that one session of about 9 prompts consumed about 95 requests because tool calls count too. He covers how MCP servers are added by editing settings.json, the Ctrl+Y YOLO toggle, the IDE companion that shows edits as inline diffs in VS Code, and small features such as /compress, /copy and themes. The main claimed differentiator is Extensions, which bundle a context file, MCP servers, custom commands, templates and access restrictions into a shareable package. The video opens with a Skywork sponsor segment and is mostly a hands-on demo with few measured results beyond the request counts.

## Key ideas
- **Gemini CLI's free tier is described as 60 requests per minute and 1000 per day, with Gemini 2.5 Pro included.** — The speaker presents the quota as the main reason to try the tool and says he will explain how far it goes. The quota is the figure to check against current docs, since it comes from the video only. ([0:00](https://youtu.be/A3AOeX1s7yw?t=0))
- **MCP servers are added by pasting their config into settings.json, not through per-transport add commands.** — The speaker contrasts this with Claude Code, which needs different add commands for HTTP and local servers, and says the flow is closer to Cursor. ([1:57](https://youtu.be/A3AOeX1s7yw?t=117))
- **Split the build into whole-page generation and component-level additions, each driven by its own slash command.** — The `page` command generates a full page and `add` adds a single component such as a modal. Both take extra context and require the ShadCN MCP server. Separate prompts give more control over each step. ([3:21](https://youtu.be/A3AOeX1s7yw?t=201))
- **The IDE companion turns edits into reviewable inline diffs in VS Code.** — The speaker runs the IDE command in the terminal, which installs the Gemini CLI companion extension. Approval is requested in both the terminal and the editor, and each inline change is accepted or rejected separately. ([4:43](https://youtu.be/A3AOeX1s7yw?t=283))
- **Request accounting counts tool calls, not just prompts, so the quota drains faster than the prompt count suggests.** — One session with about 9 prompts (roughly 10 requests per prompt) used about 95 requests, according to the session summary. The speaker estimates that works out to about 10 sessions of this size on the daily quota. This is a single-session observation, not a measured rate. ([5:52](https://youtu.be/A3AOeX1s7yw?t=352))
- **Extensions bundle context, MCP servers, custom commands, templates and restrictions into a shareable package.** — The speaker's example is a front-end extension wrapping the ShadCN MCP, with a context file (gemini.md), custom commands, templates, and a config that links the context file and forbids edits to .env or deletion of key files. He frames extensions as specialized sub-agents that teams can distribute, such as a CodeStandards extension holding a standards.md file. ([7:07](https://youtu.be/A3AOeX1s7yw?t=427))

## Techniques
- **Custom slash commands as TOML files for page and component generation** — Keep TOML command files under the project's commands folder. The speaker uses `page` to generate a whole page and `add` to add one component, both passing extra instructions as arguments. Both commands need the ShadCN MCP server active. The exact TOML keys were not shown on screen. *When:* Repeated UI-generation prompts where you want a fixed structure and control over each step, such as page then component then modal.
- **Adding MCP servers by editing settings.json** — Copy the server's JSON config and paste it into the Gemini CLI settings.json. The speaker says it works immediately, with no add command per transport type. *When:* Wiring up HTTP or local MCP servers quickly, especially if you already configure Cursor this way.
- **YOLO mode toggle for uninterrupted runs** — Press Ctrl+Y to toggle YOLO mode, which keeps the agent running without confirmation prompts, similar to Claude Code's dangerously-skip-permissions flag. *When:* Trusted, low-risk runs where confirmation prompts would stall the session. Unsafe on untrusted repos.
- **Reviewing agent edits in VS Code via the IDE companion** — Run the IDE command (transcribed as 'ID command') in the Gemini CLI terminal. It auto-installs the Gemini CLI companion extension. Approve changes in the terminal and the editor, then accept or reject each inline diff. *When:* Large codebases where you cannot review all changes in one pass and want per-hunk control in the editor.
- **Built-in session helpers** — /compress compresses the current chat context. /copy copies the latest result to paste elsewhere or hand to another AI coder. Themes are available in the settings. *When:* Long sessions where context is filling up, or when moving output between tools.
- **Packaging a team extension** — Create an extensions folder inside the Gemini config folder (the speaker says 'Gemini folder'; the exact path was not spelled out) with a folder per extension. Put a config file in it that defines the MCP server, links a context file, and sets restrictions such as blocking .env edits or deletes. Add a gemini.md context file, custom slash commands and reusable templates alongside. Share the folder so everyone gets the same setup. *When:* Standardizing a team's MCP servers, coding standards or scaffolding so each developer does not configure them separately.

## Numbers
- Free-tier limits: 60 requests per minute and 1000 requests per day. ([0:00](https://youtu.be/A3AOeX1s7yw?t=0))
- A session with about 9 prompts consumed about 95 requests (roughly 10 per prompt), because tool calls are counted as requests. The speaker estimates about 10 sessions of this size fit the daily quota. ([5:52](https://youtu.be/A3AOeX1s7yw?t=352))
- Model used throughout the demo: Gemini 2.5 Pro. ([5:52](https://youtu.be/A3AOeX1s7yw?t=352))

## Hot takes
- The video opens with a sponsored Skywork segment at 1:00, so quality is capped at 2 under the sponsorship rule.
- The claim that Gemini CLI is 'catching up' to Claude Code and that Claude Code has no equivalent to Extensions is asserted, not tested in the video.
- The per-prompt request estimate and the '10 sessions' claim come from one session summary and are not verified.
- Speaker could not find a plan mode at the time of recording; he mentions accept-edits and YOLO modes instead.
- Transcript auto-captions garble several names ('Cloud Code' for Claude Code, 'Quen' for Qwen, 'ID command' for the IDE command); these were read as Claude Code, Qwen and the IDE command.

## Tools mentioned
Gemini CLI, Gemini 2.5 Pro, ShadCN MCP (shadcn), Gemini CLI companion extension (VS Code), VS Code, Claude Code (compared, not demoed), Cursor (compared, not demoed), ChatGPT (used to draft the to-do app), TweakCN (theme source), Qwen (named as a competing free agent, no version), Skywork Super Agents (sponsor, not demoed)

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, and this video shows another CLI's packaging of context, MCP servers, commands and path restrictions into a shareable bundle, plus an auto-approve mode to compare with ProsHarness's approval flow. → *Compare the Gemini extension layout (context file, MCP config, restrictions such as blocking .env edits) with how ProsHarness packages skills and permission rules, and consider whether restrictions belong in the bundle.*
