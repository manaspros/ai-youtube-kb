# From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `9HbzAWnKbo4` · [watch](https://youtu.be/9HbzAWnKbo4) · **date:** 2026-08-18 · **length:** 20:36 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Jason Lopatecki · **orgs:** Arize, Anthropic, Uber, Booking, Daytona
- **topics:** observability, software-factory, evals, sandboxing-execution · **tags:** self-improving-agents, signal-to-pr, online-evals, llm-as-judge, trace-driven-debugging, skill-design, vpc-deployment, arize-ax, phoenix, pyroscope

> Arize's founder demos Signal, a background agent that reads production traces and logs, drafts an issue or fix with evidence, and hands it to a human reviewer, with the loop run in a sandbox.

## Summary
Jason Lopatecki (founder of Arize) argues that observability is shifting from humans clicking dashboards to agents consuming telemetry, and that traces tell an agent which code path ran. He describes an inverted loop where an event or a schedule starts an agent that gathers context through skills, writes the data into the repo as files, and opens an issue or a fix before a human looks. The human role moves from responder to reviewer, and the bottleneck becomes confidence that a fix is right. He says teams should trace and log far more data, since agents can sift through noise that humans cannot. He demos Signal, an Arize product that runs in its AX SaaS or in a customer VPC, with a pluggable harness (Claude Code, Cursor), a pluggable sandbox (Arize's, Daytona), and user-chosen skills and prompts. On skill design he says the hard part is getting the right data into a file format first, then composing narrow skills, and he says simply pointing Claude at raw data is not enough. He ends with online LLM-as-judge evals layered on production traces, where each recurring failure becomes an evaluator. The talk is a vendor pitch in places, but the loop design and skill-design advice are concrete.

## Key ideas
- **Telemetry is the input that makes agent debugging possible** — Traces show which code path actually ran. Without them, an agent is guessing among many possible paths. Speaker frames telemetry as the smoke an agent follows to a fix. ([2:38](https://youtu.be/9HbzAWnKbo4?t=158))
- **Invert the loop: the agent surfaces the issue, the human reviews** — Instead of a human spotting a problem and an agent fixing it, a background agent files an issue with evidence before anyone looks. Humans shift from grabbing tickets to driving the later investigation steps. The bottleneck is now confidence that a fix is correct, not producing it. ([4:03](https://youtu.be/9HbzAWnKbo4?t=243))
- **Every loop has a trigger, gathered context, and an output** — A periodic timer (for example every 5 minutes) or an event (for example an error) starts the run. Skills then pull context: traces first, plus logs, plus the repo. The output is an issue or a fix. ([5:24](https://youtu.be/9HbzAWnKbo4?t=324))
- **Run the local workflow in a sandbox, triggered by events** — Speaker's advice: get the agent working on a laptop first, then move the same workflow into a sandbox that an observability event can start. Teams want isolated, repeatable runs. ([6:35](https://youtu.be/9HbzAWnKbo4?t=395))
- **Concrete example: a one-to-two line fix from a stream-cancelled error** — Their in-product agent Alex hit a stream-cancelled error while calling to-do updates. A background agent (Signal) put up an issue, and the proposed fix was small. Bigger fixes still need a human to finish them. The goal is a cold start that carries the evidence. ([8:55](https://youtu.be/9HbzAWnKbo4?t=535))
- **Trace and log far more, because agents can read the noise** — Speaker expects teams to trace and log roughly 10 times more than now. Humans cannot dig through that volume, but an agent running a loop can use it to know what path the software took. ([10:17](https://youtu.be/9HbzAWnKbo4?t=617))
- **Skill design decides whether auto-fix works** — The key work is getting the right data first, such as a group of traces for one session, written into the repo as a file. Then give the agent composable skills, for example one that finds memory issues or one that cohorts by customer. Speaker says this is more than pointing Claude at the data. ([16:51](https://youtu.be/9HbzAWnKbo4?t=1011))
- **Online evals turn production failures into standing checks** — LLM-as-judge evals run on production traces. Each recurring failure, such as a prompt injection or a bad response, gets an evaluator so it is caught next time. Eval scores are attached to the trace, and the agent reads them through skills. Judges can run across the full dataset, not just samples. ([18:59](https://youtu.be/9HbzAWnKbo4?t=1139))

## Techniques
- **Trace-to-file skill** — A skill pulls the relevant traces, logs, or temp files (for example for one session) and writes them into the repo as files. The coding agent then reads them with ordinary file tools alongside the code. *When:* When a coding agent must debug production behaviour. Speaker says harnesses work well with files, and some of their files reach about 10 MB.
- **Event- or schedule-triggered agent loop** — An observability event (an error) or a periodic timer starts a run. The run gathers context via skills and outputs an issue or a draft fix, not a merged change. *When:* When you want continuous background checks on production without a human starting each investigation.
- **Composable narrow skills over raw data** — Build several small skills, each with a clear entry point, such as find memory issues, use facets, or cohort by customer, instead of one general skill over raw logs. *When:* When the agent needs to investigate varied failures and the raw data is too large to hand over whole.
- **Sandbox per run, pluggable harness** — Run the same harness you use locally (Claude Code or Cursor) in an isolated sandbox. Use Arize's sandbox, Daytona, or a managed agent service, and deploy in a customer VPC so production connections stay in the customer's network. *When:* When production data cannot leave the company network, or when runs must be isolated and reproducible.
- **Failure-to-evaluator loop** — When a failure repeats, write an LLM-as-judge evaluator for it, run it online against production traces, and record the scores on the trace. The agent later reads those scores as extra evidence. *When:* When a failure type recurs and you want it caught automatically, and when judge cost is acceptable at full-traffic scale.

## Numbers
- Speaker expects teams to trace and log about 10 times more data than they do today (his rough estimate, not measured) ([10:17](https://youtu.be/9HbzAWnKbo4?t=617))
- Some files the skills write into the repo are about 10 MB ([16:51](https://youtu.be/9HbzAWnKbo4?t=1011))
- Arize's customers include large companies such as Uber and Booking, which deploy in the customer VPC ([13:58](https://youtu.be/9HbzAWnKbo4?t=838))
- Speaker says the first version of their own in-product agent 'sucked', about two years before this talk, with no numbers given ([0:08](https://youtu.be/9HbzAWnKbo4?t=8))

## Hot takes
- Observability is moving from humans clicking dashboards to coding agents consuming telemetry.
- The bottleneck in agent-driven fixing is no longer producing the fix. It is confidence that the fix is right.
- Skill design, not pointing a coding agent at raw production data, decides whether auto-fix works.
- Teams should trace and log far more data, because agents can use volume that humans cannot.

## Tools mentioned
Arize AX, Arize Phoenix, Pyroscope, Claude Code, Cursor, Daytona, GitHub, Google Cloud logging skills

## Relevance to our work
- **agentos** (2/3): L4 observability and L2D SkillForge (mine agent telemetry into skills) match the talk's trace-to-skill loop. The talk's online-eval layer offers a candidate success signal for SkillForge. → *Prototype a skill that exports a slice of AgentOS proxy traces into repo files and check whether a coding agent can find a known failure path. Use this to test a success signal for SkillForge.*
- **prosharness** (2/3): ProsHarness already wraps Claude Code with loops, schedules, and checkpoints. The talk's event-triggered, sandboxed run that produces an issue, not a fix, matches that shape. → *Add an event-triggered mode to ProsHarness: an error event starts a checkpointed Claude Code run that writes an issue with trace evidence and stops for review.*
- **general** (1/3): Online LLM-as-judge evaluators built from each recurring production failure are a useful evals pattern for agents in general. → *Read Arize's online-evals material for how judge scores are attached to traces, then compare with our eval setup.*
