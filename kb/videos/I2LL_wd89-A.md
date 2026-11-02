# How VS Code Went from Monthly to Weekly Releases with AI — Harald Kirschner

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `I2LL_wd89-A` · [watch](https://youtu.be/I2LL_wd89-A) · **date:** 2026-10-04 · **length:** 19:35 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Harald Kirschner · **orgs:** VS Code, GitHub
- **topics:** software-factory, pr-code-review, testing-verification, context-engineering · **tags:** VS Code, weekly releases, code survival, AGENTS.md, skills, TypeScript Go, Playwright, component browser, AI triage, error stacks, staged rollouts, VSCBench, evals, prototyping

> How the VS Code team moved from monthly to weekly releases by rebuilding its own dev system around agents: code-survival metrics, agent-readable repos, fast CI, UI feedback loops, AI triage, and staged rollouts.

## Summary
Harald Kirschner, a VS Code team member, describes how a team shipping to over 50 million users moved from monthly to weekly releases by changing the whole development system, not just adding more AI use. The team tracks code survival, the share of agent-written code that actually gets committed, which rose from 55% with GPT-4.1 to 86% with Claude Opus 4.6. Faster shipping created more issues and PRs, so they added agent-readable repo docs, skills that encode expert knowledge, and much faster builds (TypeScript Go). For UI work they built automated screenshot diffs and a Playwright-based launch skill so agents can check the running app. Code review is now mandatory on every PR with tiered effort, and AI triages issues and turns error stacks into auto-opened fix PRs. Releases moved from all-at-once to staged rollouts with error monitoring, and evals are bootstrapped from GitHub issues. The speaker's main point is that the bottleneck moves each time, so you should keep finding and fixing the next feedback-loop gap.

## Key ideas
- **Track code survival, not agent usage** — VS Code measures the percent of agent-written code that gets committed, so they can see how much output is thrown away. Survival rose from 55% (GPT-4.1) to 86% (Claude Opus 4.6) through harness improvements and new models. ([0:12](https://youtu.be/I2LL_wd89-A?t=12))
- **Faster shipping creates new quality and volume problems** — More agent-filed issues, more PRs from the team and community, and more low-quality automated issues. Community-merged PRs also went up, which the speaker counts as a good sign. ([1:38](https://youtu.be/I2LL_wd89-A?t=98))
- **Speed of the whole system matters, not just code output** — With 10 to 20 agents running at once, any slow CI or lint step compounds. Moving to TypeScript Go gave about 10x faster builds, which mattered for agent feedback loops. ([7:02](https://youtu.be/I2LL_wd89-A?t=422))
- **Agents need to use the real app to check UI work** — Agent-made UI often looks right in the description and is misaligned when opened. The team built an automated component browser that screenshots every component on each change and flags unexpected visual diffs, plus a Playwright-driven skill that launches VS Code and clicks a scenario. ([8:04](https://youtu.be/I2LL_wd89-A?t=484))
- **Encode expert knowledge as skills owned by the experts** — Accessibility best practices were moved from one person who had to be pulled into reviews into a shared skill that the accessibility area owner maintains. Living AGENTS.md files help agents navigate the codebase. ([4:40](https://youtu.be/I2LL_wd89-A?t=280))
- **Make the review and triage pipeline mostly automatic with human checkpoints** — AI code review is mandatory on every PR, with low, medium or high effort depending on risk, and humans wait until comments are resolved. Issues are filtered, translated and assigned by AI. Raw telemetry is reduced to full error stacks, grouped by fingerprint, and turned into about 10 owned issues, each with an auto-opened fix PR that a human approves. ([12:54](https://youtu.be/I2LL_wd89-A?t=774))
- **Staged rollouts replace all-at-once releases** — The team used to ship to 100% at once. Because agents raise the risk and rollbacks on installed apps are costly, they now roll out in stages and watch error spikes and issues during each stage. ([14:54](https://youtu.be/I2LL_wd89-A?t=894))
- **Eval harness results can vary by model in surprising ways** — A trivial eval (write a five-character hello-world file) used 70x more tokens on the most expensive model, and that model was not the high-reasoning one. The speaker says harness and model interaction needs to be measured directly. ([15:58](https://youtu.be/I2LL_wd89-A?t=958))

## Techniques
- **Code survival metric** — Measure the share of agent-written code that gets committed, not raw generation volume. Use it to judge harness and model changes over time. *When:* When you want to know whether agent output is trusted and useful, and to compare model or harness versions.
- **Agent-readable repo docs** — Keep a lightweight AGENTS.md as a map of the codebase (where to look, what matters). Generate a first draft with an agent command, then update it as the agent makes mistakes. *When:* Before letting agents work in a repo, and whenever agents repeatedly misread the structure.
- **Expert knowledge as a shared skill with an area owner** — Turn the knowledge from one expert into a skill used by everyone. Have the expert own and review it, so non-experts get the expertise directly. *When:* When a few experts are repeatedly pulled into reviews for the same domain issue (accessibility in the talk's example).
- **Screenshot-diff component browser** — Run an automated build on each change that screenshots every UI component and reports differences, so ripple effects are caught. Attach the diff to PRs. *When:* For UI-heavy codebases where agents claim visual correctness that is not true when rendered.
- **Self-correcting launch loop** — Give the agent a skill that launches the app (here via Playwright in an Electron web app), runs a named scenario, collects logs, and re-checks after a fix. *When:* When the agent needs to diagnose and verify UI or app behavior without a human clicking through it.
- **Tiered AI code review** — Set review effort (low, medium, high) by the risk level of each repo or area, and block human review until automated comments are resolved. *When:* When PR volume from agents exceeds what humans can review, and you want to control review cost against risk.
- **Deterministic filtering before agent action** — Filter raw telemetry to error stacks with full traces, fingerprint and group them, then file issues and open fix PRs only for the grouped results. *When:* When exception volume is too high for humans or a fixed rule set to handle directly.
- **Staged rollouts with error monitoring** — Release to a growing share of users and watch error and issue signals at each stage before going wider. *When:* When agent-written changes raise regression risk and rollback is expensive.
- **Evals bootstrapped from issues** — Use a template so each new user-reported scenario in a GitHub issue is turned into an eval scenario by an agent. Track offline hill-climbing first, then run online experiments. *When:* When your product is an agent and real user scenarios need to become regression tests quickly.
- **Prototypes instead of PRs for design talks** — Build a quick prototype to hold a design conversation, and iterate on it daily, instead of landing exploratory code in the product repo. *When:* When the team needs fast feedback on how a feature should look or behave.

## Numbers
- Team size is very small, shipping to over 50 million users ([0:12](https://youtu.be/I2LL_wd89-A?t=12))
- Code survival rate: 55% with GPT-4.1 at the start, 86% with Claude Opus 4.6 today ([0:12](https://youtu.be/I2LL_wd89-A?t=12))
- Release cadence moved from monthly (since VS Code 1.0, about 10 years) to weekly ([1:38](https://youtu.be/I2LL_wd89-A?t=98))
- TypeScript Go gave about 10x faster builds ([7:02](https://youtu.be/I2LL_wd89-A?t=422))
- Raw telemetry about 51 billion events per day, filtered down to about 10 issues filed and assigned per cycle ([12:54](https://youtu.be/I2LL_wd89-A?t=774))
- Hello-world file eval: most expensive model used 70x more tokens than the baseline ([15:58](https://youtu.be/I2LL_wd89-A?t=958))

## Hot takes
- Token maxing or using AI all day is not the goal; the value comes from changing the whole shipping system around AI.
- Human approval should stay in the loop even when agents fix bugs, but humans should review after automated checks, not do the first pass.
- Measuring code survival matters more than measuring generation volume.

## Tools mentioned
VS Code, GitHub, GitHub Issues, GitHub Copilot code review, TypeScript Go, Playwright, Electron, Xcode MCP, AGENTS.md, Chrome extension

## Relevance to our work
- **prosharness** (2/3): A launch/scenario skill that drives the app, collects logs and re-verifies after fixes is a verification loop ProsHarness could run before marking a task done. Tiered review effort also fits harness-level review control. → *Add a verify step to ProsHarness plan execution that runs a named scenario and attaches logs before a task is marked complete, and try low/medium/high review effort tiers.*
- **general** (2/3): Living AGENTS.md maps and skills that encode expert knowledge with a named owner match the context-engineering interest. The code-survival metric is a simple quality signal for any coding agent. → *Track code survival (percent of agent-written lines kept) for one repo and compare harness or model changes against it.*
- **agentos** (1/3): Telemetry-to-fix pipeline (raw signals filtered into grouped, owned issues with auto-opened fix PRs) is a concrete example of the mining step SkillForge needs, but it is about exceptions, not skill-worthiness. → *Read the error-stack triage design and compare its fingerprint/grouping step with SkillForge telemetry mining before choosing a success signal.*
