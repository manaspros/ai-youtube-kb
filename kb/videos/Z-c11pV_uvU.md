# Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Z-c11pV_uvU` · [watch](https://youtu.be/Z-c11pV_uvU) · **date:** 2026-08-18 · **length:** 20:08 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Frank Coyle · **orgs:** UC Berkeley, Anthropic
- **topics:** agent-architecture, claude-code, context-engineering, multi-agent · **tags:** Claude Certified Architect, CCA exam, stop_reason, tool-use loop, subagents, context isolation, compaction, CLAUDE.md, Claude Code CI, batch API, anti-patterns, certification

> Frank Coyle (UC Berkeley) walks through the Claude Certified Architect exam's scenarios and uses each one's anti-patterns to teach agent loops, subagent context isolation, compaction, and non-interactive runs.

## Summary
Coyle, a long-time CS teacher, introduces the Claude Certified Architect (CCA) exam, released in March as a timed, proctored, scenario-based test that individuals can take for $99 once every six months. He says the five exam domains are agentic architecture (27%), Claude Code configuration and workflow (20%), prompt engineering with structured output, tool design with MCP, and context management and reliability. The exam draws four of six production scenarios at random, and he organizes the talk around them, pairing each with anti-patterns. He argues that knowing what not to do is the fastest route to correct designs, and he uses the old structured-programming result (sequence, selection, iteration) to frame the agent loop as the core primitive. The concrete advice covers stop-reason handling in a tool-use loop, hierarchical CLAUDE.md files, narrow single-purpose subagents that receive only their slice of context, forking subtask output back as summaries, compacting when context passes a token threshold, and running Claude Code non-interactively in CI with batch pricing for offline work. Much of the talk is a high-level exam overview rather than measured results, and several claims are unverified, including the compaction threshold and the batch details.

