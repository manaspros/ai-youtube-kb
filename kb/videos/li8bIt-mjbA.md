# I Couldn't Believe Claude Tasks Could Do This

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `li8bIt-mjbA` · [watch](https://youtu.be/li8bIt-mjbA) · **date:** 2026-02-02 · **length:** 10:00 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic
- **topics:** claude-code, multi-agent, agent-architecture, coding-agents · **tags:** claude-code tasks, task graph, dependency graph, sub-agents, parallel agents, agent swarm, task persistence, session resume, cowork, todos, ctrl+t, ralph loop, CLAUDE.md, PRD, sponsored segment

> Walkthrough of Claude Code's new built-in task system: a coordinator splits work into a dependency graph, runs independent sub-agents in parallel, and persists tasks outside the context window so they survive /clear and restarts.

## Summary
The video explains a new Claude Code task feature that the speaker calls an agent swarm. The main Claude instance acts as a coordinator that turns a broad request into a task graph, labels each task as sequential or parallel, and spawns sub-agents that each run with their own context window. Each task runs an investigate, plan, implement pipeline, and the model tier is matched to task complexity, with Haiku or Sonnet handling simple exploration and Opus 4.5 coordinating. Task state is stored as JSON files in a folder per session ID, with blocks and blockedBy keys encoding the dependency graph, so work resumes after /clear or a restart. The speaker reports that this replaces manual CLAUDE.md note-keeping and the Ralph loop pattern. The second half applies the same pattern to Cowork, a non-developer sibling product, for folder documentation and market research, and to a Claude Code run that parallelized PRD sections. The evidence is a single user's anecdotes with no benchmarks, and the video includes a sponsored segment.

## Key ideas
- **The main Claude instance becomes a task coordinator: it builds a task graph from a broad request, labels each task sequential or parallel, and spawns sub-agents to execute them.** — Each task then runs investigate, plan and implement stages, with each stage blocked by the previous one. The speaker frames this as moving from delegating tasks to delegating the delegation. ([0:00](https://youtu.be/li8bIt-mjbA?t=0))
- **Sub-agents get their own context windows instead of sharing one, which the speaker says is the main reason compaction is needed less often.** — The speaker describes each agent as having a fresh 200k context window isolated from the others. Previously a single context had to hold all the to-dos and compaction often mangled them. ([1:07](https://youtu.be/li8bIt-mjbA?t=67))
- **Tasks are persisted as JSON files outside the context window, so they survive /clear and session restarts.** — Files sit in a folder per session ID inside the Claude config folder (the auto-captions say 'main.cloud', presumably ~/.claude). Each file has an ID, name, description and status. ([2:24](https://youtu.be/li8bIt-mjbA?t=144))
- **Dependencies are stored as blocks and blockedBy keys, which is what enforces ordering and stops Claude skipping ahead.** — The speaker's definitions of the two keys are inverted relative to their names, so verify the semantics on a real file before relying on them. ([3:32](https://youtu.be/li8bIt-mjbA?t=212))
- **Model choice is per task: the coordinator uses Opus 4.5 while exploration and other light work goes to Haiku or Sonnet.** — The speaker says this cuts cost because effort is matched to task size, but gives no token or dollar measurements. ([2:24](https://youtu.be/li8bIt-mjbA?t=144))
- **Parallelism shortens wall-clock time: a five-step graph with two independent roots finishes in three cycles instead of five sequential waves.** — Tasks 1 and 2 have no dependencies, so they start together. Tasks 3 and 4 wait on task 1, and the final task finishes in the third cycle. ([5:00](https://youtu.be/li8bIt-mjbA?t=300))
- **The same swarm pattern works in Cowork, the non-developer product, which has more guardrails than Claude Code.** — Cowork was used to batch-read a messy projects folder and write a summary file per project, and to produce a market-research report saved into the connected folder. ([6:25](https://youtu.be/li8bIt-mjbA?t=385))
- **A PRD can be split into independent sections that Claude Code writes in parallel, and the speaker reports this turned 16 sequential steps into one parallel step.** — This is the speaker's own estimate of the effect. It is an illustrative count, not a measured speedup. ([9:03](https://youtu.be/li8bIt-mjbA?t=543))
- **The breakdown is not automatic for every request; prompting for it explicitly and inspecting the to-dos helps.** — The speaker says Claude sometimes decides a task is not complex enough to split, so asking it to break the work into tasks with dependencies triggers the graph. Ctrl+T shows the to-dos. ([9:03](https://youtu.be/li8bIt-mjbA?t=543))

## Techniques
- **Explicit dependency breakdown prompt** — When Claude handles a multi-part job as a single pass, prompt it to break the work into tasks with dependencies, which makes it create the dependency graph and manage the workflow through it. Use Ctrl+T to view the resulting to-dos. *When:* Large or multi-step work where Claude did not auto-decompose, or where you want explicit parallel and sequential structure.
- **Fan out independent sections of a spec** — Give Claude Code a PRD or design doc and ask it to split it into components, then let it spawn one agent per independent section. Sections with dependencies are ordered by the task graph. *When:* A spec with several sections that do not depend on each other.
- **Named long-running sessions** — Set an environment variable (the name is not given in the video) or a CLI flag (also not named) to the project name, so the session's task folder is keyed by a readable name rather than a random ID and can be reopened later. *When:* Long-running projects you will return to after closing the terminal.
- **Inspect task state on disk** — Look in the Claude config folder for a tasks directory with one subfolder per session ID. Each task is a JSON file with id, name, description, status, blocks and blockedBy. Read these to see what is blocked before resuming. *When:* Debugging a stalled multi-agent run or checking what a resumed session will do.
- **Batch folder documentation with Cowork** — Connect Cowork to a messy folder, ask it to inspect the folder and the CLAUDE.md and reusable commands, and have it spawn agents that read files in batches and write a summary document for each project. *When:* Cataloguing or navigating a large folder of projects or test repos.
- **Research-then-implement handoff** — Use Cowork to produce a research report and PRD saved into a shared folder, then point Claude Code at that document to break it into components for implementation. *When:* Taking a product idea from market research to a coded first pass.

## Numbers
- Each sub-agent gets a fresh 200k-token context window (speaker's statement). ([2:24](https://youtu.be/li8bIt-mjbA?t=144))
- Five-step graph with two independent roots completes in 3 cycles, versus 5 sequential waves without parallelism. ([5:00](https://youtu.be/li8bIt-mjbA?t=300))
- PRD split into sections: 16 sequential steps reduced to one parallel step (speaker's illustrative estimate, not measured). ([9:03](https://youtu.be/li8bIt-mjbA?t=543))
- Cost reduction is claimed from matching model size to task difficulty, with no figures given. ([5:00](https://youtu.be/li8bIt-mjbA?t=300))

## Hot takes
- The speaker claims the new task system finally kills the Ralph loop pattern, but gives no comparison.
- Sub-agents plus smaller models are claimed to cut cost, with no token or dollar numbers shown.
- The 16-to-1 step reduction is an illustrative count from one PRD, not a benchmark.
- The video is a secondhand explainer of a feature announcement rather than a hands-on test with failures or edge cases shown.
- The video has a sponsored segment (Lovart) around 5:00-6:25, which caps quality at 2 under the rubric.

## Tools mentioned
Claude Code, Cowork, Claude Chat, Opus 4.5, Haiku, Sonnet, CLAUDE.md, Notion, Lovart (sponsor segment, not evaluated)

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and does checkpoint/resume of long runs. Claude Code now persists its own task graph per session, which overlaps that feature and changes what ProsHarness needs to store itself. → *Verify the on-disk task JSON layout and resume behaviour in a real session, then decide whether ProsHarness checkpoints should read or reference Claude Code's task state instead of duplicating it.*
- **agentos** (1/3): The coordinator-plus-dependency-graph pattern with persisted task state is a small reference point for multi-agent orchestration in AgentOS, but this is a closed product feature, not infrastructure. → *Compare AgentOS's orchestration state model with the blocks/blockedBy file-backed task graph and decide whether durable dependency state belongs in the platform.*
