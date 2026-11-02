# Turn Cursor AI into the 500$ Devin (Just Paste this...)

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `wJk2_Ds-9cM` · [watch](https://youtu.be/wJk2_Ds-9cM) · **date:** 2025-11-02 · **length:** 6:38 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed AI LABS narrator · **orgs:** AI LABS, Cursor, Windsurf, Devin, OpenAI
- **topics:** coding-agents, context-engineering, skills-self-improvement · **tags:** cursor-rules, .cursorrules, scratchpad, lessons-learned, persistent-notes-file, task-tracking, resume-from-checkpoint, full-stack-demo, cursor-directory

> Walkthrough of a Cursor rules file that adds a lessons log and task scratchpad, used to build a full-stack Trello clone; one anecdotal demo with overstated "Devin" framing.

## Summary
The narrator presents a .cursor rules file from a GitHub repo (name garbled in captions) and claims it turns Cursor into a Devin-like autonomous engineer. The file's two key additions are a "lesson" section, where the agent records fixes and corrections, and a "scratchpad" section, where it writes a task plan and marks items done. The narrator copies a prompt from GPT into Cursor Composer and builds a Trello-style task board with a Postgres database running in Docker. Afterward, the rules file holds recorded lessons (e.g., the OpenAI model name "gpt-4") and a phased plan with phase 4 paused by the user. The narrator says that when work resumed, the agent picked up at the paused phase. The evidence is a single self-run demo with visible front-end bugs and a lost composer window, with no benchmarks or comparison. The "learns like Devin" framing is marketing; the mechanism is persistent notes files that later sessions read.

## Key ideas
- **The promise is a $20 Cursor subscription behaving like a $500 Devin. The mechanism is a rules file in the project, not a different model.** — The narrator says the repo claims about 90% of Devin's capability and that pasting its .cursor rules file into a repo is the setup. These are the narrator's and the repo's claims; no comparison is shown. ([0:00](https://youtu.be/wJk2_Ds-9cM?t=0))
- **Rules should be per project, not global. Global rules can hurt when they don't apply to a given codebase.** — The narrator advises a .cursor rules file per project, and says global Cursor settings are a poor fit because a rule that doesn't apply everywhere reduces efficiency. Cursor Directory is cited as a source of stack-specific boilerplate (TypeScript, Python, React, Next.js, PHP and others). ([1:24](https://youtu.be/wJk2_Ds-9cM?t=84))
- **Two sections drive the behavior: a lesson section that records corrections, and a scratchpad that tracks tasks. The rest of the file is standard config.** — The other parts are said to cover screenshot tools, LLM access, web browsing, and how to issue commands to the LLM. The narrator calls the lesson and scratchpad sections the real differentiators. ([2:33](https://youtu.be/wJk2_Ds-9cM?t=153))
- **The scratchpad is a checklist the agent writes and updates: tasks are created, followed in order, and marked done while pending ones stay unmarked.** — The narrator builds a Trello-style board from a GPT-written prompt pasted into Cursor Composer. Tasks persist after a page refresh, which the narrator takes as evidence of a real database behind it (Postgres in Docker, with the backend running). ([3:18](https://youtu.be/wJk2_Ds-9cM?t=198))
- **After the project, the rules file contains learned lessons, such as the correct OpenAI model name.** — The narrator reports the agent recorded that 'gpt-4' is the model name to use. He suggests this came from the agent referencing screenshots. The lesson section thus works as a project-specific correction log that later sessions can read. ([4:42](https://youtu.be/wJk2_Ds-9cM?t=282))
- **Resume works because the scratchpad keeps phase state. The agent restarted at the phase the user had paused.** — The plan had 4 phases: setup, backend, frontend, and a paused phase 4. The 'current focus' section let the agent continue from phase 4 where the user stopped it. This is a file-based checkpoint, shown in one anecdotal run. ([5:47](https://youtu.be/wJk2_Ds-9cM?t=347))

## Techniques
- **Per-project .cursor rules file** — Create .cursor/rules (or a .cursor rules file) in each repo, starting from a stack-specific template such as one from Cursor Directory, and adjust it to the project. Avoid putting project-specific rules in global Cursor settings. *When:* Starting a new repo where the team wants consistent agent output and fewer hallucinated APIs or patterns.
- **Lesson log inside the rules file** — Instruct the agent to record each fix or correction it receives in a dedicated 'lesson' section of the rules file, so the next session reads it as context. The narrator's example is recording the correct OpenAI model name. *When:* Recurring mistakes in one codebase, such as wrong API names or config values, where you want to stop repeats across sessions. It is a manual version of what SkillForge tries to automate, and it has no scoring or pruning shown.
- **Scratchpad task plan with checkboxes and a current-focus section** — Have the agent write the project overview, tech stack, project structure and phased implementation plan into a scratchpad section. It marks each task done as it completes, and keeps a current-focus pointer. Next session, it resumes from the first unmarked item. *When:* Multi-phase builds that span several sessions or are paused and resumed. It works as a lightweight checkpoint file when the agent must continue from a known point.
- **Generate the rules prompt with another model, then run it in the IDE agent** — The narrator copied a prompt that GPT wrote for this purpose and pasted it into Cursor Composer, which then created the rules and the project. The prompt text is not shown in the video. *When:* Bootstrapping the rules file for a new project without writing it from scratch. The prompt itself is not shown, so it cannot be reproduced from the video.

## Numbers
- The IDE costs about $20 per month, which the narrator compares to a $500 Devin-like assistant. Both prices are the narrator's framing, not checked. ([0:00](https://youtu.be/wJk2_Ds-9cM?t=0))
- The repo claims about 90% of Devin's capability through the rules file. This is the repo's claim, not measured. ([0:00](https://youtu.be/wJk2_Ds-9cM?t=0))
- Cursor Directory offers stack-specific rules boilerplate, including TypeScript, Python, React, Next.js and PHP. ([1:24](https://youtu.be/wJk2_Ds-9cM?t=84))
- Plan of 4 phases (setup, backend, frontend, paused phase 4). Phases 1-3 completed before the pause. ([4:42](https://youtu.be/wJk2_Ds-9cM?t=282))
- No benchmarks, success rates, token counts or timings are given. The only evidence is one self-run demo. ([3:18](https://youtu.be/wJk2_Ds-9cM?t=198))

## Hot takes
- The 'learns from mistakes like Devin' framing overstates things. The effect comes from notes in a file that the next session reads, which is persistence rather than learning.
- The speaker's own demo shows front-end bugs, and the composer window was lost before the responses could be shown. The result is anecdotal and unreproduced.
- The 'Just Paste this' title and the $500 Devin claim are hype with thin substance.

## Tools mentioned
Cursor, Cursor Composer, Windsurf, Devin, GPT (used to write the prompt), PostgreSQL, Docker, OpenAI API (gpt-4 model name), Trello (clone target, not a tool used)

## Relevance to our work
- **prosharness** (2/3): A scratchpad file with checked-off phases and a current-focus pointer is a simple file-based checkpoint and resume, which is close to ProsHarness's checkpoint/resume of long runs. It is a single anecdotal run, though. → *Before building a heavier checkpoint format in ProsHarness, test whether a plain markdown file with phase checkboxes and a current-focus line is enough to resume a Claude Code run after a restart. Measure how often the resumed run repeats completed work.*
- **agentos** (1/3): Corrections written into a lesson log that later sessions read is a manual, unscored form of the procedural-memory loop in SkillForge and EvolveCraft. The video gives no evidence on success signals or skill-worthiness. → *Use the lesson-log pattern as a cheap baseline for SkillForge. Record corrections as candidate lessons with a source tag, then compare how often they are re-read and whether they repeat mistakes, against the skill-worthiness scoring you plan to build.*
