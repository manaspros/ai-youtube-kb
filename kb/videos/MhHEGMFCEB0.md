# OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `MhHEGMFCEB0` · [watch](https://youtu.be/MhHEGMFCEB0) · **date:** 2026-05-18 · **length:** 1:01:59 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Vaibhav Srivastav (VB), Katia Gil Guzman · **orgs:** OpenAI
- **topics:** coding-agents, multi-agent, security-guardrails, pr-code-review · **tags:** codex, plugins, automations, sub-agents, custom-agent-personas, guardian-approvals, hooks, stop-hook, code-review, cloud-agents, playwright, workshop

> OpenAI's Codex workshop on plugins, background automations, code review, custom sub-agents with sandbox modes, guardian approvals, and stop hooks for long runs.

## Summary
Two OpenAI developer-experience engineers run a live workshop on the Codex agent across its app, CLI, IDE and cloud surfaces. They demo plugins that bundle skills, app connections and MCP servers, plus scheduled background automations that triage Slack and Gmail or update a spreadsheet from a codebase. They explain Codex code review, which runs a fresh review process with repo-wide context and is on by default for every PR in OpenAI's repos. The core practitioner material is custom sub-agents, defined as TOML personas with their own model, reasoning effort and read-only or write sandbox, fanned out over file slices with a concurrency cap of six. The talk then covers guardian approvals (a sub-agent that judges whether a privileged action needs a human), hooks (session start, after each tool use, stop), and a stop hook that keeps a long run going. Most of the talk is product walkthrough, and several claims (quality rankings, scale numbers) are the speakers' own with no independent evidence shown.

