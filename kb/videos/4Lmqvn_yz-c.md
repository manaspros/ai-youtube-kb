# Postgres Just Got It's Biggest Upgrade In Years

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `4Lmqvn_yz-c` · [watch](https://youtu.be/4Lmqvn_yz-c) · **date:** 2026-08-02 · **length:** 6:13 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Warren · **orgs:** Better Stack, Microsoft
- **topics:** agent-architecture, dev-tools · **tags:** postgres, durable-execution, durable-functions, workflows, scheduling, human-in-the-loop, pg-durable, docker-compose, sql

> Better Stack walkthrough of PG Durable, a Microsoft open-source Postgres extension for crash-proof durable functions, scheduling, retries and human-in-the-loop approval in plain SQL.

## Summary
The video introduces PG Durable, an open-source Postgres extension from Microsoft that persists workflow steps to disk so long-running jobs survive database restarts. Workflows are written as a graph of steps in a SQL DSL and submitted with df.start, which returns an 8-character id that can be checked with df.status or read with df.results. Built-in operators cover sequencing, parallel execution, racing, looping, conditionals, variable assignment, signal waits and cron-style waits (df.waitForSchedule). The demos show a loop that refreshes a materialized view on a one-minute schedule with no external scheduler, and an order-approval workflow that parks for up to 24 hours until df.signal wakes it. A Docker Compose setup runs the Microsoft image on Postgres 17 with shared_preload_libraries set to pgdurable. The speaker claims a 300-line SQL boilerplate example on the project site shrinks to seven lines, with retries and error handling handled by the extension. The video is a short, demo-led overview; it does not test crash recovery, scale or operational cost.

## Key ideas
- **Durable functions persist every step to disk, which gives crash and restart guarantees a plain BEGIN/COMMIT block or cron job does not.** — The speaker contrasts durable steps with a transaction or cron job: database crashes, restarts, long waits and failures are handled inside Postgres, with no external workflow service. ([0:00](https://youtu.be/4Lmqvn_yz-c?t=0))
- **Workflows are submitted from SQL with df.start and tracked by id.** — df.start returns an 8-character id. df.status reports operation state and df.results returns the final output once complete. A trivial SELECT wrapped in df.start shows the pattern. ([1:07](https://youtu.be/4Lmqvn_yz-c?t=67))
- **Scheduling without an external service is built from a loop of sequenced steps.** — The demo wraps a loop around a sequence: wait one minute, then call a procedure that refreshes materialized views and inserts a row into a log table. The job keeps firing for as long as the database runs it, and the demo shows three log rows after a few minutes. ([2:28](https://youtu.be/4Lmqvn_yz-c?t=148))
- **Human-in-the-loop approval is a parked workflow that a signal wakes.** — The order workflow selects the top order into a variable, waits up to 24 hours for a signal stored in a second variable, then uses an if to set the order to approved or rejected. The first process exits once df.signal is called from a separate approval script. ([3:32](https://youtu.be/4Lmqvn_yz-c?t=212))
- **Built-in operators replace hand-written queue, worker and retry code.** — Operators cover sequence, parallel (ampersand), race (fastest result wins), loop, if, wait-for-signal and wait-for-schedule. Error handling and retries are described as automatic, not user-coded. ([4:44](https://youtu.be/4Lmqvn_yz-c?t=284))
- **Local setup is a single Postgres 17 container with the extension preloaded.** — The compose file uses the Microsoft PG Durable image on Postgres 17 and sets shared_preload_libraries to pgdurable. The rest of the config is standard and can be changed freely. ([4:44](https://youtu.be/4Lmqvn_yz-c?t=284))

## Techniques
- **Run a recurring job inside Postgres** — Submit SELECT df.start(...) wrapping a loop operator around a sequence: a one-minute wait, then a procedure call (the demo calls a refresh-materialized-views procedure that inserts into a refresh_log table). Keep the start script running; the workflow persists and fires on the schedule. Check progress with a SELECT on the log table ordered by id. For cron-style timing, the speaker names df.waitForSchedule. *When:* Replacing an external cron, queue or scheduler for in-database maintenance jobs such as refreshes, rollups or cleanup.
- **Park a workflow until a human approves** — Workflow: SELECT the next pending record into a variable; sequence a wait for an approval signal with a 24-hour timeout, stored in a second variable; use an if to set status to approved or rejected based on the signal and timeout. Approval side: call df.signal with the workflow id and the decision payload. The original df.start process exits once the signal arrives. *When:* Approval gates where the process must not hold a connection or worker while waiting, such as order approvals or review steps.
- **Fan out and fan in** — Combine operations with the ampersand operator to run them in parallel, then sequence a final step (the demo refreshes a dashboard after three parallel operations). The exact DSL syntax for each operator is not shown on screen; see the project docs linked in the description. *When:* Several independent refresh or fetch steps followed by one dependent step.
- **Local dev via Docker Compose** — Use the Microsoft PG Durable image (Postgres 17). Add shared_preload_libraries=pgdurable under command, keep other settings default, and start the container. Run the example scripts from npm (the demo uses npm run workflow) against it. *When:* Trying PG Durable locally before deciding whether to adopt it.

## Numbers
- Durable function ids are 8 characters, returned by df.start. ([1:07](https://youtu.be/4Lmqvn_yz-c?t=67))
- Approval wait times out after 24 hours. ([3:32](https://youtu.be/4Lmqvn_yz-c?t=212))
- Demo schedule fires every minute; three log rows were visible after a few minutes of running. ([2:28](https://youtu.be/4Lmqvn_yz-c?t=148))
- Site example claims a 300-line SQL boilerplate (queues, workers, polling, retries, state tracking) reduces to seven lines with PG Durable. ([4:44](https://youtu.be/4Lmqvn_yz-c?t=284))
- Docker image runs Postgres 17. ([4:44](https://youtu.be/4Lmqvn_yz-c?t=284))

## Hot takes
- The 300-to-7-line reduction is a claim from the project site, shown as a slide, not a measured result in the video.
- The video calls the workflows crash-proof and describes retries as automatic, but it does not demonstrate a crash, a retry or a failure.
- Running long workflows inside the database may trade app-tier scaling for DB load; the video does not discuss this.
- Overview quality is decent for a short demo-led intro, but it is a product walkthrough of a Microsoft project with no sponsor disclosure and no comparison to pgmq, Temporal or similar.

## Tools mentioned
PG Durable (pgdurable, Postgres extension, Microsoft, open source), PostgreSQL 17, Docker Compose, npm (demo scripts)

## Relevance to our work
- **prosharness** (2/3): Checkpoint/resume of long agent runs and phone-driven approvals map directly onto parked workflows woken by a signal, and waitForSchedule maps onto ProsHarness loops and schedules. → *Compare PG Durable's park-and-signal approval pattern with ProsHarness's checkpoint/resume and phone approval flow, and note what a Postgres-backed checkpoint store would need (state schema, signal payload, timeout behavior).*
- **agentos** (1/3): Durable state, signal-based resume and in-DB scheduling overlap with the storage layer (Postgres, Redis) and any long-running agent job handling, but AgentOS does not currently need a database-hosted workflow engine. → *Test PG Durable's signal and wait-for-schedule operators against a long-running agent job locally before deciding whether a durable-execution layer belongs in the storage tier.*
