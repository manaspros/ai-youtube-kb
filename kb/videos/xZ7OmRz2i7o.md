# I Tried Running a Company Made of AI Agents

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `xZ7OmRz2i7o` · [watch](https://youtu.be/xZ7OmRz2i7o) · **date:** 2026-06-02 · **length:** 7:27 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Better Stack, Paperclip, GitHub
- **topics:** multi-agent, agent-architecture, token-cost-efficiency · **tags:** paperclip, multi-agent orchestration, agent org chart, tickets, heartbeats, budgets, audit log, self-hosted control plane, postgres, skills.md, coding agents, npx

> Walkthrough of Paperclip, a self-hosted control plane that runs several AI agents as a company with an org chart, tickets, heartbeats, budgets and audit logs; useful for multi-agent coordination, overkill for single-agent tasks.

## Summary
The host sets up Paperclip locally with one npx command, creates a company with a goal (ship a URL shortener MVP this week), and adds a CTO agent plus two engineer agents through adapters, one owning the backend and one owning frontend and tests. A budget is set before start and a working-directory path is configured. The agents then wake on heartbeats, the CTO breaks the goal into tickets, and the engineers pick up work, with delegation, ticket ancestry, status changes and the budget counter all visible in the dashboard. The host frames Paperclip as a management layer above workflow frameworks like CrewAI, AutoGen and LangGraph: those are checklists, while Paperclip is the manager, org chart, ticket board, budget system and audit log. The main value claimed is that cost is enforced as part of the control loop (budget set before execution) rather than checked afterward. The host lists real downsides: bad rules produce off-scope tickets, budgets do not fix sloppy prompts or vague skill files, and the run was slow. The verdict is that it is overkill for summarizing a file or patching one bug, and worth it only when many agents need to work together.

## Key ideas
- **Multi-agent setups turn into management work once you have more than one agent** — Questions like who owns a task, who remembers the goal, and who stops an agent doing the wrong thing are the problem Paperclip targets. Raw agents are useful but hard to coordinate. ([0:00](https://youtu.be/xZ7OmRz2i7o?t=0))
- **Paperclip models agents as a company: goal, org chart, tickets, heartbeats, budgets, approvals** — You define a company goal and an org chart (e.g. CEO, CTO, two engineers, a research agent). Work is coordinated through tickets, periodic heartbeats, budgets, approvals and traceability back to the goal. ([1:10](https://youtu.be/xZ7OmRz2i7o?t=70))
- **Budget is set before the agents start, not reviewed afterward** — The host sets the budget before hitting start, framing the goal as controlled autonomy so agents cannot run up an API bill. The video does not show the budget unit or its granularity. ([2:21](https://youtu.be/xZ7OmRz2i7o?t=141))
- **Heartbeat-driven loop: the CTO decomposes the goal into tickets and engineers pick them up** — Agents wake on heartbeat. The CTO agent turns the goal into tickets, engineers claim them, and the dashboard shows delegation, ticket ancestry, status changes and the budget counter tied together. The first implementation task reached a code commit, but the run was slow. ([2:21](https://youtu.be/xZ7OmRz2i7o?t=141))
- **Positioning: Paperclip is a manager layer above workflow frameworks, not another one** — CrewAI, AutoGen and LangGraph are described as workflow checklists (researcher, then planner, then writer, then reviewer). A single agent is an employee, a workflow is a checklist, and Paperclip is the manager, org chart, ticket board, budget system and audit log. ([3:36](https://youtu.be/xZ7OmRz2i7o?t=216))
- **The harder questions are about control, not code generation** — The host argues agents can already write code; the open questions are whether an agent works on the right task, stops when it should, hands off work clearly, and can be inspected. ([3:36](https://youtu.be/xZ7OmRz2i7o?t=216))
- **A shared operating model replaces one terminal or tab per tool** — Instead of separate windows for Claude Code, Cursor, a research agent and a GitHub-issue script, Paperclip offers one dashboard that the host compares to Jira or Linear for agents, with portable templates. ([4:46](https://youtu.be/xZ7OmRz2i7o?t=286))
- **Known failure modes: bad rules create nonsense tickets, and budgets do not fix sloppy prompts** — The CTO agent opened a plan the host did not want. Token burn remains real, and budgets cap spend without fixing vague rule definitions. Skill MD files define how the company behaves, so weak ones produce a confused company. ([5:56](https://youtu.be/xZ7OmRz2i7o?t=356))
- **Overkill for single-agent tasks** — For one agent that summarizes a file or patches a bug, the host says the structure is not needed. It is for many agents working together. ([6:55](https://youtu.be/xZ7OmRz2i7o?t=415))

## Techniques
- **Goal-first company setup** — Create a company with one explicit goal, add roles as agents (CTO, backend engineer, frontend and test engineer, research agent) with an adapter per agent, and set the working-directory path where code will be written. The CTO agent decomposes the goal into tickets. *When:* When more than one agent must share a project and you need delegation rather than one agent doing everything.
- **Budget-before-execution guardrail** — Set a budget for the company or agents before starting heartbeats, so spend is capped by the control loop rather than checked after a run. *When:* Long autonomous multi-agent runs where API cost could explode. The video does not show per-agent versus company-wide granularity.
- **Heartbeat wake cycles** — Agents wake on a periodic heartbeat, check their tickets, and act, instead of running continuously in one chat. *When:* Background or long-running agent teams that should resume work on a schedule and stop cleanly.
- **Ticket ancestry for traceability** — Each ticket records who assigned it and which parent work it serves, so every change can be traced back to the company goal and to its cost. *When:* When you need to audit why an agent did something and whether it still serves the end goal.
- **Skill files as company rules** — Put the team's rules and role instructions in skill MD files; the host says the quality of these files determines how the whole company behaves. *When:* When the agent team must follow consistent conventions across roles.
- **Local install and launch** — Run the npx onboard command in a clean terminal (the transcript renders it as 'NPX Paperclip AI on board'; the exact package name is not shown in the captions and should be checked against the project README). It starts a local dashboard with a bundled Postgres and auth. *When:* Trying Paperclip locally before any real project; it is self-hosted and open source so it can be inspected and modified.

## Numbers
- Paperclip has passed 64,000 stars on GitHub (self-reported by the host, not verified) ([0:00](https://youtu.be/xZ7OmRz2i7o?t=0))
- Example org chart: CEO, CTO, two engineers, and a research agent ([1:10](https://youtu.be/xZ7OmRz2i7o?t=70))
- Example goal: build and ship a URL shortener MVP this week; budget value not stated ([2:21](https://youtu.be/xZ7OmRz2i7o?t=141))
- The first implementation task reached a code commit, but the run 'took quite a bit of time' with no duration given ([2:21](https://youtu.be/xZ7OmRz2i7o?t=141))
- No spend, token count or cost-per-task figures are shown ([5:56](https://youtu.be/xZ7OmRz2i7o?t=356))

## Hot takes
- Budgets set before execution are the real differentiator; the host says most agent tools only check cost after the fact.
- The host says that if your skill MD files are weak, your company behaves like a confused startup, so the multi-agent value depends on rule quality.
- Overkill for simple scripts; the host's own verdict is that a single agent summarizing a file or patching a bug does not need this.
- The 64,000-star figure is a self-reported claim in the video and was not checked.
- The demo shows the setup and coordination but no measured outcome (cost, time, quality) for the URL shortener run.

## Tools mentioned
Paperclip, npx (Node package runner), Postgres (bundled with Paperclip), CrewAI, AutoGen, LangGraph (rendered as 'Landgraf' in captions), Claude Code, Cursor, GitHub (issues), Jira, Linear

## Relevance to our work
- **agentos** (2/3): AgentOS already has budgets (Govrix Scout) and a Merkle audit log; Paperclip treats budget as a pre-execution control loop and ties tickets to goal ancestry, which is a useful comparison for the multi-agent layer. → *Compare Paperclip's budget-before-execution and ticket-ancestry model against the Govrix Scout budget and audit path, and decide whether per-agent budgets must be enforced before a heartbeat or tool call.*
- **prosharness** (2/3): ProsHarness already has loops/schedules, checkpoint/resume and phone approvals; Paperclip's heartbeat, approvals and ticket-ancestry model overlaps with those features for multi-agent Claude Code runs. → *Review Paperclip's heartbeat, approval and ticket model to see whether ProsHarness loops should record a ticket-style parent link for each sub-task, and whether budgets should be checked before each heartbeat.*
