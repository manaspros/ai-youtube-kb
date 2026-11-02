# Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `il1c1a2FufU` · [watch](https://youtu.be/il1c1a2FufU) · **date:** 2026-08-18 · **length:** 1:15:02 · **format:** workshop · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Jason Liu · **orgs:** OpenAI, Codex
- **topics:** coding-agents, context-engineering, skills-self-improvement, multi-agent · **tags:** codex-app, pinned-threads, compaction, heartbeat, goal-verifier, app-shots, computer-use, memory-vault, agents-md, voice-input, remote-control, skills, plugins, monitor-thread, gpt-5.5

> Jason Liu (OpenAI) shows how he runs Codex as a personal ops system: pinned long-lived threads, a git-tracked memory vault, heartbeats, and goal verifiers. Main takeaway: compaction makes long threads workable.

## Summary
Jason Liu, who works at OpenAI, gives a hands-on workshop on how he uses the Codex desktop app for nearly all knowledge work, not only coding. The core claim is that compaction now works well enough that multi-week threads with hundreds of subagents keep their state, so the old advice to start a new thread every feature or after about 20 messages no longer holds. He organises work as pinned threads that act like teammates or managers, and those threads can list, rename and message each other. Context comes in through voice dictation, app shots (screenshot plus accessibility tree), plugins, and a personal memory vault kept as a git repo so he can review what the agent changed with git diff. Work is kept moving with heartbeats (a message scheduled back into the same thread), /goal runs that stop only when a verifier passes, and a monitor thread that spawns child threads for recurring issues. The talk ends with practical cautions: use low or medium reasoning effort by default, set stopping criteria for scheduled checks, and rely on permission modes and agents.md rules rather than full-auto. Many claims are anecdotes from a single power user and are not measured, and the talk is partly a product showcase for the Codex app.

