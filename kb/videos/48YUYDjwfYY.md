# Stop Rationing Tokens: Let the Harness Pick the Model — Kimchi by Cast AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `48YUYDjwfYY` · [watch](https://youtu.be/48YUYDjwfYY) · **date:** 2026-10-04 · **length:** 18:08 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Laurent (co-founder and president, Cast.ai), Zilvinas (leads engineering for Kimchi) · **orgs:** Cast.ai, Kimchi, Google, Anthropic, Uber
- **topics:** token-cost-efficiency, infra-cost-scaling, coding-agents, sandboxing-execution · **tags:** kimchi, cast-ai, model-routing, cost-per-task, token-cost, coding-agent, ferment, teleport, studio, long-running-agents, scored-completion, remote-sandbox, open-source-models, agent-harness

> Cast.ai's Kimchi team argues for routing each task to the cheapest model that still meets a quality bar, judged by cost per task, with long-running sessions kept alive in remote sandboxes.

## Summary
Laurent (Cast.ai) and Zilvinas (Kimchi engineering) present Kimchi, a coding agent whose harness picks a model per task, mixing proprietary models for hard cases with open-source models for the rest. They argue that cost per token is misleading and that cost per task at equal quality is the right comparison, citing a university white paper's figures. Over three months of internal use they report about 2.5x savings versus an all-Claude bill, and show the harness's model choice shifting over time. The team built Ferment, a milestone-based runner for tasks of two or more hours that scores its output and loops back on failed builds, and requires at least a B score before staging. Teleport runs the session in a remote VM so it survives a closed laptop, and Studio adds a shared Kanban-style board for team review of agent plans. Most of the talk is product promotion, and the savings figures are the speakers' own internal numbers.

