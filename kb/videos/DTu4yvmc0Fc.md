# DeepSeek Harness Just Changed AI Forever

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `DTu4yvmc0Fc` · [watch](https://youtu.be/DTu4yvmc0Fc) · **date:** 2026-09-02 · **length:** 5:56 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Warren · **orgs:** Better Stack, DeepSeek, Anthropic, OpenAI, Amazon Bedrock, Y Combinator
- **topics:** agent-architecture, coding-agents, observability · **tags:** plugin-architecture, trajectory-log, agent-harness, open-source, creator-mode, cordis, model-agnostic

> Short hands-on tour of an open-source, plugin-first coding harness built on the Cordis framework, covering swappable models, an append-only trajectory log, and adding plugins by prompt. Hype title, thin on setup.

## Summary
Warren from Better Stack walks through a newly released open-source agent harness that he attributes to DeepSeek, built on the Cordis plugin framework. Every capability, including the model, tools, skills, sessions and API gateway, is a plugin, so pieces can be turned off or replaced through configuration. He says the model layer accepts Anthropic, OpenAI, Bedrock or any OpenAI-compatible endpoint. The most concrete feature shown is an append-only trajectory log that records system prompts, reasoning, tool calls and per-step token counts, which he searches and inspects in the desktop app. He then uses a "creator mode" to add a dinosaur mini-game to the app from a single chat prompt. He notes a fast-growing community (desktop app, TUI, web skins) and calls the project beta. The video has no benchmarks, no config files and no discussion of plugin security.

## Key ideas
- **Plugin-first architecture: models, tools, skills, sessions and the API gateway are all plugins on the Cordis framework, so core features can be disabled or swapped in config.** — The speaker says the harness is a whole product built on an existing plugin framework that has been on GitHub since 2022. Auto-caption garbles the framework's description, so treat the exact name as uncertain. ([0:00](https://youtu.be/DTu4yvmc0Fc?t=0))
- **The model is a plugin, so the harness is not tied to one provider.** — The docs reportedly show Anthropic, OpenAI, Bedrock and any OpenAI-compatible endpoint, with a sample config that includes Claude Sonnet 4.5. No config keys are shown on screen. ([1:28](https://youtu.be/DTu4yvmc0Fc?t=88))
- **Append-only trajectory log for traceability.** — It records everything the model sees, including system prompts, reasoning and tool calls. The UI supports timeline browsing, highlighting, and search across the whole conversation, with per-step token counts. ([1:28](https://youtu.be/DTu4yvmc0Fc?t=88))
- **Creator mode lets the agent author plugins from inside the harness.** — Standard mode has the full tool set for daily work. Creator mode adds tools to inspect and write plugins. The demo adds a dinosaur game from one chat prompt, and the speaker says any feature can be added this way. ([2:46](https://youtu.be/DTu4yvmc0Fc?t=166))
- **Community ecosystem grew within days of the repo going public.** — Third-party projects include a desktop app (about 11k GitHub stars on its own), a Claude Code-style TUI, web UI skins and an awesome list. The speaker frames the project as beta with expected rough edges. ([3:51](https://youtu.be/DTu4yvmc0Fc?t=231))
- **Beta status and the speaker's outlook.** — He expects the project to grow over the next year but says it has problems today. The video gives no benchmarks, no comparison with OpenCode beyond a passing remark, and no security discussion of plugins that agents write and load. ([5:11](https://youtu.be/DTu4yvmc0Fc?t=311))

## Techniques
- **Add a plugin by prompting inside the harness** — Switch the harness to creator mode, then describe the feature in chat (demo prompt: add a dinosaur jumping game in the bottom-right corner of the app). The agent writes and registers the plugin. The speaker did not show the generated plugin files or any load/reload step. *When:* When you want to customize a plugin-based agent UI or behavior without leaving the app. Good for quick prototypes. Review generated plugin code before enabling it in a shared setup.
- **Use an append-only trajectory log to audit a run** — Open the trajectory view alongside chat, browse the full history, search for words across the whole conversation (thinking and tool calls included), and check per-step tokens (for example, one step at 187 tokens of which 94 were reasoning). The log records system prompts, reasoning and tool calls. *When:* When debugging a long agent run, checking what the model actually saw, or measuring where tokens go. Relevant to any design that needs a replayable record of agent turns.
- **Swap the model provider through plugin config** — Add a provider plugin for Anthropic, OpenAI, Bedrock or an OpenAI-compatible endpoint in the harness configuration; the speaker says the sample config includes Claude Sonnet 4.5. Exact file names and keys are not shown in the video. *When:* When you want one harness to run across several model providers, or to compare models behind the same tool and session layer.

## Numbers
- Repo reported at about 150,000 GitHub stars shortly after release (speaker's claim, shown on screen only in part). ([0:00](https://youtu.be/DTu4yvmc0Fc?t=0))
- Cordis has been on GitHub since 2022 (speaker's claim). ([0:00](https://youtu.be/DTu4yvmc0Fc?t=0))
- One sampled step took 187 tokens, of which 94 were reasoning tokens. ([1:28](https://youtu.be/DTu4yvmc0Fc?t=88))
- Desktop app has about 11,000 GitHub stars on its own. ([3:51](https://youtu.be/DTu4yvmc0Fc?t=231))
- DeepSeek V4 Pro is described as matching GLM 5.2 on intelligence at a slightly lower price, and not far below Opus. Qualitative only, with no figures. ([0:00](https://youtu.be/DTu4yvmc0Fc?t=0))

## Hot takes
- The title ("Changed AI Forever") overstates a short, single-demo tour. There are no benchmarks, config files or install steps.
- The star counts and the claim that DeepSeek built the harness were stated by the speaker and are not verified in the video. The DeepSeek attribution itself was inconsistent in the transcript.
- The most novel idea is authoring plugins by prompt inside the harness. The video does not address the security implications of an agent writing and loading code into its own runtime.
- The trajectory log is the most practically useful feature for anyone building agent observability, but the video shows only the UI, not the storage format or export options.

## Tools mentioned
DeepSeek harness (open-source agent harness, desktop app and TUI), Cordis (plugin framework; name as auto-captioned), DeepSeek V4 Pro (model; named in the video), GLM 5.2 (model used as a comparison point), Claude Sonnet 4.5 (in sample provider config), OpenClaw (named as "open claw" in the video), OpenCode (compared for in-prompt customization), QM (a harness the channel covered earlier, name as spoken)

## Relevance to our work
- **agentos** (1/3): The append-only trajectory log (system prompt, reasoning, tool calls, per-step tokens) is a reference shape for per-turn agent traces, relevant to the L4 observability work. No storage or schema detail is shown. → *Compare the trajectory log's per-turn fields with the Postgres/Timescale trace schema we plan for AgentOS L4, and decide whether reasoning tokens should be captured separately.*
- **prosharness** (1/3): An append-only event log could double as a checkpoint and resume format for long Claude Code runs, which is a ProsHarness goal. The video does not show whether replay is supported. → *Consider whether ProsHarness checkpoints can be an append-only event log that supports replay, not only state snapshots.*
