# What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `7P0elyLIxXo` · [watch](https://youtu.be/7P0elyLIxXo) · **date:** 2026-07-18 · **length:** 7:14 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Dotta · **orgs:** Paperclip
- **topics:** testing-verification, agent-architecture, multi-agent · **tags:** definition-of-done, liveness-vs-verification, control-plane, task-blockers, human-approval, audit-trail, watchdog-agent, verifier-separation, evidence-based-completion, chain-of-custody

> Dotta (Paperclip) argues "done" is a bundle of claims, not a checkbox, and shows how a control plane with blockers, reviewers, and watchdogs keeps agent work moving while still verifying it.

## Summary
The speaker argues that when an agent says a task is done, it is making several separate claims: an artifact exists, evidence supports it, a rubric was met, a reviewer checked it, an authorized person approved it, and some risk may remain. Agents can produce work faster than humans can verify it, so exhaustive human sign-off turns into what he calls verification theater. He frames the core tension as liveness (work keeps moving without blockers) versus verification (work is checked before it is trusted), and says a naive loop over a task manager breaks down once you add dependencies, blockers, multiple agents, and locked checkouts. His proposed answer is a control plane in Paperclip with explicit task state transitions, first-class blockers enforced by the system, named reviewers and approvers per task with an audit trail, and watchdog agents that keep working toward a goal until it is met, independent of which harness runs them. He closes with a checklist: define done per task in detail, separate the verifier from the author (often a different model), require evidence rather than self-report, give agents tools to verify (browser, screenshots, clicking through the UI), and make the chain of custody explicit so each agent knows who receives the work next. The talk is short and conceptual, with little measured data, and is partly a product pitch for Paperclip.

## Key ideas
- **Done is a bundle of claims, not a boolean** — Saying a task is done implies an artifact was produced, evidence exists, a rubric was met, a reviewer checked it, an authorized person approved it, residual risk is known, and there is a named next action and owner. Agents should be able to tell these apart. ([0:00](https://youtu.be/7P0elyLIxXo?t=0))
- **Exhaustive human verification fails at high volume** — Agents can create more work than humans can check. If every task needs human sign-off, the process degrades into verification theater. The fix is a protocol for how tasks move through states, not more reviewers. ([1:26](https://youtu.be/7P0elyLIxXo?t=86))
- **Liveness and verification pull against each other** — Unchecked agents produce low-quality output (he calls it AI slop, worse than nothing over time). Pure review creates a queue no human can clear. He says the job is to separate the claims that make up 'done' so each can be handled at its own pace. ([2:48](https://youtu.be/7P0elyLIxXo?t=168))
- **Three invariants for an agent control plane** — Productive work should continue, only real blockers should stop work, and infinite loops must be bounded. A plain for-loop over a task manager fails once you add dependency trees, blockers, multiple agents, and checkout locks. ([2:48](https://youtu.be/7P0elyLIxXo?t=168))
- **Paperclip enforces done through control-plane mechanisms** — Tasks have explicit state transitions. Blockers between tasks are enforced by the system. Humans approve at chosen points, and those choices leave an audit trail. Reviewers and approvers can be set per task so another agent reviews on completion. A watchdog is a separate agent given a goal that keeps the other agents working until it is met. The watchdog works with any harness (he names Pi, OpenClaw, Hermes, Claude Code, Codex). ([4:13](https://youtu.be/7P0elyLIxXo?t=253))
- **Ask for evidence, and give agents the tools to produce it** — Do not ask an agent whether it is done. Give it a browser harness, screenshot capture, and hooks to click through the UI so it can verify the work itself. Separate the verifier from the author, often by using a different model (e.g. Claude writes, Codex verifies). ([5:39](https://youtu.be/7P0elyLIxXo?t=339))
- **Define done per task and set a clear chain of custody** — Before starting, write down what done means for this task in as much detail as possible. Every agent should know who receives the work next when it finishes, so handoffs stay explicit. ([5:39](https://youtu.be/7P0elyLIxXo?t=339))

## Techniques
- **Done as a structured object** — Record the artifact, scope, rubric or standard, evidence, verifier identity, approver with authority, residual risk, and next action as separate fields rather than one done flag. *When:* Any multi-step agent workflow where merge, deploy, or customer announcement depend on different levels of confidence.
- **Cross-model verifier** — Have a different model (or harness) review the author's output against the rubric, e.g. Codex verifying Claude's code. *When:* Coding agents where the author's self-assessment is not trustworthy enough to merge or ship.
- **Evidence-first completion** — Require artifacts such as test runs, screenshots, or click-through results, and give the agent the browser or tool hooks to create them, instead of asking it if the work is done. *When:* UI or end-to-end work where a passing unit test does not show the feature works.
- **Watchdog agent for goal persistence** — A supervising agent holds a goal and keeps the worker agents running until the goal is met, using one interface regardless of the underlying harness. *When:* Long-running multi-agent work that tends to stall, or where you need a hard bound on loops.
- **Explicit state transitions with enforced blockers** — Define the allowed next states for each task and let the control plane, not the agent, enforce dependency blockers and handoff rules. *When:* Task graphs with dependencies, several agents, or locked checkouts, where a simple loop over a task list breaks.
- **Per-task reviewer and approver assignment with audit trail** — Set reviewers and approvers on each task explicitly so that a named party signs off, and log each human choice. *When:* Work where someone must stand behind the decision, such as production or customer-facing output.

## Numbers
- Illustrative only, no data given: a human may verify only a few tasks per day, which is why per-task human sign-off does not scale. ([1:26](https://youtu.be/7P0elyLIxXo?t=86))
- Speaker's rhetorical claim, not measured: following the checklist could get 100 times more work done. No evidence presented. ([5:39](https://youtu.be/7P0elyLIxXo?t=339))

## Hot takes
- A single done/green check mark flattens several different claims and is the root failure in most agent systems.
- Exhaustive human sign-off on every agent task becomes verification theater once volume grows.
- Agents should not verify their own work. The verifier should be a separate party, often a different model.
- Unbounded agent loops produce AI slop, which is worse than doing nothing over time.

## Tools mentioned
Paperclip, Pi, OpenClaw, Hermes, Claude Code, Codex

## Relevance to our work
- **agentos** (2/3): The talk's done-as-object framing addresses the open question of what counts as a success signal for skill mining. The SkillForge telemetry and governance layers could use the same structured record. → *Prototype a done record (artifact, evidence, verifier, approver, residual risk) per agent run in the telemetry schema, and test whether it works as the success signal for SkillForge skill-worthiness scoring.*
- **prosharness** (2/3): ProsHarness already splits plan, critique (Codex), and debate, and runs loops and schedules. The talk's ideas on bounded loops, watchdogs, and explicit done criteria map onto those parts. → *Add a per-task done record to ProsHarness checkpoints (rubric, evidence, verifier model, approver, next owner) and put a hard iteration bound plus a goal-watchdog on the loop scheduler.*
- **general** (1/3): Relevant to coding-agent workflows and verifier-separation. The talk is conceptual with no benchmarks. → *Try a verifier subagent on a different model for one coding task in the current repo, with a written done-rubric in CLAUDE.md, and compare it with the self-check.*
