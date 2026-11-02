# How to Use Cursor AI with Its Own Cursor Memory Bank

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `azXNHRtzd5s` · [watch](https://youtu.be/azXNHRtzd5s) · **date:** 2025-11-02 · **length:** 7:11 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Cline, Cursor, Windsurf, Unsplash
- **topics:** memory, context-engineering, coding-agents · **tags:** memory-bank, cursor-rules, cursor-user-rules, plan-mode, act-mode, markdown-context-files, task-management, project-context, nextjs

> A short walkthrough of Cline's "Memory Bank" pattern: a set of structured markdown files that keep a coding agent's project context across sessions, set up in Cursor via pasted global rules. Practical but thin, with an admitted rules bug.

## Summary
The speaker presents Memory Bank, a markdown-file pattern released by Cline (transcribed as "Klein"), as a way to stop coding agents from losing context across long sessions. The bank is a set of structured files (project brief, product context, system patterns, tech context, progress) that the agent reads and updates, plus a plan mode and an act mode with a task list. The instructions ship as plain text, so the speaker ports them into Cursor's global User Rules and asks the agent to initialize the bank for a sample Next.js wallpaper app. The agent generates the files by reading the project, and also derives Cursor rules from the system patterns, which the speaker notes is a deprecated mechanism. A workaround for plan mode is shown: the speaker blocks file edits to force planning, which he describes as a bug in the rules file. The claims that the approach reduces or eliminates hallucinations are asserted, not measured, and the video is a single anecdotal run.

## Key ideas
- **The problem: long agent sessions in Cursor or Windsurf lose context, so the user repeats themselves or the agent re-reads the codebase to recover it.** — The speaker frames the Memory Bank as a fix: structured files that persist context across sessions, so the context window is not filled with re-reading and hallucinations are claimed to drop. ([0:00](https://youtu.be/azXNHRtzd5s?t=0))
- **The bank is a fixed set of markdown files, each with a role: project brief, product context, system patterns, tech context, and progress.** — Tech context lists the stack and dependencies; the speaker says this prevents version or framework mistakes, citing a case where Cursor wrote React Router code into a Next.js project. Progress records the development cycle and tasks. The transcript lists product context twice, so the exact file set is slightly unclear. ([0:00](https://youtu.be/azXNHRtzd5s?t=0))
- **The instructions are plain text, so the pattern is not tied to Cline and can be used in any agentic IDE.** — The speaker says someone has already ported it to Cursor, and that the same files work in other agentic IDEs once the setup text is pasted. ([1:24](https://youtu.be/azXNHRtzd5s?t=84))
- **Two workflow modes: plan mode reads the bank to decide the next step, and act mode checks the bank, updates tasks, acts, then updates the docs to match what happened.** — A built-in task management layer sits alongside the memory files so the agent keeps its task list current. The speaker calls the combination memory plus task management. ([1:24](https://youtu.be/azXNHRtzd5s?t=84))
- **Initialization is a one-time prompt: paste the rules, then ask agent mode to create the bank, and the agent reads the project and fills the files itself.** — The first attempt failed because the project was copied into the folder after Cursor opened, so the agent could not see it and asked for project details. Reopening Cursor fixed it, and the speaker notes that a clean start would have skipped the question. ([2:58](https://youtu.be/azXNHRtzd5s?t=178))
- **Generated system patterns can be turned into Cursor rules, but the speaker says that Cursor rules mechanism is deprecated and only still works because the global rules point at the bank.** — The agent also produced a Mermaid diagram of the architecture, which the speaker says is hard to read in raw form. The generated rules can be edited by hand. ([4:29](https://youtu.be/azXNHRtzd5s?t=269))
- **Plan mode was enforced by making the agent unable to edit files, which the speaker calls a bug in the Cursor rules file and a workaround.** — The agent mapped out the landing-page change in plan mode, then the speaker switched it to act mode, where it edited files. This is a single run, not a tested method. ([5:54](https://youtu.be/azXNHRtzd5s?t=354))

## Techniques
- **Paste a memory-bank rules file into Cursor User Rules** — Open the Memory Bank markdown file, switch to the raw view, copy the full text, and paste it into Cursor's Rules section. The speaker uses global User Rules because per-project rules take longer to set up; he mentions tutorials exist for project-specific rules. *When:* Use when you want the same agent memory setup across all projects and do not want to configure per-project rules yet.
- **Initialize the memory bank with a single agent-mode prompt** — In Cursor agent mode, ask the agent to initialize the memory bank. It reads the rules, creates the files one at a time, reads the project, and fills in brief, context, tech stack, and progress. If the agent says it cannot see the project folder, reopen Cursor and ask again. *When:* Use at the start of a new project, or when a project has been copied into a folder that Cursor had not indexed.
- **Force plan-then-act with edit blocking** — The speaker makes the agent unable to edit files so it stays in plan mode, reviews the plan, then tells it to switch to act mode to implement. He describes the blocking as a workaround for a bug in the Cursor rules file. *When:* Use when you want to review an agent's plan before any file changes; the speaker says this is a workaround and not a supported mode switch.
- **Keep the bank current in act mode** — Each act-mode step updates the task list and then the documentation to match the work done, so the progress file tracks reality after each change. *When:* Use on long multi-session projects where a stale progress file would send the agent to the wrong task.

## Numbers
- The video runs 7:11; it demonstrates a single initialization and a single plan-then-act cycle on one sample project (a Next.js wallpaper app). ([0:00](https://youtu.be/azXNHRtzd5s?t=0))
- The speaker says the approach reduces or even eliminates hallucinations and context-window fill, but gives no measurement or comparison. ([0:00](https://youtu.be/azXNHRtzd5s?t=0))
- The bank has five or six structured markdown files (brief, product context, system patterns, tech context, progress), with product context named twice in the transcript. ([0:00](https://youtu.be/azXNHRtzd5s?t=0))

## Hot takes
- The title says 'Cursor Memory Bank', but the speaker says at the start that it is not built into Cursor. It is a Cline pattern ported to Cursor by a third party.
- The speaker says the Cursor rules approach used here is deprecated, and that his plan-mode workaround depends on what he calls a bug in the rules file.
- The hallucination and context-window claims are asserted without any measurement or before/after comparison.

## Tools mentioned
Cline (Memory Bank, named 'Klein' in the transcript), Cursor (agent mode, User Rules, Cursor 2), Windsurf, Next.js, React Router, Unsplash API, Mermaid

## Relevance to our work
- **agentos** (1/3): Markdown memory-bank files are a cheap cross-session context pattern for coding agents, adjacent to the MemoryMesh context and tiered-memory work, but it is a file convention and not a retrieval system. → *Compare the brief/context/patterns/progress file set against what MemoryMesh stores for a project, and decide whether a per-repo markdown memory file is worth exposing as a knowledge bucket.*
- **prosharness** (1/3): Its plan mode, act mode, and progress file that is updated after each act step resemble ProsHarness checkpoint/resume state, but the video gives no resume semantics and the mechanism is fragile. → *Compare the progress file's update-after-act step with ProsHarness checkpoint/resume state, and check whether a progress file could serve as the resume checkpoint format.*
