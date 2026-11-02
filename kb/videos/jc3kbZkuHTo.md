# The Human Is an Async API — Melanie Warrick, Temporal

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `jc3kbZkuHTo` · [watch](https://youtu.be/jc3kbZkuHTo) · **date:** 2026-10-05 · **length:** 19:16 · **format:** demo · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Melanie Warrick · **orgs:** Temporal, Google, LangChain
- **topics:** agent-architecture, multi-agent, governance-compliance · **tags:** durable-execution, human-in-the-loop, temporal, wait-condition, signal, langgraph, google-adk, workflows, activities, replay, approvals

> Melanie Warrick (Temporal) shows durable execution for multi-agent systems: a human approval is a wait condition plus a signal on a parked workflow, so the rest of the system keeps running and survives restarts. It is a vendor-led talk with a live ice-cream delivery demo.

## Summary
Melanie Warrick from Temporal demos a delivery system with fleet, customer and dispatch agents built on Google ADK and LangGraph, with Temporal providing durable state. She argues that a human approval should not be a blocking function call. Instead, the workflow pauses on a wait condition and resumes when an external signal delivers the human's answer, so only that one order is paused. In the live demo she kills the worker, sends an approval while it is offline, and restarts it, and the event log replays to the current step rather than re-running earlier work. She explains the three primitives (worker, workflow, activity) and says model and tool calls go in activities, while steps in the loop go in deterministic workflows. For deciding when a human should be in the loop, she advises weighing the cost of being wrong against alert fatigue. The talk is partly a Temporal pitch, but the wait-plus-signal pattern and the replay demo are concrete.

## Key ideas
- **Treat the human as an async API, not a blocking call** — A function that waits for a human can block or be lost if the service goes down. The speaker's fix is to pause only that one workflow with a wait condition and let an external signal deliver the human's answer, while other workflows keep running. ([7:10](https://youtu.be/jc3kbZkuHTo?t=430))
- **Approval state survives crashes through event-log replay** — In the demo the worker is killed, an approval is sent while it is offline, and the worker is restarted. The event log is replayed up to the paused point, not re-executed, and the queued approval is applied so the order is assigned and delivered. ([15:35](https://youtu.be/jc3kbZkuHTo?t=935))
- **Split the system into worker, workflow and activity** — The worker runs the code. The workflow holds the step-by-step state and must be deterministic. Model calls and tool calls, which touch external systems, go in activities, which may be non-deterministic. ([10:03](https://youtu.be/jc3kbZkuHTo?t=603))
- **Wrap framework components instead of rewriting the agent** — For Google ADK, the model is wrapped in a Temporal model class and tools are wrapped as activities, and the worker is given the ADK plugin. For LangGraph, nodes call LangGraph's interrupt, and the loop waits on a signal for the answer. ([10:03](https://youtu.be/jc3kbZkuHTo?t=603))
- **One child workflow per entity limits the blast radius of a pause** — Each order gets its own child workflow per framework. A high-value order that needs approval pauses only its own child, so the other orders keep being assessed and filled. ([12:43](https://youtu.be/jc3kbZkuHTo?t=763))
- **Decide human-in-the-loop by the cost of being wrong** — The speaker says this is a case-by-case call. The main factor is the cost of an error, and especially the security impact, balanced against alert fatigue from users who click yes on everything. ([16:54](https://youtu.be/jc3kbZkuHTo?t=1014))
- **Use timeouts on waits** — A wait condition can carry a timeout so a workflow does not wait forever for a human who never answers. ([8:34](https://youtu.be/jc3kbZkuHTo?t=514))

## Techniques
- **Human approval as wait condition plus signal** — Pause the workflow at the approval point with a wait condition, store that state in the durable layer, and resume when an external signal carries the human's decision. Add a timeout for how long the wait lasts. *When:* Any multi-step agent run where a human decision may take minutes, days or weeks, and the run must survive restarts.
- **Wrap every model and tool call as an activity** — Keep the agent loop and step sequence in a deterministic workflow, and run every model call and external tool call as an activity so their results are recorded and not re-run on replay. *When:* When an agent loop must resume after a crash without repeating side effects.
- **LangGraph interrupt bridged to a durable wait** — Inside a graph node, call interrupt to ask the question. In the workflow, wait on the interrupt-signal and resume the graph with the human's response. *When:* LangGraph-based agents that need a human answer in the middle of a graph.
- **Child workflow per entity** — Start one child workflow per order or item, so a paused item stops only its own child while siblings keep running. *When:* Batch or multi-entity agent systems where one item needing review should not stall the rest.
- **Cost-of-being-wrong gate for human review** — Score each action by the cost of an error, especially security impact, and route only high-cost actions to a human to limit alert fatigue. *When:* Deciding which agent actions need approval before they run.

## Numbers
- Claims a single system can keep millions of workflows parked waiting on humans (no benchmark given). ([8:34](https://youtu.be/jc3kbZkuHTo?t=514))
- Approval queued while the worker was offline was applied after restart, and the order was delivered (single demo run, no latency figures). ([15:35](https://youtu.be/jc3kbZkuHTo?t=935))

## Hot takes
- A human approval should be a signal to a parked workflow, not a blocking function call.
- Human-in-the-loop should be decided by the cost of being wrong, not by default, because alert fatigue makes constant yes-clicking the outcome.

## Tools mentioned
Temporal, Google ADK, LangGraph, Google Maps API, Google Search, Python, TypeScript, Rust

## Relevance to our work
- **prosharness** (2/3): ProsHarness already has checkpoint/resume and phone-driven approvals; this talk gives a concrete wait-plus-signal model for them. → *Store each pending approval as a persisted checkpoint state that resumes on a phone-approval signal, with a timeout that falls back to a safe default.*
- **agentos** (1/3): Durable wait-plus-signal is relevant to a gated pause, but AgentOS has no human approval flow yet. → *Read Temporal's wait-condition and signal docs before designing any human-approval pause in the Crucible exec-gate, rather than writing a blocking call.*
- **general** (1/3): Any multi-step agent run that waits for a human benefits from the pause-and-resume pattern, though the talk is partly a Temporal pitch. → *Note the cost-of-being-wrong rule for choosing which agent actions need a human.*
