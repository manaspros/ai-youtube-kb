# The End of Apps — Kitze, Sizzy.co

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `4fntwuOoedA` · [watch](https://youtu.be/4fntwuOoedA) · **date:** 2026-05-18 · **length:** 20:18 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Kitze · **orgs:** Sizzy.co, Tinkerer Club
- **topics:** agent-architecture, product-ux, multi-agent, memory · **tags:** openclaw, personal-agents, life-os, nested-topics, specialized-agents, cron, memory, local-first, codex, claude-code, wolfer, prediction

> Kitze (Sizzy.co) on his personal-agent journey, from to-do apps to OpenClaw-style agents, and his view that apps will give way to a personal agent OS that prompts the user.

## Summary
Kitze traces his 25-year search for a productivity system, from text files and Tasker through the Benji app to OpenClaw, a personal agent framework that talks through Telegram or Discord. He argues that chat apps are the wrong UI for a life OS and that one agent with all of a person's context is less useful than specialized agents organized in nested topics. He describes Wolfer, his own experimental Codex-based wrapper with predictable multi-topic conversations, cron labeling, and per-agent UI. He says current agents are unreliable on cron jobs, multi-agent handoffs, and memory. His prediction is that computers will invert the prompt flow so the AI asks the user for decisions, with local agents (possibly Apple's) replacing most consumer apps. The talk is opinionated and anecdotal, with no benchmarks.

## Key ideas
- **Specialized agents beat one general agent for personal use** — A single one-on-one chat with one agent loaded with all of a person's life context is a poor setup. Separate agents per domain (work, family, fitness) each get a provider, thinking level, system prompt, tools, and permissions. ([9:21](https://youtu.be/4fntwuOoedA?t=561))
- **Nested topics as context instead of memory** — In Wolfer, each new topic inherits the descriptions of all its parent topics in the first prompt. The agent gets project context from the tree itself, so it does not need a memory system to find it. He says he does not believe in agent memory. ([15:24](https://youtu.be/4fntwuOoedA?t=924))
- **Chat apps like Discord and Telegram are the wrong UI for a life OS** — Discord and Telegram were built for conversation, so they are being bent into agent management. Multi-agent work needs visible tool calls, stop buttons, per-agent model and capability views, and knowledge bases. ([10:37](https://youtu.be/4fntwuOoedA?t=637))
- **Cron and multi-agent reliability is the current blocker** — OpenClaw-style setups often fail on cron jobs, agent-to-agent messages, and forgetting recent messages. This is why many users in his community have stopped using them. ([10:37](https://youtu.be/4fntwuOoedA?t=637))
- **Cron messages should be labeled with the conversation they came from** — In his setup a cron message reads the whole conversation and is tagged as cron, so the agent does not seem to appear from nowhere. He treats this as a UI and context-design point. ([16:30](https://youtu.be/4fntwuOoedA?t=990))
- **Prediction: the AI prompts the user, and apps mostly disappear** — He expects the flow to invert, with the agent working in the background and asking for decisions or forms. The UI would be generated on the fly, and only specialist software such as color grading would remain as standalone apps. ([17:32](https://youtu.be/4fntwuOoedA?t=1052))
- **Local models may make Apple-style local agents good enough for most people** — He argues that a local agent with tool access to installed apps, and no data leaving the device, will satisfy most normal users, so he expects Apple to win the consumer side. This is a bet, not a measured result. ([18:29](https://youtu.be/4fntwuOoedA?t=1109))

## Techniques
- **Nested topic description injection** — Each conversation topic has a description. When a new topic starts, the system injects the descriptions of all ancestor topics into the first prompt, so the agent gets the full project context without retrieval. *When:* Multi-project personal or team agents where context is naturally hierarchical and a memory system would be unpredictable.
- **Per-topic specialized agents** — Each agent is a package of provider, model thinking level, system prompt (soul), tool and MCP list, and permissions. Each agent gets its own topic or workspace and is kept separate from the others. *When:* When one general agent starts to confuse its domains, for example a coding skill set and a personal-admin skill set in the same session.
- **Labeled cron messages with full conversation context** — A scheduled trigger reads the whole conversation history and is marked as cron in the transcript, so the agent knows where the message came from. *When:* Any scheduled or background agent job whose output must make sense to the user later.
- **Visible tool-call UI** — Show tool calls as collapsible, expandable items with loading spinners and a stop button, and let the user see which agent and capability is active in each topic. *When:* Watching or steering long-running agents where the user needs to know what is running and can stop it.

## Numbers
- Community size: a first OpenClaw Discord had fewer than 100 people with working setups ([7:00](https://youtu.be/4fntwuOoedA?t=420))
- Talk was time-boxed to 18 minutes, so only part of the use cases was shown ([9:21](https://youtu.be/4fntwuOoedA?t=561))
- Cloud Cowork is said to do about 5% of what OpenClaw does (his estimate, no measurement) ([13:17](https://youtu.be/4fntwuOoedA?t=797))
- Weekly meetup attendance fell from an initial sign-up surge to about five people ([10:37](https://youtu.be/4fntwuOoedA?t=637))

## Hot takes
- Most people will not vibe-code, and most consumer apps will disappear, replaced by a generated UI.
- Agent memory is overrated. Nested topic context is enough for most personal use.
- Apple's local-first Siri-style agent may win the mainstream because local models are getting good.
- Discord and Telegram will never be the right UI for managing a life with agents.

## Tools mentioned
OpenClaw, Hermes, Paperclip, Codex, Claude Code, Claude Cowork, Tmux, Telegram, Discord, Tasker, IFTTT, Notion, Wolfer

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code and handles loops, schedules and checkpoints. The talk's cron reliability complaints and labeled-cron pattern apply directly to scheduled runs. → *Check how ProsHarness labels scheduled-run messages and whether its scheduled runs read the full session context, as the talk describes for cron messages.*
- **agentos** (1/3): Specialized per-topic agent packages and nested topic context are a different design from AgentOS's tiered memory. Also a useful UI reference for a multi-agent control surface. → *Consider a nested-topic context option in AgentOS as a memory-free alternative to MemoryMesh for scoped agents, and compare it against the retrieval-first design.*
- **general** (1/3): Anecdotal practitioner view on multi-agent reliability problems (cron, handoffs, forgetting), useful as a failure-mode checklist. → *Read as a list of failure modes to test against before trusting a multi-agent setup.*
