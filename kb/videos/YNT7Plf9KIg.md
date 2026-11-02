# Your AI Agent Has No Nervous System — Matt Gibiec, Dynatrace

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `YNT7Plf9KIg` · [watch](https://youtu.be/YNT7Plf9KIg) · **date:** 2026-10-09 · **length:** 15:35 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Matt Gibiec · **orgs:** Dynatrace
- **topics:** observability, coding-agents, context-engineering · **tags:** observability, dependency-mapping, production-context, human-in-the-loop, dynatrace, blue-box, sales-pitch

> Vendor pitch for Dynatrace's "Blue Box" agent, which argues AI coding agents need live environment context (service dependencies, production telemetry, change history) to avoid hallucinated or breaking changes.

## Summary
Matt Gibiec, a solutions engineering director at Dynatrace, argues that AI agents act fast but without sight, so they hallucinate or automate the wrong things when they lack context about the environment. He frames context (service dependencies, how users hit applications, what changed in the repo) as the "nervous system" agents need, and says "context is king." He then pitches Blue Box, a Dynatrace agent that sits in the dev lifecycle and gives coding agents production context: dependency mapping, local testing against production data, anomaly detection against historical baselines, change correlation from the code repo, and fix suggestions scoped to the wider system. He describes a human-in-the-loop flow where the platform observes, suggests a fix, and leaves the push decision to the engineer. The talk has no benchmarks, architecture details, or measured results, and the audience poll was used to motivate the product. The session ends with a call to sign up for a preview.

## Key ideas
- **Agents fail without environment context, not because they lack a nervous system.** — The speaker says agents move fast but without sight. Missing context, details, or permissions leads to hallucinations and automations that add no value. Context is what they need, and he calls it the 'connective tissue' for agent processes. ([4:21](https://youtu.be/YNT7Plf9KIg?t=261))
- **Agents need dependency and service maps to judge whether a local change is safe.** — A feature can pass local tests and still break other services after merge. The speaker argues that dependency mapping of every agent and AI workload should feed local testing, so the developer can check the impact on connected services. ([6:40](https://youtu.be/YNT7Plf9KIg?t=400))
- **Use historical baselines to catch deviations early and tell the agent or developer.** — Historical load data defines what normal looks like. When latency or error patterns deviate, the platform can inform the coding agent in the IDE before users are hit. ([9:28](https://youtu.be/YNT7Plf9KIg?t=568))
- **Correlate production anomalies with repo changes to find the cause.** — Connecting the repo means the system knows what changed and who pushed it. That lets an anomaly be tied to a specific merge rather than treated as a general incident. ([10:28](https://youtu.be/YNT7Plf9KIg?t=628))
- **Fixes need dependency context too, since a one-line change can break the rest of the system.** — The speaker says a fix should be checked against the wider environment. He presents context-aware remediation as the goal, not patching only the symptom. ([11:31](https://youtu.be/YNT7Plf9KIg?t=691))
- **Plan before prompting: give the agent research and context before building.** — He criticises teams that start building a feature without first checking what it needs to deliver. He proposes feeding existing application and agent data into planning for a new release or feature. ([12:37](https://youtu.be/YNT7Plf9KIg?t=757))
- **Keep the human in the loop: observe, suggest, and let the engineer decide to ship.** — The flow is observe the environment and build context, detect issues and suggest a context-aware fix, then drive the SDLC while leaving the push decision to a person. ([13:36](https://youtu.be/YNT7Plf9KIg?t=816))

## Techniques
- **Dependency-mapped local testing** — Pull service and dependency maps plus production data into the developer's local test loop, so an agent or developer checks downstream impact before merge. *When:* When changes pass locally but break connected services after merge.
- **Baseline-deviation alerts to the coding agent** — Learn normal latency and error behaviour from historical load, then push deviation alerts into the IDE where the coding agent can act on them. *When:* When you want issues caught before user impact and routed to the owning developer.
- **Change-correlated incident triage** — Join runtime anomalies with repo change history (commit, author, merge) to identify which change caused the issue. *When:* When an anomaly needs a cause, not just a symptom.
- **Context-scoped fix suggestion with human approval** — Generate a fix using the application, dependency, and agent context, then surface it for a human to push or reject. *When:* When agents may remediate production-adjacent code and a person must keep control.

## Hot takes
- The speaker says agents don't need a nervous system, only environment context. The title is a deliberate twist.

## Tools mentioned
Dynatrace Blue Box

## Relevance to our work
- **agentos** (1/3): Observability (L4) and dependency-aware context for agents overlap with AgentOS's trace and telemetry pillars, but the talk is product marketing with no design detail. → *Note the dependency-map plus change-correlation idea as a possible input for SkillForge's skill-worthiness signal; no build change needed yet.*
- **prosharness** (1/3): The observe, suggest, and human-decides flow resembles ProsHarness's phone-driven approvals, but the talk says nothing about checkpointing, resume, or approvals. → *None beyond a glance at how approval gates are framed; no change needed.*
