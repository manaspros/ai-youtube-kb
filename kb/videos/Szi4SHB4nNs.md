# Codex CLI Has Just Got WAY Better!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Szi4SHB4nNs` · [watch](https://youtu.be/Szi4SHB4nNs) · **date:** 2025-11-02 · **length:** 6:35 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** OpenAI, Better Stack, Anthropic
- **topics:** coding-agents, sandboxing-execution, claude-code, mcp-and-tools · **tags:** codex-cli, sandbox-modes, approval-policy, config-toml, config-profiles, openai-compatible-endpoints, agents-md, rust-tui, claude-code-comparison, notify-script

> Better Stack tours the late-2025 Codex CLI update (Rust rewrite, ChatGPT login, sandbox and approval modes, config profiles) and candidly compares it with Claude Code.

## Summary
The host says they avoided Codex CLI because it felt buggy and GPT coding models trailed Claude, but a recent update changed that. OpenAI's terminal agent was rewritten from TypeScript (Ink) to Rust (Ratatui), which the host finds faster, and it now offers a minimal text-only UI and sign-in with a ChatGPT plan. The video covers transcript inspection, the default sandbox and its three modes, approval policies that are configured separately from the sandbox, and config.toml with named profiles, reasoning settings, a notify script and OpenAI-compatible model endpoints (only GPT-OSS worked for the host). A feature comparison concludes that Claude Code is well ahead on features and documentation, though Codex is a reasonable base to build on. The video closes with OpenAI's open-source fund offering up to $25,000 in API credits and a note that Windows is not officially supported. Overall this is a practical overview with some config detail, not a deep benchmark or internals study.

