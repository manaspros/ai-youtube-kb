# Why Developers Are Switching from Claude

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `XKdeJAKTb3M` · [watch](https://youtu.be/XKdeJAKTb3M) · **date:** 2025-11-02 · **length:** 9:22 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed) · **orgs:** Anthropic, Z.ai, OpenAI
- **topics:** models-research, coding-agents, token-cost-efficiency · **tags:** model-comparison, glm-4.6, sonnet-4.5, gpt-5-codex, opencode, cost, token-usage, coding-benchmark, vibe-coding

> Better Stack runs Sonnet 4.5, GLM 4.6 and GPT-5 Codex through three coding tasks in OpenCode (portfolio site, HN clone, Minecraft-like game); no model wins everywhere, and GLM 4.6 is pitched as the value pick.

## Summary
The video compares Claude Sonnet 4.5, GLM 4.6 and GPT-5 Codex by running the same prompts in OpenCode across three tasks of rising difficulty: a photographer portfolio site, a Hacker News clone with infinite scroll, caching, live comments and search, and a first-person Minecraft-style game. Sonnet 4.5 was consistently fastest and used the fewest tokens, but its outputs were not always the best. GPT-5 Codex produced the best portfolio design, GLM 4.6 won the HN clone, and the game was rough for all three, with the Sonnet and GLM builds needing fix prompts before they ran. The presenter's conclusion is that there is no standout model, and that GLM 4.6 is the practical choice on price. This is a single informal test with one run per model, and the video is partly sponsored by the GLM coding plan's pitch, so treat the rankings as anecdotal.

## Key ideas
- **Sonnet 4.5 was the fastest and used the fewest tokens on every task, but that did not translate to the best output.** — Across the portfolio, HN clone and game tasks, Sonnet 4.5 finished quickest (under 2 min for the portfolio, ~4 min for the HN clone, 1m46s for the game) and used the fewest tokens. The presenter still judged its results inferior on design and playability. ([0:00](https://youtu.be/XKdeJAKTb3M?t=0))
- **GPT-5 Codex won the portfolio task on design, despite being the slowest and most token-hungry on that run.** — It gave the photographer a name and site title and had a card hover effect. The presenter noted some image-length inconsistency. Sonnet 4.5 and GLM 4.6 both just used the generic title 'portfolio'. ([2:26](https://youtu.be/XKdeJAKTb3M?t=146))
- **GLM 4.6 won the Hacker News clone task on feature completeness and search quality.** — It finished in just over nine minutes with about half the tokens GPT-5 Codex used. It had a skeleton loader, nested comments, reply, and a fast search dropdown that worked without pressing enter. The presenter noted a duplicated 'Hacker News' label. GPT-5 Codex needed a follow-up fix for a 'initial story is not defined' error. ([3:53](https://youtu.be/XKdeJAKTb3M?t=233))
- **On the hardest task, the Minecraft-like game, none of the three produced a playable result without fix prompts.** — GLM 4.6 built an impressive-looking world in under four minutes but had a game-over loop and falling/lava issues. GPT-5 Codex took over 11 minutes and 86k tokens, needed a fix for an undefined variable, and had reversed controls. Sonnet 4.5 showed a blank screen and an unusably low frame rate after its fix. ([6:44](https://youtu.be/XKdeJAKTb3M?t=404))
- **The presenter's bottom line is that the models are not clearly separated, so cost decides the practical pick.** — He recommends GLM 4.6 mainly on price ($36 for the first year) and a higher usage quota than the Claude Pro plan. He flags the smaller 200K context window (vs. Sonnet's 1M), no multimodal support, and that data is processed in Singapore as possible drawbacks. ([8:12](https://youtu.be/XKdeJAKTb3M?t=492))

## Techniques
- **Same-prompt, same-harness model bake-off** — Run identical prompts through one agent harness (OpenCode) for each model, record time, tokens and cost, then open the output in a browser and test features by hand. The presenter put each model's result on a single task at a time (portfolio, HN clone, game). *When:* When you want a rough, apples-to-apples read on which model fits a coding task before committing to a plan or subscription.
- **Prompt-file execution** — Keep the task in a prompt file and tell the agent to run it (e.g. 'run the prompt file'), so each model gets the exact same instructions. *When:* When you want reproducible runs across models or agents.
- **Feed back runtime errors as follow-up prompts** — When the output fails, paste the console error (e.g. 'X is not defined') or a plain-language bug report back to the same agent and let it fix the issue. Inspect the browser elements or console to locate the problem first. *When:* When the first attempt runs but is broken, and you want to measure how quickly a model recovers rather than whether its first attempt is correct.

## Numbers
- Sonnet 4.5 portfolio site: under 2 minutes, about $0.15 ([1:10](https://youtu.be/XKdeJAKTb3M?t=70))
- GLM 4.6 portfolio site: about 2.5 minutes, cost reported as equal to Sonnet, which the presenter doubted ([1:10](https://youtu.be/XKdeJAKTb3M?t=70))
- GPT-5 Codex HN clone: about 20 minutes and over 150,000 tokens ([3:53](https://youtu.be/XKdeJAKTb3M?t=233))
- GLM 4.6 HN clone: just over 9 minutes, about half the tokens GPT-5 Codex used ([3:53](https://youtu.be/XKdeJAKTb3M?t=233))
- Sonnet 4.5 HN clone: just over 4 minutes, least tokens ([5:16](https://youtu.be/XKdeJAKTb3M?t=316))
- GLM 4.6 game: under 4 minutes (3m50s) to first build ([6:44](https://youtu.be/XKdeJAKTb3M?t=404))
- GPT-5 Codex game: over 11 minutes and 86,000 tokens ([6:44](https://youtu.be/XKdeJAKTb3M?t=404))
- Sonnet 4.5 game: 1 minute 46 seconds, least tokens ([6:44](https://youtu.be/XKdeJAKTb3M?t=404))
- GLM 4.6 price: $36 for the first year, quota higher than the Claude Pro plan ([8:12](https://youtu.be/XKdeJAKTb3M?t=492))
- GLM 4.6 context window: 200K (up from 128K); Sonnet 4.5 is 1M ([0:00](https://youtu.be/XKdeJAKTb3M?t=0))

## Hot takes
- Sonnet 4.5 is usually fastest and cheapest per task, but not always the best result.
- The presenter is not impressed by Sonnet 4.5's design versus Sonnet 4 on the HN clone task.
- GLM 4.6 is the way to go on price, even though it has the smallest context window and no multimodal support.
- There is no standout model across these three tasks.
- Data sent to Singapore is a caveat for GLM 4.6.

## Tools mentioned
Claude Sonnet 4.5, GLM 4.6 (Z.ai), GPT-5 Codex, OpenCode, Unsplash, TanStack

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and plans to drive other models through critique and debate; the per-model cost, time, and failure comparison is directly relevant to choosing critic models. → *Run a small same-prompt bake-off through ProsHarness with Sonnet, GLM, and Codex, and record tokens, wall time, and fix-prompt count per task to inform the plan-critique-debate model choice.*
- **agentos** (1/3): Cheap-model routing is relevant to AgentOS strategy routing, but this is a single anecdotal three-task test, not a benchmark. → *If strategy routing is built, log tokens and wall time per model per task in the Govrix telemetry to see whether a cheaper model holds up for a given task type.*
