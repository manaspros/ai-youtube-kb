# How to Build Quality Gates into Agentic Coding Workflows — Nnenna Ndukwe, Qodo AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `-AKPRSYccJc` · [watch](https://youtu.be/-AKPRSYccJc) · **date:** 2026-10-12 · **length:** 57:45 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Nnenna Ndukwe · **orgs:** Qodo
- **topics:** pr-code-review, context-engineering, coding-agents, testing-verification · **tags:** quality-gates, planning-templates, pr-review, autofix, rules-and-skills, severity-levels, tdd, semgrep, conventional-commits, claude-code, codex, workshop

> Hands-on workshop by a Qodo DevRel on wiring codified rules, skills, structured plans and deterministic gates into an agentic coding loop from planning through PR review and autofix.

## Summary
The speaker argues that AI coding needs a verification layer: define code quality, write it down where agents can read it, and apply the same standards at planning, code generation and review. She walks through a fork-able payments API workshop repo with AGENTS.md, rules, skills, a hidden plan directory, Semgrep and CI. Agents read the rules, pick the relevant ones, and run a plan-mode step that names the first implementation skill and a TDD handoff. A structured plan template (scope, skill routing, behavior scenarios, verification gates, failure rules, commit plan) and an execution template (starting state, handoff, definition of done) keep the work auditable. Local deterministic checks (Ruff, Pyright, Bandit, pytest, Semgrep, conventional commits) run before the PR. A Qodo PR review then pulls in the org's rules and skills, flags one reliability bug and three rule violations, and a PR-resolver skill autofixes the findings, reruns verification, commits and posts a summary back to the PR. Rules carry severity levels, and the speaker says merge-blocking determinism is what regulated customers want, though the platform does not yet guarantee that an agent will check every relevant rule. The talk is part product demo, but the planning templates and the remediation loop are concrete.

