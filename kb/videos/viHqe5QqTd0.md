# Opus 5 Built An F1 Game... for $1,200

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `viHqe5QqTd0` · [watch](https://youtu.be/viHqe5QqTd0) · **date:** 2026-09-02 · **length:** 10:08 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Better Stack presenter (unnamed) · **orgs:** Better Stack, Anthropic
- **topics:** multi-agent, agent-architecture, testing-verification, token-cost-efficiency · **tags:** gauntlet-loop, opus-5, sub-agents, critic-loop, screenshot-verification, self-built-tools, cost, vibe-coding, game-generation

> A Better Stack host runs the "Gauntlet Loop" prompt (a goal plus a real-world target, sub-agents, and a screenshot-based critic loop) on Opus 5 to build an F1 racing game, then judges how playable the result is and what it cost.

## Summary
The host reproduces a viral "Gauntlet Loop" prompt, originally shared by Matt Shumer as a Call of Duty-style shooter, changing only the target to a Formula 1 game. A lead agent coordinates about 30 sub-agents across five phases: foundation, parallel systems work, integration, then five "harsh art director" critics who score screenshots against a threshold of 90. Critic feedback goes back to the builders in a loop. The host stopped the run after 19 hours and about $1,200 of usage, at a final critic score of 67.3 that had plateaued in the 70s. The resulting game is a playable-looking but rough racing demo with menus, camera modes, a leaderboard, minimap and some penalties, and no finish screen or podium. The most useful part is the harness the model built for itself: screenshot, state-extraction and screenshot-diff tools, plus 136 single-purpose tools. The video is an entertaining single-run demo, not a controlled evaluation.

## Key ideas
- **The whole pattern is a goal plus a concrete real-world target, so the model has a reference to judge itself against. The presenter says the original prompt was about four sentences.** — The Gauntlet Loop gives a lead agent a goal and a real-world target (Call of Duty originally, Formula 1 in this test). Only the target was changed for this run. ([0:00](https://youtu.be/viHqe5QqTd0?t=0))
- **The loop is code, then screenshot-based critique, then feedback, then repeat. Sub-agents each own a small slice of the game.** — Each sub-agent codes its piece, a harsh critic looks at the screenshots, and the feedback goes back to the original agent. The loop runs until the critic is satisfied or the agents can go no further. The presenter says it ran for 19 hours before he stopped it. ([2:05](https://youtu.be/viHqe5QqTd0?t=125))
- **A meta-prompt step can generate the final working prompt. The presenter says the gauntlet pattern has a meta-prompt that asks an agent to write the prompt.** — A meta-prompt agent turns the idea into the concrete prompt. The presenter did not use this step and instead edited the original prompt. ([2:05](https://youtu.be/viHqe5QqTd0?t=125))
- **The run was organised as a 30-agent, five-phase workflow: foundation, systems, integrate, critique, then loop.** — One agent writes the core engine, 15 agents build systems (environment, models, camera effects), one agent integrates the output, and five critic agents score silhouettes, materials, lighting, world density and motion. The target score is 90 or more, and the critics' scores are broken into categories. ([2:05](https://youtu.be/viHqe5QqTd0?t=125))
- **The model built its own verification harness: three permanent tools plus 136 single-purpose tools.** — This is the most reusable part of the video: the agent extended its own toolset to make its feedback loop observable. ([3:29](https://youtu.be/viHqe5QqTd0?t=209))
- **The loop plateaued and the presenter had to stop it by hand. Critic scores improved over rounds but stalled in the 70s.** — After round five the score was 67.3. The presenter ran out of subscription allowance and time. Claude itself reportedly said the 90 target might be unrealistic. ([3:29](https://youtu.be/viHqe5QqTd0?t=209))
- **The result looks convincing in screenshots but is weak in play: steering is oversensitive, barriers fail, there is no finish screen, and the penalty system works.** — Track-limit and jump-start penalties do fire, the leaderboard, minimap, sparks and shadows work, and cars line up on the grid. Crashes pass through barriers, the cockpit and TV camera modes are rough, and after the finish line the race keeps running. ([4:50](https://youtu.be/viHqe5QqTd0?t=290))
- **The presenter did not read the code. The main value he sees is the generated assets and a fast first pass, not a playable product.** — He says he would not play it for more than five minutes in its current state, that a few more prompts could fix the barriers and handling, and that he has not looked at the code. ([9:22](https://youtu.be/viHqe5QqTd0?t=562))

## Techniques
- **Gauntlet loop (goal + real-world target + critic loop)** — Give a lead agent a goal and a concrete real-world reference (e.g. a known game genre or title). Have it spawn sub-agents that each build one slice of the system. Pass the output to a critic that looks at screenshots and scores against the reference. Feed the critique back to the builders, and repeat until a threshold (the run used 90) or until progress plateaus. The presenter's version: a foundation agent, then 15 systems agents, then one integration agent, then five critic agents with named criteria. The presenter's prompt text is not reproduced in the transcript; only the structure is described. *When:* Visual or interactive artifacts where a human-like judgment can be made from screenshots (games, UIs, 3D scenes), and where you have budget for many iterations.
- **Have the agent build its own verification tools** — Let the agent create (a) a screenshot tool that captures frames from multiple camera angles while the app runs, (b) a state-extraction tool that reports engine state (lighting, shadows, material types), (c) a screenshot comparison tool that flags regressions between rounds, and (d) small single-purpose test tools (e.g. A/B material comparisons, scripted input playback). Keep the permanent tools and reuse them each round. *When:* Long autonomous loops where the agent needs observable feedback beyond the code, or when you want a regression check between rounds.
- **Stop on plateau, not only on a threshold** — Track the critic score per round in a breakdown by category. Stop or change strategy when the score stops improving over several rounds, rather than running until the threshold is hit. In this run the score plateaued in the 70s. *When:* Any iterative critic loop, to limit cost and detect when the target is unrealistic.
- **Meta-prompt to generate the loop prompt** — Pass the base idea to an agent and ask it to write the final gauntlet prompt for you, then run that prompt. The presenter says this exists but did not use it. *When:* When you want to adapt the loop to a new target without hand-writing the full prompt.

## Numbers
- Presenter's first run cost about $1,000 in usage, and the total at stop was about $1,200 after 19 hours. ([0:00](https://youtu.be/viHqe5QqTd0?t=0))
- Loop ran for 19 hours before the presenter stopped it. ([2:05](https://youtu.be/viHqe5QqTd0?t=125))
- Workflow of 30 agents in 5 phases: 1 foundation, 15 systems, 1 integration, 5 critics, then loop. Critic target score: 90 or more. ([2:05](https://youtu.be/viHqe5QqTd0?t=125))
- Final critic score 67.3 at round 5, with plateau in the 70s. ([3:29](https://youtu.be/viHqe5QqTd0?t=209))
- Model made 3 permanent tools and 136 single-purpose tools, and took over 2,000 screenshots. ([3:29](https://youtu.be/viHqe5QqTd0?t=209))
- Total usage: 1.7 billion tokens across 137 agents. ([3:29](https://youtu.be/viHqe5QqTd0?t=209))
- Presenter's first-person shooter claim: about 50,000 lines of code from one prompt of about four sentences. ([0:00](https://youtu.be/viHqe5QqTd0?t=0))

## Hot takes
- The Gauntlet Loop is a viral demo pattern whose headline numbers come from one run by one presenter, with no baseline or repeat runs, so it is anecdotal.
- The 'for $1,200' title makes the cost the hook, but the video's own critic score plateaued at 67.3, so 'AAA-quality' framing is not supported.
- Reusing a model-built screenshot-and-state harness is more practical than the game itself: the harness is the transferable part.
- Calling the output 'no external assets' and 'Opus 5 built it' cannot be verified from the video; the presenter did not inspect the code.

## Tools mentioned
Claude Opus 5, Claude (Max plan subscription, used for the run), Claude sub-agents, Gauntlet Loop prompt (Matt Shumer)

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs long agent loops around Claude Code. The plateau-based stop, per-round checkpointing and self-built verification tools map directly onto checkpoint/resume and loop control. → *Add a plateau detector to long loops (stop after N rounds without score gain) and a per-round checkpoint of the critic score and artifacts so a run can resume or be cut off with state intact.*
- **agentos** (1/3): The critic-plus-screenshot loop and per-round score breakdown are a visual eval pattern. This is a light, one-off example, not a rigorous eval method. → *Log per-round critic scores by category (with a plateau stop condition) if we build a sub-agent eval loop for a UI or artifact.*
