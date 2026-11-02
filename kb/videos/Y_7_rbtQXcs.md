# This is basically an X-ray for your codebase...

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Y_7_rbtQXcs` · [watch](https://youtu.be/Y_7_rbtQXcs) · **date:** 2026-08-02 · **length:** 4:58 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** observability, coding-agents, evals · **tags:** session-replay, agent-trace-visualization, llm-as-judge, 3d-visualization, claude-code, codex, mindwalk, graphify

> Short Better Stack walkthrough of MindWalk v0.3, a 3D session replay for Claude Code and Codex runs, with an LLM judge that grades how the agent explored, stayed in scope and verified its work.

## Summary
The host argues that agent logs record what an agent did but not how it chose its files, so reviewing agent-written code by scrolling diffs misses the process. MindWalk renders a repo as a dark 3D city where each file is a building sized by its code, then replays a session on a timeline. Cool colors mark files the agent only read and warm colors mark files it edited. Timeline markers show sub-agent spawns, context compactions and user interruptions. The analyze command runs a judge over the session using the local claude or codex CLI, asking whether the agent explored enough before editing, stayed in scope, wandered, and verified its work, with each finding linked to a moment on the timeline. The host is candid about limits: it is version 0.3, reads only Claude Code and Codex logs (not Cursor), and Hacker News commenters questioned its purpose. He says a plain git diff is better for small changes and the tool is most useful for comparing how two models explore a task or reviewing a large, sprawling change.

## Key ideas
- **Agent logs show actions but not reasoning about which files mattered.** — The host says a transcript lists what the agent ran and edited, but not which files it judged relevant, where it searched before editing, or whether it stayed in scope. MindWalk is pitched as a way to recover that. ([0:00](https://youtu.be/Y_7_rbtQXcs?t=0))
- **Session replay as a 3D city with color-coded file access.** — Each file is a building whose height follows its code size. Files the agent glances at glow green, files it reads turn blue, and files it edits turn amber. The timeline can be scrubbed to trace the path the agent took. ([1:01](https://youtu.be/Y_7_rbtQXcs?t=61))
- **Timeline markers for orchestration events.** — Symbols mark where a sub-agent was spawned, where the context window was compacted, and where the user interrupted with a new instruction. ([1:01](https://youtu.be/Y_7_rbtQXcs?t=61))
- **Read-only ingestion of local session logs.** — The tool is a single Go binary that reads the session logs Claude Code and Codex already write to disk, and renders the 3D scene in the browser with Three.js. No agent-side instrumentation is described. ([1:01](https://youtu.be/Y_7_rbtQXcs?t=61))
- **LLM judge over the full session, with findings linked to timeline moments.** — The analyze command runs a judge using the user's local claude or codex CLI. It asks whether the agent explored enough before editing, stayed in scope, wandered, and verified its own work. Each finding is a clickable link to the relevant point in the replay. ([2:20](https://youtu.be/Y_7_rbtQXcs?t=140))
- **Map mode works without a session.** — A map command renders any repository as the 3D city without a recorded session. ([2:20](https://youtu.be/Y_7_rbtQXcs?t=140))
- **Honest scoping of when the lens is worth it.** — The host says it is early (version 0.3, Claude Code and Codex logs only). Use it to compare models' exploration patterns or to get the shape of a large agent change. For a two-line fix, reading the diff is faster. ([3:38](https://youtu.be/Y_7_rbtQXcs?t=218))

## Techniques
- **Color-coded session replay of file access** — Map each file touched in an agent session to read (glance vs. full read) or edit events from the session log, then color files by activity (green glance, blue read, amber edit) and scrub a timeline to reconstruct the path. The video shows the visual scheme only; no commands beyond the tool name are shown on screen. *When:* Reviewing a long agent run where the final diff does not show which files the agent examined or why it made its changes.
- **LLM-judge rubric over a whole agent session** — Feed the full session to a local model acting as a judge, with a fixed rubric: did it explore before editing, did it stay within scope, did it wander, did it verify its own work. Require each finding to cite a timestamp in the session so it can be checked against the replay. *When:* Auditing the process of agent runs at scale, or comparing how two models approach the same task, where outcome-only checks miss process failures.
- **Timeline event markers for multi-agent runs** — Overlay markers for sub-agent spawns, context compactions and user interrupts on the session timeline so process events can be located next to file activity. *When:* Debugging long or multi-agent sessions where compaction or sub-agent handoffs may have lost context.
- **Choose the review lens by change size** — Use a plain diff for small, local edits. Use a session replay plus judge report for large, multi-file agent changes where the diff does not show the shape of the work. *When:* Deciding how much review effort an agent-written change needs.

## Numbers
- Version 0.3 of the tool, which reads only Claude Code and Codex logs (Cursor not supported). ([2:20](https://youtu.be/Y_7_rbtQXcs?t=140))
- Video length 4:58; no benchmarks, costs, or token counts are reported. ([0:00](https://youtu.be/Y_7_rbtQXcs?t=0))

## Hot takes
- The host calls the tool too early for serious use and says a plain git diff beats it for a two-line fix.
- The judge feature is presented as the most important part, but no judge output, accuracy check, or cost is shown on screen.
- Graphify is named as a comparison point but not compared.

## Tools mentioned
MindWalk v0.3, Claude Code, Codex, Three.js, Graphify (named as a comparison, not evaluated)

## Relevance to our work
- **agentos** (1/3): Session replay and LLM-judge rubric over agent runs is a process-observability idea that touches AgentOS L4 observability and the open SkillForge question of what signal marks a successful run. → *Prototype a judge rubric (explored before editing, stayed in scope, verified own work) over stored agent traces and check whether it separates runs that pass tests from those that do not, as a candidate success signal for SkillForge.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, and this tool reads the same Claude Code session logs to replay and judge runs. → *Read ProsHarness-produced Claude Code session logs with a post-run judge pass that links findings to timestamps, and use the output in the checkpoint or review step.*