## Key ideas
- **Anti-patterns teach design faster than best practices** — The speaker's method is to show what not to do for each scenario, since knowing the failure modes leads to the right design. He ties this to the software design-pattern movement and says agents now have their own patterns and anti-patterns. ([2:03](https://youtu.be/Z-c11pV_uvU?t=123))
- **The LLM never runs tools; the loop does** — The model only emits a tool-use request with parameters. Application code executes the tool, appends the result, and calls the model again. He stresses that the model cannot act on its own. ([8:43](https://youtu.be/Z-c11pV_uvU?t=523))
- **Branch on stop_reason instead of trusting the first response** — tool_use means run the tool and continue the loop. A normal end means finish. A token-limit stop means the answer is partial and must be handled. He also suggests a human check on confidence before a result is accepted. ([4:48](https://youtu.be/Z-c11pV_uvU?t=288))
- **Loops are the core of agentic power** — He compares the agent loop to the sequence, conditional, and iteration primitives that the 1966 Böhm-Jacopini result showed are enough for general computation. In his view, the loop is what makes agent behavior powerful, though the framing is his own. ([7:17](https://youtu.be/Z-c11pV_uvU?t=437))
- **Hierarchical CLAUDE.md files control behavior by scope** — Anthropic recommends three levels of CLAUDE.md: project root, project subfolders, and directories beneath those. Together they form a rule hierarchy that shapes how Claude Code responds in each area. ([11:32](https://youtu.be/Z-c11pV_uvU?t=692))
- **Specialize subagents and do not overload them** — The anti-pattern is one agent with every tool. He prefers one job per agent with one or two tools, following the function rule that each function should do one thing. He also says not to fill the context window just because it is large. ([12:51](https://youtu.be/Z-c11pV_uvU?t=771))
- **Give each subagent only its slice of context to avoid groupthink** — His example for a critic agent passes the claim and the evidence but withholds the reasoning that produced the claim. He argues that shared reasoning causes agents to converge on one idea. ([14:18](https://youtu.be/Z-c11pV_uvU?t=858))
- **Fork subtask work and return only the summary** — Work such as log scanning runs in a forked context. Its tokens stay out of the main thread, and only the summary is added back. Letting every subtask dump full output into the main thread is the anti-pattern he names. ([15:52](https://youtu.be/Z-c11pV_uvU?t=952))
- **Compact on a token threshold and avoid interactive modes in pipelines** — He suggests compacting the context once it passes a set limit, which he gives as 150,000 tokens. Interactive mode stalls a pipeline by asking for permissions, so unattended runs should be configured to proceed without prompts. ([17:16](https://youtu.be/Z-c11pV_uvU?t=1036))

## Techniques
- **Stop-reason-driven agent loop** — Use a while-true loop that calls the model with the message history, checks stop_reason, runs any requested tool, appends its result, and stops only on a normal end. Handle the token-limit stop as a partial result. *When:* Any agent that calls tools and must not return a truncated or unverified answer.
- **Three-level CLAUDE.md hierarchy** — Put project-wide rules at the repo root, area-specific rules in project subfolders, and narrow rules in deeper directories so each level inherits and refines the one above. *When:* Large repos where different areas need different conventions for Claude Code.
- **Single-purpose subagents with minimal tools** — Give each subagent one narrow job and one or two tools, and keep its context to what that job needs. *When:* Multi-agent research or pipelines where a generalist agent gets confused or drifts.
- **Context slicing for critic and reviewer agents** — Pass a reviewing agent the claim and its evidence, but not the reasoning chain that produced the claim. *When:* Verification or critique steps where agents might otherwise agree with each other too easily.
- **Forked subtask context with summary return** — Run noisy subtasks, such as log scanning, in a separate context thread. Only the final summary goes back into the main context, and the subtask's intermediate tokens are discarded. *When:* Long coding sessions where tool output would otherwise crowd out the main task.
- **Threshold-triggered compaction** — Count tokens in the running context and run compaction when a set limit is reached. He mentions a 150k threshold and says custom compression logic can be written by extending a base class. *When:* Long-running sessions that would otherwise grow until quality or cost becomes a problem.
- **Non-interactive CI runs with batch processing** — Configure Claude Code to run without interactive permission prompts in pipelines. Send offline or overnight work through the batch interface for about 50% lower token cost, with results within 24 hours. *When:* CI jobs and bulk workloads that do not need a human in real time.

## Numbers
- Agentic architecture is 27% of the CCA exam, the largest domain he names. ([3:26](https://youtu.be/Z-c11pV_uvU?t=206))
- Claude Code configuration and workflow is 20% of the CCA exam. ([3:26](https://youtu.be/Z-c11pV_uvU?t=206))
- The exam costs $99 for individuals, who can take it once every six months. It is proctored, timed, and scenario-based, and was released in March. ([2:03](https://youtu.be/Z-c11pV_uvU?t=123))
- Six production scenarios are published, and the exam draws four at random. ([3:26](https://youtu.be/Z-c11pV_uvU?t=206))
- The speaker suggests compacting context once it passes 150,000 tokens (his example, not a documented threshold). ([15:52](https://youtu.be/Z-c11pV_uvU?t=952))
- Batch processing costs 50% fewer tokens, with results promised within at least 24 hours. ([18:48](https://youtu.be/Z-c11pV_uvU?t=1128))

## Hot takes
- Loops are not new. Structured-programming theory already showed that sequence, selection, and iteration are enough, and agents are bringing the loop back.
- A large context window is not a reason to fill it. More context means more cost and more confusion, so limit what goes in.
- Multi-agent groupthink is real, so each agent should get only its slice of the context, not the full reasoning chain.

## Tools mentioned
Claude Code, Claude API (messages, stop_reason, tool use), CLAUDE.md, MCP (Model Context Protocol), Message Batches API

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI for long runs, so the talk's points on non-interactive pipeline runs, subagent context slicing, and compaction apply directly. → *Audit ProsHarness's Claude Code invocations for interactive permission prompts that would stall unattended runs, and set them to run non-interactively.*
- **general** (2/3): Context engineering, subagent isolation, and the batch API for cheap offline work match recurring interests, though the talk is mostly an exam overview. → *Read the official CCA scenario guides for the subagent context-slicing and compaction patterns, and compare them with our current subagent handoff format.*
- **agentos** (1/3): The stop-reason and token-limit handling in the agent loop is relevant to any proxy or agent runtime that returns model output, but the talk does not cover proxies or infra. → *Check whether the AgentOS proxy and agent loop handle a max-token stop as a partial result, and add a test for it.*
