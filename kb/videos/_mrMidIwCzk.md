# I Let 30 AI Agents Loose in My Repo (Gas Town)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `_mrMidIwCzk` · [watch](https://youtu.be/_mrMidIwCzk) · **date:** 2026-03-02 · **length:** 7:28 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host · **orgs:** Better Stack, Anthropic (Claude Code)
- **topics:** multi-agent, coding-agents, software-factory · **tags:** gastown, multi-agent, orchestration, claude-code, git-persistence, parallel-agents, beads, convoys, polecats, mayor, token-cost, oversight

> A Better Stack walkthrough of Gastown, an open-source orchestrator that runs many Claude Code agents in parallel on one feature, shown on a Go to-do app with a single prompt and a candid look at the costs.

## Summary
The host introduces Gastown as an open-source orchestrator layered on top of Claude Code rather than a model. A high-level goal goes to a "mayor" agent, which splits it into task units called beads, groups them into convoys, and hands them to worker agents called polecats that run in parallel. All work runs through Git: each agent uses its own branch, merges are queued, and orchestration state is persisted so a crash can resume from saved state. In the demo, a simple Go to-do app with no auth gets one prompt asking for JWT auth on SQLite, login and register endpoints, protected routes, HTML forms, tests and a Dockerfile. The host reports that the mayor decomposed this into separate beads (schema, middleware, auth routes, UI forms, tests, Docker) that ran at the same time, and that the resulting repo had register, login, protected routes and passing tests while the existing to-do list still worked. Setup was painful (many Homebrew packages and troubleshooting), and the run consumed a lot of tokens. The host lists scalability and Git-backed persistence as pros, and oversight fatigue, cost, agent conflicts, over-engineering and repo damage as cons. The evidence is one anecdotal run with manual checking, no cost figures and no setup commands.

## Key ideas
- **Gastown is an open-source orchestrator, not a model. It sits on top of Claude Code and coordinates multiple agents, which the host compares to Kubernetes for dev workflows.** — A single mayor agent takes the high-level goal and breaks it into beads, which are grouped into convoys and executed by polecat workers in parallel. ([0:00](https://youtu.be/_mrMidIwCzk?t=0))
- **Git is the persistence and isolation layer. Each agent works on its own branch, merges go through a queue, and state is saved so a crash resumes from persisted state instead of restarting.** — The host frames this as the main advantage over a single linear Claude Code session, which loses context on crash and needs manual re-prompting. ([1:18](https://youtu.be/_mrMidIwCzk?t=78))
- **One broad prompt was decomposed into parallel work units without step-by-step prompting.** — Prompt asked for JWT auth on SQLite, login/register, route protection, HTML forms, tests and a Dockerfile. The mayor created separate beads for schema, middleware, auth endpoints, front-end forms, tests and Docker, and they were worked on at the same time. ([2:30](https://youtu.be/_mrMidIwCzk?t=150))
- **The host argues the benefit is cognitive offloading: the system holds the plan, not the human.** — The host also says this does not automatically make things a win, because running the agents may be costly. ([3:53](https://youtu.be/_mrMidIwCzk?t=233))
- **The demo output was judged to work: login and registration worked, routes were protected, tests passed, and the to-do list still functioned.** — The host checked the GitHub diff and ran the app by hand. The run ate a lot of tokens. Verification was manual; no automated acceptance criteria are shown. ([4:56](https://youtu.be/_mrMidIwCzk?t=296))
- **The stated trade-offs are oversight fatigue (reviewing a large volume of agent output), cost of many parallel agents, agent conflicts, over-engineering, and possible repo damage from broad permissions.** — The host calls it an early-stage tool and says it is not plug-and-play. Other model providers can be configured, per the host. ([4:56](https://youtu.be/_mrMidIwCzk?t=296))
- **The host's bigger claim is that the bottleneck shifts from writing code to orchestrating and reviewing it.** — This is opinion framing, not something the demo measures. It is the main thesis of the closing segment. ([6:05](https://youtu.be/_mrMidIwCzk?t=365))

## Techniques
- **Mayor-decomposed parallel feature build** — Give one high-level multi-part feature goal to a coordinator agent. It splits the goal into independent task units (schema, middleware, routes, UI, tests, Docker). Each unit runs as a separate worker on its own Git branch, and merges are queued. Gastown's own commands and config were not shown in the video. *When:* Large features with several loosely coupled parts that touch many files, where one developer would otherwise do the parts in sequence.
- **Git-backed orchestration state for crash recovery** — Persist the task graph and agent state in Git so a crashed run can resume from the last saved state instead of starting over. The host describes this without showing the mechanism. *When:* Long agent runs where losing a session halfway would waste time and tokens. Relevant as a checkpoint/resume model.
- **Verify parallel agent output by diff and running the app** — After the run, review the full diff on the remote repo, run the app, confirm the old features still work, and run the test suite. The host did this by hand, with no automated acceptance gate. *When:* Any multi-agent run whose output will be merged, since the video shows review load as the main cost.

## Numbers
- Host says Gastown can run 20 to 50 agents in parallel. The demo does not report an agent count. ([0:00](https://youtu.be/_mrMidIwCzk?t=0))
- The full auth feature was decomposed and implemented in a few minutes (no exact figure given). ([3:53](https://youtu.be/_mrMidIwCzk?t=233))
- Pros slide cites 20 to 30 concurrent agents as the scalability case. No cost, token or latency figures are given; the host says the cost is high, 'I'll let you do the math'. ([4:56](https://youtu.be/_mrMidIwCzk?t=296))
- Video length is 7:28, with one demo run. ([0:00](https://youtu.be/_mrMidIwCzk?t=0))

## Hot takes
- Gastown is 'horizontal scaling for cognition'. This is the host's framing, not measured.
- The 20 to 50 agent headline is not backed by the demo, which does not report how many agents ran.
- The real value is Git persistence and crash recovery, not raw speed.
- Parallel agents shift the bottleneck from writing code to reviewing it (oversight fatigue).
- The video's quality is capped at 2 because it is a single anecdotal run with no setup steps, commands or cost numbers. The title is also hype-leaning.

## Tools mentioned
Gastown, Claude Code, Go, SQLite, Docker, Homebrew, JWT, GitHub

## Relevance to our work
- **prosharness** (2/3): Git-persisted orchestration state with crash resume and per-agent branch isolation overlaps ProsHarness checkpoint/resume of long runs and its plan, critique and debate flow. → *Compare Gastown's Git-branch-per-worker isolation and persisted task state with ProsHarness checkpoint/resume. Check whether the same model can hold plan-critique-debate state.*
- **agentos** (1/3): Multi-agent cost and parallel token burn are a concern for any infra that fans out agent work, but the video gives no cost data or budget mechanism. → *If AgentOS adds per-run budgets, test a per-run token cap before fanning out parallel agent workers, and log the cost per worker.*
