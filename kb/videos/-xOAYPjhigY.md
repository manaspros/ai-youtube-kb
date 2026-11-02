# Claude Code Just Got a Brain Upgrade Inspired By Beads

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `-xOAYPjhigY` · [watch](https://youtu.be/-xOAYPjhigY) · **date:** 2026-02-02 · **length:** 6:11 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Anthropic, Better Stack
- **topics:** claude-code, multi-agent, context-engineering, agent-architecture · **tags:** claude-code, tasks, todos, sub-agents, task-dependencies, shared-task-list, beads, ralph-wiggum-loop, context-window, smart-zone-dumb-zone, opus-4.5

> Better Stack walkthrough of Claude Code's new task system (v2.1.6+), which replaces todos with JSON-backed tasks that support dependencies, sub-agents, and shared task lists across sessions; compared against Beads and the Ralph Wiggum loop.

## Summary
Better Stack shows that Claude Code upgraded its todo lists to a task system (requires Claude Code 2.1.6 or higher). Each task is stored as its own JSON file under a tasks directory in the user's .claude folder, with an ID, subject, description, and blocked-by/blocks dependencies. Claude can turn a plan file into tasks, then run each task in a sub-agent, so the main session used only 18% of its context. Setting a task-list ID environment variable lets multiple sessions share one task list, so one session can do work and another can verify it. The speaker argues this is similar to Beads, but Beads uses SQLite plus a single JSONL file, and the new system is a list the model picks from, not a single prompt repeated in a Ralph-style loop. The video is a short product walkthrough with a sponsor segment for Better Stack at the end. Claims about the feature come from a single tweet, which the speaker says is the only documentation at recording time.

## Key ideas
- **Todos became tasks: each task is a JSON file with id, subject, description, and blocks/blocked-by links** — The new system stores each task as its own JSON file under a tasks folder in the user's .claude directory, namespaced by project. Claude sets up dependencies between tasks, and the UI highlights the blockers. ([1:19](https://youtu.be/-xOAYPjhigY?t=79))
- **Run tasks in sub-agents to keep the main context small** — After the plan was converted to tasks, each task ran in a sub-agent, and independent tasks ran in parallel. Context use in the main session was 18% at the end. ([2:37](https://youtu.be/-xOAYPjhigY?t=157))
- **Shared task list across sessions via an environment variable** — Setting the task-list ID variable (named CLAUDE_CODE_TASK_LIST_ID in the transcript, auto-caption reads as 'code task list ID') to a directory's ID lets several sessions, in split panes, tabs, or machines, see the same progress. One session can do the work while another verifies it. ([2:37](https://youtu.be/-xOAYPjhigY?t=157))
- **Commit tasks to git and resume on another machine** — Because tasks are plain JSON, they can be committed and pulled, so work can stop on one machine and continue on another from the same point. ([4:00](https://youtu.be/-xOAYPjhigY?t=240))
- **Beads comparison: SQLite plus one JSONL file versus many JSON files** — Beads stores tasks in SQLite for fast reads and syncs them to a single JSONL file that can be shared with a team. Claude's system uses multiple JSON files, one per task. ([4:00](https://youtu.be/-xOAYPjhigY?t=240))
- **Task lists are a pick-the-next-task model, not a Ralph-style loop** — The Ralph Wiggum loop repeats one prompt against a list of tasks. The new system has the model read the whole list and choose the next task. The speaker says this is weaker for open-ended autonomous loops that should keep improving a project from a north-star prompt file. ([4:00](https://youtu.be/-xOAYPjhigY?t=240))
- **Documentation and visualization are still thin** — At recording time the only documentation was a single tweet, and there is no Kanban-style view like the one Beads has. ([5:19](https://youtu.be/-xOAYPjhigY?t=319))

## Techniques
- **Plan file to tasks, then sub-agent execution** — Ask Claude to convert a plan file into tasks. Claude creates tasks with dependencies. Ask it to run each unblocked task in its own sub-agent, so independent tasks run in parallel and the main context stays small. *When:* Multi-step implementation plans with several independent parts, where the main session's context should stay lean.
- **Shared task list across sessions via env var** — Set the task-list ID environment variable to the ID that matches the tasks directory before starting each session (exact name is as read from the auto-caption: CLAUDE_CODE_TASK_LIST_ID, verify in the docs). Sessions in different panes, tabs, or machines then share progress. Use one session to implement and another to verify. *When:* Several sessions or machines on the same project, or a builder session paired with a verifier session.
- **Version-control task state** — Commit the tasks directory to git and pull it on another machine to resume work from the same task state. *When:* Handing off long-running work between machines or teammates.

## Numbers
- Claude Code 2.1.6 or higher is required for the task tools ([1:19](https://youtu.be/-xOAYPjhigY?t=79))
- Opus 4.5 has a 200K context window; the speaker says output quality drops past about 80% of it (smart and dumb zones) ([0:00](https://youtu.be/-xOAYPjhigY?t=0))
- Main session context used after running all tasks in sub-agents: 18% ([2:37](https://youtu.be/-xOAYPjhigY?t=157))

## Hot takes
- The new task system is a 'brain upgrade' inspired by Beads, but it is not a replacement for the Ralph Wiggum loop for autonomous, open-ended work.
- The feature lacks documentation and visualization tooling at recording time, so it is still rough.
- Only a short sponsored segment at the end for Better Stack; the rest is a product walkthrough with a short demo.

## Tools mentioned
Claude Code (v2.1.6+), Beads, Ralph Wiggum loop, Opus 4.5, XDL (CLI for downloading videos from X/Twitter, used as the demo project), Better Stack

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code and handles checkpoint/resume of long runs, and this feature offers a built-in task store with dependencies, sub-agent execution, and shared task lists. → *Check whether ProsHarness checkpoint/resume should read or write the Claude Code task directory, so runs can resume from the shared task state.*
- **agentos** (1/3): Shows a file-per-task, dependency-aware task model with shared state across sessions, which is a small pattern for agent coordination, but it is not an infra topic. → *Compare this file-per-task JSON layout with the state model for ProsHarness checkpoints before adding a separate task store.*
