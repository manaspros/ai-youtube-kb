# I Just Saved $1600 With GLM 4.5

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `yD4qcd_8o2U` · [watch](https://youtu.be/yD4qcd_8o2U) · **date:** 2025-11-02 · **length:** 10:18 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** AI LABS host (unnamed) · **orgs:** ZAI, Anthropic, Lindy, Cursor
- **topics:** token-cost-efficiency, coding-agents, models-research · **tags:** GLM, GLM 4.5, Claude Code, cost, usage limits, prototyping, superdesign, parallel agents, git worktrees, Cline, Kimi K2

> AI LABS walkthrough of ZAI's $3 GLM Coding Lite plan as a cheaper Claude Code backend, with the author's side-by-side UI test and a claim of roughly $1600 saved; the cost case rests on prompt counts and one subjective comparison.

## Summary
The presenter says Claude Code quality and usage limits frustrated them, and that Anthropic admitted some quality degradation for Sonnet 4 and Opus 4.1 users. They switch Claude Code to ZAI's GLM coding plan by setting an API base URL and override environment variables manually. The Lite plan is quoted at $3 for about 120 prompts per 5-hour window, and the Pro plan at $15 for about 600 prompts, with promotional pricing that rises to $6 and $30 after the first month. In a single UI-mockup test (a model comparison studio), the presenter finds GLM very fast but needing reprompts, while Claude produced cleaner output with better animation. The video then argues that cheap prompt volume makes parallel workflows (git worktrees) and iterative prototyping with superdesign.dev affordable. Benchmark claims are repeated from ZAI with no independent verification, and the video contains a sponsor segment.

## Key ideas
- **Claude Code usage limits and perceived quality drops motivated the switch** — The presenter says the limits were never sustainable and that Anthropic acknowledged quality issues affecting a small share of Sonnet 4 users, then Opus 4.1. The presenter says the impact felt larger than Anthropic suggested. This is anecdotal and not verified. ([0:00](https://youtu.be/yD4qcd_8o2U?t=0))
- **GLM coding plan as a cheap Claude Code backend** — ZAI offers a plan that works with Claude Code and other agents. The Lite plan is quoted at $3 for about 120 prompts per 5-hour window. The presenter uses it through Claude Code's hooks and sub-agents. The plan is advertised as Claude Code-exclusive but works with other agents too. ([2:04](https://youtu.be/yD4qcd_8o2U?t=124))
- **Price and prompt comparison against Claude plans** — The Pro plan is quoted at $15 for 600 prompts per 5 hours, compared with Claude Code's $20 plan at about 45 prompts and the $100 plan at 50 to 200 prompts. Promo pricing applies only to the first month and then rises to $6 and $30. ([3:09](https://youtu.be/yD4qcd_8o2U?t=189))
- **Setup is manual env var override with the GLM base URL** — After getting an API key, the presenter sets an override environment variable and an API base URL manually rather than by script, then runs Claude Code in the target folder. The same plan also works with Cline. ([4:05](https://youtu.be/yD4qcd_8o2U?t=245))
- **Single-prompt UI comparison: GLM is fast but needs reprompting** — Both models got identical prompts to build a mock model-comparison studio UI. GLM's response time was very fast. Its first output needed polish and reprompting, while Claude's output was cleaner and had better animation. The presenter concludes the gap is in polish, not capability, and that prompting matters. ([5:05](https://youtu.be/yD4qcd_8o2U?t=305))
- **Cheap prompt volume enables parallel worktree workflows** — Running several instances in parallel across separate git worktrees (previously shown with Conductor and the BMAD method) becomes affordable at this prompt volume. The presenter presents this as a benefit of cheap prompts, not as a measured result. ([6:21](https://youtu.be/yD4qcd_8o2U?t=381))
- **Iterative UI prototyping with superdesign.dev** — The presenter uses the open-source superdesign.dev extension, which renders HTML design variations on a canvas and works with Claude Code, Cursor, or other agents. It generated three color-scheme variations from one message, with a minor overlap issue, and then iterated on chat bubble animation. ([7:23](https://youtu.be/yD4qcd_8o2U?t=443))

## Techniques
- **Point Claude Code at GLM via env var override** — Get an API key from the ZAI platform's API section. Follow the GLM coding plan docs' Claude Code integration section. Set the override env var and API base URL manually (the presenter chose manual setup over a script). Run claude from the target folder. Exact variable names are not spoken in the transcript; check the docs. *When:* When you want a cheaper or higher-volume backend for Claude Code and can accept a different model's quality tradeoffs.
- **Same-prompt side-by-side model comparison** — Give identical prompts to Claude Code on its default Claude models and to Claude Code with the GLM override, in separate folders. Compare first-pass output, then reprompt once to see whether the gap closes. *When:* When evaluating a cheaper model for UI or frontend work, to separate first-pass quality from quality after reprompting.
- **Parallel agents in separate git worktrees** — Split a task into parallel workstreams, then run each agent in its own git worktree (the presenter used Conductor and the BMAD method). Cheap prompt volume is what makes running many instances practical. *When:* When a task splits cleanly into independent subtasks and prompt cost is the limiting factor.
- **HTML-first UI prototyping on a canvas** — Use superdesign.dev to have the agent generate HTML design variants (same layout, different color schemes), view them on its canvas, pick one, then ask for targeted changes such as animation tweaks. *When:* When exploring visual design variations quickly, and iteration cost matters more than the first output's polish.

## Numbers
- GLM Coding Lite plan: $3 for about 120 prompts per 5-hour window (intro price; $6 after the first month) ([2:04](https://youtu.be/yD4qcd_8o2U?t=124))
- GLM Pro plan: $15 for 600 prompts per 5-hour window (intro; $30 after the first month) ([3:09](https://youtu.be/yD4qcd_8o2U?t=189))
- Claude Code $20 plan: about 45 prompts (presenter's figure); $100 plan: 50 to 200 prompts ([3:09](https://youtu.be/yD4qcd_8o2U?t=189))
- Earlier Anthropic docs cited for the $20 plan: 10 to 40 prompts ([1:00](https://youtu.be/yD4qcd_8o2U?t=60))
- ZAI benchmark record vs Claude 4 (from ZAI): GLM won 40%, tied 10%, lost 50% ([2:04](https://youtu.be/yD4qcd_8o2U?t=124))
- Presenter says the $1600 saving in the title is not computed in the video body ([0:00](https://youtu.be/yD4qcd_8o2U?t=0))

## Hot takes
- The title's "$1600 saved" figure is not derived in the video. The argument relies on quoted prompt counts and the presenter's own choice of plan.
- The benchmark numbers come from ZAI itself and are presented without independent verification.
- The UI test is one prompt and one design, judged subjectively by the presenter. The conclusion that GLM 'isn't performing like an older AI system' is not backed by a measured comparison.
- Claude's quality-degradation admission is presented as a motive, but the presenter's evidence is anecdotal and includes unverified 'many users' claims.
- The video contains a sponsor segment (Lindy Build) mid-video.
- Quality is capped at 3 (solid practitioner content, with a clear first-hand setup and test), since the evidence is one anecdotal test and one vendor-sourced benchmark.

## Tools mentioned
GLM (GLM 4.5 coding plan, ZAI), Claude Code, Cline, superdesign.dev, Conductor, BMAD method, Cursor, Codex, Kimi K2, Lindy Build

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and plans to run long agent runs. A cheap backend with many prompts per 5-hour window would change plan and loop cost, and the video explicitly covers hooks, sub-agents and parallel worktrees. → *Benchmark a ProsHarness plan-critique-debate loop on a GLM override against the Claude backend, counting prompts per completed task and first-pass quality, before adopting it as a default.*
- **agentos** (1/3): AgentOS routes agent traffic through a proxy and could treat GLM as one more cheap backend, but the video only shows manual env override, with no proxy or routing. → *Consider adding GLM as a low-cost backend in the AgentOS routing config and compare its cost per task against the Claude backend on the same prompt set.*
