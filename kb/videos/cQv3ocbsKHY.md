# I Found the Simplest AI Dev Tool Ever

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `cQv3ocbsKHY` · [watch](https://youtu.be/cQv3ocbsKHY) · **date:** 2025-11-02 · **length:** 5:20 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Fission AI, Better Stack, Amazon, GitHub
- **topics:** context-engineering, coding-agents, token-cost-efficiency · **tags:** spec-driven-development, openspec, opencode, change-proposals, task-lists, vite, react, archive-workflow, parallel-changes

> Walkthrough of OpenSpec, a lightweight spec-driven development tool, building a small Vite/React charting app through a propose, review tasks, apply, archive loop with OpenCode.

## Summary
The presenter introduces OpenSpec, a spec-driven development tool from Fission AI meant to stop requirements from getting lost in chat history and to cut token use, and compares it briefly with Kiro and GitHub SpecKit. He initializes OpenSpec in a fresh Vite React project with OpenCode as the agent, which creates an agents.md file and an openspec folder, then has the agent fill in the project file with purpose, tech stack and conventions. He writes a change proposal for a bar chart tool, reviews its specs, proposal and tasks, and trims the task list in natural language. Applying the change with the apply slash command produces a working app, though image export is low-res and the legend edit does not work. He then archives the finished change and runs two parallel proposals in separate tabs, which fix legend positioning and export quality, and both apply successfully. He concludes OpenSpec is simple (three commands) but has limited agent support and no real-time progress view. The video is a single unbenchmarked demo with no measured token savings.

## Key ideas
- **Spec-driven development turns a vague prompt into a document with tasks the agent follows, which the presenter says reduces bugs in the final project.** — Motivation for OpenSpec is that other spec tools lose requirements in chat history and burn tokens. The presenter frames the whole tool as three steps: draft a proposal, review the tasks, implement the tasks. ([0:00](https://youtu.be/cQv3ocbsKHY?t=0))
- **Initialization creates a project-level spec file that the agent fills in from the codebase.** — After OpenSpec init with OpenCode selected, the repo gets an agents.md file and an openspec folder. The presenter asks the agent to fill out the OpenSpec project file with purpose, tech stack, conventions and more. ([1:24](https://youtu.be/cQv3ocbsKHY?t=84))
- **Each feature change is a folder holding specs, a proposal and a tasks file, and the tasks file can be edited in plain language before any code is written.** — The bar chart change has a specs folder (chart creator), a proposal, and a tasks file with a count. Telling the agent not to run unit or integration tests shrank the task list before implementation. ([1:24](https://youtu.be/cQv3ocbsKHY?t=84))
- **The presenter's main workflow for tracking progress is the list and view commands, not the chat window.** — openspec list shows changes and completed task counts; openspec view shows active changes, completed work and total progress. Applying the change ticks tasks off in the tasks file, so view reflects completion. ([1:24](https://youtu.be/cQv3ocbsKHY?t=84))
- **First-pass output is usable but not right: the export was low-res and the legend edit did not work.** — The presenter calls the one-shot result a good first attempt. Export was low resolution with a mismatched font, and updating the legend did not take effect. ([2:51](https://youtu.be/cQv3ocbsKHY?t=171))
- **Completed changes are archived and independent changes can run in parallel in separate tabs.** — The archive slash command moves a finished proposal into the archive folder. Two new proposals (fixed legend position, higher-resolution export with sans-serif font) each got their own folder with its own tasks and were applied separately. ([2:51](https://youtu.be/cQv3ocbsKHY?t=171))
- **The legend fix worked in both directions, which is the evidence the presenter gives for the parallel-proposal workflow.** — After both changes finished, the legend moved to the bottom, left and right correctly, and could be shown or hidden. The exported image was clearly better and used a sans-serif font. ([4:16](https://youtu.be/cQv3ocbsKHY?t=256))
- **The presenter's verdict: simple to learn, but limited agent support and no live progress; the token-saving benefit is his guess, not measured.** — Only three slash commands are needed. Support for other agents is limited for now, and he wishes progress updated in real time instead of requiring the agent chat window. He suspects this is one of the ways OpenSpec keeps token usage down, which he does not test. ([4:16](https://youtu.be/cQv3ocbsKHY?t=256))

## Techniques
- **Three-step spec loop** — Draft a change proposal (proposal plus specs and tasks), review and trim the tasks in natural language, then apply the change so the agent works through the tasks file. Use this per feature, not for the whole project at once. *When:* Adding a discrete feature or fix to an existing project where you want requirements kept in files rather than chat history.
- **Project file bootstrap** — Run OpenSpec init, select the AI tool (OpenCode in the demo), then ask the agent to fill in the OpenSpec project file with purpose, tech stack and conventions. Init creates agents.md and an openspec folder. *When:* Starting a new repo or adopting OpenSpec in an existing one, so later changes share the same context.
- **Scope a change by editing its tasks** — Open the change's tasks file or ask the agent to revise it (example used: 'do not run any unit or integration tests' for a simple project). The task count drops before implementation. *When:* The generated task list is too large or includes steps you do not want, such as tests on a throwaway project.
- **Track progress from the terminal** — Run openspec list for each change with completed task counts, and openspec view for active, completed and total progress. Applying the change updates the task checkboxes. *When:* You want progress without reading the agent chat transcript.
- **Apply and archive via slash commands** — Use the OpenSpec apply slash command, optionally naming the change, and the OpenSpec archive slash command once a change is finished. Archiving moves the change folder into the archive folder. *When:* Executing a reviewed proposal and then clearing it from the active set.
- **Parallel changes in separate tabs** — Create multiple proposal folders, one per change, each with its own tasks, then run apply for each in its own agent tab. The demo ran two independent changes (legend position; export resolution and font) and both completed. *When:* Several non-overlapping changes to the same codebase that can be implemented independently.

## Numbers
- Video length is 5:20. ([0:00](https://youtu.be/cQv3ocbsKHY?t=0))
- OpenSpec workflow is three steps (draft proposal, review tasks, implement tasks) and three slash commands in total, per the presenter. ([0:00](https://youtu.be/cQv3ocbsKHY?t=0))
- Two proposals were run in parallel for the second round of changes; no task counts or token usage figures are given for either round. ([2:51](https://youtu.be/cQv3ocbsKHY?t=171))
- No token-usage or cost measurement is shown; the claim that OpenSpec reduces tokens is the presenter's guess. ([4:16](https://youtu.be/cQv3ocbsKHY?t=256))

## Hot takes
- OpenSpec is 'simplest' because it needs only three slash commands, but it supports fewer agents than other spec tools, per the presenter.
- No measured token savings are shown; the presenter guesses that the lack of real-time progress tracking is part of how token usage is kept down.
- Single-run demo on a toy app: the first attempt shipped a low-res export and a broken legend, so the value shown is mostly the follow-up change loop, not one-shot quality.

## Tools mentioned
OpenSpec, OpenCode, Vite, React, Kiro, GitHub SpecKit

## Relevance to our work
- **prosharness** (1/3): ProsHarness plans and checkpoints Claude Code runs; OpenSpec's per-change proposal, specs, tasks and archive folders are a file-based version of that plan state, and its list/view commands give a progress readout. → *Compare OpenSpec's per-change folder layout (proposal, specs, tasks, archive) and its list/view progress output with ProsHarness checkpoint files before designing plan storage.*
