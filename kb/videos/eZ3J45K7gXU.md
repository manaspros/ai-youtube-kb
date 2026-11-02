# The Open-Source Copilot Alternative Devs Are Switching To (Tabby)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `eZ3J45K7gXU` · [watch](https://youtu.be/eZ3J45K7gXU) · **date:** 2026-04-02 · **length:** 6:15 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed) · **orgs:** Better Stack
- **topics:** local-ai, coding-agents, dev-tools · **tags:** tabby, self-hosted, code-completion, copilot-alternative, privacy, docker, vscode, local-llm, code-chat, team-controls

> Walkthrough of Tabby, a self-hosted AI coding server run via Docker and used from a VS Code extension, giving Copilot-style completions and repo-aware chat with code kept on your own machine. Short promotional demo with little exact setup detail.

## Summary
The presenter argues that cloud coding assistants like Copilot can send code off the machine, may use it for training, and need a subscription and internet access. He presents Tabby as an open-source self-hosted coding server: you run one Docker command, choose the models you want, and point a VS Code extension at the local server. The demo shows multi-line tab completions, chat that uses repo context, refactoring and test generation from selected code, and a comment that gets turned into an implementation. Chat history is saved in the local Tabby web UI. He compares Tabby with Copilot (easiest, cloud), Continue (flexible, power-user), and a tool transcribed as Tab9 (likely Tabnine, enterprise-focused). He cites SSO, RBAC and audit logs as team features. He is candid about trade-offs: output quality depends on the model, smaller models are weaker, a GPU helps a lot, setup takes more work than cloud tools, and code still needs review. His verdict is that Tabby suits privacy-focused, subscription-averse, regulated or team settings, while cloud tools stay easier for the strongest model with zero setup. No benchmarks, model names or exact config are shown; the presenter points to links in the description.

## Key ideas
- **Cloud coding assistants may send code off the machine and possibly into training data; the presenter frames self-hosting as the answer.** — Tabby is positioned as a self-hosted coding server so code stays inside the user's network. The presenter also says the cost of cloud tools is hidden (per-seat monthly fees, internet dependence). ([0:00](https://youtu.be/eZ3J45K7gXU?t=0))
- **Setup is one Docker command plus a VS Code extension pointed at the local server.** — After that, multi-line completions work in the repo. The Tabby web UI shows the models in use, which all run locally. ([1:22](https://youtu.be/eZ3J45K7gXU?t=82))
- **Chat and refactor features use repo context, not just the open file.** — Selected code can be sent for refactoring, performance tuning or test generation, and a comment describing a feature can be turned into an implementation. Chat history stays in the local web UI. ([1:22](https://youtu.be/eZ3J45K7gXU?t=82))
- **Tabby is framed as a dedicated server rather than a plugin, with team-level controls.** — The presenter compares Copilot (easiest, cloud), Continue (flexible, power-user), and a tool transcribed as Tab9 (likely Tabnine, enterprise-focused). He says Tabby combines Copilot-like UX with Continue-style flexibility and team controls. ([3:43](https://youtu.be/eZ3J45K7gXU?t=223))
- **Quality depends on the chosen model and on hardware.** — Smaller models are less capable, and a GPU helps for smooth performance. The presenter ran it on a Mac M4 Pro and found it usable. ([4:34](https://youtu.be/eZ3J45K7gXU?t=274))
- **Setup is more work than cloud tools and still needs human code review.** — The presenter says the setup is not suited to non-technical users, and that AI-generated code should still be reviewed. ([4:34](https://youtu.be/eZ3J45K7gXU?t=274))
- **Decision rule: Tabby for privacy, subscription aversion, regulated environments or team reliance; cloud tools for the best model with zero setup.** — The presenter's summary is that the trade-off has narrowed: the choice is now between convenience and capable AI on your own terms. ([5:58](https://youtu.be/eZ3J45K7gXU?t=358))

## Techniques
- **Run a self-hosted completion and chat server, then point the IDE at it** — Start Tabby with a single Docker command (the exact command is not shown; the video says links are in the description). Pick the models in the Tabby web UI, then install the VS Code extension and set its server URL to the local instance. Completions and chat then go to localhost. *When:* When source code must not leave the network, when working offline, or when you want to avoid per-seat subscriptions and are willing to supply a GPU.
- **Use selected-code actions for refactor, perf and tests** — Highlight a block in the editor and ask chat to refactor, optimise for performance, or add tests. Write a descriptive comment and let completion generate the implementation below it. *When:* For reshaping legacy code, adding tests and docs, or learning an unfamiliar framework inside your own repo.
- **Match the model to hardware before judging quality** — Expect weaker output from smaller models and slow output without a GPU. Compare models in the server UI before deciding the tool is bad. *When:* Before evaluating any local coding assistant, so a poor result is not blamed on the tool alone.

## Numbers
- Tabby is described as having over 33,000 GitHub stars. ([0:00](https://youtu.be/eZ3J45K7gXU?t=0))
- Setup is one Docker command; the demo ran on a Mac M4 Pro. No latency, token or cost figures are given. ([1:22](https://youtu.be/eZ3J45K7gXU?t=82))
- Quality depends on the model and a GPU helps a lot for smooth performance. No benchmark figures are given. ([4:34](https://youtu.be/eZ3J45K7gXU?t=274))

## Hot takes
- Cloud tools may use your code to train their models. The video offers no source for this claim.
- The presenter says cloud tools are not free because users pay per developer each month. The video gives no cost comparison.
- Title hype ('Devs Are Switching To') is not backed by adoption data. The video also has no exact commands, model names or benchmarks.
- Tabby 'is not trying to be the smartest AI, it's trying to be the one we can trust.' This is marketing framing, not evidence.

## Tools mentioned
Tabby (self-hosted AI coding server, Docker), VS Code (Tabby extension), Docker, GitHub Copilot, Cursor, Continue (transcribed as 'Continued Dev'), Tab9 (transcript name; likely Tabnine), Mac M4 Pro (hardware used for the demo)

## Relevance to our work
- **agentos** (1/3): Self-hosted local-model tooling is adjacent to AgentOS's self-hosted stance, but Tabby is a developer IDE tool rather than agent infrastructure. → *Low priority: if local autocomplete is wanted on the RTX 5090 box, try Tabby as a standalone dev tool. Nothing in AgentOS changes.*