## Key ideas
- **Define code quality explicitly and codify it where agents can read it** — Quality standards should be written down (locally in the repo or in a shared context layer) and pulled into every interface: CLI, IDE and CI. The goal is that the same standards are checked at planning, codegen and review. ([3:40](https://youtu.be/-AKPRSYccJc?t=220))
- **Verify early and often with the same standards in every phase** — Operationalising context means using one set of rules and skills for planning, code generation and code review, so the agent is checked against the same bar at each step rather than only at the end. ([5:00](https://youtu.be/-AKPRSYccJc?t=300))
- **Detailed planning templates make agents follow the process and self-correct** — The speaker's experience is that the more detailed and structured the plan document the agent must re-read, the better it adheres to the process and catches missing points on its own. ([11:36](https://youtu.be/-AKPRSYccJc?t=696))
- **Pair deterministic tools with AI checks** — Linters, type checking, Bandit, pytest and Semgrep run as a local verification command. The speaker says the combination of deterministic and AI checks is the point, not either alone. ([12:50](https://youtu.be/-AKPRSYccJc?t=770))
- **Run a local code review before the PR, then automated review in CI** — Small issues are cheaper to fix before another developer sees the code. Automated review in CI or the Git provider then acts as the second gate. ([28:54](https://youtu.be/-AKPRSYccJc?t=1734))
- **Rules have severity levels, and only some should block a merge** — Rules are grouped by category (accessibility, correctness, maintainability, architecture, security) and by severity. Action-required rules can block a merge, while others are good practice and advisory. Rules can be scoped by org or repo. ([33:56](https://youtu.be/-AKPRSYccJc?t=2036))
- **Rules can be inferred from code, but inferred ones need human review** — Explicit rule files are ingested directly. Conventions the platform infers from the codebase show up as suggestions with good and bad examples, and a human must accept them before they are activated. ([36:19](https://youtu.be/-AKPRSYccJc?t=2179))
- **Determinism of rule enforcement is an open gap** — A merge-block can be configured for high-severity findings, but the speaker admits the agent may not invoke a relevant rule at all. Regulated enterprise customers want deterministic enforcement, and she says this is being raised with the product team. ([45:23](https://youtu.be/-AKPRSYccJc?t=2723))
- **Close the review loop with a remediation skill** — A PR-resolver skill pulls the critical and high findings, then either autofixes all of them or reviews each one. It reruns verification, commits and posts a summary back to the PR, so the resolved issues are crossed out. ([49:08](https://youtu.be/-AKPRSYccJc?t=2948))

## Techniques
- **Codified rules and skills pulled per phase** — Keep engineering standards as rules (with good and bad examples, category and severity) and skills in a shared or repo-local context layer. Install or sync them into the coding agent and the review tool so the same standards apply at planning, codegen and review. *When:* Several repos or a team where standards should be consistent across agents and interfaces.
- **Structured high-level plan plus execution plan** — High-level plan: problem, constraints, applicable rules, skill routing, scope, behavior scenarios, verification gates, failure and recovery rules, commit plan. Execution plan: starting state (branch, local verification commands), skill handoff, step list, test plan, definition of done with deferred items noted. *When:* Multi-step agent changes, especially payment or other sensitive mutations, and when you want the agent to run loops unattended.
- **Read-only plan mode with an explicit skill handoff** — Run the planning step in plan mode, forbid writing code or plan files, and require the plan to name the first implementation skill and the TDD prompt it chains to. *When:* Before any implementation, so the agent's constraints and test strategy are settled first.
- **Local verification command as the gate** — One verification command runs the linter, type checker, security scanners (Bandit, Semgrep), tests and commit-format checks. The agent runs it after the change and again after review fixes. *When:* Any change an agent will open as a PR.
- **Audit skills during implementation** — Use audit-style skills (boundaries, drift, naming, abstractions, dead code, error handling) to tighten code while it is being written, rather than only in review. *When:* Agent-written code that tends to drift or leave dead code.
- **Review-findings autofix loop** — Pull the PR review findings, filter by severity, either autofix all or walk through them one by one, rerun verification, commit with conventional-commit format and post a fix summary to the PR. *When:* After an automated PR review flags issues on agent-authored code.
- **Severity-tiered rules with merge blocking** — Mark rules as action-required (block merge) versus advisory. The speaker notes that the blocking is deterministic at the platform level, but whether the agent checks each rule is not guaranteed. *When:* Teams that need some standards enforced hard and others only suggested.

## Numbers
- Over 1,900 lines of changes in a deliberately large PR on an open-source project, Qodo's automated review found only one bug (a reliability bug). ([31:20](https://youtu.be/-AKPRSYccJc?t=1880))
- Demo PR review result: 5 skills invoked, one bug, three rule violations and two skill insights. ([47:18](https://youtu.be/-AKPRSYccJc?t=2838))
- Autofix-all run resolved six code issues from critical to high severity. ([50:09](https://youtu.be/-AKPRSYccJc?t=3009))
- Session length is 57:45. ([0:00](https://youtu.be/-AKPRSYccJc?t=0))

## Hot takes
- Verification has to be built into agentic engineering from the start, not added after the code is written.
- Deterministic tools and AI review should be combined rather than used as alternatives.
- Enterprises in regulated industries need deterministic merge blocking, and the agent cannot be trusted to remember to check the rules.

## Tools mentioned
Qodo, Claude Code, Codex, Semgrep, Ruff, Pyright, Bandit, pytest, GitHub CLI, uv, conventional commits, git worktrees, TESSL (skill evals, mentioned), PacMind (open-source rules layer, mentioned)

## Relevance to our work
- **prosharness** (2/3): The harness runs long Claude Code runs with checkpoints. The talk's plan template (scope, skill routing, verification gates, failure rules, definition of done) and its local verification gate map onto checkpoint and resume design, and its remediation loop is a model for a plan-then-verify step. → *Add a per-run plan template and a single verification command that the harness executes at each checkpoint before it marks the step done, then test whether a failed gate rolls back to the last checkpoint.*
