# I thought I was a Senior React Dev... until I ran React Doctor.

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `k3vyIIEZfU4` · [watch](https://youtu.be/k3vyIIEZfU4) · **date:** 2026-03-02 · **length:** 4:33 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack, Aidan Bai (React Doctor author)
- **topics:** dev-tools, coding-agents · **tags:** react, linting, oxlint, static-analysis, anti-patterns, cli, monorepo, accessibility, open-source, agent-skill

> A short walkthrough of React Doctor, a Rust-fast (OXLint-based) CLI that flags React anti-patterns, shown on an old personal project and an open-source CRM monorepo.

## Summary
Better Stack presents React Doctor, a CLI that scans React code for anti-patterns such as unnecessary useEffect, accessibility issues, prop drilling and hard-coded secrets. It runs on OXLint and builds an AST of the project to match hook usage, prop structures and component boundaries, and the speaker says it encodes 47+ React best-practice checks. Andrus runs it on a stock-chart app he wrote six years earlier and gets a near-perfect score, with three valid findings: index used as a key, Recharts loaded eagerly (suggests lazy loading), and four useState calls in one useEffect (suggests useReducer). He then runs it on the open-source Twenty CRM, where the tool detects the monorepo and reports per-package scores. The marketing site has one missing-alt error and the front package has 99 errors, which he still calls in the "green zone". The video ends by suggesting the tool for sanity-checking projects and finding places to contribute to open-source repos. It can also be run as a coding-agent skill or through a Node.js API, though the video does not demonstrate either.

## Key ideas
- **React Doctor is a CLI for detecting React anti-patterns, built on OXLint and an AST of the project.** — It looks for hook usage, prop structures and component boundaries, and the speaker says it is written against 47+ React best practices. The lint core is Rust-based, which the speaker credits for speed. ([0:00](https://youtu.be/k3vyIIEZfU4?t=0))
- **The checks go beyond style into accessibility and security.** — Examples shown include hard-coded security keys and a loading-state pattern, with guidance on when to use it versus useTransition. ([1:01](https://youtu.be/k3vyIIEZfU4?t=61))
- **It can be used as a skill for a coding agent or programmatically through a Node.js API.** — The speaker mentions both integration paths but does not demonstrate either in the video. ([1:01](https://youtu.be/k3vyIIEZfU4?t=61))
- **On an old personal project, the findings were concrete and valid.** — The tool flagged index used as a list key, Recharts as a heavy dependency that should be lazy-loaded, and four useState calls in a single useEffect that should become useReducer. ([2:04](https://youtu.be/k3vyIIEZfU4?t=124))
- **It handles monorepos by scoring each package separately.** — On the Twenty CRM repo it detected the workspace packages and produced a separate score for each, with the front package showing many more issues than the marketing site. ([2:04](https://youtu.be/k3vyIIEZfU4?t=124))
- **The speaker's suggested use is contribution discovery as well as sanity checking.** — Because the project is open source and young, he suggests running it on other repos to find places to contribute new checks or fixes. ([3:18](https://youtu.be/k3vyIIEZfU4?t=198))

## Techniques
- **Run a React anti-pattern scan on a repo** — Run the React Doctor CLI from the project root. The video does not show the exact command or flags, so check the project README. It returns a score plus a list of findings. In a monorepo it detects workspace packages and reports a score per package. *When:* Before merging or shipping a React codebase, as a quick sanity check, or to triage an unfamiliar repo.
- **Fix the three demonstrated findings** — 1) Replace array-index keys with stable IDs. 2) Lazy-load heavy chart libraries such as Recharts (for example with React.lazy and Suspense). 3) Collapse several related useState calls inside one useEffect into a single useReducer. *When:* When a scan flags these patterns. Each fix is a common React refactor, not specific to this tool.
- **Use the scanner as a coding-agent skill** — The speaker says React Doctor can be packaged as a skill so a coding agent can run it. He does not show setup steps. *When:* When an agent is writing React code and you want its output checked against the same rules before a human reviews it.

## Numbers
- The tool checks against more than 47 React best practices. ([1:01](https://youtu.be/k3vyIIEZfU4?t=61))
- The speaker says OXLint can scan tens of thousands of lines of code in milliseconds. This is an unmeasured claim. ([0:00](https://youtu.be/k3vyIIEZfU4?t=0))
- A personal six-year-old stock-chart project scored nearly perfect with three findings. ([2:04](https://youtu.be/k3vyIIEZfU4?t=124))
- The marketing-site package of Twenty CRM had 1 error, a missing alt tag. ([3:18](https://youtu.be/k3vyIIEZfU4?t=198))
- The front package of Twenty CRM had 99 errors and was still in the green zone. ([3:18](https://youtu.be/k3vyIIEZfU4?t=198))

## Hot takes
- The title and the framing ("I thought I was a Senior React Dev") are clickbait. The video is a 4.5-minute tour of one tool with no comparison to existing React linting options such as eslint-plugin-react.
- The speed claim (tens of thousands of lines in milliseconds) is asserted, not benchmarked on screen.
- The score scale and the 'green zone' threshold are never explained, so the reader cannot tell how to interpret 99 errors.
- The video shows a demo of findings, not a reproducible setup. The exact install and run commands and the skill and Node API integrations are left out.
- The tool is described as open source and young, so rule quality and false-positive rate are unknown from this video alone.

## Tools mentioned
React Doctor (CLI, Aidan Bai), OXLint (Rust-based JavaScript linter), React, Recharts, Node.js (programmatic API), Million.js (creator's earlier project, mentioned), React Grab (creator's project, mentioned), React Scan (creator's project, mentioned), Amy (named as a creator project, caption may be imprecise), Twenty (open-source Salesforce-alternative CRM, captioned as "20"), useTransition (React hook referenced)

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps Claude Code, and a fast deterministic scanner could be one of the quality checks run on agent-written React code. The video shows it can be used as an agent skill, but it demonstrates nothing about agent workflows. → *If a ProsHarness run touches React code, consider a skill that runs a deterministic React scanner as a gate after the agent's edits and before its plan-critique step.*
