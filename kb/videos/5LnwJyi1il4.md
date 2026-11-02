# These Claude Workflows Turn Claude Code Into A Whole OS

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `5LnwJyi1il4` · [watch](https://youtu.be/5LnwJyi1il4) · **date:** 2026-07-02 · **length:** 13:18 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** AI LABS host (unnamed in transcript) · **orgs:** Anthropic, AI LABS
- **topics:** coding-agents, multi-agent, claude-code, token-cost-efficiency · **tags:** dynamic-workflows, claude-code, goal-command, skills, subagents, cron, loops, routines, deep-research, second-brain, claude-md, mcp, hooks, token-usage, workflow-selection

> Walkthrough of how Claude Code's pieces (CLAUDE.md, MCP, skills, loops/routines, dynamic workflows) form an "OS", with guidance on when a deterministic workflow beats goal or a plain skill; mostly a sponsored-style pitch with thin hands-on steps.

## Summary
The speaker (AI LABS) frames Claude Code as an operating system: CLAUDE.md as kernel, MCP as drivers, skills and commands as everyday programs, loops and routines as cron jobs, and dynamic workflows as the layer tying them together. Dynamic workflows are JavaScript files under the .claude/workflows directory that define sub-agent steps and strict output schemas, run in the background, and resume after a session ends. The video contrasts workflows with skills and the goal command, saying goal is non-deterministic while workflows are deterministic, and that workflows are wide (parallel) rather than deep. It warns that workflows burn far more tokens than a normal session because each sub-agent has its own context window. It offers selection criteria: independent subtasks, a task too big for one context window, a result worth cross-verifying, and a deterministic structure. It also covers the built-in Deep Research workflow and example second-brain and coding-project setups. Hands-on detail is light, and the channel pushes its paid membership and "hype button" calls to action.

## Key ideas
- **Claude Code is framed as an OS: CLAUDE.md is the kernel, MCP the drivers, skills and commands the everyday programs, loops and routines the cron jobs, and dynamic workflows the layer that ties them together.** — Speaker maps each OS component to a Claude Code feature. The kernel analogy is the main structuring idea of the video. ([0:00](https://youtu.be/5LnwJyi1il4?t=0))
- **Workflows are deterministic and goal is not. In a workflow, code fixes the sequence of agent calls. With goal, the model decides the next step.** — Workflow plans live in a JavaScript file in the .claude/workflows directory, not in the context window. Each sub-agent call must satisfy a strict output schema and retries until the output matches it. ([3:20](https://youtu.be/5LnwJyi1il4?t=200))
- **Workflows are run with a slash command and resume after the session ends. Each run has an ID, and progress is checked with the workflows command.** — Runs happen in the background. The workflows command shows each stage, the models invoked, and token use per task. Cached agent work is restored on resume. ([4:00](https://youtu.be/5LnwJyi1il4?t=240))
- **Workflows burn far more tokens than a normal session because each sub-agent gets its own context window. Four criteria decide whether to use one: the task splits into independent units, it exceeds one context window, the result needs cross-verification, and the structure is deterministic.** — The speaker warns that a plan on a $200 subscription could run out within hours. Parallelism is lost when subtasks depend on each other. ([5:26](https://youtu.be/5LnwJyi1il4?t=326))
- **Shape of the task decides the choice. Wide tasks (many parallel subtasks) suit workflows. Deep tasks (step by step) suit goal.** — Goal runs one task at a time and does not run things in parallel. Workflows call agents in parallel and let them iterate. ([6:54](https://youtu.be/5LnwJyi1il4?t=414))
- **Deep Research is a built-in workflow in five phases: search for sources, fetch details, adversarial cross-verification, synthesis into a single document. One run cost about a million tokens on a small topic.** — Each sub-agent inherits its tools from the parent. The speaker says this is very token-heavy. ([8:17](https://youtu.be/5LnwJyi1il4?t=497))
- **The speaker suggests a competitor-analysis workflow that improves itself as it runs: when it hits a problem, it records a fix so the next run avoids the same issue.** — One run used 679,000 tokens and 34 agents and produced a markdown report with comparison metrics. The self-improvement mechanism is described only briefly. ([8:17](https://youtu.be/5LnwJyi1il4?t=497))
- **For a coding project, the same structure applies: CLAUDE.md with project context, agents for everyday roles, hooks (for example, formatting after an edit), skills for repeatable tasks, and workflows for review before shipping, migrations and end-to-end tests.** — The migration example claims a library migration took 21 minutes with a workflow versus more than an hour without one. This is a single anecdotal measurement with no detail on setup or cost. ([10:47](https://youtu.be/5LnwJyi1il4?t=647))

## Techniques
- **Start a dynamic workflow** — Put the word 'workflow' in the prompt with clear intent to build one. Claude writes a JavaScript file under .claude/workflows/. Run it with the workflow slash command and the workflow name, and pass it the plan to stress test. Check progress with the workflows command. Resume with the resume command if the session ends. *When:* A deterministic, multi-agent task that is wide, too large for one context, or needs verification.
- **Strict output schemas for sub-agents** — Define each sub-agent step in workflow code with a prompt plus a schema. The agent keeps working until its output matches the schema, then returns its findings. *When:* When downstream steps need machine-checkable structured output from parallel agents.
- **Choose workflow vs goal vs skill** — Skill: one agent follows structured instructions. Goal: non-deterministic loop toward an end condition, one task at a time. Workflow: deterministic code calling several agents, parallel. Pick by whether the task is wide or deep and whether the next step must be decided at runtime. *When:* Before starting any multi-agent or long-running task, to avoid burning tokens on the wrong mechanism.
- **Convert a skill from a session** — After a long session, ask Claude to combine the learnings from that session into a skill. *When:* When you notice you will repeat a task often.
- **Coding-project OS setup** — Keep project context in CLAUDE.md. Define project agents for everyday roles. Add hooks, for example to format a file after an agent edits it. Create skills for repeatable tasks such as adding an endpoint. Add workflows for review before shipping, migrations, and end-to-end tests. *When:* Setting up a repo that will get repeated agent-driven changes.
- **Second-brain audit workflow** — Build a workflow that checks a notes vault for broken links and reports every issue, then run fixes from the report. *When:* A personal knowledge vault connected to Claude Code has been in use for a while.

## Numbers
- A Deep Research run on a small topic used about 1,000,000 tokens. ([8:17](https://youtu.be/5LnwJyi1il4?t=497))
- A competitor-analysis workflow run used 679,000 tokens and 34 agents. ([8:17](https://youtu.be/5LnwJyi1il4?t=497))
- A library migration took 21 minutes with a workflow, versus more than an hour without one (single anecdotal test by the speaker). ([11:56](https://youtu.be/5LnwJyi1il4?t=716))
- Speaker cites a $200 plan that can run out in a few hours of heavy workflow use. ([5:26](https://youtu.be/5LnwJyi1il4?t=326))

## Hot takes
- Workflows are deterministic and goal is not, so the choice between them should be made on the shape of the task.
- Workflows are often overkill: spawning many agents for a task that does not need verification or parallelism wastes tokens.
- Sponsored or channel-promotion content: the closing segment pushes the paid AI LABS Pro membership and asks for hype and super thanks. Substance is moderate, and the framing is more a pitch than a how-to. Quality is capped at 3 for that reason.

## Tools mentioned
Claude Code, Claude Opus 4.8, CLAUDE.md, MCP, Google Calendar MCP, Notion MCP, Deep Research workflow, goal command, loops, routines, hooks, skills

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and does checkpoint/resume of long runs. The workflow resume-by-ID model and the deterministic-vs-goal split are direct comparison points, and the token warning applies to its planned multi-agent debate flow. → *Compare ProsHarness checkpoint/resume against Claude Code workflow resume-by-ID and check the token cost of plan, critique and debate stages.*
- **agentos** (1/3): Dynamic workflows with strict sub-agent schemas and cross-verification are a Claude Code analogue of multi-agent orchestration in the agent OS thesis, but the video stays at the product level. → *Check whether the .claude/workflows JavaScript pattern with per-step output schemas and resume-by-ID fits the orchestration design for the agent stack.*
