# Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `NuePCNMpWGc` · [watch](https://youtu.be/NuePCNMpWGc) · **date:** 2026-06-18 · **length:** 15:12 · **format:** talk · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Prasenjit Sarkar · **orgs:** Sonar, Anthropic, OpenAI, Google
- **topics:** pr-code-review, evals, coding-agents, testing-verification · **tags:** code-quality, static-analysis, sonarqube, mcp, remediation-agent, security, maintainability, java, leaderboard, verbosity, acdc

> Sonar argues that LLM pass rates miss security, maintainability and verbosity. It shows its Java eval of 53+ models and pitches a verify-in-loop and remediation pipeline, so it is product-heavy.

## Summary
Prasenjit Sarkar of Sonar argues that model leaderboards report only functional correctness (pass rate on HumanEval, MBPP, SWE-bench), while security, maintainability, complexity and tech debt go unmeasured. Sonar ran more than 4,444 open-source Java assignments through 53+ models and published the results on a public leaderboard. The headline finding is that the highest pass-rate model (Gemini 3.1 Pro High, 84.17%) produced verbose code, and that output volume and complexity are rising across newer models. Among the causes he lists are mixed-quality and insecure training data, hidden logic bugs, probabilistic output and missing company context. He then presents the ACDC framework (Guide, Verify, Solve) with Sonar products at each stage, most of them in beta or private beta. Verify runs static analysis through MCP inside the coding agent in about 1 to 5 seconds, versus 1 to 5 minutes for CI. The remediation agent creates one PR per issue and discards fixes that introduce new issues. The talk is short and mostly a vendor pitch, but the eval numbers and the in-loop verify idea are concrete.

## Key ideas
- **Pass rate hides code quality** — Model leaderboards measure functional correctness only. Security, real-world reliability, architecture, maintainability and tech debt are not measured. ([2:30](https://youtu.be/NuePCNMpWGc?t=150))
- **Top pass-rate model is verbose and buggy** — On the 4,444 Java tasks, the top pass-rate model (Gemini 3.1 Pro High) wrote about 307k LOC and had high bug and security issue density. Other models wrote far more code for the same tasks. ([3:39](https://youtu.be/NuePCNMpWGc?t=219))
- **Root causes of bad generated code** — The speaker lists mixed-quality and insecure training data, subtle logic errors in training data, probabilistic output, limited company context and poor explainability as the causes. ([5:52](https://youtu.be/NuePCNMpWGc?t=352))
- **Newer models: fewer but subtler defects** — Code volume and complexity are growing with each model generation. Total vulnerabilities per model are falling, but the remaining issues are finer and harder for humans to spot. ([9:48](https://youtu.be/NuePCNMpWGc?t=588))
- **ACDC loop: Guide, Verify, Solve** — The framework has an inner loop and an outer loop. Guide acts on inputs (cleaning training data, pushing codebase context into the LLM). Verify runs analysis before commit and in CI. Solve remediates issues that get past verify. ([11:01](https://youtu.be/NuePCNMpWGc?t=661))
- **Analyze before commit, not only in CI** — With an MCP-connected coding agent, the generated code is analyzed in about 1 to 5 seconds, before commit. Findings go back to the agent to fix, which is much faster than the 1 to 5 minute CI run. ([12:04](https://youtu.be/NuePCNMpWGc?t=724))
- **Regression-gated bulk remediation** — The remediation agent creates one PR per selected issue. Each fix is re-analyzed and recompiled, and fixes that add new issues are discarded. ([13:14](https://youtu.be/NuePCNMpWGc?t=794))

## Techniques
- **Dual-metric model evaluation** — Score each model on pass rate and on static-analysis metrics of its output: LOC, cyclomatic and cognitive complexity, bugs and security issues per million LOC. Compare models on both. *When:* Choosing a model for a codebase where maintainability and security matter more than the test pass rate.
- **In-loop static analysis via MCP** — Expose the analyzer as an MCP tool to the coding agent. The agent analyzes its own generated diff before commit, and fixes findings in the same session. *When:* Coding agents where fast feedback (seconds) matters more than the slower CI gate. Use it as a pre-commit check.
- **Regression-gated autofix** — For each automated fix, re-run the analysis and the compile step. Discard the fix if it creates new issues. Only then open a PR. *When:* Bulk cleanup of existing tech debt by an agent, where you must not ship regressions.
- **One PR per issue for tech debt** — Turn each selected backlog issue into its own agent-generated PR, so humans review and merge each fix separately. *When:* Large tech-debt backlogs where you want small, reviewable, revertable changes.
- **Remediation on quality-gate failure** — When the PR quality gate fails, trigger a remediation agent to fix the flagged issues in the PR. *When:* Recovering from issues that slipped through the in-loop check.

## Numbers
- Pragmatic Engineer survey (March 2026): 55% of developers use AI agents regularly (speaker's citation) ([1:09](https://youtu.be/NuePCNMpWGc?t=69))
- Sonar eval: 4,444+ Java programming assignments, run through 53+ models, open-sourced data and public leaderboard ([2:30](https://youtu.be/NuePCNMpWGc?t=150))
- Gemini 3.1 Pro High: 84.17% pass rate (highest), about 307,000 LOC, 614 bugs and 210 security issues per MLOC (as stated by speaker) ([3:39](https://youtu.be/NuePCNMpWGc?t=219))
- Claude Sonnet 4.6: about 627,000 LOC generated, about 300 security issues per MLOC (highest risk, per speaker) ([4:44](https://youtu.be/NuePCNMpWGc?t=284))
- GPT-5.4 Pro High: about 1.2 million LOC for the same assignments; GPT-5.2 High about 1 million; GPT-4.0 under 250,000 ([4:44](https://youtu.be/NuePCNMpWGc?t=284))
- Analysis in agent loop takes about 1 to 5 seconds, versus 1 to 5 minutes for a CI run ([12:04](https://youtu.be/NuePCNMpWGc?t=724))
- Analysis covers 40+ programming languages and frameworks ([13:14](https://youtu.be/NuePCNMpWGc?t=794))

## Hot takes
- Pass rates on SWE-bench or HumanEval say little about whether agent-written code is secure or maintainable.
- Each newer model writes more code and more complexity, and the defects left over are subtler, so human review gets harder over time.
- Agents should run static analysis on their own diff before commit, not rely on CI alone.

## Tools mentioned
SonarQube, SonarQube Agentic Analysis (MCP), Sonar Sweep, Sonar Context Augmentation, Sonar remediation agent, Claude Code, Codex, Gemini CLI, Devin, Cursor, Windsurf, Antigravity, SWE-bench, HumanEval, MBPP

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs Claude Code in plan, critique and checkpoint loops. A static-analysis gate after each agent edit, before commit, fits the harness and matches its checkpoint-and-resume design. → *Add a static-analysis step (for example a linter or complexity check) to the ProsHarness checkpoint loop after each Claude Code run and before commit, then measure how much time it adds.*
- **agentos** (1/3): AgentOS already plans sandboxed code execution with exec-gate guardrails (Crucible). The talk's dual-metric eval (pass rate plus complexity and issue density) is a cheap addition to any agent benchmark. → *When benchmarking coding agents in AgentOS, record LOC and cyclomatic/cognitive complexity alongside pass rate, using an off-the-shelf analyzer on the generated code.*
- **general** (1/3): Useful framing for how to judge coding models: functional pass rate is not enough. Treat the talk's numbers as vendor-produced, since no methodology is given beyond the slides. → *Read the Sonar leaderboard methodology before citing its numbers; treat the figures as the speaker's claims.*
