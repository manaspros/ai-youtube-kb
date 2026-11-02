# How I Learned to Stop Worrying and Love the Sandbox — Matt Brockman, E2B

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `fz6-NS7qpZc` · [watch](https://youtu.be/fz6-NS7qpZc) · **date:** 2026-10-06 · **length:** 59:33 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Matt Brockman · **orgs:** E2B
- **topics:** sandboxing-execution, infra-cost-scaling, agent-architecture · **tags:** sandbox, E2B, firecracker, snapshot-resume, templates, lifecycle-timeouts, orphan-processes, CTF-workshop, per-user-sandbox, filesystem-permissions, Claude Code, Codex, Nomad, Kubernetes

> E2B engineer runs a hands-on sandbox capture-the-flag, covering resource limits, snapshot/resume, templates, lifecycle timeouts, orphan processes, and per-user sandbox assignment.

## Summary
Matt Brockman of E2B runs a live CTF workshop on sandboxes for agent-generated code. He explains why agents running locally or on a shared server need isolation, and how E2B snapshots memory and disk so a paused sandbox resumes exactly where it stopped. Templates are snapshots of a running VM, so one prepared state can be copied hundreds of times or forked for parallel experiments. The workshop levels cover CPU hogs, memory and disk exhaustion, lifecycle timeouts (long timeout while a command runs, short idle timeout afterwards), orphaned background processes, per-user sandbox mapping, and read/write filesystem boundaries. Much of the talk is product walkthrough and recruiting, but the operational patterns are concrete and reusable. Open problems he names include storage pruning, GPUs (not supported), and whether sandboxes suit always-on services.

## Key ideas
- **Agent-generated code needs isolation from the host** — Agents running locally or on a shared server can use all CPU, spawn processes, delete files, and read environment variables and secrets. A sandbox limits this blast radius per user or per task. ([3:38](https://youtu.be/fz6-NS7qpZc?t=218))
- **Snapshot memory and disk, then resume instead of cold starting** — E2B pauses a sandbox by saving RAM and the filesystem, then resumes from that state. The speaker's argument is that an agent expects its world to be unchanged after a pause, so restoring exact state causes fewer errors. ([4:54](https://youtu.be/fz6-NS7qpZc?t=294))
- **Templates are snapshots of a running VM, not Docker build recipes** — Processes are started first and the running state is captured as the template. Each new sandbox resumes from that state, so the start command is already done. One template gave about 200 workshop participants identical copies. ([16:14](https://youtu.be/fz6-NS7qpZc?t=974))
- **Fork one state into parallel sandboxes for experiments** — For example, load a dataframe once, snapshot it, then fork five sandboxes that each try a different transformation in parallel. ([17:33](https://youtu.be/fz6-NS7qpZc?t=1053))
- **Use two timeouts: long while working, short when idle** — Set a long lifetime while a command runs, such as a 15-minute video job, then drop the timeout to about a minute once it returns. Idle sandboxes then pause or shut down to free capacity. This balances speed against cost, since paused sandboxes are cheap. ([31:30](https://youtu.be/fz6-NS7qpZc?t=1890))
- **Resumed sandboxes accumulate orphan processes, so cleanup is a core job** — Background processes started in an earlier session keep running when the sandbox is reused. Performance degrades over time. The speaker says much of sandbox management ends up being finding and killing orphans, and that you must track sandbox IDs so you do not lose them. ([38:24](https://youtu.be/fz6-NS7qpZc?t=2304))
- **Assign sandboxes to users with a map, not round-robin** — Keep a persistent user-to-sandbox-ID mapping so a user's repeated runs hit the same sandbox. The workshop kept this map in memory. In production, a database would hold users, active sandboxes, and history. ([44:22](https://youtu.be/fz6-NS7qpZc?t=2662))

## Techniques
- **Snapshot-and-resume sandboxes** — Pause the sandbox to save memory and disk when idle, then resume it on the next request. Use the resumed state rather than rebuilding from the image. *When:* Agent or user sessions return to the same environment after gaps, and state loss would cause agent errors.
- **Warm template with processes already running** — Start the needed services and processes in a VM, snapshot the running state as a template, then spawn copies from it. *When:* Many sandboxes need the same expensive setup, or you want to share one prepared environment across many users or tasks.
- **Fork a sandbox for parallel experiments** — Prepare shared state once, snapshot it, then start several sandboxes from that snapshot and run a different variant in each. *When:* Trying several options on the same data or repo state at once.
- **Task-scoped lifetime with a short idle timeout** — Set a long lifetime for the command's run, then reset the sandbox timeout to a short value once the command completes so it shuts down or pauses soon after. *When:* Task duration is unknown, such as data processing or scraping, and idle sandboxes are costly.
- **Orphan process inventory and reaping** — List running processes in a reused sandbox, identify orphans from earlier runs (the workshop searched for them by name), and kill them before the next task. Check the count after each run. *When:* Sandboxes are reused across requests, so leftover background processes build up.
- **Per-user sandbox assignment map** — Keep a mapping from user ID to sandbox ID. On request, return the mapped sandbox if it exists, otherwise create one and record it. Test the assignment logic with mocked sandboxes. *When:* Users need continuity across requests, and round-robin assignment would scatter their state.
- **Separate read-only and writable paths** — Declare a read-only cache for built templates and a separate writable runtime cache, and point writes only at the runtime cache. Put the same rules in the agent instruction file (agents.md). *When:* An agent should not write to parts of the filesystem that hold shared or trusted content.
- **Egress rules when secrets are present** — If a sandbox holds real secrets, restrict the network destinations it can reach. Dev-only keys reduce the need for strict rules. *When:* Sandboxes run code that could exfiltrate credentials.

## Numbers
- Target sandbox startup time under 100 ms, so many can run concurrently (a stated aim, not a measured result). ([3:38](https://youtu.be/fz6-NS7qpZc?t=218))
- Workshop created about 200 copies from one snapshotted template. ([16:14](https://youtu.be/fz6-NS7qpZc?t=974))
- A runaway process was using 99.7% of CPU in the first lab. ([19:00](https://youtu.be/fz6-NS7qpZc?t=1140))
- Disk-fill lab used a 512 MB diskfill.bin file in /tmp. ([27:12](https://youtu.be/fz6-NS7qpZc?t=1632))
- Lifecycle lab: command lifetime set to 1 hour, then reset to a 1-minute idle timeout after the task finishes. ([34:16](https://youtu.be/fz6-NS7qpZc?t=2056))
- Orphan lab: started with 3 orphaned processes, reduced to 2, then cleared to 0 by killing the remaining ones. ([40:38](https://youtu.be/fz6-NS7qpZc?t=2438))

## Hot takes
- Agents do not know time has passed while paused, so restoring exact memory and disk state produces fewer errors than rebuilding.
- Managing sandboxes at scale ends up mostly being orphan-process cleanup.
- Sandboxes are a poor fit for persistent, always-on services; a traditional server or CDN is cheaper for those.
- Do not let the AI write the code without reviewing what it does.

## Tools mentioned
E2B, Firecracker, Nomad, Kubernetes, Claude Code, Codex, Python SDK, JavaScript SDK

## Relevance to our work
- **agentos** (2/3): AgentOS Crucible (L2C) is opt-in sandboxed code execution; this talk gives concrete lifecycle, orphan-cleanup, and template patterns for that layer. → *Add a Crucible lab-style test: a sandbox that runs a long task, then idles, checking that the long timeout is reset to a short idle timeout afterwards and that orphan processes are counted and killed before reuse.*
- **prosharness** (2/3): ProsHarness checkpoint/resume of long agent runs; E2B snapshots both memory and filesystem for resume, which is the same problem. → *Compare ProsHarness checkpoint design against memory-plus-disk snapshot: record whether a checkpoint restores running processes as well as files, and whether state is safe to resume after a gap.*
- **general** (1/3): Per-user sandbox assignment and read/write path rules are general agent-infrastructure patterns, but the talk is light on measured detail.
