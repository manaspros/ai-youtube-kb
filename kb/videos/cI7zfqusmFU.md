# Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `cI7zfqusmFU` · [watch](https://youtu.be/cI7zfqusmFU) · **date:** 2026-09-18 · **length:** 20:50 · **format:** demo · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Giselle van Dongen · **orgs:** Restate
- **topics:** agent-architecture, infra-cost-scaling, multi-agent · **tags:** durable-execution, long-running-agents, virtual-objects, human-in-the-loop, cancellation, push-invocation, serverless, replay, slack-bot, deep-research

> Giselle van Dongen (Restate) argues long-running agents need a durable infrastructure layer, and demos journaled retries, human-approval suspension, keyed sessions and mid-run signal or cancel.

## Summary
The speaker argues that agents are becoming long-running, stateful, distributed processes, and that agent SDKs help with POCs but leave retry, recovery and cross-service plumbing to the team. She presents Restate, an open-source durable-execution server that sits in front of a service, proxies requests, and records each side effect in a journal so a crashed run resumes at the failed step. A live demo runs a Slack deep-research agent (planner, parallel sub-agents, writer) with an injected tool error that is retried from the journal. The talk then shows durable promises for approvals that can wait weeks without consuming serverless compute, keyed virtual objects that queue one execution per session, and routing of follow-up messages into a running agent as a signal or a cancel. It closes with the push-based invocation design and an event-log architecture inspired by Meta's event infrastructure. Most claims are demo-backed, but the talk is vendor-led and the latency figure is a single unbenchmarked claim.