## Key ideas
- **Plugins bundle skills, app connections and MCP servers into one install** — Instead of installing each skill, app and MCP server separately, a plugin packages them as one reusable workflow. Skills are reusable instructions with scripts and resources, apps are service connections (Notion, Linear, Google Drive), and MCP servers expose external tools. ([12:54](https://youtu.be/MhHEGMFCEB0?t=774))
- **Automations are scheduled background agent tasks** — The speaker treats automations like cron jobs that run a plain-language instruction on a schedule with connected apps. Examples: a 9 AM Slack triage that flags urgent messages, a Gmail check for replies, and a daily Slack summary bucketed by topic. ([19:16](https://youtu.be/MhHEGMFCEB0?t=1156))
- **Code review is a separate fresh process with repo-wide context, not only a diff read** — Codex starts a new review process with its own review system prompt. It looks past the diff at other modules to find second-order effects. The speakers say 100% of PRs across OpenAI repos get this review by default, and findings are tagged P0/P1/P2. ([31:37](https://youtu.be/MhHEGMFCEB0?t=1897))
- **Sub-agents are useful when the work splits into independent slices** — The demo asked for review of about 45 persona files. Codex built review slices (which files each sub-agent reads), spawned reviewers in new environments, then collated their findings and tore the agents down. A cap of six concurrent threads applied to the demo setup. ([35:35](https://youtu.be/MhHEGMFCEB0?t=2135))
- **Sandbox mode per sub-agent is a safety setting, not a detail** — Reviewers and vulnerability analysts should be read-only so they never execute anything. Doc writers or bug reporters need write access. Each sub-agent can also set its own model, reasoning effort and MCP servers, and can be given skills. ([41:39](https://youtu.be/MhHEGMFCEB0?t=2499))
- **Guardian approvals use a sub-agent to judge privileged actions instead of YOLO mode** — When Codex needs a privileged action (delete a directory, run a server, expose a file), a sub-agent decides from a prompt whether a human must approve. The speaker says most cases need no human, aiming to cut approval fatigue. This is experimental and is switched on through the experimental settings. ([49:57](https://youtu.be/MhHEGMFCEB0?t=2997))
- **A stop hook can keep a long-running task going** — hooks.json maps events (session start/resume, after each tool use, stop) to scripts. The speaker's stop hook runs a script that asks Codex to do one more pass, run one validating command, tighten one more thing, then stop and report. ([54:28](https://youtu.be/MhHEGMFCEB0?t=3268))
- **Past session logs are a source for automations and sub-agent ideas** — Codex session logs are stored under the .codex folder (in a sessions directory). The speaker suggests asking the agent to read past sessions and recommend automations or sub-agents to create. This is presented as a common workflow. ([57:10](https://youtu.be/MhHEGMFCEB0?t=3430))

## Techniques
- **Custom sub-agent personas as TOML files** — Each persona file sets a name, a description, a sandbox mode (read-only or write), a model, reasoning effort, MCP servers, skills and instructions. Ask Codex to draft the file from a persona description. Three defaults ship: a general fallback, a worker (execution), and an explorer. *When:* When the same role (reviewer, explorer, doc writer, vulnerability analyst) is needed repeatedly across tasks.
- **Fan-out review by file slices with an orchestrator** — The main agent partitions a large set of files into slices, gives each sub-agent its files plus repo guidance (contributing docs, skills), runs them in parallel within a concurrency cap, then collates results and closes the agents. *When:* Large repetitive review or audit work where each unit is independent, such as checking dozens of config or persona files.
- **Read-only explorer on a fast cheap model** — A PR-explorer sub-agent uses a fast text-only model (GPT-5.3 Codex Spark on Cerebras, per the speaker), read-only sandbox, and instructions to trace the execution path without proposing fixes. *When:* When you need fast code tracing or exploration and do not want the agent to change anything.
- **Parallel brainstorm of implementation options** — Ask for five to ten ways to implement a feature, then spawn one sub-agent per option to investigate it, and compare. *When:* Early design when you want to compare approaches before picking one.
- **Guardian verifier sub-agent for privileged actions** — A sub-agent gets a prompt to judge whether a requested privileged command needs human approval. Routine actions pass through; risky ones go to the user. *When:* Long autonomous runs where constant approval prompts cause fatigue, but full YOLO access is unsafe.
- **Stop hook that keeps a run going** — Register a stop event in hooks.json that runs a Python script. The script re-prompts the agent for one more validation pass and a final check before it stops. *When:* Long-running tasks where you want repeated verify-and-tighten passes without manual restarts.
- **Best-of-N cloud runs** — Start the same task in the cloud N times in parallel (the speaker used four), then pick the best output. *When:* Tasks with a clear success check where running several attempts is cheaper than one slow careful pass.
- **Playwright interactive skill for visual debugging** — The agent opens the running app in a headless browser, clicks through it, takes screenshots and analyses them, then iterates on the result. *When:* Building or debugging visual apps or games where the agent needs to see the rendered output.

## Numbers
- WebSockets connection gives roughly 1.75x faster tokens ([6:04](https://youtu.be/MhHEGMFCEB0?t=364))
- Fast mode adds about 2x more speed on top of that (as stated by the speaker) ([6:04](https://youtu.be/MhHEGMFCEB0?t=364))
- Over 3 million weekly active Codex users, more than tripled since January ([11:38](https://youtu.be/MhHEGMFCEB0?t=698))
- 100% of pull requests across OpenAI repos are reviewed by Codex Code Review by default ([31:37](https://youtu.be/MhHEGMFCEB0?t=1897))
- Demo: 45 persona files, 20 reviewers requested, concurrency cap of six agent threads ([35:35](https://youtu.be/MhHEGMFCEB0?t=2135))
- Demo: spreadsheet of 57 events written after about two minutes of codebase analysis ([22:44](https://youtu.be/MhHEGMFCEB0?t=1364))
- Three default sub-agent personas: default, worker, explorer ([41:39](https://youtu.be/MhHEGMFCEB0?t=2499))

## Hot takes
- Codex Code Review is one of the best in the industry right now (speaker's own view, with no comparison shown)
- Codex is the first harness with a native Windows sandbox, and no competing harness supports one
- Guardian approvals are meant to fix YOLO mode and reduce approval fatigue at the same time
- Local skills do not run in cloud tasks because the sandbox cannot tell whether a skill is trusted

## Tools mentioned
Codex, Codex app, Codex CLI, Codex IDE extension, Codex Code Review, Codex Security, Claude Code plugin for Codex, Playwright, ImageGen, Slack, Gmail, Google Drive, Notion, Linear, Figma, GitHub, Sentry, Cerebras, GPT-5.3 Codex Spark, GPT-5.4, GPT-5.4 Mini, GPT-5.4 Nano

## Relevance to our work
- **prosharness** (2/3): Stop hooks that keep a long run going and a guardian sub-agent that triages privileged actions both overlap ProsHarness's checkpoint loops and phone-driven approvals. Read-only review sub-agents also apply to its plan, critique and debate flow. → *Prototype a stop hook in ProsHarness that re-prompts a long run for one validation pass, and try a read-only verifier sub-agent that filters approval requests before they reach the phone.*
- **general** (2/3): Concrete sub-agent patterns (TOML persona definitions with per-agent sandbox, model and reasoning effort; file-slice fan-out with a concurrency cap) apply directly to subagents and multi-agent orchestration, one of the recurring interests. → *Write one read-only reviewer persona and one fan-out review run over a real directory, and measure wall-clock time and result quality against a single agent.*
- **agentos** (1/3): Session logs under .codex/sessions are mined by the agent to suggest automations and sub-agents. This is a small data point for SkillForge's telemetry-to-skill idea, but the talk gives no success signal or scoring method. → *Read the session-log layout the speaker describes and compare it with SkillForge's telemetry schema before deciding how to mine skill candidates.*
