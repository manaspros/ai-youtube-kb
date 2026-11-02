# Claude Code Loop: The Feature Everyone Misunderstands

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Xxqu-kz00gw` · [watch](https://youtu.be/Xxqu-kz00gw) · **date:** 2026-04-02 · **length:** 5:46 · **format:** review · **quality:** 4/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Anthropic, Better Stack, OpenAI
- **topics:** claude-code, agent-architecture · **tags:** claude-code, loop, cron, scheduled-tasks, session-memory, claude-desktop, cowork, ralph-loop, openclaw

> Better Stack walks through Claude Code's new loop skill (repeat a prompt on an interval), argues it is for re-running tasks inside one session rather than a durable assistant, and lists its limits: 3-day auto-expiry and session-only storage.

## Summary
The video explains Claude Code's loop skill, which runs a prompt at a set interval (minutes, hours or days) and uses the cron-create machinery underneath. The presenter demonstrates a short interval prompt, a daily job at a clock time (interpreted in the machine's local time, not UTC), and listing and deleting jobs by description or ID. He notes jitter on scheduled fires so many jobs do not hit the API at the same moment. He argues the hype (Discord/Telegram assistants, Ralph loops, an OpenClaw replacement) outruns the feature because cron tasks auto-expire after three days and live only in session memory, so they vanish on a new session. His suggested use is re-running a check within one session when something changes, such as tailing a log for errors, counting a job queue, or checking for new issues. For durable jobs he points to the Scheduled option in Claude Desktop (runs while the machine is on and the app is open) and Scheduled in Cowork (runs in a sandbox, not the local filesystem), and mentions a third-party terminal plugin he has not tried.

## Key ideas
- **Loop is for re-running a task within one session, not a durable always-on assistant; the name was chosen deliberately over schedule.** — The presenter says the feature is hyped beyond its usefulness, and that using it for Discord/Telegram listeners or Ralph loops is a misuse. ([0:00](https://youtu.be/Xxqu-kz00gw?t=0))
- **Syntax is an interval plus a prompt; the minimum granularity is minutes, so seconds are not supported yet.** — Loop takes an interval in minutes, hours or days and a prompt, then creates a scheduled task through the cron create skill. ([0:00](https://youtu.be/Xxqu-kz00gw?t=0))
- **Clock-time schedules use the machine's local timezone, not UTC.** — The demo sets a daily recurring prompt for 6:30 PM and the presenter warns that local machine time is what counts. ([1:25](https://youtu.be/Xxqu-kz00gw?t=85))
- **Scheduled fires are jittered to avoid many jobs hitting the Anthropic API at once.** — An hourly job can fire anywhere from zero to six minutes past the hour. ([1:25](https://youtu.be/Xxqu-kz00gw?t=85))
- **Limit one: cron tasks auto-expire after three days.** — Designed to stop forgotten long-running tasks, but it breaks listener-style use that is expected to keep running. ([2:39](https://youtu.be/Xxqu-kz00gw?t=159))
- **Limit two: cron tasks live in session memory, not on disk, so a new session starts with none scheduled.** — He schedules two tasks, closes the session, and a fresh session lists nothing. For long Ralph-style runs this means relying on compaction rather than a clean reset. ([2:39](https://youtu.be/Xxqu-kz00gw?t=159))
- **Durable scheduling options exist outside the CLI loop.** — Claude Desktop's Scheduled sidebar runs while the computer is on and the app is open. Cowork's Scheduled runs in a sandbox rather than on the local filesystem, which matters for where tasks read and write. ([3:48](https://youtu.be/Xxqu-kz00gw?t=228))

## Techniques
- **In-session interval polling with loop** — Run loop with an interval (for example 3m) and a prompt. The prompt can do anything Claude Code can do: read a file, call MCP tools, invoke a skill. Example prompt from the video: write a tweet using a skill, run every three minutes. *When:* When you would otherwise re-run the same check by hand inside one session, such as tailing the last 50 lines of a continuously updating log for errors, counting items left in a job queue, or checking for new project issues.
- **Clock-time daily job** — Put a time of day in the loop request (the demo asks for 6:30 PM) and let it create a daily recurring task. Times are the machine's local time. *When:* When a same-session reminder or check should fire at a fixed local time each day.
- **List and delete scheduled jobs** — Ask Claude to list current cron jobs (it uses the cron list tool), then delete one by describing it or giving its ID. *When:* To audit or clean up in-session schedules before they expire on their own.
- **Durable schedules via Claude Desktop or Cowork** — In Claude Desktop, open the sidebar, choose Scheduled, and set name, description, prompt, model, permissions and frequency. Cowork has a separate Scheduled option with a different modal and a model picker behind extra clicks, and it runs in a sandbox. *When:* When a task must survive session restarts and the machine is on with the app open. Pick Claude Code for local-filesystem work and Cowork for sandboxed work.
- **Avoid loop for long-lived listeners or Ralph loops** — Do not hook loop to Telegram or WhatsApp listeners that must run for days, and do not use it as a session-reset-safe long run. Rely on a durable scheduler or an external harness for those. *When:* Whenever the job must outlive a session or three days.

## Numbers
- Cron tasks auto-expire after three days. ([2:39](https://youtu.be/Xxqu-kz00gw?t=159))
- Minimum loop granularity is one minute; seconds are not supported. ([0:00](https://youtu.be/Xxqu-kz00gw?t=0))
- Hourly scheduled jobs can fire anywhere from 0 to 6 minutes past the hour (jitter). ([1:25](https://youtu.be/Xxqu-kz00gw?t=85))
- Cron tasks are session-only; two tasks scheduled in one session were gone in the next session. ([2:39](https://youtu.be/Xxqu-kz00gw?t=159))

## Hot takes
- The loop feature is more hyped than useful, and it does not replace OpenClaw-style always-on assistants because of the 3-day expiry and session-only storage.
- Loop was named that way on purpose; schedule would have implied durability it does not have.
- Desktop and Cowork scheduled tasks are the right place for durable work, not the CLI loop.

## Tools mentioned
Claude Code, loop skill, cron create skill, cron list tool, Claude Desktop, Cowork, Claude Sonnet, Claude Haiku, OpenClaw, Telegram, WhatsApp, Discord, Ralph loop, Claude remote control, async hooks, GPT 5.4, third-party terminal scheduling plugin (author Kenneth, unnamed repo)

## Relevance to our work
- **prosharness** (2/3): ProsHarness already has loops and schedules around Claude Code. This video names the two failure modes (3-day expiry, session-only storage) that a durable schedule must avoid. → *Check ProsHarness's loops/schedules against the two limits shown here: confirm schedules persist to disk and survive session restarts, and that expiry is explicit rather than silent.*
- **agentos** (1/3): Recurring checks of queues, logs and error rates are a monitoring concern, but this feature is session-scoped and not a durable scheduler. → *If AgentOS needs recurring checks (queue depth, error tails), schedule them on persistent infrastructure, not the session-scoped loop. Use the 3-day expiry and session-memory limits as the requirements to design around.*
