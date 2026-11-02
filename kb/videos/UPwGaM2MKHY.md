# The Log Is The Agent - Ishaan Sehgal, Omnara

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `UPwGaM2MKHY` · [watch](https://youtu.be/UPwGaM2MKHY) · **date:** 2026-07-18 · **length:** 15:11 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ishaan Sehgal · **orgs:** Omnara
- **topics:** agent-architecture, context-engineering, observability · **tags:** event-sourcing, append-only-log, durable-execution, agent-state, resumability, compaction, session-log, vendor-lock-in, managed-agents

> Argues an agent's identity is its append-only event log, not the model or runtime; once workers are disposable, reliability, forking, sharing and ownership follow from the log design.

## Summary
Ishaan Sehgal of Omnara argues that an agent is its durable log, not its model, runtime or sandbox, using a video game save file as the analogy. The log is the append-only history of user inputs, model outputs, tool calls and results, permissions and failures. Each worker reads the log, advances the agent one step, appends the result and can then disappear, so any other worker can resume. Context windows, UIs, audit trails and compaction are all projections of that log. He concedes compaction is lossy and recommends keeping the raw log and treating a compaction as a forked log. He says the log records the agent's view of the world, not the world, so external side effects such as sent emails are not undone by a fork. Claimed benefits are reliability (a pending permission prompt survives a crashed process), scalability (one process advancing many agents), forking across models, multiplayer sharing by access grant, and migration as an adapter problem. He criticises current harnesses for treating logs as a side effect (fire-and-forget JSONL writes, SQLite corruption issues), and argues log lock-in is deeper than model lock-in because managed providers would own the agent by owning its log. The talk closes with a pitch for Omnara's open-source managed agents platform, and gives no benchmarks.

## Key ideas
- **The agent's identity is its data, specifically its log, not the model or the runtime** — Speaker uses a Skyrim save file analogy: the console can burn down and the character survives in the save. The model and runtime are interpreters of the log. ([0:00](https://youtu.be/UPwGaM2MKHY?t=0))
- **The log is an append-only event history of every state transition** — It includes user inputs, model outputs, tool calls, tool results, permissions and failures. Every operation is either reading the log or appending to it. ([1:22](https://youtu.be/UPwGaM2MKHY?t=82))
- **Workers should be disposable; the loop reads the log, takes one step, appends, and exits** — A simplified loop reconstructs state from the log, calls the model, appends the response, runs any requested tool, appends that result and repeats. Any worker can pick the session up later. ([2:49](https://youtu.be/UPwGaM2MKHY?t=169))
- **Context, UI, debugging, auditing and compaction are all projections of the log** — Like a materialised view over a database, each of these is derived from the durable log, and the log itself is not a projection. ([4:12](https://youtu.be/UPwGaM2MKHY?t=252))
- **Compaction is lossy, so keep the raw log and treat a compaction as a forked log** — A compacted summary throws information away. If you keep the raw log you can regenerate new projections; if you discard it you have lost part of the agent. ([5:17](https://youtu.be/UPwGaM2MKHY?t=317))
- **The log records the agent's view of the world, not the world itself** — Forking back does not unsend an email or undo a file change made outside the log. The log can resume identity and context but cannot make the outside world deterministic. ([6:11](https://youtu.be/UPwGaM2MKHY?t=371))
- **Reliability and scale fall out of treating the log as the primary state** — A pending permission prompt should survive a dead process and reappear on resume. One process can advance many agents because state is rebuilt from the log each turn, which makes failover and scaling simple. ([7:25](https://youtu.be/UPwGaM2MKHY?t=445))
- **Current harnesses treat the log as a side effect, and that is the problem** — He cites JSONL writes that are fire-and-forget in Claude SDK mode, SQLite corruption reports in OpenCode, and sharded durable objects that make history hard to reconstruct. ([9:51](https://youtu.be/UPwGaM2MKHY?t=591))
- **Log lock-in is deeper than model or API lock-in** — Models, runtimes and machines are replaceable. If a provider owns the log, it effectively owns the agent, which is his argument against managed agent offerings. ([11:07](https://youtu.be/UPwGaM2MKHY?t=667))

## Techniques
- **Log-first agent loop** — Store every user input, model output, tool call, tool result, permission request and failure as an appended event. Each turn, rebuild state by reading the log, call the model, append its output, run tools, append results. Do not hold state in the process. *When:* Long-running or multi-step agents that must survive worker crashes, restarts or timeouts.
- **Persist pending permissions as events** — Write the permission request into the log before blocking on it, so a fresh worker that reconstructs the session shows the same pending prompt rather than silently dropping it. *When:* Agents that pause for human approval and may be resumed later or on another machine.
- **Projections over one record** — Keep one raw durable log and generate context windows, UI views, audit trails and debug views from it on demand, instead of maintaining each as its own source of truth. *When:* You need several views of the same agent history (model input, UI, audit, debugging) without them drifting apart.
- **Compaction as forked log** — When the context window fills, write a summarised log as a new branch that references the raw log, and keep the raw log intact for regenerating other projections. *When:* Sessions outgrow the model's context window but you still need the full record.
- **Fork at a point in the log** — Copy history up to a chosen event and continue on a different model or strategy as a new branch. *When:* Comparing models on the same starting state, or trying a different provider mid-session.
- **Share by access grant, not transcript copy** — Give a teammate or observer read or edit access to the session log instead of exporting a transcript. *When:* Handing an agent session to a colleague or letting a manager watch without taking over.

## Numbers
- One process can advance thousands of agents when state is rebuilt from the log each turn (speaker's claim, no benchmark shown) ([7:25](https://youtu.be/UPwGaM2MKHY?t=445))
- Talk length 15:11; no latency, cost or reliability benchmarks are presented ([0:00](https://youtu.be/UPwGaM2MKHY?t=0))

## Hot takes
- The agent is its log, not the model or the runtime.
- Log lock-in is a deeper lock-in than model or API lock-in, and managed agent providers want to own the log.
- Current agent harnesses treat the session log as an afterthought, and that is a reliability problem.
- Permission prompts should survive a crashed process and reappear on resume.

## Tools mentioned
Claude Code, Codex, OpenCode, Claude SDK, Cloudflare Durable Objects, SQLite, JSONL

## Relevance to our work
- **agentos** (2/3): AgentOS already plans durable storage (Postgres, Redis, Timescale) and cross-session memory; the talk's append-only session log with projections for context, audit and resume maps onto that design. → *Prototype one AgentOS agent session as an append-only event table in Postgres (input, model output, tool call, tool result, permission, failure), derive the model context from it, and test resume by killing the worker mid-tool-call.*
- **prosharness** (2/3): ProsHarness does checkpoint and resume of long Claude Code runs and phone-driven approvals; the talk's examples of a permission prompt lost on resume and a fire-and-forget write path are concrete failure cases to test the checkpoint format against. → *Add a resume test that kills the run while a permission prompt is pending and checks the prompt reappears on restart; also confirm checkpoint writes are acknowledged rather than fire-and-forget.*
- **general** (1/3): Speaker's critique of Claude Code and Codex writing session state as fire-and-forget JSONL applies to any harness we run on top of those tools. → *Read how Claude Code writes its session JSONL and whether a write failure can silently lose a session before relying on it for resume.*
