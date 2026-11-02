# Anthropic Released A New Way To "Vibe Code"

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `XWp4k9K6oK8` · [watch](https://youtu.be/XWp4k9K6oK8) · **date:** 2026-01-02 · **length:** 4:41 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** AI LABS presenter (unnamed) · **orgs:** Anthropic, automata.dev
- **topics:** coding-agents, context-engineering, agent-architecture, testing-verification · **tags:** long-running agents, initializer agent, feature list json, progress tracking, git commits per feature, puppeteer browser testing, compaction, claude.md, bmad comparison, nextjs demo

> Anthropic's long-running-agent harness: an initializer agent sets up a JSON feature list, progress file and git repo, then a coding agent implements one feature per session with browser testing and commits, so work survives compaction.

## Summary
The video describes a workflow Anthropic released for long-running Claude Code tasks. The author says agents lose progress when a single big feature triggers repeated context compaction, and that Claude marks untested features as done. The fix is two roles: an initializer step that creates CLAUDE.md, a feature_list JSON with every feature set to failing, an init script, a progress file and an initial git commit, followed by a coding loop that implements one feature at a time, tests it with Puppeteer, flips its flag to true, updates progress, and commits. The presenter builds an online Python compiler in an empty Next.js project as the demo, reports that the run used 84% of context where BMAD would have compacted twice, and suggests the approach works better than BMAD in some ways, though it is still an idea rather than a full system. The video closes with a sponsored pitch for a consultancy (automata.dev) that applies these workflows to client projects. The substance is a short, practical pattern; the claims about Anthropic's release and the 84% figure are one creator's single demo.

## Key ideas
- **Long single-shot tasks fail because context compaction loses progress: after repeated compaction the feature is half-built with no memory of its state.** — Presenter's diagnosis of the limited context window; the proposed fix is to break work into small, tracked increments rather than one-shotting features. ([0:00](https://youtu.be/XWp4k9K6oK8?t=0))
- **Claude marks untested features as complete, so testing has to be forced by the structure of the workflow.** — All features start marked failing in a JSON list; the agent flips them to true only after a browser test passes. ([0:00](https://youtu.be/XWp4k9K6oK8?t=0))
- **Split the work into an initializer step and an incremental coding step, modelled on how real engineering teams work.** — Initializer sets up CLAUDE.md, the feature list, init script, progress file and git; the coding loop then runs once per feature. ([0:53](https://youtu.be/XWp4k9K6oK8?t=53))
- **Use JSON rather than Markdown for the feature list because JSON is easier to manage in context and harder to casually rewrite.** — Presenter's stated reason; the agent is told not to alter the feature list beyond marking features implemented. ([0:53](https://youtu.be/XWp4k9K6oK8?t=53))
- **Commit in a mergeable state after every tested feature so git logs serve as the recovery mechanism.** — Descriptive commit messages let a fresh session resume from git history and the progress file rather than from the code itself. ([1:40](https://youtu.be/XWp4k9K6oK8?t=100))
- **Resuming is a one-line prompt: implement the next feature marked not done.** — Because state lives in the JSON, progress file and git log, a terminated session can continue exactly where it stopped. ([2:18](https://youtu.be/XWp4k9K6oK8?t=138))
- **Presenter reports this beats BMAD on context use, but says the approach is still a DIY idea rather than a complete system.** — Compared with BMAD, which he says compacted twice on large stories; he suggests BMAD could borrow the git discipline. ([3:25](https://youtu.be/XWp4k9K6oK8?t=205))

## Techniques
- **Initializer + incremental coder harness** — Step 1: run /init to create CLAUDE.md at the repo root with the project overview. Ask Claude to generate a feature list JSON in the project root listing every feature with its test steps, all initially marked failing. Create an init script that starts the dev server and a progress tracking file (progress.md). Make an initial git commit. Step 2: for each feature, have Claude implement it, test it end-to-end in a browser, set its JSON field from false to true, update progress.md, and commit with a descriptive message after verifying the commit. Repeat until all features are true. Tell Claude not to modify the feature list beyond flipping those flags. *When:* Long-running, multi-feature builds where a single session would compact repeatedly and lose track of partial work.
- **Forced browser verification via Puppeteer** — Connect Puppeteer (MCP or similar) so the agent can launch the browser and test each feature's listed steps before marking it done, because the agent can only read code, not see the rendered interface. *When:* Front-end or full-stack apps where bugs are not visible from code alone.
- **Resume from state, not from context** — Keep the feature JSON, progress.md and the git log as the source of truth. A new session reads these to find the next unfinished feature, so no conversation memory is needed. *When:* Sessions that may terminate or hit compaction mid-project.

## Numbers
- Presenter's demo used 84% of context after implementing many features; he says BMAD would have hit compaction twice on the same work. ([3:25](https://youtu.be/XWp4k9K6oK8?t=205))
- Tracking file is updated after each feature; the demo builds an online Python compiler in an empty Next.js project. ([0:53](https://youtu.be/XWp4k9K6oK8?t=53))

## Hot takes
- Presenter claims Anthropic released this as a solution; the transcript describes the workflow but the attribution to Anthropic is the presenter's own framing from a single video.
- Presenter says Claude's workflow is better than BMAD in some ways, based on one demo project and a single 84% context figure.
- The final third is a sponsored pitch for automata.dev consulting, so the piece is a short tutorial with a sales segment at the end.

## Tools mentioned
Claude Code, Claude.md, Puppeteer, Git, Next.js, BMAD

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code for checkpoint/resume of long runs, and this video is a concrete prompt-and-file protocol for the same problem; the JSON feature list with failing-by-default flags is a reusable verification gate. → *Try the initializer plus per-feature JSON flag loop as a ProsHarness run mode and check whether flipping flags after Puppeteer-style verification reduces false completions.*
- **agentos** (1/3): Checkpoint and resume of long agent runs via external state (feature list, progress file, git) is a lightweight form of durable execution that AgentOS's harness-style concerns overlap with. → *Compare this progress-file plus git-log resume pattern with ProsHarness checkpoint/resume before adding any new state store.*
