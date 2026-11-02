# OpenAI's NEW Cloud-based Software Engineer (Codex)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `nPAXAAbU16w` · [watch](https://youtu.be/nPAXAAbU16w) · **date:** 2025-11-02 · **length:** 5:16 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Presenter (Better Stack host, unnamed) · **orgs:** OpenAI, GitHub, Windsurf
- **topics:** coding-agents, software-factory, sandboxing-execution · **tags:** codex, openai, cloud-coding-agent, agents-md, github-integration, parallel-tasks, sandbox-network-off, swe-bench, codex-1, codex-mini

> Launch-day walkthrough of OpenAI's cloud Codex agent: parallel tasks in isolated containers, GitHub integration, AGENTS.md, and the codex-1 and codex-mini pricing.

## Summary
The presenter demos Codex, OpenAI's cloud software-engineering agent, which is separate from the Codex CLI and runs multiple tasks in parallel. Setup connects GitHub, the user picks a repo and an environment, and the agent offers starter tasks in two modes, Ask (answer questions about code) and Code (make changes). Code tasks first set up the environment, then read and edit files and run tests, linters and type checkers, with progress visible in real time. The presenter stresses verifiable evidence: each finished task shows a diff, logs, and test or console output with a pass or fail mark, and it can open a GitHub PR. The model behind it is codex-1, an o3 variant tuned for software engineering, which the speaker says beats o3 High on OpenAI's internal benchmarks and on SWE-bench Verified, though no figures are given. The speaker also reports that tasks run in an isolated cloud container with internet access disabled during execution, and suggests this limits prompt-injection exfiltration. The video is a first-look product tour with little independent testing.

## Key ideas
- **Codex is a cloud agent, distinct from the Codex CLI, that runs several coding tasks in parallel.** — Tasks take between about a minute and 30 minutes. Each task is an ask-type or code-type request, and the agent proposes starter tasks after repo onboarding. ([0:00](https://youtu.be/nPAXAAbU16w?t=0))
- **Environment configuration gives the agent the same toolchain you use locally.** — On a code task the agent first sets up packages and linters, and the environment is customizable so it matches how the team works locally. ([1:14](https://youtu.be/nPAXAAbU16w?t=74))
- **Progress is observable but mid-task course correction was not available at the time.** — You can watch the agent's steps in real time, but if it goes wrong you must wait for the task to finish before redirecting it. ([2:10](https://youtu.be/nPAXAAbU16w?t=130))
- **Repo conventions go in an AGENTS.md file that the agent loads into its context.** — The presenter suggests putting codebase working rules and commit structure in it, so the agent works like a new employee who has read the guidelines. ([2:10](https://youtu.be/nPAXAAbU16w?t=130))
- **Each finished task comes with verifiable evidence: a diff, logs, and a pass or fail mark on test runs or console output.** — The presenter suggests a failed task may flag a real bug worth fixing yourself, which makes the agent useful for triaging bug reports. ([2:10](https://youtu.be/nPAXAAbU16w?t=130))
- **Security model: the task container has internet access disabled during execution.** — The agent can only use the checked-out repo and pre-installed dependencies, with no external websites, APIs or services, which the presenter says helps against prompt injection stealing environment variables. This is the presenter's own reading. ([3:33](https://youtu.be/nPAXAAbU16w?t=213))
- **codex-1 is an o3 variant trained on real-world coding tasks, and it is not available through the API at launch.** — The speaker reports it beats o3 High on OpenAI's internal benchmarks and on SWE-bench Verified, with no numbers quoted. The API offers codex-mini-latest instead, which has no published benchmarks yet. ([3:33](https://youtu.be/nPAXAAbU16w?t=213))

## Techniques
- **Repo-level agent instructions via AGENTS.md** — Create an AGENTS.md markdown file in the repo root. Put in codebase conventions, how to structure commits, and workflow rules. The cloud agent loads it into context before each task. *When:* Before handing a repo to a cloud coding agent, so the agent follows team conventions without per-task prompting.
- **Configure the agent's dev environment to match local** — In the environment setup for the repo, pre-install language packages, linters and similar tools, so the agent's setup step mirrors how you work locally and it can run your test harness, linters and type checkers. *When:* When the agent needs to run tests or static checks to verify its own changes.
- **Turn Ask-mode suggestions into Code tasks** — Run an Ask task to review code for bugs or maintainability. Where the answer includes suggested changes, click the run-code action on a suggestion to have the agent implement it as a separate code task. *When:* For a review-then-fix loop on a codebase without writing the instructions yourself.
- **Use a failing agent task as bug triage** — Give the agent a task to fix a reported bug. If it cannot produce passing test or console evidence, treat the bug as real and work on it yourself. *When:* Triaging bug reports that come into a repo.
- **Ask for verifiable evidence in every completion** — Check the task output for a test run or console log, and for the tick or cross mark, before accepting the diff. Open a GitHub PR from the task output or pull the branch locally to review. *When:* Reviewing any agent-written change before merge.

## Numbers
- Each Codex task takes between about 1 minute and 30 minutes. ([0:00](https://youtu.be/nPAXAAbU16w?t=0))
- codex-mini-latest costs $1.50 per million input tokens and $6 per million output tokens; no benchmarks yet. ([3:33](https://youtu.be/nPAXAAbU16w?t=213))
- codex-1 is said to outperform o3 High on internal benchmarks and on SWE-bench Verified. No scores are given. ([3:33](https://youtu.be/nPAXAAbU16w?t=213))
- Access at launch was for Pro, Team and Enterprise users. ([0:00](https://youtu.be/nPAXAAbU16w?t=0))

## Hot takes
- The title and intro frame Codex as something that will 'steal Devin's' job, which is launch hype with little comparative testing behind it.
- The speaker calls the benchmark results 'absolutely insane' without quoting any numbers, so the claim is unverified.
- The presenter's prompt-injection benefit from the disabled network is his own inference, not something OpenAI is shown to have claimed in the video.

## Tools mentioned
Codex (cloud agent, ChatGPT sidebar / chatgpt.com/codex), Codex CLI (mentioned as distinct), ChatGPT, GitHub (repo connection and PR creation), AGENTS.md, codex-1 (o3 variant for SWE), codex-mini-latest, o3 High (comparison baseline), SWE-bench Verified (benchmark cited), Devin (mentioned as competitor), Windsurf (mentioned as recent OpenAI purchase)

## Relevance to our work
- **agentos** (1/3): The per-task container with network access disabled during execution, limited to the checked-out repo and pre-installed deps, is a reference point for default-deny sandboxing in Crucible's exec path. → *Compare Crucible's celld exec config against a default-deny network policy with a pre-installed-deps allowlist, and document which egress is needed for real tasks.*
- **prosharness** (1/3): AGENTS.md-style repo instructions and requiring test or log evidence before accepting a diff both map onto ProsHarness's checkpoint and approval flow around Claude Code runs. → *Have ProsHarness require a test-run or log artifact in the completion report before marking a Claude Code run done, and load a per-repo instructions file into each run.*
