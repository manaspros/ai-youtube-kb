# Fighting AI with AI — Lawrence Jones, Incident

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `L2r6vLlLgs8` · [watch](https://youtu.be/L2r6vLlLgs8) · **date:** 2026-05-18 · **length:** 17:29 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Lawrence Jones · **orgs:** Incident.io, Anthropic, Netflix, Etsy, Skyscanner
- **topics:** evals, observability, coding-agents, multi-agent · **tags:** eval-driven-development, file-system-as-context, backtests, agent-runbooks, trace-debugging, incident-response, parallel-subagents, failure-clustering, prompt-regression

> Lawrence Jones (Incident.io) on using AI tools to debug and improve multi-prompt AI systems: export UI traces and eval suites as file systems for coding agents, then run parallel backtest analysis pipelines.

## Summary
Lawrence Jones, a founding engineer at Incident.io, explains how his team manages the complexity of their AI SRE product, which runs investigations with hundreds of telemetry queries and very many prompts. He treats evals as AI unit tests stored in YAML next to the Go prompts, but large production-derived evals became unmaintainable, so the team built a small CLI that lets coding agents list, add, and edit test cases without loading the whole suite. The bigger shift was exporting their debugging UIs (traces, interactions, investigations) as plain text file trees, which Claude Code can search and reason over inside a sandbox to find which prompt or tool to change. For fleet-level questions, they run daily backtests and then a Claude Code analysis pipeline defined as markdown playbooks in a repo: roughly 25 parallel subagents analyse each investigation and write results to files, then a clustering stage groups failure modes to explain why an accuracy number moved. The speaker argues that file systems beat MCP or browser agents for bulk context, and that any complex analysis should be written as a repeatable AI runbook.

## Key ideas
- **Evals are AI unit tests, kept next to the prompts** — Each eval runs a prompt on input data and grades the output with criteria (e.g. style and meaning preserved). Evals live in YAML beside the Go prompt code and gate prompt changes before merge. ([4:43](https://youtu.be/L2r6vLlLgs8?t=283))
- **Production-derived evals become unmaintainable** — Real evals often contain a whole incident report, which is the only thing that triggers the bad behaviour. These files grow very large and coding agents hit context limits trying to read them. ([6:02](https://youtu.be/L2r6vLlLgs8?t=362))
- **A small CLI lets agents work with large eval suites** — The CLI lists test cases and adds, replaces, or edits one at a time, so the agent never loads the full suite. A runbook (or skill) tells the agent how to use it. ([6:02](https://youtu.be/L2r6vLlLgs8?t=362))
- **Agent prompt-fix loop: failing eval first, then fix, then regression check** — The agent writes an eval that reproduces the bug, edits the prompt until it passes, re-runs the full suite to catch regressions, and then consolidates the prompt so it does not bloat. ([7:31](https://youtu.be/L2r6vLlLgs8?t=451))
- **Multi-prompt systems hide the cause of bad behaviour** — The chatbot graph has around 10 or more agents (the speaker says it may be 50), and each investigation step expands into hundreds of prompts and tool calls. Knowing which prompt to change is the hard part, not the red-green cycle. ([8:48](https://youtu.be/L2r6vLlLgs8?t=528))
- **Export UI debugging views as file trees** — Agents struggle with UI tools, but they are good with files and standard tools. Each AI interaction is downloaded as a self-documenting text file tree, and Claude Code is pointed at it in a sandbox alongside the codebase to find where to change the system. ([9:50](https://youtu.be/L2r6vLlLgs8?t=590))
- **Backtest pipelines explain metric movements, not just the roll-up** — A daily backtest gives a single rolled-up accuracy number that does not show why it moved. Downloading all investigations into files and running parallel per-item analysis, then cohort clustering, produces a report on why the system does well or badly on a given customer account. ([12:28](https://youtu.be/L2r6vLlLgs8?t=748))

## Techniques
- **Eval-tool CLI for agents** — Build a small CLI that can list, get, add, replace, and edit individual test cases in a large eval suite file, so an agent never reads the whole file. Pair it with a runbook or skill that explains the workflow. *When:* Eval suites have grown large enough that agents hit context limits when they read or edit them directly.
- **Runbook-driven prompt fix** — Have the coding agent (1) write an eval that reproduces the failure, (2) edit the prompt until the eval passes with repeats and an acceptable pass rate, (3) run the whole suite to check for regressions, and (4) consolidate the prompt to keep it simple. *When:* A prompt behaves wrongly and the change must not break other cases. Use it for any prompt edit that will be merged.
- **Download trace or interaction as a file tree** — Render each AI interaction, including all prompts, tool calls, and sub-steps, as text files in a folder structure that mirrors the UI. Put it in a sandbox with the codebase and let the coding agent search it with ordinary tools. *When:* A bad interaction needs root-causing across many prompts and tools, and the UI is too slow for humans to inspect.
- **Parallel per-item analysis with file-based resume** — Fan out about 25 subagents, one per investigation or run. Each writes its analysis to a file. Keep these files as checkpoints so a run can stop and restart without redoing finished items. *When:* You must analyse hundreds or thousands of agent runs in batch, and the analysis must survive interruptions.
- **Cohort clustering over failures** — After the per-item analysis, run a second stage that clusters the findings by failure type or cause. Use the clusters to explain why a metric moved and what to change. *When:* A backtest or eval metric changes and you need causes, not only the number.
- **Analysis as a repeatable markdown playbook** — Store the analysis flow as markdown playbooks in a repo that a coding agent follows each time, so the same steps run reliably on each new batch. *When:* The same complex analysis will run again and again, for example on a daily backtest.
- **Investigate, fix, then verify in one session** — In one coding-agent session with the codebase loaded, have the agent analyse the failure, propose the change, make it, and then prove it with the eval red-green loop before opening a PR. *When:* A root cause has been found in trace or backtest analysis and a code or prompt change is the fix.

## Numbers
- Team has been building this system for about 1.5 to 2 years ([0:57](https://youtu.be/L2r6vLlLgs8?t=57))
- An investigation runs hundreds of telemetry queries (logs, metrics, traces, historical incidents), and behind it are hundreds, if not thousands, of prompts ([0:57](https://youtu.be/L2r6vLlLgs8?t=57))
- A human normally needs about an hour to fully understand an incident well enough to judge whether an investigation was right ([2:10](https://youtu.be/L2r6vLlLgs8?t=130))
- Chatbot agent graph has about 10 agents, and the speaker says it may be around 50 (too large for the slide) ([8:48](https://youtu.be/L2r6vLlLgs8?t=528))
- Daily backtests run across thousands of investigations over hundreds of customer accounts; one roll-up showed 86% accurate RCA on the team's own account ([12:28](https://youtu.be/L2r6vLlLgs8?t=748))
- Analysis pipeline starts about 25 parallel agents, one per investigation ([13:48](https://youtu.be/L2r6vLlLgs8?t=828))
- Speaker claims a runbook-based approach saves days or weeks of work (his estimate, not measured) ([16:11](https://youtu.be/L2r6vLlLgs8?t=971))

## Hot takes
- File systems are exceptionally good agent context. The speaker says an MCP server or human-use browser agents would have been much less effective than bulk-downloading the data for a coding agent to search.
- Any complex analysis should be written as an AI runbook rather than done ad hoc, and this saves days or weeks.
- Debugging tools should be built for coding agents first, since agents cannot use UI tools well.

## Tools mentioned
Claude Code, Codex, Go, YAML

## Relevance to our work
- **agentos** (2/3): SkillForge needs to mine agent telemetry into skills and has an open question on success signals. The backtest plus per-run analysis plus clustering pattern is a direct way to test candidate success signals offline. → *Prototype an offline SkillForge pass: export a batch of agent runs to text files, run about 25 parallel subagents to label each run against candidate success criteria, then cluster the failures. Use it to compare candidate success signals before building them into the pipeline.*
- **prosharness** (1/3): Its per-step file outputs and resume behaviour mirror the speaker's file-per-item checkpoints for parallel subagent runs. → *Check whether ProsHarness checkpoint/resume state for long runs can be written as per-item files that a parallel subagent fan-out fills in and a later stage reads, so resumed runs skip finished items.*
