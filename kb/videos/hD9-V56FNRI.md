# AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `hD9-V56FNRI` · [watch](https://youtu.be/hD9-V56FNRI) · **date:** 2026-09-18 · **length:** 19:48 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Salman Munaf · **orgs:** TikTok
- **topics:** agent-architecture, security-guardrails, observability, memory · **tags:** distributed-systems, idempotency, compensating-transactions, circuit-breaker, retry-storm, least-privilege, human-approval, agent-tracing, memory-as-cache, tool-contracts

> Talk arguing that once agents call tools and change state, they are distributed systems, so they need idempotency, compensation, scoped permissions, bounded retries and per-step traces.

## Summary
Salman Munaf (TikTok) argues that agents with tools are distributed systems, since their actions have side effects outside the model. He contrasts deterministic workflow coordinators with an LLM acting as a probabilistic coordinator, and says deterministic controls must bound what it can do. He walks the agent loop (plan, act, observe, persist, decide) and notes each step crosses a boundary with its own failure modes. The central failure case is a timeout, which means "unknown" rather than "failed", so tools need request IDs, idempotency keys and status lookups. He recommends persisting every step, defining compensation operations for irreversible actions, treating memory as a cache with provenance and invalidation, and capping turns, parallel calls, spend and retries with circuit breakers and backoff. He also argues for scoped credentials, approvals bound to exact parameters and expiry, and traces that capture prompts, retrieved context, tool I/O and approvals. The talk is conceptual and has no benchmarks, but the failure-mode framing is practical.

## Key ideas
- **Agents are distributed systems now because tool calls cause side effects outside the model.** — The architectural boundary moved past the LLM once agents can call APIs, change state and run loops. Each external system, state and credential the agent touches needs to be identified up front. ([2:44](https://youtu.be/hD9-V56FNRI?t=164))
- **An LLM agent is a probabilistic coordinator, so deterministic controls have to bound it.** — Classic services coordinated multi-step workflows deterministically with mapped decision trees. An agent's action space varies widely, so consequential actions need enforced limits rather than trust in the model. ([2:44](https://youtu.be/hD9-V56FNRI?t=164))
- **Persist every step of the agent loop so failed runs can be inspected and undone.** — The loop is plan, act, observe, persist, decide, and each step crosses a boundary (data read, external write, partial results, bad persisted data, retry storms). Persisting actions and retrieved context lets the agent identify where it failed and run undo operations. ([5:12](https://youtu.be/hD9-V56FNRI?t=312))
- **A timeout means unknown, not failed. Tools need idempotency keys and status lookup.** — Example: a refund tool times out and the agent can't tell whether the refund happened. Agents retry first, so request IDs and idempotency keys should make duplicate requests harmless, and a status lookup should report what a previous request did. ([7:38](https://youtu.be/hD9-V56FNRI?t=458))
- **Define a compensation operation for each side effect that can't be reversed.** — Cross-system workflows (ticket updated, email sent, CRM update fails) need a defined corrective step, such as an apology or correction email after a wrong message goes out. ([6:36](https://youtu.be/hD9-V56FNRI?t=396))
- **Treat agent context as state, and memory as a cache with provenance and invalidation.** — Context that can influence an action is state, and stale state can conflict with the source of truth. Short-term memory is the thread for one run. Long-term memory includes project files, system prompts, databases and caches. Decide which source wins on conflict, and invalidate memory when the source of truth changes. ([9:31](https://youtu.be/hD9-V56FNRI?t=571))
- **Bound the agent with circuit breakers, budgets and scoped credentials, and bind approvals to exact parameters.** — Use circuit breakers for unhealthy dependencies, exponential backoff, max turns, max parallel calls and max spend. Split read and write permissions, use tool allowlists, and avoid blanket approvals. An approval should cover a specific action, actor, timestamp and expiry. ([14:01](https://youtu.be/hD9-V56FNRI?t=841))
- **Logs are not enough. Trace the prompt, retrieved context, tool requests and responses, errors, writes and approvals.** — Teams need to reconstruct what the agent saw and why it acted. Model quality reduces mistakes but cannot remove network failures, stale data or adversarial input, so the system has to bound, observe and recover from actions. ([17:02](https://youtu.be/hD9-V56FNRI?t=1022))

## Techniques
- **Idempotency keys plus status lookup on every side-effecting tool** — Give each write or external call a request ID / idempotency key. Duplicate requests with the same key return the original result without repeating the side effect. Expose a status endpoint so the agent can check whether a timed-out request succeeded before retrying. *When:* Any tool that writes, pays, refunds, sends messages or otherwise changes external state, especially where timeouts or client retries are possible.
- **Persist each loop step and define compensation operations** — Log every plan, action, observation and write with its inputs and outputs. For each irreversible action, declare a compensating action in advance (e.g. a correction or apology email, or a reversal call) and run it when a later step in a multi-system transaction fails. *When:* Multi-step agent runs that cross system boundaries (ticketing, email, CRM, payments).
- **Retry and fanout guardrails** — Set max turns, max parallel tool calls and a spend budget per run. Use exponential backoff on retries. Wrap downstream calls in circuit breakers so the agent stops calling a dependency that is unhealthy or saturated. *When:* Any agent that calls remote services in a loop, to prevent retry storms, cascading failures and runaway cost.
- **Scoped credentials and tool allowlists** — Issue separate read and write credentials instead of full table access. Maintain an explicit allowlist of tools the agent may call. Keep destructive operations (e.g. deleting production databases) out of reach of the agent. *When:* Before connecting an agent to databases, admin APIs or production systems.
- **Parameter-bound, expiring human approvals** — Record each approval with the action, parameters, actor, timestamp and an expiry. Reject execution if parameters change (for example, an approval for a $30 refund does not authorize $300). *When:* Human-in-the-loop gates on refunds, payments, deletions or outbound communication.
- **Memory as a cached, provenance-tagged store** — Tag each memory item with its source and timestamp. Choose a source of truth for each data type, and invalidate or refresh cached memory when that source changes. Retrieve policies and records from the authoritative store rather than from stale context. *When:* Agents that rely on policy documents, customer records or long-lived memory for decisions that have consequences.
- **Tool contracts with schemas and idempotency** — Define request and response schemas for each tool and make the agent operate only within those contracts. Make operations idempotent, and set rate limits and retry policies so the agent cannot retry aggressively. *When:* When designing the tool surface an agent will use.

## Numbers
- Illustrative approval example: an approval for a $30 refund must not carry over to a $300 refund. No benchmarks, latencies or adoption stats are given. ([15:29](https://youtu.be/hD9-V56FNRI?t=929))

## Hot takes
- A tool timeout should be treated as an unknown outcome, not as a failure, so retries must be idempotent.
- Giving agents broad read-write access by default is the wrong starting point. Start from scoped credentials and tool allowlists.
- Blanket human approvals are not enough. Approvals should be tied to the exact action, parameters, actor and expiry.
- Smarter models reduce mistakes, but they cannot remove network failures, stale data or adversarial input, so architecture still matters.
- Agent context that can influence an action should be treated as state, not as conversation context.

## Tools mentioned
Replit AI agent (cited as a production-database deletion incident; not a tool under review), Air Canada chatbot (cited as an incorrect-refund incident; not a tool under review)

## Relevance to our work
- **agentos** (3/3): 
- **prosharness** (2/3): ProsHarness has checkpoint/resume and phone-driven approvals around Claude Code. The talk's persist-every-step, compensation and parameter-bound approval ideas map to those features. → *Persist each harness step with its inputs and outputs so resume can detect partial side effects, and bind phone approvals to the exact action parameters with an expiry.*
