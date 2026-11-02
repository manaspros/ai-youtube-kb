# Agents.md Is HERE… 90% of AI Tools Will Use This Now

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `Pmc4OfSlhbE` · [watch](https://youtu.be/Pmc4OfSlhbE) · **date:** 2025-11-02 · **length:** 8:04 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic, OpenAI, Google, GitHub, Hostinger
- **topics:** context-engineering, coding-agents, claude-code · **tags:** agents-md, claude-md, context-files, mcp, multi-tool-workflow, codex, gemini-cli, cursor, sponsored, opinion

> Host argues OpenAI's AGENTS.md should become the single cross-tool agent context file, replacing per-tool rules files, and says Claude Code's absence is the gap. Includes a sponsor segment.

## Summary
The host frames MCP as a standard that removed per-model, per-tool integration code, then moves to the problem of agent context files. Each tool (Claude Code, Windsurf, Kiro, Cursor, GitHub Copilot) reads its own rules file, so testing several agents on one repo means copying context by hand and each tool updates only its own file. He presents AGENTS.md, a single cross-agent context file pushed by OpenAI, and names Codex, Gemini CLI, Qwen Code, Cursor, Factory and Google Jules as adopters. Claude Code is the notable absence, and since it is closed source, the host says Anthropic alone decides whether it reads AGENTS.md. Adoption is simple from the tool-builder side: a tool must be programmed to look for the file at session start. The video shows no benchmarks, no config contents and no adoption data, and it includes a sponsored Hostinger Horizons segment around the one-minute mark.

## Key ideas
- **MCP's main contribution was a standard, not new technology** — Before MCP, each model/tool pair needed custom integration code. MCP gives any MCP client and any model a common way to connect to tools. ([0:00](https://youtu.be/Pmc4OfSlhbE?t=0))
- **Agents only know what their context file tells them at session start** — Using Claude Code as the example, CLAUDE.md is loaded automatically into a new session. The host shows that without it, a fresh session knows nothing about the repo's workflow. ([2:12](https://youtu.be/Pmc4OfSlhbE?t=132))
- **Testing several agents on one repo forces manual context copying** — To try another tool (e.g. Gemini CLI) on an existing project, the host copies the context into that tool's own file (gemini.md). ([3:19](https://youtu.be/Pmc4OfSlhbE?t=199))
- **Each tool keeps its own rules file and only updates its own** — He names separate files for Claude, Windsurf, Kiro, Cursor and GitHub Copilot. If one tool changes the project, the others never see it unless someone prompts a sync. ([4:40](https://youtu.be/Pmc4OfSlhbE?t=280))
- **AGENTS.md is OpenAI's push for one shared agent context standard** — Adopters named on the agents.md site include Codex, Gemini CLI, Qwen Code, Cursor, Factory and Google Jules. Claude Code is the notable missing one. ([5:31](https://youtu.be/Pmc4OfSlhbE?t=331))
- **Adoption is up to each tool, and Claude Code is closed source** — A tool only needs to look for AGENTS.md at session start, and Claude Code could read it alongside CLAUDE.md. Since Claude Code is not open source, only Anthropic can make that change. ([6:44](https://youtu.be/Pmc4OfSlhbE?t=404))

## Techniques
- **Single AGENTS.md as shared project context** — Put the repo's rules, workflow and current state in an AGENTS.md at the repo root, following the example structures on the agents.md site. Tools that support the standard load it at session start, so one file serves several agents. Keep CLAUDE.md alongside, since the host says Claude Code does not read AGENTS.md. Confirm each tool actually loads it. *When:* When you switch between or compare several coding agents on the same repository, instead of maintaining one rules file per tool.
- **Rely on the auto-loaded context file for session bootstrap** — Keep the project's primary workflow and standing rules in the file the tool loads automatically (CLAUDE.md for Claude Code). A new session then knows the workflow without being prompted. The host checks this by asking a fresh session for its primary workflow and getting no answer beyond what CLAUDE.md contains. *When:* When starting new agent sessions in a repo, or onboarding a new tool, to avoid re-explaining the project each time.

## Numbers
- Title claims 90% of AI tools will use AGENTS.md; the video gives no adoption data behind this. ([0:00](https://youtu.be/Pmc4OfSlhbE?t=0))
- Five separate tool-specific rules files named: Claude, Windsurf, Kiro, Cursor, GitHub Copilot. ([4:40](https://youtu.be/Pmc4OfSlhbE?t=280))
- Six named adopters of AGENTS.md: Codex, Gemini CLI, Qwen Code, Cursor, Factory, Google Jules. Shown on the agents.md site, not verified in the video. ([5:31](https://youtu.be/Pmc4OfSlhbE?t=331))
- Sponsor offer: 10% off with a promo code and a 30-day money-back guarantee for Hostinger Horizons (sponsor claim, not verified). ([1:00](https://youtu.be/Pmc4OfSlhbE?t=60))

## Hot takes
- Title overclaims: '90% of AI tools will use this' is not supported by anything in the video, which names about six adopters with no data.
- A sponsored Hostinger Horizons segment sits inside a thin opinion piece, so quality is capped at 2.
- Claims that Claude Code is 'undoubtedly the best agent' and that Cursor was overtaken are opinion with no evidence shown.
- Calling MCP 'the USB-C for AI models' is marketing framing, not technical analysis.

## Tools mentioned
AGENTS.md, CLAUDE.md, Model Context Protocol (MCP), Figma MCP server, Claude Code, OpenAI Codex, Gemini CLI, Qwen Code, Cursor, Windsurf, Kiro, GitHub Copilot, Factory, Google Jules, shadcn, Hostinger Horizons (sponsor)

## Relevance to our work
- **prosharness** (2/3): ProsHarness drives Claude Code and sends plans to Codex for critique. The video lists Codex as an AGENTS.md adopter, so project context can be shared across both steps and does not have to be copied by hand. → *Test whether Codex loads AGENTS.md in our setup. If it does, keep the project rules in one AGENTS.md plus CLAUDE.md so the Codex critique step sees the same rules as the Claude Code run.*
- **agentos** (1/3):  → *Before designing a shared context file for AgentOS-managed agents, check the agents.md adopter list against the agent targets we actually run.*