## Key ideas
- **Codex CLI was rewritten from TypeScript (Ink) to Rust (Ratatui) for speed, fewer dependencies and better security; the host finds the Rust build faster** — Minimal text-only UI with no ASCII art. Sign-in with a ChatGPT plan or API key is offered at first run. The host's experience of speed is anecdotal. ([0:00](https://youtu.be/Szi4SHB4nNs?t=0))
- **The agent's reasoning and tool calls are inspectable through a transcript view** — Pressing Esc twice or Ctrl+T opens a view showing bash commands run, files read and the model's thinking. Q returns to the main layout. ([0:00](https://youtu.be/Szi4SHB4nNs?t=0))
- **Sandbox is on by default and confines execution to the project workspace (files, processes, network)** — A sandbox flag offers three modes: Workspace Write (edit files in the directory without approval), Read Only (reads without approval, asks before edits or commands) and a full-access mode the host calls 'dangerous access'. ([1:27](https://youtu.be/Szi4SHB4nNs?t=87))
- **Approval policy is a separate axis from the sandbox, which the host finds confusing** — Four approval policies are named: on-request, never, on-failure (ask only to retry a failed command) and untrusted (run only trusted commands). Combining them with sandbox modes sets the autonomy level. ([2:54](https://youtu.be/Szi4SHB4nNs?t=174))
- **config.toml can hold sandbox and approval values plus named profiles selected with -p, along with reasoning effort, summary, verbosity and a notify script** — The host compares the notify script to Claude Code hooks, but notes Codex's notify docs are a small section. ([2:54](https://youtu.be/Szi4SHB4nNs?t=174))
- **Non-OpenAI models work only if they expose an OpenAI-compatible API and support the tool calls Codex expects** — The host got GPT-OSS working. DeepSeek failed, which the host suspects is either a config issue or missing tool support. ([2:54](https://youtu.be/Szi4SHB4nNs?t=174))
- **On features, Claude Code is ahead by the host's account, and Codex is not yet a replacement** — Items listed for Claude Code: custom prompts with arguments, custom status line, hooks, custom sub-agents, output styles, visual context, session resume, background tasks, vim mode, security review, and more detailed docs. ([4:20](https://youtu.be/Szi4SHB4nNs?t=260))
- **OpenAI's open-source fund gives up to $25,000 in API credits to open-source projects that use Codex CLI and OpenAI models** — Presented as a practical incentive to adopt Codex CLI; the host does not verify eligibility details. ([4:20](https://youtu.be/Szi4SHB4nNs?t=260))

## Techniques
- **Separate sandbox from approval when setting agent autonomy** — Pick a sandbox mode (Workspace Write, Read Only or full access) and an approval policy (on-request, never, on-failure, untrusted) independently; check the active values with /status. The host did not show exact flag spellings. *When:* Choosing how much an agent may do unattended, e.g. read-only review versus a trusted YOLO-style run.
- **Named config profiles in config.toml run with -p** — Put sandbox and approval values, model and reasoning settings in config.toml, define them as a named profile and launch with the -p flag. The host did not show the TOML syntax. *When:* Switching quickly between a restricted review mode and a permissive run mode.
- **Audit an agent run via the transcript view** — Press Ctrl+T (or Esc twice) during a session to see every bash command, file read and reasoning step; press Q to go back. *When:* Checking what an agent actually executed before trusting its result.
- **Tune model and reasoning effort per task** — Use /model to see and select the model (GPT-5 is the default, no nano or mini), then set reasoning effort in the config. The host says GPT-5 at high reasoning is good for coding. *When:* Harder coding tasks where a higher reasoning level is worth the cost.
- **Point Codex at an OpenAI-compatible endpoint for non-OpenAI models** — Configure a custom OpenAI-compatible provider in config.toml. GPT-OSS worked for the host; DeepSeek returned an error. The provider keys were not shown. *When:* Trying open-weight models behind an OpenAI-style API, provided they support tool calls.
- **Notify script for event alerts** — Set a notification script in config.toml, which the host compares to Claude Code hooks. Details were not shown. *When:* Getting alerted when a long agent turn finishes.
- **Everyday workflow commands** — /init creates AGENTS.md (not a tool-specific file); /status shows workspace, model, token usage and sandbox/approval settings; /model shows the model. Use @ to attach files, Ctrl+V to paste images, and non-interactive mode for scripted runs. Custom prompts live in a prompts folder and run as commands. *When:* Starting a repo's agent instructions, attaching context, scripting Codex runs, and reusing prompts.

## Numbers
- Codex CLI has 11 default slash commands ([1:27](https://youtu.be/Szi4SHB4nNs?t=87))
- Sandbox offers three modes ([1:27](https://youtu.be/Szi4SHB4nNs?t=87))
- Four approval policies: on-request, never, on-failure, untrusted ([2:54](https://youtu.be/Szi4SHB4nNs?t=174))
- OpenAI open-source fund gives up to $25,000 in API credits for projects using Codex CLI and OpenAI models ([4:20](https://youtu.be/Szi4SHB4nNs?t=260))
- Default model is GPT-5 (no nano or mini shown) ([1:27](https://youtu.be/Szi4SHB4nNs?t=87))

## Hot takes
- Claude Code is 'way ahead' of Codex CLI on features and documentation, so Codex is not yet a replacement, though it is a good base to build on.
- Rust rewrite is faster in the host's experience.
- Creating AGENTS.md instead of a tool-specific markdown file is a welcome convention.
- Security-first sandbox default is a strength, but sandbox and approval combinations are confusing.
- The $25k open-source credits fund is presented as a reason to try Codex.
- Windows is not officially supported.

## Tools mentioned
Codex CLI (OpenAI terminal coding agent), GPT-5, GPT-OSS, DeepSeek (tested, errored), AGENTS.md, config.toml, Ink (previous TypeScript UI), Ratatui (Rust TUI library), ChatGPT login, Codex VS Code plugin, Claude Code (comparison), Better Stack MCP (host plug), VS Code, Cursor

## Relevance to our work
- **agentos** (1/3): Codex's sandbox modes and approval policies are a reference point for Crucible's opt-in sandboxed execution and exec-gate guardrails. → *Compare Codex's three sandbox modes and four approval policies with Crucible's exec-gate design and note where a per-run profile would fit.*
- **prosharness** (1/3): ProsHarness wraps Claude Code CLI and handles approvals. Codex's separation of sandbox and approval policy, and its named profiles, are relevant prior art. → *Look at how Codex's on-request, on-failure and untrusted policies and -p profiles map onto ProsHarness approval handling.*
