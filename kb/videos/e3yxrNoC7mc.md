# OpenAI Codex Hacked: Use It with Gemini 2.5 PRO (The Best Coding Model)

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `e3yxrNoC7mc` · [watch](https://youtu.be/e3yxrNoC7mc) · **date:** 2025-11-02 · **length:** 6:37 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** OpenAI, Google, OpenRouter, Ollama
- **topics:** coding-agents, context-engineering · **tags:** codex-cli, gemini-2.5-pro, open-source-fork, multi-provider, full-auto, config-json, instructions-md, scope-control

> Walkthrough of setting up a multi-provider fork of OpenAI's Codex CLI with Gemini 2.5 Pro, including config files and full-auto use, plus a failed full-scope attempt and a narrowed retry.

## Summary
AI LABS walks through installing an open-source fork of OpenAI's Codex terminal agent that accepts non-OpenAI providers, then runs it with Gemini 2.5 Pro. Setup is an npm global install, an API key exported in the shell, a config.json naming the provider and default agentic model (copied from the repo's table), and an optional instructions.md for custom guidance. The speaker says a Gemini key needs a billing-enabled Google Cloud project, since a free key won't work with 2.5 Pro. He runs full-auto mode with one prompt: asking for every feature at once made the agent stall on one of them and burn credits. Restarting with a basic scope produced a to-do app with dark mode, shadcn/ui components and JSON-file persistence. The evidence is one demo plus the speaker's own impressions of model quality, with no benchmarks or cost figures.

## Key ideas
- **OpenAI's open-source Codex CLI was forked to support other model providers, so Gemini 2.5 Pro can drive the terminal agent.** — The speaker presents the fork's author as having changed the source to accept multiple providers. He cites Gemini 2.5 Pro's standing on the Chatbot Arena leaderboard and his own Swift cloning test as the reason to use it. ([0:00](https://youtu.be/e3yxrNoC7mc?t=0))
- **Provider choice is config-driven, and each provider has two defaults: an agentic model and a full-context model. The tool uses both.** — Per-provider setup (OpenAI, OpenRouter, Ollama, Gemini) is documented in the repo, and the Ollama option needs no key. ([1:15](https://youtu.be/e3yxrNoC7mc?t=75))
- **A Gemini key for 2.5 Pro needs a Google Cloud project with billing enabled; a free account does not work.** — The key is created in Google AI Studio by choosing a Cloud project. The speaker states the no-free-tier point without citing a source. ([2:16](https://youtu.be/e3yxrNoC7mc?t=136))
- **Shell exports last only for one terminal session, so provider config and custom instructions are kept in files.** — config.json holds the provider and default model string (copied from the repo table). instructions.md in the same Codex folder holds custom guidance the agent follows while generating code. ([2:16](https://youtu.be/e3yxrNoC7mc?t=136))
- **Run it inside a git-initialized repo, and use full-auto mode with a single prompt for greenfield builds.** — The speaker says the tool recommends a git repo, though he skips it for the test. In full-auto mode the agent asked clarifying questions about what 'fancy' meant before building. ([3:34](https://youtu.be/e3yxrNoC7mc?t=214))
- **Asking for every feature at once stalled the agent and burned credits; restarting with a basic scope worked.** — The agent got stuck on one feature and kept retrying without progress. The speaker restarted with a basic to-do app: shadcn/ui components, dark and light mode, toast notifications, JSON persistence, delete and complete actions. ([5:27](https://youtu.be/e3yxrNoC7mc?t=327))

## Techniques
- **Swap the model behind a forked CLI agent** — Install the fork globally with npm (-g). Export the chosen provider's API key in the shell. Create config.json in the Codex folder with the provider name and the default agentic model string, copied from the repo's provider table. Launch the CLI and send a test message to confirm the model responds. The video does not show the exact package name or config keys beyond these. *When:* You want a non-OpenAI model (here Gemini 2.5 Pro) inside a terminal coding agent without changing the agent's own tool loop.
- **Persist per-project agent setup in files, not shell exports** — Put the provider and default model in config.json. Put standing instructions in instructions.md in the same Codex folder. Set API keys as environment variables so they survive new terminal sessions, rather than re-exporting each time. *When:* You run the agent repeatedly and want the same provider and house rules every session.
- **Run the agent inside a git repo** — Run git init in the target directory before starting the agent, as the repo recommends. *When:* Before any agent run that writes code, so changes can be reviewed and reverted. The speaker skips this for his throwaway test.
- **Full-auto single-prompt build, then narrow scope on stall** — Paste one prompt that describes the app and enable full agent mode with a flag (the video does not name the flag; the status line showed approval mode set to full auto). Answer the agent's clarifying questions. If it loops on one feature, stop it and restart with a smaller feature set. *When:* Greenfield, low-stakes prototypes. Keep the first prompt narrow; a broad feature list risks stalls and credit burn. This is the speaker's experience from one run, not a measured method.

## Numbers
- Gemini 2.5 Pro is cited as top of the Chatbot Arena leaderboard. No score is given. ([0:00](https://youtu.be/e3yxrNoC7mc?t=0))
- Each provider has two default models: an agentic model and a full-context model. The tool uses both. ([1:15](https://youtu.be/e3yxrNoC7mc?t=75))
- Gemini 2.5 Pro has no free API tier. A billing-linked Google Cloud project is required. ([2:16](https://youtu.be/e3yxrNoC7mc?t=136))
- The full-scope attempt burned a lot of credits. No amount is stated. ([5:27](https://youtu.be/e3yxrNoC7mc?t=327))

## Hot takes
- Quality evidence for Gemini 2.5 Pro is one Swift cloning anecdote plus a leaderboard reference. No benchmark was run in the video.
- Title says 'Hacked' and 'The Best Coding Model', but the content is a setup walkthrough with one demo. Quality is capped at 2 for the hype title and thin substance.
- The demo itself partly failed: the full-scope prompt stalled and burned credits. The working app came only after the scope was cut.
- The speaker frames 'open source, so anyone can modify it' as the main value. In practice the fork swaps the model backend. It does not add new agent capabilities.

## Tools mentioned
OpenAI Codex CLI, OpenCodex (community fork of Codex CLI, name as spoken in the video; exact package name not stated), npm, Gemini 2.5 Pro, Google AI Studio, Google Cloud, OpenRouter, Ollama, shadcn/ui, Next.js, Cursor (used as the editor to open config.json), git, Chatbot Arena (leaderboard, cited for Gemini 2.5 Pro's ranking)

## Relevance to our work
- **agentos** (1/3): The fork's per-provider config (provider plus default agentic and full-context models) is a small instance of the multi-provider routing AgentOS's proxy does, but the video has no routing logic, budgets or telemetry. → *Compare the video's per-provider default model pair (agentic vs full-context) against how AgentOS's proxy picks models per request, and decide whether our routing config needs that split.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, not a multi-provider fork. The video's relevant lesson is scope control on a long run, which ProsHarness's checkpoint and plan steps already address. → *Nothing to adopt now. Revisit only if ProsHarness ever needs a non-Claude model behind its CLI loop.*
