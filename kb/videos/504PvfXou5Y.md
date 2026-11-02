# BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `504PvfXou5Y` · [watch](https://youtu.be/504PvfXou5Y) · **date:** 2026-06-18 · **length:** 12:49 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Michal Cichra · **orgs:** Safe Intelligence, Microsoft, Red Hat
- **topics:** context-engineering, testing-verification, pr-code-review · **tags:** ADR, PRD, BDD, Cucumber, executable specs, design system, git hooks, architecture linting, context compaction, agent harness, spec-driven development

> Michal Cichra on keeping agents and humans aligned by storing ADRs, PRDs and executable BDD specs in the repo, then enforcing them through git hooks, CI and import-boundary lints.

## Summary
The speaker argues that teams lose the reasons behind decisions, both when people leave and when an agent's context compacts, so the why must live in the repo. He covers three lightweight document types: ADRs that record a decision and how to enforce it, PRDs that capture the problem and the user journey, and BDD scenarios written in Cucumber that are both readable and executable. Design systems are treated the same way, as written rules plus component previews that agents can see. The enforcement loop is git hooks that run the same checks as CI (linting, formatting, type checks, duplication, architecture and document checks), so an agent that skips them gets rejected with a link back to the relevant doc. Architecture rules are enforced by restricting module imports, for example keeping the end-to-end suite away from the database and keeping templates from querying it, which removes whole bug classes such as N+1 queries. The loop is scoped per task type, with test selection based on changed files and coverage, and he reports that sessions with 20 to 50 context compactions still work because the important rules get re-read. The talk is conceptual and lightly promotional for his company's product, with few hard numbers.

## Key ideas
- **Decisions get lost in both humans and LLMs, so the why must be written down in the repo.** — Teams lose the founding engineers and their reasons over time. Agents lose context when it compacts. Recording reasons in docs lets both recover them. ([1:11](https://youtu.be/504PvfXou5Y?t=71))
- **An ADR should also say how the rule is enforced and which files it covers.** — The speaker's team has around 50 ADRs. The format is free text. A tool is still needed to enforce each rule, and its error message should cite the ADR and the fix so the agent can look it up. ([2:13](https://youtu.be/504PvfXou5Y?t=133))
- **A PRD can be very light: the problem, the goal, and the user journey.** — It is written for future readers, including the author six weeks later, and for agents. It does not need to be exhaustive. ([2:13](https://youtu.be/504PvfXou5Y?t=133))
- **Executable BDD specs close the gap that spec-driven development leaves open.** — Markdown specs say how a feature should work but not whether it does. Cucumber scenarios in plain language are easier to review than agent-written tests, and they link back to PRDs and critical user journeys. ([3:45](https://youtu.be/504PvfXou5Y?t=225))
- **Design systems can be enforced like code: written rules, component previews and snapshots that agents can see.** — An example rule is that only one primary button may appear on a page. Components are built from small pieces into larger ones and reviewed visually. ([5:44](https://youtu.be/504PvfXou5Y?t=344))
- **Git hooks and CI should run the same checks, so an agent cannot skip them.** — The checks cover linting, formatting, type checks, duplication, architecture and document lint. A rejected push comes with a link to the document that explains the fix. ([7:13](https://youtu.be/504PvfXou5Y?t=433))
- **Prevent whole classes of bugs with module-import boundaries instead of finding them one by one.** — The end-to-end suite cannot import database modules, so it is forced to test through the browser. Templates cannot query the database, which rules out N+1 queries. Data access returns plain shapes, not ORM objects. ([8:14](https://youtu.be/504PvfXou5Y?t=494))
- **Scope the loop to the task, and accept many context compactions.** — ADR, PRD and UI work each get their own focus. The UI loop skips some checks and iterates in the browser. Test selection is based on changed files and coverage. Goal runs log the model's decisions for later review. Sessions go through 20 to 50 compactions and still work because the important rules are looked up again. ([9:49](https://youtu.be/504PvfXou5Y?t=589))

## Techniques
- **ADR with enforcing lint rule** — Write each architecture decision as a short doc that gives the rationale, the enforced rule, the files in scope, and how to fix a violation. A linter or import check fails with a message that points to the ADR. *When:* Architecture rules that agents keep breaking, such as layer boundaries or banned data-access patterns.
- **Import-boundary restriction to eliminate bug classes** — Use lint rules to restrict which modules may import which. Examples: the E2E suite cannot import DB modules; templates cannot import the DB layer; repositories return plain data shapes. *When:* Recurring problems such as N+1 queries or tests that bypass the UI. Prevent the class of problem, not each instance.
- **Executable BDD scenarios linked to PRDs** — Write Cucumber feature files in plain language that describe user journeys. Step definitions execute them. Humans review the scenarios, not the step code. *When:* Spec-driven development where you must verify that the built product matches the written behavior.
- **Shared checks in git hooks and CI** — Define one set of checks and run it as the pre-push or pre-commit hook and again in CI. A rejection returns the failing rule and the doc to read. *When:* Agents that open pull requests and might skip local checks.
- **Design system as enforced rules and previews** — Document components and their states, add rules such as one primary button per page, render previews, and make them visible to agents and reviewers. Build larger components from smaller ones. *When:* Keeping UI consistent when agents generate frontend code.
- **Scoped test selection per task** — Pick the tests to run from changed files and code coverage instead of running the full suite. Use a fast browser-iteration loop for UI work. *When:* Large test suites where full runs are too slow for each agent iteration.

## Numbers
- About 50 ADRs describe the architecture of one product. ([2:13](https://youtu.be/504PvfXou5Y?t=133))
- Sessions run through 20 to 50 context compactions and still work, according to the speaker's experience over the last half year. ([11:15](https://youtu.be/504PvfXou5Y?t=675))
- Starting research can use up half of the context window. ([9:49](https://youtu.be/504PvfXou5Y?t=589))
- The speaker has about 10 years on a single product (at Microsoft and Red Hat), with no specific figures given for the enforcement results. ([0:00](https://youtu.be/504PvfXou5Y?t=0))

## Hot takes
- Code review should not be about style anymore, because style is enforced automatically, not debated.
- Prevent problem classes with rules instead of hunting for each instance, for example N+1 queries.
- Context compaction is acceptable if the important decisions are re-read; it is not a reason to avoid long agent sessions.
- Reading AI-written tests is harder than reading AI code, so use human-readable BDD scenarios as the review layer.

## Tools mentioned
Cucumber, git hooks, CI, linters, type checkers, architecture import lint, Markdown docs

## Relevance to our work
- **agentos** (2/3): AgentOS has several pillars (proxy, memory, serving, sandbox) with layer boundaries, and the talk's import-boundary rules would enforce them. The talk gives no benchmarks. → *Add an ADR folder with import-boundary lint rules for the L1/L2/L3 layers, and have each lint error cite the ADR that explains the fix.*
- **prosharness** (2/3): ProsHarness runs long Claude Code sessions with checkpoints. The talk's loop of logging decisions for review, plus rules that survive compaction, matches that design. → *Have ProsHarness save each agent decision to a reviewable log, and check whether rules in CLAUDE.md are still followed after several compactions.*
- **general** (2/3): The talk gives a concrete method for keeping decisions and rules in the repo so that agents and new people can recover the reasoning, which is relevant to context engineering. → *Write a short decision index in the repo and test whether a fresh session finds the right rule after a compaction.*
