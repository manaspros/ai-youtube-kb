# Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `W76woOYHlvY` · [watch](https://youtu.be/W76woOYHlvY) · **date:** 2026-05-18 · **length:** 20:23 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Louis Knight-Webb · **orgs:** Vibe Kanban, AI Tinkerers, OpenAI, Cloudflare
- **topics:** software-factory, coding-agents, product-ux, agent-architecture · **tags:** vibe-kanban, plan-and-review, parallel-agents, agent-run-duration, pr-shepherding, focus-maxing, agent-economics, startup-shutdown

> Louis Knight-Webb (Vibe Kanban) argues engineers will mostly plan and review as agents run longer, then live-demos shutting his company down through the tool.

## Summary
The speaker argues that coding time has not been saved by AI coding tools. It has moved into planning and reviewing work. He splits agent work into a plan-heavy mode and a review-in-the-loop mode, and says the right mode depends on the task: front-end feature work needs a human in the loop, while back-end features and refactors/migrations suit planning plus TDD. Agent run times have grown from seconds (Copilot line completion) to 5-10 minutes, and once runs pass about five minutes humans stop watching logs and start running several agents in parallel. He describes Vibe Kanban as a multi-workspace agent UI with diffs, comments and live preview, and sketches a wish list: a tool that lets a human manage many streams, yields to the human only at decision points, and also helps with QA and with shepherding PRs through review comments until deployment. The second half is a live demo of using Vibe Kanban to write the company's shutdown blog post, followed by the business reasons: about 30k monthly users and 25k GitHub stars, but a $30 subscription that lets users spend up to $3,000 of Codex tokens is unsustainable, and only enterprise sales or token resale make money. The transcript is auto-captioned and renders the company name as "VibeCampMan"; the title and slides say Vibe Kanban.

## Key ideas
- **AI has not freed up coding time; it moved the time into planning and reviewing.** — Speaker's rough estimate: for every 30 minutes of coding saved, about 20 minutes come back, and the rest goes to planning and review. Work shifted, not disappeared. ([1:08](https://youtu.be/W76woOYHlvY?t=68))
- **Choose plan-heavy or review-in-loop mode by task type, not by habit.** — Front-end feature work has too many states, edge cases and interactions to spec, so stay in the loop. Back-end feature work can be plan-heavy with TDD. Refactors and migrations should be TDD-driven and run mostly without a human in the loop. ([6:23](https://youtu.be/W76woOYHlvY?t=383))
- **Up-front planning is cheaper than review loops.** — His rule of thumb is that five minutes of planning saves about 30 minutes of reviewing agent code. Back-and-forth with half-finished agent output is the costly pattern. ([6:23](https://youtu.be/W76woOYHlvY?t=383))
- **Agent run times have grown from seconds to minutes, and that changes how humans work.** — Copilot line completion took seconds, early Cursor file edits about 30 seconds, Claude Code 1-2 minutes last year and 5-10 minutes this year. Running type checks and Playwright MCP tests takes longer still, and he argues the wait is worth it for accuracy. ([7:39](https://youtu.be/W76woOYHlvY?t=459))
- **Past about five minutes, humans stop watching agents and run them in parallel.** — A person can wait about five minutes before they start browsing other things. Longer runs push people toward multiple agents at once, so the next task is ready when they finish reviewing the last one. ([8:57](https://youtu.be/W76woOYHlvY?t=537))
- **The ideal agent tool helps a human manage many streams and yields only at decision points.** — He calls the goal focus-maxing: let the agent run as long as possible and bring the human back only when needed. Good tools should help write tasks, QA the output, review code, and handle PR review comments until deployment. ([13:10](https://youtu.be/W76woOYHlvY?t=790))
- **Subscription wrappers around coding CLIs are hard to sustain.** — Users paid about $30 a month to press a button that spends up to $3,000 of Codex tokens. The only models he sees making money are enterprise sales and token resale, and he says he and his team did neither. ([15:54](https://youtu.be/W76woOYHlvY?t=954))

## Techniques
- **Task-type mode selection** — Classify each task as front-end feature, back-end feature, or refactor/migration. Keep a human in the loop for front-end feature work. For back-end features, spend planning time up front (clarifying questions, a detailed spec). For refactors and migrations, drive the work with TDD and stay out of the loop. *When:* Before starting an agent run, to decide how much to plan versus how much to review.
- **Clarifying-question planning** — Let the model ask questions about the task repeatedly until it has no further questions, then write the plan from the answers, so edge cases are settled before the run. *When:* Back-end features or any work where a detailed spec can be written up front and fewer review rounds are the goal.
- **Parallel agent workspaces** — Run each task in its own git worktree, run a setup script to install dependencies, then run the chosen agent. Review diffs, comment on them, and preview the result in the same UI. *When:* When each agent run takes 5 minutes or more and the human needs to switch between several tasks.
- **PR comment shepherding** — Monitor the open pull request for review comments and react to each one automatically, until the change is merged and deployed. *When:* After an agent finishes a task, to handle the review-to-deploy admin work.

## Numbers
- Vibe Kanban had about 30,000 monthly active users and about 25,000 GitHub stars at the time of the talk. ([15:54](https://youtu.be/W76woOYHlvY?t=954))
- Example economics: a user pays about $30 for a subscription that lets them spend up to about $3,000 of Codex usage. ([15:54](https://youtu.be/W76woOYHlvY?t=954))
- Rule of thumb: about 5 minutes of planning saves about 30 minutes of reviewing agent-written code. ([6:23](https://youtu.be/W76woOYHlvY?t=383))
- Rough estimate: about 20 minutes saved for every 30 minutes of coding time, with the rest moved to planning and review. ([2:30](https://youtu.be/W76woOYHlvY?t=150))
- Agent run times: Copilot line completion in seconds, early Cursor file edits about 30 seconds, Claude Code 1-2 minutes last year, 5-10 minutes this year. ([7:39](https://youtu.be/W76woOYHlvY?t=459))
- Five minutes is the rough threshold where humans stop waiting for an agent and start multitasking. ([8:57](https://youtu.be/W76woOYHlvY?t=537))
- Vibe Kanban supports eight popular coding agents. ([14:37](https://youtu.be/W76woOYHlvY?t=877))
- Speaker says Vibe Kanban began about June 14, 2025. ([10:20](https://youtu.be/W76woOYHlvY?t=620))

## Hot takes
- All a software engineer will do all day is plan and review.
- Front-end QA by AI (via Chrome or Playwright MCP) is the next big breakthrough, forecast within about nine months.
- Focus-maxing: tools should be built around human attention, not around constant context switching.
- Subscription wrappers around coding agents cannot make money; only enterprise sales or token resale can.

## Tools mentioned
Vibe Kanban, Claude Code, Codex, Cursor, GitHub Copilot, Playwright MCP, GitHub, Cloudflare CDN

## Relevance to our work
- **prosharness** (2/3): Checkpoint/resume of long runs, parallel runs and phone approvals match the talk's model of agents running for 5-20 minutes and yielding to a human only at decision points. → *Make ProsHarness approvals an async queue: hold a long run at its checkpoint until the human approves, and add a loop that reads PR review comments and re-runs fixes until merge.*
- **agentos** (1/3): The talk's subscription-versus-token economics show a case where one long run burns far more tokens than the user paid for, which a budget layer would need to stop. → *Check Govrix Scout's budget enforcement for long agent runs, so a single run cannot exceed a per-run token ceiling without an explicit stop or approval.*
