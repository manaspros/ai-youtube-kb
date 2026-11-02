# Is This The Future of Vibe Coding? (Vibe Kanban)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `NKkO8JL6IJg` · [watch](https://youtu.be/NKkO8JL6IJg) · **date:** 2025-11-02 · **length:** 5:03 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Host (unnamed, Better Stack) · **orgs:** Better Stack, GitHub
- **topics:** software-factory, coding-agents, vibe-coding-app-building · **tags:** vibe-kanban, kanban, parallel-agents, git-branches, pull-requests, task-board, npx, tailwind, nuxt, open-source

> Better Stack walkthrough of Vibe Kanban, a free open-source board that assigns tasks to coding agents, runs them in parallel and sends their diffs to review; the setup is clear, but the depth is thin and the demo shows bugs.

## Summary
The host presents Vibe Kanban as a kanban board where each task card is handed to an AI coding agent that works on it in parallel. He walks through first launch (npx vibe-kanban, a full-access warning, choosing an agent and editor, connecting GitHub), project creation with optional setup and dev scripts, and task creation with a natural-language prompt. The demo builds a Nuxt and Tailwind app with a landing page and a Flappy Bird page from two parallel tasks. He then reviews the agent's diffs, opens the files in VS Code, and runs the game locally. He calls the tool free and open source, and closes by listing known bugs in the Open IDE, Dev and Merge buttons, with Merge failing on Mac but working on Windows. There is no architecture, cost, or evaluation detail, and the title's "future of vibe coding" framing is not argued.

## Key ideas
- **A kanban board dispatches tasks to coding agents** — Each card is a task. Starting it hands the task to an agent, and cards move through To Do, In Progress, In Review, Done and Canceled. Several tasks run in parallel. ([0:00](https://youtu.be/NKkO8JL6IJg?t=0))
- **Full-access warning on first launch** — The app warns that AI agents have full access to the computer and that the user runs it at their own risk. The user must accept this to continue. ([0:00](https://youtu.be/NKkO8JL6IJg?t=0))
- **Agent and editor are chosen at setup, and GitHub is required** — Supported agents named in the transcript are Claude Code, Amp, Gemini, OpenCode, and one more that the captions render as 'echo' (probably Codex). The agent CLI must be installed first. GitHub must be connected so agents can create branches and PRs. ([1:05](https://youtu.be/NKkO8JL6IJg?t=65))
- **Per-task agent and base branch, not just per-project** — Each task's detail view sets the base branch and the coding agent. The host argues mixing agents is useful because some are better at coding and others at docs or simple work. ([1:52](https://youtu.be/NKkO8JL6IJg?t=112))
- **Create task versus create-and-start** — The task form offers 'create the task' (queue it) or 'create the task and start'. The demo queues a second task and starts both, so they run side by side. ([1:52](https://youtu.be/NKkO8JL6IJg?t=112))
- **Review is diff-based and happens in the In Review column** — Finished code tasks show diffs of created and edited files. The host opens the project in VS Code, installs modules, and runs the local server to test the result. ([2:54](https://youtu.be/NKkO8JL6IJg?t=174))
- **The tool is free and open source, with visible rough edges** — The host calls it free and open source and invites contributions. He then lists bugs: the Open IDE button fails sometimes, the Dev button is disabled, and Merge does not work on Mac but does on Windows. ([2:54](https://youtu.be/NKkO8JL6IJg?t=174))

## Techniques
- **Kanban as a dispatcher for parallel agent tasks** — Write one task per card with a self-contained prompt, such as 'create a new Nuxt project with two pages and Tailwind CSS' or 'create a new GitHub repository'. Start several cards and let them run concurrently. Each agent works on its own branch, and the card's state shows progress. *When:* Independent, small, well-scoped tasks such as scaffolding, docs, or a new page. Less suited to tasks that touch the same files, since the video does not explain how conflicts are handled.
- **Setup via npx and the in-app flow** — 1) Install the agent CLI you plan to use (Claude Code in the demo). 2) Run `npx vibe-kanban`. The transcript shows the command with its space dropped, as 'npxvibe-kanban'. 3) Accept the full-access warning. 4) Pick the agent and editor (VS Code in the demo). 5) Connect GitHub. 6) Create a project from an existing repo or a new one, with optional setup-script and dev-script fields. 7) Create tasks. *When:* Trying the tool on a throwaway project first, since agents get full machine access. The video does not describe any sandboxing.
- **Per-task agent and base-branch selection** — Open the task detail view and set the base branch and the coding agent before starting. Use a different agent for documentation or simple chores than for core code. *When:* Mixed workloads where agent strengths differ, or when a task must branch from something other than the default branch.
- **Human review gate before merge** — Move finished cards to In Review. Inspect the diffs of created and edited files, open the checkout in an editor, install dependencies, and run the app locally. Only then use the Merge action. *When:* Any agent-written code. The Merge button was buggy on Mac in the video, so verify the branch in git directly if it fails.

## Numbers
- Video length is 5:03. ([0:00](https://youtu.be/NKkO8JL6IJg?t=0))
- Five board columns: To Do, In Progress, In Review, Done and Canceled. ([0:00](https://youtu.be/NKkO8JL6IJg?t=0))
- The demo runs 2 tasks in parallel. ([2:54](https://youtu.be/NKkO8JL6IJg?t=174))
- Five coding agents are listed as supported, plus one more that the captions render as 'echo'. ([1:05](https://youtu.be/NKkO8JL6IJg?t=65))
- Pricing is stated only as free and open source. No paid tiers or costs are mentioned. ([2:54](https://youtu.be/NKkO8JL6IJg?t=174))

## Hot takes
- Quality is capped at 2: the title asks whether this is 'the future of vibe coding' and calls it 'the ultimate form of vibe coding', but the video is a 5-minute walkthrough with no architecture, evaluation, or cost analysis.
- The host calls the tool 'great' and says it will make workflows 'so much faster' right after listing broken core buttons, so the verdict is not supported by what was shown.
- The full-access warning is shown but not discussed. A tool that runs agents with unrestricted machine access needs a real isolation story before it is recommended.

## Tools mentioned
Vibe Kanban (npx vibe-kanban), Claude Code, Amp, Gemini CLI, OpenCode, Codex (transcript shows 'echo', likely Codex), VS Code, GitHub, Nuxt, Tailwind CSS, MCP servers (configurable in the app)

## Relevance to our work
- **prosharness** (1/3): ProsHarness is a harness around the Claude Code CLI that handles long-run checkpoints and approvals. Vibe Kanban runs parallel Claude Code tasks with a human review gate, so the two overlap in concept. The video shows no design details to borrow. → *Compare Vibe Kanban's per-task branch plus In Review gate with ProsHarness's approval flow. Only read the source if the repo is public, and do not adopt it on the strength of this video.*