## Key ideas
- **Compare models by cost per task at equal quality, not by price per token** — The speaker cites a university white paper where a model with a low per-token price (Gemini 3 Flash, about $3.5 per million blended) cost about $705 per task, while Minimax 2.7 at about $1.5 per token cost about $148 per task. Per-token price does not predict task cost. ([2:38](https://youtu.be/48YUYDjwfYY?t=158))
- **Let the harness pick the model per task based on the outcome, not a fixed choice** — The argument is that a human cannot keep re-testing new models, but an automated harness that tracks outcome and cost can. The speaker says the selected model shifted sharply on June 12 and that the top model changed several times in June, which is why the selection has to be automated. ([3:39](https://youtu.be/48YUYDjwfYY?t=219))
- **Limiting developer tokens is the wrong fix; make the cost per outcome cheaper** — The speakers frame token caps as a bad experience for developers. Their goal is to keep the coding agent effectively unlimited while cutting cost per task, which they say grows far more slowly than token volume. ([1:39](https://youtu.be/48YUYDjwfYY?t=99))
- **Ferment: a long-running runner that scores output and loops until it passes** — The user answers setup questions up front, then the run splits the work into milestones and runs for two or more hours with a human needed only about every two to three hours. A higher-order model checks quality, and failed builds send the agent back to fix and rebuild. A run is complete only at a B grade or better. ([7:08](https://youtu.be/48YUYDjwfYY?t=428))
- **Gate on staging, keep a human before production, and treat code review as insufficient** — Changes deploy to staging automatically, but production is still gated by a human by design. The speakers name pod crash and health-check signals as checks still to be automated. They say reading diffs no longer scales, for example a product manager's 2,000-line PR, so review should focus on intent and spec. ([10:04](https://youtu.be/48YUYDjwfYY?t=604))
- **Teleport: run the agent session in a remote VM so it survives the laptop** — The local environment is synced to a container in a hyperscaler (Google is named). It behaves the same from the laptop and keeps running after it closes, with notifications when the agent needs input. The speaker says 62% of their engineers use it for coding. ([11:27](https://youtu.be/48YUYDjwfYY?t=687))
- **Studio: share agent sessions and plans as a team Kanban board** — Built on Teleport, Studio shows all running sessions in review, in progress and backlog. A teammate can claim a session that needs review, answer it, and send it back, so specs are checked before the agent executes them. ([14:25](https://youtu.be/48YUYDjwfYY?t=865))

## Techniques
- **Per-task cost-at-quality model comparison** — Score each candidate model on the same task set by both quality and total cost per completed task, and compare on cost per task rather than list price per token. *When:* Choosing or routing among models whose per-token prices and token usage differ widely.
- **Outcome-scored harness with a grade gate** — After each milestone or full run, have a separate judge model grade the output. Loop back to fix and rebuild until the grade clears a threshold such as B, then promote to staging. *When:* Long autonomous coding runs where a run should only count as done when its output has been checked.
- **Milestone-based long-run planning with up-front questions** — Collect the requirements at the start, break the task into milestones, and let the agent run for hours, asking the human only at defined checkpoints. *When:* Multi-hour coding tasks where a human is needed only occasionally.
- **Remote sandbox session that outlives the client** — Mirror the local dev environment into a managed VM or container, keep the agent running there, and send notifications when input is needed. Access the session from laptop or mobile. *When:* Agent runs that must continue while the laptop is closed or offline, or that need team visibility.
- **Team review board for agent sessions** — Expose plans and in-progress sessions on a shared board with review, in progress and backlog columns, so teammates can review and take over a session before execution. *When:* Several engineers or a PM need to check agent specs before code is produced, not after.

## Numbers
- Company that spent $500M on Anthropic in one month (cited from news; not verified by the speaker) ([0:13](https://youtu.be/48YUYDjwfYY?t=13))
- Uber CTO reportedly used the full-year Anthropic budget in four months (cited from a tweet) ([0:13](https://youtu.be/48YUYDjwfYY?t=13))
- Kimchi team size: about 300 employees, about two-thirds developers ([2:38](https://youtu.be/48YUYDjwfYY?t=158))
- Gemini 3 Flash: about $3.5 per million tokens blended, but about $705 per task in the cited study ([3:39](https://youtu.be/48YUYDjwfYY?t=219))
- Minimax 2.7: about $1.5 per token, about $148 per task in the cited study ([3:39](https://youtu.be/48YUYDjwfYY?t=219))
- About 2.5x savings versus the Claude bill over three months of internal use (speaker's internal figure) ([5:05](https://youtu.be/48YUYDjwfYY?t=305))
- Token volume rose about 1.5x while cost fell about 1.5x; the speaker also says spend grew 2.5x to 3x slower than token volume, which is inconsistent with the 1.5x figure ([5:05](https://youtu.be/48YUYDjwfYY?t=305))
- Model selection by the harness shifted sharply on June 12; Kimi 2.6 led on June 3 and Minimax 3 led on June 21 ([6:09](https://youtu.be/48YUYDjwfYY?t=369))
- Ferment runs for two or more hours, with humans needed about every two to three hours ([7:08](https://youtu.be/48YUYDjwfYY?t=428))
- A run is accepted only at a B grade or higher, with staging as the last automatic step ([10:04](https://youtu.be/48YUYDjwfYY?t=604))
- 62% of Kimchi engineers use Teleport when coding (speaker's internal figure) ([12:54](https://youtu.be/48YUYDjwfYY?t=774))

## Hot takes
- Limiting developer tokens is the wrong response to token cost; the job is to make tokens cheap and effectively unlimited.
- Per-token price is misleading; compare models on cost per completed task at equal quality.
- Reading code is no longer enough once non-engineers and agents produce large PRs; review intent and spec instead.
- Model selection should be automated by the harness and not left to humans.

## Tools mentioned
Kimchi, Ferment, Teleport, Studio, pi-mono SDK (captioned as 'PyMono SSDK'), Claude

## Relevance to our work
- **agentos** (2/3): L1 strategy routing and budgets could use cost-per-task at equal quality as the routing metric, rather than per-token price. Also a pattern for scoring long-run outputs. → *Log per-request cost plus a quality grade per task type in the Govrix proxy, and compare candidate routing strategies by cost per graded task, not cost per token.*
- **prosharness** (2/3): ProsHarness runs long checkpointed Claude Code sessions. Ferment's grade-gated loop and milestone questions overlap with checkpoint/resume and the critique step. → *Add an outcome grade gate before a checkpointed run is marked done, with a fixed threshold and a bounded retry loop, and compare it against the existing Codex critique step.*
- **general** (2/3): Recurring interest in cheap-model pipelines and agent evals. The cost-per-task-at-quality method is a reusable comparison rule for Haiku versus larger models. → *When comparing a Haiku pipeline against a larger model, report cost per task at matched grader score, not per-token price.*