## Key ideas
- **Compaction is the enabling change, so long-lived threads work** — The speaker says he has threads five weeks old with about 400 subagents that still know their job. This makes the old rule (new thread per feature, or after about 20 messages) outdated. ([2:37](https://youtu.be/il1c1a2FufU?t=157))
- **Pinned threads act as teammates, and they can coordinate** — Each pinned thread owns a workstream (chief of staff, SDK, a god thread). Threads can list, rename and message other threads, so the user can move from being an IC with an IDE to managing threads. ([5:29](https://youtu.be/il1c1a2FufU?t=329))
- **Speak to the machine instead of typing** — He uses a foot pedal for dictation and sends long, messy voice memos. Speech is about three times faster than typing, and the model can resolve vague references by searching the history. ([6:50](https://youtu.be/il1c1a2FufU?t=410))
- **App shots give the model context in one hop** — Pressing the app shot shortcut sends the image plus the app's accessibility tree. The model then has channel IDs and user IDs directly, so it can post to a Slack channel in one tool call instead of OCR plus several lookups. ([16:32](https://youtu.be/il1c1a2FufU?t=992))
- **A git-tracked personal memory vault holds the context** — The vault has projects/, people/, daily summaries and a to-do list. An agents.md line tells the agent to put code outside the vault (for example in /dev). He reviews what the agent changed with git diff. ([17:57](https://youtu.be/il1c1a2FufU?t=1077))
- **Heartbeats wake the same thread on a schedule** — Saying 'keep an eye on this every 30 minutes' schedules a message back into the thread. Examples include keeping a PR mergeable and rebased, and checking support threads hourly until someone replies. ([34:41](https://youtu.be/il1c1a2FufU?t=2081))
- **/goal uses a verifier as the stop condition** — The agent keeps working until a verification step passes, such as all unit tests passing. For long runs, the goal, plan and a work log live in editable files, so scope can change mid-run. ([39:17](https://youtu.be/il1c1a2FufU?t=2357))
- **Monitor threads spawn and forward work to child threads** — A monitor thread watches incoming feedback and creates a pinned thread per issue. If a known issue recurs, it sends a message to the downstream thread rather than opening a duplicate. ([56:06](https://youtu.be/il1c1a2FufU?t=3366))
- **Use low or medium reasoning effort by default** — He argues that X-high is a misconception for most work, that low thinking on the newest model beats earlier models, and that scheduled checks need stopping criteria, such as replying with a single word when nothing has changed. ([1:12:07](https://youtu.be/il1c1a2FufU?t=4327))

## Techniques
- **Long-lived pinned thread per workstream** — Rename the thread to the project, pin it to the sidebar, and let it delegate to subagents and create or rename other threads. Rely on compaction to keep state over weeks. *When:* Multi-week projects where one owner juggles many streams and needs one place to see status.
- **Heartbeat / loop in the same thread** — Ask the agent to keep an eye on a PR, inbox or channel every N minutes. The scheduled message returns to the same thread. Add a stopping rule, such as replying with one word when there are no updates. *When:* Waiting on external events (reviews, CI, a reply from a colleague) without losing context to a new thread each time.
- **/goal with a verifier and file-backed goal** — Define a verification command (for example, all unit tests pass). Keep the goal, plan and a state or work-log file in editable markdown, so the goal can be changed while the loop runs and a day's progress can be summarised later. *When:* Migrations or rewrites with an automated oracle, such as a test suite. Not for work without a verifier.
- **App shot plus accessibility tree** — Use the app shot shortcut in the Codex app. It sends the screenshot together with the accessibility tree so the model gets IDs and structure, not only pixels. *When:* Acting on something visible in a desktop app, such as replying in Slack or filling in a form.
- **Git-tracked personal memory vault with agents.md routing** — Keep projects/, people/ and daily summaries in one git repo. Put a rule in agents.md saying where code should be written outside the vault. Review changes with git diff. *When:* One person coordinating many projects and many contacts, who needs an auditable record of what the agent changed.
- **Monitor thread that spawns per-issue threads** — A monitor thread consumes incoming signals, opens a pinned child thread per issue, and forwards recurrences to the existing child thread. *When:* High volume of recurring issues, such as support or feedback streams.
- **Skill from one completed run, with self-edit permission** — Do the task once, have the agent document it as a skill, and state that it may edit the skill when it learns something. Use the skill for weeks before sharing it with a team. *When:* Repeated personal workflows that are about to become team tooling.
- **Annotate a localhost preview to steer the agent** — Serve slides or an HTML artifact in the in-app browser, use the annotate tool on a specific element, and let the agent apply the comment. *When:* Iterating on visual outputs such as decks or one-pagers without rewriting prompts.
- **Model and reasoning tiering** — Use the newest model at low or medium reasoning for most work, and a faster lighter model (the Spark model) for simple computer-use tasks such as clicking through a form. *When:* Background automations where latency does not matter and token budget does.

## Numbers
- Speech is about 3x faster than typing, according to the speaker ([6:50](https://youtu.be/il1c1a2FufU?t=410))
- A thread five weeks old with about 400 subagents still works (anecdote) ([2:37](https://youtu.be/il1c1a2FufU?t=157))
- Some users run a couple of billion tokens a day (speaker's observation) ([1:12](https://youtu.be/il1c1a2FufU?t=72))
- The check-notes skill has been used about 150,000 times on the speaker's OpenAI profile, though he has not invoked it by name in 2-3 months ([1:03:53](https://youtu.be/il1c1a2FufU?t=3833))
- The speaker's demo setup spans about 16 repos that are not separate sidebar projects ([19:12](https://youtu.be/il1c1a2FufU?t=1152))
- Anecdote: a /goal run rewrote the Python rich terminal library in Rust and UV in TypeScript, reported at about 100% test coverage. The speaker says this is not advice for work ([40:45](https://youtu.be/il1c1a2FufU?t=2445))
- Anecdote: a heartbeat monitored an Amazon wait-list, polling every 5 minutes then every minute; the speaker reports the outcome as a refund (about $400 back on the card) ([1:13:18](https://youtu.be/il1c1a2FufU?t=4398))

## Hot takes
- The advice to start a new thread after about 20 messages, or for every feature or code review, is no longer true because of compaction.
- Typed text input is becoming the wrong interface; voice should be the default for talking to agents.
- X-high reasoning is a misconception for most work; low or medium on the newest model is enough.
- An AI champion's real metric is how often teammates use the skills and plugins they built.
- Auto-review permissions plus an agents.md rule file have felt safer than full-auto mode in his experience.

## Tools mentioned
Codex app, Codex CLI, Codex in-app browser, computer use, Chrome extension, Slack connector, Gmail connector, Google Drive connector, Notion, Linear, Obsidian, GitHub, iMessage, iOS remote control, skills.sh, git

## Relevance to our work
- **prosharness** (3/3): The loop, goal and heartbeat patterns map directly onto ProsHarness loops and schedules. The verifier-based stop condition and the editable goal file fit checkpoint/resume of long runs. The phone-driven approvals match the remote-control pattern the speaker describes. → *Add a goal file that the loop re-reads each iteration, with a verifier command as the stop condition, and a work-log file that a cheap model can summarise for multi-day runs.*
- **agentos** (2/3): SkillForge's open question is a success signal for skills. The talk offers a practitioner proxy: skills the user corrects in place and then keeps using for weeks. It gives no measured eval. → *Record each user correction or self-edit to a skill as telemetry, and test whether repeated uncorrected use predicts later sharing, as a candidate success signal for SkillForge.*
- **general** (2/3): The stop-condition phrasing for scheduled checks and the low-thinking default are cheap ways to cut token spend on Claude Code loops. The talk gives no measured numbers for either. → *Add a 'reply NO UPDATES if nothing changed' stop condition to one recurring loop prompt, and compare token use over a week against the same loop without it.*
