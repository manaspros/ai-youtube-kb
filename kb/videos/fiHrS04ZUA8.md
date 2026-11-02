# Claude Might Be Going In A Different Direction + More

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `fiHrS04ZUA8` · [watch](https://youtu.be/fiHrS04ZUA8) · **date:** 2025-12-02 · **length:** 9:26 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** OpenAI, GitHub, Google, Anthropic, IBM, Scalekit
- **topics:** models-research, security-guardrails, coding-agents · **tags:** weekly-news, gpt-5.1, codex, gemini-3, nano-banana-2, google-deep-research, anthropic-threat-report, claude-code, mcp, usage-limits, ibm-quantum, sponsored-segment

> AI LABS weekly roundup (Dec 2025) covering GPT-5.1, Gemini 3 leaks, Google agents, an Anthropic robot-dog experiment, an Anthropic report on a Claude Code-driven espionage campaign, and IBM quantum processors.

## Summary
This is a short weekly news roundup from the AI LABS channel covering the week of late November 2025. It reports OpenAI's GPT-5.1 rollout (Instant as default, Thinking for complex tasks) and GPT-5.1-Codex-Mini in Codex, which the speaker says gives more usage and auto-switches once a user hits 90% of their limit. It covers unconfirmed leaks of Gemini 3 and "Nano Banana 2" image capabilities, plus Google's Gemini navigation in Maps, the Opal app builder, Deep Research with Gmail/Drive/Chat sources, and Ads and Analytics advisor agents. The most relevant item for us is Anthropic's report on a state-linked campaign that used Claude Code with MCP servers to attempt intrusions into about 30 targets, detected in mid-September 2025. It also mentions a small Anthropic experiment where a Claude-assisted team finished robot-dog programming tasks faster than a control team, IBM's Nighthawk and Loon quantum processors, and a Minecraft AI agent. A sponsored segment for Scalekit appears mid-video. Most items are announcements or leaks with no benchmarks or methodology, so treat them as headlines to verify rather than evidence.

## Key ideas
- **OpenAI rolled out GPT-5.1 on Nov 12 as two variants: Instant (warmer, default in ChatGPT) and Thinking (more reasoning for complex tasks). Users report better conversational tone and instruction following.** — Presented as a response to criticism that GPT-5 gave worse answers than earlier models. The speaker relays user reports rather than measurements. ([0:00](https://youtu.be/fiHrS04ZUA8?t=0))
- **GPT-5.1-Codex-Mini was added to Codex as a smaller, cheaper variant that the speaker says gives up to 4x more usage. Users are auto-switched to it at 90% of their usage limit.** — Usage-limit fallback to a cheaper model is the pattern to note. GitHub Copilot also added GPT-5.1 Codex and its mini variant in public preview. ([1:03](https://youtu.be/fiHrS04ZUA8?t=63))
- **Gemini 3 and Nano Banana 2 were reportedly leaked to testers. The claims are anecdotal: one-prompt browser macOS clone, strong front-end output, and reassembling torn-up pages.** — No evaluation or source is given. The speaker presents these as leaks and expectations, not verified results. ([1:55](https://youtu.be/fiHrS04ZUA8?t=115))
- **Google shipped several Gemini features: voice navigation in Google Maps with rerouting and stops (rollout starts with Android Auto, US first), the Opal no-code app builder (experimental, free in beta), and Deep Research with user-selected sources.** — Deep Research sources include Gmail, Drive, Google Chat and file uploads. It proposes a plan the user can edit before research starts, then produces a sourced report. ([3:55](https://youtu.be/fiHrS04ZUA8?t=235))
- **Google announced Ads Advisor and Analytics Advisor agents that work inside Google Ads and analytics accounts, for campaign management and trend or report generation.** — Access was said to arrive early next month. No details on how they are evaluated. ([5:12](https://youtu.be/fiHrS04ZUA8?t=312))
- **An Anthropic experiment gave two teams of two engineers with no robotics background the task of programming a robot dog, one team with Claude and one without. The Claude team finished much faster; both finished.** — The speaker draws the conclusion that AI may transform robotics as it has software. No task counts, timings or methodology are given, so the sample is too small to generalize from. ([6:17](https://youtu.be/fiHrS04ZUA8?t=377))
- **Anthropic reported a spying campaign detected in mid-September 2025 that it linked to Chinese state-sponsored groups. The operator used Claude Code with MCP servers to collect data and scan for vulnerabilities, targeting about 30 global organizations with partial success.** — This is the most relevant item for agent security: the agent's tool access and multi-step autonomy were the attack surface. The transcript is garbled near the end of this segment, so check the original Anthropic write-up for the exact details. ([7:04](https://youtu.be/fiHrS04ZUA8?t=424))
- **IBM launched the Nighthawk and Loon quantum processors at its Quantum Developer Conference on Nov 12. Nighthawk is claimed to be 30% faster than prior processors, and IBM targets quantum advantage by end of 2026 and fault-tolerant computing by 2029.** — The speaker ties quantum speed to faster AI training, which is speculation and not an IBM claim as reported here. ([7:04](https://youtu.be/fiHrS04ZUA8?t=424))
- **Minecraft added an AI agent called Steve that builds structures from a simple prompt, so the player does not place blocks one by one.** — Only a product mention with no details on how it works. ([8:22](https://youtu.be/fiHrS04ZUA8?t=502))

## Techniques
- **Usage-limit fallback to a smaller model** — When a user reaches about 90% of their subscription usage limit in Codex, route further requests to a smaller, cheaper model (GPT-5.1-Codex-Mini), which the speaker says gives up to 4x more usage. *When:* Use when a coding agent has a hard usage cap and you prefer degraded quality over a stopped session. Relevant to ProsHarness model switching and token budgeting.
- **Plan-then-approve for deep research** — Gemini Deep Research first proposes a research plan, lets the user edit it, runs the research over user-selected sources (Gmail, Drive, Chat, uploads), and returns a sourced report with links. *When:* Use as a UX pattern for agent tasks where the user should approve the plan before expensive retrieval and synthesis run.

## Numbers
- GPT-5.1-Codex-Mini gives up to 4x more usage than GPT-5-Codex and is used automatically at 90% of the usage limit. ([1:03](https://youtu.be/fiHrS04ZUA8?t=63))
- IBM Nighthawk is claimed to deliver 30% higher performance than previous IBM processors. ([7:04](https://youtu.be/fiHrS04ZUA8?t=424))
- Anthropic's espionage campaign was detected in mid-September 2025 and targeted about 30 global organizations, with partial success. ([7:04](https://youtu.be/fiHrS04ZUA8?t=424))
- IBM targets quantum advantage by end of 2026 and fully functional quantum computing by 2029. ([7:50](https://youtu.be/fiHrS04ZUA8?t=470))
- Robot-dog experiment: two teams of two engineers each, with and without Claude. No task counts or timings given. ([6:17](https://youtu.be/fiHrS04ZUA8?t=377))

## Hot takes
- The Gemini 3 and Nano Banana 2 capability claims rest on unverified leaks and anecdotes, presented as expectations.
- The robot-dog study is one anecdote with no sample size, timings or methodology, yet the speaker generalizes to robotics being transformed.
- The quantum-to-faster-AI link is the speaker's speculation, not something IBM is quoted as saying here.
- Sponsored segment for Scalekit (passwordless auth) mid-video, which caps quality.
- The Anthropic espionage item is the only substantive security story, and the transcript is garbled at the key moment, so check the primary Anthropic source.

## Tools mentioned
GPT-5.1, GPT-5.1 Instant, GPT-5.1 Thinking, GPT-5.1-Codex, GPT-5 Codex Mini, Codex, ChatGPT, GitHub Copilot, Gemini 3, Nano Banana 2, Google Maps, Google Opal, Gemini Deep Research, Google Ads Advisor, Google Analytics Advisor, Claude, Claude Code, MCP servers, IBM Quantum Nighthawk, IBM Quantum Loon, Minecraft AI agent Steve, Scalekit

## Relevance to our work
- **agentos** (1/3): The Anthropic report on Claude Code plus MCP servers being used for multi-step intrusion is a concrete threat model for agents with tool access, relevant to exec-gate and prompt-injection guardrails. → *Read Anthropic's published write-up on the mid-September 2025 Claude Code campaign and check whether AgentOS exec-gate rules cover multi-step tool chaining over MCP servers, not just single calls.*
- **prosharness** (1/3): Codex's auto-switch to a smaller model at 90% of usage is the same fallback ProsHarness would need around the Claude Code CLI when a budget is near exhaustion. → *Consider a budget-threshold model fallback in the ProsHarness loop runner, logged so a checkpointed run can resume on the cheaper model.*