## Key ideas
- **Agents are moving from request-response calls to persistent, asynchronous, long-running processes, so the infrastructure must change too.** — The speaker frames three waves, quoting Karpathy: chat website, then local app with tools, then persistent async entities in infrastructure. Agent SDKs are fine for POCs but do not handle distributed retry and recovery. ([0:12](https://youtu.be/cI7zfqusmFU?t=12))
- **Durable execution by journal: each side effect is recorded, so a crashed run replays to the failure point instead of restarting.** — Restate sits as a separate server in front of the service, proxies the request, and holds an open connection to the agent. The agent sends events to the journal; after a failure the journal is replayed. The speaker says this turns an ordinary function into a long-running, stateful one. ([3:31](https://youtu.be/cI7zfqusmFU?t=211))
- **The demo shows recovery from a real failure: a web search failed because the API was down, was retried, and the run completed without repeating earlier LLM calls.** — Tool errors were injected on purpose. The journal showed the planner LLM call, then the sub-agent's LLM call, then a failed search and its retry. The point is that progress is kept, not restarted. ([5:43](https://youtu.be/cI7zfqusmFU?t=343))
- **Human approval can be a durable promise that suspends the function; on serverless it uses no execution time while waiting.** — A promise is written into the journal, a Slack button asks the human, and the function resumes when the response arrives, even if the wait is weeks or spans redeploys. ([8:31](https://youtu.be/cI7zfqusmFU?t=511))
- **Workflows are the wrong model for persistent agents; a keyed virtual object (a stateful actor with an ID and isolated key-value state) fits better.** — Each session ID gets its own state, such as message history. Only one execution runs per key at a time, and a second message queues behind the first, so concurrent sessions do not overwrite each other. ([9:40](https://youtu.be/cI7zfqusmFU?t=580))
- **New user input can be routed into a running agent: an LLM classifies whether the message is relevant, then it is injected as a signal or the run is cancelled and restarted.** — Cancellation travels down the call chain, so sub-agents are cancelled before their parent and the stack unwinds. The speaker presents this as a rollback ability for agents. ([11:56](https://youtu.be/cI7zfqusmFU?t=716))
- **Turning the LLM call into its own service handler lets a team add a policy check and flow control in one place.** — Other agents call the LLM gateway over Restate's communication primitives. The example is a per-department cap of 300 concurrent LLM calls, which the speaker gives as an illustration, not a measured number. ([16:03](https://youtu.be/cI7zfqusmFU?t=963))
- **Push-based invocation, not worker polling, is the reason for low latency and serverless fit, and the server is one binary that snapshots to object storage for high availability.** — Restate pushes invocations to the service rather than having workers pull tasks. The speaker says this gives low latency and wakes serverless functions directly. Architecture is an event-driven distributed log plus an event loop, inspired by Meta's core event infrastructure. ([17:00](https://youtu.be/cI7zfqusmFU?t=1020))

## Techniques
- **Wrap every side-effecting agent step in a durable run call** — Put each LLM call, tool call or web search inside the durable step wrapper (restate.run in the Python SDK). Completed steps are read back from the journal on replay, so they are not re-executed after a crash. *When:* Any multi-step agent run that is costly or non-idempotent and must survive crashes that last hours or months.
- **Durable promise for human-in-the-loop approval** — Create a durable promise stored in the journal, send the approval request (the demo used a Slack button), and suspend. The function resumes when the callback resolves the promise. *When:* Approvals that may take days or weeks, or any run on serverless where idle waiting should cost nothing.
- **Keyed virtual object per session for serialized agent state** — Use the session ID as the key. Store chat history in isolated key-value state. The runtime queues a second request for the same key until the first finishes. *When:* Chat-style agents with many concurrent sessions where two messages must not overwrite each other's state.
- **Classify mid-run input, then signal or cancel-and-restart** — When a new message arrives during a run, have an LLM decide whether it is relevant. If so, inject it as a signal into the running loop. If not, cancel the run; cancellation propagates to sub-agents, then the parent. *When:* Users who send follow-up or corrective messages while a long research or coding agent is still working.
- **Central LLM gateway as its own durable handler** — Move LLM calls out of the agent code into a separate handler that runs policy checks and flow control (for example, per-team concurrency caps) and is called by agents through the runtime's communication primitives. *When:* An organisation has many agents that share model access and needs one place for budgets, rate limits and model swaps.

## Numbers
- Three waves of LLM use (chat site, local tool-using app, persistent asynchronous agents), as quoted from Karpathy. ([0:12](https://youtu.be/cI7zfqusmFU?t=12))
- Restate has six SDKs and integrations with most popular agent frameworks. ([18:25](https://youtu.be/cI7zfqusmFU?t=1105))
- Claimed p99 latency of about 45 ms for a 10-step workflow with push-based invocation (vendor claim, no benchmark shown). ([18:25](https://youtu.be/cI7zfqusmFU?t=1105))
- Example cap of 300 concurrent LLM calls for one department via the gateway (illustrative, not measured). ([16:03](https://youtu.be/cI7zfqusmFU?t=963))
- Scale is described as thousands of concurrent agent sessions, with one execution per session key at a time (no measurements). ([10:52](https://youtu.be/cI7zfqusmFU?t=652))

## Hot takes
- Agent SDKs are good for proofs of concept but do not solve distributed retry, recovery and connection of parts across an organisation.
- A workflow is the wrong model for a persistent agent. A stateful keyed object is the better fit.
- Pushing invocations to services beats workers polling a workflow server, for latency and for serverless.

## Tools mentioned
Restate, Slack, LiteLLM, Python

## Relevance to our work
- **prosharness** (2/3): ProsHarness already checkpoints and resumes long Claude Code runs and has phone-driven approvals. The talk gives a concrete journal-replay model and a suspend-on-approval pattern that could replace or harden that resume logic. → *Read the Restate Python SDK docs on durable steps and durable promises, then prototype one ProsHarness approval gate as a suspended promise to compare with the current checkpoint file approach.*
- **agentos** (1/3): AgentOS is a proxy for agent traffic with budgets and an audit log, but has no durable journal for agent runs. The talk is only tangential prior art for resumable runs. → *Read the Restate architecture notes (event-driven log, journal replay) as prior art before designing a resumable run layer in AgentOS.*
